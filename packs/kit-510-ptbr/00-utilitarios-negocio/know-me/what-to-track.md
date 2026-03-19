# What to Track — User Knowledge Categories

## 1. Development Preferences

### Tools & Runtime
- Package manager (npm, yarn, pnpm, bun)
- Runtime (Node.js, Deno, Bun)
- Editor/IDE (VS Code, Neovim, Cursor, etc.)
- Terminal (iTerm2, Warp, built-in)
- OS and platform details

### Code Style
- Formatting (tabs vs spaces, indent size, semicolons)
- Naming conventions (camelCase, snake_case, kebab-case)
- File organization preferences
- Comment style (minimal, verbose, JSDoc)
- Import ordering preferences
- Preferred patterns (functional vs OOP, composition vs inheritance)

### Frameworks & Libraries
- Frontend framework (React, Vue, Svelte, etc.)
- CSS approach (Tailwind, CSS modules, styled-components)
- Backend framework (Express, Fastify, Hono, etc.)
- ORM (Prisma, Drizzle, TypeORM)
- Testing (Vitest, Jest, Playwright)
- Any strong preferences for or against specific libraries

### Language Preferences
- Primary languages (TypeScript, Python, Go, etc.)
- TypeScript strictness preferences
- Type annotation habits (explicit vs inferred)
- Error handling style (try/catch, Result types, etc.)

---

## 2. Communication Style

### How They Want Responses
- Concise vs detailed explanations
- Show code first vs explain first
- Emoji usage (yes/no)
- Formal vs casual tone
- How much context they want before changes

### What Frustrates Them
- Over-explaining obvious things
- Asking too many clarifying questions
- Being too cautious / not autonomous enough
- Being too aggressive with changes
- Adding unnecessary comments or docs
- Not reading files before suggesting changes

### Teaching Preferences
- Learn by reading code vs reading explanations
- Want to understand "why" or just "how"
- Prefer inline comments or separate explanations

---

## 3. Project Context

### Current Projects
- Project name and purpose
- Target audience / customers
- Stage (prototype, MVP, growth, enterprise)
- Team size and structure
- Deployment targets (Vercel, AWS, self-hosted)

### Business Context
- Industry / domain
- Revenue model (SaaS, marketplace, etc.)
- Key constraints (budget, timeline, compliance)
- Competitors or inspirations mentioned

### Architecture Decisions
- Monolith vs microservices
- Database choices and why
- API style (REST, GraphQL, tRPC)
- State management approach
- Auth provider and strategy

---

## 4. Workflow Habits

### Git & Version Control
- Commit message style
- Branching strategy
- PR preferences (squash, merge, rebase)
- How they handle code review

### Development Flow
- TDD vs test-after vs no tests
- How they prefer to debug
- CI/CD preferences
- Deployment cadence

### Task Management
- How they break down work
- Linear, GitHub Issues, Jira, etc.
- How they prioritize

---

## 5. Corrections Log

Track every time the user corrects Claude to prevent repeat mistakes:

### Format
```markdown
### Correction: [What was wrong]
- **Date:** [When]
- **Wrong assumption:** [What Claude did/said]
- **Correct behavior:** [What the user wants instead]
- **Category:** [code-style | tool-choice | communication | architecture | other]
```

### Why This Matters
Corrections are the highest-signal memory. A user correcting you means:
1. You made an assumption that was wrong
2. The user cared enough to tell you
3. It will be frustrating if it happens again

**Rule:** Always save corrections. Always update conflicting memories.

---

## 6. Personal Context (Light Touch)

Only save if volunteered and relevant to working together:
- Timezone (for scheduling, async considerations)
- Role (founder, senior dev, junior dev, designer)
- Experience level with specific technologies
- Side projects or interests that come up
- How they prefer to be addressed

**Never save:** Real name unless they use it, location details, health info, financial info, relationship info, or anything they'd be surprised to see stored.

---

## Priority Order for Saving

When you notice multiple things in one session, prioritize:

1. **Corrections** — Highest priority, save immediately
2. **Explicit preferences** — "I always want X" — save immediately
3. **Tool/framework choices** — Save after confirmed in 1-2 sessions
4. **Communication style** — Save after clear pattern (2+ signals)
5. **Project context** — Save when stable (not brainstorming phase)
6. **Personal context** — Save only if clearly relevant and volunteered

---

## Signals to Watch For

### Explicit (Save Immediately)
- "Always use..."
- "Never do..."
- "I prefer..."
- "Remember that..."
- "Don't forget..."
- "From now on..."
- "I told you before..."

### Implicit (Save After 2+ Occurrences)
- Consistently choosing one tool over another
- Repeatedly reformatting code Claude writes
- Undoing specific types of changes
- Skipping certain suggestions every time
- A pattern in how they phrase requests
