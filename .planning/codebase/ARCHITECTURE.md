# Architecture

**Analysis Date:** 2026-03-26

## Pattern Overview

**Overall:** Content Catalog with Pack-based Organization

This is a skills catalog repository for Claude AI (claude.ai Projects and Claude Code). It is NOT a runnable application -- it is a structured collection of ~1864 Markdown-based skill definitions organized into packs, curated categories, and published as `.skill` bundles (ZIP archives).

**Key Characteristics:**
- Content-first: The primary artifact is `SKILL.md` files containing AI instruction prompts
- Two-tier organization: "packs" (source of truth) and "curated categories" (published directories)
- Symlink-based navigation: Root-level symlinks expose PT-BR categories from `packs/kit-510-ptbr/`
- Build pipeline: Python catalog script + Bash release script generate `.skill` ZIP bundles
- CI-driven releases: GitHub Actions builds catalog + bundles and publishes to GitHub Releases

## Layers

**Source Layer (Packs):**
- Purpose: Canonical storage for all skill definitions
- Location: `packs/`
- Contains: Two packs with all 1785 pack skills
  - `packs/kit-510-ptbr/` (522 skills) -- Portuguese business/marketing skills in 17 numbered subcategories
  - `packs/global-skillshare-import/` (1263 skills) -- Imported from global skillshare ecosystem, organized in 13 waves
- Depends on: Nothing
- Used by: Catalog script, release script, symlinks

**Curated Layer (Category Directories):**
- Purpose: Hand-selected skills installed from external repos (e.g., GitHub skillshare)
- Location: `frontend/`, `backend/`, `workflow/`, `tooling/`, `automation/`, `cloud-devops/`, `mobile/`, `game-dev/`, `docs-content/`, `business/`, `data-ai/`, `security/`, `core/`
- Contains: ~76 skills with `.skillshare-meta.json` provenance tracking
- Depends on: External GitHub repos (source of installations)
- Used by: Release script (builds curated `.skill` bundles)

**Navigation Layer (Root Symlinks):**
- Purpose: Shortcut access to PT-BR pack categories from repo root
- Location: Root of repository (18 symlinks)
- Contains: Symlinks like `conteudo-copy -> packs/kit-510-ptbr/01-conteudo-copy`
- Depends on: `packs/kit-510-ptbr/` subdirectories
- Used by: README.md category listing, end users browsing the repo

**Build Layer (Scripts):**
- Purpose: Catalog generation, `.skill` bundle building, quality analysis
- Location: `scripts/`
- Contains: Python and Bash scripts
- Depends on: Pack and curated skill directories
- Used by: CI pipeline, developers

**System Layer (Internal Tools):**
- Purpose: Codex/OpenAI-originated skill creation and installation tools
- Location: `.system/`
- Contains: `skill-creator/` and `skill-installer/` with their own agents/scripts
- Depends on: GitHub API for installing from external repos
- Used by: Developers creating or installing skills

**Distribution Layer (Dist):**
- Purpose: Generated build artifacts (catalog + `.skill` ZIP bundles)
- Location: `dist/`
- Contains: `pack-catalog.json`, `pack-catalog.md`, and `.skill` ZIP files per category
- Generated: Yes (by `scripts/catalog.py` and `scripts/release.sh`)
- Committed: No (in `.gitignore`)

## Data Flow

**Catalog Generation Flow:**

1. `scripts/catalog.py` scans all `SKILL.md` files under `packs/`
2. Parses YAML frontmatter (name, description, risk, tags)
3. Classifies each skill into a canonical category using keyword matching
4. Runs quality checks (missing name, short description, unset risk, duplicates)
5. Outputs `dist/pack-catalog.json` (machine-readable) and `dist/pack-catalog.md` (human-readable)

**Release Build Flow:**

1. `scripts/release.sh` collects skill directories (curated or pack-based)
2. For packs: reads `dist/pack-catalog.json` for category assignments (runs `catalog.py` if missing)
3. Validates each `SKILL.md` has `name:` and `description:` in frontmatter
4. Creates ZIP archives: `dist/<category>/<skill-name>.skill`
5. CI uploads all `.skill` files to GitHub Releases as the `latest` release

**Skill Installation Flow (Curated):**

1. Skills are installed from external GitHub repos using `.system/skill-installer/` scripts
2. Each installed skill gets a `.skillshare-meta.json` tracking source, version, and file hashes
3. Installed skills land in curated category directories (e.g., `frontend/adapt/`)

**Risk Inference Flow:**

1. `scripts/infer_risk.py` scans all `SKILL.md` files in `packs/`
2. Analyzes content against pattern lists (offensive, critical, caution, safe)
3. Adds `risk:` field to frontmatter of skills that lack it

## Key Abstractions

**Skill:**
- Purpose: A self-contained AI instruction module
- Examples: `packs/kit-510-ptbr/01-conteudo-copy/linkedin-post/SKILL.md`, `frontend/adapt/SKILL.md`
- Pattern: Directory containing a `SKILL.md` with YAML frontmatter + Markdown instructions, plus optional `references/`, `examples/`, `scripts/`, `templates/` subdirectories

**Pack:**
- Purpose: A collection of skills grouped by origin/language
- Examples: `packs/kit-510-ptbr/`, `packs/global-skillshare-import/`
- Pattern: Top-level directory under `packs/` containing subcategories or waves

**Category (Canonical):**
- Purpose: Semantic grouping for catalog/release purposes
- Examples: `security`, `frontend`, `backend`, `ai-agents`, `business`, `content`, `devops`, `data`, `automation`, `productivity`, `education`, `health`
- Pattern: Keyword-matched classification defined in `scripts/catalog.py` CATEGORIES list

**Wave:**
- Purpose: Batch import grouping for global skillshare imports
- Examples: `packs/global-skillshare-import/wave-001/` through `wave-013/`
- Pattern: Sequential numbered directories, each containing ~100 skill directories

## Entry Points

**Catalog Script:**
- Location: `scripts/catalog.py`
- Triggers: Manual run or CI pipeline
- Responsibilities: Scan packs, classify skills, check quality, output catalog

**Release Script:**
- Location: `scripts/release.sh`
- Triggers: CI pipeline on push to master, or manual run
- Responsibilities: Build `.skill` ZIP bundles for upload to claude.ai

**CI Pipeline:**
- Location: `.github/workflows/release.yml`
- Triggers: Push to `master` branch or manual `workflow_dispatch`
- Responsibilities: Run catalog.py, release.sh (curated + packs), upload to GitHub Releases

**Risk Inference:**
- Location: `scripts/infer_risk.py`
- Triggers: Manual run
- Responsibilities: Add `risk:` frontmatter to skills that lack it

## Error Handling

**Strategy:** Validation-based skip with summary reporting

**Patterns:**
- `release.sh` validates each `SKILL.md` for required frontmatter fields; skips invalid skills and reports errors in summary
- `catalog.py` tracks quality issues per skill (missing-name, description-too-short, risk-unset, duplicate-name) and includes them in catalog output
- `infer_risk.py` supports `--dry-run` mode to preview changes before applying

## Cross-Cutting Concerns

**Quality Assurance:** `scripts/catalog.py` includes quality_issues() that checks for missing names, short descriptions, unset risk levels, generic descriptions, and duplicate names across the entire catalog

**Categorization:** Keyword-based taxonomy in `scripts/catalog.py` with ~250 keywords across 12 categories. Kit-510-ptbr has an explicit folder-to-category mapping (`KIT_CATEGORY_MAP`). First keyword match wins.

**Provenance Tracking:** Curated skills include `.skillshare-meta.json` with source URL, repo, commit hash, tree hash, and per-file SHA-256 hashes

**Risk Classification:** Four-level system (safe, caution, critical, offensive) inferred by content pattern matching in `scripts/infer_risk.py`

---

*Architecture analysis: 2026-03-26*
