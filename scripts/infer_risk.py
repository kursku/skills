"""
infer_risk.py — Infer risk level for skills missing the 'risk' frontmatter field.

Uses multi-signal scoring: checks skill instructions/actions (not just description
keywords) to avoid false positives. Aligned with docs/QUALITY_BAR.md risk levels.

Usage:
    python scripts/infer_risk.py                # Dry-run (show what would change)
    python scripts/infer_risk.py --apply        # Apply changes to SKILL.md files
    python scripts/infer_risk.py --all          # Reclassify ALL skills (even already set)
    python scripts/infer_risk.py --stats        # Show statistics only

Risk levels (per QUALITY_BAR.md):
    none      — Pure text/reasoning, no side effects (e.g., brainstorming)
    safe      — Reads files, runs safe commands (e.g., linter, analyzer)
    critical  — Modifies state, deletes files, pushes to prod, handles credentials
    offensive — Pentesting, exploitation, red team tools
"""

import argparse
import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).parent.parent

# Scan both packs/ and top-level curated skill directories
SCAN_DIRS = [
    REPO_ROOT / "packs",
    REPO_ROOT / "frontend",
    REPO_ROOT / "backend",
    REPO_ROOT / "data-ai",
    REPO_ROOT / "tooling",
    REPO_ROOT / "workflow",
    REPO_ROOT / "security",
    REPO_ROOT / "core",
]

# ── Offensive: pentesting, exploitation, red team ────────────────────────────
# These patterns are strong signals — a single match is enough.
OFFENSIVE_SIGNALS = [
    r"pentest",
    r"exploit(?:ation)?",
    r"reverse.?shell",
    r"metasploit",
    r"privilege.?escalat",
    r"sqlmap",
    r"burpsuite|burp.?suite",
    r"red.?team(?:ing)?",
    r"attack.?tree",
    r"malware.?analy",
    r"rootkit",
    r"trojan",
    r"c2.?framework",
    r"command.?and.?control",
    r"buffer.?overflow",
    r"heap.?spray",
    r"rop.?chain",
    r"payload.?generat",
    r"shell.?injection",
    r"offensive.?security",
    r"brute.?force.?attack",
    r"credential.?dump",
    r"password.?crack",
    r"fuzzing.?tool",
    r"vulnerability.?exploit",
]

# ── Critical: modifies state, handles credentials, deploys ───────────────────
# Scored: needs 2+ signals from name+description, OR 1 signal in name.
CRITICAL_SIGNALS_STRONG = [
    # Credential/secret handling
    r"credential.?manag",
    r"secret.?manag",
    r"password.?manag",
    r"vault",
    r"oauth.?flow",
    r"api.?key.?manag",
    # Deployment/infra
    r"deploy(?:ment)?(?:s)?\b",
    r"ci/?cd",
    r"terraform",
    r"kubernetes|k8s",
    r"docker(?:file|.?compose)",
    r"infrastructure.?as.?code",
    # Database mutations
    r"database.?migrat",
    r"schema.?migrat",
    r"drop.?table",
    r"truncate",
    # Destructive operations
    r"rm\s+-rf",
    r"force.?push",
    r"git.?reset.?--hard",
    r"delete.?branch",
    # Social media API integration (sends on behalf of user)
    r"whatsapp.?(?:cloud\s)?api",
    r"instagram.?(?:graph\s)?api",
    r"telegram.?bot.?api",
    r"send.?message.*api",
    r"publish.*(?:post|story|tweet)",
    # Payment processing
    r"stripe.?(?:api|integration|payment)",
    r"payment.?process",
    r"billing.?system",
    r"charge.?customer",
]

CRITICAL_SIGNALS_WEAK = [
    # These only count if combined with other signals
    r"\baws\b",
    r"\bgcp\b",
    r"\bazure\b",
    r"production",
    r"pipeline",
    r"\bssh\b",
    r"\bsmtp\b",
    r"webhook",
    r"encryption",
    r"certificate",
    r"compliance",
    r"\bgdpr\b",
    r"backup.?restor",
]

# ── Safe (not none): reads files, analyzes, generates output ─────────────────
SAFE_SIGNALS = [
    r"analy[sz]",
    r"audit",
    r"review",
    r"lint",
    r"check",
    r"scan",
    r"read",
    r"inspect",
    r"diagnos",
    r"monitor",
    r"generat",
    r"creat",
    r"build",
    r"format",
    r"render",
    r"compil",
    r"test",
]

# ── None: pure text/reasoning, no tool use ───────────────────────────────────
NONE_SIGNALS = [
    r"brainstorm",
    r"ideation",
    r"copywriting",
    r"storytelling",
    r"write.*(?:copy|content|text|article|blog|post|email|headline)",
    r"marketing.*(?:strategy|plan|framework|campaign)",
    r"(?:seo|search).*(?:strategy|plan|audit|analysis)",
    r"pricing.*(?:strategy|model|framework)",
    r"funnel.*(?:strategy|design|template)",
    r"brand.*(?:voice|guide|story|strategy)",
    r"(?:content|editorial).*calendar",
    r"lesson.?plan",
    r"course.*(?:outline|structure|curriculum)",
    r"coaching",
    r"consulting",
    r"framework",
    r"template",
    r"checklist",
    r"playbook",
    r"swipe.?file",
    r"script.*(?:sales|cold|call|outreach)",
    r"(?:client|customer).*(?:journey|persona|avatar)",
]

# Categories that are inherently "none" risk (content/strategy, not tool use)
NONE_CATEGORIES = [
    "conteudo-copy", "01-conteudo-copy",
    "funis-vendas", "03-funis-vendas",
    "redes-sociais", "09-redes-sociais",
    "marca-pessoal", "14-marca-pessoal",
    "nichos-especificos", "16-nichos-especificos",
    "cursos-educacao", "13-cursos-educacao",
    "clientes-consultoria", "10-clientes-consultoria",
    "lancamento-growth", "08-lancamento-growth",
]


def extract_frontmatter(content: str) -> dict[str, str]:
    """Extract YAML frontmatter fields as raw strings."""
    match = re.match(r"^---\s*\n(.*?)\n---", content, re.DOTALL)
    if not match:
        return {}
    fields = {}
    for line in match.group(1).split("\n"):
        m = re.match(r"^(\w[\w-]*):\s*(.*)", line)
        if m:
            fields[m.group(1)] = m.group(2).strip().strip("\"'")
    return fields


def get_existing_risk(content: str) -> str | None:
    """Get existing risk value from frontmatter, or None if not set."""
    match = re.match(r"^---\s*\n(.*?)\n---", content, re.DOTALL)
    if not match:
        return None
    m = re.search(r"^risk:\s*(.+)", match.group(1), re.MULTILINE)
    if not m:
        return None
    return m.group(1).strip().strip("\"'")


def count_matches(text: str, patterns: list[str]) -> int:
    """Count how many distinct patterns match in text."""
    return sum(1 for p in patterns if re.search(p, text))


def get_kit_subfolder(path: Path) -> str:
    """Get the kit subfolder name if this is a kit skill."""
    parts = path.parts
    for i, p in enumerate(parts):
        if "kit-510" in p and i + 1 < len(parts):
            return parts[i + 1]
    return ""


def infer_risk(name: str, description: str, content: str, path: Path) -> str:
    """Infer risk level using multi-signal scoring."""
    # Use name+description for lightweight checks
    meta = f"{name} {description}".lower()
    # Use full content for action-based checks (instructions matter most)
    body = content.lower()

    # 1. Offensive — single strong signal anywhere
    if count_matches(body, OFFENSIVE_SIGNALS) >= 1:
        return "offensive"

    # 2. Critical — need strong evidence of destructive/sensitive actions
    strong_hits = count_matches(body, CRITICAL_SIGNALS_STRONG)
    weak_hits = count_matches(meta, CRITICAL_SIGNALS_WEAK)

    # Strong signal in skill name/description = critical
    if count_matches(meta, CRITICAL_SIGNALS_STRONG) >= 1:
        return "critical"
    # Multiple strong signals in body = critical
    if strong_hits >= 2:
        return "critical"
    # One strong + multiple weak = critical
    if strong_hits >= 1 and weak_hits >= 2:
        return "critical"

    # 3. Check if skill is in a "none" category (content/marketing/strategy)
    kit_sub = get_kit_subfolder(path)
    if kit_sub in NONE_CATEGORIES:
        # Even in none categories, if it has safe signals (tools), mark safe
        if count_matches(body, SAFE_SIGNALS) >= 3:
            return "safe"
        return "none"

    # 4. Check for "none" signals in description (pure text/reasoning)
    none_hits = count_matches(meta, NONE_SIGNALS)
    safe_hits = count_matches(body, SAFE_SIGNALS)

    if none_hits >= 2 and safe_hits < 3:
        return "none"

    # 5. Default: safe (reads, generates, analyzes)
    return "safe"


def set_risk_in_frontmatter(content: str, risk: str) -> str:
    """Set risk: field in frontmatter. Replaces existing or inserts new."""
    match = re.match(r"^(---\s*\n)(.*?)(\n---)", content, re.DOTALL)
    if not match:
        return content
    fm_body = match.group(2)
    if re.search(r"^risk:", fm_body, re.MULTILINE):
        fm_body = re.sub(r"^risk:.*$", f"risk: {risk}", fm_body, flags=re.MULTILINE)
    else:
        fm_body += f"\nrisk: {risk}"
    return f"{match.group(1)}{fm_body}{match.group(3)}{content[match.end():]}"


def main():
    parser = argparse.ArgumentParser(description="Infer risk levels for skills")
    parser.add_argument("--apply", action="store_true", help="Apply changes to files")
    parser.add_argument("--all", action="store_true", help="Reclassify ALL skills")
    parser.add_argument("--stats", action="store_true", help="Show statistics only")
    args = parser.parse_args()

    counts = {"none": 0, "safe": 0, "critical": 0, "offensive": 0}
    total = 0
    skipped = 0
    changed = 0

    for scan_dir in SCAN_DIRS:
        if not scan_dir.exists():
            continue
        for skill_md in sorted(scan_dir.rglob("SKILL.md")):
            total += 1
            content = skill_md.read_text(errors="replace")

            existing_risk = get_existing_risk(content)

            # Skip if already set (unless --all)
            if not args.all and existing_risk and existing_risk not in ("unknown", "none", ""):
                # Allow reclassification of "caution" (non-standard level)
                if existing_risk != "caution":
                    skipped += 1
                    continue

            fm = extract_frontmatter(content)
            name = fm.get("name", skill_md.parent.name)
            description = fm.get("description", "")

            risk = infer_risk(name, description, content, skill_md)
            counts[risk] += 1
            changed += 1

            if not args.stats:
                print(f"  {risk:10s}  {name}")

            if args.apply:
                new_content = set_risk_in_frontmatter(content, risk)
                skill_md.write_text(new_content)

    print()
    print(f"Total: {total} | Skipped (already set): {skipped} | Inferred: {changed}")
    print(f"  none: {counts['none']} | safe: {counts['safe']} | "
          f"critical: {counts['critical']} | offensive: {counts['offensive']}")

    if not args.apply and not args.stats:
        print("\nDry-run complete. Use --apply to write changes.")


if __name__ == "__main__":
    main()
