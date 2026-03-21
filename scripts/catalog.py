#!/usr/bin/env python3
"""
catalog.py — Catalog and categorize pack skills into the public taxonomy.

Usage:
    python scripts/catalog.py                      # Catalog all packs
    python scripts/catalog.py --pack global        # Only global-skillshare-import
    python scripts/catalog.py --pack kit           # Only kit-510-ptbr
    python scripts/catalog.py --category security  # Filter output by category
    python scripts/catalog.py --issues-only        # Show only skills with quality issues
    python scripts/catalog.py --json               # Output JSON to stdout

Output:
    dist/pack-catalog.md   — Human-readable catalog grouped by public category
    dist/pack-catalog.json — Machine-readable catalog used by release.sh
"""

import argparse
import json
import os
import re
import sys
from collections import defaultdict
from pathlib import Path

REPO_ROOT = Path(__file__).parent.parent
PACKS_DIR = REPO_ROOT / "packs"
DIST_DIR = REPO_ROOT / "dist"

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
if hasattr(sys.stderr, "reconfigure"):
    sys.stderr.reconfigure(encoding="utf-8", errors="replace")

# ── Public category taxonomy ───────────────────────────────────────────────────
# Order matters: first match wins. More specific patterns should come first.

# Each keyword is matched from a word boundary. More specific patterns must come
# first to avoid broad matches swallowing narrower classes.
CATEGORIES = [
    # ── Security ──────────────────────────────────────────────────────────────
    ("security", [
        "security", "owasp", "pentest", "hardening", "threat model",
        "vulnerability", "sast", "secret scan", "zero trust",
        "csrf", "xss", "firewall", "encryption", "red team",
        "blue team", "active directory", "cyber", "advogado criminal",
        "bug bounty", "malware", "exploit", "injection attack",
        "reverse engineer", "binary analysis", "memory forensics",
        "protocol reverse", "anti reversing", "obfuscat",
        "gdpr", "pci compliance", "pci dss", "wireshark",
        "shodan", "smtp penetration", "ffuf", "web fuzzing",
        "forensic", "zeroize", "semgrep", "vibe code audit",
        "production code audit", "constant time",
        "varlock", "yes md", "yes-md",
    ]),

    # ── Mobile / Games (before frontend) ─────────────────────────────────────
    ("mobile", [
        "mobile", "ios", "android", "expo", "react native", "flutter",
        "swift ui", "swiftui", "jetpack", "kotlin coroutine",
        "android ui", "native data fetching", "expo router",
    ]),

    ("game-dev", [
        "2d game", "3d game", "game art", "game audio", "game design",
        "game development", "game balance", "game content", "unity developer",
        "godot", "unreal engine", "minecraft bukkit", "bevy ecs",
        "three.js", "threejs", "three js",
    ]),

    # ── Docs / Content systems ────────────────────────────────────────────────
    ("docs-content", [
        "document", "documentation", "readme", "wiki ", "wiki-",
        "tutorial", "tutorial engineer", "tutorials", "teach",
        "citation", "latex paper", "paper publisher", "pdf official",
        "pptx official", "xlsx official", "docx official",
        "mermaid", "api document", "openapi", "c4 architect", "c4 ",
        "docs architect", "reference builder", "scientific writing",
        "professional proofreader", "internal comms",
        "avoid ai writing",
    ]),

    # ── Cloud / DevOps / Platform ────────────────────────────────────────────
    ("cloud-devops", [
        "deploy", "kubernetes", "docker", "ci cd", "pipeline",
        "terraform", "prometheus", "grafana", "observabilit",
        "slo ", "sli ", "incident responder", "incident response",
        "incident runbook", "on call", "service mesh", "gitops",
        "helm", "infra", "cloud", "aws", "azure", "gcp", "lambda",
        "serverless", "cloudflare worker", "temporal python",
        "distributed tracing", "distributed debug", "devops",
        "platform engineering", "mtls", "istio", "linkerd",
        "render automation", "vercel deployment", "azure function",
    ]),

    # ── Automation / Integrations ────────────────────────────────────────────
    ("automation", [
        "automation", "zapier", "n8n", "webhook",
        "whatsapp", "telegram", "chatbot", "bot",
        "email automation", "notification", "spreadsheet",
        "process mining", "document auto", "social media auto",
        "scraping", "lead enrich", "make scenario", "n8n workflow",
        "apify ultimate", "playwright", "e2e testing",
        "activecampaign", "airtable", "asana", "brevo", "hubspot",
        "mailchimp", "make automation", "notion automation",
        "slack automation", "github automation", "jira automation",
    ]),

    # ── Frontend / UX / Web interface ────────────────────────────────────────
    ("frontend", [
        "frontend", "react", "vue", "angular", "svelte",
        "tailwind", "landing page", "ui ux", "accessibility",
        "wcag", "html", "css", "web design", "animation",
        "nextjs", "next.js", "astro ", "shadcn", "radix ui",
        "magic ui", "stitch ui", "stitch loop", "scroll experience",
        "canvas design", "iconsax", "interactive portfolio",
        "electron", "chrome extension", "browser extension",
        "makepad", "robius", "hig components", "hig foundations",
        "hig inputs", "hig patterns", "hig platforms",
        "design system", "design spell", "ui skill", "favicon",
        "avalonia", "visual", "metadata",
        "algorithmic art", "chat widget", "remotion", "vizcom",
        "draw", "shader programming glsl",
    ]),

    # ── Backend / APIs / Languages ───────────────────────────────────────────
    ("backend", [
        "backend", "api", "fastapi", "graphql", "grpc", "microservice",
        "supabase", "firebase", "rest api", "api endpoint",
        "node", "flask", "django", "nestjs", "rails", "new rails",
        "rust pro", "rust async", "systems programming rust",
        "golang pro", "go concurrency", "typescript pro", "typescript expert",
        "typescript advanced", "javascript master", "javascript testing",
        "ruby pro", "php pro", "elixir pro", "haskell pro",
        "julia pro", "c pro", "cpp pro", "csharp pro",
        "auth implementation", "jwt", "oauth", "clerk auth",
        "payment integration", "paypal", "stripe",
        "blockchain", "web3", "nft standard", "lightning network",
        "fp errors", "fp either", "fp option", "fp pipe",
        "fp pragmatic", "fp refactor", "fp ts", "cqrs",
        "event sourc", "event store", "domain driven", "ddd tactical",
        "ddd context", "microservices pattern", "nosql", "odoo",
        "salesforce", "m365 agent", "arm cortex", "sql-pro",
        "lightning factory explainer",
    ]),

    # ── Data / AI ─────────────────────────────────────────────────────────────
    ("data-ai", [
        "agent", "orchestrat", "multi agent", "rag", "llm", "langchain",
        "langgraph", "crewai", "autogen", "memory mcp", "tool builder",
        "agentfolio", "agentmail", "agents md", "ai engineer", "ai wrapper",
        "ai agent", "ai ml", "ai native", "ai studio", "ai product",
        "bdi mental", "hosted agent", "agentic", "prompt engineering",
        "mcp builder", "mcp server", "model context protocol",
        "ml engineer", "mlops", "computer use", "voice agent",
        "fal audio", "fal generate", "fal image", "fal upscale",
        "hugging face", "imagen", "skill developer", "skill router",
        "skill sentinel", "subagent", "tool design", "dispatching",
        "context manager", "context guardian", "memory system",
        "similarity search", "vector index", "prompt library",
        "autonomous agent", "computer vision",
        # remaining uncategorized
        "context management", "context optimiz", "data structure protocol",
        "openai docs", "app builder", "blockrun",
        "acceptance orchestrat", "closed loop", "executing plan",
        "skill check", "skill seeker", "using superpower", "superpowers lab",
        "enhance prompt", "vexor", "full stack orchestrat",
        "data engineer", "data pipeline", "data driven", "data warehouse",
        "database", "postgres", "postgresql", "mysql", "sql", "dbt",
        "airflow", "spark", "warehouse", "etl", "streaming",
        "analytics dados", "airtable", "analytics tracking",
        "matplotlib", "plotly", "seaborn", "networkx", "sympy",
        "statsmodel", "backtesting", "quant", "trading strateg",
        "risk metric", "risk manager", "apify audience", "apify content",
        "apify trend", "youtube summarizer", "daily news",
        "astropy", "cirq", "qiskit", "pandas", "numpy",
        "d3.js", "d3js", "data visuali", "claude d3",
        "health analyzer", "health data", "health pattern", "wellally",
        "fitness analyzer", "nutrition analyzer", "sleep analyzer",
        "mental health", "skin health", "oral health", "rehabilitation",
        "family health", "travel health", "occupational health",
        "sexual health", "goal analyzer", "weightloss", "tcm constitution",
        "health assistant", "health trend", "emergency card", "medical",
        "claude ally health", "ai analyzer",
        "ab test setup", "clarity gate", "claude scientific skill",
        "fp data transforms",
        "健康", "营养", "睡眠", "运动", "医疗", "体质",
    ]),

    # ── Workflow / orchestration / planning ──────────────────────────────────
    ("workflow", [
        "workflow", "gsd", "kanban", "planning", "project management",
        "task management", "brainstorming", "kaizen", "conductor",
        "git workflow", "git push", "pull request", "pr writer",
        "create branch", "create issue", "iterate pr", "using git worktree",
        "closed loop", "acceptance orchestrat", "executing plan",
        "finishing a development", "verification before",
        "issues", "linear claude", "peon ping", "diary",
        "address github", "gh review", "rebase",
        "writing plans",
    ]),

    # ── Tooling / CLI / debugging / local DX ─────────────────────────────────
    ("tooling", [
        "tooling", "lint", "validate", "test driven", "tdd", "monorepo",
        "turborepo", "nx workspace", "bazel", "dependency upgrade",
        "code review", "code refactor", "codebase cleanup", "code simplif",
        "codex review", "legacy moderniz", "vibe code", "debugging",
        "error debug", "error diagnostic", "error handling", "error detective",
        "bug hunt", "systematic debug", "performance optim",
        "performance profil", "framework migration", "test fixing",
        "unit testing", "environment setup", "dx optim", "server management",
        "network setup", "web server", "network 101", "project scaffold",
        "cc-skill", "comprehensive review", "claude win11", "speckit",
        "templates", "github actions", "github issue creator", "commit",
        "shellcheck", "posix shell", "bash linux", "linux shell",
        "powershell", "busybox", "python pattern", "python packaging",
        "python performance", "uv package", "dwarf expert", "pypict",
        "search specialist", "tool design", "skill check",
        "architect review", "build", "clean code", "file organizer",
        "memory safety pattern", "modern javascript pattern", "oss hunter",
        "software architecture",
    ]),

    # ── Business / marketing / verticals ─────────────────────────────────────
    ("business", [
        "copywriting", "copy variant", "ad copy", "conteudo",
        "marca pessoal", "redes sociais", "launch email",
        "seo", "viral", "blog", "marketing", "brand",
        "social media", "copy", "email campaign",
        "cro", "conversion rate", "signup flow", "onboarding cro",
        "paywall upgrade", "form cro", "page cro",
        "app store optim", "paid ads",
        "geo fundamentals", "generative engine optim",
        "email sequence", "x article", "professional proofreader",
        "keyword extractor",
        "launch strateg", "business", "sales", "finance", "consulting", "contract",
        "pricing", "funnel", "growth", "b2b", "startup", "yc",
        "pitch", "investor", "revenue", "financeiro", "juridico",
        "advogado", "lancamento", "funil", "vendas",
        "clientes", "consultoria", "nichos", "legal",
        "hr pro", "human resource", "interview coach",
        "andruia", "niche intelligence", "tecnologico",
        "logistics", "supply chain", "carrier relationship",
        "customs trade", "energy procurement", "returns reverse",
        "production scheduling", "quality nonconformance",
        "market sizing", "competitive landscape", "team composition",
        "product manager", "product inventor",
        "segment cdp", "sred project", "leiloeiro",
        "fda food", "fda medtech",
        "elon musk", "ilya sutskever", "steve jobs", "matematico",
        "education", "learning", "course", "cursos", "educacao", "training",
        "notion", "obsidian", "speed reader", "unsplash",
        "i18n", "localization", "explain like", "ask questions if",
        "claude code guide",
    ]),
]

# kit-510-ptbr explicit mapping to public categories
KIT_CATEGORY_MAP = {
    "00-utilitarios-negocio":  "utilitarios-negocio",
    "00-utilitarios-tecnicos": "utilitarios-tecnicos",
    "01-conteudo-copy":        "conteudo-copy",
    "02-email-automacao":      "email-automacao",
    "03-funis-vendas":         "funis-vendas",
    "04-anuncios-trafego":     "anuncios-trafego",
    "05-seo-busca":            "seo-busca",
    "06-financeiro-precos":    "financeiro-precos",
    "07-juridico-compliance":  "juridico-compliance",
    "08-lancamento-growth":    "lancamento-growth",
    "09-redes-sociais":        "redes-sociais",
    "10-clientes-consultoria": "clientes-consultoria",
    "11-operacoes-sistemas":   "operacoes-sistemas",
    "12-ia-automacao":         "ia-automacao",
    "13-cursos-educacao":      "cursos-educacao",
    "14-marca-pessoal":        "marca-pessoal",
    "15-analytics-dados":      "analytics-dados",
    "16-nichos-especificos":   "nichos-especificos",
}


# ── Frontmatter parser ─────────────────────────────────────────────────────────

def parse_frontmatter(path: Path) -> dict:
    """Parse YAML-ish frontmatter from a SKILL.md file (best-effort, no deps)."""
    try:
        text = path.read_text(encoding="utf-8", errors="replace")
    except Exception:
        return {}

    if not text.startswith("---"):
        return {}

    end = text.find("\n---", 3)
    if end == -1:
        return {}

    fm_text = text[3:end]
    result = {}
    current_key = None
    list_items: list[str] = []

    def flush():
        if current_key and list_items:
            result[current_key] = list_items[:]

    for line in fm_text.splitlines():
        if line.startswith("  ") and current_key:
            # nested key (metadata: block) — skip
            continue
        list_match = re.match(r"^- (.+)$", line)
        kv_match = re.match(r"^(\w[\w-]*): ?(.*)", line)

        if list_match and current_key is not None:
            list_items.append(list_match.group(1).strip())
        elif kv_match:
            flush()
            current_key = kv_match.group(1)
            val = kv_match.group(2).strip().strip("'\"")
            result[current_key] = val
            list_items = []

    flush()  # save the last list field
    return result


# ── Category classifier ────────────────────────────────────────────────────────

def classify(name: str, description: str, tags: list, kit_subfolder: str = "") -> str:
    """Assign a public category. Returns 'uncategorized' if no match."""

    # 1. Use kit folder map if available
    if kit_subfolder and kit_subfolder in KIT_CATEGORY_MAP:
        return KIT_CATEGORY_MAP[kit_subfolder]

    # 2. Combine searchable text; normalize hyphens/underscores to spaces
    haystack = " ".join([name, description, *tags]).lower()
    haystack = re.sub(r"[-_]", " ", haystack)

    for category, keywords in CATEGORIES:
        for kw in keywords:
            kw_norm = re.sub(r"[-_]", " ", kw.lower())
            # Left-boundary only: keyword must start at a word boundary but can
            # be followed by suffixes/plurals (e.g. "agent" matches "agents",
            # "orchestrat" matches "orchestrator"/"orchestration").
            # The left boundary prevents false positives like "ci" in "social".
            if re.search(r"(?<!\w)" + re.escape(kw_norm), haystack):
                return category

    return "uncategorized"


# ── Quality issues ────────────────────────────────────────────────────────────

def quality_issues(fm: dict) -> list[str]:
    issues = []
    if not fm.get("name"):
        issues.append("missing-name")
    if not fm.get("description") or len(fm.get("description", "")) < 20:
        issues.append("description-too-short")
    risk = fm.get("risk", "")
    if risk in ("unknown", "", "none"):
        issues.append("risk-unset")
    name = fm.get("name", "")
    description = fm.get("description", "")
    if name and description and name.lower() in description.lower() and len(description) < 60:
        issues.append("description-generic")
    return issues


# ── Skill loader ──────────────────────────────────────────────────────────────

def load_skills(pack_filter: str = "") -> list[dict]:
    skills = []
    seen_names: dict[str, list[str]] = defaultdict(list)

    packs = [d for d in PACKS_DIR.iterdir() if d.is_dir()]
    if pack_filter == "global":
        packs = [p for p in packs if "global" in p.name]
    elif pack_filter == "kit":
        packs = [p for p in packs if "kit" in p.name]

    for pack_dir in sorted(packs):
        for skill_md in sorted(pack_dir.rglob("SKILL.md")):
            fm = parse_frontmatter(skill_md)
            if not fm:
                continue

            name = fm.get("name", skill_md.parent.name)
            description = fm.get("description", "")
            tags = fm.get("tags", [])
            if isinstance(tags, str):
                tags = [tags]

            # Detect kit sub-category folder
            rel = skill_md.relative_to(pack_dir)
            parts = rel.parts
            kit_subfolder = parts[0] if len(parts) >= 3 and "kit" in pack_dir.name else ""
            wave = parts[0] if len(parts) >= 3 and "global" in pack_dir.name else ""

            category = classify(name, description, tags, kit_subfolder)
            issues = quality_issues(fm)

            skill = {
                "name": str(name),
                "description": str(description),
                "category": category,
                "public_category": category,
                "pack": pack_dir.name,
                "wave": wave,
                "kit_subfolder": kit_subfolder,
                "source_pack": pack_dir.name,
                "source_wave": wave,
                "source_group": kit_subfolder or wave,
                "path": str(skill_md.parent.relative_to(REPO_ROOT)),
                "risk": fm.get("risk", "unknown"),
                "source": fm.get("source", ""),
                "tags": tags if isinstance(tags, list) else [],
                "issues": issues,
            }
            skills.append(skill)
            seen_names[str(name).lower()].append(skill["path"])

    # Mark duplicates
    for skill in skills:
        if len(seen_names[skill["name"].lower()]) > 1:
            if "duplicate-name" not in skill["issues"]:
                skill["issues"].append("duplicate-name")

    return skills


# ── Reporters ─────────────────────────────────────────────────────────────────

def write_catalog_json(skills: list[dict], out: Path):
    out.parent.mkdir(parents=True, exist_ok=True)
    with open(out, "w", encoding="utf-8") as f:
        json.dump(skills, f, ensure_ascii=False, indent=2)
    print(f"[catalog] JSON -> {out}  ({len(skills)} skills)")


def write_catalog_md(skills: list[dict], out: Path):
    out.parent.mkdir(parents=True, exist_ok=True)

    by_category: dict[str, list[dict]] = defaultdict(list)
    for s in skills:
        by_category[s["category"]].append(s)

    # Issue summary
    total = len(skills)
    with_issues = sum(1 for s in skills if s["issues"])
    duplicates = sum(1 for s in skills if "duplicate-name" in s["issues"])
    risk_unknown = sum(1 for s in skills if "risk-unset" in s["issues"])

    lines = [
        "# Public Skills Catalog",
        "",
        f"**Total:** {total} skills across {len(by_category)} public categories",
        "",
        "## Quality Overview",
        "",
        f"| Issue | Count |",
        f"|-------|-------|",
        f"| Skills with any issue | {with_issues} |",
        f"| Duplicate names | {duplicates} |",
        f"| risk: unknown / unset | {risk_unknown} |",
        f"| Uncategorized | {len(by_category.get('uncategorized', []))} |",
        "",
        "---",
        "",
    ]

    for category in sorted(by_category.keys()):
        cat_skills = sorted(by_category[category], key=lambda s: s["name"].lower())
        lines.append(f"## {category}  ({len(cat_skills)} skills)")
        lines.append("")
        lines.append("| Skill | Pack | Risk | Issues |")
        lines.append("|-------|------|------|--------|")
        for s in cat_skills:
            issue_str = ", ".join(s["issues"]) if s["issues"] else "—"
            risk = s["risk"] or "—"
            pack_short = "global" if "global" in s["pack"] else "kit"
            desc = s["description"][:70] + "…" if len(s["description"]) > 70 else s["description"]
            # Escape pipe chars that would break Markdown table cells
            safe_name = s["name"].replace("|", "\\|")
            safe_desc = desc.replace("|", "\\|")
            lines.append(f"| **{safe_name}** — {safe_desc} | {pack_short} | {risk} | {issue_str} |")
        lines.append("")

    with open(out, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))
    print(f"[catalog] MD  -> {out}  ({total} skills, {len(by_category)} categories)")


def print_issues_report(skills: list[dict]):
    problematic = [s for s in skills if s["issues"]]
    print(f"\n{'='*60}")
    print(f"QUALITY ISSUES — {len(problematic)} of {len(skills)} skills")
    print(f"{'='*60}\n")

    # Group by issue type
    by_issue: dict[str, list[dict]] = defaultdict(list)
    for s in problematic:
        for issue in s["issues"]:
            by_issue[issue].append(s)

    for issue, affected in sorted(by_issue.items(), key=lambda x: -len(x[1])):
        print(f"### {issue}  ({len(affected)} skills)")
        for s in affected[:10]:
            print(f"  - {s['name']}  [{s['pack']}]  {s['path']}")
        if len(affected) > 10:
            print(f"  ... and {len(affected) - 10} more")
        print()


# ── Main ──────────────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--pack", choices=["global", "kit", ""], default="", help="Filter by pack")
    parser.add_argument("--category", default="", help="Filter output by canonical category")
    parser.add_argument("--issues-only", action="store_true", help="Print quality issues report")
    parser.add_argument("--json", action="store_true", help="Output JSON to stdout instead of file")
    args = parser.parse_args()

    print(f"[catalog] Loading skills from {PACKS_DIR}...", file=sys.stderr)
    skills = load_skills(pack_filter=args.pack)

    if args.category:
        skills = [s for s in skills if s["category"] == args.category]

    if args.json:
        json.dump(skills, sys.stdout, ensure_ascii=False, indent=2)
        return

    if args.issues_only:
        print_issues_report(skills)
        return

    DIST_DIR.mkdir(parents=True, exist_ok=True)
    write_catalog_json(skills, DIST_DIR / "pack-catalog.json")
    write_catalog_md(skills, DIST_DIR / "pack-catalog.md")

    # Summary by category
    by_cat: dict[str, int] = defaultdict(int)
    for s in skills:
        by_cat[s["category"]] += 1

    print("\n[catalog] Category breakdown:")
    for cat, count in sorted(by_cat.items(), key=lambda x: -x[1]):
        bar = "#" * (count // 10)
        print(f"  {cat:<20} {count:>4}  {bar}")

    total_issues = sum(1 for s in skills if s["issues"])
    print(f"\n[catalog] {len(skills)} skills indexed. {total_issues} with quality issues.")
    print(f"          Run with --issues-only for full quality report.")


if __name__ == "__main__":
    main()
