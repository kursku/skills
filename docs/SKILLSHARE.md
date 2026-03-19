# Skillshare Usage For This Repository

This repository can be used as a direct source for skillshare installs and updates.

## Quick Start

1. Clone this repository.
2. In your own project, run:

```bash
skillshare init -p --targets "claude,codex,cursor"
skillshare install github.com/sickn33/antigravity-awesome-skills --track -p --all
skillshare sync -p
```

Notes:
- Use `--targets` to match your actual tools.
- Keep `--track` so `skillshare update --all -p` can pull updates from this repo.

## Windows-Friendly Setup

```powershell
skillshare init -p --targets "claude,codex,cursor"
skillshare install github.com/sickn33/antigravity-awesome-skills --track -p --all
skillshare sync -p
```

If your environment has symlink restrictions, set copy mode for a target:

```bash
skillshare target claude --mode copy -p
skillshare sync -p --force
```

## Recommended Maintenance

Run this in projects that consume skills from this repo:

```bash
skillshare check -p
skillshare update --all -p
skillshare sync -p
```

## Repository Health Check

This repo includes a validation script that checks top-level skill folders and optionally emits an index:

```powershell
./scripts/skillshare_repo_check.ps1
```

Options:
- `-WriteIndex`: writes [docs/skillshare-skills.json](docs/skillshare-skills.json)
- `-Strict`: exit with error code when required fields are missing

Examples:

```powershell
./scripts/skillshare_repo_check.ps1 -WriteIndex
./scripts/skillshare_repo_check.ps1 -WriteIndex -Strict
```

## What The Checker Validates

- Every discovered skill directory (including grouped folders) contains `SKILL.md`
- `SKILL.md` includes frontmatter with `name` and `description`
- `.skillshare-meta.json` is optional, but if present must be valid JSON

## Why This Helps Skillshare

- Reduces install/update surprises caused by malformed skill folders
- Creates a machine-readable inventory for auditing and automation
- Standardizes setup for project-mode (`-p`) teams

See the proposed folder migration map in [SKILLSHARE_MIGRATION_PROPOSAL.md](SKILLSHARE_MIGRATION_PROPOSAL.md).

## Best Practice: Organize Skills By Purpose

For large collections, use stable folder groups instead of a flat root.

Recommended top-level groups:
- `core/` for universal daily skills (planning, debug, review)
- `frontend/` for UI and web skills
- `backend/` for API, data, and infra skills
- `data-ai/` for LLM, RAG, and evaluation skills
- `security/` for security and audit skills
- `workflow/` for orchestrator and process skills
- `tooling/` for editor/CLI integration helpers
- `_experimental/` for trial skills not yet approved for broad use

Example layout:

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

### Why this structure works

- Easier discovery: users can browse by domain first.
- Safer updates: experimental items are isolated.
- Better ownership: teams can own one folder each.
- Cleaner reviews: path prefixes make diffs and audits faster.

## Naming Conventions

- Use lowercase kebab-case for folders and skill names.
- Keep path depth shallow (usually one group level is enough).
- Prefer semantic names over vendor names.
- Use consistent prefixes for workflow bundles, for example:
	- `workflow-frontend-*`
	- `workflow-backend-*`
	- `workflow-release-*`

## Skillshare Commands For Organized Installs

Install directly into a group folder:

```bash
skillshare install github.com/sickn33/antigravity-awesome-skills -s clarify,audit --into frontend -p
skillshare install github.com/sickn33/antigravity-awesome-skills -s supabase-postgres-best-practices --into backend -p
```

Validate and sync after changes:

```bash
./scripts/skillshare_repo_check.ps1 -WriteIndex
skillshare sync -p
```

## Operating Model For Teams

- Keep `core/` small and high-trust.
- Route new skills to `_experimental/` first.
- Promote from `_experimental/` to a stable domain folder after review.
- Run checker + sync in CI for every change.
- Use `--track` for shared repos so updates remain reproducible.

## Windows Notes

- If symlink behavior is inconsistent, use copy mode per target:

```bash
skillshare target claude --mode copy -p
skillshare sync -p --force
```

- Keep paths short and avoid deep nesting to reduce path-length friction.

## Pack Convention

- Large third-party or marketplace packs should live under `packs/` instead of mixing with curated first-party groups.
- Current example: `packs/kit-510-ptbr`.
- For this pack, Portuguese usage instructions are in `packs/kit-510-ptbr/README_SKILLSHARE_PT-BR.md`.

## Global Source Audit (AppData/Roaming)

To compare this repo against your global source at `AppData/Roaming/skillshare/skills`, run:

```powershell
./scripts/audit_global_skillshare_coverage.ps1
```

Generated reports:

- `docs/global-skillshare-coverage-summary.json` (counts and totals)
- `docs/global-skillshare-in-repo.txt` (skill names already present)
- `docs/global-skillshare-missing-in-repo.txt` (skill names missing in this repo)
- `docs/global-skillshare-missing-with-source-paths.csv` (missing skills with exact source paths)

### Controlled Import Waves

To import missing skills in safe batches, use:

```powershell
./scripts/import_missing_skills_wave.ps1
./scripts/audit_global_skillshare_coverage.ps1
```

Default behavior imports the first 100 missing skills into:

- `packs/global-skillshare-import/wave-001`

Wave reports:

- `docs/global-skillshare-import-wave-001-report.json`
- `docs/global-skillshare-import-wave-001-imported.txt`
- `docs/global-skillshare-import-wave-001-skipped.txt`

## Using These Skills in Claude.ai (Web)

If you are using Claude.ai in the browser (not CLI), the workflow is different:

- `skillshare` does not sync directly into Claude.ai.
- Use Claude.ai Projects and upload skill files as project knowledge.
- Trigger skills by naming them in prompts (for example, "Use skill X").

### Quick Path Selector (Beginner)

Use this table to choose your starting bundle:

| Primary goal | Start with | First prompt |
|---|---|---|
| Social and content growth | `01-conteudo-copy` + `09-redes-sociais` (from `packs/kit-510-ptbr`) | "Use social and content skills to build a 30-day content calendar." |
| Paid ads and ROI optimization | `04-anuncios-trafego` + `15-analytics-dados` (from `packs/kit-510-ptbr`) | "Use ads and analytics skills to draft a lead generation campaign plan." |
| Consulting and client ops | `10-clientes-consultoria` + `11-operacoes-sistemas` + `00-utilitarios-negocio` (from `packs/kit-510-ptbr`) | "Use consulting and operations skills to create a 30-day client onboarding workflow." |

If unsure, start with the social/content path because it is usually the easiest to validate quickly.

### Practical Claude.ai Workflow

1. Create a Claude.ai Project for your domain (for example, marketing, frontend, operations).
2. Upload selected `SKILL.md` files and supporting docs from this repo to Project Knowledge.
3. Add a short project instruction listing your preferred skills and when to apply each.
4. In chat, explicitly request a skill by name and task.

Suggested project instruction:

```text
Prioritize the uploaded skills for this project.
For each request, first identify the best matching skill and state your choice briefly.
Then execute using the guidance in that SKILL.md.
If critical context is missing, ask up to 3 concise clarification questions before executing.
```

Upload checklist:

1. Upload `SKILL.md` for each selected skill.
2. Upload referenced support files (templates/references/scripts) used by that skill.
3. Avoid uploading the entire repository unless absolutely necessary.

Example prompt:

```text
Use the skill "frontend-design" from the uploaded knowledge to create a landing page hero with CTA and responsive layout.
```

### Recommended For Claude.ai

- Keep uploads curated (10 to 40 high-value skills per project).
- Split projects by context instead of uploading the entire repository.
- Include one index file or checklist in project knowledge for discovery.
- Re-upload when skills are updated in git.

Maintenance routine:

1. Weekly: remove unused uploads and keep only active skills.
2. Biweekly: add missing support files discovered during usage.
3. Monthly: refresh uploaded files from latest git changes.
