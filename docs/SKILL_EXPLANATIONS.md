# Skill Explanations Map

This file explains what the major skill groups in this repository are for.
It is designed for new users who do not want to read hundreds of `SKILL.md` files first.

## How To Use This Map

1. Start with your outcome (for example: launch ads, improve content, automate operations).
2. Pick one group below.
3. Open 3 to 5 skills from that group.
4. Test with one concrete prompt.

## Repository-Wide Coverage

Current coverage against global skillshare source (`AppData/Roaming/skillshare/skills`):

- Global unique skill names: 1859
- Repo unique skill names: 1859
- Missing in repo: 0

Source: [global-skillshare-coverage-summary.json](global-skillshare-coverage-summary.json)

## Curated Core Groups (Top-Level)

These are your curated, hand-organized groups.

| Group | Skills | What it is for |
|---|---:|---|
| `core` | 1 | Small, trusted baseline skills used across many workflows. |
| `frontend` | 26 | UI/UX, visual quality, accessibility, metadata, and frontend polish. |
| `backend` | 2 | Backend/data engineering focused skills. |
| `data-ai` | 4 | LLM/evaluation/agent architecture and AI development strategy. |
| `workflow` | 32 | GSD orchestration commands and planning/execution lifecycle skills. |
| `tooling` | 11 | Tool integration skills (skillshare, obsidian, ask wrappers, etc.). |
| `_experimental` | 1 | Trial or staging skills before promotion. |

## Pack: Kit 510 PT-BR

Location: [packs/kit-510-ptbr](../packs/kit-510-ptbr)

This pack is focused on Portuguese business/marketing execution.

### Utility Tracks

| Category | Skills | Explanation |
|---|---:|---|
| `00-utilitarios-tecnicos` | 8 | Technical helpers: automation, integration, security, scaling, and agent ops. |
| `00-utilitarios-negocio` | 4 | Business helpers: support, research, context, and practical operations support. |

### Main Business Tracks

Each track has 30 to 32 specialized skills.

| Category | Skills | Explanation |
|---|---:|---|
| `01-conteudo-copy` | 32 | Content and copywriting templates, positioning, hooks, scripts, and messaging. |
| `02-email-automacao` | 32 | Email lifecycle automation: onboarding, reactivation, campaigns, and retention flows. |
| `03-funis-vendas` | 32 | Sales funnels: offer structure, conversion journeys, and monetization patterns. |
| `04-anuncios-trafego` | 32 | Paid acquisition strategy and campaign execution for ad channels. |
| `05-seo-busca` | 32 | SEO strategy and implementation: keyword, technical SEO, content, and visibility. |
| `06-financeiro-precos` | 32 | Pricing, revenue, unit economics, financial planning, and profitability. |
| `07-juridico-compliance` | 32 | Compliance/legal templates and operational guardrails. |
| `08-lancamento-growth` | 32 | Product/growth launch motions, experiments, and growth mechanics. |
| `09-redes-sociais` | 32 | Social strategy, content system, channel planning, and engagement playbooks. |
| `10-clientes-consultoria` | 32 | Client operations for agencies/consultants: onboarding, retention, communication. |
| `11-operacoes-sistemas` | 32 | Process and operational systemization for repeatable delivery. |
| `12-ia-automacao` | 32 | AI-assisted workflows and automation patterns for business operations. |
| `13-cursos-educacao` | 32 | Course/education product design, delivery, and learner outcomes. |
| `14-marca-pessoal` | 32 | Personal brand positioning, authority building, and visibility strategy. |
| `15-analytics-dados` | 32 | Analytics, KPI frameworks, reporting, attribution, and data-driven decisions. |
| `16-nichos-especificos` | 30 | Verticalized playbooks by industry niche. |

Source: [kit-510-category-counts.json](kit-510-category-counts.json)

## Pack: Global Skillshare Import Waves

Location: [packs/global-skillshare-import](../packs/global-skillshare-import)

These waves are staged imports from your global source.

- Wave folders (`wave-001` ... `wave-013`) are import batches.
- They prioritize complete repository coverage and traceability.
- Each wave has reports in `docs/` with imported/skipped entries.

Example report files:

- `global-skillshare-import-wave-001-report.json`
- `global-skillshare-import-wave-001-imported.txt`
- `global-skillshare-import-wave-001-skipped.txt`

## Starter Recommendations (New Users)

Choose one path and start with 2 to 3 tracks only:

1. Content + Social:
- `01-conteudo-copy`
- `09-redes-sociais`

2. Ads + Analytics:
- `04-anuncios-trafego`
- `15-analytics-dados`

3. Consulting + Operations:
- `10-clientes-consultoria`
- `11-operacoes-sistemas`
- `00-utilitarios-negocio`

## Practical Tip

Avoid loading everything at once in Claude.ai projects.
Use this map to keep each project focused by outcome and domain.
