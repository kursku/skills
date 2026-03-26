---
name: financial-projection
description: "Financial Projection — Skill especializada para financial projection"
license: MIT
metadata:
  version: 1.0.0
  author: Cafe Code AI
  category: 06-financeiro-precos
  updated: 2026-03-01
risk: safe
---

# Financial Projection

Esta skill capacita o Claude a desenvolver e analisar projeções financeiras detalhadas para empresas, cobrindo DRE, fluxo de caixa, ponto de equilíbrio e métricas de valuation.

---

## Keywords

Projeção de receita, custo variável, custo fixo, DRE projetada, fluxo de caixa projetado, ponto de equilíbrio, margem de contribuição, LTV (Lifetime Value), CAC (Customer Acquisition Cost), ROI (Return on Investment), EBITDA, capital de giro, análise de sensibilidade, balanço projetado, valuation.

---

## Quick Start

1.  **Consolidar Dados Históricos (3 anos)**: Colete receitas, custos, despesas e investimentos dos últimos 36 meses, organizando-os por categoria.
2.  **Definir Premissas de Crescimento**: Estabeleça taxas de crescimento de vendas (ex: 8% a.a.), inflação (ex: 4% a.a.), reajustes de preços (ex: 5% a.a.) e custos (ex: 3% a.a.).
3.  **Projetar Vendas e Custos Diretos**: Utilize as premissas para estimar unidades vendidas e preço médio de venda, calculando o custo variável total associado para os próximos 3-5 anos.
4.  **Estimar Custos Fixos e Despesas Operacionais**: Projete aluguéis, salários, despesas administrativas e de marketing, aplicando reajustes anuais conforme premissas específicas.
5.  **Consolidar DRE e Fluxo de Caixa Projetados**: Organize todas as projeções em um formato de DRE e, subsequentemente, em um fluxo de caixa direto para visualizar a geração de caixa operacional, de investimento e de financiamento.

---

## Core Workflows

### Workflow 1: Projeção de Fluxo de Caixa Direto Detalhado

Este workflow permite construir uma projeção de fluxo de caixa direto, essencial para entender a liquidez e a necessidade de capital de giro da empresa em diferentes cenários.

**Passos Detalhados:**

1.  **Coleta e Preparação de Dados Históricos (12-24 meses)**:
    *   **Receita Bruta**: Média mensal R$ 150.000. Sazonalidade: Pico de 20% em Dezembro, Vale de -10% em Janeiro.
    *   **Impostos sobre Vendas (Simples Nacional)**: 6% da Receita Bruta.
    *   **Custo da Mercadoria Vendida (CMV)**: 45% da Receita Bruta.
    *   **Despesas Operacionais Fixas**: Aluguel R$ 5.000, Salários R$ 30.000, Despesas Administrativas R$ 8.000, Marketing Fixo R$ 2.000.
    *   **Despesas Variáveis por Venda**: Comissões 3% da Receita Bruta.
    *   **Contas a Receber (Prazo Médio)**: 30 dias.
    *   **Contas a Pagar (Prazo Médio)**: 45 dias.
    *   **Investimentos Passados**: Compra de equipamento de R$ 50.000 em Jan/Ano 0 com depreciação de R$ 1.000/mês.
    *   **Saldo de Caixa Inicial**: R$ 20.000.

2.  **Definição de Premissas para os Próximos 12 Meses (Ano 1)**:
    *   **Crescimento da Receita**: 10% anual, aplicado linearmente mensalmente (aproximadamente 0,8% ao mês sobre a base anterior).
    *   **Reajuste de Preços**: 5% em Julho/Ano 1.
    *   **Reajuste de Custos Fixos (Aluguel, Salários)**: 5% em Jan/Ano 1.
    *   **Novo Investimento**: Aquisição de nova máquina de R$ 30.000 em Abril/Ano 1, pago à vista.
    *   **Depreciação Nova Máquina**: R$ 500/mês a partir de Abril/Ano 1.
    *   **Pagamento de Empréstimo**: R$ 2.000/mês a partir de Mar/Ano 1.

3.  **Projeção de Entradas de Caixa**:
    *   **Receita Líquida de Vendas**: (Receita Bruta Projetada * (1 - % Impostos)).
    *   **Recebimentos de Vendas**: Ajustar a Receita Líquida pelo prazo médio de contas a receber. Ex: A receita de Janeiro/Ano 1 será recebida em Fevereiro/Ano 1.
    *   **Outras Entradas**: Investimentos de sócios, empréstimos, etc. (Ex: Empréstimo de R$10.000 em Jun/Ano 1).

    *Exemplo de Cálculo de Recebimento (Julho/Ano 1, supondo Receita Bruta Jun/Ano 1 = R$165.000):*
    *   *Receita Bruta Projetada Jun/Ano 1: R$ 165.000*
    *   *Impostos sobre vendas (6%): R$ 9.900*
    *   *Receita Líquida Jun/Ano 1: R$ 155.100*
    *   *Recebimento em Julho/Ano 1 (referente a Junho/Ano 1): R$ 155.100*

4.  **Projeção de Saídas de Caixa**:
    *   **CMV Pago**: (CMV Projetado ajustado pelo prazo médio de contas a pagar). Ex: CMV de Janeiro/Ano 1 será pago em Março/Ano 1.
    *   **Despesas Operacionais Fixas Pagas**: Aluguel, Salários, Adm, Marketing (aplicar reajustes).
    *   **Despesas Variáveis Pagas**: Comissões.
    *   **Impostos Pagos**: Impostos sobre vendas.
    *   **Investimentos**: Compra da nova máquina (R$ 30.000 em Abril/Ano 1).
    *   **Pagamento de Empréstimos/Financiamentos**: (R$ 2.000/mês a partir de Mar/Ano 1).

    *Exemplo de Cálculo de CMV Pago (Abril/Ano 1, supondo CMV Fev/Ano 1 = R$75.000):*
    *   *CMV Projetado Fev/Ano 1: R$ 75.000*
    *   *Pagamento em Abril/Ano 1 (referente a Fev/Ano 1): R$ 75.000*

5.  **Cálculo do Fluxo de Caixa Líquido Mensal e Saldo Final**:
    *   `Fluxo de Caixa Líquido = Total Entradas - Total Saídas`
    *   `Saldo Final do Mês = Saldo Inicial do Mês + Fluxo de Caixa Líquido do Mês`
    *   O Saldo Final de um mês se torna o Saldo Inicial do mês seguinte.

    *Exemplo (Saldo Inicial Jan/Ano 1 = R$20.000):*
    *   *Entradas Jan/Ano 1: R$ 145.000 (Recebimentos de Dez/Ano 0)*
    *   *Saídas Jan/Ano 1: R$ 130.000 (Pagamento CMV Nov/Ano 0 + Despesas Fixas + Impostos Dez/Ano 0)*
    *   *Fluxo de Caixa Líquido Jan/Ano 1: R$ 15.000*
    *   *Saldo Final Jan/Ano 1: R$ 20.000 + R$ 15.000 = R$ 35.000*

### Workflow 2: Análise de Ponto de Equilíbrio e Margem de Segurança

Este workflow determina o volume de vendas necessário para cobrir todos os custos e despesas, e a margem de segurança da empresa.

**Passos Detalhados:**

1.  **Identificar e Consolidar Custos Fixos (Mensais)**:
    *   Agrupe todas as despesas que não variam diretamente com o volume de vendas.
    *   *Exemplo:*
        *   Aluguel: R$ 5.000
        *   Salários Fixos (Administrativo, Gerência): R$ 30.000
        *   Despesas Administrativas (Contabilidade, Softwares): R$ 8.000
        *   Marketing Fixo: R$ 2.000
        *   Depreciação: R$ 1.500
        *   **Total de Custos Fixos (CF): R$ 46.500**

2.  **Identificar e Calcular Custos Variáveis por Unidade/Percentual da Receita**:
    *   **Produto/Serviço Principal**: Venda de "Serviço Consultoria SaaS" por R$ 500/mês/cliente.
    *   **Custo Variável Unitário (CVU)**: Custos diretos associados a cada cliente (licenças de software de terceiros, suporte dedicado, comissão de vendas).
    *   *Exemplo:*
        *   Licença Software Terceiro: R$ 80/cliente
        *   Comissão de Vendas: R$ 50/cliente (10% do preço de venda)
        *   Suporte Direto (alocado): R$ 20/cliente
        *   **Total CVU: R$ 150/cliente**

3.  **Calcular a Margem de Contribuição Unitária (MCU)**:
    *   `MCU = Preço de Venda Unitário - Custo Variável Unitário`
    *   *Exemplo:*
        *   Preço de Venda Unitário: R$ 500
        *   CVU: R$ 150
        *   **MCU: R$ 350/cliente**

4.  **Calcular o Ponto de Equilíbrio em Unidades (PEU)**:
    *   `PEU = Custos Fixos Totais / Margem de Contribuição Unitária`
    *   *Exemplo:*
        *   CF: R$ 46.500
        *   MCU: R$ 350
        *   **PEU = R$ 46.500 / R$ 350 = 132,86 clientes/mês (arredondar para 133 clientes)**
    *   Isso significa que a empresa precisa adquirir e manter 133 clientes por mês apenas para cobrir seus custos fixos e variáveis.

5.  **Calcular o Ponto de Equilíbrio em Receita (PER)**:
    *   `PER = Ponto de Equilíbrio em Unidades * Preço de Venda Unitário`
    *   OU `PER = Custos Fixos Totais / (% Margem de Contribuição)`
    *   *% Margem de Contribuição = (MCU / Preço de Venda Unitário)*
    *   *Exemplo:*
        *   PEU: 133 clientes
        *   Preço de Venda Unitário: R$ 500
        *   **PER = 133 * R$ 500 = R$ 66.500/mês**
        *   *(Alternativa: %MC = R$350/R$500 = 70%. PER = R$46.500 / 0,70 = R$66.428,57)*

6.  **Calcular a Margem de Segurança (MS)**:
    *   A Margem de Segurança indica o quanto as vendas podem cair antes que a empresa comece a ter prejuízo.
    *   `MS (Receita) = (Receita de Vendas Atual - Ponto de Equilíbrio em Receita)`
    *   `MS (%) = (MS (Receita) / Receita de Vendas Atual) * 100`
    *   *Exemplo (Supondo Receita de Vendas Atual = R$ 100.000/mês, o que equivale a 200 clientes):*
        *   MS (Receita) = R$ 100.000 - R$ 66.500 = R$ 33.500
        *   **MS (%) = (R$ 33.500 / R$ 100.000) * 100 = 33,5%**
    *   A empresa pode ter uma queda de até 33,5% nas vendas antes de atingir o ponto de equilíbrio.

7.  **Análise de Cenários**:
    *   Simular o impacto de um aumento de 10% nos Custos Fixos (ex: novo funcionário) ou uma redução de 5% no Preço de Venda.
    *   *Ex: Se CF subir para R$ 51.150 (+10%), o novo PEU seria R$ 51.150 / R$ 350 = 146,14 clientes (147 clientes).*

---

## Templates

### Template de Projeção de DRE Simplificada (Anual)

```
Projeção de Demonstrativo de Resultado do Exercício (DRE) - Anual
Empresa: Consultoria Inovadora Ltda.
Período: 2024-2026 (Valores em R$)

| Item                      | 2023 (Real) | 2024 (Projetado) | 2025 (Projetado) | 2026 (Projetado) |
|---------------------------|-------------|------------------|------------------|------------------|
| **1. Receita Bruta de Vendas**| 1.800.000   | 2.070.000        | 2.380.500        | 2.737.575        |
| (-) Deduções de Vendas    | 108.000     | 124.200          | 142.830          | 164.255          |
| **= Receita Líquida de Vendas**| **1.692.000** | **1.945.800**    | **2.237.670**    | **2.573.320**    |
| (-) Custo da Mercadoria Vendida (CMV)| 761.400     | 875.610          | 1.006.951        | 1.158.094        |
| **= Lucro Bruto**         | **930.600** | **1.070.190**    | **1.230.719**    | **1.415.226**    |
| (-) Despesas Operacionais |             |                  |                  |                  |
|   Despesas com Vendas     | 180.000     | 207.000          | 238.050          | 273.758          |
|   Despesas Administrativas| 120.000     | 138.000          | 158.700          | 182.505          |
|   Despesas de Marketing   | 60.000      | 70.000           | 80.000           | 90.000           |
|   Depreciação             | 18.000      | 18.000           | 18.000           | 18.000           |
| **= Lucro Operacional (EBIT)**| **552.600** | **637.190**      | **735.969**      | **850.963**      |
| (-) Despesas Financeiras Líquidas | 15.000      | 18.000           | 20.000           | 22.000           |
| **= Lucro Antes do IR e CSLL**| **537.600** | **619.190**      | **715.969**      | **828.963**      |
| (-) Imposto de Renda e CSLL (25%)| 134.400     | 154.798          | 178.992          | 207.241          |
| **= Lucro Líquido**       | **403.200** | **464.392**      | **536.977**      | **621.722**      |

Premissas:
- Crescimento anual da Receita Bruta: 15%
- Deduções de Vendas: 6% da Receita Bruta
- CMV: 45% da Receita Líquida
- Despesas com Vendas: 10% da Receita Bruta
- Despesas Administrativas: 7% da Receita Bruta
- Despesas de Marketing: Variável conforme estratégia, com aumento anual
- Depreciação: Fixa em R$18.000/ano (ativo existente)
- Despesas Financeiras: Estimativa crescente

```

### Template de Projeção de Fluxo de Caixa (Mensal, 3 meses)

```
Projeção de Fluxo de Caixa Direto - Mensal
Empresa: Padaria Doce Sabor Ltda.
Período: Jan - Mar 2025 (Valores em R$)

| Item                      | Saldo Inicial (Dez/24) | Jan/25 (Projetado) | Fev/25 (Projetado) | Mar/25 (Projetado) |
|---------------------------|------------------------|--------------------|--------------------|--------------------|
| **SALDO INICIAL**         | **5.000**              | **5.000**          | **10.200**         | **16.400**         |
|                           |                        |                    |                    |                    |
| **ENTRADAS DE CAIXA**     |                        |                    |                    |                    |
| Receita de Vendas à Vista |                        | 30.000             | 31.500             | 33.075             |
| Recebimento Cartão Crédito (D+30) |                | 15.000             | 15.750             | 16.538             |
| Outras Receitas           |                        | 500                | 500                | 500                |
| **TOTAL ENTRADAS**        |                        | **45.500**         | **47.750**         | **50.113**         |
|                           |                        |                    |                    |                    |
| **SAÍDAS DE CAIXA**       |                        |                    |                    |                    |
| Pagamento Fornecedores (D+30) |                    | 18.000             | 18.900             | 19.845             |
| Salários                  |                        | 10.000             | 10.000             | 10.000             |
| Aluguel                   |                        | 2.000              | 2.000              | 2.000              |
| Despesas de Energia/Água  |                        | 1.200              | 1.250              | 1.300              |
| Despesas de Manutenção    |                        | 800                | 800                | 800                |
| Marketing                 |                        | 500                | 500                | 500                |
| Impostos (Simples Nacional) |                      | 2.000              | 2.100              | 2.205              |
| Investimentos (Ex: Forno novo em Mar) |            | 0                  | 0                  | 15.000             |
| Pagamento de Empréstimos  |                        | 800                | 800                | 800                |
| **TOTAL SAÍDAS**          |                        | **35.300**         | **36.350**         | **52.450**         |
|                           |                        |                    |                    |                    |
| **FLUXO DE CAIXA LÍQUIDO**|                        | **10.200**         | **11.400**         | **-2.338**         |
| **SALDO FINAL**           | **5.000**              | **15.200**         | **26.600**         | **24.262**         |

Premissas:
- Vendas à vista: 60% da Receita Bruta
- Cartão de Crédito (Recebimento D+30): 40% da Receita Bruta
- Crescimento mensal das vendas: 5%
- Pagamento Fornecedores (CMV): 60% da Receita Bruta, pago D+30
- Salários, Aluguel, Marketing, Empréstimos: Fixos
- Energia/Água: Aumento de 4% ao mês
- Impostos: 4% da Receita Bruta, pago D+30
- Investimento em Mar/25: Aquisição de forno de R$15.000
```

---

## Checklist

- [x] Dados históricos de receitas, custos e despesas consolidados (mínimo 24 meses)?
- [x] Premissas de crescimento de receita, custos e despesas definidas e justificadas? (Ex: % inflação, % crescimento mercado, reajustes salariais)
- [x] Projeção de custos variáveis por unidade ou como percentual da receita líquida detalhada?
- [x] Custos fixos operacionais e administrativos mensais/anuais discriminados?
- [x] Depreciação e amortização de ativos fixos consideradas na DRE projetada?
- [x] Impostos sobre vendas, lucro (IRPJ, CSLL) e outras contribuições calculados corretamente?
- [x] Prazo médio de recebimento de vendas e pagamento de fornecedores integrado ao fluxo de caixa?
- [x] Projeção de investimentos em ativos e desinvestimentos (venda de ativos) incluída?
- [x] Necessidade de capital de giro (Working Capital) analisada e projetada?
- [x] Ponto de equilíbrio financeiro e econômico calculados e interpretados?
- [x] Análise de sensibilidade para as premissas mais críticas realizada (ex: variação de preço, volume, custo)?
- [x] Elaboração de cenários (otimista, realista, pessimista) para as projeções?

---

## Métricas de Referência

| Métrica                 | Benchmark (Exemplo Varejo/Serviços) | Meta (Empresa em Crescimento) |
|-------------------------|-------------------------------------|-------------------------------|
| Margem Bruta            | 30% - 50%                           | > 45%                         |
| Margem EBITDA           | 10% - 25%                           | > 20%                         |
| Ponto de Equilíbrio (PE) | < 60% da Receita Projetada          | < 50%                         |
| LTV / CAC               | > 3:1                               | > 4:1                         |
| ROI (Projetado)         | > 15% a.a.                          | > 25% a.a.                    |
| Payback (Projetado)     | < 36 meses                          | < 24 meses                    |

---

## Erros Comuns

1.  **Projeção Linear de Vendas sem Fatorar Sazonalidade ou Saturação**: Acreditar que as vendas crescerão em uma linha reta sem considerar os meses de baixo desempenho ou o limite de mercado.
    *   **Como evitar**: Analisar dados históricos de sazonalidade (ex: vendas de sorvetes no inverno), realizar pesquisa de mercado para identificar o tamanho real do mercado e a capacidade de expansão, e aplicar taxas de crescimento decrescentes em horizontes mais longos.
    *   *Exemplo*: Em vez de projetar um crescimento constante de 5% ao mês, ajustar para 2% em Janeiro, 3% em Fevereiro, 7% em Março e um pico de 10% em Novembro e Dezembro, com uma taxa de crescimento geral anual de 8%.
2.  **Subestimar Custos Variáveis e Despesas Operacionais**: Não considerar aumentos de preços de fornecedores, custos de manutenção imprevistos ou a necessidade de contratar mais pessoal com o aumento da demanda.
    *   **Como evitar**: Revisar contratos com fornecedores, incluir uma margem de segurança para despesas variáveis (ex: 5-10% de folga), e detalhar custos de mão de obra por função e volume de produção.
    *   *Exemplo*: Projetar o custo da matéria-prima com base nos preços atuais, mas adicionar uma premissa de aumento de 5% anual devido à inflação e negociações com fornecedores.
3.  **Ignorar a Necessidade de Capital de Giro**: Focar apenas na DRE e no lucro, esquecendo que há um descasamento entre recebimentos e pagamentos que exige recursos para financiar a operação.
    *   **Como evitar**: Construir um fluxo de caixa direto detalhado que considere os prazos médios de recebimento e pagamento. Calcular a necessidade de capital de giro (Ativo Circulante Operacional - Passivo Circulante Operacional).
    *   *Exemplo*: Uma empresa projeta R$ 100.000 de vendas mensais, mas recebe em 30 dias e paga fornecedores em 15 dias. Isso gera uma necessidade constante de caixa para cobrir o CMV antes de receber pelas vendas. Se o CMV for R$ 60.0