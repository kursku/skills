---
name: api-integration-hub
description: "Api Integration Hub — Skill especializada para api integration hub"
license: MIT
metadata:
  version: 1.0.0
  author: Cafe Code AI
  category: 12-ia-automacao
  updated: 2026-03-01
risk: offensive
---

# Api Integration Hub

Capacita o Claude a projetar, implementar e gerenciar hubs de integração de APIs robustos, utilizando ferramentas low-code como Make/N8N/Zapier, orquestrando fluxos complexos para chatbots e sistemas diversos.

---

## Keywords

- API Gateway
- Webhooks
- OAuth 2.0
- iPaaS (Integration Platform as a Service)
- ETL (Extract, Transform, Load)
- Data Mapping
- Error Handling
- Rate Limiting
- Observability
- Low-Code Automation
- Microservices Integration
- API Versioning
- JWT Authentication

---

## Quick Start

1.  **Configurar Webhook de Entrada:** Crie um módulo "Webhook personalizado" no Make.com e copie o URL gerado para ser o endpoint do sistema de origem (ex: chatbot).
2.  **Mapear Dados Recebidos:** Envie um payload de teste para o webhook e utilize o editor de mapeamento de dados do Make.com para identificar e extrair campos relevantes (ex: `event.text`, `user.id`).
3.  **Realizar Chamada à API Externa:** Adicione um módulo "HTTP Make a request" para interagir com uma API de destino (ex: CRM). Configure o método (POST, GET), URL, cabeçalhos (ex: `Authorization: Bearer {{token}}`) e corpo da requisição com dados mapeados.
4.  **Processar Resposta e Enviar Feedback:** Analise a resposta da API externa. Adicione um módulo "HTTP Make a request" ou módulo específico do chatbot para enviar uma mensagem de volta ao usuário, confirmando a ação ou informando um erro.
5.  **Ativar Cenário e Monitorar:** Salve e ative o cenário. Configure alertas de erro no Make.com para receber notificações em caso de falhas inesperadas.

---

## Core Workflows

### Workflow 1: Orquestração de Pedidos de E-commerce via Chatbot e CRM (Make.com)

**Cenário:** Um chatbot de e-commerce recebe a intenção de compra de um cliente, verifica a disponibilidade de produtos, cria um pedido no CRM (Pipedrive) e, em seguida, notifica o cliente sobre o status do pedido.

**Passos Detalhados:**

1.  **Módulo 1: Webhook - Custom webhook (Entrada do Chatbot)**
    *   **Configuração:** Crie um webhook customizado.
    *   **Exemplo de URL do Webhook:** `https://hook.us1.make.com/abcdef123456789`
    *   **Payload de Exemplo (recebido do chatbot Blip):**
        ```json
        {
          "id": "chat-session-xyz-123",
          "from": "whatsapp:+5511987654321@wa.gw.msging.net",
          "type": "application/vnd.lime.collection+json",
          "content": {
            "items": [
              {"sku": "PROD001", "quantity": 2, "name": "Fone Bluetooth"},
              {"sku": "PROD005", "quantity": 1, "name": "Mouse Sem Fio"}
            ]
          },
          "metadata": {
            "customer_email": "cliente@example.com",
            "customer_name": "João da Silva"
          }
        }
        ```

2.  **Módulo 2: Iterator (Processar Itens do Pedido)**
    *   **Configuração:** Itera sobre `1.content.items` para processar cada produto individualmente.

3.  **Módulo 3: HTTP - Make a request (Consultar Estoque por SKU)**
    *   **Configuração:**
        *   **URL:** `https://api.meuecommerce.com/v1/products/{{2.sku}}/stock` (onde `2.sku` é o SKU do item atual do Iterator).
        *   **Método:** `GET`
        *   **Headers:**
            *   `Content-Type`: `application/json`
            *   `Authorization`: `Bearer {{connection.ecommerce_api_key}}`
    *   **Resposta Esperada:**
        ```json
        {"sku": "PROD001", "available_stock": 50, "price": 89.90}
        ```

4.  **Módulo 4: Router (Decisão: Estoque Disponível vs. Indisponível)**
    *   **Configuração:** Duas rotas.
        *   **Rota A (Estoque Suficiente):** Filtro `3.available_stock >= 2.quantity`.
        *   **Rota B (Estoque Insuficiente):** Filtro `3.available_stock < 2.quantity`.

5.  **Módulo 5A (Rota A): Pipedrive - Create a Person (Criar ou Atualizar Cliente)**
    *   **Configuração:**
        *   **Name:** `{{1.metadata.customer_name}}`
        *   **Email:** `{{1.metadata.customer_email}}`
        *   **Phone:** Extraído do `1.from` ou outro campo.

6.  **Módulo 6A (Rota A): Pipedrive - Create a Deal (Criar Negócio no CRM)**
    *   **Configuração:**
        *   **Title:** `Pedido - {{1.metadata.customer_name}} - {{Now}}`
        *   **Person:** `{{5A.data.id}}` (ID da pessoa criada/atualizada no Pipedrive)
        *   **Stage:** `Novo Pedido`
        *   **Value:** Calculado a partir de `3.price * 2.quantity` (acumulado em uma variável, se houver múltiplos itens).

7.  **Módulo 7A (Rota A): HTTP - Make a request (Notificar Chatbot - Pedido Confirmado)**
    *   **Configuração:**
        *   **URL:** `https://api.blip.ai/messages`
        *   **Método:** `POST`
        *   **Headers:**
            *   `Content-Type`: `application/json`
            *   `Authorization`: `Key {{connection.blip_api_key}}`
        *   **Corpo (JSON):**
            ```json
            {
              "id": "{{1.id}}-confirm",
              "to": "{{1.from}}",
              "type": "text/plain",
              "content": "Olá {{1.metadata.customer_name}}! Seu pedido foi confirmado com sucesso. Número do negócio: {{6A.data.id}}."
            }
            ```

8.  **Módulo 5B (Rota B): HTTP - Make a request (Notificar Chatbot - Estoque Indisponível)**
    *   **Configuração:** Similar ao 7A, mas com mensagem de erro.
    *   **Corpo (JSON):**
        ```json
        {
          "id": "{{1.id}}-fail",
          "to": "{{1.from}}",
          "type": "text/plain",
          "content": "Desculpe, {{2.name}} está com estoque insuficiente (disponível: {{3.available_stock}}). Por favor, ajuste a quantidade."
        }
        ```

### Workflow 2: Sincronização Bidirecional de Dados entre ERP e Sistema de Suporte (N8N)

**Cenário:** Novas ordens de serviço no ERP (SAP B1 via API) criam automaticamente tickets no sistema de suporte (Zendesk). Atualizações de status no Zendesk (ex: ticket resolvido) atualizam o status correspondente da ordem de serviço no ERP.

**Passos Detalhados:**

1.  **Fluxo de ERP para Zendesk:**
    *   **Módulo 1: Webhook (Entrada de Nova Ordem de Serviço do ERP)**
        *   **Configuração:** Defina um webhook.
        *   **Exemplo de URL do Webhook:** `https://n8n.meuhub.com/webhook/erp-new-order`
        *   **Payload de Exemplo (recebido do ERP):**
            ```json
            {
              "orderId": "OS-20240726-001",
              "customerId": "CUST001",
              "customerName": "Empresa Alfa Ltda.",
              "customerEmail": "suporte@alfa.com",
              "issueDescription": "Problema de conexão com o módulo financeiro.",
              "priority": "Alta",
              "createdAt": "2024-07-26T10:00:00Z"
            }
            ```
    *   **Módulo 2: Zendesk - Create Ticket (Criar Ticket no Zendesk)**
        *   **Configuração:**
            *   **Subject:** `Problema na OS {{1.json.orderId}}: {{1.json.issueDescription}}`
            *   **Comment:** `Detalhes: {{1.json.issueDescription}}. Cliente: {{1.json.customerName}}`
            *   **Requester Email:** `{{1.json.customerEmail}}`
            *   **Priority:** `{{1.json.priority}}`
            *   **Tags:** `erp_origem, os_{{1.json.orderId}}`
    *   **Módulo 3: HTTP Request (Atualizar ERP com ID do Ticket)**
        *   **Configuração:**
            *   **URL:** `https://api.meuerp.com/v1/orders/{{1.json.orderId}}/update`
            *   **Method:** `PUT`
            *   **Headers:** `Authorization: Bearer {{env.ERP_API_TOKEN}}`
            *   **Body (JSON):**
                ```json
                {
                  "status": "Em Atendimento",
                  "zendeskTicketId": "{{2.json.ticket.id}}"
                }
                ```

2.  **Fluxo de Zendesk para ERP:**
    *   **Módulo 1: Webhook (Entrada de Atualização de Ticket do Zendesk)**
        *   **Configuração:** Defina um webhook (configurado no Zendesk como "Target" para eventos de atualização de ticket).
        *   **Exemplo de URL do Webhook:** `https://n8n.meuhub.com/webhook/zendesk-ticket-update`
        *   **Payload de Exemplo (recebido do Zendesk):**
            ```json
            {
              "ticket_id": 12345,
              "current_status": "solved",
              "previous_status": "open",
              "ticket_tags": ["erp_origem", "os_OS-20240726-001"],
              "updated_at": "2024-07-26T15:30:00Z"
            }
            ```
    *   **Módulo 2: IF (Filtrar Tickets de Origem ERP e Status Resolvido)**
        *   **Configuração:**
            *   **Condição 1:** `{{1.json.ticket_tags}} contains "erp_origem"`
            *   **Condição 2:** `{{1.json.current_status}} === "solved"`
    *   **Módulo 3: Function (Extrair Order ID da Tag)**
        *   **Configuração (JavaScript):**
            ```javascript
            const tags = $json.ticket_tags;
            const orderTag = tags.find(tag => tag.startsWith('os_'));
            if (orderTag) {
              return [{ json: { orderId: orderTag.replace('os_', '') } }];
            }
            return []; // Retorna vazio se não encontrar a tag
            ```
    *   **Módulo 4: HTTP Request (Atualizar ERP com Status Resolvido)**
        *   **Configuração:**
            *   **URL:** `https://api.meuerp.com/v1/orders/{{3.json.orderId}}/update`
            *   **Method:** `PUT`
            *   **Headers:** `Authorization: Bearer {{env.ERP_API_TOKEN}}`
            *   **Body (JSON):**
                ```json
                {
                  "status": "Concluído",
                  "resolutionDate": "{{1.json.updated_at}}"
                }
                ```

---

## Templates

### Template de Configuração de Webhook de Entrada (Make.com)

```json
{
  "webhook_id": "wh-ecommerce-pedido-123",
  "method": "POST",
  "payload_example": {
    "customer_name": "Ana Silva",
    "customer_email": "ana.silva@example.com",
    "items": [
      {"sku": "PROD001", "quantity": 2, "unit_price": 89.90},
      {"sku": "PROD005", "quantity": 1, "unit_price": 49.90}
    ],
    "total_amount": 229.70,
    "chat_platform": "Whatsapp",
    "conversation_id": "abc-123-xyz"
  },
  "expected_response": {
    "status": "success",
    "message": "Pedido recebido e em processamento.",
    "order_id": "PEDIDO-20240726-001",
    "external_reference": "CRM-DEAL-98765"
  },
  "error_response_example": {
    "status": "error",
    "code": "INSUFFICIENT_STOCK",
    "message": "Produto PROD005 com estoque insuficiente.",
    "details": {"sku": "PROD005", "requested": 1, "available": 0}
  }
}
```

### Template de Requisição HTTP para API REST (N8N)

```json
{
  "node_name": "Criar Contato no Pipedrive",
  "node_type": "n8n-nodes-base.httpRequest",
  "parameters": {
    "requestMethod": "POST",
    "url": "https://api.pipedrive.com/v1/persons?api_token={{ env.PIPEDRIVE_API_TOKEN }}",
    "options": {
      "headers": [
        {"name": "Content-Type", "value": "application/json"},
        {"name": "Accept", "value": "application/json"}
      ],
      "query": []
    },
    "jsonParameters": true,
    "body": {
      "name": "{{ $json.customer_name }}",
      "email": [
        {"label": "work", "value": "{{ $json.customer_email }}", "primary": true}
      ],
      "phone": [
        {"label": "mobile", "value": "{{ $json.customer_phone }}", "primary": true}
      ],
      "owner_id": 12345,
      "visible_to": 3,
      "custom_field_api_integration_id": "{{ $json.integration_source_id }}"
    },
    "responseFormat": "json",
    "sendBinaryData": false,
    "ignoreHttpStatusErrors": false,
    "splitIntoItems": false,
    "retryOnFail": true,
    "retryAttempts": 3,
    "retryDelay": "2000"
  },
  "id": "node_pipedrive_create_person",
  "type": "n8n-nodes-base.httpRequest"
}
```

---

## Checklist

- [x] Autenticação e autorização para cada API configuradas (OAuth 2.0, API Keys, JWT).
- [x] Tratamento de erros (retry com back-off, fallback, notificação) implementado para falhas de API.
- [x] Limites de taxa (rate limiting) das APIs externas identificados e respeitados nos fluxos.
- [x] Monitoramento proativo (logs, dashboards, alertas) configurado para todas as transações.
- [x] Mapeamento de dados entre os sistemas de origem e destino validado e documentado.
- [x] Testes unitários e de ponta a ponta dos fluxos de integração realizados com dados simulados e reais.
- [x] Estratégia de versionamento de APIs considerada para futuras atualizações de endpoints.
- [x] Documentação clara dos endpoints, payloads, e comportamentos esperados do hub de integração.
- [x] Gerenciamento seguro de segredos (API keys, tokens, credenciais) utilizando variáveis de ambiente ou cofres.
- [x] Implementação de idempotência em requisições críticas para evitar duplicação de dados.
- [x] Consideração de assincronismo (filas de mensagens) para processos de longa duração ou alto volume.
- [x] Avaliação de escalabilidade e desempenho do iPaaS frente a picos de demanda.

---

## Métricas de Referência

| Métrica | Benchmark | Meta |
| :-------------------------------- | :---------- | :---------- |
| **Taxa de Sucesso de Transações** | > 99.5%     | 99.9%       |
| **Latência Média de Resposta (API Gateway)** | < 200 ms    | < 100 ms    |
| **Tempo Médio para Recuperação (MTTR)** | < 30 min    | < 10 min    |
| **Custo por Transação (iPaaS)** | < $0.005    | < $0.002    |
| **Taxa de Erros 5xx (Servidor)** | < 0.1%      | < 0.01%     |
| **Tempo de Desenvolvimento de Nova Integração** | < 3 dias    | < 1 dia     |

---

## Erros Comuns

1.  **Chaves de API ou Tokens de Autenticação Expirados/Inválidos**: Este é um dos erros mais frequentes. Sempre implementar um mecanismo de rotação de credenciais ou refresh tokens para autenticações OAuth 2.0. Para chaves de API estáticas, configure alertas de expiração e tenha um processo de renovação. **Exemplo:** Ao receber um `HTTP 401 Unauthorized`, o fluxo deve tentar usar um refresh token (se aplicável) ou enviar uma notificação imediata para o administrador para renovação manual da chave.
2.  **Mapeamento de Dados Incorreto/Incompleto**: Falha em converter tipos de dados (string para int), campos ausentes ou formatação incompatível com a API de destino. **Exemplo:** Se uma API de CRM espera um `integer` para `quantidade_de_itens` e o webhook envia uma `string` (`"2"`), converter explicitamente para `{{parseInt(2.quantity)}}`. Utilize o recurso "Data Tester" do Make/N8N para simular payloads e validar o mapeamento.
3.  **Exceder Limites de Taxa (Rate Limiting) da API Externa**: Ao fazer muitas requisições em um curto período, a API externa pode retornar um `HTTP 429 Too Many Requests`. **Exemplo:** Implementar estratégias de "back-off" e "retry" com atraso exponencial. Se o hub recebe um 429, deve esperar 5 segundos e tentar novamente, aumentando o tempo (ex: 10s, 20s) a cada falha subsequente, até um limite máximo de tentativas.
4.  **Tratamento Inadequado de Erros da API Externa**: Não considerar todos os códigos de status HTTP e mensagens de erro específicas que a API de destino pode retornar além do 200 OK. **Exemplo:** Uma API de pagamento pode retornar `HTTP 400 Bad Request` com um corpo `{"code": "INVALID_CARD", "message": "Número de cartão inválido"}`. O hub deve ser capaz de capturar este `code` e `message` para informar ao usuário final de forma amigável, em vez de um erro genérico de integração.
5.  **Falta de Logs Detalhados e Monitoramento**: Dificulta enormemente a depuração e a identificação da causa raiz de falhas em integrações complexas. **Exemplo:** Garantir que cada nó crítico de automação registre o status da execução, o payload de entrada e saída, e o tempo de resposta. Configurar alertas no iPaaS (Make/N8N) para notificar via e-mail ou Slack em caso de falhas persistentes ou exceções não tratadas.

---

## Dicas Avançadas

1.  **Implementação de Idempotência em Webhooks e Requisições API**: Para evitar o processamento duplicado de eventos ou a criação de registros repetidos quando um webhook é acionado múltiplas vezes por erro ou reenvio. **Exemplo:** Ao fazer uma requisição `POST` para criar um recurso, inclua um cabeçalho `X-Idempotency-Key: {{unique_transaction_id}}`. O servidor pode usar essa chave para garantir que a operação seja executada apenas uma vez. No lado do hub, mantenha um registro (ex: em um banco de dados simples ou cache) dos `transaction_id` já processados antes de iniciar um fluxo.
2.  **Uso de Filas de Mensagens (ex: AWS SQS, RabbitMQ) para Assincronismo e Resiliência**: Desacoplar sistemas e lidar com picos de carga ou processos de longa duração. **Exemplo:** Em vez de chamar a API de CRM diretamente após o webhook do chatbot, o webhook apenas envia a mensagem para uma fila. Um worker separado (outro fluxo Make/N8N, ou um script customizado) consome essa fila de forma assíncrona, processando os pedidos de criação de contato no CRM em seu próprio ritmo, protegendo o hub contra sobrecarga e garantindo a entrega mesmo se o CRM estiver temporariamente indisponível.
3.  **Desenvolvimento de APIs RESTful Personalizadas como Camada de Abstração (API Gateway/Proxy)**: Criar uma camada intermédia para simplificar a interação com APIs legadas, complexas ou múltiplas. **Exemplo:** Usar um framework como Node.js (Express) ou Python (Flask) para criar um endpoint `/api/v1/pedido` que, internamente, orquestra chamadas a um