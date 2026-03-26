"""
infer_risk.py — Infer risk level for skills missing the 'risk' frontmatter field.

Reads each SKILL.md, analyzes content, and adds a 'risk:' field to the YAML
frontmatter. Does NOT overwrite existing risk values.

Usage:
    python scripts/infer_risk.py                # Dry-run (show what would change)
    python scripts/infer_risk.py --apply        # Apply changes to SKILL.md files
    python scripts/infer_risk.py --stats        # Show statistics only

Risk levels:
    safe      — Read-only, informational, no external side effects
    caution   — Writes files, calls APIs, modifies state
    critical  — Handles credentials, deploys, accesses sensitive systems
    offensive — Pentesting, exploitation, red team tools
"""

import argparse
import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).parent.parent
PACKS_DIR = REPO_ROOT / "packs"

# Patterns that indicate each risk level (checked against name + description + content)
OFFENSIVE_PATTERNS = [
    r"pentest", r"exploit", r"payload", r"reverse.?shell", r"metasploit",
    r"brute.?force", r"privilege.?escalat", r"sqlmap", r"burpsuite",
    r"red.?team", r"attack.?tree", r"vulnerability.?scan", r"fuzzing",
    r"offensive", r"malware", r"rootkit", r"keylogger", r"trojan",
    r"c2.?framework", r"command.?and.?control", r"shell.?injection",
    r"buffer.?overflow", r"heap.?spray", r"rop.?chain",
]

CRITICAL_PATTERNS = [
    r"credential", r"secret", r"password", r"api.?key", r"oauth",
    r"deploy", r"production", r"ci/?cd", r"pipeline", r"infra",
    r"docker", r"kubernetes", r"k8s", r"terraform", r"aws",
    r"gcp", r"azure", r"database.?migrat", r"backup",
    r"webhook", r"smtp", r"ssh", r"ssl", r"tls",
    r"payment", r"stripe", r"billing", r"financial",
    r"whatsapp.?api", r"instagram.?api", r"telegram.?api",
    r"graph.?api", r"social.?media.?api",
    r"gdpr", r"compliance", r"hipaa", r"pci",
    r"encryption", r"certificate", r"vault",
]

CAUTION_PATTERNS = [
    r"automat", r"integra", r"api", r"webhook",
    r"write", r"create", r"update", r"delete", r"modify",
    r"scrape", r"crawl", r"bot", r"send.?email",
    r"publish", r"post", r"upload",
    r"cron", r"schedule", r"trigger",
    r"file.?system", r"disk", r"storage",
    r"database", r"sql", r"query",
    r"mutation", r"graphql.?mutation",
]


def extract_frontmatter(content: str) -> tuple[dict[str, str], int, int]:
    """Extract YAML frontmatter fields as raw strings. Returns (fields, start, end)."""
    match = re.match(r"^---\s*\n(.*?)\n---", content, re.DOTALL)
    if not match:
        return {}, 0, 0
    fm_text = match.group(1)
    fields = {}
    for line in fm_text.split("\n"):
        m = re.match(r"^(\w[\w-]*):\s*(.*)", line)
        if m:
            fields[m.group(1)] = m.group(2).strip().strip("\"'")
    return fields, match.start(), match.end()


def get_existing_risk(content: str) -> str | None:
    """Get existing risk value from frontmatter, or None if not set."""
    match = re.match(r"^---\s*\n(.*?)\n---", content, re.DOTALL)
    if not match:
        return None
    m = re.search(r"^risk:\s*(.+)", match.group(1), re.MULTILINE)
    if not m:
        return None
    return m.group(1).strip().strip("\"'")


def infer_risk(name: str, description: str, content: str) -> str:
    """Infer risk level from skill name, description, and full content."""
    text = f"{name} {description} {content}".lower()

    for pattern in OFFENSIVE_PATTERNS:
        if re.search(pattern, text):
            return "offensive"

    for pattern in CRITICAL_PATTERNS:
        if re.search(pattern, text):
            return "critical"

    for pattern in CAUTION_PATTERNS:
        if re.search(pattern, text):
            return "caution"

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
    parser.add_argument("--stats", action="store_true", help="Show statistics only")
    args = parser.parse_args()

    counts = {"safe": 0, "caution": 0, "critical": 0, "offensive": 0}
    total = 0
    skipped = 0
    changed = 0

    for skill_md in sorted(PACKS_DIR.rglob("SKILL.md")):
        total += 1
        content = skill_md.read_text(errors="replace")

        existing_risk = get_existing_risk(content)

        # Skip if already has a meaningful risk value
        if existing_risk and existing_risk not in ("unknown", "none", ""):
            skipped += 1
            continue

        fm, _, _ = extract_frontmatter(content)
        name = fm.get("name", skill_md.parent.name)
        description = fm.get("description", "")

        risk = infer_risk(name, description, content)
        counts[risk] += 1
        changed += 1

        if not args.stats:
            print(f"  {risk:10s}  {name}")

        if args.apply:
            new_content = set_risk_in_frontmatter(content, risk)
            skill_md.write_text(new_content)

    print()
    print(f"Total: {total} | Skipped (already set): {skipped} | Inferred: {changed}")
    print(f"  safe: {counts['safe']} | caution: {counts['caution']} | "
          f"critical: {counts['critical']} | offensive: {counts['offensive']}")

    if not args.apply and not args.stats:
        print("\nDry-run complete. Use --apply to write changes.")


if __name__ == "__main__":
    main()
