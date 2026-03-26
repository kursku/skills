---
name: campaign-analytics
description: "Campaign Analytics — Skill especializada para campaign analytics"
license: MIT
metadata:
  version: 1.0.0
  author: Cafe Code AI
  category: 15-analytics-dados
  updated: 2026-03-01
risk: safe
---

# Campaign Analytics

Esta skill capacita o Claude Code a realizar análises aprofundadas de performance de campanhas de marketing digital, utilizando dados do Google Analytics 4 (GA4) para otimização e atribuição.

---

## Keywords

Google Analytics 4, GA4, Atribuição de Campanha, ROAS, CPA, LTV, Eventos GA4, Dimensões Personalizadas, Métricas de Engajamento, Explorações GA4, Funil de Conversão, Otimização de Lances, Modelos de Atribuição, Dashboards Looker Studio, Segmentação de Audiência.

---

## Quick Start

1.  **Validar Configuração de Eventos e Conversões no GA4**: Acessar "Administrador" > "Eventos" e "Conversões" no GA4. Garantir que eventos chave como `purchase`, `generate_lead` ou `add_to_cart` estejam registrados e marcados como conversões.
2.  **Analisar Relatório de Aquisição de Tráfego**: Navegar para "Relatórios" > "Aquisição" > "Aquisição de Tráfego" no GA4. Segmentar por "Campanha" para identificar as fontes de tráfego mais eficazes.
3.  **Criar Exploração de Funil de Conversão**: Em "Explorações" > "Funil de Caminho" no GA4, construir um funil com eventos como `page_view` (página de produto), `add_to_cart`, `begin_checkout` e `purchase` para visualizar gargalos.
4.  **Integrar Custos de Campanhas Pagas**: Se usando Google Ads, garantir que a integração automática de custos esteja ativa. Para outras plataformas, importar dados de custo via "Administrador" > "Importação de Dados" > "Dados de Custo".

---

## Core Workflows

### Workflow 1: Análise de Performance de Campanha no GA4

Este workflow detalha como avaliar a eficácia de campanhas de marketing digital utilizando as funcionalidades do Google Analytics 4, focando em métricas de negócio e não apenas de tráfego.

**Passos Detalhados:**

1.  **Configuração Inicial de Eventos e Parâmetros Personalizados:**
    *   **Eventos de Conversão:** Certificar-se de que os eventos mais importantes para o negócio (ex: `purchase`, `generate_lead`, `appointment_booked`) estão configurados como conversões em "Administrador" > "Eventos" > "Marcar como conversão".
    *   **Parâmetros Personalizados:** Para rastrear detalhes específicos da campanha, como `campaign_id` ou `ad_group_name`, configurar dimensões personalizadas com escopo de evento. Exemplo: Criar uma dimensão personalizada "ID da Campanha Externa" mapeada para o parâmetro `campaign_id` que vem via UTMs ou integração.
    *   **Exemplo Prático**: Para uma campanha de Black Friday, garantir que o evento `purchase` capture o `value` (receita) e `currency`, e que uma dimensão personalizada `promotion_name` (valor `black_friday_2024`) esteja sendo enviada junto com o evento.

2.  **Criação de Relatório Personalizado de Aquisição e Engajamento:**
    *   **Explorações no GA4:** Utilizar a funcionalidade "Explorações" para criar relatórios flexíveis.
    *   **Relatório de Funil de Vendas por Campanha:**
        *   Navegar para "Explorações" > "Exploração de Funil".
        *   **Etapas do Funil**:
            1.  Visita à Página de Destino da Campanha (evento `page_view` com `page_location` contendo `/oferta-black-friday/`)
            2.  Adição ao Carrinho (evento `add_to_cart`)
            3.  Início de Checkout (evento `begin_checkout`)
            4.  Compra Concluída (evento `purchase`)
        *   **Dimensão de Detalhamento**: Adicionar "Campanha" (ou a dimensão personalizada `promotion_name`) como dimensão para detalhar cada etapa.
        *   **Métricas**: `Usuários`, `Visualizações`, `Eventos`, `Taxa de Engajamento`, `Receita`.
    *   **Interpretação**: Identificar onde os usuários estão abandonando o funil para campanhas específicas. Se a campanha "Email Black Friday" tem uma alta taxa de abandono no "Início de Checkout", pode indicar um problema no formulário de dados ou na oferta.

3.  **Cálculo de ROAS e CPA por Campanha:**
    *   **Dados Necessários**: Receita (do GA4 via evento `purchase`) e Custo da Campanha (integrado do Google Ads ou importado manualmente).
    *   **Fórmulas**:
        *   `ROAS (Return On Ad Spend) = (Receita Gerada pela Campanha / Custo da Campanha) * 100%`
        *   `CPA (Custo Por Aquisição) = Custo da Campanha / Número de Conversões`
    *   **Exemplo de Relatório no Looker Studio (anteriormente Google Data Studio):**
        *   **Fonte de Dados**: Conectar GA4 e Google Ads.
        *   **Tabela de Dados**:
            | Campanha           | Cliques | Impressões | Custo (R$) | Receita (R$) | Conversões | ROAS (%) | CPA (R$) |
            |--------------------|---------|------------|------------|--------------|------------|----------|----------|
            | Google Search - Promo Verão | 12.500  | 850.000    | 2.500      | 15.000       | 150        | 600%     | 16,67    |
            | Facebook Ads - Retargeting | 8.000   | 1.200.000  | 1.800      | 12.600       | 120        | 700%     | 15,00    |
            | Email Marketing - Lançamento | 5.000   | N/A        | 0          | 8.000        | 100        | N/A      | 0,00     |
        *   **Insight**: A campanha de retargeting no Facebook, embora com menos cliques, apresenta um ROAS superior (700% vs 600%), indicando maior eficiência na geração de receita por real investido.

### Workflow 2: Modelagem de Atribuição e Otimização de Orçamento

Este workflow foca na compreensão de como diferentes pontos de contato contribuem para as conversões e como usar esses insights para otimizar o investimento em mídia.

**Passos Detalhados:**

1.  **Compreensão dos Modelos de Atribuição no GA4:**
    *   **Modelo Padrão (GA4):** O Google Analytics 4 utiliza o modelo de atribuição "Baseada em Dados" (Data-Driven Attribution - DDA) como padrão. Este modelo distribui o crédito da conversão entre os diferentes pontos de contato ao longo da jornada do cliente, usando algoritmos de machine learning para entender o impacto real de cada interação.
    *   **Relatórios de Atribuição (GA4):** Acessar "Publicidade" > "Atribuição" > "Caminhos de Conversão" ou "Comparação de Modelos".
    *   **Caminhos de Conversão**: Este relatório mostra as sequências de canais que levaram a uma conversão.
        *   Exemplo: `Orgânico > Pago > Direto` ou `Email > Social