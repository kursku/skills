---
name: indexing-strategy
description: "Indexing Strategy — Skill especializada para indexing strategy"
license: MIT
metadata:
  version: 1.0.0
  author: Cafe Code AI
  category: 05-seo-busca
  updated: 2026-03-01
risk: safe
---

# Indexing Strategy

Esta skill capacita o Claude Code a otimizar a visibilidade de conteúdo em motores de busca, gerenciando eficientemente o rastreamento, a indexação e a canonização de URLs para maximizar a performance orgânica.

---

## Keywords

crawl budget, robots.txt, sitemap.xml, noindex, nofollow, canonical tags, hreflang, Google Search Console, indexability, renderização web, log analysis, duplicidade de conteúdo, HTTP status codes, meta robots, user-agent, rastreamento seletivo.

---

## Quick Start

1.  **Validar Cobertura de Indexação no GSC**: Acessar o Google Search Console, navegar até "Páginas" (ou "Cobertura") e analisar o gráfico "Páginas válidas" e os relatórios de erros para identificar problemas de indexação em larga escala.
2.  **Auditar e Otimizar Robots.txt**: Verificar o arquivo `robots.txt` em `seu_dominio.com.br/robots.txt` para garantir que não está bloqueando diretórios críticos (CSS, JS, imagens, páginas de conteúdo) e está permitindo o rastreamento adequado de páginas importantes.
3.  **Submeter e Monitorar Sitemaps.xml**: Garantir que todos os sitemaps relevantes (ex: `sitemap.xml`, `sitemap_produtos.xml`) estão submetidos no GSC e que não apresentam erros de processamento ou URLs inválidas.
4.  **Implementar Tags Canônicas**: Para qualquer conjunto de URLs que exibem conteúdo idêntico ou muito similar (ex: `https://exemplo.com/produto?cor=azul` e `https://exemplo.com/produto`), implementar a tag `rel="canonical"` apontando para a URL preferencial.

---

## Core Workflows

### Workflow 1: Otimização de Orçamento de Rastreamento (Crawl Budget)

Este workflow detalha a análise e a otimização do orçamento de rastreamento para garantir que os bots dos motores de busca priorizem as páginas mais valiosas, maximizando a indexação de conteúdo relevante e minimizando o rastreamento de páginas de baixo valor.

**Passos Detalhados:**

1.  **Análise de Logs do Servidor para Identificar Padrões de Rastreamento**:
    *   **Ferramenta**: Acesso aos logs do servidor (Apache, Nginx) ou plataformas como Splunk, ELK Stack, Screaming Frog Log File Analyser.
    *   **Ação**: Filtrar os logs para ver quais URLs estão sendo rastreadas por User-Agents como `Googlebot`, `Bingbot`. Identificar páginas que são rastreadas excessivamente sem valor SEO (ex: páginas de filtro, URLs com parâmetros desnecessários, 404s).
    *   **Exemplo**: Observar que o Googlebot gasta 30% do tempo rastreando URLs de filtro como `site.com.br/categoria?filtro=cor-vermelha&tamanho=p`, que não geram tráfego orgânico.
2.  **Identificação e Exclusão de URLs de Baixo Valor ou Duplicadas**:
    *   **Ferramenta**: Google Search Console (Relatório de Cobertura), Screaming Frog SEO Spider, Sitebulb.
    *   **Ação**: Listar URLs que não devem ser indexadas ou que são duplicatas. Inclui páginas de login, carrinhos de compra, resultados de busca interna, páginas de tags ou categorias vazias.
    *   **Exemplo**: Descobrir que `site.com.br/carrinho/` e `site.com.br/minha-conta/` estão sendo rastreadas, mas não devem ser indexadas.
3.  **Implementação de Regras no `robots.txt` para Bloqueio Estratégico**:
    *   **Ferramenta**: Editor de texto, acesso FTP/SSH ao servidor.
    *   **Ação**: Utilizar a diretiva `Disallow` para impedir o rastreamento de diretórios ou arquivos específicos. Cuidado para não bloquear recursos essenciais (CSS/JS) ou páginas que precisam ser indexadas (apenas se o `noindex` for aplicado via meta tag).
    *   **Exemplo**:
        ```
        User-agent: *
        Disallow: /wp-admin/
        Disallow: /carrinho/
        Disallow: /minha-conta/
        Disallow: /search/?
        Sitemap: https://www.exemplo.com.br/sitemap.xml
        ```
4.  **Uso de `meta noindex` para Gerenciamento Fino**:
    *   **Ferramenta**: Acesso ao código HTML do site ou sistema de gerenciamento de conteúdo (CMS).
    *   **Ação**: Para páginas que precisam ser acessíveis ao usuário, mas não devem aparecer nos resultados de busca, adicionar `<meta name="robots" content="noindex, follow">` na seção `<head>`. A diretiva `follow` é crucial para que os links internos sejam rastreados.
    *   **Exemplo**: Aplicar `noindex, follow` em páginas de agradecimento após uma compra ou em páginas de filtro complexas sem valor orgânico.
5.  **Otimização da Velocidade de Carregamento da Página (Core Web Vitals)**:
    *   **Ferramenta**: Google PageSpeed Insights, Lighthouse, GTmetrix.
    *   **Ação**: Reduzir o tamanho de imagens, minificar CSS/JS, otimizar o tempo de resposta do servidor. Páginas mais rápidas permitem que os bots rastreiem mais URLs no mesmo período.
    *   **Dados Concretos**: Redução de 2 segundos no Largest Contentful Paint (LCP) pode aumentar o número de URLs rastreadas por dia em 15-20% em sites grandes.
6.  **Implementação de `rel="nofollow"` em Links Internos de Baixo Valor**:
    *   **Ferramenta**: Acesso ao código HTML ou CMS.
    *   **Ação**: Aplicar `rel="nofollow"` em links para páginas que não precisam de "link juice" ou que não devem ser priorizadas no rastreamento interno (ex: links para termos e condições, política de privacidade em rodapés).
    *   **Exemplo**: `<a href="/politica-de-privacidade/" rel="nofollow">Política de Privacidade</a>`.

### Workflow 2: Gestão de Páginas Duplicadas e Canonização

Este workflow foca em identificar e resolver problemas de conteúdo duplicado, garantindo que os motores de busca compreendam qual versão de uma página é a canônica (preferencial) para indexação, evitando diluição de autoridade e penalidades.

**Passos Detalhados:**

1.  **Identificação de Conteúdo Duplicado**:
    *   **Ferramenta**: Google Search Console (Relatório de Cobertura, seção "Excluída por tag canônica com a versão enviada não selecionada", "Página duplicada sem URL canônica selecionada pelo Google"), Screaming Frog, Sitebulb, Siteliner.
    *   **Ação**: Realizar varreduras completas no site para encontrar URLs com conteúdo idêntico ou muito similar. Isso inclui variações de URL (HTTP/HTTPS, WWW/non-WWW, parâmetros de sessão, IDs de rastreamento, ordenação/filtragem), versões para impressão, conteúdo sindicado.
    *   **Exemplo**: `https://exemplo.com/produto` e `https://exemplo.com/produto?source=email`. Ou `http://exemplo.com` e `https://www.exemplo.com`.
2.  **Definição da URL Canônica Preferencial**:
    *   **Ação**: Para cada conjunto de páginas duplicadas, determinar qual URL é a versão "mestra" que deve ser indexada e rankeada. Esta deve ser a URL mais limpa, acessível e com melhor desempenho.
    *   **Exemplo**: Se `https://www.exemplo.com/produto-x` é a versão HTTPS com WWW, ela deve ser a canônica em detrimento de `http://exemplo.com/produto-x` ou `https://exemplo.com/produto-x`.
3.  **Implementação da Tag `rel="canonical"`**:
    *   **Ferramenta**: Acesso ao HTML (seção `<head>`) ou CMS.
    *   **Ação**: Em todas as páginas duplicadas, adicionar a tag `<link rel="canonical" href="[URL_CANONICA_PREFERENCIAL]" />` apontando para a URL definida como canônica.
    *   **Exemplo**: Em `https://exemplo.com/produto?cor=azul`, a tag seria: `<link rel="canonical" href="https://exemplo.com/produto/" />`.
4.  **Configuração de Redirecionamentos 301 para Variações HTTP/HTTPS e WWW/non-WWW**:
    *   **Ferramenta**: Arquivo `.htaccess` (Apache) ou configuração de servidor Nginx.
    *   **Ação**: Implementar redirecionamentos 301 permanentes para consolidar todas as variações para a versão HTTPS e WWW (ou non-WWW) preferencial.
    *   **Exemplo**: Todo o tráfego de `http://exemplo.com` e `http://www.exemplo.com` e `https://exemplo.com` deve ser redirecionado para `https://www.exemplo.com`.
        ```apache
        RewriteEngine On
        RewriteCond %{HTTPS} off [OR]
        RewriteCond %{HTTP_HOST} !^www\. [NC]
        RewriteRule ^(.*)$ https://www.exemplo.com%{REQUEST_URI} [L,R=301]
        ```
5.  **Gerenciamento de Parâmetros de URL no Google Search Console**:
    *   **Ferramenta**: Google Search Console (Configurações > Parâmetros de URL - *Nota: esta ferramenta é legada e Google recomenda o uso de canonicals, mas pode ser útil para cenários específicos e legados*).
    *   **Ação**: Informar ao Google como tratar parâmetros específicos de URL (ex: `sessionid`, `utm_source`) para evitar que sejam rastreados como URLs distintas.
    *   **Exemplo**: Configurar o parâmetro `sessionid` para "Não rastrear URLs" se o parâmetro não altera o conteúdo da página.
6.  **Monitoramento Pós-Implementação**:
    *   **Ferramenta**: Google Search Console (Relatório de Cobertura), ferramentas de rastreamento.
    *   **Ação**: Após a implementação, monitorar o relatório de cobertura do GSC para verificar se as páginas duplicadas estão sendo excluídas corretamente e se a versão canônica está sendo indexada.
    *   **Métrica**: Redução de "Páginas duplicadas sem URL canônica selecionada pelo Google" e aumento de "Páginas válidas" ou "Excluída por tag canônica com a versão enviada não selecionada".

---

## Templates

### Robots.txt Otimizado para E-commerce

Este exemplo de `robots.txt` bloqueia diretórios administrativos e de baixo valor, enquanto permite o rastreamento de todo o conteúdo de produto e categoria, apontando para o sitemap principal.

```
User-agent: *
Disallow: /admin/
Disallow: /carrinho/
Disallow: /minha-conta/
Disallow: /checkout/
Disallow: /search/?
Disallow: /tag/
Disallow: /*?sort=*
Disallow: /*?filter=*
Allow: /produtos/
Allow: /categorias/
Sitemap: https://www.exemplo-loja.com.br/sitemap.xml
Sitemap: https://www.exemplo-loja.com.br/sitemap-produtos.xml
```

### Canonical Tag para Conteúdo Duplicado

Exemplo de como uma tag canônica deve ser implementada na seção `<head>` de uma página com URL contendo parâmetros, apontando para sua versão limpa e preferencial.

```html
<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Página de Produto Exemplo - Cor Azul</title>
    <link rel="canonical" href="https://www.exemplo.com.br/produtos/camiseta-basica/" />
    <!-- Outras meta tags e links CSS/JS aqui -->
</head>
<body>
    <!-- Conteúdo da página de produto -->
</body>
</html>
```

### Entrada de Sitemap XML para Página de Produto

Representação de uma entrada típica em um arquivo `sitemap.xml` para uma página de produto, incluindo a frequência de modificação e prioridade.

```xml
<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
   <url>
      <loc>https://www.exemplo.com.br/produtos/camiseta-basica/</loc>
      <lastmod>2024-07-26T10:00:00+00:00</lastmod>
      <changefreq>weekly</changefreq>
      <priority>0.8</priority>
   </url>
   <url>
      <loc>https://www.exemplo.com.br/categorias/camisetas/</loc>
      <lastmod>2024-07-25T14:30:00+00:00</lastmod>
      <changefreq>daily</changefreq>
      <priority>0.9</priority>
   </url>
</urlset>
```

---

## Checklist

- [x] Verificar o relatório "Páginas" (ou "Cobertura") no Google Search Console para identificar erros e exclusões de indexação.
- [x] Auditar o arquivo `robots.txt` para garantir que não há bloqueios acidentais de recursos essenciais (CSS/JS) ou páginas importantes.
- [x] Confirmar que todos os `sitemap.xml` relevantes estão submetidos e sem erros no Google Search Console.
- [x] Implementar tags `rel="canonical"` em todas as páginas com conteúdo duplicado ou similar, apontando para a URL preferencial.
- [x] Remover tags `meta noindex` de páginas que devem ser exibidas nos resultados de busca.
- [x] Otimizar a velocidade de carregamento da página (Core Web Vitals) para melhorar o crawl budget e a experiência do usuário.
- [x] Analisar logs do servidor para identificar padrões de rastreamento de bots e URLs que consomem crawl budget desnecessariamente.
- [x] Garantir que as URLs HTTP são redirecionadas via 301 para suas versões HTTPS correspondentes.
- [x] Assegurar que as URLs sem WWW (ou com WWW, dependendo da sua preferência) são redirecionadas via 301 para a versão canônica.
- [x] Implementar tags `hreflang` para sites com conteúdo em múltiplos idiomas ou regiões, garantindo a indexação correta da versão local.

---

## Métricas de Referência

| Métrica                                   | Benchmark                       | Meta                               |
|-------------------------------------------|---------------------------------|------------------------------------|
| Páginas Válidas (GSC)                     | >85% das URLs submetidas        | >95% das URLs submetidas          |
| Erros de Cobertura (GSC)                  | <5% das URLs submetidas         | <1% das URLs submetidas           |
| Taxa de Cliques (CTR) em resultados orgânicos | 3-5% (média geral)             | >7% para termos de marca/alta intenção |
| Tempo Médio de Carregamento (LCP)         | <2.5 segundos (mobile)          | <1.5 segundos (mobile)            |
| URLs Rastreáveis por dia (GSC)            | Varia muito, mas consistente    | Aumento de 10-20% após otimização |
| Percentual de `noindex` válidos           | <10% do total de URLs indexáveis | <5% do total de URLs indexáveis    |

---

## Erros Comuns

1.  **Bloquear CSS/JS/Imagens no `robots.txt`**: Impede que o Google renderize a página corretamente, dificultando a compreensão do conteúdo e a indexação.
    *   **Como evitar**: Remover as diretivas `Disallow` que afetam recursos estáticos essenciais. Exemplo: Se `Disallow: /assets/` bloqueia CSS e JS, remova-o ou seja mais específico.
2.  **`meta noindex` em conjunto com `Disallow` no `robots.txt`**: Se uma página é `Disallow` no `robots.txt`, o Googlebot nunca a rastreará e, portanto, nunca verá a tag `noindex` no HTML, podendo manter a página no índice.
    *   **Como evitar**: Para remover uma página do índice, permita seu rastreamento (`Allow` no `robots.txt`) e utilize apenas a tag `<meta name="robots" content="noindex">` no HTML.
3.  **Canonical auto-referencial incorreta ou apontando para URL de baixo valor**: Apontar uma tag canônica para a própria URL, mas com parâmetros desnecessários, ou para uma versão não preferencial do conteúdo.
    *   **Como evitar**: A tag canônica deve sempre apontar para a versão mais "limpa" e preferencial da URL. Exemplo: Em `https://exemplo.com/produto?cor=vermelho`, o canonical deve ser `https://exemplo.com/produto/`, não `https://exemplo.com/produto?cor=vermelho`.
4.  **Sitemaps desatualizados ou incompletos**: Sitemaps que contêm URLs inexistentes (404), bloqueadas por `robots.txt` ou `noindex`, ou que não incluem todas as páginas relevantes.
    *   **Como evitar**: Gerar sitemaps dinamicamente ou regularmente, garantindo que contenham apenas URLs rastreáveis e indexáveis. Validar sitemaps no GSC após cada atualização.

---

## Dicas Avançadas

1.  **Otimização para Indexação Mobile-First**: Priorizar a versão mobile do site, garantindo que o conteúdo, links internos e estrutura de dados (schema markup) sejam consistentes e completos na versão mobile, pois esta é a principal usada pelo Google para indexação.
    *   **Exemplo**: Usar a ferramenta "Teste de compatibilidade com dispositivos móveis" do Google e auditar a paridade de conteúdo entre desktop e mobile.
2.  **Uso de Sitemaps Dinâmicos com Última Modificação e Prioridade**: Para sites com milhões de URLs (ex: e-commerce com grande estoque), gerar sitemaps programaticamente, atualizando o `<lastmod>` para sinalizar ao Google quais páginas foram alteradas e ajustando a `<priority>` para guiar o rastreamento.
    *   **Exemplo**: Um e-commerce pode gerar um sitemap diário para produtos em estoque e um semanal para categorias.
3.  **Priorização de Rastreamento via Arquitetura de Links Internos**: Usar a estrutura de links internos para guiar os crawlers, atribuindo mais "PageRank" e atenção de rastreamento a páginas mais importantes através de links textuais relevantes e menor profundidade de cliques a partir da home.
    *   **Exemplo**: A home page linka diretamente para as 5 categorias mais importantes, que por sua vez linkam para os produtos mais vendidos, concentrando o fluxo de rastreamento.
4.  **Análise de Logs de Servidor para Comportamento de Bots e Erros**: Ir além do Google Search Console para analisar logs brutos do servidor. Isso permite identificar quais recursos os bots estão acessando, a frequência, erros 4xx/5xx específicos para bots, e oportunidades para otimizar o crawl budget.
    *   **Exemplo**: Identificar que o Googlebot está constantemente rastreando milhares de URLs 404 de um diretório antigo, permitindo a implementação de redirecionamentos 301 em massa ou bloqueio via robots.txt.
5.  **Estratégias de `noindex` Seletivo para Conteúdo Gerado pelo Usuário ou de Baixo Valor**: Implementar `noindex` em páginas de filtro complexas que geram pouco valor orgânico, páginas de busca interna, tags e categorias vazias ou com conteúdo muito diluído, evitando a diluição do crawl budget e a indexação de conteúdo irrelevante.
    *   **Exemplo**: Aplicar `noindex` em `site.com.br/busca?q=termo-raro` ou `site.com.br/tag/nao-usada/` para concentrar a força de indexação em conteúdo de alto valor.