---
name: ai-meeting-assistant
description: "Ai Meeting Assistant — Skill especializada para ai meeting assistant"
license: MIT
metadata:
  version: 1.0.0
  author: Cafe Code AI
  category: 12-ia-automacao
  updated: 2026-03-01
---

# Ai Meeting Assistant

Esta skill capacita o Claude a projetar, implementar e otimizar assistentes de reunião baseados em IA, automatizando transcrição, sumarização, identificação de ações e distribuição de follow-ups.

---

## Keywords

Transcrição de reunião, Sumarização de IA, Itens de ação automatizados, Follow-up de reunião, Automação Make, N8N, Zapier, APIs de LLM, Google Meet API, Zoom API, Claude API, Anthropic API, Webhooks, Processamento de linguagem natural.

---

## Quick Start

1.  **Configurar acesso à plataforma de videoconferência**: Obter credenciais de API ou tokens OAuth para Zoom, Google Meet ou Microsoft Teams para acessar gravações pós-reunião.
2.  **Selecionar e configurar serviço de transcrição**: Integrar com APIs como Google Cloud Speech-to-Text, Azure Cognitive Services ou AssemblyAI para converter áudio da reunião em texto.
3.  **Desenvolver prompt para sumarização com Claude**: Criar um prompt estruturado para o Claude, solicitando um resumo conciso, extração de decisões e identificação de itens de ação a partir da transcrição.
4.  **Implementar automação de distribuição**: Usar ferramentas como Make.com ou N8N para orquestrar o fluxo de trabalho, enviando os resumos gerados por Claude via e-mail (SendGrid) ou para canais de comunicação (Slack/Microsoft Teams).

---

## Core Workflows

### Workflow 1: Geração Automatizada de Resumos de Reunião e Distribuição

Este workflow detalha a captura de uma gravação de reunião, sua transcrição, sumarização por IA e distribuição automática para os participantes.

**Passos detalhados:**

1.  **Configuração de Trigger (Make/N8N):**
    *   **Fonte da Reunião:** Configure um webhook ou módulo de "Novo Evento/Gravação" para Zoom, Google Meet ou Microsoft Teams.
    *   **Exemplo (Webhook Zoom):**
        *   Crie um Webhook no Zoom Developer Console para o evento `recording.completed`.
        *   O payload do webhook conterá `download_url` para o áudio/vídeo da gravação.
        *   No Make.com, adicione um módulo "Webhooks > Custom webhook" e copie o URL gerado para o Zoom.
        *   Exemplo de payload recebido pelo webhook:
            ```json
            {
              "event": "recording.completed",
              "payload": {
                "object": {
                  "uuid": "...",
                  "id": "...",
                  "host_id": "...",
                  "topic": "Reunião de Alinhamento Projeto X",
                  "type": 2,
                  "start_time": "2023-10-27T14:00:00Z",
                  "duration": 60,
                  "recording_files": [
                    {
                      "id": "...",
                      "meeting_id": "...",
                      "recording_start": "2023-10-27T14:00:00Z",
                      "recording_end": "2023-10-27T15:00:00Z",
                      "file_type": "MP4",
                      "file_extension": "MP4",
                      "file_size": 12345678,
                      "play_url": "https://zoom.us/rec/share/...",
                      "download_url": "https://zoom.us/rec/download/...",
                      "status": "completed",
                      "recording_type": "shared_screen_with_speaker_view"
                    },
                    {
                      "id": "...",
                      "meeting_id": "...",
                      "recording_start": "2023-10-27T14:00:00Z",
                      "recording_end": "2023-10-27T15:00:00Z",
                      "file_type": "AUDIO",
                      "file_extension": "M4A",
                      "file_size": 567890,
                      "play_url": "https://zoom.us/rec/share/...",
                      "download_url": "https://zoom.us/rec/download/audio/...",
                      "status": "completed",
                      "recording_type": "audio_only"
                    }
                  ]
                }
              }
            }
            ```

2.  **Transcrição de Áudio:**
    *   Use o `download_url` do arquivo de áudio (`file_type: "AUDIO"`) do payload do webhook.
    *   Envie o arquivo de áudio para uma API de transcrição.
    *   **Exemplo (Google Cloud Speech-to-Text API via N8N):**
        *   Módulo: "HTTP Request" (POST) para `https://speech.googleapis.com/v1/speech:recognize`.
        *   Headers: `Authorization: Bearer {{sua_credencial_gcp}}`, `Content-Type: application/json`.
        *   Body (JSON):
            ```json
            {
              "audio": {
                "uri": "{{URL_DE_DOWNLOAD_DO_AUDIO_DO_ZOOM}}"
              },
              "config": {
                "encoding": "M4A",
                "sampleRateHertz": 16000,
                "languageCode": "pt-BR",
                "enableAutomaticPunctuation": true
              }
            }
            ```
        *   A resposta conterá a transcrição completa no campo `results[].alternatives[0].transcript`.

3.  **Sumarização com Claude:**
    *   Pegue a transcrição completa e envie para a API do Anthropic Claude.
    *   **Exemplo (Anthropic Claude API via Make/N8N):**
        *   Módulo: "Anthropic Claude > Create a Message" (ou "HTTP Request" para a API `messages`).
        *   Modelo: `claude-3-5-sonnet-20240620`.
        *   Role: `user`.
        *   Content (prompt): Veja o "Template: Prompt para Sumarização de Reunião" abaixo.
        *   Parâmetros: `max_tokens=2000`, `temperature=0.3`.

4.  **Formatação e Distribuição do Resumo:**
    *   O output de Claude será o resumo formatado.
    *   Envie este resumo para os participantes da reunião.
    *   **Exemplo (Envio via Slack e E-mail):**
        *   **Slack (Make/N8N):** Módulo "Slack > Create a message".
            *   `Channel`: `#reunioes-projeto-x` ou canal privado com os participantes.
            *   `Text`: "Olá equipe,\n\nSegue o resumo da reunião '{{NOME_DA_REUNIAO}}' de hoje:\n\n{{RESUMO_DO_CLAUDE}}"
        *   **E-mail (SendGrid via Make/N8N):** Módulo "SendGrid > Send an email".
            *   `From`: `assistente@suaempresa.com.br`
            *   `To`: Endereços de e-mail dos participantes (extraídos do payload do Zoom ou de uma lista).
            *   `Subject`: "Resumo da Reunião: {{NOME_DA_REUNIAO}}"
            *   `Content`: "Olá,\n\nEspero que este e-mail encontre você bem. Segue o resumo detalhado da nossa reunião '{{NOME_DA_REUNIAO}}' de {{DATA_DA_REUNIAO}}:\n\n{{RESUMO_DO_CLAUDE}}\n\nAtenciosamente,\nSeu Assistente de IA."

### Workflow 2: Identificação e Atribuição de Itens de Ação e Decisões

Este workflow se concentra em extrair itens de ação, decisões e atribuí-los a indivíduos, integrando-se com ferramentas de gestão de projetos.

**Passos detalhados:**

1.  **Entrada de Dados:**
    *   Use a mesma transcrição gerada no Workflow 1 ou o resumo inicial de Claude como input.
    *   Para maior precisão na extração de itens de ação, a transcrição completa é preferível.

2.  **Extração Estruturada com Claude:**
    *   Crie um prompt específico para o Claude para extrair itens de ação, responsáveis, prazos e decisões em um formato JSON.
    *   **Exemplo (Anthropic Claude API via Make/N8N):**
        *   Módulo: "Anthropic Claude > Create a Message".
        *   Modelo: `claude-3-5-sonnet-20240620`.
        *   Role: `user`.
        *   Content (prompt): Veja o "Template: Prompt para Extração de Ações e Decisões" abaixo.
        *   Parâmetros: `max_tokens=2000`, `temperature=0.1` (para maior determinismo).
        *   O output esperado de Claude deve ser um JSON parserável.

3.  **Processamento do Output JSON:**
    *   Após receber a resposta JSON de Claude, use módulos de "Parse JSON" (Make/N8N) para transformar os dados em uma estrutura utilizável.
    *   **Exemplo de Output JSON (Claude):**
        ```json
        {
          "itens_de_acao": [
            {
              "descricao": "Finalizar a proposta comercial para o cliente Alpha",
              "responsavel": "Ana Paula",
              "prazo": "2023-11-05",
              "status": "Pendente",
              "observacoes": "Revisar cláusula de licenciamento."
            },
            {
              "descricao": "Agendar reunião de follow-up com o time de desenvolvimento",
              "responsavel": "Carlos Eduardo",
              "prazo": "2023-11-03",
              "status": "Pendente",
              "observacoes": "Verificar disponibilidade da Carla e do Rafael."
            }
          ],
          "decisoes_chave": [
            {
              "descricao": "Decidido priorizar o desenvolvimento do Módulo de Relatórios",
              "contexto": "Discussão sobre backlog de sprints",
              "impacto": "Atraso no Módulo de Integrações por 2 semanas."
            }
          ]
        }
        ```

4.  **Criação de Tarefas em Ferramentas de Gestão de Projetos:**
    *   Itere sobre os `itens_de_acao` extraídos e crie tarefas nas ferramentas apropriadas.
    *   **Exemplo (ClickUp API via Make/N8N):**
        *   Módulo "ClickUp > Create a Task".
        *   `List ID`: `{{ID_DA_LISTA_DO_PROJETO}}`
        *   `Task Name`: `{{item.descricao}}`
        *   `Description`: `Responsável: {{item.responsavel}}\nObservações: {{item.observacoes}}`
        *   `Due Date`: `{{item.prazo}}` (converter para timestamp UNIX se necessário).
        *   `Assignees`: Mapear `{{item.responsavel}}` para o ID de usuário do ClickUp.
    *   **Exemplo (Asana API via Make/N8N):** Similar ao ClickUp, usando o módulo "Asana > Create a Task".

5.  **Registro de Decisões em CRM/Base de Conhecimento:**
    *   As `decisoes_chave` podem ser registradas em sistemas como CRM (Salesforce, HubSpot) ou em uma base de conhecimento (Notion, Confluence).
    *   **Exemplo (Salesforce API via Make/N8N):** Módulo "Salesforce > Create a Record".
        *   `Object Type`: `Task` ou um objeto personalizado como `Meeting_Decision__c`.
        *   `Subject`: "Decisão da Reunião: {{decisao.descricao}}"
        *   `Description`: `Contexto: {{decisao.contexto}}\nImpacto: {{decisao.impacto}}`
        *   `Related To`: Ligar a um registro de cliente ou projeto existente.

---

## Templates

### Template: Resumo de Reunião de Alinhamento Semanal

```
Assunto: Resumo da Reunião Semanal de Alinhamento - Projeto Aurora [27/10/2023]

Olá equipe,

Segue o resumo da nossa reunião semanal de alinhamento do Projeto Aurora, realizada em 27 de outubro de 2023.

---

**Participantes:**
*   Ana Paula (Líder de Projeto)
*   Carlos Eduardo (Desenvolvimento)
*   Juliana Silva (Marketing)
*   Rafael Mendes (UX/UI)

**Pauta Principal:**
1.  Status do Módulo de Pagamentos
2.  Feedback da Sprint 3
3.  Planejamento de Marketing para Lançamento
4.  Próximos Passos e Itens de Ação

---

**Decisões Chave:**

1.  **Priorização do Módulo de Pagamentos:** Decidido que o Módulo de Pagamentos terá prioridade máxima para a próxima semana, visando a conclusão até 03/11.
2.  **Aprovação da Campanha de Lançamento:** A campanha de marketing apresentada pela Juliana foi aprovada, com foco em mídias sociais e email marketing para a primeira fase.
3.  **Reunião de Retrospectiva:** Agendada uma reunião de retrospectiva dedicada para a Sprint 3 na próxima terça-feira, 31/10, às 10h.

---

**Itens de Ação:**

*   **Ana Paula:**
    *   Revisar e aprovar o escopo final do Módulo de Pagamentos. (Prazo: 28/10)
    *   Agendar a reunião de retrospectiva da Sprint 3. (Prazo: 29/10)
*   **Carlos Eduardo:**
    *   Iniciar o desenvolvimento do Módulo de Pagamentos, focando nas integrações com Stripe. (Prazo: 03/11)
    *   Fornecer um update diário sobre o progresso do Módulo de Pagamentos. (Início: 30/10)
*   **Juliana Silva:**
    *   Preparar os criativos e textos para a campanha de lançamento inicial. (Prazo: 01/11)
    *   Configurar as automações de email marketing para a fase pré-lançamento. (Prazo: 02/11)
*   **Rafael Mendes:**
    *   Finalizar os protótipos de alta fidelidade para as telas de checkout. (Prazo: 30/10)
    *   Realizar uma mini-sessão de validação interna com o time de desenvolvimento. (Prazo: 31/10)

---

**Próxima Reunião:**
*   **Data:** 03 de novembro de 2023
*   **Horário:** 14:00h
*   **Pauta Sugerida:** Status do Módulo de Pagamentos, Planejamento da Sprint 4, Métricas da Campanha de Lançamento.

Qualquer dúvida ou necessidade de esclarecimento, por favor, entre em contato.

Atenciosamente,
Assistente de IA do Projeto Aurora
```

### Template: Prompt para Extração de Ações e Decisões

```
Você é um especialista em processamento de linguagem natural e assistente de reuniões. Sua tarefa é analisar a transcrição de uma reunião e extrair as seguintes informações de forma estruturada:

1.  **Itens de Ação:** Qualquer tarefa ou atividade que precise ser realizada, incluindo o responsável, um prazo (se mencionado ou inferível), e um status inicial (Pendente).
2.  **Decisões Chave:** Qualquer decisão importante tomada durante a reunião, com um breve contexto e seu impacto.

Apresente as informações em formato JSON, seguindo a estrutura fornecida abaixo. Se um campo não puder ser extraído de forma clara, preencha com `null` ou deixe vazio, mas priorize a predição inteligente de prazos baseada em menções como "próxima semana" ou "até sexta".

**Formato JSON Esperado:**

```json
{
  "itens_de_acao": [
    {
      "descricao": "string",
      "responsavel": "string",
      "prazo": "YYYY-MM-DD"
    }
  ],
  "decisoes_chave": [
    {
      "descricao": "string",
      "contexto": "string",
      "impacto": "string"
    }
  ]
}
```

**Transcrição da Reunião:**

<transcription>
[INSERIR TRANSCRIÇÃO DA REUNIÃO AQUI]

Exemplo de transcrição: "Ana, você pode finalizar a proposta comercial para o cliente Alpha até o final da próxima semana? Carlos, por favor, agende uma reunião de follow-up com o time de desenvolvimento para discutir a integração, tente para esta sexta-feira. Decidimos que vamos priorizar o desenvolvimento do Módulo de Relatórios, o que significa que o Módulo de Integrações terá um atraso de duas semanas. Juliana, inicie a campanha de email marketing o mais rápido possível."
</transcription>

**Sua resposta JSON:**
```json
```
```

---

## Checklist

- [ ] Credenciais de API (Zoom/Google Meet/MS Teams) obtidas e configuradas corretamente para acesso a gravações.
- [ ] Serviço de transcrição (GCP Speech-to-Text/AssemblyAI) selecionado, com chave de API e cota de uso verificadas.
- [ ] Webhook para `recording.completed` configurado e testado entre a plataforma de videoconferência e a ferramenta de automação (Make/N8N).
- [ ] Fluxo de automação (Make/N8N) criado para capturar o URL da gravação de áudio.
- [ ] Módulo de envio de áudio para a API de transcrição configurado com o formato de arquivo correto (`M4A`, `MP4`).
- [ ] Prompt de sumarização para Claude otimizado com instruções claras para o formato desejado (resumo, decisões, ações).
- [ ] Módulo de chamada à API do Anthropic Claude configurado com a `API Key` e o `model` apropriados.
- [ ] Mapeamento dos campos do resumo gerado por Claude para os canais de distribuição (email via SendGrid, Slack).
- [ ] Permissões de envio de email (SendGrid) ou postagem em canal (Slack) configuradas para o assistente de IA.
- [ ] Fluxo de extração de itens de ação e decisões configurado para gerar JSON parserável por Claude.
- [ ] Módulos de "Parse JSON" (Make/N8N) adicionados para processar a saída de Claude.
- [ ] Integração com ferramentas de gestão de projetos (ClickUp/Asana) configurada para criar tarefas automaticamente.
- [ ] Mapeamento de responsáveis para IDs de usuário nas ferramentas de gestão de projetos validado.
- [ ] Cenário de erro (ex: transcrição falha, API offline) tratado com notificações ou retentativas.

---

## Métricas de Referência

| Métrica                                | Benchmark        | Meta             |
|----------------------------------------|------------------|------------------|
| Tempo Médio para Geração de Resumo     | 10 minutos       | < 5 minutos      |
| Precisão da Transcrição                | 90% (Word Error Rate) | > 95% (WER)     |
| Taxa de Identificação de Itens de Ação | 80%              | > 95%            |
| Taxa de Conclusão de Itens de Ação     | 60%              | > 80%            |
| Redução do Tempo de Preparação Pós-Reunião | 30%              | > 50%            |
| Satisfação dos Participantes (NPS)     | 7/10             | > 9/10           |

---

## Erros Comuns

1.  **Transcrição imprecisa ou incompleta**: Linguagem técnica específica ou ruído de fundo excessivo pode comprometer a qualidade da transcrição, resultando em resumos incorretos.
    *   **Como evitar**: Utilizar APIs de transcrição com modelos customizáveis ou capazes de aprender jargões específicos. Por exemplo, treinar modelos de fala com vocabulários personalizados via Google Custom Speech. Adicionar instruções ao prompt de Claude para "compensar" por possíveis ruídos ou termos técnicos complexos, pedindo inferência contextual.
2.  **Prompts genéricos ou mal estruturados para Claude**: Um prompt que não especifica claramente o formato de saída, o nível de detalhe ou as informações a serem extraídas resultará em resumos inconsistentes ou incompletos.
    *   **Como evitar**: Sempre usar o formato de "few-shot learning" ou "zero-shot learning" com exemplos claros dentro do prompt, ou definir restrições de formato (ex: JSON Schema) e "role-playing" para Claude (ex: "Você é um especialista em gestão de projetos..."). Validar o prompt com várias transcrições de teste.
3.  **Falha na integração ou mapeamento de dados**: Problemas na passagem de dados entre a plataforma de videoconferência, o serviço de transcrição, Claude e as ferramentas de gestão de projetos podem impedir a automação completa. Ex: o nome do responsável na transcrição não corresponde a um ID de usuário no ClickUp.
    *   **Como evitar**: Implementar validação de dados em cada etapa da automação (Make/N8N). Usar tabelas de lookup (ex: um Google Sheet com nomes de usuários e seus respectivos IDs em diferentes ferramentas) para mapear nomes de pessoas para IDs de sistema. Testar o fluxo de ponta a ponta com dados reais.

---

## Dicas Avançadas

1.  **Ajuste Fino de LLMs para Jargões Específicos**: Para equipes com terminologia altamente especializada (e.g., medicina, engenharia aeroespacial), considere o ajuste fino (fine-tuning) de modelos de linguagem (se a API do Claude permitir ou usar modelos open-source como Llama 2 ou Mistral com técnicas de LoRA) ou a criação de bibliotecas de termos para incluir em prompts. Isso melhora drasticamente a compreensão e sumarização de conteúdo técnico. Por exemplo, um prompt pode incluir `CONTEXTO: Esta reunião aborda a arquitetura de microserviços em um ambiente Kubernetes, focando em CI/CD.`
2.  **Análise de Tendências de Reunião com BI**: Armazene os metadados das reuniões (duração, participantes, número de itens de ação, decisões chave, tópicos recorrentes) em um banco de dados (ex: PostgreSQL) e conecte-o a uma ferramenta de Business Intelligence (ex: Power BI, Tableau). Isso permite identificar tendências como reuniões excessivamente longas, equipes sobrecarregadas com ações, ou tópicos que requerem mais atenção. `SQL: SELECT AVG(duration_minutes), COUNT(action_items) FROM meetings WHERE date BETWEEN '2023-01-01' AND '2023-03-31';`
3.  **Feedback Loop Contínuo com RAG (Retrieval-Augmented Generation)**: Implemente um sistema onde os usuários podem fornecer feedback sobre a qualidade dos resumos e itens de ação gerados. Use este feedback para criar um banco de dados de "exemplos bons" e "exemplos ruins". Antes de gerar um novo resumo, o Claude pode consultar este banco de dados (via RAG) para obter exemplos relevantes, melhorando a qualidade iterativamente. `PROMPT COM RAG: Analise a transcrição abaixo. Use os seguintes exemplos de resumos bem avaliados para guiar sua resposta: [INSERIR_EXEMPLOS_DO_BANCO_DE_DADOS].`
4.  **Integração com Ferramentas de Conteúdo e Conhecimento**: Além de ferramentas de gestão de projetos, integre o assistente para criar e atualizar automaticamente artigos em bases de conhecimento (ex: Notion, Confluence) com as decisões e informações-chave da reunião. Isso transforma reuniões em ativos de conhecimento. `API: POST /confluence/api/content { "title": "Decisões Reunião Projeto Alpha - 27/10", "body": { "storage": { "value": "{{RESUMO_DO_CLAUDE}}", "representation": "wiki" } } }`
5.  **Detecção de Sentimento e Engajamento**: Utilize APIs de análise de sentimento (ex: Google Cloud Natural Language API) na transcrição da reunião para identificar o tom geral da discussão. Isso pode ajudar a gerentes a entender o engajamento da equipe ou identificar potenciais conflitos. `OUTPUT: "Sentimento Geral da Reunião: Neutro, com picos de frustração na discussão sobre prazos."`