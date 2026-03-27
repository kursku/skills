# Como usar skills com Skillshare (CLI)

Este repositorio pode ser usado como fonte direta para instalar e atualizar skills via terminal.

## Inicio rapido

1. Clone este repositorio.
2. No seu projeto, execute:

```bash
skillshare init -p --targets "claude,codex,cursor"
skillshare install github.com/kursku/skills --track -p --all
skillshare sync -p
```

Notas:
- Use `--targets` para configurar suas ferramentas.
- Mantenha `--track` para que `skillshare update --all -p` puxe atualizacoes deste repo.

## Configuracao no Windows

```powershell
skillshare init -p --targets "claude,codex,cursor"
skillshare install github.com/kursku/skills --track -p --all
skillshare sync -p
```

Se seu ambiente tem restricoes de symlinks, use modo copia:

```bash
skillshare target claude --mode copy -p
skillshare sync -p --force
```

## Manutencao recomendada

Execute nos projetos que consomem skills deste repo:

```bash
skillshare check -p
skillshare update --all -p
skillshare sync -p
```

## Verificacao de saude do repositorio

Este repo inclui um script de validacao que verifica as pastas de skills:

```powershell
./scripts/skillshare_repo_check.ps1
```

Opcoes:
- `-WriteIndex`: gera [docs/skillshare-skills.json](docs/skillshare-skills.json)
- `-Strict`: retorna erro quando campos obrigatorios estao faltando

Exemplos:

```powershell
./scripts/skillshare_repo_check.ps1 -WriteIndex
./scripts/skillshare_repo_check.ps1 -WriteIndex -Strict
```

## O que o verificador valida

- Cada diretorio de skill contem `SKILL.md`
- `SKILL.md` inclui frontmatter com `name` e `description`
- `.skillshare-meta.json` e opcional, mas se presente deve ser JSON valido

## Organizacao por dominio

Para colecoes grandes, use pastas agrupadas por area:

- `core/` — skills universais (planejamento, debug, review)
- `frontend/` — UI e web
- `backend/` — APIs, dados e infra
- `data-ai/` — LLM, RAG e avaliacao
- `security/` — seguranca e auditoria
- `workflow/` — orquestracao e processos
- `tooling/` — ferramentas de editor/CLI
- `_experimental/` — skills em teste

### Por que essa estrutura funciona

- **Descoberta facil:** usuarios navegam por dominio primeiro
- **Atualizacoes seguras:** itens experimentais ficam isolados
- **Propriedade clara:** equipes podem cuidar de uma pasta cada
- **Reviews mais rapidos:** prefixos de caminho facilitam diffs e auditorias

## Convencoes de nomenclatura

- Use lowercase kebab-case para pastas e nomes de skills
- Mantenha a profundidade de caminho rasa (um nivel de agrupamento e suficiente)
- Prefira nomes semanticos em vez de nomes de fornecedores
- Use prefixos consistentes para bundles de workflow:
  - `workflow-frontend-*`
  - `workflow-backend-*`
  - `workflow-release-*`

## Comandos para instalacao organizada

Instalar em uma pasta especifica:

```bash
skillshare install github.com/kursku/skills -s clarify,audit --into frontend -p
skillshare install github.com/kursku/skills -s supabase-postgres-best-practices --into backend -p
```

Validar e sincronizar apos mudancas:

```bash
./scripts/skillshare_repo_check.ps1 -WriteIndex
skillshare sync -p
```

## Modelo operacional para equipes

- Mantenha `core/` pequeno e confiavel
- Direcione novas skills para `_experimental/` primeiro
- Promova de `_experimental/` para uma pasta estavel apos review
- Execute verificador + sync no CI para cada mudanca
- Use `--track` para repos compartilhados

## Convencao de packs

- Packs grandes de terceiros devem ficar em `packs/` em vez de misturar com pastas curadas
- Exemplo atual: `packs/kit-510-ptbr` (skills em portugues)
- Instrucoes em portugues: `packs/kit-510-ptbr/README_SKILLSHARE_PT-BR.md`

## Usando no claude.ai (navegador)

Se voce usa o claude.ai no navegador, o fluxo e diferente e mais simples:

1. Baixe o arquivo `SKILL.md` da skill desejada
2. No claude.ai, va em **Personalizar** → **Habilidades** → **+** (adicionar)
3. Faca upload do arquivo `SKILL.md`
4. A skill fica disponivel em todos os seus chats

Veja o [README principal](../README.md) para o passo a passo completo com imagens.

### Seletor rapido para iniciantes

| Objetivo | Comece com | Primeiro prompt |
|----------|-----------|-----------------|
| Conteudo e redes sociais | `conteudo-copy` + `redes-sociais` | "Use as skills de conteudo e redes sociais para criar um calendario de 30 dias." |
| Anuncios e ROI | `anuncios-trafego` + `analytics-dados` | "Use as skills de anuncios e analytics para planejar uma campanha de geracao de leads." |
| Consultoria e clientes | `clientes-consultoria` + `operacoes-sistemas` | "Use as skills de consultoria e operacoes para criar um fluxo de onboarding de clientes." |

### Manutencao para usuarios do claude.ai

- Mantenha entre 10 e 40 skills ativas por vez
- Remova skills que voce nao usa mais
- Atualize os arquivos quando houver mudancas no repositorio
