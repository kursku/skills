---
name: process-mining
description: "Process Mining — Skill especializada para process mining"
license: MIT
metadata:
  version: 1.0.0
  author: Cafe Code AI
  category: 12-ia-automacao
  updated: 2026-03-01
risk: critical
---

# Process Mining

Esta skill capacita o Claude a aplicar técnicas de Process Mining para otimizar fluxos de trabalho, identificar gargalos e automatizar processos de negócios, usando ferramentas de integração e APIs.

---

## Keywords

*   Descoberta de Processos
*   Conformidade de Processos
*   Otimização de Fluxos
*   Análise de Gargalos
*   Log de Eventos
*   Modelo BPMN
*   Automação Robótica de Processos (RPA)
*   Integração API
*   Ferramentas ETL
*   Mineração de Tarefas
*   Análise de Variantes
*   Automação Inteligente

---

## Quick Start

1.  Coletar logs de eventos de sistemas transacionais (ERP, CRM, sistemas de tickets) via APIs, webhooks ou exportações diretas.
2.  Estruturar os dados de log em um formato padronizado: `(ID do Caso, Nome da Atividade, Timestamp, Recurso, Atributos)`.
3.  Importar o log de eventos para uma ferramenta de Process Mining (e.g., Celonis, Disco, ou script PM4Py em Python).
4.  Visualizar o modelo de processo descoberto e identificar as variantes de processo mais frequentes e suas respectivas durações.
5.  Analisar os desvios do modelo ideal, mapear gargalos e propor pontos de automação e melhoria para o fluxo de trabalho.

---

## Core Workflows

### Workflow 1: Descoberta e Otimização de Gargalos em Processos de Onboarding de Clientes

Este workflow foca em identificar e automatizar pontos de lentidão no processo de onboarding de novos clientes, melhorando a experiência e reduzindo o tempo para o cliente atingir o "valor".

1.  **Coleta de Dados de Log de Eventos**:
    *   **Origem**: Sistemas de CRM (ex: HubSpot, Salesforce), plataforma de e-mail marketing (ex: ActiveCampaign), sistema de suporte (ex: Zendesk), ferramenta de gestão de projetos (ex: Asana).
    *   **Método**:
        *   **APIs**: Utilizar endpoints como `GET /deals/{dealId}/timeline` (HubSpot) ou `GET /api/v2/tickets` (Zendesk) para extrair eventos cronologicamente.
        *   **Webhooks**: Configurar webhooks para disparar eventos em tempo real quando status de negócio mudam no CRM ou e-mails são abertos/clicados no marketing. Exemplo: Webhook no HubSpot para `POST https://seu-webhook.com/process-log` ao mudar o estágio de um negócio para "Cliente Ativo".
        *   **Exportação**: Para sistemas legados, exportar dados em CSV ou Excel e pré-processar.
    *   **Exemplo de Eventos**: "Cliente Criado", "Email de Boas-Vindas Enviado", "Configuração de Conta Iniciada", "Chamada de Onboarding Realizada", "Treinamento Concluído", "Suporte Ativado".

2.  **Estruturação e Pré-processamento do Log**:
    *   **Formato**: Unificar todos os eventos em um arquivo CSV ou XES com colunas mínimas: `Case ID` (ID do cliente), `Activity Name` (nome da ação), `Timestamp` (data e hora do evento), `Resource` (quem executou, e.g., SDR Ana, Sistema Marketing), `Attributes` (e.g., Tipo de Plano, Segmento do Cliente).
    *   **Exemplo de Pré-processamento (Python)**:
        ```python
        import pandas as pd
        from datetime import datetime

        def preprocess_log(df):
            df['Timestamp'] = pd.to_datetime(df['Timestamp'])
            df = df.sort_values(by=['Case ID', 'Timestamp'])
            return df

        # Carregar dados de diferentes fontes
        crm_data = pd.read_csv('hubspot_events.csv')
        email_data = pd.read_csv('activecampaign_events.csv')
        support_data = pd.read_csv('zendesk_events.csv')

        # Consolidar e padronizar
        # ... (lógica para mapear colunas e criar Case ID, Activity, Timestamp, Resource)

        unified_log = pd.concat([crm_data_processed, email_data_processed, support_data_processed])
        unified_log_clean = preprocess_log(unified_log)
        unified_log_clean.to_csv('onboarding_event_log.csv', index=False)
        ```

3.  **Análise de Processos com Ferramenta de Process Mining**:
    *   **Carregamento**: Importar `onboarding_event_log.csv` para Disco, Celonis, ou usar PM4Py.
    *   **Descoberta do Modelo**: Gerar um modelo de processo (e.g., grafo de precedência, BPMN) para visualizar o fluxo real.
        *   Exemplo PM4Py: `import pm4py; log = pm4py.read_xes('onboarding_log.xes'); bpmn_graph = pm4py.discover_bpmn_inductive(log)`.
    *   **Análise de Desempenho**: Identificar os caminhos mais longos, atividades com maior tempo de espera e gargalos.
        *   Foco em transições entre atividades que apresentam alta duração média. Exemplo: "Configuração de Conta Iniciada" -> "Treinamento Concluído" com média de 5 dias, quando a meta é 2 dias.

4.  **Identificação de Oportunidades de Automação**:
    *   **Gargalo**: Se a transição "Email de Boas-Vindas Enviado" para "Configuração de Conta Iniciada" é manual e inconsistente, causando atrasos.
        *   **Automação Proposta**: Criar um cenário no Make.com ou N8N.io que, ao detectar um novo cliente com status "Ativo" no CRM (via webhook), automaticamente:
            1.  Dispara um e-mail de boas-vindas personalizado via API do ActiveCampaign: `POST /api/3/contact_automations/{automation_id}/run`.
            2.  Cria uma tarefa de "Configuração de Conta" no Asana para o CSM responsável via API: `POST /api/1.0/tasks`.
            3.  Envia uma mensagem de notificação para o canal do Slack do time de onboarding.
    *   **Gargalo**: Se a etapa "Solicitação de Documentos Iniciais" é manual e atrasa o "Treinamento Concluído".
        *   **Automação Proposta**: Implementar um chatbot proativo (integrado via API com sistema de CRM) que detecta a necessidade de documentos e envia um formulário ou solicita informações diretamente ao cliente, atualizando o status no CRM via API após o recebimento.

5.  **Implementação e Monitoramento Contínuo**:
    *   Desenvolver e testar as automações em Make/N8N/Zapier.
    *   Configurar dashboards de monitoramento dos KPIs de processo (tempo de ciclo, throughput, taxa de conclusão) para avaliar o impacto das automações.
    *   Continuar coletando logs para novas rodadas de Process Mining e refinamento.

### Workflow 2: Análise de Conformidade e Automação de Exceções em Processos de Aprovação de Despesas

Este workflow aborda a detecção de não conformidades em processos de aprovação financeira e a automação de ações corretivas.

1.  **Coleta de Dados de Log de Eventos**:
    *   **Origem**: Sistema de gestão de despesas (ex: SAP Concur, Expensify), ERP (ex: SAP, Oracle Financials).
    *   **Método**:
        *   **APIs**: `GET /api/v1/expenses` para obter relatórios de despesas e seus status de aprovação.
        *   **Exportação**: Exportar logs de aprovação e status das despesas.
    *   **Exemplo de Eventos**: "Despesa Submetida", "Aprovador Designado", "Aprovação Gerencial", "Aprovação Financeira", "Rejeitada por Política", "Reembolso Processado".

2.  **Estruturação e Pré-processamento do Log**:
    *   **Formato**: `Case ID` (ID do relatório de despesas), `Activity Name`, `Timestamp`, `Resource` (funcionário, gerente, sistema), `Attributes` (valor da despesa, tipo de despesa, política aplicada).

3.  **Definição de Regras de Conformidade**:
    *   **Exemplos**:
        *   "Toda despesa acima de R$ 500,00 deve ter 'Aprovação Gerencial' E 'Aprovação Financeira'."
        *   "Despesas de viagem acima de R$ 1.000,00 devem ser aprovadas por um gerente sênior (Recurso: 'Gerente Sênior X')."
        *   "Nenhuma despesa pode ser 'Reembolso Processado' sem uma etapa de 'Aprovação' prévia."

4.  **Análise de Conformidade com Ferramenta de Process Mining**:
    *   **Carregamento**: Ingerir o log de eventos na ferramenta.
    *   **Verificação de Regras**: Utilizar os recursos de verificação de conformidade da ferramenta para comparar o processo real com as regras definidas.
        *   Identificar casos onde a sequência "Despesa Submetida" -> "Reembolso Processado" ocorre para valores > R$ 500,00 sem as duas aprovações.
        *   Visualizar as variantes não-conformes e suas frequências.

5.  **Automação de Notificações e Ações Corretivas para Não Conformidades**:
    *   **Cenário**: Uma despesa de R$ 700,00 é aprovada por um gerente, mas segue para "Reembolso Processado" sem a "Aprovação Financeira".
    *   **Automação Proposta (Make/N8N)**:
        1.  **Gatilho**: Monitorar o sistema de despesas (via webhook ou API de polling) por eventos de "Reembolso Processado".
        2.  **Condição**: Se o valor da despesa for > R$ 500,00 E o histórico do caso não incluir "Aprovação Financeira".
        3.  **Ação 1 (Notificação)**:
            *   Enviar um e-mail de alerta para o departamento financeiro e o gerente via API (ex: SendGrid): `POST /api/mail/send` com assunto "Não Conformidade - Despesa [ID] Reembolsada Sem Aprovação Financeira".
            *   Enviar uma notificação via Slack/Teams: `POST https://hooks.slack.com/services/...` com detalhes da despesa e o problema.
        4.  **Ação 2 (Correção)**:
            *   Se a política permitir, a automação pode acionar uma API para reverter o status da despesa para "Pendente de Revisão Financeira" ou "Rejeitada" no sistema de despesas: `PUT /api/v1/expenses/{expenseId}/status` com `{"status": "Pending Finance Review"}`.
            *   Um prompt para um chatbot pode ser acionado para o aprovador: "Olá, detectei que a despesa [ID da Despesa] foi aprovada por [Aprovador] sem a [Aprovação Financeira] necessária, pois o valor é R$ [Valor]. Deseja reverter a aprovação ou escalar este caso?"

6.  **Monitoramento Contínuo**:
    *   Acompanhar o índice de conformidade em dashboards.
    *   Registrar as ações corretivas automatizadas e o impacto na redução de não conformidades.

---

## Templates

### Template de Log de Eventos (CSV)

```csv
Case ID,Activity,Timestamp,Resource,Amount,Category,Plan_Type,Client_Segment
ONB-001,Cliente Criado,2023-10-01 09:00:00,SDR Ana,0.00,Onboarding,Enterprise,Large
ONB-001,Email de Boas-Vindas Enviado,2023-10-01 09:05:00,Sistema Marketing,0.00,Onboarding,Enterprise,Large
ONB-001,Configuração de Conta Iniciada,2023-10-02 11:30:00,CSM João,0.00,Onboarding,Enterprise,Large
ONB-001,Chamada de Onboarding Realizada,2023-10-03 10:00:00,CSM João,0.00,Onboarding,Enterprise,Large
ONB-001,Treinamento Concluído,2023-10-05 16:00:00,CSM João,0.00,Onboarding,Enterprise,Large
EXP-023,Despesa Submetida,2023-11-10 14:00:00,Funcionario B,850.00,Viagem,N/A,N/A
EXP-023,Aprovador Designado,2023-11-10 14:05:00,Sistema Financeiro,850.00,Viagem,N/A,N/A
EXP-023,Aprovação Gerencial,2023-11-11 09:00:00,Gerente X,850.00,Viagem,N/A,N/A
EXP-023,Reembolso Processado,2023-11-11 11:00:00,Sistema Pagamentos,850.00,Viagem,N/A,N/A
EXP-024,Despesa Submetida,2023-11-12 10:00:00,Funcionario C,300.00,Material Escritório,N/A,N/A
EXP-024,Aprovador Designado,2023-11-12 10:05:00,Sistema Financeiro,300.00,Material Escritório,N/A,N/A
EXP-024,Aprovação Gerencial,2023-11-12 14:00:00,Gerente Y,300.00,Material Escritório,N/A,N/A
EXP-024,Reembolso Processado,2023-11-12 16:00:00,Sistema Pagamentos,300.00,Material Escritório,N/A,N/A
```

### Prompt para Chatbot de Otimização de Processo (com dados de Process Mining)

```
Você é um assistente de otimização de processos. Analisei os dados de Process Mining para o processo de "Atendimento ao Cliente" e identifiquei um gargalo significativo que afeta 30% dos casos.

O caminho mais frequente (70% dos casos) é:
1. Cliente Abre Ticket (Duração Média: 0 horas)
2. Atendente Designado (Duração Média: 0.5 horas)
3. Resposta Inicial Enviada (Duração Média: 1 hora)
4. Solicitação de Mais Informações (Duração Média: 2 horas) -> AQUI ESTÁ O GARGALO!
5. Cliente Fornece Informações (Duração Média: 8 horas)
6. Resolução do Ticket (Duração Média: 4 horas)

A transição de "Solicitação de Mais Informações" para "Cliente Fornece Informações" tem um tempo médio de 8 horas, sendo o maior tempo de espera no processo. Além disso, 30% dos tickets necessitam de *duas ou mais* rodadas de "Solicitação de Mais Informações", indicando falta de clareza inicial.

Com base nesta análise, proponha 3 ações concretas e automatizáveis para reduzir este gargalo e o tempo total de resolução do ticket. Inclua sugestões de como usar APIs, webhooks ou integrações com Make/N8N/Zapier e como um chatbot ou IA pode participar.
```

---

## Checklist

-   [x] Dados de log de eventos extraídos de sistemas transacionais e formatados (ID do Caso, Atividade, Timestamp, Recurso, Atributos).
-   [x] Ferramenta de Process Mining (ou script PM4Py) configurada e com dados carregados.
-   [x] Modelo de processo descoberto e visualizado (e.g., grafo de precedência, BPMN) para identificação de fluxos reais.
-   [x] Principais variantes de processo identificadas, quantificadas e analisadas por frequência e desempenho.
-   [x]