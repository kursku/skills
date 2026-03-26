---
name: acquisition-channel-ranking
description: "Acquisition Channel Ranking — Skill especializada para acquisition channel ranking"
license: MIT
metadata:
  version: 1.0.0
  author: Cafe Code AI
  category: 08-lancamento-growth
  updated: 2026-03-01
risk: safe
---

# Acquisition Channel Ranking

Esta skill capacita o Claude a identificar, analisar e priorizar canais de aquisição de clientes com base em seu desempenho real, potencial de escala e retorno sobre o investimento (LTV/CAC).

---

## Keywords

LTV/CAC, CPA, ROAS, Payback Period, Atribuição Multitoque, Canais Pagos, Canais Orgânicos, Funil de Aquisição, Growth Hacking, Otimização de Canais, Modelagem de Atribuição, Custo por Lead (CPL), Retenção de Clientes, Cohort Analysis.

---

## Quick Start

1.  **Consolide Dados de Custo e Conversão:** Agregue o investimento total e o número de aquisições (clientes pagantes) para cada canal de marketing ativo (e.g., Google Ads, Meta Ads, SEO, Email Marketing) nos últimos 3-6 meses.
2.  **Calcule LTV Estimado por Canal:** Determine o Lifetime Value (LTV) médio dos clientes para cada canal, considerando ticket médio, frequência de compra e taxa de churn. Exemplo: Clientes de SEO têm LTV médio de R$ 800, enquanto de Meta Ads têm LTV de R$ 550.
3.  **Calcule CAC por Canal:** Divida o investimento total de cada canal pelo número de clientes adquiridos por ele, utilizando um modelo de atribuição consistente (e.g., Linear ou Ponderado por Posição).
4.  **Determine o Ratio LTV/CAC:** Calcule a relação LTV/CAC para cada canal. Priorize os canais com LTV/CAC > 3, indicando viabilidade e potencial de lucro.
5.  **Identifique Top 3 Canais:** Com base no LTV/CAC e potencial de escala, selecione os três canais mais promissores para focar esforços e investimento.

---

## Core Workflows

### Workflow 1: Modelagem de Atribuição e Cálculo Preciso de LTV/CAC Ponderado

Este workflow detalha a metodologia para calcular o LTV/CAC de forma mais precisa, considerando a jornada do cliente e não apenas o último ponto de contato.

**Passo 1: Seleção e Implementação de um Modelo de Atribuição Avançado**
*   **Ação:** Abandone o modelo de "Último Clique" para focar em modelos que distribuam crédito por múltiplos pontos de contato. Modelos como "Linear", "Baseado em Posição" (First/Last Click com ponderação central) ou "Time Decay" são mais adequados.
*   **Ferramentas:** Configure o modelo de atribuição no Google Analytics 4 (GA4) ou em uma ferramenta de atribuição de terceiros (e.g., Mixpanel, Segment, HubSpot).
*   **Exemplo:** Para um SaaS B2B, um cliente pode ter visto um anúncio no LinkedIn (1º toque), lido um artigo de blog via busca orgânica (2º toque), participado de um webinar (3º toque) e, por fim, clicado em um email de follow-up para assinar (4º toque). Com um modelo Linear, cada toque recebe 25% do crédito pela conversão. Se o LTV desse cliente for R$ 3.000, cada canal recebe R$ 750 em valor atribuído.

**Passo 2: Coleta e Consolidação de Dados Agregados por Canal**
*   **Ação:** Reúna dados de investimento, volume de leads/MQLs/SQLs e aquisições (clientes pagantes) de cada plataforma. Importante incluir custos indiretos (salários da equipe de marketing, licenças de ferramentas).
*   **Fontes de Dados:** Google Ads, Meta Ads (Facebook/Instagram), LinkedIn Ads, Google Analytics, CRM (Salesforce, HubSpot), Ferramentas de Automação de Marketing (RD Station, ActiveCampaign).
*   **Exemplo:**
    *   **Google Ads:** Investimento: R$ 12.000, Clientes: 150 (atribuídos pelo modelo).
    *   **Meta Ads:** Investimento: R$ 8.000, Clientes: 100 (atribuídos pelo modelo).
    *   **SEO:** Investimento: R$ 5.000 (custo de conteúdo, otimização), Clientes: 200 (atribuídos pelo modelo).
    *   **Email Marketing:** Investimento: R$ 1.500 (ferramenta, tempo), Clientes: 75 (atribuídos pelo modelo).

**Passo 3: Cálculo do CAC Ponderado por Canal**
*   **Ação:** Utilize os clientes atribuídos pelo modelo de atribuição para calcular o CAC.
*   **Fórmula:** `CAC = (Investimento Total do Canal + Custos Indiretos Atribuídos) / Clientes Atribuídos pelo Modelo`
*   **Exemplo:**
    *   **Google Ads:** R$ 12.000 / 150 Clientes = R$ 80,00 CAC.
    *   **Meta Ads:** R$ 8.000 / 100 Clientes = R$ 80,00 CAC.
    *   **SEO:** R$ 5.000 / 200 Clientes = R$ 25,00 CAC.
    *   **Email Marketing:** R$ 1.500 / 75 Clientes = R$ 20,00 CAC.

**Passo 4: Cálculo do LTV Segmentado por Canal**
*   **Ação:** O LTV pode variar significativamente dependendo do canal de aquisição. Calcule o LTV médio para clientes que tiveram seu primeiro contato ou principal atribuição de valor via um canal específico.
*   **Fórmula (simplificada):** `LTV = (Ticket Médio x Frequência de Compra Anual x Vida Útil do Cliente em Anos) - Custos de Manutenção`
*   **Exemplo:**
    *   **Google Ads:** Clientes do Google Ads tendem a ter um ticket médio de R$ 150/mês e churn de 5% ao mês. LTV estimado: R$ 2.850.
    *   **Meta Ads:** Clientes de Meta Ads, ticket médio de R$ 120/mês e churn de 7% ao mês. LTV estimado: R$ 1.714.
    *   **SEO:** Clientes de SEO, ticket médio de R$ 180/mês e churn de 3% ao mês. LTV estimado: R$ 5.820.
    *   **Email Marketing:** Clientes de Email, ticket médio de R$ 160/mês e churn de 4% ao mês. LTV estimado: R$ 3.840.

**Passo 5: Geração do Ranking LTV/CAC e Análise de Rentabilidade**
*   **Ação:** Compile os dados em uma tabela e calcule o LTV/CAC para cada canal. Priorize os canais com os maiores ratios.
*   **Exemplo de Tabela Final:**

| Canal             | Investimento Mensal (R$) | Clientes Atribuídos | CAC (R$) | LTV Estimado (R$) | LTV/CAC |
| :---------------- | :----------------------- | :------------------ | :------- | :---------------- | :------ |
| SEO               | 5.000                    | 200                 | 25       | 5.820             | 232,8   |
| Email Marketing   | 1.500                    | 75                  | 20       | 3.840             | 192,0   |
| Google Ads        | 12.000                   | 150                 | 80       | 2.850             | 35,6    |
| Meta Ads          | 8.000                    | 100                 | 80       | 1.714             | 21,4    |

*   **Conclusão:** SEO e Email Marketing são os canais mais rentáveis, com um LTV/CAC significativamente superior. Google Ads e Meta Ads são viáveis, mas com margens menores, exigindo otimização contínua.

### Workflow 2: Otimização e Alocação Estratégica de Orçamento com Base no Ranking

Este workflow foca em como usar o ranking de canais para otimizar a alocação de orçamento e planejar testes de escala.

**Passo 1: Análise de Potencial de Escala dos Canais Top-Ranked**
*   **Ação:** Para os canais com LTV/CAC mais alto, avalie o potencial de escalar o volume de aquisição sem degradar a rentabilidade. Considere o tamanho do mercado endereçável, saturação do canal e capacidade operacional.
*   **Exemplo:** Para SEO, apesar do LTV/CAC altíssimo, a escalabilidade é limitada pela demanda de busca e tempo de ranqueamento. Para Email Marketing, a escalabilidade depende do volume de leads qualificados gerados por outros canais ou parcerias. Google Ads, embora com menor LTV/CAC, oferece alta escalabilidade via aumento de lances e expansão de palavras-chave.

**Passo 2: Planejamento de Testes de Alocação e Otimização**
*   **Ação:** Defina experimentos para aumentar o investimento nos canais de melhor desempenho e/ou otimizar os canais intermediários.
*   **Exemplo:**
    *   **SEO:** Investir 30% a mais em produção de conteúdo de cauda longa para termos com alto volume e baixa concorrência, visando aumentar o tráfego orgânico qualificado em 15% nos próximos 6 meses.
    *   **Email Marketing:** Criar uma sequência de automação de 3 emails pós-conversão para clientes de outros canais, visando upsell e cross-sell, com meta de aumentar o LTV em 10% para essas coortes.
    *   **Google Ads:** Realizar teste A/B em lances e criativos para campanhas de fundo de funil, visando reduzir o CAC em 10% mantendo o volume.
    *   **Meta Ads:** Segmentar audiências lookalike com base nos "top 10% LTV clientes" para tentar replicar o perfil de clientes de maior valor, com meta de aumentar o LTV médio do canal em 5%.

**Passo 3: Estabelecimento de Critérios de Sucesso e Falha para Testes**
*   **Ação:** Antes de iniciar qualquer teste, defina claramente os KPIs que determinarão se o experimento foi bem-sucedido ou não.
*   **Exemplo:**
    *   **Teste Google Ads:** Critério de sucesso: Redução do CAC em 10% ou aumento do LTV/CAC em 15% após 4 semanas. Critério de falha: Aumento do CAC em mais de 5% ou queda no LTV/CAC.
    *   **Teste SEO:** Critério de sucesso: Aumento de 10% no tráfego orgânico qualificado e 5% no número de MQLs oriundos de SEO nos próximos 3 meses, mantendo o CAC atual. Critério de falha: Nenhum impacto significativo após 4 meses.

**Passo 4: Realocação Dinâmica de Orçamento e Iteração**
*   **Ação:** Com base nos resultados dos testes e na análise contínua do ranking LTV/CAC, realoque o orçamento de forma dinâmica. Canais que performam abaixo das expectativas podem ter seu orçamento reduzido ou realocado para testes em outros canais.
*   **Frequência:** Revisar o ranking e a alocação de orçamento mensalmente ou trimestralmente.
*   **Exemplo:** Se o teste em Google Ads reduziu o CAC em 12% e aumentou o LTV/CAC para 40, transferir 10% do orçamento do canal Meta Ads para Google Ads no próximo mês fiscal, buscando maximizar o retorno total sobre o investimento em aquisição. Se o canal de parcerias se mostrar promissor em um POC com LTV/CAC > 10, alocar um orçamento inicial de R$ 3.000 para um teste de escala.

---

## Templates

### Tabela de Ranking de Canais de Aquisição Completa

```
| Canal             | Orçamento Atual (R$) | Investimento Período (R$) | Clientes Adquiridos | CAC (R$) | LTV Estimado (R$) | LTV/CAC | Potencial Escala (1-5) | Ação Recomendada                                     |
|-------------------|----------------------|---------------------------|---------------------|----------|-------------------|---------|------------------------|------------------------------------------------------|
| SEO               | 5.000                | 15.000                    | 600                 | 25       | 5.820             | 232,8   | 3                      | Aumentar investimento em conteúdo (30%) e otimização |
| Email Marketing   | 1.500                | 4.500                     | 225                 | 20       | 3.840             | 192,0   | 4                      | Expandir automação e testar parcerias de lead gen    |
| Google Ads (Search)| 12.000               | 36.000                    | 450                 | 80       | 2.850             | 35,6    | 5                      | Otimizar lances, testar novos formatos de anúncio    |
| Meta Ads (Feed)   | 8.000                | 24.000                    | 300                 | 80       | 1.714             | 21,4    | 4                      | Testar novas audiências Lookalike, otimizar criativos|
| LinkedIn Ads (B2B)| 2.000                | 6.000                     | 50                  | 120      | 4.500             | 37,5    | 3                      | Testar campanhas com foco em C-levels, segmentação + fina |
| Afiliados         | 1.000                | 3.000                     | 20                  | 150      | 2.500             | 16,7    | 2                      | Avaliar rentabilidade, considerar pausar ou reestruturar |
```

### Plano de Teste de Canal de Aquisição (POC)

```
**Nome do Teste:** Expansão de Campanhas de Google Ads para termos de Cauda Longa
**Canal:** Google Ads (Search)
**Objetivo do Teste:** Aumentar o volume de MQLs em 20% oriundos de Google Ads, mantendo o LTV/CAC acima de 30.
**Orçamento Alocado:** R$ 3.000 adicionais (total R$ 15.000 para Google Ads no mês).
**Duração do Teste:** 4 semanas (01/10/2025 - 28/10/2025).
**KPIs Primários:**
  - Número de MQLs de Google Ads
  - CAC de Google Ads (MQL)
  - LTV/CAC de Google Ads (Cliente)
**KPIs Secundários:**
  - Custo por Clique (CPC)
  - Taxa de Cliques (CTR)
  - Posição Média do Anúncio
**Hipótese:** Ao expandir para termos de cauda longa, atingiremos um público mais qualificado e com menor custo de aquisição, melhorando o LTV/CAC geral do canal.
**Critério de Sucesso:**
  - Aumento de 20% no volume de MQLs de Google Ads.
  - LTV/CAC do canal Google Ads mantido acima de 30 ou melhorado.
  - CAC (MQL) não aumenta mais de 10%.
**Critério de Falha:**
  - Volume de MQLs não aumenta ou aumenta menos de 10%.
  - LTV/CAC do canal Google Ads cai abaixo de 25.
  - CAC (MQL) aumenta mais de 15%.
**Próximos Passos (se sucesso):** Alocar R$ 5.000 adicionais para escalar campanhas de cauda longa no próximo trimestre.
**Próximos Passos (se falha):** Reverter as mudanças, analisar palavras-chave de baixa performance e investigar outras estratégias de otimização de campanhas existentes.
```

---

## Checklist

- [x] Dados de investimento e conversão por canal estão consolidados em uma única fonte (CRM, BI)?
- [x] O modelo de atribuição escolhido (e.g., Linear, Ponderado por Posição) está implementado e configurado corretamente nas ferramentas de análise?
- [x] O LTV dos clientes é calculado e segmentado por canal de aquisição ou por características relevantes do segmento que o canal atrai?
- [x] O CAC é calculado considerando não apenas o gasto direto em mídia, mas também os custos indiretos (salários, ferramentas, conteúdo)?
- [x] Há um processo automatizado ou manual para recalcular o LTV/CAC e o ranking de canais mensalmente ou trimestralmente?
- [x] Canais com alto LTV/CAC, mas baixo volume, foram analisados detalhadamente para identificar gargalos e potencial de escala?
- [x] O orçamento de aquisição é realocado dinamicamente com base nos resultados do ranking e nos testes de otimização?
- [x] Foram definidos critérios claros de sucesso e falha antes de iniciar testes de alocação de orçamento em novos canais ou estratégias?
- [x] O time de marketing e vendas está alinhado com as prioridades dos canais de aquisição e com os KPIs de LTV/CAC?
- [x] São realizadas análises de coorte por canal para entender a evolução do LTV e da retenção ao longo do tempo?

---

## Métricas de Referência

| Métrica               | Benchmark (Geral) | Meta (Empresa em Growth) |
| :-------------------- | :---------------- | :----------------------- |
| LTV/CAC               | > 3:1             | > 5:1                    |
| CAC (como % do LTV)   | < 33%             | < 20%                    |
| Payback Period (SaaS) | < 12 meses        | < 6 meses                |
| Taxa de Churn (Mensal)| < 5%              | < 2%                     |
| ROAS (Média)          | > 2:1             | > 4:1                    |
| Taxa de Conversão (Lead->Cliente) | 1-5% (B2B), 0.5-2% (e-commerce)| 3-8% (B2B), 1-3% (e-commerce)|

---

## Erros Comuns

1.  **Atribuição Simplista (Último Clique ou Primeiro Clique)**: Este modelo ignora a complexidade da jornada do cliente, creditando toda a conversão a um único ponto de contato.
    *   **Como evitar com exemplo**: Implemente modelos de atribuição mais sofisticados como "Linear" ou "Baseado em Posição" no Google Analytics 4. Por exemplo, um cliente que viu um anúncio no Facebook, depois pesquisou no Google e clicou em um email antes de comprar, terá o crédito dividido entre esses canais, em vez de apenas o email.
2.  **Cálculo Incompleto do CAC**: Muitos negócios calculam o CAC apenas com o gasto direto em mídia, excluindo salários da equipe de marketing, licenças de ferramentas, custos de conteúdo e agências.
    *   **Como evitar com exemplo**: Garanta que todos os custos associados ao marketing e vendas para aquisição de novos clientes estejam incluídos no cálculo. Se sua equipe de marketing custa R$ 20.000/mês e o gasto em mídia é R$ 30.000/mês, e você adquire 100 clientes, o CAC real é (R$ 20.000 + R$ 30.000) / 100 = R$ 500, não apenas R$ 300.
3.  **LTV Estático ou Não Segmentado**: Assumir que todos os clientes, independentemente do canal de origem, terão o mesmo Lifetime Value. Isso mascara a real rentabilidade de cada canal.
    *   **Como evitar com exemplo**: Calcule o LTV por coorte de aquisição e, crucialmente, por canal. Clientes vindos de referências podem ter um LTV 2x maior que os de campanhas de tráfego pago frio devido a maior lealdade e menor churn. Segmentar LTV por canal revela que, embora o CAC do canal A seja maior, seu LTV superior o torna mais lucrativo.

---

## Dicas Avançadas

1.  **Análise de Cohorts por Canal e Mês de Aquisição**: Vá além do LTV/CAC médio. Analise a evolução do LTV e da retenção de clientes por coortes (grupos de clientes adquiridos no mesmo período) e por canal.
    *   **Exemplo Prático**: Clientes adquiridos via SEO em janeiro de 2024 podem ter um LTV acumulado de R$ 1.500 após 6 meses, enquanto os de Meta Ads do mesmo período têm R$ 900. Isso confirma a superioridade de SEO no longo prazo e informa decisões de investimento futuras.
2.  **Identificação de Canais Complementares e Sinergias**: Alguns canais não performam bem isoladamente, mas são cruciais para a performance de outros.
    *   **Exemplo Prático**: Investir em branding (anúncios de display ou podcasts) pode não gerar muitas conversões diretas (baixo LTV/CAC), mas pode reduzir o CAC de campanhas de performance em Google Ads ao aumentar o volume de buscas diretas e o Quality Score dos anúncios.
3.  **Modelagem Preditiva de LTV (pLTV)**: Utilize machine learning para prever o LTV de novos clientes com base em seu comportamento inicial (primeiros 7-30 dias).
    *   **Exemplo Prático**: Um cliente de e-commerce que faz uma segunda compra dentro de 15 dias após a primeira tem 80% de chance de ter um pLTV 3x maior que o cliente médio. Isso permite identificar rapidamente clientes de alto valor e otimizar estratégias de retenção específicas por canal.
4.  **Teste de Canais Não Convencionais ou "Hidden Gems"**: Nem todos os canais óbvios serão os melhores. Explore nichos ou plataformas menos exploradas por sua concorrência.
    *   **Exemplo Prático**: Para um SaaS B2B, testar parcerias com newsletters de nicho, comunidades no Slack/Discord específicas da indústria, ou até mesmo eventos online focados em um problema específico. Um canal de parceria com um influenciador de nicho pode ter um CAC inicial alto, mas um LTV/CAC > 10 devido à alta qualificação da audiência.
5.  **Otimização do Funil Pós-Aquisição por Canal**: A experiência do cliente logo após a aquisição pode ser otimizada com base no canal de origem para maximizar o LTV.
    *