---
name: notification-system
description: "Notification System — Skill especializada para projetar, implementar e otimizar sistemas de notificação utilizando automação, APIs e IA."
license: MIT
metadata:
  version: 1.0.0
  author: Cafe Code AI
  category: 12-ia-automacao
  updated: 2026-03-01
risk: offensive
---

# Notification System

Esta skill capacita o Claude a atuar como um engenheiro de sistemas de notificação, desenhando e implementando fluxos robustos e multicanais usando ferramentas de automação, APIs de provedores e IA para personalização.

---

## Keywords

SMS, Email Transacional, Push Notification, Webhook, API Gateway, Message Queue, SMTP, Twilio, SendGrid, Make.com, N8N, Zapier, Firebase Cloud Messaging, Kafka, RabbitMQ, SQS, Automação, LGPD, GDPR, Opt-out.

---

## Quick Start

1.  **Mapear Canais Necessários**: Identifique se o sistema requer SMS (Twilio), Email (SendGrid/Mailgun) ou Push (Firebase Cloud Messaging).
2.  **Configurar Provedores de API**: Crie contas nos provedores selecionados e obtenha as chaves de API necessárias (API Key, Auth Token, Sender ID).
3.  **Desenhar Fluxo de Automação**: Esboce o fluxo lógico no Make.com, N8N ou Zapier, definindo os gatilhos (webhooks, schedules) e as ações (chamadas de API).
4.  **Implementar Conexões Iniciais**: Configure os módulos de conexão nos provedores de automação, inserindo as credenciais de API.
5.  **Testar Notificação Ponto-a-Ponto**: Dispare o gatilho e verifique o recebimento da notificação no canal de destino com dados reais.

---

## Core Workflows

### Workflow 1: Automação de Notificação de Compra com Confirmação Multicanal

Este workflow detalha a criação de um sistema automatizado que, após uma compra online, envia um e-mail de confirmação detalhado e um SMS com o status do pedido, utilizando um webhook, SendGrid e Twilio via Make.com.

**Cenário**: Um cliente finaliza uma compra em um e-commerce. O sistema deve enviar um e-mail de confirmação com os itens comprados e um SMS informando que o pedido foi recebido.

**Passos Detalhados**:

1.  **Configuração do Webhook no E-commerce**: Configure a plataforma de e-commerce (ex: Shopify, WooCommerce) para disparar um webhook POST para um endpoint do Make.com/N8N/Zapier sempre que um novo pedido for criado. O payload JSON esperado deve incluir `order_id`, `customer_email`, `customer_phone`, `items` (lista de produtos) e `total_amount`.

    Exemplo de Payload JSON (simulado):
    ```json
    {
      "event": "order_created",
      "order_id": "ORD-2024-00123",
      "customer_email": "joao.silva@email.com",
      "customer_phone": "+5511987654321",
      "shipping_address": "Rua Exemplo, 123, São Paulo, SP",
      "items": [
        {"product_id": "P001", "name": "Fone Bluetooth XZ1", "quantity": 1, "price": 149.90},
        {"product_id": "P002", "name": "Capa Smartphone Ultra", "quantity": 1, "price": 39.90}
      ],
      "total_amount": 189.80,
      "currency": "BRL",
      "timestamp": "2024-03-01T10:30:00Z"
    }
    ```

2.  **Recepção do Webhook no Make.com**: Configure um módulo "Webhooks > Custom webhook" no Make.com para escutar o POST do e-commerce. Copie o URL gerado.

3.  **Processamento dos Dados e Formatação para Email**:
    *   Use um módulo "Tools > Set multiple variables" para extrair os campos `customer_email`, `customer_phone`, `order_id` e `items` do payload do webhook.
    *   Para os `items`, utilize um módulo "Tools > Text aggregator" ou um script para formatar a lista de produtos em um HTML amigável para o e-mail.

    Exemplo de agregação de itens para HTML:
    ```html
    <ul>
    {% for item in items %}
      <li>{{ item.name }} ({{ item.quantity }}x) - R$ {{ item.price|number_format(2, ',', '.') }}</li>
    {% endfor %}
    </ul>
    ```

4.  **Envio de E-mail de Confirmação via SendGrid**:
    *   Adicione um módulo "SendGrid > Send an Email".
    *   Configure as credenciais SendGrid (API Key).
    *   **To**: `customer_email` (mapeado do webhook).
    *   **From**: `noreply@suaempresa.com.br`
    *   **Subject**: `Confirmação de Pedido #{{ order_id }} - Sua Empresa`
    *   **Content**: Utilize um template HTML pré-definido (ver seção Templates) e preencha os campos dinâmicos (`order_id`, `aggregated_items_html`, `total_amount`).

5.  **Envio de SMS de Status via Twilio**:
    *   Adicione um módulo "Twilio > Send an SMS".
    *   Configure as credenciais Twilio (Account SID, Auth Token).
    *   **To**: `customer_phone` (mapeado do webhook).
    *   **From**: `+1234567890` (seu número Twilio).
    *   **Message**: `Seu pedido #{{ order_id }} em Sua Empresa foi recebido! Acompanhe em: [link_rastreio].`

6.  **Gerenciamento de Erros e Logs**: Adicione tratamento de erros para falhas de envio (ex: Twilio/SendGrid retornam erro). Use um módulo "Tools > Router" para direcionar falhas para um módulo "Google Sheets > Add a Row" para registrar o erro e notificar a equipe interna via Slack (próximo workflow).

### Workflow 2: Sistema de Alerta de Monitoramento Crítico com Fallback

Este workflow cria um sistema de alerta para falhas críticas de infraestrutura, notificando a equipe via Slack e, como fallback, por e-mail, registrando todos os eventos em um sistema de log.

**Cenário**: Um serviço crítico (ex: API de pagamentos) está inoperante. A equipe de operações precisa ser alertada imediatamente via Slack e, se a notificação no Slack falhar, por e-mail.

**Passos Detalhados**:

1.  **Gatilho de Alerta (Webhook)**: Um sistema de monitoramento externo (ex: Uptime Robot, Prometheus Alertmanager) é configurado para disparar um webhook POST para um endpoint do N8N quando um serviço crítico atinge um estado de alerta.

    Exemplo de Payload JSON (simulado de Uptime Robot):
    ```json
    {
      "monitorID": "789012345",
      "monitorURL": "https://api.pagamentos.com/status",
      "monitorFriendlyName": "API Pagamentos Produção",
      "alertType": "2",
      "alertTypeDesc": "Down",
      "alertDetails": "HTTP status code 500 - Internal Server Error",
      "alertDateTime": 1678886400,
      "alertDateTime_ISO8601": "2024-03-01T10:00:00Z"
    }
    ```

2.  **Recepção do Webhook no N8N**: Configure um nó "Webhooks > Webhook" no N8N para receber o payload do sistema de monitoramento.

3.  **Preparação da Mensagem para Slack**:
    *   Use um nó "Set" para extrair `monitorFriendlyName`, `alertTypeDesc`, `alertDetails` e `monitorURL`.
    *   **Prompt para Claude para Resumir Alerta**: Use um nó "AI > Chat Completions" (se a integração estiver disponível ou via HTTP Request para API da Anthropic) para gerar uma mensagem concisa e acionável para o Slack.

    ```
    Prompt para Claude:
    "Gere uma mensagem concisa e urgente para o Slack sobre um alerta de sistema.
    O sistema: {{ $json.monitorFriendlyName }}
    Status: {{ $json.alertTypeDesc }}
    Detalhes: {{ $json.alertDetails }}
    Link de monitoramento: {{ $json.monitorURL }}

    Exemplo de Saída Esperada:
    🚨 ALERTA CRÍTICO: API Pagamentos Produção INOPERANTE!
    Detalhes: HTTP status code 500 - Internal Server Error.
    Verificar imediatamente: https://api.pagamentos.com/status"
    ```

4.  **Envio para Slack**:
    *   Adicione um nó "Slack > Send Message".
    *   Configure as credenciais Slack (Webhook URL ou Bot Token).
    *   **Channel**: `#canal-alertas-devops`
    *   **Text**: Use a saída gerada pelo Claude.

5.  **Fallback para Email (se Slack falhar)**:
    *   Adicione um nó "IF" após o nó "Slack" para verificar se a operação do Slack foi bem-sucedida.
    *   No ramo "False" (falha do Slack), adicione um nó "SendGrid > Send an Email".
    *   **To**: `equipe-ops@suaempresa.com.br`
    *   **From**: `alerts@suaempresa.com.br`
    *   **Subject**: `[URGENTE] Falha no Alerta Slack para: {{ $json.monitorFriendlyName }}`
    *   **Content**: Reutilize a mensagem gerada pelo Claude, adicionando um aviso sobre a falha no Slack.

6.  **Log de Eventos**:
    *   Independentemente do sucesso ou falha das notificações, adicione um nó "Google Sheets > Add Row" para registrar o evento.
    *   **Sheet Name**: `Logs de Alerta`
    *   **Columns**: `timestamp`, `monitor_name`, `alert_type`, `details`, `slack_status`, `email_status`. Popule com os dados do webhook e o status de cada tentativa de notificação.

---

## Templates

### Template Email de Confirmação de Pedido (HTML)

Este template é um exemplo real de e-mail transacional HTML, preenchido com dados de exemplo.

```html
<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <title>Confirmação de Pedido #ORD-2024-00123</title>
    <style>
        body { font-family: Arial, sans-serif; line-height: 1.6; color: #333; }
        .container { width: 100%; max-width: 600px; margin: 0 auto; padding: 20px; border: 1px solid #ddd; border-radius: 5px; }
        .header { background-color: #f8f8f8; padding: 10px 0; text-align: center; }
        .header img { max-width: 150px; }
        .content { padding: 20px 0; }
        .footer { text-align: center; font-size: 0.9em; color: #777; border-top: 1px solid #eee; padding-top: 10px; margin-top: 20px; }
        ul { list-style-type: none; padding: 0; }
        li { margin-bottom: 5px; }
        .total { font-weight: bold; font-size: 1.1em; text-align: right; margin-top: 15px; }
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <img src="https://www.suaempresa.com.br/logo.png" alt="Logo Sua Empresa">
            <h1>Obrigado pela sua compra!</h1>
        </div>
        <div class="content">
            <p>Olá João,</p>
            <p>Seu pedido <strong>#ORD-2024-00123</strong> foi recebido com sucesso e está sendo processado. Abaixo, os detalhes da sua compra:</p>

            <h3>Itens do Pedido:</h3>
            <ul>
                <li>Fone Bluetooth XZ1 (1x) - R$ 149,90</li>
                <li>Capa Smartphone Ultra (1x) - R$ 39,90</li>
            </ul>
            <p class="total">Total: R$ 189,80</p>

            <p>Você pode acompanhar o status do seu pedido a qualquer momento <a href="https://www.suaempresa.com.br/rastreio/ORD-2024-00123">clicando aqui</a>.</p>
            <p>Em breve, enviaremos atualizações sobre o envio. Se tiver qualquer dúvida, entre em contato conosco.</p>
            <p>Atenciosamente,<br>Equipe Sua Empresa</p>
        </div>
        <div class="footer">
            <p>&copy; 2024 Sua Empresa. Todos os direitos reservados.</p>
            <p><a href="https://www.suaempresa.com.br/privacidade">Política de Privacidade</a> | <a href="https://www.suaempresa.com.br/termos">Termos de Uso</a></p>
        </div>
    </div>
</body>
</html>
```

### Template de Prompt para Geração de Conteúdo de SMS

Este prompt é para o Claude gerar o corpo de uma mensagem SMS de forma concisa e útil, dados os parâmetros.

```
Prompt para Claude:
"Gere uma mensagem SMS de confirmação de pedido para um cliente.
O SMS deve ser conciso (máx. 160 caracteres), amigável e informativo.
Inclua o número do pedido e o nome do primeiro item do pedido.

Dados de entrada:
Order ID: ORD-2024-00123
Primeiro item: Fone Bluetooth XZ1

Exemplo de Saída Esperada:
Seu pedido #ORD-2024-00123 (Fone Bluetooth XZ1) foi recebido! Acompanhe em: [link_rastreio]. Sua Empresa agradece!"
```

---

## Checklist

- [x] Definir provedores de canal (Twilio para SMS, SendGrid para Email, Firebase Cloud Messaging para Push).
- [x] Implementar retry mechanisms com backoff exponencial para falhas temporárias de envio.
- [x] Configurar queues de mensagem (ex: RabbitMQ, AWS SQS) para desacoplar o envio e lidar com alto volume.
- [x] Monitorar taxas de entrega, abertura e cliques de todas as notificações.
- [x] Gerenciar opt-out/unsubscribe conforme regulamentação (LGPD, GDPR), integrando com sistemas de CRM.
- [x] Segmentar audiência para garantir que notificações sejam relevantes e personalizadas.
- [x] Testar cenários de falha, como API de provedor de notificação inoperante ou credenciais inválidas.
- [x] Implementar um sistema de log detalhado para cada notificação enviada (conteúdo, destinatário, status, erros).
- [x] Utilizar templates parametrizados para o conteúdo das notificações, facilitando a personalização e manutenção.
- [x] Definir limites de frequência (rate limiting) por usuário e canal para evitar spam e sobrecarga.
- [x] Criptografar dados sensíveis de clientes (ex: telefones, e-mails) em repouso e em trânsito.
- [x] Avaliar a latência de envio de notificações e otimizar gargalos.

---

## Métricas de Referência

| Métrica                         | Benchmark     | Meta          |
|---------------------------------|---------------|---------------|
| Taxa de Entrega Email (Transacional) | >95%          | >98%          |
| Taxa de Abertura Email (Transacional) | 60-80%        | >70%          |
| Latência de Envio SMS           | <5 segundos   | <2 segundos   |
| Taxa de Cliques Push Notification | 5-15%         | >8%           |
| Taxa de Erro API de Notificação | <0.1%         | <0.05%        |
| Taxa de Opt-out Email           | <0.5%         | <0.2%         |

---

## Erros Comuns

1.  **Credenciais de API Vencidas ou Inválidas**: Este erro ocorre quando as chaves de API para Twilio, SendGrid, etc., expiram, são revogadas ou estão incorretas.
    *   **Como evitar**: Implemente monitoramento de status das APIs de provedores. Use variáveis de ambiente nos sistemas de automação (Make/N8N) e configure alertas para credenciais que se aproximam do vencimento. Teste as credenciais regularmente em ambientes de desenvolvimento.
2.  **Payload Incorreto ou Dados Faltando**: Enviar um JSON/XML com estrutura errada ou campos obrigatórios ausentes para a API do provedor de notificação. Ex: `to` faltando no SendGrid, `body` vazio no Twilio.
    *   **Como evitar**: Valide a estrutura do payload antes de enviar para a API externa. Utilize JSON Schema para validar a entrada do webhook. Nos fluxos de automação, use nós de "Set" ou "Function" para garantir que todos os campos necessários estejam presentes e no formato correto antes da chamada da API.
3.  **Não Gerenciar Opt-out/Unsubscribe**: Continuar enviando notificações para usuários que solicitaram exclusão, resultando em penalidades (LGPD, GDPR) e blacklist de IP.
    *   **Como evitar**: Implemente uma lógica robusta de gerenciamento de opt-out. Integre o fluxo de notificação com seu sistema de CRM ou banco de dados de preferências do usuário para verificar o status de permissão antes de cada envio. Para e-mails, garanta que o cabeçalho `List-Unsubscribe` esteja presente e funcione.

---

## Dicas Avançadas

1.  **Notificações Transacionais vs. Marketing Separadas**: Mantenha os provedores e, idealmente, os IPs de envio de notificações transacionais (confirmações de compra, redefinições de senha) separados das notificações de marketing. Isso protege sua reputação de IP para mensagens críticas, evitando que e-mails importantes caiam na caixa de spam devido a campanhas de marketing com baixo engajamento ou alta taxa de reclamação.
2.  **Sistema de Fallback em Cascata Inteligente**: Desenvolva uma hierarquia de comunicação com fallback automático. Por exemplo, tente enviar uma notificação Push (mais rápida e barata). Se falhar ou não houver token, tente SMS. Se SMS falhar ou for muito caro para o contexto, envie um e-mail. Use condicionais (IF/Router) nos fluxos de automação para orquestrar essa lógica.
3.  **Personalização Dinâmica de Conteúdo com IA**: Utilize modelos de linguagem (Claude) para gerar ou adaptar dinamicamente o conteúdo das notificações com base no perfil do usuário, histórico de interação ou contexto atual. Por exemplo, um e-mail de "abandono de carrinho" pode ter um tom diferente e recomendar produtos complementares com base nos itens visualizados recentemente, gerado por um prompt.
4.  **A/B Testing Automatizado de Notificações**: Implemente A/B testing para otimizar o desempenho das notificações. Teste diferentes linhas de assunto de e-mail, CTAs em Push notifications ou horários de envio de SMS. Ferramentas como o N8N podem ser configuradas para dividir o tráfego e registrar os resultados, permitindo que a IA analise e sugira melhorias.
5.  **Gerenciamento de Preferências de Usuário Self-Service**: Permita que os usuários controlem suas próprias preferências de notificação através de um portal self-service. Isso inclui a escolha de canais (email, SMS, push), frequência (diária, semanal) e tipos de notificação (promoções, atualizações de pedidos). Integre este sistema de preferências diretamente com seus fluxos de automação para garantir conformidade e relevância.