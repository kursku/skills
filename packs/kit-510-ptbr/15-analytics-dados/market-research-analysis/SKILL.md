---
name: market-research-analysis
description: "Market Research Analysis — Skill especializada para market research analysis"
license: MIT
metadata:
  version: 1.0.0
  author: Cafe Code AI
  category: 15-analytics-dados
  updated: 2026-03-01
risk: safe
---

# Market Research Analysis

Esta skill capacita o Claude a executar análises de mercado detalhadas, utilizando dados de Google Analytics 4 para identificar tendências, segmentar audiências e otimizar estratégias digitais.

---

## Keywords

GA4 Analytics, Análise de Cohort, Atribuição de Marketing, Segmentação de Audiência, LTV (Lifetime Value), CPA (Custo por Aquisição), ROAS (Retorno sobre Gasto com Anúncios), Funil de Conversão, Explorações GA4, Dimensões Personalizadas, Métricas Personalizadas, Jornada do Cliente.

---

## Quick Start

1.  **Valide a Coleta de Eventos Essenciais no GA4**: Confirme se eventos como `page_view`, `view_item`, `add_to_cart`, `begin_checkout`, `purchase` e `generate_lead` estão sendo coletados corretamente, com parâmetros de item e valor devidamente configurados.
2.  **Crie uma Exploração de Funil de Vendas**: No GA4, navegue até `Explorar > Galeria de modelos > Funil de Vendas`, configure os passos para `view_item > add_to_cart > begin_checkout > purchase` e adicione uma dimensão de quebra como `Grupo de canais padrão` para identificar gargalos por origem de tráfego.
3.  **Configure uma Audiência de Alto LTV Potencial**: No GA4, vá em `Administrador > Audiências > Nova audiência`, crie uma audiência baseada em eventos de `purchase` com `valor_total_da_compra > R$ 500` e `count_of_purchases >= 2` para segmentar clientes recorrentes de alto valor.
4.  **Analise o Relatório de Atribuição Baseado em Dados**: Acesse `Publicidade > Atribuição > Caminhos de Conversão` e filtre por um tipo de conversão específico (ex: `purchase`). Compare o modelo "Baseado em dados" com "Último clique" para identificar canais que contribuem em etapas iniciais da jornada mas são subestimados pelo modelo padrão.

---

## Core Workflows

### Workflow 1: Análise de Segmentação de Mercado e Comportamento de Consumo no GA4

Este workflow detalha a identificação e análise de segmentos de mercado específicos através de dados comportamentais no Google Analytics 4, permitindo a personalização de estratégias de marketing.

**Passos Detalhados:**

1.  **Estruturar a Pergunta de Negócio**: Em vez de "identificar o público", defina, por exemplo: "Quais segmentos de usuários demonstram maior engajamento e LTV no e-commerce de vestuário online 'TrendyWear' e como seu comportamento difere entre mobile e desktop?"
2.  **Configurar Dimensões Personalizadas Essenciais**:
    *   No GA4, vá em `Administrador > Definições de dados > Definições personalizadas > Criar dimensão personalizada`.
    *   **Exemplo 1**: Crie uma dimensão de escopo de usuário `customer_segment` que captura o segmento de um usuário (e.g., "Novato", "Leal", "VIP") enviado via `gtag('set', {'user_properties': {'customer_segment': 'VIP'}})` após o login ou compra.
    *   **Exemplo 2**: Crie uma dimensão de escopo de evento `product_category` para o evento `view_item` se a categoria não for automaticamente coletada, usando `gtag('event', 'view_item', {'items': [{'item_category': 'Roupas de Verão'}]})`.
3.  **Criar Explorações de Segmento de Usuários**:
    *   No GA4, navegue até `Explorar > Galeria de modelos > Exploração de Segmentos de Usuários`.
    *   **Configuração de Segmentos**:
        *   **Segmento A (Mobile Engajado)**: `Dispositivo = mobile` E `Sessões por usuário >= 3` E `Duração média da sessão >= 180 segundos`.
        *   **Segmento B (Desktop Comprador)**: `Dispositivo = desktop` E `Evento = purchase` E `Receita total > R$ 200`.
    *   **Análise de Métricas**: Compare `Taxa de Conversão`, `LTV`, `Receita por usuário`, `Média de engajamento por sessão` e `Número de eventos` entre os segmentos.
    *   **Visualização**: Utilize gráficos de barras para comparar o desempenho das métricas-chave e tabelas para detalhar eventos específicos (e.g., `add_to_cart`, `view_item_list`) por segmento.
4.  **Análise de Coorte para Retenção**:
    *   No GA4, vá em `Explorar > Galeria de modelos > Exploração de Coorte`.
    *   **Definição de Coorte**: Use `Aquisição de usuários` como a base da coorte e `Data da primeira compra` ou `Data do primeiro engajamento` como o critério de inclusão.
    *   **Métricas de Detalhamento**: Selecione `Transações`, `Receita total` e `Usuários ativos`.
    *   **Interpretação**: Observe a porcentagem de retenção em semanas ou meses subsequentes e a receita gerada por cada coorte. Uma queda acentuada na retenção da coorte de Janeiro/2024 após a 3ª semana pode indicar um problema com a experiência pós-compra ou um produto específico.

### Workflow 2: Otimização de Atribuição de Marketing e ROI com Dados de GA4

Este workflow foca em entender a contribuição real de cada canal de marketing para as conversões, utilizando os modelos de atribuição do GA4 para otimizar o investimento e o ROAS.

**Passos Detalhados:**

1.  **Definir Eventos de Conversão Prioritários**: Confirme que os principais eventos de conversão (e.g., `purchase`, `generate_lead`, `form_submit`, `subscription_start`) estão marcados como conversões no GA4 (`Administrador > Eventos > Marcar como conversão`).
2.  **Analisar Relatórios de Atribuição de Conversões**:
    *   Navegue até `Publicidade > Atribuição > Comparação de modelos`.
    *   **Modelos de Comparação**: Selecione "Último clique (pago e orgânico)" e "Baseado em dados".
    *   **Dimensão**: Escolha `Grupo de canais padrão` ou `Origem/Mídia`.
    *   **Métrica**: `Conversões` e `Receita total`.
    *   **Interpretação**: Observe as diferenças nas contagens de conversão e receita entre os modelos. Se o canal "Display" tiver 100 conversões no "Baseado em dados" mas apenas 10 no "Último clique", isso indica que ele é um canal importante na fase inicial da jornada do cliente, sendo subestimado pelo modelo de último clique.
3.  **Analisar Caminhos de Conversão**:
    *   Acesse `Publicidade > Atribuição > Caminhos de Conversão`.
    *   **Dimensão Principal**: `Grupo de canais padrão` ou `Origem/Mídia`.
    *   **Comprimento do Caminho**: Filtre por caminhos com 3 ou mais interações para entender jornadas complexas.
    *   **Interpretação**: Identifique sequências comuns de canais que levam a conversões (e.g., `Orgânico > Direto > E-mail` ou `Social Pago > Pesquisa Paga > Direto`). Canais que aparecem frequentemente no início dos caminhos são valiosos para o reconhecimento da marca, mesmo que não sejam o último clique.
4.  **Calcular ROAS por Canal com Base no Modelo de Dados**:
    *   Exporte os dados de conversão por canal (usando o modelo "Baseado em dados") do GA4.
    *   Obtenha os dados de custo de campanha de suas plataformas de anúncios (Google Ads, Facebook Ads, etc.).
    *   **Fórmula ROAS**: `(Receita Atribuída ao Canal / Custo do Canal) * 100`.
    *   **Exemplo**: Se o canal "Pesquisa Paga" gerou R$ 15.000 em receita atribuída (pelo modelo baseado em dados) e teve um custo de R$ 3.000, o ROAS é `(15000 / 3000) * 100 = 500%`.
5.  **Otimização de Orçamento com Base na Atribuição**:
    *   Direcione o orçamento para canais com maior ROAS no modelo "Baseado em dados", mesmo que não sejam os últimos cliques.
    *   Invista em canais que iniciam a jornada do cliente (e.g., Display, Social Pago) se o modelo de atribuição mostrar que eles contribuem significativamente para a decisão final.

---

## Templates

### Brief de Pesquisa de Mercado para Análise GA4 - Lançamento de Produto "FitLife Suplementos"

```
**Título do Projeto:** Análise de Mercado para Lançamento do Suplemento "Proteína Max" da FitLife Suplementos

**Objetivo Central:** Entender o perfil comportamental dos usuários de suplementos proteicos no website da FitLife e identificar oportunidades de otimização para o lançamento da "Proteína Max", focando em engajamento e conversão de novos clientes.

**Perguntas de Negócio Específicas:**
1. Qual o LTV médio dos clientes que já compraram suplementos proteicos nos últimos 6 meses?
2. Quais os principais canais de aquisição para usuários que visualizam produtos da categoria "Suplementos Proteicos"?
3. Existe uma diferença significativa na taxa de conversão entre usuários mobile e desktop para produtos de alta proteína?
4. Quais eventos de micro-conversão (e.g., `add_to_cart`, `view_item_list` na categoria) estão mais correlacionados com a compra final de suplementos?
5. Qual o comportamento de engajamento (tempo na página, número de sessões) de usuários que visitam páginas de "Proteína Max" mas não compram?

**Período de Análise dos Dados GA4:** 01/01/2024 a 31/03/2024 (3 meses pré-lançamento)

**Segmentos de Audiência a Explorar:**
*   **Compradores de Suplementos Proteicos**: Usuários que acionaram o evento `purchase` com `item_category = 'Suplementos Proteicos'`.
*   **Visitantes da Categoria Proteína**: Usuários que visualizaram produtos (`view_item`) na categoria 'Suplementos Proteicos' mas não compraram.
*   **Novos Usuários Adquiridos**: Usuários cuja `primeira_visita` ocorreu no período de análise e que interagiram com a categoria.

**Relatórios e Explorações GA4 Requeridos:**
*   **Exploração de Funil de Vendas**: Da visualização da página do produto "Proteína Max" até a compra (`view_item_ProteinaMax > add_to_cart > begin_checkout > purchase`).
*   **Exploração de Segmentos de Usuários**: Comparando o comportamento dos segmentos definidos acima em relação a `LTV`, `Taxa de Conversão`, `Eventos de Engajamento`.
*   **Relatório de Aquisição de Tráfego**: Filtrado por `item_category = 'Suplementos Proteicos'`.
*   **Relatório de Atribuição (Caminhos de Conversão)**: Para eventos de `purchase` na categoria 'Suplementos Proteicos'.

**Entregáveis Esperados:**
*   Relatório de insights sobre o perfil do consumidor de suplementos proteicos.
*   Recomendações de otimização para funil de vendas do novo produto.
*   Sugestões de segmentação para campanhas de marketing pós-lançamento.
```

### Relatório de Desempenho de Segmento de Audiência (GA4) - E-commerce de Vestuário "TrendyWear"

```
**Título do Relatório:** Desempenho do Segmento "Compradores Recorrentes de Alto Valor" - Q1 2024

**Período de Análise:** 01/01/2024 - 31/03/2024

**Segmento Analisado:**
*   **Nome:** Compradores Recorrentes de Alto Valor
*   **Definição GA4:** `purchase` event count >= 2 E `lifetime_value` >= R$ 800

**Visão Geral do Segmento:**
*   **Número de Usuários no Segmento:** 12.450
*   **Representatividade na Audiência Total:** 8.5%
*   **Principais Canais de Aquisição:** Pesquisa Orgânica (35%), E-mail Marketing (28%), Direto (19%)

**Métricas Chave de Desempenho:**

| Métrica GA4                   | Valor do Segmento | Média do Site | Diferença vs. Média |
|-------------------------------|-------------------|---------------|---------------------|
| Receita Total (R$)            | R$ 9.870.000      | R$ 1.250.000  | +690%               |
| Receita por Usuário (R$)      | R$ 792,77         | R$ 86,21      | +819%               |
| Taxa de Conversão de E-commerce | 12.8%             | 1.9%          | +573%               |
| Média de Itens por Compra     | 2.7               | 1.5           | +80%                |
| Duração Média da Sessão       | 00:04:15          | 00:01:50      | +131%               |
| Taxa de Engajamento           | 78.5%             | 55.2%         | +42%                |

**Análise Comportamental:**
*   **Produtos Mais Vistos:** Vestidos de Verão (18%), Calças Jeans Premium (15%), Blusas de Seda (12%).
*   **Caminhos de Conversão Comuns:**
    1.  E-mail Marketing -> Direto -> Purchase
    2.  Pesquisa Orgânica -> Pesquisa Paga (Marca) -> Purchase
    3.  Referral (Blog de Moda) -> Direto -> Purchase
*   **Interação com Eventos:** Alta frequência de `add_to_cart` (média de 4 por usuário antes da compra) e `view_item` (média de 15 por usuário).

**Insights e Recomendações:**
*   **Foco no E-mail Marketing:** O canal de e-mail é crucial para nutrir e converter este segmento de alto valor. Investir em automações de e-mail personalizadas e ofertas exclusivas.
*   **Otimização de Páginas de Produtos:** Garantir a qualidade das páginas dos produtos mais visualizados por este segmento (Vestidos, Jeans, Blusas) para maximizar a conversão, incluindo avaliações e fotos de alta qualidade.
*   **Estratégias de Retenção:** Desenvolver programas de fidelidade e comunicação personalizada baseada nas preferências de compra deste segmento, aproveitando o alto LTV.
*   **Atribuição Multitoque:** Reconhecer a importância dos canais de início de jornada (Referral, Pesquisa Orgânica) para este segmento e otimizar o investimento considerando sua contribuição inicial.
```

---

## Checklist

-   [x] Validar a coleta de dados de e-commerce (itens, valor, moeda) no GA4.
-   [x] Confirmar que os eventos de conversão primários estão marcados corretamente no GA4.
-   [x] Auditar a configuração de Dimensões e Métricas Personalizadas relevantes para a pesquisa.
-   [x] Criar e analisar no mínimo duas "Explorações" no GA4 (ex: Funil de Vendas, Segmentos de Usuários).
-   [x] Comparar modelos de atribuição (Último Clique vs. Baseado em Dados) para as principais conversões.
-   [x] Segmentar a audiência por LTV ou valor de compra para identificar clientes de alto valor.
-   [x] Documentar as hipóteses de mercado antes de iniciar a análise de dados.
-   [x] Correlacionar dados de GA4 com dados de custo de mídia externa para cálculo de ROAS real.
-   [x] Analisar a jornada do cliente através dos "Caminhos de Conversão" no GA4 Publicidade.
-   [x] Verificar a consistência dos dados em diferentes relatórios do GA4 para evitar discrepâncias.

---

## Métricas de Referência

| Métrica GA4            | Benchmark (E-commerce Geral) | Meta (Empresa Fictícia "TechGadget") |
|------------------------|------------------------------|--------------------------------------|
| Taxa de Conversão E-commerce | 1.5% - 3.5%                  | 4.0%                                 |
| Custo por Aquisição (CPA) | R$ 80 - R$ 250               | R$ 120                               |
| Lifetime Value (LTV)   | R$ 400 - R$ 1.500              | R$ 1.000                             |
| ROAS (Retorno sobre Ad Spend) | 2x - 4x                      | 3.5x                                 |
| Taxa de Engajamento    | 50% - 70%                    | 65%                                  |
| Média de Sessões por Usuário | 1.5 - 2.5                    | 2.0                                  |

---

## Erros Comuns

1.  **Coleta de Dados Inconsistente ou Incompleta**: Muitos analistas assumem que o GA4 está coletando todos os dados necessários sem verificar. Por exemplo, parâmetros como `item_id`, `item_name`, `price`, `quantity` podem estar faltando nos eventos de e-commerce, inviabilizando análises detalhadas de produtos.
    *   **Como evitar**: Realize uma auditoria detalhada de implementação do GA4 usando o "DebugView" e ferramentas como o Google Tag Assistant. Confirme que todos os eventos e parâmetros esperados estão sendo enviados corretamente para cada etapa do funil.
2.  **Foco Exclusivo no Último Clique para Atribuição**: Utilizar apenas o modelo de atribuição de "Último Clique" leva a uma visão distorcida do valor real de canais que contribuem em etapas anteriores da jornada, como Display ou Social. Isso pode resultar em subinvestimento em canais cruciais para o reconhecimento e consideração da marca.
    *   **Como evitar**: Sempre compare múltiplos modelos de atribuição no GA4 (e.g., "Último Clique", "Primeiro Clique", "Linear", "Baseado em Dados") nos relatórios de `Publicidade > Atribuição`. Priorize a otimização de orçamento com base no modelo "Baseado em Dados" para uma visão mais holística.
3.  **Ignorar Micro-Conversões**: Concentrar-se apenas em grandes conversões (ex: `purchase`) sem analisar eventos intermediários (e.g., `add_to_cart`, `view_promotion`, `form_start`, `scroll_depth`) impede a identificação de gargalos no funil e a compreensão completa da intenção do usuário.
    *   **Como evitar**: Configure e monitore eventos de micro-conversão no GA4. Utilize "Explorações de Funil" para visualizar o fluxo entre esses eventos e identificar onde os usuários estão abandonando, permitindo otimizações mais precisas antes da conversão final.

---

## Dicas Avançadas

1.  **Integração GA4 com BigQuery para Análise SQL Avançada**: Para análises de mercado que exigem cruzamento de dados complexos ou modelagem preditiva, exporte seus dados brutos do GA4 para o Google BigQuery. Isso permite escrever queries SQL personalizadas para, por exemplo, calcular o LTV de forma mais sofisticada, criar modelos de propensão à compra ou segmentar usuários com base em padrões de comportamento não visíveis nos relatórios padrão do GA4.
    *   **Exemplo**: Use SQL para agrupar usuários por `user_pseudo_id`, calcular o tempo entre a primeira visita e a primeira compra, e correlacionar com a origem do tráfego para entender a velocidade da jornada de conversão por canal.
2.  **Utilização de Análise Preditiva e Audiências Preditivas no GA4**: Aproveite os recursos de machine learning do GA4 para identificar usuários com alta probabilidade de realizar uma compra ou de abandonar a plataforma. O GA4 pode criar automaticamente audiências preditivas (e.g., "Compradores potenciais de 7 dias", "Usuários com probabilidade de abandono") que podem ser usadas para campanhas de remarketing direcionadas ou para personalizar a experiência no site.
    *   **Exemplo**: Crie uma campanha no Google Ads visando apenas a audiência "Compradores potenciais de 7 dias" com ofertas especiais, aumentando a eficiência do investimento em mídia paga.
3.  **Implementação de User-ID para Mapeamento da Jornada Cross-Device**: Para ter uma visão unificada do usuário através de diferentes dispositivos e sessões (e.g., mobile, desktop, aplicativo), implemente o `User-ID` no GA4. Ao atribuir um ID persistente e não pessoalmente identificável a usuários logados, você pode reconstruir a jornada completa do cliente, independentemente do dispositivo utilizado.
    *   **Exemplo**: Analise uma "Exploração de Caminho" para um `User-ID` específico e veja que o usuário pesquisou no mobile, adicionou ao carrinho no desktop e finalizou a compra no aplicativo, revelando a complexidade da jornada.
4.  **Criação de Métricas Personalizadas para KPIS de Mercado Específicos**: Se as métricas padrão do GA4 não atendem completamente às suas necessidades de pesquisa de mercado, crie métricas personalizadas com base em eventos. Por exemplo, uma métrica para "Visualizações de Detalhes de SKU por Categoria" ou "Média de Interações com Conteúdo Educacional".
    *   **Exemplo**: Defina uma métrica de evento `engagement_score` para cada `page_view` que considera o `tempo_na_pagina` e `scroll_depth`, permitindo segmentar usuários com alto engajamento em conteúdo específico e otimizar estratégias de conteúdo para eles.
5.  **Análise de Cohorte para Avaliar o Impacto de Mudanças de Produto/Estratégia**: Use a exploração de coorte para isolar o impacto de lançamentos de produtos, mudanças de UI/UX ou campanhas de marketing em grupos específicos de usuários ao longo do tempo. Defina a coorte com base na data da primeira interação após o lançamento ou mudança.
    *   **Exemplo**: Após o lançamento de uma nova funcionalidade no dia 15/03, crie uma coorte de usuários `Adquiridos em 15/03` e compare sua taxa de retenção nas semanas subsequentes com a coorte `Adquiridos em 08/03` para quantificar o impacto da funcionalidade.