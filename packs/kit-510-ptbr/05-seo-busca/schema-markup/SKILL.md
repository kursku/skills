---
name: schema-markup
description: "Schema Markup — Skill especializada para schema markup"
license: MIT
metadata:
  version: 1.0.0
  author: Cafe Code AI
  category: 05-seo-busca
  updated: 2026-03-01
risk: safe
---

# Schema Markup

Esta skill capacita o Claude a gerar, validar e otimizar implementações de Schema Markup para melhorar a visibilidade em resultados de busca enriquecidos.

---

## Keywords

*   Schema.org
*   JSON-LD
*   Rich Snippets
*   Structured Data
*   Google Search Console
*   Validação Schema
*   SEO Técnico
*   Microdata
*   RDFa
*   Knowledge Graph
*   Product Schema
*   Article Schema
*   FAQPage Schema

---

## Quick Start

1.  **Identifique o tipo de conteúdo**: Determine qual tipo de Schema.org melhor descreve a página (e.g., `Article`, `Product`, `LocalBusiness`).
2.  **Gere JSON-LD inicial**: Utilize um gerador como o Merkle Schema Markup Generator para criar o código JSON-LD básico para o tipo de conteúdo escolhido.
3.  **Insira o código na página**: Adicione o script JSON-LD dentro da seção `<head>` ou `<body>` do HTML da página.
4.  **Valide com a ferramenta do Google**: Teste o URL da página no [Google Rich Results Test](https://search.google.com/test/rich-results) para verificar erros e pré-visualizar os rich snippets.
5.  **Monitore no Search Console**: Acompanhe o desempenho e a cobertura dos rich snippets na seção "Aprimoramentos" do Google Search Console.

---

## Core Workflows

### Workflow 1: Implementação de Schema.org para Artigo (Article)

Este workflow descreve a criação e inserção de Schema Markup `Article` para um post de blog, otimizando-o para exibir rich snippets de notícias ou artigos.

1.  **Selecione o tipo `Article`**: Para posts de blog, artigos de notícias ou publicações editoriais, `Article` (ou sub-tipos como `NewsArticle` ou `BlogPosting`) é o mais adequado.
2.  **Identifique as propriedades essenciais**: Um `Article` básico requer `headline`, `image`, `datePublished`, `dateModified`, `author` (com `name` e `url`), `publisher` (com `name` e `logo`).
    *   `headline`: Título principal do artigo, por exemplo, "Guia Completo de Schema Markup para SEO".
    *   `image`: URL de uma imagem representativa do artigo (mínimo 696px de largura), por exemplo, "https://www.exemplo.com.br/imagens/schema-markup-guia.jpg".
    *   `datePublished`: Data de publicação no formato ISO 8601, por exemplo, "2023-10-27T08:00:00+03:00".
    *   `dateModified`: Data da última modificação, se houver, no mesmo formato. Se não houver, pode ser igual a `datePublished`.
    *   `author`: Um objeto `Person` ou `Organization` com `name` ("João Silva") e `url` ("https://www.exemplo.com.br/autores/joao-silva").
    *   `publisher`: Um objeto `Organization` com `name` ("Exemplo Blog") e `logo` (URL da imagem do logo da organização, por exemplo, "https://www.exemplo.com.br/imagens/logo-exemplo.png").
3.  **Gere o JSON-LD**: Crie o script JSON-LD com as propriedades identificadas.
    ```json
    <script type="application/ld+json">
    {
      "@context": "https://schema.org",
      "@type": "Article",
      "headline": "Guia Completo de Schema Markup para SEO",
      "image": [
        "https://www.exemplo.com.br/imagens/schema-markup-guia.jpg"
       ],
      "datePublished": "2023-10-27T08:00:00+03:00",
      "dateModified": "2023-10-27T10:30:00+03:00",
      "author": {
        "@type": "Person",
        "name": "João Silva",
        "url": "https://www.exemplo.com.br/autores/joao-silva"
      },
      "publisher": {
        "@type": "Organization",
        "name": "Exemplo Blog",
        "logo": {
          "@type": "ImageObject",
          "url": "https://www.exemplo.com.br/imagens/logo-exemplo.png"
        }
      },
      "description": "Aprenda a implementar e otimizar Schema Markup para melhorar a visibilidade de seus artigos nos resultados de busca."
    }
    </script>
    ```
4.  **Incorpore na página**: Adicione o bloco `<script>` gerado na seção `<head>` do HTML da página do artigo.
5.  **Valide e monitore**: Utilize o Google Rich Results Test para verificar a validade e o Google Search Console para monitorar a performance e identificar possíveis erros de rastreamento ou interpretação.

### Workflow 2: Otimização de Schema para Produtos (Product) com Reviews

Este workflow detalha a implementação de Schema Markup `Product` para uma página de produto de e-commerce, incluindo informações de preço, disponibilidade e avaliações agregadas.

1.  **Selecione o tipo `Product`**: Para páginas de produtos de e-commerce, utilize o tipo `Product`.
2.  **Identifique as propriedades essenciais para e-commerce**:
    *   `name`: Nome do produto, por exemplo, "Smartphone X Pro 128GB".
    *   `image`: URLs das imagens do produto, por exemplo, "https://www.loja.com/imagens/smxpro_frente.jpg".
    *   `description`: Descrição breve do produto.
    *   `sku` e `mpn`: Códigos de identificação do produto (Stock Keeping Unit, Manufacturer Part Number).
    *   `brand`: Marca do produto, por exemplo, "TechBrand".
    *   `offers`: Um objeto `Offer` que inclui `priceCurrency` ("BRL"), `price` ("2999.99"), `itemCondition` (`NewCondition`), `availability` (`InStock` ou `OutOfStock`), e `url` (URL da página do produto).
    *   `aggregateRating`: Um objeto `AggregateRating` para avaliações, incluindo `ratingValue` (média das avaliações, e.g., "4.7"), `reviewCount` (número total de avaliações, e.g., "125").
3.  **Gere o JSON-LD**: Crie o script JSON-LD com as propriedades identificadas.
    ```json
    <script type="application/ld+json">
    {
      "@context": "https://schema.org/",
      "@type": "Product",
      "name": "Smartphone X Pro 128GB",
      "image": [
        "https://www.loja.com/imagens/smxpro_frente.jpg",
        "https://www.loja.com/imagens/smxpro_traseira.jpg"
       ],
      "description": "O Smartphone X Pro oferece desempenho superior com câmera de 108MP e tela OLED.",
      "sku": "SMXPRO-128GB-BR",
      "mpn": "TECH-XPRO-128",
      "brand": {
        "@type": "Brand",
        "name": "TechBrand"
      },
      "offers": {
        "@type": "Offer",
        "url": "https://www.loja.com/produto/smartphone-x-pro",
        "priceCurrency": "BRL",
        "price": "2999.99",
        "itemCondition": "https://schema.org/NewCondition",
        "availability": "https://schema.org/InStock",
        "seller": {
          "@type": "Organization",
          "name": "Minha Loja Online"
        }
      },
      "aggregateRating": {
        "@type": "AggregateRating",
        "ratingValue": "4.7",
        "reviewCount": "125"
      },
      "review": [
        {
          "@type": "Review",
          "reviewRating": {
            "@type": "Rating",
            "ratingValue": "5"
          },
          "author": {
            "@type": "Person",
            "name": "Ana Paula"
          },
          "reviewBody": "Adorei o celular, câmera excelente e bateria dura muito!"
        }
      ]
    }
    </script>
    ```
4.  **Incorpore na página**: Insira o JSON-LD dentro da seção `<head>` ou `<body>` da página do produto.
5.  **Valide e monitore**: Use o Google Rich Results Test para garantir que os rich snippets de produto e avaliação sejam detectados corretamente. Acompanhe os relatórios de "Produto" e "Snippets de Avaliação" no Google Search Console.

---

## Templates

### JSON-LD para Evento (Event)

```json
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Event",
  "name": "Conferência de Marketing Digital 2024",
  "startDate": "2024-05-15T09:00",
  "endDate": "2024-05-17T18:00",
  "eventStatus": "https://schema.org/EventScheduled",
  "eventAttendanceMode": "https://schema.org/OfflineEventAttendanceMode",
  "location": {
    "@type": "Place",
    "name": "Centro de Convenções São Paulo",
    "address": {
      "@type": "PostalAddress",
      "streetAddress": "Rua das Flores, 123",
      "addressLocality": "São Paulo",
      "addressRegion": "SP",
      "postalCode": "01000-000",
      "addressCountry": "BR"
    }
  },
  "image": [
    "https://www.conferencia-marketing.com.br/imagens/banner-conferencia.jpg",
    "https://www.conferencia-marketing.com.br/imagens/logo-evento.png"
   ],
  "description": "A maior conferência de marketing digital do Brasil, com palestrantes renomados e workshops práticos.",
  "offers": {
    "@type": "Offer",
    "url": "https://www.conferencia-marketing.com.br/ingressos",
    "price": "599.00",
    "priceCurrency": "BRL",
    "availability": "https://schema.org/InStock",
    "validFrom": "2023-11-01T00:00"
  },
  "organizer": {
    "@type": "Organization",
    "name": "Agência Marketing Pro",
    "url": "https://www.agenciamarketingpro.com.br"
  }
}
</script>
```

### JSON-LD para Perguntas Frequentes (FAQPage)

```json
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [{
    "@type": "Question",
    "name": "O que é Schema Markup?",
    "acceptedAnswer": {
      "@type": "Answer",
      "text": "Schema Markup é um vocabulário de microdados que você pode adicionar ao seu HTML para ajudar os motores de busca a entender melhor o conteúdo das suas páginas. Isso pode levar a rich snippets nos resultados de busca."
    }
  },{
    "@type": "Question",
    "name": "Como implemento Schema Markup no meu site?",
    "acceptedAnswer": {
      "@type": "Answer",
      "text": "A forma mais recomendada é utilizando JSON-LD (JavaScript Object Notation for Linked Data). Você insere um bloco de código JavaScript com a estrutura de dados na seção &lt;head&gt; ou &lt;body&gt; da sua página."
    }
  },{
    "@type": "Question",
    "name": "Quais são os benefícios de usar Schema Markup?",
    "acceptedAnswer": {
      "@type": "Answer",
      "text": "Os principais benefícios incluem maior visibilidade nos resultados de busca através de rich snippets (estrelas de avaliação, preços, horários de evento), aumento da taxa de cliques (CTR) e uma melhor compreensão do seu conteúdo pelos motores de busca."
    }
  }]
}
</script>
```

---

## Checklist

- [x] O tipo de Schema Markup (`@type`) corresponde ao conteúdo principal da página (e.g., `Product` para produto, `Article` para blog post).
- [x] Todas as propriedades *obrigatórias* para o `@type` selecionado estão preenchidas.
- [x] Todas as propriedades *recomendadas* foram consideradas e, se aplicável, preenchidas.
- [x] Os dados no Schema Markup refletem *exatamente* o conteúdo visível na página (não oculto ou desatualizado).
- [x] O JSON-LD está sintaticamente correto (sem erros de vírgula, chaves, aspas).
- [x] O Schema Markup foi validado usando o Google Rich Results Test e não apresenta erros críticos.
- [x] O site está implementando Schema Markup para tipos de conteúdo que geram rich snippets valiosos para o negócio (e.g., Product, Review, Event, FAQPage).
- [x] O desempenho dos rich snippets está sendo monitorado no Google Search Console (seção "Aprimoramentos").
- [x] Imagens referenciadas no Schema (e.g., `image`, `logo`) têm as dimensões mínimas recomendadas pelo Google.
- [x] URLs dentro do Schema Markup são canônicas e acessíveis.

---

## Métricas de Referência

| Métrica | Benchmark (Média) | Meta (Otimizado) |
|:--------|:------------------|:-----------------|
| CTR (com rich snippets) | 5% - 8% | 10% - 15% |
| Impressões (com rich snippets) | > 20% das impressões totais | > 40% das impressões totais |
| Rich Results Coverage (Search Console) | > 80% das páginas elegíveis | > 95% das páginas elegíveis |
| Validação de Schema (erros) | 0.5% - 1% de erros | 0% de erros |
| Posição Média (rich snippets) | Posições 1-3 | Posições 1-2 |

---

## Erros Comuns

1.  **Dados Inconsistentes**: O Schema Markup apresenta informações diferentes do conteúdo visível na página.
    *   **Como evitar**: Sempre garanta que os dados no JSON-LD (preço, nome do produto, avaliação, etc.) correspondam exatamente ao que o usuário vê na página. Por exemplo, se o preço no Schema é R$100, mas na página é R$90, isso é um erro. Use dados dinâmicos do CMS/e-commerce para preencher o Schema.
2.  **Propriedades Obrigatórias Faltando**: Um tipo de Schema.org requer certas propriedades que não são preenchidas, resultando em rich snippets inválidos.
    *   **Como evitar**: Consulte a documentação oficial do Schema.org e do Google para cada `@type` que você planeja usar. O Google Rich Results Test indicará quais propriedades obrigatórias estão faltando. Por exemplo, `Product` sem `name` ou `offers` será inválido.
3.  **Sintaxe JSON-LD Incorreta**: Erros de vírgulas, aspas, chaves ou colchetes mal posicionados, tornando o JSON-LD ilegível para os motores de busca.
    *   **Como evitar**: Utilize um validador de JSON (como jsonlint.com) antes de inserir o código na página. Preste atenção especial ao final de cada objeto e lista, onde as vírgulas são necessárias, exceto no último item. Exemplo: `{"prop1": "valor1", "prop2": "valor2"}` é correto, `{"prop1": "valor1", "prop2": "valor2",}` é incorreto.

---

## Dicas Avançadas

1.  **Aninhamento de Schemas (Nested Schemas)**: Combine múltiplos tipos de Schema em um único bloco JSON-LD para descrever entidades complexas. Por exemplo, um `Article` pode ter um `VideoObject` e `ImageObject` aninhados, ou um `Product` pode aninhar `Review` e `AggregateRating`. Isso cria um grafo de conhecimento mais rico e preciso.
    *   **Exemplo**: Um `Article` sobre um produto pode incluir o `Product` schema dentro da propriedade `about` ou `mentions`, ligando o artigo diretamente ao produto.
2.  **Schema Dinâmico com Geradores no Lado do Servidor**: Para sites grandes ou com conteúdo em constante mudança (e-commerce, notícias), gere o JSON-LD programaticamente usando dados do banco de dados ou API. Isso garante que o Schema Markup esteja sempre atualizado e consistente.
    *   **Exemplo**: Em um sistema PHP, Python ou Node.js, crie funções que puxam o título, data, autor e imagens do CMS e as interpolam em um template JSON-LD antes de renderizar a página.
3.  **Utilize `sameAs` para Consistência de Entidades**: Use a propriedade `sameAs` para vincular entidades (Pessoas, Organizações) a suas representações em outras plataformas (Wikipedia, LinkedIn, redes sociais). Isso ajuda os motores de busca a consolidar o conhecimento sobre a entidade.
    *   **Exemplo**: No `author` do `Article` ou `publisher` do `Organization`, adicione `sameAs`: `["https://twitter.com/nomedousuario", "https://www.linkedin.com/in/nomedousuario"]`.
4.  **Marcação de Vídeos com `VideoObject`**: Para páginas que contêm vídeos, implemente `VideoObject` para aumentar as chances de aparecer em carrosséis de vídeo ou rich snippets de vídeo. Inclua `name`, `description`, `thumbnailUrl`, `uploadDate` e `contentUrl`.
    *   **Exemplo**: Uma página de receita pode ter um `Recipe` schema e, dentro dele, um `VideoObject` descrevendo o vídeo de preparo.
5.  **Teste Rigoroso em Ambiente de Desenvolvimento**: Antes de lançar o Schema Markup para produção, teste-o exaustivamente em um ambiente de staging. Use o Google Rich Results Test e o Schema Markup Validator para garantir que não haja erros e que os rich snippets esperados sejam detectados. Isso evita problemas de indexação e penalidades por marcação incorreta.