# External Integrations

**Analysis Date:** 2026-03-26

## APIs & External Services

**GitHub API:**
- Used by the skill installer to download skills from GitHub repos
  - SDK/Client: Python `urllib.request` (stdlib, no external deps)
  - Auth: `GITHUB_TOKEN` or `GH_TOKEN` env var (optional, for rate limit avoidance)
  - Implementation: `.system/skill-installer/scripts/github_utils.py`
  - Endpoints: `https://api.github.com/repos/{repo}/contents/{path}?ref={ref}`

**GitHub CLI (`gh`):**
- Used in CI for creating GitHub Releases and uploading `.skill` artifacts
  - Implementation: `.github/workflows/release.yml` (lines 39-54)
  - Operations: `gh release delete`, `gh release create`
  - Auth: `secrets.GITHUB_TOKEN` (GitHub Actions automatic token)

**Skillshare Registry (runkids/skillshare):**
- External community skill registry that this repo can import from
  - Runner: `tooling/skillshare/scripts/run.sh` — npx-style binary downloader
  - Registry source: `https://github.com/runkids/skillshare`
  - Cache: `$XDG_CACHE_HOME/skillshare` or `$HOME/.cache/skillshare`

## AI Provider Wrappers (Tooling Skills)

These are skills that wrap external AI CLIs for a "deliberation protocol" (multi-model consultation). They are skill content, not repo infrastructure.

**OpenAI Codex CLI:**
- Wrapper: `tooling/codex-ask/codex-wrapper.sh`
- Requires: `codex` CLI installed locally
- Used for: Multi-model deliberation sessions

**Google Gemini CLI:**
- Wrapper: `tooling/gemini-ask/gemini-wrapper.sh`
- Requires: `gemini` CLI installed locally
- Used for: Multi-model deliberation sessions

**Moonshot/Kimi API:**
- Wrapper: `tooling/kimi-ask/kimi-wrapper.sh`
- Requires: `curl` + `KIMI_API_KEY` env var
- Used for: Multi-model deliberation sessions via HTTP API

**Claude (Anthropic):**
- Skill: `tooling/claude-ask/SKILL.md`
- Used for: Multi-model deliberation (self-consultation pattern)

## Data Storage

**Databases:**
- None — This is a file-based catalog repo

**File Storage:**
- Local filesystem only
- `dist/` directory for built `.skill` ZIP archives (gitignored)
- `docs/` directory for JSON reports and documentation

**Caching:**
- None at repo level
- Skillshare runner caches binary at `$HOME/.cache/skillshare/`

## Authentication & Identity

**Auth Provider:**
- None — No user authentication system
- GitHub token used only for API rate limits and CI releases

## Monitoring & Observability

**Error Tracking:**
- None

**Logs:**
- Shell `echo` statements in `scripts/release.sh` (prefixed with `[release]`)
- Python `print()` in `scripts/catalog.py`
- No structured logging

## CI/CD & Deployment

**Hosting:**
- GitHub (source code and releases)
- Skills are distributed as `.skill` ZIP files attached to GitHub Releases

**CI Pipeline:**
- GitHub Actions (`.github/workflows/release.yml`)
- Trigger: Push to `master` branch or manual `workflow_dispatch`
- Runner: `ubuntu-latest`
- Steps:
  1. Checkout code (`actions/checkout@v4`)
  2. Set up Python 3.12 (`actions/setup-python@v5`)
  3. Build catalog (`python3 scripts/catalog.py`)
  4. Build curated `.skill` files (`bash scripts/release.sh`)
  5. Build all pack `.skill` files (`bash scripts/release.sh --packs all`)
  6. Delete previous `latest` release
  7. Create new `latest` release with all `.skill` files attached

**Release Strategy:**
- Rolling `latest` tag — each push to `master` replaces the previous release
- Release title: "Skills — ultima versao"
- All `.skill` files uploaded as release assets

## Environment Configuration

**Required env vars:**
- None for local development (all scripts work without env vars)
- `GITHUB_TOKEN` — Required in CI (provided automatically by GitHub Actions via `secrets.GITHUB_TOKEN`)

**Optional env vars:**
- `GITHUB_TOKEN` or `GH_TOKEN` — For authenticated GitHub API requests in skill installer (avoids rate limits)

**Secrets location:**
- GitHub Actions secrets only (`secrets.GITHUB_TOKEN`)
- No local secrets files

## Webhooks & Callbacks

**Incoming:**
- None

**Outgoing:**
- None

## Target Platform

**claude.ai:**
- Skills are designed to be uploaded to claude.ai Projects as instruction content
- Upload path: claude.ai > Project > Settings > Add content
- `.skill` files are ZIP archives recognized by claude.ai's skill upload feature

**Claude Code / CLI:**
- Skills can also be installed via `skillshare install <skill>` for CLI usage
- Installer: `.system/skill-installer/scripts/install-skill-from-github.py`

---

*Integration audit: 2026-03-26*
