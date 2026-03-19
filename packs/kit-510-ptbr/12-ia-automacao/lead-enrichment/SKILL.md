---
name: lead-enrichment
description: "Lead Enrichment — Skill especializada para lead enrichment"
license: MIT
metadata:
  version: 1.0.0
  author: Cafe Code AI
  category: 12-ia-automacao
  updated: 2026-03-01
---

# Lead Enrichment

Esta skill capacita o Claude a arquitetar, implementar e otimizar fluxos de automação para enriquecimento de dados de leads, utilizando APIs, chatbots e plataformas como Make/N8N/Zapier.

---

## Keywords

*   Enriquecimento de Leads
*   Automação de Marketing
*   Sales Enablement
*   APIs de Dados B2B
*   CRM Data Sync
*   Make.com Integração
*   N8N Fluxos
*   Zapier Automações
*   Webhooks
*   Qualificação de Leads IA
*   Data Cleansing
*   Inteligência de Vendas
*   Processamento de Leads

---

## Quick Start

1.  **Selecione uma Ferramenta de Enriquecimento:** Escolha um provedor de dados B2B (ex: Clearbit, Apollo.io, Hunter.io, ZoomInfo). Cadastre-se e obtenha sua chave de API para acesso programático e verifique os limites de requisição.
2.  **Identifique a Fonte de Leads:** Determine o ponto de entrada principal dos novos leads (ex: formulário de contato do website, landing page de campanha, integração com LinkedIn Sales Navigator) para configurar o gatilho da automação.
3.  **Mapeie os Campos Essenciais:** Liste os campos de dados que você já possui sobre o lead (ex: email, nome, URL da empresa) e os campos que você deseja enriquecer (ex: cargo, faturamento anual da empresa, número de funcionários, setor de atuação, tecnologias utilizadas).
4.  **Configure um Teste de API Manual:** Utilize uma ferramenta como Postman ou `curl` para realizar uma requisição de teste à API de enriquecimento com um email de lead real, analisando a estrutura da resposta JSON e a qualidade dos dados retornados.
    ```bash
    curl -X GET "https://person.clearbit.com/v2/people/find?email=joao.silva@exemplo.com.br" \
         -u "sk_YOUR_CLEARBIT_API_KEY:"
    ```
5.  **Prepare o CRM para Novos Campos:** Crie ou verifique a existência de campos personalizados em seu CRM (ex: HubSpot, Salesforce, Pipedrive) para armazenar os dados enriquecidos (ex: `c_cargo_enriquecido`, `c_faturamento_anual_empresa`).

---

## Core Workflows

### Workflow 1: Enriquecimento de Leads B2B em Tempo Real com Make.com

Este workflow detalha a automação do enriquecimento de leads imediatamente após a sua captação, usando um webhook para receber o lead e uma API de enriquecimento para buscar dados adicionais, atualizando um CRM.

**Passos Detalhados:**

1.  **Gatilho (Webhook de Formulário):** Um formulário de captação de leads (ex: Typeform, HubSpot Forms, Landing Page Builder) é configurado para enviar um POST request para um Webhook personalizado do Make.com sempre que um novo lead é submetido. O payload JSON deve conter, no mínimo, o `email` do lead.
    *   **Exemplo de Payload do Webhook (POST para `https://hook.us1.make.com/abcdefgh123456789`):**
        ```json
        {
          "email": "joao.silva@exemplo.com.br",
          "primeiroNome": "João",
          "sobrenome": "Silva",
          "origem": "Webinar_Q2_2024_Software"
        }
        ```
2.  **Módulo "Webhooks > Custom webhook" (Make.com):** No Make.com, adicione este módulo como o ponto de partida do seu cenário. O Make.com fornecerá um URL único para o webhook. Copie este URL e configure-o como o endpoint de envio no seu formulário de leads.
3.  **Módulo "HTTP > Make a request" (Enriquecimento de Pessoa - Clearbit):** Conecte o Webhook a um módulo "HTTP > Make a request". Configure-o para chamar a API de enriquecimento de pessoa (ex: Clearbit Person API).
    *   **URL:** `https://person.clearbit.com/v2/people/find`
    *   **Method:** `GET`
    *   **Headers:**
        *   `Authorization`: `Bearer sk_YOUR_CLEARBIT_API_KEY`
        *   `Content-Type`: `application/json`
    *   **Query String Parameters:**
        *   `email`: Mapeie para `{{1.email}}` (o email vindo do webhook).
    *   **Parse response:** Marque "Yes".
    *   **Tratamento de Erros:** Adicione um roteador (Router) após este módulo. Uma rota para sucesso (filtro `Status Code` igual a `200`) e outra para falha (filtro `Status Code` maior ou igual a `400`). Leads com falha podem ser enviados para uma planilha de revisão manual ou notificação via Slack.
4.  **Módulo "Text parser > Extract pattern" (Extrair Domínio):** Para o enriquecimento da empresa, você precisará do domínio do email. Use este módulo para extrair o domínio de `{{1.email}}` (ex: `exemplo.com.br` de `joao.silva@exemplo.com.br`).
    *   **Pattern:** `(?<=@)[^.]+\.[^.]+$`
    *   **Exemplo de Saída:** `exemplo.com.br`
5.  **Módulo "HTTP > Make a request" (Enriquecimento de Empresa - Clearbit):** Conecte o módulo de extração de domínio a um segundo módulo "HTTP > Make a request".
    *   **URL:** `https://company.clearbit.com/v2/companies/find`
    *   **Method:** `GET`
    *   **Headers:** `Authorization`: `Bearer sk_YOUR_CLEARBIT_API_KEY`
    *   **Query String Parameters:**
        *   `domain`: Mapeie para a saída do módulo "Text parser" (o domínio extraído).
6.  **Módulo do CRM (Ex: HubSpot CRM):** Conecte os módulos de enriquecimento (pessoa e empresa) a um módulo do seu CRM (ex: "HubSpot CRM > Create or Update a Contact").
    *   **Email:** Mapeie para `{{1.email}}`.
    *   **Propriedades a Atualizar:** Mapeie os dados enriquecidos da Clearbit para os campos correspondentes no CRM.
        *   `firstname`: `{{1.primeiroNome}}` (do webhook, se disponível) ou `{{CLEARBIT_PERSON.name.givenName}}`
        *   `lastname`: `{{1.sobrenome}}` (do webhook, se disponível) ou `{{CLEARBIT_PERSON.name.familyName}}`
        *   `jobtitle`: `{{CLEARBIT_PERSON.employment.title}}`
        *   `company`: `{{CLEARBIT_COMPANY.name}}`
        *   `industry`: `{{CLEARBIT_COMPANY.category.industry}}`
        *   `annual_revenue`: `{{CLEARBIT_COMPANY.metrics.annualRevenue}}`
        *   `num_employees`: `{{CLEARBIT_COMPANY.metrics.employees}}`
        *   `source`: `{{1.origem}}`
7.  **Ativação:** Teste o cenário end-to-end com múltiplos leads, valide os dados enriquecidos no CRM e ative o cenário no Make.com.

### Workflow 2: Qualificação de Leads Automatizada com IA (Claude) e Segmentação Dinâmica

Este workflow integra inteligência artificial para qualificar leads enriquecidos, categorizá-los e disparar ações de marketing ou vendas personalizadas.

**Passos Detalhados:**

1.  **Gatilho (Atualização de Contato no CRM - N8N):** Configure um módulo "HubSpot > Watch Contacts" (ou similar para outros CRMs) no N8N. Este gatilho será disparado quando um contato no HubSpot for criado ou atualizado, especificamente quando os campos `jobtitle` e `industry` (preenchidos pelo Workflow 1) não estiverem vazios.
    *   **Filtro:** `jobtitle IS NOT EMPTY` AND `industry IS NOT EMPTY`.
2.  **Coleta de Dados Enriquecidos:** O módulo do N8N extrai os dados relevantes do lead do CRM.
    *   **Exemplo de Dados Coletados pelo N8N:**
        ```json
        {
          "id": "lead_abc123",
          "email": "maria.gomes@techsolucoes.com",
          "firstName": "Maria",
          "lastName": "Gomes",
          "jobTitle": "Gerente de TI",
          "companyName": "Tech Soluções SA",
          "industry": "Tecnologia da Informação",
          "annualRevenue": 5000000,
          "numEmployees": 150
        }
        ```
3.  **Chamada à API da Anthropic (Claude):** Utilize um módulo "HTTP Request" no N8N para enviar os dados enriquecidos do lead para a API do Claude para avaliação.
    *   **URL:** `https://api.anthropic.com/v1/messages`
    *   **Method:** `POST`
    *   **Headers:**
        *   `x-api-key`: `YOUR_CLAUDE_API_KEY`
        *   `anthropic-version`: `2023-06-01`
        *   `content-type`: `application/json`
    *   **Body (JSON - usando expressões N8N para mapear campos):**
        ```json
        {
          "model": "claude-3-opus-20240229",
          "max_tokens": 500,
          "messages": [
            {
              "role": "user",
              "content": "Avalie o lead a seguir para determinar seu perfil de qualificação (MQL ou SQL) e sugerir a persona mais adequada. Use os critérios de um ICP para SaaS B2B que vende soluções de automação para empresas de médio e grande porte, com faturamento acima de R$3M e mais de 100 funcionários, buscando Gerentes ou Diretores de TI/Operações. Responda APENAS com um JSON contendo 'qualificacao', 'persona' e 'motivo'.\n\nDados do Lead:\nNome: {{ $json.firstName }} {{ $json.lastName }}\nCargo: {{ $json.jobTitle }}\nEmpresa: {{ $json.companyName }}\nIndústria: {{ $json.industry }}\nFaturamento Anual: R${{ $json.annualRevenue }}\nNúmero de Funcionários: {{ $json.numEmployees }}"
            }
          ]
        }
        ```
4.  **Processamento da Resposta da IA (N8N):** O Claude retornará um JSON dentro do campo `content` da resposta. Use um módulo "JSON" para parsear a string JSON e extrair os campos `qualificacao`, `persona` e `motivo`.
    *   **Exemplo de Resposta do Claude (após parsing):**
        ```json
        {
          "qualificacao": "SQL",
          "persona": "Tomador de Decisão de TI",
          "motivo": "O lead Maria Gomes, Gerente de TI na Tech Soluções (Indústria de TI, Faturamento R$5M, 150 funcionários), se encaixa perfeitamente no nosso ICP para soluções de automação, atuando como tomador de decisão direto."