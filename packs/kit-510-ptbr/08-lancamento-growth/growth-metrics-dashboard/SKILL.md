---
name: growth-metrics-dashboard
description: "Growth Metrics Dashboard — Skill especializada para growth metrics dashboard"
license: MIT
metadata:
  version: 1.0.0
  author: Cafe Code AI
  category: 08-lancamento-growth
  updated: 2026-03-01
risk: safe
---

# Growth Metrics Dashboard

Esta skill capacita o Claude a projetar, implementar e otimizar dashboards de métricas de crescimento, focando em aquisição, ativação, retenção e receita para produtos digitais.

---

## Keywords

Métricas de Crescimento, Dashboard de Growth, AARRR, Pirate Metrics, Cohort Analysis, Funil de Vendas, LTV, CAC, MRR, Activation Rate, Churn Rate, Amplitude Analytics, Mixpanel, Google Data Studio.

---

## Quick Start

1.  **Mapear o Funil AARRR**: Identifique as etapas de Aquisição, Ativação, Retenção, Receita e Referência para o produto digital (ex: SaaS de produtividade para equipes).
2.  **Selecionar Ferramenta BI e Integrar Dados**: Configure a integração inicial de dados entre a base do produto (ex: PostgreSQL) e plataformas de eventos (ex: Amplitude) com ferramentas como Metabase, Power BI ou Google Data Studio.
3.  **Definir Métricas Primárias por Etapa**: Escolha 3-5 métricas-chave para cada etapa do funil (ex: Ativação: % de usuários que completam o onboarding, Retenção: WAUs por cohort).
4.  **Construir o Esqueleto do Dashboard**: Crie as visualizações iniciais para as métricas selecionadas, agrupando-as logicamente por etapa do funil para facilitar a leitura.
5.  **Configurar Alertas Essenciais**: Estabeleça alertas automáticos em ferramentas como Slack ou e-mail para quedas significativas em métricas críticas como "Daily Active Users (DAU)" ou "Taxa de Conversão de Trial para Pago".

---

## Core Workflows

### Workflow 1: Construção de Dashboard de Funil AARRR para SaaS B2B

**Objetivo**: Visualizar a performance do funil de growth e identificar gargalos na jornada do cliente para um SaaS de gestão de projetos.

**Passo 1: Definição de Etapas e Eventos Chave**:
Para um SaaS de gestão de projetos, os eventos que marcam cada etapa do funil AARRR seriam:
*   **Aquisição**: `User Registered` (cadastro inicial), `Trial Started` (início do período de teste gratuito).
*   **Ativação**: `Project Created` (primeiro projeto criado), `Team Invited` (primeiro convite de equipe enviado), `Feature X Used` (uso de uma feature chave do produto 3x na primeira semana).
*   **Retenção**: `Weekly Active Users` (WAU), `Monthly Active Users` (MAU), `Login Frequency` (frequência de logins).
*   **Receita**: `Subscription Started` (assinatura paga efetivada), `Upgrade Plan` (upgrade de plano), `MRR` (Receita Recorrente Mensal).
*   **Referência**: `Invite Sent` (convite para amigos/colegas), `Review Submitted` (avaliação de produto).

**Passo 2: Coleta e Integração de Dados**:
Conecte a base de dados do produto (ex: PostgreSQL para dados de usuário e assinatura) e plataformas de marketing (ex: HubSpot para dados de leads) ao Google Data Studio (Looker Studio). Use BigQuery como um data warehouse intermediário para consolidar e processar eventos de usuário de plataformas como Amplitude ou Mixpanel.

**Passo 3: Criação de Métricas Calculadas no Data Studio**:
*   `Activation Rate`: `(COUNT_DISTINCT(CASE WHEN EventName = 'Project Created' THEN UserID END) / COUNT_DISTINCT(CASE WHEN EventName = 'Trial Started' THEN UserID END)) * 100`
*   `Trial-to-Paid Conversion`: `(COUNT_DISTINCT(CASE WHEN EventName = 'Subscription Started' THEN UserID END) / COUNT_DISTINCT(CASE WHEN EventName = 'Trial Started' THEN UserID END)) * 100`
*   `Churn Rate (Mensal)`: `(COUNT_DISTINCT(CASE WHEN EventName = 'Subscription Cancelled' AND DATE_TRUNC(SubscriptionCancelDate, MONTH) = CURRENT_DATE THEN UserID END) / COUNT_DISTINCT(CASE WHEN EventName = 'Subscription Started' AND DATE_TRUNC(SubscriptionStartDate, MONTH) < CURRENT_DATE THEN UserID END)) * 100`

**Passo 4: Visualização no Dashboard**:
*   **Gráfico de Funil**: Represente visualmente as transições de `Aquisição` -> `Ativação` -> `Receita` com os números de usuários em cada etapa.
*   **Gráficos de Linha**: Mostre a evolução de `MRR`, `WAU` e `MAU` ao longo do tempo.
*   **Tabela de Cohort**: Exiba a `Retention Rate` por data de aquisição dos usuários (semanal ou mensal).
*   **Cartões de Score**: Destaque métricas chave como `Activation Rate`, `Trial-to-Paid Conversion` e `CAC` (Custo de Aquisição de Cliente) com indicadores de tendência.

### Workflow 2: Otimização de Dashboard de Retenção com Análise de Cohort para App Mobile

**Objetivo**: Aprofundar a compreensão da retenção de usuários e identificar cohorts com melhor/pior performance para um aplicativo mobile de fitness.

**Passo 1: Definição do Cohort e Métrica de Retenção**:
*   **Cohort**: Agrupar usuários pela semana ou mês de sua primeira abertura do aplicativo (evento `App Opened`).
*   **Métrica de Retenção**: `User Active` definido como um usuário que abriu o app e registrou pelo menos um treino na semana/mês subsequente à sua aquisição.

**Passo 2: Extração de Dados para Análise de Cohort (SQL)**:
Exporte dados de usuário e eventos de `App Opened` e `Workout Logged` do Amplitude ou Mixpanel. Para um banco de dados SQL (ex: PostgreSQL):
```sql
WITH user_cohorts AS (
    SELECT
        user_id,
        MIN(event_timestamp) AS first_seen_at
    FROM events
    WHERE event_name = 'App Opened'
    GROUP BY user_id
),
user_activity AS (
    SELECT
        user_id,
        DATE_TRUNC('week', event_timestamp) AS activity_week
    FROM events
    WHERE event_name = 'Workout Logged'
    GROUP BY user_id, DATE_TRUNC('week', event_timestamp)
)
SELECT
    DATE_TRUNC('week', uc.first_seen_at) AS cohort_week,
    COUNT(DISTINCT uc.user_id) AS total_users_in_cohort,
    DATE_DIFF('week', DATE_TRUNC('week', uc.first_seen_at), ua.activity_week) AS weeks_since_cohort,
    COUNT(DISTINCT ua.user_id) AS retained_users
FROM user_cohorts uc
JOIN user_activity ua ON uc.user_id = ua.user_id
WHERE ua.activity_week >= DATE_TRUNC('week', uc.first_seen_at)
GROUP BY 1, 3
ORDER BY 1, 3;
```
Este query irá gerar os dados necessários para construir uma tabela de cohort, mostrando quantos usuários de cada cohort inicial estavam ativos em semanas subsequentes.

**Passo 3: Visualização da Matriz de Cohort**:
Crie um gráfico de tabela de calor (heatmap) em sua ferramenta de BI. As linhas representam o cohort de aquisição (ex: "Semana de 01/Jan") e as colunas representam as semanas/meses subsequentes (ex: "Semana 0", "Semana 1", "Semana 2"). Cada célula exibirá a porcentagem de retenção para aquele cohort naquela semana.

**Passo 4: Análise e Ação**:
*   **Identificação de Padrões**: Observe quedas abruptas de retenção em cohorts específicos (ex: usuários de uma campanha de marketing de baixo valor) ou retenção excepcionalmente alta (ex: usuários que usaram o recurso de "desafio de 30 dias" na primeira semana).
*   **Ações Otimizadas**: Use esses insights para otimizar campanhas de aquisição (direcionando para públicos que retêm melhor) ou melhorar a experiência de onboarding (incentivando o uso de recursos que aumentam a retenção).

---

## Templates

### Template de Dashboard de Performance de Growth

```
# Dashboard de Performance de Growth - Produto Alpha
(Atualizado: 2024-07-25)

## Visão Geral do Funil (Últimos 30 dias)
- **Novos Cadastros**: 15.200 (vs. 13.500 mês anterior, ↑ 12%)
- **Trials Iniciados**: 2.800 (vs. 2.500 mês anterior, ↑ 12%)
- **Ativação (1º Projeto Criado)**: 1.120 usuários (40% dos trials, ↑ 2pp)
- **Novas Assinaturas Pagas**: 280 (10% dos trials, ↑ 1pp)
- **MRR Crescimento**: R$ 12.000 (vs. R$ 10.500 mês anterior, ↑ 14%)

## Métricas de Aquisição
| Métrica             | Valor (Últimos 30d) | Tendência | Benchmark |
|---------------------|---------------------|-----------|-----------|
| Visitantes Únicos   | 180.000             | ↑ 5%      | 200.000   |
| Taxa de Conversão Landing Page | 8.4%                | ↑ 0.2pp   | 9%        |
| Custo por Aquisição (CAC) | R$ 50               | ↓ R$ 5    | R$ 55     |

## Métricas de Ativação
| Métrica             | Valor (Últimos 30d) | Tendência | Benchmark |
|---------------------|---------------------|-----------|-----------|
| % Ativados (1º Projeto) | 40%                 | ↑ 2pp     | 45%       |
| Tempo para 1ª Ação Chave | 12 minutos          | ↓ 1min    | 10 min    |

## Métricas de Retenção
| Métrica             | Valor (Últimos 30d) | Tendência | Benchmark |
|---------------------|---------------------|-----------|-----------|
| Retenção D7         | 35%                 | ↑ 1pp     | 40%       |
| Churn Rate Mensal   | 4.8%                | ↓ 0.5pp   | 5%        |
| DAU                 | 8.500               | ↑ 3%      | 9.000     |

## Métricas de Receita
| Métrica             | Valor (Últimos 30d) | Tendência | Benchmark |
|---------------------|---------------------|-----------|-----------|
| MRR                 | R$ 280.000          | ↑ 4.5%    | R$ 300.000|
| ARR                 | R$ 3.360.000        | ↑ 4.5%    | R$ 3.600.000|
| LTV (Média)         | R$ 1.200            | ↑ R$ 50   | R$ 1.300  |

## Ações Recomendadas
- Investigar a queda na retenção D7 para o cohort da semana 28 (campanha de TikTok Ads) e pausar/otimizar a campanha.
- Otimizar o fluxo de onboarding para reduzir o tempo até a 1ª ação chave em 20% através de um teste A/B.
- Analisar os usuários que atingiram o benchmark de 1ª ação chave em menos de 10 minutos para identificar padrões.
```

### Modelo de Tracking Plan para Novos Recursos

```
# Tracking Plan - Recurso "Colaboração em Tempo Real"

## Propósito
Monitorar o uso e impacto do novo recurso de colaboração em tempo real na ativação e retenção de equipes.

## Eventos a Rastrear
| Evento                    | Propriedades             | Descrição                                         | Gatilho                                    |
|---------------------------|--------------------------|---------------------------------------------------|--------------------------------------------|
| `real_time_collaboration_started` | `project_id`, `user_id`, `num_collaborators`, `plan_type` | Início de uma sessão de colaboração em tempo real | Usuário inicia a edição colaborativa      |
| `real_time_collaboration_ended`   | `project_id`, `user_id`, `duration_seconds`, `num_changes` | Fim de uma sessão de colaboração             | Usuário fecha o projeto/sai da sessão    |
| `comment_added_realtime`  | `project_id`, `user_id`, `comment_id`, `comment_type` | Adição de comentário em tempo real             | Usuário adiciona um comentário colaborativo |
| `document_shared`         | `project_id`, `user_id`, `share_method`, `recipient_type` | Compartilhamento de documento editado colaborativamente | Usuário compartilha o documento         |

## Métricas Chave a Monitorar
- **Taxa de Adoção**: % de projetos com pelo menos 1 sessão de colaboração em tempo real por semana.
- **Engajamento**: Média de sessões por projeto ativo por semana.
- **Duração Média da Sessão**: `AVG(duration_seconds)` por usuário.
- **Número Médio de Colaboradores**: `AVG(num_collaborators)` por sessão.
- **Correlação com Retenção**: Comparar a retenção de cohorts que usaram o recurso vs. aqueles que não usaram.

## Ferramentas de Análise
- Amplitude Analytics (para funis, análise de usuários e cohort)
- Google Data Studio (para dashboard de alto nível e visão agregada)

## Propriedades do Usuário Adicionais (se relevante)
- `team_size` (tamanho da equipe do usuário)
- `industry` (indústria do usuário)
```

---

## Checklist

- [x] Mapear o funil de crescimento completo (AARRR/Pirate Metrics) para o produto, definindo cada etapa e seus respectivos eventos.
- [x] Definir métricas primárias e secundárias acionáveis para cada etapa do funil (ex: Taxa de Ativação, Churn Rate).
- [x] Garantir que todos os eventos de usuário relevantes para as métricas estejam sendo rastreados de forma consistente e com as propriedades necessárias.
- [x] Validar a integridade e precisão dos dados em todas as fontes (ex: Google Analytics, Amplitude, Mixpanel, Banco de Dados).
- [x] Escolher a ferramenta de Business Intelligence (BI) mais adequada (Google Data Studio, Power BI, Tableau, Metabase) e configurar todas as conexões de dados.
- [x] Criar visualizações claras e intuitivas para cada métrica chave (gráficos de linha para tendências, barras para comparação, funis para conversão, tabelas de