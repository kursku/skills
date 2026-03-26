---
name: financial-health-check
description: "Financial Health Check — Skill especializada para financial health check"
license: MIT
metadata:
  version: 1.0.0
  author: Cafe Code AI
  category: 06-financeiro-precos
  updated: 2026-03-01
risk: critical
---

# Financial Health Check

Esta skill capacita o Claude a realizar uma análise profunda da saúde financeira de empresas, identificando pontos fortes, fracos e recomendando estratégias de otimização para sustentabilidade e rentabilidade.

---

## Keywords

Análise Financeira, DRE, Balanço Patrimonial, Fluxo de Caixa, Rentabilidade, Liquidez, Endividamento, Margem Bruta, Margem Líquida, Ponto de Equilíbrio, ROI, LTV/CAC, Precificação, Projeções Financeiras.

---

## Quick Start

1.  **Coletar Dados Financeiros:** Obtenha os relatórios financeiros (Demonstrativo de Resultado do Exercício - DRE, Balanço Patrimonial - BP, Demonstrativo de Fluxo de Caixa - DFC) dos últimos 3 a 5 anos fiscais da empresa em questão.
2.  **Calcular Indicadores Chave:** Utilize os dados coletados para calcular automaticamente os principais indicadores de liquidez (ex: Liquidez Corrente), rentabilidade (ex: Margem Líquida) e endividamento (ex: Endividamento Geral).
3.  **Comparar com Benchmarks:** Compare os indicadores calculados com as métricas de referência do setor de atuação da empresa (ex: Margem Líquida para SaaS é diferente de Varejo).
4.  **Identificar Anomalias e Tendências:** Analise a evolução dos indicadores ao longo dos anos, buscando picos, quedas ou tendências que exijam investigação. Por exemplo, um aumento constante do Passivo Circulante sem acompanhamento do Ativo Circulante.
5.  **Gerar Diagnóstico Preliminar:** Com base nas comparações e tendências, formule um diagnóstico inicial da saúde financeira, destacando áreas críticas e oportunidades.

---

## Core Workflows

### Workflow 1: Análise Detalhada de Rentabilidade e Ponto de Equilíbrio

Este workflow foca na capacidade da empresa de gerar lucro e no volume mínimo de vendas necessário para cobrir seus custos.

1.  **Extração de Dados da DRE:**
    *   Extraia a Receita Bruta, Custos Variáveis (Custo de Mercadoria Vendida - CMV, Custo do Serviço Prestado - CSP), Despesas Operacionais Fixas (Aluguel, Salários administrativos, Marketing fixo) diretamente da DRE dos últimos 3 períodos.
    *   *Exemplo:* Para uma empresa de software, a receita bruta foi R$1.200.000 em 2023, os custos variáveis (licenças de terceiros, comissões de venda) foram R$300.000, e as despesas fixas (salários da equipe de desenvolvimento, aluguel do escritório) foram R$500.000.

2.  **Cálculo da Margem de Contribuição (MC):**
    *   Calcule a Margem de Contribuição Total (Receita Bruta - Custos Variáveis Totais) e a Margem de Contribuição Percentual (MC Total / Receita Bruta).
    *   Para produtos/serviços específicos, calcule a Margem de Contribuição Unitária (Preço de Venda Unitário - Custo Variável Unitário).
    *   *Fórmula:* `MC Total = Receita Bruta - Custos Variáveis Totais`
    *   *Fórmula:* `MC Percentual = (MC Total / Receita Bruta) * 100`
    *   *Exemplo:* MC Total = R$1.200.000 - R$300.000 = R$900.000. MC Percentual = (R$900.000 / R$1.200.000) * 100 = 75%.

3.  **Cálculo do Ponto de Equilíbrio (PE):**
    *   Determine o Ponto de Equilíbrio Contábil, ou seja, o volume de vendas (em unidades ou em valor) necessário para que a empresa não tenha lucro nem prejuízo.
    *   *Fórmula (em valor):* `PE (valor) = Despesas Fixas Totais / MC Percentual`
    *   *Fórmula (em unidades):* `PE (unidades) = Despesas Fixas Totais / MC Unitária`
    *   *Exemplo:* PE (valor) = R$500.000 / 0.75 = R$666.666,67. Isso significa que a empresa precisa faturar R$666.666,67 para cobrir todos os seus custos fixos e variáveis.

4.  **Análise de Retorno sobre Investimento (ROI):**
    *   Para projetos ou investimentos específicos, calcule o ROI para avaliar a eficiência do capital empregado.
    *   *Fórmula:* `ROI = (Ganho do Investimento - Custo do Investimento) / Custo do Investimento`
    *   *Exemplo:* Um investimento em nova ferramenta de marketing de R$50.000 gerou R$75.000 em vendas adicionais (lucro bruto). ROI = (R$75.000 - R$50.000) / R$50.000 = 0.50 ou 50%.

5.  **Recomendações de Otimização:**
    *   Com base nos cálculos, identifique se a empresa está operando acima ou abaixo do seu PE e se seus ROIs são satisfatórios. Proponha estratégias como redução de custos fixos, otimização de custos variáveis ou revisão da precificação para aumentar a MC.

### Workflow 2: Avaliação de Liquidez e Endividamento

Este workflow avalia a capacidade da empresa de cumprir suas obrigações financeiras de curto e longo prazo.

1.  **Coleta de Dados do Balanço Patrimonial (BP):**
    *   Extraia o Ativo Circulante (Caixa, Bancos, Contas a Receber, Estoques), Passivo Circulante (Fornecedores, Empréstimos de Curto Prazo, Salários a Pagar) e Patrimônio Líquido (PL) do BP dos últimos 3 períodos.
    *   *Exemplo:* Em 2023, o Ativo Circulante foi R$800.000, o Passivo Circulante R$1.000.000 e o Ativo Total R$2.500.000.

2.  **Cálculo dos Índices de Liquidez:**
    *   **Liquidez Corrente:** `Ativo Circulante / Passivo Circulante`. Indica a capacidade de pagamento de curto prazo.
    *   **Liquidez Seca:** `(Ativo Circulante - Estoques) / Passivo Circulante`. Exclui estoques por serem menos líquidos.
    *   **Liquidez Imediata:** `Caixa e Equivalentes de Caixa / Passivo Circulante`. Mostra a capacidade de pagar dívidas imediatas.
    *   *Exemplo:* Liquidez Corrente = R$800.000 / R$1.000.000 = 0.8x. Isso é preocupante, pois indica que a empresa não tem ativos de curto prazo suficientes para cobrir suas dívidas de curto prazo.

3.  **Cálculo dos Índices de Endividamento:**
    *   **Endividamento Geral:** `(Passivo Circulante + Passivo Não Circulante) / Ativo Total`. Indica a proporção dos ativos financiados por terceiros.
    *   **Capital de Terceiros sobre Patrimônio Líquido:** `(Passivo Circulante + Passivo Não Circulante) / Patrimônio Líquido`. Mostra a dependência de capital de terceiros em relação ao capital próprio.
    *   *Fórmula LTV/CAC (para empresas de recorrência):* `LTV = (Receita Média por Cliente * Margem Bruta Média) / Taxa de Churn`. `CAC = Custo Total de Marketing e Vendas / Número de Novos Clientes`. `Razão LTV/CAC`.
    *   *Exemplo:* Endividamento Geral = (R$1.000.000 + R$500.000) / R$2.500.000 = 1.500.000 / 2.500.000 = 0.6x. Isso significa que 60% dos ativos são financiados por terceiros, o que pode ser considerado moderado a alto dependendo do setor.

4.  **Análise do Fluxo de Caixa Operacional (FCO):**
    *   Avalie se o FCO (gerado pelas atividades principais da empresa) é positivo e suficiente para cobrir investimentos e dívidas, sem depender excessivamente de financiamentos. Um FCO consistentemente negativo é um forte sinal de alerta.
    *   *Exemplo:* Se o FCO dos últimos 3 anos foi R$150.000, R$80.000 e -R$50.000, há uma tendência preocupante de diminuição da geração de caixa operacional.

5.  **Recomendações para Gerenciamento de Caixa e Dívidas:**
    *   Com base nos índices, sugira ações como renegociação de prazos com fornecedores, otimização de estoques, redução de despesas operacionais ou busca por capital próprio para fortalecer a estrutura financeira.

---

## Templates

### Template: Relatório de Ponto de Equilíbrio Detalhado

```
# Análise de Ponto de Equilíbrio - Produto/Serviço "Consultoria Estratégica"

## Dados de Entrada:
-   **Período da Análise:** Ano Fiscal 2023
-   **Produto/Serviço:** Consultoria Estratégica para PMEs
-   **Preço de Venda Unitário:** R$ 15.000,00
-   **Custo Variável Unitário (Comissões, Licenças de Software, Deslocamento):** R$ 4.500,00
-   **Despesas Fixas Totais Mensais (Salários fixos, Aluguel, Marketing Institucional):** R$ 55.000,00

## Cálculos:
-   **Margem de Contribuição Unitária (MCU):**
    *   Preço de Venda Unitário - Custo Variável Unitário
    *   R$ 15.000,00 - R$ 4.500,00 = **R$ 10.500,00**

-   **Margem de Contribuição Percentual:**
    *   (MCU / Preço de Venda Unitário) * 100
    *   (R$ 10.500,00 / R$ 15.000,00) * 100 = **70%**

-   **Ponto de Equilíbrio em Unidades (PEu):**
    *   Despesas Fixas Totais Mensais / MCU
    *   R$ 55.000,00 / R$ 10.500,00 = **5.24 unidades/mês (arredondado para 6 unidades)**
    *   *Interpretação:* A empresa precisa vender no mínimo 6 projetos de consultoria por mês para cobrir todos os seus custos.

-   **Ponto de Equilíbrio em Valor (PEv):**
    *   Despesas Fixas Totais Mensais / Margem de Contribuição Percentual
    *   R$ 55.000,00 / 0.70 = **R$ 78.571,43/mês**
    *   *Interpretação:* A empresa precisa faturar R$ 78.571,43 por mês com este serviço para não ter lucro nem prejuízo.

## Conclusão e Recomendações:
A empresa atualmente vende em média 8 projetos de consultoria por mês, o que a coloca acima do ponto de equilíbrio. No entanto, uma queda de 2 projetos já a deixaria em situação crítica.
**Recomendação:**
1.  **Monitorar a Margem de Contribuição:** Qualquer aumento nos custos variáveis ou redução no preço de venda impactará diretamente o PE.
2.  **Reduzir Despesas Fixas:** Avaliar oportunidades para otimizar despesas fixas (ex: renegociar aluguel) para diminuir o PE e aumentar a margem de segurança.
3.  **Análise de Sensibilidade:** Simular cenários de venda (ex: 4, 5, 7 projetos/mês) para entender o impacto no lucro e na necessidade de caixa.
```

### Template: Sumário de Índices Financeiros Chave

```
# Sumário de Índices Financeiros - Empresa "Tech Solutions Ltda."

## Período Analisado: 31/12/2023

| Indicador           | Fórmula                     | Valor Atual | Benchmark Setor (TI/SaaS) | Análise                                            | Recomendação                                                                                             |
|---------------------|-----------------------------|-------------|---------------------------|----------------------------------------------------|----------------------------------------------------------------------------------------------------------|
| **Liquidez Corrente** | Ativo Circulante / Passivo Circulante | 0.95x       | > 1.5x                    | Capacidade de pagamento de curto prazo é insuficiente. | Reavaliar prazos de recebimento e pagamento, negociar dívidas de curto prazo para alongar o perfil.      |
| **Liquidez Seca**   | (Ativo Circulante - Estoques) / Passivo Circulante | 0.90x       | > 1.0x                    | Similar à liquidez corrente, com poucos estoques relevantes. | Otimizar gestão de contas a receber e avaliar adiantamentos de clientes.                                 |
| **Margem Bruta**    | (Receita Líquida - CMV) / Receita Líquida | 65%         | 60-75%                    | Saudável, dentro da média do setor.                | Manter controle rigoroso sobre custos variáveis e otimizar processos de entrega de serviço.              |
| **Margem Líquida**  | Lucro Líquido / Receita Líquida | 8%          | 10-15%                    | Abaixo do benchmark. Despesas operacionais elevadas. | Revisar DRE para identificar despesas operacionais excessivas, buscar otimização de gastos de marketing e administrativos. |
| **Endividamento Geral** | (Passivo Circulante + Passivo Não Circulante) / Ativo Total | 0.70x       | < 0.60x                   | Alto nível de endividamento, risco financeiro elevado. | Elaborar plano de redução de dívida, priorizar quitação de empréstimos com juros mais altos. Considerar aumento de capital próprio. |
| **LTV/CAC**         | (LTV calculado / CAC calculado) | 2.5:1       | > 3:1                     | Custo de aquisição de cliente é relativamente alto. | Otimizar campanhas de marketing para melhorar a conversão, focar na retenção para aumentar LTV.           |

## Conclusão Geral:
A Tech Solutions Ltda. apresenta uma boa margem bruta, indicando eficiência na entrega de seus serviços. Contudo, enfrenta desafios significativos em liquidez, endividamento e rentabilidade líquida, além de um LTV/CAC subótimo. A estrutura de custos operacionais e a gestão da dívida precisam de atenção imediata.

```

---

## Checklist

-   [x] Verificar a consistência e integridade dos dados contábeis (DRE, BP, DFC) dos últimos 3-5 anos.
-   [x] Calcular a Margem Bruta e a Margem Líquida de cada período para identificar tendências de rentabilidade.
-   [x] Analisar o Ponto de Equilíbrio em unidades e valor para todos os produtos/serviços principais.
-   [x] Avaliar a Liquidez Corrente e a Liquidez Seca para determinar a capacidade de pagamento de curto prazo.
-   [x] Calcular o Nível de Endividamento Geral e a relação Capital de Terceiros/Patrimônio Líquido.
-   [x] Comparar o crescimento da Receita com o crescimento dos Custos e Despesas Operacionais ao longo do tempo.
-   [x] Analisar o Fluxo de Caixa Operacional (FCO) para entender a geração de caixa das atividades principais.
-   [x] Calcular a razão LTV/CAC (Lifetime Value / Customer Acquisition Cost) para empresas com modelo de recorrência.
-   [x] Identificar e categorizar as despesas discricionárias para possíveis cortes ou otimizações.
-   [x] Realizar uma projeção de caixa para os próximos 6-12 meses, considerando cenários otimista, realista e pessimista.

---

## Métricas de Referência

| Métrica                 | Benchmark Setor (Tecnologia/SaaS) | Benchmark Setor (Varejo) | Meta (Empresa XYZ) |
|-------------------------|-----------------------------------|--------------------------|--------------------|
| **Margem Líquida**      | 10% - 15%                         | 3% - 7%                  | > 12%              |
| **Liquidez Corrente**   | > 1.5x                            | > 1.2x                   | > 1.8x             |
| **Endividamento Geral** | < 0.60x                           | < 0.70x                  | < 0.50x            |
| **LTV/CAC**             | > 3:1                             | Não aplicável            | > 3.5:1            |
| **Ponto de Equilíbrio** | Conhecido e Monitorado Mensalmente | Conhecido e Monitorado Mensalmente | 15% abaixo da receita atual |
| **ROI**                 | > 15% para novos projetos         | > 10% para novos projetos | > 20%              |

---

## Erros Comuns

1.  **Ignorar a Sazonalidade dos Dados**: Analisar um único trimestre de forma isolada, sem considerar o contexto anual ou as flutuações sazonais do setor. Por exemplo, comparar o faturamento de dezembro (pico de vendas no varejo) com o de janeiro (período de baixa) sem ajuste, levará a conclusões errôneas sobre a saúde da receita. Para evitar, sempre compare períodos homólogos (ex: Q1 2023 vs Q1 2022) e utilize médias móveis.
2.  **Não Comparar com Benchmarks do Setor**: Avaliar métricas financeiras (ex: Margem Líquida de 5%) sem ter um ponto de referência setorial. Uma margem de 5% pode ser excelente para um supermercado, mas péssima para uma empresa de software. Para evitar, sempre pesquise e utilize benchmarks específicos para o setor e porte da empresa em análise.
3.  **Focar Apenas na Receita Bruta**: Celebrar o crescimento da receita sem analisar o impacto nos custos variáveis e nas despesas operacionais. Uma receita crescente acompanhada de custos e despesas que crescem ainda mais rápido pode resultar em prejuízo. Para evitar, sempre analise a rentabilidade (Margem Bruta, Margem Líquida) e o Ponto de Equilíbrio em conjunto com o crescimento da receita.

---

## Dicas Avançadas

1.  **Análise de Sensibilidade para o Ponto de Equilíbrio**: Não basta calcular o PE, é crucial entender como ele se altera com variações nos custos variáveis, preços de venda ou despesas fixas. Simule, por exemplo, o impacto de um aumento de 10% no custo da matéria-prima ou de uma redução de 5% no preço de venda no PE da empresa. Isso prepara para cenários adversos.
2.  **Cenarização de Fluxo de Caixa (What-If Analysis)**: Desenvolva projeções de fluxo de caixa para cenários otimista, realista e pessimista. Por exemplo, no cenário pessimista, projete uma queda de 20% nas vendas e um aumento de 10% nas despesas. Isso revela a robustez do caixa da empresa sob diferentes pressões e ajuda a planejar reservas ou linhas de crédito.
3.  **Análise da Alavancagem Operacional e Financeira**: Avalie como as mudanças na receita impactam o Lucro Operacional (alavancagem operacional) e o Lucro Líquido (alavancagem financeira). Empresas com alta alavancagem operacional (muitos custos fixos) têm grandes variações de lucro com pequenas variações de receita. Entender isso permite gerenciar riscos e oportunidades.
4.  **Integração da Análise Financeira com OKRs Estratégicos**: Conecte as métricas financeiras com os Objetivos e Resultados-Chave (OKRs) da empresa. Por exemplo, se um OKR é "Aumentar a participação de mercado em 15%", a análise financeira deve avaliar o CAC e o ROI das campanhas de aquisição para garantir que esse crescimento seja rentável e sustentável.
5.  **Análise de Ciclo de Conversão de Caixa (CCC)**: Para empresas com gestão de estoque e contas a receber/pagar complexas, calcule o CCC. `CCC = Dias de Estoque + Dias de Contas a Receber - Dias de Contas a Pagar`. Um CCC menor indica que a empresa está convertendo seus investimentos em caixa mais rapidamente, o que é um sinal de eficiência operacional e liquidez.