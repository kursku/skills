---
name: annual-budget
description: "Annual Budget — Skill especializada para a criação, gestão e análise de orçamentos anuais, focada em projeções financeiras, controle de despesas e otimização de resultados."
license: MIT
metadata:
  version: 1.0.0
  author: Cafe Code AI
  category: 06-financeiro-precos
  updated: 2026-03-01
risk: safe
---

# Annual Budget

Esta skill capacita o Claude a planejar, executar e monitorar orçamentos anuais, garantindo alocação eficiente de recursos e atingimento de metas financeiras através de análise aprofundada e controle rigoroso.

---

## Keywords

Projeção de Receita, Orçamento de Despesas, Análise de Variância, Ponto de Equilíbrio, Margem de Lucro, Custo Fixo, Custo Variável, ROI Projetado, Fluxo de Caixa Projetado, Centro de Custo, Revisão Orçamentária, Forecast Contínuo.

---

## Quick Start

1.  **Coletar Dados Históricos Financeiros:** Reúna os demonstrativos de resultado (DRE), balanços e fluxos de caixa dos últimos três a cinco anos.
2.  **Estabelecer Premissas Macroeconômicas:** Defina taxas de inflação, câmbio, crescimento do PIB e taxas de juros projetadas para o período orçamentário.
3.  **Projetar Receita Detalhada:** Estime as vendas de cada produto/serviço, considerando volume, preço médio, sazonalidade e planos de marketing.
4.  **Orçar Despesas Operacionais:** Levante custos variáveis por unidade e detalhe todas as despesas fixas (salários, aluguel, marketing, TI) mês a mês.
5.  **Consolidar DRE Projetado:** Compile todas as projeções em um DRE futuro, calculando Margem Bruta, EBITDA e Lucro Líquido esperados para aprovação.

---

## Core Workflows

### Workflow 1: Elaboração do Orçamento Operacional Detalhado

Este workflow descreve o processo passo a passo para construir um orçamento operacional anual robusto, focando em detalhamento e realismo das projeções.

*   **Passo 1: Projeção de Receita por Linha de Produto/Serviço**
    *   **Ação:** Analisar dados históricos de vendas (unidades e preço médio) dos últimos 3 anos, tendências de mercado, planos de marketing e lançamentos de novos produtos para o ano seguinte.
    *   **Exemplo Concreto:** Para o produto "Software de Gestão PYMES", as vendas históricas foram de 1.200 licenças a R$ 350,00/licença no ano anterior. Com o lançamento da versão 3.0 e uma campanha de marketing digital intensiva, projeta-se um aumento de 18% no volume de licenças e um ajuste de 7% no preço médio devido a novas funcionalidades.
        *   **Cálculo:**
            *   Volume Projetado: 1.200 * (1 + 0,18) = 1.416 licenças
            *   Preço Médio Projetado: R$ 350,00 * (1 + 0,07) = R$ 374,50
            *   Receita Bruta Projetada para PYMES: 1.416 licenças * R$ 374,50/licença = R$ 529.992,00

*   **Passo 2: Estimativa de Custos Variáveis**
    *   **Ação:** Calcular o custo direto por unidade vendida para cada produto/serviço, incluindo custos de aquisição, licenciamento de terceiros, embalagem, frete, etc.
    *   **Exemplo Concreto:** O custo de licenciamento de módulos de terceiros para o "Software de Gestão PYMES" é de R$ 80,00/licença. O custo de distribuição digital e suporte de primeiro nível é de R$ 15,00/licença.
        *   **Cálculo:**
            *   Custo Variável Total por Licença: R$ 80,00 + R$ 15,00 = R$ 95,00/licença
            *   Projeção Total de Custo Variável para PYMES: 1.416 licenças * R$ 95,00/licença = R$ 134.520,00

*   **Passo 3: Orçamento de Despesas Fixas (Operacionais e Administrativas)**
    *   **Ação:** Levantar todas as despesas que não variam diretamente com o volume de vendas, detalhando-as por centro de custo e mês. Incluir salários, aluguéis, marketing institucional, TI, consultorias, etc.
    *   **Exemplo Concreto:**
        *   Aluguel do escritório central: R$ 12.000,00/mês (Total Anual: R$ 144.000,00).
        *   Salários da equipe administrativa (5 pessoas): R$ 25.000,00/mês. Encargos sociais (FGTS, INSS, 13º, férias) estimados em 75% sobre o salário base.
            *   **Cálculo:** Custo total com salários + encargos: R$ 25.000,00 * (1 + 0,75) = R$ 43.750,00/mês (Total Anual: R$ 525.000,00).
        *   Investimento em Marketing Institucional e Branding: R$ 8.000,00/mês (Total Anual: R$ 96.000,00).
        *   Licenças de software interno (ERP, CRM): R$ 3.000,00/mês (Total Anual: R$ 36.000,00).

*   **Passo 4: Consolidação e Elaboração do DRE Projetado**
    *   **Ação:** Somar todas as projeções de receita e custos/despesas para construir o Demonstrativo de Resultado do Exercício (DRE) projetado completo.
    *   **Fórmulas Reais:**
        *   **Receita Líquida:** Receita Bruta - Deduções de Vendas (impostos, devoluções)
        *   **Lucro Bruto:** Receita Líquida - Custos Variáveis (Custos dos Produtos Vendidos)
        *   **Margem Bruta (%):** (Lucro Bruto / Receita Líquida) * 100
        *   **EBITDA:** Lucro Bruto - Despesas Operacionais Fixas (Marketing, Administrativas, Vendas, etc.) + Depreciação + Amortização
        *   **Lucro Líquido:** EBITDA - Despesas Financeiras - Impostos sobre o Lucro

### Workflow 2: Análise de Variância Orçamentária Mensal

Este workflow detalha como monitorar o desempenho financeiro em relação ao orçamento, identificar desvios e tomar ações corretivas.

*   **Passo 1: Coleta de Dados Financeiros Reais do Mês**
    *   **Ação:** Obter os dados financeiros reais (receita, custos, despesas) do mês encerrado diretamente do sistema contábil ou ERP da empresa.
    *   **Exemplo Concreto:** Para o mês de Outubro, a receita real apurada para o "Software de Gestão PYMES" foi R$ 495.000,00, e as despesas reais com Marketing Institucional foram R$ 9.200,00.

*   **Passo 2: Comparação Orçado vs. Real**
    *   **Ação:** Confrontar cada linha de receita e despesa do orçamento mensal aprovado com o resultado real apurado no Passo 1.
    *   **Exemplo Concreto:**
        *   Receita "Software PYMES" orçada para Outubro: R$ 510.000,00. Real: R$ 495.000,00.
        *   Despesas Marketing Institucional orçadas para Outubro: R$ 8.000,00. Real: R$ 9.200,00.

*   **Passo 3: Cálculo da Variância**
    *   **Ação:** Determinar a diferença absoluta e percentual entre o valor orçado e o valor real para cada item.
    *   **Fórmulas Reais:**
        *   **Variância Absoluta:** Real - Orçado
        *   **Variância Percentual:** ((Real - Orçado) / Orçado) * 100
    *   **Exemplo Concreto:**
        *   **Receita "Software PYMES":**
            *   Variância Absoluta: R$ 495.000,00 - R$ 510.000,00 = -R$ 15.000,00
            *   Variância Percentual: (-R$ 15.000,00 / R$ 510.000,00) * 100 = -2,94% (Desvio negativo)
        *   **Despesas Marketing Institucional:**
            *   Variância Absoluta: R$ 9.200,00 - R$ 8.000,00 = +R$ 1.200,00
            *   Variância Percentual: (+R$ 1.200,00 / R$ 8.000,00) * 100 = +15,00% (Desvio positivo)

*   **Passo 4: Análise das Causas e Ações Corretivas**
    *   **Ação:** Investigar os motivos das variâncias significativas (geralmente acima de +/- 5-10%) e propor planos de ação para corrigir o curso ou ajustar as expectativas.
    *   **Exemplo Concreto:**
        *   **Receita "Software PYMES" (-2,94%):** Desvio negativo foi aceitável, mas investigou-se que um parceiro de vendas teve um mês abaixo do esperado. Ação: Realizar reunião de alinhamento com o parceiro para otimizar estratégias de vendas para o próximo mês.
        *   **Despesas Marketing Institucional (+15,00%):** Desvio positivo significativo. A causa foi um investimento extra em anúncios para um evento setorial de última hora, não previsto no orçamento. Ação: Avaliar o ROI do evento. Se positivo, considerar a inclusão de um fundo de contingência para marketing em futuros orçamentos ou ajustar o budget de marketing para os meses restantes para compensar.

---

## Templates

### Template de Projeção de Receita Anual Detalhada

```
# Projeção de Receita Anual - TECH SOLUTIONS LTDA - Ano Fiscal 2025

| Produto/Serviço         | Vendas 2024 (Unidades) | Preço Médio 2024 (R$) | Previsão Cresc. Volume (%) | Previsão Cresc. Preço (%) | Vendas 2025 (Unidades Projetadas) | Preço Médio 2025 (R$ Projetado) | Receita Bruta 2025 (R$ Projetada) |
|-------------------------|------------------------|-----------------------|----------------------------|---------------------------|-----------------------------------|-----------------------------------|-----------------------------------|
| Software Gestão PYMES   | 1.200                  | 350,00                | 18%                        | 7%                        | 1.416                             | 374,50                            | 529.992,00                        |
| Software Gestão Médias  | 800                    | 600,00                | 15%                        | 5%                        | 920                               | 630,00                            | 579.600,00                        |
| Licenças Adicionais     | 300                    | 100,00                | 25%                        | 10%                       | 375                               | 110,00                            | 41.250,00                         |
| Serviços de Suporte     | 600 (horas)            | 180,00                | 10%                        | 8%                        | 660 (horas)                       | 194,40                            | 128.200,00                        |
| **TOTAL RECEITA BRUTA** |                        |                       |                            |                           |                                   |                                   | **1.279.042,00**                  |
```

### Template de Orçamento de Despesas Operacionais (Anual)

```
# Orçamento de Despesas Operacionais - TECH SOLUTIONS LTDA - Ano Fiscal 2025

| Categoria de Despesa   | Jan (R$) | Fev (R$) | Mar (R$) | Abr (R$) | Mai (R$) | Jun (R$) | Jul (R$) | Ago (R$) | Set (R$) | Out (R$) | Nov (R$) | Dez (R$) | Total Anual (R$) |
|------------------------|----------|----------|----------|----------|----------|----------|----------|----------|----------|----------|----------|----------|------------------|
| Salários e Encargos    | 43.750   | 43.750   | 43.750   | 43.750   | 43.750   | 43.750   | 43.750   | 43.750   | 43.750   | 43.750   | 43.750   | 43.750   | 525.000          |
| Aluguel                | 12.000   | 12.000   | 12.000   | 12.000   | 12.000   | 12.000   | 12.000   | 12.000   | 12.000   | 12.000   | 12.000   | 12.000   | 144.000          |
| Marketing Digital      | 8.000    | 8.500    | 9.000    | 8.200    |