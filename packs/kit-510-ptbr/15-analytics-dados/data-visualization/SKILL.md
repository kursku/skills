---
name: data-visualization
description: "Data Visualization — Skill especializada para criar visualizações de dados, dashboards e relatórios impactantes a partir de dados do Google Analytics 4 e outras fontes, focando em storytelling e insights acionáveis."
license: MIT
metadata:
  version: 1.0.0
  author: Cafe Code AI
  category: 15-analytics-dados
  updated: 2026-03-01
risk: safe
---

# Data Visualization

Esta skill capacita o Claude a projetar e implementar visualizações de dados avançadas, transformando métricas brutas do Google Analytics 4 (GA4) em dashboards acionáveis e relatórios estratégicos para otimização de performance e compreensão do comportamento do usuário.

---

## Keywords

Google Analytics 4, GA4, Looker Studio, BigQuery, Atribuição de Marketing, Funil de Conversão, Dashboards Interativos, Métricas de Engajamento, Dimensões Personalizadas, Explorações GA4, Storytelling com Dados, Heatmaps, Gráficos de Série Temporal, Cohort Analysis.

---

## Quick Start

1.  **Conectar GA4 ao Looker Studio:** Abra o Looker Studio, clique em "Criar" -> "Fonte de dados". Selecione "Google Analytics", autorize a conexão e escolha sua propriedade GA4.
2.  **Criar Dashboard de Performance:** Adicione um novo relatório, insira um gráfico de série temporal (Time series chart) com a dimensão `Data` e a métrica `Sessões` do GA4.
3.  **Visualizar Engajamento:** Crie um cartão de resultados (Scorecard) com a métrica `Tempo médio de engajamento` e um gráfico de barras para `Visualizações por evento` (Event count) agrupado por `Nome do evento` (Event name).
4.  **Configurar Filtro de Data:** Adicione um controle de filtro de data ao dashboard, configurando-o para aplicar a todas as fontes de dados do relatório.
5.  **Publicar e Compartilhar:** Nomeie o dashboard, salve e use a opção de compartilhamento para gerar um link ou incorporar.

---

## Core Workflows

### Workflow 1: Análise Visual de Funil de Conversão E-commerce no Looker Studio com GA4

Este workflow detalha a construção de um dashboard de funil de conversão para e-commerce usando dados do GA4, permitindo identificar gargalos no processo de compra.

**Passos Detalhados:**

1.  **Conectar GA4 e BigQuery (Opcional, mas recomendado para flexibilidade):**
    *   No Looker Studio, adicione sua fonte de dados GA4. Para análises mais complexas de funil, especialmente com eventos personalizados ou regras de negócio específicas, configure a exportação de dados do GA4 para o BigQuery e use o conector BigQuery no Looker Studio.
    *   **Exemplo de Configuração GA4 para BigQuery:**
        *   Acesse o GA4, vá em "Administrador" > "Configurações do BigQuery".
        *   Clique em "Vincular" e siga os passos para conectar seu projeto do Google Cloud.
        *   Verifique se os eventos de e-commerce (`view_item`, `add_to_cart`, `begin_checkout`, `purchase`) estão sendo coletados corretamente no DebugView do GA4.
2.  **Definir Etapas do Funil:**
    *   Considere as etapas padrão de um funil de e-commerce: `Visualização de Item` -> `Adição ao Carrinho` -> `Início de Checkout` -> `Compra`.
    *   **Métricas e Dimensões GA4 Relevantes:**
        *   `Contagem de eventos` (Event count) para cada evento de funil.
        *   `Usuários ativos` (Active users) ou `Usuários totais` (Total users) para a base.
        *   `Nome do evento` (Event name) como dimensão de segmentação.
3.  **Construir o Gráfico de Funil (Looker Studio):**
    *   Adicione um gráfico de "Funil" (Funnel chart) ao seu relatório.
    *   **Configuração do Gráfico:**
        *   **Dimensão:** `Nome do evento` (Event name) ou um campo calculado que categorize as etapas.
        *   **Métrica:** `Contagem de eventos` (Event count).
        *   **Ordem:** Edite a ordem de classificação para que as etapas do funil apareçam na sequência correta (e.g., `view_item` antes de `add_to_cart`).
    *   **Exemplo de Campo Calculado (se usar BigQuery ou para agrupar eventos):**
        ```
        CASE
          WHEN event_name = 'view_item' THEN '1. Visualizou Produto'
          WHEN event_name = 'add_to_cart' THEN '2. Adicionou ao Carrinho'
          WHEN event_name = 'begin_checkout' THEN '3. Iniciou Checkout'
          WHEN event_name = 'purchase' THEN '4. Concluiu Compra'
          ELSE 'Outros'
        END
        ```
        *   No Looker Studio, clique em "Adicionar um campo" na fonte de dados e insira esta fórmula como "Etapa do Funil". Use este novo campo como sua dimensão.
4.  **Adicionar Métricas de Drop-off:**
    *   Crie scorecards com campos calculados para mostrar a taxa de drop-off entre cada etapa.
    *   **Exemplo de Fórmula para Taxa de Drop-off (Looker Studio):**
        *   Drop-off `view_item` para `add_to_cart`: `(COUNT(CASE WHEN event_name = 'view_item' THEN 1 ELSE NULL END) - COUNT(CASE WHEN event_name = 'add_to_cart' THEN 1 ELSE NULL END)) / COUNT(CASE WHEN event_name = 'view_item' THEN 1 ELSE NULL END)`
        *   Para simplificar, use métricas separadas para cada evento e calcule a taxa de conversão entre elas.
        *   `Taxa Conversão Item->Carrinho`: `(COUNT(CASE WHEN event_name = 'add_to_cart' THEN 1 ELSE NULL END) / COUNT(CASE WHEN event_name = 'view_item' THEN 1 ELSE NULL END))`
5.  **Segmentação e Filtragem:**
    *   Adicione um controle de `Grupo de Canais Padrão` (Default channel grouping) ou `Fonte / Mídia` (Source / Medium) para analisar o funil por canal.
    *   Adicione um filtro de data para permitir a análise em diferentes períodos.
6.  **Visualizar Insights:** Identifique a etapa com a maior queda de usuários. Por exemplo, se a transição de "Adicionou ao Carrinho" para "Iniciou Checkout" for a mais crítica, investigate problemas na página do carrinho ou no processo inicial de checkout.

### Workflow 2: Visualização Comparativa de Modelos de Atribuição no Looker Studio

Este workflow visa comparar a performance dos canais de marketing utilizando diferentes modelos de atribuição do GA4 para entender melhor o impacto de cada ponto de contato na jornada do cliente.

**Passos Detalhados:**

1.  **Acessar Dados de Atribuição no GA4:**
    *   No GA4, vá em "Publicidade" > "Atribuição" > "Comparação de modelos".
    *   Observe os modelos disponíveis: "Último clique (canais pagos e orgânicos)", "Primeiro clique", "Linear", "Decadência Temporal", "Baseado na Posição" e "Baseado em dados" (Data-Driven Attribution - DDA).
2.  **Conectar GA4 e BigQuery (Recomendado):**
    *   Embora o GA4 forneça relatórios de atribuição, para visualizações customizadas no Looker Studio que comparem múltiplos modelos ou envolvam dados de outras fontes, a exportação para o BigQuery é crucial.
    *   **Exemplo de Query BigQuery (simplificada para o conceito):**
        ```sql
        -- Esta query é ilustrativa para o conceito de atribuição.
        -- No GA4 BigQuery, a atribuição Data-Driven é um campo complexo (attribution_info)
        -- e requer desaninhamento ou uso de eventos purchase com attribution_id.
        -- Para uma comparação direta de modelos, utilize os dados agregados do GA4 via API ou relatórios.
        -- Para Looker Studio, vamos usar as métricas de atribuição disponíveis no conector GA4.
        SELECT
          traffic_source.source,
          SUM(ecommerce.purchase_revenue) AS revenue_last_click, -- Exemplo: usando evento purchase diretamente
          -- Métricas de atribuição Data-Driven, Last Click etc. são acessadas via conector GA4 no Looker Studio
          -- como métricas pré-agregadas (e.g., "Receita de Compra com Atribuição Data-Driven")
        FROM `seu-projeto.sua_dataset.events_*`
        WHERE event_name = 'purchase'
          AND _TABLE_SUFFIX BETWEEN FORMAT_DATE('%Y%m%d', DATE_SUB(CURRENT_DATE(), INTERVAL 90 DAY)) AND FORMAT_DATE('%Y%m%d', CURRENT_DATE())
        GROUP BY 1
        ORDER BY revenue_last_click DESC;
        ```
3.  **Criar o Relatório de Comparação no Looker Studio:**
    *   Adicione uma nova página ao seu dashboard.
    *   **Adicionar Tabela de Comparação:**
        *   Insira uma tabela.
        *   **Dimensão:** `Grupo de Canais Padrão` (Default channel grouping) ou `Fonte / Mídia` (Source / Medium).
        *   **Métricas:**
            *   `Total de receita (atribuição de último clique)` (Total revenue - Last click attribution)
            *   `Total de receita (atribuição baseada em dados)` (Total revenue - Data-driven attribution)
            *   `Total de conversões` (Total conversions) (para contexto)
    *   **Adicionar Gráfico de Barras Agrupadas:**
        *   Insira um gráfico de "Barras Agrupadas" (Grouped bar chart).
        *   **Dimensão:** `Grupo de Canais Padrão`.
        *   **Métricas:** As mesmas métricas de receita com atribuição de último clique e baseada em dados.
        *   Isso permitirá uma comparação visual rápida da contribuição de receita de cada canal sob diferentes modelos.
4.  **Adicionar Controles de Filtro:**
    *   Inclua um controle de `Data` e, se pertinente, um controle de `Campanha` ou `Evento`.
5.  **Analisar e Interpretar:**
    *   Observe como a receita é distribuída entre os canais em cada modelo.
    *   Canais que recebem mais crédito no modelo "Data-Driven" do que no "Último Clique" geralmente desempenham um papel importante no início ou meio da jornada do cliente.
    *   **Exemplo:** Se "Organic Search" tem uma receita significativamente maior no DDA comparado ao Último Clique, isso indica que o SEO contribui mais para iniciar jornadas de conversão do que apenas capturar a conversão final. Use essa informação para justificar investimentos em canais de topo de funil.

---

## Templates

### Template de Dashboard de Performance de Conteúdo (Looker Studio)

```
{
  "name": "Dashboard de Performance de Conteúdo GA4",
  "description": "Dashboard para monitorar a performance de páginas e artigos do site, identificando o conteúdo mais engajador e as fontes de tráfego.",
  "dataSources": [
    {
      "type": "GA4",
      "name": "Google Analytics 4 - Web",
      "properties": {
        "propertyId": "GA4_PROPERTY_ID_AQUI"
      }
    }
  ],
  "pages": [
    {
      "name": "Visão Geral de Conteúdo",
      "components": [
        {
          "type": "Scorecard",
          "metrics": ["Sessões", "Usuários ativos", "Visualizações", "Tempo médio de engajamento"],
          "title": "Métricas Chave de Engajamento"
        },
        {
          "type": "Table",
          "dimensions": ["Caminho da página e string de consulta", "Título da página"],
          "metrics": ["Sessões", "Usuários ativos", "Tempo médio de engajamento", "Taxa de rejeição", "Visualizações"],
          "sort": {"metric": "Sessões", "order": "DESC"},
          "title": "Páginas Mais Acessadas"
        },
        {
          "type": "Time series chart",
          "dimensions": ["Data"],
          "metrics": ["Visualizações", "Usuários ativos"],
          "title": "Visualizações e Usuários por Data"
        },
        {
          "type": "Bar chart",
          "dimensions": ["Grupo de Canais Padrão"],
          "metrics": ["Sessões"],
          "sort": {"metric": "Sessões", "order": "DESC"},
          "title": "Sessões por Canal"
        }
      ]
    }
  ],
  "controls": [
    {
      "type": "Date range control",
      "defaultDateRange": "Últimos 30 dias"
    },
    {
      "type": "Filter control",
      "dimension": "Grupo de Canais Padrão",
      "title": "Filtrar por Canal"
    }
  ]
}
```

### Template de Configuração de Alerta Personalizado (GA4) para Queda de Conversão

```
{
  "name": "Alerta de Queda de Conversão de Compra",
  "description": "Alerta automático para notificar sobre quedas significativas na taxa de conversão de compras, indicando potenciais problemas no checkout ou campanhas.",
  "type": "Custom Insight",
  "scope": "Propriedade GA4",
  "conditions": [
    {
      "metric": "Taxa de conversão de compra",
      "operator": "DIMINUI_EM_PERCENTAGEM",
      "value": "20%",
      "timeframe": "Diariamente",
      "compareTo": "Média dos últimos 7 dias"
    }
  ],
  "recipients": ["email@example.com", "outro.email@example.com"],
  "schedule": "Diariamente às 09:00 AM (fuso horário local)",
  "notes": "Verificar possíveis erros no carrinho, problemas de gateway de pagamento ou baixa performance de campanhas ativas."
}
```

---

## Checklist

- [x]  As cores dos gráficos são consistentes e transmitem o significado correto (ex: verde para positivo, vermelho para negativo)?
- [x]  Todos os gráficos possuem títulos descritivos e legendas claras?
- [x]  O dashboard possui filtros de data e segmentação que funcionam corretamente e são intuitivos?
- [x]  O tipo de gráfico escolhido é o mais adequado para o tipo de dado e a mensagem que se quer transmitir (ex: linha para série temporal, barra para comparação categórica)?
- [x]  Evitei a sobrecarga de informações, mantendo apenas os dados essenciais em cada visualização?
- [x]  As métricas e dimensões utilizadas são relevantes para o objetivo do relatório e são oriundas do GA4 (ou BigQuery)?
- [x]  A acessibilidade das cores foi considerada (contraste suficiente, evitar combinações problemáticas para daltônicos)?
- [x]  O dashboard foi testado em diferentes dispositivos/tamanhos de tela para garantir responsividade?
- [x]  Há um fluxo narrativo claro (storytelling) que guia o usuário através dos insights do dashboard?
- [x]  Os dados estão atualizados e a fonte de dados (GA4) está conectada corretamente?

---

## Métricas de Referência

| Métrica GA4              | Benchmark (E-commerce) | Meta (E-commerce)       |
|--------------------------|------------------------|-------------------------|
| Taxa de Conversão de Compra | 1.5% - 2.5%            | > 3.0%                  |
| Taxa de Engajamento        | 60% - 75%              | > 75%                   |
| ARPU (Receita por Usuário) | $15.00 - $30.00        | > $35.00                |
| Receita por Sessão         | $0.50 - $1.50          | > $2.00                 |
| % Abandono de Carrinho     | 60% - 75%              | < 60%                   |
| Tempo Médio de Engajamento | > 60 segundos          | > 90 segundos           |

---

## Erros Comuns

1.  **Gráficos de Pizza com Mais de 5 Fatias**: **Como evitar**: Gráficos de pizza se tornam ilegíveis com muitas categorias. Em vez disso, use gráficos de barras para comparar mais de 5 categorias, ou agrupe as categorias menores em "Outros". Exemplo: Ao invés de 10 fontes de tráfego em pizza, use um gráfico de barras e foque nas top 5.
2.  **Uso Inconsistente de Cores**: **Como evitar**: Defina uma paleta de cores padrão para seu dashboard. Use a mesma cor para representar a mesma métrica ou dimensão em diferentes gráficos. Exemplo: Sempre usar azul para "Sessões Orgânicas" e verde para "Sessões Pagas" em todos os gráficos de tráfego.
3.  **Não Normalizar Dados (Comparar Totais Brutos com Bases Diferentes)**: **Como evitar**: Ao comparar diferentes segmentos ou períodos, use percentuais, taxas ou índices para garantir uma comparação justa. Exemplo: Comparar "Taxa de Conversão" entre dois canais é mais relevante do que comparar "Número total de conversões" se os canais tiverem volumes de tráfego muito diferentes.
4.  **Excesso de Informação em um Único Gráfico/Dashboard**: **Como evitar**: Cada gráfico deve ter um propósito claro e transmitir uma única mensagem. Divida dashboards complexos em múltiplas páginas ou use filtros para permitir que o usuário explore os detalhes sob demanda. Exemplo: Em vez de um único gráfico com 10 linhas de métricas diferentes, crie 2-3 gráficos menores, cada um com 2-3 linhas relacionadas.
5.  **Ignorar a Contextualização dos Dados**: **Como evitar**: Sempre adicione um título descritivo e, se necessário, uma breve anotação ou texto explicativo ao lado de gráficos importantes para fornecer contexto e interpretar o que os dados estão mostrando. Exemplo: Em vez de apenas "Sessões por Mês", use "Sessões Totais por Mês (Impacto da Campanha X em Março)".

---

## Dicas Avançadas

1.  **Implementar "Small Multiples" no Looker Studio**: Crie gráficos pequenos e repetitivos para comparar facilmente a mesma métrica em diferentes dimensões (ex: vendas por produto ao longo do tempo, repetido para cada região). Isso pode ser feito usando filtros de relatório para cada seção ou replicando gráficos e ajustando filtros de nível de componente.
2.  **Utilizar Parâmetros de URL para Dashboards Dinâmicos**: No Looker Studio, é possível passar parâmetros via URL para pré-filtrar relatórios. Isso permite criar links personalizados que abrem o dashboard já filtrado por um cliente, campanha ou período específico, economizando tempo e tornando o compartilhamento mais eficiente. Exemplo: `https://lookerstudio.google.com/reporting/report-id/page/page-id?params={"control_0":{"value":"campaign_name"}}`.
3.  **Criar Métricas e Dimensões Personalizadas Complexas no Looker Studio**: Vá além das métricas padrão do GA4. Use campos calculados para criar métricas de negócio específicas. Exemplo: Uma métrica para "Receita por Sessão Engajada" (`SUM(CASE WHEN event_name = 'purchase' THEN (SELECT value.double_value FROM UNNEST(event_params) WHERE key = 'value') ELSE 0 END) / COUNT(DISTINCT CASE WHEN engagement_time_msec > 10000 THEN CONCAT(user_pseudo_id, CAST(ga_session_id AS STRING)) END)` - esta é uma formulação complexa e requer BigQuery para ser precisa para sessões engajadas).
4.  **Explorar o Recurso de "Explorações" do GA4 para Prototipagem**: Antes de construir um dashboard complexo no Looker Studio, use as "Explorações" (Explorations) do GA4 para validar suas hipóteses, testar combinações de dimensões/métricas e identificar padrões. A "Exploração de Funil" e a "Exploração de Caminho" são excelentes para prototipar funis e jornadas do usuário.
5.  **Integrar Dados de CRM ou Outras Fontes via Google Apps Script**: Para uma visão 360°, conecte dados de CRM (ex: Salesforce, Hubspot) ou planilhas de marketing ao Looker Studio usando conectores personalizados desenvolvidos com Google Apps Script. Isso permite cruzar dados de GA4 com informações de vendas offline ou de leads, criando um dashboard unificado de atribuição completa.