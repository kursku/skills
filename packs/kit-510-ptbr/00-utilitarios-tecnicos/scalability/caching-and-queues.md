# Caching & Async Processing Reference

## Caching Strategies

### Cache-Aside (Lazy Loading) — Most Common
```typescript
async function getUser(id: string) {
  // 1. Check cache
  const cached = await redis.get(`user:${id}`);
  if (cached) return JSON.parse(cached);

  // 2. Cache miss → fetch from DB
  const user = await db.user.findUnique({ where: { id } });
  if (!user) return null;

  // 3. Populate cache with TTL
  await redis.setex(`user:${id}`, 300, JSON.stringify(user)); // 5min
  return user;
}
```
**Best for:** Read-heavy workloads, data that tolerates brief staleness.

### Write-Through (Immediate Consistency)
```typescript
async function updateUser(id: string, data: Partial<User>) {
  // 1. Write to DB
  const user = await db.user.update({ where: { id }, data });

  // 2. Immediately update cache
  await redis.setex(`user:${id}`, 300, JSON.stringify(user));

  return user;
}
```
**Best for:** Data that must be consistent between cache and DB.

### Write-Behind (Async Write)
```typescript
async function updateUserFast(id: string, data: Partial<User>) {
  // 1. Write to cache (fast)
  await redis.setex(`user:${id}`, 300, JSON.stringify({ ...existing, ...data }));

  // 2. Queue DB write (async)
  await queue.add('sync-user-to-db', { id, data });

  return { ...existing, ...data };
}
```
**Best for:** High-write throughput where brief inconsistency is acceptable.

### Cache Invalidation Patterns

| Pattern | How | When |
|---------|-----|------|
| **TTL expiry** | `setex(key, 300, value)` | Default — simple, predictable |
| **Explicit delete** | `del(key)` on write | When you need instant consistency |
| **Tag-based** | Group keys, purge by tag | Related entities (user + user's orders) |
| **Versioned keys** | `user:${id}:v${version}` | Avoid stale reads entirely |

### TTL Guidelines

| Data Type | TTL | Rationale |
|-----------|-----|-----------|
| User session | 1 hour | Security + memory |
| User profile | 5-15 min | Changes infrequently |
| Product catalog | 1-24 hours | Updates are batched |
| Config/feature flags | 30-60 sec | Needs fast propagation |
| Static assets (CDN) | 1 year | Versioned URLs |
| API responses | 1-60 min | Depends on freshness need |

---

## Redis Patterns

### Rate Limiting (Sliding Window)
```typescript
async function rateLimit(userId: string, limit = 100, windowSec = 60) {
  const now = Date.now() / 1000;
  const window = Math.floor(now / windowSec);
  const key = `rate:${userId}:${window}`;
  const prevKey = `rate:${userId}:${window - 1}`;

  const [curr, prev] = await Promise.all([redis.get(key), redis.get(prevKey)]);
  const elapsed = (now % windowSec) / windowSec;
  const estimate = (parseInt(prev || '0') * (1 - elapsed)) + parseInt(curr || '0');

  if (estimate >= limit) return { allowed: false, retryAfter: Math.ceil(windowSec * (1 - elapsed)) };

  const count = await redis.incr(key);
  if (count === 1) await redis.expire(key, windowSec * 2);
  return { allowed: true, remaining: Math.max(0, limit - Math.ceil(estimate) - 1) };
}
```

### Distributed Lock (Redlock)
```typescript
async function withLock<T>(resource: string, ttlMs: number, fn: () => Promise<T>): Promise<T> {
  const lockValue = crypto.randomBytes(16).toString('hex');
  const acquired = await redis.set(`lock:${resource}`, lockValue, 'NX', 'PX', ttlMs);

  if (acquired !== 'OK') throw new Error('Could not acquire lock');

  try {
    return await fn();
  } finally {
    // Release only if we still own it (Lua for atomicity)
    await redis.eval(
      `if redis.call("get",KEYS[1]) == ARGV[1] then return redis.call("del",KEYS[1]) else return 0 end`,
      1, `lock:${resource}`, lockValue
    );
  }
}

// Usage: prevent duplicate processing
await withLock(`process:order:${orderId}`, 30000, async () => {
  await processOrder(orderId);
});
```

### Session Storage
```typescript
async function createSession(userId: string): Promise<string> {
  const sessionId = crypto.randomUUID();
  await redis.setex(`session:${sessionId}`, 3600, JSON.stringify({
    userId, createdAt: Date.now()
  }));
  return sessionId;
}

async function getSession(sessionId: string) {
  const data = await redis.get(`session:${sessionId}`);
  if (!data) return null;
  // Extend TTL on access (sliding expiration)
  await redis.expire(`session:${sessionId}`, 3600);
  return JSON.parse(data);
}
```

### Sorted Set (Leaderboards / Rankings)
```typescript
// Add score
await redis.zadd('leaderboard', score, `user:${userId}`);

// Top 10
const top10 = await redis.zrevrange('leaderboard', 0, 9, 'WITHSCORES');

// User's rank
const rank = await redis.zrevrank('leaderboard', `user:${userId}`);
```

---

## Message Queues

### When to Use a Queue

| Scenario | Queue? | Why |
|----------|--------|-----|
| Email sending | Yes | Slow, can fail, user doesn't wait |
| Image processing | Yes | CPU-heavy, decouple from request |
| Payment processing | Maybe | Depends on UX (sync for checkout) |
| Webhook delivery | Yes | External service may be down |
| Report generation | Yes | Long-running, deliver async |
| Real-time chat | No | Use WebSockets/SSE instead |
| Simple CRUD | No | Adds unnecessary complexity |

### BullMQ (Node.js + Redis)
```typescript
import { Queue, Worker } from 'bullmq';

// Producer
const emailQueue = new Queue('email', { connection: { host: 'redis' } });

await emailQueue.add('welcome', { to: 'user@example.com', name: 'John' }, {
  attempts: 3,
  backoff: { type: 'exponential', delay: 1000 },
  removeOnComplete: 1000,
  removeOnFail: 5000
});

// Consumer
const worker = new Worker('email', async (job) => {
  await sendEmail(job.data.to, job.data.name);
}, {
  connection: { host: 'redis' },
  concurrency: 5,
  limiter: { max: 10, duration: 1000 } // 10 per second
});

worker.on('completed', (job) => console.log(`Done: ${job.id}`));
worker.on('failed', (job, err) => console.error(`Failed: ${job?.id}`, err));
```

### Queue-Based Load Leveling
```
Spike: 10,000 req/s ─→ Queue (buffer) ─→ Workers process at 1,000/s
                                          (auto-scale based on queue depth)
```

```typescript
// Producer: Enqueue immediately, respond fast
app.post('/process', async (req, res) => {
  const job = await queue.add('process', req.body);
  res.json({ jobId: job.id, status: 'queued' });
});

// Consumer: Process at sustainable rate
const worker = new Worker('process', async (job) => {
  await heavyProcessing(job.data);
}, { concurrency: 10 });
```

---

## Event-Driven Architecture

### Pub/Sub Pattern
```typescript
// Publisher (doesn't know who listens)
await redis.publish('order:created', JSON.stringify({ orderId, userId, total }));

// Subscriber 1: Send confirmation email
redis.subscribe('order:created', (message) => {
  const order = JSON.parse(message);
  emailQueue.add('order-confirmation', order);
});

// Subscriber 2: Update analytics
redis.subscribe('order:created', (message) => {
  const order = JSON.parse(message);
  analyticsQueue.add('track-purchase', order);
});

// Subscriber 3: Notify warehouse
redis.subscribe('order:created', (message) => {
  const order = JSON.parse(message);
  warehouseQueue.add('prepare-shipment', order);
});
```

### CQRS (Command Query Responsibility Segregation)
```
Write path: API → Command Handler → Write DB (normalized)
                                  → Publish event
Read path:  API → Query Handler → Read DB/Cache (denormalized, optimized for reads)
                                  ← Event → Update read model
```

```typescript
// Write side: Normalize, validate, enforce business rules
async function createOrder(cmd: CreateOrderCommand) {
  const order = await writeDb.orders.create({ data: cmd });
  await eventBus.publish('order.created', order);
  return order.id;
}

// Read side: Denormalized, fast, optimized for specific queries
eventBus.subscribe('order.created', async (event) => {
  await readDb.orderViews.upsert({
    where: { orderId: event.id },
    create: {
      orderId: event.id,
      customerName: event.customerName, // Denormalized!
      total: event.total,
      itemCount: event.items.length
    }
  });
});

// Query the read model (no joins needed)
async function getOrderDashboard(customerId: string) {
  return readDb.orderViews.findMany({ where: { customerId } });
}
```

**When CQRS is worth it:**
- Read and write patterns are very different
- Read:write ratio > 10:1
- Need different scaling strategies for reads vs writes
- Complex read queries that would require expensive joins

**When CQRS is overkill:**
- Simple CRUD applications
- Low traffic (< 1000 req/s)
- Read and write models are nearly identical
