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

Use o script `scripts/release.sh` para gerar todos os bundles automaticamente:

```bash
# Todas as skills curadas (exclui packs/ por padrão)
./scripts/release.sh

# Ver o que seria gerado, sem criar arquivos
./scripts/release.sh --dry-run

# Apenas uma categoria
./scripts/release.sh --category frontend

# Incluir packs/ também (atenção: gera ~1800 arquivos)
./scripts/release.sh --include-packs
```

**Output:** `dist/<categoria>/<skill-name>.skill`

```
dist/
├── backend/
│   ├── luau-roblox.skill
│   └── supabase-postgres-best-practices.skill
├── frontend/
│   ├── adapt.skill
│   ├── animate.skill
│   └── ...
├── tooling/
├── workflow/
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
| 10–80 skills | Upload por categoria (ex: subir toda a `frontend/` de uma vez se suportado) |
| 80+ skills (packs) | Use a API do claude.ai se disponível, ou mantenha nos packs do repositório |

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
