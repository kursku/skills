# API Design & Service Resilience Reference

## Pagination

### Cursor-Based (Recommended for Scale)
```typescript
// Constant performance regardless of page depth
app.get('/posts', async (req, res) => {
  const limit = Math.min(parseInt(req.query.limit) || 20, 100); // Max 100
  const cursor = req.query.cursor;

  const posts = await prisma.post.findMany({
    take: limit + 1, // Fetch 1 extra to detect hasMore
    ...(cursor && { cursor: { id: cursor }, skip: 1 }),
    orderBy: { id: 'asc' }
  });

  const hasMore = posts.length > limit;
  const data = hasMore ? posts.slice(0, -1) : posts;

  res.json({
    data,
    pagination: {
      hasMore,
      nextCursor: hasMore ? data[data.length - 1].id : null
    }
  });
});
```

### Offset-Based (Simple, Limited Scale)
```typescript
// Performance degrades at high offsets (DB scans offset + limit rows)
app.get('/posts', async (req, res) => {
  const page = Math.max(parseInt(req.query.page) || 1, 1);
  const limit = Math.min(parseInt(req.query.limit) || 20, 100);
  const offset = (page - 1) * limit;

  // DANGER: offset=100000 scans 100K rows to skip them
  if (offset > 10000) return res.status(400).json({ error: 'Use cursor pagination for deep pages' });

  const [data, total] = await Promise.all([
    prisma.post.findMany({ skip: offset, take: limit, orderBy: { id: 'asc' } }),
    prisma.post.count()
  ]);

  res.json({ data, pagination: { page, limit, total, totalPages: Math.ceil(total / limit) } });
});
```

**Rule:** Use cursor for APIs consumed by infinite scroll or programmatic clients. Use offset only for admin UIs where page numbers matter and data is small.

---

## Rate Limiting

### Tiered Rate Limiting
```typescript
import rateLimit from 'express-rate-limit';

// Global: 100 req/15min per IP
app.use('/api/', rateLimit({
  windowMs: 15 * 60 * 1000,
  max: 100,
  standardHeaders: true,
  legacyHeaders: false
}));

// Auth: 5 attempts/15min (strict)
app.use('/auth/', rateLimit({
  windowMs: 15 * 60 * 1000,
  max: 5,
  skipSuccessfulRequests: true
}));

// Per-tier limiting
app.use('/api/v1/', rateLimit({
  windowMs: 60 * 1000,
  max: (req) => {
    if (req.user?.tier === 'enterprise') return 5000;
    if (req.user?.tier === 'pro') return 1000;
    return 100;
  }
}));
```

### Response Headers
```
X-RateLimit-Limit: 100
X-RateLimit-Remaining: 42
X-RateLimit-Reset: 1700000000
Retry-After: 30
```

---

## Circuit Breaker

### Implementation (Opossum)
```typescript
import CircuitBreaker from 'opossum';

const paymentBreaker = new CircuitBreaker(
  async (userId: string, amount: number) => {
    return await paymentService.charge(userId, amount);
  },
  {
    timeout: 3000,                  // 3s timeout per call
    errorThresholdPercentage: 50,   // Open at 50% failure
    resetTimeout: 30000,            // Try again after 30s
    volumeThreshold: 10             // Min requests before calculating %
  }
);

// Fallback when circuit is open
paymentBreaker.fallback(() => ({ status: 'degraded', message: 'Payments temporarily unavailable' }));

// Use it
const result = await paymentBreaker.fire(userId, 99.99);

// Monitor
paymentBreaker.on('open', () => logger.error('Payment circuit OPEN'));
paymentBreaker.on('halfOpen', () => logger.warn('Payment circuit testing...'));
paymentBreaker.on('close', () => logger.info('Payment circuit recovered'));
```

### Circuit Breaker States
```
CLOSED ──(failures > threshold)──→ OPEN ──(resetTimeout)──→ HALF-OPEN
  ↑                                                             │
  └──────────(success)──────────────────────────────────────────┘
  └──────────────────────────────────(failure)──→ OPEN
```

### Configuration Guidelines
- `timeout`: Set to p99 latency + 20% buffer
- `errorThresholdPercentage`: 50% for aggressive, 25% for conservative
- `resetTimeout`: 30-60s (match service recovery time)
- `volumeThreshold`: 10-20 (avoid opening on 1 failure)

---

## Graceful Shutdown

```typescript
const server = http.createServer(app);
let shuttingDown = false;

process.on('SIGTERM', async () => {
  console.log('SIGTERM received, draining...');
  shuttingDown = true;

  // 1. Stop accepting new connections
  server.close(async () => {
    // 2. Close DB, cache, queue connections
    await Promise.allSettled([
      prisma.$disconnect(),
      redis.quit(),
      worker.close()
    ]);
    process.exit(0);
  });

  // 3. Force exit after 30s if still draining
  setTimeout(() => {
    console.error('Forced shutdown after timeout');
    process.exit(1);
  }, 30000);
});

// Reject new requests during shutdown
app.use((req, res, next) => {
  if (shuttingDown) return res.status(503).json({ error: 'Shutting down' });
  next();
});
```

---

## Load Balancing

### Strategy Selection

| Strategy | Use When |
|----------|----------|
| **Round Robin** | All instances are equal, stateless |
| **Least Connections** | Instances have varying capacity |
| **Consistent Hashing** | Need session affinity or cache locality |
| **Weighted** | Mixed instance sizes |

### Health Checks (Kubernetes)
```yaml
# Startup: Is the app initialized?
startupProbe:
  httpGet: { path: /startup, port: 8080 }
  periodSeconds: 10
  failureThreshold: 30    # 5 min max startup

# Readiness: Can it handle traffic?
readinessProbe:
  httpGet: { path: /ready, port: 8080 }
  periodSeconds: 10
  failureThreshold: 3     # Remove after 3 failures

# Liveness: Is it alive? (restart if not)
livenessProbe:
  httpGet: { path: /health, port: 8080 }
  periodSeconds: 20
  failureThreshold: 3
```

```typescript
app.get('/ready', async (req, res) => {
  const dbOk = await prisma.$queryRaw`SELECT 1`.then(() => true).catch(() => false);
  const redisOk = await redis.ping().then(() => true).catch(() => false);
  const ready = dbOk && redisOk && !shuttingDown;
  res.status(ready ? 200 : 503).json({ ready, db: dbOk, redis: redisOk });
});

app.get('/health', (req, res) => res.json({ alive: true }));
```

---

## Stateless Design

### Session Externalization
```typescript
// WRONG: In-memory sessions (breaks with multiple instances)
const sessions = new Map();

// CORRECT: Redis-backed sessions
import session from 'express-session';
import RedisStore from 'connect-redis';

app.use(session({
  store: new RedisStore({ client: redis }),
  secret: process.env.SESSION_SECRET,
  resave: false,
  saveUninitialized: false,
  cookie: { secure: true, httpOnly: true, maxAge: 3600000 }
}));
```

### Stateless Auth (JWT)
```typescript
// No server-side state needed — token carries identity
const token = jwt.sign({ sub: userId, role: 'user' }, secret, { expiresIn: '15m' });

// Any instance can verify without shared state
const user = jwt.verify(token, secret);
```

**JWT vs Redis Sessions:**
| Factor | JWT | Redis Sessions |
|--------|-----|----------------|
| Revocation | Hard (wait for expiry) | Instant (delete key) |
| Scalability | Excellent (no state) | Good (Redis cluster) |
| Token size | Large (payload in token) | Small (session ID only) |
| Server load | None | Redis lookup per request |

**Rule:** Use JWT for stateless APIs and microservices. Use Redis sessions when you need instant revocation (admin panels, security-sensitive apps).

---

## API Response Optimization

### Compression
```typescript
import compression from 'compression';
app.use(compression({ threshold: 1024, level: 6 })); // Compress responses > 1KB
```

### Field Selection
```typescript
// Let clients request only fields they need
app.get('/users/:id', async (req, res) => {
  const fields = req.query.fields?.split(',') || ['id', 'name', 'email'];
  const allowed = ['id', 'name', 'email', 'avatar', 'role'];
  const select = Object.fromEntries(
    fields.filter(f => allowed.includes(f)).map(f => [f, true])
  );
  const user = await prisma.user.findUnique({ where: { id: req.params.id }, select });
  res.json({ data: user });
});
```

### Batch Endpoints
```typescript
// Instead of N individual requests, batch them
app.post('/users/batch', async (req, res) => {
  const ids = req.body.ids;
  if (!Array.isArray(ids) || ids.length > 100) {
    return res.status(400).json({ error: 'Max 100 IDs per batch' });
  }
  const users = await prisma.user.findMany({ where: { id: { in: ids } } });
  res.json({ data: users });
});
```
