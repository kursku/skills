---
name: budget-allocation
description: "Budget Allocation — Skill especializada para budget allocation"
license: MIT
metadata:
  version: 1.0.0
  author: Cafe Code AI
  category: 04-anuncios-trafego
  updated: 2026-03-01
risk: safe
---

# Budget Allocation

Esta skill capacita o Claude a otimizar a distribuição de orçamentos de publicidade digital em Meta Ads, Google Ads e TikTok Ads para maximizar o retorno sobre investimento (ROAS) e eficiência de custo por aquisição (CPA).

---

## Keywords

Otimização de Orçamento Ads, Alocação de Verba Digital, Meta Ads Budget, Google Ads Funding, TikTok Ads Spend, ROAS Maximization, CPA Efficiency, Campaign Budget Optimization (CBO), Portfolio Bidding Google Ads, Multi-Platform Ad Spend, Incrementality Testing, Digital Marketing Budgeting, Performance Marketing Allocation.

---

## Quick Start

1.  **Consolidar Dados de Performance Recentes**: Extraia o ROAS e o CPA dos últimos 30 dias para cada campanha ativa em Meta Ads, Google Ads e TikTok Ads.
2.  **Identificar Campanhas de Alto Retorno**: Priorize campanhas com ROAS superior a 3.5x e CPA abaixo de R$50,00 como candidatas para receber mais orçamento.
3.  **Realocar 15% do Orçamento Total**: Transfira 15% do orçamento total mensal de campanhas de baixo desempenho (ROAS < 2.0x ou CPA > R$80,00) para as campanhas de alto retorno identificadas.
4.  **Ajustar Orçamentos Diários**: Implemente os novos valores de orçamento diário nas plataformas e programe uma revisão em 7 dias.

---

## Core Workflows

### Workflow 1: Alocação Dinâmica de Orçamento Baseada em Performance e Saturação

Este workflow foca em ajustar o orçamento entre campanhas e plataformas com base em métricas de performance e sinais de saturação de público.

1.  **Coleta e Consolidação de Dados de Performance (Semanal)**:
    *   **Meta Ads**: Exporte dados de `ROAS de Compras`, `CPA de Compras`, `Frequência de Impressões` e `Alcance` por conjunto de anúncios e campanha dos últimos 7 dias.
    *   **Google Ads**: Exporte `ROAS de Conversão`, `CPA` e `Parcela de Impressões Perdidas (Orçamento)` por campanha dos últimos 7 dias.
    *   **TikTok Ads**: Exporte `ROAS` e `CPA` por campanha e grupo de anúncios, incluindo `Frequência` e `Alcance` dos últimos 7 dias.
    *   **Exemplo**:
        *   Meta Ads - Campanha A (Retargeting): ROAS 5.2x, CPA R$25, Frequência 3.8.
        *   Meta Ads - Campanha B (Aquisição): ROAS 2.7x, CPA R$60, Frequência 1.2.
        *   Google Ads - Campanha C (Search Branded): ROAS 6.8x, CPA R$15.
        *   Google Ads - Campanha D (Shopping): ROAS 3.0x, CPA R$48, Parcela Perdida (Orçamento) 15%.
        *   TikTok Ads - Campanha E (Aquisição): ROAS 2.1x, CPA R$75, Frequência 2.5.

2.  **Análise de Potencial e Saturação**:
    *   **Identificar Ganhadores**: Campanhas com ROAS > 3.5x e CPA < R$40,00.
    *   **Identificar Perdedores**: Campanhas com ROAS < 2.0x e CPA > R$70,00.
    *   **Avaliar Saturação**: Frequência > 3.0 em Meta/TikTok Ads (últimos 7 dias) ou `Parcela de Impressões Perdidas (Orçamento)` < 5% no Google Ads para campanhas de alto ROAS indicam possível saturação ou teto de gasto.
    *   **Exemplo Análise**:
        *   Campanha A (Meta Retargeting): Excelente ROAS e CPA, mas Frequência 3.8. Possível saturação se o orçamento for muito aumentado.
        *   Campanha B (Meta Aquisição): Desempenho mediano, Frequência baixa. Há espaço para aumento de orçamento.
        *   Campanha C (Google Branded): Ótimo ROAS/CPA. Provavelmente já está maximizada, mas verificar `Parcela de Impressões Perdidas`.
        *   Campanha D (Google Shopping): Bom ROAS, CPA aceitável, mas 15% de `Parcela Perdida (Orçamento)`. Indicação clara de que mais orçamento pode gerar mais volume.
        *   Campanha E (TikTok Aquisição): ROAS e CPA abaixo da meta. Pode ser candidata a corte de orçamento ou otimização profunda.

3.  **Proposta de Re-Alocação de Orçamento (Diário/Semanal)**:
    *   **Aumento (Escala)**:
        *   Campanhas com ROAS > 3.5x e Frequência < 2.5 (Meta/TikTok) ou `Parcela de Impressões Perdidas (Orçamento)` > 10% (Google): Aumentar orçamento em 10-20%.
        *   **Exemplo**: Campanha D (Google Shopping) com 15% de `Parcela Perdida`. Aumentar orçamento diário de R$300 para R$360.
    *   **Manutenção (Otimização)**:
        *   Campanhas com ROAS entre 2.5x e 3.5x e Frequência entre 2.5 e 3.5 (Meta/TikTok) ou `Parcela de Impressões Perdidas (Orçamento)` entre 5-10% (Google): Manter orçamento, focar em otimizações criativas ou de segmentação.
        *   **Exemplo**: Campanha B (Meta Aquisição). Manter R$400 diários, testar novos públicos lookalike.
    *   **Redução (Corte)**:
        *   Campanhas com ROAS < 2.0x, CPA > R$70,00 e Frequência > 3.0 ou `Parcela de Impressões Perdidas (Orçamento)` < 5%: Reduzir orçamento em 10-20% ou pausar.
        *   **Exemplo**: Campanha E (TikTok Aquisição). Reduzir orçamento diário de R$200 para R$160.
    *   **Rebalanceamento para Retargeting**: Manter 20-30% do orçamento total para campanhas de retargeting, que geralmente apresentam ROAS superior.

4.  **Implementação e Monitoramento Contínuo**:
    *   Aplique os ajustes de orçamento nas plataformas.
    *   Monitore as métricas-chave diariamente. Se uma campanha aumentar o ROAS significativamente após o aumento, considere um novo ajuste incremental.

### Workflow 2: Otimização de Orçamento com CBO e Estratégias de Lance de Portfólio

Este workflow detalha a utilização de ferramentas de alocação automática das plataformas para otimizar o gasto.

1.  **Estruturação de Campanhas para CBO (Meta Ads / TikTok Ads)**:
    *   **Agrupamento Lógico**: Crie campanhas com objetivos claros (Ex: Aquisição - Prospecção, Aquisição - Lookalike, Retargeting - Carrinho Abandonado).
    *   **Múltiplos Conjuntos de Anúncios**: Dentro de cada campanha CBO, inclua 3 a 5 conjuntos de anúncios com públicos distintos (Ex: Lookalike 1%, Lookalike 1-3%, Interesses amplos, Retargeting de 30 dias).
    *   **Definição de Orçamento de Campanha**: Aloque um orçamento diário ou vitalício para a campanha, deixando a plataforma distribuir entre os conjuntos de anúncios.
    *   **Exemplo**:
        *   **Campanha Meta Ads**: `Compras - Aquisição - CBO`
            *   Orçamento Diário: R$800,00
            *   Conjunto de Anúncios 1: Público Lookalike 1% (Base de Compradores)
            *   Conjunto de Anúncios 2: Público Interesses (e.g., "Moda Sustentável", "Beleza Natural")
            *   Conjunto de Anúncios 3: Público Amplo (sem segmentação, apenas idade/gênero)
            *   Configuração: Lance de "Menor Custo" ou "Custo por Resultado Alvo" (R$55,00).

2.  **Configuração de Estratégias de Lance de Portfólio (Google Ads)**:
    *   **Agrupamento de Campanhas**: Agrupe campanhas com objetivos semelhantes (Ex: todas as campanhas de Shopping, ou todas as campanhas de Search não-branded) em um portfólio.
    *   **Estratégia de Lance Centralizada**: Aplique uma estratégia de lance de portfólio (Ex: "Maximizar valor da conversão com ROAS-alvo" ou "Maximizar conversões com CPA-alvo") a esse grupo de campanhas.
    *   **Definição de Alvos**: Defina um ROAS alvo (Ex: 350%) ou CPA alvo (Ex: R$45,00) que se aplique ao conjunto de campanhas.
    *   **Exemplo**:
        *   **Portfólio Google Ads**: `e-commerce - Max Value ROAS Target`
            *   Campanha 1: Shopping - Todos os Produtos
            *   Campanha 2: Search - Genéricos (e.g., "comprar tênis", "loja de roupas")
            *   Campanha 3: Display - Remarketing
            *   Estratégia de Lance: `Maximizar valor da conversão com ROAS-alvo` (ROAS Alvo: 350%)
            *   Orçamento Total Diário para o portfólio: R$1.200,00

3.  **Ajuste de Limites de Gasto e ROI (TikTok Ads)**:
    *   **Orçamento de Campanha e Grupo de Anúncios**: No TikTok Ads, você pode definir orçamentos tanto na campanha quanto no grupo de anúncios. Para CBO, defina o orçamento na campanha.
    *   **Otimização de Lance**: Utilize estratégias de lance como "Custo Mais Baixo" ou "Custo Máximo" (para CPA) ou "ROAS Mais Alto" (para valor).
    *   **Limites de CPA/ROAS**: Se estiver usando "Custo Mais Baixo", adicione um `Limite de Custo` (Max CPA) para evitar gastos excessivos em resultados caros.
    *   **Exemplo**:
        *   **Campanha TikTok Ads**: `Vendas - CBO - Coleção Verão`
            *   Orçamento Diário: R$600,00
            *   Grupo de Anúncios 1: Público Personalizado (Interesse em Moda)
            *   Grupo de Anúncios 2: Público Lookalike 1% (Engajamento Vídeo)
            *   Estratégia de Lance: `Custo Mais Baixo` com `Limite de Custo`: R$70,00 (CPA máximo aceitável).

4.  **Monitoramento e Iteração**:
    *   Monitore a distribuição do orçamento pelas plataformas e o desempenho dos conjuntos de anúncios/campanhas dentro das estratégias de portfólio/CBO.
    *   Ajuste os orçamentos da campanha e os alvos de lance (ROAS/CPA) conforme necessário para otimizar o desempenho geral.

---

## Templates

### Planilha de Alocação de Orçamento Mensal Consolidado

```
| Plataforma | Campanha/Tipo | Orçamento Atual (R$) | ROAS Médio (30d) | CPA Médio (30d) | % ROAS vs. Meta | % CPA vs. Meta | Sugestão Novo Orçamento (R$) | Ajuste (%) | Justificativa |
|------------|---------------|----------------------|------------------|-----------------|-----------------|----------------|-----------------------------|------------|---------------|
| Meta Ads   | Aquisição - CBO    | 5.000                | 2.8x             | 55.00           | -20%            | +10%           | 4.500                       | -10%       | ROAS abaixo da meta, CPA alto. Reduzir e otimizar criativos. |
| Meta Ads   | Retargeting - DPA  | 3.000                | 6.5x             | 18.00           | +30%            | -20%           | 3.500                       | +17%       | Excelente ROAS/CPA. Aumentar para capturar mais conversões de fundo de funil. |
| Google Ads | Search - Branded   | 2.000                | 7.2x             | 12.00           | +40%            | -30%           | 2.000                       | 0%         | Performance sólida, já maximizada para volume de busca. |
| Google Ads | Shopping - Smart   | 4.000                | 3.1x             | 45.00           | +5%             | +5%            | 4.800                       | +20%       | Bom ROAS, CPA ok. Google Ads indica potencial de aumento via "Parcela de Impressões Perdidas". |
| TikTok Ads | Aquisição - Vídeo  | 2.500                | 1.9x             | 85.00           | -35%            | +70%           | 1.500                       | -40%       | ROAS e CPA muito fora da meta. Reduzir e testar novos criativos/públicos. |
| **TOTAL**  |               | **16.500**           |                  |                 |                 |                | **16.300**                  |            |               |
```

### Relatório de Desempenho Pós-Alocação (Semanal)

```
| Plataforma | Campanha/Tipo | Orçamento Alocado (R$) | Orçamento Gasto (R$) | ROAS Realizado | CPA Realizado | % Desvio ROAS vs. Alvo | % Desvio CPA vs. Alvo | Observações |
|------------|---------------|------------------------|----------------------|----------------|---------------|------------------------|-----------------------|-------------|
| Meta Ads   | Aquisição - CBO    | 4.500                  | 4.480                | 2.9x           | 52.00         | +3%                    | -5%                   | Pequena melhora, ainda com espaço para otimização de criativos. |
| Meta Ads   | Retargeting - DPA  | 3.500                  | 3.500                | 6.8x           | 17.50         | +5%                    | -3%                   | Mantendo excelente performance. |
| Google Ads | Search - Branded   | 2.000                  | 1.990                | 7.0x           | 12.50         | -3%                    | +4%                   | Estável, conforme esperado. |
| Google Ads | Shopping - Smart   | 4.800                  | 4.790                | 3.3x           | 43.00         | +6%                    | -4%                   | Aumento de ROAS e redução de CPA após incremento de orçamento. |
| TikTok Ads | Aquisição - Vídeo  | 1.500                  | 1.490                | 2.2x           | 78.00         | +16%                   | -8%                   | Melhorou levemente, mas CPA ainda alto. Requer revisão de público/oferta. |
```

---

## Checklist

- [x] Consolidar dados de ROAS, CPA e volume de conversões por campanha/plataforma.
- [x] Analisar a frequência de exibição e alcance em Meta/TikTok Ads para detectar saturação.
- [x] Verificar a `Parcela de Impressões Perdidas (Orçamento)` no Google Ads.
- [x] Identificar campanhas com ROAS consistentemente acima da meta (e.g., 3.5x).
- [x] Identificar campanhas com CPA consistentemente abaixo da meta (e.g., R$40,00).
- [x] Priorizar orçamentos para campanhas de retargeting (maior ROAS esperado).
- [x] Alocar 20-30% do orçamento total para campanhas de retargeting.
- [x] Considerar a sazonalidade e eventos promocionais (Black Friday, Dia das Mães) na alocação.
- [x] Implementar testes A/B de orçamento para validar mudanças significativas.
- [x] Utilizar CBO (Campaign Budget Optimization) no Meta Ads e TikTok Ads para distribuição automática.
- [x] Aplicar estratégias de lance de portfólio no Google Ads para gerenciar múltiplos orçamentos.
- [x] Programar revisões semanais de desempenho e reajustes de orçamento.

---

## Métricas de Referência

| Métrica                      | Benchmark (e-commerce) | Meta (Exemplo) |
|------------------------------|------------------------|----------------|
| ROAS (Return on Ad Spend)    | 3.0x - 5.0x            | 3.5x           |
| CPA (Custo por Aquisição)    | R$30,00 - R$80,00      | R$45,00        |
| CTR (Click-Through Rate) Meta Ads | 1.5% - 3.0%            | 2.2%           |
| CPC (Custo por Clique) Google Search | R$1,50 - R$5,00        | R$2,80         |
| CPM (Custo por Mil Impressões) TikTok Ads | R$15,00 - R$35,00      | R$25,00        |
| Frequência (Meta/TikTok - 7d) | 2.5 - 3.5              | 3.0            |

---

## Erros Comuns

1.  **Alocar orçamento baseado apenas no ROAS bruto sem considerar o volume**: Uma campanha pode ter um ROAS de 10.0x com apenas 5 conversões, enquanto outra com ROAS de 3.0x gera 200 conversões. O erro é focar apenas no ROAS alto e ignorar o potencial de escala.
    *   **Como evitar**: Priorize o lucro total gerado e o volume de conversões. Utilize uma métrica como "Lucro Bruto de Anúncios" (Receita - Custo dos Anúncios - Custo dos Produtos) ou "ROAS Ponderado pelo Volume" para tomar decisões de alocação. Ex: Se a campanha de ROAS 3.0x gera R$15.000 em vendas e a de ROAS 10.0x gera R$1.000, é mais vantajoso escalar a primeira.

2.  **Ignorar a saturação de público e continuar injetando dinheiro**: Manter ou aumentar o orçamento em públicos que já viram os anúncios várias vezes leva a um aumento do CPM e CPA, e uma queda do ROAS.
    *   **Como evitar**: Monitore a `Frequência de Impressões` (especialmente em Meta Ads e TikTok Ads) e o `Alcance` semanalmente. Se a frequência média está acima de 3.5-4.0 nas últimas 7-14 dias, o público pode estar saturado. Reduza o orçamento para essa audiência e invista em prospecção de novos públicos ou teste novos criativos. Ex: Uma campanha de aquisição no Meta Ads com frequência 4.8 nos últimos 7 dias deve ter seu orçamento reduzido em 15-20% e o excedente realocado para um público lookalike 1-3% diferente.

3.  **Não diferenciar orçamentos para campanhas de topo, meio e fundo de funil**: Tratar todas as campanhas com a mesma expectativa de ROAS e CPA, sem reconhecer que campanhas de aquisição (topo) terão ROAS menor, mas maior volume, enquanto retargeting (fundo) terá ROAS maior, mas menor volume.
    *   **Como evitar**: Estabeleça metas de ROAS e CPA diferenciadas para cada etapa do funil. Aloque uma proporção maior do orçamento (70-80%) para campanhas de aquisição e brand awareness, e uma menor (20-30%) para campanhas de retargeting de alta intenção. Ex: Para um orçamento total de R$10.000, destinar R$7.500 para prospecção em Meta Ads e Google Search, e R$2.500 para retargeting em Meta Ads DPA e Google Display.

---

## Dicas Avançadas

1.  **Modelagem de Atribuição Customizada**: Vá além dos modelos padrão ("último clique", "linear") e crie um modelo de atribuição baseado em dados (Data-Driven Attribution) no Google Analytics 4 ou use ferramentas de atribuição externas para entender o verdadeiro impacto de cada touchpoint. Isso permite alocar orçamento para canais que contribuem para a jornada, mas não recebem o crédito final. Ex: Um clique inicial em um anúncio de display pode não ser o "último clique", mas é crucial para iniciar a jornada. Um modelo customizado atribuirá parte do crédito a ele.

2.  **Testes de Incrementalidade Geográfica (Geo-Lift Tests)**: Em vez de apenas comparar ROAS, execute testes controlados para medir o impacto *incremental* de um aumento de orçamento. Selecione regiões geograficamente semelhantes e aplique o aumento de orçamento em uma (grupo de teste) enquanto mantém a outra (grupo de controle) inalterada. Compare o aumento de vendas e lucratividade entre os grupos para validar a eficácia real do investimento adicional. Ex: Aumentar o orçamento em 20% no Meta Ads para o estado de Minas Gerais e comparar o desempenho de vendas com o estado do Paraná, que manteve o orçamento.

3.  **Automação de Regras de Orçamento com Scripts**: Utilize scripts personalizados (Google Ads Scripts, Meta Automated Rules) para automatizar ajustes de orçamento baseados em desempenho em tempo real. Configure regras para aumentar orçamentos de campanhas que excedem o ROAS alvo em 20% por 3 dias consecutivos ou reduzir orçamentos de campanhas com CPA 30% acima do alvo. Ex: Um script no Google Ads que aumenta o orçamento diário em 10% para campanhas com ROAS > 4.0x no dia anterior, limitado a um máximo de 20% de aumento semanal.

4.  **Análise de Margem de Lucro Bruta por Produto/Campanha**: Alocar orçamento não apenas pelo ROAS ou CPA genérico, mas considerando a margem de lucro bruta dos produtos promovidos. Priorize campanhas que vendem produtos com maior margem, mesmo que o ROAS absoluto seja ligeiramente menor que o de produtos de baixa margem, pois o lucro final será maior. Ex: Um produto com ROAS de 3.0x e margem de 60% é mais lucrativo que um produto com ROAS de 4.0x e margem de 20%, ao mesmo volume de vendas.

5.  **Previsão de Orçamento com Tendências Sazonais e Externas**: Use dados históricos de sazonalidade (feriados, épocas de vendas) e fatores externos (lançamentos de produtos, tendências de mercado) para prever o desempenho futuro e pré-alocar orçamentos. Ferramentas de BI ou modelos de Machine Learning podem ajudar a construir cenários de alocação otimizados para picos e vales de demanda. Ex: Aumentar o orçamento em 40% em campanhas de Google Shopping 3 semanas antes da Black Friday, com base na análise de ROAS e volume de conversões dos últimos 3 anos para esse período.