---
name: campaign-audit
description: "Campaign Audit — Skill especializada para campaign audit"
license: MIT
metadata:
  version: 1.0.0
  author: Cafe Code AI
  category: 04-anuncios-trafego
  updated: 2026-03-01
risk: safe
---

# Campaign Audit

Esta skill capacita a realizar auditorias detalhadas e acionáveis em campanhas de Meta Ads, Google Ads e TikTok Ads para otimizar performance e maximizar o retorno sobre o investimento (ROAS).

---

## Keywords

Auditoria de campanhas, Meta Ads, Google Ads, TikTok Ads, otimização de performance, ROAS, CPC, CTR, CPA, segmentação de público, criativos, estratégias de lances, estrutura de conta, funil de conversão, análise de dados, pixel de rastreamento, eventos de conversão, palavras-chave negativas.

---

## Quick Start

1.  **Acesso e Exportação de Dados**: Obtenha acesso total às contas de anúncios (Meta Ads Manager, Google Ads, TikTok Ads Manager). Exporte relatórios de performance dos últimos 30-90 dias, segmentando por campanha, conjunto de anúncios/grupo de anúncios e anúncio/criativo. Inclua métricas como impressões, cliques, CTR, CPC, CPM, custo total, conversões, custo por conversão (CPA) e valor de conversão (ROAS).
2.  **Verificação de Rastreamento**: Confirme a correta implementação do Pixel da Meta, Tag do Google Ads e Pixel do TikTok, e verifique se os eventos de conversão essenciais (PageView, AddToCart, Purchase, Lead) estão disparando corretamente e com o valor atribuído, se aplicável. Use o Gerenciador de Eventos da Meta, Google Tag Assistant e TikTok Pixel Helper.
3.  **Análise de Desempenho Macro**: Compare o desempenho geral da conta com metas predefinidas e benchmarks do setor. Identifique campanhas com ROAS abaixo da meta, CPA muito alto ou CTR muito baixo.
4.  **Identificação de Anomalias**: Busque por picos ou quedas abruptas em métricas-chave. Investigue o contexto: mudanças de orçamento, novos criativos, alterações de público ou sazonalidade.

---

## Core Workflows

### Workflow 1: Auditoria de Estrutura, Objetivos e Segmentação de Campanhas

Este workflow foca na validação da base estratégica das campanhas, assegurando que a estrutura da conta e a segmentação de público estejam alinhadas com os objetivos de negócio e otimizadas para performance.

**Passos Detalhados:**

1.  **Validação de Objetivos de Campanha**:
    *   **Meta Ads**: Em cada campanha, acesse as "Configurações da Campanha" e verifique o "Objetivo de Campanha". Uma campanha de e-commerce com objetivo de "Tráfego" ou "Engajamento" é um erro comum. O ideal para vendas diretas é "Vendas" ou "Leads" para captação.
        *   **Exemplo**: Cliente com e-commerce de moda. Campanha principal de vendas configurada como "Tráfego". **Ação**: Alterar o objetivo para "Vendas" e selecionar a otimização para "Compras" para o algoritmo focar em usuários com maior probabilidade de comprar.
    *   **Google Ads**: Em "Configurações da Campanha", revise o "Objetivo da Campanha". Para e-commerce, garanta que seja "Vendas" ou "Leads", otimizando para "Compras" ou "Envio de Formulário".
        *   **Exemplo**: Campanha de Pesquisa para um SaaS com objetivo "Tráfego do site". **Ação**: Mudar para "Leads" e otimizar para "Envio de Formulário" ou "Início de Teste Gratuito".
    *   **TikTok Ads**: Verifique o "Objetivo de Publicidade". Para vendas, priorize "Vendas" ou "Geração de Leads".
        *   **Exemplo**: Campanha de produto digital usando "Alcance". **Ação**: Mudar para "Vendas" ou "Geração de Leads" com otimização para "Concluir Pagamento" ou "Envio de Formulário".

2.  **Análise de Estrutura de Conta e Granularidade**:
    *   Avalie se a conta está organizada de forma lógica: Campanhas por objetivo, tipo de público (prospecção, remarketing), funil (topo, meio, fundo) ou produto/serviço.
    *   Verifique se há muitos conjuntos/grupos de anúncios com orçamentos muito pequenos, diluindo o aprendizado dos algoritmos.
    *   **Exemplo Meta Ads**: 15 conjuntos de anúncios de prospecção, cada um com R$10/dia. **Ação**: Consolidar públicos semelhantes em 3-5 conjuntos de anúncios com R$50-R$100/dia para dar mais poder ao CBO (Campaign Budget Optimization) ou ABO (Ad Set Budget Optimization) e permitir que o algoritmo encontre o público ideal.
    *   **Exemplo Google Ads**: 5 grupos de anúncios idênticos em palavras-chave, apenas mudando o tipo de correspondência. **Ação**: Consolidar em 1-2 grupos de anúncios com palavras-chave bem agrupadas por tema, aproveitando os tipos de correspondência dentro do mesmo grupo.

3.  **Auditoria de Segmentação de Público**:
    *   **Sobreposição de Públicos**: Utilize a ferramenta de "Sobreposição de Público" no Gerenciador de Anúncios da Meta para identificar públicos que se cruzam significativamente (acima de 20-30%). A sobreposição pode causar concorrência interna e aumentar o CPM.
        *   **Exemplo**: Público "Interesse em Fitness" e "Pessoas que seguem academias" no mesmo topo de funil. **Ação**: Exclua um do outro ou teste campanhas separadas para entender qual performa melhor.
    *   **Exclusões de Público**: Verifique se públicos de remarketing estão sendo excluídos de campanhas de prospecção. Clientes existentes ou leads já convertidos devem ser excluídos de campanhas de "primeira compra".
        *   **Exemplo Meta Ads**: Campanha de prospecção sem exclusão de "Compradores dos últimos 90 dias". **Ação**: Adicionar a lista de "Compradores dos últimos 90 dias" como exclusão para evitar gastar em quem já comprou.
    *   **Tamanho do Público**: Avalie se o público é muito restrito (poucas impressões) ou muito amplo (CPM alto, relevância baixa).
        *   **Exemplo TikTok Ads**: Público com base em interesses muito específicos (<500k pessoas no Brasil). **Ação**: Expandir interesses relacionados ou usar públicos lookalike a partir de 1% para ganhar escala.

### Workflow 2: Análise de Performance de Criativos, Lances e Palavras-chave

Este workflow mergulha nos elementos táticos das campanhas, avaliando a eficácia dos anúncios, a otimização dos lances e a relevância das palavras-chave para garantir que o investimento esteja gerando o melhor resultado possível.

**Passos Detalhados:**

1.  **Performance de Criativos e Anúncios**:
    *   **Meta Ads/TikTok Ads**: Analise o CTR (Click-Through Rate), VTR (View-Through Rate para vídeo), CPM (Custo por Mil Impressões) e a taxa de conversão por anúncio/criativo.
        *   **Exemplo**: Anúncio A (vídeo) tem CTR de 2.5% e CPA de R$ 30, enquanto Anúncio B (imagem) tem CTR de 0.8% e CPA de R$ 80. **Ação**: Pausar o Anúncio B, alocar mais orçamento para o Anúncio A e criar variações do Anúncio A.
        *   **Benchmark**: CTR ideal para Meta/TikTok é geralmente acima de 1.5% para prospecção e 3%+ para remarketing. VTR acima de 30% é bom para vídeos curtos.
    *   **Google Ads (Pesquisa)**: Avalie a "Pontuação de Qualidade" das palavras-chave e a "Relevância do Anúncio". Um baixo "Índice de Qualidade" indica problemas na relação palavra-chave - anúncio - página de destino.
        *   **Exemplo**: Palavra-chave "curso marketing digital" com Índice de Qualidade 3/10. **Ação**: Melhorar a copy do anúncio para incluir mais a palavra-chave, garantir que a landing page tenha conteúdo relevante para "curso marketing digital" e adicionar mais palavras-chave negativas.

2.  **Otimização de Estratégias de Lances e Orçamento**:
    *   **Meta Ads/TikTok Ads**: Verifique se a estratégia de lance está alinhada com o objetivo (ex: "Custo por Resultado" para maximizar conversões, "Maior Volume" para fase de aprendizado).
        *   **Exemplo**: Campanha de vendas usando "Lance Mais Baixo" (maior volume) mas com CPA muito alto. **Ação**: Trocar para "Custo por Resultado" e definir um Custo por Compra (CPA) alvo de, por exemplo, R$45, para dar instrução mais clara ao algoritmo.
    *   **Google Ads**: Analise a estratégia de lances (ex: "Maximizar Conversões", "ROAS Alvo", "CPC Manual"). Para campanhas de performance, "Maximizar Conversões" ou "ROAS Alvo" são geralmente mais eficazes.
        *   **Exemplo**: Campanha de e-commerce com "CPC Manual" e ROAS baixo. **Ação**: Mudar para "Maximizar o Valor da Conversão" com um ROAS Alvo de 300% (3x o investimento) para otimizar automaticamente.
    *   **Distribuição de Orçamento**: Observe onde o orçamento está sendo consumido e se ele está gerando resultados proporcionais.
        *   **Exemplo**: Campanha X consumindo 70% do orçamento total, mas gerando apenas 30% das conversões. **Ação**: Reduzir o orçamento da Campanha X e realocar para campanhas com melhor ROAS ou CPA.

3.  **Análise de Palavras-chave (Google Ads)**:
    *   **Relatório de Termos de Pesquisa**: Identifique termos de pesquisa que estão gerando cliques, mas sem conversões, ou termos irrelevantes.
        *   **Exemplo**: Campanha para "consultoria SEO" está recebendo cliques de "curso SEO gratuito". **Ação**: Adicionar "curso", "gratuito" e "gratis" como palavras-chave negativas de correspondência exata ou de frase.
    *   **Correspondência de Palavras-chave**: Verifique se os tipos de correspondência (exata `[keyword]`, frase `"keyword"`, ampla `keyword`) estão sendo utilizados de forma estratégica para controlar o tráfego e a relevância.
        *   **Exemplo**: Todas as palavras-chave em correspondência ampla, resultando em termos de pesquisa muito genéricos. **Ação**: Converter as palavras-chave de melhor performance para correspondência de frase e exata, e usar ampla modificada ou ampla de forma mais controlada para descoberta.

---

## Templates

### Relatório Simplificado de Auditoria de Campanha (Meta Ads)

```
## Relatório de Auditoria Simplificada - Campanha "Vendas Diretas - Prospecção" (Meta Ads)

**Período da Análise:** 01/01/2024 - 31/01/2024
**Investimento Total:** R$ 5.000,00
**Resultados:** 50 Compras
**CPA Médio:** R$ 100,00
**ROAS:** 1.8 (Valor de Conversão: R$ 9.000,00)
**Benchmark CPA:** R$ 70,00
**Benchmark ROAS:** 3.0

---

**1. Estrutura e Objetivo:**
*   **Status Atual:** Objetivo "Tráfego" configurado para campanha de e-commerce. Orçamento de campanha (CBO) ativo, 8 conjuntos de anúncios ativos.
*   **Problema:** Objetivo "Tráfego" não otimiza para "Compras", resultando em cliques de baixo valor e CPA elevado. Muitos conjuntos de anúncios diluem o orçamento e o aprendizado do algoritmo.
*   **Recomendação:** Alterar objetivo da campanha para "Vendas". Consolidar conjuntos de anúncios por tema ou público-alvo em 3-4 ad sets, com orçamento CBO focado.

**2. Segmentação de Público:**
*   **Status Atual:** Público "Interesses em Moda Casual" e "Comportamento de Compradores Engajados" com 35% de sobreposição. Exclusão de "Compradores 30 dias" ausente.
*   **Problema:** Sobreposição de públicos aumenta o custo e a concorrência interna. Ausência de exclusão gasta em usuários que já converteram.
*   **Recomendação:** Excluir "Compradores 30 dias" da campanha de prospecção. Testar os públicos sobrepostos em campanhas separadas ou combinar os mais performáticos.

**3. Criativos e Anúncios:**
*   **Status Atual:** Anúncio A (Vídeo produto) - CTR 2.8%, CPA R$ 75. Anúncio B (Imagem estática) - CTR 0.9%, CPA R$ 120. Anúncio C (Carrossel) - CTR 1.5%, CPA R$ 90.
*   **Problema:** Anúncio B está performando muito abaixo da média, elevando o CPA geral.
*   **Recomendação:** Pausar Anúncio B. Alocar mais orçamento para Anúncio A. Criar 2-3 novas variações do Anúncio A e testar.

**4. Estratégia de Lances:**
*   **Status Atual:** Estratégia "Lance Mais Baixo" sem limite de custo.
*   **Problema:** Falta de controle sobre o custo por resultado, contribuindo para o CPA acima do benchmark.
*   **Recomendação:** Mudar a estratégia de lance para "Custo por Resultado" com um limite de CPA alvo de R$ 70,00.

**Resumo de Ações Urgentes:**
1.  **Alterar Objetivo da Campanha para "Vendas".**
2.  **Consolidar Conjuntos de Anúncios.**
3.  **Excluir "Compradores 30 dias" da prospecção.**
4.  **Pausar Anúncio B e criar variações do Anúncio A.**
5.  **Mudar estratégia de lance para "Custo por Resultado" (CPA Alvo R$ 70,00).**
```

### Plano de Ação Pós-Auditoria (Google Ads)

```
## Plano de Ação Pós-Auditoria - Campanha "Serviço de Consultoria SEO" (Google Ads)

**Período da Análise:** 01/02/2024 - 29/02/2024
**Investimento Total:** R$ 3.500,00
**Resultados:** 15 Leads (Formulário)
**CPA Médio:** R$ 233,33
**ROAS:** N/A (serviço, foco em CPA)
**Benchmark CPA:** R$ 150,00

---

**1. Rastreamento e Conversões:**
*   **Problema Identificado:** Tag de conversão para "Envio de Formulário" disparando múltiplas vezes por sessão, inflacionando o número de leads.
*   **Ação:** Revisar a implementação da Tag do Google Ads via Google Tag Manager. Adicionar regra de disparo único por página ou usar eventos de "Envio de Formulário" do GA4 para uma contagem mais precisa.
*   **Responsável:** Equipe de Desenvolvimento/Analytics
*   **Prazo:** 05/03/2024

**2. Palavras-chave e Relevância:**
*   **Problema Identificado:** Relatório de Termos de Pesquisa mostra cliques para "curso de seo" e "seo gratuito". Palavra-chave "consultoria seo" com Índice de Qualidade 4/10.
*   **Ação:** Adicionar "curso", "gratuito", "gratis", "aprender" como palavras-chave negativas de correspondência de frase e exata. Otimizar a copy dos anúncios e a landing page para refletir "consultoria seo" de forma mais proeminente, buscando aumentar o Índice de Qualidade.
*   **Responsável:** Gestor de Tráfego
*   **Prazo:** 07/03/2024

**3. Otimização de Lances e Orçamento:**
*   **Problema Identificado:** Estratégia de lance "Maximizar Cliques" com CPA muito alto.
*   **Ação:** Mudar estratégia de lance para "Maximizar Conversões" com um CPA alvo de R$ 150,00. Ajustar o orçamento diário de R$ 120 para R$ 100 para manter o CPA dentro do alvo inicial enquanto otimiza.
*   **Responsável:** Gestor de Tráfego
*   **Prazo:** 04/03/2024

**4. Extensões de Anúncio:**
*   **Problema Identificado:** Apenas extensões de sitelink básicas ativas. Faltam extensões de frase de destaque e snippet estruturado com foco nos diferenciais da consultoria.
*   **Ação:** Criar e implementar extensões de frase de destaque com "Especialistas Certificados", "Atendimento Personalizado", "Resultados Comprovados". Adicionar snippet estruturado para "Serviços: Auditoria SEO, Otimização On-page, Link Building".
*   **Responsável:** Gestor de Tráfego
*   **Prazo:** 08/03/2024

**Monitoramento:** Acompanhar CPA e volume de leads diariamente nas primeiras 2 semanas após as implementações.
```

---

## Checklist

- [X]  Verificar se o objetivo da campanha está alinhado com a meta de negócio (Vendas, Leads, Tráfego).
- [X]  Confirmar a correta implementação e disparo dos eventos de conversão (Pixel da Meta, Tag do Google, Pixel do TikTok).
- [X]  Analisar a sobreposição de públicos entre conjuntos de anúncios (Meta Ads).
- [X]  Auditar as exclusões de público (compradores, leads, visitantes irrelevantes) em campanhas de prospecção.
- [X]  Revisar a performance de CTR, VTR (vídeo), CPM e CPA/ROAS por criativo/anúncio.
- [X]  Validar a estratégia de lances e orçamento (CBO/ABO, CPA Alvo, ROAS Alvo) para otimização.
- [X]  No Google Ads, analisar o Relatório de Termos de Pesquisa e adicionar palavras-chave negativas.
- [X]  No Google Ads, verificar o Índice de Qualidade das palavras-chave e a relevância dos anúncios.
- [X]  Avaliar a coerência entre o anúncio, a página de destino e a oferta (congruência).
- [X]  Analisar a distribuição de orçamento entre campanhas e conjuntos de anúncios, identificando desperdícios.
- [X]  Verificar a frequência de exibição dos anúncios para evitar fadiga de criativo.
- [X]  Conferir a segmentação demográfica e geográfica, ajustando conforme os dados de performance.

---

## Métricas de Referência

| Métrica               | Benchmark (Prospecção) | Benchmark (Remarketing) | Meta (E-commerce) | Meta (Geração de Leads) |
|-----------------------|------------------------|-------------------------|-------------------|-------------------------|
| **CTR (Meta/TikTok)** | 1.0% - 2.0%            | 3.0% - 5.0%             | > 1.8%            | > 1.5%                  |
| **CTR (Google Search)**| 3.0% - 6.0%            | N/A                     | > 4.5%            | > 4.0%                  |
| **CPC (Meta/TikTok)** | R$ 0.80 - R$ 2.50      | R$ 0.30 - R$ 1.00       | < R$ 1.50         | < R$ 2.00               |
| **CPC (Google Search)**| R$ 2.00 - R$ 8.00      | N/A                     | < R$ 5.00         | < R$ 6.00               |
| **ROAS (Meta/Google)**| 1.5 - 2.5              | 4.0 - 8.0               | > 3.0             | N/A                     |
| **CPA (Meta/Google)** | R$ 50 - R$ 150         | R$ 10 - R$ 40           | N/A               | < R$ 80                 |
| **CPM (Meta/TikTok)** | R$ 15 - R$ 35          | R$ 5 - R$ 15            | < R$ 25           | < R$ 30                 |
| **Taxa de Conversão** | 1.0% - 3.0%            | 5.0% - 10.0%            | > 2.5%            | > 2.0%                  |

*Nota: Os benchmarks podem variar significativamente por setor, produto, preço e região.*

---

## Erros Comuns

1.  **Rastreamento de Conversão Incorreto ou Quebrado**: O pixel da Meta ou a tag do Google Ads não está disparando corretamente, ou os eventos de conversão estão configurados de forma errada (ex: Purchase sem valor).
    *   **Como evitar**: Use sempre o Google Tag Manager (GTM) para gerenciar tags. Após qualquer implementação ou alteração, verifique imediatamente o disparo dos eventos usando o Google Tag Assistant, Meta Pixel Helper ou TikTok Pixel Helper, e o "Gerenciador de Eventos" de cada plataforma, testando o fluxo de conversão real.
2.  **Segmentação de Público Muito Ampla sem Exclusões**: Campanhas de prospecção rodando sem exclusão de públicos de remarketing ou compradores recentes. Isso leva a um desperdício de verba, pois você está impactando pessoas que já conhecem ou compraram o produto, com anúncios de topo de funil.
    *   **Como evitar**: Sempre crie e utilize públicos de exclusão para remarketing (ex: "Visitantes do site últimos 30 dias", "Compradores últimos 90 dias") em campanhas de prospecção. Para Meta Ads, utilize a ferramenta de "Sobreposição de Público" para identificar e resolver conflitos entre ad sets.
3.  **Fadiga de Criativo/Anúncio com Frequência Alta**: Um anúncio com alta frequência (ex: 3.5+ em 7 dias) para o mesmo público tende a perder performance, elevando o CPM e reduzindo o CTR, pois o público já viu o anúncio várias vezes.
    *   **Como evitar**: Monitore a métrica de "Frequência" semanalmente. Ao atingir 2.5-3.0, prepare novos criativos ou pause os anúncios fatigados. Teste sempre novas variações de criativos e copies para manter o público engajado.
4.  **Uso Inadequado de Tipos de Correspondência de Palavras-chave (Google Ads)**: Deixar todas as palavras-chave em correspondência ampla sem controle resulta em tráfego irrelevante e gasto excessivo.
    *   **Como evitar**: Utilize uma combinação estratégica de correspondência exata `[termos]`, de frase `"termos"` e ampla `termos`. Comece com frase e exata para palavras-chave de alta intenção e use ampla para descoberta controlada, sempre acompanhando de perto o Relatório de Termos de Pesquisa para adicionar negativos.
5.  **Falta de Testes A/B Consistentes em Criativos e Ofertas**: Rodar a mesma combinação de anúncio por longos períodos sem testar variações impede a descoberta de elementos de maior performance.
    *   **Como evitar**: Implemente uma rotina de testes A/B. Crie 2-3 variações de criativos (imagens, vídeos, copies) por conjunto de anúncios a cada 2-4 semanas. Teste diferentes chamadas para ação (CTAs) e ofertas para identificar quais geram o melhor CPA ou ROAS.

---

## Dicas Avançadas

1.  **Análise de Funil Pós-Clique com GA4**: Não se limite às métricas das plataformas de anúncios. Integre o Google Analytics 4 (GA4) para entender o comportamento do usuário *após* o clique no anúncio. Analise métricas como taxa de rejeição, tempo na página, páginas por sessão e o caminho até a conversão. Isso revela problemas na landing page ou no fluxo de checkout que as plataformas de anúncios não mostram.
    *   **Exemplo Prático**: Uma campanha de Meta Ads tem um CTR alto e um bom CPC, mas o GA4 mostra uma taxa de rejeição de 80% na landing page. Isso indica que, embora o anúncio atraia cliques, a página de destino não é relevante ou engajadora o suficiente.
2.  **Auditoria de "Decay Rate" de Criativos**: Monitore a queda de performance (CTR, CPA) de criativos ao longo do tempo. Crie um gráfico de performance diária ou semanal para cada anúncio principal. Identifique o ponto em que um criativo começa a "cansar" o público e planeje sua substituição *antes* que o desempenho caia drasticamente.
    *   **Exemplo Prático**: Um vídeo no TikTok Ads performa excelentemente por 3 semanas, mas na 4ª semana seu CTR cai de 2.0% para 0.8% e o CPA dobra. Isso é o "decay rate" entrando em ação, indicando que é hora de testar um novo vídeo.
3.  **Uso de Regras Automatizadas para Otimização em Larga Escala**: Para contas com muitas campanhas e conjuntos de anúncios, configure regras automatizadas para otimizações diárias.
    *   **Exemplo Prático (Meta Ads)**: Criar uma regra para pausar anúncios que tenham CPA > R$ 100 e impressões > 5.000 nos últimos 3 dias. Ou uma regra para aumentar o orçamento de campanhas com ROAS > 4.0 em 10% diariamente, limitado a um máximo.
4.  **Análise de Atribuição Multi-Touch**: Utilize modelos de atribuição que vão além do "último clique", como "linear", "baseado em posição" ou "decaimento temporal" no Google Analytics ou no Google Ads. Isso ajuda a valorizar canais de topo de funil (Meta Ads de prospecção, Google Display) que contribuem para a jornada do cliente, mas não recebem o crédito final.
    *   **Exemplo Prático**: Uma campanha de branding no TikTok Ads pode não gerar conversões diretas (último clique), mas ao analisar a atribuição multi-touch, você percebe que muitos usuários expostos a ela convertem posteriormente via pesquisa orgânica ou Google Ads.
5.  **Segmentação Avançada por LTV (Lifetime Value)**: Se houver dados de LTV, crie públicos personalizados e campanhas focadas em clientes de alto valor. No Meta Ads, por exemplo, você pode criar um público personalizado de "Compradores com LTV > X" e usar isso para campanhas de upsell/cross-sell ou como seed para Lookalikes de alto valor.
    *   **Exemplo Prático**: Uma empresa de SaaS identifica seus clientes de maior LTV. Cria um público lookalike de 1% baseado nesses clientes e direciona campanhas de prospecção com ofertas exclusivas, atraindo usuários com maior probabilidade de se tornarem clientes valiosos