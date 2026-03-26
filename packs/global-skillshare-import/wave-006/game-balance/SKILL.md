---
name: game-balance
description: >
  Analyze and tune balance in MechaScrapyard — stat progression curves, resource income rates,
  upgrade cost scaling, glory pool thresholds, prestige cycle feel, and combat rewards. Use this
  skill whenever the user asks about balance, tuning, numbers, pacing, or whether something feels
  right or wrong in the game loop. Trigger on: "does the prestige feel rewarding enough?", "is
  scrap income too slow?", "stat growth feels grindy", "glory feels too low", "is the upgrade
  curve fair?", "what should I tweak to make cycle 2 feel different?", "combat doesn't pay off",
  "street cred threshold too hard to reach", or any question about whether game numbers feel good.
  Also trigger when the user is about to design a new phase or mechanic and needs to know if it
  fits existing balance ranges.
risk: safe
---

# Game Balance Analyst — MechaScrapyard

You're analyzing balance for **MechaScrapyard**, a cyberpunk idle RPG with a prestige loop. The
game runs in real time (dt-based), so income rates and growth curves compound over actual session
length. Balance lives in the intersection of math and feel — always reason about both.

**Read `references/formulas.md` first.** It has all known formulas and tuning values extracted
from the source. Verify against the live source files if the user reports something that doesn't
match, or if the question concerns a system not yet in the reference.

---

## What to analyze and how

### 1. Stat Progression Curves

The diminishing returns formula is `scale = 1 / (1 + val / 50)`. At val=50, growth is half speed.
At val=100 (the cap), it's one-third. This creates a soft ceiling that gates Phase 5 content.

When asked about stat pacing, simulate the curve mentally or compute it:
- How many in-game seconds at max task rate to reach val=50? val=75? val=100?
- Does the glory pool multiplier (1.05×–1.30×) make a meaningful difference on cycle 2?
- Are there stats that max out too fast (muscle) or too slow (focus) relative to when they matter?

Flag if: a stat can reach its cap before the player would naturally prestige, making the curve
pointless. Or if a stat never realistically caps, meaning upgrades that gate on high values are
unreachable.

### 2. Resource Income & Upgrade Costs

Resource pacing determines if the player feels momentum or friction. The key ratio is:
**"minutes to afford next upgrade at current income"**.

When analyzing:
- Calculate effective scrap rate: `0.6/sec × (1 + focus × 0.05)` baseline
- Compare against the upgrade cost curve: `baseCost × costScale^owned`
- At costScale=1.5, the 5th purchase costs `base × 1.5^4 = 5.06×` the first
- Is there a point where income clearly can't keep up with upgrade costs (intentional friction)?
  Or does income snowball past upgrades (making them feel trivial)?

Flag if: upgrade costs reach a point where realistic session income can't fund them within a
single prestige cycle. Or the inverse — upgrades are so cheap relative to income that the player
never has a meaningful "save up" moment.

### 3. Glory Pool & Prestige Cycle Feel

The glory pool is the prestige meta-progression. It accumulates across cycles, never resets, and
unlocks bonuses at 6 thresholds (50/150/300/500/1000/2500).

**Typical first cycle glory:**
- Max phase home (phase_4=50): +50
- Story missions (5 × 5): +25
- Side missions (10 × 2): +20
- Combat missions (5 missions × 3 repeats × 3): +45
- Economy bonus: +10–20
- Subtotal: ~150–160 base
- × alignment (1.10) × consistency (1.15) × first prestige (1.50) ≈ **285–300 glory**

This puts cycle 1 at threshold 300 (×1.15 stat growth, +2 SP, K.I.T.A. level 2).
**Is that right?** A player who completes everything hits the 300 threshold in one cycle. A player
who rushes might only hit 150. This spread is the pacing question.

When asked about prestige feel, evaluate:
- Does cycle 1 feel meaningfully rewarded? (Landing at 150 vs 300 matters a lot)
- Is the jump from 1000 to 2500 for that last +0.05× worth multiple cycles of grinding?
- Are glory shop items priced correctly relative to typical per-cycle glory?

### 4. Street Credibility Thresholds

Street cred runs -20 to +100. Key thresholds: 30 (mid negotiation), 40 (DTL/loyalty bonus), 60
(high negotiation). On prestige, positive cred resets to 30%.

Evaluate: is the 40 threshold reachable in a normal cycle without dedicated grinding? Is the 30%
preservation on prestige enough to feel like progress carries over, or does it feel like starting
over?

### 5. Combat Rewards

Combat earns glory at prestige time (min(completedCount, 3) × 3 per mission), plus loot during
combat. The loot table (1d8: 50% scrap, 37.5% 1d6 supply, 12.5% nothing) should be compared
against the opportunity cost of doing combat vs. perpetual tasks.

Flag if: combat feels like a net loss economically vs. just running perpetual tasks. Or if
repeating the same missions 3× for glory is obviously the optimal strategy, reducing variety.

---

## How to structure your analysis

**For a focused question** (e.g., "is stat growth too slow?"):
1. State the relevant formula with actual numbers
2. Compute the key values (time to 50, time to 100, etc.)
3. Identify the tension or finding
4. Give a concrete tuning recommendation with specific proposed values

**For a broad audit** (e.g., "audit the prestige cycle"):
Structure the output as sections:

```
## Balance Audit: [Topic]

### Finding: [Short label]
[What the numbers show. Be specific — "at val=50, growth is 50% of base" not "growth slows down."]

### Risk: [What feels wrong or could break]
[Player experience implication.]

### Recommendation
[Specific change: "Change the denominator from 50 to 35 to make growth feel faster in the mid-range."]
[Or: "The system is working as intended — don't touch it."]
```

---

## What good tuning recommendations look like

Always ground suggestions in the specific formula or data value being changed, not vague
adjectives. Include the change as a one-liner the developer can apply directly.

**Good:**
> The consistency bonus is a hardcoded ×1.15 regardless of player behavior. This means it rewards
> nothing. Consider making it earned: track morality sign-flips across the cycle, then award
> ×1.15 only if the player stayed in one alignment (morale never crossed from positive to negative
> or vice versa). This also gives the alignment system teeth.

**Bad:**
> The prestige system could feel more rewarding if the bonuses were bigger.

---

## Cross-file investigation

`references/formulas.md` gives you the math, but **the data files are where the real balance lives**.
Formulas only tell you how numbers are processed — the data files tell you what numbers actually
exist in the game. Always read the relevant data files before concluding an analysis, not just
when something seems wrong.

### Which files to read for each topic

| Question | Files to read |
|----------|--------------|
| Prestige / glory | `src/game.js` (`_calculatePrestigeGlory`), `data/mecha/glory_shop.json`, `data/mecha/missions.json` (count story vs combat missions, check tags) |
| Resource income / upgrade costs | `data/mecha/tasks.json` (task rates + crafting costs), `data/mecha/upgrades.json` (full list, costScale, max) |
| Stat growth | `src/game.js` (`_growStat`), `src/modules/runner.js` (task stat gain rates) |
| Combat economy | `data/mecha/missions.json` (encounter missions), `data/mecha/combat_config.json` |
| Street cred / faction | `src/game.js` (threshold logic), `data/mecha/factions.json` |
| Glory shop | `data/mecha/glory_shop.json` — read every item, total max spend, compare to per-cycle glory |

### What to look for that formulas won't tell you

- **Classification traps** — missions that have both `narrative` blocks and combat `encounter` tags
  may be misclassified by the prestige glory calculator. The formula assumes these are mutually
  exclusive, but the data may violate that assumption.
- **Crafting sinks vs income** — tasks.json has both income tasks and crafting tasks. A crafting
  task that drains a resource faster than income produces it creates an invisible wall the formulas
  reference won't show.
- **Shop completability** — sum the total glory cost to max every glory shop item. If a first-cycle
  player can buy most of them, there's no long-term savings goal.
- **Mission count vs formula assumptions** — the formulas reference uses estimates. Count the
  actual missions in missions.json; the real number may change the prestige projection significantly.
- **Patrol vs story misclassification** — patrol missions returning only +2 glory each while
  requiring energy and combat creates a quiet trap. Verify mission tags match player expectations.

### Source files for formula verification

- `src/game.js` — all runtime formulas (search function names from formulas.md)
- `src/modules/runner.js` — task and skill XP rates
- `data/mecha/missions.json` — full mission list with tags, encounter, narrative, rewards
- `data/mecha/tasks.json` — perpetual task rates and crafting costs
- `data/mecha/upgrades.json` — upgrade list with baseCost, costScale, max
- `data/mecha/glory_shop.json` — shop items with costs and effects
