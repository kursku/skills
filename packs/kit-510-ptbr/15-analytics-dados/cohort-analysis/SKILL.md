---
name: cohort-analysis
description: "Cohort Analysis — Skill especializada para cohort analysis"
license: MIT
metadata:
  version: 1.0.0
  author: Cafe Code AI
  category: 15-analytics-dados
  updated: 2026-03-01
risk: safe
---

# Cohort Analysis

Esta skill capacita o Claude a executar análises de coorte, identificando padrões de comportamento de grupos de usuários ao longo do tempo para otimizar estratégias de retenção e monetização usando dados do Google Analytics 4.

---

## Keywords

GA4, Retenção de Usuários, LTV por Coorte, Churn, Análise de Aquisição, Segmentação Temporal, Ciclo de Vida do Cliente, Comportamento do Usuário, Cohorts de Eventos, Explorações GA4, Funil de Retenção, Sticky Factor, Atribuição de Marketing.

---

## Quick Start

1.  Acesse o Google Analytics 4 e navegue até "Relatórios > Retenção" no menu lateral esquerdo.
2.  Selecione a dimensão "Coorte de Aquisição" para agrupar usuários pela data do primeiro acesso ao site/aplicativo.
3.  Observe o gráfico de "Retenção de usuários" para identificar a curva geral de declínio do engajamento ao longo do tempo.
4.  Analise a tabela "Retenção por coorte" para comparar o percentual de usuários retidos entre diferentes grupos de aquisição ao longo das semanas ou meses.
5.  Filtre o período de análise para os últimos 6 meses para obter uma visão macro e identificar tendências de longo prazo.

---

## Core Workflows

### Workflow 1: Análise de Retenção de Usuários por Coorte de Aquisição no GA4

**Objetivo:** Entender como a retenção de usuários varia entre coortes de aquisição no GA4, identificando padrões e oportunidades de otimização de engajamento e produto.

**Passos Detalhados:**

1.  **Acessar o Relatório de Retenção:** No Google Analytics 4, navegue até `Relatórios > Retenção` no painel de navegação esquerdo.
2.  **Configurar Período e Dimensão da Coorte:**
    *   Defina o intervalo de datas para os últimos 6 meses (exemplo: "1 de Janeiro de 2024" a "30 de Junho de 2024").
    *   Verifique se a dimensão "Coorte de Aquisição" está selecionada no cartão de "Retenção de usuários". A granularidade da coorte (diária, semanal, mensal) será ajustada automaticamente pelo GA4 com base no período selecionado.
3.  **Interpretar o Gráfico de Retenção de Usuários:**
    *   Analise a curva descendente do gráfico. Uma queda mais suave indica melhor retenção.
    *   **Exemplo Concreto:** Se o gráfico mostra uma queda acentuada de 70% na retenção após a semana 1 para coortes recentes, isso aponta para um problema crítico no engajamento inicial do usuário, talvez relacionado ao onboarding ou à proposta de valor imediata.
4.  **Analisar a Tabela "Retenção por coorte":**
    *   Esta tabela exibe o percentual de usuários retidos para cada coorte de aquisição em diferentes períodos de tempo (Dia 0, Semana 1, Semana 2, etc., ou Mês 0, Mês 1, Mês 2, etc.).
    *   **Exemplo Concreto de Dados:**
        *   Coorte de 01/Jan/2024 (semana de aquisição): Retenção Semana 1: 35%, Semana 2: 28%, Semana 3: 22%.
        *   Coorte de 01/Mar/2024 (semana de aquisição): Retenção Semana 1: 42%, Semana 2: 35%, Semana 3: 29%.
    *   **Insight:** A coorte de Março/2024 demonstra uma retenção significativamente superior nos primeiros ciclos de vida. Isso sugere que alguma iniciativa de marketing, otimização de produto ou melhoria no processo de onboarding implementada em Março foi eficaz.
5.  **Exportar Dados para Análise Aprofundada:**
    *   Clique no ícone de "Compartilhar este relatório" (canto superior direito do relatório) e selecione "Fazer download do arquivo > CSV".
    *   Esta exportação permite manipular os dados em planilhas (Google Sheets, Excel) ou ferramentas de BI para cálculos personalizados de taxas de churn, LTV por coorte ou criação de visualizações específicas.
6.  **Propor Ações Baseadas em Insights:**
    *   Se a retenção da coorte de Janeiro/2024 é notavelmente menor, investigar as campanhas de aquisição ativas naquele mês, a experiência do usuário no site/app, ou mudanças no produto/serviço que podem ter impactado negativamente.
    *   Sugira campanhas de reengajamento segmentadas para as coortes com baixa retenção (exemplo: e-mail marketing com cupom de desconto exclusivo para usuários da coorte de Janeiro que não retornaram após 2 semanas).
    *   Replicar as táticas de aquisição e engajamento que beneficiaram a coorte de Março/2024, como o foco em canais específicos ou mensagens de boas-vindas.

### Workflow 2: Segmentação de Coortes para Otimização de LTV no GA4

**Objetivo:** Identificar e comparar o Lifetime Value (LTV) de diferentes coortes de aquisição para direcionar investimentos de marketing e otimizar estratégias de monetização.

**Passos Detalhados:**

1.  **Criar uma Exploração de Usuários:** No Google Analytics 4, navegue até `Explorar > Exploração de Usuários` no painel de navegação esquerdo.
2.  **Adicionar Segmentos de Coorte:**
    *   Na seção "Segmentos", clique em "+" para criar um novo segmento.
    *   Crie "Segmentos de Usuários" distintos para cada coorte que deseja comparar.
    *   **Segmento Exemplo 1 (Coorte A):**
        *   Nome: "Coorte Aquisição Orgânica - Jan 2024"
        *   Condição: `Primeiro acesso` está `entre 01/01/2024 e 31/01/2024` E `Origem do primeiro acesso` é `google` E `Médio do primeiro acesso` é `organic`.
    *   **Segmento Exemplo 2 (Coorte B):**
        *   Nome: "Coorte Aquisição Paga - Jan 2024"
        *   Condição: `Primeiro acesso` está `entre 01/01/2024 e 31/01/2024` E `Médio do primeiro acesso` é `cpc`.
    *   Aplique ambos os segmentos à exploração, arrastando-os para a seção "Comparação de segmentos".
3.  **Adicionar Métricas de Monetização e Engajamento:**
    *   Na seção "Métricas", clique em "+" e adicione: `Receita total`, `Receita média por usuário`, `Compras`, `Sessões engajadas`, `Tempo médio de engajamento`.
    *   Arraste estas métricas para a seção "Valores" da exploração.
4.  **Configurar Dimensões e Visualização:**
    *   Na seção "Dimensões", adicione `ID do usuário` (se implementado) ou `ID do dispositivo` (se disponível para explorações específicas). Para uma visão sumária, a comparação de segmentos já será suficiente.
    *   Selecione a visualização "Tabela" para facilitar a comparação.
5.  **Comparar LTV e Engajamento entre Coortes:**
    *   Analise os valores agregados de "Receita total", "Receita média por usuário" e outras métricas para cada segmento de coorte.
    *   **Exemplo Concreto de Dados:**
        *   "Coorte Aquisição Orgânica - Jan 2024": Receita Média por Usuário: R$ 185,00; Sessões Engajadas por Usuário: 8.5.
        *   "Coorte Aquisição Paga - Jan 2024": Receita Média por Usuário: R$ 110,00; Sessões Engajadas por Usuário: 5.2.
    *   **Insight:** Usuários adquiridos organicamente em Janeiro de 2024 demonstram um LTV e engajamento significativamente superiores em comparação com os usuários adquiridos via mídia paga no mesmo período.
6.  **Identificar Padrões e Sugerir Otimizações:**
    *   Investigar as características dos usuários da coorte orgânica (demografia, interesses, comportamento de navegação no site/app) para entender o que impulsiona seu LTV superior.
    *   Propor realocação do orçamento de marketing, priorizando canais e estratégias de aquisição que historicamente atraem coortes de alto LTV.
    *   Desenvolver campanhas de retenção ou upsell específicas para a coorte de aquisição paga, visando aumentar seu LTV e engajamento.
    *   Recomendar a criação de dashboards personalizados no Looker Studio (Google Data Studio) para monitorar continuamente o LTV por coorte de aquisição, fonte e meio.

---

## Templates

### Requisição de Dados Detalhados de Retenção de Coorte (GA4 Data API v2)

Este template JSON pode ser usado para solicitar dados de retenção de coortes específicas via GA4 Data API v2, permitindo análises mais customizadas fora da interface do GA4.

```json
{
  "dimensions": [
    {"name": "cohortNthDay"},
    {"name": "cohort"},
    {"name": "cohortDate"}
  ],
  "metrics": [
    {"name": "cohortTotalUsers"},
    {"name": "cohortActiveUsers"}
  ],
  "dateRanges": [
    {"startDate": "2024-01-01", "endDate": "2024-06-30"}
  ],
  "cohortSpec": {
    "cohorts": [
      {
        "name": "Coorte Jan