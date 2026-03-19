---
name: pricing-calculator
description: "Pricing Calculator — Skill especializada para pricing calculator"
license: MIT
metadata:
  version: 1.0.0
  author: Cafe Code AI
  category: 06-financeiro-precos
  updated: 2026-03-01
---

# Pricing Calculator

Esta skill capacita o Claude a desenvolver e validar modelos de precificação robustos, calcular rentabilidade e projetar cenários financeiros para produtos e serviços, utilizando fórmulas e templates práticos.

---

## Keywords

precificação, cálculo de preços, margem de lucro, markup, ponto de equilíbrio, ROI, LTV, CAC, análise de custos, estratégia de preços, modelo de precificação, projeção financeira, break-even.

---

## Quick Start

1.  Listar e categorizar todos os custos diretos e indiretos associados ao produto ou serviço a ser precificado.
2.  Aplicar uma taxa de Markup de 50% sobre o custo total unitário para definir um preço de venda inicial.
3.  Calcular a Margem de Lucro Bruta esperada com base nesse preço e custo, verificando a sustentabilidade.
4.  Simular o Ponto de Equilíbrio em unidades e valor financeiro, considerando os custos fixos mensais.
5.  Ajustar o preço com base em uma pesquisa rápida de preços de concorrentes diretos e valor percebido pelo cliente no mercado.

---

## Core Workflows

### Workflow 1: Desenvolvimento de Modelo de Precificação por Custo Mais Markup

Este workflow guia a criação de um preço de venda inicial baseado nos custos do produto ou serviço, adicionando uma margem de lucro desejada através do markup.

1.  **Identificar e Categorizar Custos Detalhados**:
    *   **Custos Diretos (CV)**: Matéria-prima, mão de obra direta de produção, embalagens, comissões de venda.
        *   Exemplo: Para um software SaaS: Salário do desenvolvedor por hora de recurso implementado (R$ 50/hora), licenças de bibliotecas por usuário (R$ 5/usuário/mês), custo de infraestrutura por usuário (R$ 2/usuário/mês).
    *   **Custos Indiretos (CF)**: Aluguel de escritório, salários administrativos, marketing, seguros, depreciação de equipamentos.
        *   Exemplo: Aluguel mensal de R$ 3.000, salário do gerente de projeto R$ 6.000, custo de marketing digital R$ 1.000.
    *   **Custo Total Fixo Mensal**: Soma de todos os custos indiretos fixos (CF).
        *   Exemplo: R$ 3.000 (aluguel) + R$ 6.000 (gerente) + R$ 1.000 (marketing) = R$ 10.000/mês.
    *   **Custo Variável Unitário (CVU)**: Soma dos custos diretos por unidade de produto/serviço.
        *   Exemplo: Para um plano de software SaaS com 10 horas de desenvolvimento inicial e licenças/infra para 1 usuário: (10h * R$ 50/h) + R$ 5 (licença) + R$ 2 (infra) = R$ 507/usuário inicial.

2.  **Calcular o Custo Unitário Total (CUT)**:
    *   Para produtos/serviços com volume de produção definido, o CUT é (Custos Fixos Totais / Volume de Produção) + Custo Variável Unitário.
    *   Para serviços com volume variável, é mais comum focar no Custo Variável Unitário para a precificação direta, e usar os Custos Fixos para o Ponto de Equilíbrio.
    *   Exemplo (para um software SaaS, focando no CVU inicial): R$ 507 por usuário inicial.

3.  **Definir a Taxa de Markup Desejada**:
    *   O markup é um percentual aplicado sobre o custo para obter o preço de venda. Ele deve cobrir os custos e gerar lucro.
    *   Exemplo: Definir um Markup de 60% para um software SaaS, visando um bom retorno sobre o investimento e cobrindo os custos indiretos.

4.  **Aplicar a Fórmula do Preço de Venda**:
    *   `Preço de Venda = Custo Unitário Total * (1 + Taxa de Markup)`
    *   Exemplo: `R$ 507 * (1 + 0.60) = R$ 507 * 1.60 = R$ 811.20` (Preço de Venda Inicial Sugerido para o plano SaaS).

5.  **Validar a Margem de Lucro Bruta**:
    *   `Margem de Lucro Bruta (%) = ((Preço de Venda - Custo Unitário Total) / Preço de Venda) * 100`
    *   Exemplo: `((R$ 811.20 - R$ 507) / R$ 811.20) * 100 = (R$ 304.20 / R$ 811.20) * 100 = 37.5%` (Margem de Lucro Bruta).

### Workflow 2: Análise de Rentabilidade e Ponto de Equilíbrio

Este workflow foca em determinar quantas unidades (ou qual volume de vendas) são necessárias para cobrir os custos e começar a gerar lucro.

1.  **Listar Custos Fixos Totais Mensais (CF)**:
    *   Consolide todos os custos que não variam com o volume de produção ou vendas em um mês.
    *   Exemplo: Aluguel de R$ 3.000, salários administrativos fixos R$ 12.000, licenças de software de gestão R$ 500, marketing institucional R$ 1.500. Total CF = R$ 17.000/mês.

2.  **Determinar o Preço de Venda Unitário (PVU) e Custo Variável Unitário (CVU)**:
    *   Utilize o preço de venda calculado no Workflow 1 e o custo variável unitário.
    *   Exemplo: PVU = R$ 811.20 (para o plano SaaS), CVU = R$ 507 (para o plano SaaS).

3.  **Calcular a Margem de Contribuição Unitária (MCU)**:
    *   A MCU é o valor que cada unidade vendida contribui para cobrir os custos fixos e gerar lucro.
    *   `MCU = Preço de Venda Unitário - Custo Variável Unitário`
    *   Exemplo: `R$ 811.20 - R$ 507 = R$ 304.20` por plano SaaS vendido.

4.  **Calcular o Ponto de Equilíbrio em Unidades (PEu)**:
    *   O PEu indica quantas unidades precisam ser vendidas para que a receita total seja igual aos custos totais (lucro zero).
    *   `PEu = Custos Fixos Totais / Margem de Contribuição Unitária`
    *   Exemplo: `R$ 17.000 / R$ 304.20 = 55.88`, arredondando para 56 planos SaaS por mês.

5.  **Calcular o Ponto de Equilíbrio em Valor (PEv)**:
    *   O PEv indica a receita total necessária para cobrir todos os custos.
    *   `PEv = Ponto de Equilíbrio em Unidades * Preço de Venda Unitário`
    *   `PEv = Custos Fixos Totais / (Margem de Contribuição Unitária / Preço de Venda Unitário)` (ou CF / %MC)
    *   Exemplo: `56 planos * R$ 811.20 = R$ 45.427.20` ou `R$ 17.000 / (R$ 304.20 / R$ 811.20) = R$ 17.000 / 0.375 = R$ 45.333.33` (diferença por arredondamento).

6.  **Projetar Cenários para Atingir o Lucro Desejado**:
    *   Para determinar quantas unidades vender para atingir um lucro específico.
    *   `Unidades para Lucro Desejado = (Custos Fixos Totais + Lucro Desejado) / Margem de Contribuição Unitária`
    *   Exemplo: Para um lucro desejado de R$ 10.000/mês: `(R$ 17.000 + R$ 10.000) / R$ 304.20 = R$ 27.000 / R$ 304.20 = 88.75`, arredondando para 89 planos SaaS por mês.

---

## Templates

### Template de Análise de Custos Unitários de Produto/Serviço

```
### Análise de Custos Unitários - Produto: Software SaaS - Plano Essencial

**1. Custos Variáveis Unitários (CVU)**
| Item de Custo Variável | Descrição | Valor Unitário (R$) |
|-------------------------|-----------|---------------------|
| Mão de Obra Direta      | 10 horas desenvolvimento inicial | 500.00 (10h * R$50/h) |
| Licença de Bibliotecas  | Por usuário/mês | 5.00 |
| Infraestrutura Cloud    | Por usuário/mês | 2.00 |
| Suporte ao Cliente      | 0.5 hora por usuário/mês | 25.00 (0.5h * R$50/h) |
| **Total CVU**           |           | **532.00**          |

**2. Custos Fixos Mensais (CF)**
| Item de Custo Fixo | Descrição | Valor Mensal (R$) |
|--------------------|-----------|-------------------|
| Aluguel Escritório | Proporcional ao produto | 3,000.00 |
| Salários Adm/Vendas | Proporcional ao produto | 12,000.00 |
| Marketing Institucional | Campanhas de branding | 1,500.00 |
| Licenças Software Gestão | CRM, ERP | 500.00 |
| **Total CF**       |           | **17,000.00**     |

**Resumo de Custos:**
*   **Custo Variável Unitário (CVU): R$ 532.00**
*   **Custo Fixo Mensal (CF): R$ 17,000.00**
```

### Template de Projeção de Precificação e Rentabilidade

```
### Projeção de Precificação e Rentabilidade - Produto: Software SaaS - Plano Essencial

**Dados de Entrada:**
*   Custo Variável Unitário (CVU): R$ 532.00
*   Custos Fixos Mensais (CF): R$ 17,000.00
*   Taxa de Markup Desejada: 60%
*   Lucro Mensal Desejado: R$ 10,000.00

**Cálculos de Precificação:**
*   **Preço de Venda Sugerido (PVS):**
    *   PVS = CVU * (1 + Markup)
    *   PVS = R$ 532.00 * (1 + 0.60) = R$ 851.20
*   **Margem de Lucro Bruta (%):**
    *   Margem = ((PVS - CVU) / PVS) * 100
    *   Margem = ((R$ 851.20 - R$ 532.00) / R$ 851.20) * 100 = 37.50%

**Cálculos de Rentabilidade:**
*   **Margem de Contribuição Unitária (MCU):**
    *   MCU = PVS - CVU
    *   MCU = R$ 851.20 - R$ 532.00 = R$ 319.20
*   **Ponto de Equilíbrio em Unidades (PEu):**
    *   PEu = CF / MCU
    *   PEu = R$ 17,000.00 / R$ 319.20 = 53.26 => **54 unidades/mês**
*   **Ponto de Equilíbrio em Valor (PEv):**
    *   PEv = PEu * PVS
    *   PEv = 54 * R$ 851.20 = **R$ 45,964.80/mês**
*   **Unidades para Lucro Desejado (ULD):**
    *   ULD = (CF + Lucro Desejado) / MCU
    *   ULD = (R$ 17,000.00 + R$ 10,000.00) / R$ 319.20 = 84.58 => **85 unidades/mês**
```

---

## Checklist

- [x] Todos os custos diretos do produto/serviço estão identificados e quantificados por unidade?
- [x] Os custos indiretos e fixos foram levantados e alocados corretamente ao período de análise?
- [x] A taxa de markup ou margem de lucro bruta desejada foi definida e justificada pelas metas financeiras?
- [x] O preço de venda calculado é competitivo e alinhado com o valor percebido pelo cliente no mercado?
- [x] O ponto de equilíbrio em unidades e valor financeiro foi calculado para o período (mensal/trimestral)?
- [x] A sensibilidade do preço a variações nos custos (matéria-prima, mão de obra) e no volume de vendas foi simulada?
- [x] O LTV (Lifetime Value) e o CAC (Custo de Aquisição de Cliente) foram analisados para precificação de modelos de assinatura?
- [x] O modelo de precificação considera diferentes tiers, pacotes ou estratégias para descontos e promoções sazonais?
- [x] Existe um plano claro para a revisão periódica da estratégia de precificação, considerando mudanças de mercado e custos?
- [x] A estrutura de preços reflete a estratégia de posicionamento da marca (premium, valor, econômico)?

---

## Métricas de Referência

| Métrica | Benchmark | Meta |
|---------------------------|----------------------------------|----------------|
| Markup Bruto | 30% - 150% (setor de serviços/varejo) | 60% (para SaaS) |
| Margem de Lucro Bruta | 25% - 70% (indústria/serviços) | 45% (para SaaS) |
| Ponto de Equilíbrio (tempo) | 6-24 meses (startups) | 12 meses |
| LTV/CAC Ratio | > 3:1 (bom) | 4:1 |
| % Custo Variável sobre Receita | < 50% | 40% |
| ROI (Retorno sobre Investimento) | > 20% (bom) | 30% |

---

## Erros Comuns

1.  **Ignorar custos indiretos na formação do preço**: Muitas empresas focam apenas nos custos diretos, subestimando o custo real do produto/serviço.
    *   **Como evitar com exemplo**: Ao precificar um serviço de consultoria, além das horas do consultor (custo direto), aloque uma parcela proporcional do aluguel do escritório, salários da equipe de suporte e licenças de software de gestão (custos indiretos). Utilize o Template de Análise de Custos Unitários para garantir que todos os custos sejam contabilizados.

2.  **Precificar apenas pelo custo sem considerar o valor de mercado ou concorrência**: Isso pode levar a preços muito altos (perdendo clientes) ou muito baixos (deixando dinheiro na mesa).
    *   **Como evitar com exemplo**: Antes de definir o preço final de um novo aplicativo de produtividade, pesquise o preço de 3-5 concorrentes diretos, analise suas funcionalidades e o valor percebido que seu aplicativo entrega (ex: economia de X horas por semana ao usuário). Se o custo sugere R$50/mês, mas o mercado aceita R$80/mês por funcionalidades similares ou superiores, ajuste o preço para R$75/mês para capturar mais valor.

3.  **Não simular cenários de volume de vendas**: Definir um preço sem projetar quantos produtos ou serviços precisam ser vendidos para cobrir os custos e gerar lucro desejado.
    *   **Como evitar com exemplo**: Para um produto com custo fixo mensal de R$10.000 e margem de contribuição unitária de R$50, calcular que são necessárias 200 unidades vendidas para o ponto de equilíbrio. Em seguida, projete que para um lucro de R$5.000, 300 unidades são necessárias. Se o plano de marketing só prevê 150 vendas, o preço ou os custos precisam ser revistos.

---

## Dicas Avançadas

1.  **Implementar Precificação Baseada em Valor (Value-Based Pricing)**: Em vez de focar nos custos internos, precifique com base no valor percebido ou no benefício econômico que seu produto/serviço gera para o cliente.
    *   **Exemplo**: Um sistema de automação que economiza R$ 5.000/mês em mão de obra para uma empresa pode ser precificado em R$ 1.500/mês, pois o cliente ainda obtém um benefício líquido de R$ 3.500/mês, gerando um alto ROI para ele, independentemente do seu custo de desenvolvimento.

2.  **Utilizar Precificação Dinâmica em Ambientes Online**: Ajuste os preços em tempo real com base em algoritmos que consideram demanda, estoque, preços da concorrência, horário e histórico de navegação do usuário.
    *   **Exemplo**: Um e-commerce de passagens aéreas que aumenta os preços para voos em horários de pico ou quando a disponibilidade de assentos está baixa, ou uma loja online que oferece um desconto personalizado a um cliente que abandonou o carrinho de compras.

3.  **Realizar Análise de Elasticidade de Preço**: Medir como a demanda do seu produto ou serviço reage a mudanças no preço. Isso ajuda a encontrar o ponto de preço que maximiza a receita ou o lucro.
    *   **Exemplo**: Conduzir testes A/B com diferentes grupos de clientes, oferecendo o mesmo produto a R$100 e R$120. Se a queda na demanda pelo preço mais alto for mínima e o aumento da receita for significativo, o preço de R$120 pode ser mais vantajoso, indicando baixa elasticidade.

4.  **Desenvolver Modelos de Precificação SaaS (Software as a Service) com Tiers e Recursos Variáveis**: Oferecer diferentes pacotes (planos Básico, Pro, Enterprise) com funcionalidades, limites de uso (usuários, armazenamento, transações) e níveis de suporte escalonados.
    *   **Exemplo**: Um plano "Básico" a R$ 99/mês para até 5 usuários com 1GB de armazenamento; um plano "Pro" a R$ 299/mês para até 20 usuários com 10GB e suporte prioritário; e um plano "Enterprise" com preço personalizado para grandes corporações com funcionalidades avançadas e suporte 24/7.

5.  **Considerar o Ciclo de Vida do Produto na Estratégia de Preços**: As fases de introdução, crescimento, maturidade e declínio de um produto exigem abordagens de precificação distintas para otimizar o desempenho.
    *   **Exemplo**: Na fase de introdução de um novo gadget, usar um preço de penetração baixo para ganhar mercado rapidamente. No crescimento, aumentar o preço à medida que a demanda e o reconhecimento da marca crescem. Na maturidade, manter preços competitivos com foco em promoções. No declínio, reduzir os preços para liquidar estoque.