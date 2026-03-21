# Release Guide

## Objetivo

Publicar skills para o claude.ai seguindo o modelo novo do repositório:

- o catálogo público final é organizado pelas categorias em `dist/`
- `packs/` é apenas mecanismo interno de ingestão, composição e transição
- o artefato publicado continua sendo o arquivo `.skill`

## Formato exigido pelo claude.ai

Cada skill precisa de um arquivo `.skill` que é, na prática, um ZIP renomeado contendo pelo menos:

```text
my-skill.skill
└── SKILL.md
└── references/
└── ...
```

O `SKILL.md` precisa ter frontmatter YAML com pelo menos:

```yaml
---
name: my-skill
description: "O que essa skill faz e quando usá-la."
---
```

## Modelo de publicação

### Estrutura pública

As skills publicadas devem ser consumidas pelas categorias finais em `dist/`.

Exemplos:

- `dist/conteudo-copy/`
- `dist/email-automacao/`
- `dist/frontend/`
- `dist/security/`
- `dist/workflow/`

### Estrutura operacional

As coleções em `packs/` ainda podem ser usadas para compor e classificar skills durante a transição, mas não devem ser tratadas como estrutura pública principal.

Resumo:

- `dist/` = navegação pública final
- `packs/` = ingestão e composição interna

Detalhamento estratégico:

- [PUBLIC_CATALOG_STRATEGY.md](C:\Users\nicol\Downloads\skills\docs\PUBLIC_CATALOG_STRATEGY.md)
- [PUBLIC_TAXONOMY_MIGRATION.md](C:\Users\nicol\Downloads\skills\docs\PUBLIC_TAXONOMY_MIGRATION.md)

## Gerando os arquivos `.skill`

Use o pipeline conforme o tipo de release:

```bash
# release público curado
./scripts/release.sh
```

Exemplos úteis:

```bash
# Ver o que seria gerado sem criar artefatos
./scripts/release.sh --dry-run

# Release público curado por categoria
./scripts/release.sh --category frontend
./scripts/release.sh --category conteudo-copy
./scripts/release.sh --category security

# Release operacional pack-backed por categoria pública
./scripts/release.sh --packs frontend
./scripts/release.sh --packs conteudo-copy

# Release operacional pack-backed completo
./scripts/release.sh --packs all
```

## Quando usar `scripts/catalog.py`

Use `scripts/catalog.py` apenas quando precisar atualizar a classificação operacional vinda de `packs/`.

Exemplo:

```bash
python3 scripts/catalog.py
```

Esse passo é útil quando:

- novas skills foram adicionadas em `packs/kit-510-ptbr`
- novas importações chegaram em `packs/global-skillshare-import`
- a classificação operacional precisa ser recalculada antes do release

Esse comando gera catálogo operacional em `build/catalog/pack-release-catalog.*`.

Ele não muda a decisão estrutural do repositório:

- o catálogo final continua sendo `dist/`
- `packs/` continua sendo backstage operacional

## Categorias públicas finais

### PT-BR

- `utilitarios-negocio`
- `utilitarios-tecnicos`
- `conteudo-copy`
- `email-automacao`
- `funis-vendas`
- `anuncios-trafego`
- `seo-busca`
- `financeiro-precos`
- `juridico-compliance`
- `lancamento-growth`
- `redes-sociais`
- `clientes-consultoria`
- `operacoes-sistemas`
- `ia-automacao`
- `cursos-educacao`
- `marca-pessoal`
- `analytics-dados`
- `nichos-especificos`

### Importadas

- `frontend`
- `backend`
- `data-ai`
- `tooling`
- `workflow`
- `security`
- `cloud-devops`
- `mobile`
- `game-dev`
- `docs-content`
- `automation`
- `business`

## Output esperado

Os artefatos agora saem em dois trilhos:

- release público curado: `dist/<categoria>/`
- release operacional pack-backed: `dist-packs/<categoria>/`

Exemplo:

```text
dist/
├── conteudo-copy/
├── email-automacao/
├── frontend/
├── security/
└── workflow/

dist-packs/
├── conteudo-copy/
├── frontend/
└── workflow/
```

> `dist/` continua sendo a superfície pública final. `dist-packs/` é saída operacional separada para releases derivados de `packs/`.

## Upload no claude.ai

O claude.ai aceita upload individual de `.skill`.

Fluxo:

1. gerar os arquivos `.skill`
2. abrir [claude.ai/customize/skills](https://claude.ai/customize/skills)
3. clicar em `Add skill`
4. fazer upload do arquivo desejado

Alternativa por Projeto:

- Projeto → Configurações → Add content → upload do `.skill`

## Estratégia recomendada de publicação

### Pequenos lotes

Use quando:

- você quer subir poucas skills
- está validando uma categoria nova
- quer revisar manualmente antes do upload

Fluxo:

```bash
./scripts/release.sh --category frontend
```

### Publicação orientada por catálogo

Use quando:

- você já classificou as skills
- quer publicar um bloco consistente da taxonomia pública final

Fluxo:

```bash
./scripts/release.sh
```

### Atualização com ingestão operacional

Use quando:

- houve mudança em `packs/`
- a classificação precisa ser regenerada antes do build

Fluxo:

```bash
python3 scripts/catalog.py
./scripts/release.sh
```

## Fluxo recomendado no repositório

1. Criar ou atualizar a skill-fonte.
2. Garantir que o `SKILL.md` tenha frontmatter válido.
3. Se necessário, atualizar a classificação operacional com `scripts/catalog.py`.
4. Gerar os `.skill` com `./scripts/release.sh`.
5. Validar a saída em `dist/<categoria>/`.
6. Fazer upload no claude.ai.

## Validação antes do upload

O pipeline deve garantir:

- presença de `name:` e `description:` no frontmatter
- estrutura mínima válida do pacote
- saída classificada em categoria pública final

Verificação manual simples:

```bash
head -5 frontend/adapt/SKILL.md
```

Deve mostrar o frontmatter com `name:` e `description:`.

## Critério de qualidade para release

Uma skill está pronta para publicação quando:

- tem `SKILL.md` válido
- está associada a uma categoria pública final
- não depende de `packs/` para ser compreendida pelo usuário final
- pode ser encontrada pelo catálogo público sem expor sua estrutura de ingestão
