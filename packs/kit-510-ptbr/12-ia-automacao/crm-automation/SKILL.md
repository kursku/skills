---
name: crm-automation
description: "Crm Automation — Skill especializada para crm automation"
license: MIT
metadata:
  version: 1.0.0
  author: Cafe Code AI
  category: 12-ia-automacao
  updated: 2026-03-01
---

# Crm Automation

Esta skill capacita o Claude a projetar, implementar e otimizar automações de CRM usando ferramentas como Make, N8N, Zapier, APIs e prompts de IA para elevar a eficiência operacional e a experiência do cliente.

---

## Keywords

Automação CRM, Lead Scoring, Nutrição de Leads, Customer Journey, Webhook CRM, API Pipedrive, API HubSpot, Make, N8N, Zapier, Prompt Engenharia, Segmentação de Clientes, Automação de Vendas, Automação de Suporte, Experiência do Cliente.

---

## Quick Start

1.  **Configurar Webhook de Novo Lead (RD Station para Make.com)**: No RD Station, configure um webhook para enviar dados de novas conversões (formulários, landing pages) para um URL de webhook customizado do Make.com.
2.  **Mapear Dados no Módulo Inicial (Make.com)**: No Make, use o módulo "Webhooks > Custom webhook" e execute-o uma vez com um lead de teste para mapear automaticamente campos como `name`, `email`, `company_name`, `job_title` do payload do RD Station.
3.  **Implementar Filtro de Lead Scoring Básico (Make.com)**: Adicione um filtro após o webhook para qualificar leads. Por exemplo, `job_title` CONTAINS "Diretor" OR `company_name` CONTAINS "S.A." AND `email` DOES NOT CONTAIN "gmail.com".
4.  **Criar Contato e Negócio no CRM (Pipedrive API)**: Para leads qualificados, use o módulo "Pipedrive > Create a Person" com os dados mapeados e, em seguida, "Pipedrive > Create a Deal" associando-o à pessoa criada e definindo um estágio inicial (ex: "Novo Lead Qualificado").
5.  **Acionar E-mail de Boas-vindas Personalizado (SendGrid API)**: Após a criação no CRM, adicione um módulo "SendGrid > Send an Email" com o `email` do lead, `subject` como "Bem-vindo(a), {{1.name}} à nossa comunidade!" e um `content` que inclua o nome da empresa do lead.

---

## Core Workflows

### Workflow 1: Automação de Qualificação e Distribuição de Leads B2B com IA

Este fluxo automatiza a recepção de leads, sua qualificação por IA e a distribuição para o CRM, garantindo que apenas leads ICP (Ideal Customer Profile) cheguem aos vendedores, com personalização inicial.

**Ferramenta Principal:** Make.com (ou N8N)

**Passos Detalhados:**

1.  **Gatilho: Novo Contato via Formulário do Website (HubSpot Forms)**
    *   **Módulo:** `Webhooks > Custom webhook` (Make.com)
    *   **Configuração:** Crie um novo webhook no Make.com e copie o URL. No HubSpot, vá em `Automações > Workflows`, crie um novo workflow baseado em formulário e adicione uma ação "Disparar Webhook" (GET ou POST) para o URL do Make, enviando todas as propriedades do contato.
    *   **Exemplo de Payload Recebido (Make.com):**
        ```json
        {
          "objectType": "CONTACT",
          "objectId": 123456,
          "propertyName": "email",
          "propertyValue": "carlos.silva@solucoesdigitais.com.br",
          "changeSource": "FORM",
          "properties": {
            "email": "carlos.silva@solucoesdigitais.com.br",
            "firstname": "Carlos",
            "lastname": "Silva",
            "company": "Soluções Digitais Ltda.",
            "jobtitle": "Gerente de Projetos",
            "phone": "+551199887766",
            "lifecyclestage": "lead"
          }
        }
        ```
2.  **Módulo: Classificação de Perfil e Sugestão de Ações (OpenAI GPT-4 via HTTP)**
    *   **Função:** Enviar os dados do lead para a API do OpenAI para classificar se o lead é um ICP e sugerir tópicos para o primeiro contato.
    *   **Módulo:** `HTTP > Make a request`
    *   **Configuração:**
        *   **URL:** `https://api.openai.com/v1/chat/completions`
        *   **Method:** `POST`
        *   **Headers:** `Authorization: Bearer {{YOUR_OPENAI_API_KEY}}`, `Content-Type: application/json`
        *   **Body (JSON):**
            ```json
            {
              "model": "gpt-4o",
              "messages": [
                {"role": "system", "content": "Você é um especialista em qualificação de leads B2B. Avalie os leads com base no perfil e sugira personalizações."},
                {"role": "user", "content": "Analise o lead com Nome: {{1.properties.firstname}} {{1.properties.lastname}}, Empresa: {{1.properties.company}}, Cargo: {{1.properties.jobtitle}}. Nosso ICP são empresas de tecnologia com mais de 50 funcionários e cargos de gerência/diretoria. Classifique o lead como 'ICP' ou 'Não ICP'. Se ICP, sugira 3 tópicos de personalização para o primeiro e-mail de prospecção, focando em como nossa solução de automação de processos pode resolver um problema específico da área de TI. Se Não ICP, indique o motivo. Retorne em formato JSON."},
                {"role": "assistant", "content": "{\n  \"classificacao\": \"ICP\",\n  \"motivo_desqualificacao\": \"N/A\",\n  \"topicos_personalizacao\": [\n    \"Desafios na integração de sistemas legados e modernos para otimização de fluxos de trabalho.\",\n    \"Aumento da eficiência operacional em projetos de TI através da automação inteligente.\",\n    \"Melhoria na visibilidade e controle sobre os processos de desenvolvimento e entrega.\"\n  ]\n}"}
              ],
              "response_format": {"type": "json_object"}
            }
            ```
3.  **Módulo: Roteador (Filtro Condicional)**
    *   **Função:** Direcionar o fluxo com base na classificação da IA.
    *   **Módulo:** `Router`
    *   **Filtro 1 (Rota ICP):** `{{2.choices[0].message.content.classificacao}}` (parsee o JSON) `Equal to` `ICP`
    *   **Filtro 2 (Rota Não ICP):** `{{2.choices[0].message.content.classificacao}}` (parsee o JSON) `Equal to` `Não ICP`
4.  **Rota ICP: Criar/Atualizar Contato e Negócio (Pipedrive API)**
    *   **Módulo:** `Pipedrive > Create a Person`
        *   `Name:` `{{1.properties.firstname}} {{1.properties.lastname}}`
        *   `Email:` `{{1.properties.email}}`
        *   `Phone:` `{{1.properties.phone}}`
        *   `Organization:` `{{1.properties.company}}`
    *   **Módulo:** `Pipedrive > Create a Deal`
        *   `Title:` `Novo Negócio - {{1.properties.company}}`
        *   `Person:` `{{ID da pessoa criada no módulo anterior}}`
        *   `Stage:` `1 (Novo Lead Qualificado)`
        *   `Value:` `0`
    *   **Módulo:** `Pipedrive > Create an Activity`
        *   `Subject:` `Primeiro Contato - {{1.properties.company}}`
        *   `Type:` `call`
        *   `Due Date:` `{{addHours(now; 24)}}` (para agendar para o dia seguinte)
        *   `Assigned To:` `{{ID do vendedor responsável (ex: via Round Robin ou lógica de território)}}`
        *   `Note:` `Lead qualificado por IA. Tópicos sugeridos para conversa: {{2.choices[0].message.content.topicos_personalizacao}}`
5.  **Rota Não ICP: Enviar E-mail de Desqualificação (SendGrid API)**
    *   **Módulo:** `SendGrid > Send an Email`
    *   **Configuração:**
        *   `To:` `{{1.properties.email}}`
        *   `From:` `marketing@suaempresa.com.br`
        *   `Subject:` `Agradecemos seu interesse, {{1.properties.firstname}}!`
        *   `Content (HTML):`
            ```html
            <p>Olá {{1.properties.firstname}},</p>
            <p>Agradecemos muito seu interesse em nossos serviços. Recebemos seu contato, mas após uma análise inicial, identificamos que seu perfil de <b>{{1.properties.company}}</b> no momento não se alinha diretamente com nossa oferta principal devido a: <b>{{2.choices[0].message.content.motivo_desqualificacao}}</b>.</p>
            <p>De qualquer forma, adoraríamos que você explorasse nossos recursos gratuitos em <a href="https://www.suaempresa.com.br/blog">nosso blog</a>.</p>
            <p>Atenciosamente,<br>Equipe Sua Empresa</p>
            ```

### Workflow 2: Automação de Notificação de Churn Potencial e Reconexão

Este workflow detecta clientes com baixo engajamento no produto, busca seus dados no CRM, avalia o risco de churn com lógica customizada e aciona ações proativas para o CSM ou e-mails de reconexão.

**Ferramenta Principal:** N8N (ou Make.com)

**Passos Detalhados:**

1.  **Gatilho: Evento de Baixo Engajamento (Webhook de Product Analytics)**
    *   **Módulo:** `Webhooks > Webhook` (N8N)
    *   **Configuração:** Crie um webhook no N8N. Seu sistema de product analytics (ex: Mixpanel, Amplitude, ou um sistema interno) deve enviar um evento POST para este URL quando um usuário atingir um limite de inatividade (ex: 15 dias sem login).
    *   **Exemplo de Payload Recebido (N8N):**
        ```json
        {
          "user_id": "usr_98765",
          "last_activity_date": "2024-07-15T14:30:00Z",
          "plan_type": "Enterprise",
          "account_id": "acc_112233"
        }
        ```
2.  **Módulo: Buscar Dados do Cliente (HubSpot CRM API)**
    *   **Função:** Usar o `user_id` ou `account_id` para buscar o contato correspondente no HubSpot e obter informações como `email`, `firstname`, `lastname`, `hs_owner_id` (ID do CSM).
    *   **Módulo:** `HTTP Request`
    *   **Configuração:**
        *   **Method:** `GET`
        *   **URL:** `https://api.hubapi.com/crm/v3/objects/contacts?email={{$json.user_id}}&properties=firstname,lastname,email,hs_owner_id,hs_object_id` (assumindo que `user_id` é o email, ou ajuste a propriedade de busca)
        *   **Headers:** `Authorization: Bearer {{YOUR_HUBSPOT_API_KEY}}`
        *   **JSON Parse:** Marque para parsear a resposta.
3.  **Módulo: Avaliação de Risco de Churn (Code Node - JavaScript)**
    *   **Função:** Calcular o nível de risco de churn com base na data da última atividade e no plano do cliente.
    *   **Módulo:** `Code` (N8N)
    *   **Código JavaScript:**
        ```javascript
        const lastActivityDate = new Date($item(0).json.last_activity_date);
        const currentDate = new Date();
        const diffTime = Math.abs(currentDate - lastActivityDate);
        const diffDays = Math.ceil(diffTime / (1000 * 60 * 60 * 24)); // Diferença em dias

        const planType = $item(0).json.plan_type;
        let riskLevel = "Baixo";
        let actionSuggestion = "N/A";

        if (planType === "Enterprise" && diffDays > 20) {
            riskLevel = "Alto";
            actionSuggestion = "Agendar call de reconexão urgente, oferecer consultoria de uso avançado.";
        } else if (planType === "Pro" && diffDays > 30) {
            riskLevel = "Médio";
            actionSuggestion = "Enviar e-mail de dicas de uso personalizado, verificar uso de funcionalidades chave.";
        } else if (planType === "Basic" && diffDays > 45) {
            riskLevel = "Médio";
            actionSuggestion = "Enviar e-mail de 'sentimos sua falta' com novos recursos.";
        }

        return [{
            json: {
                ...$item(0).json, // Mantém os dados originais do webhook
                ...$item(1).json.results[0].properties, // Adiciona propriedades do HubSpot
                riskLevel: riskLevel,
                daysInactive: diffDays,
                actionSuggestion: actionSuggestion
            }
        }];
        ```
4.  **Módulo: Roteador (IF/Else)**
    *   **Função:** Criar ramificações para diferentes níveis de risco.
    *   **Módulo:** `IF`
    *   **Condição 1 (Rota Alto Risco):** `{{$json.riskLevel}}` `is equal to` `Alto`
    *   **Condição 2 (Rota Médio Risco):** `{{$json.riskLevel}}` `is equal to` `Médio`
5.  **Rota Alto Risco:**
    *   **Módulo: Notificar CSM no Slack (Slack API)**
        *   **Módulo:** `Slack >