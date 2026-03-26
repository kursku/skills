---
name: answer-engine-optimization
description: "Answer Engine Optimization — Skill especializada para answer engine optimization"
license: MIT
metadata:
  version: 1.0.0
  author: Cafe Code AI
  category: 05-seo-busca
  updated: 2026-03-01
risk: safe
---

# Answer Engine Optimization

Esta skill capacita o Claude a otimizar conteúdo para ser a resposta direta e autoritativa em motores de busca e assistentes de voz, focando na intenção de resposta e dados estruturados.

---

## Keywords

Answer Engine Optimization, featured snippets, People Also Ask, schema markup, dados estruturados, intenção de resposta, busca conversacional, otimização de FAQ, busca por voz, SERP features, zero-click searches, entity SEO, rich results.

---

## Quick Start

1.  **Analise SERPs para "Respostas Diretas":** Pesquise 5 termos-chave de alto valor no Google para identificar oportunidades de Featured Snippets (parágrafo, lista, tabela), PAA (Pessoas Também Perguntam) e caixas de respostas diretas. Ex: "como fazer café expresso".
2.  **Implemente Schema `FAQPage`:** Escolha uma página de produto ou serviço com perguntas frequentes e adicione o `FAQPage` Schema Markup em JSON-LD, testando imediatamente com o Google Rich Results Test para validação.
3.  **Reformule Conteúdo para Intenção de Resposta:** Identifique parágrafos existentes que podem servir como respostas diretas (concisas, 40-60 palavras) e mova-os para logo abaixo de um subtítulo H2 ou H3 que corresponda à pergunta específica.
4.  **Otimize para "Pessoas Também Perguntam":** Use ferramentas como AlsoAsked.com para encontrar perguntas relacionadas ao seu tópico principal e incorpore-as naturalmente em novos subtítulos (H3, H4) ou parágrafos concisos dentro do seu conteúdo.
5.  **Monitore Posições de Snippets:** Configure um rastreador de posições (como Ahrefs ou SEMrush) para monitorar o ganho ou perda de Featured Snippets e a posição para seus termos-chave otimizados, avaliando o impacto da AEO.

---

## Core Workflows

### Workflow 1: Otimização de Conteúdo para Featured Snippets e PAA

Este workflow foca em adaptar o conteúdo textual para ser facilmente extraído pelo Google como Featured Snippets (parágrafo, lista, tabela) e para responder a perguntas em "Pessoas Também Perguntam" (PAA).

*   **Passo 1: Identificação de Oportunidades de Snippets Existentes e Potenciais.**
    *   **Ferramentas:** Ahrefs, SEMrush, Google Search Console, Google SERP.
    *   **Ação:** Utilize Ahrefs ou SEMrush para encontrar palavras-chave com featured snippets que sua empresa já possui (para otimização e proteção) ou que seus concorrentes dominam. No Ahrefs, vá para "Organic Keywords", filtre por "SERP features" e selecione "Featured snippet". Para novas oportunidades, procure por termos-chave com alta intenção de pergunta ("o que é", "como fazer", "melhor para", "passo a passo") que ainda não exibem um snippet ou exibem um de baixa qualidade.
    *   **Exemplo:** Uma loja de eletrônicos identifica que seu principal concorrente possui um featured snippet para "como escolher um fone de ouvido gamer", enquanto sua página similar está na posição 4, mas sem snippet. Esta é uma oportunidade clara.
*   **Passo 2: Análise da Estrutura e Formato do Snippet Dominante.**
    *   **Ação:** Realize uma busca exata no Google para o termo-chave identificado. Observe o formato do snippet dominante (parágrafo, lista numerada, lista com marcadores, tabela), a extensão do texto (geralmente 40-60 palavras para parágrafos, 4-8 itens para listas) e a fonte que o Google está priorizando.
    *   **Exemplo:** Para "como escolher um fone de ouvido gamer", o snippet dominante é um parágrafo conciso que enumera 3 a 4 critérios essenciais, como "qualidade de áudio, conforto e microfone".
*   **Passo 3: Reestruturação e Otimização do Conteúdo para a Resposta Direta.**
    *   **Ação:** Edite o conteúdo da sua página. Crie um parágrafo de resposta conciso (40-60 palavras), direto e informativo, localizado logo abaixo de um subtítulo H2 ou H3 que corresponda exatamente à pergunta. Use linguagem clara, sem jargões e foque na resposta principal. Para listas ou tabelas, formate o conteúdo de forma que seja fácil de extrair.
    *   **Exemplo:** No artigo "Guia Completo: Como Escolher seu Fone de Ouvido Gamer", adicione um H2 "## Como Escolher um Fone de Ouvido Gamer Ideal?" e, imediatamente abaixo, o parágrafo otimizado: "Para escolher um fone de ouvido gamer ideal, foque em três pilares: qualidade de áudio (drivers de 50mm são ótimos), conforto para longas sessões (almofadas de espuma viscoelástica) e um microfone de comunicação clara (com cancelamento de ruído). A conectividade (USB ou 3.5mm) e a compatibilidade com sua plataforma também são cruciais para a experiência de jogo."
*   **Passo 4: Otimização para "Pessoas Também Perguntam" (PAA).**
    *   **Ferramentas:** AlsoAsked.com, Google SERP.
    *   **Ação:** Expanda as perguntas do PAA em novos subtítulos H3 ou H4 dentro do conteúdo. Para cada nova pergunta, forneça uma resposta direta e concisa (2-3 frases) que agregue valor ao tópico principal. Isso aumenta a cobertura semântica e a chance de capturar mais rich results.
    *   **Exemplo:** Para o mesmo tema de fones gamer, o PAA inclui "Qual a diferença entre fone gamer e fone comum?" e "Qual a melhor marca de fone gamer?". Crie seções "### Qual a diferença entre fone gamer e fone comum?" e "### Qual a melhor marca de fone gamer?" com respostas diretas e relevantes.

### Workflow 2: Implementação e Monitoramento de Schema Markup para AEO

Este workflow orienta na aplicação de dados estruturados para melhorar a visibilidade em rich results e featured snippets, fornecendo contexto explícito aos motores de busca.

*   **Passo 1: Seleção de Páginas e Tipos de Schema Relevantes.**
    *   **Ação:** Identifique páginas do seu site com alto potencial para rich results: páginas de FAQ, artigos de "como fazer", produtos com avaliações, eventos, receitas, artigos de blog. Escolha o tipo de Schema.org mais adequado para cada página (e.g., `FAQPage`, `HowTo`, `Product`, `Event`, `Recipe`, `Article`). Priorize páginas com alto tráfego ou alto potencial de conversão.
    *   **Exemplo:** Para uma página de suporte de um SaaS com 15 perguntas e respostas sobre o produto, a seção de FAQs é perfeita para `FAQPage` Schema. Para um blog post "Como Instalar um Plugin WordPress", o `HowTo` Schema é ideal, detalhando os passos.
*   **Passo 2: Geração do Código Schema Markup em JSON-LD.**
    *   **Ferramentas:** Geradores de Schema online (e.g., TechnicalSEO.com Schema Markup Generator, Schema.dev), ou codificação manual em JSON-LD.
    *   **Ação:** Preencha os campos obrigatórios do Schema com dados extraídos diretamente do conteúdo visível da página. Para `FAQPage`, cada `Question` e `Answer` deve ter um par correspondente no HTML da página. Para `HowTo`, cada `step` deve refletir um passo real no conteúdo.
    *   **Exemplo para `FAQPage`:**
        ```json
        {
          "@context": "https://schema.org",
          "@type": "FAQPage",
          "mainEntity": [{
            "@type": "Question",
            "name": "Qual é a política de devolução da Loja de Moda X?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "Nossa política de devolução permite que você solicite a troca ou reembolso em até 7 dias corridos após o recebimento do produto, desde que esteja em sua embalagem original, com etiquetas e sem sinais de uso. Entre em contato com nosso suporte para iniciar o processo."
            }
          },{
            "@type": "Question",
            "name": "Como faço para rastrear meu pedido da Loja de Moda X?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "Após a confirmação do envio, você receberá um e-mail com o código de rastreamento. Acesse a área 'Meus Pedidos' em nosso site e insira o código para acompanhar a entrega em tempo real."
            }
          }]
        }
        ```
*   **Passo 3: Implementação do Schema no HTML da Página.**
    *   **Ação:** Cole o JSON-LD gerado dentro da tag `<head>` ou `<body>` da sua página. Se estiver usando um CMS como WordPress, utilize plugins de SEO (Rank Math, Yoast SEO Premium) que oferecem geradores integrados e campos específicos para adicionar Schema sem modificar o código diretamente.
    *   **Exemplo:** No WordPress, em um post, vá para as configurações do Rank Math, selecione o tipo de Schema "FAQ" e preencha as perguntas e respostas. O plugin inserirá o JSON-LD automaticamente.
*   **Passo 4: Validação e Teste do Schema Markup.**
    *   **Ferramentas:** Google Rich Results Test (ferramenta principal), Google Schema Markup Validator.
    *   **Ação:** Submeta a URL da página para o Google Rich Results Test. Verifique se há erros ou avisos e se os rich results esperados (e.g., FAQ, HowTo) são detectados e exibidos corretamente na pré-visualização. Corrija quaisquer problemas identificados antes de prosseguir.
    *   **Exemplo:** Ao testar a URL `https://www.loja-moda-x.com.br/central-de-ajuda`, o Rich Results Test deve mostrar "Resultados ricos detectados: Perguntas Frequentes" e uma pré-visualização de como apareceria na SERP.
*   **Passo 5: Monitoramento de Performance e Rich Results no Google Search Console.**
    *   **Ação:** Após a implementação e a reindexação pelo Google (pode levar alguns dias), monitore a seção "Melhorias" (ou "Aprimoramentos") no Google Search Console (GSC). Verifique os relatórios específicos para o tipo de Schema implementado (e.g., "Perguntas Frequentes", "Como fazer", "Produto") para acompanhar o status de indexação, erros e a performance (impressões, cliques) dos seus rich results.
    *   **Exemplo:** No GSC, observe se o número de itens válidos para "Perguntas Frequentes" aumenta e se há um incremento nas impressões e cliques para as páginas com esse tipo de rich result.

---

## Templates

### Template de Conteúdo para Featured Snippet (Parágrafo)

```
### O que é [Termo-Chave Principal]?

[Termo-Chave Principal] é [definição concisa e direta, com 40-60 palavras, sem introdução ou conclusão. Foque em responder a pergunta de forma clara e autoritativa. Utilize linguagem simples e evite jargões desnecessários. Inclua o termo-chave e sinônimos relevantes. Idealmente, comece com a resposta principal e depois adicione um ou dois detalhes complementares para contextualizar.]

Exemplo:

### O que é Marketing de Conteúdo?

Marketing de Conteúdo é uma estratégia focada na criação e distribuição de conteúdo valioso, relevante e consistente para atrair e reter um público-alvo claramente definido. Seu objetivo é engajar clientes, construir autoridade da marca e, por fim, impulsionar ações lucrativas, como vendas e cadastros, sem uma abordagem de venda direta, mas sim educando e informando.
```

### Template de Schema `HowTo` (Exemplo para "Como Trocar a Bateria do seu Notebook")

```json
{
  "@context": "https://schema.org",
  "@type": "HowTo",
  "name": "Como Trocar a Bateria do seu Notebook Dell Inspiron 15",
  "description": "Um guia passo a passo detalhado sobre como substituir a bateria interna de um notebook Dell Inspiron 15 com segurança e eficiência, economizando custos de manutenção.",
  "image": {
    "@type": "ImageObject",
    "url": "https://www.assistenciatecnica.com.br/imagens/trocar-bateria-dell-inspiron.jpg",
    "width": "1200",
    "height": "800"
  },
  "totalTime": "PT20M",
  "estimatedCost": {
    "@type": "MonetaryAmount",
    "currency": "BRL",
    "value": "350.00"
  },
  "supply": [{
    "@type": "HowToSupply",
    "name": "Nova bateria compatível para Dell Inspiron 15"
  },{
    "@type": "HowToSupply",
    "name": "Kit de chaves de precisão (Phillips e Torx)"
  },{
    "@type": "HowToSupply",
    "name": "Espátula plástica (ferramenta de alavanca)"
  },{
    "@type": "HowToSupply",
    "name": "Pulso antiestático (recomendado)"
  }],
  "tool": [{
    "@type": "HowToTool",
    "name": "Chave Phillips"