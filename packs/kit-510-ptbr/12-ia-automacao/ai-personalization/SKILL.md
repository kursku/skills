---
name: ai-personalization
description: "Ai Personalization — Skill especializada para ai personalization"
license: MIT
metadata:
  version: 1.0.0
  author: Cafe Code AI
  category: 12-ia-automacao
  updated: 2026-03-01
---

# Ai Personalization

Esta skill capacita o Claude a criar e implementar estratégias de personalização de IA para interações de usuários em chatbots e automações, utilizando APIs e fluxos de dados em plataformas como Make, N8N e Zapier.

---

## Keywords

`Personalização Dinâmica`, `Segmentação Comportamental`, `Conteúdo Adaptativo`, `Engajamento Contextual`, `Perfil do Usuário`, `Webhook Personalizado`, `API de Personalização`, `Automação N8N`, `Prompts Condicionais`, `Machine Learning (MLOps)`, `Next-Best-Action`, `Retenção de Cliente`.

---

## Quick Start

1.  **Configurar Coleta de Dados de Eventos**: Implemente um webhook no seu site ou aplicativo para capturar eventos de comportamento do usuário (ex: `produto_visualizado`, `item_adicionado_carrinho`).
2.  **Atualizar Perfil do Usuário em DB/CRM**: Configure um módulo em N8N/Make/Zapier para receber o webhook e atualizar os atributos do perfil do usuário (ex: `preferencia_categoria`, `historico_compras`) em um banco de dados ou CRM.
3.  **Criar Prompt Condicional com Atributos**: Desenvolva um prompt para o Claude que utilize variáveis do perfil do usuário para gerar respostas ou recomendações contextualizadas.
4.  **Integrar Automação com Claude**: No N8N/Make, configure um módulo para chamar a API do Claude, passando os atributos do usuário como parte do prompt, e utilize a resposta para enviar uma mensagem personalizada (ex: e-mail, SMS, mensagem de chatbot).

---

## Core Workflows

### Workflow 1: Personalização de Respostas em Chatbot Baseada em Histórico de Navegação

Este workflow detalha como usar o histórico de navegação de um usuário para personalizar as interações de um chatbot, oferecendo conteúdo ou produtos altamente relevantes.

**Passos detalhados:**

1.  **Captura de Eventos de Navegação**:
    *   **Ferramenta**: JavaScript no frontend do site + Webhook.
    *   **Exemplo de JavaScript**:
        ```javascript
        document.addEventListener('DOMContentLoaded', function() {
            // Monitora visualização de produto
            const productPage = document.querySelector('.product-detail-page');
            if (productPage) {
                const productId = productPage.dataset.productId;
                const productCategory = productPage.dataset.productCategory;
                const userId = getUserIdFromCookie(); // Função para obter ID do usuário
                if (userId && productId) {
                    sendWebhookEvent('product_viewed', {
                        user_id: userId,
                        product_id: productId,
                        category: productCategory,
                        timestamp: new Date().toISOString()
                    });
                }
            }
        });

        function sendWebhookEvent(eventType, payload) {
            fetch('https://your-n8n-webhook-url.com/webhook/product-events', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ event_type: eventType, data: payload })
            }).then(response => console.log('Evento enviado:', response.status));
        }
        ```
2.  **Processamento do Evento e Atualização do Perfil do Usuário**:
    *   **Ferramenta**: N8N (ou Make/Zapier).
    *   **Configuração N8N**:
        *   **Módulo 1: Webhook Trigger**: Configurado para receber `POST` na URL `https://your-n8n-webhook-url.com/webhook/product-events`.
        *   **Módulo 2: Code (JavaScript)**: Para extrair `user_id`, `category` e atualizar uma preferência no perfil.
            ```javascript
            const event = $json.data;
            const userId = event.user_id;
            const category = event.category;

            // Lógica para acumular preferências ou registrar a última categoria visitada
            // Exemplo: Atualizar um campo 'last_viewed_category' e 'category_interest_score'
            return {
                json: {
                    user_id: userId,
                    last_viewed_category: category,
                    timestamp: event.timestamp
                }
            };
            ```
        *   **Módulo 3: Database/CRM Node**: Conecte a um banco de dados (ex: PostgreSQL, MongoDB) ou CRM (ex: HubSpot, Salesforce) para atualizar o perfil do usuário com `last_viewed_category` e `timestamp`.
            *   **Exemplo de SQL para atualização**:
                ```sql
                UPDATE users
                SET last_viewed_category = '{{ $json.last_viewed_category }}',
                    updated_at = '{{ $json.timestamp }}'
                WHERE user_id = '{{ $json.user_id }}';
                ```
3.  **Geração de Resposta Personalizada pelo Claude**:
    *   **Ferramenta**: API do Claude + N8N.
    *   **Configuração N8N**:
        *   **Módulo 1: Chatbot Trigger**: Quando um usuário inicia uma conversa.
        *   **Módulo 2: Database/CRM Node**: Consulta o perfil do usuário para obter `last_viewed_category` e `historico_compras`.
        *   **Módulo 3: Claude API Node**: Envia um prompt dinâmico.
            *   **Prompt de Exemplo (passado no corpo da requisição da API)**:
                ```
                Você é um assistente de vendas online. Um cliente, {{$node["Database/CRM"].json["user_name"]}}, acabou de visitar a categoria de {{$node["Database/CRM"].json["last_viewed_category"]}}. Ele já comprou {{$node["Database/CRM"].json["historico_compras"]}}. Sugira 2-3 produtos ou artigos dessa categoria que sejam altamente relevantes para ele, considerando o histórico de compras. Mencione um benefício específico para ele.
                ```
        *   **Módulo 4: Chatbot Response**: Envia a resposta gerada pelo Claude de volta ao usuário.

### Workflow 2: Segmentação Dinâmica de Campanhas via Automação Make para Reengajamento

Este workflow automatiza a segmentação de usuários com base em seu engajamento com e-mails e aciona campanhas de reengajamento personalizadas.

**Passos detalhados:**

1.  **Monitoramento de Engajamento de E-mail**:
    *   **Ferramenta**: Make (formerly Integromat) + Serviço de E-mail Marketing (ex: Mailchimp, ActiveCampaign).
    *   **Configuração Make**:
        *   **Módulo 1: Webhook Custom**: Configurado para receber eventos de `email_opened` ou `link_clicked` do seu provedor de e-mail marketing.
        *   **Exemplo de Payload de Webhook (ActiveCampaign)**:
            ```json
            {
              "type": "contact_link_clicked",
              "date_time": "2023-10-27 15:00:00",
              "contact": { "id": "123", "email": "usuario@email.com" },
              "link": { "id": "456", "url": "https://suaempresa.com/ofertas/viagens" }
            }
            ```
2.  **Atualização de Atributos de Segmentação**:
    *   **Ferramenta**: Make + CRM/Planilha.
    *   **Configuração Make**:
        *   **Módulo 2: Filter**: Para verificar se o evento é `link_clicked` e a URL contém `/ofertas/viagens`.
        *   **Módulo 3: Google Sheets (ou CRM)**: Adicionar ou atualizar uma tag `interessado_viagem` para o `contact.email` na planilha de segmentos.
            *   **Exemplo de Adicionar Linha/Atualizar Célula**:
                *   `Planilha ID`: `[ID da sua planilha de segmentos]`
                *   `Ação`: `Atualizar uma célula`
                *   `Linha ID`: Pesquisar pelo e-mail do contato
                *   `Coluna`: `Segmentos`
                *   `Valor`: `interessado_viagem`
3.  **Disparo de Campanha Personalizada**:
    *   **Ferramenta**: Make + Claude API + Serviço de E-mail Marketing/SMS.
    *   **Configuração Make**:
        *   **Módulo 4: Filter**: Verificar se o usuário foi marcado como `interessado_viagem`.
        *   **Módulo 5: Claude API**: Gerar um conteúdo de e-mail ou SMS específico.
            *   **Prompt de Exemplo**:
                ```
                Você é um especialista em marketing de viagens. Escreva um parágrafo curto (máximo 500 caracteres) para um e-mail de reengajamento para um cliente que demonstrou interesse em "ofertas de viagens". O cliente é {{$node["Google Sheets"].json["contact_name"]}}. Sugira um destino popular para viagens de aventura e um para relaxamento, com um call-to-action para visitar a página de pacotes.
                ```
        *   **Módulo 6: SendGrid (ou outro serviço de e-mail)**: Enviar o e-mail com o conteúdo gerado pelo Claude.
            *   **Corpo do E-mail**: `{{$node["Claude API"].json.completion}}`
            *   **Assunto**: `Descubra sua próxima aventura, {{$node["Google Sheets"].json["contact_name"]}}!`

---

## Templates

### Prompt para Recomendação de Conteúdo Personalizado

```
Você é um curador de conteúdo especializado em tecnologia. Um usuário, {nome_usuario}, tem um perfil que indica forte interesse em {categoria_principal_interesse} e {categoria_secundaria_interesse}. O histórico recente mostra que ele visualizou artigos sobre {topico_recente_visualizado}. Recomende 3 artigos ou vídeos recentes que se alinhem perfeitamente com esses interesses e com o tópico recente. Inclua um breve resumo de cada recomendação e o link (placeholder).

Exemplo de uso:
Input: {nome_usuario: "Ana Clara", categoria_principal_interesse: "Inteligência Artificial", categoria_secundaria_interesse: "Desenvolvimento Web", topico_recente_visualizado: "Novas APIs para LLMs"}

Output:
Olá, Ana Clara! Que bom te ver por aqui. Com base no seu interesse em Inteligência Artificial e Desenvolvimento Web, e na sua recente pesquisa sobre APIs para LLMs, preparei estas recomendações:

1.  **Artigo: "Construindo Aplicações Web com a API do Claude 3 Opus"**
    *   Resumo: Explore um guia prático sobre como integrar o Claude 3 Opus em suas aplicações web, focando em casos de uso de personalização e automação.
    *   Link: [https://blog.tech.com/claude3-opus-web-apps]
2.  **Vídeo: "Machine Learning Ops para Modelos de Linguagem em Produção"**
    *   Resumo: Entenda os desafios e melhores práticas para gerenciar e escalar LLMs em ambientes de produção, essencial para desenvolvedores.
    *   Link: [https://youtube.com/mlops-llms]
3.  **Artigo: "Personalização Contextual com Embeddings: Além do Básico"**
    *   Resumo: Mergulhe em técnicas avançadas de personalização usando embeddings para criar experiências de usuário ultra-relevantes.
    *   Link: [https://blog.tech.com/embeddings-personalization]
```

### Webhook para Captura de Intenção de Compra

```json
POST /api/purchase_intent_events HTTP/1.1
Content-Type: application/json

{
  "user_id": "usr_98765",
  "email": "joao.silva@example.com",
  "event_type": "item_added_to_cart",
  "product_id": "prod_54321",
  "product_name": "Fone de Ouvido Bluetooth Premium",
  "product_category": "Áudio e Fones",
  "price": 299.90,
  "quantity": 1,
  "timestamp": "2023-10-27T14:45:00Z",
  "session_id": "sess_fghijk",
  "referrer_url": "https://ecommerce.com/ofertas-do-dia"
}
```

---

## Checklist

-   [x] Identificar fontes de dados de comportamento do usuário (ex: cliques, visualizações, compras, interações de chatbot).
-   [x] Definir atributos de personalização (ex: `preferencia_categoria`, `nivel_engajamento`, `historico_compras`, `ultimo_produto_visualizado`).
-   [x] Mapear eventos de usuário para atualização de perfil em DB/CRM (ex: `product_viewed` -> `last_viewed_category`).
-   [x] Configurar webhooks para captura de eventos em tempo real, garantindo a baixa latência.
-   [x] Desenvolver prompts dinâmicos para o Claude que utilizem múltiplos atributos do perfil do usuário para contextualização.
-   [x] Implementar lógicas condicionais em automações (Make/N8N/Zapier) para ativar fluxos de personalização específicos (ex: se `cart_abandoned`, enviar lembrete).
-   [x] Monitorar métricas de performance das interações personalizadas (CTR, taxa de conversão, tempo de sessão, redução de churn).
-   [x] Estabelecer um ciclo de feedback contínuo para otimizar os modelos e prompts de personalização com base nos resultados.
-   [x] Garantir a conformidade com leis de privacidade de dados (LGPD/GDPR) na coleta, armazenamento e uso de informações personalizadas.
-   [x] Realizar testes A/B para comparar o desempenho de interações personalizadas versus não personalizadas ou com diferentes abordagens de personalização.

---

## Métricas de Referência

| Métrica                                | Benchmark   | Meta        |
|:---------------------------------------|:------------|:------------|
| Taxa de Cliques (CTR) em Mensagens Personalizadas | 15-25%      | >20%        |
| Taxa de Conversão de Vendas (Atribuída à Personalização) | 5-10%       | >8%         |
| Redução na Taxa de Churn por Usuário   | 10-20%      | <15%        |
| Aumento do Tempo Médio de Sessão (Site/App) | 15-25%      | >20%        |
| Taxa de Engajamento em Chatbot (Respostas Úteis) | 70-85%      | >80%        |
| Custo por Aquisição (CAC) de Cliente (Otimizado por Personalização) | R$ 50-100   | <R$ 70      |

---

## Erros Comuns

1.  **Super-personalização ou "Creepiness"**: Utilizar dados muito íntimos ou óbvios, fazendo o usuário sentir que está sendo excessivamente monitorado, sem um consentimento claro ou valor agregado percebido.
    *   **Como evitar**: Defina limites claros para a profundidade e o tipo de dados usados na personalização. Concentre-se em agregar valor real ao usuário. Ex: Em vez de dizer "Você viu o produto X às 14h32", diga "Percebemos seu interesse em produtos da categoria X, confira essas novidades!". Seja transparente sobre como os dados são usados para melhorar a experiência.
2.  **Dados de Perfil Desatualizados ou Inconsistentes**: Recomendações baseadas em informações antigas ou conflitantes levam a interações irrelevantes e frustrantes. Ex: Recomendar um produto que o usuário já comprou ou que não se encaixa mais no seu perfil.
    *   **Como evitar**: Implemente rotinas de atualização periódica e validação de dados em tempo real. Utilize timestamps para cada atributo e priorize dados mais recentes. Considere um "decay rate" para interesses antigos. Ex: Um clique em uma categoria há 6 meses tem menos peso que uma visualização de produto na última hora.
3.  **Falta de Testes A/B e Iteração**: Lançar estratégias de personalização sem testar diferentes abordagens ou sem um plano para otimização contínua, resultando em desempenho subótimo sem saber o porquê.
    *   **Como evitar**: Sempre projete seus fluxos de personalização com testes A/B em mente. Compare uma versão personalizada com uma genérica, ou duas versões com diferentes níveis/tipos de personalização. Monitore métricas chave e use esses insights para iterar e refinar seus prompts e lógicas de automação. Ex: Testar um prompt que foca em "benefício individual" versus um que foca em "popularidade do produto".

---

## Dicas Avançadas

1.  **Personalização Preditiva com MLOps**: Vá além da personalização reativa (baseada em histórico) e implemente modelos de Machine Learning para prever a "Next-Best-Action" (próxima melhor ação) ou o risco de churn. Integre esses modelos (via APIs) aos seus fluxos de automação para alimentar o Claude com insights preditivos. Ex: Usar um modelo de ML no Google Cloud AI Platform para prever qual categoria de produto um usuário tem maior probabilidade de comprar e passar essa previsão como um atributo `predicted_interest` para o Claude.
2.  **Personalização Multi-canal Sincronizada**: Garanta que a experiência personalizada seja consistente e coesa em todos os pontos de contato com o usuário (chatbot, e-mail, SMS, notificação push, site). Um usuário que interagiu com um produto no chatbot deve ver a mesma recomendação ou uma continuação dela no e-mail ou no site. Ex: Após um usuário abandonar um carrinho no site, um chatbot pode iniciar uma conversa mencionando os itens específicos do carrinho, e um e-mail subsequente pode oferecer um desconto nesses mesmos itens.
3.  **Feedback Loop Contínuo e Adaptativo**: Implemente mecanismos onde o sistema de personalização "aprende" com as respostas do usuário. Se uma recomendação é ignorada ou uma interação é negativa, o sistema deve ajustar o perfil do usuário ou a estratégia de personalização para futuras interações. Ex: Se o Claude recomenda 3 produtos de "esportes" e o usuário responde "não gosto de esportes", o atributo `preferencia_categoria` para "esportes" deve ser diminuído, e a IA deve tentar outras categorias.
4.  **Micro-segmentação em Tempo Real com Embeddings**: Em vez de depender apenas de categorias amplas, utilize embeddings (representações vetoriais) de itens, documentos ou interações de usuário para encontrar similaridades mais granulares. Isso permite a micro-segmentação dinâmica em tempo real. Ex: Gerar um embedding do texto de uma conversa de chatbot e compará-lo com embeddings de produtos para recomendar o item exato que corresponde à intenção expressa, mesmo que não esteja em uma categoria predefinida.
5.  **Personalização de Intenção Explícita e Implícita**: Combine a personalização baseada em dados comportamentais implícitos (navegação, cliques) com a intenção explícita do usuário (perguntas no chatbot, preferências declaradas). Priorize a intenção explícita quando disponível. Ex: Se o usuário diz "Quero comprar um laptop para trabalho", mesmo que seu histórico mostre interesse em jogos, a IA deve priorizar a recomendação de laptops para trabalho.