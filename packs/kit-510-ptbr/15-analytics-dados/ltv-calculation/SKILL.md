---
name: ltv-calculation
description: "Ltv Calculation — Skill especializada para ltv calculation"
license: MIT
metadata:
  version: 1.0.0
  author: Cafe Code AI
  category: 15-analytics-dados
  updated: 2026-03-01
risk: safe
---

# Ltv Calculation

Esta skill capacita o Claude a calcular, analisar e otimizar o Lifetime Value (LTV) de clientes, integrando dados do Google Analytics 4 (GA4) para decisões estratégicas baseadas em dados.

---

## Keywords

*   LTV Cálculo
*   Lifetime Value
*   GA4 LTV
*   Custo de Aquisição de Cliente (CAC)
*   Receita Média por Usuário (ARPU)
*   Churn Rate
*   Cohort Analysis
*   Monetização Cliente
*   Atribuição de LTV
*   CLTV
*   Engajamento Cliente

---

## Quick Start

1.  Verifique a configuração de eventos de e-commerce (ex: `purchase`, `add_to_cart`) no GA4 para garantir a coleta correta de `value` e `currency`.
2.  Ative a exportação de dados do GA4 para o BigQuery, garantindo que os eventos de usuário e compra estejam acessíveis para análise detalhada.
3.  Execute uma query SQL no BigQuery para calcular o LTV histórico médio por coorte de aquisição, somando a receita de cada usuário ao longo do tempo.
4.  Crie um dashboard no Looker Studio (ou Power BI/Tableau) conectando-o ao BigQuery para visualizar o LTV por canal, coorte e segmento de cliente.

---

## Core Workflows

### Workflow 1: Cálculo e Análise de LTV Histórico com GA4 e BigQuery

Este workflow detalha o processo de extração e cálculo do Lifetime Value (LTV) de clientes usando dados brutos do Google Analytics 4 (GA4) exportados para o BigQuery, permitindo uma análise profunda por coortes.

**Passo 1: Validação da Coleta de Dados de E-commerce no GA4**
Antes de qualquer cálculo de LTV, é crucial que os eventos de e-commerce no GA4 estejam configurados corretamente. O evento `purchase` deve ser implementado com os parâmetros `value` (valor total da transação) e `currency` (moeda da transação).

*   **Verificação no GA4 DebugView:** Realize uma compra de teste e monitore o DebugView no GA4 para confirmar que o evento `purchase` está sendo disparado com os parâmetros `value` (ex: `125.50`) e `currency` (ex: `BRL`).
*   **Exemplo de GTM para GA4:**
    ```javascript
    // Exemplo de Data Layer para evento de compra
    window.dataLayer = window.dataLayer || [];
    dataLayer.push({
      event: "purchase",
      ecommerce: {
        transaction_id: "T_12345",
        value: 125.50,
        currency: "BRL",
        tax: 10.00,
        shipping: 5.00,
        items: [
          {
            item_id: "SKU_45678",
            item_name: "Camiseta Premium",
            price: 70.00,
            quantity: 1
          },
          {
            item_id: "SKU_90123",
            item_name: "Calça Jeans",
            price: 55.50,
            quantity: 1
          }
        ]
      }
    });
    ```
    Garanta que a tag de evento GA4 no GTM mapeie corretamente `ecommerce.value` para o parâmetro `value` do evento `purchase`.

**Passo 2: Exportação e Acesso aos Dados do GA4 no BigQuery**
Acesse o Google Cloud Console e configure o link entre sua propriedade GA4 e o BigQuery. Isso garantirá que os dados de eventos brutos sejam exportados diariamente para uma tabela no BigQuery (`seu_projeto.seu_dataset.events_YYYYMMDD`).

*   **Verificação:** Após 24-48 horas da configuração, verifique a existência de tabelas `events_YYYYMMDD` no seu dataset do BigQuery.
*   **Estrutura de Tabela:** Familiarize-se com a estrutura da tabela, em particular as colunas `user_pseudo_id` (identificador único do usuário), `event_timestamp` (carimbo de data/hora do evento) e `event_params` (array de parâmetros do evento, onde `value` e `currency` são armazenados).

**Passo 3: Cálculo do LTV Histórico por Coorte no BigQuery**
Utilize uma query SQL para identificar a primeira compra de cada usuário (definindo a coorte de aquisição) e, em seguida, somar todas as compras subsequentes feitas por esses usuários para calcular o LTV.

*   **Definição de Coorte:** A coorte será definida pelo mês da primeira compra de cada `user_pseudo_id`.
*   **Fórmula:** LTV de um cliente é a soma de todas as receitas geradas por ele ao longo de sua vida útil como cliente. Para um grupo (coorte), o LTV médio é `(Receita Total da Coorte) / (Número de Clientes na Coorte)`.

**Passo 4: Visualização do LTV em Dashboards no Looker Studio**
Conecte o Looker Studio (ou outra ferramenta de BI) à sua tabela de LTV calculada no BigQuery.

*   **Gráfico de Linhas de LTV Cumulativo por Coorte:** Mostre a evolução do LTV médio de cada coorte ao longo do tempo (ex: LTV_30d, LTV_60d, LTV_90d). Isso revela o valor que os clientes de cada coorte geram nos primeiros meses.
*   **Tabela de LTV por Mês de Aquisição:** Apresente o LTV médio de cada coorte, permitindo comparar a performance de aquisição ao longo do tempo.

### Workflow 2: Atribuição de LTV e Otimização de Campanhas de Marketing

Este workflow foca em como usar o LTV para entender a real contribuição de cada canal de marketing e otimizar o investimento em aquisição de clientes.

**Passo 1: Seleção do Modelo de Atribuição no GA4**
No GA4, o modelo de atribuição padrão é "Baseado em Dados" (Data-Driven Attribution - DDA). Este modelo usa machine learning para distribuir o crédito de uma conversão entre os diferentes pontos de contato ao longo da jornada do cliente.

*   **Acesso:** Navegue para **Administrador > Configurações de Atribuição** no GA4. Confirme que o modelo "Baseado em Dados" está selecionado e a "Janela de Lookback" para eventos de conversão está configurada (ex: 90 dias para aquisição).
*   **Consideração:** Embora o DDA seja robusto, para análises específicas de LTV, pode ser útil comparar com modelos como "Primeiro Clique" ou "Último Clique" para entender a contribuição inicial versus a final.

**Passo 2: Segmentação de Usuários por Canal de Aquisição no GA4**
Para analisar o LTV por canal, você precisa identificar o canal que trouxe o usuário pela primeira vez. O GA4 oferece dimensões como `Primeiro grupo de canais padrão do usuário` (`first_user_default_channel_group`).

*   **Relatórios GA4:** Utilize os relatórios de "Aquisição de Usuários" no GA4. Aplique filtros para analisar o LTV médio de usuários provenientes de "Busca Orgânica", "Busca Paga", "Direto", "Mídia Social", etc.
*   **Criação de Segmentos:** Crie segmentos personalizados no GA4, por exemplo, "Usuários Adquiridos via Google Ads" usando a condição `Primeiro grupo de canais padrão do usuário` `exatamente corresponde` `Paid Search`.

**Passo 3: Análise do LTV por Canal de Aquisição**
Exporte os dados segmentados do GA4 (ou use o BigQuery) para calcular o LTV médio para cada canal de aquisição.

*   **Comparativo de LTV:**
    *   **LTV Médio Google Ads (Search):** R$ 550,00
    *   **LTV Médio Orgânico:** R$ 800,00
    *   **LTV Médio Social Pago:** R$ 320,00
    *   **LTV Médio Email Marketing:** R$ 680,00
*   **Insight:** Clientes adquiridos via busca orgânica mostram um LTV 45% maior que os de busca paga, e 150% maior que os de social pago. Isso indica que, embora a busca paga traga volume, a orgânica atrai clientes de maior valor a longo prazo.

**Passo 4: Otimização de Campanhas com Foco em LTV**
Use os insights do LTV por canal para realocar orçamentos e otimizar estratégias de marketing.

*   **Alocação de Orçamento:** Reduza o investimento em canais com LTV baixo (ex: Social Pago) e aumente em canais com LTV alto (ex: Orgânico, Email Marketing, ou segmentos específicos de Google Ads com LTV comprovado).
*   **Otimização de Lances em Google Ads:** Em vez de otimizar apenas para CPA (Custo por Aquisição) ou ROAS (Retorno sobre Gasto com Anúncios) imediato, ajuste os lances considerando o LTV esperado do cliente. Se o LTV de clientes de uma campanha específica de Google Ads é R$ 1.200 e o CPA é R$ 200, é um canal lucrativo a longo prazo, mesmo que o ROAS imediato seja menor que outra campanha com LTV de R$ 400 e CPA de R$ 50.
*   **Exemplo Prático:** Uma campanha de Google Ads para "Comprar tênis de corrida" tem um LTV médio de R$ 450,00. Uma campanha para "Comprar tênis casual" tem LTV de R$ 300,00. Priorize a otimização e o investimento na campanha de "tênis de corrida".

---

## Templates

### Query SQL para LTV Histórico por Coorte (BigQuery GA4)

```sql
WITH UserFirstPurchase AS (
  -- Identifica a data da primeira compra para cada usuário
  SELECT
    user_pseudo_id,
    MIN(PARSE_DATE('%Y%m%d', event_date)) AS first_purchase_date
  FROM
    `seu_projeto.seu_dataset.events_*` -- Substitua pelo seu projeto e dataset
  WHERE
    event_name = 'purchase'
    AND (SELECT ep.value.double_value FROM UNNEST(event_params) AS ep WHERE ep.key = 'value') IS NOT NULL -- Garante que o valor da compra existe
  GROUP BY
    user_pseudo_id
),
UserPurchases AS (
  -- Agrega todas as compras por usuário com seus respectivos valores
  SELECT
    t1.user_pseudo_id,
    PARSE_DATE('%Y%m%d', t1.event_date) AS purchase_date,
    (SELECT ep.value.double_value FROM UNNEST(t1.event_params) AS ep WHERE ep.key = 'value') AS purchase_value
  FROM
    `seu_projeto.seu_dataset.events_*` AS t1 -- Substitua pelo seu projeto e dataset
  WHERE
    t1.event_name = 'purchase'
    AND (SELECT ep.value.double_value FROM UNNEST(t1.event_params) AS ep WHERE ep.key = 'value') IS NOT NULL
)
SELECT
  FORMAT_DATE('%Y-%m', ufp.first_purchase_date) AS acquisition_month, -- Mês de aquisição do cliente (primeira compra)
  COUNT(DISTINCT ufp.user_pseudo_id) AS total_users_acquired, -- Número total de clientes na coorte
  SUM(up.purchase_value) AS total_revenue_from_cohort, -- Receita total gerada por essa coorte
  SUM(up.purchase_value) / COUNT(DISTINCT ufp.user_pseudo_id) AS average_ltv_per_user_in_cohort -- LTV médio por cliente na coorte
FROM
  UserFirstPurchase AS ufp
JOIN
  UserPurchases AS up
  ON ufp.user_pseudo_id = up.user_pseudo_id
WHERE
  up.purchase_date >= ufp.first_purchase_date -- Considera apenas compras feitas após a primeira compra
GROUP BY
  acquisition_month
ORDER BY
  acquisition_month;
```

### Estrutura de Relatório LTV no Looker Studio

```
Título: Dashboard de Lifetime Value (LTV) - E-commerce Exemplo
Fonte de Dados: BigQuery (GA4 Export - Tabela de LTV Calculada)

Página 1: Visão Geral do LTV
  - Cartão de Pontuação: LTV Médio Geral (Ex: R$ 650,00 - calculado pela média de 'average_ltv_per_user_in_cohort' do período)
  - Gráfico de Linhas: LTV Cumulativo por Coorte (Mês de Aquisição)
    - Dimensão: Mês de Aquisição ('acquisition_month')
    - Métrica: LTV Médio (Cumulative) - Crie um campo calculado para somar o LTV médio ao longo dos meses.
    - Exemplo de dados:
      - Jan/2023: LTV_30d R$180, LTV_60d R$250, LTV_90d R$310
      - Fev/2023: LTV_30d R$200, LTV_60d R$280, LTV_90d R$350
  - Tabela: LTV por Mês de Aquisição e Período (30, 60, 90, 180 dias)
    - Colunas: Mês de Aquisição, Total Clientes, LTV_30d, LTV_60d, LTV_90d, LTV_180d (necessita cálculo prévio no BigQuery ou campos calculados no Looker Studio)
    - Exemplo de dados:
      | Mês Aquisição | Total Clientes | LTV_30d | LTV_60d | LTV_90d | LTV_180d |
      |---------------|----------------|---------|---------|---------|----------|
      | 2023-01       | 1200           | R$180   | R$250   | R$310   | R$420    |
      | 2023-02       | 1500           | R$200   | R$280   | R$350   | R$480    |
  - Gráfico de Barras: Top 5 Canais de Aquisição por LTV
    - Dimensão: Canal de Aquisição (GA4 First user default channel group, com LTV médio agregado)
    - Métrica: LTV Médio
    - Exemplo de dados: Orgânico (R$800), Email (R$680), Paid Search (R$550), Referral (R$400), Social Pago (R$320)

Página 2: LTV por Segmento
  - Filtro: Categoria de Produto Mais Comprada (Ex: Roupas, Eletrônicos, Livros)
  - Tabela: LTV por Gênero e Idade (se dados demográficos disponíveis e relevantes no GA4/CRM)
  - Gráfico de Pizza: Distribuição do LTV por Status de Cliente (Ex: Novo Cliente vs. Cliente Recorrente)
  - Gráfico de Barras: Comparativo LTV entre Campanhas Específicas de Google Ads
    - Dimensão: Nome da Campanha (ou ID da Campanha)
    - Métrica: LTV Médio
```

---

## Checklist

- [x] Confirmar que o link GA4-BigQuery está ativo e exportando dados diários de eventos para `seu_projeto.seu_dataset.events_YYYYMMDD`.
- [x] Validar a coleta de eventos `purchase` com os parâmetros `value` e `currency` no GA4 (via DebugView ou relatórios de eventos).
- [x] Implementar uma lógica de coorte para agrupar usuários pela data de sua primeira compra ou interação mais significativa no BigQuery.
- [x] Calcular o LTV histórico usando a soma cumulativa da receita líquida por usuário ao longo do tempo (considerando devoluções/cancelamentos).
- [x] Segmentar usuários por `first_user_default_channel_group` ou `first_user_source/medium` para analisar o LTV por canal de aquisição.
- [x] Desenvolver um dashboard interativo no Looker Studio (ou ferramenta de BI similar) para monitorar o LTV por coorte, canal e outros segmentos.
- [x] Analisar a relação entre Custo de Aquisição de Cliente (CAC) e LTV por canal para identificar oportunidades de otimização de investimento.
- [x] Considerar a aplicação de modelos de LTV preditivo (ex: BG/NBD, Gamma-Gamma) para estimar o valor futuro dos clientes.
- [x] Criar alertas automatizados para quedas significativas no LTV médio de coortes recentes, indicando possíveis problemas de qualidade de aquisição ou retenção.
- [x] Testar diferentes estratégias de retenção de clientes (ex: programas de fidelidade, automação de e-mail) e medir seu impacto direto no LTV.

---

## Métricas de Referência

| Métrica                 | Benchmark (e-commerce médio) | Meta (e-commerce de alto crescimento) |
|-------------------------|------------------------------|---------------------------------------|
| LTV Médio (12 meses)    | R$ 300 - R$ 800              | R$ 900+                               |
| Relação LTV:CAC         | 3:1                          | 4:1+                                  |
| Ticket Médio (AOV)      | R$ 150 - R$ 250              | R$ 300+                               |
| Taxa de Recompra (6 meses) | 20% - 35%                    | 40%+                                  |
| Churn Rate Mensal       | 3% - 7%                      | 1% - 2%                               |
| LTV por Canal (Paid Search) | R$ 400 - R$ 700              | R$ 800+                               |

---

## Erros Comuns

1.  **Não considerar devoluções/cancelamentos no cálculo do LTV**: O LTV deve refletir a receita *líquida*. Muitos calculam o LTV somando todas as compras sem subtrair os valores de itens devolvidos ou pedidos cancelados.
    *   **Como evitar**: Ao extrair dados do GA4 via BigQuery, inclua a lógica para identificar e subtrair o valor de eventos de `refund` ou ajustar o valor do `purchase` se a API de Measurement Protocol for usada para registrar devoluções. Certifique-se de que o `value` no evento `purchase` já seja líquido ou que as devoluções sejam tratadas como eventos separados com valores negativos.

2.  **Usar apenas LTV histórico para decisões prospectivas**: O LTV histórico é uma métrica retrospectiva. Para otimizar lances de anúncios, prever rentabilidade de novos clientes ou alocar orçamento de marketing de forma eficiente, o LTV preditivo é mais adequado.
    *   **Como evitar**: Complemente a análise de LTV histórico com um modelo de LTV preditivo (CLTV - Customer Lifetime Value). Isso pode ser feito com algoritmos de Machine Learning (ex: BG/NBD para previsão de compras e Gamma-Gamma para previsão de valor) ou modelos estatísticos mais simples baseados em dados de coortes anteriores.

3.  **Ignorar a segmentação detalhada do LTV**: Um LTV médio geral pode mascarar diferenças significativas entre segmentos de clientes, canais de aquisição ou categorias de produtos.
    *   **Como evitar**: Sempre segmente o LTV por dimensões críticas como `first_user_default_channel_group`, tipo de produto da primeira compra, dados demográficos, comportamento de engajamento, etc. Exemplo: um LTV geral de R$ 500 pode esconder um LTV de R$ 1.200 para clientes de busca orgânica e R$ 250 para clientes de social pago, exigindo estratégias de investimento muito diferentes.

4.  **Não vincular o LTV ao Custo de Aquisição de Cliente (CAC)**: Calcular o LTV isoladamente é menos acionável. A relação LTV:CAC é fundamental para avaliar a sustentabilidade e a lucratividade das estratégias de aquisição.
    *   **Como evitar**: Sempre calcule o CAC por canal e compare-o com o LTV do mesmo canal. Uma relação LTV:CAC de 3:1 ou