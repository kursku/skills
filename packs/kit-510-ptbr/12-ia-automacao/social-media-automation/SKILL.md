---
name: social-media-automation
description: "Social Media Automation — Skill especializada para social media automation"
license: MIT
metadata:
  version: 1.0.0
  author: Cafe Code AI
  category: 12-ia-automacao
  updated: 2026-03-01
risk: critical
---

# Social Media Automation

Esta skill capacita o Claude a projetar, implementar e otimizar estratégias de automação de mídias sociais utilizando ferramentas como Make, n8n, Zapier e APIs, focando em eficiência e escalabilidade na gestão de conteúdo e engajamento.

---

## Keywords

Automação de Conteúdo Social, Agendamento Inteligente de Posts, Monitoramento de Engajamento Automatizado, Geração de Leads via Social, Integração de CRM Social, Análise de Sentimento com IA, Webhooks para Redes Sociais, APIs de Mídias Sociais, Automação de Respostas Diretas, Publicação Cruzada Programada, RSS para Social Media, Campanhas Automatizadas de Engajamento.

---

## Quick Start

1.  **Configurar Conexões API:** Conecte as contas de Facebook Pages, Instagram Business, LinkedIn Pages e X (Twitter) APIs no seu hub de automação (Make.com, n8n ou Zapier). Assegure que as permissões de publicação e leitura de comentários estejam ativadas.
2.  **Webhook de Gatilho de Conteúdo:** Crie um webhook customizado para receber notificações de novos artigos do seu blog (via RSS, WordPress API ou CMS headless) ou atualizações de produtos (via Shopify/WooCommerce API) que servirão como base para novas postagens.
3.  **Geração de Legenda com IA:** Configure um módulo para chamar a Anthropic Claude API (ou outra LLM) para gerar 3-5 variações de legendas otimizadas para cada plataforma social, utilizando o título, URL e resumo do conteúdo recebido pelo webhook. Inclua hashtags relevantes e CTAs específicos.
4.  **Agendamento e Publicação Distribuída:** Implemente um módulo de roteamento e agendamento para distribuir as postagens geradas em diferentes plataformas. Utilize dados de horários de pico de engajamento (por exemplo, 9h, 13h, 17h para Instagram; 10h, 14h para LinkedIn) ou um algoritmo de rodízio para maximizar o alcance.
5.  **Monitoramento Básico de Menções:** Crie um fluxo secundário para monitorar menções diretas da sua marca em X (Twitter) ou comentários em postagens do Facebook/Instagram, encaminhando-os para um canal Slack ou e-mail específico para intervenção humana rápida.

---

## Core Workflows

### Workflow 1: Automação de Publicação de Conteúdo Multiplataforma via RSS e IA

Este workflow automatiza a criação e publicação de posts em diversas redes sociais a partir de novos artigos do seu blog, utilizando IA para gerar legendas otimizadas e agendamento inteligente.

**Passos Detalhados (Exemplo Make.com):**

1.  **Gatilho: Monitorar Feed RSS (Módulo RSS > Watch RSS Feed Items)**
    *   **URL do Feed:** `https://seublogdemarketing.com.br/feed`
    *   **Intervalo:** A cada 15 minutos.
    *   Este módulo detectará automaticamente novos artigos publicados no seu blog, extraindo o título, URL, resumo e, se disponível, a URL da imagem destacada.

2.  **Geração de Legendas com IA (Módulo HTTP > Make a request para Anthropic Claude API)**
    *   **Método:** `POST`
    *   **URL:** `https://api.anthropic.com/v1/messages`
    *   **Headers:**
        *   `x-api-key`: `YOUR_CLAUDE_API_KEY`
        *   `anthropic-version`: `2023-06-01`
        *   `content-type`: `application/json`
    *   **Corpo da Requisição (JSON):**
        ```json
        {
          "model": "claude-3-opus-20240229",
          "max_tokens": 1000,
          "messages": [
            {
              "role": "user",
              "content": "Gere 3 legendas distintas e engajadoras para um novo artigo de blog. O artigo é sobre 'As 5 Estratégias de SEO Local para Pequenas Empresas'. Inclua um emoji relevante, 3-5 hashtags específicas e um CTA claro para ler o artigo. Crie uma versão para X (Twitter) com no máximo 280 caracteres, uma para LinkedIn (profissional, até 600 caracteres) e uma para Instagram (com emojis e hashtags populares de SEO). \n\n**Título do Artigo:** {{1.title}}\n**URL do Artigo:** {{1.link}}\n**Resumo:** {{1.description}}"
            }
          ]
        }
        ```
    *   **Saída:** A IA retornará um JSON contendo as legendas geradas para cada plataforma.

3.  **Roteamento e Publicação no X (Twitter) (Módulo X > Create a Tweet)**
    *   **Mensagem:** Parseie a legenda gerada pela IA para X. Exemplo: `{{2.choices[0].message.content.twitter_caption}} {{1.link}}`
    *   **Imagem (Opcional):** `{{1.enclosures[].url}}` (se o RSS fornecer).
    *   **Agendamento:** Adicione um módulo de agendamento se desejar postar em horários específicos.

4.  **Roteamento e Publicação no LinkedIn (Módulo LinkedIn > Create a Share)**
    *   **Texto:** Parseie a legenda gerada pela IA para LinkedIn. Exemplo: `{{2.choices[0].message.content.linkedin_caption}}`
    *   **URL:** `{{1.link}}`
    *   **Visibilidade:** `Public`

5.  **Roteamento e Publicação no Instagram (Módulo Instagram for Business > Create Post)**
    *   **Imagem URL:** `{{1.enclosures[].url}}` (obrigatório para posts no Instagram).
    *   **Legenda:** Parseie a legenda gerada pela IA para Instagram. Exemplo: `{{2.choices[0].message.content.instagram_caption}}`

### Workflow 2: Automação de Atendimento e Engajamento em Comentários do Instagram/Facebook

Este workflow monitora comentários em suas postagens e responde automaticamente ou encaminha para o atendimento humano, baseando-se em análise de sentimento e palavras-chave, otimizando o tempo de resposta e a qualidade do engajamento.

**Passos Detalhados (Exemplo n8n):**

1.  **Gatilho: Novo Comentário no Instagram (Módulo Instagram Trigger > New Comment on Media)**
    *   **Tipo de Evento:** `New Comment`
    *   **Conta:** Selecione sua conta de Instagram Business.
    *   Este módulo será acionado sempre que um novo comentário for feito em qualquer uma das suas postagens.

2.  **Análise de Sentimento (Módulo HTTP Request > Google Cloud Natural Language API)**
    *   **Método:** `POST`
    *   **URL:** `https://language.googleapis.com/v1/documents:analyzeSentiment?key=YOUR_GOOGLE_CLOUD_API_KEY`
    *   **Corpo da Requisição (JSON):**
        ```json
        {
          "document": {
            "type": "PLAIN_TEXT",
            "content": "{{$json.text}}"
          },
          "encodingType": "UTF8"
        }
        ```
    *   **Saída:** O score de sentimento (e.g., -1.0 a 1.0) e magnitude.

3.  **Filtragem e Roteamento Condicional (Módulo IF)**
    *   **Condição 1 (Comentário Negativo ou Pergunta Complexa):**
        *   `{{$json.sentiment.score}}` `<` `-0.2` (sentimento negativo)
        *   OU `{{$json.text}}` `contains` `preço` OU `suporte` OU `problema` (palavras-chave de problema)
        *   **Ação:** Enviar para Slack/CRM.

    *   **Condição 2 (Comentário Positivo):**
        *   `{{$json.sentiment.score}}` `>` `0.2` (sentimento positivo)
        *   **Ação:** Gerar resposta com IA.

    *   **Condição 3 (Outros/Neutros):**
        *   **Ação:** Opcional: Arquivar, ou encaminhar para revisão.

4.  **Ação para Comentário Negativo/Pergunta (Módulo Slack > Send Message / Zendesk > Create Ticket)**
    *   **Slack:**
        *   **Canal:** `#atendimento-social`
        *   **Mensagem:** `Novo comentário crítico no Instagram de {{ $json.username }}: "{{ $json.text }}". Link da postagem: {{ $json.permalink }}`
    *   **Zendesk:**
        *   **Assunto:** `Comentário Instagram: {{ $json.text.substring(0, 50) }}`
        *   **Descrição:** `Usuário: {{ $json.username }}\nComentário: "{{ $json.text }}"\nLink: {{ $json.permalink }}`

5.  **Ação para Comentário Positivo: Gerar Resposta com IA (Módulo HTTP Request para Anthropic Claude API)**
    *   **Método/URL/Headers:** Conforme Workflow 1.
    *   **Corpo da Requisição (JSON):**
        ```json
        {
          "model": "claude-3-sonnet-20240229",
          "max_tokens": 200,
          "messages": [
            {
              "role": "user",
              "content": "Um usuário fez um comentário positivo: 'Adorei esse post! Muito útil para o meu negócio.' no Instagram. Gere uma resposta curta e amigável agradecendo e incentivando a interação futura, talvez com uma pergunta. Não exceda 150 caracteres. O comentário foi: \"{{$json.text}}\""
            }
          ]
        }
        ```
    *   **Saída:** A resposta gerada pela IA.

6.  **Ação para Comentário Positivo: Publicar Resposta (Módulo Instagram > Reply Comment)**
    *   **Media ID:** `{{$json.media_id}}`
    *   **Comment ID:** `{{$json.id}}`
    *   **Mensagem:** `{{$json.response_from_claude}}` (parsear a saída do passo 5).

---

## Templates

### Prompt para Geração de Legenda Otimizada para SEO e Engajamento

```
Você é um especialista em marketing de conteúdo para mídias sociais. Sua tarefa é criar legendas atraentes e otimizadas para o artigo de blog fornecido. O objetivo é maximizar o engajamento e o tráfego para o site.

**Artigo:**
Título: {{TITULO_DO_ARTIGO}}
URL: {{URL_DO_ARTIGO}}
Tópicos Chave: {{LISTA_DE_TOPICOS_CHAVE_DO_ARTIGO}}
Resumo: {{RESUMO_DO_ARTIGO}}

**Instruções:**
1.  Gere 3 legendas distintas e criativas para cada uma das seguintes plataformas: X (Twitter), LinkedIn, Instagram.
2.  Para X (Twitter): Máximo de 280 caracteres, inclua 2-3 hashtags relevantes e um emoji. Otimize para cliques.
3.  Para LinkedIn: Tom profissional, até 600 caracteres, inclua 3-5 hashtags relevantes, um parágrafo inicial que gere curiosidade e um CTA claro para "Leia o artigo completo".
4.  Para Instagram: Até 2.200 caracteres (mas mantenha a primeira linha impactante), inclua 5-10 hashtags populares e nichadas, 2-3 emojis, e um CTA para "Link na Bio" ou "Confira nos Stories".
5.  Em todas as legendas, adicione um senso de urgência ou benefício claro para o leitor.
6.  Assegure que as legendas reflitam o conteúdo do artigo e sejam gramaticalmente corretas.

**Formato de Saída (JSON):**
```json
{
  "twitter_caption": "...",
  "linkedin_caption": "...",
  "instagram_caption": "..."
}
```

**Exemplo Preenchido para o Título "Desvendando o Algoritmo do Instagram 2024":**

```
Você é um especialista em marketing de conteúdo para mídias sociais. Sua tarefa é criar legendas atraentes e otimizadas para o artigo de blog fornecido. O objetivo é maximizar o engajamento e o tráfego para o site.

**Artigo:**
Título: Desvendando o Algoritmo do Instagram 2024: Estratégias Essenciais para Crescer
URL: https://seublog.com/algoritmo-instagram-2024
Tópicos Chave: Algoritmo Instagram, Engajamento, Reels, Stories, SEO Instagram, Crescimento Orgânico
Resumo: O Instagram está sempre mudando. Este guia detalhado explora as atualizações mais recentes do algoritmo em 2024 e oferece estratégias práticas para marcas e criadores aumentarem seu alcance e engajamento.

**Instruções:**
1.  Gere 3 legendas distintas e criativas para cada uma das seguintes plataformas: X (Twitter), LinkedIn, Instagram.
2.  Para X (Twitter): Máximo de 280 caracteres, inclua 2-3 hashtags relevantes e um emoji. Otimize para cliques.
3.  Para LinkedIn: Tom profissional, até 600 caracteres, inclua 3-5 hashtags relevantes, um parágrafo inicial que gere curiosidade e um CTA claro para "Leia o artigo completo".
4.  Para Instagram: Até 2.200 caracteres (mas mantenha a primeira linha impactante), inclua 5-10 hashtags populares e nichadas, 2-3 emojis, e um CTA para "Link na Bio" ou "Confira nos Stories".
5.  Em todas as legendas, adicione um senso de urgência ou benefício claro para o leitor.
6.  Assegure que as legendas reflitam o conteúdo do artigo e sejam gramaticalmente corretas.

**Formato de Saída (JSON):**
```json
{
  "twitter_caption": "🤯 O algoritmo do Instagram mudou de novo em 2024! Não fique para trás. Descubra as estratégias ESSENCIAIS para crescer seu perfil agora. Clique e domine o jogo! #InstagramTips #AlgoritmoInstagram",
  "linkedin_caption": "O cenário digital está em constante evolução, e o Instagram não é exceção. Em 2024, entender as nuances do algoritmo da plataforma é mais crucial do que nunca para profissionais de marketing e negócios que buscam expandir seu alcance e engajamento. Nosso novo artigo detalha as atualizações recentes e oferece um guia prático com estratégias comprovadas para otimizar sua presença. Aprenda a alavancar Reels, Stories e SEO para Instagram. Não perca a oportunidade de posicionar sua marca à frente da concorrência. Leia o artigo completo e transforme sua estratégia de crescimento: [URL_DO_ARTIGO] #MarketingDigital #InstagramBusiness #Algoritmo2024 #EstrategiaDeMidiasSociais",
  "instagram_caption": "ALGORITMO DO INSTAGRAM 2024: Você está preparado? 🤔\n\nAs regras do jogo mudaram, e quem não se adapta, fica para trás! 🚀 Nosso novo artigo mergulha fundo nas atualizações mais recentes do algoritmo do Instagram e te entrega um mapa completo para bombar seu perfil.\n\nDescubra:\n✨ Como os Reels e Stories estão dominando o feed.\n🔍 Dicas de SEO para ser encontrado facilmente.\n📈 Estratégias de engajamento que realmente funcionam.\n\nChega de postar no escuro! Garanta que seu conteúdo seja visto pelas pessoas certas. ✨\n\n👉 LINK NA BIO para o guia completo! Não perca tempo, comece a crescer HOJE! #InstagramAlgoritmo #CrescerNoInstagram #DicasDeMarketing #SocialMediaBrasil #ReelsStrategy #EngajamentoInstagram #SEOInstagram #MarketingDigital"
}
```

### Configuração de Webhook para Notificação de Novo Comentário

```json
{
  "object": "page",
  "entry": [
    {
      "id": "123456789012345",
      "time": 1678886400,
      "changes": [
        {
          "field": "feed",
          "value": {
            "item": "comment",
            "verb": "add",
            "comment_id": "987654321098765",
            "parent_id": "112233445566778",
            "post_id": "112233445566778",
            "sender_id": "234567890123456",
            "created_time": 1678886390,
            "message": "Adorei essa dica! Muito útil para o meu negócio.",
            "from": {
              "id": "234567890123456",
              "name": "Maria Silva"
            },
            "permalink_url": "https://www.facebook.com/123456789012345/posts/112233445566778/?comment_id=987654321098765"
          }
        }
      ]
    }
  ]
}
```

---

## Checklist

- [x] Credenciais de API para Facebook Pages, Instagram Business, LinkedIn e X (Twitter) configuradas e testadas.
- [x] Webhooks de entrada (RSS, CMS, e-commerce) funcionando e enviando dados estruturados.
- [x] Modelos de prompt para IA (Claude API) específicos para cada plataforma social e tipo de conteúdo.
- [x] Regras de análise de sentimento e palavras-chave para roteamento de engajamento definidas e ajustadas.
- [x] Horários de pico de engajamento para cada rede social identificados e configurados nos módulos de agendamento.
- [x] Fluxos de fallback para atendimento humano ou notificação de erro configurados para cenários de falha.
- [x] Monitoramento de desempenho (cliques, engajamento, conversões) integrado com ferramentas de analytics (e.g., Google Analytics, CRM).
- [x] Estratégia de moderação de conteúdo automatizada (ex: remoção de spam, filtragem de palavras-chave negativas) implementada.
- [x] Testes A/B para diferentes legendas, CTAs e horários de postagem automatizados planejados e em execução.
- [x] Segmentação de público para campanhas sociais automatizadas configurada com base em dados de CRM ou tags.
- [x] Automação para respostas a DMs/mensagens diretas com IA ou templates pré-definidos.
- [x] Relatórios semanais/mensais de desempenho das automações sociais configurados e enviados por e-mail/Slack.

---

## Métricas de Referência

| Métrica                 | Benchmark (Médio da Indústria) | Meta (Otimizado com Automação) |
|-------------------------|--------------------------------|--------------------------------|
| **Taxa de Engajamento (ER)** | 1.5% - 3%                      | 4% - 6%                        |
| **Cliques no Link (CTR)**   | 0.5% - 1.5%                    | 2% - 3%                        |
| **Custo Por Clique (CPC)**  | R$ 0.80 - R$ 2.50              | R$ 0.50 - R$ 1.20              |
| **Alcance Orgânico**      | 10% - 20% da base de seguidores | 25% - 40% da base de seguidores |
| **Tempo Médio de Resposta (TMR)** | 2-4 horas                      | 5-30 minutos                   |
| **Taxa de Conversão Social** | 0.8% - 1.5%                    | 1.8% - 3%                      |

---

## Erros Comuns

1.  **Publicação Duplicada ou Inconsistente:** Ocorre quando a lógica de deduplicação em fluxos de publicação via RSS/CMS falha ou quando há um erro no agendamento, resultando em múltiplas postagens do mesmo conteúdo.
    *   **Como evitar:** Implementar um módulo de "Data Store" ou "Cache" que armazene os IDs dos conteúdos já publicados e verifique antes de cada nova publicação. Exemplo: Antes de postar no Twitter, o fluxo verifica se o `article_id` já existe na tabela de "posts_publicados".
2.  **Respostas Automatizadas Genéricas/Irrelevantes:** Prompts de IA mal elaborados ou regras de filtragem de comentários muito amplas levam a respostas que não agregam valor ou até prejudicam a percepção da marca.
    *   **Como evitar:** Refinar continuamente os prompts da IA, adicionando exemplos de respostas desejadas e indesejadas. Utilizar um nó de "Review" humano para monitorar as primeiras 100 respostas geradas automaticamente e ajustar o prompt. Exemplo: Para um comentário como "Onde acho mais informações?", a resposta "Acesse nosso site!" é genérica. O ideal é "Para mais detalhes sobre o produto X, você pode visitar nossa página de FAQs em [link] ou falar com nosso suporte via DM!".
3.  **Ignorar Limites de API:** Exceder as quotas de requisições por segundo/minuto/hora das APIs de mídias sociais ou da própria IA, resultando em falhas de automação e bloqueios temporários.
    *   **Como evitar:** Implementar "delays" ou "rate limiters" (disponíveis em Make/n8n) entre as chamadas de API, especialmente em fluxos de grande volume. Consultar a documentação da API para os limites específicos e configurar os módulos de acordo. Exemplo: Se a API do X permite 300 requisições em 3 horas, distribua suas postagens para não exceder esse limite em curtos períodos.

---

## Dicas Avançadas

1.  **IA Generativa para Criativos Visuais Dinâmicos:** Não se limite a legendas. Utilize APIs de IA generativa de imagens (e.g., DALL-E 3, Midjourney API, Stable Diffusion) para criar imagens personalizadas para cada postagem, baseadas no conteúdo do artigo ou nas palavras-chave do produto. Isso aumenta significativamente o engajamento visual.
    *   **Exemplo:** Um fluxo que, ao receber um novo artigo de "Dicas de jardinagem", gera uma imagem única de um jardim vibrante com base nos tópicos do texto.
2.  **Monitoramento de Concorrentes e Tendências com Automação:** Crie automações para monitorar feeds RSS de blogs de concorrentes, menções de palavras-chave da indústria (via Social Listening APIs) e tendências emergentes (Google Trends API). Use esses dados para alimentar a IA na geração de novos tópicos de conteúdo ou ajustar sua estratégia em tempo real.
    *   **Exemplo:** Um fluxo que detecta um pico de menções sobre "sustentabilidade em embalagens" e sugere à equipe de conteúdo a criação de um artigo ou postagem sobre o tema.
3.  **Personalização Hiper-Segmentada com Dados de CRM:** Integre suas automações sociais com seu CRM (e.g., HubSpot, Salesforce). Use dados do cliente (histórico de compras, interesses, estágio no funil de vendas) para personalizar respostas a comentários, mensagens diretas e até mesmo o conteúdo de anúncios automatizados.
    *   **Exemplo:** Se um cliente que comprou o "Produto A" comenta, a IA pode responder com "Que bom que você gostou! Temos também o acessório Y que complementa perfeitamente o Produto A. Gostaria de saber mais?".
4.  **Automação de Testes A/B Contínuos:** Configure fluxos que alternam automaticamente entre diferentes versões de legendas, CTAs, imagens ou horários de postagem para o mesmo conteúdo. Monitore as métricas de engajamento e cliques para identificar a versão de melhor desempenho e otimizar futuras automações.
    *   **Exemplo:** Publicar a legenda A em uma postagem e a legenda B em outra, monitorando o CTR e engajamento para determinar qual padrão usar nos próximos 10 posts.
5.  **Integração com Business Intelligence (BI) e Dashboards:** Conecte os dados de desempenho das suas automações sociais (engajamento, cliques, leads gerados) a ferramentas de BI como Power BI ou Tableau. Isso permite a criação de dashboards em tempo real para visualizar o impacto das suas automações e tomar decisões estratégicas baseadas em dados consolidados.
    *   **Exemplo:** Um dashboard que exibe o número de leads qualificados gerados por cada campanha automatizada no LinkedIn nos últimos 30 dias, segmentado por tipo de conteúdo.