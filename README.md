# Skills para claude.ai

Skills são módulos de instrução especializada que ensinam o Claude a lidar com tarefas específicas. Pense nelas como conhecimento de especialista que você pode carregar no seu Projeto do claude.ai.

---

## Como instalar no claude.ai

<!-- demo GIF — gerado por scripts/record_install_demo.py -->
![Instalando uma skill no claude.ai](docs/assets/install-demo.gif)

**1. Escolha uma skill nas categorias abaixo e clique em ⬇ Download**

**2. Acesse [claude.ai/customize/skills](https://claude.ai/customize/skills)**

**3. Clique em "Add skill" e faça upload do arquivo `.skill` baixado**

**4. Pronto! A skill está disponível em todos os seus chats e Projetos**

> **Alternativa (Projetos):** Se preferir usar a skill apenas em um Projeto específico, abra o Projeto → Configurações → Add content → faça upload do `.skill`.

---

## claude.ai vs Claude Desktop

| | claude.ai (web) | Claude Desktop / CLI |
|---|---|---|
| **Como instalar** | Upload do `.skill` em [claude.ai/customize/skills](https://claude.ai/customize/skills) | `skillshare install` via terminal |
| **Formato** | Arquivo `.skill` (ZIP renomeado com `SKILL.md`) | Pasta com `SKILL.md` diretamente |
| **Escopo** | Global — disponível em todos os chats e Projetos | Por projeto ou global, conforme config |
| **Atualização** | Re-upload manual | `skillshare update --all` |

Se você usa o **claude.ai no navegador**, siga o passo a passo acima.
Se você usa o **Claude Desktop ou Claude Code**, veja [docs/SKILLSHARE.md](docs/SKILLSHARE.md) para instalar via `skillshare`.

---

## Categorias

Este repositório deve funcionar como **catálogo público principal de skills**.

Por isso, existem três camadas diferentes:

- **categorias públicas finais (`dist/`)**: navegação oficial de consumo e distribuição.
- **raiz técnica (`backend/`, `frontend/`, `tooling/`, etc.)**: organização atual das skills-fonte.
- **`packs/`**: camada legada de composição editorial, mantida temporariamente durante a transição.

O catálogo publicado para consumo está organizado em dois blocos:

- **Categorias PT-BR (principal):** atualmente geradas a partir da coleção PT-BR existente.
- **Categorias importadas:** atualmente geradas a partir da coleção importada do ecossistema global.

As descrições ficam com português como padrão, com apoio em inglês em itálico para facilitar o uso por novos usuários de CLI.

As pastas da raiz como `backend/`, `core/`, `data-ai/`, `frontend/`, `security/`, `tooling/` e `workflow/` continuam existindo como estrutura-fonte. O objetivo, daqui para frente, é que todas as skills publicadas sejam redistribuídas para as categorias públicas finais, sem depender conceitualmente de `packs/`.

> Resumo: `dist/` é a navegação oficial, a raiz ainda é a estrutura-fonte atual, e `packs/` deve desaparecer do modelo público ao longo da migração.

---

<!-- BEGIN PTBR CATEGORIES -->
## Categorias PT-BR (Principal) / Portuguese Categories (Primary)

Estas são as categorias públicas finais do catálogo PT-BR. Hoje elas ainda são geradas a partir da coleção PT-BR existente, mas a direção do repositório é que essa taxonomia pública se torne a estrutura oficial visível do catálogo.

- [Utilitarios de Negocio / Business Utilities](./dist/utilitarios-negocio/) — Skills utilitarias de negocio para atendimento, pesquisa, perfil e suporte geral. _(Business utility skills for support, research, profile and general assistance.)_
- [Utilitarios Tecnicos / Technical Utilities](./dist/utilitarios-tecnicos/) — Skills utilitarias tecnicas para integracao, automacao, seguranca e engenharia. _(Technical utility skills for integration, automation, security and engineering.)_
- [Conteudo & Copy / Content & Copywriting](./dist/conteudo-copy/) — Skills focadas em conteudo, copywriting e producao de materiais persuasivos. _(Skills for content, copywriting and persuasive assets.)_
- [Email & Automacao / Email & Automation](./dist/email-automacao/) — Skills para e-mail marketing, automacoes e sequencias de comunicacao. _(Skills for email marketing, automation and lifecycle sequences.)_
- [Funis de Vendas / Sales Funnels](./dist/funis-vendas/) — Skills para funis, ofertas, conversao e estrategia comercial. _(Skills for funnels, offers, conversion and sales strategy.)_
- [Anuncios & Trafego / Paid Ads & Traffic](./dist/anuncios-trafego/) — Skills para midia paga, criativos, tracking e otimizacao de campanhas. _(Skills for paid media, creatives, tracking and campaign optimization.)_
- [SEO & Busca / SEO & Search](./dist/seo-busca/) — Skills para SEO, conteudo organico, SERP e crescimento em busca. _(Skills for SEO, search visibility and organic growth.)_
- [Financeiro & Precos / Finance & Pricing](./dist/financeiro-precos/) — Skills para precificacao, financas, projecoes e saude economica. _(Skills for pricing, finance, projections and business economics.)_
- [Juridico & Compliance / Legal & Compliance](./dist/juridico-compliance/) — Skills para contratos, politicas, conformidade e documentacao juridica. _(Skills for contracts, policies, compliance and legal docs.)_
- [Lancamento & Growth / Launch & Growth](./dist/lancamento-growth/) — Skills para growth, aquisicao, retencao e lancamentos. _(Skills for launch strategy, acquisition, retention and growth.)_
- [Redes Sociais / Social Media](./dist/redes-sociais/) — Skills para conteudo, posicionamento e crescimento em redes sociais. _(Skills for content, positioning and social growth.)_
- [Clientes & Consultoria / Clients & Consulting](./dist/clientes-consultoria/) — Skills para operacao de consultoria, relacionamento e gestao de clientes. _(Skills for consulting operations, client management and delivery.)_
- [Operacoes & Sistemas / Operations & Systems](./dist/operacoes-sistemas/) — Skills para processos, operacao, documentacao e gestao de sistemas. _(Skills for processes, operations, documentation and systems management.)_
- [IA & Automacao / AI & Automation](./dist/ia-automacao/) — Skills para IA aplicada, automacao, agentes e integracoes inteligentes. _(Skills for applied AI, automation, agents and intelligent integrations.)_
- [Cursos & Educacao / Courses & Education](./dist/cursos-educacao/) — Skills para cursos, educacao, programas e produtos de aprendizagem. _(Skills for education products, courses and learning programs.)_
- [Marca Pessoal / Personal Brand](./dist/marca-pessoal/) — Skills para marca pessoal, autoridade, reputacao e presenca profissional. _(Skills for personal brand, authority, reputation and visibility.)_
- [Analytics & Dados / Analytics & Data](./dist/analytics-dados/) — Skills para analytics, metricas, dashboards e analise de dados. _(Skills for analytics, metrics, dashboards and data analysis.)_
- [Nichos Especificos / Specific Niches](./dist/nichos-especificos/) — Skills de marketing e estrategia para nichos e verticais especificos. _(Skills for marketing and strategy across specific niches and verticals.)_

---
<!-- END PTBR CATEGORIES -->

<!-- BEGIN GLOBAL IMPORT CATEGORIES -->
## Categorias Importadas (Global Skillshare) / Imported Categories

Estas são as categorias públicas finais das skills importadas. Hoje elas ainda são geradas a partir da coleção importada existente, mas a direção do repositório é que essa taxonomia pública se torne a estrutura oficial visível do catálogo.

- [Frontend / Interface Web](./dist/frontend/) — Skills para interface web, design systems, frameworks frontend, acessibilidade e experiencias no navegador. _(Skills for web UI, design systems, frontend frameworks, accessibility and browser experiences.)_
- [Backend / Servidor](./dist/backend/) — Skills para APIs, bancos de dados, frameworks server-side e arquitetura backend. _(Skills for APIs, databases, server-side frameworks and backend architecture.)_
- [Dados & IA / Data & AI](./dist/data-ai/) — Skills para LLMs, agentes, machine learning, avaliacao, busca vetorial e sistemas de IA. _(Skills for LLMs, agents, ML, evaluation, vector search and AI systems.)_
- [Ferramentas / Tooling](./dist/tooling/) — Skills para ferramentas de desenvolvedor, CLIs, fluxos locais e utilitarios gerais. _(Skills for developer tools, CLI skills, local workflows and general-purpose utilities.)_
- [Fluxos & Orquestracao / Workflow](./dist/workflow/) — Skills para orquestracao de projetos, planejamento e sistemas de execucao. _(Skills for project orchestration, planning and execution systems.)_
- [Seguranca / Security](./dist/security/) — Skills para auditoria de seguranca, hardening, threat modeling e testes ofensivos/defensivos. _(Skills for security auditing, hardening, threat modeling and offensive/defensive testing.)_
- [Cloud & DevOps](./dist/cloud-devops/) — Skills para plataformas cloud, infraestrutura, deploy, containers e operacao de plataforma. _(Skills for cloud platforms, infrastructure, deployment, containers and platform operations.)_
- [Mobile](./dist/mobile/) — Skills para iOS, Android, Expo, React Native, Flutter e engenharia mobile. _(Skills for iOS, Android, Expo, React Native, Flutter and mobile-specific engineering.)_
- [Games / Game Dev](./dist/game-dev/) — Skills para engines de jogos, sistemas de gameplay, 3D interativo e desenvolvimento de jogos. _(Skills for game engines, gameplay systems, interactive 3D and game development.)_
- [Docs & Conteudo / Docs & Content](./dist/docs-content/) — Skills para documentacao, escrita, sistemas de conteudo e fluxos de publicacao. _(Skills for documentation, writing, content systems and publishing workflows.)_
- [Automacao & Integracoes / Automation & Integrations](./dist/automation/) — Skills para integracoes, automacoes SaaS, workflows e conectores externos. _(Skills for app integrations, SaaS automations, workflows and external tool connectors.)_
- [Negocios & Growth / Business & Growth](./dist/business/) — Skills para produto, marketing, analytics, vendas, precificacao e operacao de negocios. _(Skills for product, marketing, analytics, sales, pricing and business operations.)_

---
<!-- END GLOBAL IMPORT CATEGORIES -->

## Estrategia do Repositorio

- **Este repo publico:** principal, canonico e distribuivel.
- **Repo privado:** secundario, operacional e de apoio.
- **`packs/`:** mecanismo transitório de migração, não estrutura pública final desejada.
- **Direção de longo prazo:** classificar todas as skills nas categorias públicas finais e remover `packs/` da narrativa e, quando viável, da árvore pública.

Detalhamento: veja [docs/PUBLIC_CATALOG_STRATEGY.md](./docs/PUBLIC_CATALOG_STRATEGY.md) e [docs/PUBLIC_TAXONOMY_MIGRATION.md](./docs/PUBLIC_TAXONOMY_MIGRATION.md).

## Contribuindo

Quer criar uma skill ou melhorar uma existente? Abra uma issue ou Pull Request.
