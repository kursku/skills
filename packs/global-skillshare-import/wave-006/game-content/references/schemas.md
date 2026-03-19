# MechaScrapyard — Content Schemas Reference

## Naming Conventions

| Prefix | Type | Example |
|--------|------|---------|
| `evt_` | Event | `evt_grandpa_memorial` |
| `msn_` | Mission | `msn_fathers_debt_01` |
| `flag_` | Story flag | `flag_delivered_taeyang_cargo` |
| `contact_` | Contact | `contact_doc_rivas` |
| `glory_shop_` | Glory shop item | `glory_shop_extra_sp` |

---

## Event Schema (`data/mecha/events.json`)

```json
{
  "id": "evt_unique_id",
  "name": "Display Name",
  "speaker": "grandpa",
  "require": "g.some_flag>0",
  "seen": false,
  "desc": "The main narrative text shown to the player.",
  "result": {
    "reputation": 1,
    "title": "Optional title unlock"
  },
  "choices": [
    {
      "id": "choice_id",
      "label": "Short action label",
      "desc": "Longer explanation shown under the label.",
      "morality": 10,
      "effect": {
        "creds": 200,
        "rep_police": 15,
        "rep_corporate": -20
      },
      "flag": "flag_verb_noun",
      "log": "Short narrative log entry shown after choosing."
    }
  ],
  "repeatable": false
}
```

**Field notes:**
- `require`: Only fires once require is true. Omit for events that fire at game start.
- `seen`: Always `false` in data files; set to `true` at runtime after triggering.
- `result`: Optional. Applied when the event fires (no choice required).
- `choices`: Optional. If present, player must choose before proceeding.
- `choices[].morality`: Positive = Paragon direction, negative = Shadow direction. ±5 minor, ±10 moderate, ±20 significant.
- `choices[].effect`: Resource/rep changes applied on selection. See resource keys below.
- `choices[].flag`: Sets a persistent flag readable via `g.flag_name>0` in future requires.
- `choices[].log`: Terminal-style narrative entry confirming what happened.
- `repeatable`: Only include if `true` (defaults to false).

**Valid speaker values:**
`grandpa`, `kenji`, `system`, `ironjaw_enforcer`, `mira` (contact), `fen` (contact),
`contact_doc_rivas`, `contact_kohl`, or any contact ID.

---

## Mission Schema (`data/mecha/missions.json`)

### Minimal (combat/patrol):
```json
{
  "id": "msn_unique_id",
  "name": "Mission Name",
  "desc": "Player-facing description.",
  "flavor": "Atmospheric one-liner.",
  "group": "combat",
  "type": "mission",
  "missionType": "patrol",
  "difficulty": 2,
  "require": "g.level>=3",
  "cost": { "energy": 20 },
  "enemies": ["scrap_drone", "rogue_labor"],
  "turnLimit": 20,
  "rewards": {
    "glory": 3,
    "creds": 40,
    "scrap": 30
  },
  "firstClearBonus": {
    "glory": 3,
    "reputation": 1
  },
  "failRewards": {
    "glory": 1,
    "scrap": 10
  }
}
```

### Full (story mission):
```json
{
  "id": "msn_unique_id",
  "name": "Mission Name",
  "desc": "Player-facing description.",
  "flavor": "Atmospheric one-liner.",
  "group": "combat",
  "type": "mission",
  "missionType": "story",
  "phase": 4,
  "difficulty": 5,
  "require": "g.level>=6&&g.flag_something>0",
  "cost": { "energy": 30 },
  "enemies": ["enemy_taeyang_guard_mk2", "enemy_taeyang_enforcer"],
  "turnLimit": 30,
  "onComplete": { "event": "evt_follow_up_event" },
  "rewards": {
    "glory": 8,
    "creds": 120,
    "data_chips": 5,
    "flags": ["flag_verb_noun"]
  },
  "firstClearBonus": {
    "glory": 5,
    "reputation": 3
  },
  "failRewards": {
    "glory": 2,
    "creds": 20
  },
  "storyBeats": [
    {
      "trigger": "on_complete",
      "log": "Terminal log entry shown after mission resolves."
    }
  ],
  "debrief": [
    "Short debrief line 1.",
    "Short debrief line 2.",
    "Implication or thread to pull."
  ],
  "narrative": {
    "speaker": "kenji",
    "briefing_pages": [
      "Pre-mission dialogue line from speaker."
    ],
    "debriefing_victory": [
      "Victory debrief from speaker."
    ],
    "debriefing_defeat": [
      "Defeat debrief from speaker."
    ]
  },
  "intel": {
    "level1": {
      "cost": { "data_chips": 1 },
      "reveals": "Basic tactical info about enemy composition."
    },
    "level2": {
      "cost": { "data_chips": 3, "rep_exile": 10 },
      "reveals": "Deeper intel — a vulnerability, a secret objective, hidden context."
    }
  }
}
```

**missionType values:** `survey`, `patrol`, `secure`, `elimination`, `story`

**difficulty scale:** 1 (starter) → 3 (mid) → 5 (challenging) → 7+ (late game)

---

## Contact Schema (`data/mecha/contacts.json`)

```json
{
  "id": "contact_name",
  "name": "Display Name",
  "faction": "faction_underground",
  "specialty": "salvage",
  "desc": "Brief NPC bio. One or two sentences.",
  "loyalty": 0,
  "loyaltyMax": 10,
  "unlockRequire": "rep_police>=20",
  "benefit": {
    "threshold": 5,
    "effect": "Description of what the contact provides at loyalty 5"
  },
  "highLoyaltyBenefit": {
    "threshold": 8,
    "effect": "Enhanced benefit at loyalty 8"
  }
}
```

**faction values:** `none`, `faction_ntpd`, `faction_underground`, `faction_taeyang_syndicate`,
`faction_covenant`, `faction_ironjaw`, `faction_arena`

**specialty values (examples):** `repair`, `intel`, `salvage`, `combat`, `heat_reduction`,
`fabrication`, `negotiation`

---

## Glory Shop Schema (`data/mecha/glory_shop.json`)

```json
{
  "id": "glory_shop_unique_id",
  "name": "Upgrade Name",
  "desc": "What this permanently gives the player across all prestige cycles.",
  "cost_glory_pool": 75,
  "effect": "internal_effect_key",
  "max": 1,
  "owned": 0
}
```

**max**: How many times the player can buy this. 1 = one-time, 2–3 = stackable.
**owned**: Always 0 in data files; updated at runtime.

---

## Resource / Rep Keys

**Resources (usable in `effect`, `rewards`, `cost`):**
`creds`, `scrap`, `electronic_scrap`, `energy`, `data_chips`, `parts`, `xp`, `glory`,
`glory_pool`, `reputation`, `morality`, `street_cred`

**Faction rep keys:**
| Key | Faction |
|-----|---------|
| `rep_police` | NTPD |
| `rep_corporate` | Taeyang Syndicate |
| `rep_underground` | Underground |
| `rep_exile` | Covenant of the Exiled |
| `rep_ironjaw` | Ironjaw |
| `rep_arena` | Arena Circuit |

---

## Enemy Roster

| ID | Name | Notes |
|----|------|-------|
| `scrap_drone` | Scrap Drone | Early game, basic |
| `rogue_labor` | Rogue Labor | Early-mid |
| `security_unit` | Security Unit | Corporate |
| `rival_grunt` | Ironjaw Grunt | Ironjaw faction |
| `corrupted_sentinel` | Corrupted Sentinel | Mid game |
| `ironjaw_enforcer` | Ironjaw Enforcer | Mid game |
| `covenant_test_unit` | Covenant Test Unit | Covenant faction |
| `enemy_taeyang_drone` | Taeyang Surveillance Drone | Taeyang early |
| `enemy_taeyang_guard_mk1` | Taeyang Corp Security Unit | Taeyang mid |
| `enemy_taeyang_guard_mk2` | Taeyang Security MK.II | Taeyang late |
| `enemy_taeyang_enforcer` | Taeyang Enforcer Unit | Taeyang heavy |
| `enemy_bounty_hunter` | Mercenary Hunter | Hired |
| `enemy_rust_king_scout` | Rust King Scout | Rust King faction |
| `enemy_rust_king_fighter` | Rust King Fighter | Rust King faction |
| `enemy_rust_king_ambush` | Rust King Ambush Unit | Rust King faction |
| `enemy_rust_king_raider` | Rust King Raider | Rust King heavy |
| `enemy_arena_qualifier` | Arena Qualifier | Arena |
| `enemy_arena_contender` | Arena Contender | Arena |
| `nephilim_operator` | Nephilim Operator | Late/prestige |

---

## Require Expression Syntax

Requires are evaluated as expressions. Use `g.KEY` to reference game state:

```
g.level>=6                       Player pilot level
g.glory>=20                      Lifetime glory in this run
g.scrap>=100                     Current scrap on hand
g.street_cred>=30                Street credibility
g.morality>=40                   Alignment: Paragon
g.morality<=-40                  Alignment: Shadow
g.msn_mission_id>=1              Mission completed at least once
g.flag_verb_noun>0               Story flag set (from choice or reward)
g.garage>0                       Upgrade built (references upgrade ID)
g.rep_police>=25                 Faction rep threshold
```

Chain with `&&`: `g.level>=6&&g.flag_found_surveillance>0`
