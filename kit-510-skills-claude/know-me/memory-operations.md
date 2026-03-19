# Memory Operations — How to Store, Organize, Update & Recall

## Memory Architecture

```
~/.claude/projects/<project-path>/memory/
├── MEMORY.md              ← Auto-loaded (first 200 lines). Index + key facts.
├── user-preferences.md    ← Dev tools, code style, framework choices
├── project-context.md     ← What they're building, business context
├── tech-stack.md          ← Languages, frameworks, versions, infrastructure
├── communication-style.md ← How they want Claude to interact
└── corrections.md         ← Mistakes Claude made — never repeat these
```

### MEMORY.md Rules
- First 200 lines are auto-loaded into every conversation
- Keep it as an index: short summaries + pointers to topic files
- Don't put detailed info here — put it in topic files
- Budget: ~20 lines per section, max 6-8 sections

### Topic File Rules
- Lazy-loaded (only read when relevant)
- No line limit, but keep organized
- Group by category with `###` headers
- Include date/context for each entry

---

## Saving Operations

### Save a New Preference
```
1. Check MEMORY.md — does a relevant section exist?
2. If yes → Read the linked topic file → Add entry
3. If no → Create section in MEMORY.md + create/update topic file
4. Verify: Re-read the file to confirm it saved correctly
```

**MEMORY.md entry format:**
```markdown
## User Preferences
- Uses bun, Tailwind, Vitest — see `user-preferences.md`
```

**Topic file entry format:**
```markdown
### Package Manager: bun
- **Observed:** 2026-03-10
- **Context:** User said "I always use bun"
- **Detail:** Use bun for all package management. Use `bun install`, `bun run`, `bunx`.
```

### Save a Correction
```
1. Read corrections.md (or create it)
2. Add the correction entry
3. Find and UPDATE any conflicting memory in other files
4. Update MEMORY.md if the correction affects a summary line
```

**Correction entry format:**
```markdown
### Correction: Don't add JSDoc to unchanged functions
- **Date:** 2026-03-10
- **Wrong assumption:** Claude added JSDoc comments to existing functions while editing nearby code
- **Correct behavior:** Only modify code that's directly related to the task. Never add comments, types, or docs to unchanged code.
- **Category:** code-style
```

### Save Project Context
```
1. Read project-context.md (or create it)
2. Add/update the project entry
3. Update MEMORY.md summary line
```

**Project entry format:**
```markdown
### Project: [Name]
- **Type:** B2B SaaS for dental practices
- **Stage:** MVP, launching Q2 2026
- **Stack:** Next.js, Supabase, Tailwind, Vercel
- **Team:** Solo founder + 1 contractor
- **Key constraints:** Bootstrap budget, need to ship fast
```

---

## Updating Operations

### When to Update (Not Create New)
- User corrects a previously saved preference
- A preference changes ("actually, switching to pnpm")
- Project context evolves (MVP → growth stage)
- A saved entry turns out to be wrong

### Update Process
```
1. Read the topic file containing the outdated entry
2. Use Edit tool to replace the old entry with the new one
3. If MEMORY.md summary is affected, update that too
4. Do NOT keep the old entry — replace it cleanly
```

### When to Delete
- User says "forget X" or "don't remember that"
- Information is clearly outdated and no longer relevant
- A correction makes a previous entry completely wrong
- Duplicate entries discovered

---

## Recall Operations

### Before Starting Any Task
Quick mental checklist:
1. MEMORY.md is auto-loaded — scan it for relevant preferences
2. If task involves code: Do I know their style preferences?
3. If task involves architecture: Do I know their stack and constraints?
4. If task involves communication: Do I know their preferred style?

### Deep Recall (When Needed)
```
1. Read the relevant topic file before making decisions
2. Example: Before suggesting a testing approach → read user-preferences.md
3. Example: Before choosing a library → read tech-stack.md
4. Example: Before writing a long explanation → read communication-style.md
```

### Applying Recalled Knowledge
- **Do:** Silently apply preferences (use bun without asking)
- **Don't:** Announce that you're using stored preferences ("Based on my memory of your preferences...")
- **Do:** Reference context naturally ("Since this is a dental SaaS, HIPAA compliance matters here")
- **Don't:** Quiz the user on stored info ("I remember you use Tailwind, is that still true?")

---

## MEMORY.md Template

```markdown
# Project Memory

## User Preferences
- [Package manager], [framework], [testing tool] — see `user-preferences.md`
- Communication: [concise/detailed], [casual/formal] — see `communication-style.md`

## Current Project
- [One-line description] — see `project-context.md`
- Stack: [key technologies] — see `tech-stack.md`

## Important Corrections
- [Most critical correction] — see `corrections.md`
- [Second most critical]

## Key Patterns
- [Any recurring workflow or habit worth noting]
```

---

## Conflict Resolution

When new information conflicts with stored memory:

| Scenario | Action |
|----------|--------|
| User explicitly corrects | Update immediately, no questions |
| User implies different preference | Ask once: "I noticed you're using X — should I default to that?" |
| User's action contradicts stored pref | Don't ask — might be one-off. Note if it happens again. |
| Two memories conflict with each other | Read both, keep the more recent one |

---

## Hygiene — Periodic Maintenance

### When to Audit Memory
- Start of a new project (old project context may be stale)
- User mentions something that contradicts stored memory
- MEMORY.md approaching 200-line limit

### Audit Steps
1. Read MEMORY.md — is everything still accurate?
2. Check each topic file — remove outdated entries
3. Consolidate duplicates
4. Verify topic file links in MEMORY.md still point to real files

### MEMORY.md Space Management
If approaching 200 lines:
1. Move detailed entries to topic files (keep only summaries)
2. Remove entries for completed/abandoned projects
3. Merge similar entries
4. Delete anything that's now in CLAUDE.md (no duplication)

---

## Anti-Patterns

| Don't Do This | Do This Instead |
|---------------|-----------------|
| Save every detail from every session | Save stable patterns confirmed across interactions |
| Save speculative conclusions | Verify before writing to memory |
| Duplicate info that's in CLAUDE.md | Reference CLAUDE.md, don't copy it |
| Save temporary task state | Only save durable preferences |
| Announce every memory save | Save quietly unless it's a correction acknowledgment |
| Save without reading existing memory first | Always check for duplicates/conflicts before writing |
| Store sensitive data (keys, passwords) | Never store credentials or secrets |
| Ignore corrections | Corrections are highest-priority saves |
