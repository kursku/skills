---
name: game-content
description: >
  Author new game content for MechaScrapyard — events, story missions, contacts, and glory shop
  items — as valid JSON that slots directly into the data files. Use this skill whenever the user
  asks to write, add, or create any of the following: a new event or story beat, a mission (combat
  or story), a contact NPC, a glory shop upgrade, a moral choice branch, faction rep gating, or
  story flags. Also trigger this skill when the user describes a narrative scenario they want in the
  game — "I want a mid-game Taeyang confrontation", "add a mission where the player has to choose
  between Ironjaw and NTPD", "write some grandpa dialogue for when the garage is built" — even if
  they don't say the word "content" or "JSON". If the task involves adding anything to the game's
  narrative, combat, or progression systems, this skill applies.
risk: caution
---

# Game Content Authoring

You're authoring content for **MechaScrapyard** — a cyberpunk idle RPG set in New Tokyo's
Scrapyard District. The game is built around a prestige loop where the player restores their
father's mecha, builds faction relationships, and uncovers a mystery. The tone is gritty, earned,
and atmospheric (primary reference: Hacknet — text as UI). Content should feel like a real OS
readout, not a game tutorial.

Before generating anything, **read `references/schemas.md`** for the exact field structure of the
content type being requested.

---

## Workflow

### 1. Clarify the request

Identify:
- **Content type**: event, mission, contact, glory shop item, or story flag
- **Placement**: which phase of the game (early = scrapyard chores, mid = faction conflicts, late =
  Taeyang conspiracy), or which existing content it follows/triggers from
- **Mechanical hook**: what condition unlocks it (`require`), what it rewards, whether it has
  choices that branch morality or faction rep
- **Narrative intent**: who's speaking, what the player learns, what emotion it should land on

If the request is vague ("write a mission"), ask one focused question — "What faction or phase is
this for?" — rather than asking everything at once.

### 2. Research existing content

Before writing, scan the relevant file to understand:
- What IDs already exist (to avoid collisions and to pick a good naming pattern)
- What story flags have already been set (so your `require` can reference real ones)
- What enemies and speakers are available

Available enemy IDs, faction rep keys, speaker names, and naming conventions are in
`references/schemas.md`.

### 3. Draft the content

Write the JSON following the exact schema for the content type. Key principles:

**Tone** — Write `desc` and `flavor` as if you're the system terminal. Short, dry, specific.
No em dashes used decoratively. No "discover" or "journey". Facts and implications.
- Good: *"The enforcer drops a dataslate on the workbench without a word."*
- Bad: *"You discover a mysterious clue that sets you on an unexpected journey."*

**Require expressions** — Use `g.KEY>=VALUE` or `g.FLAG>0` syntax. Chain with `&&`. Reference
real player stats (`g.level`, `g.glory`, `g.scrap`, `g.street_cred`) or game flags (`g.msn_ID>=1`,
`g.flag_NAME>0`). Never invent require keys that don't exist in the game.

**Flags** — Set flags that downstream content can gate on. Name them `flag_verb_noun` (e.g.,
`flag_delivered_taeyang_cargo`, `flag_found_surveillance`). When a choice sets a flag, other events
can check it via `require: "g.flag_name>0"`.

**Morality** — Choices that involve compromise, loyalty, or ambiguity should shift morality
(±5–20). Choices that explicitly betray someone or enable systemic harm are higher magnitude.
Paragon threshold: +40. Shadow threshold: -40.

**Rewards** — Keep rewards proportional to difficulty and narrative weight. Story missions reward
more glory and narrative flags than grinding missions. Fail rewards should exist but be smaller.

### 4. Validate

Before presenting the output, mentally check:
- IDs are unique (not duplicating existing ones you saw)
- `require` references real keys
- Enemy IDs exist in the enemy roster
- Speaker names are real NPC IDs or "system"
- Flags set here have names consistent with existing convention

### 5. Present and place

Show the JSON and tell the user exactly where to place it:
- Which file (`data/mecha/events.json`, `missions.json`, etc.)
- Where in the array (after what existing entry, or at the end)
- If the content chains to an existing event or mission, show how to wire it (e.g., add
  `"onComplete": {"event": "evt_your_new_event"}` to the mission)

If writing multiple pieces that chain together (e.g., a mission that fires an event), show them
together with the wiring explained.

---

## Content type quick reference

| Type | File | Key fields | Notes |
|------|------|------------|-------|
| Lore event | events.json | id, name, speaker, require, desc, result?, choices? | Fires when require becomes true |
| Combat mission | missions.json | + enemies, turnLimit, cost, rewards | Standard gameplay loop |
| Story mission | missions.json | + narrative, storyBeats, debrief, intel? | Richer structure, phase-gated |
| Contact | contacts.json | loyalty, benefit, highLoyaltyBenefit | Unlocks via rep or progress |
| Glory shop | glory_shop.json | cost_glory_pool, effect, max, owned | Persists through prestige |

For full field-by-field reference, see `references/schemas.md`.
