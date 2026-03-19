# Escalation Guide

When and how to escalate customer issues beyond standard support.

## Escalation Tiers

### Tier 1 — Standard Support (Handle Directly)
- Password resets and account access
- How-to questions and feature guidance
- Known bug workarounds
- Billing questions with clear answers
- Feature requests (log and acknowledge)
- General product feedback

### Tier 2 — Senior Support / Team Lead
**Escalate when:**
- Customer has contacted support 3+ times for the same issue
- Issue requires account-level changes beyond standard permissions
- Customer explicitly requests a manager or supervisor
- Refund exceeds standard authorization limit
- Bug affects customer's business operations with no workaround
- Compliance or legal language in the customer's message

**How to escalate:**
```
Internal note:
- Customer: [Name, Account ID]
- Issue: [One-sentence summary]
- Attempts: [What was already tried]
- Why escalating: [Specific reason]
- Recommended action: [Your suggestion]
- Urgency: [Low / Medium / High / Critical]
```

### Tier 3 — Engineering
**Escalate when:**
- Bug cannot be reproduced but customer provides strong evidence
- Data integrity issue (missing data, corrupted records, sync failures)
- Performance degradation affecting specific accounts
- Security concern (unauthorized access, data exposure)
- Integration/API issue requiring code-level investigation

**Include in engineering escalation:**
```
- Account ID / User ID:
- Environment: [Production / Staging]
- Steps to reproduce:
- Expected behavior:
- Actual behavior:
- Error messages / logs:
- Browser / Device / OS:
- Frequency: [Always / Intermittent / Once]
- Impact: [Number of users affected]
- Customer communication: [What we told the customer]
```

### Tier 4 — Executive / Crisis
**Escalate immediately when:**
- Data breach or security incident
- Service-wide outage lasting 30+ minutes
- Legal threat or regulatory complaint
- Press/media involvement
- Enterprise customer threatening churn (ARR > [threshold])
- Any issue involving PII exposure

## SLA Reference

| Priority | First Response | Resolution Target | Examples |
|----------|---------------|-------------------|----------|
| Critical | 15 minutes | 4 hours | Outage, data breach, complete service failure |
| High | 1 hour | 8 hours | Major feature broken, billing error, business-blocking |
| Medium | 4 hours | 24 hours | Non-critical bug, account question, feature request |
| Low | 24 hours | 72 hours | General feedback, how-to, enhancement suggestion |

## Handoff Best Practices

### When handing off to another agent:
1. **Summarize the full history** — don't make the customer repeat themselves
2. **Share what you've already tried** — avoid duplicate troubleshooting
3. **Set customer expectations** — tell them who's taking over and when they'll hear back
4. **Warm handoff when possible** — introduce the next agent by name

### Handoff message to customer:
```
Hi [Name],

I want to make sure you get the best help possible on this. I'm bringing in [Agent/Team] who specializes in [area]. I've shared the full details of our conversation so you won't need to repeat anything.

[Agent/Team] will reach out to you within [timeframe]. If you don't hear back by then, reply to this message and I'll follow up personally.

Best,
[Agent]
```

### Internal handoff note:
```
Handing off to: [Agent/Team]
Customer: [Name] — [sentiment: frustrated/neutral/escalated]
Summary: [2-3 sentences covering the full issue]
What's been tried: [List of actions taken]
What customer expects: [Their stated desired outcome]
Recommended next step: [Your suggestion]
```

## De-escalation Techniques

When a customer is angry or threatening:

1. **Let them vent** — Don't interrupt or rush to a solution
2. **Validate explicitly** — "You're right to be upset about this"
3. **Take ownership** — "This is on us, and here's what I'm doing about it"
4. **Be specific** — Vague promises increase frustration; give concrete actions and timelines
5. **Offer something tangible** — Credit, extension, direct contact, expedited fix
6. **Follow up proactively** — Don't wait for them to chase you

### Phrases that de-escalate:
- "I would be frustrated too if this happened to me."
- "You shouldn't have to deal with this. Let me fix it."
- "I'm going to personally make sure this gets resolved."
- "Here's exactly what's going to happen next..."

### Phrases to avoid:
- "Per our policy..." (sounds bureaucratic)
- "Unfortunately..." (feels like a dead end)
- "There's nothing I can do" (always find something)
- "You should have..." (blames the customer)
- "As I mentioned previously..." (condescending)
- "Calm down" (invalidating)

## CSAT Optimization Tips

Practices that consistently improve satisfaction scores:

1. **Speed matters most when the customer is frustrated** — respond faster to negative-sentiment tickets
2. **Personalize beyond the name** — reference their specific use case, plan, or history
3. **Exceed expectations on resolution** — if you can solve it in one reply, do it
4. **Follow up after resolution** — a check-in 24-48 hours later shows you care
5. **Admit mistakes directly** — customers forgive errors faster when you own them
6. **Give direct answers first** — lead with "Yes", "No", or the solution, then explain
