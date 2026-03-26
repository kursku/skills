---
name: site-speed-optimization
description: "Site Speed Optimization — Skill especializada para site speed optimization"
license: MIT
metadata:
  version: 1.0.0
  author: Cafe Code AI
  category: 05-seo-busca
  updated: 2026-03-01
risk: safe
---

# Site Speed Optimization

Esta skill capacita o Claude a diagnosticar, planejar e executar otimizações avançadas de velocidade para websites, focando em métricas Core Web Vitals e impacto no SEO.

---

## Keywords

Core Web Vitals, LCP otimização, FID melhoria, CLS correção, otimização de imagens, compressão GZIP/Brotli, cache de navegador, lazy loading, critical CSS, remoção de CSS/JS não utilizado, pré-carregamento de fontes, CDN implementação, otimização de servidor, tree shaking, WebP conversão, TTFB redução, TBT otimização, render-blocking resources.

---

## Quick Start

1.  **Auditoria Inicial com PageSpeed Insights**: Analisar `https://www.exemplo.com.br` e `https://www.exemplo.com.br/categoria-produto` para identificar os principais gargalos LCP (Largest Contentful Paint), FID (First Input Delay) e CLS (Cumulative Layout Shift) em dispositivos móveis e desktop.
2.  **Otimização de Imagens Críticas**: Converter todas as imagens do *hero section* e das primeiras galerias para WebP ou AVIF, comprimir com Squoosh.app e implementar `loading="lazy"` para imagens abaixo da dobra. Ex: `hero-banner.jpg` (2MB) para `hero-banner.webp` (200KB).
3.  **Minificação e Agrupamento de CSS/JS**: Utilizar ferramentas de build (ex: Webpack, Gulp) ou plugins de cache para CMS (ex: WP Rocket, LiteSpeed Cache) para minificar e agrupar todos os arquivos `.css` e `.js`, reduzindo o número de requisições HTTP e o tamanho dos arquivos.
4.  **Ativar Cache do Navegador**: Configurar cabeçalhos HTTP `Cache-Control: max-age=2592000, public` e `Expires` para recursos estáticos (imagens, fontes, CSS, JS) via `.htaccess` ou configuração do servidor web (Nginx/Apache), permitindo que o navegador armazene esses arquivos por 30 dias.
5.  **Priorizar Conteúdo Acima da Dobra (Critical CSS)**: Extrair o CSS essencial para renderizar o conteúdo visível inicial (acima da dobra) de páginas como `https://www.exemplo.com.br/` e embuti-lo diretamente no `<head>` do HTML, adiando o carregamento do restante do CSS.

---

## Core Workflows

### Workflow 1: Otimização Avançada de Imagens para Core Web Vitals

Este workflow foca em reduzir o tempo de carregamento da Maior Pintura de Conteúdo (LCP) e evitar mudanças de layout cumulativas (CLS) causadas por imagens, que são frequentemente os maiores bloqueadores de velocidade em qualquer página web.

**Passos Detalhados:**

1.  **Identificação de Imagens LCP Candidatas e Causas de CLS**:
    *   **Ferramenta**: PageSpeed Insights ou Chrome DevTools (aba "Performance" com "Web Vitals" habilitado).
    *   **Ação**: Analisar `https://www.exemplo.com.br/pagina-de-produto` no PageSpeed Insights. Na seção "Diagnósticos", buscar "Largest Contentful Paint element" para identificar a imagem principal. No DevTools, gravar um carregamento e identificar eventos de "Layout Shift" e seus causadores (geralmente imagens sem `width`/`height`).
    *   **Exemplo**: O PSI indica `<img src="/img/product/main-shoe.jpg">` como o LCP element, contribuindo com 3.2s para o LCP total de 4.5s. Além disso, várias imagens de galeria na página não possuem dimensões explícitas.
2.  **Conversão para Formatos Modernos e Compressão Otimizada**:
    *   **Ferramenta**: Squoosh.app, `cwebp` (CLI), `imagemin` (Node.js) ou CDNs de imagem.
    *   **Ação**: Converter `main-shoe.jpg` (1.8MB, 1600x1200px) para WebP com qualidade 75 (`cwebp -q 75 main-shoe.jpg -o main-shoe.webp`). Para navegadores com suporte a AVIF, gerar uma versão `main-shoe.avif`.
    *   **Exemplo**: `main-shoe.webp` com 250KB.
3.  **Dimensionamento Responsivo com `srcset` e `sizes`**:
    *   **Ação**: Gerar múltiplos tamanhos da imagem otimizada para diferentes resoluções de tela e densidades de pixel.
    *   **Exemplo (HTML)**:
        ```html
        <picture>
          <source srcset="/img/product/main-shoe.avif 1600w,
                          /img/product/main-shoe-medium.avif 900w,
                          /img/product/main-shoe-small.avif 450w" type="image/avif">
          <source srcset="/img/product/main-shoe.webp 1600w,
                          /img/product/main-shoe-medium.webp 900w,
                          /img/product/main-shoe-small.webp 450w" type="image/webp">
          <img src="/img/product/main-shoe.jpg"
               srcset="/img/product/main-shoe-small.webp 450w,
                       /img/product/main-shoe-medium.webp 900w,
                       /img/product/main-shoe.webp 1600w"
               sizes="(max-width: 480px) 450px,
                      (max-width: 1024px) 900px,
                      1600px"
               alt="Tênis principal do produto"
               width="1600" height="1200"
               fetchpriority="high"
               loading="eager">
        </picture>
        ```
    *   **Nota**: `width` e `height` são **fundamentais** para reservar o espaço e evitar CLS. `fetchpriority="high"` e `loading="eager"` são para a imagem LCP.
4.  **Lazy Loading Estratégico e Priorização**:
    *   **Ação**: Para imagens *abaixo da dobra* (não LCP), usar `loading="lazy"`.
    *   **Exemplo**: `<img src="/img/product/related-item.webp" alt="Item relacionado" loading="lazy" width="300" height="200">`. Isso economiza recursos, carregando-as apenas quando se tornam visíveis.
5.  **Integração com CDN de Imagens**:
    *   **Ferramenta**: Cloudinary, Imgix, AWS CloudFront, Cloudflare.
    *   **Ação**: Configurar o CDN para servir as imagens. Utilizar as funcionalidades do CDN para otimização automática (redimensionamento, compressão, formato ideal) via URL.
    *   **Exemplo**: Mudar `src="/img/product/main-shoe.webp"` para `src="https://cdn.exemplo.com.br/img/product/main-shoe.webp?w=1600&h=1200&f=webp&q=75"`.

### Workflow 2: Otimização de Recursos Bloqueadores de Renderização (CSS e JavaScript)

Este workflow aborda a remoção de recursos que impedem a renderização inicial da página e a interatividade, melhorando o First Contentful Paint (FCP), LCP e as métricas de interatividade (FID/TBT).

**Passos Detalhados:**

1.  **Análise de Recursos Bloqueadores e Cobertura**:
    *   **Ferramenta**: PageSpeed Insights (seção "Eliminar recursos que bloqueiam a renderização") e Chrome DevTools (aba "Coverage").
    *   **Ação**: No DevTools, carregar `https://www.exemplo.com.br/` e analisar a aba "Coverage" para identificar o percentual de CSS e JS não utilizado em `style.css` (78% não utilizado) e `scripts.js` (65% não utilizado).
2.  **Extração e Injeção de Critical CSS**:
    *   **Ferramenta**: `critical` NPM package, PurgeCSS, ou geradores online.
    *   **Ação**: Usar `critical` para extrair o CSS necessário para o conteúdo acima da dobra da página inicial.
    *   **Exemplo (HTML)**:
        ```html
        <head>
            <style>
                /* Conteúdo do Critical CSS extraído */
                body{font-family:'Roboto',sans-serif;margin:0;color:#333}
                .header{background:#fff;padding:15px 20px;box-shadow:0 2px 4px rgba(0,0,0,.1)}
                .hero-section{background-color:#f8f8f8;padding:60px 20px;text-align:center}
                h1{font-size:2.5em;color:#007bff}
                /* ... estilos essenciais para o viewport inicial ... */
            </style>
            <!-- Carregar o CSS completo de forma assíncrona -->
            <link rel="stylesheet" href="/css/main.css" media="print" onload="this.media='all'">
            <noscript><link rel="stylesheet" href="/css/main.css"></noscript>
            <!-- ... outros elementos do head ... -->
        </head>
        ```
    *   **Nota**: `media="print"` com `onload="this.media='all'"` é uma técnica para carregar CSS de forma não bloqueadora.
3.  **Adiamento (Defer) e Carregamento Assíncrono (Async) de JavaScript**:
    *   **Ação**: Identificar scripts que não são cruciais para a renderização inicial e adicionar os atributos `defer` ou `async`.
    *   **Exemplo**:
        *   Analytics: `<script src="https://www.googletagmanager.com/gtag/js?id=UA-XXXXX-Y" async></script>`
        *   Widgets de chat: `<script src="/js/chat-widget.js" defer></script>`
        *   Carrosséis de imagem: `<script src="/js/swiper.min.js" defer></script>`
    *   **Dica**: `defer` mantém a ordem de execução e espera o HTML ser parseado; `async` executa assim que o script é baixado, sem garantia de ordem.
4.  **Minificação e Compressão de Recursos**:
    *   **Ação**: Garantir que todos os arquivos CSS, JavaScript e HTML sejam minificados (removendo espaços em branco, comentários) e servidos com compressão GZIP ou Brotli.
    *   **Ferramenta**: `uglify-js` (JS), `cssnano` (CSS), ou módulos de servidor (mod_deflate para Apache, gzip para Nginx).
    *   **