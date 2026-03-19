# Services & FinOps Reference

## Observability Cost Control

### The Problem
- Traces: 60-70% of observability costs
- Logs: 20-30% of observability costs
- Total market: $34.1B in 2026 — most of it wasted

### Platform Pricing (Monthly, Mid-Size Team)
| Platform | Cost | Pricing Model |
|----------|------|---------------|
| Datadog | $8,000+ | Per host + per GB + per metric (complex) |
| New Relic | $1,000-2,000 | Per user + per GB ingested |
| Grafana Cloud | $1,500 | Per signal volume + per user |
| Self-hosted Grafana + Prometheus | $200-500 | Infrastructure only |

### Log Sampling (Immediate Savings)
```typescript
import pino from 'pino';

const logger = pino({
  level: process.env.NODE_ENV === 'production' ? 'warn' : 'debug',
});

// Sample INFO-level logs in production
const SAMPLE_RATE = 0.1; // Log 10% of info events
function infoSampled(msg: string, data?: object) {
  if (Math.random() < SAMPLE_RATE) logger.info(data, msg);
}

// Always log errors and warnings (no sampling)
logger.error({ err, traceId }, 'Payment failed');
logger.warn({ userId }, 'Rate limit approaching');

// Sample info-level
infoSampled('Request completed', { path: req.path, duration: ms });
```
**Saves:** 90% log volume reduction while keeping all errors.

### Trace Sampling
```typescript
// Tail sampling: Keep 100% of errors + slow requests, sample the rest
const tracer = require('dd-trace').init({
  sampleRate: 0.1,  // Send 10% of normal traces
  // But always send error traces (configured in Datadog agent)
});
```
**Saves:** 70-80% on trace costs while keeping all interesting traces.

### High-Cardinality Metric Pitfalls
```typescript
// BAD: Creates millions of time series ($$$$)
counter.inc({ user_id: userId, request_id: requestId });

// GOOD: Aggregate by meaningful dimensions only
counter.inc({ endpoint: '/api/users', method: 'GET', status: '200' });
```
**Rule:** Never put user IDs, request IDs, timestamps, or UUIDs in metric labels.

### Retention Policies
| Log Type | Retention | Rationale |
|----------|----------|-----------|
| Application errors | 90 days | Debugging, postmortems |
| Access logs | 30 days | Security review period |
| Debug logs | 7 days | Short-term troubleshooting |
| Health check logs | 1 day | Almost never needed |
| CI/CD logs | 14 days | Build debugging |

---

## Auth Provider Economics

### Pricing Comparison (2026)

| Provider | Free Tier | Paid | SAML SSO |
|----------|----------|------|----------|
| Clerk | 10K MAUs | $0.02/MAU | $99/month |
| Auth0 | 7.5K MAUs | $240/month (3K MAUs) | $1,500/month |
| Supabase Auth | 50K MAUs | Included in Pro ($25) | Included |
| Keycloak | Unlimited | Free (self-host) | Free |
| Firebase Auth | 50K MAUs | Free (phone auth costs) | Not available |

### Cost at Scale
```
10,000 MAUs:
  Clerk: Free
  Auth0: $240/month
  Supabase: $25/month (included in Pro)
  Firebase: Free

100,000 MAUs:
  Clerk: $1,800/month (90K × $0.02)
  Auth0: $1,500+/month (Enterprise tier required)
  Supabase: $25/month (still included!)
  Firebase: Free (but limited features)

1,000,000 MAUs:
  Clerk: $19,800/month
  Auth0: Custom pricing ($$$$)
  Supabase: $25/month (yes, really)
  Self-hosted Keycloak: $50-200/month (infrastructure only)
```

**Rule:** Supabase Auth is cheapest at scale if you use Supabase. Self-hosted Keycloak for maximum control. Clerk for best DX at moderate scale.

---

## Search Service Costs

### Pricing (250K Records, 1M Searches/Month)
| Service | Monthly Cost | Self-Hostable |
|---------|-------------|---------------|
| Algolia | $500+ | No |
| Meilisearch Cloud | $59 | Yes (free) |
| Typesense Cloud | $60 | Yes (free) |
| Elasticsearch (AWS) | $200+ | Yes |
| Self-hosted Meilisearch | $15-30 (server) | Yes |

**Rule:** Start with Meilisearch (free self-hosted or $59 cloud). Only use Algolia if you need their specific features (AI recommendations, crawling).

---

## Email Service Costs

### Pricing (100K Emails/Month)
| Service | Cost | Notes |
|---------|------|-------|
| AWS SES | $10 | Cheapest, requires setup |
| Resend | $20 | Great DX, React Email |
| Postmark | $50 | Best deliverability |
| SendGrid | $20-50 | Established, complex pricing |

**Rule:** AWS SES for cost-sensitive. Resend for developer experience. Postmark for transactional email deliverability.

---

## FinOps Practices

### Cost Allocation Tags (Foundation)
```bash
# Tag ALL resources — untagged = unaccountable
aws ec2 create-tags --resources i-1234567890 --tags \
  Key=Environment,Value=production \
  Key=Team,Value=backend \
  Key=CostCenter,Value=engineering \
  Key=Service,Value=api-server
```

**Required tags:**
| Tag | Purpose | Example |
|-----|---------|---------|
| Environment | Filter prod vs dev costs | production, staging, dev |
| Team | Accountability | backend, frontend, data |
| Service | Granular attribution | api-server, worker, cron |
| CostCenter | Finance allocation | engineering, marketing |

### Budget Alerts
```bash
# AWS Budget with alert at 80% and 100%
aws budgets create-budget --account-id 123456789 --budget '{
  "BudgetName": "Monthly-Total",
  "BudgetLimit": { "Amount": "2000", "Unit": "USD" },
  "TimeUnit": "MONTHLY",
  "BudgetType": "COST"
}' --notifications-with-subscribers '[
  {
    "Notification": {
      "NotificationType": "ACTUAL",
      "ComparisonOperator": "GREATER_THAN",
      "Threshold": 80
    },
    "Subscribers": [{ "SubscriptionType": "EMAIL", "Address": "team@company.com" }]
  }
]'
```

### Unit Economics Tracking
```typescript
// Track cost per business metric
const metrics = {
  totalMonthlyCost: 2033,          // From AWS Cost Explorer
  monthlyActiveUsers: 50000,
  monthlyOrders: 100000,
  monthlyApiRequests: 10_000_000,
};

const unitEconomics = {
  costPerUser: metrics.totalMonthlyCost / metrics.monthlyActiveUsers,        // $0.041
  costPerOrder: metrics.totalMonthlyCost / metrics.monthlyOrders,            // $0.020
  costPerRequest: metrics.totalMonthlyCost / metrics.monthlyApiRequests,     // $0.0002
  costPerThousandRequests: (metrics.totalMonthlyCost / metrics.monthlyApiRequests) * 1000, // $0.20
};

// Alert if unit cost increases >20%
if (unitEconomics.costPerUser > previousMonth.costPerUser * 1.2) {
  alert('Cost per user increased >20% — investigate');
}
```

### Monthly Cost Review Checklist
- [ ] Review Cost Explorer for top 5 cost increases
- [ ] Check for untagged resources
- [ ] Identify idle/unused resources (0% CPU, no traffic)
- [ ] Review reserved capacity utilization (unused RIs = waste)
- [ ] Check for cost anomalies (unexpected spikes)
- [ ] Compare unit economics to previous month
- [ ] Review spot instance interruption rate (if using spot)
- [ ] Check data transfer costs by service

---

## Managed vs Self-Hosted Decision

### When Managed is Cheaper
- Team < 5 engineers (engineering time is expensive)
- Usage is low-moderate (managed pricing beats server costs)
- Need compliance/certifications (managed handles this)
- Ops expertise is limited

### When Self-Hosted is Cheaper
- Scale exceeds managed plan limits (1M+ MAUs for auth, 1M+ searches)
- You have ops/DevOps capability
- Data sovereignty requirements
- Predictable, stable workload

### Cost Crossover Points (Approximate)
```
Auth: Self-host at ~200K MAUs (Keycloak replaces $2K+/month Clerk/Auth0)
Search: Self-host at ~500K records (Meilisearch replaces $500+/month Algolia)
Database: Self-host at ~$500/month managed bill (but factor in ops time)
Redis: Self-host at ~$100/month managed bill
Email: Almost never self-host (SES at $0.10/1K is hard to beat)
```

---

## Cost Optimization Priority Matrix

| Action | Effort | Monthly Savings | Do First? |
|--------|--------|----------------|-----------|
| S3 Intelligent-Tiering | 5 min | $30-200 | Yes |
| Log retention policies | 10 min | $10-50 | Yes |
| Fix N+1 queries | 1-2 hours | $50-150 | Yes |
| WebP/AVIF images | 2-4 hours | $50-200 | Yes |
| VPC Endpoints | 1 hour | $50-300 | Yes |
| Lambda memory tuning | 1-2 hours | $20-100 | Yes |
| Bundle tree-shaking | 2-4 hours | $50-200 | Yes |
| Redis caching layer | 1-2 days | $50-300 | If read-heavy |
| Container right-sizing | 2-4 hours | $30-200 | If K8s |
| Reserved/Savings Plans | 1 hour | $200-1000 | If stable workload |
| Self-host auth/search | 1-2 weeks | $100-500 | At scale only |
| Trace sampling | 1 hour | $50-500 | If using Datadog/NR |
