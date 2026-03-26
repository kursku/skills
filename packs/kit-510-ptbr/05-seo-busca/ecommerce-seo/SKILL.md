---
name: ecommerce-seo
description: "Ecommerce Seo — Skill especializada para otimização de motores de busca em plataformas de comércio eletrônico, abrangendo aspectos técnicos, de conteúdo e autoridade."
license: MIT
metadata:
  version: 1.0.0
  author: Cafe Code AI
  category: 05-seo-busca
  updated: 2026-03-01
risk: safe
---

# Ecommerce Seo

Esta skill capacita o Claude a se tornar um especialista em otimização de mecanismos de busca para e-commerce, focando em aumento de visibilidade orgânica, tráfego qualificado e conversões.

---

## Keywords

*   SEO para e-commerce
*   Otimização de produtos online
*   Schema markup e-commerce
*   Link building para lojas virtuais
*   Velocidade de carregamento e-commerce
*   SEO técnico para marketplaces
*   Pesquisa de palavras-chave transacionais
*   Conteúdo para categorias de loja
*   Auditoria SEO de e-commerce
*   Otimização de imagens de produto
*   Gestão de URL para e-commerce
*   Páginas de produto SEO

---

## Quick Start

1.  **Auditar estrutura de URLs e indexação**: Utilize o Google Search Console para identificar páginas não indexadas ou com erros de rastreamento (ex: erros 4xx, 5xx) e verifique a padronização de URLs para produtos e categorias (ex: `https://www.lojaexemplo.com.br/categoria/produto-sku`).
2.  **Mapear palavras-chave transacionais**: Execute uma pesquisa focada em termos com alta intenção de compra para as 5 categorias de produtos mais vendidas, usando ferramentas como Semrush ou Ahrefs para identificar termos como "comprar [nome do produto]", "[modelo] preço", "melhor [tipo de produto] online".
3.  **Implementar Schema Markup de Produto**: Adicione o Schema.org `Product` e `Offer` em formato JSON-LD nas 10 páginas de produto com maior volume de buscas, incluindo `name`, `image`, `description`, `sku`, `brand`, `offers` (com `price`, `priceCurrency`, `availability`).
4.  **Otimizar velocidade das páginas principais**: Analise as 5 páginas de categoria e 5 páginas de produto mais visitadas com PageSpeed Insights, focando em métricas como LCP (Largest Contentful Paint) abaixo de 2.5s e CLS (Cumulative Layout Shift) abaixo de 0.1, comprimindo imagens e adiando scripts não essenciais.
5.  **Revisar meta descrições e títulos para CTR**: Crie títulos (max 60 caracteres) e meta descrições (max 155 caracteres) atraentes para as 20 páginas de produto e 5 de categoria com maior tráfego orgânico, incluindo a palavra-chave principal e um CTA implícito (ex: "Oferta exclusiva", "Entrega rápida").

---

## Core Workflows

### Workflow 1: Otimização On-Page Completa para Páginas de Produto de Alto Potencial

Este workflow visa maximizar a visibilidade e a taxa de cliques de páginas de produto específicas, transformando-as em ativos de SEO poderosos.

1.  **Identificação de Produtos de Alto Potencial**:
    *   **Passo**: Utilize dados de vendas da plataforma de e-commerce e relatórios de palavras-chave do Google Search Console.
    *   **Exemplo**: Filtrar produtos que geram mais de R$5.000/mês em vendas ou que aparecem na primeira página do Google para termos como "aspirador de pó robô [marca]" com CTR orgânico abaixo de 3% (indicando potencial de melhoria).
2.  **Pesquisa de Palavras-Chave Transacionais Específicas**:
    *   **Passo**: Além do nome do produto, pesquise sinônimos, variações de marca/modelo e termos de cauda longa com intenção de compra.
    *   **Exemplo**: Para "Smart TV Samsung 55 polegadas 4K", pesquisar "TV 55 polegadas Samsung UHD", "preço Smart TV Samsung 55", "melhor TV 4K Samsung 55". Ferramentas: Semrush, Ahrefs.
3.  **Otimização do Título da Página (Title Tag)**:
    *   **Passo**: Incluir a palavra-chave principal, marca, modelo e um diferencial, mantendo até 60 caracteres.
    *   **Exemplo**: `Smart TV Samsung 55" 4K | Modelo QN55Q60BAGXZD | LojaExemplo`
4.  **Criação de Meta Descrição Atrativa**:
    *   **Passo**: Escrever uma descrição concisa (até 155 caracteres) que inclua a palavra-chave, benefícios e um call-to-action (CTA).
    *   **Exemplo**: `Compre a Smart TV Samsung 55" 4K QLED com Tizen e controle de voz. Imagens vívidas e som imersivo. Frete grátis na LojaExemplo!`
5.  **Otimização do Conteúdo da Página de Produto**:
    *   **Passo**: Desenvolver descrições de produto detalhadas (mínimo 300 palavras), utilizando as palavras-chave secundárias e termos LSI (Indexação Semântica Latente). Incluir seções de "Benefícios", "Especificações Técnicas", "Perguntas Frequentes".
    *   **Exemplo**: Para um "Fone de Ouvido Bluetooth Sony WH-1000XM5", a descrição deve abordar cancelamento de ruído, bateria, conforto, qualidade de áudio, conectividade, e incluir termos como "headphone sem fio", "fone cancelamento de ruído", "melhor fone Sony".
6.  **Otimização de Imagens e Vídeos**:
    *   **Passo**: Comprimir imagens (WebP, JPEG otimizado), adicionar `alt text` descritivo com palavras-chave, e otimizar vídeos para carregamento rápido (YouTube embed, lazy load).
    *   **Exemplo**: `alt="Fone de Ouvido Bluetooth Sony WH-1000XM5 com cancelamento de ruído"`
7.  **Implementação de Schema Markup Avançado**:
    *   **Passo**: Além de `Product` e `Offer`, adicione `Review` (avaliações de clientes), `AggregateRating` (classificação média) e `BreadcrumbList`.
    *   **Exemplo**: Adicionar `itemReviewed` apontando para o produto, com `author`, `datePublished`, `reviewBody` e `ratingValue`.
8.  **Linkagem Interna Estratégica**:
    *   **Passo**: Linkar a página de produto a partir de páginas de categoria relevantes, posts de blog relacionados e outros produtos complementares.
    *   **Exemplo**: Em um post de blog sobre "Melhores fones para viajar", criar um link contextual para a página do "Fone de Ouvido Bluetooth Sony WH-1000XM5".

### Workflow 2: Construção de Autoridade para Páginas de Categoria Através de Link Building e Conteúdo Estratégico

Este workflow foca em fortalecer a autoridade das páginas de categoria, que são cruciais para o ranqueamento de termos mais amplos e competitivos.

1.  **Análise de Concorrência para Backlinks**:
    *   **Passo**: Identificar as 3-5 principais páginas de categoria concorrentes que ranqueiam para as palavras-chave alvo. Usar Ahrefs ou Semrush para analisar seus perfis de backlink.
    *   **Exemplo**: Para a categoria "Smartphones", analisar os backlinks das páginas de categoria de grandes varejistas como Magazine Luiza, Americanas, Casas Bahia.
2.  **Identificação de Oportunidades de Conteúdo para Linkagem**:
    *   **Passo**: Pesquisar blogs, portais de notícias e sites de nicho que já linkam para concorrentes ou que poderiam se beneficiar de conteúdo relacionado aos produtos da categoria.
    *   **Exemplo**: Buscar blogs de tecnologia que escrevem sobre "review de celulares", "melhores smartphones 2024", "comparativo de câmeras de celular".
3.  **Criação de Conteúdo "Linkable Asset"**:
    *   **Passo**: Desenvolver conteúdo de alta qualidade (guias, infográficos, estudos de caso, comparativos detalhados) que possa atrair links naturais e ser utilizado em campanhas de outreach.
    *   **Exemplo**: Criar um "Guia Completo para Escolher Seu Primeiro Smartphone Android" ou um "Comparativo Detalhado das Câmeras dos Top 5 Smartphones do Ano". Publicar este conteúdo no blog do e-commerce.
4.  **Campanha de Outreach Personalizada**:
    *   **Passo**: Entrar em contato com editores e webmasters de sites relevantes, apresentando o conteúdo "linkable asset" e sugerindo a inclusão de um link para ele (e, indiretamente, para a página de categoria relevante).
    *   **Exemplo**: Enviar e-mail para editores de sites de tecnologia como Tecnoblog, Canaltech, TudoCelular, com o assunto "Conteúdo exclusivo: Guia de Smartphones para o seu blog".
5.  **Otimização do Conteúdo da Página de Categoria**:
    *   **Passo**: Reforçar o conteúdo textual da página de categoria com introduções detalhadas (mínimo 200 palavras), FAQs específicos da categoria e pequenos parágrafos descritivos para subcategorias ou filtros mais importantes.
    *   **Exemplo**: Na página de "Smartphones", adicionar uma introdução sobre a evolução dos celulares, e uma seção de "Perguntas Frequentes sobre Smartphones" (ex: "Qual a diferença entre Android e iOS?", "Como escolher o melhor processador?").
6.  **Monitoramento e Relatórios de Backlinks**:
    *   **Passo**: Acompanhar o crescimento do número de backlinks e o Domain Authority (DA) ou Domain Rating (DR) da página de categoria e do domínio.
    *   **Exemplo**: Utilizar Ahrefs para monitorar novos backlinks, domínios de referência e a evolução do DR. Relatar o impacto no ranqueamento das palavras-chave da categoria.

---

## Templates

### Schema Markup de Produto (JSON-LD)

```json
{
  "@context": "https://schema.org/",
  "@type": "Product",
  "name": "Smart TV Samsung 55 Polegadas 4K Neo QLED QN55QN90CAGXZD",
  "image": [
    "https://www.lojaexemplo.com.br/imagens/tv-samsung-55-frontal.jpg",
    "https://www.lojaexemplo.com.br/imagens/tv-samsung-55-lateral.jpg",
    "https://www.lojaexemplo.com.br/imagens/tv-samsung-55-controle.jpg"
  ],
  "description": "Experimente a próxima geração de imagem com a Smart TV Samsung 55 polegadas 4K Neo QLED. Tecnologia Mini LED, processador Neural Quantum 4K, e som imersivo com Dolby Atmos. Perfeita para filmes, jogos e esportes.",
  "sku": "QN55QN90CAGXZD",
  "mpn": "QN55QN90CAGXZD",
  "brand": {
    "@type": "Brand",
    "name": "Samsung"
  },
  "review": {
    "@type": "Review",
    "reviewRating": {
      "@type": "Rating",
      "ratingValue": "5",
      "bestRating": "5"
    },
    "author": {
      "@type": "Person",
      "name": "Mariana Silva"
    },
    "datePublished": "2024-02-15",
    "reviewBody": "Imagem fantástica e som impressionante. A melhor TV que já tive!",
    "itemReviewed": {
        "@type": "Product",
        "name": "Smart TV Samsung 55 Polegadas 4K Neo QLED QN55QN90CAGXZD"
    }
  },
  "aggregateRating": {
    "@type": "AggregateRating",
    "ratingValue": "4.8",
    "reviewCount": "125"
  },
  "offers": {
    "@type": "Offer",
    "url": "https://www.lojaexemplo.com.br/smart-tv-samsung-55-neo-qled",
    "priceCurrency": "BRL",
    "price": "5999.00",
    "priceValidUntil": "2024-12-31",
    "itemCondition": "https://schema.org/NewCondition",
    "availability": "https://schema.org/InStock",
    "seller": {
      "@type": "Organization",
      "name": "LojaExemplo"
    }
  }
}
```

### Template de Meta Descrição para Categoria de Produto

```
[Palavra-chave Principal da Categoria] | [Número] Modelos Disponíveis | [Benefício/Diferencial]. Compre [Tipo de Produto] online com [Chamada para Ação: Frete Grátis/Melhores Preços/Entrega Rápida] na LojaExemplo.
```

**Exemplo Preenchido:**

`Smartphones | Mais de 200 Modelos Disponíveis | Conectividade e Inovação. Compre celulares online com os melhores preços e entrega rápida na LojaExemplo.`

---

## Checklist

- [X] URLs amigáveis e otimizadas para todas as páginas de produto e categoria.
- [X] Implementação de `canonical tags` para evitar conteúdo duplicado (ex: variantes de produto, páginas de filtro).
- [X] Otimização de títulos (Title Tags) e meta descrições com palavras-chave e CTAs.
- [X] Conteúdo rico e exclusivo nas páginas de produto (mínimo 300 palavras) e categoria (mínimo 200 palavras).
- [X] Imagens de produto otimizadas (compressão, alt text descritivo, lazy load).
- [X] Implementação de Schema Markup (Product, Offer, Review, AggregateRating, BreadcrumbList) em JSON-LD.
- [X] Velocidade de carregamento (LCP < 2.5s, CLS < 0.1) monitorada e otimizada via PageSpeed Insights.
- [X] Criação de links internos contextuais entre produtos, categorias e posts de blog.
- [X] Auditoria de erros 4xx e 5xx com redirecionamentos 301 implementados para páginas descontinuadas.
- [X] Configuração e monitoramento de desempenho no Google Search Console e Google Analytics 4.

---

## Métricas de Referência

| Métrica                 | Benchmark (E-commerce) | Meta (E-commerce)     |
|-------------------------|------------------------|-----------------------|
| Taxa de Conversão Orgânica | 1.5% - 3%              | > 3.5%                |
| Receita por Usuário Orgânico | R$ 50 - R$ 150         | > R$ 180              |
| Posição Média de KW      | 8 - 15 (top 10 KWs)    | < 5 (top 10 KWs)      |
| CTR Orgânico              | 2% - 5% (1ª página)    | > 6% (1ª página)      |
| LCP (Largest Contentful Paint) | 2.5s - 4s              | < 2.5s                |
| Taxa de Rejeição Orgânica | 30% - 50%              | < 25%                 |

---

## Erros Comuns

1.  **Conteúdo duplicado gerado por filtros de navegação**: Lojas virtuais frequentemente criam URLs únicas para cada combinação de filtros (cor, tamanho, marca), resultando em centenas de páginas quase idênticas.
    *   **Como evitar**: Implementar `canonical tags` apontando para a URL da categoria principal ou usar `noindex, follow` para URLs de filtro com baixo valor de SEO, além de parametrizar URLs no Google Search Console para que o Google as ignore. Exemplo: `https://www.loja.com.br/camisas?cor=azul&tamanho=m` deve ter canonical para `https://www.loja.com.br/camisas`.
2.  **Imagens de produto sem otimização (peso, alt text)**: Imagens grandes e sem atributos `alt` impactam negativamente a velocidade de carregamento e a acessibilidade, perdendo oportunidades de ranqueamento em busca de imagens.
    *   **Como evitar**: Comprimir todas as imagens para WebP ou JPEG otimizado antes de fazer upload. Adicionar `alt text` descritivos que incluam a palavra-chave do produto. Exemplo: `alt="Tênis Esportivo Masculino Nike Air Zoom Pegasus 39 Azul"`.
3.  **Páginas de produto descontinuadas ou fora de estoque sem redirecionamento 301**: Produtos que saem do catálogo ou ficam permanentemente fora de estoque e geram erros 404, prejudicam a experiência do usuário e o crawl budget.
    *   **Como evitar**: Implementar redirecionamento 301 para uma página de produto similar, para a categoria superior ou para uma página de "produtos relacionados". Evitar redirecionar para a homepage. Exemplo: Redirecionar `https://www.loja.com.br/produto-antigo` para `https://www.loja.com.br/produto-novo-similar` ou `https://www.loja.com.br/categoria-do-produto`.

---

## Dicas Avançadas

1.  **Implementação de Price Drop Schema para alertas de preço**: Utilize o Schema.org `Offer` para marcar preços de produtos e, quando o preço cair, atualize o `price` e adicione a propriedade `hasOfferCatalog` se aplicável. Isso pode habilitar alertas de preço nos resultados de busca do Google, aumentando o CTR.
    *   **Exemplo**: Atualizar o `price` de R$1200 para R$999 em um produto, e a data `priceValidUntil` para refletir a promoção.
2.  **Otimização para busca por voz e assistentes de compra**: Estruture o conteúdo das descrições de produtos e FAQs com linguagem natural e perguntas e respostas diretas que os usuários fariam a assistentes de voz. Utilize Schema `Question` e `Answer` para FAQs.
    *   **Exemplo**: Em uma página de produto de cafeteira, incluir a pergunta "Qual o melhor tipo de café para essa máquina?" e sua resposta clara.
3.  **Personalização de resultados de busca com dados de CRM/Histórico de Compras**: Embora não seja um recurso direto de SEO, a integração de dados de CRM permite entender melhor o comportamento do cliente e criar clusters de produtos que podem ser promovidos em conteúdo de blog ou guias para atrair tráfego orgânico mais qualificado e personalizado.
    *   **Exemplo**: Se muitos clientes compram "câmeras DSLR" e "lentes zoom", criar um guia de "Como escolher lentes para fotografia de paisagem com sua DSLR" e linkar para produtos relevantes.
4.  **Uso de hreflang para e-commerce multiregional/multilíngue**: Para lojas que operam em diferentes países ou idiomas, implemente tags `hreflang` corretamente para indicar ao Google as versões de página específicas para cada região/idioma, evitando duplicação de conteúdo e direcionando o usuário certo para a loja certa.
    *   **Exemplo**: Na página `loja.com/br/tenis`, adicionar `<link rel="alternate" hreflang="en-us" href="https://loja.com/us/sneakers" />` e `<link rel="alternate" hreflang="x-default" href="https://loja.com/br/tenis" />`.
5.  **Criação de Páginas de Subcategorias e Páginas de Filtro com Conteúdo Otimizado**: Em vez de apenas bloquear páginas de filtro, identifique combinações de filtros populares que podem ser transformadas em subcategorias reais com conteúdo único, títulos otimizados e URL amigável.
    *   **Exemplo**: A partir de `loja.com/camisas`, se "camisas sociais masculinas" for um termo com volume, criar `loja.com/camisas/sociais-masculinas` com sua própria otimização.