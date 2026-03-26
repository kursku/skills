---
name: image-seo
description: "Image Seo — Skill especializada para otimizar imagens para mecanismos de busca, melhorando a visibilidade e performance."
license: MIT
metadata:
  version: 1.0.0
  author: Cafe Code AI
  category: 05-seo-busca
  updated: 2026-03-01
risk: safe
---

# Image Seo

Esta skill capacita o Claude a otimizar imagens digitalmente para SEO, focando em performance, visibilidade em buscas e experiência do usuário.

---

## Keywords

`otimização de imagens`, `alt text`, `lazy loading`, `srcset`, `webP`, `schema markup imagem`, `compressão de imagem`, `nome de arquivo imagem`, `imagem responsiva`, `sitemap de imagens`, `CDN imagens`, `Core Web Vitals imagens`, `LCP imagem`, `CLS imagem`.

---

## Quick Start

1.  **Comprimir Imagens Existentes**: Utilize TinyPNG ou Squoosh para reduzir o tamanho de todas as imagens, priorizando o formato WebP.
2.  **Renomear Arquivos Descritivamente**: Altere nomes genéricos como `IMG001.jpg` para `tenis-corrida-masculino-nike-air.webp` antes de subir.
3.  **Preencher Alt Text Otimizado**: Adicione descrições concisas e ricas em palavras-chave no atributo `alt` de cada imagem.
4.  **Implementar Lazy Loading**: Ative o carregamento preguiçoso para imagens fora da dobra, utilizando `loading="lazy"` ou um plugin.
5.  **Especificar Dimensões**: Adicione os atributos `width` e `height` para todas as tags `<img>` e `picture`.

---

## Core Workflows

### Workflow 1: Otimização de Imagens para Produtos de E-commerce

Este workflow foca em garantir que as imagens de produtos contribuam para a visibilidade em buscas de produtos e melhorem a experiência de compra.

**Passos Detalhados:**

1.  **Padronização de Dimensionamento e Formato:**
    *   **Dimensão**: Defina uma largura máxima padrão para imagens de produto (ex: 1200px para a imagem principal, 800px para miniaturas). Mantenha a proporção original.
    *   **Formato**: Priorize WebP para todas as imagens. Se não for possível, utilize JPEG progressivo com compressão entre 80-85%.
    *   **Ferramentas**: Use ferramentas como Squoosh (web), ImageOptim (macOS) ou plugins de CMS (ex: Imagify para WordPress) para automação.
    *   **Exemplo**: Uma imagem de 1920x1080px deve ser redimensionada para 1200px de largura (mantendo a proporção) e convertida para `.webp`.

2.  **Nomenclatura de Arquivos Otimizada:**
    *   **Formato**: Use hífens para separar palavras, minúsculas e inclua a palavra-chave principal do produto, SKU e, se relevante, cor ou modelo.
    *   **Evitar**: Nomes genéricos, caracteres especiais, espaços.
    *   **Exemplo**: Em vez de `DSC00123.jpg`, use `tenis-corrida-nike-air-zoom-pegasus-38-azul-sku12345.webp`.

3.  **Preenchimento de Alt Text Estratégico:**
    *   **Objetivo**: Descrever a imagem de forma concisa para usuários cegos e mecanismos de busca, incluindo a palavra-chave principal do produto.
    *   **Conteúdo**: A descrição deve ser natural e não uma lista de palavras-chave.
    *   **Exemplo**: `<img src="tenis-corrida-nike-air-zoom-pegasus-38-azul-sku12345.webp" alt="Tênis de corrida masculino Nike Air Zoom Pegasus 38 azul, vista lateral">`. Para diferentes ângulos, varie a descrição: `alt="Detalhe da sola do Tênis Nike Air Zoom Pegasus 38"`.

4.  **Implementação de Imagens Responsivas (srcset e sizes):**
    *   **Objetivo**: Entregar o tamanho de imagem mais adequado para cada dispositivo, melhorando a velocidade de carregamento.
    *   **Uso**: Utilize os atributos `srcset` e `sizes` na tag `<img>`.
    *   **Exemplo**:
        ```html
        <img src="tenis-corrida-padrao.webp"
             alt="Tênis de corrida masculino Nike Air Zoom Pegasus 38 azul"
             width="1200" height="800"
             srcset="tenis-corrida-320w.webp 320w,
                     tenis-corrida-640w.webp 640w,
                     tenis-corrida-1200w.webp 1200w"
             sizes="(max-width: 600px) 320px,
                    (max-width: 1024px) 640px,
                    1200px">
        ```

5.  **Uso de Schema Markup para Produtos:**
    *   **Objetivo**: Fornecer dados estruturados aos mecanismos de busca, aumentando a chance de rich results na busca de imagens e produtos.
    *   **Implementação**: Inclua a propriedade `image` dentro do `Product` Schema.
    *   **Exemplo**: Veja o template de Schema Markup abaixo.

### Workflow 2: Otimização Semântica de Imagens para Conteúdo (Blogs/Artigos)

Este workflow otimiza imagens inseridas em artigos de blog ou páginas de conteúdo, visando relevância contextual e performance.

**Passos Detalhados:**

1.  **Seleção e Contextualização da Imagem:**
    *   **Relevância**: Escolha imagens que complementem e ilustrem o texto adjacente, não apenas decorativas.
    *   **Qualidade**: Prefira imagens de alta resolução e relevância visual para o tópico do parágrafo.
    *   **Exemplo**: Em um artigo sobre "Melhores Estratégias de SEO 2024", insira um infográfico sobre "SEO On-Page Checklist" ao lado da seção correspondente.

2.  **Dimensionamento e Compressão para Conteúdo:**
    *   **Dimensão**: Redimensione imagens para se adequarem à largura do layout do conteúdo (ex: 800px para imagens de corpo de texto, 1200px para imagens de destaque).
    *   **Compressão**: Use WebP sempre que possível. Para gráficos e ilustrações com poucas cores, PNG otimizado pode ser uma alternativa, mas WebP é preferencial.
    *   **Exemplo**: Um gráfico explicando um conceito de marketing digital deve ter 800px de largura e ser salvo como `grafico-ciclo-de-vida-cliente.webp`.

3.  **Nomenclatura de Arquivos com Palavras-Chave de Conteúdo:**
    *   **Formato**: Use palavras-chave relevantes ao tema do artigo ou parágrafo onde a imagem está inserida.
    *   **Exemplo**: Para um gráfico em um artigo sobre "SEO Técnico", use `auditoria-seo-tecnico-checklist.webp`. Evite `grafico1.webp`.

4.  **Alt Text Descritivo e Semântico:**
    *   **Objetivo**: Descrever o conteúdo visual da imagem de forma útil, incorporando palavras-chave do contexto do artigo.
    *   **Conteúdo**: Vá além da simples descrição. Pense no que a imagem representa para o leitor e para o tópico.
    *   **Exemplo**: Para uma imagem de um gráfico: `alt="Gráfico de barras mostrando o crescimento do tráfego orgânico após a implementação de SEO técnico em um site de e-commerce"`.

5.  **Uso de Legendas (Captions):**
    *   **Objetivo**: Fornecer contexto adicional visível para o usuário, que também pode ser lido pelos mecanismos de busca, reforçando a relevância da imagem.
    *   **Implementação**: Use a tag `<figcaption>` dentro de `<figure>`.
    *   **Exemplo**:
        ```html
        <figure>
          <img src="auditoria-seo-tecnico-checklist.webp" alt="Checklist para auditoria de SEO técnico com 15 itens principais" width="800" height="500">
          <figcaption><em>Checklist detalhado para a realização de uma auditoria completa de SEO técnico em seu website.</em></figcaption>
        </figure>
        ```

6.  **Lazy Loading para Todas as Imagens Fora da Dobra:**
    *   **Objetivo**: Melhorar o Largest Contentful Paint (LCP) e o tempo total de carregamento da página, carregando imagens apenas quando o usuário rola a página até elas.
    *   **Implementação**: Adicione `loading="lazy"` à tag `<img>`.
    *   **Exemplo**: `<img src="imagem-do-meio-do-artigo.webp" alt="..." loading="lazy" width="800" height="600">`.

---

## Templates

### Nome de Arquivo e Alt Text para Produto (Exemplo: Blusa Feminina)

```
Nome do arquivo: blusa-feminina-malha-algodao-azul-marinho-p-sku789.webp
Alt Text: Blusa feminina de malha de algodão azul marinho, tamanho P, vista frontal
```

### Schema Markup para Imagem (dentro de Product Schema)

```json
{
  "@context": "https://schema.org/",
  "@type": "Product",
  "name": "Smartphone Samsung Galaxy S24 Ultra 5G 512GB",
  "image": [
    "https://www.exemplo.com.br/imagens/galaxy-s24-ultra-frontal-titanio-preto.webp",
    "https://www.exemplo.com.br/imagens/galaxy-s24-ultra-traseira-titanio-preto.webp",
    "https://www.exemplo.com.br/imagens/galaxy-s24-ultra-lateral-caneta.webp"
   ],
  "description": "O novo Samsung Galaxy S24 Ultra 5G com inteligência artificial Galaxy AI, câmera de 200MP e S Pen integrada na cor Titânio Preto.",
  "sku": "SM-S928BZKLZTO",
  "brand": {
    "@type": "Brand",
    "name": "Samsung"
  },
  "offers": {
    "@type": "Offer",
    "url": "https://www.exemplo.com.br/produto/galaxy-s24-ultra-512gb",
    "priceCurrency": "BRL",
    "price": "7299.00",
    "itemCondition": "https://schema.org/NewCondition",
    "availability": "https://schema.org/InStock"
  }
}
```

---

## Checklist

- [x] Imagens comprimidas para WebP ou JPEG progressivo (<150KB para a maioria)?
- [x] Nomes de arquivo são descritivos, em minúsculas, com hífens e palavras-chave?
- [x] Alt text preenchido em todas as imagens com descrições relevantes e palavras-chave (não stuffing)?
- [x] Atributos `srcset` e `sizes` implementados para imagens responsivas?
- [x] Lazy loading ativado para todas as imagens fora da dobra da página (`loading="lazy"`)?
- [x] Imagens principais (LCP) com `preload` implementado?
- [x] Dimensões de imagem explícitas (`width` e `height`) na tag HTML?
- [x] Imagens incluídas no sitemap XML de imagens, se aplicável?
- [x] URLs de imagem são amigáveis, consistentes e estruturadas?
- [x] Schema Markup (Product, Article, ImageObject) referenciando as imagens?
- [x] Legendas (captions) utilizadas para contextualizar imagens em artigos?
- [x] Conteúdo visual relevante ao texto adjacente, não apenas decorativo?

---

## Métricas de Referência

| Métrica                      | Benchmark (Bom) | Meta (Aspiracional) |
|------------------------------|-----------------|---------------------|
| LCP (Largest Contentful Paint) | < 2.5 segundos  | < 1.8 segundos      |
| CLS (Cumulative Layout Shift)  | < 0.1           | < 0.05              |
| Tráfego da Busca de Imagens    | > 5% do orgânico| > 10% do orgânico   |
| Taxa de Compressão Média       | > 70%           | > 85%               |
| Tempo de Carregamento Imagens  | < 500 ms        | < 300 ms            |

---

## Erros Comuns

1.  **Alt text genérico ou ausente**: Utilizar `alt="imagem"` ou deixar o atributo vazio. Isso impede que os mecanismos de busca e leitores de tela compreendam o contexto da imagem.
    *   **Como evitar**: Descreva o conteúdo visual da imagem de forma concisa e inclua palavras-chave relevantes.
    *   **Exemplo**: Em vez de `<img src="grafico.webp" alt="imagem">`, use `<img src="grafico-desempenho-seo.webp" alt="Gráfico de barras mostrando o desempenho de SEO do último trimestre com aumento de tráfego">`.

2.  **Imagens não comprimidas ou em formato pesado**: Uploadar imagens em formatos como PNG para fotos complexas ou JPEG sem otimização, resultando em arquivos grandes que atrasam o carregamento da página.
    *   **Como evitar**: Converta imagens para WebP sempre que possível. Para JPEGs, use compressão de 80-85%. Use ferramentas como Squoosh, TinyPNG ou plugins de otimização de imagem.
    *   **Exemplo**: Evite imagens de 2MB. Otimize para que fiquem abaixo de 150KB para a maioria dos casos.

3.  **Não especificar dimensões (`width`, `height`) no HTML**: Isso causa o "Cumulative Layout Shift" (CLS), pois o navegador precisa recalcular o layout da página após o carregamento das imagens.
    *   **Como evitar**: Sempre inclua os atributos `width` e `height` nas tags `<img>` e `<picture>`.
    *   **Exemplo**: Em vez de `<img src="produto.webp" alt="Produto">`, use `<img src="produto.webp" alt="Produto" width="800" height="600">`.

---

## Dicas Avançadas

1.  **CDNs Otimizados para Imagens**: Implemente um CDN (Content Delivery Network) que ofereça otimização automática de imagens (ex: Cloudinary, Imgix, Akamai). Esses serviços podem redimensionar, comprimir e converter imagens para o formato ideal (ex: WebP) em tempo real, baseado no dispositivo e navegador do usuário, além de entregá-las a partir do servidor mais próximo.
    *   **Exemplo**: Ao invés de `dominio.com/img/original.jpg`, use `cloudinary.com/minha-conta/image/upload/f_auto,q_auto,w_800/original.jpg`.

2.  **Sitemap de Imagens Dedicado**: Para sites com um grande volume de imagens (e-commerce, galerias de fotos), crie um sitemap XML exclusivo para imagens. Isso ajuda o Google a descobrir e indexar todas as suas imagens de forma mais eficiente, especialmente aquelas que não estão diretamente ligadas a uma página indexável.
    *   **Estrutura**: `<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:image="http://www.google.com/schemas/sitemap-image/1.1"><url><loc>https://www.exemplo.com.br/pagina-do-produto.html</loc><image:image><image:loc>https://www.exemplo.com.br/imagens/produto-principal.webp</image:loc><image:title>Smartphone X</image:title><image:caption>Smartphone X com tela OLED</image:caption></image:image></url></urlset>`.

3.  **Preload de Imagens LCP**: Identifique a imagem que contribui para o Largest Contentful Paint (LCP) da sua página e adicione um `link rel="preload"` no cabeçalho HTML. Isso instrui o navegador a carregar essa imagem com alta prioridade, melhorando significativamente a métrica LCP.
    *   **Exemplo**: `<link rel="preload" as="image" href="/imagens/hero-banner-otimizado.webp">` (coloque antes de qualquer tag de script bloqueadora).

4.  **Uso da Tag `<picture>` para Controle Fino de Formatos/Resoluções**: A tag `<picture>` oferece controle granular sobre a entrega de diferentes formatos de imagem (ex: WebP para navegadores modernos, JPEG para fallback) ou diferentes resoluções para diferentes viewports, garantindo a melhor imagem para cada cenário.
    *   **Exemplo**:
        ```html
        <picture>
          <source srcset="imagem-desktop.webp" media="(min-width: 1024px)" type="image/webp">
          <source srcset="imagem-mobile.webp" media="(max-width: 1023px)" type="image/webp">
          <source srcset="imagem-desktop.jpg" media="(min-width: 1024px)" type="image/jpeg">
          <source srcset="imagem-mobile.jpg" media="(max-width: 1023px)" type="image/jpeg">
          <img src="imagem-fallback.jpg" alt="Descrição da imagem responsiva" width="1200" height="800">
        </picture>
        ```

5.  **Análise e Monitoramento com Lighthouse e Search Console**: Use o Google Lighthouse para auditar regularmente o desempenho das imagens em suas páginas, prestando atenção às recomendações de "Properly size images", "Defer offscreen images", e "Serve images in next-gen formats". Monitore o relatório "Experiência da página" no Google Search Console para identificar problemas de Core Web Vitals relacionados a imagens.