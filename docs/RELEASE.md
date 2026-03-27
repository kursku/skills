# Guia de Release — Enviando Skills para o claude.ai

## Formato exigido pelo claude.ai

Cada skill precisa de um arquivo `.skill` (que e um ZIP renomeado) contendo:

```
my-skill.skill   <- ZIP renomeado
└── SKILL.md     <- Obrigatorio (com frontmatter YAML: name + description)
└── references/  <- Opcional
└── ...
```

O `SKILL.md` precisa ter o frontmatter YAML com pelo menos:

```yaml
---
name: my-skill
description: "O que essa skill faz e quando usa-la."
---
```

---

## Gerando os arquivos `.skill`

### Skills curadas (76 skills)

Use o `scripts/release.sh` diretamente:

```bash
# Todas as skills curadas
./scripts/release.sh

# Ver o que seria gerado sem criar arquivos
./scripts/release.sh --dry-run

# So uma categoria
./scripts/release.sh --category frontend
```

### Pack skills (1785 skills)

Primeiro gere o catalogo (necessario uma vez, ou apos mudancas nos packs):

```bash
python3 scripts/catalog.py
```

Depois use `--packs <categoria>` no release:

```bash
# Pack skills de uma categoria especifica
./scripts/release.sh --packs security
./scripts/release.sh --packs ai-agents
./scripts/release.sh --packs devops

# Todas as pack skills (gera ~1785 arquivos)
./scripts/release.sh --packs all

# Ver o que o catalogo encontrou por categoria
python3 scripts/catalog.py --issues-only
```

**Categorias disponiveis nos packs:**

| Categoria | Skills | Descricao |
|-----------|--------|-----------|
| `devops` | ~406 | CI/CD, deploy, pipelines, Kubernetes |
| `ai-agents` | ~278 | Agentes, RAG, LLM, MCP, orchestration |
| `business` | ~204 | Vendas, financas, juridico, CRM |
| `content` | ~180 | Copywriting, SEO, social media, email |
| `security` | ~138 | Auditoria, OWASP, pentest, hardening |
| `backend` | ~117 | APIs, cloud, databases, frameworks |
| `frontend` | ~105 | UI, React, mobile, games, acessibilidade |
| `automation` | ~103 | Zapier, n8n, bots, webhooks |
| `data` | ~65 | Data engineering, analytics, SQL |
| `education` | ~39 | Cursos, documentacao, tutoriais |
| `productivity` | ~17 | GSD, Notion, Kanban, planejamento |
| `tooling` | ~8 | Utilitarios tecnicos, CLI, integracoes |
| `uncategorized` | ~125 | Aguardando classificacao |

**Output:** `dist/<categoria>/<skill-name>.skill`

```
dist/
├── security/
│   ├── 007.skill
│   ├── api-fuzzing-bug-bounty.skill
│   └── ...
├── ai-agents/
├── devops/
└── ...
```

> A pasta `dist/` esta no `.gitignore` — os `.skill` files sao artefatos de build, nao devem ser commitados.

---

## Fazendo upload no claude.ai

O claude.ai aceita **um `.skill` por upload**. Nao ha batch upload oficial na UI.

### Onde fazer upload

Acesse **Personalizar** → **Habilidades** → faca o **Upload do SKILL.md** (ou do arquivo `.skill` gerado).

As skills instaladas ficam disponiveis em **todos os seus chats e Projetos**.

> **Alternativa por Projeto:** Para instalar em apenas um Projeto, abra o Projeto → Configuracoes → Adicionar conteudo → faca upload do `.skill`.

### Estrategia recomendada por volume:

| Volume | Estrategia |
|--------|-----------|
| 1–10 skills | Upload manual via Personalizar → Habilidades |
| 10–80 skills (curadas) | Build por categoria e upload por lote |
| 80–1785 skills (packs) | Priorize por categoria: rode `--packs security` e suba o que for relevante |
| Tudo de uma vez | So via API do claude.ai (quando disponivel) |

> **Dica:** Use o catalogo para decidir o que subir. `python3 scripts/catalog.py --issues-only` mostra skills com problemas de qualidade que provavelmente nao valem o upload.

### Passo a passo (upload manual):

1. Rode `./scripts/release.sh` para gerar os `.skill` files em `dist/`
2. No claude.ai, va em **Personalizar** → **Habilidades**
3. Faca o **Upload** dos arquivos `.skill` da pasta `dist/` desejada
4. Cada `.skill` vira uma skill disponivel na sua conta

---

## Fluxo de release no repositorio

```
1. Desenvolver/atualizar a skill em sua pasta (ex: frontend/adapt/)
2. Editar o SKILL.md com as instrucoes e o frontmatter correto
3. Commitar na branch de feature
4. Apos merge no master, rodar: ./scripts/release.sh
5. Fazer upload dos .skill files gerados em dist/
```

---

## Validacao antes do upload

O script `release.sh` valida automaticamente que cada `SKILL.md` tem `name:` e `description:` no frontmatter. Skills invalidas sao listadas como "skipped" no output.

Para validar manualmente uma skill:

```bash
head -5 frontend/adapt/SKILL.md
# Deve mostrar os campos name: e description:
```
