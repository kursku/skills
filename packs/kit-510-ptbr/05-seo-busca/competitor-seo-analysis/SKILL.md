---
name: competitor-seo-analysis
description: "Competitor Seo Analysis — Skill especializada para competitor seo analysis"
license: MIT
metadata:
  version: 1.0.0
  author: Cafe Code AI
  category: 05-seo-busca
  updated: 2026-03-01
risk: safe
---

# Competitor Seo Analysis

Esta skill capacita o Claude a executar análises aprofundadas de SEO de concorrentes, identificando estratégias de palavras-chave, backlinks, conteúdo e lacunas de mercado para otimização de performance orgânica.

---

## Keywords

*   Análise de lacunas de conteúdo concorrente
*   Engenharia reversa de backlinks de rivais
*   Estratégia de palavras-chave de competidores
*   Auditoria de SEO on-page de concorrentes
*   Identificação de oportunidades de SERP features
*   Análise de tráfego orgânico de rivais
*   Monitoramento de rankings de concorrentes
*   Mapeamento de intenção de busca de concorrentes
*   Análise de arquitetura de informação de concorrentes
*   Benchmarking de Core Web Vitals de competidores
*   Estratégias de conteúdo pillar/cluster de concorrentes
*   Análise de Schema Markup de rivais

---

## Quick Start

1.  **Identificar Concorrentes Diretos:** Utilize ferramentas como SEMrush ou Ahrefs (Site Explorer) para listar 3-5 domínios concorrentes diretos com base em sobreposição de palavras-chave e tráfego orgânico no nicho de "e-commerce de produtos orgânicos".
2.  **Extrair Palavras-Chave de Oportunidade:** Em Ahrefs (Content Gap) ou SEMrush (Keyword Gap), insira os concorrentes e o seu domínio. Exporte as palavras-chave que os concorrentes ranqueiam nas top 10 posições e o seu domínio não ranqueia ou ranqueia além da 20ª posição.
3.  **Auditar Principais Backlinks dos Concorrentes:** No Ahrefs (Site Explorer -> Backlinks) ou Majestic SEO, analise os 50 domínios de referência com maior Domain Rating (DR)/Citation Flow (CF) que apontam para seus concorrentes. Identifique padrões de link building.
4.  **Comparar Estrutura de Conteúdo:** Faça um rápido scan visual dos sites dos concorrentes para identificar suas principais categorias de conteúdo, estrutura de URLs e uso de pillar pages.

---

## Core Workflows

### Workflow 1: Análise de Lacunas de Conteúdo e Palavras-Chave de Concorrentes

Este workflow visa descobrir palavras-chave valiosas que seus concorrentes ranqueiam, mas seu site não, e planejar o conteúdo para preencher essas lacunas.

**Passos Detalhados:**

1.  **Identificação e Validação de Concorrentes Primários:**
    *   **Ferramentas:** SEMrush (Organic Research -> Competitors) ou Ahrefs (Site Explorer -> Competing Domains).
    *   **Ação:** Insira seu domínio (`exemplo.com.br`). A ferramenta listará concorrentes que compartilham palavras-chave ranqueadas. Filtre para identificar os 3-5 concorrentes mais relevantes para seu modelo de negócio (e.g., para um e-commerce de suplementos veganos, `organicoja.com.br`, `naturezapura.com.br`, `vidasaudavelshop.com.br`). Priorize aqueles com Domain Rating (DR) ou Domain Authority (DA) similar ou superior ao seu.
    *   **Exemplo:** Para `meusuplementovegano.com.br`, o SEMrush sugere `organicoja.com.br` (DR 65), `naturezapura.com.br` (DR 58), `vidasaudavelshop.com.br` (DR 52).

2.  **Extração de Palavras-Chave dos Concorrentes:**
    *   **Ferramentas:** Ahrefs (Content Gap) ou SEMrush (Keyword Gap).
    *   **Ação:** No Ahrefs Content Gap, insira os 3-5 domínios dos concorrentes no campo "Show keywords that targets one of the below" e seu domínio no campo "But the following target doesn't rank for". Defina as posições para os concorrentes como "Top 10" e para seu domínio como "Any position" (ou "Doesn't rank") para encontrar as maiores lacunas.
    *   **Filtros Cruciais:**
        *   `Volume de Busca`: Mínimo de 100/mês para garantir relevância.
        *   `Keyword Difficulty (KD)`: Máximo de 50 para focar em oportunidades realistas a curto/médio prazo.
        *   `Intenção de Busca`: Analise a SERP para as palavras-chave identificadas e categorize-as em informacional, navegacional, transacional ou comercial para entender o tipo de conteúdo necessário.
    *   **Exemplo:** O Ahrefs revela que `organicoja.com.br` ranqueia em #3 para "melhores proteínas vegetais para ganho de massa" (Vol. 1.2K, KD 35), enquanto `meusuplementovegano.com.br` não ranqueia. Esta é uma lacuna de conteúdo transacional/informativa.

3.  **Priorização e Clusterização de Conteúdo:**
    *   **Ação:** Exporte a lista de palavras-chave. Utilize uma planilha para agrupar as palavras-chave por tópicos ou intenção de busca. Priorize as que têm alto volume, KD moderado e alta relevância para seu negócio.
    *   **Exemplo:**
        *   **Cluster 1 (Proteína Vegetal):** "melhores proteínas vegetais para ganho de massa", "proteína de ervilha vale a pena", "receitas com proteína de arroz".
        *   **Cluster 2 (Suplementos Veganos):** "vitamina B12 vegana onde comprar", "creatina vegana benefícios", "ômega 3 vegano para que serve".
    *   **Output:** Crie um plano editorial com 20-30 tópicos de conteúdo baseados nessas lacunas, especificando o tipo de conteúdo (artigo de blog, página de produto, guia, infográfico).

### Workflow 2: Análise de Perfil de Backlinks e Oportunidades de Link Building

Este workflow foca em entender a estratégia de link building dos seus concorrentes para identificar oportunidades de adquirir backlinks de alta qualidade.

**Passos Detalhados:**

1.  **Extração de Backlinks dos Concorrentes:**
    *   **Ferramentas:** Ahrefs (Site Explorer -> Backlinks) ou SEMrush (Backlink Analytics).
    *   **Ação:** Para cada um dos 3-5 concorrentes primários, exporte a lista completa de backlinks. Filtre por "DoFollow" e ordene por Domain Rating (DR) ou Authority Score (AS) do domínio de referência, do maior para o menor.
    *   **Filtros Cruciais:**
        *   `Domínio de Referência DR/AS`: Mínimo de 40 para focar em links de alta autoridade.
        *   `Tipo de Link`: Priorize links editoriais, guest posts, menções em notícias.
        *   `Data`: Concentre-se nos links mais recentes (últimos 12-24 meses) para identificar estratégias ativas.
    *   **Exemplo:** Para `organicoja.com.br`, o Ahrefs mostra um backlink de `saudebemestar.com.br` (DR 78) em um artigo sobre "Fontes de Proteína Vegana".

2.  **Identificação de Oportunidades de Link Intersect:**
    *   **Ferramentas:** Ahrefs (Link Intersect) ou SEMrush (Backlink Gap).
    *   **Ação:** Insira os 3-5 domínios dos concorrentes e seu próprio domínio no campo "Target". A ferramenta mostrará quais domínios linkam para seus concorrentes, mas não para você.
    *   **Priorização:** Foco em domínios que linkam para 2 ou mais concorrentes, pois são mais propensos a linkar para outros sites relevantes no nicho.
    *   **Exemplo:** `blogdavegana.com.br` (DR 55) linka para `organicoja.com.br` e `naturezapura.com.br`, mas não para `meusuplementovegano.com.br`. Este é um prospect de outreach de alta qualidade.

3.  **Análise de Âncoras e Contexto dos Backlinks:**
    *   **Ferramentas:** Ahrefs (Site Explorer -> Anchors) ou SEMrush (Backlink Analytics -> Anchors).
    *   **Ação:** Analise os anchor texts mais comuns usados nos backlinks dos concorrentes. Observe se são de marca, genéricos, exatos ou parcialmente correspondentes. Além disso, visite as URLs de referência para entender o contexto do link. O link é natural? É editorial?
    *   **Exemplo:** `organicoja.com.br` recebe muitos links com âncoras como "suplementos orgânicos", "comprar vegano" e "organicoja review". O contexto geralmente é de artigos de blog ou reviews de produtos. Isso sugere uma estratégia de âncoras variadas e naturais.

4.  **Criação de Estratégia de Outreach:**
    *   **Ação:** Compile uma lista de 50-100 prospects de link building identificados no passo 2. Para cada um, encontre o contato (e-mail, formulário de contato) e desenvolva uma proposta de outreach personalizada, destacando o valor que seu conteúdo ou produto pode agregar ao site deles.
    *   **Exemplo:** Para `blogdavegana.com.br`, a proposta poderia ser: "Percebemos que vocês abordam sobre suplementos veganos e linkam para X e Y. Gostaríamos de sugerir nosso guia completo sobre [tópico relevante], que complementaria perfeitamente seu artigo sobre [tópico deles]."

---

## Templates

### Template: Análise de Lacunas de Conteúdo Concorrente

```
| ID | Palavra-Chave (KW) | Volume Busca (Global) | KD (Dificuldade) | Intenção de Busca | Rank Concorrente A | Rank Concorrente B | Nosso Rank | Oportunidade | Tipo de Conteúdo Sugerido | Título Proposto |
|----|--------------------|-----------------------|------------------|-------------------|--------------------|--------------------|------------|--------------|---------------------------|-----------------|
| 01 | melhores proteínas vegetais para ganho de massa | 1.200 | 35 | Transacional/Informativa | 3 | 5 | Não ranqueia | ALTA | Artigo de Blog/Guia | "Guia Completo: Melhores Proteínas Vegetais para Ganho de Massa Muscular" |
| 02 | vitamina b12 vegana onde comprar | 800 | 28 | Transacional | 2 | 4 | 25 | MÉDIA | Página de Categoria/Produto | "Vitamina B12 Vegana: Onde Comprar e Marcas Recomendadas" |
| 03 | benefícios do ômega 3 vegano | 950 | 42 | Informativa | 6 | 8 | Não ranqueia | ALTA | Artigo de Blog | "Descubra os Benefícios Essenciais do Ômega 3 Vegano para Sua Saúde" |
| 04 | whey protein vegano é bom | 500 | 20 | Informativa | 4 | 7 | Não ranqueia | ALTA | Artigo de Blog/FAQ | "Whey Protein Vegano: É Realmente Eficaz? Análise Completa" |
| 05 | creatina vegana para atletas | 400 | 18 | Transacional/Informativa | 5 | 9 | 32 | MÉDIA | Artigo de Blog/Produto | "Creatina Vegana: Potencialize Seu Desempenho Atlético Naturalmente" |
```

### Template: Análise de Perfil de Backlinks de Concorrentes

```
| ID | Domínio de Referência | DR/AS | URL do Link | Anchor Text | Concorrente(s) Linkado(s) | Status Outreach | Notas |
|----|-----------------------|-------|-------------|-------------|---------------------------|-----------------|-------|
| 01 | saudebemestar.com.br | 78 | saudebemestar.com.br/proteinas-veganas | proteínas vegetais | organicoja.com.br | PENDENTE | Blog de saúde de alta autoridade, contato via formulário. Sugerir conteúdo complementar sobre fontes de proteína. |
| 02 | blogdavegana.com.br | 55 | blogdavegana.com.br/suplementos-naturais | suplementos naturais | organicoja.com.br, naturezapura.com.br | PENDENTE | Blog de nicho, relevante. Propor guest post ou menção em artigo existente. |
| 03 | vivabem.com.br | 72 | vivabem.com.br/melhores-lojas-organicas | loja orgânica | organicoja.com.br | PENDENTE | Portal de notícias com seção de saúde. Entrar em contato com editor da seção. |
| 04 | revistavegana.net | 48 | revistavegana.net/review-suplementos | review suplementos veganos | naturezapura.com.br | PENDENTE | Revista especializada. Oferecer amostra de produto para review. |
| 05 | alimentacaosaudavel.org | 60 | alimentacaosaudavel.org/guia-veganismo | guia veganismo | vidasaudavelshop.com.br | PENDENTE | Organização sem fins lucrativos. Propor parceria de conteúdo educativo. |
```

---

## Checklist

- [X] Identificar e validar 3-5 concorrentes diretos e indiretos usando ferramentas como Ahrefs/SEMrush.
- [X] Extrair as 10.000 principais palavras-chave orgânicas de cada concorrente (com volume de busca > 100).
- [X] Realizar análise de lacunas de palavras-chave (content gap) entre seu domínio e os concorrentes.
- [X] Mapear a intenção de busca (informativa, transacional, navegacional) para as palavras-chave de oportunidade.
- [X] Auditar os 50 principais backlinks "DoFollow" de cada concorrente (DR/AS > 40).
- [X] Identificar domínios de referência que linkam para múltiplos concorrentes, mas não para o seu (Link Intersect).
- [X] Analisar a estrutura de URLs, arquitetura do site e uso de pillar pages/clusters de conteúdo dos concorrentes.
- [X] Comparar o uso de Schema Markup (Product, FAQ, HowTo) dos concorrentes e identificar oportunidades de rich snippets.
- [X] Avaliar a velocidade de carregamento (LCP, FID, CLS) e Core Web Vitals dos concorrentes usando PageSpeed Insights.
- [X] Monitorar menções da marca dos concorrentes em mídias sociais e portais de notícias para insights de PR e awareness.

---

## Métricas de Referência

| Métrica | Benchmark (Exemplo de Nicho) | Meta (Exemplo de Nicho) |
|-----------------------------------|------------------------------|--------------------------|
| Share of Voice (SOV) em Top 10 KW | 25%                          | 35%                      |
| Domain Rating (DR)/Authority Score (AS) | 50                           | 60+                      |
| Número de Palavras-Chave Ranqueadas (Top 10) | 5.000                        | 7.000+                   |
| Taxa de Cliques (CTR) em Snippets Destacados | 8%                           | 12%+                     |
| Número de Backlinks de Domínios Únicos (DR>40) | 150                          | 250+                     |
| Velocidade de Carregamento (Largest Contentful Paint - LCP) | 2.5 segundos                 | < 1.8 segundos           |

---

## Erros Comuns

1.  **Foco exclusivo em volume de busca**: Ignorar a intenção do usuário e a dificuldade da palavra-chave, perseguindo apenas KWs de alto volume.
    *   **Como evitar**: Priorize palavras-chave com alta intenção de compra ou informacional relevante, mesmo com volume menor, e considere o Keyword Difficulty (KD) para chances reais de ranqueamento. Exemplo: "comprar açaí orgânico entrega rápida" (volume 200, KD 20) pode ser mais valiosa que "benefícios do açaí" (volume 10K, KD 70) para um e-commerce, pois a intenção é transacional.
2.  **Copiar cegamente a estratégia de backlinks**: Adquirir links de baixa qualidade ou irrelevantes apenas porque um concorrente os tem, sem avaliar a relevância ou autoridade do domínio de referência.
    *   **Como evitar**: Avaliar a autoridade (DR/DA), relevância e contexto de cada link. Focar em links editoriais de domínios com DR > 40 e que sejam tematicamente relevantes. Exemplo: Um link de um diretório genérico de empresas (DR 15) é menos valioso que um de um blog de nicho (DR 50) com um artigo contextualizado.
3.  **Analisar apenas concorrentes diretos de produto/serviço**: Perder oportunidades de palavras-chave e links de concorrentes indiretos ou de conteúdo que dominam a SERP para termos relevantes.
    *   **Como evitar**: Expandir a análise para blogs, portais de notícias e sites de reviews que ranqueiam para as mesmas palavras-chave, mesmo que não vendam os mesmos produtos/serviços. Exemplo: Um blog de receitas veganas pode ser um concorrente de conteúdo para "como usar proteína vegetal em receitas", mesmo não sendo um e-commerce de suplementos.

---

## Dicas Avançadas

1.  **Engenharia Reversa de Clusters de Conteúdo dos Concorrentes**: Em vez de analisar apenas palavras-chave individuais, identifique os clusters de tópicos que os concorrentes dominam. Utilize ferramentas como Screaming Frog para mapear a arquitetura de informação dos concorrentes e identificar suas "pillar pages" e "cluster content" adjacentes.
    *   **Exemplo Prático**: O concorrente `organicoja.com.br` tem uma "pillar page" intitulada "Guia Completo de Alimentação Vegana", que linka para artigos de cluster como "Fontes de Proteína Vegana", "Vitaminas Essenciais para Veganos" e "Receitas Veganas Rápidas". Isso revela uma estratégia de conteúdo bem estruturada para dominar um tópico amplo.
2.  **Análise Detalhada de SERP Features e Conteúdo Visual**: Não se limite a palavras-chave e links. Analise como os concorrentes dominam as SERP Features (Featured Snippets, PAA - People Also Ask, Imagens, Vídeos, Rich Snippets de Produto). Use SEMrush (SERP Features) ou Ahrefs (Organic Keywords -> SERP) para identificar essas oportunidades.
    *   **Exemplo Prático**: Se um concorrente domina o Featured Snippet para "receita de bolo vegano sem glúten", analise a estrutura do conteúdo, a formatação (listas, tabelas) e a concisão da resposta para replicar/melhorar e tentar "roubar" esse snippet.
3.  **Monitoramento de Alterações de Conteúdo e Estrutura dos Concorrentes**: Utilize ferramentas de monitoramento de websites (ex: Visualping, ChangeTower) para ser alertado sobre novas páginas, atualizações de conteúdo, mudanças de títulos/meta descrições e alterações na arquitetura do site dos concorrentes. Isso permite reagir rapidamente a novas estratégias de SEO ou lacunas que eles estão preenchendo.
    *   **Exemplo Prático**: Um alerta mostra que `naturezapura.com.br` adicionou uma nova seção sobre "Suplementos Adaptógenos" com 10 artigos novos. Isso sinaliza um novo foco de palavras-chave e uma oportunidade para você criar conteúdo similar ou melhor para competir.
4.  **Análise de Intenção de Busca Implícita e Experiência do Usuário (UX)**: Além das palavras-chave explícitas, inferir a intenção de busca implícita pelos tipos de conteúdo que os concorrentes ranqueiam e como eles otimizam a UX. Observe tempo na página e taxa de rejeição (se dados públicos estiverem disponíveis, ex: SimilarWeb para concorrentes).
    *   **Exemplo Prático**: Se um concorrente tem um baixo bounce rate e alto tempo na página em sua categoria de "vitaminas veganas", ele provavelmente oferece uma UX superior com filtros de produto excelentes, descrições detalhadas e avaliações de clientes bem visíveis. Isso indica que a intenção do usuário nessa página é "comparar e decidir", e a UX do concorrente atende a isso.
5.  **Análise de Schema Markup para Otimização de Rich Snippets**: Compare o uso de Schema Markup (Product, Review, FAQ, HowTo, Recipe) entre seu site e os concorrentes. Ferramentas como o Google Rich Results Test ou Schema Markup Generator podem ajudar na inspeção e criação.
    *   **Exemplo Prático**: Se os concorrentes para "melhores suplementos para imunidade" estão usando `FAQPage Schema` para exibir perguntas frequentes diretamente na SERP, e seu site não, essa é uma oportunidade para implementar o mesmo e potencialmente obter rich snippets, aumentando sua visibilidade e CTR.