---
name: ai-customer-support
description: "Ai Customer Support — Skill especializada para ai customer support"
license: MIT
metadata:
  version: 1.0.0
  author: Cafe Code AI
  category: 12-ia-automacao
  updated: 2026-03-01
risk: safe
---

# Ai Customer Support

Esta skill capacita o Claude a projetar, implementar e otimizar soluções de suporte ao cliente baseadas em IA, integrando chatbots, automações e APIs para resolver problemas reais e escalar operações.

---

## Keywords

Chatbot de atendimento, Automação CX, IA em suporte, NLU para clientes, Triagem automática, Resolução de tickets, Integração CRM, Fluxo de atendimento, Prompt engineering CX, Webhooks para suporte, APIs de IA, Satisfação do cliente IA.

---

## Quick Start

1.  **Analisar dados de tickets existentes**: Extrair as 5 intenções de contato mais frequentes e o volume de tickets para cada uma, identificando oportunidades de automação.
2.  **Modelar fluxo para "Redefinição de Senha"**: Desenhar um fluxo de chatbot para a intenção `redefinir_senha` que capture o email do usuário e acione uma API.
3.  **Configurar webhook para notificação**: Criar um webhook no Make/N8N para enviar uma notificação (ex: Slack) quando um ticket de "alta prioridade" for gerado por uma escalada da IA.
4.  **Criar prompt inicial para chatbot**: Desenvolver um prompt para o chatbot que defina seu persona e suas capacidades, além de instruí-lo a coletar informações essenciais antes de qualquer ação.

---

## Core Workflows

### Workflow 1: Triagem e Resolução Automática de Tickets Nível 1

Este workflow automatiza a resolução de dúvidas frequentes e de baixo risco, liberando agentes humanos para questões mais complexas.

**Cenário de Exemplo**: Um cliente entra em contato perguntando "Como faço para redefinir minha senha?".

**Passos Detalhados**:

1.  **Captura da Interação (Chatbot/Interface)**: O cliente digita sua pergunta em um widget de chat no website ou em um canal de mensagem (WhatsApp, Telegram).
    *   **Tecnologias**: Chatbot (ex: Manychat, Dialogflow, Botpress) integrado ao site ou aplicativo de mensagens.
    *   **Exemplo**: O cliente digita "Minha senha não funciona, preciso redefinir".

2.  **Análise de Linguagem Natural (NLU)**: O chatbot processa a entrada do usuário para identificar a intenção (`redefinir_senha`) e extrair entidades relevantes (ex: `email_cliente`).
    *   **Ferramentas**: Modelos de NLU embutidos na plataforma de chatbot ou APIs de NLU (ex: Google Cloud Natural Language API, OpenAI GPT).
    *   **Prompt de Exemplo para NLU (para Claude)**:
        ```
        Você é um sistema de NLU para suporte ao cliente. Dada a frase do usuário, identifique a intenção principal e extraia entidades.

        Frase: "Minha senha não funciona, preciso redefinir. Meu email é joao.silva@exemplo.com."
        Intenção: redefinir_senha
        Entidades: {"email": "joao.silva@exemplo.com"}

        Frase: "Não consigo acessar minha conta."
        Intenção: problema_acesso_conta
        Entidades: {}

        Frase: "{input_do_cliente}"
        Intenção:
        Entidades:
        ```

3.  **Validação e Coleta de Dados**: Se o email não foi fornecido, o chatbot solicita. Se foi, valida o formato.
    *   **Exemplo de Interação**:
        *   Chatbot: "Para redefinir sua senha, por favor, me informe o email associado à sua conta."
        *   Cliente: "joao.silva@exemplo.com"

4.  **Acionamento de API de Backend**: Com o email validado, o chatbot faz uma chamada para a API interna da empresa que gera e envia um link seguro de redefinição de senha.
    *   **Tecnologias**: Plataforma de automação (Make/N8N/Zapier) configurada para fazer requisições HTTP POST/GET.
    *   **Exemplo de Configuração (N8N/Make - Módulo HTTP Request)**:
        *   **URL**: `https://api.suaempresa.com/v1/users/reset-password`
        *   **Método**: `POST`
        *   **Headers**: `Content-Type: application/json`, `Authorization: Bearer {{sua_api_key}}`
        *   **Body (JSON)**:
            ```json
            {
              "email": "{{webhook.body.email_cliente}}",
              "redirect_url": "https://www.suaempresa.com/redefinir-senha-sucesso"
            }
            ```
        *   **Resposta Esperada**: `{"status": "success", "message": "Link de redefinição enviado para o email."}`

5.  **Confirmação ao Cliente**: O chatbot informa ao cliente que o link foi enviado e fornece instruções adicionais.
    *   **Exemplo de Resposta**: "Perfeito, João! Acabamos de enviar um link de redefinição de senha para joao.silva@exemplo.com. Por favor, verifique sua caixa de entrada e, se não encontrar, confira a pasta de spam. O link é válido por 30 minutos."

6.  **Registro da Interação (CRM/Helpdesk)**: A interação é registrada no sistema de CRM ou helpdesk, com status "Resolvido por IA", para fins de auditoria e métricas.
    *   **Tecnologias**: Integração via API (ex: Zendesk API, HubSpot API) ou conector nativo da plataforma de automação.
    *   **Exemplo de Requisição (Zapier para Zendesk)**:
        *   **Ação**: Create Ticket
        *   **Subject**: "Redefinição de Senha Automática"
        *   **Description**: "Cliente {{webhook.body.email_cliente}} solicitou e recebeu link de redefinição via IA."
        *   **Status**: "Closed"
        *   **Tags**: "automacao_ia", "redefinir_senha"

### Workflow 2: Escalada Inteligente e Contextualizada para Agente Humano

Este workflow garante que, quando a IA não consegue resolver o problema, o cliente seja transferido para um agente humano com todo o contexto necessário, minimizando a frustração.

**Cenário de Exemplo**: Um cliente está frustrado e diz "Minha compra foi cancelada, não entendi o motivo e preciso resolver agora! O pedido é o #78901."

**Passos Detalhados**:

1.  **Detecção de Complexidade/Frustração (NLU/Regras)**: O chatbot detecta palavras-chave de frustração ("preciso resolver agora", "não entendi", "urgente"), múltiplas negativas ou uma intenção que não pode ser resolvida automaticamente (ex: `problema_cancelamento_pedido`).
    *   **Tecnologias**: NLU avançado com análise de sentimento, regras pré-definidas na plataforma de chatbot.
    *   **Exemplo de Prompt para Detecção de Frustração (para Claude)**:
        ```
        Você é um sistema de análise de sentimento para suporte. Avalie a frase do usuário.
        Frase: "Minha compra foi cancelada, não entendi o motivo e preciso resolver agora! O pedido é o #78901."
        Sentimento: Frustração/Urgência
        Intenção: Problema_cancelamento_pedido
        ```

2.  **Coleta de Dados Essenciais**: Antes de transferir, a IA tenta coletar informações cruciais para o agente (ID do pedido, email, breve descrição).
    *   **Exemplo de Interação**:
        *   Chatbot: "Compreendo que isso é frustrante. Para que eu possa te ajudar a transferir para a equipe certa, poderia me confirmar o número do pedido e o email da compra?"
        *   Cliente: "Sim, o pedido é #78901 e o email é maria.silva@exemplo.com."

3.  **Sumarização da Conversa (Geração de Texto)**: A IA gera um resumo conciso da conversa até o momento, incluindo o problema inicial, as tentativas de resolução (se houver) e os dados coletados.
    *   **Tecnologias**: Modelos de linguagem grandes (LLMs) via API (ex: OpenAI GPT, Anthropic Claude).
    *   **Prompt de Exemplo para Sumarização (para Claude)**:
        ```
        Você é um assistente de IA. Sumarize a seguinte conversa entre um cliente e um chatbot em no máximo 3 frases, focando no problema e nos dados relevantes.

        Histórico da Conversa:
        Cliente: "Minha compra foi cancelada, não entendi o motivo e preciso resolver agora! O pedido é o #78901."
        Chatbot: "Compreendo que isso é frustrante. Para que eu possa te ajudar a transferir para a equipe certa, poderia me confirmar o número do pedido e o email da compra?"
        Cliente: "Sim, o pedido é #78901 e o email é maria.silva@exemplo.com."

        Sumário:
        ```
        *   **Saída Esperada**: "O cliente Maria Silva (maria.silva@exemplo.com) está frustrada com o cancelamento do pedido #78901 e não compreende o motivo. Ela necessita de uma resolução urgente."

4.  **Criação de Ticket no Helpdesk e Notificação**: Um novo ticket é criado no sistema de helpdesk (ex: Zendesk, Freshdesk) com o sumário e os dados do cliente. Um webhook ou integração direta notifica a equipe de agentes.
    *   **Tecnologias**: Make/N8N/Zapier, APIs de Helpdesk (ex: `POST /api/v2/tickets` para Zendesk).
    *   **Exemplo de Corpo da Requisição (JSON para Zendesk API)**:
        ```json
        {
          "ticket": {
            "subject": "Escalada: Cancelamento Urgente - Pedido #{{pedido_id}}",
            "comment": {
              "body": "Cliente: {{nome_cliente}} ({{email_cliente}})\n\nSumário da Interação com IA:\n{{sumario_gerado_pela_ia}}\n\nPor favor, assumir este atendimento com prioridade.",
              "public": false
            },
            "priority": "high",
            "requester": {
              "name": "{{nome_cliente}}",
              "email": "{{email_cliente}}"
            },
            "tags": ["automacao_ia", "escalada", "cancelamento_pedido", "urgente"]
          }
        }
        ```
    *   **Exemplo de Notificação (Webhook para Slack)**:
        *   **URL**: `https://hooks.slack.com/services/T012345/B678901/XXXXXXXXXXXXXXXX`
        *   **Método**: `POST`
        *   **Body (JSON)**:
            ```json
            {
              "text": ":alert: *Novo Ticket de Alta Prioridade - Escalado pela IA*\n*Assunto:* {{ticket_subject}}\n*Cliente:* {{nome_cliente}} (<mailto:{{email_cliente}}|{{email_cliente}}>)\n*Sumário da IA:*\n```\n{{sumario_gerado_pela_ia}}\n```\n*Link do Ticket:* {{link_do_ticket_no_helpdesk}}"
            }
            ```

5.  **Mensagem ao Cliente e Transferência**: O chatbot informa ao cliente que ele será transferido e que um agente já tem todo o contexto.
    *   **Exemplo de Resposta**: "Entendido, Maria. Seu caso é importante e já criei um ticket (#{{id_do_ticket}}). Um de nossos especialistas em cancelamentos já recebeu todo o contexto da nossa conversa e entrará em contato em breve por aqui ou por email. Agradeço sua paciência!"

---

## Templates

### Prompt para Triagem de Intenção e Entidades

```
Você é um modelo de linguagem avançado especializado em atendimento ao cliente. Dada a interação do usuário, identifique a intenção principal e extraia entidades relevantes. Responda apenas com a Intenção e as Entidades em formato JSON.

Interação: "Minha internet não está funcionando, já reiniciei o modem 3 vezes e verifiquei os cabos. Preciso de ajuda urgente."
Intenção: problema_internet
Entidades: {"problema": "internet não funcionando", "tentativas_resolucao": "reiniciei o modem 3 vezes e verifiquei os cabos", "urgencia": true}

Interação: "Gostaria de saber o status do meu pedido 12345 que comprei ontem."
Intenção: status_pedido
Entidades: {"id_pedido": "12345", "data_compra": "ontem"}

Interação: "Qual o horário de funcionamento da loja do shopping Iguatemi no feriado de Natal?"
Intenção: horario_funcionamento
Entidades: {"local": "loja do shopping Iguatemi", "evento": "feriado de Natal"}

Interação: "Não recebi o email de confirmação da minha compra."
Intenção: problema_email_confirmacao
Entidades: {}

Interação: "{pergunta_do_cliente}"
Intenção:
Entidades:
```

### Mensagem de Escalada para Agente (via Sistema de Tickets)

```
Assunto: Escalada IA: [Intenção Detectada] - Cliente [Nome do Cliente] - [ID do Pedido/Serviço se houver]

Prezado(a) [Nome do Agente ou Equipe],

Este ticket foi gerado por uma escalada inteligente do nosso chatbot. A IA identificou que o problema do cliente requer atenção humana e forneceu o contexto abaixo.

**Dados do Cliente:**
*   **Nome:** [Nome do Cliente, ex: João da Silva]
*   **Email:** [Email do Cliente, ex: joao.silva@email.com]
*   **ID do Cliente/Usuário (se disponível):** [ID_Cliente_CRM, ex: CTM-98765]

**Contexto da Conversa com a IA:**
[Sumário conciso da conversa gerado pela IA, ex: "O cliente está com problemas para ativar o novo chip de telefone após a portabilidade. Ele já tentou reiniciar o aparelho e verificar o sinal, mas sem sucesso. A IA não conseguiu resolver o problema diretamente e escalou. O número de telefone envolvido é (XX) 9XXXX-XXXX."]

**Detalhes Adicionais (Entidades Extraídas):**
*   **Intenção Principal:** [Intenção_Detectada, ex: `problema_ativacao_chip`]
*   **Produto/Serviço:** [Produto_Relacionado, ex: `chip_celular`, `portabilidade`]
*   **Frustração Detectada:** [Nível/Tipo de Frustração, ex: `Alta`, `Urgência`]
*   **Tentativas de Solução (pelo cliente/IA):** [Tentativas, ex: `reiniciar aparelho`, `verificar sinal`]

**Prioridade:** [Alta/Média]

Por favor, assuma este atendimento e utilize o contexto fornecido para uma resolução eficiente.

Atenciosamente,
Sistema de Automação de Suporte
```

---

## Checklist

-   [x] Mapear as 10 intenções de atendimento mais frequentes do histórico de tickets.
-   [x] Configurar modelos de NLU para identificar intenções com precisão > 85% e extrair 3-5 entidades-chave por intenção.
-   [x] Integrar o chatbot com a base de conhecimento (FAQs, artigos de ajuda) para respostas baseadas em RAG (Retrieval Augmented Generation).
-   [x] Implementar um fluxo de escalada para agentes humanos que inclua sumário automático e dados do cliente.
-   [x] Configurar webhooks para notificar equipes internas (Slack/Teams) sobre escaladas de alta prioridade ou erros do chatbot.
-   [x] Criar um mecanismo para coletar feedback do cliente sobre a performance da IA (ex: "Isso resolveu seu problema? Sim/Não").
-   [x] Desenvolver um processo para treinamento contínuo do chatbot com transcrições de conversas reais e feedback dos agentes.
-   [x] Testar cenários de ponta (edge cases), perguntas fora do escopo e tentativas repetidas de um mesmo problema.
-   [x] Implementar lógica para detectar e mitigar "loops de conversa" ou repetições excessivas do chatbot.
-   [x] Definir e monitorar métricas de performance do chatbot (Taxa de Resolução por IA, CSAT, Taxa de Escalada).

---

## Métricas de Referência

| Métrica                      | Benchmark (Indústria) | Meta Interna |
| :--------------------------- | :-------------------- | :----------- |
| Taxa de Resolução por IA     | 60% - 75%             | 70%          |
| Tempo Médio de Resposta (IA) | < 5 segundos          | < 3 segundos |
| CSAT (IA)                    | 4.0 - 4.5 (escala 5)  | 4.2          |
| Taxa de Escalada para Agente | 20% - 35%             | 25%          |
| Custo por Interação (IA)     | $0.10 - $0.50         | $0.20        |
| Precisão da NLU              | 85% - 95%             | 90%          |

---

## Erros Comuns

1.  **"Alucinações" do Chatbot**: O chatbot inventa informações ou responde com dados incorretos quando não tem a resposta.
    *   **Como evitar**: Implementar RAG (Retrieval Augmented Generation) estrito, onde o chatbot é instruído a buscar respostas APENAS em uma base de conhecimento curada e validada. Se a informação não for encontrada, ele deve escalar para um humano ou indicar que não possui a informação.
    *   **Exemplo**: O prompt do chatbot deve incluir: "Responda SOMENTE com base nas informações do artigo fornecido. Se a resposta não estiver clara no artigo, diga 'Não tenho informações suficientes para responder a isso agora, mas posso te transferir para um especialista.'"

2.  **Loops de Conversa Incessantes**: O chatbot fica preso em um ciclo de perguntas ou respostas repetidas, frustrando o cliente.
    *   **Como evitar**: Implementar contadores de repetição e detecção de frustração no fluxo. Se o cliente repetir a mesma pergunta 3 vezes ou usar palavras-chave como "não entendi", "ajuda", "urgente" sem progresso, o sistema deve automaticamente oferecer escalada ou opções claras de saída.
    *   **Exemplo**: No Make/N8N, após cada interação, incremente um contador. Se `contador > 2` para a mesma intenção, ative um sub-workflow de escalada: "Parece que não estou conseguindo te ajudar com isso. Gostaria que um agente humano assumisse? (Sim/Não)".

3.  **Falta de Contexto na Escalada**: O agente humano recebe o ticket sem saber o que foi conversado anteriormente com a IA, forçando o cliente a repetir toda a história.
    *   **Como evitar**: Garantir que o workflow de escalada sempre inclua a sumarização da conversa e a extração de entidades-chave (ID do cliente, ID do pedido, problema principal) antes de criar o ticket ou transferir. O sumário deve ser o primeiro item visível no ticket do agente.
    *   **Exemplo**: O corpo do ticket criado via API no Zendesk/Freshdesk deve conter o sumário gerado por LLM e os dados do cliente no campo de descrição, como mostrado no "Template de Escalada para Agente".

---

## Dicas Avançadas

1.  **Personalização Dinâmica com Perfil do Cliente**: Integre o chatbot com seu CRM (Salesforce, HubSpot) para acessar o perfil completo do cliente (histórico de compras, plano atual, tickets anteriores). Use esses dados para personalizar as respostas e oferecer soluções proativas, como sugerir um upgrade de plano ou informar sobre um problema em andamento.
    *   **Exemplo Prático**: Ao iniciar uma conversa, a IA consulta o CRM com o email do cliente. Se o cliente possui o "Plano Premium", o chatbot pode começar com: "Olá, [Nome do Cliente]! Percebi que você é um cliente Premium. Como posso te ajudar hoje com seu [Produto/Serviço Premium]?"

2.  **Detecção Preditiva de Churn e Intervenção**: Utilize análise de sentimento e padrões de interação da IA para identificar clientes com alto risco de churn (ex: múltiplas reclamações, perguntas sobre cancelamento, tom negativo persistente). Configure alertas automáticos para a equipe de sucesso do cliente ou para um gerente, permitindo uma intervenção humana proativa.
    *   **Exemplo Prático**: No N8N/Make, após 3 interações consecutivas com sentimento negativo OU se a intenção `cancelar_assinatura` for detectada, um fluxo é acionado para criar um ticket de "Risco de Churn" com prioridade alta e notificar o gestor da conta via Slack/Email.

3.  **Otimização Contínua com Feedback Loop Agente-IA**: Implemente um sistema onde agentes humanos possam corrigir ou validar as respostas da IA diretamente na interface do helpdesk. Esse feedback é então usado para retreinar e melhorar o modelo de IA, criando um ciclo de melhoria contínua.
    *   **Exemplo Prático**: Na interface do Zendesk, um agente pode ter um botão "Melhorar Resposta da IA" ao lado de uma resposta automática. Ao clicar, ele pode editar a resposta sugerida e essa edição é enviada para um dataset de treinamento da IA, que será revisado e incorporado em futuras atualizações do modelo.

4.  **Geração Automática de Artigos de Conhecimento**: A partir de interações recorrentes que a IA não conseguiu resolver ou de perguntas complexas que exigiram intervenção humana, use a própria IA para rascunhar novos artigos para a base de conhecimento. Esses rascunhos são então revisados e aprovados por um humano.
    *   **Exemplo Prático**: Quando um ticket é fechado e a tag `novo_artigo_sugerido` está presente, um fluxo automatizado (Make/N8N) envia o histórico da conversa para um LLM com um prompt como: "Com base neste ticket resolvido, rascunhe um artigo de FAQ sobre 'Como resolver [problema principal do ticket]' em português brasileiro, com passos claros e exemplos." O rascunho é então enviado para revisão em uma ferramenta de gestão de conteúdo.