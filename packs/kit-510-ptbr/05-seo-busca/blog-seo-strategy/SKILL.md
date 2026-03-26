---
name: blog-seo-strategy
description: "Blog Seo Strategy — Skill especializada para blog seo strategy"
license: MIT
metadata:
  version: 1.0.0
  author: Cafe Code AI
  category: 05-seo-busca
  updated: 2026-03-01
risk: safe
---

# Blog Seo Strategy

Esta skill capacita o Claude a criar e otimizar estratégias de SEO para blogs, desde a pesquisa de palavras-chave até a construção de links e otimização técnica.

---

## Keywords

- Estratégia de SEO para blog
- Pesquisa de palavras-chave para conteúdo
- Otimização on-page blog WordPress
- Conteúdo otimizado para blog
- Link building para artigos de blog
- SEO técnico para blogs
- Schema markup para posts
- Análise de SERP para blog
- Otimização de velocidade blog
- Marketing de conteúdo SEO
- Ferramentas de SEO para blog
- Conteúdo pilar e cluster topics

---

## Quick Start

1.  Mapear 5 palavras-chave de cauda longa para um novo post sobre "Receitas Veganas para Iniciantes" usando ferramentas como Ahrefs ou SEMrush.
2.  Estruturar o outline do artigo com H1, H2s e H3s, incluindo pelo menos 3 perguntas frequentes (FAQs) identificadas na SERP para o tópico.
3.  Configurar o plugin Yoast SEO ou Rank Math no WordPress para o post, preenchendo o título SEO, meta descrição e slug com a palavra-chave principal e variações.
4.  Gerar e otimizar 2-3 imagens para o post (redimensionar para <150KB, adicionar alt text descritivo, lazy load).
5.  Publicar o artigo e solicitar a indexação manual via Google Search Console para agilizar o rastreamento.

---

## Core Workflows

### Workflow 1: Otimização de Conteúdo para Rankear na Posição Zero (Featured Snippet)

**Objetivo**: Conquistar a posição zero (Featured Snippet) para um termo de busca informacional, aumentando a visibilidade e o CTR.

**Passo 1: Identificação de Oportunidades de Featured Snippet.**
-   **Ferramenta**: SEMrush Keyword Magic Tool ou Ahrefs Keywords Explorer.
-   **Ação**: Filtrar palavras-chave com "SERP Features" indicando Featured Snippet (Parágrafo, Lista, Tabela). Priorizar termos com perguntas diretas ("o que é...", "como fazer...", "qual o melhor...") ou listas implícitas.
-   **Exemplo Concreto**: Pesquisar por "como fazer café expresso em casa". Observar se há um Featured Snippet existente e qual seu formato.

**Passo 2: Análise da SERP e Conteúdo do Snippet Atual.**
-   **Ação**: Realizar a busca no Google para o termo identificado. Analisar o conteúdo do Featured Snippet existente: tipo (parágrafo, lista, tabela), concisão, fonte, e quais informações ele apresenta ou omite.
-   **Exemplo Concreto**: Para "melhores ferramentas de SEO", o snippet atual pode ser uma lista. Para "o que é SEO técnico", um parágrafo de 50 palavras.

**Passo 3: Estruturação do Conteúdo para Snippet.**
-   **Ação**: Criar um bloco de texto conciso (40-60 palavras para parágrafo) ou uma lista/tabela clara e direta, respondendo à pergunta de forma superior e mais completa que o snippet atual. Posicionar este bloco logo após o H1 ou no início da seção relevante do artigo.
-   **Exemplo Concreto (Parágrafo)**: Para a busca "qual a melhor ração para gatos filhotes", incluir um parágrafo como: "A melhor ração para gatos filhotes deve ser formulada especificamente para essa fase de crescimento, rica em proteínas de alta qualidade, vitaminas e minerais essenciais para o desenvolvimento saudável. Marcas como Royal Canin Kitten e Hills Science Diet Kitten são frequentemente recomendadas por veterinários devido ao seu balanço nutricional e digestibilidade."
-   **Exemplo Concreto (Lista)**: Para "passos para instalar WordPress", criar uma lista ordenada no HTML:
    ```html
    <ol>
        <li>Escolha um provedor de hospedagem web (ex: Hostinger, Bluehost).</li>
        <li>Registre um nome de domínio (ex: Registro.br, GoDaddy).</li>
        <li>Baixe o pacote WordPress do site oficial.</li>
        <li>Crie um banco de dados MySQL no painel de controle da sua hospedagem.</li>
        <li>Faça o upload dos arquivos do WordPress via FTP para o diretório raiz do seu domínio.</li>
        <li>Acesse seu domínio no navegador e siga as instruções do instalador do WordPress.</li>
    </ol>
    ```

**Passo 4: Otimização Técnica e Semântica.**
-   **Ação**: Assegurar que o conteúdo do snippet esteja em um elemento HTML semanticamente correto (`<p>`, `<ul>`, `<ol>` ou `<table>`). Utilizar a palavra-chave principal e variações semânticas ao longo do texto para reforçar a relevância.
-   **Ferramenta**: Google Natural Language API (para análise de entidades e relevância) ou manualmente, pensando em sinônimos e termos relacionados.
-   **Exemplo Concreto**: Para "receitas veganas", usar "pratos à base de plantas", "culinária sem carne", "dieta vegetal", "alimentos 100% vegetais" para enriquecer o vocabulário semântico.

**Passo 5: Monitoramento e Ajustes.**
-   **Ferramenta**: Google Search Console (Relatório de Performance, Posições), Rank Tracker (para monitorar featured snippets e posições).
-   **Ação**: Após a publicação, monitorar o desempenho do artigo. Se não conquistar o snippet, analisar a concorrência que o detém, ajustar a fraseologia, concisão ou estrutura do bloco de conteúdo. Pequenas alterações podem fazer a diferença.

### Workflow 2: Construção de Links (Link Building) para Artigos de Blog com Técnica de Guest Post

**Objetivo**: Adquirir backlinks de alta qualidade de sites relevantes para aumentar a autoridade de domínio (DA/DR) e a relevância de um artigo específico do blog.

**Passo 1: Identificação de Conteúdo Pilar para Link Building.**
-   **Ação**: Selecionar um artigo do blog com conteúdo aprofundado, original e com potencial para atrair links, geralmente um "guia completo", "estudo de caso", ou "pesquisa original". Este será o artigo que receberá o backlink.
-   **Exemplo Concreto**: O artigo "Guia Completo de Otimização de Imagens para SEO: Aumente o Tráfego e a Velocidade" é um bom candidato.

**Passo 2: Pesquisa de Prospects para Guest Post.**
-   **Ferramenta**: Ahrefs Content Explorer, SEMrush Topic Research, Google avançado (`intitle:"escrever para nós" marketing digital`, `intitle:"guest post" tecnologia`, `[nicho] "contribua"`).
-   **Ação**: Encontrar blogs e sites relevantes no mesmo nicho ou nichos adjacentes que aceitem guest posts ou que tenham um perfil de links interessante. Filtrar por Domain Rating (DR) alto (DR > 40) e forte relevância temática.
-   **Exemplo Concreto**: Procurar blogs de "Marketing Digital", "Performance Web", "E-commerce" que aceitem contribuições. Um blog como "Rock Content Blog" (DR 80+) ou "Viver de Blog" (DR 70+) seriam excelentes prospects.

**Passo 3: Análise de Relevância e Autoridade dos Prospects.**
-   **Ferramenta**: Ahrefs Site Explorer, Moz Link Explorer ou SEMrush Domain Overview.
-   **Ação**: Verificar o perfil de backlinks do prospect (número de domínios de referência, qualidade dos links), o tráfego orgânico estimado, a qualidade geral do conteúdo e a presença de links para concorrentes. Priorizar sites com bom tráfego orgânico e links de alta qualidade.
-   **Exemplo Concreto**: Um blog sobre "Otimização de Sites" com DR 68, tráfego mensal de 90k e boa diversidade de domínios de referência é um prospect ideal.

**Passo 4: Criação da Proposta de Guest Post.**
-   **Ação**: Desenvolver 3-5 ideias de tópicos para guest posts que sejam altamente relevantes para o público do prospect e que permitam, de forma natural e contextual, um link para o seu artigo pilar.
-   **Template de Email**: Utilizar o "Template de Email de Proposta de Guest Post" da seção `## Templates`.
-   **Exemplo Concreto**: Se o artigo pilar é "Guia Completo de Otimização de Imagens para SEO", ideias para guest post podem ser: "5 Ferramentas Essenciais para Otimização de Imagens para Web", "Como a Compressão de Imagens Impacta Diretamente o Core Web Vitals do seu Site", "Checklist para Imagens de Produtos em E-commerce: Maximizando Conversões".

**Passo 5: Redação do Guest Post e Inserção do Backlink.**
-   **Ação**: Escrever um artigo de alta qualidade (1000-1500 palavras), original e útil para o público do prospect. Inserir o backlink para o seu artigo pilar de forma natural e contextual, usando um anchor text relevante e descritivo.
-   **Exemplo Concreto**: Em um guest post sobre "Velocidade de Carregamento de Sites", o link para "Guia Completo de Otimização de Imagens para SEO" pode ser: "Para um aprofundamento sobre como otimizar suas imagens sem perder qualidade e melhorar significativamente o desempenho do seu site, consulte nosso [Guia Completo de Otimização de Imagens para SEO](https://www.seublog.com.br/otimizacao-imagens-seo)."

**Passo 6: Acompanhamento e Monitoramento.**
-   **Ferramenta**: Google Search Console (Relatório de Links Externos), Ahrefs (Backlinks), SEMrush Link Building Tool.
-   **Ação**: Após a publicação, monitorar o link para garantir que ele esteja ativo e siga as diretrizes (dofollow). Avaliar o impacto no rankeamento e no tráfego orgânico do artigo pilar e na autoridade de domínio geral do seu blog.

---

## Templates

### Template: Email de Proposta de Guest Post

```
Assunto: Ideia de Conteúdo para o Blog [Nome do Blog Prospect] - [Sua Ideia de Tópico 1]

Olá [Nome do Editor/Dono do Blog],

Meu nome é [Seu Nome] e sou [Sua Posição, ex: Especialista em SEO de Conteúdo] no [Nome do Seu Blog/Empresa], onde publicamos artigos aprofundados sobre [Nicho do Seu Blog, ex: marketing digital e otimização web].

Sou um grande fã do conteúdo de vocês, especialmente do artigo "[Nome de um Artigo Específico do Blog Prospect, ex: 'Guia Completo de SEO Local para Pequenas Empresas']". A qualidade e profundidade de seus posts são sempre impressionantes e muito úteis para a comunidade.

Percebi que vocês abordam frequentemente temas como [Tema Relacionado ao Seu Conteúdo/Nicho, ex: performance de sites e estratégias de conteúdo] e pensei que meu conhecimento poderia agregar ainda mais valor aos seus leitores. Gostaria de propor algumas ideias de artigos que acredito que seriam muito interessantes para o público do [Nome do Blog Prospect]:

1.  **[Sua Ideia de Tópico 1, ex: Como a Otimização de Imagens Impacta Diretamente seus Core Web Vitals]**: Um guia prático sobre como otimizar imagens para melhorar a velocidade de carregamento e experiência do usuário.
2.  **[Sua Ideia de Tópico 2, ex: Estratégias de Conteúdo para Conquistar a Posição Zero no Google]**: Explorando técnicas