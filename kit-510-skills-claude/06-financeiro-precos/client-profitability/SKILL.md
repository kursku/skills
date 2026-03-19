---
name: client-profitability
description: "Client Profitability — Skill especializada para client profitability"
license: MIT
metadata:
  version: 1.0.0
  author: Cafe Code AI
  category: 06-financeiro-precos
  updated: 2026-03-01
---

# Client Profitability

Esta skill capacita o Claude a analisar, calcular e otimizar a lucratividade de clientes individuais e segmentos, fornecendo insights acionáveis para decisões estratégicas de precificação, alocação de recursos e retenção.

---

## Keywords

Rentabilidade do Cliente, LTV (Lifetime Value), CAC (Customer Acquisition Cost), Margem de Contribuição por Cliente, Segmentação por Lucratividade, ROI do Cliente, Custo de Servir Cliente (CTS), Precificação Dinâmica, Otimização de Portfólio de Clientes, Análise de Cohorte de Lucratividade, Churn de Clientes Lucrativos, Gestão de Portfólio.

---

## Quick Start

1.  **Coletar Dados Transacionais por Cliente**: Agrupar todas as receitas (vendas de produtos, serviços, taxas de licença) e custos diretos (custo do produto vendido, horas de serviço, comissões de venda, custos de aquisição) para cada cliente individual nos últimos 12 meses.
2.  **Calcular Margem de Contribuição Bruta por Cliente (MCC)**: Subtrair os custos diretos atribuíveis de cada cliente de sua receita total. Priorizar os 5 clientes com maior receita e os 5 com menor receita para esta análise inicial.
3.  **Identificar Clientes de Baixa Lucratividade**: Filtrar os clientes cuja MCC representa menos de 10% de sua receita total e listar os custos específicos que mais impactam negativamente sua rentabilidade.
4.  **Projetar LTV para Cliente Típico**: Utilizar dados históricos de retenção e receita média para estimar o Customer Lifetime Value (LTV) de um cliente novo na base, considerando um período de 3 anos.

---

## Core Workflows

### Workflow 1: Análise Detalhada da Lucratividade Individual do Cliente

Este workflow permite calcular a Margem de Contribuição por Cliente (MCC) e identificar os fatores que mais influenciam a rentabilidade de cada conta.

**Passos Detalhados:**

1.  **Agregação de Receitas por Cliente**: Consolidar todas as fontes de receita geradas por um cliente específico em um período definido (ex: anual). Isso inclui vendas de produtos/serviços, taxas de licença, contratos de manutenção, upgrades, etc.
    *   **Exemplo**: Para o cliente "TecnoSoluções Ltda." em 2023:
        *   Venda de Licença de Software Premium: R$ 80.000
        *   Contrato de Suporte e Manutenção (anual): R$ 15.000
        *   Horas de Consultoria para Implementação: R$ 25.000
        *   **Receita Total do Cliente**: R$ 120.000

2.  **Identificação e Alocação de Custos Diretos Atribuíveis**: Mapear e atribuir todos os custos diretamente relacionados à aquisição, serviço e retenção desse cliente.
    *   **Custo de Aquisição (CAC)**: Comissões de vendas, custos específicos de marketing direcionado ao cliente.
        *   **Exemplo**: Comissão de Venda (5% da licença): R$ 4.000; Campanha de prospecção digital focada: R$ 1.000. **CAC Total**: R$ 5.000.
    *   **Custo para Servir (CTS)**: Custos diretos do produto vendido (CPV), salários/horas de equipe de suporte técnico e consultores dedicados, licenças de ferramentas de terceiros utilizadas exclusivamente para o cliente, despesas de viagem.
        *   **Exemplo**: CPV da Licença: R$ 15.000; Salário/Horas de Consultor (50h x R$150/h): R$ 7.500; Salário/Horas de Suporte (20h x R$100/h): R$ 2.000; Licenças de software de terceiros para projeto específico: R$ 3.000; Despesas de viagem para reuniões: R$ 1.500. **CTS Total**: R$ 29.000.
    *   **Custo de Retenção**: Programas de fidelidade, brindes, eventos exclusivos.
        *   **Exemplo**: Participação em evento exclusivo para clientes VIP: R$ 1.000. **Custo de Retenção Total**: R$ 1.000.

3.  **Cálculo da Margem de Contribuição por Cliente (MCC)**:
    *   **Fórmula**: `MCC = Receita Total do Cliente - (CAC + CTS + Custo de Retenção)`
    *   **Exemplo para TecnoSoluções Ltda.**:
        *   MCC = R$ 120.000 - (R$ 5.000 + R$ 29.000 + R$ 1.000)
        *   MCC = R$ 120.000 - R$ 35.000
        *   **MCC = R$ 85.000**
    *   **Percentual da MCC sobre a Receita**: `(MCC / Receita Total) * 100%`
        *   Percentual = (R$ 85.000 / R$ 120.000) * 100% = **70,83%**

4.  **Análise e Interpretação**: Comparar a MCC com a média do portfólio de clientes e identificar clientes com MCC abaixo da média para investigar os custos excessivos ou oportunidades de precificação.

### Workflow 2: Segmentação de Clientes por Lucratividade e Estratégias Acionáveis

Este workflow foca em agrupar clientes com base em sua lucratividade e definir planos de ação específicos para cada segmento, otimizando o portfólio e a alocação de recursos.

**Passos Detalhados:**

1.  **Classificação dos Clientes por MCC Percentual**: Utilizar a Margem de Contribuição por Cliente (MCC) calculada no Workflow 1, expressa como percentual da receita, para categorizar os clientes.
    *   **Exemplo de Categorias (ajustáveis à realidade da empresa)**:
        *   **Clientes Estrela (Altíssima Lucratividade)**: MCC > 60%
        *   **Clientes Ouro (Alta Lucratividade)**: MCC entre 40% e 60%
        *   **Clientes Prata (Lucratividade Média)**: MCC entre 20% e 40%
        *   **Clientes Bronze (Baixa Lucratividade)**: MCC entre 5% e 20%
        *   **Clientes Desafio (Não-Lucrativos ou Prejuízo)**: MCC < 5%

2.  **Análise de LTV (Customer Lifetime Value) e CAC (Customer Acquisition Cost)**: Para cada segmento, calcular o LTV médio e o CAC médio para entender o potencial de longo prazo e o custo de entrada.
    *   **Fórmula LTV**: `(Receita Média por Transação x Número Médio de Transações por Ano x Vida Útil Média do Cliente em Anos) - Custo de Aquisição do Cliente`
    *   **Fórmula CAC**: `(Total de Custos de Vendas e Marketing para aquisição de novos clientes) / (Número de Novos Clientes Adquiridos)`
    *   **Fórmula LTV:CAC Ratio**: `LTV / CAC` (Um LTV:CAC de 3:1 é geralmente considerado saudável).
    *   **Exemplo**:
        *   **Segmento "Clientes Ouro"**: LTV médio R$ 250.000, CAC médio R$ 15.000. LTV:CAC Ratio = 16.6:1 (Excelente).
        *   **Segmento "Clientes Bronze"**: LTV médio R$ 30.000, CAC médio R$ 10.000. LTV:CAC Ratio = 3:1 (Aceitável).

3.  **Definição de Estratégias por Segmento**: Elaborar planos de ação específicos para otimizar a rentabilidade de cada grupo.

    *   **Clientes Estrela/Ouro**:
        *   **Estratégia**: Retenção premium, programas de fidelidade, ofertas de up-sell/cross-sell de alto valor, co-criação de soluções, tratamento VIP.
        *   **Exemplo**: Oferecer acesso antecipado a novas funcionalidades, consultoria estratégica proativa, descontos exclusivos em eventos da indústria, alocação de um gerente de contas sênior.

    *   **Clientes Prata**:
        *   **Estratégia**: Otimização de custos de serviço, identificação de oportunidades de up-sell/cross-sell de produtos de margem média, automação de processos de atendimento.
        *   **Exemplo**: Incentivar a adoção de portais de autoatendimento, oferecer pacotes de serviços complementares, revisar a estrutura de preços de serviços adicionais.

    *   **Clientes Bronze**:
        *   **Estratégia**: Análise aprofundada dos custos de serviço (CTS), renegociação de termos contratuais, aumento de preços, ou migração para produtos/serviços de menor custo e automação.
        *   **Exemplo**: Implementar uma estrutura de preços por volume para serviços, automatizar o suporte de primeiro nível, ou oferecer um pacote de serviço mais básico com preço reduzido.

    *   **Clientes Desafio**:
        *   **Estratégia**: Investigação da causa raiz do prejuízo, tentativa de renegociação ou otimização radical, e, se inviável, plano de desativação gradual ou redirecionamento para parceiros.
        *   **Exemplo**: Analisar se o cliente exige um nível de serviço desproporcional, propor renegociação de contrato com aumento de preço ou remoção de serviços não essenciais, ou iniciar um processo de transição para um provedor alternativo se a rentabilidade não puder ser recuperada.

4.  **Monitoramento Contínuo**: Estabelecer um ciclo de revisão trimestral da lucratividade dos clientes e ajustar as estratégias conforme necessário.

---

## Templates

### Template: Planilha de Análise de Lucratividade por Cliente (MCC)

```
| Cliente             | Receita Total (R$) | Custo de Aquisição (R$) | Custo para Servir (CTS) (R$) | Custo de Retenção (R$) | MCC (R$) | %MCC sobre Receita | LTV (R$) | CAC (R$) | LTV:CAC Ratio |
|---------------------|--------------------|-------------------------|------------------------------|------------------------|----------|--------------------|----------|----------|---------------|
| Alpha Consultoria   | 150.000            | 8.000                   | 30.000                       | 2.000                  | 110.000  | 73,33%             | 450.000  | 8.000    | 56,25:1       |
| Beta Engenharia     | 80.000             | 5.000                   | 25.000                       | 1.000                  | 49.000   | 61,25%             | 200.000  | 5.000    | 40:1          |
| Gama Logística      | 40.000             | 3.000                   | 18.000                       | 500                    | 18.500   | 46,25%             | 75.000   | 3.000    | 25:1          |
| Delta Comércio      | 25.000             | 2.500                   | 15.000                       | 800                    | 6.700    | 26,80%             | 40.000   | 2.500    | 16:1          |
| Épsilon Serviços    | 15.000             | 1.500                   | 12.000                       | 300                    | 1.200    | 8,00%              | 20.000   | 1.500    | 13,33:1       |
```

### Template: Projeção Simplificada de LTV (Customer Lifetime Value)

```
Projeção de LTV para Cliente Tipo "Pequena Empresa" (SaaS)

| Variável                                     | Valor Exemplo | Unidade/Descrição                               |
|----------------------------------------------|---------------|-------------------------------------------------|
| Receita Média Mensal por Cliente (ARPU)      | R$ 500        | Assinatura mensal do software                   |
| Taxa de Churn Mensal                         | 2%            | Percentual de clientes que cancelam por mês     |
| Vida Útil Média do Cliente (1/Churn Rate)    | 50            | Meses (1/0.02)                                  |
| Custo de Aquisição por Cliente (CAC)         | R$ 1.500      | Custo total para adquirir um novo cliente       |
|                                              |               |                                                 |
| **Cálculo de LTV:**                          |               |                                                 |
| LTV Bruto = ARPU * Vida Útil Média           | R$ 25.000     | R$ 500/mês * 50 meses                           |
| LTV Líquido = LTV Bruto - CAC                | R$ 23.500     | R$ 25.000 - R$ 1.500                            |
```

---

## Checklist

- [ ] Coletar *todas* as fontes de receita (produtos, serviços, taxas, upgrades) para cada cliente individualmente nos últimos 12 meses.
- [ ] Mapear e atribuir *todos* os custos diretos de aquisição (comissão, marketing específico), serviço (CPV, horas de suporte/consultoria) e retenção (brindes, eventos) a cada cliente.
- [ ] Calcular a Margem de Contribuição por Cliente (MCC) para, no mínimo, os 20% clientes de maior receita e os 20% de menor receita.
- [ ] Segmentar a base de clientes em grupos de alta, média e baixa lucratividade com base na MCC percentual.
- [ ] Calcular o LTV (Customer Lifetime Value) e o CAC (Customer Acquisition Cost) médios para cada segmento de clientes.
- [ ] Analisar o LTV:CAC Ratio para cada segmento, identificando aqueles com proporção abaixo de 3:1.
- [ ] Desenvolver estratégias específicas de retenção, up-sell, otimização de custos ou renegociação para cada segmento de lucratividade.
- [ ] Revisar a política de descontos e termos de pagamento, garantindo que não comprometam a MCC dos clientes.
- [ ] Mapear o tempo gasto pela equipe de atendimento, suporte e vendas em clientes específicos e correlacionar com a lucratividade.
- [ ] Estabelecer um ciclo de revisão trimestral da lucratividade do cliente e ajustar as ações estratégicas.

---

## Métricas de Referência

| Métrica                         | Benchmark (Exemplo SaaS B2B) | Meta (Exemplo SaaS B2B)   |
|---------------------------------|------------------------------|---------------------------|
| Margem de Contribuição Cliente  | > 40% da receita do cliente  | > 60% da receita do cliente |
| LTV:CAC Ratio                   | 3:1 a 5:1                    | > 7:1                     |
| Custo para Servir (CTS)         | < 15% da receita do cliente  | < 10% da receita do cliente |
| Churn Rate de Clientes Lucrativos | < 0.5% ao mês                | < 0.2% ao mês             |
| Payback Period do CAC           | < 12 meses                   | < 6 meses                 |

---

## Erros Comuns

1.  **Ignorar custos indiretos na análise de cliente**: Muitas empresas focam apenas nos custos variáveis diretos, esquecendo de alocar custos indiretos (como parte do aluguel do escritório, despesas administrativas) que, embora não diretamente atribuíveis, são consumidos pelos clientes. Isso superestima a MCC real.
    *   **Como evitar**: Desenvolver um modelo de custeio por atividade (Activity-Based Costing - ABC) para alocar custos indiretos de forma mais precisa, mesmo que simplificada, aos clientes. Por exemplo, alocar custos de infraestrutura de TI com base no número de usuários ou volume de dados por cliente.
2.  **Focar apenas na receita total e não na lucratividade**: Celebrar grandes contratos sem analisar o custo real para servir esses clientes pode levar a "clientes pesadelo" que consomem recursos desproporcionalmente, gerando prejuízo.
    *   **Como evitar**: Integrar a análise de MCC e LTV:CAC Ratio em todas as propostas de novos negócios e renovações de contrato. Antes de fechar um grande negócio, simular sua MCC projetada e o impacto no custo de servir a carteira.
3.  **Não segmentar clientes após a análise**: Obter os dados de lucratividade sem agir sobre eles é um esforço perdido. Tratar todos os clientes da mesma forma, independentemente de sua rentabilidade, desperdiça recursos em clientes de baixa margem e subvaloriza os clientes mais lucrativos.
    *   **Como evitar**: Criar planos de ação específicos para cada segmento de lucratividade (Clientes Estrela, Ouro, Prata, Bronze, Desafio), alocando recursos de marketing, vendas e atendimento de forma diferenciada. Implementar um CRM que permita essa segmentação e rastreamento de ações.

---

## Dicas Avançadas

1.  **Implementar Precificação Baseada em Valor Percebido por Segmento**: Em vez de apenas custo-plus, ajuste a precificação para clientes de alta lucratividade com base no valor que eles derivam de seus produtos/serviços, permitindo capturar uma fatia maior desse valor. Para clientes de menor lucratividade, considere modelos de precificação mais eficientes ou em camadas.
    *   **Exemplo**: Clientes do segmento "Estrela" podem aceitar um preço premium para um serviço de consultoria estratégica que lhes garante um ROI elevado, enquanto clientes "Prata" podem preferir um pacote mais acessível de suporte técnico.
2.  **Desenvolver um "Customer Profitability Index (CPI)"**: Crie um índice composto que combine MCC, LTV, e potencial de crescimento futuro do cliente. Isso oferece uma visão mais holística do valor do cliente, além da rentabilidade atual.
    *   **Exemplo**: `CPI = (MCC % * 0.4) + (LTV:CAC Ratio * 0.3) + (Potencial de Crescimento * 0.3)`. Clientes com CPI alto recebem mais investimento.
3.  **Otimização do Portfólio de Produtos/Serviços com Base na Lucratividade do Cliente**: Analise quais produtos ou serviços são consistentemente comprados pelos clientes mais lucrativos e quais são os preferidos pelos clientes menos lucrativos. Direcione o desenvolvimento e marketing para ofertas que atraem e retêm clientes de alto valor.
    *   **Exemplo**: Se clientes "Estrela" sempre compram a "Licença Premium + Módulo X", enquanto clientes "Desafio" só compram a "Licença Básica", considere aprimorar o "Módulo X" e reavaliar a oferta básica.
4.  **Alocação de Recursos de Equipe (Vendas, Suporte, Sucesso do Cliente) por Lucratividade Projetada**: Direcione os melhores talentos e maior tempo de dedicação para os clientes com maior LTV e MCC potencial. Evite que as equipes de alto custo gastem tempo excessivo com clientes de baixa rentabilidade.
    *   **Exemplo**: Alocar Account Managers sêniores para clientes "Estrela" e "Ouro", enquanto clientes "Bronze" são atendidos por suporte automatizado e equipes júnior, com escalonamento apenas para problemas críticos.
5.  **Análise de Coorte de Lucratividade**: Agrupe clientes por sua data de aquisição (coortes) e monitore a evolução de sua MCC e LTV ao longo do tempo. Isso revela tendências de lucratividade por safra de clientes e permite ajustar as estratégias de aquisição e retenção.
    *   **Exemplo**: Observar que a coorte de clientes adquiridos no Q1/2022 tem uma MCC média 15% maior após 18 meses do que a coorte do Q3/2022, indicando uma mudança na qualidade dos leads ou no processo de onboarding que precisa ser investigada.
---