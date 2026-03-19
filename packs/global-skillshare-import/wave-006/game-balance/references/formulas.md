# MechaScrapyard — Balance Formulas Reference

This file documents the actual formulas as implemented in the codebase. Always verify against the source files if you suspect drift — this is a snapshot, not authoritative truth.

**Source files:**
- Main logic: `src/game.js`
- Runner/task logic: `src/modules/runner.js`
- Player base values: `data/mecha/player.json`
- Glory shop: `data/mecha/glory_shop.json`
- Upgrades: `data/mecha/upgrades.json`
- Tasks: `data/mecha/tasks.json`
- Skills: `data/mecha/skills.json`
- Combat config: `data/mecha/combat_config.json`
- Factions: `data/mecha/factions.json`

---

## Stat Growth

### Diminishing Returns (`_growStat`, game.js ~1735)
```
scale = 1 / (1 + stat.val / 50)
effective_gain = amount * scale * gloryPoolMult
stat.val = min(stat.max, stat.val + effective_gain)
```

At val=0: scale=1.00 (full rate)
At val=25: scale=0.67
At val=50: scale=0.50 (half rate)
At val=75: scale=0.40
At val=100: scale=0.33 (stat max)

### Passive Task Stat Growth (runner.js ~331)
- `t_income` → charisma: `0.001 * trainSpeed * dt`
- `t_recipe` → focus: `0.001 * trainSpeed * dt`
- `t_exploration` → neuro: `0.001 * trainSpeed * dt`
(All multiplied by diminishing returns scale above)

### Base Perpetual Task Rates (tasks.json)
- Scavenge Scrap: +0.6 scrap/sec, costs 0.15 energy/sec
- Heavy Lifting: +0.05 muscle/sec, costs 0.5 energy/sec
- Repair Circuitry: +0.05 neuro/sec, costs 0.4 energy/sec
- Drone Chasing: +0.05 reflex/sec, costs 0.6 energy/sec
- Endure Wastes: +0.05 grit/sec, costs 0.8 energy/sec

---

## Resource Income

### Focus Multiplier (game.js ~453)
```
multiplier = 1 + (focus * 0.05)
effectiveRate = item.rate * multiplier  (positive rates only)
```
At focus=1: ×1.05; focus=10: ×1.50; focus=20: ×2.00

### Energy Regeneration
- Base rate: +0.3/sec
- Max energy: 50
- Stress recovery: `grit * 0.1` per sec

---

## Glory Pool System

### Threshold Bonuses (`_getGloryPoolBonuses`, game.js ~2005)
| Pool | Stat Growth Mult | Bonus SP | K.I.T.A. Start Level | Start Maneuver | Faction Bonus |
|------|-----------------|----------|----------------------|----------------|---------------|
| 0    | ×1.00           | 0        | 1                    | No             | 0             |
| 50   | ×1.05           | 0        | 1                    | No             | 0             |
| 150  | ×1.10           | +1       | 1                    | No             | 0             |
| 300  | ×1.15           | +2       | 2                    | No             | 0             |
| 500  | ×1.20           | +2       | 2                    | Yes            | 0             |
| 1000 | ×1.25           | +5       | 2                    | Yes            | +15 rep       |
| 2500 | ×1.30           | +5       | 2                    | Yes            | +15 rep       |

Glory pool is cumulative across prestige cycles (never resets, just grows).

---

## Prestige Glory Calculation (`_calculatePrestigeGlory`, game.js ~1104)

### Base Glory Components
| Source | Amount |
|--------|--------|
| Phase bonus (highest home tier) | phase_1=5, phase_2=15, phase_3=30, phase_4=50, phase_5=80 |
| Story mission completed | +5 each |
| Side mission completed | +2 each |
| Combat mission repeats | min(completedCount, 3) × 3 per mission |
| Economy bonus | floor(totalResources × 0.01), max 30 |

### Multiplier Stack (applied to base glory)
| Factor | Multiplier |
|--------|-----------|
| Alignment: Pragmatist | ×1.05 |
| Alignment: Paragon (morale ≥ 40) | ×1.10 |
| Alignment: Shadow (morale ≤ -40) | ×1.10 |
| Consistency bonus | ×1.15 (currently hardcoded, not player-earned) |
| First prestige bonus | ×1.50 (cycleCount === 0 only) |

**Full formula:** `floor(baseGlory × alignmentMult × 1.15 × firstBonus)`

### Glory Shop Items (glory_shop.json)
| Item | Cost (glory pool) | Max | Effect |
|------|-------------------|-----|--------|
| Legacy Training | 50 | 3 | +skill points on cycle start |
| K.I.T.A. Memory Module | 100 | 1 | K.I.T.A. starts at higher level |
| City Reputation | 150 | 2 | +faction rep on cycle start |
| Hidden Cache | 75 | 1 | Starting resource cache |

---

## Prestige Reset Behavior

### What resets
- All stats back to 1
- All resources to starting values
- All missions/items locked again
- Morality resets to 0

### What persists
- Glory pool (cumulative, never resets)
- Glory shop purchases
- Street cred: positive × 0.30 preserved; negative → 0
- Story flags (certain ones persist for narrative continuity)
- Cycle count +1

---

## Street Credibility

**Range:** -20 to +100
**Starting value:** 0
**Prestige reset:** positive × 0.30, negative → 0

### Threshold Effects
| Threshold | Effect |
|-----------|--------|
| ≥ 40 | DTL bleed rate ×0.75 (25% reduction) |
| ≥ 40 | Contact loyalty gain ×1.50 |
| 0–29 | Negotiation tier: LOW |
| 30–59 | Negotiation tier: MID |
| ≥ 60 | Negotiation tier: HIGH |

---

## Upgrade Cost Scaling

```
cost[n] = baseCost * costScale^owned
```
- Scrap Compressor: base 50, scale 1.5 → 50, 75, 112, 168, 253...
- Energy Cell: base 25, scale 1.4 → 25, 35, 49, 68, 96...

---

## Skill System

### Skill Point Thresholds
Skill points awarded at skill levels: 4, 8, 12, 16, 20
(1 point per threshold crossed — max 5 points per skill)

### Sub-Skill Costs
- Tier 1: 1 SP | Tier 2: 2 SP | Tier 3: 3 SP | Tier 4: 4 SP

### Skill Mod Formulas (`base//cap/offset`)
| Skill | Formula | Effect at max |
|-------|---------|---------------|
| Gathering | 0.02 × level, cap 100 | +2.00 (200% bonus) |
| Mecha Tech | 0.05 × min(level, 20) | +1.00 |
| Combat | 0.5 × min(level, 20) | +10 |
| Hacking | 0.01 × min(level, 20) | +0.20 |
| Investigation | 0.03 × min(level, 20) | +0.60 |

### Skill XP Growth (runner.js)
- Primary: 0.01/sec × trainSpeed
- Secondary: 0.005/sec × trainSpeed (half rate)

---

## K.I.T.A. (Android Companion)

### XP to Next Level
```
xpToNext = floor(100 * 1.5^(level - 1))
```
Level 1→2: 100 XP | Level 2→3: 150 XP | Level 3→4: 225 XP | Level 4→5: 338 XP

---

## Combat

### Glory from Combat (combat_config.json)
- Base survival: +1 glory
- Torso destroyed: +2 glory
- Tactical excellence: +2 glory

### Starting Mecha (Hayabusa Mk.I)
- ATK: 10, DEF: 10, ENR: 50, COR: 5
- Torso: 40 HP / 3 integrity
- Arms: 20 HP / 2 integrity
- Legs: 30 HP / 2 integrity

### Loot Table (1d8)
- 1–2: 50 scrap
- 3–6: 1d6 supply
- 7–8: nothing

---

## Faction Reputation Tiers
| Rep | Tier | Unlocks |
|-----|------|---------|
| 0 | Unknown | — |
| 10 | Acquaintance | Basic vendor, patrol missions |
| 25 | Trusted | Full vendor, contracts |
| 50 | Allied | Exclusive blueprints, restricted missions |
| 75 | Honored | Prototypes, special ops |
| 100 | Legend | All blueprints, honorary status |
