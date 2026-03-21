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

O catálogo publicado na raiz está organizado em dois blocos:

- **Categorias PT-BR (principal):** baseadas em `packs/kit-510-ptbr`, que continua sendo a fonte de verdade para o catálogo em português.
- **Categorias importadas:** publicadas a partir de `packs/global-skillshare-import`, mantendo agrupamentos semânticos estáveis para skills vindas do ecossistema global.

As descrições ficam com português como padrão, com apoio em inglês em itálico para facilitar o uso por novos usuários de CLI.

---

<!-- BEGIN PTBR CATEGORIES -->
## Categorias PT-BR (Principal) / Portuguese Categories (Primary)

As skills de `packs/kit-510-ptbr` continuam sendo a fonte de verdade. A publicação na raiz usa categorias em português como padrão, com apoio em inglês em itálico para facilitar o uso por novos usuários de CLI.

- [Utilitarios de Negocio / Business Utilities](./utilitarios-negocio/) — Skills utilitarias de negocio para atendimento, pesquisa, perfil e suporte geral. _(Business utility skills for support, research, profile and general assistance.)_
- [Utilitarios Tecnicos / Technical Utilities](./utilitarios-tecnicos/) — Skills utilitarias tecnicas para integracao, automacao, seguranca e engenharia. _(Technical utility skills for integration, automation, security and engineering.)_
- [Conteudo & Copy / Content & Copywriting](./conteudo-copy/) — Skills focadas em conteudo, copywriting e producao de materiais persuasivos. _(Skills for content, copywriting and persuasive assets.)_
- [Email & Automacao / Email & Automation](./email-automacao/) — Skills para e-mail marketing, automacoes e sequencias de comunicacao. _(Skills for email marketing, automation and lifecycle sequences.)_
- [Funis de Vendas / Sales Funnels](./funis-vendas/) — Skills para funis, ofertas, conversao e estrategia comercial. _(Skills for funnels, offers, conversion and sales strategy.)_
- [Anuncios & Trafego / Paid Ads & Traffic](./anuncios-trafego/) — Skills para midia paga, criativos, tracking e otimizacao de campanhas. _(Skills for paid media, creatives, tracking and campaign optimization.)_
- [SEO & Busca / SEO & Search](./seo-busca/) — Skills para SEO, conteudo organico, SERP e crescimento em busca. _(Skills for SEO, search visibility and organic growth.)_
- [Financeiro & Precos / Finance & Pricing](./financeiro-precos/) — Skills para precificacao, financas, projecoes e saude economica. _(Skills for pricing, finance, projections and business economics.)_
- [Juridico & Compliance / Legal & Compliance](./juridico-compliance/) — Skills para contratos, politicas, conformidade e documentacao juridica. _(Skills for contracts, policies, compliance and legal docs.)_
- [Lancamento & Growth / Launch & Growth](./lancamento-growth/) — Skills para growth, aquisicao, retencao e lancamentos. _(Skills for launch strategy, acquisition, retention and growth.)_
- [Redes Sociais / Social Media](./redes-sociais/) — Skills para conteudo, posicionamento e crescimento em redes sociais. _(Skills for content, positioning and social growth.)_
- [Clientes & Consultoria / Clients & Consulting](./clientes-consultoria/) — Skills para operacao de consultoria, relacionamento e gestao de clientes. _(Skills for consulting operations, client management and delivery.)_
- [Operacoes & Sistemas / Operations & Systems](./operacoes-sistemas/) — Skills para processos, operacao, documentacao e gestao de sistemas. _(Skills for processes, operations, documentation and systems management.)_
- [IA & Automacao / AI & Automation](./ia-automacao/) — Skills para IA aplicada, automacao, agentes e integracoes inteligentes. _(Skills for applied AI, automation, agents and intelligent integrations.)_
- [Cursos & Educacao / Courses & Education](./cursos-educacao/) — Skills para cursos, educacao, programas e produtos de aprendizagem. _(Skills for education products, courses and learning programs.)_
- [Marca Pessoal / Personal Brand](./marca-pessoal/) — Skills para marca pessoal, autoridade, reputacao e presenca profissional. _(Skills for personal brand, authority, reputation and visibility.)_
- [Analytics & Dados / Analytics & Data](./analytics-dados/) — Skills para analytics, metricas, dashboards e analise de dados. _(Skills for analytics, metrics, dashboards and data analysis.)_
- [Nichos Especificos / Specific Niches](./nichos-especificos/) — Skills de marketing e estrategia para nichos e verticais especificos. _(Skills for marketing and strategy across specific niches and verticals.)_

---
<!-- END PTBR CATEGORIES -->

<!-- BEGIN GLOBAL IMPORT CATEGORIES -->
## Categorias Importadas (Global Skillshare) / Imported Categories

As skills de `packs/global-skillshare-import` continuam sendo a fonte de importação. A publicação na raiz usa categorias semânticas estáveis, com português como linguagem principal e apoio em inglês em itálico para novos usuários de CLI.

- [Frontend / Interface Web](./frontend/) — Skills para interface web, design systems, frameworks frontend, acessibilidade e experiencias no navegador. _(Skills for web UI, design systems, frontend frameworks, accessibility and browser experiences.)_
- [Backend / Servidor](./backend/) — Skills para APIs, bancos de dados, frameworks server-side e arquitetura backend. _(Skills for APIs, databases, server-side frameworks and backend architecture.)_
- [Dados & IA / Data & AI](./data-ai/) — Skills para LLMs, agentes, machine learning, avaliacao, busca vetorial e sistemas de IA. _(Skills for LLMs, agents, ML, evaluation, vector search and AI systems.)_
- [Ferramentas / Tooling](./tooling/) — Skills para ferramentas de desenvolvedor, CLIs, fluxos locais e utilitarios gerais. _(Skills for developer tools, CLI skills, local workflows and general-purpose utilities.)_
- [Fluxos & Orquestracao / Workflow](./workflow/) — Skills para orquestracao de projetos, planejamento e sistemas de execucao. _(Skills for project orchestration, planning and execution systems.)_
- [Seguranca / Security](./security/) — Skills para auditoria de seguranca, hardening, threat modeling e testes ofensivos/defensivos. _(Skills for security auditing, hardening, threat modeling and offensive/defensive testing.)_
- [Cloud & DevOps](./cloud-devops/) — Skills para plataformas cloud, infraestrutura, deploy, containers e operacao de plataforma. _(Skills for cloud platforms, infrastructure, deployment, containers and platform operations.)_
- [Mobile](./mobile/) — Skills para iOS, Android, Expo, React Native, Flutter e engenharia mobile. _(Skills for iOS, Android, Expo, React Native, Flutter and mobile-specific engineering.)_
- [Games / Game Dev](./game-dev/) — Skills para engines de jogos, sistemas de gameplay, 3D interativo e desenvolvimento de jogos. _(Skills for game engines, gameplay systems, interactive 3D and game development.)_
- [Docs & Conteudo / Docs & Content](./docs-content/) — Skills para documentacao, escrita, sistemas de conteudo e fluxos de publicacao. _(Skills for documentation, writing, content systems and publishing workflows.)_
- [Automacao & Integracoes / Automation & Integrations](./automation/) — Skills para integracoes, automacoes SaaS, workflows e conectores externos. _(Skills for app integrations, SaaS automations, workflows and external tool connectors.)_
- [Negocios & Growth / Business & Growth](./business/) — Skills para produto, marketing, analytics, vendas, precificacao e operacao de negocios. _(Skills for product, marketing, analytics, sales, pricing and business operations.)_

---
<!-- END GLOBAL IMPORT CATEGORIES -->
## Contribuindo

Quer criar uma skill ou melhorar uma existente? Abra uma issue ou Pull Request.
