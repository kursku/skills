---
name: seo-audit-checklist
description: "Seo Audit Checklist — Skill especializada para seo audit checklist"
license: MIT
metadata:
  version: 1.0.0
  author: Cafe Code AI
  category: 05-seo-busca
  updated: 2026-03-01
risk: safe
---

# Seo Audit Checklist

Esta skill capacita o Claude a executar auditorias de SEO completas e detalhadas, identificando oportunidades de otimização técnica, de conteúdo e de autoridade para melhorar o ranqueamento e a visibilidade orgânica.

---

## Keywords

*   Auditoria SEO técnica
*   Checklist SEO on-page
*   Análise de backlinks
*   Otimização de performance web
*   Schema markup SEO
*   Pesquisa de palavras-chave competitiva
*   Análise de rastreabilidade e indexação
*   Core Web Vitals auditoria
*   Análise de conteúdo duplicado
*   Auditoria de arquitetura de site
*   Otimização de Experiência do Usuário (UX) para SEO

---

## Quick Start

1.  **Coletar URLs para auditoria:** Utilize o Google Search Console, inserindo "site:seusite.com.br" para exportar as URLs indexadas, focando nas páginas com maior tráfego orgânico ou potencial.
2.  **Verificar saúde técnica inicial:** Realize um crawl rápido com uma ferramenta como Screaming Frog SEO Spider em "seusite.com.br" para identificar erros 4xx/5xx, redirecionamentos e títulos/meta descrições duplicados.
3.  **Analisar desempenho em ferramentas:** Conecte o Google Analytics e Google Search Console para avaliar tendências de tráfego orgânico, impressões, cliques e posicionamento médio para as principais palavras-chave.
4.  **Auditar Core Web Vitals:** Utilize o PageSpeed Insights para a homepage e páginas de categoria/produto mais acessadas para identificar gargalos de velocidade (LCP, FID, CLS).
5.  **Identificar concorrentes diretos e suas estratégias:** Empregue SEMrush ou Ahrefs para listar os 3-5 principais concorrentes que ranqueiam para suas keywords mais importantes e analise seus perfis de backlink e conteúdo.

---

## Core Workflows

### Workflow 1: Auditoria Técnica de Rastreadilidade e Indexação

Este workflow foca em garantir que os motores de busca possam acessar, rastrear e indexar seu conteúdo de forma eficiente, crucial para a visibilidade orgânica.

*   **Passo 1: Verificação de Arquivos `robots.txt` e `sitemap.xml`**
    *   **Ação:** Acesse `seusite.com.br/robots.txt` e `seusite.com.br/sitemap.xml`.
    *   **Detalhes:** No `robots.txt`, verifique diretivas `Disallow` que bloqueiam acidentalmente páginas essenciais ou recursos (CSS/JS). No `sitemap.xml`, confirme que ele lista apenas URLs canônicas e indexáveis, e que foi submetido e está sem erros no Google Search Console. Identifique se URLs problemáticas (ex: páginas de filtro, parâmetros de sessão) estão sendo rastreadas indevidamente.
    *   **Exemplo de erro:** `Disallow: /wp-content/uploads/` (bloqueia imagens) ou `Disallow: /blog/categoria-importante/` (bloqueia conteúdo valioso). Um `sitemap.xml` que inclui centenas de URLs 404 ou URLs com `noindex`.
*   **Passo 2: Análise de Status Codes e Redirecionamentos**
    *   **Ferramenta:** Screaming Frog SEO Spider (ou similar).
    *   **Ação:** Rastreie o site e filtre por "Client Error (4xx)" e "Server Error (5xx)". Verifique também a cadeia de redirecionamentos.
    *   **Detalhes:** Corrija URLs quebradas (404) implementando redirecionamentos 301 para a página mais relevante ou removendo links internos para elas. Analise redirecionamentos 301/302 para garantir que não há cadeias longas (mais de 2 saltos) ou loops de redirecionamento, que degradam a experiência do usuário e o SEO.
    *   **Exemplo:** Uma URL `seusite.com.br/produto-antigo` retornando 404 deve ser redirecionada 301 para `seusite.com.br/produto-novo`. Uma cadeia `A -> B -> C` deve ser consolidada para `A -> C`.
*   **Passo 3: Verificação de Indexação no Google Search Console**
    *   **Ação:** Acesse a seção "Indexação > Páginas" no Google Search Console.
    *   **Detalhes:** Identifique URLs "Excluídas" ou com "Erro". Analise as causas, como "Página com redirecionamento", "Rastreamento anômalo", "Página duplicada sem URL canônica escolhida pelo Google". Priorize a correção de URLs importantes que deveriam estar indexadas, mas não estão.
    *   **Exemplo:** Se 500 URLs estão como "Página duplicada sem URL canônica escolhida pelo Google", verifique a implementação de `rel="canonical"` nessas páginas, garantindo que a URL canônica esteja correta e acessível.

### Workflow 2: Auditoria de Conteúdo e Otimização On-Page

Este workflow se concentra na qualidade e otimização do conteúdo e dos elementos on-page para melhorar a relevância e a experiência do usuário.

*   **Passo 1: Análise de Conteúdo Duplicado e Canibalização de Keywords**
    *   **Ferramenta:** SiteLiner, Screaming Frog (para identificar títulos e meta descrições duplicados), Google Search Console (Relatório de Desempenho).
    *   **Ação:** Execute as ferramentas para encontrar blocos de texto idênticos ou muito semelhantes em diferentes URLs. No GSC, na seção "Desempenho > Páginas", filtre por uma keyword principal e veja se várias URLs ranqueiam para ela.
    *   **Detalhes:** Conteúdo duplicado interno dilui a autoridade e pode confundir os motores de busca. A canibalização ocorre quando várias páginas do seu site competem pela mesma palavra-chave. Resolva consolidando conteúdo, diferenciando as páginas ou usando `rel="canonical"`.
    *   **Exemplo:** As páginas `/blog/melhores-smartphones-2023` e `/blog/guia-compra-smartphone` ranqueiam para "melhores smartphones". Se o conteúdo for muito similar, considere unificá-los ou reescrevê-los para intenções de busca distintas.
*   **Passo 2: Otimização de Títulos, Meta Descrições e H1s**
    *   **Ação:** Para cada página prioritária, avalie e otimize o `<title>`, `<meta description>` e `<h1>`.
    *   **Detalhes:** O `<title>` deve ter a keyword principal no início, ser conciso (50-60 caracteres) e único para cada página. A `<meta description>` deve ter até 150-160 caracteres, ser persuasiva e incluir a keyword para atrair cliques. O `<h1>` deve ser único na página e refletir o conteúdo principal, idealmente com a keyword principal.
    *   **Exemplo:**
        *   **Título Atual:** `Produtos`
        *   **Título Otimizado:** `Comprar Tênis de Corrida Masculino | Frete Grátis | Loja ABC (59 caracteres)`
        *   **Meta Descrição Atual:** `Veja nossos tênis.`
        *   **Meta Descrição Otimizada:** `Encontre os melhores tênis de corrida masculinos com tecnologia de ponta e frete grátis. Variedade de marcas e modelos para sua performance. (158 caracteres)`
        *   **H1 Atual:** `Tênis`
        *   **H1 Otimizado:** `Explore Nossos Tênis de Corrida Masculinos Exclusivos`
*   **Passo 3: Implementação e Validação de Schema Markup**
    *   **Ação:** Identifique os tipos de schema relevantes para suas páginas (e.g., `Product`, `Review`, `Article`, `LocalBusiness`, `FAQPage`).
    *   **Detalhes:** Gere o JSON-LD apropriado com todas as propriedades necessárias e insira-o no `<head>` ou `<body>` da página. Valide cada implementação usando a "Ferramenta de Teste de Rich Results" do Google para garantir a sintaxe correta e a elegibilidade para rich snippets.
    *   **Exemplo:** Para uma página de produto, implemente o schema `Product` com `name`, `image`, `description`, `sku`, `brand`, `offers` (incluindo `price`, `priceCurrency`, `availability`), e `aggregateRating` (se houver avaliações).

---

## Templates

### Template de Relatório de Erros 4xx

```
Relatório de Erros 4xx - Auditoria SEO
Site: loja-esportiva.com.br
Data da Auditoria: 2024-07-26

| URL Original (404)                                   | Status Code | Página Referenciadora (Origem do Link Interno)           | Ação Recomendada                                      | Observações                                 | Prioridade |
|------------------------------------------------------|-------------|----------------------------------------------------------|-------------------------------------------------------|---------------------------------------------|------------|
| https://loja-esportiva.com.br/tenis/nike-antigo      | 404         | https://loja-esportiva.com.br/categoria/promocoes        | Implementar 301 para /tenis/nike-air-max              | Produto descontinuado, mas similar existe   | Alta       |
| https://loja-esportiva.com.br/blog/artigo-quebrado   | 404         | https://loja-esportiva.com.br/blog/melhores-tenis        | Corrigir link interno ou remover do artigo            | Link para artigo removido/unificado         | Média      |
| https://loja-esportiva.com.br/contato/mapa-antigo    | 404         | Nenhum link interno encontrado                           | Remover do sitemap e do Google Search Console         | Página antiga, sem relevância ou tráfego    | Baixa      |
| https://loja-esportiva.com.br/calcados/produto-x     | 404         | https://loja-esportiva.com.br/categoria/calcados         | Implementar 301 para /calcados/marca-y-modelo-z       | Produto substituído por novo modelo         | Alta       |
```

### Template de Otimização de Meta Tags e H1

```
Template de Otimização de Meta Tags (Título, Descrição e H1)
Site: loja-esportiva.com.br
Página: https://loja-esportiva.com.br/categoria/tenis-corrida-masculino

| Campo             | Status Atual (Análise)                                    | Sugestão de Otimização                                                  | Caracteres (Sugestão) | Keyword Principal              | Observações                                                                        |
|-------------------|-----------------------------------------------------------|-------------------------------------------------------------------------|-----------------------|--------------------------------|------------------------------------------------------------------------------------|
| Título (Title Tag)| "Tênis Masculino para Correr - Loja Esportiva"            | "Tênis de Corrida Masculino | Melhores Preços e Marcas | Loja Esportiva"         | 60                    | tênis de corrida masculino     | Inclui marca, preço, e termo de cauda longa para maior especificidade.             |
| Meta Descrição    | "Compre os melhores tênis masculinos para sua corrida."   | "Encontre tênis de corrida masculinos com amortecimento superior e design moderno. Frete grátis e troca fácil. Confira nossos modelos!" | 159                   | tênis de corrida masculinos    | Chamada para ação, benefícios (frete grátis), palavras-chave secundárias.          |
| H1                | "Tênis para Correr"                                       | "Descubra Nossos Tênis de Corrida Masculinos Exclusivos"                | 55                    | Tênis de Corrida Masculinos    | Mais descritivo e persuasivo, usando sinônimos e chamando a atenção.             |
```

---

## Checklist

-   [ ] Verificar `robots.txt` para bloqueios indevidos de recursos essenciais (CSS, JS) ou páginas importantes.
-   [ ] Validar `sitemap.xml` no Google Search Console, garantindo que todas as URLs importantes estão listadas, são indexáveis e sem erros.
-   [ ] Analisar erros 4xx/5xx e redirecionamentos 301/302 para evitar cadeias longas (mais de 2 saltos) ou loops.
-   [ ] Auditar Core Web Vitals (LCP, FID, CLS) para a homepage e páginas-chave via PageSpeed Insights, com foco em otimização de imagens e defer JS.
-   [ ] Verificar a unicidade e otimização de `<title>` e `<meta description>` em todo o site (usando Screaming Frog para identificar duplicatas e excessos de caracteres).
-   [ ] Identificar e resolver problemas de conteúdo duplicado e canibalização de keywords através de consolidação ou `rel="canonical"`.
-   [ ] Implementar e validar `rel="canonical"` em páginas com conteúdo semelhante ou parâmetros de URL.
-   [ ] Auditar a presença e correção de Schema Markup (JSON-LD) para produtos, artigos, FAQs, LocalBusiness, etc., utilizando a Ferramenta de Teste de Rich Results.
-   [ ] Testar a responsividade do site em diferentes dispositivos móveis usando o Teste de Compatibilidade com Dispositivos Móveis do Google.
-   [ ] Analisar a hierarquia de URLs e a estrutura de links internos para otimização do PageRank e da experiência de navegação.
-   [ ] Verificar a velocidade de carregamento de imagens e implementar lazy loading onde apropriado.
-   [ ] Analisar e otimizar URLs para serem amigáveis, curtas e descritivas (ex: `/tenis-corrida-masculino` ao invés de `/p?id=123&cat=1`).

---

## Métricas de Referência

| Métrica                                | Benchmark                                         | Meta                                                   |
|----------------------------------------|---------------------------------------------------|--------------------------------------------------------|
| Taxa de rastreamento (URLs rastreadas/dia) | Varia (ex: 500-5000 para sites médios), sem quedas bruscas | Estável ou crescente, conforme adição de conteúdo novo |
| LCP (Largest Contentful Paint)         | < 2.5 segundos (bom)                              | < 1.8 segundos                                         |
| % de URLs indexadas vs. enviadas no GSC | > 90% das URLs canônicas                            | > 95% das URLs canônicas                               |
| Taxa de Cliques Orgânicos (CTR)        | 1-5% (depende da posição e tipo de query)         | 3-7% (para top 5 posições)                             |
| Erros 4xx no GSC                       | 0% em páginas essenciais                           | 0% em todas as páginas indexáveis                      |
| Páginas com Rich Results               | > 20% das páginas de produto/artigo elegíveis     | > 50% das páginas de produto/artigo elegíveis          |

---

## Erros Comuns

1.  **Bloquear CSS/JS no `robots.txt`**: Impede o Googlebot de renderizar a página corretamente, resultando em uma compreensão incompleta do layout e conteúdo, afetando a indexação e ranqueamento.
    *   **Como evitar**: Remover diretivas `Disallow` que afetem pastas de recursos estáticos essenciais, como `/wp-content/themes/`, `/assets/css/`, `/js/`, ou qualquer outra pasta que contenha arquivos de estilo e script. Use o "Teste de robots.txt" no Google Search Console.
    *   **Exemplo**: Um `robots.txt` não deve conter `Disallow: /wp-includes/css/` ou `Disallow: /assets/js/`, pois isso impede o renderização adequada.
2.  **Ignorar a importância do conteúdo duplicado interno**: Ter muitas páginas com conteúdo quase idêntico ou meta tags iguais (títulos, descrições) confunde os motores de busca e dilui a autoridade do site, levando à canibalização de keywords.
    *   **Como evitar**: Utilizar `rel="canonical"` para apontar para a versão preferencial, consolidar conteúdo redundante em uma única página abrangente, ou reescrever as páginas para maior diferenciação e intenções de busca distintas.
    *   **Exemplo**: Páginas de produto com cores diferentes, mas descrições idênticas. Aponte as páginas variantes para a página principal via canonical ou adicione conteúdo único e relevante para cada variação.
3.  **Não validar Schema Markup após a implementação**: Erros na sintaxe JSON-LD, dados incompletos ou incompatíveis com as diretrizes do Google podem impedir que os dados estruturados sejam usados, resultando na perda de oportunidades para rich snippets e visibilidade aprimorada.
    *   **Como evitar**: Sempre usar a "Ferramenta de Teste de Rich Results" do Google para validar cada implementação de schema markup imediatamente após a inserção. Corrigir quaisquer avisos ou erros reportados.
    *   **Exemplo**: Um schema `Product` implementado em uma página de e-commerce sem os campos obrigatórios `price` ou `priceCurrency` não será elegível para Rich Results de produto, como preços exibidos diretamente nos resultados de busca.

---

## Dicas Avançadas

1.  **Análise de Log Server para Insights de Rastreamento Aprofundados**: Vá além do Google Search Console. Analise os logs do seu servidor para entender exatamente como os bots do Google (Googlebot) interagem com o seu site. Identifique quais páginas são rastreadas com mais frequência, o tempo gasto em cada uma e padrões de rastreamento ineficientes.
    *   **Exemplo Prático**: Se os logs mostrarem que o Googlebot está gastando uma quantidade significativa de recursos rastreando URLs 404 ou páginas de filtro irrelevantes (ex: `?cor=vermelho&tamanho=p`), otimize seu `robots.txt` para `Disallow` essas seções ou use parâmetros de URL no GSC para direcionar o orçamento de rastreamento para páginas de alto valor.
2.  **Uso Estratégico de Ferramentas de Visualização de Links Internos**: Ferramentas como Sitebulb ou as visualizações de gráfico do Screaming Frog SEO Spider permitem mapear a arquitetura de links internos do seu site. Isso ajuda a identificar "silos" de conteúdo isolados, páginas órfãs sem links, e a distribuição ineficiente de PageRank.
    *   **Exemplo Prático**: Descobrir que uma página crucial de serviço ou produto, que gera receita, está a 5 cliques de profundidade da homepage, enquanto um blog post antigo e menos relevante está a apenas 2 cliques. Reestruture os links internos para priorizar a página de serviço, adicionando links de artigos relevantes e menus de navegação.
3.  **Auditoria de Intenção de Busca para Conteúdo Existente**: Não se limite apenas à pesquisa de palavras-chave. Audite a *intenção* por trás das palavras-chave para as quais seu conteúdo já ranqueia. Avalie se o conteúdo atual realmente atende à intenção predominante (inform