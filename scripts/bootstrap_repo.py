#!/usr/bin/env python3
"""
bootstrap_repo.py — Configura um repositorio de skills com estrutura completa.

Pega um repo de skills (gerado pelo skillshare ou manual) e aplica:
- Organizacao por categorias com READMEs
- Scripts de catalogo, risk inference e testes
- CI/CD (GitHub Actions release workflow + quality gate)
- README principal com passo a passo visual
- Docs traduzidos em PT-BR
- .gitignore completo

Uso:
    python3 bootstrap_repo.py                    # Interativo
    python3 bootstrap_repo.py --repo-name "meu-repo" --github-user "usuario"
    python3 bootstrap_repo.py --dry-run          # Mostra o que faria sem alterar

Requisitos:
    - Python 3.10+
    - Rodar na raiz do repositorio de skills
"""

import argparse
import json
import os
import re
import shutil
import sys
from pathlib import Path


# ── Default categories for marketing/content repos ──────────────────────────
DEFAULT_CATEGORIES = {
    "conteudo-copy": {
        "title": "Conteudo & Copy",
        "desc": "Skills para copywriting, headlines, roteiros, posts e materiais persuasivos.",
        "keywords": ["copy", "headline", "roteiro", "post", "content", "blog", "newsletter",
                      "storytelling", "script", "video script", "carousel", "caption"],
    },
    "email-automacao": {
        "title": "Email & Automacao",
        "desc": "Skills para sequencias de email, automacoes, campanhas e nurturing.",
        "keywords": ["email", "automacao", "automation", "drip", "nurture", "sequence",
                      "newsletter", "welcome", "onboarding email"],
    },
    "funis-vendas": {
        "title": "Funis de Vendas",
        "desc": "Skills para funis, ofertas, checkout, upsell e estrategia comercial.",
        "keywords": ["funnel", "funil", "checkout", "upsell", "downsell", "offer",
                      "sales", "venda", "pricing", "launch"],
    },
    "anuncios-trafego": {
        "title": "Anuncios & Trafego",
        "desc": "Skills para Meta Ads, Google Ads, TikTok Ads, criativos e tracking.",
        "keywords": ["ads", "trafego", "traffic", "meta ads", "google ads", "tiktok",
                      "campaign", "tracking", "pixel", "retarget"],
    },
    "seo-busca": {
        "title": "SEO & Busca",
        "desc": "Skills para SEO tecnico, conteudo organico, keywords e rankeamento.",
        "keywords": ["seo", "keyword", "search", "rank", "serp", "backlink", "organic",
                      "indexing", "schema", "sitemap"],
    },
    "redes-sociais": {
        "title": "Redes Sociais",
        "desc": "Skills para conteudo, engajamento e crescimento em redes sociais.",
        "keywords": ["social media", "instagram", "linkedin", "tiktok", "twitter",
                      "reels", "stories", "hashtag", "engagement", "community"],
    },
    "ia-automacao": {
        "title": "IA & Automacao",
        "desc": "Skills para IA aplicada, agentes, chatbots e integracoes inteligentes.",
        "keywords": ["ai", "ia", "agent", "chatbot", "llm", "prompt", "automation",
                      "n8n", "zapier", "make", "workflow"],
    },
    "marca-pessoal": {
        "title": "Marca Pessoal",
        "desc": "Skills para autoridade, reputacao, networking e presenca profissional.",
        "keywords": ["brand", "marca", "personal brand", "authority", "reputation",
                      "networking", "thought leader", "speaking"],
    },
    "negocios": {
        "title": "Negocios & Estrategia",
        "desc": "Skills para gestao, financas, clientes, operacoes e estrategia.",
        "keywords": ["business", "negocio", "strategy", "client", "consulting",
                      "pricing", "finance", "operation", "management", "legal"],
    },
    "desenvolvimento": {
        "title": "Desenvolvimento",
        "desc": "Skills para frontend, backend, DevOps e engenharia de software.",
        "keywords": ["react", "next", "node", "python", "api", "deploy", "docker",
                      "database", "frontend", "backend", "devops", "code"],
    },
}


def find_skills(root: Path) -> list[dict]:
    """Find all SKILL.md files and extract metadata."""
    skills = []
    for skill_md in sorted(root.rglob("SKILL.md")):
        # Skip template
        if "template" in str(skill_md).lower() and skill_md.parent.name == "template":
            continue
        # Skip hidden dirs
        if any(p.startswith(".") for p in skill_md.parts):
            continue

        content = skill_md.read_text(errors="replace")
        match = re.match(r"^---\s*\n(.*?)\n---", content, re.DOTALL)
        fm = {}
        if match:
            for line in match.group(1).split("\n"):
                m = re.match(r"^(\w[\w-]*):\s*(.*)", line)
                if m:
                    fm[m.group(1)] = m.group(2).strip().strip("\"'")

        name = fm.get("name", skill_md.parent.name)
        description = fm.get("description", "")

        skills.append({
            "name": name,
            "description": description,
            "path": str(skill_md.parent.relative_to(root)),
            "risk": fm.get("risk", ""),
            "source": fm.get("source", ""),
            "frontmatter": fm,
            "skill_md": skill_md,
        })

    return skills


def classify_skill(skill: dict, categories: dict) -> str:
    """Classify a skill into a category based on keywords."""
    text = f"{skill['name']} {skill['description']}".lower()

    best_cat = "outros"
    best_score = 0

    for cat_id, cat_info in categories.items():
        score = sum(1 for kw in cat_info["keywords"] if kw.lower() in text)
        if score > best_score:
            best_score = score
            best_cat = cat_id

    return best_cat


def generate_gitignore() -> str:
    return """# Build artifacts
dist/

# Planning (internal)
.planning/

# Python
*.pyc
__pycache__/
.pytest_cache/

# Node
node_modules/

# Environment
.env
.env.*

# OS
.DS_Store
Thumbs.db

# IDE
.vscode/
.idea/

# Temporary files
*.tmp
*.bak
"""


def generate_release_workflow(repo_name: str) -> str:
    return f"""name: Release Skills

on:
  push:
    branches:
      - main
      - master
  workflow_dispatch:

permissions:
  contents: write

jobs:
  release:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout
        uses: actions/checkout@v4

      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: "3.12"

      - name: Install test dependencies
        run: pip install pytest

      - name: Run tests
        run: python3 -m pytest scripts/test_catalog.py scripts/test_infer_risk.py -v

      - name: Build catalog
        run: python3 scripts/catalog.py

      - name: Quality gate
        run: |
          python3 -c "
          import json, sys
          with open('dist/pack-catalog.json') as f:
              catalog = json.load(f)
          missing_name = sum(1 for s in catalog if 'missing-name' in s.get('issues', []))
          if missing_name > 0:
              print(f'FAIL: {{missing_name}} skills missing name')
              sys.exit(1)
          print(f'OK: {{len(catalog)}} skills indexed, no critical issues')
          "

      - name: Build .skill files
        run: bash scripts/release.sh --packs all

      - name: Package skills by category
        run: |
          mkdir -p dist/release
          for category_dir in dist/*/; do
            category=$(basename "$category_dir")
            [ "$category" = "release" ] && continue
            skill_count=$(find "$category_dir" -name "*.skill" | wc -l)
            [ "$skill_count" -eq 0 ] && continue
            (cd dist && zip -qr "release/${{category}}.zip" "$category"/*)
          done

      - name: Delete existing latest release
        env:
          GH_TOKEN: ${{{{ secrets.GITHUB_TOKEN }}}}
        run: |
          gh release delete latest --yes 2>/dev/null || true
          git push --delete origin latest 2>/dev/null || true

      - name: Create release and upload skills
        env:
          GH_TOKEN: ${{{{ secrets.GITHUB_TOKEN }}}}
        run: |
          gh release create latest \\
            --title "Skills — ultima versao" \\
            --notes "Arquivos de skills organizados por categoria." \\
            --latest \\
            dist/release/*.zip
"""


def generate_readme(repo_name: str, github_user: str, categories: dict,
                    skill_counts: dict, total_skills: int) -> str:
    lines = [
        f"# Skills para Claude — +{total_skills} skills prontas para usar",
        "",
        f"[![Skills](https://img.shields.io/badge/skills-{total_skills}%2B-blue)]"
        f"(https://github.com/{github_user}/{repo_name}) "
        f"[![PT-BR](https://img.shields.io/badge/idioma-PT--BR-yellow)]"
        f"(https://github.com/{github_user}/{repo_name})",
        "",
        "O [Claude](https://claude.ai) e um assistente de IA da Anthropic. "
        "**Skills** sao instrucoes que ensinam o Claude a dominar tarefas especificas "
        "— como contratar um especialista sob demanda.",
        "",
        "---",
        "",
        "## Como usar",
        "",
        "**1.** Escolha uma skill nas categorias abaixo",
        "",
        "**2.** Clique em **[Ver skill]** e baixe o arquivo `SKILL.md`",
        "",
        "**3.** No [claude.ai](https://claude.ai), va em **Personalizar** → **Habilidades** → **+**",
        "",
        "**4.** Faca upload do arquivo. O Claude agora e especialista naquele assunto!",
        "",
        "> **Dica:** voce pode adicionar varias skills — elas ficam disponiveis em todos os seus chats.",
        "",
        "---",
        "",
        "## Categorias",
        "",
        "| Categoria | Skills | Descricao |",
        "|-----------|:------:|-----------|",
    ]

    for cat_id, cat_info in categories.items():
        count = skill_counts.get(cat_id, 0)
        if count > 0:
            lines.append(f"| [{cat_info['title']}](./{cat_id}/) | {count} | {cat_info['desc']} |")

    # Add "outros" if it has skills
    if skill_counts.get("outros", 0) > 0:
        lines.append(f"| [Outros](./outros/) | {skill_counts['outros']} | Skills diversas e utilitarias |")

    lines += [
        "",
        "---",
        "",
        "## Perguntas frequentes",
        "",
        "**Preciso pagar para usar?**",
        "As skills sao gratuitas. Voce so precisa de uma conta no [claude.ai](https://claude.ai) (tem plano gratuito).",
        "",
        "**Posso usar varias skills ao mesmo tempo?**",
        "Sim. Adicione quantas quiser — elas ficam disponiveis em todos os seus chats.",
        "",
        "---",
        "",
        "## Contribuindo",
        "",
        "1. Faca um fork do repositorio",
        "2. Crie sua skill seguindo o formato `SKILL.md` (veja o [template](./docs/SKILL_TEMPLATE.md))",
        "3. Abra um Pull Request",
        "",
        f"Duvidas? Abra uma [issue](https://github.com/{github_user}/{repo_name}/issues).",
        "",
    ]

    return "\n".join(lines)


def generate_category_readme(cat_info: dict, skills: list[dict]) -> str:
    lines = [
        f"# {cat_info['title']}",
        "",
        cat_info["desc"],
        "",
        "---",
        "",
    ]

    for skill in sorted(skills, key=lambda s: s["name"]):
        desc = skill["description"]
        if len(desc) > 150:
            desc = desc[:147] + "..."
        if not desc:
            desc = skill["name"].replace("-", " ").title()

        lines += [
            f"### {skill['name']}",
            desc,
            "",
            f"[Ver skill](../{skill['path']}/)",
            "",
            "---",
            "",
        ]

    lines.append("[← Voltar para todas as categorias](../README.md)")
    return "\n".join(lines)


def copy_scripts(source_repo: Path, target_repo: Path):
    """Copy essential scripts from source to target repo."""
    scripts_to_copy = [
        "scripts/catalog.py",
        "scripts/infer_risk.py",
        "scripts/release.sh",
        "scripts/test_catalog.py",
        "scripts/test_infer_risk.py",
    ]
    (target_repo / "scripts").mkdir(exist_ok=True)

    for script in scripts_to_copy:
        src = source_repo / script
        dst = target_repo / script
        if src.exists():
            shutil.copy2(src, dst)
            print(f"  Copiado: {script}")


def copy_docs(source_repo: Path, target_repo: Path):
    """Copy essential docs from source to target repo."""
    docs_to_copy = [
        "docs/QUALITY_BAR.md",
        "docs/SKILL_ANATOMY.md",
        "docs/SKILL_TEMPLATE.md",
        "docs/COMMUNITY_GUIDELINES.md",
        "docs/FAQ.md",
        "docs/COMO_CRIAR_SKILL.md",
    ]
    (target_repo / "docs").mkdir(exist_ok=True)

    for doc in docs_to_copy:
        src = source_repo / doc
        dst = target_repo / doc
        if src.exists():
            shutil.copy2(src, dst)
            print(f"  Copiado: {doc}")


def copy_assets(source_repo: Path, target_repo: Path):
    """Copy screenshot assets."""
    src_assets = source_repo / "docs" / "assets"
    dst_assets = target_repo / "docs" / "assets"
    if src_assets.exists():
        dst_assets.mkdir(parents=True, exist_ok=True)
        for f in src_assets.iterdir():
            if f.suffix.lower() in (".png", ".jpg", ".gif"):
                shutil.copy2(f, dst_assets / f.name)
                print(f"  Copiado: docs/assets/{f.name}")


def main():
    parser = argparse.ArgumentParser(description="Bootstrap um repo de skills")
    parser.add_argument("--repo-name", help="Nome do repositorio")
    parser.add_argument("--github-user", help="Username do GitHub")
    parser.add_argument("--source-repo", default=str(Path(__file__).parent.parent),
                        help="Repo fonte para copiar scripts/docs (default: este repo)")
    parser.add_argument("--target", default=".", help="Diretorio do repo alvo (default: .)")
    parser.add_argument("--dry-run", action="store_true", help="Mostra o que faria sem alterar")
    args = parser.parse_args()

    target = Path(args.target).resolve()
    source = Path(args.source_repo).resolve()

    if not (target / ".git").exists() and not args.dry_run:
        print(f"ERRO: {target} nao e um repositorio git.")
        print("Rode este script na raiz do repositorio de skills.")
        sys.exit(1)

    # Interactive prompts if not provided
    repo_name = args.repo_name or input("Nome do repositorio (ex: minhas-skills): ").strip()
    github_user = args.github_user or input("Username do GitHub: ").strip()

    if not repo_name or not github_user:
        print("ERRO: repo-name e github-user sao obrigatorios.")
        sys.exit(1)

    print(f"\n{'[DRY-RUN] ' if args.dry_run else ''}Configurando repo: {github_user}/{repo_name}")
    print(f"  Alvo: {target}")
    print(f"  Fonte: {source}")

    # 1. Find existing skills
    print("\n1. Buscando skills existentes...")
    skills = find_skills(target)
    print(f"  Encontradas: {len(skills)} skills")

    if len(skills) == 0:
        print("  AVISO: Nenhuma skill encontrada. O repo sera configurado vazio.")

    # 2. Classify skills
    print("\n2. Classificando skills por categoria...")
    categories = DEFAULT_CATEGORIES.copy()
    skill_by_cat: dict[str, list] = {cat: [] for cat in categories}
    skill_by_cat["outros"] = []

    for skill in skills:
        cat = classify_skill(skill, categories)
        skill_by_cat[cat].append(skill)

    skill_counts = {cat: len(skills) for cat, skills in skill_by_cat.items()}
    for cat, count in sorted(skill_counts.items(), key=lambda x: -x[1]):
        if count > 0:
            title = categories.get(cat, {}).get("title", cat.title())
            print(f"  {title}: {count} skills")

    if args.dry_run:
        print("\n[DRY-RUN] Arquivos que seriam criados:")
        print("  .gitignore")
        print("  README.md")
        print("  .github/workflows/release.yml")
        print("  scripts/ (5 arquivos)")
        print("  docs/ (6 arquivos)")
        for cat, cat_skills in skill_by_cat.items():
            if cat_skills:
                print(f"  {cat}/README.md")
        print("\nRode sem --dry-run para aplicar.")
        return

    # 3. Create .gitignore
    print("\n3. Criando .gitignore...")
    (target / ".gitignore").write_text(generate_gitignore())

    # 4. Copy scripts
    print("\n4. Copiando scripts...")
    copy_scripts(source, target)

    # 5. Copy docs
    print("\n5. Copiando docs...")
    copy_docs(source, target)

    # 6. Copy assets
    print("\n6. Copiando assets (screenshots)...")
    copy_assets(source, target)

    # 7. Create CI workflow
    print("\n7. Criando workflow de CI/CD...")
    workflows_dir = target / ".github" / "workflows"
    workflows_dir.mkdir(parents=True, exist_ok=True)
    (workflows_dir / "release.yml").write_text(generate_release_workflow(repo_name))

    # 8. Create category directories with READMEs
    print("\n8. Criando categorias com READMEs...")
    for cat_id, cat_skills in skill_by_cat.items():
        if not cat_skills:
            continue
        cat_info = categories.get(cat_id, {"title": cat_id.title(), "desc": ""})
        cat_dir = target / cat_id
        cat_dir.mkdir(exist_ok=True)
        readme_content = generate_category_readme(cat_info, cat_skills)
        (cat_dir / "README.md").write_text(readme_content)
        print(f"  {cat_id}/README.md ({len(cat_skills)} skills)")

    # 9. Create main README
    print("\n9. Criando README principal...")
    total = len(skills)
    readme = generate_readme(repo_name, github_user, categories, skill_counts, total)
    (target / "README.md").write_text(readme)

    # 10. Summary
    print(f"""
{'='*60}
Setup completo!

  Skills encontradas: {total}
  Categorias criadas: {sum(1 for v in skill_by_cat.values() if v)}
  Scripts copiados: 5
  Docs copiados: 6
  CI/CD: .github/workflows/release.yml

Proximos passos:
  1. Revise o README.md e ajuste categorias se necessario
  2. Rode: python3 scripts/infer_risk.py --all --apply
  3. Rode: python3 scripts/catalog.py
  4. Faca commit e push
  5. O workflow de release vai buildar automaticamente
{'='*60}
""")


if __name__ == "__main__":
    main()
