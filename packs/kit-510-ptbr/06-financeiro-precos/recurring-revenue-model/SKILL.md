---
name: recurring-revenue-model
description: "Recurring Revenue Model — Skill especializada para recurring revenue model"
license: MIT
metadata:
  version: 1.0.0
  author: Cafe Code AI
  category: 06-financeiro-precos
  updated: 2026-03-01
risk: critical
---

# Recurring Revenue Model

Esta skill capacita o Claude a modelar, analisar e otimizar estratégias financeiras para negócios baseados em receita recorrente, fornecendo ferramentas para precificação, projeções e métricas de desempenho.

---

## Keywords

SaaS, Assinatura, MRR, ARR, Churn, LTV, CAC, Upsell, Cross-sell, Análise de Cohort, Ciclo de Cobrança, Retenção, Precificação Recorrente, ARPU, Expansão MRR, Contração MRR, Payback CAC.

---

## Quick Start

1.  **Configure a Coleta de Dados de Assinantes:** Implemente um sistema para registrar cada nova assinatura, cancelamento, upgrade e downgrade de forma granular, associando-os a um cliente e data específicos.
2.  **Calcule o MRR Inicial:** Some a receita mensal recorrente de todas as assinaturas ativas no final do mês passado para estabelecer uma base de comparação. Ex: Se em 31/Dez/2023 haviam 500 clientes pagando um total de R$50.000, este é o MRR inicial de Jan/2024.
3.  **Identifique Fontes de MRR:** Separe o MRR em categorias como Novo MRR, Expansão MRR (upsells/cross-sells), Contração MRR (downgrades) e Churn MRR (cancelamentos) para entender o crescimento líquido.
4.  **Monitore a Taxa de Churn:** Calcule o Churn de Clientes e o Churn de Receita (MRR Churn) mensalmente, dividindo o número ou valor perdido pelo total do período anterior para identificar a erosão da base.

---

## Core Workflows

### Workflow 1: Análise e Projeção de MRR/ARR

Este workflow detalha como estruturar a análise e projeção da Receita Mensal Recorrente (MRR) e Receita Anual Recorrente (ARR) para um negócio de software como serviço (SaaS).

**Passos Detalhados:**

1.  **Coleta e Segmentação do MRR:**
    *   **MRR Bruto (Gross MRR):** Total da receita recorrente gerada em um mês.
    *   **Novo MRR:** Receita de novos clientes que assinaram no mês. Ex: 50 novos clientes a R$100/mês = R$5.000.
    *   **Expansão MRR (Expansion MRR):** Receita adicional de clientes existentes via upsells ou cross-sells. Ex: 10 clientes fizeram upgrade de R$100 para R$150/mês, gerando 10 * R$50 = R$500.
    *   **Contração MRR (Contraction MRR):** Redução de receita de clientes existentes via downgrades. Ex: 5 clientes fizeram downgrade de R$150 para R$100/mês, gerando 5 * R$50 = R$250 de contração.
    *   **Churn MRR (Lost MRR):** Receita perdida de clientes que cancelaram. Ex: 20 clientes que pagavam R$100/mês cancelaram, resultando em R$2.000 de Churn MRR.

2.  **Cálculo do MRR Líquido (Net MRR):**
    *   **Fórmula:** `MRR_Líquido = MRR_Inicial + Novo_MRR + Expansão_MRR - Contração_MRR - Churn_MRR`
    *   **Exemplo:** Se MRR Inicial (mês anterior) era R$50.000, com Novo MRR de R$5.000, Expansão MRR de R$500, Contração MRR de R$250 e Churn MRR de R$2.000.
        `MRR_Líquido = 50.000 + 5.000 + 500 - 250 - 2.000 = R$53.250`
    *   Este é o MRR do final do mês atual.

3.  **Projeção de MRR para o Próximo Período:**
    *   **Assuma Taxas:** Utilize taxas históricas de Churn, Expansão e aquisição de novos clientes.
    *   **Exemplo de Projeção (Mês Seguinte):**
        *   MRR Atual: R$53.250
        *   Previsão de Churn MRR (5% do MRR Atual): 0.05 * 53.250 = R$2.662,50
        *   Previsão de Expansão MRR (1% do MRR Atual): 0.01 * 53.250 = R$532,50
        *   Previsão de Novo MRR (baseado em pipeline de vendas): R$6.000
        *   **MRR Projetado:** `53.250 - 2.662,50 + 532,50 + 6.000 = R$57.120`
    *   **ARR (Receita Anual Recorrente):** Simplesmente multiplique o MRR por 12. `ARR = MRR * 12`.
        *   Exemplo: `57.120 * 12 = R$685.440`

4.  **Análise de Cohort:** Agrupe clientes por mês de aquisição para analisar o desempenho de retenção e expansão ao longo do tempo. Uma cohort de Março/2023 com 100 clientes e MRR inicial de R$10.000 pode ser rastreada para ver seu MRR remanescente em Junho/2023 (e.g., R$8.500), revelando a taxa de churn e expansão específica daquele grupo.

### Workflow 2: Análise de Rentabilidade e Crescimento (LTV/CAC)

Este workflow concentra-se na avaliação da viabilidade financeira da aquisição de clientes e seu valor a longo prazo, utilizando as métricas LTV (Lifetime Value) e CAC (Customer Acquisition Cost).

**Passos Detalhados:**

1.  **Cálculo do Custo de Aquisição de Clientes (CAC):**
    *   **Fórmula:** `CAC = (Total de Custos de Vendas e Marketing) / (Número de Novos Clientes Adquiridos)`
    *   **Exemplo:** Em um trimestre, foram gastos R$20.000 em campanhas de marketing e R$10.000 em salários da equipe de vendas, resultando em 100 novos clientes.
        `CAC = (20.000 + 10.000) / 100 = R$300 por cliente`
    *   **Considerações:** Inclua todos os custos diretos e indiretos de aquisição, como ferramentas, publicidade paga, eventos, comissões de vendas.

2.  **Cálculo do Lifetime Value (LTV):**
    *   **Fórmula Simples:** `LTV = (ARPU * Margem Bruta Média) / Churn_Rate`
        *   `ARPU (Average Revenue Per User):` Receita Média por Usuário (MRR Total / Número de Clientes). Ex: R$53.250 / 500 clientes = R$106,50.
        *   `Margem Bruta Média:` (Receita - Custo dos Produtos/Serviços Vendidos) / Receita. Ex: 70%.
        *   `Churn Rate:` Taxa de Churn de Clientes Mensal. Ex: (20 clientes perdidos / 520 clientes iniciais) = 3.85%.
    *   **Exemplo de LTV:** `LTV = (106,50 * 0,70) / 0,0385 = 74,55 / 0,0385 = R$1.936,36`
    *   **Fórmula Alternativa (mais robusta se a taxa de churn for alta ou variável):** `LTV = ARPU * (1 / Churn Rate) * Margem Bruta Média` (Assumindo que 1/Churn Rate é a vida útil média do cliente em meses).

3.  **Análise da Razão LTV:CAC:**
    *   **Fórmula:** `Razão LTV:CAC = LTV / CAC`
    *   **Exemplo:** `1.936,36 / 300 = 6,45`
    *   **Interpretação:** Uma razão de 3:1 ou superior é geralmente considerada saudável para negócios SaaS. Neste caso (6,45:1), o negócio tem um excelente retorno sobre o