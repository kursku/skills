---
name: kpi-framework
description: "Kpi Framework — Skill especializada para kpi framework"
license: MIT
metadata:
  version: 1.0.0
  author: Cafe Code AI
  category: 15-analytics-dados
  updated: 2026-03-01
risk: safe
---

# Kpi Framework

Esta skill capacita o Claude a desenvolver, implementar e otimizar frameworks de KPIs robustos e acionáveis, focando em análise de dados com Google Analytics 4 (GA4), dashboards e atribuição de marketing.

---

## Keywords

Framework KPI, Google Analytics 4, Métricas de Desempenho, Dashboards GA4, Atribuição de Marketing, Eventos GA4, Conversões GA4, Modelagem de Dados, Otimização de Funil, Análise Preditiva, Dimensões Personalizadas, Métricas Personalizadas.

---

## Quick Start

1.  **Defina Objetivos de Negócio SMART**: Estabeleça metas específicas, mensuráveis, atingíveis, relevantes e com prazo definido, como "Aumentar a Taxa de Conversão de Compra em 15% nos próximos 6 meses para o público de novos usuários".
2.  **Mapeie Micro-conversões e Eventos GA4**: Identifique as ações intermediárias que levam ao objetivo principal (ex: `view_item_list`, `add_to_cart`, `begin_checkout`) e configure-as como eventos recomendados ou personalizados no GA4.
3.  **Configure Conversões Chave no GA4**: Marque os eventos mais críticos para o negócio (ex: `purchase`, `generate_lead`) como conversões dentro da interface do GA4 (Administrador > Eventos > Marcar como conversão).
4.  **Crie Dimensões e Métricas Personalizadas Essenciais**: Para capturar dados específicos do seu negócio (ex: `product_brand` como dimensão personalizada, `margin_value` como métrica personalizada) e enriquecer a análise de KPIs.
5.  **Construa um Dashboard de Monitoramento no Looker Studio**: Conecte o GA4 e visualize os KPIs primários e secundários em um painel interativo, como "Taxa de Conversão de Compra", "Receita por Usuário" e "CPA por Canal".

---

## Core Workflows

### Workflow 1: Construção de Framework KPI para E-commerce com GA4

Este workflow detalha a criação de um framework KPI para um e-commerce, desde a definição dos objetivos até a configuração e visualização no GA4 e Looker Studio.

**Passos Detalhados:**

1.  **Definição do Objetivo Estratégico do E-commerce**:
    *   **Exemplo**: Aumentar o Volume Bruto de Mercadorias (GMV) em 20% no próximo trimestre, focando em clientes recorrentes.
2.  **Identificação de KPIs Primários e Secundários**:
    *   **KPI Primário (GMV)**: `SUM(price * quantity)` de todas as transações de compra. No GA4, corresponde à métrica "Receita Total".
    *   **KPI Secundários (Fatores do GMV)**:
        *   `Taxa de Conversão de Compra`: `(Total de Compras / Total de Sessões)`
        *   `Valor Médio do Pedido (AOV)`: `Receita Total / Total de Compras`
        *   `Receita por Usuário (RPU)`: `Receita Total / Total de Usuários`
        *   `Frequência de Compra`: `Total de Compras / Total de Compradores Únicos`
3.  **Mapeamento de Eventos e Parâmetros Relevantes no GA4**:
    *   **`view_item_list`**: Evento para visualização de lista de produtos. Parâmetros: `item_list_name`, `item_id`, `item_name`.
    *   **`view_item`**: Evento para visualização de um produto específico. Parâmetros: `item_id`, `item_name`, `price`, `currency`.
    *   **`add_to_cart`**: Evento para adição ao carrinho. Parâmetros: `item_id`, `item_name`, `price`, `quantity`.
    *   **`begin_checkout`**: Evento para início do checkout. Parâmetros: `value`, `currency`.
    *   **`purchase`**: Evento de compra finalizada. Parâmetros: `transaction_id`, `value`, `currency`, `shipping`, `tax`, `items` (array de produtos).
    *   **Configuração GA4**: Certifique-se de que a camada de dados (dataLayer) do seu site está enviando esses eventos com os parâmetros corretos via GTM (Google Tag Manager) para o GA4. Valide no DebugView do GA4.
4.  **Configuração de Conversões no GA4**:
    *   Marque o evento `purchase` como uma conversão em "Administrador > Eventos".
    *   Crie uma audiência personalizada de "Compradores Recorrentes" (Usuários que realizaram `purchase` > 1 vez) para segmentação e análise.
5.  **Criação de Relatórios Personalizados e Dashboards**:
    *   **Relatórios Exploratórios GA4**: Use a ferramenta "Explorações" para criar relatórios de "Funil de Vendas" (visualizando `view_item_list` -> `view_item` -> `add_to_cart` -> `begin_checkout` -> `purchase`) e "Caminhos do Usuário" para entender fluxos.
    *   **Dashboard no Looker Studio**:
        *   Conecte o GA4 como fonte de dados.
        *   Adicione gráficos de evolução para `Receita Total`, `Taxa de Conversão de Compra`, `AOV`.
        *   Crie tabelas detalhando `Receita por Canal de Aquisição` (com modelo de atribuição "baseado em dados").
        *   Inclua um scorecard para o GMV atual versus meta.

### Workflow 2: Otimização de KPIs de Atribuição e Engajamento em Conteúdo B2B

Este workflow foca em como usar o GA4 para entender a contribuição de diferentes canais e o engajamento com conteúdo, otimizando o funil de aquisição de leads B2B.

**Passos Detalhados:**

1.  **Definição de Objetivo de Negócio B2B**:
    *   **Exemplo**: Aumentar a Taxa de Conversão de MQL (Marketing Qualified Lead) para SQL (Sales Qualified Lead) em 10% no próximo semestre, otimizando o conteúdo e os pontos de contato iniciais.
2.  **Identificação de KPIs de Atribuição e Engajamento**:
    *   **KPI de Atribuição**: `Leads Qualificados por Origem` (ex: Organic Search, Paid Search, Social, Direct). Acompanhar o `valor` do evento `generate_lead` atribuído a cada canal.
    *   **KPI de Engajamento**:
        *   `Tempo Médio de Engajamento por Página de Conteúdo` (ex: blog posts, whitepapers).
        *   `Profundidade de Rolagem (Scroll Depth)` em páginas críticas (ex: landing pages).
        *   `Taxa de Conversão de Conteúdo para Lead` (ex: downloads de e-books, preenchimento de formulário).
3.  **Configuração de Eventos de Engajamento e Conversão no GA4**:
    *   **Eventos de Engajamento Aprimorado**: Certifique-se de que "Rolagem" e "Engajamento com vídeo" estão ativos em "Administrador > Fluxos de dados > Configurações de tag > Coleta de eventos".
    *   **Evento `generate_lead`**: Disparado no envio de formulários de contato, download de materiais ricos. Incluir `lead_type` (ex: `ebook_download`, `contact_form`) e `lead_value` (estimativa). Marque como conversão.
    *   **Dimensões Personalizadas**: Crie uma dimensão personalizada baseada no parâmetro `page_category` para agrupar tipos de conteúdo (ex: `blog_post`, `whitepaper`, `case_study`).
4.  **Análise de Caminhos de Conversão e Atribuição**:
    *   **Relatório "Caminhos de Conversão" (Publicidade > Atribuição)**: Analise as sequências de canais que levam a um `generate_lead`. Identifique os canais que iniciam, assistem e fecham a conversão. Compare modelos de atribuição (linear, baseada em dados) para entender a contribuição real.
    *   **Relatório "Visão Geral de Aquisição"**: Segmente por `lead_type` para ver quais canais trazem quais tipos de leads.
5.  **Otimização Baseada em Insights**:
    *   **Exemplo 1 (Atribuição)**: Se o relatório "Caminhos de Conversão" mostra que "Pesquisa Orgânica" frequentemente inicia o caminho para leads de "Whitepaper", mas "Email Marketing" fecha a conversão, foque em otimizar o SEO para termos de topo de funil e a nutrição por e-mail para engajamento.
    *   **Exemplo 2 (Engajamento)**: Se o `Tempo Médio de Engajamento` em "Artigos de Blog" é baixo, mas `Profundidade de Rolagem` é alta para "Case Studies", otimize o conteúdo do blog para ser mais direto e adicione CTAs mais visíveis para downloads de case studies.
    *   **Segmentação de Audiências**: Crie audiências no GA4 de "Usuários Engajados com Conteúdo B2B" (tempo de engajamento > 60s em páginas de blog e > 50% de rolagem) para retargeting em campanhas pagas.

---

## Templates

### Template de Ficha de KPI

```markdown
**Nome do KPI:** Taxa de Conversão de Compra
**Descrição:** A porcentagem de sessões que resultaram em uma compra no e-commerce.
**Objetivo Estratégico Relacionado:** Aumento do GMV e otimização do funil de vendas.
**Fórmula:** (Total de eventos `purchase` / Total de eventos `session_start`) * 100
**Fonte de Dados:** Google Analytics 4 (Relatório "Monetização > Visão geral de e-commerce", ou "Eventos").
**Frequência de Monitoramento:** Diária, Semanal, Mensal.
**Meta:** 2.5% (Benchmark do setor para e-commerce em moda).
**Responsável:** Analista de Marketing Digital / Gerente de E-commerce.
**Observações:** Excluir sessões de bots ou tráfego interno.
```

### Template de Dashboard de Acompanhamento GA4 (Visão Geral E-commerce)

```markdown
# Dashboard de Performance E-commerce - GA4

**Período:** Últimos 30 dias

---

## Scorecards Principais

| Métrica                 | Valor Atual | Variação (vs. período anterior) | Meta    |
|-------------------------|-------------|---------------------------------|---------|
| Receita Total           | R$ 150.000  | +12%                            | R$ 160.000 |
| Taxa de Conversão de Compra | 2.3%        | +0.3 p.p.                       | 2.5%    |
| Valor Médio do Pedido (AOV) | R$ 250      | -5%                             | R$ 260  |
| Usuários Ativos         | 65.000      | +8%                             | 70.000  |

---

## Tendência de Receita e Conversão (Gráfico de Linha)

**Eixo Y1:** Receita Total (R$)
**Eixo Y2:** Taxa de Conversão de Compra (%)
**Eixo X:** Data

---

## Desempenho por Canal de Aquisição (Tabela)

| Canal de Aquisição | Receita Total | Taxa de Conversão | AOV     | Custo (GA4/Ads) | ROAS (Receita/Custo) |
|--------------------|---------------|-------------------|---------|-----------------|----------------------|
| Organic Search     | R$ 60.000     | 2.8%              | R$ 280  | -               | -                    |
| Paid Search        | R$ 45.000     | 2.1%              | R$ 240  | R$ 10.000       | 4.5x                 |
| Email              | R$ 25.000     | 3.5%              | R$ 300  | -               | -                    |
| Direct             | R$ 10.000     | 1.8%              | R$ 220  | -               | -                    |

---

## Funil de Compras (Gráfico de Funil GA4)

1.  **Visualizações de Produto (`view_item`)**: 100.000
2.  **Adições ao Carrinho (`add_to_cart`)**: 25.000 (25% taxa de abandono)
3.  **Início de Checkout (`begin_checkout`)**: 10.000 (60% taxa de abandono)
4.  **Compras (`purchase`)**: 6.000 (40% taxa de abandono)

---

## Produtos Mais Vendidos (Tabela)

| Produto ID | Nome do Produto   | Receita Total | Quantidade Vendida |
|------------|-------------------|---------------|--------------------|
| P001       | Tênis Esportivo   | R$ 20.000     | 100                |
| P002       | Camiseta Dry-Fit  | R$ 15.000     | 150                |
| P003       | Mochila Urbana    | R$ 12.000     | 60                 |
```

---

## Checklist

- [x] O objetivo de negócio do KPI está claramente definido e alinhado com a estratégia geral.
- [x] O KPI é mensurável e possui uma fonte de dados confiável (GA4 configurado corretamente).
- [x] Os eventos e parâmetros necessários para o KPI estão configurados e validados no GA4 (via DebugView).
- [x] Dimensões e métricas personalizadas essenciais para o KPI foram criadas no GA4.
- [x] O KPI é acionável, permitindo a tomada de decisões claras e estratégicas.
- [x] Existe um benchmark ou meta realista para o KPI, baseado em dados históricos ou de mercado.
- [x] A frequência de monitoramento do KPI está definida e é adequada à sua natureza.
- [x] Um responsável claro foi atribuído para o monitoramento e otimização do KPI.
- [x] O KPI está integrado a um dashboard visual e acessível (ex: Looker Studio).
- [x] O modelo de atribuição no GA4 (Preferencialmente "baseado em dados") foi revisado e compreendido para análise do KPI.

---

## Métricas de Referência

| Métrica                      | Benchmark (E-commerce Geral) | Meta (Exemplo) |
|------------------------------|------------------------------|----------------|
| Taxa de Conversão de Compra  | 1.5% - 3.5%                  | 2.8%           |
| Valor Médio do Pedido (AOV)  | R$ 150 - R$ 400              | R$ 280         |
| Custo por Aquisição (CPA)    | R$ 30 - R$ 150               | R$ 60          |
| Taxa de Rejeição (Bounce Rate) | 30% - 50%                    | < 40%          |
| Tempo Médio de Engajamento   | 60s - 180s                   | > 120s         |
| ROAS (Retorno sobre Investimento em Anúncios) | 2.5x - 4x                    | > 3x           |

---

## Erros Comuns

1.  **Escolha de Métricas de Vaidade**: Focar em KPIs como "visualizações de página" ou "usuários" sem conectá-los a um objetivo de negócio real.
    *   **Como evitar**: Sempre pergunte: "Este KPI me ajuda a tomar uma decisão para o objetivo de negócio X?". Ex: Em vez de "Total de Visualizações de Página", use "Taxa de Conversão de Páginas de Produto para Adição ao Carrinho".
2.  **Configuração Incorreta ou Incompleta do GA4**: Eventos e conversões mal implementados levam a dados errados, inviabilizando a análise de KPIs.
    *   **Como evitar**: Use o DebugView do GA4 e o Google Tag Assistant para validar *todos* os eventos, parâmetros e conversões em tempo real durante a implementação e após qualquer alteração no site.
3.  **Ignorar o Contexto do Negócio e do Setor**: Adotar KPIs genéricos ou benchmarks sem considerar as especificidades da sua indústria, público-alvo ou modelo de negócio.
    *   **Como evitar**: Pesquise benchmarks específicos para seu nicho de mercado e ajuste as metas e expectativas. Um e-commerce de luxo terá um AOV diferente de um de produtos de consumo rápido.
4.  **Falta de Acionabilidade dos KPIs**: Definir KPIs que, mesmo medidos, não fornecem insights claros sobre o que precisa ser feito para melhorar.
    *   **Como evitar**: Cada KPI deve ter uma clara relação de causa e efeito com ações que podem ser tomadas. Se o KPI "Taxa de Abandono de Carrinho" aumenta, a ação pode ser "Otimizar o fluxo de checkout" ou "Revisar custos de frete".
5.  **Confundir Atribuição (GA4) com Último Clique**: Utilizar o modelo de atribuição "Último Clique" por padrão no GA4 para todos os relatórios, ignorando a contribuição de outros canais ao longo da jornada do cliente.
    *   **Como evitar**: Prefira o modelo de atribuição "Baseado em Dados" no GA4 (relatórios de Publicidade > Atribuição) para ter uma visão mais holística da contribuição de cada canal, especialmente em jornadas de compra complexas.

---

## Dicas Avançadas

1.  **Utilização de Dimensões e Métricas Personalizadas para Segmentação Profunda**: Para um e-commerce, crie dimensões personalizadas para `product_category`, `product_brand` e `user_segment` (ex: `VIP`, `Novo Cliente`). Combine com métricas personalizadas como `product_margin` (se enviada via dataLayer) para analisar a rentabilidade de KPIs por segmentos específicos. Ex: "Margem de Lucro por Categoria de Produto e Segmento VIP".
2.  **Análise de Cohort para Retenção e LTV (Lifetime Value)**: No GA4, use a "Exploração de Cohort" para analisar a retenção de usuários ao longo do tempo. Crie cohorts baseados na data da primeira compra e acompanhe KPIs como `Receita por Usuário` ou `Frequência de Compra` para entender o LTV. Isso permite identificar quais cohorts performam melhor e otimizar estratégias de aquisição.
3.  **Integração GA4 com BigQuery para Modelagem de Atribuição Preditiva**: Exporte os dados brutos do GA4 para o BigQuery. Com SQL e modelos de machine learning (ex: Markov Chains, Shapley Values), desenvolva modelos de atribuição mais sofisticados que vão além dos padrões do GA4, permitindo prever a contribuição futura de canais e otimizar o investimento em marketing com base no LTV real.
4.  **Criação de Audiências Preditivas no GA4**: Utilize os recursos de audiências preditivas do GA4 (ex: "Potenciais Compradores", "Potenciais Abandono de Compra") para segmentar usuários que provavelmente farão uma compra nos próximos 7 dias ou que tendem a abandonar. Integre essas audiências com Google Ads para campanhas de retargeting ou prospecção altamente direcionadas, otimizando o CPA.
5.  **Análise de Desempenho de Campanha com Parâmetros UTM Avançados**: Implemente uma taxonomia de UTMs rigorosa e consistente (ex: `utm_source=facebook_ads`, `utm_medium=cpc`, `utm_campaign=black_friday_2024`, `utm_content=banner_promocional_2x1`, `utm_term=tenis_esportivo_azul`). Use essas dimensões no GA4 para analisar o desempenho de KPIs como `Taxa de Conversão` e `ROAS` em um nível granular, identificando quais criativos ou segmentos de campanha geram os melhores resultados.