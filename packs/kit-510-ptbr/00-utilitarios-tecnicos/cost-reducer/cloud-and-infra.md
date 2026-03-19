# Cloud & Infrastructure Cost Reference

## Instance Right-Sizing

### Detection
```
If average CPU < 30% → instance is oversized
If average CPU > 70% → approaching capacity
Sweet spot: 40-60% average CPU utilization
```

### EC2 Pricing Strategy
| Strategy | Discount | Commitment | Use For |
|----------|----------|-----------|---------|
| On-Demand | 0% | None | Variable/unpredictable load |
| Savings Plans | 40-60% | 1-3 year | Steady baseline compute |
| Reserved | 50-72% | 1-3 year | Specific instance types |
| Spot | Up to 90% | None (2-min interruption) | Batch, CI/CD, fault-tolerant |

**Hybrid approach** (40-60% total savings):
- Baseline (24/7 load): Savings Plans
- Variable load: On-Demand
- Batch/CI: Spot instances

### Kubernetes Right-Sizing
```yaml
# Step 1: Monitor actual usage with metrics-server
kubectl top pods -n production

# Step 2: Compare requests vs actual
# If request=500m CPU but actual=80m → overprovisioned 6x

# Step 3: Right-size
resources:
  requests:
    cpu: 100m       # Match actual + 25% buffer
    memory: 128Mi
  limits:
    cpu: 200m       # 2x request for burst
    memory: 256Mi
```
**Savings:** Right-sizing typically saves 30-70% on compute costs.

---

## Serverless Cost Optimization

### Lambda Memory Tuning

```
Memory vs Cost (10M invocations/month):
128MB:  $21/month  — 8s avg (slow, cheap per-ms but long duration)
256MB:  $38/month  — 4.5s avg
512MB:  $75/month  — 2.2s avg (sweet spot for most workloads)
1024MB: $150/month — 1.1s avg (for CPU-bound)
2048MB: $300/month — 700ms avg (overkill for I/O-bound)
```

**Rule:** Use AWS Lambda Power Tuning to find the cost-optimal memory. Often 512MB is cheapest overall (shorter duration offsets higher per-ms cost).

### Provisioned Concurrency — Usually Overkill
```
On-demand invocation: $0.0000002 per request
Provisioned concurrency: $0.015/unit/hour = $10.80/month per unit

10 units = $108/month — just to keep functions warm
```
**Only use when:** Cold start latency violates a revenue-impacting SLA.
**Alternative:** Scheduled warm-up pings (80-95% warm at 5-15% the cost).

### Lambda Best Practices
```typescript
// Initialize OUTSIDE handler (reused across warm invocations)
const s3 = new S3Client({});
let dbPool: Pool | null = null;

export const handler = async (event: any) => {
  if (!dbPool) dbPool = new Pool({ max: 1 }); // Lazy init, reused
  const result = await dbPool.query('SELECT 1');
  return { statusCode: 200, body: JSON.stringify(result) };
};
```

### API Gateway Cost Trap
```
1B HTTP API requests/month:
  Requests: $900
  Execution logging: $530  ← 37% of total spend!

Fix: Disable execution logging in production
     Use HTTP APIs instead of REST APIs (71% cheaper)
```

### Graviton (ARM) Instances
- Lambda ARM: 20% cheaper + often faster than x86
- EC2 Graviton: 20-40% better price-performance
```yaml
# Lambda: Add architecture
Runtime: nodejs20.x
Architectures: [arm64]  # 20% cheaper
```

---

## Data Transfer Cost Traps

### The NAT Gateway Problem
```
NAT Gateway costs:
  Hourly: $0.065/hour = $47.45/month
  Data processing: $0.045/GB

100GB/month through NAT:
  $47.45 + (100 × $0.045) = $51.95/month

vs VPC Gateway Endpoint (S3/DynamoDB): FREE
vs VPC Interface Endpoint: $8.76/month + $0.01/GB = $9.76/month
```

**Fix priority:**
1. S3 traffic → Gateway Endpoint (free)
2. DynamoDB traffic → Gateway Endpoint (free)
3. Other AWS services → Interface Endpoints (78% cheaper than NAT)
4. Internet traffic → Only thing that needs NAT

### Cross-Region Transfer
```
Same region: Free (within same AZ) or $0.01/GB (cross-AZ)
Cross-region: $0.02/GB
Internet egress: $0.09/GB (first 10TB)

Rule: Keep data and compute in the same region
```

### CloudFront vs Direct S3
```
Direct S3 egress: $0.09/GB
CloudFront: $0.085/GB (cheaper!) + caching reduces origin fetches

3TB/month:
  Direct S3: $270
  CloudFront: $127.50 + $15 origin fetch = $142.50
  Savings: $127.50/month
```

---

## Storage Optimization

### S3 Lifecycle Policies
```json
{
  "Rules": [
    {
      "ID": "archive-logs",
      "Filter": { "Prefix": "logs/" },
      "Transitions": [
        { "Days": 30, "StorageClass": "STANDARD_IA" },
        { "Days": 90, "StorageClass": "GLACIER" }
      ]
    },
    {
      "ID": "delete-old-builds",
      "Filter": { "Prefix": "ci-builds/" },
      "Expiration": { "Days": 30 }
    }
  ]
}
```

### Storage Cost Comparison
| Tier | $/GB/month | Access Cost | Use For |
|------|-----------|-------------|---------|
| S3 Standard | $0.023 | Free GETs | Frequently accessed |
| S3 Infrequent | $0.0125 | $0.01/1K GETs | Monthly access |
| S3 Glacier Instant | $0.004 | $0.01/1K GETs | Quarterly access |
| S3 Glacier Deep | $0.00099 | $0.02/1K GETs + hours retrieval | Yearly/archive |

**Rule:** Enable Intelligent-Tiering on all buckets. It auto-moves data and costs nothing if data is accessed frequently.

---

## Container Optimization

### Multi-Stage Docker Builds
```dockerfile
# Build stage (includes dev tools)
FROM node:20 AS builder
WORKDIR /app
COPY package*.json ./
RUN npm ci
COPY . .
RUN npm run build

# Production stage (minimal)
FROM node:20-alpine
WORKDIR /app
COPY --from=builder /app/dist ./dist
COPY --from=builder /app/node_modules ./node_modules
COPY --from=builder /app/package*.json ./
CMD ["node", "dist/index.js"]
```

**Image size comparison:**
| Base Image | Size |
|-----------|------|
| node:20 (debian) | 1.1GB |
| node:20-alpine | 180MB |
| distroless/nodejs20 | 130MB |

**Cost savings per 100 deploys/month:**
- 1.1GB → 180MB = 920MB saved per pull
- 100 deploys × 920MB = 92GB less transfer
- At $0.09/GB = **$8.28/month** + faster deploys

---

## CI/CD Cost Reduction

### Build Caching
```yaml
# GitHub Actions: Cache node_modules
- uses: actions/cache@v4
  with:
    path: node_modules
    key: ${{ runner.os }}-node-${{ hashFiles('package-lock.json') }}

# Docker layer caching
- uses: docker/build-push-action@v5
  with:
    cache-from: type=gha
    cache-to: type=gha,mode=max
```

**Impact:** 10-minute build → 30-second build (cached) = 95% reduction in CI compute.

### Self-Hosted Runners
```
GitHub Actions: $0.008/minute (Linux)
  100 builds/month × 10 min = 1000 min = $8/month (cheap for small teams)

At scale: 10,000 builds/month × 10 min = $800/month
Self-hosted EC2 spot: ~$15/month
Savings at scale: $785/month
```

**Rule:** Use GitHub-hosted for small teams. Self-host at > 5000 minutes/month.

### Parallel vs Sequential
```yaml
# Sequential: 10 + 5 + 3 = 18 minutes
jobs:
  lint: ...
  test: { needs: lint }
  build: { needs: test }

# Parallel: max(10, 5, 3) = 10 minutes (44% faster)
jobs:
  lint: ...
  test: ...        # No dependency on lint
  build: ...       # Only depends on test passing
```

---

## Database Pricing Comparisons

### PostgreSQL (10GB, 100 QPS peak)

| Provider | Monthly Cost | Notes |
|----------|-------------|-------|
| AWS RDS db.t4g.medium | $65 | Managed, Multi-AZ extra |
| Supabase Pro | $45-50 | Includes auth, realtime, storage |
| Neon Launch | $22.50 | Scale-to-zero, cheapest for bursty |
| PlanetScale (MySQL) | $39 | Branching, serverless |

**Rule:** Neon for dev/bursty, Supabase for full-stack, RDS for enterprise/control.

### Redis

| Provider | Monthly Cost | Notes |
|----------|-------------|-------|
| ElastiCache cache.t4g.micro | $12.24 | AWS managed |
| Upstash | $0-10 | Pay-per-request, scale-to-zero |
| Redis Cloud | $7 | Managed, free tier |

**Rule:** Upstash for low-traffic/serverless. ElastiCache for predictable high-traffic.

---

## Real-World Pricing Scenario

### E-Commerce (1M Users, 1M Orders/Month)

**Before optimization:**
```
RDS db.t4g.large:      $108/month  (N+1 queries, missing indexes)
Lambda (untuned):       $150/month  (1024MB, could be 512MB)
S3 Standard (50TB):    $1,150/month (no lifecycle policies)
NAT Gateway:            $275/month  (S3 traffic going through NAT)
CloudWatch Logs:        $50/month   (30-day retention, all levels)
Vercel bandwidth (3TB): $300/month  (unoptimized bundles/images)
TOTAL:                 $2,033/month
```

**After optimization:**
```
RDS db.t4g.micro + Redis: $23/month   (caching + indexes → smaller DB)
Lambda (512MB, ARM):      $38/month   (right-sized + Graviton)
S3 Intelligent-Tiering:  $628/month   (auto-tiered)
VPC Endpoints:            $10/month   (replaced NAT for S3)
CloudWatch Logs:          $12/month   (7-day retention, sampling)
Vercel bandwidth (1.5TB): $75/month   (WebP + tree-shaking)
TOTAL:                   $786/month

SAVINGS: $1,247/month = $14,964/year (61% reduction)
```
