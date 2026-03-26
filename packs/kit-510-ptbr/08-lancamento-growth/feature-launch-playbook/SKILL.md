---
name: feature-launch-playbook
description: "Feature Launch Playbook — Skill especializada para feature launch playbook"
license: MIT
metadata:
  version: 1.0.0
  author: Cafe Code AI
  category: 08-lancamento-growth
  updated: 2026-03-01
risk: safe
---

# Feature Launch Playbook

Esta skill equipa o Claude com um framework pragmático para planejar, executar e otimizar lançamentos de funcionalidades, maximizando ativação e retenção.

---

## Keywords

Lançamento de features, Go-to-Market (GTM) de feature, Aceleração de adoção, Ativação de produto, Retenção pós-lançamento, Ciclo de feedback de features, Growth hacking, Experimentação de lançamento, Análise de impacto de feature, Feature adoption.

---

## Quick Start

1.  **Validação Pré-Lançamento com Early Adopters**: Antes de qualquer desenvolvimento, conduza entrevistas de 30 minutos com 5-10 usuários do segmento "Ideal Customer Profile" para validar a hipótese de valor da feature e identificar dores críticas não atendidas. Ex: "Você usaria um painel de automação que reduz a entrada manual de dados em 50%?"
2.  **Configuração de Event Tracking**: Implemente eventos de rastreamento no Amplitude ou Mixpanel para `feature_viewed`, `feature_activated` (primeiro uso), e `key_action_within_feature` (ex: `automation_rule_created`) em até 2 dias após a finalização do escopo.
3.  **Lançamento Segmentado com Feature Flag**: Utilize uma ferramenta como LaunchDarkly para liberar a feature `nova_automacao_email` para 10% da sua base de "Early Adopters" (usuários que se inscreveram para betas) nas primeiras 24 horas após o deploy.
4.  **Monitoramento Imediato da Ativação**: Monitore a taxa de ativação (DAU/MAU que usaram a feature) e o tempo médio para o primeiro uso nas primeiras 72 horas pós-lançamento via dashboard no Looker Studio. Acione alertas se a ativação estiver abaixo de 20%.

---

## Core Workflows

### Workflow 1: Orquestração de Lançamento de Feature Gated (Acesso Exclusivo)

Este workflow detalha o processo de lançamento de uma feature com acesso restrito a um segmento específico de usuários, ideal para features premium ou em fase de teste.

1.  **Segmentação e Habilitação (Pré-lançamento)**:
    *   **Identificação do Segmento**: No Braze, identifique 500 usuários do segmento "Clientes Enterprise Ativos" (ARPU > $1000, logados > 15 dias no mês) que expressaram interesse em automação.
    *   **Configuração do Gate**: Configure a `feature_automacao_avancada_email` no LaunchDarkly para ser visível e funcional apenas para este segmento de 500 usuários. Defina um "kill switch" para desativar instantaneamente em caso de problemas críticos.
    *   **Exemplo**: Para a feature "Editor de Fluxos de Automação Visual", o acesso é restrito a clientes do plano "Enterprise Growth" que já utilizam o módulo de "Campanhas de E-mail" há pelo menos 3 meses.

2.  **Comunicação Direcionada (Lançamento)**:
    *   **Criação do Conteúdo**: Redija um e-mail personalizado no Customer.io com o assunto "Acesso Antecipado: Libere o Poder do Editor de Fluxos de Automação Visual!" para o segmento pré-selecionado. O e-mail deve focar nos benefícios (ex: "Crie sequências complexas em minutos, visualize todo o funil do cliente") e incluir um CTA claro "Acessar Agora".
    *   **In-App Message Contextual**: Configure uma mensagem in-app via Intercom para aparecer quando um usuário do segmento visitar a página de "Automações" pela primeira vez, informando sobre a nova funcionalidade.
    *   **Exemplo**: O e-mail terá um link direto para `app.empresa.com/automacao/editor-visual` e um vídeo-tutorial de 60 segundos incorporado, demonstrando a criação de um fluxo de boas-vindas.

3.  **Monitoramento de Ativação e Engajamento (Pós-lançamento)**:
    *   **Dashboard de Ativação**: Utilize um dashboard no Power BI para monitorar em tempo real a `taxa_de_ativacao_editor_visual` (usuários que acessaram o editor e criaram seu primeiro fluxo) e o `tempo_medio_primeiro_fluxo_criado`.
    *   **Métrica Chave**: A meta de ativação para este segmento de elite é de 45% em 7 dias. Se a taxa cair abaixo de 30%, acionar o time de Sucesso do Cliente para follow-up proativo.
    *   **Exemplo**: Se a `taxa_de_ativacao_editor_visual` estiver em 38% no terceiro dia, o time de Growth iniciará uma campanha de retargeting via push notification para os usuários que visualizaram o e-mail mas não ativaram, oferecendo um template de fluxo pronto.

4.  **Coleta de Feedback e Iteração (Pós-lançamento)**:
    *   **Pesquisa In-App Segmentada**: Após o usuário criar seu terceiro fluxo no editor, exiba um formulário de feedback NPS no Typeform perguntando "Qual a probabilidade de você recomendar o Editor de Fluxos de Automação Visual a um colega?"
    *   **Entrevistas Qualitativas**: Agende 10 entrevistas de 45 minutos com usuários que ativaram e deram feedback negativo (NPS 0-6) para entender os pontos de fricção e "jobs-to-be-done" não atendidos.
    *   **Exemplo**: Use mapas de calor e gravações de sessão do Hotjar na página do editor para identificar áreas de confusão ou elementos não clicados, direcionando melhorias de UX para a próxima sprint.

### Workflow 2: Otimização Contínua de Adoção de Feature via Experimentação A/B

Este workflow foca em refinar a experiência de adoção de uma feature já lançada, utilizando testes A/B para maximizar seu uso.

1.  **Identificação de Gargalo (Análise)**:
    *   **Análise do Funil**: No Google Analytics 4, observe o funil de adoção da feature "Relatórios Personalizados". Identifique que 55% dos usuários que clicam em "Criar Novo Relatório" abandonam o processo antes de selecionar as dimensões.
    *   **Hipótese**: A interface inicial de seleção de dimensões é confusa ou exige muitos passos.
    *   **Exemplo**: O funil mostra que de 1000 cliques em "Criar Novo Relatório", apenas 450 chegam à tela de "Visualizar Relatório", indicando uma queda significativa na etapa de configuração.

2.  **Criação de Variações para Teste A/B (Design)**:
    *   **Variante A (Controle)**: Manter o fluxo atual de seleção de dimensões (lista de 50 opções com barra de busca simples).
    *   **Variante B (Teste)**: Implementar um assistente de "Quick Start" que sugere 5 templates de relatórios pré-definidos (ex: "Vendas Semanais", "Churn por Segmento") e um filtro de categoria para dimensões (ex: "Dados de Cliente", "Dados de Vendas").
    *   **Implementação**: Configure o A/B test via Optimizely, direcionando 50% do tráfego de novos usuários para a Variante B.

3.  **Execução do Teste e Coleta de Dados (Lançamento Controlado)**:
    *   **Duração do Teste**: Rode o teste por 21 dias ou até atingir significância estatística (p-value < 0.05 e intervalo de confiança de 95% para a métrica primária).
    *   **Métricas Primárias**: `relatorio_criado_completamente_rate` (usuários que criaram e salvaram um relatório) e `tempo_para_primeiro_relatorio_salvo`.
    *   **Métricas Secundárias**: `nps_feature_relatorios` e `uso_recorrente_relatorios_semanal`.
    *   **Exemplo**: O teste é monitorado diariamente. Se a `relatorio_criado_completamente_rate` da Variante B atingir 35% contra 28% da Variante A após 15 dias, e o p-value for 0.02, a Variante B será considerada vencedora.

4.  **Análise e Implementação (Pós-teste)**:
    *   **Tomada de Decisão**: Se a Variante B demonstrar uma melhoria estatisticamente significativa, implemente-a para 100% dos usuários.
    *   **Documentação dos Aprendizados**: Crie um documento no Confluence intitulado "A/B Test: Otimização Onboarding Relatórios Personalizados - Lições Aprendidas" detalhando a hipótese, variações, resultados e próximos passos.
    *   **Exemplo**: Após a implementação da Variante B, observe um aumento de 18% na criação de relatórios e uma redução de 1 minuto no `tempo_para_primeiro_relatorio_salvo`. Os próximos passos incluem testar a ordem dos templates pré-definidos.

---

## Templates

### Template de Email de Lançamento de Feature Gated (Acesso Antecipado)

```
Assunto: 🚀 Exclusivo para Você: Sua Nova Análise Preditiva de Churn está Liberada!

Olá [Nome do Usuário],

Temos uma excelente notícia para você! Como um de nossos clientes Enterprise mais valiosos, você foi selecionado para ter acesso antecipado à nossa mais revolucionária funcionalidade: a **Análise Preditiva de Churn**.

Com a Análise Preditiva de Churn, você poderá:
- **Identificar Clientes em Risco com 90% de Precisão**: Receba alertas proativos e intervenha antes que seja tarde.
- **Visualizar Fatores de Risco Chave**: Entenda os motivos por trás do churn através de gráficos intuitivos e recomendações acionáveis.
- **Otimizar Estratégias de Retenção**: Crie campanhas segmentadas e personalizadas baseadas em dados preditivos para maximizar o LTV.

Sabemos que você valoriza a **retenção de clientes e a receita recorrente**, e essa feature foi criada pensando exatamente em como podemos te ajudar a superar suas metas.

**Como Começar:**
1.  Acesse sua conta agora: [Link Direto para a Feature na Plataforma]
2.  Assista ao nosso rápido tutorial de 90 segundos para aproveitar ao máximo o poder da predição: [Link para Vídeo Tutorial no YouTube/Vimeo]

Sua opinião é fundamental para nós. Se tiver qualquer dúvida ou feedback inicial, nossa equipe de Sucesso do Cliente está à disposição para ajudar.

Aproveite a novidade e prepare-se para transformar sua estratégia de retenção!

Atenciosamente,

A Equipe [Nome da Empresa]
```

### Template de Relatório Pós-Lançamento de Feature

```
**Relatório Pós-Lançamento: Recomendações de Conteúdo A.I.**

**Data do Lançamento:** 2024-05-15
**Período de Análise:** 2024-05-15 a 2024-05-29 (14 dias)
**Equipe Responsável:** Produto (João Silva), Growth (Maria Souza), Marketing (Carlos Ribeiro)

**1. Objetivo do Lançamento:**
Aumentar a taxa de cliques (CTR) em conteúdos recomendados em 15% para usuários de planos Pro e Enterprise, com meta de 40% de ativação da feature em 7 dias (usuários que visualizaram e interagiram com 3+ recomendações).

**2. Métricas Chave e Resultados:**
-   **Usuários Alcançados (Total):** 15.000 (Segmento: Pro/Enterprise)
-   **Taxa de Ativação (7 dias):** 38% (Meta: 40%) - *Resultado: Ligeiramente abaixo da meta (2% de delta).*
-   **CTR em Conteúdo Recomendado:** 18% (Benchmark: 15%; Meta: 20%) - *Resultado: Acima do benchmark, mas abaixo da meta.*
-   **Uso Recorrente (DAU/MAU após 7 dias):** 12% (Meta: 15%) - *Resultado: Abaixo da meta.*
-   **Tempo Médio de Sessão com Feature:** 3 min 45 seg (Benchmark: 2 min) - *Resultado: Acima do benchmark, indicando engajamento inicial para quem ativa.*
-   **NPS da Feature (Coletado via Intercom):** +28 (Benchmark: +35) - *Resultado: Abaixo do benchmark, sugere oportunidades de melhoria.*

**3. Análise de Performance:**
-   **Pontos Positivos:** O e-mail de lançamento teve uma taxa de abertura de 35% e um CTR de 10%, indicando bom interesse inicial. Usuários que ativaram a feature demonstraram engajamento considerável (tempo de sessão). O aumento do CTR em relação ao benchmark é promissor.
-   **Pontos de Atenção:** A taxa de ativação ficou ligeiramente abaixo da meta. Observamos que 25% dos usuários que clicam no link do e-mail não chegam à página da feature devido a um problema de carregamento lento em navegadores mais antigos (identificado via Sentry). O NPS da feature sugere que a clareza da proposta de valor ou a qualidade das recomendações para alguns usuários ainda precisa ser otimizada. A retenção da feature também é um ponto de preocupação.

**4. Ações Recomendadas (Próximos 7-14 dias):**
1.  **Prioridade 1 (Engenharia):** Corrigir bug de carregamento lento em navegadores antigos (P0, ETA: 24h).
2.  **Prioridade 2 (Produto/UX):** Implementar um tour guiado de 3 passos na primeira ativação da feature para reforçar os benefícios e um botão "O que é isso?" para contextualizar as recomendações (Sprint atual).
3.  **Prioridade 3 (Marketing/Growth):** Criar campanha de retargeting (push notification e e-mail) para usuários que clicaram mas não ativaram, com foco em um caso de uso específico (ex: "Descubra conteúdos que seus concorrentes estão usando").
4.  **Prioridade 4 (Produto/Dados):** Realizar 5 entrevistas de 30 minutos com usuários com NPS baixo para entender os pontos de fricção específicos nas recomendações (ex: relevância, diversidade). Analisar logs de interação para otimizar o algoritmo de recomendação.

**5. Próximos Passos:**
-   Reavaliar métricas em 7 dias após a implementação das ações.
-   Planejar A/B test para o título do e-mail de retargeting e para a posição das recomendações na interface.
-   Investigar a correlação entre a ativação da feature e o churn geral do cliente.
```

---

## Checklist

- [x] Validação da hipótese de valor da feature com 5-10 usuários-alvo através de entrevistas de problema/solução.
- [x] Definição clara das métricas de sucesso (ex: `activation_rate`, `churn_reduction`) e benchmarks para a feature.
- [x] Configuração de Feature Flag (ex: LaunchDarkly) para controle de visibilidade e lançamento gradual.
- [x] Implementação de eventos de rastreamento de ativação (`feature_viewed`, `feature_used_first_time`, `key_action_within_feature`) no Amplitude/Mixpanel.
- [x] Criação de segmento de "Early Adopters" ou "Beta Testers" para o primeiro grupo de lançamento.
- [x] Redação e agendamento de comunicação de lançamento (email, in-app message, push notification) com CTAs claros e focados em benefício.
- [x] Preparação de dashboard de monitoramento em tempo real (ex: Looker Studio, Power BI) para as métricas da feature, com alertas configurados.
- [x] Planejamento de canais de feedback (NPS in-app, Typeform, entrevistas) pós-lançamento.
- [x] Treinamento da equipe de Suporte ao Cliente sobre a nova feature, incluindo FAQs e cenários de uso.
- [x] Documentação interna (Confluence/Notion) com roadmap pós-lançamento, próximos experimentos e lições aprendidas.
- [x] Garantia de que a feature tem um "kill switch" funcional para revers