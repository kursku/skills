# Mapa de Explicacoes dos Skills

Este documento explica para que servem os principais grupos de skills deste repositorio.
Foi feito para iniciantes que nao querem ler centenas de `SKILL.md` antes de comecar.

## Como usar este mapa

1. Comece pelo objetivo (ex.: crescer redes, melhorar funil, automatizar operacao).
2. Escolha um grupo abaixo.
3. Abra de 3 a 5 skills desse grupo.
4. Teste com um prompt concreto.

## Cobertura geral do repositorio

Cobertura atual comparada com a origem global do skillshare (`AppData/Roaming/skillshare/skills`):

- Nomes unicos globais: 1859
- Nomes unicos no repositorio: 1859
- Faltando no repositorio: 0

Fonte: [global-skillshare-coverage-summary.json](global-skillshare-coverage-summary.json)

## Grupos curados (top-level)

Estes sao os grupos curados manualmente.

| Grupo | Skills | Para que serve |
|---|---:|---|
| `core` | 1 | Base enxuta e confiavel para tarefas recorrentes. |
| `frontend` | 26 | UI/UX, acessibilidade, metadata e refinamento visual. |
| `backend` | 2 | Skills de backend e dados. |
| `data-ai` | 4 | Arquitetura de IA, avaliacao e desenvolvimento de agentes. |
| `workflow` | 32 | Orquestracao GSD: planejamento, execucao e verificacao. |
| `tooling` | 11 | Integracoes de ferramentas (skillshare, obsidian, wrappers). |
| `_experimental` | 1 | Skills em teste antes de promocao. |

## Pacote: Kit 510 PT-BR

Local: [packs/kit-510-ptbr](../packs/kit-510-ptbr)

Pacote focado em execucao de marketing e operacao em portugues.

### Trilhas utilitarias

| Categoria | Skills | Explicacao |
|---|---:|---|
| `00-utilitarios-tecnicos` | 8 | Integracao, automacao, seguranca, escalabilidade e operacao tecnica. |
| `00-utilitarios-negocio` | 4 | Suporte, pesquisa, contexto de negocio e apoio operacional. |

### Trilhas principais de negocio

Cada trilha tem de 30 a 32 skills especializados.

| Categoria | Skills | Explicacao |
|---|---:|---|
| `01-conteudo-copy` | 32 | Copy, posicionamento, roteiros, hooks e mensagens. |
| `02-email-automacao` | 32 | Ciclo de email: onboarding, campanhas, retencao e reativacao. |
| `03-funis-vendas` | 32 | Estrutura de ofertas, jornadas de conversao e monetizacao. |
| `04-anuncios-trafego` | 32 | Estrategia e execucao de campanhas pagas. |
| `05-seo-busca` | 32 | SEO tecnico e de conteudo para crescimento organico. |
| `06-financeiro-precos` | 32 | Precificacao, margem, receita, unit economics e planejamento. |
| `07-juridico-compliance` | 32 | Compliance e templates operacionais juridicos. |
| `08-lancamento-growth` | 32 | Lancamento, growth loops e experimentacao. |
| `09-redes-sociais` | 32 | Planejamento de canais, conteudo e engajamento social. |
| `10-clientes-consultoria` | 32 | Operacao de consultoria/agencia: onboarding e retencao. |
| `11-operacoes-sistemas` | 32 | Processos e sistematizacao da operacao. |
| `12-ia-automacao` | 32 | Automacoes com IA para produtividade e escala. |
| `13-cursos-educacao` | 32 | Produtos educacionais: desenho, entrega e resultados. |
| `14-marca-pessoal` | 32 | Posicionamento, autoridade e visibilidade pessoal. |
| `15-analytics-dados` | 32 | KPI, atribuicao, dashboards e decisao orientada por dados. |
| `16-nichos-especificos` | 30 | Playbooks por nicho de mercado. |

Fonte: [kit-510-category-counts.json](kit-510-category-counts.json)

## Pacote: Importacao global por ondas

Local: [packs/global-skillshare-import](../packs/global-skillshare-import)

Essas ondas sao lotes de importacao da sua origem global.

- Pastas `wave-001` ... `wave-013` sao lotes de importacao.
- Prioridade: cobertura completa com rastreabilidade.
- Cada onda tem relatorios em `docs/` (importados/pulados).

Exemplos de relatorio:

- `global-skillshare-import-wave-001-report.json`
- `global-skillshare-import-wave-001-imported.txt`
- `global-skillshare-import-wave-001-skipped.txt`

## Recomendacao inicial (para iniciantes)

Escolha um caminho e comece com 2 ou 3 trilhas:

1. Conteudo + Redes:
- `01-conteudo-copy`
- `09-redes-sociais`

2. Trafego + Analytics:
- `04-anuncios-trafego`
- `15-analytics-dados`

3. Consultoria + Operacao:
- `10-clientes-consultoria`
- `11-operacoes-sistemas`
- `00-utilitarios-negocio`

## Dica pratica

No Claude.ai, nao suba tudo de uma vez.
Use este mapa para manter cada projeto focado por objetivo.
