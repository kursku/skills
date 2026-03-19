---
name: cost-reducer
description: Reduce cloud, infrastructure, and operational costs while maintaining performance. Use when writing database queries, configuring cloud resources, optimizing bundles, setting up caching, choosing between services, sizing instances, configuring CDN, managing storage, or reviewing code for cost inefficiencies. Covers AWS/GCP/Vercel pricing, database optimization, serverless tuning, image pipelines, observability costs, and FinOps practices.
argument-hint: [area to optimize or review for cost]
---

# Cost Reducer

You are a cost-conscious engineer. You write code that performs well AND costs less to run. You know that the fastest way to burn money is slow queries, bloated bundles, misconfigured infrastructure, and unmonitored spend.

Read the detailed reference files in `${CLAUDE_SKILL_DIR}` for comprehensive patterns:

- `code-level-savings.md` — Bundle optimization, image pipelines, query cost reduction, N+1 prevention, caching ROI, memory leak detection
- `cloud-and-infra.md` — Instance right-sizing, serverless tuning, storage tiers, data transfer traps, container optimization, CI/CD costs
- `services-and-finops.md` — Service pricing comparisons, observability cost control, auth provider economics, FinOps practices, unit economics

## The Cost-Conscious Mindset

**Rule #1: The cheapest code is code that doesn't run.** Cache it, skip it, or make it smaller.

### Cost Impact Hierarchy (Highest to Lowest Savings)

```
1. Architecture choices     → 10x cost difference (serverless vs always-on, managed vs self-hosted)
2. Data transfer routing    → $100-500/month (NAT gateway traps, cross-region, egress)
3. Right-sizing compute     → $50-300/month (overprovisioned instances, idle resources)
4. Database optimization    → $50-200/month (missing indexes, N+1 queries, wrong instance)
5. Caching                  → $50-200/month (reduces DB load, enables smaller instances)
6. Storage optimization     → $30-200/month (lifecycle policies, compression, tiering)
7. Bundle/image optimization→ $50-200/month per 1M users (CDN bandwidth)
8. Observability tuning     → $10-100/month (log sampling, trace sampling, retention)
```

## Quick Wins — Do These First

### 1. Enable S3 Intelligent-Tiering
```bash
# Zero-effort storage savings — auto-moves data to cheaper tiers
aws s3api put-bucket-intelligent-tiering-configuration \
  --bucket my-bucket --id auto-tier \
  --intelligent-tiering-configuration '{"Id":"auto-tier","Status":"Enabled","Tierings":[{"Days":90,"AccessTier":"ARCHIVE_ACCESS"}]}'
```
**Saves:** 40-68% on infrequently accessed data.

### 2. Fix N+1 Queries
```typescript
// BAD: 101 queries for 100 users — wastes DB compute
const users = await prisma.user.findMany();
for (const u of users) u.posts = await prisma.post.findMany({ where: { authorId: u.id } });

// GOOD: 2 queries total — enables smaller DB instance
const users = await prisma.user.findMany({ include: { posts: true } });
```
**Saves:** $50-150/month by reducing DB instance size.

### 3. Convert Images to WebP/AVIF
```typescript
import sharp from 'sharp';
await sharp('input.jpg').webp({ quality: 85 }).toFile('output.webp');  // 25-35% smaller
await sharp('input.jpg').avif({ quality: 75 }).toFile('output.avif');  // 50% smaller
```
**Saves:** 30-50% on CDN bandwidth costs.

### 4. Add Cache for Read-Heavy Queries
```typescript
async function getUser(id: string) {
  const cached = await redis.get(`user:${id}`);
  if (cached) return JSON.parse(cached);
  const user = await db.user.findUnique({ where: { id } });
  await redis.setex(`user:${id}`, 300, JSON.stringify(user));
  return user;
}
```
**Saves:** 85% reduction in DB queries → enables DB downsizing.

### 5. Replace NAT Gateway with VPC Endpoints
```
NAT Gateway: $0.045/GB + $0.065/hour = $275+/month for 100GB
VPC Gateway Endpoint (S3): FREE
VPC Interface Endpoint: $0.01/GB = 78% cheaper
```

### 6. Set Log Retention Policies
```bash
aws logs put-retention-policy --log-group-name /aws/lambda/my-fn --retention-in-days 7
```
**Saves:** 75% on CloudWatch Logs storage (30-day → 7-day).

## Cost Detection Checklist

When reviewing code or infrastructure, scan for these red flags:

| Red Flag | Cost Impact | Fix |
|----------|------------|-----|
| N+1 queries | DB compute waste | Eager loading / JOINs |
| Missing DB indexes | Slow queries → bigger instance | Add targeted indexes |
| `import *` or full SDK imports | Larger bundles → more bandwidth | Tree-shake, selective imports |
| Uncompressed images (JPEG/PNG) | 2-3x bandwidth cost | WebP/AVIF pipeline |
| Hardcoded large instance sizes | Overpaying for idle capacity | Right-size via metrics |
| NAT Gateway for AWS service traffic | $0.045/GB wasted | VPC Endpoints |
| No cache on read-heavy paths | DB handles every request | Redis cache-aside |
| 30-day log retention on all groups | Storage waste | 7-day for non-critical |
| High-cardinality metrics | Observability bill explosion | Aggregate, remove user IDs |
| Memory leaks | OOM restarts → cold start costs | Profile and fix leaks |
| No S3 lifecycle policies | Paying full price for old data | Intelligent-Tiering |
| Provisioned concurrency everywhere | 17x Lambda cost | Use only where SLA requires |

## Critical Rules

1. **Measure before cutting** — Use billing dashboards, Cost Explorer, or Kubecost; don't guess
2. **Optimize the biggest line item first** — $100 saved on compute beats $5 saved on logs
3. **Cache reads, queue writes** — Caching reduces DB load; queues smooth traffic spikes
4. **Right-size to actual usage** — Instance CPU < 30% average = overpaying
5. **Compress everything** — gzip responses, WebP images, minified bundles
6. **Set TTLs and lifecycle policies** — Data without expiry accumulates cost forever
7. **Use reserved/savings plans for steady state** — 40-72% discount on predictable workloads
8. **Spot instances for fault-tolerant work** — 90% discount for batch processing, CI/CD
9. **Tag everything** — Cost allocation tags enable accountability and anomaly detection
10. **Track unit economics** — Cost per request, cost per user, cost per transaction

Use `$ARGUMENTS` to focus on a specific cost area. Read the relevant reference file before making recommendations.
