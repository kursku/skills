---
name: dynamic-pricing
description: "Dynamic Pricing — Skill especializada para dynamic pricing"
license: MIT
metadata:
  version: 1.0.0
  author: Cafe Code AI
  category: 06-financeiro-precos
  updated: 2026-03-01
risk: critical
---

# Dynamic Pricing

Esta skill capacita o Claude a implementar e otimizar estratégias de precificação dinâmica, ajustando preços em tempo real com base em demanda, oferta, concorrência e comportamento do consumidor para maximizar receita e margem.

---

## Keywords

Precificação algorítmica, otimização de receita, elasticidade de demanda, segmentação de preços, precificação baseada em valor, concorrência em tempo real, gestão de yield, precificação por surto (surge pricing), automação de preços, estratégias competitivas, precificação preditiva, LTV/CAC.

---

## Quick Start

1.  Coletar dados históricos de vendas (preço, volume, data, promoções, custo unitário) e dados de mercado (preços dos concorrentes, eventos externos) dos últimos 12-24 meses.
2.  Selecionar o modelo de elasticidade de demanda adequado para o produto ou serviço (ex: regressão log-log para e-commerce) e calibrá-lo com os dados coletados.
3.  Definir as regras de negócio e restrições de preço para cada SKU ou categoria (preço mínimo absoluto, preço máximo relativo à concorrência, margem alvo).
4.  Implementar um algoritmo de ajuste de preços que reaja a mudanças na demanda, níveis de estoque, preços da concorrência e eventos sazonais, executando ajustes automáticos.

---

## Core Workflows

### Workflow 1: Otimização de Preços por Elasticidade de Demanda

Este workflow detalha a construção de um sistema de precificação dinâmica focado em maximizar a receita e o lucro através da compreensão da sensibilidade do preço.

*   **Passo 1: Coleta e Pré-processamento de Dados para Modelagem**
    *   **Ação**: Reunir dados históricos de vendas da SKU "Smartwatch Xylo 3.0" dos últimos 18 meses, incluindo: `data_venda`, `hora_venda`, `preco_unitario_vendido`, `volume_vendido`, `custo_unitario_produto`, `desconto_aplicado_percentual`, `canal_venda`. Coletar também dados de preços dos 3 principais concorrentes para produtos equivalentes ("Smartwatch Alpha", "Smartwatch Beta") e indicadores de demanda externa (ex: feriados, eventos promocionais).
    *   **Exemplo de Dados**:
        *   `Data: 2023-10-26, Preço: R$ 899, Volume: 120, Custo: R$ 550, Concorrente A: R$ 920, Concorrente B: R$ 880, Promoção: 0`
        *   `Data: 2023-11-24 (Black Friday), Preço: R$ 699, Volume: 850, Custo: R$ 550, Concorrente A: R$ 750, Concorrente B: R$ 700, Promoção: 1`
    *   **Fórmula de Margem Bruta**: `Margem Bruta = (Preço Venda - Custo Unitário) / Preço Venda`.

*   **Passo 2: Modelagem da Elasticidade de Preço**
    *   **Ação**: Utilizar regressão linear múltipla para estimar a elasticidade-preço, incorporando variáveis como preço próprio, preços dos concorrentes, promoções e sazonalidade.
    *   **Fórmula (Exemplo de Modelo Log-Log)**:
        `log(Volume Vendido) = β0 + β1 * log(Preço Unitário) + β2 * log(Preço Concorrente A) + β3 * log(Preço Concorrente B) + β4 * Promoção_Binária + β5 * Sazonalidade_Mês`
        *   O coeficiente `β1` representa a elasticidade-preço. Se `β1 = -1.5`, um aumento de 1% no preço próprio resulta em uma queda de 1.5% no volume de vendas (produto elástico).
    *   **Exemplo**: Para o "Smartwatch Xylo 3.0", `β1` foi estimado em -1.8, indicando alta sensibilidade a mudanças de preço. `β2` (preço concorrente A) foi de 0.5, indicando que o aumento do preço do concorrente A aumenta a demanda pelo Xylo 3.0.

*   **Passo 3: Definição de Regras e Restrições de Negócio**
    *   **Ação**: Estabelecer limites claros para o ajuste de preços, garantindo lucratividade e competitividade.
    *   **Regras e Fórmulas**:
        *   **Preço Mínimo Absoluto**: `Preço Min = Custo Unitário * (1 + Margem Mínima Alvo)`
            *   Exemplo: Para o Smartwatch Xylo 3.0, com Custo R$ 550 e Margem Mínima Alvo de 15%, o `Preço Min = R$ 550 * (1 + 0.15) = R$ 632.50`.
        *   **Preço Máximo Relativo à Concorrência**: `Preço Max = Preço Concorrente Mais Alto * 1.05` (não exceder 5% do concorrente mais caro) OU `Preço Max = Preço Concorrente Mais Barato * 1.20` (não ser mais de 20% mais caro).
            *   Exemplo: Se Concorrente A está a R$ 950 e Concorrente B a R$ 890, o `Preço Max` seria R$ 950 * 1.05 = R$ 997.50.
        *   **Margem Alvo Ponderada**: Manter a margem bruta média acima de 25%.
    *   **Restrições Operacionais**: Evitar ajustes de preço mais de 3 vezes por hora; evitar quedas de preço superiores a 5% em uma única transação.

*   **Passo 4: Implementação do Algoritmo de Ajuste Dinâmico**
    *   **Ação**: Desenvolver um algoritmo que utilize os dados em tempo real (demanda, estoque, concorrência) e o modelo de elasticidade para ajustar os preços automaticamente, respeitando as regras e restrições.
    *   **Lógica do Algoritmo (Exemplo)**:
        *   **Disparador**: A cada 15 minutos, ou quando o preço de um concorrente muda em > R$ 10, ou quando o estoque cai/sobe 10%.
        *   **Condição 1 (Baixa Demanda / Alto Estoque)**: Se `Volume Vendas (última hora)` < `Média Histórica (última hora)` * 0.8 E `Estoque` > `Estoque Máximo` * 0.7:
            *   **Ação**: Reduzir preço em 1% a cada ciclo até `Preço Mínimo` ou até que `Margem Bruta` atinja 20%.
            *   Exemplo: Preço atual R$ 899. Estoque 80%. Vendas 30% abaixo da média. Algoritmo reduz para R$ 890.91.
        *   **Condição 2 (Alta Demanda / Baixo Estoque)**: Se `Volume Vendas (última hora)` > `Média Histórica (última hora)` * 1.2 E `Estoque` < `Estoque Máximo` * 0.3:
            *   **Ação**: Aumentar preço em 0.5% a cada ciclo até `Preço Máximo` ou até que a redução de volume esperada (pela elasticidade) compense o aumento da receita.
            *   Exemplo: Preço atual R$ 899. Estoque 25%. Vendas 20% acima da média. Algoritmo aumenta para R$ 903.45.
        *   **Condição 3 (Reação à Concorrência)**: Se `Preço Concorrente A` < `Preço Atual` * 0.95:
            *   **Ação**: Ajustar preço para `Preço Concorrente A` + `Diferencial Competitivo` (ex: R$ 15), desde que `Margem Bruta` > `Margem Mínima`.
            *   Exemplo: Concorrente A reduz para R$ 850. Algoritmo ajusta para R$ 865, desde que R$ 865 > R$ 632.50 (preço mínimo).

### Workflow 2: Precificação Baseada em Valor e Segmentação de Clientes

Este workflow foca em adaptar os preços à percepção de valor e à disposição a pagar de diferentes segmentos de clientes, maximizando o LTV.

*   **Passo 1: Segmentação de Clientes por LTV e Disposição a Pagar**
    *   **Ação**: Calcular o Lifetime Value (LTV) e o Custo de Aquisição de Clientes (CAC) para identificar segmentos de alto e baixo valor. Realizar pesquisas ou análises de dados comportamentais para estimar a disposição a pagar por diferentes features ou serviços.
    *   **Fórmulas**:
        *   `LTV = (Valor Médio Compra * Frequência Compra * Vida Útil Cliente) - CAC`
        *   `CAC = Custo Total Marketing e Vendas / Número de Novos Clientes`
    *   **Exemplo**:
        *   **Segmento A: "Entusiastas Premium"**: LTV médio > R$ 5.000, sensibilidade baixa a preço para features exclusivas, alta disposição a pagar por inovação e suporte prioritário.
        *   **Segmento B: "Compradores Custo-Benefício"**: LTV médio R$ 800 - R$ 2.500, alta sensibilidade a preço, foco em funcionalidade básica e durabilidade.
        *   **Pesquisa**: Um estudo de Gabor-Granger para um novo software de design gráfico revela que o Segmento A está disposto a pagar até R$ 250/mês por um "Plano Pro com IA", enquanto o Segmento B prefere um "Plano Essencial" até R$ 80/mês.

*   **Passo 2: Criação de Ofertas e Pacotes de Produtos Diferenciados**
    *   **Ação**: Desenvolver diferentes versões do produto ou serviço (pacotes, tiers) para atender às necessidades e à disposição a pagar de cada segmento.
    *   **Exemplo (Software SaaS de CRM)**:
        *   **Plano Básico (R$ 79/mês)**: Para pequenas empresas (Segmento B). Inclui: 1 usuário, 500 contatos, suporte por e-mail, funcionalidades essenciais de vendas.
        *   **Plano Pro (R$ 199/mês)**: Para empresas em crescimento (Segmento A/B). Inclui: 5 usuários, 5.000 contatos, suporte prioritário, automação de marketing, relatórios avançados.
        *   **Plano Enterprise (R$ 499/mês)**: Para grandes corporações (Segmento A). Inclui: Usuários ilimitados, contatos ilimitados, suporte 24/7, consultoria dedicada, integrações customizadas.

*   **Passo 3: Precificação Personalizada e Ofertas Dinâmicas por Segmento**
    *   **Ação**: Utilizar o perfil do cliente e seu comportamento para oferecer preços ou pacotes personalizados de forma dinâmica (ex: via website, e-mail marketing, app).
    *   **Exemplo de Regras Dinâmicas**:
        *   **Para "Entusiastas Premium" (Segmento A)**:
            *   **Condição**: Usuário logado, histórico de compras premium, LTV > R$ 5.000.
            *   **Ação**: Apresentar "Plano Pro" com um "upgrade gratuito por 3 meses" para o recurso de IA (valor percebido alto), ou "Plano Enterprise" com desconto de 15% na primeira assinatura.
            *   **Objetivo**: Maximizar o LTV, incentivando a compra da versão mais completa.
        *   **Para "Compradores Custo-Benefício" (Segmento B)**:
            *   **Condição**: Usuário logado, histórico de compras básicas, LTV < R$ 2.500, tempo de permanência na página do "Plano Básico".
            *   **Ação**: Oferecer um período de teste estendido para o "Plano Básico" (ex: 30 dias em vez de 7) ou um cupom de R$ 20 de desconto na primeira mensalidade do "Plano Básico".
            *   **Objetivo**: Reduzir a barreira de entrada e converter clientes sensíveis a preço.
        *   **Para "Clientes Inativos" (qualquer segmento)**:
            *   **Condição**: Usuário que não loga há 60 dias, LTV > R$ 1.000.
            *   **Ação**: Enviar e-mail com oferta de "reativação": 50% de desconto no Plano Pro por 3 meses.

*   **Passo 4: Análise de Custo para Servir (CTS) por Segmento**
    *   **Ação**: Calcular o custo para atender cada segmento, garantindo que as estratégias de precificação personalizadas mantenham a rentabilidade.
    *   **Fórmula**: `CTS = Custo Suporte + Custo Infraestrutura + Custo Marketing Pessoalizado + Outros Custos Diretos por Segmento`
    *   **Exemplo**:
        *   **Segmento A ("Entusiastas Premium")**: Pode ter um CTS mais alto devido ao suporte prioritário 24/7 e consultoria dedicada (ex: R$ 150/mês). Se o `Preço Líquido` do Plano Enterprise for R$ 450/mês, a `Margem Líquida` é R$ 300.
        *   **Segmento B ("Compradores Custo-Benefício")**: CTS mais baixo devido ao suporte por e-mail e autoatendimento (ex: R$ 20/mês). Se o `Preço Líquido` do Plano Básico for R$ 79/mês, a `Margem Líquida` é R$ 59.
    *   **Objetivo**: Assegurar que, mesmo com a personalização, a relação `(Preço - CTS) / Preço` seja sustentável e contribua para a margem geral da empresa.

---

## Templates

### Template 1: Análise de Elasticidade de Preço (Planilha CSV)

```csv
Data,SKU,Preço Venda,Volume Vendido,Custo Unitário,Preço Concorrente A,Preço Concorrente B,Promoção Ativa (0/1),Elasticidade Calculada
2023-01-05,Smartphone XYZ,1500,250,900,1550,1480,0,
2023-01-12,Smartphone XYZ,1480,270,900,1550,1480,0,
2023-01-19,Smartphone XYZ,1450,300,900,1550,1480,0,
2023-01-26,Smartphone XYZ,1400,350,900,1550,1480,0,
2023-02-02,Smartphone XYZ,1350,420,900,1550,1480,0,
2023-02-09,Smartphone XYZ,1300,480,900,1550,1480,0,
2023-02-16,Smartphone XYZ,1250,550,900,1550,1480,0,-1.75
2023-02-23,Smartphone XYZ,1200,620,900,1550,1480,1,
2023-03-01,Tablet ABC,800,180,500,820,790,0,
2023-03-08,Tablet ABC,780,200,500,820,790,0,
2023-03-15,Tablet ABC,750,230,500,820,790,0,-1.20
```

### Template 2: Regras de Precificação Dinâmica (JSON)

```json
{
  "product_id": "SKU001-SmartwatchXylo3.0",
  "category": "Eletrônicos/Wearables",
  "base_price": 899.00,
  "cost_unit": 550.00,
  "min_margin_percentage": 0.15,
  "min_price_absolute": 632.50,
  "max_price_relative_competitor": {
    "competitor_price_source": "highest",
    "multiplier": 1.05
  },
  "target_margin_percentage": 0.25,
  "elasticity_coefficient": -1.8,
  "dynamic_rules": [
    {
      "rule_id": "DEMAND_LOW_STOCK_HIGH",
      "trigger": {
        "metric": "sales_volume_last_hour",
        "condition": "below_average_x_percent",
        "threshold": 0.8,
        "and_metric": "stock_level",
        "and_condition": "above_capacity_x_percent",
        "and_threshold": 0.7
      },
      "action": {
        "type": "decrease_price_by_percentage",
        "value": 0.01,
        "limit_to_min_price": true,
        "limit_to_min_margin": 0.20,
        "frequency_cap_per_hour": 3
      }
    },
    {
      "rule_id": "DEMAND_HIGH_STOCK_LOW",
      "trigger": {
        "metric": "sales_volume_last_hour",
        "condition": "above_average_x_percent",
        "threshold": 1.2,
        "and_metric": "stock_level",
        "and_condition": "below_capacity_x_percent",
        "and_threshold": 0.3
      },
      "action": {
        "type": "increase_price_by_percentage",
        "value": 0.005,
        "limit_to_max_price_relative": true,
        "frequency_cap_per_hour": 3
      }
    },
    {
      "rule_id": "COMPETITOR_PRICE_DROP",
      "trigger": {
        "metric": "competitor_price_A",
        "condition": "below_own_price_x_percent",
        "threshold": 0.95
      },
      "action": {
        "type": "adjust_price_to_competitor_plus_fixed",
        "competitor_source": "competitor_price_A",
        "fixed_difference": 15.00,
        "limit_to_min_margin": 0.18
      }
    }
  ]
}
```

---

## Checklist

- [x] Dados históricos de vendas (preço, volume, custo) coletados e limpos para os últimos 12-24 meses.
- [x] Dados de preços dos principais concorrentes atualizados em tempo real ou diariamente.
- [x] Elasticidade de preço calculada e validada para cada SKU ou categoria de produto relevante.
- [x] Definição clara de preço mínimo (custo + margem mínima) e preço máximo (teto de valor percebido/concorrência).
- [x] Algoritmo de ajuste de preços implementado e testado em ambiente de simulação (sandbox).
- [x] Regras de negócio para promoções e eventos sazonais integradas ao sistema de precificação.
- [x] Monitoramento em tempo real de KPIs de precificação: margem média, receita total, taxa de conversão, LTV.
- [x] Mecanismo de fallback para preços manuais em caso de falha do sistema dinâmico ou eventos inesperados.
- [x] Segmentação de clientes definida para ofertas e precificação personalizada (LTV, disposição a pagar).
- [x] Análise de Custo para Servir (CTS) por segmento de cliente realizada para garantir rentabilidade.

---

## Métricas de Referência

| Métrica | Benchmark (Varejo Online) | Meta (Otimizado) |
|---------------------------------|---------------------------|--------------------------|
| **Margem Bruta Média** | 30% - 40% | 38% - 48% |
| **Elasticidade de Preço (próprio)** | -1.0 a -2.0 | -1.2 a -1.8 (otimizada) |
| **Taxa de Conversão (Preço Ajustado)** | 1.5% - 2.5% | 2.0% - 3.5% |
| **LTV/CAC Ratio** | > 2:1 | > 3:1 |
| **Turnover de Estoque (SKUs com DP)** | 6x - 10x/ano | 8x - 12x/ano |
| **ARPU