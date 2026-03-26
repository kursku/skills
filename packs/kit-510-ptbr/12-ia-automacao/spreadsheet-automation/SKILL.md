---
name: spreadsheet-automation
description: "Spreadsheet Automation — Skill especializada para spreadsheet automation"
license: MIT
metadata:
  version: 1.0.0
  author: Cafe Code AI
  category: 12-ia-automacao
  updated: 2026-03-01
risk: safe
---

# Spreadsheet Automation

Esta skill capacita o Claude a projetar, implementar e otimizar fluxos de automação de planilhas usando ferramentas no-code/low-code, APIs e modelos de linguagem para processamento e análise de dados.

---

## Keywords

Google Sheets API, Make.com Flows, N8N Workflows, Zapier Integrations, Google Apps Script, Webhook Processing, Data Transformation, Claude Prompts for Spreadsheets, API Authentication (OAuth 2.0), CSV Parsing, Relatórios Automatizados, Excel Online Automation.

---

## Quick Start

1.  **Conectar Planilha à Plataforma de Automação**: Configure uma conexão entre o Google Sheets (ou MS Excel Online) e sua ferramenta de automação (Make/N8N/Zapier) usando um módulo de "Watch New Rows" ou "New Spreadsheet Row" para monitorar entradas.
2.  **Criar Webhook de Entrada**: Adicione um módulo "Webhook" na sua automação para receber dados de formulários (Typeform, Google Forms) ou outros sistemas externos que disparam eventos.
3.  **Mapear Campos e Dados**: Utilize a interface visual da plataforma para mapear colunas da planilha para os dados recebidos do webhook ou para dados gerados por uma API ou por uma resposta do Claude.
4.  **Testar Fluxo com Dados Reais**: Execute a automação com um registro de teste completo, verificando se os dados são corretamente lidos, transformados e escritos na planilha de destino, validando cada etapa.

---

## Core Workflows

### Workflow 1: Automação de Feedback de Clientes e Atualização de CRM em Planilha

*   **Cenário**: Uma empresa coleta feedback de clientes via um formulário online (Typeform) e precisa registrar as respostas em uma planilha de CRM, categorizar o sentimento do feedback usando o Claude e alertar a equipe para avaliações negativas.
*   **Passos Detalhados**:
    1.  **Trigger de Webhook (Typeform)**: Configure um webhook no Typeform para enviar dados de novas submissões para um módulo "Webhook" no Make.com (ou N8N/Zapier). O webhook do Typeform enviará um payload JSON contendo as respostas.
        *   *Exemplo de Payload recebido (simplificado)*:
            ```json
            {
              "form_id": "form_abc123",
              "submission_id": "sub_xyz789",
              "answers": [
                {"field_id": "name_field", "type": "text", "text": "Ana Silva"},
                {"field_id": "email_field", "type": "email", "email": "ana.silva@exemplo.com"},
                {"field_id": "feedback_field", "type": "long_text", "text": "O suporte foi demorado e não resolveu meu problema. Péssima experiência!"},
                {"field_id": "rating_field", "type": "number", "number": 2}
              ]
            }
            ```
    2.  **Extração e Transformação de Dados**: Use módulos de "Parse JSON" ou funções de mapeamento para extrair `name`, `email`, `feedback_text` e `rating` do payload do Typeform.
        *   *Mapeamento no Make.com*: Acessar `{{1.answers[].text}}` para o campo de feedback específico.
    3.  **Análise de Sentimento com Claude API**: Envie o texto do feedback para o Claude para análise de sentimento.
        *   *Prompt Claude Real para Análise de Sentimento*:
            ```
            Você é um analista de sentimentos de feedback de clientes.
            Analise o seguinte feedback e retorne APENAS um dos seguintes rótulos: "Positivo", "Neutro", "Negativo".

            Feedback: "O suporte foi demorado e não resolveu meu problema. Péssima experiência!"

            Rótulo:
            ```
        *   *Resposta esperada do Claude*: `Negativo`
    4.  **Atualização da Planilha Google Sheets**: Use um módulo "Add a Row" ou "Update a Row" do Google Sheets.
        *   *Planilha de Exemplo*: "CRM Feedback Clientes" com colunas: `ID Submissão`, `Nome Cliente`, `Email`, `Feedback`, `Classificação`, `Sentimento`, `Status Alerta`.
        *   *Campos a preencher no Google Sheets*:
            *   `ID Submissão`: `{{submission_id}}` (do Typeform)
            *   `Nome Cliente`: `{{name}}` (do Typeform)
            *   `Email`: `{{email}}` (do Typeform)
            *   `Feedback`: `{{feedback_text}}` (do Typeform)
            *   `Classificação`: `{{rating}}` (do Typeform)
            *   `Sentimento`: `{{Claude_response_sentiment}}` (da API do Claude)
            *   `Status Alerta`: `PENDENTE` (se o sentimento for 'Negativo' ou a classificação for menor ou igual a 3)
    5.  **Notificação Condicional (Slack/Email)**: Adicione um roteador (router) ou filtro na automação para verificar o `Sentimento` ou a `Classificação`. Se for 'Negativo' ou `<= 3`, envie uma mensagem para o Slack da equipe de suporte ou um email para o gerente.
        *   *Mensagem Slack Exemplo*:
            ```
            ALERTA DE FEEDBACK NEGATIVO URGENTE!
            Cliente: Ana Silva (ana.silva@exemplo.com)
            Feedback: "O suporte foi demorado e não resolveu meu problema. Péssima experiência!"
            Classificação: 2/5
            Sentimento: Negativo
            Ação: Verifique o registro na planilha "CRM Feedback Clientes" para follow-up imediato.
            ```

### Workflow 2: Geração de Resumos Executivos de Dados de Vendas em Planilha

*   **Cenário**: Uma planilha "Vendas Mensais" contém dados diários de vendas (Produto, Quantidade, Preço Unitário, Data, Vendedor). É preciso gerar um resumo executivo mensal automaticamente, destacando tendências e insights, usando o Claude, e enviá-lo por email.
*   **Passos Detalhados**:
    1.  **Agendamento de Execução (Scheduler)**: Configure a automação para rodar no primeiro dia útil de cada mês às 9h AM.
    2.  **Leitura de Dados da Planilha Google Sheets**: Use um módulo "Get Multiple Ranges" ou "Search Rows" para ler todos os dados de vendas do mês anterior, filtrando pela coluna 'Data'.
        *   *Exemplo de Dados Lidos (JSON interno)*:
            ```json
            [
              {"Data": "2024-02-01", "Produto": "Widget A", "Quantidade": 10, "PrecoUnitario": 50.00, "Vendedor": "Carlos"},
              {"Data": "2024-02-01", "Produto": "Gadget B", "Quantidade": 5, "PrecoUnitario": 120.00, "Vendedor": "Maria"},
              {"Data": "2024-02-29", "Produto": "Widget A", "Quantidade": 8, "PrecoUnitario": 50.00, "Vendedor": "Carlos"}
            ]
            ```
    3.  **Pré-processamento e Agregação (Data Transformer)**: Use módulos de "Array Aggregator" ou "Code" (JavaScript/Python no N8N) para somar vendas por produto, por vendedor, calcular total de receita e média de vendas diárias.
        *   *Exemplo de Dados Agregados (interno na automação)*:
            ```json
            {
              "TotalVendasMes": 152300.00,
              "ProdutosMaisVendidos": [{"Produto": "Widget A", "Receita": 65000.00}, {"Produto": "Gadget B", "Receita": 45000.00}],
              "VendedoresTop": [{"Vendedor": "Carlos", "Receita": 80000.00}, {"Vendedor": "Maria", "Receita": 50000.00}],
              "MediaVendasDiarias": 5251.72,
              "MesReferencia": "Fevereiro 2024"
            }
            ```
    4.  **Geração do Resumo com Claude API**: Envie os dados agregados para o Claude para gerar um resumo executivo.
        *   *Prompt Claude Real para Resumo Executivo*:
            ```
            Você é um analista de negócios e deve