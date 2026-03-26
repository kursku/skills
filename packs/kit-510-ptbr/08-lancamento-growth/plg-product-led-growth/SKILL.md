---
name: plg-product-led-growth
description: "Plg Product Led Growth — Skill especializada para plg product led growth"
license: MIT
metadata:
  version: 1.0.0
  author: Cafe Code AI
  category: 08-lancamento-growth
  updated: 2026-03-01
risk: safe
---

# Plg Product Led Growth

Esta skill capacita o Claude a implementar estratégias de Product-Led Growth (PLG), focando na otimização da experiência do produto para impulsionar aquisição, ativação, retenção e monetização de forma autônoma.

---

## Keywords

Product-Led Growth, PLG, Ativação, Retenção, Time-to-Value, TTV, Product Qualified Leads, PQL, Growth Loops, Onboarding, Freemium, Self-serve, Feature Adoption, Upsell, Experiência do Primeiro Valor, FTV, Churn Rate, NRR.

---

## Quick Start

1.  **Mapear o Caminho Crítico para o "Aha! Moment"**: Identifique a jornada do seu usuário desde o primeiro contato até a realização do valor principal do produto, focando nos eventos-chave que geram engajamento. Para um SaaS de gestão de projetos, o "Aha!" pode ser o usuário criar o primeiro projeto e convidar um membro da equipe.
2.  **Instrumentar Métricas de Ativação Essenciais**: Configure ferramentas de analytics (e.g., Mixpanel, Amplitude) para rastrear eventos que indicam a ativação do usuário, como "Projeto Criado", "Tarefa Concluída" ou "Integração Conectada", medindo o sucesso inicial.
3.  **Desenhar um Onboarding Guiado pelo Valor**: Crie uma sequência de passos no produto que leve o usuário diretamente ao "Aha! Moment", minimizando fricção e evitando tours de funcionalidades genéricos. Em vez de um tour, um "assistente de configuração" que ajuda a criar o primeiro projeto real.
4.  **Experimentar Micro-Iterações Contínuas nos Fluxos**: Execute pequenos testes A/B em elementos do onboarding ou fluxos de ativação para otimizar a taxa de sucesso. Teste duas versões do CTA na tela inicial para "Criar Primeiro Projeto" e analise qual gera mais cliques e ativações.

---

## Core Workflows

### Workflow 1: Otimização da Experiência "Aha! Moment" e Ativação

Este workflow detalha a criação de um caminho claro para o usuário experimentar o valor principal do produto rapidamente, convertendo novos registros em usuários ativados e engajados.

*   **Passo 1: Identificação do "Aha! Moment" e Eventos de Ativação Críticos**: Colabore com equipes de produto e dados para analisar o comportamento dos usuários mais retidos versus os que churnam rapidamente. Defina os 1-3 eventos-chave que correlacionam diretamente com a percepção de valor.
    *   **Exemplo Prático (SaaS de Email Marketing)**:
        *   **Hipótese**: Usuários que enviam a primeira campanha de email dentro de 48 horas têm 3x mais probabilidade de se tornarem pagantes.
        *   **"Aha! Moment"**: A campanha de email ser enviada com sucesso e gerar as primeiras aberturas/cliques.
        *   **Eventos Críticos de Ativação**: 1. Conexão de lista de contatos (mínimo 100 emails); 2. Criação do primeiro email (usando template); 3. Agendamento/Envio da campanha.
*   **Passo 2: Mapeamento da Jornada do Usuário até o "Aha! Moment"**: Desenhe o fluxo exato de cliques, telas e decisões que o usuário precisa fazer para chegar aos eventos críticos. Identifique pontos de fricção, dúvidas ou desistências que impedem a ativação.
    *   **Ferramentas**: User journey maps, gravação de sessão (e.g., Hotjar), funis de conversão em analytics (e.g., Amplitude).
    *   **Exemplo Prático (SaaS de Email Marketing)**:
        *   **Jornada Simplificada**: Cadastro -> Ver dashboard -> Clicar "Criar Campanha" -> Escolher template -> Editar conteúdo -> Conectar lista -> Agendar envio.
        *   **Fricções Comuns**: Dificuldade em importar contatos (muitos formatos, falta de guia); sobrecarga de opções de templates; dúvidas sobre conformidade GDPR.
*   **Passo 3: Redução da Fricção e Aceleração do Tempo ao Valor (TTV)**: Implemente melhorias no produto e na comunicação in-app para guiar o usuário de forma mais eficiente e intuitiva.
    *   **Estratégias**: Onboarding contextualizado, checklists de progresso com validação automática, tutoriais curtos e interativos, remoção de funcionalidades não essenciais no primeiro uso para evitar sobrecarga.
    *   **Exemplo Prático (SaaS de Email Marketing)**:
        *   **Ação 1 (Importação de Contatos)**: Adicionar um wizard guiado com opções de upload de CSV, integração com CRMs populares (HubSpot, Salesforce) e um vídeo explicativo de 60 segundos sobre melhores práticas.
        *   **Ação 2 (Criação de Email)**: Pré-selecionar o template mais popular para novos usuários e fornecer exemplos de conteúdo para o primeiro email, como "Primeiro Email de Boas-Vindas".
        *   **Ação 3 (Primeiro Envio)**: Um checklist de "Pré-lançamento" com validações automáticas (e.g., lista conectada, remetente configurado) e um CTA claro para "Enviar Agora", com feedback visual de sucesso.
*   **Passo 4: Medição e Iteração Contínua da Ativação**: Monitore as métricas de ativação e TTV. Realize testes A/B para validar as melhorias e continue iterando o fluxo de onboarding e a experiência do primeiro uso.
    *   **Métricas Chave**: Taxa de ativação (e.g., % de usuários que enviam 1ª campanha), TTV (tempo médio para 1ª campanha), % de usuários que completam o onboarding checklist.
    *   **Meta de Referência**: Aumentar a taxa de ativação de 25% para 40% em 3 meses.

### Workflow 2: Implementação de um Ciclo Virtuoso de Engajamento e Expansão

Este workflow foca em manter os usuários engajados após a ativação e incentivá-los a explorar funcionalidades de maior valor, levando à expansão do uso e, eventualmente, à monetização.

*   **Passo 1: Identificação de Gaps de Valor e Oportunidades de Expansão**: Após a ativação inicial, observe como os usuários engajam com as funcionalidades principais. Identifique onde eles poderiam obter mais valor (e, consequentemente, onde há potencial para upsell ou cross-sell) através de análise de comportamento.
    *   **Ferramentas**: Heatmaps de funcionalidades (Pendo, Amplitude), pesquisas in-app (Typeform), entrevistas com usuários para entender necessidades não atendidas.
    *   **Exemplo Prático (SaaS de Gestão de Projetos)**:
        *   **Usuário Ativado**: Já criou e gerenciou 3 projetos individuais em 30 dias.
        *   **Oportunidade de Expansão**: Usuários que gerenciam mais de 5 projetos em 30 dias se beneficiariam de funcionalidades de "Relatórios Avançados" ou "Gerenciamento de Portfólio", que são parte do plano Premium.
        *   **Gap de Valor**: Perda de visibilidade sobre o desempenho do projeto em nível estratégico e dificuldade em comparar múltiplos projetos.
*   **Passo 2: Criação de "Nudges" Contextuais para Adoção de Funcionalidades e Upgrade**: Desenvolva mensagens e elementos de UI que guiem os usuários para funcionalidades de maior valor ou para o próximo nível do plano, baseando-se no seu comportamento de uso.
    *   **Princípios**: Timing (quando o usuário está mais propenso a agir), Relevância (solucionando um problema atual do usuário), Clareza (CTA explícito e benefício claro).
    *   **Exemplo Prático (SaaS de Gestão de Projetos)**:
        *   **Nudge 1 (Adoção de Funcionalidade)**: Após o usuário criar o 4º projeto, um banner discreto na barra lateral sugere: "Gerenciando múltiplos projetos? Experimente nossos 'Relatórios de Portfólio' para uma visão unificada e tome decisões mais estratégicas."
        *   **Nudge 2 (Upgrade)**: Quando o usuário atinge 80% do limite de projetos do plano atual, um modal aparece suavemente: "Você está aproveitando ao máximo o [Nome do Plano Atual]! Com o [Nome do Plano Premium], você desbloqueia projetos ilimitados e relatórios avançados para escalar sua gestão sem interrupções."
        *   **Nudge 3 (Valor Adicional)**: Email automatizado 30 dias após a ativação para usuários que não exploraram integrações: "Maximize sua produtividade: Conecte [Produto] com Slack, Google Drive e mais. Veja como [Benefício da Integração]!"
*   **Passo 3: Desenvolvimento de um "Growth Loop" de Viralidade/Referência (Opcional, mas Poderoso)**: Projete o produto de forma que o uso por um usuário naturalmente convide outros, ou que a saída do produto gere valor para outros, criando um ciclo de aquisição embutido e sustentável.
    *   **Exemplo Prático (Ferramenta de Colaboração de Design)**:
        *   **Loop**: Usuário A cria um design e compartilha com Usuário B para feedback. Usuário B precisa se cadastrar (ou já está cadastrado) para comentar/editar. Usuário B, por sua vez, cria um design e convida Usuário C, perpet