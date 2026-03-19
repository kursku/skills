# Skill System Reference

## Frontmatter Fields

All fields are specified in YAML frontmatter at the top of `SKILL.md`.

### Required Fields

| Field | Type | Description |
|-------|------|-------------|
| `name` | string | Kebab-case identifier. Becomes the `/slash-command`. Must match directory name. |
| `description` | string | What the skill does. Claude uses this for auto-activation matching. Include action verbs and trigger phrases. |

### Optional Fields

| Field | Type | Default | Description |
|-------|------|---------|-------------|
| `argument-hint` | string | — | Shown in autocomplete after the command name. Use `[brackets]` for placeholders. |
| `user-invocable` | boolean | `true` | If `false`, skill cannot be called via `/command`. Only auto-activates. |
| `auto-activate` | boolean | `true` | If `false`, skill only runs when explicitly invoked via `/command`. |
| `allowed-tools` | string[] | all | Whitelist of tools the skill can use. Restricts to only these tools. |
| `disallowed-tools` | string[] | none | Blacklist of tools. Skill can use everything except these. |

### Invocation Control Matrix

| `user-invocable` | `auto-activate` | Behavior |
|-------------------|-----------------|----------|
| `true` (default) | `true` (default) | Full access: slash command + auto-activates |
| `true` | `false` | Slash command only, never auto-activates |
| `false` | `true` | Auto-activate only, no slash command |
| `false` | `false` | Never runs (useless — avoid this) |

### Tool Restriction Examples

```yaml
# Only allow reading and searching — no edits
allowed-tools:
  - Read
  - Glob
  - Grep
  - Agent

# Allow everything except destructive tools
disallowed-tools:
  - Bash
  - Write
  - Edit
```

## Variables

Variables are replaced at invocation time before Claude sees the content.

| Variable | Description | Available in |
|----------|-------------|-------------|
| `$ARGUMENTS` | Everything the user typed after `/command`. Empty string if no arguments. | SKILL.md |
| `$0` | Alias for `$ARGUMENTS` | SKILL.md |
| `${CLAUDE_SKILL_DIR}` | Absolute path to the skill's directory. Use for referencing supporting files. | SKILL.md |
| `${CLAUDE_SESSION_ID}` | Unique ID for the current Claude Code session. | SKILL.md |

### Variable Usage

```markdown
# In SKILL.md

The user wants: $ARGUMENTS

Read `${CLAUDE_SKILL_DIR}/reference.md` for details.

Session: ${CLAUDE_SESSION_ID}
```

**Important**: `$ARGUMENTS` and `$0` are the same. Use `$ARGUMENTS` for clarity.

## Shell Injection

Embed live command output in SKILL.md using `!`backtick` ` syntax:

```markdown
Current branch: !`git branch --show-current`
Node version: !`node --version`
Changed files: !`git diff main --name-only`
```

**How it works:**
- Commands execute when the skill is activated (not at definition time)
- Output replaces the `!`command`` inline
- If the command fails, the error output is included instead
- Commands run in the current working directory

**Use cases:**
- Inject project state (git branch, recent commits, env vars)
- Generate dynamic context (file lists, config values)
- Pre-compute information Claude needs

**Caution:**
- Commands run with the user's permissions
- Keep commands fast — slow commands delay skill activation
- Don't use for side effects (the skill content is for context, not execution)

## File Structure

```
skills/
└── my-skill/
    ├── SKILL.md          # Required — main instructions (loaded on activation)
    ├── reference.md      # Optional — detailed reference (read on-demand)
    ├── examples.md       # Optional — code examples (read on-demand)
    └── scripts/          # Optional — bundled scripts
        └── check.sh
```

### Loading Behavior

- **SKILL.md**: Loaded into context when the skill activates (via slash command or auto-activation)
- **Supporting `.md` files**: NOT automatically loaded. Only read when SKILL.md tells Claude to read them via `${CLAUDE_SKILL_DIR}` references
- **Scripts/other files**: Available on disk but never auto-loaded. Referenced via `${CLAUDE_SKILL_DIR}`

This means:
- Keep SKILL.md focused — it's always loaded
- Put detailed references in separate files — they're only loaded when needed
- Supporting files don't cost context tokens unless explicitly read

## Permissions

Skills inherit the user's permission settings. A skill cannot bypass permission restrictions.

- If the user has `Bash` set to "ask", the skill will still prompt for Bash usage
- `allowed-tools` in frontmatter further restricts (intersects with) user permissions
- `disallowed-tools` adds restrictions on top of user permissions

## Skill Resolution

When multiple skills could match:
1. Exact slash command match takes priority
2. For auto-activation, Claude evaluates all skill descriptions against the user's message
3. Multiple skills can auto-activate simultaneously if relevant
4. Project skills (`.claude/skills/`) and personal skills (`~/.claude/skills/`) are both searched

## Naming Conventions

- **Directory name**: kebab-case, matches `name` field exactly
- **SKILL.md**: Always uppercase `SKILL.md`
- **Supporting files**: lowercase kebab-case `.md` files
- **Scripts**: lowercase, appropriate extension (`.sh`, `.py`, `.ts`)
