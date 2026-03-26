---
name: reporting-automation
description: "Reporting Automation — Skill especializada para automação de relatórios de marketing e análise de dados."
license: MIT
metadata:
  version: 1.0.0
  author: Cafe Code AI
  category: 15-analytics-dados
  updated: 2026-03-01
risk: safe
---

# Reporting Automation

Esta skill capacita o Claude Code a automatizar a extração, transformação e visualização de dados de marketing digital, com foco em Google Analytics 4, para a geração eficiente de relatórios periódicos e dashboards dinâmicos.

---

## Keywords

Google Analytics 4, GA4 API, BigQuery Export, Looker Studio, Python, Pandas, SQL, ETL, Automação de Relatórios, Dashboards Dinâmicos, Atribuição de Marketing, Métricas de Performance, Google Cloud Functions, Cloud Scheduler, Data Studio.

---

## Quick Start

1.  **Configurar GA4 BigQuery Export:** Habilitar a exportação contínua de eventos do seu Google Analytics 4 para um projeto no Google BigQuery.
2.  **Credenciais de Acesso:** Criar uma Service Account no Google Cloud Platform com os papéis `BigQuery Data Viewer` e `Analytics Hub Viewer` e gerar uma chave JSON.
3.  **Script de Extração Inicial:** Desenvolver um script Python para extrair dados brutos do BigQuery usando a biblioteca `google-cloud-bigquery`.
4.  **Conexão no Looker Studio:** Conectar o Looker Studio (antigo Data Studio) à tabela resultante no BigQuery ou ao Google Analytics 4 Data API.
5.  **Agendamento da Automação:** Agendar a execução do script Python em ambiente serverless, como Google Cloud Functions, utilizando o Cloud Scheduler para periodicidade diária.

---

## Core Workflows

### Workflow 1: Automação de Relatório Mensal de Performance de Campanhas GA4 para Google Sheets

Este workflow detalha a criação de um processo automatizado para extrair dados de performance de campanhas do Google Analytics 4 via BigQuery, processá-los com Python e atualizar um relatório no Google Sheets, com envio de e-mail.

1.  **Extração de Dados Brutos via BigQuery Export:**
    *   **Ação:** Escrever e executar uma query SQL no BigQuery para extrair métricas de campanhas do GA4 para o mês anterior.
    *   **Exemplo de Query SQL:**
        ```sql
        SELECT
          FORMAT_DATE('%Y-%m-%d', PARSE_DATE('%Y%m%d', event_date)) AS data,
          traffic_source.source AS fonte,
          traffic_source.medium AS meio,
          traffic_source.name AS campanha,
          SUM(CASE WHEN event_name = 'session_start' THEN 1 ELSE 0 END) AS sessoes_iniciadas,
          COUNT(DISTINCT user_pseudo_id) AS total_usuarios,
          SUM(CASE WHEN event_name = 'purchase' THEN 1 ELSE 0 END) AS total_compras,
          SUM(CASE WHEN event_name = 'purchase' THEN (SELECT value.double_value FROM UNNEST(event_params) WHERE key = 'value') ELSE 0 END) AS receita_total
        FROM
          `seu-projeto-gcp.seu-dataset-ga4.events_*`
        WHERE
          _TABLE_SUFFIX BETWEEN FORMAT_DATE('%Y%m%d', DATE_SUB(CURRENT_DATE(), INTERVAL 1 MONTH)) AND FORMAT_DATE('%Y%m%d', DATE_SUB(CURRENT_DATE(), INTERVAL 1 DAY))
        GROUP BY 1, 2, 3, 4
        ORDER BY data DESC, receita_total DESC;
        ```
    *   **Ferramenta:** Google BigQuery Console ou `google-cloud-bigquery` library em Python.

2.  **Transformação e Agregação com Python/Pandas:**
    *   **Ação:** Carregar os dados extraídos para um DataFrame Pandas, calcular métricas derivadas (e.g., Taxa de Conversão, Receita por Sessão) e agrupar por canal/campanha.
    *   **Exemplo de Código Python:**
        ```python
        import pandas as pd
        # df_raw é o DataFrame resultante da query BigQuery
        df_processed = df_raw.copy()
        df_processed['taxa_conversao_compra'] = (df_processed['total_compras'] / df_processed['sessoes_iniciadas']) * 100
        df_processed['receita_por_sessao'] = df_processed['receita_total'] / df_processed['sessoes_iniciadas']
        
        # Agregação para o relatório final
        df_report = df_processed.groupby(['fonte', 'meio']).agg(
            total_sessoes=('sessoes_iniciadas', 'sum'),
            total_compras=('total_compras', 'sum'),
            receita_total=('receita_total', 'sum')
        ).reset_index()
        df_report['taxa_conversao_compra'] = (df_report['total_compras'] / df_report['total_sessoes']) * 100
        ```
    *   **Ferramenta:** Python com biblioteca Pandas.

3.  **Geração e Atualização de Relatório em Planilha Google Sheets:**
    *   **Ação:** Utilizar a API do Google Sheets (via `gspread` ou `pygsheets`) para atualizar abas específicas em uma planilha pré-formatada com os dados processados.
    *   **Exemplo de Código Python:**
        ```python
        import gspread
        # gc é o cliente gspread autenticado
        spreadsheet_name = "Relatório Mensal GA4 - MAI2024"
        sh = gc.open(spreadsheet_name)
        worksheet = sh.worksheet("Performance por Canal") # Nome da aba no Sheets
        
        # Limpar e atualizar a aba
        worksheet.clear()
        worksheet.update([df_report.columns.values.tolist()] + df_report.values.tolist(), 'A1')
        ```
    *   **Ferramenta:** Python com biblioteca `gspread`.

4.  **Disparo de E-mail com Resumo Executivo:**
    *   **Ação:** Enviar um e-mail com um resumo dos principais insights e um link para o relatório atualizado.
    *   **Exemplo de Código Python:**
        ```python
        import smtplib
        from email.mime.text import MIMEText
        
        sender_email = "automatizacao@suaempresa.com"
        receiver_email = "gerencia@suaempresa.com"
        password = "SUA_SENHA_APP" # Ou token de autenticação
        
        msg = MIMEText(f"""
        Prezado(a) Gerente,
        
        O relatório mensal de performance do GA4 para MAI/2024 foi atualizado.
        
        Destaques:
        - Receita Total: R$ {df_report['receita_total'].sum():,.2f}
        - Taxa de Conversão Média: {df_report['taxa_conversao_compra'].mean():.2f}%
        
        Acesse o relatório completo aqui: [Link para o Google Sheet]
        
        Atenciosamente,
        Seu Time de Analytics Automatizado
        """)
        msg['Subject'] = "Relatório Mensal GA4 - MAI/2024 Disponível"
        msg['From'] = sender_email
        msg['To'] = receiver_email
        
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(sender_email, password)
            smtp.send_message(msg)
        ```
    *   **Ferramenta:** Python com biblioteca `smtplib`.

### Workflow 2: Automação de Dashboard de Monitoramento de Tráfego em Tempo Próximo Real com GA4 Data API e Looker Studio

Este workflow foca na extração de dados do GA4 Data API para monitoramento quase em tempo real, disponibilizando-os para um dashboard dinâmico no Looker Studio.

1.  **Configuração de Credenciais GA4 Data API:**
    *   **Ação:** Garantir que a Service Account criada no GCP tenha o papel `Google Analytics Data API Viewer`.
    *   **Exemplo:** O arquivo `key.json` da Service Account deve estar acessível ao ambiente de execução do script.
    *   **Ferramenta:** Google Cloud IAM & Admin.

2.  **Extração de Dados com GA4 Data API (Python):**
    *   **Ação:** Desenvolver um script Python para buscar métricas e dimensões específicas do GA4 Data API. Para "quase em tempo real", a janela de dados é curta (e.g., últimos 30 minutos, último dia).
    *   **Exemplo de Código Python:**
        ```python
        from google.analytics.data_v1beta import BetaAnalyticsDataClient
        from google.analytics.data_v1beta.types import RunReportRequest, Dimension, Metric, DateRange
        
        client = BetaAnalyticsDataClient.from_service_account_json('path/to/your/key.json')
        property_id = 'SEU_GA4_PROPERTY_ID' # Ex: '123456789'
        
        request = RunReportRequest(
            property=f"properties/{property_id}",
            dimensions=[
                Dimension(name="date"),
                Dimension(name="sessionSource"),
                Dimension(name="sessionMedium")
            ],
            metrics=[
                Metric(name="sessions"),
                Metric(name="conversions"),
                Metric(name="totalRevenue")
            ],
            date_ranges=[DateRange(start_date="1daysAgo", end_date="today")]
        )
        response = client.run_report(request)
        
        # Processar a resposta para um DataFrame Pandas
        data_rows = []
        for row in response.rows:
            row_data = {
                "data": row.dimension_values[0].value,
                "fonte": row.dimension_values[1].value,
                "meio": row.dimension_values[2].value,
                "sessoes": int(row.metric_values[0].value),
                "conversoes": int(row.metric_values[1].value),
                "receita": float(row.metric_values[2].value)
            }
            data_rows.append(row_data)
        df_realtime = pd.DataFrame(data_rows)
        ```
    *   **Ferramenta:** Python com biblioteca `google-analytics-data`.

3.  **Publicação de Dados para Dashboard Dinâmico (Looker Studio):**
    *   **Ação:** Armazenar os dados extraídos em uma tabela BigQuery para que o Looker Studio possa consumi-los. O Looker Studio pode se conectar diretamente ao GA4 Data API, mas para transformações ou enriquecimento, o BigQuery é preferível.
    *   **Exemplo de Código Python (continuando do passo 2):**
        ```python
        from google.cloud import bigquery
        
        bq_client = bigquery.Client.from_service_account_json('path/to/your/key.json')
        table_id = "seu-projeto-gcp.seu-dataset-ga4.realtime_traffic_data"
        
        # Configurar esquema da tabela BigQuery
        job_config = bigquery.LoadJobConfig(
            schema=[
                bigquery.SchemaField("data", "DATE"),
                bigquery.SchemaField("fonte", "STRING"),
                bigquery.SchemaField("meio", "STRING"),
                bigquery.SchemaField("sessoes", "INTEGER"),
                bigquery.SchemaField("conversoes", "INTEGER"),
                bigquery.SchemaField("receita", "FLOAT"),
            ],
            write_disposition="WRITE_TRUNCATE", # Sobrescrever a cada atualização
        )
        
        # Carregar DataFrame para BigQuery
        job = bq_client.load_table_from_dataframe(df_realtime, table_id, job_config=job_config)
        job.result() # Esperar o job completar
        print(f"Dados carregados para {table_id}")
        ```
    *   **Ferramenta:** Python com biblioteca `google-cloud-bigquery` e Looker Studio.

4.  **Agendamento da Extração/Atualização:**
    *   **Ação:** Configurar o script Python para rodar periodicamente (e.g., a cada 15 ou 30 minutos) usando Google Cloud Functions e Cloud Scheduler.
    *   **Exemplo:** Uma Cloud Function acionada por HTTP, que é chamada por um job do Cloud Scheduler.
    *   **Ferramenta:** Google Cloud Functions, Google Cloud Scheduler.

---

## Templates

### Template de Query BigQuery para Análise de Conversão por Canal

```sql
SELECT
  FORMAT_DATE('%Y-%m-%d', PARSE_DATE('%Y%m%d', event_date)) AS data_referencia,
  traffic_source.source AS fonte_trafego,
  traffic_source.medium AS meio_trafego,
  traffic_source.name AS nome_campanha,
  COUNT(DISTINCT user_pseudo_id) AS total_usuarios_unicos,
  SUM(CASE WHEN event_name = 'session_start' THEN 1 ELSE 0 END) AS sessoes_iniciadas,
  SUM(CASE WHEN event_name = 'add_to_cart' THEN 1 ELSE 0 END) AS itens_adicionados_carrinho,
  SUM(CASE WHEN event_name = 'purchase' THEN 1 ELSE 0 END) AS compras_efetuadas,
  SUM(CASE WHEN event_name = 'purchase' THEN (SELECT value.double_value FROM UNNEST(event_params) WHERE key = 'value') ELSE 0 END) AS receita_total_compra,
  SUM(CASE WHEN event_name = 'generate_lead' THEN 1 ELSE 0 END) AS leads_gerados
FROM
  `seu-projeto-gcp.seu-dataset-ga4.events_*`
WHERE
  _TABLE_SUFFIX BETWEEN '20240501' AND '20240531'
GROUP BY 1, 2, 3, 4
ORDER BY data_referencia DESC, receita_total_compra DESC;
```

### Template de Estrutura de Relatório Mensal de E-commerce (Google Sheets)

```
Relatório de Performance Digital - MAI/2024

Visão Geral
Sessões: 485.678 (+12% vs Abr/24)
Usuários: 398.123 (+10% vs Abr/24)
Receita Total: R$ 387.900 (+18% vs Abr/24)
Compras Efetuadas: 7.210 (+15% vs Abr/24)
Taxa de Conversão (Compras/Sessões): 1.48% (+0.04 pp vs Abr/24)
Custo por Aquisição (Compras): R$ 53.79 (excluindo custos de mídia não integrada)

Performance por Canal (Top 5 em Receita)
| Canal (Fonte/Meio) | Sessões | Receita Total | Compras | Taxa Conv. |
|--------------------|---------|---------------|---------|------------|
| google / cpc       | 120.000 | R$ 150.000    | 3.000   | 2.50%      |
| google / organic   | 150.000 | R$ 120.000    | 1.800   | 1.20%      |
| email / newsletter | 50.000  | R$ 45.000     | 900     | 1.80%      |
| (direct) / (none)  | 40.000  | R$ 30.000     | 400     | 1.00%      |
| facebook / cpc     | 30.000  | R$ 25.000     | 500     | 1.67%      |

Destaques e Próximos Passos
- A campanha de Dia das Mães via Google Ads (google / cpc) foi a principal alavanca da receita em MAI/24, gerando R$ 85.000,00 especificamente.
- Houve uma queda de 5% no tráfego orgânico proveniente de buscas por "promoções de verão" em relação ao mês anterior, apesar do aumento geral. Investigar sazonalidade ou ranqueamento de palavras-chave específicas.
- Próximo passo: Testar segmentação de público semelhante para campanhas de display com foco em usuários que abandonaram o carrinho, visando aumentar a taxa de conversão em 0.2 pp.
- Aumentar o budget para campanhas de e-mail marketing, que apresentaram um ROAS de 4.5x (assumindo custo de R$10.000 para email).
```

---

## Checklist

- [x] Conectar o Google Analytics 4 ao BigQuery para exportação contínua de eventos.
- [x] Criar e configurar Service Accounts no GCP com permissões adequadas para GA4 Data API e BigQuery.
- [x] Desenvolver scripts Python robustos para extração de dados (BigQuery ou GA4 Data API).
- [x] Implementar tratamento de erros (ex: retentativas, logging) nos scripts de automação.
- [x] Configurar o agendamento dos scripts (e.g., Cloud Functions + Cloud Scheduler, ou Airflow/Composer).
- [x] Desenvolver ou atualizar dashboards no Looker Studio/Power BI para consumir as fontes de dados automatizadas.
- [x] Validar a integridade e consistência dos dados automatizados versus a interface do GA4.
- [x] Configurar alertas automáticos para anomalias em métricas chave (ex: queda de receita > 15% em 24h).
- [x] Documentar o fluxo completo de ETL (Extração, Transformação, Carga) e a lógica de qualquer métrica customizada.
- [x] Automatizar o envio de relatórios sumários ou notificações por e-mail/Slack.

---

## Métricas de Referência

| Métrica                      | Benchmark (E-commerce) | Meta (E-commerce) |
|------------------------------|------------------------|-------------------|
| Taxa de Conversão (Compras)  | 1.5% - 2.5%            | > 2.8%            |
| Receita por Usuário          | R$ 30 - R$ 60          | > R$ 70           |
| ROAS (Retorno sobre Investimento em Anúncios) | 3.0x - 5.0x