---
name: discount-strategy
description: "Discount Strategy — Skill especializada para desenvolver, implementar e otimizar estratégias de desconto para maximizar receita, volume de vendas e lucratividade, mitigando riscos de desvalorização da marca."
license: MIT
metadata:
  version: 1.0.0
  author: Cafe Code AI
  category: 06-financeiro-precos
  updated: 2026-03-01
risk: critical
---

# Discount Strategy

Esta skill capacita o Claude a formular e executar estratégias de desconto eficientes, analisando impacto financeiro, otimizando ofertas e monitorando desempenho para objetivos específicos de negócio.

---

## Keywords

Precificação dinâmica, elasticidade de preço, margem de contribuição, ROI de desconto, break-even de desconto, Lifetime Value (LTV), Custo de Aquisição de Cliente (CAC), promoções sazonais, bundle pricing, frete grátis, descontos progressivos, desconto por volume, canibalização de vendas, desvalorização de marca, markup, mark-down.

---

## Quick Start

1.  **Calcular Margem de Contribuição (MC) Atual**: Para o SKU `PROD-007` com preço de R$120 e CMV de R$45, a MC é R$75.
2.  **Simular Break-Even de Desconto**: Para um desconto de 15% (novo preço R$102, nova MC R$57), calcule o aumento percentual de vendas necessário para manter a MC total (ex: se 100 unidades vendidas, precisa de 131.5 unidades).
3.  **Configurar Ação Promocional no Sistema**: Implementar um cupom `VERAO15OFF` no e-commerce para o `PROD-007` com validade de 15 dias.
4.  **Monitorar Taxas de Conversão e LTV de Clientes Adquiridos**: Acompanhar taxa de uso do cupom, conversão do carrinho e LTV médio dos clientes que usaram o desconto.

---

## Core Workflows

### Workflow 1: Avaliação de Viabilidade de Desconto para Aceleração de Vendas de Software SaaS

Este workflow detalha a análise financeira para implementar um desconto inicial em um plano de software SaaS, visando o aumento rápido da base de usuários sem comprometer a saúde financeira a longo prazo.

**Contexto:** Lançamento do plano "Essencial" do SaaS "GestãoPro", com objetivo de adquirir 500 novos clientes nos primeiros 3 meses.

**Passos Detalhados:**

1.  **Definição dos Parâmetros Financeiros Iniciais:**
    *   **Preço Cheio Mensal (P_cheio)**: R$150/mês
    *   **Custo Variável por Cliente (CV)**: R$30/mês (infraestrutura, suporte básico)
    *   **Margem de Contribuição Base (MC_base)**: P_cheio - CV = R$150 - R$30 = R$120.
    *   **Taxa de Churn Média Esperada (mensal)**: 5% (para calcular LTV)
    *   **Custo de Aquisição de Cliente (CAC_base)**: R$250 (sem desconto)

2.  **Proposta de Desconto:**
    *   **Tipo de Desconto**: 20% OFF nos primeiros 3 meses de assinatura.
    *   **Preço Descontado (P_desc)**: R$150 * (1 - 0.20) = R$120/mês nos primeiros 3 meses.
    *   **Margem de Contribuição com Desconto (MC_desc)**: R$120 - R$30 = R$90/mês nos primeiros 3 meses.

3.  **Análise de Ponto de Equilíbrio (Break-Even do Desconto):**
    *   **Perda de Margem por Unidade Descontada (Mensal)**: MC_base - MC_desc = R$120 - R$90 = R$30.
    *   **Número de Unidades Adicionais Necessárias para Compensar a Perda de Margem de 1 Unidade Descontada**: Perda por Unidade / MC_desc = R$30 / R$90 = 0.33 unidades.
    *   **Cenário de Vendas**: Se a meta é adquirir 500 clientes com desconto nos 3 meses:
        *   Perda total de margem no período de desconto: 500 clientes * R$30/cliente/mês * 3 meses = R$45.000.
        *   Para compensar esta perda com a margem descontada (R$90/mês), seriam necessários: R$45.000 / R$90/mês = 500 unidades-mês adicionais. Isso significa que, para cada cliente que você atraiu com o desconto, o "custo" do desconto requer que você tenha atraído 0.33 clientes *adicionais* que você não teria sem a promoção, *apenas para compensar a perda na margem*.
        *   **Decisão**: O desconto é viável se a campanha for capaz de gerar um volume de vendas que supere esse "custo" de margem.

4.  **Projeção de LTV e CAC com Desconto:**
    *   **LTV de Cliente com Desconto (considerando preço cheio após 3 meses)**:
        *   Primeiros 3 meses: R$120/mês * 3 meses = R$360.
        *   Meses subsequentes (considerando 12 meses de vida útil média): R$150/mês * 9 meses = R$1350.
        *   LTV Total = R$360 + R$1350 = R$1710.
    *   **Estimativa de CAC com Desconto**: A promoção pode reduzir o CAC. Supondo que o CAC caia para R$180.
    *   **LTV/CAC com Desconto**: R$1710 / R$180 = 9.5. (Comparar com LTV/CAC base: (R$150 * 12) / R$250 = 7.2).
    *   **Decisão**: Se o LTV/CAC melhora ou se mantém robusto, o desconto é uma ferramenta eficaz para aquisição.

5.  **Plano de Implementação e Monitoramento:**
    *   **Configuração**: Criar um código de cupom `GESTAOPRO20OFF` no sistema de billing com validade de 90 dias e limite de 500 usos.
    *   **Comunicação**: Anunciar o desconto em landing pages, campanhas de e-mail marketing e anúncios pagos direcionados a leads qualificados.
    *   **Métricas de Acompanhamento**: Taxa de conversão de leads para clientes com o cupom, taxa de churn dos clientes adquiridos via desconto (comparar com base), LTV médio desses clientes.

### Workflow 2: Otimização de Descontos para Queima de Estoque Excedente em E-commerce

Este workflow aborda a estratégia de desconto para liquidar estoque parado, minimizando perdas e liberando capital, considerando os custos de manutenção de estoque.

**Contexto:** E-commerce de eletrônicos, 800 unidades do "Fone Bluetooth X" (modelo 2023) encalhadas. Custo de estoque: R$8/unid/mês.

**Passos Detalhados:**

1.  **Dados do Produto e Custo de Estoque:**
    *   **Preço Cheio (P_cheio)**: R$250
    *   **Custo da Mercadoria Vendida (CMV)**: R$100
    *   **Margem de Contribuição (MC_base)**: R$150
    *   **Estoque Atual**: 800 unidades
    *   **Custo de Manutenção de Estoque**: R$8/unid/mês
    *   **Tempo para Liquidação Ideal**: 45 dias

2.  **Cálculo do Preço Mínimo Aceitável:**
    *   O preço mínimo deve cobrir o CMV e, idealmente, evitar custos futuros de estoque.
    *   Custo de estoque esperado para mais 2 meses (se não vender): 2 meses * R$8/unid = R$16/unid.
    *   **Preço Mínimo de Venda (para evitar perdas maiores)**: CMV + Custo de Estoque Futuro = R$100 + R$16 = R$116.
    *   **Desconto Máximo Aceitável**: (P_cheio - Preço Mínimo) / P_cheio = (R$250 - R$116) / R$250 = R$134 / R$250 = 53.6%.

3.  **Estratégia de Desconto Progressivo:**
    *   **Fase 1 (Semanas 1-2): Desconto Moderado**
        *   **Desconto**: 30% OFF. Preço: R$175. MC: R$75.
        *   **Objetivo**: Vender 40% do estoque (320 unidades).
        *   **Cálculo de MC Esperada**: 320 unidades * R$75/unid = R$24.000.
    *   **Fase 2 (Semanas 3-4): Desconto Agressivo (se necessário)**
        *   **Desconto**: 45% OFF. Preço: R$137.50. MC: R$37.50.
        *   **Objetivo**: Vender 30% do estoque remanescente (240 unidades).
        *   **Cálculo de MC Esperada**: 240 unidades * R$37.50/unid = R$9.000.
    *   **Fase 3 (Última Semana): Desconto Máximo ou Bundle (se ainda houver estoque)**
        *   **Desconto**: 55% OFF. Preço: R$112.50. MC: R$12.50. (Ainda acima do preço mínimo de R$116, considerando um custo de estoque de 2 meses).
        *   **Objetivo**: Vender os 10% restantes (80 unidades).
        *   **Cálculo de MC Esperada**: 80 unidades * R$12.50/unid = R$1.000.
        *   **Alternativa**: Bundle com um produto de alto giro e margem, por exemplo, "Compre Fone X e leve Fone Y com 50% de desconto".

4.  **Cálculo do ROI do Desconto (na perspectiva de evitar perdas de estoque):**
    *   **Receita Total Esperada com Descontos**: (320 * R$175) + (240 * R$137.50) + (80 * R$112.50) = R$56.000 + R$33.000 + R$9.000 = R$98.000.
    *   **CMV Total**: 800 unidades * R$100 = R$80.000.
    *   **Lucro Bruto Ajustado (antes de custos operacionais do desconto)**: R$98.000 - R$80.000 = R$18.000.
    *   **Custo Potencial de Manutenção de Estoque Evitado (Ex: por 3 meses)**: 800 unidades * R$8/unid/mês * 3 meses = R$19.200.
    *   **ROI do Desconto**: O benefício aqui é o *capital liberado* e as *perdas evitadas*. O "lucro" de R$18.000 supera o custo de manter o estoque. O ROI é considerado alto, pois o objetivo principal é liquidar.

5.  **Execução e Monitoramento:**
    *   **Canais**: Campanhas de e-mail marketing segmentadas para clientes interessados em eletrônicos, destaque na home page, anúncios de retargeting para visitantes da página do produto.
    *   **Métricas**: Monitorar volume de vendas diário, estoque remanescente, MC por unidade vendida, e o custo de marketing da campanha em relação à receita gerada.

---

## Templates

### Template de Análise de Impacto de Desconto

```
| SKU/Serviço | Preço Cheio (R$) | CMV (R$) | MC Base (R$) | MC Base (%) | % Desconto | Preço Desc. (R$) | MC Desc. (R$) | MC Desc. (%) | Vendas Atuais (Unid/Mês) | MC Total Atual (R$) | Unid. Adic. para Break-Even (Unid/Mês) | Aumento % Vendas Nec. |
|-------------|------------------|----------|--------------|-------------|------------|------------------|---------------|--------------|--------------------------|---------------------|------------------------------------------|--------------------------|
| SaaS Pro   | 250.00           | 50.00    | 200.00       | 80.00%      | 10%        | 225.00           | 175.00        | 77.78%       | 100                        | 20,000.00           | 14.29                                    | 14.29%                   |
| SaaS Pro   | 250.00           | 50.00    | 200.00       | 80.00%      | 20%        | 200.00           | 150.00        | 75.00%       | 100                        | 20,000.00           | 33.33                                    | 33.33%                   |
| Fone BT X  | 250.00           | 100.00   | 150.00       | 60.00%      | 30%        | 175.00           | 75.00         | 42.86%       | 50                         | 7,500.00            | 50.00                                    | 100.00%                  |
| Camiseta Y | 80.00            | 30.00    | 50.00        | 62.50%      | 15%        | 68.00            | 38.00         | 55.88%       | 200                        | 10,000.00           | 63.16                                    | 31.58%                   |
```
*Fórmulas de referência:*
*   `MC Base (R$)` = `Preço Cheio (R$)` - `CMV (R$)`
*   `MC Base (%)` = (`MC Base (R$)` / `Preço Cheio (R$)`) * 100
*   `Preço Desc. (R$)` = `Preço Cheio (R$)` * (1 - `% Desconto`)
*   `MC Desc. (R$)` = `Preço Desc. (R$)` - `CMV (R$)`
*   `MC Desc. (%)` = (`MC Desc. (R$)` / `Preço Desc. (R$)`) * 100
*   `MC Total Atual (R$)` = `Vendas Atuais (Unid/Mês)` * `MC Base (R$)`
*   `Unid. Adic. para Break-Even (Unid/Mês)` = `Vendas Atuais (Unid/Mês)` * ((`MC Base (R$)` / `MC Desc. (R$)`) - 1)
*   `Aumento % Vendas Nec.` = (`Unid. Adic. para Break-Even (Unid/Mês)` / `Vendas Atuais (Unid/Mês)`) * 100

### Template de Plano de Ação para Campanha de Desconto

```
| ID Campanha | SKU/Serviço Alvo | Objetivo Principal                   | Tipo de Desconto           | % / Valor Desconto | Condições de Aplicação                                 | Período de Ativação | Canal(is) de Divulgação | Métrica de Sucesso (Primária) | Meta Específica            | Responsável | Status      |
|-------------|------------------|--------------------------------------|----------------------------|--------------------|--------------------------------------------------------|---------------------|-------------------------|-------------------------------|----------------------------|-------------|-------------|
| DS-001      | SaaS Essencial   | Acelerar aquisição de novos clientes | % OFF nos primeiros meses  | 20% OFF (3 meses)  | Para os primeiros 500 novos clientes                   | 01/03/2026 - 31/05/2026 | Landing Page, Email Mkt   | Taxa de Conversão             | 15% de conversão de leads  | Marketing   | Em Andamento |
| DS-002      | Fone BT X