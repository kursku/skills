# Release Guide — Uploading Skills to claude.ai

## Formato exigido pelo claude.ai

Cada skill precisa de um arquivo `.skill` (que é um ZIP renomeado) contendo:

```
my-skill.skill   ← ZIP renomeado
└── SKILL.md     ← Obrigatório (com frontmatter YAML: name + description)
└── references/  ← Opcional
└── ...
```

O `SKILL.md` precisa ter o frontmatter YAML com pelo menos:

```yaml
---
name: my-skill
description: "O que essa skill faz e quando usá-la."
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

# Só uma categoria
./scripts/release.sh --category frontend
```

### Pack skills (1785 skills)

Primeiro gere o catálogo (necessário uma vez, ou após mudanças nos packs):

```bash
python3 scripts/catalog.py
```

Depois use `--packs <categoria>` no release:

```bash
# Pack skills de uma categoria específica
./scripts/release.sh --packs security
./scripts/release.sh --packs ai-agents
./scripts/release.sh --packs devops

# Todas as pack skills (gera ~1785 arquivos)
./scripts/release.sh --packs all

# Ver o que o catálogo encontrou por categoria
python3 scripts/catalog.py --issues-only
```

**Categorias disponíveis nos packs:**

| Categoria | Skills | Descrição |
|-----------|--------|-----------|
| `devops` | ~406 | CI/CD, deploy, pipelines, Kubernetes |
| `ai-agents` | ~278 | Agentes, RAG, LLM, MCP, orchestration |
| `business` | ~204 | Vendas, finanças, jurídico, CRM |
| `content` | ~180 | Copywriting, SEO, social media, email |
| `security` | ~138 | Auditoria, OWASP, pentest, hardening |
| `backend` | ~117 | APIs, cloud, databases, frameworks |
| `frontend` | ~105 | UI, React, mobile, games, acessibilidade |
| `automation` | ~103 | Zapier, n8n, bots, webhooks |
| `data` | ~65 | Data engineering, analytics, SQL |
| `education` | ~39 | Cursos, documentação, tutoriais |
| `uncategorized` | ~125 | Aguardando classificação |

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

> A pasta `dist/` está no `.gitignore` — os `.skill` files são artefatos de build, não devem ser commitados.

---

## Fazendo upload no claude.ai

O claude.ai aceita **um `.skill` por upload**. Não há batch upload oficial na UI.

### Estratégia recomendada por volume:

| Volume | Estratégia |
|--------|-----------|
| 1–10 skills | Upload manual direto no claude.ai |
| 10–80 skills (curadas) | Build por categoria e upload por lote |
| 80–1785 skills (packs) | Priorize por categoria: rode `--packs security` e suba o que for relevante |
| Tudo de uma vez | Só via API do claude.ai (quando disponível) |

> **Dica:** Use o catálogo para decidir o que subir. `python3 scripts/catalog.py --issues-only` mostra skills com problemas de qualidade que provavelmente não valem o upload.

### Passo a passo (upload manual):

1. Rode `./scripts/release.sh` para gerar os `.skill` files em `dist/`
2. Acesse [claude.ai](https://claude.ai) → Skills → Upload
3. Faça upload dos arquivos `.skill` da pasta `dist/` desejada
4. Cada `.skill` vira uma skill disponível na sua conta

---

## Fluxo de release no repositório

```
1. Desenvolver/atualizar a skill em sua pasta (ex: frontend/adapt/)
2. Editar o SKILL.md com as instruções e o frontmatter correto
3. Commitar na branch de feature
4. Após merge no master, rodar: ./scripts/release.sh
5. Fazer upload dos .skill files gerados em dist/
```

---

## Validação antes do upload

O script `release.sh` valida automaticamente que cada `SKILL.md` tem `name:` e `description:` no frontmatter. Skills inválidas são listadas como "skipped" no output.

Para validar manualmente uma skill:

```bash
head -5 frontend/adapt/SKILL.md
# Deve mostrar os campos name: e description:
```
