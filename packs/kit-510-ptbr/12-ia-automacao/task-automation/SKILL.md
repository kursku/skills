---
name: task-automation
description: "Task Automation — Skill especializada para projetar, construir e otimizar fluxos de trabalho automatizados utilizando chatbots, Make, N8N, Zapier e APIs."
license: MIT
metadata:
  version: 1.0.0
  author: Cafe Code AI
  category: 12-ia-automacao
  updated: 2026-03-01
---

# Task Automation

Esta skill capacita o Claude a atuar como um engenheiro de automação, projetando e implementando soluções robustas para otimização de processos, integração de sistemas e orquestração de tarefas repetitivas, com foco em eficiência e escalabilidade.

---

## Keywords

Automação de Processos, Integração de APIs, Webhooks, Make.com, N8N, Zapier, Prompt Engineering, Chatbot Orchestration, RPA (Robotic Process Automation), Data Mapping, ETL (Extract, Transform, Load), API Gateway, Low-Code Automation, Serverless Functions, Business Process Automation.

---

## Quick Start

1.  **Escolher o Gatilho (Trigger):** Defina o evento que iniciará o fluxo de automação, como um novo registro em um banco de dados, um e-mail recebido com um assunto específico ou uma requisição HTTP via webhook.
2.  **Mapear Fluxo de Dados:** Identifique as informações essenciais que precisam ser extraídas do gatilho e passadas para as próximas etapas, desenhando o caminho dos dados entre os sistemas.
3.  **Configurar Ações Sequenciais:** Organize as etapas que devem ser executadas em resposta ao gatilho, como chamar uma API, enviar uma mensagem, atualizar um CRM ou processar dados com um LLM.
4.  **Testar a Automação:** Execute o fluxo com dados de teste para verificar se todas as etapas estão funcionando conforme o esperado e se o mapeamento de dados está correto.
5.  **Monitorar e Otimizar:** Implemente ferramentas de monitoramento para acompanhar a execução, identificar falhas e otimizar o desempenho do fluxo, ajustando filtros ou adicionando tratamento de erros.

---

## Core Workflows

### Workflow 1: Automatização de Qualificação de Leads e Agendamento via Chatbot e CRM

Este workflow automatiza o processo de qualificação de leads recebidos via chatbot e o agendamento de reuniões, integrando um chatbot (ex: ManyChat, Dialogflow), uma plataforma de automação (Make.com ou N8N) e um CRM (ex: Pipedrive, HubSpot).

**Passos Detalhados:**

1.  **Gatilho (Chatbot - ManyChat):** Um lead completa um formulário de qualificação dentro do chatbot, indicando interesse em um produto específico e fornecendo e-mail, telefone e segmento. O chatbot envia esses dados via Webhook para o Make.com.

    *   **Configuração Webhook (ManyChat):** URL do Webhook do Make.com com método POST, enviando um JSON com `{"email": "{{email}}", "telefone": "{{phone}}", "segmento": "{{segmento_interesse}}"}`.

2.  **Processamento (Make.com/N8N - Módulo Webhook):** O Make.com recebe os dados do ManyChat.

    *   **Exemplo de Payload Recebido:**
        ```json
        {
          "email": "joao.silva@example.com",
          "telefone": "+5511987654321",
          "segmento": "Desenvolvimento de Software"
        }
        ```

3.  **Qualificação com LLM (Make.com/N8N - Módulo Claude AI):** Utiliza um LLM para qualificar o lead com base no `segmento` e gerar uma mensagem de apresentação inicial personalizada.

    *   **Prompt de Exemplo:**
        ```
        Você é um especialista em vendas B2B. Analise o segmento "{{segmento}}" do lead "joao.silva@example.com".
        Classifique-o como "Alta Prioridade", "Média Prioridade" ou "Baixa Prioridade" para nossa solução de automação de processos.
        Em seguida, crie uma frase de apresentação concisa e engajadora, destacando um benefício específico para este segmento.

        Formato de saída:
        Prioridade: [Prioridade]
        Mensagem: [Mensagem personalizada]
        ```

    *   **Resposta Esperada do LLM:**
        ```
        Prioridade: Alta Prioridade
        Mensagem: Olá João, percebemos seu interesse em automação para Desenvolvimento de Software. Nossa solução pode otimizar seus ciclos de entrega em até 30% e reduzir erros manuais.
        ```

4.  **Criação/Atualização no CRM (Make.com/N8N - Módulo Pipedrive/HubSpot):** Os dados do lead, incluindo a prioridade e a mensagem gerada, são enviados para o CRM.

    *   **API Call (Pipedrive - Criar Pessoa):**
        ```http
        POST https://api.pipedrive.com/v1/persons?api_token=SEU_TOKEN
        Content-Type: application/json

        {
          "name": "João Silva",
          "email": [
            { "label": "work", "value": "joao.silva@example.com", "primary": true }
          ],
          "phone": [
            { "label": "work", "value": "+5511987654321", "primary": true }
          ],
          "cf_prioridade_lead": "Alta Prioridade",
          "cf_mensagem_inicial": "Olá João, percebemos seu interesse em automação para Desenvolvimento de Software. Nossa solução pode otimizar seus ciclos de entrega em até 30% e reduzir erros manuais."
        }
        ```

5.  **Agendamento Automático (Make.com/N8N - Módulo Calendly/Acuity Scheduling):** Se a prioridade for "Alta" ou "Média", o fluxo gera um link de agendamento personalizado e o envia ao lead.

    *   **Geração de Link (Calendly API):**
        ```http
        POST https://api.calendly.com/scheduled_events/lookup
        Content-Type: application/json

        {
          "email": "joao.silva@example.com",
          "event_type_uuid": "SEU_EVENT_TYPE_UUID"
        }
        ```
        (Isso é mais para consultar, para gerar um link direto, geralmente usa-se o Calendly link pré-preenchido ou envia-se o link base)

6.  **Notificação e Follow-up (Make.com/N8N - Módulo WhatsApp Business API ou E-mail):** Envia a mensagem de apresentação e o link de agendamento via WhatsApp ou e-mail.

    *   **WhatsApp API (Mensagem de Texto):**
        ```http
        POST https://graph.facebook.com/v18.0/ID_DO_SEU_NEGOCIO/messages
        Content-Type: application/json

        {
          "messaging_product": "whatsapp",
          "to": "5511987654321",
          "type": "template",
          "template": {
            "name": "apresentacao_e_agendamento",
            "language": { "code": "pt_BR" },
            "components": [
              {
                "type": "body",
                "parameters": [
                  { "type": "text", "text": "João" },
                  { "type": "text", "text": "percebemos seu interesse em automação para Desenvolvimento de Software. Nossa solução pode otimizar seus ciclos de entrega em até 30% e reduzir erros manuais." },
                  { "type": "text", "text": "https://calendly.com/suaempresa/reuniao-descoberta" }
                ]
              }
            ]
          }
        }
        ```

### Workflow 2: Sincronização de Pedidos E-commerce e Gestão de Estoque/ERP

Este workflow automatiza a sincronização de novos pedidos de uma plataforma de e-commerce (ex: Shopify) com um sistema de gestão (ERP, ex: Bling) e notifica a equipe de logística, garantindo que o estoque seja atualizado e o pedido processado.

**Passos Detalhados:**

1.  **Gatilho (Shopify Webhook):** Um novo pedido é realizado na loja Shopify. O Shopify envia um webhook para o N8N/Make.com.

    *   **Configuração Webhook (Shopify Admin):** Evento "Order Creation", URL do Webhook do N8N/Make.com com formato JSON.

2.  **Processamento (N8N/Make.com - Módulo Webhook):** O N8N/Make.com recebe o payload do Shopify.

    *   **Exemplo de Payload Simplificado:**
        ```json
        {
          "id": 1234567890,
          "email": "cliente@email.com",
          "created_at": "2023-10-26T10:00:00-03:00",
          "total_price": "99.90",
          "line_items": [
            {
              "id": 987654321,
              "product_id": 112233,
              "variant_id": 445566,
              "title": "Camisa Polo Azul",
              "quantity": 2,
              "price": "49.95",
              "sku": "CP-AZUL-M"
            }
          ],
          "shipping_address": {
            "first_name": "Maria",
            "last_name": "Souza",
            "address1": "Rua Exemplo, 123",
            "city": "São Paulo",
            "province": "SP",
            "zip": "01000-000",
            "country": "Brazil"
          }
        }
        ```

3.  **Transformação de Dados (N8N/Make.com - Módulo Code/Função):** Os dados do Shopify são mapeados e transformados para o formato exigido pelo ERP (Bling). Isso pode incluir a concatenação de nome e sobrenome, formatação de endereço e mapeamento de SKUs.

    *   **Exemplo de Mapeamento/Transformação (pseudocódigo):**
        ```javascript
        let pedidoBling = {
          "idPedidoLoja": webhookData.id,
          "data": new Date(webhookData.created_at).toISOString().split('T')[0],
          "cliente": {
            "nome": webhookData.shipping_address.first_name + " " + webhookData.shipping_address.last_name,
            "email": webhookData.email,
            "endereco": webhookData.shipping_address.address1,
            "cidade": webhookData.shipping_address.city,
            "uf": webhookData.shipping_address.province,
            "cep": webhookData.shipping_address.zip
          },
          "itens": webhookData.line_items.map(item => ({
            "codigo": item.sku,
            "descricao": item.title,
            "qtde": item.quantity,
            "valor": item.price
          }))
        };
        ```

4.  **Criação de Pedido no ERP (N8N/Make.com - Módulo Bling API):** Os dados transformados são enviados para a API do Bling para criar um novo pedido de venda.

    *   **API Call (Bling - Criar Pedido de Venda):**
        ```http
        POST https://www.bling.com.br/Api/v3/pedidos/vendas
        Content-Type: application/json
        Authorization: Bearer SEU_TOKEN

        {
          "numero": "PEDIDO_SHOPIFY_" + webhookData.id,
          "data": new Date(webhookData.created_at).toISOString().split('T')[0],
          "dataPrevista": new Date(Date.now() + 7 * 24 * 60 * 60 * 1000).toISOString().split('T')[0], // 7 dias à frente
          "tipo": "ecommerce",
          "situacao": "Em Aberto",
          "cliente": {
            "nome": webhookData.shipping_address.first_name + " " + webhookData.shipping_address.last_name,
            "email": webhookData.email,
            "endereco": webhookData.shipping_address.address1,
            "numero": "123", // Assumindo que o número é extraído de address1 ou um campo separado
            "bairro": "Centro", // Assumindo que o bairro é inferido ou outro campo
            "cidade": webhookData.shipping_address.city,
            "estado": webhookData.shipping_address.province,
            "cep": webhookData.shipping_address.zip,
            "pais": "BR"
          },
          "itens": [
            {
              "codigo": webhookData.line_items[0].sku,
              "descricao": webhookData.line_items[0].title,
              "quantidade": webhookData.line_items[0].quantity,
              "valor": webhookData.line_items[0].price
            }
          ],
          "observacoes": "Pedido importado automaticamente via Shopify Webhook."
        }
        ```

5.  **Notificação da Equipe (N8N/Make.com - Módulo Slack/Microsoft Teams):** Uma mensagem é enviada para um canal específico da equipe de logística/expedição, informando sobre o novo pedido e os itens a serem despachados.

    *   **Slack API (Post Message):**
        ```http
        POST https://slack.com/api/chat.postMessage
        Content-Type: application/json
        Authorization: Bearer xoxb-SEU_TOKEN

        {
          "channel": "#pedidos-ecommerce",
          "text": "📦 *Novo Pedido Shopify!* \n\n*ID Shopify:* {{webhookData.id}}\n*Cliente:* {{webhookData.shipping_address.first_name}} {{webhookData.shipping_address.last_name}}\n*Itens:* {{webhookData.line_items[0].quantity}}x {{webhookData.line_items[0].title}} (SKU: {{webhookData.line_items[0].sku}})\n*Total:* R$ {{webhookData.total_price}}\n*Status Bling:* Em Aberto"
        }
        ```

---

## Templates

### Prompt para Resumir e Extrair Intenção de E-mail de Suporte

```
Você é um analista de suporte ao cliente. Sua tarefa é ler o e-mail abaixo, resumir o problema central em uma frase e extrair a intenção principal do cliente (ex: "Solicitar reembolso", "Reportar bug", "Pedir informação", "Reclamação de produto"). Classifique também a urgência como "Baixa", "Média", "Alta".

E-mail:
"Prezados,

Comprei o 'Fone Bluetooth Xtreme Bass' de vocês na semana passada, pedido #BR12345. Chegou ontem, mas o lado esquerdo do fone não está emitindo som. Já tentei reiniciar, recarregar e parear novamente com meu celular, mas nada funciona. Estou bastante frustrado, pois esperava um produto de qualidade superior. Gostaria de saber como proceder para a troca ou devolução, pois não faz sentido ficar com um produto que não funciona corretamente.

Atenciosamente,
Carlos Eduardo"

Formato de saída:
Resumo: [Resumo do problema]
Intenção: [Intenção principal]
Urgência: [Urgência]
```

### Configuração de Webhook de Entrada para N8N (HTTP Request)

```json
{
  "nodes": [
    {
      "parameters": {
        "httpMethod": "POST",
        "path": "novo-lead-vendas",
        "responseMode": "lastNode",
        "options": {}
      },
      "name": "Webhook",
      "type": "n8n-nodes-base.webhook",
      "typeVersion": 1,
      "position": [250, 300],
      "id": "12345678-abcd-efgh-ijkl-mnopqrstuvwx",
      "webhookId": "7890abcdef-1234-5678-90ab-cdef12345678"
    }
  ],
  "connections": {}
}
```

---

## Checklist

- [ ] Definição clara do gatilho e dos dados de entrada esperados.
- [ ] Mapeamento completo de todos os campos de dados entre os sistemas envolvidos.
- [ ] Implementação de tratamento de erros para cada etapa crítica do fluxo.
- [ ] Configuração de logs e alertas para monitoramento proativo de falhas.
- [ ] Validação dos dados de entrada para evitar processamento de informações inválidas.
- [ ] Uso de credenciais de API seguras (tokens de ambiente, OAuth 2.0) e não hardcoded.
- [ ] Testes de ponta a ponta com cenários de sucesso e falha.
- [ ] Documentação do fluxo de automação e dos pontos de integração.
- [ ] Otimização para minimizar o número de requisições e processamento desnecessário.
- [ ] Plano de rollback ou recuperação em caso de falha crítica na automação.

---

## Métricas de Referência

| Métrica                 | Benchmark (Médio) | Meta (Otimizado) |
|-------------------------|-------------------|------------------|
| Tempo de Execução (s)   | 5-10 segundos     | < 2 segundos     |
| Taxa de Erro (%)        | 0.5% - 1%         | < 0.1%           |
| Economia de Horas (mês) | 20-40 horas/mês   | > 60 horas/mês   |
| ROI (Retorno sobre Investimento) | 150% - 300%       | > 400%           |
| Volume Processado (unidades/dia) | 500-1000          | > 2000           |

---

## Erros Comuns

1.  **Mapeamento de Dados Incorreto/Incompleto**: Fazer um mapeamento direto de `full_name` para `nome_completo` mas o sistema destino espera `first_name` e `last_name` separados. **Como evitar:** Utilize módulos de transformação de dados (ex: "Set" no Make, "Code" no N8N) para dividir, formatar ou concatenar campos antes de enviar para o sistema destino. Exemplo: `{{split(webhook.name, ' ')[0]}}` para `first_name` e `{{split(webhook.name, ' ')[1]}}` para `last_name`.
2.  **Tratamento de Erros Inadequado**: Falha em lidar com respostas de API que não sejam 200 OK, como 400 Bad Request, 401 Unauthorized ou 500 Internal Server Error, causando a interrupção abrupta do fluxo sem notificação. **Como evitar:** Implemente `Error Handlers` (Make.com) ou blocos `Try/Catch` (N8N) para capturar exceções. Em caso de erro, envie uma notificação para a equipe responsável (Slack/Email) e tente um `retry` com `exponential backoff` ou registre a falha para análise posterior, sem parar o fluxo principal.
3.  **Autenticação de API Expirada ou Inválida**: Tokens de acesso (Bearer, JWT) que expiram sem um mecanismo de refresh automático, ou chaves de API incorretas, resultando em falhas de conexão. **Como evitar:** Sempre que possível, utilize métodos de autenticação robustos como OAuth 2.0 que permitem a renovação automática de tokens. Para chaves estáticas, armazene-as em variáveis de ambiente ou cofres de segredos e configure alertas para quando um erro de autenticação persistir. Monitore a validade dos tokens.

---

## Dicas Avançadas

1.  **Idempotência em Webhooks**: Ao projetar webhooks de entrada, especialmente para eventos que podem ser disparados múltiplas vezes (ex: falhas de rede que causam retries), implemente um mecanismo para processar cada evento apenas uma vez. Use um `ID de transação` ou `ID de evento` único do payload para verificar se ele já foi processado antes de executar as ações principais. Isso evita duplicação de registros ou ações indesejadas.
2.  **Filas de Mensagens para Escalabilidade**: Para automações de alto volume ou com picos de tráfego, utilize filas de mensagens (ex: AWS SQS, RabbitMQ, Kafka) entre o gatilho e o processamento principal. O webhook apenas enfileira o evento, e outro processo consome da fila, desacoplando o recebimento do processamento e aumentando a resiliência e a capacidade de lidar com grandes cargas.
3.  **Processamento Assíncrono e Retries com Backoff Exponencial**: Para chamadas de API externas que podem ser lentas ou instáveis, configure o workflow para realizar chamadas assíncronas e implementar `retries` com `exponential backoff`. Se a primeira tentativa falhar, aguarde 1 segundo, tente novamente. Se falhar, aguarde 2 segundos, depois 4, 8, etc., até um limite máximo de tentativas. Isso reduz a carga no sistema externo e aumenta a chance de sucesso.
4.  **Versionamento e Controle de Mudanças**: Trate suas automações como código. Utilize ferramentas de controle de versão (Git) para N8N (com workflows em JSON/YAML) ou exporte regularmente os blueprints de Make/Zapier. Isso permite rastrear mudanças, reverter para versões anteriores e colaborar em equipe, garantindo a integridade e histórico do fluxo.
5.  **Monitoramento Detalhado com Métricas Personalizadas**: Além dos logs básicos, envie métricas personalizadas para ferramentas de APM (Application Performance Monitoring) como Datadog, New Relic ou Prometheus. Monitore o tempo de execução de cada módulo, o número de itens processados, a taxa de sucesso/falha por tipo de integração e o uso de recursos. Isso permite identificar gargalos e otimizar proativamente.