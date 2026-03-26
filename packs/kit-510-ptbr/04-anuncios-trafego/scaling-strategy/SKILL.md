---
name: scaling-strategy
description: "Scaling Strategy — Skill especializada para scaling strategy"
license: MIT
metadata:
  version: 1.0.0
  author: Cafe Code AI
  category: 04-anuncios-trafego
  updated: 2026-03-01
risk: safe
---

# Scaling Strategy

Esta skill capacita o Claude a implementar e otimizar estratégias de escala para campanhas de anúncios digitais em Meta Ads, Google Ads e TikTok Ads, maximizando o ROAS e o volume de conversões.

---

## Keywords

Vertical Scaling, Horizontal Scaling, CBO, ABO, Target ROAS, Lookalike Audiences, Performance Max, Broad Audiences, Bid Cap, Cost Cap, Creative Refresh, Ad Fatigue, Budget Allocation, Incrementality Test.

---

## Quick Start

1.  Analise o ROAS ou CPA das campanhas ativas nas últimas 72 horas para identificar aquelas com performance 20% acima da meta e margem para escala.
2.  Aumente o orçamento de campanhas CBO (Meta Ads) em 15-20% a cada 48-72 horas, desde que o ROAS se mantenha estável ou com queda controlada (máximo 10%).
3.  Duplique o conjunto de anúncios com melhor ROAS/CPA (Google Ads) e teste um Target CPA 10% menor ou Target ROAS 15% maior, usando o mesmo criativo e audiência.
4.  Lance uma campanha de teste (TikTok Ads) com audiência Lookalike de 1% baseada em "Compradores (últimos 90 dias)" e orçamento de R$150/dia.

---

## Core Workflows

### Workflow 1: Escala Vertical Sustentável em Meta Ads com CBO

Este workflow detalha a estratégia de aumento de orçamento para campanhas de conversão em Meta Ads, focando na sustentabilidade do ROAS e prevenção de "ad fatigue".

**Passos Detalhados:**

1.  **Identificação de Campanha Candidata:**
    *   Monitore campanhas de Vendas (CBO) que consistentemente entregam um ROAS pelo menos 20% acima da meta nos últimos 3 a 5 dias.
    *   **Exemplo:** Campanha "Vendas - Coleção Inverno 2024" com ROAS médio de 3.5x nas últimas 72h, enquanto o ROAS alvo é 2.8x. Orçamento atual R$ 600/dia, gerando 15-20 compras diárias.
    *   Verifique se o conjunto de anúncios principal não está com alta frequência (> 3.0 em 7 dias) ou CPM em ascensão acentuada, indicando "ad fatigue".

2.  **Análise de Janela de Atribuição e Estabilidade:**
    *   Confirme que o ROAS é estável na janela de atribuição principal (ex: 7 dias clique, 1 dia visualização).
    *   Verifique o custo por compra (CPA) diário e semanal. Evite escalar se o CPA estiver flutuando muito ou em tendência de alta nas últimas 24-48h.
    *   **Exemplo:** O CPA médio está em R$ 40. Não escale se o CPA das últimas 24h for R$ 55, mesmo com bom ROAS total.

3.  **Aumento Gradual do Orçamento:**
    *   Aumente o orçamento da campanha CBO em incrementos de 15-20% a cada 48-72 horas.
    *   **Exemplo Prático:**
        *   Orçamento inicial: R$ 600/dia.
        *   Aumento 1 (Dia 1): R$ 600 + 20% = R$ 720/dia.
        *   Aguarde 48-72h, monitore ROAS e CPA.
        *   Se ROAS > 3.0x: Aumento 2 (Dia 3/4): R$ 720 + 20% = R$ 864/dia.
        *   Continue este processo, sempre observando as métricas.
    *   **Dica:** Aumentos maiores podem "chocar" o algoritmo, levando a CPA mais alto e ROAS menor temporariamente.

4.  **Manutenção e Otimização Contínua:**
    *   Enquanto escala, continue testando novos criativos dentro da mesma campanha CBO. Pause anúncios com CTR abaixo de 1.5% ou CPM significativamente acima da média da campanha.
    *   Monitore a frequência dos anúncios e o CPM. Se a frequência ultrapassar 3.5 em 7 dias e o CPM subir 20% sem melhora no ROAS, é hora de renovar os criativos ou expandir a audiência.
    *   **Exemplo:** Se um vídeo que performava bem agora tem CTR de 1.2% e CPM de R$ 50, enquanto a média é R$ 35, pause-o e insira um novo vídeo com ângulo diferente.

### Workflow 2: Expansão Horizontal de Audiência e Plataforma em Google Ads e TikTok Ads

Este workflow foca em encontrar novas fontes de volume de conversões, expandindo para novas audiências e explorando outras plataformas.

**Passos Detalhados:**

1.  **Identificação de Oportunidades de Expansão:**
    *   Analise o teto de volume das campanhas atuais. Uma campanha de Google Search com ROAS 5x, mas que gasta apenas R$ 200/dia de um orçamento potencial de R$ 1000/dia, indica volume limitado para a audiência atual.
    *   Considere o estágio do funil de marketing. Se as campanhas de retargeting e lookalikes de 1% estão saturadas, explore lookalikes mais amplas ou audiências abertas.

2.  **Teste de Audiências Lookalike em TikTok Ads:**
    *   Crie diferentes segmentos de audiência Lookalike com base em eventos de pixel de alta intenção, como "Adicionar ao Carrinho" ou "Iniciação de Checkout".
    *   **Exemplo Prático:**
        *   Crie uma audiência Lookalike 1% baseada em "Iniciação de Checkout (últimos 60 dias)".
        *   Crie outra audiência Lookalike 3% baseada em "Visualização Completa de Produto (últimos 90 dias)".
        *   Lance campanhas de teste separadas para cada uma, com orçamento inicial de R$ 100-150/dia por audiência, otimizando para "Comprar". Use criativos de alta performance da Meta Ads ou novos criativos nativos do TikTok.
        *   **Configurações de Lances (TikTok Ads):** Experimente `Bid Cap` R$ 45 ou `Cost Cap` R$ 38 para controlar o CPA inicial.

3.  **Expansão para Google Performance Max:**
    *   Para Google Ads, se campanhas de Search e Shopping atingiram seu limite, configure uma campanha Performance Max.
    *   **Configuração Detalhada:**
        *   Inclua todos os tipos de assets (texto, imagem, vídeo), feeds de produtos (se for e-commerce), e sinais de audiência (listas de clientes, visitantes do site, listas de remarketing).
        *   **Exemplo de Sinal de Audiência:** Upload de lista de e-mails de clientes (Match Rate > 60%), lista de visitantes do site (últimos 180 dias), e interesses como "Compradores Online de Roupas".
        *   Defina `Target ROAS` (se e-commerce) ou `Target CPA` (se lead gen) com base na performance média da conta (ex: Target ROAS 300% se a média é 350%).
        *   Inicie com um orçamento 20-30% do que você gasta nas campanhas de Search e Shopping mais performáticas, e escale gradualmente.

4.  **Análise de Resultados e Realocação de Orçamento:**
    *   Após 7-10 dias de teste, compare o CPA e ROAS das novas audiências/campanhas com as referências da conta.
    *   **Exemplo:**
        *   Se a Lookalike 1% do TikTok Ads atingir um CPA de R$ 42 e ROAS de 2.5x (meta: CPA < R$ 45, ROAS > 2.2x), aumente o orçamento dela em 20%.
        *   Se a campanha Performance Max no Google Ads atingir ROAS 3.2x (meta: 3.0x), realoque 20% do orçamento de campanhas de Google Shopping menos eficientes para ela.
    *   Desative ou ajuste as campanhas que não atingirem as métricas esperadas após o período de teste.

---

## Templates

### Plano de Aumento de Orçamento Meta Ads (CBO)

```
Campanha ID: 987654321 - Vendas - Calçados Femininos Verão
Objetivo: Aumentar volume de compras em 30% mantendo ROAS > 2.8x
Orçamento Atual (CBO): R$ 800/dia
ROAS Médio (7D): 3.6x
CPA Médio (7D): R$ 45
Frequência Média (7D): 2.8
Passo 1: Aumentar orçamento para R$ 960 (+20%) em 2024-08-01 14:00 BRT.
Observações: Monitorar CPM, Frequência, ROAS 1D Click e CPA 1D Click nas próximas 48h.
Passo 2 (se ROAS >= 3.0x em 48h): Aumentar para R$ 1150 (+20%) em 2024-08-03 14:00 BRT.
Contingência: Se ROAS cair abaixo de 2.7x ou CPA subir acima de R$ 55, reverter para orçamento anterior e analisar performance dos criativos. Planejar teste A/B de novos criativos.
```

### Plano de Teste de Audiência Google Ads Performance Max

```
Nome da Campanha: PMax - Expansão de Mercado - Produto Premium
Objetivo: Gerar 100 novas conversões (compras) com CPA < R$ 70 e ROAS > 3.0x
Orçamento Diário: R$ 300
Data de Início: 2024-08-05
Data de Fim (Teste Inicial): 2024-08-19 (14 dias)
Sinais de Audiência:
  - Lista de Clientes Atuais (Email Hash): Upload concluído.
  - Visitantes do Site (Últimos 90 dias): Incluído.
  - Segmento Personalizado: Pessoas que pesquisaram "relógio de luxo feminino", "joias artesanais".
  - Interesses: Compradores de produtos de luxo, entusiastas de moda.
Assets:
  - Títulos: "Relógios de Luxo Exclusivos", "Coleção Limitada", "Estilo e Sofisticação".
  - Descrições: "Descubra a elegância da nossa nova coleção de relógios.", "Design único, qualidade superior, entrega rápida."
  - Imagens: 5 imagens de alta resolução dos produtos.
  - Vídeos: 2 vídeos curtos (15s, 30s) de estilo de vida com os produtos.
  - Feed de Produtos: Conectado ao Google Merchant Center.
Estratégia de Lances: Maximize o valor da conversão com Target ROAS de 320%.
Métricas de Monitoramento: ROAS, CPA, Volume de Conversões, Custo por Cliente Adquirido.
Ação Pós-Teste: Se ROAS > 3.0x, escalar orçamento em 25% semanalmente. Se ROAS < 2.5x, pausar e revisar assets e sinais de audiência.
```

---

## Checklist

- [x] Verificar ROAS/CPA das campanhas nas últimas 72h e 7 dias, identificando tendências.
- [x] Analisar "Ad Fatigue" (frequência, CPM, CTR) dos criativos de maior gasto em Meta/TikTok Ads.
- [x] Confirmar a janela de atribuição e modelo de atribuição (ex: 7D click, 1D view) para garantir dados consistentes.
- [x] Avaliar se a capacidade operacional (estoque, logística, atendimento) consegue absorver o aumento de tráfego/vendas.
- [x] Testar novos ângulos criativos e formatos (vídeo, carrossel, imagem) em campanhas de escala pelo menos semanalmente.
- [x] Implementar estratégias de "bid cap" ou "cost cap" em Meta/TikTok Ads para controlar o custo por resultado em campanhas de teste.
- [x] Segmentar audiências lookalike em diferentes porcentagens (1%, 3%, 5%) para testes de performance e expansão.
- [x] Alocar 10-20% do orçamento total de mídia paga para testes incrementais de novas audiências, plataformas ou formatos.
- [x] Revisar a saúde da conta (Meta: Account Health; Google: Recomendações de Otimização) para identificar problemas técnicos ou de políticas.
- [x] Considerar o impacto de sazonalidade, eventos ou promoções futuras na performance de escala.
- [x] Analisar o share of voice competitivo em Google Search para identificar oportunidades de lances mais agressivos.
- [x] Verificar a qualidade das landing pages para garantir que estão otimizadas para conversão em alto volume.

---

## Métricas de Referência

| Métrica | Benchmark (e-commerce Brasil) | Meta (Exemplo) |
|---------|-------------------------------|----------------|
| CTR     | 1.5% - 3.5%                   | > 2.0%         |
| CPC     | R$ 0.80 - R$ 2.50             | < R$ 1.60      |
| CPM     | R$ 15 - R$ 45                 | < R$ 32        |
| ROAS    | 2.5x - 4.0x                   | > 3.0x         |
| CPA     | R$ 30 - R$ 80                 | < R$ 55        |
| Frequência (7D) | 2.5 - 3.5                   | < 3.0          |

---

## Erros Comuns

1.  **Escalar orçamento de forma muito agressiva**: Aumentar o orçamento em 50% ou mais de uma única vez pode desestabilizar os algoritmos de otimização das plataformas, levando a picos de CPA e uma queda acentuada no ROAS.
    *   **Como evitar**: Implementar aumentos graduais de 15-20% no orçamento a cada 48-72 horas, permitindo que o algoritmo se adapte e encontre novas oportunidades de conversão. Exemplo: Em vez de ir de R$500 para R$1000/dia, faça R$500 -> R$600 -> R$720 -> R$864.
2.  **Ignorar "Ad Fatigue" (Fadiga de Anúncio)**: Continuar usando os mesmos criativos por um período prolongado em campanhas de alto orçamento eleva o CPM e reduz o CTR, pois a audiência já viu o anúncio múltiplas vezes.
    *   **Como evitar**: Implementar um cronograma de teste e renovação de criativos semanalmente. Pause criativos com frequência > 3.5 (7 dias) e CTR < 1.0%. Crie 3-5 novos criativos (vídeos, imagens, carrosséis) com ângulos e mensagens diferentes para testar e substituir os fatigados.
3.  **Não expandir audiência ou plataforma em paralelo à escala vertical**: Focar apenas no aumento de orçamento das campanhas existentes limita o potencial de crescimento e torna a escala insustentável a longo prazo, pois se atinge o "teto" da audiência.
    *   **Como evitar**: Alocar 15-25% do orçamento total para testes de novas audiências (ex: lookalikes 3-5%, audiências amplas com otimização forte) e explorar novas plataformas (ex: se o foco é Meta/Google, teste TikTok Ads). Exemplo: Se gasta R$2000/dia em Meta Ads, destine R$400/dia para testar novas audiências no Meta ou uma nova campanha no TikTok.

---

## Dicas Avançadas

1.  **Implementar Bidding Estratégico com Cost/Bid Caps (Meta e TikTok Ads)**: Quando o ROAS começa a cair em escala, use `Cost Cap` ou `Bid Cap` para forçar o algoritmo a buscar conversões dentro de um limite de custo específico. Isso pode estabilizar o CPA, mas pode reduzir o volume.
    *   **Exemplo Prático**: Uma campanha de Vendas em Meta Ads tem um CPA médio de R$ 45. Ao escalar, o CPA subiu para R$ 60. Crie um novo conjunto de anúncios com `Cost Cap` de R$ 50 para tentar otimizar a um custo controlável.
2.  **Utilizar Audiências Broad (Amplos) com Bidding Otimizado (Meta Ads e Google Performance Max)**: Em vez de segmentar audiências muito específicas, confie no algoritmo para encontrar os melhores compradores em audiências amplas (ex: "Brasil - 18+"). Isso funciona melhor com pixels bem treinados e muitos dados de conversão.
    *   **Exemplo Prático**: No Meta Ads, crie uma campanha de Vendas com uma audiência sem segmentação de interesses/comportamentos, apenas localização e idade, otimizando para "Comprar". No Google PMax, use todos os sinais de audiência, mas não restrinja excessivamente.
3.  **Aproveitar "Value-Based Bidding" (Lances Baseados em Valor)**: Em Google Ads (Target ROAS) e Meta Ads (Maximum Value), otimize para o valor da conversão, não apenas para a conversão. Isso direciona o tráfego para clientes que tendem a gastar mais, maximizando o ROAS em escala.
    *   **Exemplo Prático**: Para um e-commerce, configure o `Target ROAS` em 350% no Google Shopping. No Meta Ads, use a otimização para "Valor Máximo" se o pixel estiver configurado para passar o valor de compra.
4.  **Teste de Incremento (Incrementality Testing)**: Para validar se a escala está realmente trazendo novos clientes e não apenas canibalizando outras fontes, realize testes de incremento. Isso envolve pausar anúncios em uma região ou segmento de audiência para medir o impacto nas vendas orgânicas ou de outros canais.
    *   **Exemplo Prático**: Selecione 2 estados com perfis demográficos e de compra similares. Em um deles, pause temporariamente todas as campanhas pagas por 7-10 dias (grupo de controle). No outro, mantenha a escala ativa (grupo de teste). Compare as vendas totais (orgânicas + diretas) entre os grupos para estimar o incremento real.
5.  **Segmentação Geográfica por Performance em Google Ads**: Ao escalar campanhas de Google Search ou Display, analise o desempenho por localização geográfica. Se uma cidade ou estado tem ROAS significativamente maior e CPA menor, crie campanhas específicas para essa região com orçamentos mais agressivos e lances otimizados.
    *   **Exemplo Prático**: Se a análise de Google Analytics mostra que o estado de São Paulo tem um ROAS 20% maior que a média nacional para suas campanhas de Search, crie uma nova campanha de Search focada apenas em São Paulo, com um orçamento 30% maior e um Target CPA 10% mais baixo.