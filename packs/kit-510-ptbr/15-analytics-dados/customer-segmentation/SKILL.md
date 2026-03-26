---
name: customer-segmentation
description: "Customer Segmentation — Skill especializada para customer segmentation"
license: MIT
metadata:
  version: 1.0.0
  author: Cafe Code AI
  category: 15-analytics-dados
  updated: 2026-03-01
risk: safe
---

# Customer Segmentation

Esta skill capacita o Claude a estruturar, executar e analisar estratégias de segmentação de clientes usando Google Analytics 4 e outras ferramentas de dados.

---

## Keywords

Google Analytics 4, GA4, Segmentação Comportamental, Segmentação Demográfica, RFM, LTV, Valor do Ciclo de Vida do Cliente, Audiências GA4, Explorações GA4, Atribuição de Marketing, Métricas de Segmento, Clusterização de Clientes, Personas Digitais, Funil de Conversão, Retenção de Clientes, Google BigQuery, Dimensões Personalizadas GA4.

---

## Quick Start

1.  **Configurar Eventos de Conversão no GA4**: Assegure que eventos chave como `purchase`, `add_to_cart`, `lead_form_submit` e `sign_up` estejam marcados como conversões em "Administrador > Eventos".
2.  **Habilitar Sinais do Google**: Ative "Sinais do Google" em "Administrador > Configurações de Dados > Coleta de Dados" para acesso a dados demográficos e de interesses.
3.  **Criar uma Audiência Inicial de "Compradores Recentes"**: Navegue para "Administrador > Audiências", clique em "Nova audiência", selecione "Criar uma audiência personalizada". Defina "Incluir usuários quando: Evento = `purchase` E Data do Evento (últimos 30 dias)".
4.  **Analisar Desempenho da Audiência no Relatório "Usuários > Visão geral"**: Publique a audiência e, após 24-48 horas, aplique-a como uma comparação de segmento no relatório para ver métricas de engajamento e conversão.
5.  **Exportar Audiência para Google Ads**: Vincule o GA4 ao Google Ads e ative a audiência para retargeting, observando o desempenho da campanha e o custo por aquisição (CPA) do segmento.

---

## Core Workflows

### Workflow 1: Criação de Segmentos RFM-like no GA4 para Otimização de Retenção

Este workflow detalha a construção de segmentos baseados nos princípios de Recência, Frequência e Valor Monetário (RFM) utilizando os recursos de Audiências e Explorações do GA4, focando na retenção e valor do cliente.

**Passos Detalhados:**

1.  **Definir Critérios para Recência, Frequência e Valor Monetário (RFM-like):**
    *   **Recência:** Última vez que o usuário realizou uma compra (`purchase` event).
        *   Exemplo: "Recente" = comprou nos últimos 30 dias.
        *   Exemplo: "Antigo" = comprou há mais de 90 dias.
    *   **Frequência:** Número de compras (`purchase` event count).
        *   Exemplo: "Frequente" = `>= 3` compras.
        *   Exemplo: "Ocasional" = `1-2` compras.
    *   **Valor Monetário:** Receita total gerada (`value` parameter do `purchase` event).
        *   Exemplo: "Alto Valor" = `total_revenue >= $500`.
        *   Exemplo: "Médio Valor" = `$100 <= total_revenue < $500`.

2.  **Criar Audiências Baseadas em Recência e Frequência no GA4:**
    *   Acesse "Administrador > Audiências > Nova audiência > Criar uma audiência personalizada".
    *   **Audiência "Compradores Recentes & Frequentes":**
        *   Condição 1: "Incluir Usuários > Evento = `purchase`"
        *   Grupo de Condição 2 (dentro do mesmo grupo OU):
            *   Condição: "Evento = `purchase`" com "Contagem de Eventos (no mesmo evento) >= 3"
            *   Condição: "Data do Evento (para o evento `purchase`) está nos últimos 30 dias"
        *   Nome da Audiência: `CRM_CompradoresRecentesFrequentes_30d_3+Compras`
    *   **Audiência "Compradores Antigos & Ocasionais":**
        *   Condição 1: "Incluir Usuários > Evento = `purchase`"
        *   Grupo de Condição 2 (dentro do mesmo grupo OU):
            *   Condição: "Evento = `purchase`" com "Contagem de Eventos (no mesmo evento) <= 2"
            *   Condição: "Data do Evento (para o evento `purchase`) está há mais de 90 dias"
        *   Nome da Audiência: `CRM_CompradoresAntigosOcasionais_90d+d_1-2Compras`
    *   *Nota:* O valor monetário direto como critério de audiência é mais complexo no GA4 sem dimensões personalizadas de usuário específicas. Para "Valor Monetário", usaremos a análise em "Explorações".

3.  **Analisar o Desempenho e Valor Monetário dos Segmentos via Explorações (Explorations):**
    *   Acesse "Explorar" no menu lateral esquerdo do GA4.
    *   Crie uma nova "Exploração de Forma Livre".
    *   **Configuração da Exploração:**
        *   **Dimensões:** Importe `Nome da audiência` (Audience name), `País` (Country), `Primeira fonte/mídia do usuário` (User first source/medium).
        *   **Métricas:** Importe `Receita total` (Total revenue), `Receita por usuário` (Revenue per user), `Conversões` (Conversions), `Taxa de conversão de compra` (Purchase conversion rate).
        *   **Linhas:** Arraste `Nome da audiência`.
        *   **Valores:** Arraste `Receita total`, `Receita por usuário`, `Conversões`, `Taxa de conversão de compra`.
        *   **Filtros:** Adicione um filtro "Nome da audiência" para incluir as audiências RFM-like criadas (e.g., "Nome da audiência" "contém" `CRM_CompradoresRecentes`).
    *   **Interpretação:** Compare a `Receita por usuário` e `Taxa de conversão de compra` entre as diferentes audiências. Por exemplo, a audiência `CRM_CompradoresRecentesFrequentes_30d_3+Compras` deve apresentar uma `Receita por usuário` significativamente maior (ex: R$ 150,00) e `Taxa de conversão de compra` mais alta (ex: 5.8%) em comparação com `CRM_CompradoresAntigosOcasionais_90d+d_1-2Compras` (ex: R$ 35,00 e 0.9%).

4.  **Ativação e Otimização:**
    *   **Exportar para Google Ads:** Use as audiências para campanhas de retargeting personalizadas, oferecendo promoções exclusivas para "Compradores Antigos & Ocasionas" para reengajá-los.
    *   **Personalização de Conteúdo:** Integre as audiências com plataformas de otimização de experiência para exibir banners ou recomendações de produtos específicos no site, baseados no histórico de compra do segmento.

### Workflow 2: Segmentação de Usuários por Canal de Atribuição e Análise de LTV

Este workflow foca em entender o comportamento e o Valor do Ciclo de Vida (LTV) de usuários provenientes de diferentes canais de marketing, usando os modelos de atribuição do GA4.

**Passos Detalhados:**

1.  **Definir Canais de Atribuição para Análise:**
    *   Foco em `Primeira fonte/mídia do usuário` (User first source/medium) para entender o canal que *introduziu* o usuário.
    *   Exemplos: `google / cpc`, `google / organic`, `(direct) / (none)`, `facebook / social`, `email / newsletter`.

2.  **Criar Segmentos Personalizados Baseados em Atribuição no GA4:**
    *   Acesse "Explorar" no GA4 e crie uma "Exploração de Segmentos".
    *   Clique em "Novo segmento > Segmento de usuário".
    *   **Segmento "Usuários de Busca Paga (Google Ads)":**
        *   Condição: "Incluir Usuários > Primeira fonte/mídia do usuário" "contém" `google / cpc`
        *   Nome do Segmento: `Atrib_BuscaPagaGoogleAds`
    *   **Segmento "Usuários de Busca Orgânica (Google)":**
        *   Condição: "Incluir Usuários > Primeira fonte/mídia do usuário" "contém" `google / organic`
        *   Nome do Segmento: `Atrib_BuscaOrganicaGoogle`
    *   **Segmento "Usuários de Email Marketing":**
        *   Condição: "Incluir Usuários > Primeira fonte/mídia do usuário" "contém" `email / newsletter`
        *   Nome do Segmento: `Atrib_EmailMarketing`
    *   *Nota:* Para fontes/mídias específicas, assegure-se de que a tagagem UTM esteja correta nas suas campanhas de marketing para refletir com precisão a origem.

3.  **Analisar o LTV e Comportamento dos Segmentos com "Exploração de Ciclo de Vida do Usuário":**
    *   Em "Explorar", crie uma "Exploração de Ciclo de Vida do Usuário" (User Lifetime).
    *