---
name: payment-gateway-compare
description: "Payment Gateway Compare — Skill especializada para payment gateway compare"
license: MIT
metadata:
  version: 1.0.0
  author: Cafe Code AI
  category: 06-financeiro-precos
  updated: 2026-03-01
---

# Payment Gateway Compare

Esta skill capacita o Claude a realizar análises financeiras aprofundadas e comparações estratégicas entre diferentes gateways de pagamento, otimizando custos e performance.

---

## Keywords

- Taxa de transação
- Adquirência
- Subadquirente
- Gateway de pagamento
- Chargeback
- Conciliação financeira
- Custo de setup
- Custos fixos mensais
- PSD2 (Open Banking)
- PCI DSS
- Liquidação financeira
- Antifraude
- MDR (Merchant Discount Rate)
- Taxa de aprovação

---

## Quick Start

1. Liste os provedores de gateway de pagamento considerados para análise (ex: Stripe, PagSeguro, Pagar.me, Stone).
2. Colete as taxas de transação (débito, crédito à vista, crédito parcelado, Pix) e custos fixos (mensalidade, setup) de cada provedor.
3. Obtenha o volume de transações projetado e o ticket médio por modalidade de pagamento para o período.
4. Insira os dados coletados no "Template de Comparação de Gateways de Pagamento" para um cálculo inicial de custos.
5. Avalie as taxas de aprovação e chargeback históricas ou projetadas para cada solução de pagamento.

---

## Core Workflows

### Workflow 1: Análise de Custo Total de Propriedade (TCO) de Gateways para E-commerce

Este workflow detalha o cálculo do custo total de propriedade (TCO) para diferentes gateways de pagamento, considerando não apenas as taxas percentuais, mas também custos fixos, taxas por transação e o impacto de chargebacks e falsos positivos.

**Passo 1: Coleta e Estruturação de Dados de Custos e Volumes**
*   **Exemplo de Cenário:** Um e-commerce de eletrônicos com faturamento mensal projetado de R$ 300.000,00, distribuído em 2.000 transações com ticket médio de R$ 150,00.
    *   **Distribuição de Pagamentos:** 60% Crédito à Vista, 30% Crédito Parcelado (2x), 10% Débito.
    *   **Provedor A (Ex: Stripe):**
        *   Crédito à Vista: 3.5% + R$ 0,60 por transação
        *   Crédito Parcelado (2x): 4.99% + R$ 0,60 por transação
        *   Débito: 2.0% + R$ 0,50 por transação
        *   Pix: 0.99% (teto R$ 0,99)
        *   Custo Fixo Mensal: R$ 49,00
        *   Custo de Setup: R$ 0,00
        *   Taxa de Antecipação (D+1): 1.5% ao mês
    *   **Provedor B (Ex: PagSeguro):**
        *   Crédito à Vista: 3.19% + R$ 0,40 por transação
        *   Crédito Parcelado (2x): 4.59% + R$ 0,40 por transação
        *   Débito: 1.99% + R$ 0,30 por transação
        *   Pix: 0.99% (teto R$ 0,99)
        *   Custo Fixo Mensal: R$ 0,00
        *   Custo de Setup: R$ 0,00
        *   Taxa de Antecipação (D+1): 2.5% ao mês (já embutida em algumas ofertas, considerar como custo adicional se não)

**Passo 2: Cálculo dos Custos de Transação por Modalidade e Provedor**
*   **Projeção de Transações:**
    *   Crédito à Vista: 2.000 * 0.60 = 1.200 transações
    *   Crédito Parcelado: 2.000 * 0.30 = 600 transações
    *   Débito: 2.000 * 0.10 = 200 transações
*   **Receita Projetada por Modalidade:**
    *   Crédito à Vista: 1.200 * R$ 150 = R$ 180.000
    *   Crédito Parcelado: 600 * R$ 150 = R$ 90.000
    *   Débito: 200 * R$ 150 = R$ 30.000

*   **Custo Mensal Provedor A (Stripe):**
    *   Crédito à Vista: `(R$ 180.000 * 0.035) + (1.200 * R$ 0,60) = R$ 6.300 + R$ 720 = R$ 7.020`
    *   Crédito Parcelado: `(R$ 90.000 * 0.0499) + (600 * R$ 0,60) = R$ 4.491 + R$ 360 = R$ 4.851`
    *   Débito: `(R$ 30.000 * 0.020) + (200 * R$ 0,50) = R$ 600 + R$ 100 = R$ 700`
    *   Custo Fixo Mensal: `R$ 49`
    *   **Custo Total Provedor A:** `R$ 7.020 + R$ 4.851 + R$ 700 + R$ 49 = R$ 12.620`

*   **Custo Mensal Provedor B (PagSeguro):**
    *   Crédito à Vista: `(R$ 180.000 * 0.0319) + (1.200 * R$ 0,40) = R$ 5.742 + R$ 480 = R$ 6.222`
    *   Crédito Parcelado: `(R$ 90.000 * 0.0459) + (600 * R$ 0,40) = R$ 4.131 + R$ 240 = R$ 4.371`
    *   Débito: `(R$ 30.000 * 0.0199) + (200 * R$ 0,30) = R$ 597 + R$ 60 = R$ 657`
    *   Custo Fixo Mensal: `R$ 0`
    *   **Custo Total Provedor B:** `R$ 6.222 + R$ 4.371 + R$ 657 + R$ 0 = R$ 11.250`

**Passo 3: Incorporação de Custos Indiretos (Antifraude, Chargeback, Falsos Positivos)**
*   **Cenário Antifraude:**
    *   **Provedor A:** Taxa de aprovação 93%, Taxa de Chargeback 0.4%, 10 Falsos Positivos/mês.
    *   **Provedor B:** Taxa de aprovação 95%, Taxa de Chargeback 0.2%, 5 Falsos Positivos/mês.
    *   **Custo Médio Chargeback:** R$ 150 (valor transação) + R$ 20 (multa) + R$ 30 (operacional) = R$ 200.

*   **Custo Antifraude Provedor A:**
    *   Chargebacks: `(2.000 transações * 0.004) * R$ 200 = 8 * R$ 200 = R$ 1.600`
    *   Falsos Positivos (Perda de Receita): `10 * R$ 150 (ticket médio) = R$ 1.500`
    *   **Custo Total Antifraude A:** `R$ 1.600 + R$ 1.500 = R$ 3.100`

*   **Custo Antifraude Provedor B:**
    *   Chargebacks: `(2.000 transações * 0.002) * R$ 200 = 4 * R$ 200 = R$ 800`
    *   Falsos Positivos (Perda de Receita): `5 * R$ 150 (ticket médio) = R$ 750`
    *   **Custo Total Antifraude B:** `R$ 800 + R$ 750 = R$ 1.550`

**Passo 4: Cálculo do Custo Total de Propriedade (TCO) Mensal**
*   **TCO Provedor A:** `R$ 12.620 (custo transacional) + R$ 3.100 (custo antifraude) = R$ 15.720`
*   **TCO Provedor B:** `R$ 11.250 (custo transacional) + R$ 1.550 (custo antifraude) = R$ 12.800`

**Conclusão:** No cenário hipotético, o Provedor B apresenta um TCO mensal significativamente menor, mesmo com taxas de transação ligeiramente mais altas em algumas modalidades, devido à sua melhor performance em antifraude e menor número de custos fixos.

### Workflow 2: Otimização de Fluxo de Caixa via Antecipação de Recebíveis

Este workflow compara as opções de antecipação de recebíveis entre gateways, analisando o impacto no fluxo de caixa e o custo efetivo do capital.

**Passo 1: Coleta de Dados de Recebíveis e Taxas de Antecipação**
*   **Cenário:** Empresa com R$ 100.000 em vendas de crédito parcelado (média de 3 parcelas) com liquidação D+30, D+60, D+90. Necessidade de antecipar 50% dos recebíveis para D+2.
*   **Provedor X:**
    *   Taxa de Antecipação D+2: 2.0% ao mês sobre o valor antecipado.
    *   Recebíveis a antecipar: R$ 50.000.
*   **Provedor Y:**
    *   Taxa de Antecipação D+2: 1.8% ao mês sobre o valor antecipado.
    *   Recebíveis a antecipar: R$ 50.000.

**Passo 2: Cálculo do Custo da Antecipação por Provedor**
*   **Provedor X:**
    *   Custo mensal: `R$ 50.000 * 0.020 = R$ 1.000`
    *   Recebível líquido após antecipação: `R$ 50.000 - R$ 1.000 = R$ 49.000`
*   **Provedor Y:**
    *   Custo mensal: `R$ 50.000 * 0.018 = R$ 900`
    *   Recebível líquido após antecipação: `R$ 50.000 - R$ 900 = R$ 49.100`

**Passo 3: Análise do Impacto no Fluxo de Caixa e Custo Efetivo**
*   **Provedor X:** Liberação de R$ 49.000 em D+2, com custo de `R$ 1.000`. Custo efetivo anual: `(R$ 1.000 / R$ 49.000) * 12 * 100% = 24.49% ao ano`.
*   **Provedor Y:** Liberação de R$ 49.100 em D+2, com custo de `R$ 900`. Custo efetivo anual: `(R$ 900 / R$ 49.100) * 12 * 100% = 21.99% ao ano`.

**Passo 4: Considerações Estratégicas**
*   Um custo de antecipação menor (Provedor Y) representa uma economia direta e um capital de giro mais barato.
*   Avaliar a flexibilidade das opções de antecipação (parcial ou total, diferentes prazos) e a facilidade de solicitação via dashboard ou API.
*   Comparar o custo da antecipação com outras fontes de capital de giro (empréstimos bancários, linhas de crédito) para garantir que a antecipação seja a opção mais vantajosa.

---

## Templates

### Template de Comparação de Gateways de Pagamento (Valores Mensais Projetados)

```
# Comparativo de Gateways de Pagamento - Projeção Mensal

**Cenário Base:**
*   Faturamento Mensal Projetado: R$ 300.000,00
*   Número de Transações: 2.000
*   Ticket Médio: R$ 150,00

| Métrica / Gateway | Provedor A (Ex: Stripe) | Provedor B (Ex: PagSeguro) | Provedor C (Ex: Pagar.me) |
|-------------------|--------------------------|----------------------------|---------------------------|
| **Receita Bruta Projetada** | R$ 300.000,00            | R$ 300.000,00              | R$ 300.000,00             |
| **Volume Transações** | 2.000                    | 2.000                      | 2.000                     |
| **Distribuição Transações** |                          |                            |                           |
|   Crédito à Vista (60%) | 1.200 transações         | 1.200 transações           | 1.200 transações          |
|   Crédito Parcelado (30%) | 600 transações           | 600 transações             | 600 transações            |
|   Débito (10%)        | 200 transações           | 200 transações             | 200 transações            |
| **Taxas de Transação** |                          |                            |                           |
|   Crédito à Vista (%) | 3.5% + R$ 0,60/transação | 3.19% + R$ 0,40/transação  | 3.49% + R$ 0,55/transação |
|   Crédito Parcelado (%) | 4.99% + R$ 0,60/transação| 4.59% + R$ 0,40/transação  | 4.89% + R$ 0,55/transação |
|   Débito (%)          | 2.0% + R$ 0,50/transação | 1.99% + R$ 0,30/transação  | 1.89% + R$ 0,45/transação |
|   Pix (%)             | 0.99% (teto R$ 0,99)     | 0.99% (teto R$ 0,99)       | 0.89% (teto R$ 0,89)      |
| **Custos Fixos** |                          |                            |                           |
|   Custo Fixo Mensal (R$) | R$ 49,00                 | R$ 0,00                    | R$ 99,00                  |
|   Custo Setup (R$)    | R$ 0,00                  | R$ 0,00                    | R$ 0,00                   |
| **Custo Transacional Mensal (R$)** | R$ 12.620,00             | R$ 11.250,00               | R$ 12.085,00              |
| **Performance Antifraude** |                          |                            |                           |
|   Taxa de Aprovação (%) | 93%                      | 95%                        | 94%                       |
|   Taxa de Chargeback (%) | 0.4%                     | 0.2%                       | 0.3%                      |
|   Falsos Positivos (unid/mês) | 10                     | 5                          | 7                         |
| **Custo Indireto Antifraude (R$)** | R$ 3.100,00              | R$ 1.550,00                | R$ 2.050,00               |
| **Custo Total de Propriedade (TCO) Mensal (R$)** | **R$ 15.720,00**         | **R$ 12.800,00**           | **R$ 14.135,00**          |
| **TCO % do Faturamento** | 5.24%                    | 4.27%                      | 4.71%                     |
| **Prazos de Liquidação Padrão** | D+30                     | D+14                       | D+2                       |
| **Taxa de Antecipação (D+2) %** | 1.5% ao mês              | 2.5% ao mês                | 1.7% ao mês               |
| **Recursos Adicionais** | Recorrência, Link de Pagamento | Checkout Transparente, Boleto | API Completa, Multibandeira |
```

### Análise de Rentabilidade por Meio de Pagamento (Exemplo)

```
# Análise de Rentabilidade por Meio de Pagamento

**Período:** Mês de Janeiro
**Faturamento Total Bruto:** R$ 100.000,00

| Meio de Pagamento | Volume Transações | Receita Bruta (R$) | Taxa Gateway (%) | Custo Gateway (R$) | Taxa Adquirente (%) | Custo Adquirente (R$) | Custo Total Meio Pagamento (R$) | Lucro Bruto Meio Pagamento (R$) | Margem Bruta (%) |
|-------------------|-------------------|--------------------|------------------|--------------------|---------------------|-----------------------|---------------------------------|---------------------------------|------------------|
| **Crédito à Vista** | 300               | R$ 45.000,00       | 3.2%             | R$ 1.440,00        | 0.0%                | R$ 0,00               | R$ 1.440,00                     | R$ 43.560,00                    | 96.8%            |
| **Crédito 2x**    | 150               | R$ 22.500,00       | 4.8%             | R$ 1.080,0