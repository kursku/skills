---
name: affiliate-commission-calc
description: "Affiliate Commission Calc — Skill especializada para affiliate commission calc"
license: MIT
metadata:
  version: 1.0.0
  author: Cafe Code AI
  category: 06-financeiro-precos
  updated: 2026-03-01
risk: safe
---

# Affiliate Commission Calc

Esta skill capacita o Claude a calcular, projetar e otimizar comissões de afiliados, modelando diversos cenários de remuneração e performance.

---

## Keywords

Cálculo de comissão, Marketing de afiliados, Estruturas de comissão, Modelagem de pagamentos, Otimização de ganhos, Análise de performance de afiliado, ROI de afiliado, Taxa de conversão de afiliado, CPA de afiliado, CPL de afiliado, EPC, LTV de afiliado.

---

## Quick Start

1.  **Defina o Modelo de Comissão**: Escolha entre percentual sobre venda, valor fixo por venda, CPL (Custo Por Lead) ou CPA (Custo Por Aquisição).
2.  **Informe os Dados Base**: Forneça o valor unitário do produto/serviço (ex: R$ 299,00) ou o custo por lead/ação (ex: R$ 15,00 por lead).
3.  **Especifique a Taxa/Valor da Comissão**: Indique o percentual (ex: 12%) ou o valor fixo (ex: R$ 50,00) da comissão por unidade/ação.
4.  **Simule o Volume**: Apresente o volume esperado de vendas, leads ou ações (ex: 150 vendas, 300 leads) para obter o cálculo total da comissão.

---

## Core Workflows

### Workflow 1: Cálculo e Projeção de Comissão Percentual e Escalonada por Vendas

Este workflow detalha como calcular comissões baseadas em um percentual sobre o valor da venda, incluindo cenários escalonados que recompensam maiores volumes.

**Passos Detalhados:**

1.  **Coleta de Dados da Oferta**:
    *   **Produto**: Curso Online "Marketing Digital Essencial"
    *   **Preço de Venda Unitário**: R$ 497,00
    *   **Taxa de Comissão Base**: 15% sobre o valor da venda líquida (após impostos e taxas da plataforma, se aplicável, mas para simplificação, usaremos o preço cheio).
    *   **Estrutura de Comissão Escalonada (Opcional)**:
        *   0-50 vendas/mês: 15%
        *   51-100 vendas/mês: 18%
        *   Acima de 100 vendas/mês: 20%

2.  **Cálculo da Comissão Base por Unidade**:
    *   Comissão por Unidade = Preço de Venda Unitário * Taxa de Comissão Base
    *   Exemplo: R$ 497,00 * 0.15 = R$ 74,55 por venda

3.  **Projeção de Ganhos para Diferentes Volumes (Sem Escalabilidade)**:
    *   **Cenário 1 (Baixo Volume)**: 30 vendas/mês
        *   Comissão Total = 30 * R$ 74,55 = R$ 2.236,50
    *   **Cenário 2 (Volume Médio)**: 75 vendas/mês
        *   Comissão Total = 75 * R$ 74,55 = R$ 5.591,25
    *   **Cenário 3 (Alto Volume)**: 120 vendas/mês
        *   Comissão Total = 120 * R$ 74,55 = R$ 8.946,00

4.  **Cálculo de Ganhos com Estrutura Escalonada**:
    *   **Cenário de 75 vendas/mês**:
        *   Primeiras 50 vendas: 50 * (R$ 497,00 * 0.15) = 50 * R$ 74,55 = R$ 3.727,50
        *   Próximas 25 vendas (75-50): 25 * (R$ 497,00 * 0.18) = 25 * R$ 89,46 = R$ 2.236,50
        *   Comissão Total = R$ 3.727,50 + R$ 2.236,50 = R$ 5.964,00
    *   **Cenário de 120 vendas/mês**:
        *   Primeiras 50 vendas: 50 * (R$ 497,00 * 0.15) = R$ 3.727,50
        *   Próximas 50 vendas (100-50): 50 * (R$ 497,00 * 0.18) = R$ 4.473,00
        *   Vendas restantes (120-100): 20 * (R$ 497,00 * 0.20) = R$ 1.988,00
        *   Comissão Total = R$ 3.727,50 + R$ 4.473,00 + R$ 1.988,00 = R$ 10.188,50

### Workflow 2: Análise de Custo por Ação (CPA) e Projeção de ROI para Afiliados

Este workflow foca em modelos de comissão baseados em ações específicas (leads, cadastros, testes gratuitos) e a importância de analisar o retorno sobre o investimento do anunciante.

**Passos Detalhados:**

1.  **Definição do Modelo de CPA/CPL**:
    *   **Oferta**: Software SaaS de Gestão Financeira (teste gratuito de 30 dias).
    *   **Ação Desejada**: Cadastro para Teste Gratuito (CPL - Custo Por Lead).
    *   **Comissão por Ação (CPL)**: R$ 25,00 por cada cadastro qualificado.
    *   **Custo Médio de Conversão (do Lead para Cliente Pagante)**: 15% dos leads convertem em clientes pagantes.
    *   **Receita Média por Cliente (LTV - Lifetime Value)**: R$ 600,00 (considerando assinatura mensal de R$ 50,00 por 12 meses).

2.  **Cálculo da Comissão Total para um Volume de Ações**:
    *   **Cenário**: Afiliado gera 200 cadastros qualificados em um mês.
    *   Comissão Total = Número de Cadastros * Comissão por Ação
    *   Exemplo: 200 * R$ 25,00 = R$ 5.000,00

3.  **Análise do Custo por Aquisição de Cliente (CAC) Gerado pelo Afiliado**:
    *   Clientes Convertidos = Número de Cadastros * Taxa de Conversão
    *   Exemplo: 200 * 0.15 = 30 clientes pagantes
    *   CAC Gerado pelo Afiliado = Comissão Total / Clientes Convertidos
    *   Exemplo: R$ 5.000,00 / 30 = R$ 166,67 por cliente

4.  **Cálculo do ROI e Comparação com LTV**:
    *   ROI para o Anunciante (por cliente) = (LTV - CAC Gerado pelo Afiliado) / CAC Gerado pelo Afiliado
    *   Exemplo: (R$ 600,00 - R$ 166,67) / R$ 166,67 = R$ 433,33 / R$ 166,67 ≈ 2.60 ou 260%
    *   **Interpretação**: Para cada R$ 1,00 investido em comissão para o afiliado, o anunciante espera um retorno de R$ 2,60. Este ROI de 260% é excelente, indicando que a comissão de R$ 25,00 por lead é sustentável e lucrativa, dado o LTV do cliente.

5.  **Otimização da Comissão (Opcional)**:
    *   Se o ROI fosse muito baixo (ex: abaixo de 100%), o anunciante poderia considerar reduzir o CPL ou negociar um modelo de CPA sobre a venda final.
    *   Se o ROI for muito alto e o volume de leads for baixo, o anunciante poderia considerar aumentar o CPL para atrair mais afiliados de alta performance, melhorando a competitividade da oferta.

---

## Templates

### Simulação de Comissão por Venda Direta

```
# Relatório de Simulação de Comissão de Afiliado - Venda Direta

## Informações do Produto
Nome do Produto: eBook "Finanças Pessoais Descomplicadas"
Preço de Venda Unitário: R$ 69,90

## Estrutura de Comissão
Tipo: Percentual sobre Venda
Taxa de Comissão: 20%

## Cenários de Vendas e Comissões
| Cenário | Vendas (Unidades) | Receita Bruta (R$) | Comissão por Venda (R$) | Comissão Total (R$) |
|---------|-------------------|--------------------|-------------------------|---------------------|
| Mínimo  | 20                | 1.398,00           | 13,98                   | 279,60              |
| Médio   | 50                | 3.495,00           | 13,98                   | 699,00              |
| Otimista| 100               | 6.990,00           | 13,98                   | 1.398,00            |
| Recorde | 150               | 10.485,00          | 13,98                   | 2.097,00            |

## Fórmulas Utilizadas
Comissão por Venda = Preço de Venda Unitário * Taxa de Comissão
Comissão Total = Vendas (Unidades) * Comissão por Venda

## Observações
*   Esta simulação não considera taxas de plataforma, impostos ou eventuais reembolsos.
*   A comissão é calculada sobre o preço de venda bruto.
```

### Projeção de Ganhos com Modelo CPL (Custo Por Lead)

```
# Projeção de Ganhos de Afiliado - Modelo Custo Por Lead (CPL)

## Informações da Oferta
Oferta: Cadastro para Webinar Gratuito "Segredos do Investimento Inteligente"
Comissão por Lead Qualificado: R$ 12,00

## Cenários de Geração de Leads e Ganhos
| Cenário | Leads Gerados | Comissão por Lead (R$) | Comissão Total (R$) |
|---------|---------------|------------------------|---------------------|
| Mínimo  | 80            | 12,00                  | 960,00              |
| Médio   | 150           | 12,00                  | 1.800,00            |
| Otimista| 300           | 12,00                  | 3.600,00            |
| Recorde | 500           | 12,00                  | 6.000,00            |

## Análise de Conversão para o Anunciante (Exemplo)
Taxa de Conversão Lead -> Cliente: 5%
LTV (Lifetime Value) por Cliente: R$ 800,00

## Cálculo do CAC e ROI (para o Anunciante no Cenário Otimista)
Leads Gerados: 300
Comissão Total: R$ 3.600,00
Clientes Convertidos: 300 * 0.05 = 15
CAC Gerado pelo Afiliado: R$ 3.600,00 / 15 = R$ 240,00
ROI para o Anunciante: (R$ 800,00 - R$ 240,00) / R$ 240,00 = 2.33 ou 233%

## Observações
*   "Leads Gerados" refere-se a leads qualificados, conforme as regras do programa de afiliados.
*   O ROI é uma métrica crucial para o anunciante avaliar a sustentabilidade do CPL.
```

---

## Checklist

- [x] Confirmar a estrutura de comissão (percentual, valor fixo, CPL, CPA, híbrida).
- [x] Verificar o valor unitário do produto/serviço ou o valor por ação/lead.
- [x] Definir a janela de atribuição do cookie (ex: 30, 60, 90 dias) e seu impacto.
- [x] Considerar o tratamento de reembolsos, chargebacks e cancelamentos de pedidos.
- [x] Avaliar a necessidade de comissões escalonadas por volume ou performance.
- [x] Incluir taxas de plataforma de pagamento (ex: Hotmart, Eduzz, Stripe) no cálculo da base líquida.
- [x] Projetar cenários de volume (otimista, realista, pessimista) para a comissão total.
- [x] Analisar o impacto de impostos e encargos sobre o recebimento da comissão pelo afiliado.
- [x] Comparar a comissão oferecida com benchmarks de mercado para ofertas similares.
- [x] Calcular o Custo por Aquisição (CAC) efetivo gerado pelo afiliado para o anunciante.

---

## Métricas de Referência

| Métrica                      | Benchmark (Mercado Geral)  | Meta (Otimização)          |
|------------------------------|----------------------------|----------------------------|
| **Taxa de Comissão (Venda)** | 10% - 30% (produtos digitais), 5% - 15% (físicos) | 20% - 40% (digital), 10% - 20% (físico) |
| **CPA (Custo Por Aquisição)**| 10% - 30% do LTV (para o anunciante) | < 20% do LTV               |
| **CPL (Custo Por Lead)**     | R$ 5,00 - R$ 50,00 (varia muito por nicho) | R$ 10,00 - R$ 30,00 (nichos específicos) |
| **EPC (Ganhos Por Clique)**  | R$ 0,50 - R$ 3,00 (varia por nicho e oferta) | > R$ 1,50                  |
| **Taxa de Conversão (Afiliado)**| 0.5% - 3% (geral), 5% - 10% (audiência quente) | > 2% (geral), > 7% (audiência quente) |
| **LTV/CAC (Anunciante)**     | > 3:1                      | > 5:1                      |

---

## Erros Comuns

1.  **Ignorar Reembolsos e Chargebacks**: Calcular a comissão apenas sobre as vendas brutas sem descontar devoluções pode levar a pagamentos indevidos.
    *   **Como evitar**: Implementar um período de carência (ex: 30 dias) após a venda antes de liberar a comissão, permitindo que eventuais reembolsos sejam processados e descontados. Exemplo: Se um produto foi vendido por R$100 com 20% de comissão (R$20), mas o cliente pediu reembolso em 15 dias, a comissão de R$20 deve ser estornada ou não paga.
2.  **Não Considerar a Janela de Atribuição do Cookie**: Afiliados podem perder comissões se a janela de atribuição for muito curta ou se a lógica de "último clique" não for transparente.
    *   **Como evitar**: Comunicar claramente a duração do cookie (ex: "cookie de 60 dias") e a regra de atribuição (ex: "último clique válido"). Para um produto de R$200 com 10% de comissão, se um cliente clica no link do afiliado A, depois no afiliado B, e compra em 5 dias, a comissão de R$20 vai para o afiliado B se a regra for "último clique".
3.  **Usar Taxas Fixas em Mercados Voláteis ou de Alto Volume**: Uma taxa de comissão fixa pode ser insustentável para o anunciante em grandes volumes ou desmotivadora para afiliados de alta performance.
    *   **Como evitar**: Implementar uma estrutura de comissão escalonada, onde a taxa aumenta com o volume de vendas ou leads, incentivando o crescimento. Exemplo: 10% para até 50 vendas, 12% para 51-100 vendas, e 15% acima de 100 vendas, para um produto de R$100.
4.  **Não Otimizar a Taxa de Comissão com base no LTV do Cliente**: Pagar comissões que excedem o valor de vida útil do cliente para o anunciante (ou que resultam em CAC insustentável).
    *   **Como evitar**: Calcular o LTV médio de um cliente adquirido via afiliado e assegurar que o CAC (incluindo a comissão) seja uma fração sustentável (ex: 1/3 do LTV). Se o LTV for R$300, o CAC ideal máximo seria R$100. Se a comissão por venda é R$120, a oferta é insustentável.

---

## Dicas Avançadas

1.  **Modelagem de Comissão Baseada em LTV (Lifetime Value)**: Para produtos de assinatura ou com upsells recorrentes, calcule a comissão como uma porcentagem do LTV projetado do cliente. Isso permite pagar comissões mais generosas no início, pois se sabe que o cliente trará mais receita ao longo do tempo. Exemplo: Em vez de 10% da primeira mensalidade de R$50, pague 50% da primeira mensalidade (R$25) + 5% das mensalidades seguintes por 6 meses, baseando-se em um LTV médio de R$300.
2.  **Comissões Híbridas (CPL + CPA)**: Combine modelos para otimizar a aquisição. Pague um valor menor por lead qualificado (CPL) e um bônus maior por cada lead que se converte em cliente pagante (CPA). Isso incentiva o afiliado a focar na qualidade do lead. Exemplo: R$5 por lead qualificado + R$50 por cada lead que se torna cliente.
3.  **Análise de Cohort para Afiliados**: Monitore o desempenho de grupos de clientes trazidos por afiliados específicos ao longo do tempo. Isso revela quais afiliados atraem clientes de maior LTV ou menor churn, permitindo otimizar as parcerias e recompensar o valor de longo prazo, não apenas o volume inicial.
4.  **Otimização Dinâmica de Taxas de Comissão por Tier de Afiliado**: Crie diferentes "tiers" (níveis) de afiliados (ex: Iniciante, Prata, Ouro, Diamante) com base no volume histórico de vendas ou na qualidade dos leads. Ofereça taxas de comissão progressivamente maiores para afiliados de tiers mais altos, incentivando a lealdade e a performance dos parceiros mais valiosos.
5.  **Comissões Recorrentes para Produtos de Assinatura**: Em vez de uma única comissão, pague uma porcentagem da mensalidade do cliente enquanto ele permanecer ativo. Isso cria um fluxo de renda passivo para o afiliado e alinha seus interesses com a retenção do cliente para o anunciante. Exemplo: 15% da mensalidade de R$99,00, paga a cada mês que o cliente indicado renovar a assinatura.