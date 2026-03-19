# Infrastructure Scaling Reference

## Kubernetes Autoscaling (HPA)

### Configuration
```yaml
apiVersion: autoscaling/v2
kind: HorizontalPodAutoscaler
metadata:
  name: api-hpa
spec:
  scaleTargetRef:
    apiVersion: apps/v1
    kind: Deployment
    name: api
  minReplicas: 2            # Always 2+ for HA (never 1 in production)
  maxReplicas: 20
  metrics:
  - type: Resource
    resource:
      name: cpu
      target:
        type: Utilization
        averageUtilization: 70    # Scale up at 70% CPU
  behavior:
    scaleUp:
      stabilizationWindowSeconds: 0     # Scale up immediately
      policies:
      - type: Percent
        value: 100                       # Can double capacity
        periodSeconds: 15
    scaleDown:
      stabilizationWindowSeconds: 300   # Wait 5min before scaling down
      policies:
      - type: Percent
        value: 50                        # Max 50% reduction per cycle
        periodSeconds: 60
```

### Resource Requests & Limits
```yaml
resources:
  requests:                    # What HPA bases utilization on
    cpu: 250m                  # Reserve 250 milliCPU
    memory: 512Mi
  limits:
    cpu: 500m                  # Hard cap
    memory: 1Gi
```

**Rules:**
- HPA measures % of **request**, not limit
- If request=250m, actual=175m → utilization=70% → triggers scale
- `minReplicas: 2+` in production (single pod = downtime during restart)
- Target utilization 50-70% gives spike headroom

### Custom Metrics Scaling
```yaml
# Scale on queue depth instead of CPU
metrics:
- type: External
  external:
    metric:
      name: queue_depth
      selector:
        matchLabels:
          queue: email-processing
    target:
      type: AverageValue
      averageValue: "100"     # 1 pod per 100 queued messages
```

---

## Serverless Patterns

### Cold Start Optimization
```typescript
// Lazy-load heavy dependencies
let dbClient: PrismaClient | null = null;

export const handler = async (event: any) => {
  // Initialize only on first invocation (reused across warm invocations)
  if (!dbClient) {
    const { PrismaClient } = await import('@prisma/client');
    dbClient = new PrismaClient();
  }

  return dbClient.user.findMany();
};
```

**Cold start costs by memory:**
| Memory | Cold Start | Cost/invocation |
|--------|-----------|----------------|
| 256MB | ~400ms | $0.0000004 |
| 512MB | ~280ms | $0.0000008 |
| 1024MB | ~150ms | $0.0000017 |

**Rule:** Allocate 1.5x typical memory usage — faster execution + faster cold starts.

### Provisioned Concurrency
- Cost: ~$0.015/unit/hour ($10.80/month per unit)
- Use only when: Cold start latency violates SLA
- Alternative: Keep a minimum of warm instances via scheduled pings

---

## CDN Caching

### Cache-Control Headers
```typescript
// Static assets (versioned URLs — cache forever)
res.set('Cache-Control', 'public, max-age=31536000, immutable');

// API responses (cache at edge, short client cache)
res.set('Cache-Control', 'public, max-age=0, s-maxage=3600, stale-while-revalidate=60');

// Private/authenticated content
res.set('Cache-Control', 'private, max-age=300');

// Never cache
res.set('Cache-Control', 'no-store');
```

### Header Reference

| Header | Meaning |
|--------|---------|
| `max-age=N` | Browser caches for N seconds |
| `s-maxage=N` | CDN caches for N seconds (overrides max-age at edge) |
| `immutable` | Never revalidate (use with hashed filenames) |
| `stale-while-revalidate=N` | Serve stale for N seconds while refreshing in background |
| `private` | Only browser caches (not CDN) — use for user-specific data |
| `no-store` | Never cache anywhere |

### Cache Busting via Content Hashing
```javascript
// Webpack/Vite: Auto-hash filenames
output: { filename: '[name].[contenthash].js' }

// Result: app.a3f9d2c1.js → new hash on every change
// Combine with: Cache-Control: public, max-age=31536000, immutable
// No purging needed — new URL = new request
```

---

## Deployments

### Blue-Green (Zero Downtime, Instant Rollback)
```
1. Deploy v2 alongside v1 (both running)
2. Test v2 thoroughly
3. Switch load balancer: v1 → v2
4. Keep v1 for 1 hour (instant rollback)
5. Decommission v1
```
**Tradeoff:** Requires 2x resources during deployment.

### Canary (Gradual, Lower Risk)
```
1. Deploy v2 to 1 pod (5% traffic)
2. Monitor errors + latency for 5min
3. If healthy: ramp to 25% → 50% → 100%
4. If unhealthy: auto-rollback to v1
```
```yaml
# Flagger canary config
analysis:
  interval: 1m
  threshold: 5
  maxWeight: 50
  stepWeight: 10          # +10% per minute
  metrics:
  - name: request-success-rate
    thresholdRange: { min: 99 }   # Require 99%+ success
  - name: request-duration
    thresholdRange: { max: 500 }  # p99 < 500ms
```

### Database Migrations in Deployments
```sql
-- SAFE: Backward compatible (both versions work)
ALTER TABLE users ADD COLUMN new_field TEXT DEFAULT '';

-- UNSAFE: Breaks old version
ALTER TABLE users DROP COLUMN old_field;
ALTER TABLE users RENAME COLUMN name TO full_name;
```

**Rule:** Always deploy in 3 phases:
1. Add new column (backward compatible)
2. Deploy new code that uses new column
3. Remove old column (after old code is gone)

---

## Observability

### The Four Golden Signals
| Signal | What to Measure | Alert When |
|--------|----------------|------------|
| **Latency** | p50, p95, p99 response time | p99 > 500ms |
| **Traffic** | Requests per second | Unusual spike or drop |
| **Errors** | Error rate (5xx / total) | > 1% error rate |
| **Saturation** | CPU, memory, DB connections, queue depth | > 80% utilization |

### Structured Logging
```typescript
import pino from 'pino';
const logger = pino({ level: 'info' });

// GOOD: Structured, searchable
logger.info({ userId: '123', action: 'login', duration: 45 }, 'User logged in');
// Output: {"level":30,"userId":"123","action":"login","duration":45,"msg":"User logged in"}

// BAD: Unstructured
console.log(`User 123 logged in in 45ms`);
```

### Request Tracing
```typescript
import { v4 as uuid } from 'uuid';

// Middleware: Add trace ID to every request
app.use((req, res, next) => {
  req.traceId = req.headers['x-trace-id'] || uuid();
  res.setHeader('x-trace-id', req.traceId);
  next();
});

// Include in all logs
logger.info({ traceId: req.traceId, path: req.path }, 'Request started');

// Pass to downstream services
const response = await fetch('https://service-b.internal/api', {
  headers: { 'x-trace-id': req.traceId }
});
```

### Key Metrics to Track

```typescript
import { Counter, Histogram, Gauge } from 'prom-client';

// Request duration (histogram for percentiles)
const httpDuration = new Histogram({
  name: 'http_request_duration_seconds',
  help: 'HTTP request duration',
  labelNames: ['method', 'route', 'status'],
  buckets: [0.01, 0.05, 0.1, 0.25, 0.5, 1, 2.5, 5]
});

// Error counter
const httpErrors = new Counter({
  name: 'http_errors_total',
  help: 'HTTP errors',
  labelNames: ['method', 'route', 'status']
});

// Active connections gauge
const dbConnections = new Gauge({
  name: 'db_active_connections',
  help: 'Active database connections'
});

// Middleware
app.use((req, res, next) => {
  const end = httpDuration.startTimer({ method: req.method, route: req.route?.path });
  res.on('finish', () => {
    end({ status: res.statusCode });
    if (res.statusCode >= 500) {
      httpErrors.inc({ method: req.method, route: req.route?.path, status: res.statusCode });
    }
  });
  next();
});
```

---

## Concurrency Patterns

### Worker Threads (CPU-bound work)
```typescript
import { Worker, isMainThread, parentPort } from 'worker_threads';

if (isMainThread) {
  // Main thread: Offload CPU-heavy work
  async function processImage(buffer: Buffer): Promise<Buffer> {
    return new Promise((resolve, reject) => {
      const worker = new Worker(__filename, { workerData: { buffer } });
      worker.on('message', resolve);
      worker.on('error', reject);
    });
  }
} else {
  // Worker thread: Do the heavy lifting
  const { workerData } = require('worker_threads');
  const result = heavyImageProcessing(workerData.buffer);
  parentPort?.postMessage(result);
}
```

### Cluster Mode (Multi-process)
```typescript
import cluster from 'cluster';
import os from 'os';

if (cluster.isPrimary) {
  const numWorkers = os.cpus().length;
  for (let i = 0; i < numWorkers; i++) cluster.fork();

  cluster.on('exit', (worker) => {
    console.error(`Worker ${worker.process.pid} died, replacing...`);
    cluster.fork();
  });
} else {
  // Each worker runs the HTTP server
  app.listen(3000);
}
```

### Backpressure (Prevent Overload)
```typescript
// Stream processing with backpressure
import { Transform } from 'stream';

const processor = new Transform({
  highWaterMark: 1000, // Buffer max 1000 chunks
  transform(chunk, encoding, callback) {
    processChunk(chunk)
      .then(result => callback(null, result))
      .catch(err => callback(err));
  }
});

// Pipeline automatically handles backpressure
inputStream.pipe(processor).pipe(outputStream);
```

### Semaphore (Limit Concurrent Operations)
```typescript
class Semaphore {
  private queue: (() => void)[] = [];
  private running = 0;

  constructor(private max: number) {}

  async acquire(): Promise<void> {
    if (this.running < this.max) { this.running++; return; }
    return new Promise(resolve => this.queue.push(resolve));
  }

  release(): void {
    this.running--;
    const next = this.queue.shift();
    if (next) { this.running++; next(); }
  }
}

// Limit to 10 concurrent DB operations
const sem = new Semaphore(10);
async function queryWithLimit(sql: string) {
  await sem.acquire();
  try { return await db.query(sql); }
  finally { sem.release(); }
}
```

---

## Load Testing

### Before Optimizing, Profile
```bash
# Quick load test with k6
k6 run --vus 50 --duration 30s script.js

# Artillery (Node.js)
npx artillery quick --count 50 --num 100 http://localhost:3000/api/users
```

### What to Measure During Load Tests

| Metric | Tool | Warning Sign |
|--------|------|-------------|
| p99 latency | k6, Artillery | > 500ms |
| Throughput | k6 | Plateaus while CPU < 100% (IO bottleneck) |
| Error rate | k6 | > 0 (should be zero under expected load) |
| DB connections | pg_stat_activity | Near max_connections |
| Memory | top/htop | Continuously growing (leak) |
| CPU per process | top | Single core at 100% (need cluster mode) |

**Rule:** Test at 2x expected peak traffic. If it survives, you have margin.
