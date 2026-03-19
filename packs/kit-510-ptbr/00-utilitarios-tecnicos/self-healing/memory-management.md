# Memory Management Reference

## Memory Architecture

```
~/.claude/projects/<encoded-project-path>/memory/
├── MEMORY.md              # Index file (first 200 lines auto-loaded)
├── patterns.md            # Discovered code patterns
├── debugging.md           # Debugging strategies that worked
├── architecture.md        # Architecture decisions and rationale
├── conventions.md         # Codebase conventions discovered
├── tooling.md             # Build tools, scripts, CLI commands
├── external-resources.md  # Useful URLs, docs, references
└── [topic].md             # Any other topic-specific file
```

### How Memory Loading Works

1. **Session start**: MEMORY.md lines 1–200 are injected into context automatically
2. **Topic files**: Never auto-loaded. Claude must explicitly Read them when needed
3. **Cross-session**: All memory persists across conversations in the same project
4. **Cross-worktree**: Memory is shared across git worktrees of the same repo

### The 200-Line Budget

MEMORY.md has a hard constraint: only the first 200 lines load. Use them wisely:

**Good MEMORY.md structure:**
```markdown
# Project Memory

## Quick Reference
- Build: `npm run build` (takes ~45s)
- Test: `npm test -- --watch`
- Deploy: `npm run deploy:staging`
- DB: PostgreSQL 15, Redis 7

## Tech Stack
Next.js 14 (App Router), TypeScript, Prisma, TailwindCSS

## Key Patterns
See patterns.md for discovered code patterns
See conventions.md for codebase conventions

## Architecture Decisions
See architecture.md for ADRs and rationale

## Debugging
See debugging.md for strategies that worked

## Known Gotchas
- Auth middleware runs before API routes, not after
- Redis connection pool max is 10 in dev, 50 in prod
- Image uploads must go through /api/upload, not direct S3

## Recent Learnings
- [topic]: brief summary (see [file].md for details)
```

**Anti-patterns:**
- Chronological entries ("March 5: did X, March 6: did Y")
- Entire code blocks in MEMORY.md (put in topic files)
- Duplicate entries scattered across the file
- Entries longer than 2 lines (summarize, link to topic file)

## When to Write Memory

### Always Save
- **User corrections**: When the user says "actually, it should be X" — save immediately
- **Non-obvious discoveries**: Things that took real effort to figure out
- **Environment specifics**: Build commands, deploy steps, required env vars
- **Recurring gotchas**: Traps you or the user fell into
- **Architecture decisions**: Why things are the way they are (not just what)

### Sometimes Save
- **Useful patterns**: Only if they're project-specific (not general knowledge)
- **External resources**: URLs to docs/guides that were actually helpful
- **User preferences**: Workflow preferences the user explicitly stated

### Never Save
- **Session-specific state**: What you're currently working on
- **Speculative conclusions**: Unverified assumptions from reading one file
- **General knowledge**: Things any developer would know
- **Secrets or credentials**: API keys, tokens, passwords — never persist these
- **Information in CLAUDE.md**: Don't duplicate what's already there

## Memory Hygiene Operations

### Audit (run periodically)
1. Read MEMORY.md — is everything still accurate?
2. Check each topic file — is anything outdated?
3. Look for duplicates across files
4. Verify links from MEMORY.md to topic files are valid
5. Check line count — is MEMORY.md under 200 lines?

### Prune
- Remove entries about code that no longer exists
- Delete topic files with no remaining valid entries
- Consolidate overlapping topic files
- Remove "learned on [date]" prefixes — dates aren't useful for reference

### Reorganize
- Move misplaced entries to the correct topic file
- Update MEMORY.md index when topic files change
- Merge small topic files (under 10 lines) into MEMORY.md directly
- Split large topic files (over 200 lines) into subtopics

## Memory Update Workflow

```
1. Read MEMORY.md
2. Read relevant topic file (if it exists)
3. Decide: update existing entry, add new entry, or create new topic file
4. Make the edit (use Edit tool, not Write, for existing files)
5. If topic file changed, verify MEMORY.md index still references it
6. If MEMORY.md changed, verify it's under 200 lines
```

## Topic File Template

```markdown
# [Topic Name]

## [Subtopic]
- Key point with context
- Another point
  - Supporting detail if needed

## [Another Subtopic]
- Entries organized by relevance, not chronology
```

Keep topic files focused. If a file covers too many unrelated things, split it.
