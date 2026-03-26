---
name: competitive-analysis
description: "Competitive Analysis — Skill especializada para competitive analysis"
license: MIT
metadata:
  version: 1.0.0
  author: Cafe Code AI
  category: 15-analytics-dados
  updated: 2026-03-01
risk: safe
---

# Competitive Analysis

Esta skill capacita o Claude a realizar análises competitivas aprofundadas utilizando dados do Google Analytics 4, identificando lacunas e oportunidades estratégicas no mercado digital.

---

## Keywords

GA4 Competitive Benchmarking, Share of Search, Análise de Funil Competitivo, Attribution Model Comparison, Customer Journey Mapping (Concorrente), Conteúdo de Alta Performance (Concorrente), Métricas de Engajamento Comparativas, Estratégia de SEO Competitiva, Análise de Segmentos de Audiência, LTV Competitivo, Análise de Campanhas Pagas (Estimativa), Otimização de Conversão Competitiva.

---

## Quick Start

1.  **Configurar eventos de engajamento no GA4 para benchmark interno**: Implementar eventos personalizados no GA4 como `scroll_90_percent` (quando o usuário rola 90% da página) e `time_on_page_threshold` (ex: 60 segundos) para medir engajamento profundo em seu site, estabelecendo uma base de comparação para inferir o desempenho de concorrentes.
2.  **Identificar concorrentes e coletar dados de tráfego externo**: Utilizar ferramentas como SimilarWeb ou SEMrush para obter estimativas de tráfego, fontes de tráfego, e comportamento do usuário (tempo na página, taxa de rejeição) para 3-5 concorrentes diretos e 2-3 indiretos.
3.  **Criar um relatório de "Exploração de Funil" no GA4 para simular jornadas de clientes**: Configure um funil no GA4 para o seu site (ex: `visualização_produto` > `adicionar_ao_carrinho` > `checkout` > `compra`) e compare as taxas de abandono com benchmarks do setor e dados inferidos dos concorrentes.
4.  **Exportar dados de engajamento do GA4 e integrar com insights competitivos no Looker Studio**: Criar um dashboard no Looker Studio que combine suas métricas de engajamento do GA4 (taxa de conversão, tempo médio de engajamento) com os dados de tráfego e palavras-chave dos concorrentes obtidos via ferramentas de terceiros, visualizando oportunidades.

---

## Core Workflows

### Workflow 1: Análise de Share of Search e Otimização de Funil de Conversão do Concorrente (GA4 e Ferramentas Externas)

Este workflow detalha como combinar dados do GA4 com informações de ferramentas de inteligência competitiva para entender o share of search dos concorrentes e identificar pontos fracos em seus funis de conversão.

1.  **Identificação de Concorrentes Chave e Palavras-chave de Domínio**:
    *   **Ação**: Usar SEMrush ou Ahrefs para identificar os 5 principais concorrentes que ranqueiam para suas palavras-chave mais estratégicas. Exemplo de consulta no SEMrush: `site_concorrente.com.br` -> `Organic Research` -> `Positions` para ver as palavras-chave principais e seu volume de tráfego.
    *   **Exemplo Prático**: Para um e-commerce de eletrônicos, o SEMrush pode revelar que "LojaConcorrenteX.com.br" domina "melhor smartphone custo-benefício" com 15.000 visitas/mês e posição 1.
2.  **Coleta de Dados de Tráfego e Engajamento do Concorrente (Estimado)**:
    *   **Ação**: Utilizar SimilarWeb para estimar o tráfego total, fontes de tráfego (direto, orgânico, pago, social, referência) e métricas de engajamento (tempo médio na página, taxa de rejeição) dos concorrentes.
    *   **Exemplo Prático**: SimilarWeb mostra que "LojaConcorrenteY.com.br" tem 2M visitas/mês, com 40% de tráfego orgânico, tempo médio na página de 2:10 e taxa de rejeição de 55%.
3.  **Construção de Funil de Conversão Competitivo (Inferido)**:
    *   **Ação**: No GA4, criar um "Exploração de Funil" para o seu site com as etapas críticas (ex: `page_view` `/categoria/` -> `add_to_cart` -> `purchase`). Compare suas taxas de abandono em cada etapa com benchmarks da indústria e com o desempenho *inferido* dos concorrentes (baseado em reviews, estrutura do site, e dados de engajamento externos).
    *   **Exemplo Prático**:
        *   **GA4**: `Explorações` -> `Funil de Conversão`.
        *   **Etapa 1**: `event_name` = `page_view` com `page_location` contendo `/eletronicos/`
        *   **Etapa 2**: `event_name` = `add_to_cart`
        *   **Etapa 3**: `event_name` = `purchase`
        *   **Análise**: Se seu funil mostra 75% de abandono entre `add_to_cart` e `purchase`, e o benchmark da indústria é 70%, há uma oportunidade. Para o concorrente, podemos inferir que se ele tem um tempo médio na página menor e maior taxa de rejeição, seu funil pode ser menos eficiente em etapas iniciais.
4.  **Análise de Atribuição de Tráfego Competitiva (Estimada)**:
    *   **Ação**: No GA4, analisar os relatórios de "Modelos de Atribuição" e "Caminhos de Conversão" para entender como os diferentes canais contribuem para suas conversões. Use essa visão para inferir como os concorrentes podem estar orquestrando suas campanhas, combinando dados de SEMrush (anúncios pagos, tráfego orgânico) e SimilarWeb (fontes de tráfego).
    *   **Exemplo Prático**: Seu GA4 (Relatórios -> Publicidade -> Atribuição -> Modelos de Atribuição) revela que "Display" tem um papel significativo como primeiro toque no modelo "Baseado em Dados". Se o SEMrush mostra que o concorrente "LojaConcorrenteZ.com.br" investe pesadamente em display, é provável que ele também utilize essa estratégia para awareness.
    *   **Fórmula**: CPA (Custo Por Aquisição) = Custo Total da Campanha / Número de Conversões. Compare seu CPA por canal no GA4 com estimativas de CPA de mercado para o segmento do concorrente.

### Workflow 2: Identificação de Oportunidades de Conteúdo e SEO Através de Benchmarking GA4

Este workflow foca em usar o GA4 em conjunto com ferramentas de SEO para identificar lacunas de conteúdo e palavras-chave onde os concorrentes superam e você pode otimizar.

1.  **Identificação das Páginas de Maior Desempenho no GA4 (Seu Site)**:
    *   **Ação**: Acessar `Relatórios` -> `Engajamento` -> `Páginas e Telas` no GA4. Ordenar por `Visualizações` e `Tempo médio de engajamento`. Filtrar por `path da página` para focar em artigos de blog ou páginas de produto específicas.
    *   **Exemplo Prático**: Sua página `/blog/guia-smartphones-2024` tem 10.000 visualizações/mês e um tempo médio de engajamento de 3:15.
2.  **Análise de Conteúdo dos Concorrentes com Ferramentas SEO**:
    *   **Ação**: Usar Ahrefs ou SEMrush para identificar as páginas com maior tráfego orgânico dos seus concorrentes. Analisar os tópicos, formatos de conteúdo, e palavras-chave para as quais essas páginas ranqueiam.
    *   **Exemplo Prático**: No Ahrefs, `Site Explorer` -> `nomedoconcorrente.com.br` -> `Top Pages`. Identifica que "ConcorrenteTech.com" tem um artigo `/review-melhor-tv-4k` com 25.000 visitas/mês, ranqueando para 500 palavras-chave, incluindo "melhor tv 4k custo-benefício".
3.  **Comparação de Métricas de Engajamento e Oportunidades**:
    *   **Ação**: Comparar o `Tempo Médio de Engajamento` e `Taxa de Conversão` (se aplicável, usando eventos de conversão no GA4 como `gerar_lead` ou `add_to_cart`) das suas páginas com os dados de engajamento estimados dos concorrentes (SimilarWeb) e o potencial de tráfego (Ahrefs/SEMrush).
    *   **Exemplo Prático**: Sua página `/blog/guia-smartphones-2024` tem um bom engajamento, mas a página do concorrente sobre "review de TV 4K" tem mais tráfego e provavelmente mais leads. Isso sugere uma oportunidade para você criar um review detalhado sobre "melhores TVs 4K" com foco em conversão (ex: link para produtos afiliados).
4.  **Mapeamento de Lacunas de Conteúdo e Tópicos**:
    *   **Ação**: Criar uma matriz comparativa dos tópicos de conteúdo que você aborda vs. os concorrentes. Priorizar tópicos onde os concorrentes ranqueiam bem e você tem pouca ou nenhuma cobertura, ou onde seu conteúdo é superficial.
    *   **Exemplo Prático**: Matriz revela que você não tem conteúdo aprofundado sobre "gamificação em e-commerce", enquanto um concorrente direto tem 3 artigos de blog com alto tráfego orgânico sobre o tema.

---

## Templates

### Template de Análise Competitiva de Conteúdo e SEO

```
# Relatório de Análise Competitiva de Conteúdo - Mês/Ano

**Análise Geral:**
- **Seu Site:** Seusite.com.br
- **Concorrente Primário:** Concorrente1.com.br
- **Concorrente Secundário:** Concorrente2.com.br

**Métricas Chave de Desempenho (Seu Site - GA4):**
- **Sessões Mês Anterior:** 150.000
- **Usuários Ativos:** 120.000
- **Tempo Médio de Engajamento:** 1:45
- **Taxa de Conversão (Eventos 'purchase'):** 1.8%
- **Páginas Mais Acessadas (GA4):**
    - /blog/melhores-laptops (15.000 visualizações, 2:30 engajamento)
    - /produtos/smartphone-xyz (10.000 visualizações, 1:40 engajamento)

**Tabela de Comparação de Conteúdo e SEO (Concorrentes):**

| URL da Página (Concorrente) | Tópico Principal | Tráfego Orgânico Estimado (SEMrush) | Palavras-chave Ranqueadas (Top 5) | Tempo Médio de Engajamento (Estimado SimilarWeb) | Oportunidade |
|-----------------------------|------------------|------------------------------------|-----------------------------------|--------------------------------------------------|--------------|
| Concorrente1.com.br/guia-notebooks-gamers | Guia Notebooks Gamers | 22.000 | notebook gamer barato, melhor notebook gamer | 3:45 | Criar um guia mais atualizado, com vídeo e comparativo de performance. |
| Concorrente1.com.br/review-tv-oled | Review TV OLED | 18.000 | tv oled vale a pena, tv oled 2024 | 4:10 | Desenvolver review detalhado com foco em custo-benefício e dicas de calibração. |
| Concorrente2.com.br/fones-bluetooth-esporte | Fones Bluetooth Esporte | 12.000 | fone esporte sem fio, melhor fone corrida | 2:50 | Produzir conteúdo comparativo com teste de resistência à água e bateria. |
| Concorrente2.com.br/melhor-cadeira-gamer | Cadeira Gamer | 10.000 | cadeira gamer boa e barata, cadeira escritório gamer | 2:15 | Mapear lacunas nas palavras-chave do concorrente e criar um review focado em ergonomia. |

**Conclusões e Recomendações:**
- O Concorrente1 domina o segmento de reviews aprofundados para produtos de alto valor. Priorizar a criação de conteúdo similar, com foco em dados técnicos e comparativos.
- Há uma lacuna em "acessórios para esportes" que o Concorrente2 explora. Investigar a criação de conteúdo relevante para esse nicho.
- Otimizar o tempo de engajamento das suas páginas de produto com mais vídeos e FAQs interativas, visando superar a média dos concorrentes.
```

### Template de Dashboard de Benchmarking de Funil de Conversão (Looker Studio - Exemplo de Dados)

```
# Dashboard de Benchmarking de Funil de Conversão - Período: Últimos 30 dias

**Visão Geral:**
- **Taxa de Conversão Geral (Seu Site - GA4):** 2.1%
- **Taxa de Abandono Média do Funil (Seu Site - GA4):** 68%
- **Benchmark da Indústria (E-commerce Geral):** 1.8% Conversão, 70% Abandono

**Gráfico: Funil de Conversão (Seu Site vs. Benchmark da Indústria)**
```
(Gráfico de funil visualizado no Looker Studio, comparando barras)
Etapa 1: Visitas (Página Inicial/Categoria)
    Seu Site: 100.000
    Benchmark: 100.000
Etapa 2: Visualizações de Produto (Eventos 'view_item')
    Seu Site: 45.000 (45% de conversão da Etapa 1)
    Benchmark: 40.000 (40% de conversão da Etapa 1)
Etapa 3: Adição ao Carrinho (Eventos 'add_to_cart')
    Seu Site: 15.000 (33% de conversão da Etapa 2)
    Benchmark: 14.000 (35% de conversão da Etapa 2)
Etapa 4: Início do Checkout (Eventos 'begin_checkout')
    Seu Site: 8.000 (53% de conversão da Etapa 3)
    Benchmark: 7.000 (50% de conversão da Etapa 3)
Etapa 5: Compra (Eventos 'purchase')
    Seu Site: 2.100 (26% de conversão da Etapa 4)
    Benchmark: 1.800 (25% de conversão da Etapa 4)
```

**Tabela de Métricas Detalhadas por Etapa (Seu Site - GA4):**

| Etapa do Funil | Usuários na Etapa | Taxa de Abandono (da Etapa Anterior) | Tempo Médio na Etapa |
|----------------|-------------------|--------------------------------------|----------------------|
| Visitas        | 100.000           | N/A                                  | 0:45                 |
| Visualizações de Produto | 45.000            | 55%                                  | 1:20                 |
| Adição ao Carrinho | 15.000            | 67%                                  | 0:50                 |
| Início do Checkout | 8.000             | 47%                                  | 1:05                 |
| Compra         | 2.100             | 74%                                  | 0:30                 |

**Insights e Ações Sugeridas:**
- A maior taxa de abandono do seu funil ocorre entre 'Início do Checkout' e 'Compra' (74%), significativamente acima do benchmark de 65% para essa etapa.
- **Ação:** Investigar formulários de checkout, opções de pagamento e custos de frete. Realizar testes A/B para otimizar essa etapa crítica.
- Sua taxa de conversão de 'Visitas' para 'Visualizações de Produto' (45%) é superior ao benchmark (40%), indicando boa atração inicial.
```

---

## Checklist

- [ ] Configurar eventos personalizados no GA4 para medir engajamento profundo (ex: `scroll_90_percent`, `video_play`).
- [ ] Identificar e listar 3-5 concorrentes diretos e 2-3 indiretos, com seus respectivos domínios.
- [ ] Coletar estimativas de tráfego, fontes de tráfego e métricas de engajamento (tempo na página, taxa de rejeição) para cada concorrente via SimilarWeb/SEMrush.
- [ ] Criar um relatório de "Exploração de Funil" no GA4 para o seu site e comparar as taxas de abandono por etapa com benchmarks do setor.
- [ ] Analisar o relatório de "Modelos de Atribuição" no GA4, focando no modelo "Baseado em Dados", para entender o valor de cada canal na sua jornada e inferir a estratégia dos concorrentes.
- [ ] Utilizar ferramentas de SEO (Ahrefs, SEMrush) para identificar as 10 principais palavras-chave orgânicas para as quais seus concorrentes ranqueiam e que você não cobre.
- [ ] Monitorar as "Páginas e Telas" mais visitadas pelos concorrentes (via SimilarWeb/Ahrefs) para identificar tópicos de conteúdo de sucesso.
- [ ] Segmentar audiências no GA4 para "usuários que visualizam páginas de produto, mas não adicionam ao carrinho" e "compradores recorrentes", analisando seu comportamento para inferir estratégias de CRO e retenção dos concorrentes.
- [ ] Criar um dashboard no Looker Studio integrando dados do GA4 (seu site) e ferramentas de terceiros (concorrentes) para uma visualização holística da análise competitiva.
- [ ] Documentar as principais lacunas de conteúdo e oportunidades de otimização de funil identificadas.

---

## Métricas de Referência

| Métrica                      | Benchmark da Indústria (E-commerce) | Meta para Superar |
|------------------------------|-------------------------------------|-------------------|
| Taxa de Conversão E-commerce | 1.5% - 2.5%                         | 3.0%              |
| Taxa de Rejeição (Conteúdo)  | 40% - 60%                           | < 45%             |
| Tempo Médio de Engajamento (Sessão) | 60s - 120s                          | > 90s             |
| Taxa de Abandono de Carrinho | 65% - 80%                           | < 70%             |
| Custo por Aquisição (CPA) - Digital | R$20 - R$80                         | < R$50            |
| Share of Voice (Orgânico)    | Varia muito por nicho               | Aumento de 10%    |

---

## Erros Comuns

1.  **Comparar métricas de GA4 sem contexto de mercado ou volume de tráfego do concorrente**: Apenas observar sua Taxa de Rejeição de 50% e comparar com um "benchmark" de 40% sem considerar que o concorrente tem 10x mais tráfego, ou um modelo de negócio completamente diferente (blog vs. e-commerce).
    *   **Como evitar**: Sempre contextualize os dados. Use ferramentas como SimilarWeb para estimar o tamanho e a natureza do tráfego do concorrente. Ajuste suas expectativas e metas com base em concorrentes diretos e similares em escala, ou use benchmarks específicos para seu nicho.
2.  **Ignorar a atribuição de canal em análises competitivas**: Focar apenas no "último clique" e não entender a jornada completa do cliente, perdendo insights sobre canais de descoberta e influência que os concorrentes podem estar otimizando.
    *   **Como evitar**: Utilize o modelo de atribuição "Baseado em Dados" do GA4 (Relatórios -> Publicidade -> Atribuição -> Modelos de Atribuição) para entender a contribuição de cada canal ao longo da jornada. Infira as estratégias de canais dos concorrentes observando suas campanhas de display, social e SEO através de ferramentas externas.
3.  **Analisar dados de concorrentes de forma estática, sem monitorar tendências**: Coletar dados de um único ponto no tempo e não acompanhar as mudanças no desempenho competitivo, o que pode levar a estratégias desatualizadas.
    *   **Como evitar**: Estabelecer um ciclo de análise mensal ou trimestral. Compare as tendências de tráfego, engajamento e palavras-chave ranqueadas dos concorrentes ao longo do tempo. Use a funcionalidade de "Comparação de Períodos" no Looker Studio ou ferramentas como SEMrush para rastrear o histórico das posições de palavras-chave.

---

## Dicas Avançadas

1.  **Análise de Cluster de Conteúdo por Tópico (GA4 e Ferramentas SEO)**: Agrupar suas páginas no GA4 (via `Relatórios` -> `Engajamento` -> `Páginas e Telas`, exportar e categorizar manualmente ou via script) por tópicos semânticos (ex: "smartphones", "wearables"). Em seguida, usar Ahrefs ou SEMrush para identificar os