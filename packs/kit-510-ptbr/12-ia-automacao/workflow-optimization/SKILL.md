---
name: workflow-optimization
description: "Workflow Optimization — Skill especializada para otimização de fluxos de trabalho através de IA e automação"
license: MIT
metadata:
  version: 1.0.0
  author: Cafe Code AI
  category: 12-ia-automacao
  updated: 2026-03-01
risk: safe
---

# Workflow Optimization

Esta skill capacita o Claude a projetar, implementar e otimizar fluxos de trabalho utilizando chatbots, plataformas de automação (Make/N8N/Zapier), APIs e prompts avançados, transformando processos manuais em operações eficientes e inteligentes.

---

## Keywords

Automação de Processos, Orquestração de Fluxos, Integração de APIs, Chatbots Inteligentes, LLMs (Large Language Models), Webhooks, Make.com, N8N, Zapier, Otimização de Prompt, Tratamento de Exceções, Monitoramento de Automação, Governança de Automação, BPMN, Integração Contínua, RAG (Retrieval Augmented Generation).

---

## Quick Start

1.  **Mapear o processo "as-is"**: Crie um diagrama de fluxo de dados ou um mapa de processo (ex: BPMN) para visualizar todas as etapas manuais, pontos de decisão e sistemas envolvidos em um fluxo de trabalho existente.
2.  **Analisar pontos de automação**: Identifique tarefas repetitivas, baseadas em regras claras, com alto volume e que não exigem julgamento humano complexo, como extração de dados de e-mails ou entrada em sistemas, para potenciais de automação.
3.  **Prototipar integração básica**: Utilize Make/N8N/Zapier para conectar duas ou três ferramentas essenciais do fluxo (ex: Formulário -> Planilha -> Notificação) e testar a comunicação entre elas.
4.  **Implementar monitoramento inicial**: Configure logs de execução e alertas básicos (ex: para Slack ou e-mail) para acompanhar o status da automação e identificar falhas precocemente.

---

## Core Workflows

### Workflow 1: Automação de Qualificação de Leads via Chatbot e CRM

Este fluxo automatiza a qualificação inicial de leads, reduzindo o tempo de resposta e garantindo que leads mais promissores cheguem rapidamente à equipe de vendas.

*   **Contexto**: Um novo lead preenche um formulário de contato no site ou inicia uma conversa via chatbot.
*   **Passo 1: Captura do Lead e Ativação do Webhook**. Um formulário (ex: Typeform, Google Forms) ou chatbot envia os dados do lead para um webhook configurado no Make.com ou N8N.
    *   **Exemplo de Webhook URL (Make.com)**: `https://hook.us1.make.com/abcdefghijklmn`
    *   **Exemplo de Payload de Entrada (JSON)**:
        ```json
        {
          "nome": "João Silva",
          "email": "joao.silva@empresa.com",
          "telefone": "+55 (11) 98765-4321",
          "empresa": "Tech Solutions Ltda.",
          "mensagem_inicial": "Gostaria de saber mais sobre as soluções de IA para otimização de processos."
        }
        ```
*   **Passo 2: Qualificação via LLM (Claude)**. O cenário de automação envia a mensagem e dados iniciais do lead para a API do Claude com um prompt específico para qualificação e extração de intenção.
    *   **Exemplo de Requisição para Claude (JSON payload)**:
        ```json
        {
          "model": "claude-3-opus-20240229",
          "messages": [
            {
              "role": "user",
              "content": "Analise o seguinte perfil de lead e classifique-o como 'Quente', 'Morno' ou 'Frio' para um serviço de consultoria em IA. Extraia o nome da empresa, o cargo (se implícito) e o interesse principal. Retorne um JSON. \nLead: 'Olá, meu nome é João Silva da Tech Solutions Ltda. Meu e-mail é joao.silva@empresa.com. Gostaria de saber mais sobre as soluções de IA para otimização de processos.'"
            }
          ],
          "max_tokens": 500,
          "temperature": 0.2
        }
        ```
    *   **Exemplo de Output do Claude (JSON)**:
        ```json
        {
          "classificacao": "Quente",
          "empresa": "Tech Solutions Ltda.",
          "cargo": "Não especificado (potencial tomador de decisão)",
          "interesse_principal": "soluções de IA para otimização de processos"
        }
        ```
*   **Passo 3: Atualização do CRM**. O resultado da qualificação (JSON) é mapeado e enviado via API para o sistema CRM (ex: Salesforce, HubSpot, Pipedrive).
    *   **Exemplo de Mapeamento (Make.com/N8N)**: `Lead Status` <- `classificacao`, `Company Name` <- `empresa`, `Custom Field: Interest` <- `interesse_principal`.
    *   **Exemplo de JSON para Pipedrive API (criar pessoa e oportunidade)**:
        ```json
        {
          "name": "João Silva",
          "email": [{"label": "work", "value": "joao.silva@empresa.com", "primary": true}],
          "phone": [{"label": "work", "value": "+5511987654321", "primary": true}],
          "org_name": "Tech Solutions Ltda.",
          "custom_fields": {"classificacao_lead": "Quente", "interesse_ia": "Otimização de Processos"},
          "stage_id": 1, // Ex: ID do estágio "Lead Qualificado"
          "title": "Oportunidade - IA para Otimização de Processos"
        }
        ```
*   **Passo 4: Notificação e Atribuição de Vendas**. Uma notificação é enviada ao time de vendas via Slack ou e-mail, atribuindo o lead qualificado ao vendedor responsável, com um link direto para o registro no CRM. Isso acelera o contato inicial e o follow-up.

### Workflow 2: Otimização de Respostas de Suporte com IA e Base de Conhecimento (RAG)

Este fluxo melhora a eficiência do suporte ao cliente, fornecendo respostas rápidas e precisas, reduzindo o tempo de resolução e o volume de tickets.

*   **Contexto**: Um cliente envia uma dúvida para o suporte via chat, e-mail ou plataforma de tickets.
*   **Passo 1: Captura da Mensagem de Suporte**. Um webhook no Make.com/N8N recebe a mensagem do cliente de uma plataforma de suporte (ex: Zendesk, Intercom, Freshdesk) ou do sistema de e-mail.
    *   **Exemplo de Payload de Zendesk (simplificado)**:
        ```json
        {
          "ticket_id": "TKT-2024-07-29-001",
          "subject": "Dúvida sobre valor da fatura",
          "description": "Recebi minha fatura de julho e o valor está diferente do esperado. Poderiam verificar?",
          "requester_email": "cliente@email.com",
          "status": "novo"
        }
        ```
*   **Passo 2: Busca na Base de Conhecimento (RAG)**. A descrição do problema do cliente é usada para buscar informações relevantes em uma base de conhecimento estruturada (ex: Airtable, Notion, Google Sheets, ou um banco de dados vetorial) via API.
    *   **Exemplo de Requisição para Airtable (buscar artigos por palavra-chave)**:
        `GET https://api.airtable.com/v0/appXYZ/KB_Artigos?filterByFormula=SEARCH('fatura', {Conteudo_Artigo})`
    *   **Exemplo de Resultado da Busca**:
        ```
        Conteúdo Artigo 1: "Faturas são geradas no dia 5 de cada mês. Alterações podem ocorrer devido a consumo extra, upgrades de plano ou serviços adicionais. Para contestar uma fatura, por favor, envie um e-mail para financeiro@empresa.com com o número da fatura e o motivo da contestação."
        Conteúdo Artigo 2: "Como verificar seu consumo: Acesse o painel do cliente, seção 'Uso e Consumo'."
        ```
*   **Passo 3: Geração de Resposta Otimizada com Claude**. A mensagem original do cliente e os trechos relevantes da base de conhecimento são enviados para a API do Claude para gerar uma resposta útil, empática e acionável.
    *   **Exemplo de Prompt para Claude (JSON payload)**:
        ```json
        {
          "model": "claude-3-sonnet-20240229",
          "messages": [
            {
              "role": "user",
              "content": "Contexto da Base de Conhecimento:\n'Artigo Faturas: Faturas são geradas no dia 5 de cada mês. Alterações podem ocorrer devido a consumo extra, upgrades ou serviços adicionais. Para contestar, envie email para financeiro@empresa.com.'\n'Artigo Consumo: Acesse o painel do cliente, seção 'Uso e Consumo'.' \n\nMensagem do Cliente: 'Minha fatura veio com um valor inesperado este mês. Poderiam verificar?'\n\nCom base no contexto fornecido, elabore uma resposta útil e empática para o cliente sobre a divergência na fatura, orientando sobre como entender o valor e como proceder para contestar, se necessário. Use um tom profissional e direto."
            }
          ],
          "max_tokens": 800,
          "temperature": 0.5
        }
        ```
    *   **Exemplo de Output do Claude**:
        ```
        Prezado(a) cliente, compreendo sua preocupação com o valor da fatura de julho. Nossas faturas são geradas no dia 5 de cada mês, e alterações podem ocorrer devido a consumo extra, upgrades de plano ou serviços adicionais.

        Para verificar o detalhamento do seu consumo, você pode acessar o painel do cliente na seção 'Uso e Consumo'.

        Caso após essa verificação a divergência persista e deseje contestar a fatura, por favor, envie um e-mail para financeiro@empresa.com, mencionando o número da sua fatura e o motivo da contestação. Nossa equipe financeira estará pronta para auxiliá-lo(a).
        ```
*   **Passo 4: Envio da Resposta**. A resposta gerada pelo Claude é enviada de volta ao cliente pela plataforma de suporte ou e-mail, ou apresentada ao agente de suporte como uma sugestão de resposta.
*   **Passo 5: Feedback e Iteração (Opcional)**. Um módulo permite que o agente de suporte forneça feedback sobre a qualidade da resposta gerada pela IA, alimentando um processo de ajuste do prompt ou da base de conhecimento para melhorias contínuas.

---

## Templates

### Prompt para Extração Estruturada de Dados

```
Você é um assistente especialista em extração de informações. Sua tarefa é extrair os seguintes campos de qualquer texto fornecido e retornar o resultado em formato JSON. Se um campo não for encontrado, retorne `null`.

Campos a Extrair:
- `nome_completo`: Nome completo da pessoa.
- `email`: Endereço de email.
- `telefone`: Número de telefone (formatado como +XX (XX) XXXXX-XXXX).
- `empresa`: Nome da empresa.
- `cargo`: Cargo da pessoa na empresa.
- `interesse_principal`: O principal tópico ou serviço de interesse mencionado.
- `urgencia`: Nível de urgência da solicitação (Baixa, Média, Alta), se detectável.

Exemplo de Texto:
"Olá, sou Pedro Rocha, da Inovatech Soluções. Meu e-mail é pedro.rocha@inovatech.com.br e meu celular é (11) 98765-4321. Tenho grande interesse em discutir a implementação de soluções de automação de processos. Precisamos disso o mais rápido possível!"

Exemplo de Saída JSON Esperada:
```json
{
  "nome_completo": "Pedro Rocha",
  "email": "pedro.rocha@inovatech.com.br",
  "telefone": "+55 (11) 98765-4321",
  "empresa": "Inovatech Soluções",
  "cargo": null,
  "interesse_principal": "implementação de soluções de automação de processos",
  "urgencia": "Alta"
}
```

Agora, extraia os dados do seguinte texto:
"Preciso de informações sobre a integração da API. Meu nome é Mariana Costa, trabalho na startup 'AgilizaTI'. Meu contato é mariana.c@agilizati.com.br. Gostaria de entender melhor a cobrança de serviços de IA, mas não é urgente."
```

### Configuração de Webhook de Entrada (Exemplo para Make.com/N8N)

```json
{
  "event": "novo_contato_site",
  "timestamp": "2024-07-29T14:45:00Z",
  "data": {
    "id_formulario": "FORM-WEB-001",
    "nome_completo": "Fernanda Santos",
    "email": "fernanda.santos@exemplo.com",
    "telefone": "+55 (31) 91234-5678",
    "empresa": "Soluções Criativas S.A.",
    "cargo": "Gerente de Marketing",
    "assunto": "Proposta de parceria para conteúdo de IA",
    "mensagem": "Buscamos empresas parceiras para desenvolver conteúdo inovador sobre IA e automação para nosso blog e redes sociais.",
    "origem_trafego": "Google Ads - IA",
    "preferencia_contato": "email"
  },
  "headers": {
    "Content-Type": "application/json",
    "User-Agent": "LeadCaptureSystem/1.0",
    "X-Api-Key": "sua_chave_api_aqui"
  }
}
```

---

## Checklist

- [X] Mapeamento detalhado do processo "as-is" (BPMN ou diagrama de fluxo).
- [X] Definição clara dos gatilhos, condições