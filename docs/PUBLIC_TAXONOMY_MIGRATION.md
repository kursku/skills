# Public Taxonomy Migration

## Objetivo

Substituir o modelo público centrado em `packs/` por uma taxonomia pública final, estável e navegável, em que todas as skills publicadas sejam classificadas diretamente nas categorias oficiais do catálogo.

## Decisão

No repositório público:

- a taxonomia oficial deve ser a taxonomia visível em `dist/`
- `packs/` deve existir apenas como mecanismo transitório de composição e migração
- a origem de uma skill deve virar metadado de proveniência, não estrutura principal de navegação

## Problema Estrutural Atual

Hoje existem três modelos diferentes convivendo ao mesmo tempo:

1. `packs/kit-510-ptbr`
- organiza a coleção PT-BR por grupos numerados

2. `packs/global-skillshare-import`
- organiza a coleção importada por `wave-*`

3. `dist/`
- já expõe a taxonomia pública final que o usuário deveria enxergar

O problema é que o mecanismo interno de composição ainda compete com a estrutura pública. Para quem consome o repositório, isso cria a impressão de que:

- `packs/` é a estrutura principal
- algumas skills estão "fora da organização oficial"
- a navegação pública é derivada, mas não canônica

## Taxonomia Pública Canônica

### PT-BR

As categorias públicas finais da coleção PT-BR já existem em `dist/`:

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

As categorias públicas finais da coleção importada já existem em `dist/`:

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

## Mapeamento Concreto de `packs/kit-510-ptbr`

O pack PT-BR já pode ser migrado sem ambiguidade estrutural relevante:

| Origem em `packs/kit-510-ptbr` | Categoria pública final |
| --- | --- |
| `00-utilitarios-negocio` | `dist/utilitarios-negocio` |
| `00-utilitarios-tecnicos` | `dist/utilitarios-tecnicos` |
| `01-conteudo-copy` | `dist/conteudo-copy` |
| `02-email-automacao` | `dist/email-automacao` |
| `03-funis-vendas` | `dist/funis-vendas` |
| `04-anuncios-trafego` | `dist/anuncios-trafego` |
| `05-seo-busca` | `dist/seo-busca` |
| `06-financeiro-precos` | `dist/financeiro-precos` |
| `07-juridico-compliance` | `dist/juridico-compliance` |
| `08-lancamento-growth` | `dist/lancamento-growth` |
| `09-redes-sociais` | `dist/redes-sociais` |
| `10-clientes-consultoria` | `dist/clientes-consultoria` |
| `11-operacoes-sistemas` | `dist/operacoes-sistemas` |
| `12-ia-automacao` | `dist/ia-automacao` |
| `13-cursos-educacao` | `dist/cursos-educacao` |
| `14-marca-pessoal` | `dist/marca-pessoal` |
| `15-analytics-dados` | `dist/analytics-dados` |
| `16-nichos-especificos` | `dist/nichos-especificos` |

## Mapeamento Concreto de `packs/global-skillshare-import`

As importadas não estão separadas hoje por categoria pública, mas por ondas (`wave-001` até `wave-013`). A regra de migração deve ser:

1. manter `wave-*` apenas como histórico de ingestão
2. classificar cada skill importada em uma categoria pública final
3. registrar a origem da ingestão em metadado

### Metadados recomendados para skills importadas

- `source_pack: global-skillshare-import`
- `source_wave: wave-00x`
- `source_origin: <repo ou coleção original, se houver>`
- `public_category: <categoria final>`

### Regra de publicação

Uma skill importada não deve ser publicada para navegação pública por `wave-*`.

Ela deve aparecer apenas em:

- sua categoria pública final
- metadados de proveniência

## Arquitetura Alvo

### Estado de transição aceitável

- `packs/` ainda existe para compor e migrar
- `dist/` continua sendo a navegação pública oficial
- README e docs públicas falam em categorias finais, não em packs

### Estado alvo do repositório público

Escolha recomendada:

1. promover a taxonomia pública final para estrutura principal visível
2. remover `packs/` da narrativa pública
3. manter qualquer backstage de composição em repo privado ou área interna explícita

Isso pode ser feito de duas formas.

### Opção A: raiz pública continua técnica, `dist/` segue como catálogo

Vantagens:

- menor ruptura imediata
- menos risco operacional
- migração gradual

Desvantagens:

- ainda existe duplicidade mental entre "fonte" e "catálogo"
- o público continua navegando por uma saída de build

### Opção B: a taxonomia pública final sobe para a estrutura principal do repositório

Exemplo desejado:

- `conteudo-copy/`
- `email-automacao/`
- `frontend/`
- `security/`
- `workflow/`
- etc.

Vantagens:

- o repositório público passa a refletir exatamente o catálogo oficial
- elimina a ambiguidade entre estrutura-fonte e estrutura pública
- reduz a necessidade de explicar o repositório no README

Desvantagens:

- exige migração maior
- pede reorganização do pipeline de release
- pode exigir mover backstage para repo privado antes

### Recomendação

Seguir em duas etapas:

1. curto prazo: manter `dist/` como catálogo oficial e reduzir `packs/` a mecanismo interno
2. médio prazo: migrar o repositório público para a Opção B

## Fases de Migração

### Fase 1: alinhar discurso público

- README aponta para `dist/`
- docs públicas deixam `packs/` como transitório
- releases deixam de apresentar `packs/` como produto principal

### Fase 2: classificar tudo por categoria final

- concluir o mapeamento da coleção PT-BR
- classificar todas as skills importadas das `wave-*` em categorias finais
- registrar proveniência via metadados

### Fase 3: reduzir dependência operacional de `packs/`

- ajustar `scripts/catalog.py` para tratar `packs/` como ingestão, não como taxonomia pública
- revisar `docs/RELEASE.md`
- mover backstage operacional para repo privado quando conveniente

### Fase 4: simplificar a árvore pública

- escolher entre manter `dist/` como saída oficial ou promover a taxonomia pública para a raiz
- remover `packs/` da superfície pública do repositório

## Impacto em Documentação e Release

### README

Deve falar apenas em:

- categorias públicas finais
- como instalar e consumir skills
- estratégia resumida de migração

### `docs/RELEASE.md`

Deve ser reescrito para:

- usar categorias públicas finais como modelo principal
- tratar `packs/` como entrada operacional
- evitar linguagem como "pack skills" como se fosse produto principal

### `scripts/catalog.py`

Deve evoluir para:

- receber skills de fontes diferentes
- normalizar tudo para a taxonomia pública canônica
- registrar origem como metadado
- gerar catálogo público sem expor a estrutura de ingestão

## Critério de Pronto

A migração estrutural estará madura quando:

- nenhuma skill pública depender conceitualmente de `packs/` para ser entendida
- toda skill publicada tiver uma categoria pública final explícita
- a origem de uma skill for metadado, não localização principal
- o README puder explicar o repositório sem mencionar `packs/` como estrutura central
