# game-content skill — session notes

## Status
**Iteration 1 complete.** Eval viewer generated, awaiting user review of outputs.

Review file: `C:/Users/nicol/.claude/skills/game-content-workspace/iteration-1/review.html`

---

## What the skill does
Authors new game content for MechaScrapyard as valid JSON ready to drop into data files:
- **Events** (`events.json`) — lore triggers, grandpa dialogue, choice branches
- **Story missions** (`missions.json`) — with narrative, intel tiers, storyBeats, debrief
- **Contacts** (`contacts.json`) — NPC loyalty system entries
- **Glory shop items** (`glory_shop.json`) — prestige-persistent upgrades

Skill files:
- `SKILL.md` — workflow + quick reference table
- `references/schemas.md` — full field-by-field schemas, enemy roster, faction rep keys, require expression syntax

---

## Iteration 1 results

**Benchmark delta: +0.00** — both with-skill and baseline passed all assertions 100%.

### What this means
The assertions were too easy — bare Claude can produce structurally valid JSON without the skill. The real value difference is qualitative:

| With skill | Baseline |
|-----------|---------|
| Explicit validation steps documented | Sometimes richer structure (3 intel tiers vs 2) |
| Better flag naming rationale | More storyBeats (on_start + on_complete) |
| Narrative arc integration (KZ-INDUSTRIAL breadcrumb) | Can find require keys by reading gameState.js directly |
| `street_cred` penalty on NTPD betrayal choice | Introduced new NPC speaker `yara_underground` |

### Key question for next iteration
Do the with-skill outputs feel more **trustworthy and ready to drop in**? Or does the baseline produce richer content?

---

## What to do next

### Option A — Improve the skill
The skill needs to add clearer value over baseline. Ideas:
1. **Add require key validation** — instruct skill to verify require keys against `gameState.js` (baseline did this better on eval 0)
2. **Add richer storyBeats guidance** — encourage `on_start` beats, not just `on_complete`
3. **Add narrative integration step** — explicitly check what existing flags/arcs the new content can connect to

### Option B — Improve the assertions
Write harder assertions that only the skill would pass:
- Require key exists in actual game code (not invented)
- At least one storyBeat with `on_start` trigger (story missions)
- Content references at least one existing flag from the game's current flag inventory
- Validation section present in output

### Likely answer
Both. Tighten the skill on require key verification and narrative integration, and add assertions that test those properties. Re-run iteration 2.

---

## Pending: game-balance skill
After finishing game-content, create `game-balance` skill:
- Analyzes stat progression curves (diminishing returns, glory pool multipliers, prestige scaling)
- Sanity-checks resource income rates against player experience arc
- Validates prestige cycle feel
- Suggests tuning changes with reasoning
- Most valuable right before Phase 5

## Pending: phase-advance skill
Automates phase completion ritual:
- Audit current phase completion criteria
- Mark specs done in PHASE_INDEX.md
- Commit + create git tag
- Stub next phase's spec files
