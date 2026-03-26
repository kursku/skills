---
name: predictive-analytics
description: "Predictive Analytics — Skill especializada para predictive analytics"
license: MIT
metadata:
  version: 1.0.0
  author: Cafe Code AI
  category: 15-analytics-dados
  updated: 2026-03-01
risk: safe
---

# Predictive Analytics

Esta skill capacita a utilização e otimização de modelos preditivos do Google Analytics 4 para antecipar comportamentos de usuários e resultados de negócios, permitindo estratégias proativas.

---

## Keywords

Probabilidade de Churn GA4, Probabilidade de Compra GA4, Previsão de Receita GA4, Audiências Preditivas, Otimização LTV, Modelagem de Atribuição Preditiva, Google Analytics 4 ML, BigQuery ML, Retenção de Clientes, Segmentação Comportamental, Performance de Campanha Preditiva, Análise de Cohorts Preditivos.

---

## Quick Start

1.  **Verificar Elegibilidade GA4**: Acessar Administrador > Configurações de Dados > Coleta de Dados e assegurar que as métricas preditivas estão ativadas e o fluxo de dados atende aos requisitos mínimos (ex: >1.000 usuários com eventos de compra nos últimos 28 dias e >1.000 usuários com churn nos últimos 28 dias).
2.  **Criar Audiência de Alto Valor**: Navegar em Administrador > Audiências > Nova Audiência > Modelos Preditivos. Selecionar "Probabilidade de Compra" e configurar para "Os 10% de usuários com maior probabilidade de compra nos próximos 7 dias". Salvar como "Compradores Futuros - Top 10%".
3.  **Exportar para Google Ads**: Conectar a audiência "Compradores Futuros - Top 10%" ao Google Ads.
4.  **Analisar Desempenho**: Criar um relatório de exploração de "Funil de Vendas" no GA4, aplicando um segmento para a audiência "Compradores Futuros - Top 10%" para observar sua taxa de conversão em comparação com o restante dos usuários.

---

## Core Workflows

### Workflow 1: Prevenção Proativa de Churn com Audiências Preditivas GA4

Este workflow detalha como identificar e intervir proativamente com usuários com alta probabilidade de churn, utilizando as capacidades preditivas do Google Analytics 4.

1.  **Verificação de Requisitos de Dados**: No GA4, navegue até Administrador > Audiências. Ao criar uma nova audiência preditiva, o sistema informará se há dados suficientes para "Probabilidade de Churn". Geralmente, são necessários pelo menos 1.000 usuários recorrentes com eventos de compra e 1.000 usuários que não retornaram (churn) nos últimos 28 dias para que o modelo seja treinado.
2.  **Criação da Audiência de Alto Risco de Churn**:
    *   No GA4, vá para **Administrador > Audiências > Nova Audiência**.
    *   Escolha **Modelos Preditivos** e selecione "Probabilidade de Churn".
    *   Defina a condição: "Probabilidade de Churn (7 dias) > 80". Isso segmentará os 20% dos usuários com maior risco de churn nos próximos 7 dias. Nomeie a audiência como "Alto Risco Churn - 7 Dias".
    *   Opcional: Adicione condições de exclusão, como "Usuários que já realizaram uma compra nos últimos 3 dias", para focar naqueles que não estão ativamente engajados.
3.  **Configuração de Gatilho de Audiência para Eventos Personalizados**:
    *   Dentro da configuração da audiência "Alto Risco Churn - 7 Dias", habilite a opção "Criar evento quando a audiência é acionada".
    *   Nomeie o evento como `churn_risk_high`. Este evento será disparado sempre que um usuário entrar nesta audiência, permitindo automações.
4.  **Ativação de Campanhas de Retenção**:
    *   **Google Ads**: Conecte a audiência "Alto Risco Churn - 7 Dias" ao Google Ads. Crie uma campanha de remarketing com criativos específicos e ofertas de retenção (e.g., "Sua próxima compra com 25% de desconto" ou "Frete grátis no seu próximo pedido").
    *   **Plataforma de E-mail Marketing/CRM (via BigQuery)**: Exporte a lista de `user_id`s dos usuários na audiência `churn_risk_high` via BigQuery (se a integração GA4-BigQuery estiver ativa). Use esta lista para acionar fluxos de e-mail marketing personalizados, mensagens no aplicativo ou contato direto por equipes de sucesso do cliente.
5.  **Monitoramento e Otimização**:
    *   No GA4, crie um **Relatório de Exploração > Visão geral do usuário**. Adicione um segmento para "Alto Risco Churn - 7 Dias" e compare métricas como "Sessões por usuário", "Eventos por sessão", "Receita por usuário" *antes* e *depois* da intervenção da campanha.
    *   Analise a taxa de retenção dos usuários que receberam a campanha vs. um grupo de controle (se implementado) para validar a eficácia da estratégia.

### Workflow 2: Otimização de LTV (Lifetime Value) e Aquisição de Clientes de Alto Valor com GA4

Este workflow foca em identificar usuários com alto potencial de LTV e otimizar estratégias de aquisição e engajamento para maximizar o valor.

1.  **Verificação de Requisitos de Dados para LTV**: Assim como no churn, o GA4 precisa de dados robustos de eventos de compra e receita para treinar modelos de "Probabilidade de Compra" e "Previsão de Receita". Acompanhe a elegibilidade nas configurações de audiência.
2.  **Criação de Audiência de Alto LTV Potencial**:
    *   No GA4, vá para **Administrador > Audiências > Nova Audiência > Modelos Preditivos**.
    *   Selecione "Probabilidade de Compra" e "Previsão de Receita".
    *   Crie uma audiência para "Usuários que nunca compraram E Probabilidade de Compra (7 dias) > 90% E Previsão de Receita (28 dias) > R$ 500". Nomeie a audiência como "Potenciais LTV Alto - R$500+".
    *   Esta audiência identificará visitantes que ainda não compraram, mas o GA4 prevê que farão uma compra de alto valor.
3.  **Ativação de Campanhas de Aquisição e Engajamento**:
    *   **Google Ads (Look-alike)**: Use a audiência "Potenciais LTV Alto - R$500+" como semente para criar audiências look-alike no Google Ads. Isso permite direcionar campanhas de aquisição a novos usuários que se assemelham aos seus futuros clientes mais valiosos.
    *   **Remarketing Direcionado**: Para os usuários dentro da audiência "Potenciais LTV Alto - R$500+", crie campanhas de remarketing com mensagens que destaquem os benefícios de produtos de alto valor ou ofertas de primeira compra que incentivem a conversão (e.g., "Primeira compra com 15% de desconto para produtos premium").
4.  **Análise de Atribuição Preditiva**:
    *   No GA4, acesse **Publicidade > Modelagem de Atribuição > Comparação de Modelos**.
    *   Compare o modelo "Data-driven" com outros modelos (e.g., Último clique) para entender a contribuição de diferentes canais para a aquisição de usuários que posteriormente entram nas audiências de "Potenciais LTV Alto".
    *   Identifique os canais que consistentemente trazem usuários com alta probabilidade de se tornarem clientes de alto LTV e realoque o orçamento de marketing para esses canais.
5.  **Relatórios de Exploração de LTV**:
    *   Crie um **Relatório de Exploração > Tempo de vida do usuário** no GA4.
    *   Adicione um segmento para a audiência "Potenciais LTV Alto - R$500+" e observe como o LTV real se desenvolve ao longo do tempo para esses usuários, validando a precisão do modelo preditivo. Compare com o LTV médio de outras audiências.

---

## Templates

### Configuração de Audiência Preditiva GA4 (Probabilidade de Compra)

```json
{
  "name": "Compradores Altamente Propensos (7 Dias)",
  "description": "Usuários com probabilidade de compra nos próximos 7 dias > 90º percentil, que ainda não compraram.",
  "conditions": [
    {
      "type": "PREDICTIVE_METRIC",
      "metric": "purchase_probability",
      "operator": "GREATER_THAN_OR_EQUAL",
      "value": "90"
    },
    {
      "type": "EVENT",
      "event_name": "purchase",
      "operator": "DOES_NOT_EXIST"
    }
  ],
  "duration_days": 28,
  "event_trigger": {
    "name": "high_purchase_propensity",
    "description": "Evento disparado quando um usuário entra na audiência de alta propensão a comprar."
  },
  "export_destinations": ["GOOGLE_ADS", "BIGQUERY"]
}
```

### Fórmula Simplificada de Previsão de Receita (Fora do GA4, para contexto)

```
Previsão de Receita (Próximos N Dias) = (Número de Compradores Preditivos * Valor Médio de Pedido) + (Número de Compras Recorrentes Preditivas * Valor Médio de Pedido)
```
*   **Exemplo para 7 dias**:
    *   Número de Compradores Preditivos (aqueles que ainda não compraram, mas o modelo prevê que comprarão): 150
    *   Número de Compras Recorrentes Preditivas (clientes existentes que o modelo prevê que comprarão novamente): 50
    *   Valor Médio de Pedido (VMP): R$ 120,00
    *   Previsão de Receita (7 Dias) = (150 * 120) + (50 * 120)
    *   Previsão de Receita (7 Dias) = 18.000 + 6.000 = R$ 24.000,00
*   **Nota**: O GA4 utiliza algoritmos de Machine Learning complexos para Previsão de Receita, mas esta fórmula ilustra os componentes lógicos subjacentes para uma estimativa rápida.

---

## Checklist

- [x] Verificar a elegibilidade dos fluxos de dados GA4 para as métricas preditivas (Probabilidade de Churn, Probabilidade de Compra, Previsão de Receita).
- [x] Criar audiências preditivas estratégicas no GA4 para cenários de retenção (ex: "Alto Risco Churn - 7 Dias") e aquisição de LTV (ex: "Potenciais LTV Alto - R$500+").
- [x] Configurar eventos de gatilho (`churn_risk_high`, `high_purchase_propensity`) para as audiências preditivas para automação.
- [x] Conectar as audiências preditivas ao Google Ads para ativação de campanhas de remarketing, look-alike e ofertas personalizadas.
- [x] Desenvolver e implementar estratégias de retenção ou aquisição específicas para cada audiência preditiva identificada.
- [x] Monitorar a performance das campanhas ativadas usando relatórios de exploração do GA4, segmentando por audiência preditiva.
- [x] Avaliar a precisão dos modelos preditivos do GA4 comparando as previsões com o comportamento real do usuário ao longo do tempo.
- [x] Utilizar o relatório de "Modelagem de Atribuição" no GA4 para entender quais canais contribuem para a aquisição de usuários de alto LTV.
- [x] Considerar a exportação de dados do GA4 para BigQuery para enriquecimento com dados de CRM e criação de modelos preditivos mais avançados.
- [x] Realizar testes A/B nas mensagens e ofertas para as audiências preditivas, otimizando a taxa de conversão e retenção.

---

## Métricas de Referência

| Métrica                      | Benchmark (e-commerce) | Meta (e-commerce) |
|------------------------------|------------------------|-------------------|
| Probabilidade de Churn (média)| < 50%                  | < 30%             |
| Probabilidade de Compra (média)| > 8%                   | > 20%             |
| Previsão de Receita (28 dias)| Varia por negócio      | +15% sobre a média|
| LTV Preditivo vs. Real       | Desvio < 20%           | Desvio < 10%      |
| ROI de Campanhas Preditivas  | > 4:1                  | > 6:1             |
| Taxa de Retenção de Clientes | 25-45%                 | > 55%             |

---

## Erros Comuns

1.  **Ignorar os Requisitos Mínimos de Dados do GA4**: As métricas preditivas do GA4 exigem um volume mínimo de eventos e usuários para treinar os modelos. Tentar usar sem esses dados resultará em "Não elegível" ou modelos imprecisos.
    *   **Como evitar**: Verificar proativamente os relatórios de elegibilidade nas configurações de audiência do GA4. Focar na coleta consistente de eventos de `purchase`, `add_to_cart`, `page_view` e `session_start` por um período prolongado (pelo menos 28 dias).
2.  **Não Conectar Audiências Preditivas a Ações de Marketing**: Criar as audiências no GA4, mas não as utilizar em campanhas ativas no Google Ads, e-mail marketing ou CRM.
    *   **Como evitar**: Sempre exportar as audiências preditivas criadas para o Google Ads imediatamente. Desenvolver um plano de ativação para cada audiência (ex: "Alto Risco Churn" -> Campanha de desconto; "Potenciais LTV Alto" -> Campanha de upsell/look-alike).
3.  **Focar Apenas em Previsões de Curto Prazo**: Limitar a análise preditiva a previsões de 7 ou 28 dias, perdendo a oportunidade de estratégias de longo prazo.
    *   **Como evitar**: Integrar dados do GA4 com BigQuery para criar modelos preditivos de LTV de longo prazo (6 meses, 1 ano) que considerem o ciclo de vida completo do cliente. Usar as previsões de curto prazo para táticas e as de longo prazo para estratégias.

---

## Dicas Avançadas

1.  **Enriquecimento de Modelos Preditivos via BigQuery ML**: Exporte os dados brutos do GA4 para o BigQuery. Combine-os com dados de CRM (ex: histórico de atendimento, dados demográficos externos, interações offline) e use o BigQuery ML para construir modelos preditivos mais robustos e personalizados (ex: propensão a assinar, propensão a upgrade) que superem as capacidades padrão do GA4, importando os resultados como dimensões/métricas personalizadas.
2.  **Atribuição Preditiva Ponderada por LTV**: Em vez de apenas usar o modelo de atribuição "Data-driven" padrão do GA4, desenvolva um modelo de atribuição customizado no BigQuery que pondera a contribuição de cada touchpoint não apenas pela conversão, mas também pelo LTV preditivo do usuário. Isso permite otimizar o investimento em mídia para canais que geram clientes de maior valor futuro, e não apenas volume de conversões.
3.  **Implementação de Testes A/B Dinâmicos com Previsões**: Utilize plataformas de otimização de experiência (ex: Google Optimize, VWO, Optimizely) integradas com GA4 e BigQuery para realizar testes A/B dinâmicos. Por exemplo, um usuário identificado como "Alto Risco Churn" pode receber automaticamente uma oferta de desconto maior em um teste A/B, enquanto um "Potencial LTV Alto" recebe uma mensagem focada em benefícios premium.
4.  **Segmentação de Cohorts Preditivos Detalhada**: Crie relatórios de coorte no GA4 (ou BigQuery) baseados não apenas na data de aquisição, mas também no *status preditivo* inicial do usuário (ex: coorte de "Alto Risco Churn" ao entrar no site). Isso permite analisar como grupos com diferentes predisposições se comportam ao longo do tempo e validar a eficácia das intervenções preditivas.
5.  **Automação de Orçamento de Mídia Baseado em LTV Preditivo**: Utilize APIs do Google Ads e dados de LTV preditivo do GA4/BigQuery para automatizar ajustes de lance e orçamento. Por exemplo, se a audiência "Potenciais LTV Alto" tem um ROI significativamente maior, o sistema pode alocar mais orçamento para campanhas que visam essa audiência ou suas look-alikes de forma programática.