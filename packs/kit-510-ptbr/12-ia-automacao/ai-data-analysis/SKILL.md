---
name: ai-data-analysis
description: "Ai Data Analysis — Skill especializada para ai data analysis com foco em automação, APIs e prompts."
license: MIT
metadata:
  version: 1.0.0
  author: Cafe Code AI
  category: 12-ia-automacao
  updated: 2026-03-01
risk: offensive
---

# Ai Data Analysis

Esta skill capacita o Claude a atuar como um especialista em análise de dados orientada por IA, integrando-se a sistemas de automação (Make/N8N/Zapier), APIs e engenharia de prompts para extrair insights, detectar padrões e automatizar relatórios em tempo real.

---

## Keywords

Análise Preditiva, Processamento de Linguagem Natural (PLN) para Dados, Automação de Insights, ETL com IA, Modelagem de Tópicos, Reconhecimento de Padrões, Webhooks de Dados, Ingestão de Dados via API, Prompt Engineering para Insights, Visualização Automatizada, Detecção de Anomalias, Análise de Sentimento.

---

## Quick Start

1.  **Configurar Conector de Dados**: Escolha uma fonte de dados (ex: planilha Google Sheets, CRM via API, webhook de formulário) e estabeleça a conexão inicial no Make/N8N.
2.  **Estruturar Prompt Inicial de Análise**: Crie um prompt detalhado para o Claude que inclua o contexto dos dados, a pergunta de análise e o formato de saída desejado (ex: JSON, texto sumário).
3.  **Testar Fluxo Básico de API**: Envie um pequeno conjunto de dados de teste para a API do Claude via Make/N8N e valide a resposta inicial.
4.  **Processar Resposta da IA**: Configure o módulo subsequente no Make/N8N para parsear a resposta do Claude e encaminhar os insights para um destino (ex: Slack, Google Sheets).

---

## Core Workflows

### Workflow 1: Análise Automatizada de Feedback de Clientes via PLN e Webhook

Este fluxo automatiza a coleta, análise de sentimento e extração de tópicos de feedback de clientes, transformando dados brutos em insights acionáveis sem intervenção manual.

**Passos Detalhados:**

1.  **Recepção de Feedback via Webhook**:
    *   **Contexto**: Um formulário de feedback (ex: Typeform, Google Forms) ou sistema de CRM envia novas entradas para um webhook.
    *   **Configuração Make/N8N**: Crie um módulo "Webhook" no Make/N8N/Zapier. Copie a URL gerada.
    *   **Exemplo de Webhook Payload (JSON)**:
        ```json
        {
          "id_feedback": "FB-20231026-001",
          "texto_feedback": "O aplicativo está lento demais e a interface é confusa. Não consigo encontrar o que preciso.",
          "data_envio": "2023-10-26T14:30:00Z",
          "cliente_id": "CLI-4567"
        }
        ```
    *   **Configuração da Fonte**: No Typeform ou Zapier, configure a ação para enviar os dados do formulário para a URL do webhook do Make/N8N.

2.  **Preparação e Envio de Dados para LLM**:
    *   **Contexto**: O feedback bruto precisa ser formatado para uma análise eficaz por um modelo de linguagem grande (LLM).
    *   **Configuração Make/N8N**: Após o módulo Webhook, adicione um módulo "Text Aggregator" ou "Code" para formatar os dados.
    *   **Prompt Real para Análise de Sentimento e Tópicos**:
        ```
        Você é um analista de dados especialista em feedback de clientes.
        Analise o seguinte feedback do cliente e forneça:
        1. O sentimento geral (Positivo, Negativo, Neutro).
        2. Tópicos principais mencionados (liste até 3).
        3. Uma breve justificativa para o sentimento e os tópicos identificados.

        Formato de saída esperado (JSON):
        {
          "sentimento": "[sentimento]",
          "topicos": ["[topico1]", "[topico2]"],
          "justificativa": "[justificativa]"
        }

        Feedback:
        {{texto_feedback}}
        ```
        *   `{{texto_feedback}}` seria substituído pelo dado do webhook.
    *   **Módulo LLM**: Adicione um módulo "Claude" ou "OpenAI" e configure a chamada de API usando o prompt acima e o `texto_feedback` do webhook.

3.  **Processamento e Armazenamento/Alerta de Insights**:
    *   **Contexto**: A resposta do LLM precisa ser parseada e os insights encaminhados para visualização ou alerta.
    *   **Configuração Make/N8N**: Use um módulo "JSON Parser" para extrair `sentimento`, `topicos` e `justificativa` da resposta do LLM.
    *   **Destino dos Dados**:
        *   **Google Sheets**: Adicione um módulo "Google Sheets" para inserir uma nova linha com `id_feedback`, `data_envio`, `sentimento`, `topicos` e `justificativa`.
        *   **Slack**: Para feedback negativo, adicione um módulo "Slack" para enviar uma notificação para o canal de suporte com os detalhes do feedback e a análise da IA.

### Workflow 2: Detecção de Anomalias em Séries Temporais Financeiras com IA e Automação

Este fluxo monitora dados financeiros (ex: vendas diárias, preços de ações) e utiliza IA para identificar padrões incomuns ou anomalias, disparando alertas proativos.

**Passos Detalhados:**

1.  **Coleta de Dados Agendada via API**:
    *   **Contexto**: Dados históricos de vendas diárias ou preços de ações são periodicamente coletados de uma API.
    *   **Configuração Make/N8N**: Crie um módulo "Schedule" para executar o fluxo diariamente às 09:00 AM.
    *   **Módulo API**: Adicione um módulo "HTTP Request" para chamar uma API financeira (ex: Alpha Vantage, um CRM interno).
    *   **Exemplo de Chamada API (GET)**: `GET https://api.exemplo.com/vendas_diarias?data_inicio={{data_7d_atras}}&data_fim={{hoje}}`
    *   **Exemplo de Resposta API (JSON)**:
        ```json
        {
          "vendas": [
            {"data": "2023-10-20", "valor": 1200.50},
            {"data": "2023-10-21", "valor": 1150.20},
            {"data": "2023-10-22", "valor": 1300.75},
            {"data": "2023-10-23", "valor": 1280.10},
            {"data": "2023-10-24", "valor": 1220.00},
            {"data": "2023-10-25", "valor": 1180.30},
            {"data": "2023-10-26", "valor": 550.90}
          ]
        }
        ```

2.  **Pré-processamento e Envio para LLM**:
    *   **Contexto**: Os dados brutos da API precisam ser formatados em uma string clara para o LLM identificar anomalias.
    *   **Configuração Make/N8N**: Use um módulo "Code" ou "Text Aggregator" para criar uma string formatada com os dados da série temporal.
    *   **Prompt Real para Detecção de Anomalias**:
        ```
        Você é um analista de dados financeiros especializado em detecção de anomalias.
        Analise a seguinte série temporal de vendas diárias.
        Identifique se o último valor da série é uma anomalia em comparação com os valores anteriores.
        Justifique sua resposta com base nos dados fornecidos.

        Série Temporal de Vendas Diárias:
        Data, Valor
        2023-10-20, 1200.50
        2023-10-21, 1150.20
        2023-10-22, 1300.75
        2023-10-23, 1280.10
        2023-10-24, 1220.00
        2023-10-25, 1180.30
        2023-10-26, 550.90

        Formato de saída esperado (JSON):
        {
          "anomalia_detectada": [true/false],
          "ultimo_valor": [valor],
          "media_historica_recente": [valor],
          "desvio_padrao_recente": [valor],
          "justificativa": "[justificativa da anomalia]"
        }
        ```
    *   **Módulo LLM**: Envie a string formatada com o prompt para a API do Claude.

3.  **Disparo de Alerta Condicional**:
    *   **Contexto**: Se uma anomalia for detectada, um alerta deve ser enviado imediatamente.
    *   **Configuração Make/N8N**: Use um módulo "JSON Parser" para extrair `anomalia_detectada` e `justificativa`.
    *   **Módulo Roteador/Filtro**: Adicione um módulo "Router" ou "Filter" para criar um caminho condicional.
        *   **Condição**: `anomalia_detectada` é `true`.
    *   **Alerta Slack/Email**: Se a condição for verdadeira, use um módulo "Slack" ou "Email" para enviar um alerta contendo a justificativa da anomalia e o valor detectado.
        *   **Exemplo de Mensagem Slack**: "⚠️ **ALERTA DE ANOMALIA DE VENDAS** ⚠️\nO valor de vendas de hoje ({{ultimo_valor}}) é significativamente inferior à média. A IA detectou uma anomalia. Justificativa: {{justificativa}}."

---

## Templates

### Template de Prompt para Resumo e Extração de Entidades

```
Você é um especialista em análise de documentos e extração de informações.
Dado o seguinte texto, extraia as seguintes entidades em formato JSON:
1. Nomes de pessoas.
2. Nomes de organizações.
3. Datas mencionadas.
4. Locais.
5. Um resumo conciso do texto (máximo 50 palavras).

Texto:
"A reunião anual da Tech Solutions, realizada em São Paulo no dia 15 de março de 2024, contou com a presença de Maria Silva, CEO da Inovatech, e João Pereira, diretor de P&D da empresa. Discutiu-se o lançamento do novo produto 'Alpha', previsto para o segundo semestre."

Formato de saída esperado (JSON):
{
  "pessoas": ["Maria Silva", "João Pereira"],
  "organizacoes": ["Tech Solutions", "Inovatech"],
  "datas": ["15 de março de 2024"],
  "locais": ["São Paulo"],
  "resumo": "A reunião anual da Tech Solutions em São Paulo, 15 de março de 2024, com Maria Silva (Inovatech) e João Pereira, discutiu o lançamento do produto 'Alpha'."
}
```

### Template de Configuração de Webhook para Ingestão de Dados de Logs

```json
{
  "timestamp": "2023-10-26T14:45:00Z",
  "service": "api-gateway",
  "level": "ERROR",
  "message": "Falha na autenticação do usuário 'user_xpto' do IP '203.0.113.42'. Token expirado.",
  "request_id": "REQ-789012",
  "user_agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/118.0.0.0 Safari/537.36"
}
```

---

## Checklist

- [x] Validação do esquema de dados recebidos via webhook ou API antes do processamento pela IA.
- [x] Otimização da contagem de tokens em prompts para reduzir custos e latência da API.
- [x] Implementação de lógica de re-tentativa (retry logic) para chamadas de API do LLM em caso de falhas transitórias.
- [x] Monitoramento da latência das respostas do LLM e dos tempos de execução dos fluxos de automação.
- [x] Versionamento de prompts de análise para rastrear melhorias e regressões nos insights da IA.
- [x] Estratégia de cache para resultados de LLM em análises repetitivas de dados estáticos.
- [x] Configuração de alertas automáticos para desvios significativos nas métricas ou anomalias detectadas.
- [x] Teste de resiliência de fluxos de automação com volumes de dados acima do esperado.
- [x] Definição de limites de custo para o uso da API do LLM para evitar surpresas na fatura.
- [x] Tratamento de erros para respostas inesperadas ou incompletas da API do LLM.

---

## Métricas de Referência

| Métrica                         | Benchmark (Indústria) | Meta (Projeto)         |
|---------------------------------|-----------------------|------------------------|
| Acurácia de Classificação (PLN) | > 85%                 | > 92%                  |
| Tempo de Processamento/Análise  | < 5 segundos          | < 2 segundos           |
| Custo por Análise (tokens)      | < $0.001              | < $0.0005              |
| Redução de Erros Manuais        | > 70%                 | > 85%                  |
| F1-Score Detecção Anomalias     | > 0.75                | > 0.88                 |
| Cobertura de Fontes de Dados    | > 80%                 | > 95%                  |

---

## Erros Comuns

1.  **Overfitting em Prompts**: Criar prompts excessivamente específicos para um conjunto de dados, resultando em desempenho fraco quando novos dados, ligeiramente diferentes, são introduzidos.
    *   **Como evitar**: Utilize prompts mais flexíveis e genéricos. Teste o prompt com uma variedade de dados de teste (incluindo edge cases) antes de colocar em produção. Exemplo: Em vez de "Analise o sentimento desta reclamação sobre o app lento", use "Analise o sentimento geral deste feedback do cliente".

2.  **Latência Excessiva da API do LLM**: Atrasos significativos na obtenção de respostas do LLM, impactando a reatividade de fluxos em tempo real ou em massa.
    *   **Como evitar**: Implemente chamadas assíncronas quando possível. Considere o uso de modelos LLM menores para tarefas específicas que exigem baixa latência. Otimize o tamanho do prompt e do input de dados para reduzir o número de tokens processados. Utilize uma estratégia de "batch processing" para enviar múltiplos itens de dados em uma única chamada de API quando a latência por item não for crítica.

3.  **Ingestão de Dados Inconsistente**: Dados recebidos via webhooks ou APIs que variam em formato, tipo ou completude, causando falhas no processamento ou análises incorretas pela IA.
    *   **Como evitar**: Implemente validação de esquema rigorosa nos módulos iniciais do Make/N8N. Use JSON Schema para definir o formato esperado e rejeite dados que não o conformem. Inclua etapas de tratamento de erros e transformação de dados para normalizar os inputs antes de enviar para o LLM. Exemplo: Um módulo "Set multiple variables" no N8N para padronizar nomes de campos (ex: `feedback_text` para `texto_feedback`).

---

## Dicas Avançadas

1.  **Chain-of-Thought Prompting para Análises Complexas**: Para análises que exigem múltiplos passos de raciocínio, instrua a IA a "pensar alto" ou a detalhar seus passos antes de dar a resposta final. Isso melhora a acurácia e a interpretabilidade.
    *   **Exemplo Prático**: Em vez de pedir "Classifique este email como spam ou não spam", peça "Analise este email passo a passo para determinar se é spam. Primeiro, identifique a origem. Segundo, procure por palavras-chave suspeitas. Terceiro, avalie a estrutura da frase. Finalmente, classifique-o como spam ou não spam e justifique."

2.  **Uso de Embeddings para Similaridade Semântica**: Para tarefas como recomendação de conteúdo, agrupamento de documentos ou busca semântica, gere embeddings (vetores numéricos) de textos usando um modelo de embedding e compare a similaridade entre eles. Isso é mais eficiente e preciso que a busca por palavras-chave.
    *   **Exemplo Prático**: Use a API de embeddings do Claude/OpenAI para gerar um vetor para cada feedback de cliente. Armazene esses vetores em um banco de dados vetorial. Ao receber um novo feedback, gere seu embedding e encontre os feedbacks mais "próximos" semanticamente para identificar tendências ou problemas recorrentes.

3.  **Human-in-the-Loop (HITL) para Validação e Treinamento**: Integre um processo onde um humano revisa e corrige uma amostra das análises da IA. Essas correções podem ser usadas para refinar prompts, ajustar configurações ou até mesmo para fine-tuning de modelos menores.
    *   **Exemplo Prático**: Após a IA classificar 100 feedbacks, envie 10 aleatórios para revisão manual em uma planilha Google Sheets. Se houver discrepâncias, use o feedback corrigido para aprimorar o prompt da IA.

4.  **Enriquecimento de Dados Contextuais com APIs Externas**: Antes de enviar dados para o LLM, enriqueça-os com informações adicionais de APIs externas para fornecer mais contexto à análise.
    *   **Exemplo Prático**: Ao analisar um endereço de cliente, use uma API de geocodificação (ex: Google Maps API) para obter coordenadas geográficas e dados demográficos da área. Em seguida, envie "Endereço: [endereço], Latitude: [lat], Longitude: [lon], Demografia: [dados demográficos]" para o LLM para uma análise de segmentação mais rica.

5.  **Monitoramento de Drift de Modelos (Prompt Drift)**: Monitore a performance da IA ao longo do tempo. Se a qualidade dos insights começar a degradar, pode ser um sinal de que os dados de entrada mudaram ou que o prompt precisa ser ajustado.
    *   **Exemplo Prático**: Periodicamente, re-avalie um conjunto de dados de teste fixo com o prompt atual. Compare os resultados com as respostas ideais pré-definidas. Se a acurácia cair abaixo de um limiar (ex: 5%), acione um alerta para revisão do prompt ou do modelo.