# Codex Consultation Output Format

Template for final output at Synthesize step.

```
══════════════════════════════════════════════════════════════════════════════
CODEX CONSULTATION SUMMARY
══════════════════════════════════════════════════════════════════════════════

Question:    [question]
Iterations:  [N]/8 ([converged|cap reached|early exit: reason])
Ledger:      [F1, F2, ...] or "none"

──────────────────────────────────────────────────────────────────────────────
AGREED ([count])
──────────────────────────────────────────────────────────────────────────────

| # | Point | Evidence |
|---|-------|----------|
| 1 | [point] | [execution|textual|n/a] |

──────────────────────────────────────────────────────────────────────────────
DISMISSED ([count])
──────────────────────────────────────────────────────────────────────────────

| # | Point | Tag | Reason |
|---|-------|-----|--------|
| 1 | [point] | [REJECTED|CONCEDED|UNDEFENDED|OUT-OF-SCOPE] | [reason] |

──────────────────────────────────────────────────────────────────────────────
UNRESOLVED ([count])
──────────────────────────────────────────────────────────────────────────────

| # | Point | Status | Crux |
|---|-------|--------|------|
| 1 | [point] | [blocked|tradeoff|definitional] | [what would resolve] |

──────────────────────────────────────────────────────────────────────────────
SURFACED QUESTIONS
──────────────────────────────────────────────────────────────────────────────

- [empirical blocker question]

──────────────────────────────────────────────────────────────────────────────
NOT EVALUATED ([count])
──────────────────────────────────────────────────────────────────────────────

| # | Point | Reason |
|---|-------|--------|
| 1 | [point] | [phase violation|raised in DEVELOPMENT|phase closed] |

══════════════════════════════════════════════════════════════════════════════
```

## Formatting Rules

- **Empty sections:** Replace table with `— none —`
- **Counts:** Include count in each section header
- **Exit reason:** One of: `converged`, `cap reached`, `early exit: trivial`, `early exit: quality`

## Justification Requirement

Dismissed and Unresolved items must include substantive one-line reasons. Generic fills ("not accepted", "unclear") are insufficient.

**Dismissed:** State the specific flaw, evidence, or procedural reason.
- Good: "out-of-scope: addresses deployment, not design"
- Good: "undefended after reminder"
- Bad: "not accepted"

**Unresolved:** State why resolution was blocked.
- Good: "blocked on load data"
- Good: "definitional: 'scalable' undefined"
- Bad: "couldn't resolve"
