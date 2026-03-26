---
name: "gsd-set-profile"
description: "Switch model profile for GSD agents (quality/balanced/budget)"
metadata:
  short-description: "Switch model profile for GSD agents (quality/balanced/budget)"
risk: safe
---

<codex_skill_adapter>
## A. Skill Invocation
- This skill is invoked by mentioning `$gsd-set-profile`.
- Treat all user text after `$gsd-set-profile` as `{{GSD_ARGS}}`.
- If no arguments are present, treat `{{GSD_ARGS}}` as empty.

## B. AskUserQuestion → request_user_input Mapping
GSD workflows use `AskUserQuestion` (Claude Code syntax). Translate to Codex `request_user_input`:

Parameter mapping:
- `header` → `header`
- `question` → `question`
- Options formatted as `"Label" — description` → `{label: "Label", description: "description"}`
- Generate `id` from header: lowercase, replace spaces with underscores

Batched calls:
- `AskUserQuestion([q1, q2])` → single `request_user_input` with multiple entries in `questions[]`

Multi-select workaround:
- Codex has no `multiSelect`. Use sequential single-selects, or present a numbered freeform list asking the user to enter comma-separated numbers.

Execute mode fallback:
- When `request_user_input` is rejected (Execute mode), present a plain-text numbered list and pick a reasonable default.

## C. Task() → spawn_agent Mapping
GSD workflows use `Task(...)` (Claude Code syntax). Translate to Codex collaboration tools:

Direct mapping:
- `Task(subagent_type="X", prompt="Y")` → `spawn_agent(agent_type="X", message="Y")`
- `Task(model="...")` → omit (Codex uses per-role config, not inline model selection)
- `fork_context: false` by default — GSD agents load their own context via `<files_to_read>` blocks

Parallel fan-out:
- Spawn multiple agents → collect agent IDs → `wait(ids)` for all to complete

Result parsing:
- Look for structured markers in agent output: `CHECKPOINT`, `PLAN COMPLETE`, `SUMMARY`, etc.
- `close_agent(id)` after collecting results from each agent
</codex_skill_adapter>

<objective>
Switch the model profile used by GSD agents. Controls which Claude model each agent uses, balancing quality vs token spend.

Routes to the set-profile workflow which handles:
- Argument validation (quality/balanced/budget)
- Config file creation if missing
- Profile update in config.json
- Confirmation with model table display
</objective>

<execution_context>
@C:/Users/nicol/.codex/get-shit-done/workflows/set-profile.md
</execution_context>

<process>
**Follow the set-profile workflow** from `@C:/Users/nicol/.codex/get-shit-done/workflows/set-profile.md`.

The workflow handles all logic including:
1. Profile argument validation
2. Config file ensuring
3. Config reading and updating
4. Model table generation from MODEL_PROFILES
5. Confirmation display
</process>
