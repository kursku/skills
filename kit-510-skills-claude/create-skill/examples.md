# Skill Examples

Real-world examples covering the major skill patterns. Use these as inspiration when creating new skills.

## 1. Task Skill with Side Effects — Deploy

A skill that performs actions. Uses `auto-activate: false` since deployment should be explicit.

```markdown
---
name: deploy
description: Deploy the application to production or staging environments. Use when the user wants to deploy, ship, release, or push to production.
argument-hint: [environment: staging|production]
auto-activate: false
---

# Deploy Skill

You are an expert at safely deploying this application. Follow the deployment checklist precisely.

## Pre-Deploy Checklist
1. Verify no uncommitted changes: `git status --porcelain`
2. Ensure all tests pass: `npm test`
3. Check the target environment from `$ARGUMENTS` (default: staging)
4. Build the application: `npm run build`

## Deploy Process

### Staging
```bash
npx vercel deploy --env preview
```

### Production
**Always confirm with the user before deploying to production.**
```bash
npx vercel deploy --prod
```

## Post-Deploy
1. Run smoke tests against the deployed URL
2. Check application logs for errors
3. Report the deployment URL to the user

## Critical Rules
1. Never deploy with uncommitted changes
2. Never deploy to production without explicit user confirmation
3. Always run tests before deploying
4. Always report the final deployment URL
```

**Directory structure:**
```
skills/deploy/
└── SKILL.md
```

---

## 2. Research Skill with Subagents — Deep Research

A skill that gathers information using Agent tool for parallel research.

```markdown
---
name: deep-research
description: Perform deep research on a topic using web search and analysis. Use when the user wants thorough research, a literature review, competitive analysis, or in-depth investigation of a topic.
argument-hint: [topic or question to research]
---

# Deep Research Skill

You are an expert researcher. Conduct thorough, multi-source research on the given topic.

## Research Process

1. **Parse the query**: Break `$ARGUMENTS` into 3-5 specific research questions
2. **Parallel research**: Launch Agent subagents to research each question simultaneously
3. **Synthesize**: Combine findings into a structured report
4. **Cite sources**: Include URLs for all claims

## Execution

For each research question, launch an Agent with subagent_type "general-purpose":
- Give each agent a specific, focused research question
- Have agents use WebSearch and WebFetch to gather information
- Run all agents in parallel for speed

## Output Format

Deliver a structured report:
- **Executive Summary** (2-3 sentences)
- **Key Findings** (bulleted, with source URLs)
- **Detailed Analysis** (organized by research question)
- **Open Questions** (what couldn't be answered)

## Critical Rules
1. Always launch agents in parallel, not sequentially
2. Minimum 3 different sources per major claim
3. Distinguish facts from opinions in the report
4. Include publication dates for time-sensitive information
```

---

## 3. Dynamic Context Skill — PR Summary

A skill that uses shell injection to provide live project context.

```markdown
---
name: pr-summary
description: Summarize the current PR or branch changes. Use when the user wants a PR overview, change summary, or review preparation.
---

# PR Summary

## Current State

Branch: !`git branch --show-current`
Base comparison: !`git merge-base HEAD main`

### Changed files
!`git diff main --name-only`

### Diff statistics
!`git diff main --stat`

### Recent commits on this branch
!`git log main..HEAD --oneline`

## Instructions

Analyze the changes above and produce:

1. **Summary**: One paragraph explaining what this PR does and why
2. **Changes by area**: Group changed files by feature/component
3. **Risk assessment**: Flag any high-risk changes (DB migrations, auth, payments, config)
4. **Review notes**: Specific things a reviewer should pay attention to
5. **Testing suggestions**: What should be tested manually

If `$ARGUMENTS` contains additional context (like a PR number), incorporate it.
```

---

## 4. Knowledge/Reference Skill — API Conventions

A pure knowledge skill that auto-activates when relevant. No slash command needed.

```markdown
---
name: api-conventions
description: API design conventions and patterns for this project. Use when writing new API endpoints, controllers, routes, or reviewing API code. Covers REST conventions, error handling, authentication, and response formats.
user-invocable: false
---

# API Conventions

## URL Structure
- Plural nouns for resources: `/users`, `/orders`, `/products`
- Nest for direct relationships: `/users/:id/orders`
- Max 2 levels of nesting: `/users/:id/orders` not `/users/:id/orders/:oid/items/:iid`
- Use query params for filtering: `/orders?status=pending&limit=10`

## HTTP Methods
- `GET` — Read (never mutates)
- `POST` — Create new resource
- `PUT` — Full replacement of resource
- `PATCH` — Partial update
- `DELETE` — Remove resource

## Response Envelope

All responses use this format:
```json
{
  "data": {},
  "error": null,
  "meta": { "page": 1, "total": 42 }
}
```

## Error Format
```json
{
  "data": null,
  "error": {
    "code": "VALIDATION_ERROR",
    "message": "Human-readable message",
    "details": [{ "field": "email", "issue": "invalid format" }]
  }
}
```

## Status Codes
- `200` — Success
- `201` — Created
- `400` — Validation error
- `401` — Not authenticated
- `403` — Not authorized
- `404` — Not found
- `409` — Conflict
- `500` — Server error

## Authentication
All endpoints require `Authorization: Bearer <token>` except those under `/public/`.
```

---

## 5. Skill with Bundled Scripts

A skill that includes executable scripts in its directory.

```markdown
---
name: db-migrate
description: Create and run database migrations safely. Use when the user wants to create a migration, run migrations, or check migration status.
argument-hint: [migration name or action: create|run|status]
auto-activate: false
---

# Database Migration Skill

You are an expert at managing database migrations safely.

## Available Actions

Parse `$ARGUMENTS` to determine the action:

- **create [name]**: Generate a new migration file
- **run**: Apply pending migrations
- **status**: Show migration status
- **rollback**: Revert the last migration

## Migration Template

Use the template at `${CLAUDE_SKILL_DIR}/scripts/migration-template.sql` when creating new migrations.

## Safety Checks

Before running any migration:
1. Run `${CLAUDE_SKILL_DIR}/scripts/check-pending.sh` to verify pending migrations
2. Ensure the database is backed up for production
3. Always run on staging first

## Critical Rules
1. Never run migrations on production without explicit user confirmation
2. Every migration must have a rollback
3. Never modify an already-applied migration — create a new one
4. Test migrations on a fresh database before applying
```

**Directory structure:**
```
skills/db-migrate/
├── SKILL.md
└── scripts/
    ├── check-pending.sh
    └── migration-template.sql
```

---

## 6. Skill with Supporting Reference Files

A skill that splits content across multiple files to stay under the SKILL.md size limit. Follows the same pattern as the trigger-dev skill.

```markdown
---
name: terraform
description: Write and manage Terraform infrastructure code. Use when the user wants to create infrastructure, add cloud resources, write Terraform modules, or manage infrastructure as code.
argument-hint: [infrastructure to create or modify]
---

# Terraform Skill

You are an expert at writing production-grade Terraform infrastructure code.

Read the detailed reference files in `${CLAUDE_SKILL_DIR}` for comprehensive details:

- `reference-resources.md` — AWS/GCP/Azure resource patterns, naming conventions, tagging
- `reference-modules.md` — Module structure, inputs/outputs, composition patterns
- `reference-state.md` — State management, backends, workspaces, import

## Critical Rules

1. Always use variables for environment-specific values
2. Tag all resources with `environment`, `team`, and `managed-by`
3. Use modules for any resource group used more than once
4. Never hardcode credentials — use IAM roles or secret references
5. Always include `terraform.tfvars.example` with placeholder values
6. Use `terraform fmt` and `terraform validate` before committing
7. Pin provider versions in `versions.tf`

## Quick Patterns

### Basic Resource
```hcl
resource "aws_s3_bucket" "data" {
  bucket = "${var.project}-${var.environment}-data"
  tags   = local.common_tags
}
```

### Module Usage
```hcl
module "vpc" {
  source      = "./modules/vpc"
  environment = var.environment
  cidr_block  = var.vpc_cidr
}
```

Use `$ARGUMENTS` to understand what infrastructure the user wants. Build complete, production-ready Terraform code.
```

**Directory structure:**
```
skills/terraform/
├── SKILL.md
├── reference-resources.md
├── reference-modules.md
└── reference-state.md
```

---

## Pattern Summary

| Pattern | Key Characteristics |
|---------|-------------------|
| **Task** | `auto-activate: false`, step-by-step process, confirmation gates |
| **Research** | Uses Agent subagents, parallel execution, structured output |
| **Dynamic** | Shell injection `!`command``, live context, minimal instructions |
| **Knowledge** | `user-invocable: false`, pure reference, no actions |
| **Scripts** | `${CLAUDE_SKILL_DIR}/scripts/`, external tooling |
| **Reference files** | Split content, `${CLAUDE_SKILL_DIR}/*.md`, lazy loading |
