---
name: unit-economics
description: "Unit Economics — Skill especializada para unit economics"
license: MIT
metadata:
  version: 1.0.0
  author: Cafe Code AI
  category: 06-financeiro-precos
  updated: 2026-03-01
risk: safe
---

# Unit Economics

Esta skill capacita a analisar a lucratividade e viabilidade de cada unidade de negócio ou cliente, otimizando estratégias de precificação e crescimento.

---

## Keywords

LTV, CAC, Margem de Contribuição, Ponto de Equilíbrio, ROI, MRR por cliente, Churn, Payback Unitário, Custo de Venda, ARPU, Precificação, Viabilidade, Rentabilidade, Modelagem Financeira.

---

## Quick Start

1.  Coletar dados de receita e custos diretos por transação ou cliente em uma planilha.
2.  Calcular a Margem de Contribuição de um produto ou serviço específico.
3.  Determinar o LTV (Lifetime Value) e o CAC (Customer Acquisition Cost) médios por segmento de cliente.
4.  Simular cenários de precificação e o impacto direto no Ponto de Equilíbrio.

---

## Core Workflows

### Workflow 1: Análise de Viabilidade de um Novo Produto Digital (SaaS)

Este workflow detalha o processo para avaliar a saúde financeira de um novo produto SaaS, focando nas métricas unitárias essenciais.

*   **Passo 1: Definir a Unidade de Análise.**
    *   Para um produto SaaS, a unidade de análise principal é o "assinante mensal". É fundamental padronizar essa unidade para todos os cálculos.
    *   **Exemplo:** Para o SaaS "AnalyticsPro", a unidade de análise é o "assinante pagante por mês".

*   **Passo 2: Calcular a Receita Média por Unidade (ARPU).**
    *   O ARPU (Average Revenue Per User) é a receita média gerada por cada assinante.
    *   **Fórmula:** ARPU = Receita Total Mensal / Número de Assinantes Ativos.
    *   **Exemplo:** Se o "AnalyticsPro" tem um Plano Básico (R$99/mês) e um Plano Pro (R$199/mês), e 70% dos clientes usam o Básico e 30% o Pro, o ARPU médio seria: (0.70 * R$99) + (0.30 * R$199) = R$69.30 + R$59.70 = **R$129.00**.

*   **Passo 3: Levantar Custos Variáveis Diretos por Unidade.**
    *   Identifique todos os custos que aumentam ou diminuem diretamente com o número de assinantes.
    *   **Exemplo:**
        *   Custo de infraestrutura (cloud) por usuário: R$18.00
        *   Custo de suporte (chat, e-mail) por usuário: R$12.00
        *   Taxas de processamento de pagamento: R$5.00
        *   **Total de Custos Variáveis (CV) por Assinante:** R$18 + R$12 + R$5 = **R$35.00**.

*   **Passo 4: Calcular a Margem de Contribuição (MC) Unitária.**
    *   A MC unitária é a receita por assinante que sobra após cobrir os custos variáveis diretos, e que contribui para os custos fixos e lucro.
    *   **Fórmula:** MC Unitária = ARPU - CV Unitário.
    *   **Exemplo:** MC Unitária = R$129.00 - R$35.00 = **R$94.00**.

*   **Passo 5: Projetar o LTV (Lifetime Value).**
    *   O LTV representa a receita total que um cliente gera para o negócio durante todo o seu relacionamento. Requer a taxa de churn (cancelamento).
    *   **Fórmula:** LTV = (MC Unitária / Taxa de Churn Mensal).
    *   **Exemplo:** Se a taxa de churn mensal projetada é de 2.5%:
        *   Vida útil média do cliente = 1 / 0.025 = 40 meses.
        *   LTV = R$94.00 * 40 = **R$3.760.00**.

*   **Passo 6: Estimar o CAC (Customer Acquisition Cost).**
    *   O CAC é o custo médio para adquirir um novo cliente.
    *   **Fórmula:** CAC = (Total de Investimento em Marketing + Vendas) / Número de Novos Clientes Adquiridos.
    *   **Exemplo:** Em um mês, foram gastos R$10.000 em marketing e R$5.000 em vendas para adquirir 30 novos clientes.
        *   CAC = (R$10.000 + R$5.000) / 30 = R$15.000 / 30 = **R$500.00**.

*   **Passo 7: Avaliar a Relação LTV/CAC.**
    *   Esta métrica é crucial para a sustentabilidade. Uma relação saudável indica que o valor que um cliente gera é significativamente maior do que o custo para adquiri-lo.
    *   **Fórmula:** LTV / CAC.
    *   **Exemplo:** LTV/CAC = R$3.760.00 / R$500.00 = **7.52**. (Um LTV/CAC > 3:1 é geralmente considerado excelente).

*   **Passo 8: Calcular o Payback Period do CAC.**
    *   Tempo necessário para que a margem de contribuição gerada por um cliente cubra o custo de sua aquisição.
    *   **Fórmula:** Payback Period = CAC / MC Unitária Mensal.
    *   **Exemplo:** Payback Period = R$500.00 / R$94.00 = **5.32 meses**. (Idealmente, menos de 12 meses).

*   **Decisão:** Com um LTV/CAC de 7.52 e um payback de 5.32 meses, o produto "AnalyticsPro" demonstra uma excelente viabilidade unitária, indicando que a estratégia de precificação e aquisição de clientes é robusta.

### Workflow 2: Otimização de Precificação para um E-commerce de Produtos Físicos

Este workflow foca em como usar Unit Economics para ajustar a precificação de um produto específico em um e-commerce, visando maximizar a lucratividade.

*   **Passo 1: Selecionar um SKU para Análise Detalhada.**
    *   Escolha um produto representativo ou um que esteja com margem apertada.
    *   **Exemplo:** "Smartwatch Xtreme 2.0".

*   **Passo 2: Coletar Preço de Venda Unitário (PVU).**
    *   Registre o preço atual de venda do produto.
    *   **Exemplo:** PVU atual = **R$450.00**.

*   **Passo 3: Identificar Custos Diretos por Unidade.**
    *   Liste todos os custos que variam diretamente com a venda de uma unidade.
    *   **Exemplo:**
        *   Custo da mercadoria vendida (CMV): R$200.00
        *   Custo de embalagem unitária: R$5.00
        *   Comissão do marketplace (12% sobre o PVU): 0.12 * R$450.00 = R$54.00
        *   Impostos sobre a venda (PIS/COFINS/ICMS - média 10% sobre o PVU): 0.10 * R$450.00 = R$45.00
        *   Custo de frete (proporcional, se a empresa arca com parte): R$15.00
        *   **Total de Custos Variáveis (CV) por Unidade:** R$200 + R$5 + R$54 + R$45 + R$15 = **R$319.00**.

*   **Passo 4: Calcular Margem de Contribuição Unitária (MCU) em Valor e Percentual.**
    *   **Fórmula:** MCU = PVU - CV Unitário.
    *   **Fórmula:** MCU % = (MCU / PVU) * 100.
    *   **Exemplo:**
        *   MCU = R$450.00 - R$319.00 = **R$131.00**.
        *   MCU % = (R$131.00 / R$450.00) * 100 = **29.11%**.

*   **Passo 5: Simular Impacto de Aumento de Preço.**
    *   Teste um aumento de preço e recalcule a MCU.
    *   **Exemplo:** Aumentar o PVU em 8% para R$486.00.
        *   Novos custos variáveis: CMV (R$200) + Embalagem (R$5) + Comissão (0.12 * R$486 = R$58.32) + Impostos (0.10 * R$486 = R$48.60) + Frete (R$15) = R$326.92.
        *   Nova MCU = R$486.00 - R$326.92 = **R$159.08**.
        *   Nova MCU % = (R$159.08 / R$486.00) * 100 = **32.73%**.
        *   Nota: A margem de contribuição em percentual aumentou de 29.11% para 32.73%.

*   **Passo 6: Analisar a Elasticidade da Demanda (Estimativa).**
    *   Estime como a quantidade vendida pode reagir ao novo preço. Utilize dados históricos ou benchmarks da indústria.
    *   **Exemplo:** Se o aumento de 8% no PVU resultar em uma queda de 5% nas vendas (elasticidade -0.625), compare o lucro total.
        *   Cenário Antigo (100 unidades): Faturamento = 100 * R$450 = R$45.000. Lucro de Contribuição = 100 * R$131 = R$13.100.
        *   Cenário Novo (95 unidades): Faturamento = 95 * R$486 = R$46.170. Lucro de Contribuição = 95 * R$159.08 = R$15.112.60.
        *   Mesmo com a queda de vendas, o lucro de contribuição total aumentou em R$2.012.60.

*   **Passo 7: Avaliar o Ponto de Equilíbrio Unitário (em volume).**
    *   Calcule quantas unidades precisam ser vendidas para cobrir os custos fixos.
    *   **Fórmula:** Ponto de Equilíbrio em Volume (PEV) = Custos Fixos Mensais / MCU.
    *   **Exemplo:** Custos Fixos Mensais (aluguel, salários fixos, marketing institucional) = R$20.000.
        *   Com preço antigo: PEV = R$20.000 / R$131.00 = **152.67 unidades**.
        *   Com preço novo: PEV = R$20.000 / R$159.08 = **125.72 unidades**.

*   **Decisão:** O aumento de preço de 8% no Smartwatch Xtreme 2.0 é vantajoso. Ele eleva a Margem de Contribuição unitária, aumenta o lucro de contribuição total mesmo com uma pequena perda de volume, e reduz o número de unidades necessárias para atingir o ponto de equilíbrio, melhorando a saúde financeira geral do produto.

---

## Templates

### Análise de LTV/CAC Mensal - Produto SaaS "GrowthHack"

```
# Análise de LTV/CAC Mensal - Produto SaaS "GrowthHack"

**Período:** Fevereiro/2024

**1. Dados de Receita por Cliente (ARPU)**
*   Receita Total Mensal (MRR): R$ 120.000,00
*   Número de Clientes Ativos: 600
*   ARPU (Average Revenue Per User/Unit): R$ 120.000,00 / 600 = **R$ 200,00**

**2. Dados de Custos Variáveis por Cliente**
*   Custo de Infraestrutura (AWS) por Cliente: R$ 30,00
*   Custo de Suporte Premium por Cliente: R$ 20,00
*   Taxas de Processamento de Pagamento (média): R$ 10,00
*   Total de Custos Variáveis (CV) por Cliente: R$ 30 + R$ 20 + R$ 10 = **R$ 60,00**

**3. Margem de Contribuição (MC) por Cliente**
*   MC por Cliente: ARPU - CV = R$ 200,00 - R$ 60,00 = **R$ 140,00**

**4. Taxa de Churn Mensal**
*   Clientes no Início do Mês: 615
*   Clientes Perdidos no Mês: 12
*   Taxa de Churn: 12 / 615 = **1,95%**

**5. Lifetime Value (LTV)**
*   Vida Útil Média do Cliente (1 / Churn): 1 / 0,0195 = 51,28 meses
*   LTV: MC por Cliente * Vida Útil Média = R$ 140,00 * 51,28 = **R$ 7.179,20**

**6. Customer Acquisition Cost (CAC)**
*   Investimento em Marketing (Mês): R$ 18.000,00 (campanhas digitais, conteúdo)
*   Investimento em Vendas (Mês): R$ 10.000,00 (salários, comissões)
*   Número de Novos Clientes Adquiridos no Mês: 50
*   CAC: (R$ 18.000,00 + R$ 10