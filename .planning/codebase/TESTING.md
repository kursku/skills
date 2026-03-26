# Testing Patterns

**Analysis Date:** 2026-03-26

## Test Framework

**Runner:**
- No formal test framework (no Jest, Vitest, pytest, etc.)
- Validation is script-based: Python and PowerShell scripts that check skill quality
- No `package.json`, no `npm test`, no test runner configuration

**Assertion Approach:**
- Scripts return exit codes (0 = pass, 1 = fail)
- Python functions return `(bool, str)` tuples with pass/fail + message
- PowerShell scripts accumulate `$errors` arrays and report at end

**Run Commands:**
```bash
# Validate a single skill (Codex/OpenAI schema)
python3 .system/skill-creator/scripts/quick_validate.py <skill-directory>

# Validate curated skills (PowerShell, checks frontmatter + meta)
pwsh scripts/skillshare_repo_check.ps1            # soft mode
pwsh scripts/skillshare_repo_check.ps1 -Strict     # strict mode (exit 1 on errors)

# Dry-run release build (validates all skills during bundling)
bash scripts/release.sh --dry-run

# Infer risk levels (dry-run)
python3 scripts/infer_risk.py                      # show what would change
python3 scripts/infer_risk.py --stats              # statistics only

# Build catalog (validates pack skills during cataloging)
python3 scripts/catalog.py
python3 scripts/catalog.py --issues-only           # show only skills with quality issues
```

## Validation Scripts

### `quick_validate.py` (Primary Validator)

**Location:** `.system/skill-creator/scripts/quick_validate.py`

**What it checks:**
1. `SKILL.md` exists in the skill directory
2. File starts with `---` (YAML frontmatter present)
3. Frontmatter is valid YAML and is a dictionary
4. Only allowed keys: `name`, `description`, `license`, `allowed-tools`, `metadata`
5. `name` field exists and is a string
6. `name` matches regex `^[a-z0-9-]+$` (kebab-case)
7. `name` does not start/end with hyphen or contain consecutive hyphens
8. `name` is max 64 characters
9. `description` field exists and is a string
10. `description` contains no angle brackets (`<` or `>`)
11. `description` is max 1024 characters

**Pattern:**
```python
def validate_skill(skill_path):
    """Returns (bool, str) - (is_valid, message)"""
    skill_path = Path(skill_path)
    skill_md = skill_path / "SKILL.md"
    if not skill_md.exists():
        return False, "SKILL.md not found"
    # ... checks ...
    return True, "Skill is valid!"
```

**Usage in skill creation workflow:**
```bash
# Step 5 of skill creation process
python3 .system/skill-creator/scripts/quick_validate.py path/to/skill-folder
```

### `skillshare_repo_check.ps1` (Repo-Wide Validator)

**Location:** `scripts/skillshare_repo_check.ps1`

**What it checks across all curated skills:**
1. Frontmatter exists (starts with `---`)
2. `name` field is present and non-empty
3. `description` field is present and non-empty
4. `.skillshare-meta.json` exists and is valid JSON (if present)

**Scope:**
- Scans skills at depth 2-3 from repo root
- Excludes: `.git`, `.system`, `docs`, `scripts` directories
- Only checks approved group folders: `core`, `frontend`, `backend`, `data-ai`, `security`, `workflow`, `tooling`, `_experimental`

**Outputs:**
- Skill count
- PASS/FAIL with error list
- Optional: writes `docs/skillshare-skills.json` index (with `-WriteIndex` flag)

### `release.sh` (Build-Time Validation)

**Location:** `scripts/release.sh`

**What it validates during build:**
- Each `SKILL.md` must have `name:` in frontmatter
- Each `SKILL.md` must have `description:` in frontmatter
- Skills failing validation are skipped with error logged

**Pattern:**
```bash
validate_skill() {
  local skill_md="$1"
  if ! grep -qE '^name:' "$skill_md"; then
    echo "MISSING_NAME"; return
  fi
  if ! grep -qE '^description:' "$skill_md"; then
    echo "MISSING_DESC"; return
  fi
  echo "OK"
}
```

### `infer_risk.py` (Risk Classification)

**Location:** `scripts/infer_risk.py`

**What it does:**
- Scans all `packs/` SKILL.md files
- Infers risk level using regex pattern matching against skill name + description + content
- Priority: offensive > critical > caution > safe
- Only processes skills with `risk: unknown`, `risk: none`, or missing risk
- Does NOT overwrite existing meaningful risk values

**Modes:**
- Dry-run (default): shows what would change
- `--apply`: writes changes to SKILL.md files
- `--stats`: statistics only

### `catalog.py` (Catalog Builder + Quality Checker)

**Location:** `scripts/catalog.py`

**What it does:**
- Catalogs and categorizes all pack skills
- Uses keyword-based taxonomy matching (pattern → category)
- Outputs `dist/pack-catalog.md` and `dist/pack-catalog.json`
- `--issues-only` flag shows skills with quality issues

## CI/CD Pipeline

### GitHub Actions Workflow

**Location:** `.github/workflows/release.yml`

**Trigger:** Push to `master` branch or manual `workflow_dispatch`

**Steps:**
1. Checkout code
2. Set up Python 3.12
3. Run `python3 scripts/catalog.py` (build catalog)
4. Run `bash scripts/release.sh` (build curated .skill files)
5. Run `bash scripts/release.sh --packs all` (build ALL pack .skill files)
6. Collect built `.skill` files
7. Delete existing `latest` GitHub release
8. Create new `latest` release with all `.skill` files attached

**What is validated in CI:**
- Catalog generation succeeds (valid YAML frontmatter across pack skills)
- Release build succeeds (name + description present in all bundled skills)
- Skills failing validation are skipped (not blocking), but logged

**What is NOT validated in CI:**
- No `quick_validate.py` run in CI (strict Codex schema not enforced repo-wide)
- No linting or formatting checks
- No automated tests (no test runner)
- No coverage requirements

## Test File Organization

**No test files exist.** There are no `*.test.*`, `*.spec.*`, or `test_*.py` files in the repository.

Validation is embedded in the scripts themselves:
- `.system/skill-creator/scripts/quick_validate.py` - single-skill validation
- `scripts/skillshare_repo_check.ps1` - repo-wide validation
- `scripts/release.sh` - build-time validation
- `scripts/catalog.py` - catalog-time quality checks

## Quality Bar (5 Automated Checks)

Defined in `docs/QUALITY_BAR.md`, a skill earns the "Validated" badge by passing:

1. **Metadata Integrity**: Valid YAML frontmatter with `name` (kebab-case, matches folder), `description` (under 200 chars), `risk` level, and `source` URL
2. **Clear Triggers**: Must have a "When to Use" section with accepted headings
3. **Safety & Risk Classification**: Must declare risk level (none/safe/critical/offensive)
4. **Copy-Pasteable Examples**: At least one code block or interaction example
5. **Explicit Limitations**: List of known edge cases

**Note:** These 5 checks are documented as the quality standard, but `quick_validate.py` only enforces checks 1 (partially). The full 5-check validation was historically in a `validate_skills.py` script (referenced in docs but not present in the current repo).

## Mocking

**Not applicable** - No test framework, no mocking.

## Fixtures and Factories

**Not applicable** - No test data fixtures.

## Coverage

**Requirements:** None enforced. No coverage tooling.

## Test Types

**Structural Validation (automated):**
- YAML frontmatter parsing and field checks
- Naming convention enforcement (kebab-case, length limits)
- Required field presence (name, description)
- JSON validity for `.skillshare-meta.json`

**Content Quality (manual/semi-automated):**
- Risk level inference via pattern matching (`infer_risk.py`)
- Category classification via keyword taxonomy (`catalog.py`)
- "When to Use" section presence (documented but not currently enforced)

**Build Validation (CI):**
- Catalog generation success
- .skill ZIP bundle creation success
- Skills with missing name/description are skipped with error log

**No unit tests, integration tests, or E2E tests exist.**

## Adding New Validation

**For a new single-skill check:**
Add to `.system/skill-creator/scripts/quick_validate.py` in the `validate_skill()` function. Return `(False, "error message")` for failures.

**For a new repo-wide check:**
Add to `scripts/skillshare_repo_check.ps1` in the `foreach ($skill in $skillFiles)` loop. Append to `$errors` array for failures.

**For CI enforcement:**
Add a step to `.github/workflows/release.yml` before the build steps. Use `set -e` or explicit exit codes to block releases on failure.

## Common Validation Patterns

**Checking frontmatter in Python:**
```python
import re
import yaml

content = Path("SKILL.md").read_text()
match = re.match(r"^---\n(.*?)\n---", content, re.DOTALL)
if match:
    frontmatter = yaml.safe_load(match.group(1))
    name = frontmatter.get("name", "")
    description = frontmatter.get("description", "")
```

**Checking frontmatter in Bash:**
```bash
if ! grep -qE '^name:' "$skill_md"; then
    echo "MISSING_NAME"
fi
```

**Checking frontmatter in PowerShell:**
```powershell
$lines = Get-Content -Path $skillFile
if ($lines[0].Trim() -eq "---") {
    # Parse line by line looking for name: and description:
}
```

---

*Testing analysis: 2026-03-26*
