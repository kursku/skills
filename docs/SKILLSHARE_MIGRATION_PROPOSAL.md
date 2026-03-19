# Skillshare Folder Migration Plan (Applied)

This proposal maps every current top-level skill folder to a target organization model for easier browsing, ownership, and maintenance.

Scope:
- Mapping and rollout guidance.
- Folder moves have been applied in the current branch.

## Target Model

```text
.skillshare/skills/
  core/
  frontend/
  backend/
  data-ai/
  security/
  workflow/
  tooling/
  _experimental/
```

## Full Mapping (Current -> Proposed Group)

### core
- internal-comms

### frontend
- adapt
- animate
- audit
- baseline-ui
- bolder
- brand-guidelines
- clarify
- colorize
- composition-patterns
- critique
- delight
- develop-web-game
- distill
- extract
- fixing-accessibility
- fixing-metadata
- fixing-motion-performance
- harden
- normalize
- onboard
- optimize
- polish
- quieter
- react-native-skills
- remotion
- teach-impeccable

### backend
- luau-roblox
- supabase-postgres-best-practices

### data-ai
- advanced-evaluation
- bdi-mental-states
- hosted-agents
- project-development

### security
- (no dedicated top-level security skills currently)

### workflow
- gsd-add-phase
- gsd-add-tests
- gsd-add-todo
- gsd-audit-milestone
- gsd-check-todos
- gsd-cleanup
- gsd-complete-milestone
- gsd-debug
- gsd-discuss-phase
- gsd-execute-phase
- gsd-health
- gsd-help
- gsd-insert-phase
- gsd-join-discord
- gsd-list-phase-assumptions
- gsd-map-codebase
- gsd-new-milestone
- gsd-new-project
- gsd-pause-work
- gsd-plan-milestone-gaps
- gsd-plan-phase
- gsd-progress
- gsd-quick
- gsd-reapply-patches
- gsd-remove-phase
- gsd-research-phase
- gsd-resume-work
- gsd-set-profile
- gsd-settings
- gsd-update
- gsd-validate-phase
- gsd-verify-work

### tooling
- claude-ask
- codex-ask
- defuddle
- filesystem-context
- gemini-ask
- json-canvas
- kimi-ask
- obsidian-bases
- obsidian-cli
- obsidian-markdown
- skillshare

### _experimental
- template

## Why This Mapping

- Keeps daily UX/design workflow skills in one place (`frontend/`).
- Isolates orchestration-heavy commands (`workflow/`) for power users.
- Separates platform/tool bridge skills (`tooling/`) from domain skills.
- Reserves `_experimental/` as a safe pre-promotion lane.

## Rollout Plan

1. Approve mapping as-is or edit exceptions.
2. Move folders in one branch using `git mv`.
3. Run checker and regenerate index:

```powershell
./scripts/skillshare_repo_check.ps1 -WriteIndex -Strict
```

4. Update docs references that point to old paths.
5. Run target sync validation in a test project:

```bash
skillshare install github.com/sickn33/antigravity-awesome-skills --track -p --all
skillshare sync -p
skillshare diff -p --no-tui
```

## Move Safety Rules

- Keep skill folder names unchanged; only move parent path.
- Do not change SKILL frontmatter `name` during the move.
- Move in one atomic PR to avoid partial path drift.
- Keep `template` isolated until promoted.

## Optional Second-Pass Improvements

- Add ownership metadata per group in docs.
- Split `frontend/` into `frontend/design` and `frontend/perf` only if count exceeds maintainable size.
- Add CI check to fail when new top-level folders are created outside approved groups.
