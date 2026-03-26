---
name: voice-bot-design
description: "Voice Bot Design — Skill especializada para voice bot design"
license: MIT
metadata:
  version: 1.0.0
  author: Cafe Code AI
  category: 12-ia-automacao
  updated: 2026-03-01
risk: safe
---

# Voice Bot Design
Esta skill capacita o Claude a projetar, prototipar e otimizar interfaces conversacionais de voz, focando em usabilidade, fluxo natural e integração com plataformas de automação.

---

## Keywords
IVR, ASR, TTS, NLU, VUI, Voice UX, Design Conversacional, Diálogo de Voz, Fluxogramas de Voz, Teste de Usabilidade de Voz, Automação por Voz, Integração de APIs de Voz.

---

## Quick Start
1.  **Mapear Jornada do Usuário por Voz**: Esboçar o caminho crítico que um usuário percorre para resolver uma necessidade específica através do bot de voz, identificando pontos de decisão e expectativas de fala. Ex: `(Início: "Quero agendar") -> (Bot: "Qual serviço?") -> (Usuário: "Limpeza") -> (Bot: "Data e Hora?") -> (Fim: "Agendamento confirmado")`.
2.  **Definir Gramática de Interação**: Criar listas de frases e palavras-chave que o usuário provavelmente usará para cada intenção, alimentando o modelo de NLU (Natural Language Understanding). Ex: Para a intenção `solicitar_saldo`, frases como `("qual meu saldo", "quanto tenho na conta", "saldo atual")`.
3.  **Prototipar Fluxo de Diálogo no Voiceflow**: Construir um protótipo inicial do bot de voz utilizando uma ferramenta como Voiceflow ou Landbot, configurando prompts de TTS e capturas de ASR para simular a interação completa.
4.  **Testar com Usuários Reais (Wizard of Oz)**: Conduzir testes de usabilidade com participantes reais, onde um humano simula a resposta do bot para coletar feedback sobre a naturalidade do diálogo e a clareza dos prompts, antes de codificar.
5.  **Integrar com Webhooks para Automação Externa**: Configurar um webhook na plataforma do bot de voz (ex: Dialogflow CX, Amazon Lex) para disparar um fluxo no Make.com após uma intenção específica, como `agendar_chamada`, enviando os dados coletados.

---

## Core Workflows

### Workflow 1: Criação de Fluxo de Agendamento de Serviço por Voz com Integração Make.com

Este workflow detalha a construção de um módulo de agendamento de serviço via bot de voz, integrando com um sistema externo de calendário através do Make.com.

**Passos Detalhados:**

1.  **Análise de Intenção e Entidades**:
    *   **Intenção Principal**: `agendar_servico`.
    *   **Entidades Necessárias**: `tipo_servico` (e.g., "limpeza", "manutenção", "instalação"), `data` (e.g., "amanhã", "próxima terça"), `hora` (e.g., "10 da manhã", "14h"), `nome_cliente`, `telefone_cliente`.
    *   **Exemplo de Frases de Treinamento (Dialogflow CX)**:
        *   "Gostaria de agendar uma `limpeza` para `amanhã` às `10 da manhã`."
        *   "Preciso de uma `manutenção` na `próxima quinta` à `tarde`."
        *   "Quero marcar uma `instalação`."

2.  **Desenho do Diálogo no Voiceflow/Dialogflow CX**:
    *   **Prompt Inicial**: "Em que tipo de serviço posso ajudar com o agendamento?"
    *   **Captura `tipo_servico`**:
        *   `User`: "Uma limpeza."
        *   `Bot`: "Certo, uma limpeza. Para qual data e hora?"
    *   **Captura `data` e `hora`**:
        *   `User`: "Para `quarta-feira` que vem, às `9h`."
        *   `Bot`: "Confirmando: agendamento de `limpeza` para `quarta-feira` que vem às `9h`. Seu nome, por favor?"
    *   **Captura `nome_cliente`**:
        *   `User`: "Meu nome é `Ana Silva`."
        *   `Bot`: "Obrigado, Ana. E um telefone para contato?"
    *   **Captura `telefone_cliente`**:
        *   `User`: "É `98765-4321`."
        *   `Bot`: "Perfeito. Irei agendar sua limpeza para quarta-feira que vem às 9h, em nome de Ana Silva, telefone 98765-4321. Posso confirmar?"
    *   **Confirmação Final**:
        *   `User`: "Sim, pode confirmar."
        *   `Bot`: "Agendamento realizado! Em breve você receberá uma confirmação por SMS. Tenha um ótimo dia!"

3.  **Configuração de Webhook de Fulfillment (Dialogflow CX)**:
    *   Após a confirmação final (`sim, pode confirmar`), configurar um webhook que envie os parâmetros coletados (`tipo_servico`, `data`, `hora`, `nome_cliente`, `telefone_cliente`) para um endpoint HTTP no Make.com.
    *   **Exemplo de Payload JSON enviado pelo Dialogflow CX para o Make.com:**
        ```json
        {
          "sessionInfo": {
            "parameters": {
              "tipo_servico": "limpeza",
              "data": "2024-10-23T09:00:00-03:00",
              "nome_cliente": "Ana Silva",
              "telefone_cliente": "987654321"
            }
          },
          "fulfillmentInfo": {
            "tag": "agendar_servico_finalizado"
          }
        }
        ```

4.  **Criação de Cenário no Make.com**:
    *   **Módulo 1: Webhooks - Custom Webhook**: Recebe o JSON do Dialogflow CX.
    *   **Módulo 2: Google Calendar - Create an Event**: Mapeia os dados do webhook para criar um evento no Google Agenda da empresa.
        *   **Título**: `Agendamento: {{1.sessionInfo.parameters.tipo_servico}} - {{1.sessionInfo.parameters.nome_cliente}}`
        *   **Início**: `{{1.sessionInfo.parameters.data}}` (parsear se necessário)
        *   **Fim**: `{{addHours(1.sessionInfo.parameters.data; 1)}}` (ex: 1 hora de duração)
        *   **Descrição**: `Telefone: {{1.sessionInfo.parameters.telefone_cliente}}`
    *   **Módulo 3 (Opcional): Twilio - Send an SMS**: Envia uma confirmação por SMS para o cliente.
        *   **To**: `{{1.sessionInfo.parameters.telefone_cliente}}`
        *   **Message**: "Olá {{1.sessionInfo.parameters.nome_cliente}}, seu agendamento de {{1.sessionInfo.parameters.tipo_servico}} foi confirmado para {{formatDate(1.sessionInfo.parameters.data; "DD/MM/YYYY HH:mm")}}. Atenciosamente, [Sua Empresa]."

### Workflow 2: Otimização de Resposta em Casos de Não-Entendimento (No-Match) e Fallback

Este workflow foca em refinar a experiência do usuário quando o bot de voz não consegue entender a fala (No-Match) ou a intenção (Fallback), evitando frustração e direcionando para soluções.

**Passos Detalhados:**

1.  **Análise de Logs de No-Match**:
    *   Exportar logs de interações do bot de voz (ex: Dialogflow CX Analytics, Amazon Lex Conversation Logs) e filtrar por eventos de "No-Match" ou "Fallback".
    *   Identificar padrões nas transcrições de fala que não foram entendidas. Usuários estão usando gírias? Pronunciando mal termos técnicos? Há muito ruído de fundo?
    *   **Exemplo de Log Bruto**: `User: "Preciso de um s'gunda via da minha conta"` -> `Bot: [No-Match]` (Provável erro de ASR ou falta de treinamento de NLU para "segunda via").

2.  **Ajuste da Sensibilidade do ASR e do NLU**:
    *   **ASR (Automatic Speech Recognition)**: Em plataformas como Google Cloud Speech-to-Text ou AWS Transcribe, ajustar modelos de linguagem personalizados com vocabulário específico do domínio (e.g., nomes de produtos, termos técnicos). Adicionar "segunda via" como termo prioritário.
    *   **NLU (Natural Language Understanding)**: Adicionar mais frases de treinamento para intenções existentes que falharam. Criar novas intenções se um padrão de fala recorrente não estiver sendo mapeado corretamente.
    *   **Exemplo de Treinamento NLU (Dialogflow CX)**:
        *   `Intenção: solicitar_segunda_via`
        *   `Frases`: "quero a segunda via", "minha conta", "boleto atrasado", "preciso do extrato", "manda o PDF da fatura".

3.  **Implementação de Estratégias de Repetição e Refraseamento**:
    *   **Primeiro Fallback**: "Desculpe, não entendi. Você pode repetir de outra forma, por favor?" (Com um limite de 2 repetições).
    *   **Segundo Fallback**: "Ainda não consegui entender. Poderia me dizer qual é o assunto principal que você gostaria de resolver?" (Prompt mais amplo para tentar capturar um tópico geral).
    *   **Exemplo de Prompt (TTS)**: `tts_prompt: "Não compreendi. Você disse 'assistência técnica' ou 'assistência médica'?"` (Usar quando há ambiguidade entre duas intenções próximas).

4.  **Encaminhamento Inteligente para Agente Humano ou Outro Canal**:
    *   Após o segundo ou terceiro fallback sem sucesso, oferecer opções claras de escalonamento.
    *   **Opção 1 (Agente Humano)**: "Parece que não estou conseguindo te ajudar. Gostaria de falar com um de nossos atendentes humanos? Diga 'sim' ou 'falar com atendente'."
        *   Integrar com um módulo de transferência de chamada (ex: Twilio Voice, Genesys Cloud) ou um sistema de fila.
    *   **Opção 2 (Outro Canal)**: "Se preferir, posso enviar um link para nosso chat online ou enviar um SMS com o número do nosso WhatsApp. Qual opção você prefere?"
        *   Disparar um webhook para um cenário no N8N que envia o link do chat por SMS (via Twilio) ou registra uma solicitação de contato no CRM.

5.  **Monitoramento Contínuo e Retreinamento**:
    *   Configurar alertas para altas taxas de no-match.
    *   Revisar logs semanalmente para identificar novas oportunidades de treinamento de NLU e ASR.
    *   A cada 2-4 semanas, reavaliar o desempenho do modelo com novos dados coletados das interações reais.

---

## Templates

### Template de Prompt para Coleta de Entidade (Data e Hora)

```
{
  "prompt_text": "Certo, entendi. Para qual data e hora você gostaria de agendar? Por exemplo, 'próxima terça às 10 da manhã' ou 'dia 15 de agosto às 14h'.",
  "expected_entities": ["@sys.date", "@sys.time"],
  "reprompt_text": "Desculpe, não entendi a data ou a hora. Poderia repetir, por favor?",
  "max_attempts": 2,
  "fallback_action": "escalate_to_human"
}
```

### Template de Mensagem de Confirmação Final (TTS)

```
{
  "tts_message": "Confirmando seu pedido: {item_principal} para {data_agendamento} às {hora_agendamento}, em nome de {nome_cliente}. Seu telefone de contato é {telefone_cliente}. Confirma as informações?",
  "expected_responses": ["sim", "não", "corrigir"],
  "on_confirm": {
    "action": "trigger_webhook",
    "webhook_name": "final_booking_confirmation",
    "payload_variables": ["item_principal", "data_agendamento", "hora_agendamento", "nome_cliente", "telefone_cliente"]
  },
  "on_deny": {
    "action": "recollect_information",
    "start_from_step": "reconfirm_all_details"
  },
  "on_correct": {
    "action": "recollect_information",
    "start_from_step": "ask_which_info_to_correct"
  }
}
```

---

## Checklist

- [x]  Mapeamento completo da jornada do usuário por voz para casos de uso chave.
- [x]  Definição clara das intenções e entidades para cada fluxo de voz.
- [x]  Gramáticas de fala (ASR) e treinamento de NLU otimizados para termos específicos do domínio e sotaques regionais.
- [x]  Design de diálogos com prompts concisos, diretos e que evitam ambiguidades.
- [x]  E