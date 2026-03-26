---
name: email-analytics
description: "Email Analytics — Skill especializada para configurar, analisar e otimizar campanhas de email marketing usando dados do Google Analytics 4 e outras ferramentas."
license: MIT
metadata:
  version: 1.0.0
  author: Cafe Code AI
  category: 15-analytics-dados
  updated: 2026-03-01
risk: safe
---

# Email Analytics

Essa skill capacita o Claude a configurar, analisar e otimizar campanhas de email marketing usando dados do Google Analytics 4 e outras ferramentas, focando em atribuição e comportamento do usuário.

---

## Keywords

GA4, UTM, Taxa de Abertura, CTR Email, Conversão de Email, Atribuição Multicanal, LTV Email, Segmentação de Audiência, Funil de Email, ROI Email, Jornada do Cliente, Engajamento de Email.

---

## Quick Start

1.  **Configurar Parâmetros UTM em Todas as URLs de Email**: Garanta que cada link em seus emails contenha `utm_source=email`, `utm_medium=email_marketing` (ou outro específico como `newsletter`, `promocional`), e `utm_campaign` (nome da campanha).
2.  **Criar Relatório Personalizado de Origem/Mídia no GA4**: Navegue até "Relatórios > Biblioteca > Criar novo relatório > Relatório detalhado". Adicione as dimensões "Origem", "Mídia" e "Campanha" e métricas como "Sessões", "Usuários", "Taxa de Engajamento", "Conversões" e "Receita Total".
3.  **Filtrar Tráfego de Email no GA4**: No relatório personalizado, aplique um filtro para `Mídia` "contém" `email` para isolar o tráfego de email e iniciar a análise.
4.  **Conferir Taxas de Abertura e Cliques (Open Rate/CTR) na Plataforma de Email**: Acesse as métricas primárias da sua ferramenta de envio de email (Mailchimp, RD Station, ActiveCampaign) para ter uma visão inicial do desempenho antes de mergulhar no GA4.

---

## Core Workflows

### Workflow 1: Análise Detalhada de Performance de Campanhas de Email no GA4

Este workflow foca em como extrair insights profundos da performance de campanhas de email, correlacionando métricas de engajamento do email com o comportamento do usuário e conversões no site, utilizando o Google Analytics 4.

1.  **Verificação e Padronização de UTMs:**
    *   **Passo:** Antes de qualquer análise, confirme que todas as campanhas de email estão usando uma estrutura consistente de parâmetros UTM.
    *   **Exemplo:** Para uma campanha de Black Friday, use `utm_source=email_marketing`, `utm_medium=newsletter_promocional`, `utm_campaign=black_friday_2024_ofertas`, `utm_content=banner_principal` ou `utm_term=desconto_especial`. A consistência é vital para a agregação de dados no GA4.
2.  **Criação de Exploração de Funil para Email no GA4:**
    *   **Passo:** No GA4, vá para "Explorar > Galeria de Modelos > Exploração de funil". Crie um funil que comece com um evento de "page_view" ou "session_start" com a dimensão `Mídia` igual a `email_marketing` (ou o valor usado no `utm_medium`).
    *   **Exemplo:**
        *   **Etapa 1:** Sessão Iniciada por Email (`Mídia` = `email_marketing`)
        *   **Etapa 2:** Visualização da Página do Produto (`event_name` = `page_view`, `page_location` contém `/produto/`)
        *   **Etapa 3:** Adição ao Carrinho (`event_name` = `add_to_cart`)
        *   **Etapa 4:** Compra Concluída (`event_name` = `purchase`)
    *   **Objetivo:** Identificar gargalos na jornada do usuário que veio de email, como alta taxa de abandono na página do produto, indicando desalinhamento entre a oferta do email e a landing page.
3.  **Segmentação de Audiência por Engajamento de Email:**
    *   **Passo:** No GA4, crie segmentos de público com base em eventos específicos ou propriedades de usuário relacionados ao email.
    *   **Exemplo:**
        *   **Segmento "Compradores via Email Recentes":** Usuários com `Mídia` = `email_marketing` E `event_name` = `purchase` nos últimos 30 dias.
        *   **Segmento "Visitantes de Email Não-Conversores":** Usuários com `Mídia` = `email_marketing` E `event_name` != `purchase` nas últimas 7 dias.
    *   **Aplicação:** Use esses segmentos em relatórios de "Visão geral da aquisição" ou "Comportamento" para comparar métricas como LTV, taxa de retenção e eventos subsequentes entre grupos de usuários que interagiram com emails de maneiras diferentes.
4.  **Análise de Desempenho por Campanha/Assunto:**
    *   **Passo:** Utilize o relatório personalizado criado no Quick Start ou uma exploração livre no GA4, adicionando as dimensões `Campanha` e `Conteúdo do Anúncio` (para `utm_content`).
    *   **Exemplo:** Compare a `Taxa de Conversão de Compras` para `utm_campaign=black_friday_2024_ofertas` vs. `utm_campaign=natal_2024_guia_presentes`. Dentro de `black_friday_2024_ofertas`, analise qual `utm_content` (ex: `banner_principal` vs. `link_texto_desconto`) gerou mais receita. Isso ajuda a refinar criativos e copys futuras.

### Workflow 2: Otimização de Atribuição Multicanal para Campanhas de Email

Este workflow detalha como o email contribui na jornada do cliente em conjunto com outros canais, utilizando modelos de atribuição e explorações avançadas no GA4 para otimizar o investimento e a estratégia de comunicação.

1.  **Configuração de Atribuição no GA4:**
    *   **Passo:** Entenda que o GA4 usa o modelo de atribuição "Baseado em dados" (Data-Driven Attribution - DDA) por padrão. Este modelo distribui o crédito da conversão entre todos os pontos de contato da jornada do cliente.
    *   **Exemplo:** Em "Administrador > Configurações de Atribuição", verifique se o DDA está ativo. Compreender o modelo padrão é crucial para interpretar os relatórios de atribuição.
2.  **Análise de Caminhos de Conversão:**
    *   **Passo:** No GA4, vá para "Explorar > Galeria de Modelos > Caminhos de conversão". Selecione "Origem/Mídia" ou "Campanha" como dimensão.
    *   **Exemplo:** Observe sequências como `(email_marketing -> busca_organica -> direct) para purchase` ou `(social -> email_marketing -> direct) para purchase`. O email pode aparecer no início, meio ou fim da jornada.
    *   **Objetivo:** Identificar se o email atua predominantemente como um canal de descoberta (primeiro toque), de nutrição (meio da jornada) ou de fechamento (último toque).
3.  **Comparação de Modelos de Atribuição para Email:**
    *   **Passo:** No GA4, vá para "Publicidade > Atribuição > Comparação de modelos". Selecione as dimensões "Origem/Mídia" ou "Campanha".
    *   **Exemplo:** Compare o modelo "Baseado em dados" com "Último clique" e "Primeiro clique" para a `Mídia` `email_marketing`.
        *   Se o "Primeiro clique" atribui significativamente mais conversões ao email do que o "Último clique", isso sugere que o email é eficaz em iniciar jornadas de compra.
        *   Se o "Último clique" atribui mais, o email é um forte fechador de vendas.
    *   **Insight Prático:** Se o email tem alto valor no "Primeiro Clique", considere estratégias para capturar mais leads via email no topo do funil. Se alto no "Último Clique", otimize as ofertas e CTAs dos emails de retargeting ou promoções finais.
4.  **Otimização de Campanhas de Email Baseada em Atribuição:**
    *   **Passo:** Use os insights dos caminhos de conversão e comparação de modelos para ajustar o conteúdo e o momento dos emails.
    *   **Exemplo:** Se o email frequentemente aparece como um segundo ou terceiro toque antes da conversão, crie sequências de nutrição mais robustas que complementem outros canais. Por exemplo, um email pós-engajamento em mídia social com um recurso aprofundado ou um guia. Se o email é um forte iniciador, concentre-se em ofertas de valor para novos inscritos.

---

## Templates

### Estrutura de Parâmetros UTM para Campanhas de Email

```
https://www.seusite.com.br/pagina-de-destino?utm_source=email_marketing&utm_medium=newsletter_semanal&utm_campaign=promocao_verao_2025&utm_content=banner_colecao_praia&utm_term=desconto_15_biquinis
```

### Relatório Semanal de Performance de Email no GA4 (Visão Geral)

```
**Relatório Semanal de Performance de Email - [Data Início] a [Data Fim]**

**Visão Geral:**
*   Sessões de Email: 12.540 (+15% vs. semana anterior)
*   Usuários de Email: 9.870 (+12% vs. semana anterior)
*   Taxa de Engajamento: 58.3% (Meta: >55%)
*   Receita Gerada via Email: R$ 32.150 (+22% vs. semana anterior)
*   Conversões (Compras): 420 (+18% vs. semana anterior)

**Campanhas de Destaque:**
*   **"Oferta Exclusiva Fim de Semana" (utm_campaign=oferta_fds):**
    *   Sessões: 3.100
    *   Receita: R$ 15.200 (ROI de 350% considerando custo de envio)
    *   Taxa de Conversão: 4.8%
*   **"Newsletter Conteúdo Novo" (utm_campaign=newsletter_conteudo):**
    *   Sessões: 5.800
    *   Receita: R$ 8.500 (Atribuição de primeiro toque forte)
    *   Taxa de Engajamento: 65%

**Recomendações:**
*   Replicar estrutura de oferta para campanhas futuras com base no desempenho da "Oferta Exclusiva".
*   Analisar caminhos de conversão para a "Newsletter Conteúdo Novo" para otimizar sequências de nutrição.
*   Testar A/B diferentes CTAs em emails de abandono de carrinho.
```

---

## Checklist

-   [x] Todas as campanhas de email com parâmetros UTM completos e consistentes (`source`, `medium`, `campaign`, `content`, `term`).
-   [x] Parâmetros UTM validados com a ferramenta de envio de email antes do disparo.
-   [x] Relatórios personalizados no GA4 configurados para monitorar tráfego de email (Origem/Mídia, Campanha).
-   [x] Segmentos de público no GA4 criados para usuários de email (compradores, engajados, abandonadores).
-   [x] Exploração de funil no GA4 para analisar a jornada do usuário que veio de email.
-   [x] Modelos de atribuição comparados no GA4 para entender o papel do email (primeiro, meio, último toque).
-   [x] Métricas de plataforma de email (Open Rate, CTR, Bounce Rate) correlacionadas com métricas do GA4 (Sessões, Conversões).
-   [x] Testes A/B (assunto, CTA, layout) planejados e executados com base em hipóteses de melhoria de performance.
-   [x] Análise de LTV (Lifetime Value) de clientes adquiridos via email versus outros canais.
-   [x] Configuração de exclusão de bots e tráfego interno no GA4 para garantir dados limpos.

---

## Métricas de Referência

| Métrica                      | Benchmark (E-commerce) | Meta (E-commerce) |
| :--------------------------- | :--------------------- | :---------------- |
| Taxa de Abertura (Open Rate) | 20-25%                 | >28%              |
| Taxa de Cliques (CTR)        | 2.5-3.5%               | >4%               |
| Taxa de Conversão (Email)    | 1.5-2.5%               | >3%               |
| Receita por Email