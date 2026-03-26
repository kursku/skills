# Codebase Structure

**Analysis Date:** 2026-03-26

## Directory Layout

```
Skills/
├── packs/                          # Source of truth for all pack skills (1785 total)
│   ├── kit-510-ptbr/               # Portuguese business/marketing skills (522)
│   │   ├── 00-utilitarios-negocio/ # Business utilities
│   │   ├── 00-utilitarios-tecnicos/# Technical utilities
│   │   ├── 01-conteudo-copy/       # Content & copywriting
│   │   ├── 02-email-automacao/     # Email & automation
│   │   ├── 03-funis-vendas/        # Sales funnels
│   │   ├── 04-anuncios-trafego/    # Paid ads & traffic
│   │   ├── 05-seo-busca/          # SEO & search
│   │   ├── 06-financeiro-precos/   # Finance & pricing
│   │   ├── 07-juridico-compliance/ # Legal & compliance
│   │   ├── 08-lancamento-growth/   # Launch & growth
│   │   ├── 09-redes-sociais/       # Social media
│   │   ├── 10-clientes-consultoria/# Clients & consulting
│   │   ├── 11-operacoes-sistemas/  # Operations & systems
│   │   ├── 12-ia-automacao/        # AI & automation
│   │   ├── 13-cursos-educacao/     # Courses & education
│   │   ├── 14-marca-pessoal/       # Personal brand
│   │   ├── 15-analytics-dados/     # Analytics & data
│   │   └── 16-nichos-especificos/  # Specific niches
│   └── global-skillshare-import/   # Imported global skills (1263)
│       ├── wave-001/               # Import batches (~100 skills each)
│       ├── wave-002/
│       ├── ...
│       └── wave-013/
├── frontend/                       # Curated frontend skills (26 skills)
├── backend/                        # Curated backend skills (2 skills)
├── workflow/                       # Curated workflow/orchestration skills (32 skills)
├── tooling/                        # Curated developer tools (11 skills)
├── automation/                     # Curated automation skills
├── cloud-devops/                   # Curated cloud/DevOps skills
├── mobile/                         # Curated mobile skills
├── game-dev/                       # Curated game dev skills
├── docs-content/                   # Curated docs/content skills
├── business/                       # Curated business skills
├── data-ai/                        # Curated data/AI skills
├── security/                       # Curated security skills (empty, README only)
├── core/                           # Core skills (internal-comms)
├── scripts/                        # Build and analysis scripts
│   ├── catalog.py                  # Catalog generator (pack scanning + classification)
│   ├── release.sh                  # .skill bundle builder (ZIP creation)
│   ├── infer_risk.py               # Risk level inference for skills
│   ├── record_install_demo.py      # Installation demo recorder
│   ├── audit_global_skillshare_coverage.ps1  # PowerShell audit scripts
│   ├── compare_skill_coverage.ps1
│   ├── import_missing_skills_wave.ps1
│   └── skillshare_repo_check.ps1
├── .system/                        # Internal system skills (Codex/OpenAI origin)
│   ├── skill-creator/              # Skill authoring guide + agents
│   └── skill-installer/            # Skill installation tool + scripts
├── .github/
│   └── workflows/
│       └── release.yml             # CI: catalog + bundle + GitHub Release
├── _experimental/                  # Experimental/template skills
│   └── template/
│       └── SKILL.md                # Minimal skill template
├── docs/                           # Documentation (60 files)
│   ├── SKILL_ANATOMY.md            # Skill structure reference
│   ├── SKILL_TEMPLATE.md           # Skill template with all fields
│   ├── RELEASE.md                  # Release guide
│   ├── SKILLSHARE.md               # Skillshare CLI installation guide
│   ├── QUALITY_BAR.md              # Quality standards
│   ├── BUNDLES.md                  # Workflow bundles documentation
│   ├── SOURCES.md                  # Skill sources reference
│   ├── SEC_SKILLS.md               # Security skills catalog
│   └── global-skillshare-import-wave-*.txt  # Import logs per wave
├── docs-content/                   # Curated docs/content skills
├── dist/                           # Generated build output (gitignored)
│   ├── pack-catalog.json           # Machine-readable catalog
│   └── pack-catalog.md             # Human-readable catalog
├── .planning/                      # GSD planning documents
├── conteudo-copy -> packs/kit-510-ptbr/01-conteudo-copy  # Root symlinks (18 total)
├── email-automacao -> packs/kit-510-ptbr/02-email-automacao
├── ...                             # (all PT-BR categories symlinked)
├── README.md                       # Main catalog with category listings
├── workflow_bundles_readme.md      # Workflow bundle documentation
└── .gitignore                      # Excludes dist/, .DS_Store, etc.
```

## Directory Purposes

**`packs/`:**
- Purpose: Canonical source of truth for all 1785 pack skills
- Contains: Two pack collections, each with subcategories/waves containing skill directories
- Key files: Each skill has `SKILL.md` with YAML frontmatter

**`packs/kit-510-ptbr/`:**
- Purpose: Portuguese-language business and marketing skills
- Contains: 17 numbered subcategories (00-16), each containing skill directories
- Key files: `README.md` per subcategory, `SKILL.md` per skill

**`packs/global-skillshare-import/`:**
- Purpose: Skills imported from the global skillshare ecosystem
- Contains: 13 waves (wave-001 through wave-013), each with ~100 skill directories
- Key files: `SKILL.md` per skill, some include `resources/`, `reference/`, `templates/`

**Curated category directories (`frontend/`, `backend/`, `workflow/`, etc.):**
- Purpose: Hand-installed skills from external GitHub repos
- Contains: Skill directories with `SKILL.md` and `.skillshare-meta.json`
- Key files: `.skillshare-meta.json` tracks provenance (source URL, commit hash, file hashes)

**`scripts/`:**
- Purpose: Build tooling, catalog generation, quality analysis
- Contains: Python scripts (.py), Bash scripts (.sh), PowerShell scripts (.ps1)
- Key files: `catalog.py` (main catalog builder), `release.sh` (bundle builder), `infer_risk.py` (risk classifier)

**`.system/`:**
- Purpose: Internal Codex/OpenAI system skills for skill management
- Contains: `skill-creator/` (authoring guide with agents and references), `skill-installer/` (installation scripts)
- Key files: Each has `SKILL.md`, `agents/`, `scripts/`, `assets/`

**`docs/`:**
- Purpose: Project documentation, import logs, schema references
- Contains: Markdown guides, JSON reports, text import logs
- Key files: `SKILL_ANATOMY.md`, `SKILL_TEMPLATE.md`, `RELEASE.md`, `QUALITY_BAR.md`

**`dist/`:**
- Purpose: Generated build artifacts (gitignored)
- Contains: `pack-catalog.json`, `pack-catalog.md`, and `<category>/<skill>.skill` ZIP bundles
- Generated: Yes, by `scripts/catalog.py` and `scripts/release.sh`
- Committed: No

**`_experimental/`:**
- Purpose: Experimental or template skills not included in releases
- Contains: `template/SKILL.md` (minimal starter template)

## Key File Locations

**Entry Points:**
- `scripts/catalog.py`: Main catalog generation script
- `scripts/release.sh`: Bundle builder for `.skill` ZIP files
- `.github/workflows/release.yml`: CI pipeline definition

**Configuration:**
- `.gitignore`: Excludes `dist/`, `.DS_Store`, managed skillshare directories
- `.system/.codex-system-skills.marker`: Marker file for Codex system detection

**Core Logic:**
- `scripts/catalog.py`: Category taxonomy (CATEGORIES list), kit category map (KIT_CATEGORY_MAP), frontmatter parser, classifier, quality checker
- `scripts/release.sh`: Skill validation, ZIP bundling, curated vs pack collection logic
- `scripts/infer_risk.py`: Risk pattern matching (offensive/critical/caution/safe)

**Templates:**
- `docs/SKILL_TEMPLATE.md`: Full skill template with all fields
- `_experimental/template/SKILL.md`: Minimal skill starter

**Documentation:**
- `README.md`: Main project readme with category catalog
- `docs/SKILL_ANATOMY.md`: Skill structure reference
- `docs/RELEASE.md`: Release/build guide
- `workflow_bundles_readme.md`: Multi-skill bundle definitions

## Naming Conventions

**Files:**
- `SKILL.md`: Required skill definition file (UPPERCASE, always this exact name)
- `.skillshare-meta.json`: Provenance tracking for curated skills (hidden file)
- `README.md`: Category/directory descriptions
- Scripts: `snake_case.py`, `snake_case.sh`, `snake_case.ps1`

**Directories (Skills):**
- Skill directories: `lowercase-with-hyphens` (e.g., `linkedin-post`, `react-native-skills`)
- Must match the `name:` field in the skill's `SKILL.md` frontmatter

**Directories (Pack Categories):**
- Kit-510-ptbr: `NN-category-name` with two-digit prefix (e.g., `01-conteudo-copy`, `16-nichos-especificos`)
- Global import: `wave-NNN` with three-digit prefix (e.g., `wave-001`, `wave-013`)

**Directories (Curated Categories):**
- Lowercase-with-hyphens matching semantic domain (e.g., `frontend`, `cloud-devops`, `data-ai`, `game-dev`)

**Root Symlinks:**
- Portuguese category names matching target directory basename without numeric prefix (e.g., `conteudo-copy` -> `packs/kit-510-ptbr/01-conteudo-copy`)

## Where to Add New Code

**New Skill (PT-BR pack):**
- Create directory: `packs/kit-510-ptbr/<NN-category>/<skill-name>/SKILL.md`
- Follow frontmatter format: `name`, `description`, `license`, `metadata`, `risk` fields
- Optionally add `resources/`, `references/`, `examples/` subdirectories

**New Skill (Global import):**
- Create directory: `packs/global-skillshare-import/wave-NNN/<skill-name>/SKILL.md`
- Use standard frontmatter: `name`, `description`, `risk`, `source`, `date_added`

**New Curated Skill (from external repo):**
- Use `.system/skill-installer/` scripts to install from GitHub
- Or manually create directory under the appropriate category (e.g., `frontend/<skill-name>/`)
- Include `.skillshare-meta.json` for provenance tracking

**New Build Script:**
- Place in `scripts/`
- Python for data processing, Bash for build/release, PowerShell for Windows-specific audits

**New Category Taxonomy Keyword:**
- Edit `scripts/catalog.py`, add keywords to the appropriate entry in the `CATEGORIES` list
- For kit-510-ptbr folder mappings, update `KIT_CATEGORY_MAP`

**New Documentation:**
- Place in `docs/`
- Use UPPERCASE.md naming for guides (e.g., `GUIDE_NAME.md`)

## Special Directories

**`dist/`:**
- Purpose: Build output (catalog JSON/MD + .skill ZIP bundles)
- Generated: Yes
- Committed: No (in `.gitignore`)

**`.system/`:**
- Purpose: Codex/OpenAI internal system skills
- Generated: No
- Committed: Yes
- Note: Excluded from release builds by `release.sh`

**`_experimental/`:**
- Purpose: Experimental skills and templates
- Generated: No
- Committed: Yes
- Note: Excluded from release builds by `release.sh`

**`.planning/`:**
- Purpose: GSD project planning documents
- Generated: Yes (by GSD commands)
- Committed: Varies

**Root symlinks (18 total):**
- Purpose: Navigation shortcuts for PT-BR categories
- Pattern: `<category-name>` -> `packs/kit-510-ptbr/<NN-category-name>`
- Note: These are filesystem symlinks, not directories

---

*Structure analysis: 2026-03-26*
