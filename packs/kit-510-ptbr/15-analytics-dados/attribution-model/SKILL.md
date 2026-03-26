---
name: attribution-model
description: "Attribution Model — Skill especializada para análise, comparação e implementação de modelos de atribuição no Google Analytics 4, otimizando investimentos em marketing digital."
license: MIT
metadata:
  version: 1.0.0
  author: Cafe Code AI
  category: 15-analytics-dados
  updated: 2026-03-01
risk: safe
---

# Attribution Model

Esta skill capacita o Claude a compreender, analisar e aplicar modelos de atribuição de marketing no contexto do Google Analytics 4 (GA4), fornecendo insights acionáveis para otimização de campanhas.

---

## Keywords

Last Click, First Click, Linear, Time Decay, Data-Driven, Atribuição Multi-Touch, GA4, Model Comparison Tool, Caminhos de Conversão, CPA, ROAS, LTV, Canais de Marketing, Janela de Lookback, Eventos de Conversão, Contribuição de Canais, Otimização de Lances.

---

## Quick Start

1.  Acessar o Google Analytics 4 e navegar até "Publicidade" > "Atribuição" > "Modelos de atribuição e Comparação de modelos".
2.  Selecionar "Last Click" e "Data-Driven" como modelos de comparação primários para uma análise inicial.
3.  Escolher "Compradores" ou "Receita de compra" como métrica de conversão para avaliar o impacto.
4.  Analisar a diferença percentual na contribuição de cada canal entre os modelos para identificar subvalorização ou supervalorização.
5.  Exportar os dados para um spreadsheet e calcular o ROAS (Retorno sobre o Investimento em Publicidade) por canal sob diferentes modelos.

---

## Core Workflows

### Workflow 1: Análise e Comparação Detalhada de Modelos de Atribuição no GA4

Este workflow guia o processo de examinar a performance de diferentes canais de marketing sob variados modelos de atribuição, utilizando as ferramentas nativas do GA4 para identificar oportunidades de otimização de investimento.

1.  **Acessar a Seção de Publicidade no GA4**:
    *   No menu lateral esquerdo do GA4, clicar em "Publicidade".
    *   Navegar até "Atribuição" e selecionar "Modelos de atribuição e Comparação de modelos".

2.  **Configurar Parâmetros de Análise**:
    *   **Dimensão**: Manter "Grupo de canais padrão da sessão" ou selecionar "Fonte", "Mídia" ou "Campanha" para análise mais granular. Por exemplo, selecionar "Fonte".
    *   **Métrica de Conversão**: Escolher a conversão principal para análise. Ex: "purchase" (compra) ou "lead_form_submit" (envio de formulário de lead).
    *   **Modelos de Atribuição**: No menu suspenso, selecionar os modelos a serem comparados. Recomenda-se começar com:
        *   `Last Click` (modelo de base para entender a atribuição final).
        *   `First Click` (para entender canais de descoberta/awareness).
        *   `Linear` (para distribuição igualitária).
        *   `Data-Driven` (o modelo inteligente do GA4, que usa dados históricos para atribuir crédito de forma mais justa).
    *   **Janela de Lookback**: Ajustar a janela de lookback para eventos de conversão e aquisição de usuários. A janela padrão para eventos de conversão é 90 dias, e para eventos de aquisição de usuários é 30 dias. Para produtos de ciclo de vendas mais longo, considerar 120 dias ou mais para eventos de conversão. Para produtos de compra impulsiva, 30-60 dias pode ser suficiente.

3.  **Interpretar o Relatório de Comparação de Modelos**:
    *   A tabela exibirá a contagem de conversões e o valor das conversões para cada canal sob os modelos selecionados.
    *   **Analisar a coluna "Diferença %"**: Esta coluna é crucial. Ela mostra a variação percentual na atribuição de crédito entre o modelo de atribuição principal e os outros modelos.
        *   Um valor positivo indica que o canal recebe **mais crédito** no modelo de comparação do que no modelo principal.
        *   Um valor negativo indica que o canal recebe **menos crédito**.
    *   **Exemplo Prático**: Se o canal "Organic Search" mostra +25% na comparação entre Last Click (principal) e Data-Driven, significa que o Organic Search contribui para 25% mais conversões quando se considera todo o caminho do cliente, e não apenas o último clique. Isso sugere que o Last Click subestima o valor do Organic Search.

4.  **Identificar Oportunidades de Otimização**:
    *   **Canais Subvalorizados**: Canais que recebem significativamente mais crédito nos modelos First Click, Linear ou Data-Driven em comparação com o Last Click são frequentemente subvalorizados. Ex: "Display", "Organic Social", "Email". Considerar realocar orçamento para esses canais no início da jornada ou em pontos intermediários.
    *   **Canais Supervalorizados**: Canais que recebem muito menos crédito nos modelos multi-touch comparados ao Last Click podem estar supervalorizados. Ex: "Direct", "Paid Search" (para termos de marca, se não for ajustado). Avaliar se o investimento atual é justificado apenas pela atribuição final.
    *   **Exemplo de Decisão**: Se o "Paid Search" (termos genéricos) tem uma diferença de -15% no modelo Data-Driven vs. Last Click, mas "Display" tem +20%, pode-se considerar reduzir o investimento em Paid Search para termos genéricos e aumentar o investimento em Display, dado que Display contribui mais para a jornada geral.

### Workflow 2: Configuração de Eventos de Conversão e Parâmetros para Atribuição Robusta no GA4

Este workflow garante que o GA4 esteja coletando os dados corretos e de forma granular para uma análise de atribuição precisa. A qualidade da atribuição depende diretamente da qualidade dos dados de conversão.

1.  **Verificar e Configurar Eventos de Conversão Essenciais**:
    *   No GA4, navegar até "Administrador" > "Fluxos de dados" > "Selecionar o fluxo de dados web".
    *   Clicar em "Configurar definições da tag" e depois em "Mostrar tudo" na seção "Coleta de eventos".
    *   Verificar se os eventos que representam marcos importantes da jornada do cliente (e-commerce: `add_to_cart`, `begin_checkout`, `purchase`; Geração de Leads: `form_submit`, `contact_us`) estão sendo coletados.
    *   Marcar como conversão (`toggle`) apenas os eventos que representam o objetivo final. Ex: `purchase` e `generate_lead`. Eventos intermediários como `add_to_cart` são importantes para funil, mas não como conversão final para modelos de atribuição.

2.  **Implementar Parâmetros de Evento para Contexto Rico**:
    *   Para cada evento de conversão, garantir que parâmetros contextuais relevantes estejam sendo enviados.
    *   **Exemplo para `purchase`**:
        ```javascript
        gtag('event', 'purchase', {
          transaction_id: 'T_12345',
          value: 75.00,
          currency: 'BRL',
          items: [
            { item_id: 'SKU_A', item_name: 'Produto X', price: 50.00, quantity: 1 },
            { item_id: 'SKU_B', item_name: 'Produto Y', price: 25.00, quantity: 1 }
          ]
        });
        ```
        Parâmetros como `value` e `currency` são cruciais para calcular o ROAS e o valor das conversões.
    *   **Exemplo para `generate_lead`**:
        ```javascript
        gtag('event', 'generate_lead', {
          form_name: 'contato_principal',
          lead_source: 'website_form',
          value: 150.00, // Valor estimado do lead, se aplicável
          currency: 'BRL'
        });
        ```
        `form_name` e `lead_source` podem ser usados para segmentar e entender a qualidade dos leads por origem.

3.  **Configurar Dimensões Personalizadas (Custom Dimensions) para Segmentação Avançada**:
    *   Se informações adicionais forem relevantes para a atribuição (ex: tipo de cliente, segmento de produto), configurar dimensões personalizadas.
    *   No GA4, navegar até "Administrador" > "Definições de dados" > "Definições personalizadas".
    *   Criar uma nova dimensão personalizada no escopo "Evento" ou "Usuário".
    *   **Exemplo**: Criar uma dimensão de escopo de usuário chamada "User Segment" (segmento do usuário) que recebe valores como "Cliente Novo", "Cliente Recorrente". Isso permite analisar a atribuição de forma diferente para cada segmento.
    *   **Implementação (exemplo)**:
        ```javascript
        gtag('set', 'user_properties', {
          user_segment: 'Cliente Novo'
        });
        ```

4.  **Ajustar a Janela de Lookback de Atribuição**:
    *   Em "Administrador" > "Configurações de atribuição", revisar a "Janela de lookback para eventos de conversão" e "Janela de lookback para eventos de aquisição".
    *   **Eventos de Conversão**: O padrão é 90 dias. Para produtos de alto valor ou ciclos de venda longos (imóveis, carros, serviços B2B), considere aumentar para 120 dias ou até o máximo de 425 dias para garantir que toques anteriores sejam creditados.
    *   **Eventos de Aquisição**: O padrão é 30 dias. Manter este valor para a maioria dos casos, a menos que a aquisição de um usuário seja intrinsecamente um processo muito mais longo.
    *   **Impacto**: Uma janela muito curta pode fazer com que canais que atuam no início da jornada sejam subestimados. Uma janela muito longa pode diluir o crédito para interações mais recentes.

---

## Templates

### Relatório Comparativo de Atribuição de Canais (GA4)

```
# Relatório de Comparação de Modelos de Atribuição (GA4)
Data da Análise: 2024-07-26
Período: 2024-04-01 a 2024-06-30
Métrica de Conversão: purchase (Compras)
Modelos Comparados: Last Click, Data-Driven

| Grupo de Canais Padrão | Conversões (Last Click) | Valor Conv. (Last Click) | Conversões (Data-Driven) | Valor Conv. (Data-Driven) | Diferença % Conv. (DD vs LC) | Diferença % Valor (DD vs LC) | ROAS (Last Click) | ROAS (Data-Driven) |
|------------------------|-------------------------|--------------------------|--------------------------|---------------------------|------------------------------|------------------------------|-------------------|--------------------|
| Organic Search         | 550                     | R$ 55.000,00             | 720                      | R$ 78.000,00              | +30.9%                       | +41.8%                       | 5.5               | 7.8                |
| Paid Search            | 800                     | R$ 120.000,00            | 680                      | R$ 105.000,00             | -15.0%                       | -12.5%                       | 4.0               | 3.5                |
| Direct                 | 300                     | R$ 45.000,00             | 280                      | R$ 42.000,00              | -6.7%                        | -6.7%                        | N/A               | N/A                |
| Email                  | 120                     | R$ 18.000,00             | 160                      | R$ 25.000,00              | +33.3%                       | +38.9%                       | 6.0               | 8.3                |
| Display                | 90                      | R$ 13.500,00             | 140                      | R$ 22.000,00              | +55.6%                       | +63.0%                       | 1.5               | 2.4                |
| Organic Social         | 70                      | R$ 10.500,00             | 90                       | R$ 14.000,00              | +28.6%                       | +33.3%                       | 3.5               | 4.7                |
| Referral               | 50                      | R$ 7.500,00              | 60                       | R$ 9.000,00               | +20.0%                       | +20.0%                       | 2.5               | 3.0                |
| Total                  | 1980                    | R$ 269.000,00            | 2130                     | R$ 295.000,00             | +7.6%                        | +9.7%                        | 3.8               | 4.2                |

**Insights e Recomendações:**
*   **Organic Search e Email:** São significativamente subvalorizados pelo modelo Last Click. O modelo Data-Driven revela que contribuem para um volume maior de conversões e valor. Recomenda-se aumentar o investimento em estratégias de SEO e Email Marketing, focando em conteúdo de topo e meio de funil.
*   **Display:** Apresenta o maior crescimento relativo no modelo Data-Driven, indicando forte papel na fase de awareness e consideração. Considerar aumentar orçamento em campanhas de display para prospecção, apesar de um ROAS absoluto menor, devido ao seu papel como "canal assistido".
*   **Paid Search:** Embora ainda seja um canal forte, o Data-Driven mostra uma contribuição ligeiramente menor que o Last Click, especialmente para termos de marca, onde tende a ser o último clique. Avaliar a eficiência do investimento em termos genéricos e considerar otimizar para CPA em campanhas de fundo de funil.
*   **Diretoria:** Manter monitoramento, pois a atribuição direta muitas vezes mascara impactos de outros canais anteriores.

*Nota: ROAS calculado com base em dados de custo de campanha externos (não inclusos nesta tabela) para Paid Search, Display e Organic Social (para campanhas pagas). Para Direct, Organic Search, Email e Referral, o ROAS é calculado sobre o valor da conversão, assumindo custo zero ou custo de operação indireto.*
```

### Script de Análise de Caminhos de Conversão (Python/Pandas - Exemplo Abstrato)

```python
import pandas as pd

# Simulação de dados de caminhos de conversão do GA4 (exportado via BigQuery ou API)
# Cada linha representa um caminho de um usuário até a conversão
data = {
    'user_id': ['user_1', 'user_2', 'user_3', 'user_4', 'user_5'],
    'path': [
        ['Organic Search', 'Paid Search', 'Direct'],
        ['Display', 'Organic Social', 'Email', 'Direct'],
        ['Paid Search', 'Paid Search', 'Direct'],
        ['Organic Search', 'Email', 'Direct'],
        ['Display', 'Organic Search', 'Paid Search']
    ],
    'conversion_value': [100, 150, 80, 200, 120]
}
df = pd.DataFrame(data)

# Análise de ocorrência de canais no caminho
channel_counts = {}
for path in df['path']:
    for channel in set(path): # Usar set para contar uma vez por caminho
        channel_counts[channel] = channel_counts.get(channel, 0) + 1

print("Ocorrência de canais em caminhos de conversão:")
for channel, count in sorted(channel_counts.items(), key=lambda item: item[1], reverse=True):
    print(f"- {channel}: {count} vezes")

# Cálculo de valor médio da conversão por canal no caminho (simplificado)
channel_value_contribution = {}
for index, row in df.iterrows():
    value_per_channel = row['conversion_value'] / len(set(row['path'])) # Divisão linear simplificada
    for channel in set(row['path']):
        channel_value_contribution[channel] = channel_value_contribution.get(channel, 0) + value_per_channel

print("\nContribuição de valor (Linear Simplificada) por canal:")
for channel, value in sorted(channel_value_contribution.items(), key=lambda item: item[1], reverse=True):
    print(f"- {channel}: R$ {value:.2f}")

# Este script ilustra a lógica. Para dados reais do GA4, seria necessário:
# 1. Exportar dados de "Caminhos de conversão" do GA4 (Publicidade > Atribuição > Caminhos de conversão)
#    ou usar a integração GA4 + BigQuery para um dataset mais robusto.
# 2. Processar a string do caminho para uma lista de canais.
# 3. Aplicar modelos de atribuição mais sofisticados (Markov, Shapley Value) se a análise for fora do GA4.
```

---

## Checklist

- [x] Confirmar que todos os eventos de conversão críticos estão configurados corretamente no GA4 e marcados como conversões.
- [x] Validar que os parâmetros `value` e `currency` estão sendo enviados para os eventos de compra ou lead.
- [x] Analisar o relatório "Caminhos de conversão" no GA4 para entender sequências comuns de interação dos usuários.
- [x] Comparar ativamente "Last Click" e "Data-Driven" no relatório de "Modelos de atribuição e Comparação de modelos" do GA4.
- [x] Avaliar a "Diferença %" entre os modelos para cada canal para identificar sub/supervalorização.
- [x] Ajustar a janela de lookback de atribuição nas configurações do GA4 para refletir o ciclo de vendas real do negócio.
- [x] Considerar a criação de dimensões personalizadas para segmentar a análise de atribuição por tipo de cliente ou produto.
- [x] Integrar os dados de custo de publicidade (Google Ads, Facebook Ads, etc.) no GA4 para um cálculo preciso de ROAS e CPA nos relatórios.
- [x] Compartilhar insights de atribuição com as equipes de mídia e conteúdo para otimização de lances e estratégias.
- [x] Monitorar as tendências dos modelos de atribuição mensalmente para detectar mudanças no comportamento do consumidor.

---

## Métricas de Referência

| Métrica                         | Benchmark (E-commerce) | Meta (E-commerce) | Benchmark (Geração de Leads B2B) | Meta (Geração de Leads B2B) |
|---------------------------------|------------------------|-------------------|----------------------------------|-----------------------------|
| **CPA (Custo por Aquisição)**   | R$ 50 - R$ 150         | < R$ 80           | R$ 200 - R$ 800                  | < R$ 400                    |
| **ROAS (Retorno sobre Invest.)**| 2.5x - 4.0x            | > 3.0x            | N/A (foco em CPL)                | N/A                         |
| **Taxa de Conversão (Site)**    | 1.5% - 3.0%            | > 2.0%            | 3.0% - 6.0%                      | > 4.5%                      |
| **Valor Médio do Pedido (AOV)** | R$ 200 - R$ 500        | > R$ 350          | N/A                              | N/A                         |
| **LTV (Lifetime Value)**        | > 3x CPA               | > 4x CPA          | > 5x CPL                         | > 8x CPL                    |
| **Conversões Assistidas (%)**   | 30% - 60%              | > 40%             | 40% - 70%                        | > 50%                       |

*Benchmarks e metas são altamente dependentes do setor, margens de lucro e estratégia de negócios. Os valores acima são exemplos genéricos para referência.*

---

## Erros Comuns

1.  **Usar apenas o modelo Last Click para todas as decisões de investimento**: O Last Click atribui 100% do crédito ao último ponto de contato. Isso subestima canais que atuam no início da jornada (awareness) ou no meio (consideração).
    *   **Como evitar**: Sempre compare o Last Click com modelos multi-touch como Linear, Time Decay ou, preferencialmente, Data-Driven no GA4. Para um e-commerce de moda, por exemplo, o Last Click pode supervalorizar o "Direct" ou "Paid Search (Marca)", enquanto "Organic Social" e "Display" são cruciais no início da jornada, sendo subestimados.

2.  **Não integrar dados de custo de publicidade no GA4**: Sem os custos de campanha importados, o GA4 não pode calcular métricas de ROI (ROAS, CPA) dentro de seus relatórios, limitando a capacidade de otimização de lances baseada em atribuição.
    *   **Como evitar**: Vincule suas contas de Google Ads, Search Console e Media para importação automática. Para outras plataformas (Facebook Ads, LinkedIn Ads), utilize a importação de dados de custo via CSV ou API na interface do GA4 (Administrador > Conexões de produtos > Importação de dados).

3.  **Ignorar a janela de lookback na análise de atribuição**: Uma janela de lookback muito curta (ex: 7 dias) pode cortar interações importantes que ocorreram antes, especialmente para produtos com ciclo de vendas longo.
    *   **Como evitar**: Ajuste a janela de lookback (Administrador > Configurações de atribuição) para que ela cubra a maioria dos ciclos de vendas. Para um serviço B2B complexo, uma janela de 90 a 120 dias para eventos de conversão é mais realista do que os 30 dias padrão.

---

## Dicas Avançadas

1.  **Utilizar o GA4 + BigQuery para Análise de Atribuição Customizada**: Para análises mais complexas ou modelos de atribuição personalizados (ex: modelo Shapley Value), exporte seus dados brutos do GA4 para o BigQuery. Isso permite construir modelos programaticamente usando SQL, Python ou R, superando as limitações dos modelos pré-definidos do GA4. Por exemplo, você pode criar um modelo de atribuição baseado em Markov Chain para identificar os "caminhos mais prováveis" e a importância de cada canal em transições.

2.  **Segmentação de Audiências nos Relatórios de Atribuição**: Não analise a atribuição de forma homogênea para todos os usuários. Segmente o relatório de "Modelos de atribuição e Comparação de modelos" por "Novo usuário" vs. "Usuário recorrente", ou por "País", "Dispositivo", "Segmento de Audiência" (se configurado). A contribuição dos canais pode variar drasticamente. Por exemplo, o Display pode ter um impacto maior na aquisição de novos usuários, enquanto o Email é mais eficaz para usuários recorrentes.

3.  **Análise de Contribuição de Canais Assistidos**: Embora o GA4 foque nos modelos de atribuição final, é crucial entender os "canais assistidos". Canais que não geram o último clique, mas aparecem em vários pontos antes da conversão, são vitais. No GA4, o relatório "Caminhos de conversão" permite explorar as sequências. Uma análise mais aprofundada via BigQuery pode quantificar o "valor assistido" de cada canal, identificando aqueles que preparam o terreno para a conversão final.

4.  **Implementação de Testes A/B para Modelos de Atribuição**: Para validar a eficácia de um novo modelo de atribuição na otimização de lances, execute testes A/B. Por exemplo, em Google Ads, crie duas campanhas idênticas, mas configure cada uma para otimizar com base em diferentes modelos de atribuição (ex: uma usando Last Click e outra usando Data-Driven). Monitore o ROAS ou CPA de cada campanha para determinar qual modelo resulta em melhor performance de negócio.

5.  **Considerar o Tempo de Ciclo de Vendas e Recorrência**: Para negócios com ciclos de vendas longos ou compras recorrentes, a atribuição deve considerar o LTV (Lifetime Value) e não apenas a conversão inicial. Um canal que gera um cliente com LTV alto pode ter um CPA mais elevado na primeira compra, mas ser mais valioso a longo prazo. Use o GA4 para correlacionar o canal de aquisição inicial com métricas de LTV.