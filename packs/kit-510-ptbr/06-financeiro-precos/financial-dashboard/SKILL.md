---
name: financial-dashboard
description: "Financial Dashboard — Skill especializada para financial dashboard"
license: MIT
metadata:
  version: 1.0.0
  author: Cafe Code AI
  category: 06-financeiro-precos
  updated: 2026-03-01
risk: safe
---

# Financial Dashboard

Esta skill capacita o Claude Code a projetar, construir, analisar e otimizar dashboards financeiros complexos, garantindo a tomada de decisões estratégicas baseada em dados concretos de rentabilidade, fluxo de caixa e valor do cliente.

---

## Keywords

Fluxo de Caixa, Margem Bruta, Ponto de Equilíbrio, LTV/CAC, Projeção Financeira, Rentabilidade, ROI, EBITDA, DRE, Balanço Patrimonial, KPI Financeiro, Análise de Sensibilidade.

---

## Quick Start

1.  **Coletar Dados Financeiros Brutos:** Extraia demonstrações contábeis (DRE, Balanço Patrimonial, DFC) dos últimos 12-24 meses do ERP ou sistema contábil, juntamente com dados de vendas do CRM.
2.  **Estruturar Modelagem de Dados:** Importe os dados para uma ferramenta de BI (Power BI, Tableau, Google Data Studio) e crie um modelo de dados relacional, conectando tabelas de receitas, custos, despesas e clientes.
3.  **Calcular Métricas Essenciais:** Desenvolva medidas para Margem Bruta, Margem Líquida, EBITDA, Ponto de Equilíbrio, LTV, CAC e ROI em sua ferramenta de BI, aplicando as fórmulas apropriadas.
4.  **Criar Visualizações Iniciais:** Construa gráficos de linha para tendências de receita e lucro, gráficos de barra para despesas por categoria e cartões de KPI para as métricas mais críticas.
5.  **Configurar Atualização Automática:** Agende a atualização diária ou semanal das fontes de dados para garantir que o dashboard reflita sempre as informações mais recentes.

---

## Core Workflows

### Workflow 1: Construção e Análise de Rentabilidade do Negócio

Este workflow detalha a criação de um segmento do dashboard focado exclusivamente na performance de rentabilidade, permitindo identificar gargalos e oportunidades de otimização.

**Passos Detalhados:**

1.  **Extração e Preparação de Dados da DRE:**
    *   **Ação:** Exporte a Demonstração de Resultado do Exercício (DRE) detalhada dos últimos 24 meses do sistema contábil (e.g., TOTVS, SAP Business One, Conta Azul).
    *   **Exemplo:** Um arquivo `.csv` contendo colunas como `Data`, `Receita Bruta`, `Deduções de Vendas`, `Receita Líquida`, `Custo dos Produtos Vendidos (CPV)`, `Despesas Operacionais (Salários, Aluguel, Marketing)`, `Despesas Financeiras`, `IRPJ/CSLL`.
    *   **Ferramenta:** SQL query diretamente no banco de dados, exportação via interface do ERP ou integração via API.

2.  **Cálculo das Métricas de Rentabilidade:**
    *   **Ação:** No Power BI (ou ferramenta similar), crie as seguintes medidas DAX (Data Analysis Expressions) para calcular as principais métricas de rentabilidade.
    *   **Exemplo de Fórmulas DAX:**
        *   `Margem Bruta = DIVIDE(SUM(DRE[Receita Líquida]) - SUM(DRE[CPV]), SUM(DRE[Receita Líquida]))`
        *   `Margem Líquida = DIVIDE(SUM(DRE[Lucro Líquido]), SUM(DRE[Receita Líquida]))`
        *   `EBITDA = SUM(DRE[Lucro Antes do IR e Contribuição Social]) + SUM(DRE[Despesas Financeiras]) + SUM(DRE[Depreciação e Amortização])`
    *   **Contexto:** Estas fórmulas utilizam as colunas da DRE para calcular os indicadores chave.

3.  **Visualização de Tendências de Rentabilidade:**
    *   **Ação:** Crie gráficos que mostrem a evolução das métricas de rentabilidade ao longo do tempo e sua composição.
    *   **Exemplo:**
        *   **Gráfico de Linha:** Exiba `Margem Bruta` e `Margem Líquida` mensais para os últimos 24 meses. Isso revela se a lucratividade está crescendo, estagnando ou diminuindo.
        *   **Gráfico de Barras Empilhadas:** Mostre a composição das `Despesas Operacionais` (e.g., Marketing, Vendas, Administrativas) por mês, permitindo identificar áreas de maior gasto.
        *   **Cartão KPI:** Exiba o `EBITDA` do último trimestre com uma seta indicando a variação percentual em relação ao trimestre anterior (e.g., "EBITDA T4 2023: R$ 1.2M, +8% vs T3").

4.  **Análise de Desvios e Cenários:**
    *   **Ação:** Compare as métricas atuais com metas orçamentárias e benchmarks do setor, identificando desvios significativos.
    *   **Exemplo:**
        *   Se a `Margem Líquida` projetada para o mês era de 15% e a realizada foi de 12%, investigue quais despesas superaram o orçamento ou se a receita ficou abaixo do esperado.
        *   Utilize filtros no dashboard para analisar a rentabilidade por `Linha de Produto`, `Região Geográfica` ou `Canal de Vendas`, descobrindo qual segmento é mais ou menos lucrativo.
        *   **Impacto:** Um desvio de 3 pontos percentuais na margem pode indicar a necessidade de renegociar preços com fornecedores, otimizar processos de produção ou revisar estratégias de precificação.

### Workflow 2: Otimização de Fluxo de Caixa e Ponto de Equilíbrio

Este workflow foca em garantir a saúde financeira da empresa a curto e médio prazo, otimizando a gestão do dinheiro e identificando o volume de vendas necessário para cobrir os custos.

**Passos Detalhados:**

1.  **Consolidação de Dados de Fluxo de Caixa:**
    *   **Ação:** Reúna dados de todas as entradas (recebimentos de clientes, empréstimos, investimentos) e saídas (pagamentos a fornecedores, salários, despesas operacionais, impostos) de caixa dos últimos 6-12 meses.
    *   **Exemplo:** Planilha com colunas `Data`, `Tipo de Transação (Receita/Despesa)`, `Categoria (Vendas, Salários, Aluguel)`, `Valor`, `Conta Bancária`.
    *   **Ferramenta:** Conciliação bancária, extratos bancários, dados do sistema de contas a pagar/receber.

2.  **Projeção de Fluxo de Caixa Futuro:**
    *   **Ação:** Desenvolva um modelo de projeção que estime as entradas e saídas de caixa para os próximos 3 a 6 meses, considerando variáveis como sazonalidade, prazos de recebimento e pagamento, e planos de investimento.
    *   **Exemplo:**
        *   **Receitas:** Projete com base no histórico de vendas, pipeline de vendas e taxa de conversão (e.g., "70% das vendas de software de R$50k fecham no próximo mês, gerando R$35k em entradas").
        *   **Despesas:** Inclua custos fixos (aluguel R$10k, salários R$40k), custos variáveis (CPV 30% da receita), despesas de marketing (R$5k/mês) e investimentos planejados (compra de equipamento R$20k em Março).
    *   **Formato:** Uma tabela mensal com `Saldo Inicial`, `Recebimentos Totais`, `Pagamentos Totais`, `Saldo Final`.

3.  **Cálculo do Ponto de Equilíbrio (Break-Even Point):**
    *   **Ação:** Utilize os dados de custos fixos e variáveis unitários para calcular o ponto de equilíbrio em unidades e em valor monetário.
    *   **Exemplo de Fórmulas:**
        *   `Custos Fixos Totais = Soma(Aluguel, Salários Fixos, Assinaturas de Software)` (e.g., R$ 50.000)
        *   `Preço de Venda Unitário` (e.g., R$ 250)
        *   `Custo Variável Unitário` (e.g., R$ 100, incluindo matéria-prima e comissão)
        *   `Margem de Contribuição Unitária = Preço de Venda Unitário - Custo Variável Unitário` (R$ 250 - R$ 100 = R$ 150)
        *   `Ponto de Equilíbrio (em Unidades) = Custos Fixos Totais / Margem de Contribuição Unitária` (R$ 50.000 / R$ 150 = 333.33 unidades)
        *   `Ponto de Equilíbrio (em Valor) = Ponto de Equilíbrio (em Unidades) * Preço de Venda Unitário` (333.33 * R$ 250 = R$ 83.332,50)
    *   **Visualização:** Um gráfico de barras que mostra o volume de vendas necessário para atingir o PE, com uma linha indicando as vendas atuais.

4.  **Identificação de Gargalos e Ações Corretivas:**
    *   **Ação:** Analise a projeção de fluxo de caixa para identificar meses com saldo negativo ou baixo, e o ponto de equilíbrio para entender a sustentabilidade operacional.
    *   **Exemplo:**
        *   Se a projeção indica um saldo de caixa negativo de R$20.000 em abril, sugerir:
            *   **Renegociação de Prazos:** Contatar fornecedores para estender prazos de pagamento de 30 para 60 dias para pagamentos de R$15.000.
            *   **Adiantamento de Recebíveis:** Analisar a possibilidade de antecipar R$10.000 em recebíveis de clientes com boa reputação.
            *   **Corte de Despesas:** Suspender temporariamente um investimento de R$5.000 em marketing não essencial.
        *   Se o Ponto de Equilíbrio em unidades (333) está muito próximo ou acima das vendas médias mensais (300), sugerir:
            *   **Aumento de Preço:** Avaliar um aumento de preço de 5% para o produto, se o mercado permitir.
            *   **Redução de Custos Variáveis:** Negociar descontos por volume com fornecedores de matéria-prima para reduzir o Custo Variável Unitário em 10%.
            *   **Redução de Custos Fixos:** Analisar a substituição de um software caro por uma alternativa mais acessível, economizando R$500/mês.

---

## Templates

### Modelo de Planilha de DRE Simplificada (Mensal)

```
| Mês/Ano | Receita Bruta (R$) | Deduções de Vendas (R$) | Receita Líquida (R$) | Custo dos Produtos Vendidos (R$) | Margem Bruta (R$) | Despesas Operacionais (R$) | Despesas Administrativas (R$) | Despesas de Marketing (R$) | Lucro Operacional (R$) | Despesas Financeiras (R$) | Lucro Antes IR/CSLL (R$) | IR e CSLL (R$) | Lucro Líquido (R$) |
|---------|--------------------|--------------------------|----------------------|----------------------------------|-------------------|----------------------------|-------------------------------|-----------------------------|-------------------------|---------------------------|--------------------------|----------------|--------------------|
| JAN/2024| 150.000,00         | 15.000,00                | 135.000,00           | 60.000,00                        | 75.000,00         | 25.000,00                  | 10.000,00                     | 5.000,00                    | 50.000,00               | 2.000,00                  | 48.000,00                | 12.000,00      | 36.000,00          |
| FEV/2024| 160.000,00         | 16.000,00                | 144.000,00           | 64.000,00                        | 80.000,00         | 26.000,00                  | 10.500,00                     | 5.500,00                    | 54.000,00               | 2.200,00                  | 51.800,00                | 12.950,00      | 38.850,00          |
| MAR/2024| 140.000,00         | 14.000,00                | 126.000,00           | 56.000,00                        | 70.000,00         | 24.000,00                  | 9.500,00                      | 4.500,00                    | 46.000,00               | 1.800,00                  | 44.200,00                | 11.050,00      | 33.150,00          |
```

### Cálculo de LTV e CAC (Exemplo de SaaS)

```
| Métrica | Descrição | Valor (Exemplo) | Fórmula (se aplicável) |
|---|---|---|---|
| **LTV (Lifetime Value)** | | | |
| Receita Média Mensal por Cliente (ARPU) | Receita total / Nº de clientes ativos | R$ 250,00 | Receita Recorrente Mensal (MRR) / Nº Clientes |
| Taxa de Churn Mensal | % de clientes que cancelam por mês | 3,00% | (Clientes Perdidos / Clientes Iniciais) * 100 |
| Vida Útil Média do Cliente (Meses) | 1 / Taxa de Churn Mensal | 33,33 meses | 1 / 0,03 |
| LTV Total (R$) | ARPU * Vida Útil Média do Cliente | R$ 8.332,50 | R$ 250 * 33,33 |
| | | | |
| **CAC (Custo de Aquisição de Cliente)** | | | |
| Total de Gastos com Marketing e Vendas | Gastos com campanhas, salários equipe, ferramentas | R$ 30.000,00 | Soma de despesas Mkt/Vendas no período |
| Número de Novos Clientes Adquiridos | Clientes que iniciaram contrato no período | 50 | Contagem de novos contratos |
| CAC Total (R$) | Total de Gastos / Nº Novos Clientes | R$ 600,00 | R$ 30.000 / 50 |
| | | | |
| **LTV/CAC Ratio** | Medida de eficiência do investimento em aquisição | 13,89 | R$ 8.332,50 / R$ 600,00 |
```

---

## Checklist

- [x] Dados da DRE, Balanço Patrimonial e DFC extraídos e atualizados.
- [x] Margem Bruta e Margem Líquida calculadas e visualizadas em gráficos de tendência.
- [x] Ponto de Equilíbrio em unidades e valor monetário calculado e exibido.
- [x] Projeção de Fluxo de Caixa para os próximos 3-6 meses desenvolvida e monitorada.
- [x] Métricas de LTV e CAC calculadas e o LTV/CAC Ratio analisado.
- [x] Dashboards segmentados por linha de produto, região ou canal de vendas para análise granular.
- [x] Alertas automatizados configurados para desvios de orçamento ou queda de métricas chave (e.g., margem abaixo de 10%).
- [x] Análise de sensibilidade para cenários financeiros (otimista, pessimista) aplicada a projeções.
- [x] Segurança e privacidade dos dados financeiros sensíveis garantidas.
- [x] KPIs financeiros principais exibidos em um painel de controle executivo.

---

## Métricas de Referência

| Métrica | Benchmark (Setor de SaaS B2B Pequenas Empresas) | Meta (Exemplo) |
|---|---|---|
| Margem Bruta | 70% - 85% | > 75% |
| Margem Líquida | 15% - 25% | > 20% |
| LTV/CAC Ratio | > 3:1 | > 4:1 |
| Ponto de Equilíbrio (Meses de Venda) | 3 - 6 meses | < 4 meses |
| Ciclo de Conversão de Caixa (DCC) | 30 - 60 dias | < 45 dias |
| ROI (Retorno sobre Investimento) | 15% - 30% | > 20% |

---

## Erros Comuns

1.  **Ignorar a Qualidade dos Dados de Origem**: Muitos dashboards falham porque os dados extraídos do ERP ou CRM estão inconsistentes, incompletos ou incorretos.
    *   **Como evitar**: Implemente rotinas de validação de dados no processo de ETL (Extração, Transformação, Carga). Por exemplo, verifique se todas as receitas têm uma categoria associada, se não há valores negativos em campos que deveriam ser positivos (e.g., custo de venda), e se as datas estão no formato correto. Antes de carregar, execute um script que identifique e reporte registros com valores nulos em campos obrigatórios como `Receita Líquida` ou `CPV`.

2.  **Focar Apenas em Métricas de Vaidade**: Exibir apenas métricas como "Receita Bruta Total" sem contexto ou sem relacioná-las a custos e lucratividade pode levar a decisões enganosas. Uma alta receita não significa necessariamente alta lucratividade.
    *   **Como evitar**: Priorize métricas de rentabilidade (Margem Bruta, Margem Líquida, EBITDA), eficiência (LTV/CAC, Ciclo de Conversão de Caixa) e liquidez. Para cada métrica de receita, sempre inclua sua contraparte de custo ou lucro. Por exemplo, ao lado do gráfico de `Receita Total`, apresente o gráfico de `Lucro Líquido` e um cartão de KPI com a `Margem Líquida` do período.

3.  **Não Segmentar os Dados Adequadamente**: Um dashboard financeiro genérico para toda a empresa dificulta a identificação de problemas específicos. Diferentes produtos, regiões ou canais podem ter performances financeiras muito distintas.
    *   **Como evitar**: Inclua filtros e dimensões de segmentação no dashboard. Permita que o usuário analise a DRE e as métricas de rentabilidade por `Linha de Produto`, `Região Geográfica`, `Canal de Vendas (e-commerce, loja física)` ou `Tipo de Cliente (B2B, B2C)`. Isso permite, por exemplo, descobrir que o "Produto X" é altamente lucrativo, enquanto o "Produto Y" está gerando prejuízo e precisa de revisão de preços ou custos.

---

## Dicas Avançadas

1.  **Implementar Análise de Sensibilidade para Projeções:** Em vez de uma única projeção de fluxo de caixa ou DRE, crie cenários (otimista, base, pessimista) alterando variáveis chave como volume de vendas, preço médio e custo de matéria-prima.
    *   **Exemplo Prático**: No Excel ou Power BI, crie parâmetros de entrada para "Crescimento de Vendas (%)", "Aumento de Preço (%)" e "Redução de Custo (%)". Ao variar esses parâmetros de -10% a +10%, o dashboard deve recalcular e exibir o `Lucro Líquido` projetado e o `Saldo Final de Caixa` para cada cenário, mostrando a robustez ou fragilidade do plano financeiro.

2.  **Utilizar Modelos Preditivos de Machine Learning para Fluxo de Caixa:** Em vez de projeções lineares, treine um modelo de séries temporais (e.g., ARIMA, Prophet) com dados históricos de entradas e saídas de caixa para prever o fluxo de caixa com maior precisão, considerando sazonalidade e tendências não-lineares.
    *   **Exemplo Prático**: Integrar um script Python (via Power BI ou Tableau) que utiliza a biblioteca `Prophet` do Facebook para prever os recebimentos e pagamentos dos próximos 6 meses, baseando-se em 3 anos de histórico de transações. O modelo pode identificar automaticamente picos de recebimento no final do ano e aumento de despesas de marketing em campanhas sazonais.

3.  **Integrar Dados de Mercado e Benchmarking Competitivo:** Não analise as métricas financeiras de forma isolada. Compare o desempenho da empresa com o de concorrentes diretos ou com a média do setor.
    *   **Exemplo Prático**: Adquirir relatórios de mercado (e.g., Statista, IBGE setorial) ou dados de empresas de capital aberto do mesmo setor. No dashboard, adicione um painel que compare a `Margem Bruta` da sua empresa (e.g., 45%) com a média do setor (e.g., 55%), ou o `LTV/CAC Ratio` (e.g., 2.5:1) com o benchmark (e.g., 3.5:1), fornecendo contexto para a performance.

4.  **Desenvolver Dashboards Prescritivos com Recomendações de Ação:** Vá além da simples visualização de dados e use regras de negócio ou algoritmos para sugerir ações específicas com base nos resultados.
    *   **Exemplo Prático**: Se a `Margem Líquida` de um produto cair abaixo de 10% por dois meses consecutivos, o dashboard pode exibir uma "Recomendação: Avaliar aumento de preço em 5% ou negociar redução de 10% no CPV com fornecedor X". Se o `Ponto de Equilíbrio` em unidades exceder as vendas projetadas, sugerir "Aumentar investimento em marketing em R$5.000 ou buscar redução de custos fixos de R$2.000".

5.  **Utilizar Análise de Cohort para LTV e Churn:** Em vez de um LTV médio global, analise o LTV e a taxa de churn por coortes de clientes (grupos de clientes que foram adquiridos no mesmo período). Isso revela padrões de retenção e valor ao longo do tempo.
    *   **Exemplo Prático**: Crie um gráfico de coorte que mostre a `Receita Média por Cliente` para clientes adquiridos em Janeiro/2023, Fevereiro/2023, etc., ao longo dos meses subsequentes. Isso pode revelar que clientes adquiridos em campanhas específicas (e.g., "Black Friday") têm um LTV mais baixo ou churn mais rápido, indicando que a estratégia de aquisição para esses grupos precisa ser revisada.