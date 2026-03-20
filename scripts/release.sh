#!/usr/bin/env bash
# release.sh — Build .skill bundles from the repo for upload to claude.ai
#
# Usage:
#   ./scripts/release.sh                         # Build all curated skills (excludes packs/)
#   ./scripts/release.sh --category frontend     # Build only a specific curated category
#   ./scripts/release.sh --packs security        # Build pack skills of a catalog category
#   ./scripts/release.sh --packs all             # Build ALL pack skills (1785 files)
#   ./scripts/release.sh --dry-run               # Show what would be built, no output files
#
# Pack categorization is driven by dist/pack-catalog.json (run scripts/catalog.py first).
# Output: dist/<category>/<skill-name>.skill
#
# A .skill file is a ZIP archive containing the skill's folder contents.
# Required: SKILL.md with YAML frontmatter (name + description fields).

set -euo pipefail

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
DIST_DIR="$REPO_ROOT/dist"
FILTER_CATEGORY=""
PACKS_CATEGORY=""   # if set, build pack skills of this catalog category ("all" = every pack)
DRY_RUN=false

# ── Parse args ───────────────────────────────────────────────────────────────
while [[ $# -gt 0 ]]; do
  case "$1" in
    --category)   FILTER_CATEGORY="$2"; shift ;;
    --packs)      PACKS_CATEGORY="$2"; shift ;;
    --dry-run)    DRY_RUN=true ;;
    --help|-h)
      sed -n '2,17p' "$0" | sed 's/^# //'
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

# ── Collect curated skill directories (non-pack) ──────────────────────────────
SKILL_DIRS=()
SKILL_CATS=()  # parallel array: category for each entry in SKILL_DIRS

if [[ -z "$PACKS_CATEGORY" ]]; then
  # Curated skills only (not in packs/)
  mapfile -t ALL_CURATED < <(
    find "$REPO_ROOT" -name "SKILL.md" \
      ! -path "*/packs/*" \
      ! -path "*/.system/*" \
      ! -path "*/_experimental/*" \
      | sed 's|/SKILL.md$||' \
      | sort
  )
  for dir in "${ALL_CURATED[@]}"; do
    category="$(basename "$(dirname "$dir")")"
    if [[ -n "$FILTER_CATEGORY" && "$category" != "$FILTER_CATEGORY" ]]; then
      continue
    fi
    SKILL_DIRS+=("$dir")
    SKILL_CATS+=("$category")
  done
fi

# ── Collect pack skill directories (catalog-driven) ───────────────────────────
if [[ -n "$PACKS_CATEGORY" ]]; then
  CATALOG="$DIST_DIR/pack-catalog.json"
  if [[ ! -f "$CATALOG" ]]; then
    log "Pack catalog not found. Running scripts/catalog.py first..."
    python3 "$REPO_ROOT/scripts/catalog.py"
  fi

  if ! command -v python3 &>/dev/null; then
    log "ERROR: python3 required for pack catalog filtering."
    exit 1
  fi

  filter_arg="$PACKS_CATEGORY"
  [[ "$filter_arg" == "all" ]] && filter_arg=""

  # Output "path<TAB>category" lines in a single python3 call; avoids per-skill subprocesses
  mapfile -t PACK_PATH_CATS < <(
    python3 - "$CATALOG" "$filter_arg" <<'PYEOF'
import json, sys
catalog = json.load(open(sys.argv[1]))
cat_filter = sys.argv[2] if len(sys.argv) > 2 else ""
for s in catalog:
    if not cat_filter or s["category"] == cat_filter:
        print(s["path"] + "\t" + s["category"])
PYEOF
  )
  for entry in "${PACK_PATH_CATS[@]}"; do
    rel="${entry%%	*}"
    cat="${entry##*	}"
    SKILL_DIRS+=("$REPO_ROOT/$rel")
    SKILL_CATS+=("$cat")
  done
fi

if [[ -n "$PACKS_CATEGORY" && -n "$FILTER_CATEGORY" ]]; then
  log "WARNING: --category is ignored when --packs is set. Use --packs <category> to filter pack skills."
fi

if [[ ${#SKILL_DIRS[@]} -eq 0 ]]; then
  log "No skills found matching the given filters."
  if [[ -n "$PACKS_CATEGORY" ]]; then
    log "Hint: run 'python3 scripts/catalog.py' to rebuild the catalog first."
  fi
  exit 1
fi

log "Found ${#SKILL_DIRS[@]} skill(s) to bundle."
[[ "$DRY_RUN" == true ]] && log "(dry-run mode — no files will be written)"

# ── Build .skill files ────────────────────────────────────────────────────────
BUILT=0
SKIPPED=0
ERRORS=()

build_skill() {
  local skill_dir="$1"
  local category="$2"
  local skill_name
  skill_name="$(basename "$skill_dir")"
  local skill_md="$skill_dir/SKILL.md"

  local status
  status="$(validate_skill "$skill_md")"
  if [[ "$status" != "OK" ]]; then
    ERRORS+=("$category/$skill_name ($status)")
    ((SKIPPED++)) || true
    return
  fi

  local out_dir="$DIST_DIR/$category"
  local out_file="$out_dir/$skill_name.skill"

  if [[ "$DRY_RUN" == true ]]; then
    info "would build → dist/$category/$skill_name.skill"
    ((BUILT++)) || true
    return
  fi

  mkdir -p "$out_dir"
  (
    cd "$skill_dir"
    zip -qr "$out_file" . --exclude "*.DS_Store" --exclude "__pycache__/*"
  )
  ((BUILT++)) || true
}

for i in "${!SKILL_DIRS[@]}"; do
  build_skill "${SKILL_DIRS[$i]}" "${SKILL_CATS[$i]}"
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
