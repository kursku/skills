---
name: luau-roblox
description: Luau and Roblox development patterns for strict typing, Roblox service architecture, client/server security, DataStore persistence, RemoteEvent design, and incremental game systems.
triggers:
  - luau
  - roblox
  - roblox studio
  - remoteevent
  - datastoreservice
  - task.wait
  - strict mode
  - rojo
  - incremental game
type: general
risk: offensive
---

# Luau / Roblox Development Skill

Applies to any work inside a Roblox game project written in Luau. Covers correct patterns
for strict typing, service architecture, security, persistence, and game-loop design.

---

## 1. Mandatory File Header

Every `.lua` / `.luau` file **must** start with:

```luau
--!strict
```

No exceptions. This enables Luau's full type-checker and prevents entire classes of runtime
errors. Never omit it, never suppress it with `--!nonstrict`.

---

## 2. Service Acquisition

Always use `game:GetService()` at the **top of the file**, before any logic.
Never access services through `game.ServiceName` (breaks in some load orders).

```luau
--!strict
local Players       = game:GetService("Players")
local RunService    = game:GetService("RunService")
local DataStoreService = game:GetService("DataStoreService")
local ReplicatedStorage = game:GetService("ReplicatedStorage")
```

---

## 3. Module Pattern

Every service / controller / module exports a single table named identically to the file.
Always export an `init()` function for one-time setup called from the bootstrap script.

```luau
--!strict
local MyService = {}

-- Called once by the bootstrap (init.server.luau / init.client.luau)
function MyService.init()
    -- setup, bind events, start loops
end

-- Public API
function MyService.doThing(player: Player, value: number): boolean
    -- logic
    return true
end

return MyService
```

Rules:
- Module table: **PascalCase** matching the filename (`EconomyService`, `HUDController`)
- Functions: **camelCase** (`awardKnowledge`, `tryLevelUp`)
- Constants: **SCREAMING_SNAKE_CASE** (`local MAX_ENERGY = 100`)
- Roblox service refs: **PascalCase** (`local Players = ...`)
- Types: **PascalCase** (`type PlayerData = {...}`)

---

## 4. `task.*` API — Never Use Deprecated Alternatives

| Deprecated | Correct replacement |
|---|---|
| `wait(n)` | `task.wait(n)` |
| `spawn(fn)` | `task.spawn(fn)` |
| `delay(n, fn)` | `task.delay(n, fn)` |
| `coroutine.wrap(fn)()` | `task.spawn(fn)` |

`wait()` is deprecated, inaccurate on frame boundaries, and will be removed.
`task.*` is the only correct async primitive in modern Luau.

Server tick loop example:
```luau
task.spawn(function()
    while true do
        task.wait(1)
        MyService.tick()
    end
end)
```

---

## 5. Client / Server Architecture

| Container | Script type | Runs on |
|---|---|---|
| `ServerScriptService` | `Script` | Server only |
| `StarterPlayerScripts` | `LocalScript` | Client only |
| `ReplicatedStorage` | `ModuleScript` | Both (shared) |

**The server is always authoritative.** The client:
- Displays UI and shows state
- Fires RemoteEvents to *request* actions
- Never computes economic values — the server does that

Never expose a `RemoteFunction` from client to server (blocks the thread and is exploitable).
Use `RemoteEvent` only. The server fires back data via a separate event if needed.

---

## 6. RemoteEvent Security

Roblox exploiters can fire any RemoteEvent with arbitrary arguments at any time.

### Never trust client-provided amounts

```luau
-- BAD — exploitable
remoteEvent.OnServerEvent:Connect(function(player, upgradeId, cost)
    playerData.knowledge -= cost
end)

-- GOOD — server looks up the real cost
remoteEvent.OnServerEvent:Connect(function(player, upgradeId)
    local config = UpgradeConfig[upgradeId]
    if not config then return end
    local data = DataService.getPlayerData(player)
    if not data or data.knowledge < config.cost then return end
    data.knowledge -= config.cost
    -- apply effect
end)
```

### Validate all arguments

```luau
local function onBuyUpgrade(player: Player, upgradeId: unknown)
    -- type check
    if type(upgradeId) ~= "string" then return end
    -- membership check
    if not UpgradeConfig[upgradeId] then return end
    -- data check
    local data = DataService.getPlayerData(player)
    if not data then return end
    -- economy check
    if data.knowledge < UpgradeConfig[upgradeId].cost then return end
    -- safe to proceed
end
```

### Rate-limit all remotes

```luau
local lastFire: {[Player]: number} = {}
local DEBOUNCE = 0.5  -- seconds

remoteEvent.OnServerEvent:Connect(function(player: Player, ...)
    local now = os.clock()
    if lastFire[player] and (now - lastFire[player]) < DEBOUNCE then return end
    lastFire[player] = now
    -- proceed
end)

-- Clean up on player leave to avoid memory leaks
game:GetService("Players").PlayerRemoving:Connect(function(player)
    lastFire[player] = nil
end)
```

---

## 7. DataStore Patterns

Always wrap DataStore calls in `pcall`. Always log failures with a consistent prefix.

```luau
local function saveData(player: Player, data: PlayerData)
    local key = "player_" .. player.UserId
    local ok, err = pcall(function()
        dataStore:SetAsync(key, data)
    end)
    if not ok then
        warn("[DataService] SetAsync failed for " .. key .. ": " .. tostring(err))
    end
end
```

### Merge saved data onto a known default

Never trust that a saved record has all fields (new fields added after initial save, corrupted
data, etc.). Always merge onto the default template:

```luau
local function mergeWithDefault(saved: {[string]: unknown}, default: PlayerData): PlayerData
    local result = table.clone(default)
    for key, value in saved do
        if result[key] ~= nil and type(value) == type(result[key]) then
            result[key] = value
        end
    end
    return result
end
```

### Save cadence
- Auto-save every **30 seconds** via a `task.spawn` loop
- Always save on `Players.PlayerRemoving` — use `task.defer` to ensure it fires:

```luau
Players.PlayerRemoving:Connect(function(player)
    saveData(player, DataService.getPlayerData(player))
end)
```

---

## 8. Type Definitions (`Types.lua`)

Define all shared data shapes in `src/shared/Types.lua`. Import them in every file that uses them.

```luau
--!strict
export type PlayerData = {
    knowledge: number,
    energy: number,
    diplomas: number,
    mathLevel: number,
    scienceLevel: number,
    historyLevel: number,
    peLevel: number,
    totalKnowledgeEarned: number,
}

export type UpgradeConfig = {
    id: string,
    displayName: string,
    baseCost: number,
    growth: number,
    bonusPerLevel: number,
}
```

Always annotate function parameters and return types explicitly — never rely on inference
when the function is part of a public API.

---

## 9. Config Over Magic Numbers

All gameplay numbers live in config files under `src/shared/config/`. Never hardcode values
in service logic.

```luau
-- BAD
local cost = 25 * (1.25 ^ level)

-- GOOD
local cfg = SubjectsConfig[subjectId]
local cost = cfg.baseCost * (cfg.growth ^ level)
```

Upgrade cost formula: `cost = baseCost * (growth ^ level)`

---

## 10. Error Handling

Use `pcall` around any throwable operation. Log with the format `[ServiceName] message`.

```luau
local ok, result = pcall(function()
    return dataStore:GetAsync(key)
end)
if not ok then
    warn("[DataService] GetAsync failed: " .. tostring(result))
    return nil
end
```

---

## 11. No Globals

Never write to `_G` or `shared`. Pass dependencies as arguments or module-level locals
set during `init()`. This keeps modules testable and avoids order-of-require issues.

---

## 12. File Length

Keep files under **300 lines**. If a service grows past that, extract a sub-module.
Example: `StudyService` grows large → extract `StudyCalculator` as a pure-function module.

---

## 13. Incremental Game Patterns (School_Incremental Specific)

### Economy tick (1 second cadence)

```luau
-- In EconomyService.init()
task.spawn(function()
    while true do
        task.wait(1)
        for _, player in Players:GetPlayers() do
            EconomyService.tick(player)
        end
    end
end)
```

### Knowledge gain calculation

Knowledge per study = `BaseStudyGain * knowledgeMultiplier`

where `knowledgeMultiplier` accumulates from Subject levels:
`multiplier += mathLevel * MathConfig.bonusPerLevel`

### Prestige formula

`diplomas = math.floor(totalKnowledgeEarned / PrestigeConfig.baseCost)`

### Boss reward delivery

Boss rewards are rare currencies. Deliver via `EconomyService.awardCurrency`, not by
direct attribute write, so all validation and logging stays in one place.

### Subject upgrade cost

`cost = subject.baseCost * (subject.growth ^ currentLevel)`

Computed in `UpgradeCalculator.lua` — never inline this formula in UI or service code.

---

## 14. Remotes Naming Convention

All RemoteEvents and RemoteFunctions live in `src/shared/Remotes.lua`.
Name them **PascalCase verb-noun**: `RequestStudy`, `BuyUpgrade`, `RequestPrestige`, `BossDefeated`.

```luau
-- Remotes.lua
--!strict
local ReplicatedStorage = game:GetService("ReplicatedStorage")
local Remotes = ReplicatedStorage:WaitForChild("Remotes")

return {
    RequestStudy    = Remotes:WaitForChild("RequestStudy") :: RemoteEvent,
    BuyUpgrade      = Remotes:WaitForChild("BuyUpgrade")  :: RemoteEvent,
    RequestPrestige = Remotes:WaitForChild("RequestPrestige") :: RemoteEvent,
    SyncPlayerData  = Remotes:WaitForChild("SyncPlayerData")  :: RemoteEvent,
}
```

---

## Quick Reference

```
Strict mode:           --!strict  (every file, no exceptions)
Async:                 task.wait / task.spawn / task.delay  (never wait/spawn/delay)
Services:              game:GetService()  (never game.ServiceName)
Module table:          PascalCase, one per file
Functions:             camelCase
Constants:             SCREAMING_SNAKE_CASE
Remotes:               PascalCase verb-noun, all in Remotes.lua
Security:              validate type + membership + economy on every OnServerEvent
Rate limit:            0.5s debounce per player per remote
DataStore:             always pcall, always merge onto default template
Save cadence:          30s auto + PlayerRemoving
File length:           max 300 lines
Magic numbers:         forbidden — use config files
Upgrade cost formula:  baseCost * (growth ^ level)
Prestige formula:      floor(totalKnowledgeEarned / baseCost)
Economy tick:          1 second server loop
```
