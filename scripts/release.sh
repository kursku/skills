#!/usr/bin/env bash
# release.sh — Build .skill bundles from the repo for upload to claude.ai
#
# Usage:
#   ./scripts/release.sh                    # Build all curated skills (excludes packs/)
#   ./scripts/release.sh --include-packs    # Build everything, including packs/
#   ./scripts/release.sh --category frontend # Build only a specific category
#   ./scripts/release.sh --dry-run          # Show what would be built, no output files
#
# Output: dist/<category>/<skill-name>.skill
#
# A .skill file is a ZIP archive containing the skill's folder contents.
# Required: SKILL.md with YAML frontmatter (name + description fields).

set -euo pipefail

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
DIST_DIR="$REPO_ROOT/dist"
INCLUDE_PACKS=false
FILTER_CATEGORY=""
DRY_RUN=false

# ── Parse args ───────────────────────────────────────────────────────────────
while [[ $# -gt 0 ]]; do
  case "$1" in
    --include-packs)  INCLUDE_PACKS=true ;;
    --category)       FILTER_CATEGORY="$2"; shift ;;
    --dry-run)        DRY_RUN=true ;;
    --help|-h)
      sed -n '2,14p' "$0" | sed 's/^# //'
      exit 0 ;;
    *) echo "Unknown option: $1"; exit 1 ;;
  esac
  shift
done

# ── Helpers ──────────────────────────────────────────────────────────────────
log()  { echo "[release] $*"; }
info() { echo "  $*"; }

validate_skill() {
  local skill_md="$1"
  # Must have a name: and description: in frontmatter
  if ! grep -qE '^name:' "$skill_md"; then
    echo "MISSING_NAME"
    return
  fi
  if ! grep -qE '^description:' "$skill_md"; then
    echo "MISSING_DESC"
    return
  fi
  echo "OK"
}

# ── Collect skill directories ─────────────────────────────────────────────────
mapfile -t ALL_SKILL_DIRS < <(
  find "$REPO_ROOT" -name "SKILL.md" \
    ! -path "*/.system/*" \
    ! -path "*/_experimental/*" \
    | sed 's|/SKILL.md$||' \
    | sort
)

SKILL_DIRS=()
for dir in "${ALL_SKILL_DIRS[@]}"; do
  # Exclude packs unless requested
  if [[ "$dir" == */packs/* ]] && [[ "$INCLUDE_PACKS" == false ]]; then
    continue
  fi
  # Filter by category if specified
  if [[ -n "$FILTER_CATEGORY" ]]; then
    category="$(basename "$(dirname "$dir")")"
    [[ "$category" != "$FILTER_CATEGORY" ]] && continue
  fi
  SKILL_DIRS+=("$dir")
done

if [[ ${#SKILL_DIRS[@]} -eq 0 ]]; then
  log "No skills found matching the given filters."
  exit 1
fi

log "Found ${#SKILL_DIRS[@]} skill(s) to bundle."
[[ "$DRY_RUN" == true ]] && log "(dry-run mode — no files will be written)"

# ── Build .skill files ────────────────────────────────────────────────────────
BUILT=0
SKIPPED=0
ERRORS=()

for skill_dir in "${SKILL_DIRS[@]}"; do
  skill_name="$(basename "$skill_dir")"
  category="$(basename "$(dirname "$skill_dir")")"
  skill_md="$skill_dir/SKILL.md"

  # Validate
  status="$(validate_skill "$skill_md")"
  if [[ "$status" != "OK" ]]; then
    ERRORS+=("$category/$skill_name ($status)")
    ((SKIPPED++)) || true
    continue
  fi

  out_dir="$DIST_DIR/$category"
  out_file="$out_dir/$skill_name.skill"

  if [[ "$DRY_RUN" == true ]]; then
    info "would build → dist/$category/$skill_name.skill"
    ((BUILT++)) || true
    continue
  fi

  mkdir -p "$out_dir"

  # Create zip: contents of skill_dir packed as flat structure
  # (SKILL.md at root of the zip, references/ alongside it)
  (
    cd "$skill_dir"
    zip -qr "$out_file" . --exclude "*.DS_Store" --exclude "__pycache__/*"
  )

  ((BUILT++)) || true
done

# ── Summary ───────────────────────────────────────────────────────────────────
echo ""
log "Done. $BUILT built, $SKIPPED skipped."
if [[ ${#ERRORS[@]} -gt 0 ]]; then
  log "Skipped due to validation errors:"
  for e in "${ERRORS[@]}"; do
    info "  - $e"
  done
fi

if [[ "$DRY_RUN" == false && $BUILT -gt 0 ]]; then
  log "Output: $DIST_DIR/"
  find "$DIST_DIR" -name "*.skill" | sort | while read -r f; do
    rel="${f#"$DIST_DIR/"}"
    size="$(du -sh "$f" 2>/dev/null | cut -f1)"
    info "$rel  ($size)"
  done
fi
