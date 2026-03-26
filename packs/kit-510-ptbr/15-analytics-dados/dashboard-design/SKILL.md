---
name: dashboard-design
description: "Dashboard Design — Skill especializada para dashboard design"
license: MIT
metadata:
  version: 1.0.0
  author: Cafe Code AI
  category: 15-analytics-dados
  updated: 2026-03-01
risk: safe
---

# Dashboard Design

Esta skill capacita o Claude a projetar dashboards de analytics focados em GA4 e BigQuery, otimizando a visualização de dados para insights acionáveis e tomadas de decisão estratégica em marketing digital e e-commerce.

---

## Keywords

GA4, Looker Studio, BigQuery Export, Atribuição de Marketing, Funil de Conversão, Análise Cohort, Métricas de Engajamento, Dimensões Personalizadas, Relatórios de Aquisição, Visualização de Dados, KPIs de Marketing, CRO, LTV, CPA, ROAS, Eventos Personalizados.

---

## Quick Start

1.  **Conecte o GA4 ao Looker Studio:** Abra o Looker Studio, crie um novo relatório e adicione "Google Analytics" como fonte de dados, selecionando a propriedade GA4 desejada.
2.  **Adicione um Scorecard de Conversões:** Insira um scorecard exibindo a métrica `Eventos de conversão` filtrada para `event_name = 'purchase'` para monitorar vendas.
3.  **Crie um Gráfico de Série Temporal:** Utilize um gráfico de linhas com `Data` na dimensão de detalhe e `Total de usuários` e `Sessões engajadas` como métricas para visualizar tendências de audiência.
4.  **Insira uma Tabela de Canais de Aquisição:** Adicione uma tabela com a dimensão `Grupo de canais padrão da primeira interação do usuário` e métricas como `Novos usuários`, `Sessões engajadas` e `Receita total`.

---

## Core Workflows

### Workflow 1: Criação de Dashboard de Performance de E-commerce no Looker Studio com GA4

Este workflow foca na construção de um dashboard essencial para monitorar a performance de vendas e engajamento em lojas virtuais, utilizando dados do Google Analytics 4.

1.  **Verificação e Configuração de Eventos de E-commerce no GA4:**
    *   Garanta que os eventos de e-commerce padrão do GA4, como `view_item_list`, `view_item`, `add_to_cart`, `begin_checkout` e `purchase`, estejam corretamente implementados e coletando dados.
    *   Confirme que os parâmetros de item (ex: `item_id`, `item_name`, `price`, `quantity`) estão sendo enviados com esses eventos.
    *   **Exemplo:** No `purchase` event, verificar se `value` e `currency` estão populados.

2.  **Conexão da Propriedade GA4 ao Looker Studio:**
    *   No Looker Studio, crie um novo relatório em branco.
    *   Clique em "Adicionar dados", selecione "Google Analytics" e escolha a conta e propriedade GA4 correspondente ao seu e-commerce.

3.  **Construção da Seção de Visão Geral (KPIs Principais):**
    *   Adicione scorecards para os seguintes KPIs, utilizando o filtro de data "Últimos 30 dias" para todos:
        *   `Total de usuários`
        *   `Sessões engajadas`
        *   `Taxa de engajamento` (métrica calculada: `Sessões engajadas` / `Sessões`)
        *   `Eventos de conversão` (filtrado para `event_name = 'purchase'`)
        *   `Receita total`
        *   `Valor médio do pedido (AOV)` (métrica calculada: `Receita total` / `Eventos de conversão` (purchase))
    *   **Exemplo:** Um scorecard de `Receita total` exibindo "R$ 150.875" com uma comparação de "+18,5% vs. período anterior".

4.  **Criação do Relatório de Aquisição de Usuários e Receita por Canal:**
    *   Insira um gráfico de tabela.
    *   **Dimensão:** `Grupo de canais padrão da primeira interação do usuário`.
    *   **Métricas:** `Novos usuários`, `Sessões engajadas`, `Receita total`, `Eventos de conversão` (purchase).
    *   **Ordenação:** Pela métrica `Receita total` em ordem decrescente.
    *   **Exemplo:** Uma linha da tabela mostrando "Organic Search" com 5.200 novos usuários, 3.800 sessões engajadas, R$ 75.000 de receita e 300 conversões de compra.

5.  **Visualização da Evolução de Receita e Conversões:**
    *   Adicione um gráfico de série temporal (linhas).
    *   **Dimensão de detalhe:** `Data`.
    *   **Métricas:** `Receita total` e `Eventos de conversão` (purchase).
    *   **Exemplo:** Duas linhas, uma para receita e outra para conversões, mostrando a tendência diária, identificando picos de vendas em 15/01 (promoção) e 28/01 (fim de mês).

6.  **Análise de Produtos Mais Vendidos:**
    *   Insira um gráfico de tabela ou barras empilhadas.
    *   **Dimensão:** `Nome do item`.
    *   **Métricas:** `Receita do item`, `Quantidade do item`.
    *   **Filtro:** Incluir `event_name = 'purchase'`.
    *   **Exemplo:** Tabela listando "Camisa Polo Azul" com R$ 12.500 de receita e 250 unidades vendidas, "Tênis Esportivo X" com R$ 10.200 e 100 unidades vendidas.

### Workflow 2: Análise de Funil de Conversão e Atribuição Multicanal com GA4 e BigQuery

Este workflow demonstra como ir além dos relatórios padrão do GA4, utilizando a exportação para BigQuery para construir funis de conversão personalizados e analisar a atribuição de marketing de forma mais granular.

1.  **Configuração da Exportação GA4 para BigQuery:**
    *   Confirme que a exportação diária de dados brutos do GA4 para o BigQuery está ativa e funcionando. Isso permite acesso a cada evento individual e seus parâmetros.
    *   **Exemplo:** Verifique a existência de tabelas diárias como `seu_projeto.seu_dataset.events_20240101` no seu projeto BigQuery.

2.  **Definição dos Eventos do Funil de Conversão:**
    *   Identifique a sequência lógica de eventos que representam o funil de conversão no seu negócio.
    *   **Exemplo de Funil de E-commerce:** `view_item_list` (visualizou categoria) -> `view_item` (visualizou produto) -> `add_to_cart` (adicionou ao carrinho) -> `begin_checkout` (iniciou checkout) -> `purchase` (comprou).

3.  **Criação de Query SQL para Mapeamento do Funil no BigQuery:**
    *   Desenvolva uma query SQL que identifique quais usuários passaram por cada etapa do funil.
    *   **Query Exemplo para Funil de E-commerce (Últimos 30 dias):**
        ```sql
        SELECT
          user_pseudo_id,
          MAX(CASE WHEN event_name = 'view_item_list' THEN 1 ELSE 0 END) AS step_1_view_list,
          MAX(CASE WHEN event_name = 'view_item' THEN 1 ELSE 0 END) AS step_2_view_item,
          MAX(CASE WHEN event_name = 'add_to_cart' THEN 1 ELSE 0 END) AS step_3_add_to_cart,
          MAX(CASE WHEN event_name = 'begin_checkout' THEN 1 ELSE 0 END) AS step_4_begin_checkout,
          MAX(CASE WHEN event_name = 'purchase' THEN 1 ELSE 0 END) AS step_5_purchase
        FROM
          `seu_projeto.seu_dataset.events_*` -- Substitua pelo seu projeto e dataset GA4
        WHERE
          _TABLE_SUFFIX BETWEEN FORMAT_DATE('%Y%m%d', DATE_SUB(CURRENT_DATE(), INTERVAL 30 DAY)) AND FORMAT_DATE('%Y%m%d', CURRENT_DATE())
        GROUP BY
          user_pseudo_id
        HAVING
          step_1_view_list = 1 -- Apenas usuários que iniciaram o funil
        ```

4.  **Criação do Dashboard de Funil no Looker Studio (via BigQuery):**
    *   No Looker Studio, adicione uma nova fonte de dados, selecionando "BigQuery".
    *   Escolha "Consulta Personalizada" e cole a query SQL desenvolvida no passo anterior.
    *   Crie um gráfico de funil (ou barras empilhadas) usando as colunas `step_1_view_list` a `step_5_purchase` como métricas, somando a contagem de usuários em cada etapa.
    *   **Exemplo:** Visualização do funil mostrando 10.000 usuários em `view_item_list`, 5.000 em `view_item`, 1.500 em `add_to_cart`, 500 em `begin_checkout` e 150 em `purchase`, destacando as quedas.

5.  **Análise de Caminhos de Conversão e Atribuição no GA4 (Relatórios Padrão):**
    *   Acesse o GA4 > "Publicidade" > "Atribuição" > "Caminhos de conversão".
    *   Selecione `purchase` como tipo de conversão.
    *   Analise os caminhos mais comuns que os usuários percorrem antes de converter, observando a sequência de canais (ex: "Organic Search -> Direct -> Email -> Purchase").
    *   **Exemplo:** Identificar que "Email" é frequentemente o último ponto de contato antes da compra, mas "Organic Search" e "Paid Search" iniciam muitos caminhos.

6.  **Comparação de Modelos de Atribuição no GA4:**
    *   No GA4 > "Publicidade" > "Atribuição" > "Comparação de modelos".
    *   Compare o modelo de atribuição "Data-driven" (padrão do GA4) com outros modelos como "Último clique" ou "Primeiro clique" para entender como o crédito das conversões é distribuído entre os canais.
    *   **Exemplo:** Observar que o "Data-driven" atribui 20% mais crédito ao "Paid Search" do que o "Último clique" para `purchase` events, indicando seu papel importante no início da jornada.

---

## Templates

### Dashboard de Performance de Campanhas (Looker Studio)

```
# Dashboard de Performance de Campanhas - Google Ads & GA4

## Visão Geral - Período: Últimos 30 Dias (Controle de Data no canto superior direito)

| Métrica GA4 / Google Ads | Valor Atual | Delta vs. Período Anterior |
|--------------------------|-------------|----------------------------|
| Custo Total (Google Ads) | R$ 15.000   | +10%                       |
| Cliques (Google Ads)     | 45.000      | +12%                       |
| Impressões (Google Ads)  | 1.200.000   | +8%                        |
| Conversões (Compra - GA4)| 750         | +15%                       |
| Receita Total (GA4)      | R$ 140.000  | +20%                       |
| ROAS (Receita / Custo)   | 9.33x       | +0.83x                     |
| CPA (Custo / Conversões) | R$ 20,00    | -R$ 2,50                   |

---

## Performance por Campanha (GA4 & Google Ads)

**Gráfico:** Tabela interativa com controle de filtro para `Nome da Campanha` (Google Ads)

| Nome da Campanha        | Custo (R$) | Cliques | Impressões | Conversões (Compra) | Receita (R$) | ROAS | CPA (R$) |
|-------------------------|------------|---------|------------|---------------------|--------------|------|----------|
| Shopping - Produtos Novos | 6.000      | 18.000  | 500.000    | 300                 | 75.000       | 12.5x| 20,00    |
| Search - Palavras Chave | 4.000      | 12.000  | 300.000    | 200                 | 40.000       | 10x  | 20,00    |
| Display - Retargeting   | 2.500      | 8.000   | 250.000    | 150                 | 20.000       | 8x   | 16,67    |
| Performance Max         | 2.500      | 7.000   | 150.000    | 100                 | 5.000        | 2x   | 25,00    |

---

## Evolução de Receita e Custo por Dia (Série Temporal)

**Gráfico:** Linhas para `Receita Total (GA4)` e `Custo (Google Ads)` por `Data`
*   **Insights:** Identificar dias com melhor ROAS, correlacionar com eventos ou promoções.
*   **Configuração:** Adicionar um eixo Y duplo para comparar métricas com escalas diferentes.

---

## Top Páginas de Destino de Campanha (GA4)

**Gráfico:** Tabela com `Página de destino e tela`, `Visualizações`, `Taxa de Engajamento`, `Receita Total`
*   **Filtro:** Incluir apenas URLs que contenham "utm_campaign=" ou "gclid=".
*   **Insights:** Avaliar a performance pós-clique das páginas para otimização de UX/CRO.
```

### Dashboard de Engajamento e Retenção de Usuários (Looker Studio)

```
# Dashboard de Engajamento e Retenção de Usuários - Google Analytics 4

## Visão Geral do Engajamento - Período: Últimos 30 Dias

| Métrica GA4               | Valor Atual | Delta vs. Período Anterior |
|---------------------------|-------------|----------------------------|
| Sessões Engajadas         | 11.230      | +10.5%                     |