---
name: webhook-integration
description: "Webhook Integration — Skill especializada para webhook integration"
license: MIT
metadata:
  version: 1.0.0
  author: Cafe Code AI
  category: 12-ia-automacao
  updated: 2026-03-01
risk: offensive
---

# Webhook Integration

Esta skill capacita o Claude a projetar, implementar e depurar integrações de webhook para automatizar fluxos de trabalho e conectar sistemas, com foco em plataformas como Make, N8N e Zapier.

---

## Keywords

Webhook, Payload, Endpoint, Listener, Webhook URL, HTTP POST, JSON, API Gateway, OAuth, Token de Acesso, Make.com, N8N, Zapier, Automação, Event-driven, Retry Policy, Idempotência, Signature.

---

## Quick Start

1.  **Obter Webhook URL:** Gere um endpoint único em sua plataforma de automação (ex: Make.com > Webhooks > Custom Webhook > "Copy address to clipboard").
2.  **Configurar Disparador:** Cole o Webhook URL no sistema de origem (ex: Stripe, Typeform, CRM) que enviará os dados, definindo o evento de disparo (ex: "nova venda", "novo lead", "atualização de status").
3.  **Capturar Payload:** Envie um evento de teste do sistema de origem para o Webhook URL e capture o payload JSON na plataforma de automação para analisar a estrutura dos dados.
4.  **Processar e Mapear Dados:** Use módulos na plataforma de automação (ex: "JSON Parser", "Text Parser") para extrair e transformar informações específicas do payload, mapeando-as para os campos de destino.
5.  **Testar e Ativar Fluxo:** Execute o cenário completo na plataforma de automação, monitorando logs e verificando se os dados são processados e enviados corretamente para o destino final (ex: Google Sheets, Slack, CRM), e então ative-o.

---

## Core Workflows

### Workflow 1: Recebimento de Leads de Formulário Web e Notificação no Slack via Make.com

Este workflow detalha a criação de uma integração de webhook para capturar novos leads de um formulário web (ex: Typeform, Jotform) e enviar uma notificação formatada para um canal Slack, utilizando o Make.com como orquestrador.

**Passos Detalhados:**

1.  **Criação do Webhook no Make.com:**
    *   Acesse Make.com e crie um novo cenário.
    *   Adicione um módulo "Webhooks" e selecione "Custom Webhook".
    *   Clique em "Add a hook", dê um nome descritivo (ex: `leads_form_contato`), e clique em "Save".
    *   Copie o "Webhook URL" gerado (ex: `https://hook.eu1.make.com/abcdefghijk1234567890`). Este será o endpoint que seu formulário irá chamar.

2.  **Configuração do Formulário Web (Exemplo Typeform):**
    *   No painel do seu formulário (ex: Typeform), navegue até a seção "Connect" ou "Integrations".
    *   Localize a opção "Webhooks" e clique em "Add a webhook".
    *   Cole o "Webhook URL" do Make.com no campo apropriado.
    *   Configure o evento para disparar em "On new submission" ou similar.
    *   Envie um teste preenchendo o formulário para que o Make.com possa "ouvir" e capturar a estrutura do payload.

3.  **Mapeamento e Processamento do Payload no Make.com:**
    *   Após a captura do payload de teste, o Make.com exibirá os dados recebidos. Inspecione a estrutura JSON.
    *   Adicione um módulo "Slack" e selecione a ação "Create a Message".
    *   Conecte sua conta Slack.
    *   No campo "Channel", selecione o canal de destino (ex: `#leads-novos`).
    *   No campo "Text", construa a mensagem usando os dados mapeados do webhook e formatação Markdown. É crucial verificar o JSON real capturado para os caminhos corretos.
        ```markdown
        *NOVO LEAD RECEBIDO!* 🚀
        Nome: {{1.form_response.answers[0].text}}
        Email: {{1.form_response.answers[1].email}}
        Telefone: {{1.form_response.answers[2].text}}
        Origem: Formulário de Contato - {{1.form_response.definition.title}}
        Submetido em: {{1.form_response.submitted_at}}
        ```
        *(Nota: Os índices `[0]`, `[1]`, `[2]` e os caminhos `form_response.answers` ou `form_response.definition.title` podem variar ligeiramente dependendo da estrutura exata do payload do seu Typeform. Sempre use a visualização do payload capturado para mapear com precisão.)*

4.  **Tratamento de Erros e Monitoramento (Recomendado):**
    *   Adicione um módulo "Error Handler" (ferramenta Make.com) para notificar em caso de falha no envio para o Slack.
    *   Configure-o para enviar um e-mail para a equipe de TI com os detalhes do erro e o payload original, permitindo depuração rápida.

**Exemplo de Payload (Typeform simplificado):**

```json
{
  "event_id": "EV-XYZ12345",
  "event_type": "form_response",
  "form_response": {
    "form_id": "abcdefg",
    "submitted_at": "2024-07-26T10:00:00Z",
    "definition": {
      "title": "Formulário de Contato do Site"
    },
    "answers": [
      {
        "field": { "id": "name_field", "type": "text", "ref": "nome_completo" },
        "type": "text",
        "text": "João Silva"
      },
      {
        "field": { "id": "email_field", "type": "email", "ref": "email_contato" },
        "type": "email",
        "email": "joao.silva@exemplo.com"
      },
      {
        "field": { "id": "phone_field", "type": "text", "ref": "telefone_contato" },
        "type": "text",
        "text": "+5511987654321"
      }
    ]
  }
}
```

### Workflow 2: Sincronização de Dados de Vendas de E-commerce com CRM via N8N (HTTP Request)

Este workflow foca em como usar um webhook para receber informações de novas vendas de uma plataforma de e-commerce (ex: WooCommerce via plugin) e criar/atualizar um registro de contato ou negócio em um CRM (ex: Pipedrive) usando o N8N.

**Passos Detalhados:**

1.  **Configuração do Webhook no N8N:**
    *   Inicie um novo workflow no N8N.
    *   Adicione um nó "Webhook" e configure-o como "POST" (geralmente é o método padrão para recebimento de dados de eventos).
    *   O N8N gerará um "Webhook URL" (ex: `https://yourn8n.com/webhook-test/your-unique-id`). Este URL será o destino das notificações do seu e-commerce.

2.  **Configuração na Plataforma de E-commerce (Exemplo WooCommerce):**
    *   No painel do WooCommerce, navegue até "WooCommerce > Configurações > Avançado > Webhooks".
    *   Clique em "Adicionar webhook".
    *   Dê um nome (ex: `N8N_Nova_Venda`).
    *   Defina o "Tópico" como "Pedido criado" (`order.created`).
    *   Cole o "Webhook URL" do N8N no campo "URL de entrega".
    *   Selecione o formato do payload como JSON.
    *   Envie um pedido de teste no e-commerce para que o N8N possa capturar o payload e inspecionar a estrutura dos dados.

3.  **Processamento e Envio para CRM no N8N:**
    *   Após a captura do payload, inspecione a estrutura JSON recebida no nó "Webhook" do N8N.
    *   Adicione um nó "Set" para extrair e renomear campos importantes para o Pipedrive.
        *   `order.billing.first_name` para `firstName`
        *   `order.billing.last_name` para `lastName`
        *   `order.billing.email` para `email`
        *   `order.total` para `dealValue`
        *   `order.id` para `orderId`
    *   Adicione um nó "Pipedrive" para criar um novo negócio (Deal).
    *   Conecte sua conta do Pipedrive (via API Key).
    *   Configure o nó para a operação "Create Deal".
    *   Mapeie os campos de entrada do nó "Set" para os campos correspondentes no Pipedrive:
        *   `Title`: `Novo Pedido #{{ $json.orderId }} - {{ $json.firstName }} {{ $json.lastName }}`
        *   `Value`: `{{ $json.dealValue }}`
        *   `Currency`: `BRL`
        *   `Person Email`: `{{ $json.email }}` (Isso criará ou associará uma pessoa automaticamente)
        *   `Stage`: Selecione o ID da etapa de "Novo Lead" ou "Prospecção" no seu Pipedrive.
    *   **Opcional - Idempotência**: Adicione um nó "Code" ou um nó de banco de dados para verificar se `orderId` já foi processado para evitar duplicação em caso de retries.

4.  **Tratamento de Erros e Logs:**
    *   Adicione um nó "Respond to Webhook" no final do fluxo para enviar um status HTTP 200 OK de volta ao WooCommerce, indicando que o webhook foi recebido, mesmo que o processamento interno falhe (para não gerar retries indesejados no WooCommerce).
    *   Utilize o nó "Log" para registrar os payloads processados e os resultados das operações do CRM.
    *   Configure notificações por e-mail ou Slack (usando um nó "Send Email" ou "Slack") em caso de falha na criação/atualização do CRM, incluindo o payload original para depuração.

**Exemplo de Payload (WooCommerce simplificado):**

```json
{
  "id": 12345,
  "status": "processing",
  "currency": "BRL",
  "total": "199.90",
  "customer_id": 678,
  "billing": {
    "first_name": "Maria",
    "last_name": "Santos",
    "address_1": "Rua Exemplo, 123",
    "city": "São Paulo",
    "state": "SP",
    "postcode": "01000-000",
    "country": "BR",
    "email": "maria.santos@exemplo.com",
    "phone": "11999998888"
  },
  "line_items": [
    {
      "id": 1,
      "name": "Produto X",
      "product_id": 987,
      "quantity": 1,
      "total": "199.90"
    }
  ],
  "date_created": "2024-07-26T15:30:00"
}
```

---

## Templates

### Template 1: Configuração de Webhook para Notificação de Evento (JSON)

Este é um exemplo de um corpo de requisição HTTP POST para um webhook, formatado em JSON, que um sistema de origem enviaria ao disparar um evento.

```json
{
  "event_type": "new_user_registration",
  "timestamp": "2024-07-26T14:30:00Z",
  "payload": {
    "user_id": "usr_abc123",
    "email": "novo.usuario@exemplo.com",
    "name": "Carlos Nogueira",
    "source": "website_signup_form",
    "metadata": {
      "ip_address": "203.0.113.45",
      "browser": "Chrome",
      "os": "macOS"
    }
  },
  "signature": "sha256=a1b2c3d4e5f6g7h8i9j0k1l2m3n4o5p6q7r8s9t0u1v2w3x3y4z5a6b7c8d9e0f1"
}
```

### Template 2: Prompt para Claude para Ajuda em Depuração de Webhook no Zapier

Este prompt auxilia na depuração de um problema de webhook no Zapier, fornecendo contexto e solicitando uma análise detalhada.

```
Sou um especialista em automação e estou enfrentando um problema de depuração com um webhook no Zapier.
O sistema de origem (Plataforma de E-learning) está enviando dados quando um aluno conclui um curso, mas meu Zap não está criando o certificado no Google Drive corretamente.

**Detalhes:**
- **Zapier Trigger:** Catch Hook (Webhook)
- **Payload Capturado (Zapier - Teste de Trigger):**
```json
{
  "studentId": "S-007",
  "studentName": "Laura Mendes",
  "studentEmail": "laura.mendes@email.com",
  "courseTitle": "Introdução à Programação Python",
  "completionDate": "2024-07-25",
  "score": 95,
  "certificateUrl": null
}
```
- **Ação do Zapier:** Google Drive - Create File From Text
  - **File Name:** `Certificado - {{studentName}} - {{courseTitle}}`
  - **File Content:**
    ```
    CERTIFICADO DE CONCLUSÃO
    Este certifica que {{studentName}} concluiu o curso de "{{courseTitle}}"
    com a pontuação de {{score}}%.
    Data de Conclusão: {{