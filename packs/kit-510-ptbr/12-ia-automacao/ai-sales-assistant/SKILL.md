---
name: ai-sales-assistant
description: "Ai Sales Assistant — Skill especializada para ai sales assistant"
license: MIT
metadata:
  version: 1.0.0
  author: Cafe Code AI
  category: 12-ia-automacao
  updated: 2026-03-01
risk: safe
---

# Ai Sales Assistant

Esta skill capacita o Claude a configurar e gerenciar assistentes de vendas baseados em IA, otimizando qualificação de leads, personalização de comunicação e automação de agendamentos para equipes de vendas.

---

## Keywords

Automação de Vendas, Qualificação de Leads, AI Generativa, CRM Automation, Outreach Personalizado, Webhooks Make, N8N Workflows, API LLM, Agendamento Inteligente, Sales Enablement, Lead Scoring AI, Conversational AI Sales.

---

## Quick Start

1.  **Configurar Credenciais de API**: Obtenha chaves de API para seu CRM (Pipedrive, HubSpot), plataforma de e-mail (SendGrid, Mailgun) e LLM (Anthropic Claude, OpenAI).
2.  **Mapear Campos de Lead**: Identifique os campos cruciais no seu CRM (Nome, Empresa, Cargo, Segmento, Necessidade) que serão usados para alimentar o prompt de qualificação da IA.
3.  **Criar Webhook de Entrada**: Configure um webhook em sua ferramenta de automação (Make/N8N) para receber dados de novos leads do seu formulário web ou sistema de captação.
4.  **Desenhar Prompt Inicial de Qualificação**: Elabore um prompt que instrua a LLM a qualificar um lead com base nos dados recebidos e critérios de ICP (Ideal Customer Profile) específicos.
5.  **Testar Fluxo End-to-End**: Envie um lead de teste através do seu formulário, monitore o processamento pela automação, a resposta da LLM e a atualização no CRM.

---

## Core Workflows

### Workflow 1: Qualificação de Leads Inbound com IA e Atualização de CRM

Este workflow automatiza a análise e qualificação de leads recém-capturados, utilizando uma LLM para determinar o "fit" e o "interesse" do lead, atualizando o CRM e notificando a equipe de vendas.

**Passos Detalhados:**

1.  **Captura de Lead e Acionamento de Webhook:**
    *   Um novo lead preenche um formulário no site (ex: formulário do Typeform, HubSpot Forms).
    *   O envio do formulário dispara um webhook POST para um endpoint configurado no Make.com ou N8N.
    *   **Exemplo de Payload de Webhook (JSON):**
        ```json
        {
          "nome": "Ana Silva",
          "email": "ana.silva@techsolutions.com",
          "empresa": "Tech Solutions Ltda.",
          "cargo": "Gerente de TI",
          "telefone": "+5511987654321",
          "mensagem": "Buscamos uma solução para otimizar nossos processos de DevOps e reduzir custos."
        }
        ```

2.  **Processamento no Make/N8N e Chamada à LLM:**
    *   O módulo de webhook no Make/N8N recebe o payload.
    *   Os dados do lead são formatados e enviados para a API da LLM (ex: Claude 3.5 Sonnet).
    *   **Configuração de Chamada HTTP (Make.com - Módulo "Make a request"):**
        *   **URL:** `https://api.anthropic.com/v1/messages`
        *   **Method:** `POST`
        *   **Headers:**
            *   `x-api-key`: `{{sua_chave_api_anthropic}}`
            *   `anthropic-version`: `2023-06-01`
            *   `content-type`: `application/json`
        *   **Body (JSON):**
            ```json
            {
              "model": "claude-3-5-sonnet-20240620",
              "max_tokens": 500,
              ""messages": [
                {
                  "role": "user",
                  "content": "Analise o seguinte lead e determine se ele é um SQL (Sales Qualified Lead) para nossa empresa, que oferece soluções SaaS para otimização de DevOps. Nossos critérios de ICP incluem: empresas de tecnologia com mais de 50 funcionários, buscando redução de custos ou melhoria de eficiência em TI. O lead deve ter cargo gerencial ou superior em TI. Retorne um JSON com 'qualificado': true/false, 'motivo': 'texto', 'score': 1-10, 'proxima_acao': 'texto'.\n\nDados do Lead:\nNome: {{1.nome}}\nEmail: {{1.email}}\nEmpresa: {{1.empresa}}\nCargo: {{1.cargo}}\nMensagem: {{1.mensagem}}"
                }
              ]
            }
            ```
        *   *(Onde `{{1.nome}}`, etc., são variáveis do webhook de entrada)*

3.  **Análise da Resposta da LLM e Tomada de Decisão:**
    *   A LLM retorna um JSON com a qualificação.
    *   O módulo seguinte no Make/N8N parseia a resposta e usa um roteador (router) ou condicional para direcionar o fluxo.
    *   **Exemplo de Resposta da LLM:**
        ```json
        {
          "qualificado": true,
          "motivo": "A empresa Tech Solutions atua no segmento de tecnologia, o cargo de Gerente de TI é decisor e a mensagem indica busca por otimização de DevOps, alinhado ao nosso ICP.",
          "score": 8,
          "proxima_acao": "Enviar e-mail de apresentação de caso de sucesso e agendar demonstração."
        }
        ```

4.  **Atualização do CRM e Notificação:**
    *   **Lead Qualificado (qualificado: true):**
        *   Módulo "Update a Person/Deal" no Pipedrive ou HubSpot para marcar o lead como "SQL", atualizar um campo customizado "AI Qualification Score" e adicionar notas da LLM.
        *   Módulo "Send a Message" no Slack ou Email para o time de vendas com os detalhes do lead e a recomendação da LLM.
        *   **Exemplo de Mensagem Slack:**
            ```
            🔥 NOVO SQL QUALIFICADO POR AI!
            Lead: Ana Silva (Tech Solutions Ltda. - Gerente de TI)
            Email: ana.silva@techsolutions.com
            Score AI: 8/10
            Motivo: Alinhado com ICP em tecnologia, busca otimização DevOps.
            Próxima Ação Sugerida: Enviar caso de sucesso e agendar demo.
            Link CRM: [Link para o lead no Pipedrive]
            ```
    *   **Lead Não Qualificado (qualificado: false):**
        *   Módulo "Update a Person" no CRM para marcar o lead como "Não Qualificado pela AI" e direcioná-lo para uma trilha de nutrição de marketing.
        *   Opcional: Enviar um e-mail automático de nutrição genérico.

### Workflow 2: Geração de E-mails de Prospecção Personalizados e Agendamento Automatizado

Este workflow utiliza a IA para criar e-mails de prospecção altamente personalizados, baseados em dados do lead, e automatiza o processo de agendamento de reuniões.

**Passos Detalhados:**

1.  **Acionamento Pós-Qualificação ou Manual:**
    *   O workflow é acionado quando um lead atinge um estágio específico no CRM (ex: "SQL - Pronto para Contato") ou por um acionamento manual de um vendedor.
    *   Módulo "Watch Deals/Persons" no Make/N8N para monitorar o CRM ou um webhook de acionamento manual.

2.  **Coleta de Dados do Lead e Contexto:**
    *   Recupera todos os dados relevantes do lead do CRM (Nome, Empresa, Cargo, Segmento, Interesses identificados, Notas de qualificação da IA).
    *   Opcional: Busca informações adicionais sobre a empresa (notícias recentes, menções) via APIs de enriquecimento de dados (ex: Clearbit, Apollo).

3.  **Geração do E-mail Personalizado pela LLM:**
    *   Os dados coletados são enviados para a API da LLM com um prompt detalhado para gerar um e-mail de prospecção.
    *   **Configuração de Chamada HTTP (N8N - Módulo "HTTP Request"):**
        *   **URL:** `https://api.anthropic.com/v1/messages`
        *   **Method:** `POST`
        *   **Headers:** `x-api-key`, `anthropic-version`, `content-type`
        *   **Body (JSON):**
            ```json
            {
              "model": "claude-3-5-sonnet-20240620",
              "max_tokens": 1000,
              "messages": [
                {
                  "role": "user",
                  "content": "Crie um e-mail de prospecção altamente personalizado para o lead {{Nome Lead}} da {{Empresa Lead}}, cargo {{Cargo Lead}}. Nossa solução é para otimização de DevOps e nosso ICP são empresas de tecnologia. O lead demonstrou interesse em '{{Interesse Identificado}}' e sua empresa '{{Contexto Empresa}}'. Use um tom profissional e amigável. O objetivo é agendar uma conversa inicial de 15 minutos para entender melhor os desafios dele. Inclua um link para agendamento via Calendly. Limite-se a 3 parágrafos curtos. Assinatura: [Seu Nome], [Seu Cargo] na [Sua Empresa].\n\nDados do Lead:\nNome: {{Nome Lead}}\nEmpresa: {{Empresa Lead}}\nCargo: {{Cargo Lead}}\nInteresse: {{Interesse Identificado}}\nContexto Empresa: {{Contexto Empresa}}"
                }
              ]
            }
            ```
        *   *(Onde `{{Nome Lead}}`, etc., são variáveis do CRM ou enriquecimento)*

4.  **Envio do E-mail via API de E-mail Marketing:**
    *   A resposta da LLM contendo o e-mail é extraída e enviada via API (ex: SendGrid, Mailgun) para o lead.
    *   **Configuração de Envio de E-mail (SendGrid - Módulo "Send an Email"):**
        *   **From:** `[seu_email_vendas]@suaempresa.com`
        *   **To:** `{{Email Lead}}`
        *   **Subject:** `Ideias para otimizar DevOps na {{Empresa Lead}} - [Seu Nome] da [Sua Empresa]`
        *   **Content (HTML ou Plain Text):** `{{Resposta LLM.choices[0].message.content}}` (Assumindo que a LLM retorna o corpo do e-mail diretamente)

5.  **Monitoramento e Follow-up (Opcional):**
    *   Configurar módulos para monitorar aberturas e cliques no e-mail (via webhooks do SendGrid).
    *   Se não houver resposta em X dias, disparar um prompt para a LLM gerar um e-mail de follow-up diferente.
    *   Se houver clique no link de agendamento, atualizar o status no CRM.
    *   **Exemplo de Link de Agendamento (Calendly):**
        `https://calendly.com/seu-nome/conversa-inicial-devops?name={{Nome Lead}}&email={{Email Lead}}` (Parâmetros pré-preenchidos)

---

## Templates

### Prompt para Análise de Sentimento em Mensagens de Lead

```
Você é um especialista em vendas e precisa analisar o sentimento e a urgência de uma mensagem de um lead. A mensagem pertence a um cliente em potencial para soluções de automação de processos de negócios.

Analise a mensagem a seguir e retorne um JSON com os seguintes campos:
- `sentimento`: 'positivo', 'neutro', 'negativo'
- `urgencia`: 'alta', 'media', 'baixa'
- `palavras_chave_interesse`: uma lista de 3 a 5 termos que indicam o foco principal do lead (ex: 'redução de custos', 'otimização de tempo', 'integração de sistemas').
- `proxima_acao_sugerida`: uma frase curta com a melhor próxima ação para o vendedor, baseada no sentimento e urgência.

Mensagem do Lead:
"Olá, estou com dificuldades em integrar o CRM com nosso ERP e o time de vendas está perdendo muito tempo com tarefas manuais. Precisamos de algo que acelere isso urgentemente, pois estamos perdendo vendas."

```

### E-mail de Follow-up para Lead com Agendamento Pré-preenchido

```
Assunto: Re: Conversa sobre otimização de processos na [Nome da Empresa do Lead]

Olá [Nome do Lead],

Espero que esteja tudo bem.

Vi que você baixou nosso e-book "5 Estratégias para Acelerar Vendas com Automação" e pensei que talvez tivéssemos uma conversa interessante.

Muitas empresas como a [Nome da Empresa do Lead] enfrentam desafios na integração de sistemas e na otimização de processos de vendas, resultando em perda de tempo e oportunidades. Tenho algumas ideias sobre como a [Sua Empresa] poderia ajudar a resolver isso.

Que tal agendarmos uma breve conversa de 15 minutos? Você pode escolher o melhor horário diretamente aqui: [Link do Calendly com parâmetros de lead pré-preenchidos, ex: https://calendly.com/seunome/15min?name=NomeDoLead&email=email@empresa.com].

Fico à disposição!

Atenciosamente,

[Seu Nome]
[Seu Cargo]
[Sua Empresa]
[Seu Telefone]
```

---

## Checklist

- [x] Configurar autenticação para APIs do CRM (Pipedrive/HubSpot).
- [x] Mapear campos de lead do formulário de entrada para o prompt de qualificação da LLM.
- [x] Implementar webhook de entrada para captura de leads em Make/N8N.
- [x] Testar o prompt de qualificação da LLM com cenários de leads qualificados e não qualificados.
- [x] Configurar regras condicionais no fluxo de automação para leads qualificados e não qualificados.
- [x] Integrar API de e-mail marketing (SendGrid/Mailgun) para envio de e-mails personalizados.
- [x] Validar o tom de voz e estilo dos e-mails gerados pela IA para alinhamento com a marca.
- [x] Incorporar link de agendamento de reuniões (Calendly/SavvyCal) com pré-preenchimento de dados do lead.
- [x] Criar um sistema de notificação (Slack/Email) para o time de vendas sobre novos SQLs.
- [x] Implementar um fallback manual para revisão de leads complexos ou ambíguos.

---

## Métricas de Referência

| Métrica | Benchmark (Indústria) | Meta (Ai Sales Assistant) |
|------------------------------------|----------------------------|---------------------------|
| Taxa de Qualificação de Leads (SQL) | 15% - 25%                 | 30% - 40%                 |
| Tempo Médio de Resposta ao Lead    | 24 horas                   | < 1 hora                  |
| Taxa de Conversão de SQL para Reunião | 20% - 35%                 | 40% - 55%                 |
| Custo por Lead Qualificado (CPL)   | R$50 - R$200              | R$30 - R$80               |
| Taxa de Abertura de E-mails (Outreach) | 20% - 30%                 | 35% - 50%                 |
| Taxa de Resposta de E-mails (Outreach) | 5% - 10%                  | 12% - 20%                 |

---

## Erros Comuns

1.  **Prompts Genéricos e Pouco Contextualizados**: Muitos usuários iniciam com prompts vagos como "Qualifique este lead". Isso resulta em respostas superficiais e pouco úteis.
    *   **Como evitar**: Forneça à LLM um contexto detalhado do seu ICP, critérios de qualificação específicos e exemplos de boas/más qualificações.
    *   **Exemplo**: Em vez de "Qualifique este lead", use "Avalie se este lead é um SQL para nossa plataforma SaaS de automação de RH, considerando que empresas com menos de 100 funcionários ou sem departamento de RH estruturado não são nosso ICP. O lead {{dados_do_lead}} indica busca por {{problema_mencionado}}."

2.  **Falta de Sincronização de Dados Bidirecional com o CRM**: A automação envia dados para o CRM, mas não lê de volta ou não atualiza status de forma consistente, levando a informações desatualizadas.
    *   **Como evitar**: Implemente módulos de "Get a Record" (Pipedrive) ou "Search Objects" (HubSpot) antes de atualizações, e configure webhooks no CRM para disparar ações de follow-up ou re-qualificação quando um status for alterado manualmente.
    *   **Exemplo**: Após um e-mail automatizado ser enviado, o fluxo deve atualizar um campo no CRM como "E-mail de Prospecção Enviado" e a data. Se o vendedor alterar o status do lead para "Reunião Agendada", um novo fluxo pode ser acionado para pausar follow-ups automatizados.

3.  **Ignorar a Intervenção Humana para Casos Complexos**: Confiar 100% na IA para qualificação ou prospecção sem um "plano B" para leads que a IA não consegue processar ou que são ambíguos.
    *   **Como evitar**: Implemente uma condição no fluxo de automação onde, se o score de qualificação da IA estiver abaixo de um certo limite (ex: 5/10) ou se a LLM indicar incerteza, o lead seja direcionado para uma fila de revisão humana ou receba uma notificação para um vendedor analisar manualmente.
    *   **Exemplo**: A LLM retorna `{"qualificado": null, "motivo": "Dados insuficientes para qualificação"}`. O fluxo então envia uma notificação no Slack para o time de vendas: "Lead {{Nome Lead}} precisa de revisão manual - AI sem dados suficientes."

---

## Dicas Avançadas

1.  **Uso de Embeddings para Personalização Profunda**: Em vez de apenas passar dados brutos para o prompt, gere embeddings (representações vetoriais) de documentos da sua empresa (casos de sucesso, descrições de produtos) e da mensagem do lead. Use RAG (Retrieval Augmented Generation) para que a LLM tenha acesso a informações contextuais relevantes para gerar respostas ainda mais precisas e personalizadas.
    *   **Exemplo Prático**: Armazenar descrições de soluções por segmento em um banco de dados vetorial. Quando um lead da indústria 'Varejo' é qualificado, o assistente busca embeddings relacionados a 'Varejo' e os injeta no prompt da LLM para gerar um e-mail que mencione especificamente desafios e soluções para esse setor.

2.  **A/B Testing Automatizado de Prompts e Mensagens**: Crie variantes de prompts para qualificação ou e-mails de prospecção. Use a ferramenta de automação para distribuir leads entre as variantes (ex: 50% para Prompt A, 50% para Prompt B) e monitore as métricas de performance (taxa de qualificação, taxa de abertura/resposta) para identificar qual prompt gera melhores resultados.
    *   **Exemplo Prático**: No Make/N8N, use um módulo "Router" com um "Random Switch" para enviar leads para dois caminhos diferentes. Cada caminho terá um prompt ligeiramente diferente para a LLM gerar o e-mail. Monitore as taxas de abertura e clique de cada e-mail para otimizar o prompt.

3.  **Sistema de Feedback Contínuo e Fine-tuning (Opcional)**: Crie um mecanismo onde os vendedores podem dar feedback rápido (positivo/negativo) sobre a qualificação ou a qualidade do e-mail gerado pela IA. Colete esse feedback e use-o para refinar os prompts ou até mesmo para fazer fine-tuning de modelos menores de LLMs para tarefas específicas.
    *   **Exemplo Prático**: Adicionar botões de "✅ Útil" / "❌ Não Útil" na notificação do Slack sobre o lead qualificado. Ao clicar, um webhook envia o feedback para um banco de dados, que pode ser usado para analisar a performance do prompt e ajustá-lo periodicamente.

4.  **Geração Proativa de Relatórios e Insights pela IA**: Configure a IA para analisar periodicamente os dados do CRM e das interações e gerar relatórios com insights sobre tendências de leads, gargalos no funil de vendas ou oportunidades de otimização dos prompts e fluxos.
    *   **Exemplo Prático**: Uma vez por semana, um módulo no Make/N8N extrai dados de leads qualificados e não qualificados do CRM. Esses dados são enviados para a LLM com um prompt como "Analise as tendências de qualificação dos últimos 7 dias. Identifique padrões de leads não qualificados e sugira 3 ajustes potenciais nos critérios de ICP ou no prompt de qualificação." O resultado é enviado por e-mail para o gerente de vendas.

5.  **Integração com Ferramentas de Enriquecimento de Dados Condicional**: Em vez de enriquecer todos os leads, use a IA para identificar leads com potencial alto, mas com dados incompletos. Somente para esses, dispare um processo de enriquecimento de dados via APIs como Clearbit ou Apollo, economizando custos e otimizando o uso de créditos.
    *   **Exemplo Prático**: Após a qualificação inicial, se o score for alto (ex: >7) mas o campo "Cargo" ou "Telefone" estiver vazio, a LLM pode indicar a necessidade de enriquecimento. O fluxo então usa essa indicação para disparar a API de enriquecimento para aquele lead específico antes de prosseguir com o contato.