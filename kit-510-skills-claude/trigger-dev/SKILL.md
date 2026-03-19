---
name: trigger-dev
description: Build Trigger.dev background jobs, automations, and workflows in TypeScript. Use when the user wants to create tasks, scheduled jobs, AI agent workflows, queued background processing, cron jobs, or any long-running async work with Trigger.dev. Triggers on imports from @trigger.dev/sdk or mentions of trigger.dev.
argument-hint: [description of what to build]
---

# Trigger.dev Skill

You are an expert at building production-grade Trigger.dev v4 background tasks, workflows, and automations in TypeScript.

Read the detailed reference files in `${CLAUDE_SKILL_DIR}` for comprehensive code patterns:

- `core-reference.md` — Tasks, runs, triggering, queues, concurrency, retries, errors, idempotency, wait functions
- `config-reference.md` — trigger.config.ts, build extensions, deployment, CLI, project structure, env vars, monorepos
- `advanced-reference.md` — AI integration, streams, realtime, middleware, locals, lifecycle hooks, metadata, tags, scheduled tasks

## Setup Checklist

If starting a new Trigger.dev project or adding to an existing one, refer to https://trigger.dev/docs/manual-setup and use the `mcp__trigger__search_docs` tool for the latest setup instructions. Core steps:

1. Install packages: `npm add @trigger.dev/sdk@latest` and `npm add -D @trigger.dev/build@latest`
2. Create `trigger.config.ts` at project root with `defineConfig({ project: "<ref>", dirs: ["./src/trigger"] })`
3. Add `TRIGGER_SECRET_KEY` to `.env`
4. Create task files in the configured `dirs` directory
5. Run `npx trigger.dev@latest dev` for local development
6. Deploy with `npx trigger.dev@latest deploy`

## Core Patterns

### Basic Task
```typescript
import { task } from "@trigger.dev/sdk";

export const myTask = task({
  id: "my-task",
  run: async (payload: { data: string }, { ctx }) => {
    return { result: "done" };
  },
});
```

### Schema-Validated Task
```typescript
import { schemaTask } from "@trigger.dev/sdk";
import { z } from "zod";

export const myTask = schemaTask({
  id: "my-task",
  schema: z.object({ name: z.string(), age: z.number() }),
  run: async (payload) => { /* payload is typed and validated */ },
});
```

### Scheduled Task (Cron)
```typescript
import { schedules } from "@trigger.dev/sdk";

export const dailyCleanup = schedules.task({
  id: "daily-cleanup",
  cron: "0 0 * * *",
  run: async (payload) => {
    // payload.timestamp, payload.lastTimestamp, payload.timezone
  },
});
```

### Trigger from Backend
```typescript
import { tasks } from "@trigger.dev/sdk";
import type { myTask } from "~/trigger/my-task";

const handle = await tasks.trigger<typeof myTask>("my-task", { data: "hello" });
```

### Trigger from Inside a Task
```typescript
const result = await otherTask.triggerAndWait({ data: "hello" });
if (result.ok) console.log(result.output);
```

## Critical Rules

1. **Task IDs must be unique** across the entire project
2. **Payloads and return values must be JSON serializable** — no classes, functions, or circular refs
3. **Always export tasks** from trigger files (unexported tasks become hidden/internal-only)
4. **Use type-only imports** when triggering from backend: `import type { myTask } from "~/trigger/my-task"`
5. **trigger.config.ts must be at the project root** — it cannot be nested
6. **Use `AbortTaskRunError`** to fail without retrying on permanent errors
7. **Wait functions are free** — tasks checkpoint during waits, no compute charges
8. **Concurrency limits only count actively executing runs** — delayed/waiting runs don't count
9. **Max 10 tags per run**, max 256KB metadata per run, max 1000 items per batch
10. **Use `idempotencyKeys.create()`** inside tasks to prevent duplicate child triggers during retries
11. **Use the `mcp__trigger__search_docs` tool** to look up the latest docs when unsure about any API
12. **Use `mcp__trigger__deploy`** to deploy tasks, **`mcp__trigger__list_runs`** to check runs, **`mcp__trigger__trigger_task`** to trigger tasks

## Machine Presets

| Preset | vCPU | RAM |
|--------|------|-----|
| micro | 0.25 | 0.25 GB |
| small-1x (default) | 0.5 | 0.5 GB |
| small-2x | 1 | 1 GB |
| medium-1x | 1 | 2 GB |
| medium-2x | 2 | 4 GB |
| large-1x | 4 | 8 GB |
| large-2x | 8 | 16 GB |

## Key SDK Imports

```typescript
import {
  task, schemaTask, schedules, batch, tasks, runs, queues,
  tags, metadata, wait, auth, idempotencyKeys, logger, streams,
  AbortTaskRunError, configure, query,
} from "@trigger.dev/sdk";
import { ai } from "@trigger.dev/sdk/ai";
```

Use `$ARGUMENTS` to understand what the user wants to build. Read the reference files for detailed patterns before writing code.
