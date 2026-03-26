---
name: customer-journey-analytics
description: "Customer Journey Analytics — Skill especializada para customer journey analytics"
license: MIT
metadata:
  version: 1.0.0
  author: Cafe Code AI
  category: 15-analytics-dados
  updated: 2026-03-01
risk: safe
---

# Customer Journey Analytics

Esta skill capacita o Claude a analisar, mapear e otimizar a jornada do cliente utilizando dados de comportamento e ferramentas como Google Analytics 4, identificando pontos de fricção e oportunidades de personalização.

---

## Keywords

Jornada do Cliente, Análise Comportamental, GA4 Exploration, Modelagem de Atribuição, Touchpoints Digitais, Eventos Personalizados GA4, Funis de Conversão, Cohorts Analysis, Lifetime Value (LTV), Customer Acquisition Cost (CAC), Visualização de Funil, Path Exploration, User ID GA4.

---

## Quick Start

1.  Verifique a coleta dos eventos automáticos `page_view`, `session_start` e `first_visit` no DebugView do GA4.
2.  Configure um relatório de "Exploração de Caminho" no GA4, iniciando com o evento `session_start` para visualizar os fluxos iniciais.
3.  Crie um segmento de usuários que completaram o evento `purchase` para analisar os caminhos pré-conversão no relatório de "Exploração de Caminho".
4.  Implemente o `user_id` no GA4 para unificar a jornada do cliente em diferentes dispositivos e sessões após o login.
5.  Configure os eventos `view_item`, `add_to_cart`, `begin_checkout` e `purchase` com parâmetros de e-commerce detalhados.

---

## Core Workflows

### Workflow 1: Análise de Funil de Conversão no GA4 para Otimização de Checkout

Este workflow foca em identificar e resolver gargalos no processo de compra, desde a visualização do produto até a finalização do pedido.

1.  **Validação de Eventos Essenciais de E-commerce:** Confirme que os eventos `view_item`, `add_to_cart`, `begin_checkout`, `add_shipping_info`, `add_payment_info` e `purchase` estão sendo coletados no GA4 com seus respectivos parâmetros (`item_id`, `item_name`, `value`, `currency`). Acesse o DebugView do GA4 ou o relatório "Tempo real" para monitorar a emissão desses eventos durante testes de usuário ou em produção. Por exemplo, garanta que o evento `purchase` contenha o `transaction_id` e o `value` total da compra.
2.  **Criação do Relatório de Funil Específico:** No GA4, navegue para "Explorar" > "Exploração de Funil". Selecione "Funil aberto" e adicione os passos na seguinte ordem: `view_item` (passo 1), `add_to_cart` (passo 2), `begin_checkout` (passo 3), `add_shipping_info` (passo 4), `add_payment_info` (passo 5), `purchase` (passo 6). Aplique um filtro para `device = mobile` para analisar o desempenho do funil em dispositivos móveis. Observe a taxa de abandono entre `begin_checkout` e `add_payment_info`.
3.  **Segmentação de Abandono de Carrinho:** Crie um segmento de usuários no GA4 que iniciaram o evento `begin_checkout` mas não registraram o evento `purchase` dentro de um período de 60 minutos. Exporte este segmento para o Google Ads para campanhas de retargeting ou para o seu CRM para acionar e-mails de recuperação de carrinho, oferecendo um cupom de 10% de desconto ou frete grátis.
4.  **Análise de Atribuição e Caminhos de Conversão:** No GA4, acesse "Publicidade" > "Atribuição" > "Caminhos de Conversão". Selecione o evento `purchase` como conversão. Analise os canais que mais contribuíram nos primeiros e últimos touchpoints. Se `organic_search` ou `paid_social` frequentemente iniciam a jornada, enquanto `email` ou `direct` a finalizam, isso indica a necessidade de estratégias de topo de funil para descoberta e estratégias de fundo de funil para conversão via e-mail.
5.  **Exemplo Concreto:** Um e-commerce de roupas de cama identifica que 55% dos usuários abandonam entre `add_shipping_info` e `add_payment_info` em dispositivos móveis. Uma investigação mais aprofundada revela que o formulário de endereço é longo e não possui auto-preenchimento. A equipe de UX/UI é acionada para simplificar o formulário e implementar auto-complete, resultando em uma redução de 18% na taxa de abandono desse passo no mês seguinte.

### Workflow 2: Mapeamento da Jornada Pós-Compra e Análise de LTV no GA4

Este workflow visa entender o comportamento do cliente após a compra, otimizando a retenção e o Lifetime Value (LTV).

1.  **Configuração de Eventos Pós-Compra e Engajamento:** Garanta a coleta de eventos personalizados como `product_review_submit` (quando um cliente envia uma avaliação de produto), `newsletter_signup` (após a compra), `customer_service_contact` (quando um cliente entra em contato com o suporte), e `loyalty_program_enroll` (se houver um programa de fidelidade). Estes eventos fornecem insights valiosos sobre o engajamento pós-conversão.
2.  **Análise de LTV por Cohort de Aquisição:** No GA4, acesse "Explorar" > "Exploração de Cohort". Defina a "Inclusão de cohort" por "Data da aquisição" e a "Granularidade" por "Semana". Selecione "Receita total" como métrica. Compare o LTV de cohorts adquiridos por `paid_search` versus `referral` ao longo de 90 dias. Por exemplo, cohorts de `paid_search` podem ter um LTV médio de R$ 300 após 60 dias, enquanto cohorts de `referral` podem atingir R$ 450, indicando que clientes referidos são mais valiosos a longo prazo.
3.  **Mapeamento de Caminho Pós-Compra:** Utilize "Exploração de Caminho" no GA4. Defina o ponto de partida como o evento `purchase` e analise os 3-5 eventos seguintes mais comuns. Se a maioria dos clientes que compram um produto A em seguida visualiza produtos complementares B e C, isso indica uma oportunidade para automação de e-mail marketing com sugestões de cross-sell. Se muitos clientes que compram um produto complexo como um software, em seguida, registram o evento `customer_service_contact` ou `help_center_visit`, pode haver um problema de onboarding que precisa ser abordado.
4.  **Criação de Segmentos de Clientes Fiéis e em Risco:** Crie segmentos no GA4 de usuários que realizaram `purchase` mais de uma vez (`repeat_customer`) ou que interagiram com 3+ eventos pós-compra (ex: `product_review_submit`, `newsletter_signup`). Paralelamente, crie um segmento de "usuários em risco" que não registraram nenhum evento de engajamento nos últimos 30 dias após uma compra. Exporte estes segmentos para campanhas de retenção personalizadas (ofertas exclusivas para fiéis, reengajamento para em risco).
5.  **Exemplo Concreto:** Uma empresa de assinatura de cosméticos descobre, via "Exploração de Caminho" pós-assinatura, que 60% dos novos assinantes que completam o evento `profile_preferences_set` (definição de preferências de produtos) também interagem com o conteúdo `blog_post_view` sobre "rotinas de beleza". Aqueles que não definem as preferências têm uma taxa de churn 15% maior no primeiro mês. Isso sugere que a definição de preferências é um passo crucial para engajamento e retenção, e a equipe de produto deve incentivar ativamente sua conclusão, talvez com um lembrete via e-mail após 24h da assinatura.

---

## Templates

### Template de Configuração de Evento Personalizado GA4 para Interação com Botão Específico

```javascript
// Exemplo de implementação para gtag.js para um botão de "Solicitar Demonstração"
gtag('event', 'lead_form_interaction', {
  event_category: 'Lead Generation',
  event_label: 'Botão: Solicitar Demonstração',
  value: 0, // Não há valor monetário direto, mas pode ser ponderado
  form_name: 'demonstration_request_form',
  page_path: window.location.pathname
});

// Exemplo para um clique em um banner de promoção
gtag('event', 'banner_click', {
  event_category: 'Promoção',
  event_label: 'Banner: Black Friday - 50% OFF',
  promo_id: 'promo_bf_50off',
  creative_name: 'hero_banner_blackfriday',
  page_path: window.location.pathname
});
```

### Template de Relatório Personalizado GA4 para Análise de Etapas de Jornada de Conteúdo

```
// No painel de "Explorar" do GA4
// Tipo de Exploração: Funil
// Nome do Funil: Jornada de Conteúdo para Assinatura de Newsletter
// Técnicas:
//   Passos do Funil:
//     1. page_view (Nome do evento: 'Visita à Página Principal do Blog')
//        Condição: event_name = 'page_view' E page_path contém '/blog/'
//     2. page_view (Nome do evento: 'Leitura de Artigo Profundo')
//        Condição: event_name = 'page_view' E page_path contém '/blog/guia-avancado-marketing-digital/'
//     3. scroll_depth (Nome do evento: 'Rolagem 75% Artigo')
//        Condição: event_name = 'scroll_depth' E percent_scrolled = 75 E page_path contém '/blog/guia-avancado-marketing-digital/'
//     4. newsletter_signup_form_view (Nome do evento: 'Visualização Formulário Newsletter')
//        Condição: event_name = 'newsletter_signup_form_view'
//     5. generate_lead (Nome do evento: 'Assinatura Newsletter Concluída')
//        Condição: event_name = 'generate_lead' E form_name = 'newsletter_popup'
// Segmentos:
//   - Usuários Referidos: session_source_medium = 'google / cpc' OU 'facebook / social'
//   - Usuários Orgânicos: session_source_medium = 'google / organic'
// Dimensões:
//   - Fonte / Mídia da sessão
//   - Categoria do Dispositivo
// Métricas:
//   - Usuários ativos
//   - Taxa de conversão do funil
//   - Visualizações
//   - Tempo médio de engajamento
```

---

## Checklist

- [x] Eventos essenciais de funil (ex: `view_item`, `add_to_cart`, `purchase`) configurados no GA4 com parâmetros corretos.
- [x] Implementação do `user_id` para identificação unificada de usuários cross-device e para análises de LTV.
- [x] Criação de Explorations de Funil no GA4 para mapear as principais jornadas de conversão (e-commerce, geração de leads, etc.).
- [x] Configuração de eventos personalizados para touchpoints não-padrão (ex: cliques em banners específicos, interações com chat, erros de formulário).
- [x] Análise de "Exploração de Caminho" no GA4 para identificar fluxos de navegação incomuns ou otimizáveis antes e depois da conversão.
- [x] Revisão e aplicação de modelos de atribuição (ex: Posição, Data-driven) para diferentes tipos de conversão e eventos.
- [x] Segmentação de usuários no GA4 baseada em comportamento (ex: "abandonadores de carrinho", "compradores recorrentes", "usuários engajados").
- [x] Integração de dados GA4 com CRM (via Measurement Protocol ou exportação) para enriquecer a visão do cliente e o cálculo de LTV.
- [x] Criação de um dashboard no Looker Studio (antigo Google Data Studio) para visualização consolidada da jornada do cliente.
- [x] Implementação de testes A/B em etapas críticas da jornada, baseando-se em insights de abandono de funil.

---

## Métricas de Referência

| Métrica                                | Benchmark (E-commerce B2C) | Meta (E-commerce B2C) |
|----------------------------------------|-----------------------------|-----------------------|
| Taxa de Conversão (Checkout para Purchase) | 2.5% - 4%                   | 4.5% - 6%             |
| Taxa de Abandono de Carrinho           | 65% - 78%                   | < 60%                 |
| Taxa de Clientes Recorrentes (90 dias) | 12% - 18%                   | > 25%                 |
| LTV (6 meses)                          | R$ 300 - R$ 700             | R$ 800+               |
| Tempo Médio até a 1ª Compra            | 4 - 8 dias                  | < 4 dias              |
| Taxa de Retenção (Mês 1)               | 25% - 35%                   | > 40%                 |

---

## Erros Comuns

1.  **Coleta inconsistente de eventos GA4**: Não garantir que todos os passos críticos da jornada (ex: `add_to_cart`, `begin_checkout`, `purchase`) estão sendo registrados com os parâmetros corretos (`value`, `currency`, `item_id`). Isso leva a funis de conversão incompletos e dados de receita incorretos. **Como evitar**: Implementar uma camada de dados (`dataLayer`) robusta e realizar auditorias regulares com o DebugView do GA4 e relatórios de tempo real para validar a emissão e estrutura dos eventos. Utilize a documentação oficial do GA4 para eventos de e-commerce.
2.  **Ignorar a modelagem de atribuição**: Usar apenas o modelo de "Último Clique" para todas as análises de jornada, subestimando a importância de canais de descoberta (ex: orgânico, social) e de engajamento intermediário. Isso pode levar a decisões de investimento de marketing equivocadas. **Como evitar**: No GA4, explore os relatórios de "Atribuição" > "Caminhos de Conversão" e "Comparação de Modelos". Analise como diferentes modelos (ex: Posição, Linear, Data-driven) redistribuem o crédito de conversão e use essas informações para otimizar o mix de marketing, valorizando os canais iniciais e intermediários que contribuem para a jornada.
3.  **Não unificar a jornada do usuário**: Falha em implementar o `user_id` no GA4, resultando em múltiplas sessões e usuários para a mesma pessoa em diferentes dispositivos ou navegadores. Isso impede uma visão holística do comportamento do cliente e distorce análises de LTV e cohort. **Como evitar**: Trabalhar com a equipe de desenvolvimento para implementar o `user_id` assim que o usuário faz login ou se identifica em qualquer ponto da jornada. Certifique-se de que o `user_id` seja consistente em todas as interações e dispositivos, permitindo que o GA4 costure a jornada completa daquele indivíduo.

---

## Dicas Avançadas

1.  **Cross-device stitching com `user_id` para precisão do LTV**: Para obter a visão mais precisa da jornada do cliente e do LTV, a implementação do `user_id` no GA4 é indispensável. Ao invés de confiar apenas em `device_id` (que pode criar usuários duplicados para a mesma pessoa em diferentes dispositivos), o `user_id` permite unificar todas as sessões e eventos de um mesmo usuário em smartphones, tablets e desktops. Exemplo: um usuário que pesquisa um produto no celular via `organic_search`, adiciona ao carrinho no desktop via `direct` e finaliza a compra no tablet via `email_marketing` terá sua jornada corretamente atribuída a um único usuário, revelando a complexidade real dos touchpoints e o verdadeiro LTV.
2.  **Análise de micro-momentos com eventos personalizados e parâmetros enriquecidos**: Não se limite aos eventos padrão do GA4. Crie eventos personalizados para micro-interações que sinalizam intenção ou fricção. Exemplo: `scroll_depth` (com parâmetro `percent_scrolled`), `video_play_complete` (com `video_title`), `form_field_error` (com `field_name` e `error_message`), `chat_widget_open`. Monitorar `form_field_error` com `field_name = 'cpf'` após o `begin_checkout` pode indicar um problema específico de validação de CPF que está causando abandono.
3.  **Utilização de Audiências Preditivas do GA4 para marketing proativo**: Aproveite as audiências preditivas do GA4 (ex: "Usuários com probabilidade de compra", "Usuários com probabilidade de abandono", "Usuários com probabilidade de churn") para segmentar proativamente seus esforços de marketing. Exemplo: Crie uma campanha de e-mail marketing com um incentivo de desconto ou um conteúdo de valor para a audiência "Usuários com probabilidade de abandono (próximos 7 dias)" antes que eles realmente deixem de interagir com sua marca, aumentando as chances de retenção.
4.  **Integração bidirecional com CRM para enriched LTV e personalização**: Conecte o GA4 com seu sistema de CRM para trazer dados offline e de valor do cliente para suas análises. Use o `user_id` como chave para enviar dados de compras recorrentes, interações com suporte, status de fidelidade e até o NPS do CRM de volta ao GA4 via Measurement Protocol ou importação de dados. Isso permite segmentar e analisar o LTV de forma muito mais precisa, considerando todo o ciclo de vida do cliente e criando audiências para personalização baseadas em dados unificados.
5.