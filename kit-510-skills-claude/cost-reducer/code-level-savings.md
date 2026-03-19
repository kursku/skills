# Code-Level Cost Savings Reference

## Bundle Size Optimization

### Impact on Cost
- Vercel: $0.15/GB after 1TB included
- 1M users × 3MB page = 3TB = **$300/month in bandwidth**
- 35% bundle reduction → **$105/month saved**

### Tree-Shaking
```javascript
// BAD: Imports entire library (can't tree-shake)
import * as lodash from 'lodash';       // 70KB+
import { everything } from 'aws-sdk';    // 50MB+

// GOOD: Named imports (tree-shakeable)
import { debounce } from 'lodash-es';    // 1KB
import { S3Client } from '@aws-sdk/client-s3'; // 30KB
```

### Dynamic Imports (Code Splitting)
```typescript
// BAD: Heavy component loaded on every page
import HeavyChart from './HeavyChart';

// GOOD: Loaded only when needed
const HeavyChart = lazy(() => import('./HeavyChart'));

// Next.js dynamic import
const AdminPanel = dynamic(() => import('./AdminPanel'), {
  loading: () => <Skeleton />,
  ssr: false  // Skip server rendering for client-only components
});
```

### Bundle Analysis
```bash
# Analyze what's in your bundle
npx webpack-bundle-analyzer dist/stats.json

# Next.js built-in
ANALYZE=true next build

# Vite
npx vite-bundle-visualizer
```

**Common bloat sources:**
| Library | Typical Size | Lightweight Alternative |
|---------|-------------|----------------------|
| moment.js | 70KB | date-fns (tree-shakeable) or dayjs (2KB) |
| lodash | 70KB | lodash-es (tree-shakeable) or native JS |
| aws-sdk v2 | 50MB+ | @aws-sdk/client-* v3 (modular) |
| chart.js | 200KB | Load dynamically, only on chart pages |

---

## Image Optimization Pipeline

### Format Savings
| Format | vs JPEG | Browser Support |
|--------|---------|----------------|
| WebP | 25-35% smaller | 97% |
| AVIF | 50% smaller | 93% |

### Server-Side Pipeline (Sharp)
```typescript
import sharp from 'sharp';

async function optimizeForWeb(input: Buffer, filename: string) {
  const sizes = [640, 1280, 1920];
  const results = [];

  for (const width of sizes) {
    // WebP (primary)
    await sharp(input).resize(width).webp({ quality: 85 })
      .toFile(`public/img/${filename}-${width}w.webp`);

    // AVIF (modern browsers)
    await sharp(input).resize(width).avif({ quality: 75 })
      .toFile(`public/img/${filename}-${width}w.avif`);

    // JPEG fallback
    await sharp(input).resize(width).jpeg({ quality: 80, mozjpeg: true })
      .toFile(`public/img/${filename}-${width}w.jpg`);
  }
}
```

### Responsive HTML
```html
<picture>
  <source srcset="/img/hero-640w.avif 640w, /img/hero-1280w.avif 1280w" type="image/avif" />
  <source srcset="/img/hero-640w.webp 640w, /img/hero-1280w.webp 1280w" type="image/webp" />
  <img src="/img/hero-1280w.jpg" alt="Hero" loading="lazy" decoding="async" />
</picture>
```

### Next.js Image (Automatic Optimization)
```javascript
// next.config.js
module.exports = {
  images: {
    formats: ['image/avif', 'image/webp'],
    minimumCacheTTL: 86400 * 365,  // Cache 1 year
    deviceSizes: [640, 828, 1200, 1920],
  }
};
```

**Cost impact:** 1M image requests/month × 500KB avg → 500GB bandwidth.
With WebP: 325GB → **saves $26/month** at $0.15/GB.

---

## Database Query Cost

### Expensive Query Detection
```sql
-- Find queries that cost the most total time
SELECT query, calls, total_exec_time / 1000 AS total_sec, mean_exec_time AS avg_ms
FROM pg_stat_statements ORDER BY total_exec_time DESC LIMIT 10;

-- Find sequential scans on large tables (missing indexes)
SELECT schemaname, relname, seq_scan, seq_tup_read,
       idx_scan, idx_tup_fetch
FROM pg_stat_user_tables
WHERE seq_scan > 100 AND seq_tup_read > 10000
ORDER BY seq_tup_read DESC;
```

### Index Cost of Queries
```sql
-- Before: Sequential scan, costs 1000 units, 150ms
EXPLAIN ANALYZE SELECT * FROM orders WHERE customer_id = 123 AND status = 'active';
-- Seq Scan on orders  (cost=0.00..1000.00 rows=5000)
-- Execution Time: 156.234 ms

-- After: Add targeted index
CREATE INDEX idx_orders_customer_status ON orders(customer_id, status);

-- Now: Index scan, costs 0.4 units, 3ms (50x faster)
-- Index Scan using idx_orders_customer_status  (cost=0.00..0.40 rows=5)
-- Execution Time: 3.234 ms
```

**Cost translation:** Reducing avg query time from 150ms to 3ms means the same DB instance handles 50x more queries → downsize from db.t4g.large ($108/month) to db.t4g.micro ($10.80/month). **Saves $97/month.**

### N+1 Query Prevention
```typescript
// Prisma — use include (2 queries instead of N+1)
const users = await prisma.user.findMany({
  include: { posts: true, orders: { select: { id: true, total: true } } }
});

// GraphQL — use DataLoader (batches within request)
const userLoader = new DataLoader(async (ids) => {
  const users = await db.user.findMany({ where: { id: { in: ids } } });
  return ids.map(id => users.find(u => u.id === id));
});
```

### Materialized Views (Precompute Expensive Aggregations)
```sql
CREATE MATERIALIZED VIEW order_stats AS
SELECT customer_id, COUNT(*) as orders, SUM(total) as revenue
FROM orders GROUP BY customer_id;

-- Refresh periodically (not on every write)
REFRESH MATERIALIZED VIEW CONCURRENTLY order_stats;

-- Saves: Eliminates expensive GROUP BY on every dashboard load
```

---

## Caching ROI

### When Caching Pays Off

```
Cache saves money when:
  (DB queries avoided × cost per query) > (Redis instance cost)

Example:
  10M requests/month, 85% cache hit → 8.5M queries avoided
  DB instance saved: db.t4g.large → db.t4g.micro = $97/month saved
  Redis cost: cache.t4g.micro = $12.24/month
  NET SAVINGS: $84.76/month
```

### When Caching Costs More Than It Saves
- Cache hit ratio < 50% (too many misses)
- Write-heavy workload (constant cache invalidation)
- Working set too large for cache instance
- TTL < 10 seconds (almost every request misses)

### Cache TTL Guidelines

| Data Type | TTL | Rationale |
|-----------|-----|-----------|
| Feature flags | 30-60s | Fast propagation needed |
| User profile | 5-15 min | Infrequent changes |
| Product catalog | 1-24 hours | Batch updates |
| Static config | 1 hour | Rarely changes |
| CDN static assets | 1 year | Versioned URLs (hash-based) |

---

## Memory Leak Detection

**Real case:** 4 lines of code caused **$12,000/month** in AWS costs from OOM restarts.

### Common Leak Patterns
```javascript
// LEAK: Event listeners never cleaned up
class UserService {
  constructor() {
    eventBus.on('userUpdate', this.handleUpdate);  // Never removed!
  }
  // Fix: Remove listener in destroy/cleanup
  destroy() { eventBus.off('userUpdate', this.handleUpdate); }
}

// LEAK: Closures holding large objects
function processData(hugeArray) {
  return function getStats() {
    return hugeArray.length;  // Holds entire array in memory forever
  };
}
// Fix: Extract only what you need
function processData(hugeArray) {
  const length = hugeArray.length;
  return function getStats() { return length; };
}

// LEAK: Growing collections without bounds
const cache = new Map();
function cacheResult(key, value) {
  cache.set(key, value);  // Never evicted!
}
// Fix: Use LRU cache with max size
import { LRUCache } from 'lru-cache';
const cache = new LRUCache({ max: 1000 });
```

### Detection
```bash
# Node.js heap snapshot
node --inspect app.js
# Open chrome://inspect → Take heap snapshot → Compare two snapshots

# In code: Monitor heap usage
setInterval(() => {
  const { heapUsed, heapTotal } = process.memoryUsage();
  if (heapUsed / heapTotal > 0.85) {
    console.warn(`Memory pressure: ${(heapUsed / 1024 / 1024).toFixed(0)}MB used`);
  }
}, 30000);
```

**Cost impact:** Memory leaks cause OOM restarts → cold start overhead → 20-40% higher cloud bills.

---

## Compression

### Response Compression
```typescript
import compression from 'compression';
app.use(compression({ threshold: 1024, level: 6 }));
// Reduces JSON responses by 70-90%
// 100KB response → 10-30KB
```

### Before Storage
```typescript
import zlib from 'zlib';

// Compress before S3 upload
const compressed = zlib.gzipSync(JSON.stringify(data));
await s3.putObject({
  Bucket: 'my-bucket', Key: 'data.json.gz',
  Body: compressed, ContentEncoding: 'gzip'
}).promise();
// JSON logs compress 80-90% → massive S3 savings
```

### Static Asset Compression
```javascript
// Vite/webpack: Generate .br and .gz files at build time
// vite.config.ts
import viteCompression from 'vite-plugin-compression';
export default {
  plugins: [
    viteCompression({ algorithm: 'brotliCompress' }), // Brotli: 20% better than gzip
    viteCompression({ algorithm: 'gzip' }),
  ]
};
```
