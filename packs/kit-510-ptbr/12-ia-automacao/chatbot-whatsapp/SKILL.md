---
name: chatbot-whatsapp
description: "Chatbot Whatsapp — Skill especializada para chatbot whatsapp"
license: MIT
metadata:
  version: 1.0.0
  author: Cafe Code AI
  category: 12-ia-automacao
  updated: 2026-03-01
---

# Chatbot Whatsapp

Esta skill capacita o Claude a projetar, implementar e otimizar chatbots para WhatsApp utilizando plataformas de automação no-code/low-code, APIs e IA, focando em conversão e suporte eficiente.

---

## Keywords

WhatsApp Business API, Make.com, N8N, Zapier, Webhook, Chatbot IA, Mensageria Ativa, Fluxo Conversacional, NLP, Dialogflow CX, OpenAI API, Meta Cloud API, Template Message, Automação.

---

## Quick Start

1.  **Acesso à WhatsApp Business API**: Obtenha acesso à WhatsApp Business API, seja via um provedor de soluções (BSP) ou diretamente através da Meta Cloud API para desenvolvedores.
2.  **Configuração de Webhook Inicial**: No Make.com ou N8N, crie um módulo de "Webhook" e copie a URL gerada. Configure esta URL no painel de desenvolvedor da Meta para receber mensagens de entrada.
3.  **Fluxo de Resposta Simples**: Crie um cenário/workflow que, ao receber uma mensagem (detectada pelo webhook), envie uma resposta de texto simples como "Olá! Como posso ajudar?".
4.  **Teste de Conectividade**: Envie uma mensagem de teste para o número do seu chatbot no WhatsApp para verificar se o webhook está recebendo e o chatbot respondendo corretamente.
5.  **Integração IA Básica**: Adicione um módulo de integração com OpenAI (Chat Completion) após o webhook para gerar respostas mais dinâmicas, usando a mensagem do usuário como prompt.

---

## Core Workflows

### Workflow 1: Implementação de Chatbot de Suporte ao Cliente com Make.com e OpenAI API

Este workflow descreve a criação de um chatbot de suporte inteligente para WhatsApp, capaz de responder a perguntas frequentes e escalar para atendimento humano quando necessário, utilizando Make.com para orquestração e OpenAI para inteligência conversacional.

**Passo 1: Configuração do Webhook de Entrada (Make.com)**

*   **Objetivo**: Receber mensagens do WhatsApp Business API.
*   **Ações**:
    1.  No Make.com, adicione um módulo "Webhooks" e selecione "Custom webhook".
    2.  Copie o "Webhook URL" gerado.
    3.  No painel de desenvolvedor da Meta (developers.facebook.com), vá para seu aplicativo > WhatsApp > Configuração da API.
    4.  Na seção "Webhooks", clique em "Editar".
    5.  Cole o "Webhook URL" no campo "URL de Retorno de Chamada".
    6.  No campo "Verificar Token", insira um token secreto (ex: `MEUSEGREDOWHATSPP`). Este token deve ser o mesmo configurado no módulo Webhook do Make.com.
    7.  Clique em "Gerenciar" na seção "Webhooks" e assine o campo `messages` para receber mensagens de texto.
*   **Exemplo de Payload de Entrada (JSON recebido pelo Webhook)**:

    ```json
    {
      "object": "whatsapp_business_account",
      "entry": [
        {
          "id": "123456789012345",
          "changes": [
            {
              "value": {
                "messaging_product": "whatsapp",
                "metadata": {
                  "display_phone_number": "5511987654321",
                  "phone_number_id": "123456789012345"
                },
                "contacts": [
                  {
                    "profile": { "name": "Cliente Teste" },
                    "wa_id": "5511998877665"
                  }
                ],
                "messages": [
                  {
                    "from": "5511998877665",
                    "id": "wamid.AB...",
                    "timestamp": "1678886400",
                    "text": { "body": "Preciso de ajuda com meu pedido #12345" },
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

**Passo 2: Processamento da Mensagem com IA (OpenAI API no Make.com)**

*   **Objetivo**: Gerar uma resposta inteligente com base na mensagem do usuário.
*   **Ações**:
    1.  Adicione um módulo "OpenAI" e selecione "Create a Chat Completion".
    2.  **Conexão**: Configure sua chave de API do OpenAI.
    3.  **Modelo**: Selecione `gpt-3.5-turbo` ou `gpt-4`.
    4.  **Mensagens**: Adicione dois itens na lista "Messages":
        *   **Role**: `system`, **Content**: `Você é um atendente virtual de suporte da [Nome da Empresa]. Responda de forma prestativa e objetiva. Se for sobre um pedido, sempre peça o número do pedido para verificação. Se não souber responder, sugira transferir para um atendente humano.`.
        *   **Role**: `user`, **Content**: `{{1.value.messages[].text.body}}` (mapeando a mensagem do usuário do webhook).
    5.  **Max Tokens**: Defina um valor apropriado (ex: `150`).
*   **Exemplo de Prompt para OpenAI**:

    ```
    Sistema: Você é um atendente virtual de suporte da Empresa X. Responda de forma prestativa e objetiva. Se for sobre um pedido, sempre peça o número do pedido para verificação. Se não souber responder, sugira transferir para um atendente humano.
    Usuário: Preciso de ajuda com meu pedido #12345
    ```

**Passo 3: Envio da Resposta para o WhatsApp (HTTP Request no Make.com)**

*   **Objetivo**: Enviar a resposta gerada pela IA de volta para o usuário no WhatsApp.
*   **Ações**:
    1.  Adicione um módulo "HTTP" e selecione "Make a request".
    2.  **Método**: `POST`.
    3.  **URL**: `https://graph.facebook.com/v18.0/{{metadata.phone_number_id}}/messages` (mapeie o `phone_number_id` do webhook de entrada).
    4.  **Headers**:
        *   `Authorization`: `Bearer SEU_ACCESS_TOKEN_DO_WHATSAPP` (obtenha um token de acesso permanente do Meta for Developers).
        *   `Content-Type`: `application/json`.
    5.  **Body (JSON)**:

        ```json
        {
          "messaging_product": "whatsapp",
          "to": "{{1.value.messages[].from}}",
          "type": "text",
          "text": {
            "body": "{{2.choices[].message.content}}"
          }
        }
        ```

        (mapeie o `from` do webhook e a resposta da OpenAI).

**Passo 4: Tratamento de Erros e Fallback (Make.com)**

*   **Objetivo**: Gerenciar falhas na automação e oferecer um caminho para atendimento humano.
*   **Ações**:
    1.  Adicione um "Error handler" ao seu cenário.
    2.  Configure o Error Handler para enviar uma notificação (ex: Slack, email) para a equipe interna em caso de qualquer falha nos módulos anteriores.
    3.  Dentro do Error Handler, adicione um módulo HTTP para enviar uma mensagem padrão ao usuário do WhatsApp informando sobre o erro e oferecendo suporte humano: `"Desculpe, tive um problema para processar sua solicitação. Por favor, aguarde enquanto um de nossos atendentes analisa seu caso."`

### Workflow 2: Automação de Mensageria Ativa com N8N e Planilha Google Sheets

Este workflow demonstra como enviar mensagens proativas (Template Messages) para clientes do WhatsApp, disparadas por eventos em uma planilha Google Sheets (ex: status de pedido alterado), utilizando N8N como orquestrador.

**Passo 1: Gatilho da Automação (N8N - Google Sheets)**

*   **Objetivo**: Detectar novas linhas ou alterações em uma planilha que indicam a necessidade de enviar uma mensagem.
*   **Ações**:
    1.  No N8N, adicione um módulo "Google Sheets" e selecione "Watch new rows" ou "Read a Spreadsheet" (com filtro).
    2.  **Credenciais**: Conecte sua conta Google Sheets.
    3.  **Spreadsheet**: Selecione a planilha onde os dados dos clientes e eventos são registrados (ex: "Pedidos_eCommerce").
    4.  **Sheet Name**: Especifique a aba (ex: "Pedidos Processados").
    5.  **Trigger on**: "New Row" (ou configure um filtro para `status: "Pagamento Confirmado"`).
*   **Exemplo de Dados de Entrada (Linha da Planilha)**:

    ```json
    {
      "nome_cliente": "Ana Silva",
      "telefone_cliente": "5511998877665",
      "numero_pedido": "P12345",
      "status_pedido": "Pagamento Confirmado",
      "data_evento": "2024-03-01T10:00:00Z"
    }
    ```

**Passo 2: Envio de Template Message Aprovada (N8N - HTTP Request)**

*   **Objetivo**: Enviar uma Template Message pré-aprovada pela Meta para o cliente, informando sobre o evento.
*   **Ações**:
    1.  Adicione um módulo "HTTP Request".
    2.  **Método**: `POST`.
    3.  **URL**: `https://graph.facebook.com/v18.0/{{$env.WHATSAPP_PHONE_ID}}/messages` (utilize uma variável de ambiente para o ID do telefone).
    4.  **Headers**:
        *   `Authorization`: `Bearer {{$env.WHATSAPP_ACCESS_TOKEN}}` (variável de ambiente para o token de acesso).
        *   `Content-Type`: `application/json`.
    5.  **Body (JSON)**: Este é um exemplo para um template chamado `confirmacao_pagamento`. Certifique-se de que o template esteja aprovado no Meta Business Manager.

        ```json
        {
          "messaging_product": "whatsapp",
          "to": "{{$json.telefone_cliente}}",
          "type": "template",
          "template": {
            "name": "confirmacao_pagamento",
            "language": { "code": "pt_BR" },
            "components": [
              {
                "type": "body",
                "parameters": [
                  { "type": "text", "text": "{{$json.nome_cliente}}" },
                  { "type": "text", "text": "{{$json.numero_pedido}}" },
                  { "type": "text", "text": "Pix" }
                ]
              },
              {
                "type": "button",
                "sub_type": "url",
                "index": 0,
                "parameters": [
                  { "type": "text", "text": "Ver Detalhes" }
                ]
              }
            ]
          }
        }
        ```

        *Mapeie `nome_cliente`, `numero_pedido`, `telefone_cliente` e outros parâmetros diretamente dos dados do Google Sheets (`$json.campo_da_planilha`).*

**Passo 3: Atualização de Status na Planilha (N8N - Google Sheets)**

*   **Objetivo**: Registrar que a mensagem foi enviada com sucesso, evitando duplicidade e fornecendo rastreabilidade.
*   **Ações**:
    1.  Adicione um módulo "Google Sheets" e selecione "Update Row".
    2.  **Credenciais**: Use a mesma conexão.
    3.  **Spreadsheet**: Selecione a mesma planilha.
    4.  **Sheet Name**: Especifique a aba.
    5.  **Key Column**: Selecione a coluna que identifica unicamente a linha (ex: `numero_pedido`).
    6.  **Key Value**: Mapeie `{{$json.numero_pedido}}` do gatilho.
    7.  **Update Columns**: Adicione uma coluna (ex: `status_whatsapp`) e defina o valor como `Mensagem Enviada` ou `{{$now("YYYY-MM-DD HH:mm:ss")}}`.

---

## Templates

### Template de Mensagem de Boas-Vindas com Botões de Resposta Rápida

```json
{
  "messaging_product": "whatsapp",
  "to": "5511998877665",
  "type": "interactive",
  "interactive": {
    "type": "button",
    "header": {
      "type": "text",
      "text": "Bem-vindo(a) à Loja Exemplo!"
    },
    "body": {
      "text": "Olá Ana Silva! Eu sou o assistente virtual da Loja Exemplo. Como posso ajudar você hoje?"
    },
    "action": {
      "buttons": [
        {
          "type": "reply",
          "reply": {
            "id": "RASTREAR_PEDIDO",
            "title": "Rastrear meu Pedido"
          }
        },
        {
          "type": "reply",
          "reply": {
            "id": "FALAR_ATENDENTE",
            "title": "Falar com Atendente"
          }
        },
        {
          "type": "reply",
          "reply": {
            "id": "SUGESTOES_PRODUTOS",
            "title": "Ver Produtos"
          }
        }
      ]
    }
  }
}
```

### Template de Notificação de Entrega Agendada (Aprovado pela Meta)

```json
{
  "messaging_product": "whatsapp",
  "to": "5511998877665",
  "type": "template",
  "template": {
    "name": "entrega_agendada",
    "language": { "code": "pt_BR" },
    "components": [
      {
        "type": "header",
        "parameters": [
          {
            "type": "image",
            "image": {
              "link": "https://www.exemplo.com/imagens/icone-caminhao.png"
            }
          }
        ]
      },
      {
        "type": "body",
        "parameters": [
          { "type": "text", "text": "Maria da Silva" },
          { "type": "text", "text": "P123456789" },
          { "type": "text", "text": "05/03/2026" },
          { "type": "text", "text": "08:00 às 12:00" },
          { "type": "text", "text": "Rua das Flores, 123" }
        ]
      },
      {
        "type": "button",
        "sub_type": "url",
        "index": 0,
        "parameters": [
          { "type": "text", "text": "Acompanhar Pedido" }
        ]
      }
    ]
  }
}
```

---

## Checklist

- [x] Obter e configurar um número de telefone na WhatsApp Business API (via provedor ou Meta Cloud API).
- [x] Configurar um webhook para receber mensagens de entrada na plataforma de automação (Make/N8N/Zapier).
- [x] Criar fluxos de conversa (árvore de decisão ou IA) para as principais intenções do usuário.
- [x] Registrar e ter templates de mensagens pré-aprovados pela Meta para mensageria ativa.
- [x] Implementar mecanismos de fallback para atendimento humano em casos complexos.
- [x] Configurar um dashboard para monitoramento de métricas do chatbot (conversas iniciadas, taxa de resolução).
- [x] Realizar testes completos de ponta a ponta do fluxo do chatbot com diferentes cenários.
- [x] Garantir conformidade com as políticas de mensagens do WhatsApp e LGPD.
- [x] Implementar tratamento de erros e notificações para falhas na automação.
- [x] Definir um processo para atualização e melhoria contínua do chatbot com base em feedback.

---

## Métricas de Referência

| Métrica                         | Benchmark | Meta      |
|---------------------------------|-----------|-----------|
| Taxa de Resolução do Chatbot    | 60-75%    | >80%      |
| Tempo Médio de Resposta Inicial | <5 segundos | <2 segundos |
| CSAT (Customer Satisfaction Score) | 4.0/5.0   | >4.5/5.0  |
| Taxa de Transferência para Atendente | 25-40%    | <20%      |
| Volume de Mensagens Processadas | 5.000/mês | 10.000+/mês |
| Taxa de Conversão (mensageria ativa) | 5-15%     | >18%      |

---

## Erros Comuns

1.  **Não configurar o token de verificação do webhook corretamente**: O Meta Cloud API exige um token de verificação para validar seu webhook. Se o token configurado no painel da Meta não for idêntico ao configurado no Make/N8N, as mensagens não serão entregues. Verifique a correspondência exata, incluindo case-sensitivity.
2.  **Enviar mensagens fora da janela de 24h ou sem Template Message**: O WhatsApp só permite mensagens de marketing, promoção ou reengajamento via Template Messages pré-aprovadas. Fora da janela de 24 horas de interação ativa iniciada pelo usuário, qualquer mensagem que não seja um template será rejeitada pela API. Sempre utilize Templates para iniciar conversas ou enviar notificações proativas.
3.  **Exceder limites de Rate Limit da API**: Enviar um volume muito grande de mensagens em um curto período pode levar ao bloqueio temporário do seu número pela API do WhatsApp. Implemente um mecanismo de fila e retry com backoff exponencial ou distribua o envio de mensagens em lotes menores para evitar atingir os limites.
4.  **Não tratar variações de entrada do usuário (IA)**: Usuários digitam de diversas formas e com erros de digitação. Chatbots baseados estritamente em regras (palavras-chave exatas) falham em entender a intenção. Utilize processamento de linguagem natural (NLP/NLU) via integrações com OpenAI, Dialogflow, ou similares, para compreender a intenção por trás de frases como "queria saber do meu pedido" ou "rastrear minha encomenda", mesmo com variações.
5.  **Ignorar a política de opt-in para mensageria ativa**: Enviar Template Messages para usuários que não deram consentimento explícito (opt-in) para receber comunicações pode resultar em bloqueios e penalidades. Garanta que você tenha um registro claro do consentimento do usuário antes de iniciar qualquer conversa proativa.

---

## Dicas Avançadas

1.  **Personalização Contextual com Dados CRM**: Integre o chatbot com seu sistema CRM (ex: Salesforce, HubSpot) ou banco de dados de clientes via APIs. Ao identificar o usuário pelo número de telefone (WA ID), recupere informações como nome, histórico de compras, status de pedidos e preferências. Utilize esses dados para personalizar dinamicamente a conversa.
    *   **Exemplo**: "Olá, [Nome do Cliente]! Vi que seu pedido [Número do Pedido] de [Produto] está a caminho e deve chegar em [Data]. Posso ajudar com mais alguma coisa relacionada à sua compra recente?"
2.  **A/B Testing de Fluxos Conversacionais e Prompts de IA**: Utilize ferramentas de automação (Make/N8N) para dividir o tráfego de usuários entre diferentes versões de fluxos de conversa, prompts de IA ou mensagens de boas-vindas. Monitore métricas como taxa de resolução, CSAT e conversão para identificar qual abordagem gera os melhores resultados e otimizar continuamente o desempenho do chatbot.
    *   **Exemplo**: Testar dois prompts diferentes para o OpenAI para a mesma intenção do usuário e comparar a qualidade da resposta gerada e a taxa de follow-up.
3.  **Integração com Sistemas Legados via APIs para Automação Completa**: Não se limite a apenas responder. Use a automação (Make/N8N/Zapier) para conectar o chatbot a sistemas ERP, estoque, agendamento de serviços ou portais de clientes. Isso permite que o chatbot execute ações reais em outros sistemas sem intervenção humana