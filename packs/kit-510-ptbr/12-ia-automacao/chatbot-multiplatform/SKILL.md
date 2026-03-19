---
name: chatbot-multiplatform
description: "Chatbot Multiplatform — Skill especializada para chatbot multiplatform"
license: MIT
metadata:
  version: 1.0.0
  author: Cafe Code AI
  category: 12-ia-automacao
  updated: 2026-03-01
---

# Chatbot Multiplatform

Esta skill capacita o Claude a projetar, implementar e otimizar chatbots multiplatforma, integrando-os com ferramentas de automação e APIs para experiências de conversação robustas e escaláveis.

---

## Keywords

Chatbot Multiplatform, Integração WhatsApp API, Facebook Messenger Bot, Telegram Bot, Make.com Automação, N8N Workflows, Zapier Chatbot, Webhook API, Dialogflow CX, Google Gemini API, OpenAI GPT-4, Custom Intents, Fallback Strategies, Live Chat Handoff, NLP Tuning, Prompt Engineering Chatbot.

---

## Quick Start

1.  **Configurar Webhook Inicial:** Crie um endpoint `POST` no Make.com ou N8N, por exemplo, `https://hook.us1.make.com/abcdefgh`, para receber mensagens do WhatsApp Business API.
2.  **Mapear Entidades de Mensagem:** Utilize módulos "Parse JSON" ou "Set Multiple Variables" para extrair `message.from` (ID do usuário), `message.text.body` (conteúdo da mensagem) e `message.id` (ID da mensagem) do payload JSON recebido.
3.  **Primeira Resposta Dinâmica com LLM:** Conecte um módulo "Router" para direcionar a mensagem a um módulo "ChatGPT" ou "Google Gemini" com um prompt inicial como: "Você é um assistente de vendas da Loja X. Responda à pergunta do cliente: {{2.text.body}}".
4.  **Enviar Resposta para Plataforma:** Envie a resposta gerada pelo LLM de volta para o WhatsApp utilizando o módulo "WhatsApp Business Cloud API" com `to: {{2.from}}` e `text.body: {{3.choices[0].message.content}}`.

---

## Core Workflows

### Workflow 1: Integração WhatsApp com LLM e CRM (Vendas e Suporte)

Este workflow detalha a criação de um chatbot de vendas e suporte via WhatsApp, integrado com um LLM para respostas inteligentes e um CRM para registro de interações e transbordo.

*   **Trigger (Make.com/N8N):** Webhook do WhatsApp Business API.
    *   **Exemplo Payload (recebido no webhook):**
        ```json
        {
          "object": "whatsapp_business_account",
          "entry": [
            {
              "id": "<WAB_ID>",
              "changes": [
                {
                  "value": {
                    "messaging_product": "whatsapp",
                    "metadata": {
                      "display_phone_number": "5511987654321",
                      "phone_number_id": "<PHONE_ID>"
                    },
                    "contacts": [
                      {
                        "profile": { "name": "João Silva" },
                        "wa_id": "5511999998888"
                      }
                    ],
                    "messages": [
                      {
                        "from": "5511999998888",
                        "id": "wamid.XXXXXXXXXXXXX",
                        "timestamp": "1678886400",
                        "text": { "body": "Olá, gostaria de saber sobre o preço do produto X." },
                        "type": "text"
                      }
                    ]
                  },
                  "field": "messages"
                }
              ]
            }
          ]
        }
        ```
*   **Passo 1: Extrair Dados da Mensagem:** Módulo "Set Multiple Variables" ou "Parse JSON".
    *   `whatsappUser = {{webhook.body.entry[0].changes[0].value.messages[0].from}}`
    *   `userMessage = {{webhook.body.entry[0].changes[0].value.messages[0].text.body}}`
    *   `userName = {{webhook.body.entry[0].changes[0].value.contacts[0].profile.name}}`
    *   `messageId = {{webhook.body.entry[0].changes[0].value.messages[0].id}}`
*   **Passo 2: Contextualizar e Gerar Resposta com LLM:** Módulo "ChatGPT" (ou Gemini).
    *   **Model:** `gpt-4o`
    *   **System Prompt:** `Você é o assistente de vendas e suporte virtual da TechStore Brasil. Seu objetivo é qualificar leads, responder perguntas sobre produtos (SKUs: TS001, TS002, TS003) e agendar demonstrações ou direcionar para o suporte técnico. Mantenha um tom amigável, profissional e prestativo. Se o cliente solicitar explicitamente falar com um humano, inicie o processo de transbordo. O cliente atual se chama {{userName}}.`
    *   **User Message:** `{{userMessage}}`
    *   **Tools (Opcional - para buscar dados externos):**
        ```json
        [
          {
            "type": "function",
            "function": {
              "name": "get_product_info",
              "description": "Obtém informações como preço e estoque de um produto pelo SKU.",
              "parameters": {
                "type": "object",
                "properties": {
                  "sku": { "type": "string", "description": "O SKU do produto." }
                },
                "required": ["sku"]
              }
            }
          }
        ]
        ```
*   **Passo 3: Lógica de Transbordo (Handoff) ou Armazenamento no CRM:** Módulo "Router" ou "Filter".
    *   **Condição 1 (Transferência para Humano):** Se `{{ChatGPT.choices[0].message.content}}` contiver `[TRANSFERIR_HUMANO]` (tag definida no prompt do LLM) ou se `userMessage` contiver "falar com atendente", "humano", "suporte urgente".
        *   Módulo "HTTP Request" para enviar notificação para canal Slack/Teams.
            *   URL: `https://hooks.slack.com/services/YOUR/SLACK/WEBHOOK_PLACEHOLDER`
            *   Headers: `Content-Type: application/json`
            *   Body: `{"text": "🚨 Novo pedido de atendimento humano! Cliente: {{userName}} ({{whatsappUser}}). Mensagem: '{{userMessage}}'. Link para conversar: [https://seudash.com/chat/{{whatsappUser}}]"} `
        *   Módulo "WhatsApp Business Cloud API" para responder: "Entendido, {{userName}}! Já alertei nossa equipe de especialistas, e um deles entrará em contato com você em breve. Por favor, aguarde alguns minutos."
    *   **Condição 2 (Resposta Padrão e Registro no CRM):** Se não for transferência.
        *   Módulo "HTTP Request" (POST) para registrar a conversa no CRM (ex: HubSpot, Pipedrive).
            *   URL: `https://api.hubapi.com/crm/v3/objects/notes`
            *   Headers: `Authorization: Bearer YOUR_HUBSPOT_API_KEY`, `Content-Type: application/json`
            *   Body:
                ```json
                {
                  "properties": {
                    "hs_note_body": "Conversa WhatsApp com {{userName}} ({{whatsappUser}}):\nCliente: {{userMessage}}\nBot: {{ChatGPT.choices[0].message.content}}",
                    "hs_timestamp": "{{now()}}",
                    "hs_created_by_user_id": "chatbot_id"
                  }
                }
                ```
        *   Módulo "WhatsApp Business Cloud API" para enviar a resposta `{{ChatGPT.choices[0].message.content}}` de volta para `{{whatsappUser}}`.

### Workflow 2: Gerenciamento de Conteúdo e Publicação Multi-Canal (Telegram e Facebook Messenger)

Este workflow automatiza a geração de ideias e a publicação de conteúdo em diferentes plataformas sociais, utilizando um chatbot como interface de comando.

*   **Trigger 1 (Make.com/N8N):** Webhook de nova mensagem em grupo do Telegram.
    *   **Exemplo Payload:**
        ```json
        {
          "update_id": 123456789,
          "message": {
            "message_id": 123,
            "from": { "id": 987654321, "is_bot": false, "first_name": "Ana" },
            "chat": { "id": -100111222333, "title": "Grupo Marketing Tech", "type": "supergroup" },
            "date": 1678886400,
            "text": "/gerarideia para novo post sobre automação de marketing"
          }
        }
        ```
*   **Passo 1: Filtrar Comandos do Telegram:** Módulo "Router" ou "Filter".
    *   **Filtro:** `{{telegram.message.text}}` começa com `/gerarideia`
*   **Passo 2: Gerar Ideias de Post com LLM:** Módulo "ChatGPT" (ou Gemini).
    *   **Model:** `gpt-3.5-turbo` (para economia em tarefas mais simples).
    *   **System Prompt:** `Você é um especialista em marketing digital focado em tecnologia e IA. Sua tarefa é gerar 3 ideias criativas para posts em redes sociais, incluindo título, breve descrição e 2-3 hashtags relevantes para cada ideia. Mantenha um tom engajador e atualizado.`
    *   **User Message:** `Gere ideias para posts sobre: {{replace(telegram.message.text, "/gerarideia ", "")}}`
*   **Passo 3: Publicar Ideias no Grupo Telegram:** Módulo "Telegram Bot".
    *   **Chat ID:** `{{telegram.message.chat.id}}`
    *   **Text:** `*Novas Ideias de Post para o Grupo Marketing Tech:*\n\n{{ChatGPT.choices[0].message.content}}` (Usar formatação Markdown)

*   **Trigger 2 (Make.com/N8N):** Webhook de nova mensagem privada para página do Facebook Messenger.
    *   **Exemplo de uso:** Um usuário envia uma mensagem para a página com o texto do post e anexa uma imagem.
*   **Passo 1.1: Extrair Conteúdo e Anexos:** Módulo "Parse JSON" ou "Set Multiple Variables".
    *   `facebookMessage = {{webhook.body.entry[0].messaging[0].message.text}}`
    *   `facebookAttachmentURL = {{webhook.body.entry[0].messaging[0].message.attachments[0].payload.url}}` (se houver anexo)
*   **Passo 1.2: Fazer Upload da Imagem (se houver):** Módulo "Cloudinary" ou "Google Drive: Upload a file from URL".
    *   **File URL:** `{{facebookAttachmentURL}}`
    *   **Resultado:** `cloudinaryPublicURL = {{cloudinary.url}}`
*   **Passo 1.3: Publicar Post no Facebook Page:** Módulo "Facebook Pages".
    *   **Page ID:** `{{PAGE_ID_DA_EMPRESA}}` (Obtido das configurações da sua página no Facebook Developers)
    *   **Message:** `{{facebookMessage}}`
    *   **Photo URL:** `{{cloudinaryPublicURL}}` (se `facebookAttachmentURL` existir, caso contrário deixar vazio ou omitir)
*   **Passo 1.4: Confirmar Publicação ao Usuário:** Módulo "Facebook Messenger".
    *   **Recipient ID:** `{{webhook.body.entry[0].messaging[0].sender.id}}`
    *   **Message Text:** "Seu post foi publicado com sucesso na página do Facebook! Confira em [https://facebook.com/SuaPaginaEmpresa]"

---

## Templates

### Prompt para Geração de Resposta de Vendas (LLM)

```
Você é um assistente de vendas da "Tech Solutions Brasil", especializado em produtos de TI e serviços de consultoria. Seu objetivo é ajudar clientes a encontrar a solução ideal, responder a dúvidas técnicas e de preços, e direcionar para um especialista humano quando necessário. Mantenha um tom profissional, amigável e objetivo.

**Contexto do Cliente:**
Nome: Mariana
Interesse inicial: Software de gestão de projetos.
Histórico: Visitou nossa página do produto 'ProjManager' há 2 horas. Ela já perguntou sobre integração com Slack.
Histórico de Conversa:
- Cliente: "Olá, gostaria de saber mais sobre o ProjManager. Ele se integra com o Slack?"
- Bot: "Olá Mariana! Sim, o ProjManager possui integração nativa com o Slack. Ele também se integra com Jira e Google Drive, facilitando a gestão de equipes e projetos. Posso te ajudar com mais alguma dúvida?"

**Informações de Produtos/Serviços (apenas para referência, não cite diretamente):**
- ProjManager: Software SaaS, R$199/mês (plano básico), R$499/mês (plano premium), integração Slack/Jira/Google Drive.
- Consultoria Agile: A partir de R$500/hora.
- Suporte Técnico: Disponível de segunda a sexta, das 9h às 18h.

**Mensagem do Cliente:**
"Ah, que ótimo! E qual a diferença entre o plano básico e o premium do ProjManager?"

**Sua Resposta (seja conciso e útil):**
```

### Payload Webhook para Envio de Mensagem Interativa com Botões (WhatsApp)

```json
{
  "messaging_product": "whatsapp",
  "recipient_type": "individual",
  "to": "5511987654321",
  "type": "interactive",
  "interactive": {
    "type": "button",
    "header": {
      "type": "text",
      "text": "Bem-vindo(a) à Tech Solutions!"
    },
    "body": {
      "text": "Olá João! Para qual de nossos serviços você gostaria de mais informações hoje?"
    },
    "footer": {
      "text": "Escolha uma opção abaixo:"
    },
    "action": {
      "buttons": [
        {
          "type": "reply",
          "reply": {
            "id": "SERVICE_PROJMANAGER_INFO",
            "title": "ProjManager SaaS"
          }
        },
        {
          "type": "reply",
          "reply": {
            "id": "SERVICE_CONSULTORIA_INFO",
            "title": "Consultoria TI"
          }
        },
        {
          "type": "reply",
            "reply": {
            "id": "SERVICE_FALAR_HUMANO",
            "title": "Falar com Atendente"
          }
        }
      ]
    }
  }
}
```

---

## Checklist

- [x] Mapeamento completo de canais de comunicação (WhatsApp Business API, Messenger, Telegram, Webchat).
- [x] Configuração de webhooks em ferramenta de automação (Make/N8N) para cada canal.
- [x] Estrutura de prompt engineering para LLM com persona, contexto e histórico de conversa definidos.
- [x] Lógica de identificação de intenções (intents) do usuário implementada (LLM ou NLU dedicado como Dialogflow).
- [x] Estratégia de fallback para intenções não reconhecidas, erros do LLM ou mensagens inesperadas.
- [x] Mecanismo de transbordo (handoff) para atendimento humano integrado com sistema de tickets ou chat ao vivo.
- [x] Integração com APIs externas (CRM, ERP, Base de Conhecimento, Agendamento) para dados dinâmicos.
- [x] Monitoramento de logs, erros e métricas de desempenho do chatbot em tempo real.
- [x] Plano de testes abrangente para diferentes cenários de conversa, intenções e plataformas.
- [x] Definição e implementação de regras para tratamento de dados sensíveis e conformidade com LGPD.

---

## Métricas de Referência

| Métrica                         | Benchmark | Meta   |
|---------------------------------|-----------|--------|
| Taxa de Resolução na 1ª Interação | 60%       | 80%    |
| Taxa de Transbordo para Humano   | 30%       | 15%    |
| Tempo Médio de Resposta do Bot  | < 3s      | < 1s   |
| Taxa de Satisfação do Usuário (CSAT) | 3.5/5     | 4.2/5  |
| % de Redução de Custo de Atendimento | 20%       | 40%    |
| Taxa de Erro do LLM (Resposta Inadequada) | 10%       | 3%     |

---

## Erros Comuns

1.  **Prompts Genéricos e Ausência de Contexto**: O LLM gera respostas vagas, redundantes ou fora do escopo, frustrando o usuário.
    *   **Como evitar**: Incluir persona específica (ex: "Você é um especialista em suporte técnico de roteadores Cisco"), histórico da conversa (`chat_history`), e informações relevantes do usuário (nome, ID do cliente) no prompt. Ex: `System: Você é o suporte da XYZ. Histórico: "{{hist.msg}}". Cliente: "{{user.name}}". Pergunta: "{{user.msg}}"`.
2.  **Webhooks Mal Configurados ou Sem Tratamento de Erros**: Mensagens não chegam, são processadas incorretamente, ou o bot para de responder sem aviso.
    *   **Como evitar**: Validar payloads JSON no Make/N8N com módulos "Parse JSON" e usar ferramentas de debug para inspecionar dados. Implementar retries automáticos e configurar notificações de erro (ex: e-mail, Slack) para falhas de API ou workflow. Ex: Em N8N, use o "Error Workflow" para enviar um alerta ao Slack.
3.  **Falta de Estratégia de Transbordo (Handoff)**: Usuários frustrados sem uma opção clara e eficiente de falar com um atendente humano quando o bot
