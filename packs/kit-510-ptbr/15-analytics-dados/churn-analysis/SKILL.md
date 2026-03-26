---
name: churn-analysis
description: "Churn Analysis — Skill especializada para churn analysis"
license: MIT
metadata:
  version: 1.0.0
  author: Cafe Code AI
  category: 15-analytics-dados
  updated: 2026-03-01
risk: safe
---

# Churn Analysis

Esta skill capacita o Claude a realizar análises aprofundadas de churn, identificando padrões de perda de usuários e clientes, segmentando grupos de risco e propondo estratégias de retenção baseadas em dados concretos do Google Analytics 4.

---

## Keywords

Churn Rate, Retenção de Clientes, Lifetime Value (LTV), GA4 Explorations, Segmentação de Audiência, Análise Cohort, Prevenção de Churn, Modelagem Preditiva, Atribuição de Churn, Eventos GA4, Audiências Preditivas, Customer Journey Analytics, Desengajamento, Fidelização.

---

## Quick Start

1.  **Validar Configuração de Eventos GA4**: Verificar se `user_cancellation`, `subscription_end`, `plan_downgrade` (para SaaS) ou `purchase` e `refund` (para e-commerce) estão sendo disparados corretamente no GA4.
2.  **Criar Exploração de Funil de Churn**: No GA4, configurar uma exploração de funil para mapear o `customer_journey` até o evento de churn, identificando gargalos.
3.  **Definir Audiência Preditiva 'Prováveis Churners'**: Utilizar as capacidades preditivas do GA4 para criar uma audiência automática de usuários com alta probabilidade de churn nos próximos 7 dias.
4.  **Monitorar Painel de Retenção**: Acessar o relatório padrão "Retenção" do GA4 para uma visão inicial da taxa de retenção por coorte e do valor da vida útil do usuário.
5.  **Exportar Dados para BI (Opcional)**: Para análises mais complexas, exportar dados de eventos e usuários do GA4 via BigQuery para uma ferramenta de BI como Looker Studio, Power BI ou Tableau.

---

## Core Workflows

### Workflow 1: Identificação e Segmentação de Churn no GA4

Este workflow foca em como utilizar o Google Analytics 4 para identificar usuários em risco de churn e segmentá-los para ações direcionadas.

**Passos Detalhados:**

1.  **Verificação de Eventos de Ciclo de Vida**:
    *   **Ação**: Acessar "Administrador" > "Configurações de dados" > "Eventos" no GA4.
    *   **Exemplo**: Confirmar a existência e o disparo de eventos como `session_start`, `page_view`, `add_to_cart`, `purchase`, `subscription_start`, `subscription_renew`, `subscription_cancel` ou `refund`. É crucial ter eventos que marquem tanto o engajamento quanto o desengajamento. Se o churn for definido por inatividade, certificar-se de que a `session_duration` e `user_engagement` estão sendo coletados.
    *   **Configuração Real**: Para um SaaS, um evento `subscription_cancel` disparado após a confirmação do cancelamento é essencial. Para e-commerce, `refund` ou ausência de `purchase` por X dias após a última compra.

2.  **Criação de Exploração de Funil para o Customer Journey**:
    *   **Ação**: Navegar para "Explorar" > "Explorações" > "Caminho" no GA4.
    *   **Exemplo**:
        *   **Nome da Exploração**: "Jornada de Churn - SaaS"
        *   **Etapa 1**: `session_start` (Usuário inicia sessão)
        *   **Etapa 2**: `view_plan_page` (Usuário visita página de planos)
        *   **Etapa 3**: `subscription_start` (Usuário assina)
        *   **Etapa 4 (Opcional)**: `feature_X_used` (Usuário usa recurso chave)
        *   **Etapa 5**: `subscription_cancel` (Usuário cancela assinatura)
    *   **Análise**: Observar as taxas de conversão entre as etapas e, principalmente, onde a maior perda ocorre antes do `subscription_cancel`. Isso revela pontos de fricção ou desengajamento precoce.

3.  **Definição de Audiências Preditivas 'Prováveis Churners'**:
    *   **Ação**: Ir para "Administrador" > "Configurações de dados" > "Audiências" > "Nova Audiência" > "Audiências Preditivas" no GA4.
    *   **Exemplo**: Selecionar a audiência "Prováveis Churners" (se elegível pela volumetria de dados). O GA4 usa modelos de machine learning para identificar usuários que provavelmente não farão uma compra ou não retornarão em 7 dias.
    *   **Configuração Alternativa (Manual)**: Se a preditiva não for elegível, criar uma audiência com base em condições de eventos:
        *   **Nome**: "Usuários de Baixo Engajamento (Risco Churn)"
        *   **Condições**:
            *   `user_engagement` < 60 segundos nos últimos 7 dias.
            *   `session_start` = 1 nos últimos 7 dias (apenas uma sessão).
            *   EXCLUIR `purchase` ou `subscription_start` nos últimos 30 dias.
    *   **Uso**: Ativar essa audiência para campanhas de reengajamento no Google Ads ou exportar via BigQuery para outras plataformas.

### Workflow 2: Análise de Causas Raiz e Atribuição de Churn

Este workflow aborda a investigação das razões por trás do churn e a atribuição de eventos ou campanhas que podem ter influenciado a decisão do usuário.

**Passos Detalhados:**

1.  **Análise de Cohort para Retenção**:
    *   **Ação**: Acessar "Relatórios" > "Retenção" > "Retenção de usuários por coorte" no GA4.
    *   **Exemplo**: Analisar a retenção de usuários que iniciaram sessão em semanas ou meses específicos. Se uma coorte de "Usuários adquiridos em Janeiro/2024" tem uma queda acentuada na retenção após 30 dias em comparação com "Usuários adquiridos em Dezembro/2023", investigar o que mudou (campanhas, produto, onboarding) para essa coorte específica.
    *   **Insight**: Uma queda abrupta na retenção de uma coorte específica pode indicar problemas de qualidade do produto, falha no onboarding ou expectativas desalinhadas pela campanha de aquisição.

2.  **Cruzamento de Dados de Churn com Eventos de Interação**:
    *   **Ação**: Utilizar a "Exploração de Caminho" ou "Exploração do Usuário" no GA4 para observar a sequência de eventos antes do churn.
    *   **Exemplo (Exploração de Caminho)**:
        *   **Ponto de Partida**: Evento `subscription_cancel` ou `refund`.
        *   **Passos Anteriores**: Analisar os 3-5 eventos que ocorreram *antes* do evento de churn.
        *   **Cenário**: Muitos usuários cancelam após `view_pricing_page` (indicando busca por alternativas) ou após `submit_support_ticket` (indicando problemas não resolvidos).
    *   **Exemplo (Exploração do Usuário)**:
        *   **Ação**: Filtrar por usuários na audiência "Prováveis Churners" e analisar suas jornadas individuais.
        *   **Cenário**: Identificar padrões como "não usou o recurso X", "visitou a página de suporte várias vezes", "não abriu e-mails de onboarding".

3.  **Análise de Atribuição de Eventos Pré-Churn**:
    *   **Ação**: Exportar dados do GA4 para BigQuery e usar SQL para analisar a sequência de eventos e suas fontes/mídias antes do churn.
    *   **Exemplo (SQL no BigQuery)**:
        ```sql
        SELECT
            user_pseudo_id,
            event_name,
            event_timestamp,
            (SELECT value.string_value FROM UNNEST(event_params) WHERE key = 'page_location') as page_location,
            (SELECT value.string_value FROM UNNEST(event_params) WHERE key = 'source') as source,
            (SELECT value.string_value FROM UNNEST(event_params) WHERE key = 'medium') as medium
        FROM
            `project_id.dataset_id.events_*`
        WHERE
            event_name IN ('subscription_cancel', 'refund', 'view_pricing_page', 'submit_support_ticket')
            AND _TABLE_SUFFIX BETWEEN 'YYYYMMDD' AND 'YYYYMMDD'
        ORDER BY
            user_pseudo_id, event_timestamp
        ```
    *   **Análise**: Correlacionar a origem (source/medium) de sessões que precedem o churn com o volume de churners. Por exemplo, se usuários vindo de campanhas "X" possuem uma taxa de churn significativamente maior, a campanha pode estar atraindo o público errado ou gerando expectativas irreais.

4.  **Geração de Relatórios de Engajamento e Retenção no GA4**:
    *   **Ação**: Utilizar os relatórios padrões "Engajamento" e "Retenção" do GA4 para monitoramento contínuo.
    *   **Exemplo**:
        *   **Relatório "Visão geral do engajamento"**: Focar em "Sessões engajadas por usuário", "Tempo médio de engajamento" e "Contagem de eventos". Quedas nessas métricas podem ser precursores de churn.
        *   **Relatório "Retenção de usuários por coorte"**: Monitorar a retenção ao longo do tempo para identificar tendências positivas ou negativas em grupos específicos.

---

## Templates

### Relatório de Churn Mensal (Resumido)

```
**Relatório de Churn - Mês: Fevereiro/2024**

**1. Visão Geral do Churn**
*   **Churn Rate Mensal**: 3.8% (Janeiro: 3.5%)
*   **Número de Churners**: 1,250 clientes (Janeiro: 1,100)
*   **Receita Perdida (MRR Churn)**: R$ 85.000 (Janeiro: R$ 78.000)

**2. Segmentação de Churners**
*   **Clientes Novos (0-90 dias)**: 45% do churn total (Taxa de Churn: 7.2%)
*   **Clientes Experientes (>90 dias)**: 55% do churn total (Taxa de Churn: 2.1%)
*   **Segmento por Plano (SaaS)**:
    *   Plano Básico: 60% do churn (Taxa de Churn: 4.5%)
    *   Plano Premium: 25% do churn (Taxa de Churn: 1.8%)
    *   Plano Enterprise: 15% do churn (Taxa de Churn: 0.9%)

**3. Causas Iniciais (Baseado em GA4 e Feedback)**
*   **Falta de Engajamento com Recurso Chave X**: 30% dos churners (identificado por baixa `feature_X_used` antes do cancelamento).
*   **Problemas de Suporte**: 20% dos churners (identificado por `submit_support_ticket` e `support_ticket_closed` com baixa satisfação).
*   **Preço/Concorrência**: 15% dos churners (inferido por `view_pricing_page` antes do cancelamento e feedback direto).

**4. Ações Recomendadas**
*   **Onboarding**: Otimizar o onboarding para Clientes Novos (0-90 dias) do Plano Básico, com foco no recurso X.
*   **Suporte**: Treinamento da equipe de suporte e revisão de FAQs para os problemas mais frequentes identificados.
*   **Reengajamento**: Campanhas direcionadas (e-mail, push) para a audiência "Usuários de Baixo Engajamento (Risco Churn)" do GA4.
```

### Definição de Audiência Preditiva "Prováveis Churners" (GA4)

```
**Nome da Audiência:** Prováveis Churners (SaaS/E-commerce)

**Descrição:** Usuários com alta probabilidade de churn nos próximos 7 dias, baseada no comportamento de eventos de engajamento e desengajamento.

**Condições da Audiência:**

**1. Usar modelo preditivo:**
   *   **Critério:** Probabilidade de Churn
   *   **Condição:** Probabilidade de Churn está no Top 10% dos usuários (ou outro percentil relevante, ajustado pela elegibilidade do modelo GA4).

**OU (se modelo preditivo não estiver disponível/elegível):**

**2. Criar manualmente com base em eventos e tempo:**
   *   **Condição 1 (Comportamento de Inatividade Recente):**
       *   Eventos: `session_start`
       *   Parâmetros: `event_count` < 2
       *   Período: Últimos 7 dias
   *   **Condição 2 (Exclusão de Engajamento Recente - OU):**
       *   Eventos: `purchase` (para e-commerce) OU `subscription_start` OU `feature_X_used` (para SaaS)
       *   Parâmetros: `event_count` = 0
       *   Período: Últimos 30 dias
   *   **Condição 3 (Histórico de Engajamento - E):**
       *   Eventos: `session_start`
       *   Parâmetros: `event_count` >= 3
       *   Período: Últimos 90 dias (para garantir que não são usuários novos sem histórico)

**Disparar para:** Google Ads, BigQuery (para integração com CRM/Automação de Marketing).
```

---

## Checklist

-   [x] Eventos de ciclo de vida do cliente (ex: `subscription_start`, `subscription_cancel`, `purchase`, `refund`) configurados e validados no GA4.
-   [x] Métricas de engajamento (ex: `user_engagement`, `session_duration`, `event_count`) rastreadas e monitoradas no GA4.
-   [x] Exploração de Funil no GA4 configurada para mapear a jornada do cliente até o churn.
-   [x] Audiência de "Prováveis Churners" (preditiva ou manual) criada e monitorada no GA4.
-   [x] Dados de churn cruzados com outras fontes (ex: feedback de clientes, tickets de suporte, pesquisas de satisfação).
-   [x] Análise de cohort para retenção realizada, identificando grupos de usuários com baixa retenção.
-   [x] Relatórios de atribuição de churn (seja no GA4 ou via BigQuery) gerados para entender canais/fontes de risco.
-   [x] Painel de churn (ex: no Looker Studio) atualizado com métricas chave e tendências.
-   [x] Estratégias de retenção (ex: campanhas de reengajamento, melhorias no produto) baseadas nos insights da análise de churn.
-   [x] Definição clara de "churn" para o negócio (ex: inatividade de 30 dias, cancelamento de assinatura, ausência de compra por 90 dias).

---

## Métricas de Referência

| Métrica                      | Benchmark (SaaS B2B) | Benchmark (SaaS B2C) | Meta (Exemplo) |
| :--------------------------- | :------------------- | :------------------- | :------------- |
| Churn Rate Mensal            | 0.5% - 2%            | 3% - 7%              | < 2%           |
| Churn Rate Anual             | 5% - 15%             | 25% - 50%            | < 10%          |
| Churn de Receita (MRR Churn) | 0.2% - 1%            | 2% - 5%              | < 0.8%         |
| Taxa de Retenção de Clientes | 90% - 95%            | 70% - 85%            | > 92%          |
| Tempo Médio para Churn       | > 12 meses           | 3 - 6 meses          | > 10 meses     |

---

## Erros Comuns

1.  **Não diferenciar Churn Voluntário e Involuntário**:
    *   **Erro**: Tratar todos os churns da mesma forma. O churn voluntário (cliente decide sair) e involuntário (falha no cartão de crédito) exigem abordagens de retenção distintas.
    *   **Como evitar**: Implementar eventos GA4 específicos ou integrar dados de pagamento que permitam categorizar o churn. Exemplo: `subscription_cancel` (voluntário) vs. `payment_failure` sem renovação (involuntário). Criar audiências separadas para cada tipo.
2.  **Focar apenas na Taxa de Churn Total, ignorando segmentos**:
    *   **Erro**: Olhar apenas para a métrica global, sem entender quais segmentos de clientes estão churnando mais ou por que.
    *   **Como evitar**: Sempre segmentar a análise de churn por tipo de plano, coorte de aquisição, fonte de tráfego, tipo de produto, região, etc., usando as "Explorações" e "Audiências" do GA4. Exemplo: Identificar que o Churn Rate é 15% para clientes do "Plano Básico" versus 2% para o "Plano Premium".
3.  **Não ter eventos de ciclo de vida do cliente bem definidos no GA4**:
    *   **Erro**: Não ter eventos claros que marquem o início, engajamento e fim da jornada do cliente, dificultando a identificação precisa do churn e seus precursores.
    *   **Como evitar**: Mapear o `customer_journey` e garantir que todos os pontos críticos (ex: `signup`, `first_purchase`, `subscription_start`, ``feature_used`, `subscription_cancel`, `refund`) sejam disparados como eventos no GA4 com parâmetros relevantes. Isso permite criar funis e audiências precisas.

---

## Dicas Avançadas

1.  **Integração de Dados CRM/Transacionais via User-ID no GA4**: Para uma visão 360°, envie o `user_id` do seu CRM para o GA4. Isso permite cruzar eventos de comportamento online com dados offline (ex: valor do contrato, histórico de suporte, feedback de vendas), enriquecendo a análise de churn e a segmentação de risco.
2.  **Modelagem Preditiva de Churn Fora do GA4 (e Importação)**: Para cenários complexos, utilize ferramentas de Machine Learning (Python/R) para construir modelos preditivos de churn mais sofisticados, incorporando dados de diversas fontes (GA4 via BigQuery, CRM, produto). Os resultados (ex: score de risco de churn para cada `user_id`) podem ser importados de volta para o GA4 como dimensões personalizadas para segmentação e ativação.
3.  **Análise de "Micro-Churns" ou Desengajamento Precoce**: Em vez de esperar pelo churn final, monitore eventos de desengajamento (ex: `session_duration` abaixo do normal, `feature_X_not_used` por X dias, visita à página de "cancelar" ou "preços da concorrência") como indicadores precoces. Crie audiências específicas no GA4 para esses "micro-churners" e ative campanhas de reengajamento proativas.
4.  **Atribuição Multi-touch para Churn**: Utilize modelos de atribuição mais avançados (ex: linear, baseado em tempo, data-driven via BigQuery) para entender não apenas o último ponto de contato antes do churn, mas toda a sequência de interações que contribuíram para a decisão. Isso revela quais canais ou campanhas estão consistentemente presentes na jornada de churn.
5.  **Personalização da Jornada de Reengajamento com Audiências GA4**: Após identificar segmentos de churners (ex: "churn por preço", "churn por falta de uso"), crie audiências GA4 para cada um. Utilize essas audiências para personalizar mensagens em campanhas de e-mail marketing, anúncios no Google Ads ou notificações push, abordando a causa raiz específica do churn para cada grupo.