---
name: profit-margin-analyzer
description: "Profit Margin Analyzer — Skill especializada para análise e otimização de margens de lucro, precificação estratégica e projeções financeiras."
license: MIT
metadata:
  version: 1.0.0
  author: Cafe Code AI
  category: 06-financeiro-precos
  updated: 2026-03-01
risk: safe
---

# Profit Margin Analyzer

Esta skill capacita o Claude a realizar análises aprofundadas de margens de lucro, identificar otimizações e projetar impactos financeiros com base em dados concretos de receitas e custos.

---

## Keywords

Margem Bruta, Margem Operacional, Margem Líquida, Ponto de Equilíbrio, Markup, Precificação Estratégica, Custo Variável, Custo Fixo, Análise de Rentabilidade, ROI, LTV/CAC, Projeção Financeira.

---

## Quick Start

1.  Coletar dados de Receita Total, Custo dos Produtos Vendidos (CPV) e Despesas Operacionais para o período a ser analisado.
2.  Calcular a Margem Bruta utilizando a fórmula `(Receita Total - CPV) / Receita Total` e expressar em percentual.
3.  Calcular a Margem Operacional subtraindo as Despesas Operacionais da Margem Bruta (em valor absoluto) e dividindo pela Receita Total.
4.  Identificar o Ponto de Equilíbrio em unidades e receita, utilizando Custos Fixos e Margem de Contribuição Unitária.
5.  Simular o impacto de um aumento de 5% no preço de venda ou uma redução de 3% no CPV sobre a Margem Líquida.

---

## Core Workflows

### Workflow 1: Análise Detalhada de Margem Bruta, Operacional e Líquida

Este workflow permite uma avaliação profunda da rentabilidade de uma empresa, desde a venda do produto até o lucro final, identificando os principais componentes que afetam cada nível de margem.

1.  **Reunir Dados Financeiros Brutos**: Solicitar ao usuário os dados de vendas, Custo dos Produtos Vendidos (CPV), despesas operacionais e despesas não operacionais/impostos para um período específico (ex: último trimestre).
    *   **Exemplo Prático**: Para a "Padaria Doce Pão" no 3º Trimestre de 2024:
        *   Receita Bruta de Vendas: R$ 250.000
        *   Devoluções e Abatimentos: R$ 5.000
        *   Custo dos Produtos Vendidos (CPV): R$ 90.000 (farinha, açúcar, ovos, gás)
        *   Despesas Operacionais:
            *   Salários e Encargos (padeiros, atendentes): R$ 60.000
            *   Aluguel: R$ 10.000
            *   Marketing e Publicidade: R$ 5.000
            *   Despesas Administrativas (contabilidade, material de escritório): R$ 3.000
        *   Despesas Financeiras: R$ 2.000
        *   Impostos (IRPJ/CSLL): R$ 8.000

2.  **Calcular Receita Líquida**: Subtrair devoluções e abatimentos da receita bruta.
    *   **Cálculo**: `R$ 250.000 (Receita Bruta) - R$ 5.000 (Devoluções) = R$ 245.000 (Receita Líquida)`.

3.  **Calcular Margem Bruta**: Avalia a lucratividade do negócio após considerar apenas os custos diretos de produção ou aquisição.
    *   **Fórmula**: `Margem Bruta = (Receita Líquida - CPV) / Receita Líquida`
    *   **Cálculo**: `(R$ 245.000 - R$ 90.000) / R$ 245.000 = R$ 155.000 / R$ 245.000 = 0.6326` ou 63.26%.
    *   **Interpretação**: "A Padaria Doce Pão tem uma Margem Bruta de 63.26%, indicando uma boa rentabilidade na venda de seus produtos antes de considerar as despesas operacionais."

4.  **Calcular Margem Operacional**: Mede a eficiência das operações principais da empresa, excluindo custos financeiros e impostos.
    *   **Fórmula**: `Margem Operacional = (Receita Líquida - CPV - Despesas Operacionais) / Receita Líquida`
    *   **Total Despesas Operacionais**: R$ 60.000 + R$ 10.000 + R$ 5.000 + R$ 3.000 = R$ 78.000.
    *   **Cálculo**: `(R$ 245.000 - R$ 90.000 - R$ 78.000) / R$ 245.000 = R$ 77.000 / R$ 245.000 = 0.3143` ou 31.43%.
    *   **Interpretação**: "A Margem Operacional de 31.43% da Padaria Doce Pão é sólida, mostrando que as operações diárias são eficientes na geração de lucro."

5.  **Calcular Margem Líquida**: Representa o lucro real da empresa após todas as despesas, impostos e custos financeiros.
    *   **Fórmula**: `Margem Líquida = (Receita Líquida - CPV - Despesas Operacionais - Despesas Financeiras - Impostos) / Receita Líquida`
    *   **Lucro Líquido**: `R$ 77.000 (Lucro Operacional) - R$ 2.000 (Financ.) - R$ 8.000 (Impostos) = R$ 67.000`.
    *   **Cálculo**: `R$ 67.000 / R$ 245.000 = 0.2735` ou 27.35%.
    *   **Interpretação**: "Com uma Margem Líquida de 27.35%, a Padaria Doce Pão demonstra excelente lucratividade final, indicando boa gestão de todas as categorias de custos."

### Workflow 2: Análise de Ponto de Equilíbrio, Markup e Projeção de Margem para Novos Produtos

Este workflow foca em planejamento e precificação, crucial para lançamentos de produtos ou reavaliação de estratégias.

1.  **Coletar Dados de Custo e Preço para um Produto Específico**: Precisamos do preço de venda unitário, custo variável unitário e custos fixos totais alocáveis ao produto.
    *   **Exemplo Prático**: Para o lançamento do "SmartWatch Fit Pro" pela empresa "TecnoVida":
        *   Preço de Venda Unitário Desejado: R$ 1.200
        *   Custo Variável Unitário (componentes, montagem, comissão de venda): R$ 450
        *   Custos Fixos Mensais Atribuíveis ao Produto (marketing do lançamento, salário do gerente de produto): R$ 150.000

2.  **Calcular Margem de Contribuição Unitária**: Essencial para o cálculo do Ponto de Equilíbrio.
    *   **Fórmula**: `Margem de Contribuição Unitária = Preço de Venda Unitário - Custo Variável Unitário`
    *   **Cálculo**: `R$ 1.200 - R$ 450 = R$ 750`.
    *   **Interpretação**: "Cada SmartWatch Fit Pro vendido contribui com R$ 750 para cobrir os custos fixos da TecnoVida."

3.  **Calcular Ponto de Equilíbrio (PE) em Unidades e Receita**: Determina quantas unidades precisam ser vendidas ou qual receita deve ser gerada para cobrir todos os custos.
    *   **PE em Unidades (Fórmula)**: `Custos Fixos Totais / Margem de Contribuição Unitária`
    *   **Cálculo PE em Unidades**: `R$ 150.000 / R$ 750 = 200 unidades`.
    *   **PE em Receita (Fórmula)**: `Ponto de Equilíbrio (Unidades) * Preço de Venda Unitário`
    *   **Cálculo PE em Receita**: `200 unidades * R$ 1.200 = R$ 240.000`.
    *   **Interpretação**: "A TecnoVida precisa vender 200 unidades do SmartWatch Fit Pro, gerando R$ 240.000 em receita mensal, para cobrir todos os seus custos fixos associados ao produto."

4.  **Análise de Markup e Precificação**: Avaliar a estratégia de preço em relação ao custo.
    *   **Fórmula Markup**: `Markup = (Preço de Venda - Custo) / Custo` (Este é o markup sobre o custo).
    *   **Cálculo Markup (sobre Custo Variável)**: `(R$ 1.200 - R$ 450) / R$ 450 = R$ 750 / R$ 450 = 1.6667` ou 166.67%.
    *   **Fórmula Margem Bruta (sobre Venda)**: `Margem Bruta = (Preço de Venda - Custo) / Preço de Venda`
    *   **Cálculo Margem Bruta**: `(R$ 1.200 - R$ 450) / R$ 1.200 = R$ 750 / R$ 1.200 = 0.625` ou 62.5%.
    *   **Comparação**: "O markup de 166.67% sobre o custo variável e a margem bruta de 62.5% são excelentes para o SmartWatch Fit Pro, posicionando o produto de forma lucrativa e oferecendo espaço para promoções futuras."

5.  **Projeção de Margem e Lucratividade para Diferentes Cenários de Venda**: Simular o impacto de diferentes volumes de venda.
    *   **Cenário Realista (300 unidades/mês)**:
        *   Receita: `300 * R$ 1.200 = R$ 360.000`
        *   Custo Variável Total: `300 * R$ 450 = R$ 135.000`
        *   Lucro Operacional: `R$ 360.000 - R$ 135.000 (CV) - R$ 150.000 (CF) = R$ 75.000`
        *   Margem Operacional: `(R$ 75.000 / R$ 360.000) * 100 = 20.83%`
    *   **Interpretação**: "No cenário realista de 300 unidades vendidas, a TecnoVida projeta um lucro operacional de R$ 75.000 e uma Margem Operacional de 20.83% para o SmartWatch Fit Pro, confirmando a viabilidade do lançamento."

---

## Templates

### Template de Análise de Margem - Mensal

```
### Análise de Margem de Lucro - Loja de Roupas "Estilo Urbano" - Julho/2024

**1. Dados de Receita:**
   - Receita Bruta de Vendas: R$ 150.000
   - Descontos e Devoluções: R$ 5.000
   - **Receita Líquida**: R$ 145.000

**2. Custos dos Produtos Vendidos (CPV):**
   - Custo Direto da Mercadoria (Fornecedores): R$ 60.000
   - Frete de Compra: R$ 2.000
   - Impostos sobre Compra: R$ 1.000
   - **CPV Total**: R$ 63.000

**3. Despesas Operacionais (Fixas e Vari