# Skill Creation Guide (for Self-Healing)

## When to Create a Skill

A skill should be created when ALL of these are true:

1. **Repeated pattern**: The workflow has appeared 2+ times (or is clearly reusable)
2. **Non-trivial**: It involves multiple steps, decisions, or specialized knowledge
3. **Stable**: The pattern is unlikely to change significantly soon
4. **Not already covered**: No existing skill handles this workflow

**Do NOT create a skill for:**
- One-off tasks (save to memory instead)
- Simple commands (document in CLAUDE.md or memory)
- General programming knowledge (Claude already knows this)
- Unstable/experimental workflows (wait until they stabilize)

## Skill Creation Checklist

### 1. Choose the Type

| Type | When | Example |
|------|------|---------|
| **Task** | Performs actions, has side effects | deploy, migrate, publish |
| **Knowledge** | Provides reference context | api-patterns, style-guide |
| **Dynamic** | Injects live project state | pr-summary, env-check |
| **Research** | Gathers and synthesizes information | deep-dive, audit |

### 2. Determine Scope

- **Project** (`.claude/skills/`) — Default. Use when the pattern is project-specific
- **Personal** (`~/.claude/skills/`) — Use when the pattern applies across all projects

### 3. Write the Frontmatter

```yaml
---
name: kebab-case-name          # Must match directory name
description: Action-oriented description with trigger phrases...
argument-hint: [what the user provides]
# Only add these when needed:
# auto-activate: false         # For dangerous operations
# user-invocable: false        # For pure knowledge skills
# allowed-tools: [Read, Grep]  # For read-only skills
---
```

**Description quality matters most.** Claude uses it for auto-activation. Include:
- What the skill does (action verbs)
- When to use it (trigger phrases)
- Keywords users might say

### 4. Structure the SKILL.md

```markdown
---
[frontmatter]
---

# Title

One-sentence role statement.

Reference to supporting files (if any):
Read `${CLAUDE_SKILL_DIR}/reference.md` for details.

## Core Instructions
[Main guidance — specific and actionable]

## Critical Rules
[Numbered list, max 10-12]

## Quick Templates
[Minimal, copy-paste-ready patterns]

Final note about $ARGUMENTS usage.
```

### 5. Add Supporting Files (if needed)

Create separate `.md` files when:
- Content exceeds ~50 lines
- Reference material is only needed on-demand
- Multiple code examples would bloat SKILL.md

Reference them with `${CLAUDE_SKILL_DIR}`:
```markdown
Read `${CLAUDE_SKILL_DIR}/api-patterns.md` for the complete reference.
```

### 6. Verify

- [ ] SKILL.md is under 300 lines
- [ ] Directory name matches `name` field
- [ ] Description includes trigger phrases
- [ ] Supporting files use `${CLAUDE_SKILL_DIR}` references
- [ ] No hardcoded paths
- [ ] `$ARGUMENTS` is referenced for user input
- [ ] Templates are minimal (pattern, not full app)

## Skill from Pattern — Decision Flow

```
Noticed a pattern?
  ↓
Has it appeared 2+ times? ──No──→ Save to memory instead
  ↓ Yes
Is it non-trivial (3+ steps)? ──No──→ Add to CLAUDE.md or memory
  ↓ Yes
Is it project-specific? ──No──→ Create in ~/.claude/skills/
  ↓ Yes
Create in .claude/skills/
```

## Common Skill Patterns Worth Creating

- **Error handling workflows**: Project-specific debugging sequences
- **Code generation templates**: Repeated boilerplate with conventions
- **Review checklists**: PR review, security audit, performance review
- **Migration workflows**: Database, API version, framework upgrades
- **Testing patterns**: Project-specific test structure and utilities
- **Integration patterns**: How this project connects to external services

## Naming Conventions

- **Directories**: `kebab-case` (e.g., `api-generator`)
- **SKILL.md**: Always uppercase
- **Supporting files**: `lowercase-kebab.md` (e.g., `api-patterns.md`)
- **Scripts**: lowercase with extension (e.g., `validate.sh`)
