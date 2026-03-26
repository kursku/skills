# Codebase Concerns

**Analysis Date:** 2026-03-26

## Tech Debt

**Catalog only indexes pack skills, ignoring 76 curated skills:**
- Issue: `scripts/catalog.py` only scans `packs/` directory. The 76 curated skills spread across top-level category directories (`frontend/`, `backend/`, `workflow/`, `tooling/`, `data-ai/`, `core/`) are never indexed, never quality-checked, and never appear in `dist/pack-catalog.json`.
- Files: `scripts/catalog.py` (line 27: `PACKS_DIR = REPO_ROOT / "packs"`), `scripts/release.sh` (lines 61-79 handle curated separately but with no quality checks)
- Impact: Curated skills bypass all quality issue detection (duplicate-name, risk-unset, description-too-short). The catalog gives an incomplete picture of the repo. Category distribution stats are wrong.
- Fix approach: Extend `catalog.py` to also scan top-level category directories, or unify all skills under `packs/`. The `release.sh` already finds curated skills separately, so there is precedent for dual scanning.

**All 76 curated skills missing `risk`, `source`, and `date_added` frontmatter:**
- Issue: Every skill outside `packs/` lacks `risk:`, `source:`, and `date_added:` in frontmatter. The `infer_risk.py` script only targets `packs/` (line 25: `PACKS_DIR = REPO_ROOT / "packs"`).
- Files: All skills under `workflow/`, `tooling/`, `frontend/` (via `.skillshare-meta.json` imports), `backend/`, `data-ai/`, `core/`
- Impact: These skills ship in `.skill` bundles without risk classification. Users cannot assess safety. The quality bar (documented in `docs/QUALITY_BAR.md`) requires risk metadata.
- Fix approach: Run `infer_risk.py` against all SKILL.md files, not just packs. Update the script's `PACKS_DIR` or add a second scan path.

**Risk level terminology inconsistency:**
- Issue: `docs/QUALITY_BAR.md` defines risk levels as `[none, safe, critical, offensive, unknown]` with "none" for pure text/reasoning. `scripts/infer_risk.py` uses `[safe, caution, critical, offensive]` with no "none" or "unknown" level. The `catalog.py` quality check flags `risk: unknown` and empty risk as issues but does not flag `risk: none`.
- Files: `docs/QUALITY_BAR.md` (lines 17-24), `scripts/infer_risk.py` (lines 12-17), `scripts/catalog.py` (lines 369-371)
- Impact: No single source of truth for valid risk levels. Skills may have inconsistent risk values. "caution" exists in data but not in the quality bar spec. "none" exists in the spec but not in the inference script.
- Fix approach: Align on a single canonical set of risk levels. Update `QUALITY_BAR.md`, `infer_risk.py`, and `catalog.py` to use the same values.

**136 skills contain generic boilerplate content:**
- Issue: 136 pack skills contain the template phrase "Working on ... tasks or workflows" indicating they were auto-generated with minimal customization. These provide little value beyond their frontmatter description.
- Files: Scattered across `packs/global-skillshare-import/wave-*/*` (search for "Working on.*tasks or workflows" in SKILL.md files)
- Impact: Inflates skill count without adding substance. Users who install these get generic instructions that add no domain-specific value. Undermines trust in the catalog.
- Fix approach: Either enrich these skills with real content, or flag them with a `quality: stub` field and exclude from release bundles.

**Overly broad risk inference patterns:**
- Issue: `infer_risk.py` CRITICAL_PATTERNS include very broad terms like `deploy`, `production`, `pipeline`, `aws`, `azure`, `gcp`, `ssl`, `tls`, `billing`, `financial`, `compliance`, `certificate`. CAUTION_PATTERNS include `api`, `write`, `create`, `update`, `delete`, `automat`, `integra`. This results in 911 out of 1785 skills (51%) classified as "critical" -- far too many.
- Files: `scripts/infer_risk.py` (lines 37-48 for CRITICAL, lines 50-59 for CAUTION)
- Impact: Risk inflation makes the classification meaningless. A skill that merely mentions "API" in its description gets flagged as "caution" or higher. Skills about AWS documentation get marked "critical" even if they are read-only guides.
- Fix approach: Require pattern matches against the skill's actual instructions/actions, not just description text. Use multi-signal scoring (e.g., if the skill contains `rm`, `delete`, `deploy` commands in code blocks, elevate risk).

## Known Bugs

**Duplicate skills in game-development wave-006:**
- Symptoms: 5 duplicate skill pairs exist: `2d-games`, `3d-games`, `game-art`, `game-audio`, `game-design` each appear both at `packs/global-skillshare-import/wave-006/<name>/` and nested under `packs/global-skillshare-import/wave-006/game-development/<name>/`.
- Files: `packs/global-skillshare-import/wave-006/game-art/`, `packs/global-skillshare-import/wave-006/game-development/game-art/`, and same pattern for the other 4 skills
- Trigger: The wave-006 import created both flat and nested copies.
- Workaround: `catalog.py` detects and flags these as `duplicate-name` but does not prevent them from being bundled and released.

**`remotion` skill exists in both curated and pack locations:**
- Symptoms: `frontend/remotion/` (curated) and a pack version both exist. They may diverge in content.
- Files: `frontend/remotion/SKILL.md`, corresponding pack SKILL.md
- Trigger: Skill was imported to packs without removing the curated version.
- Workaround: None. Both get bundled -- curated version by `release.sh` default mode, pack version by `--packs all`.

## Security Considerations

**No validation in CI pipeline:**
- Risk: The release workflow (`release.yml`) builds and publishes `.skill` files without running any validation step. No frontmatter schema check, no content quality gate, no risk verification.
- Files: `.github/workflows/release.yml`
- Current mitigation: `release.sh` does a minimal name/description check before bundling.
- Recommendations: Add a CI step that runs `catalog.py --issues-only` and fails if critical issues are found (missing names, unset risk). Add a step to validate that no `.env` or credential files are included in `.skill` bundles.

**Skills bundled with potentially sensitive files:**
- Risk: `.skill` files are ZIP archives of entire skill directories. Some skills contain scripts, configs, and test data that may include example credentials or API patterns.
- Files: All skills processed by `scripts/release.sh` (line 163: `zip -qr "$out_file" . --exclude "*.DS_Store" --exclude "__pycache__/*"`)
- Current mitigation: Only `.DS_Store` and `__pycache__` are excluded from ZIPs.
- Recommendations: Add exclusion patterns for `.env*`, `*.key`, `*.pem`, `credentials*`, `secrets*`, `node_modules/`, `.git/`.

## Performance Bottlenecks

**Massive .skill bundle sizes for bloated skills:**
- Problem: Some skills contain hundreds of bundled files with large binaries. When built as `.skill` ZIPs, these become unusable.
- Files: `packs/global-skillshare-import/wave-008/loki-mode/` (1101 files, 11MB), `packs/global-skillshare-import/wave-007/last30days/` (41 files, 15MB with JPEG/MP3 assets), `packs/global-skillshare-import/wave-003/canvas-design/` (83 files, 5.6MB with font files)
- Cause: Skills were imported wholesale from GitHub repos without stripping non-essential files (benchmarks, test datasets, media assets, font files).
- Improvement path: Add a `.skillignore` mechanism (like `.gitignore`) per skill to exclude non-essential files from bundles. Or add a max bundle size check in CI.

**Keyword-based category classification has O(n*m) complexity:**
- Problem: `catalog.py` `classify()` function iterates all keywords for all categories for every skill. With ~300 keywords across 12 categories and 1785 skills, this is ~540K regex operations.
- Files: `scripts/catalog.py` (lines 337-358)
- Cause: Linear scan with regex per keyword.
- Improvement path: Pre-compile keyword patterns into a single alternation regex per category, or use a trie/set-based lookup.

## Fragile Areas

**Category classification via keyword lists:**
- Files: `scripts/catalog.py` (lines 35-265)
- Why fragile: 300+ hardcoded keywords drive all categorization. Adding a new skill whose name/description contains a common word (like "build", "api", "copy") causes silent miscategorization. Order-dependent matching means the first category to match wins, which is non-obvious.
- Safe modification: When adding keywords, test with `python3 scripts/catalog.py --json | python3 -c "import json,sys; [print(s['name'],s['category']) for s in json.load(sys.stdin) if s['category']=='<target>']"` to verify no false positives.
- Test coverage: Zero. No unit tests exist for classification logic.

**YAML frontmatter parser is hand-rolled:**
- Files: `scripts/catalog.py` (lines 292-332)
- Why fragile: The `parse_frontmatter()` function is a best-effort regex parser that skips nested keys, does not handle multiline strings, and may break on edge cases (e.g., colons in values, quoted strings with special chars).
- Safe modification: Test with edge-case SKILL.md files before changing.
- Test coverage: Zero.

**Release script derives category from parent directory name:**
- Files: `scripts/release.sh` (line 72: `category="$(basename "$(dirname "$dir")")"`)
- Why fragile: Curated skill category is inferred from the directory structure (`frontend/adapt/` → category "frontend"). If a skill is nested deeper (e.g., `frontend/react-native-skills/rules/`), the category would be wrong. This also means moving a skill directory changes its release category silently.
- Safe modification: Use frontmatter `category:` field as the primary source.
- Test coverage: Zero.

## Scaling Limits

**Single-file catalog output:**
- Current capacity: 1785 skills produce an 864KB JSON catalog and 230KB Markdown catalog.
- Limit: At 5000+ skills, the JSON catalog will exceed 2MB and the Markdown catalog will be unreadable. GitHub release asset upload may hit limits with thousands of individual `.skill` files.
- Scaling path: Split catalog by category into separate JSON files. Consider a paginated or searchable index.

**Flat wave directories:**
- Current capacity: 13 import waves with skills scattered across them.
- Limit: Wave directories have no deduplication enforcement. As more waves are imported, duplicate detection depends entirely on `catalog.py` name matching, which is case-insensitive but does not compare content.
- Scaling path: Add content hashing (already partially done via `.skillshare-meta.json` `file_hashes`) as a dedup mechanism.

## Dependencies at Risk

**PowerShell scripts for non-Windows users:**
- Risk: 4 out of 8 scripts are `.ps1` files (`audit_global_skillshare_coverage.ps1`, `compare_skill_coverage.ps1`, `import_missing_skills_wave.ps1`, `skillshare_repo_check.ps1`). These require PowerShell, which is not standard on Linux/macOS.
- Files: `scripts/*.ps1`
- Impact: Contributors on Linux/macOS cannot run audit or import scripts without installing PowerShell.
- Migration plan: Port critical scripts to Python (which is already a dependency for `catalog.py` and `infer_risk.py`).

## Missing Critical Features

**No automated quality gate for imports:**
- Problem: When new skills are imported (via `import_missing_skills_wave.ps1` or manual commit), no CI check validates quality. Skills with missing frontmatter, stub content, or duplicate names are merged without detection.
- Blocks: Quality bar goals documented in `docs/QUALITY_BAR.md` cannot be enforced.

**No content deduplication:**
- Problem: Only skill names are checked for duplicates (case-insensitive). Two skills with different names but identical content are not detected. Skills imported from different waves may contain the same underlying content with renamed directories.
- Blocks: Cannot reliably identify redundant skills for cleanup.

**No skill versioning or update tracking:**
- Problem: Skills imported from external repos (tracked via `.skillshare-meta.json` with `version` and `tree_hash`) have no automated mechanism to check for upstream updates. Only 40 skills have `.skillshare-meta.json` files.
- Blocks: Imported skills may become stale as upstream repos evolve.

## Test Coverage Gaps

**Zero automated tests for core scripts:**
- What's not tested: `scripts/catalog.py` (classification, frontmatter parsing, quality checks, duplicate detection), `scripts/infer_risk.py` (risk inference patterns), `scripts/release.sh` (bundle building, validation)
- Files: `scripts/catalog.py`, `scripts/infer_risk.py`, `scripts/release.sh`
- Risk: Classification bugs, false-positive risk ratings, and broken bundle builds go undetected. The 911-out-of-1785 critical risk rate suggests the inference is already producing incorrect results.
- Priority: High. These scripts drive the entire release pipeline.

**No CI validation step:**
- What's not tested: The release workflow runs `catalog.py` and `release.sh` but never checks for errors or quality regressions. A commit that adds 100 broken skills with missing frontmatter will still produce a release.
- Files: `.github/workflows/release.yml`
- Risk: Low-quality skills shipped to users without any quality gate.
- Priority: High.

**No integration test for .skill bundle contents:**
- What's not tested: Whether generated `.skill` ZIP files contain the expected files, have valid frontmatter, and exclude unwanted files (binaries, test data, credentials).
- Files: `scripts/release.sh` (line 163: ZIP creation)
- Risk: Bloated or broken bundles shipped to users.
- Priority: Medium.

---

*Concerns audit: 2026-03-26*
