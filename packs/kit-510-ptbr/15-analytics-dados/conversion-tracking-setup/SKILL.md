---
name: conversion-tracking-setup
description: "Conversion Tracking Setup — Skill especializada para configurar e otimizar o rastreamento de conversões no Google Analytics 4, garantindo dados precisos para análise de desempenho e atribuição."
license: MIT
metadata:
  version: 1.0.0
  author: Cafe Code AI
  category: 15-analytics-dados
  updated: 2026-03-01
risk: safe
---

# Conversion Tracking Setup

Esta skill capacita o Claude a configurar, validar e otimizar o rastreamento de conversões em plataformas como Google Analytics 4, garantindo dados precisos para análise de desempenho de marketing e atribuição.

---

## Keywords

GA4 Conversão, Eventos Personalizados, Google Tag Manager Setup, Enhanced Ecommerce GA4, Modelagem de Atribuição, Validação de Conversão, DebugView GA4, Consent Mode, Measurement Protocol GA4, Data Layer E-commerce, Meta de Venda Online, CPA Tracking, ROAS Otimização, Relatórios de Conversão, Parâmetros de Evento.

---

## Quick Start

1.  **Integrar GTM ao site**: Incluir os snippets de código do Google Tag Manager imediatamente após a tag `<head>` e a tag `<body>` no código HTML do seu site.
2.  **Configurar Tag GA4 no GTM**: Criar uma tag do tipo "Google Analytics: Configuração do GA4" no GTM, inserindo o ID da sua propriedade GA4 (ex: `G-XXXXXXXXX`) e definindo-a para disparar em "Todas as Páginas".
3.  **Identificar Evento Chave**: Determinar qual ação do usuário representa uma conversão (ex: `purchase` para compra, `generate_lead` para preenchimento de formulário, `sign_up` para cadastro).
4.  **Configurar Evento de Conversão no GTM**: Criar uma nova "Tag de Evento do GA4" no GTM para o evento identificado, associando-a à Tag de Configuração GA4 e definindo um gatilho específico para a ação de conversão.
5.  **Marcar como Conversão no GA4**: Acessar a interface do Google Analytics 4, navegar em "Administrador" > "Eventos" e marcar o evento configurado como uma conversão.
6.  **Validar com DebugView**: Usar a ferramenta DebugView do GA4 para monitorar o disparo do evento de conversão em tempo real e verificar se todos os parâmetros esperados estão sendo enviados corretamente.

---

## Core Workflows

### Workflow 1: Configuração de Conversão de E-commerce para GA4 via GTM

Este workflow detalha a implementação do rastreamento de compras completas em um e-commerce, utilizando o Data Layer, Google Tag Manager e Google Analytics 4.

1.  **Implementação do Data Layer de E-commerce**: O desenvolvedor do site deve inserir um objeto `dataLayer.push` na página de confirmação de compra, contendo todos os detalhes da transação e dos itens comprados, seguindo o esquema Enhanced Ecommerce do GA4. Este `dataLayer.push` deve ser executado *antes* que o GTM seja inicializado.
    *   **Exemplo de `dataLayer.push` (página de confirmação de compra):**
        ```javascript
        window.dataLayer = window.dataLayer || [];
        dataLayer.push({
          event: "purchase",
          ecommerce: {
            transaction_id: "ORDEM-2023-XYZ789",
            value: 129.90,
            currency: "BRL",
            tax: 15.50,
            shipping: 12.00,
            coupon: "DESCONTO10",
            items: [
              {
                item_id: "PROD-ABC",
                item_name: "Tênis Esportivo X",
                affiliation: "Loja Principal",
                coupon: "FRETEGRATIS",
                currency: "BRL",
                discount: 10.00,
                item_brand: "Marca A",
                item_category: "Calçados",
                item_variant: "Azul Marinho P",
                price: 89.90,
                quantity: 1
              },
              {
                item_id: "PROD-DEF",
                item_name: "Meia Compressão",
                affiliation: "Loja Principal",
                currency: "BRL",
                price: 30.00,
                quantity: 1
              }
            ]
          }
        });
        ```
2.  **Criação de Variáveis de Data Layer no GTM**: No Google Tag Manager, criar variáveis do tipo "Variável da Camada de Dados" para cada dado relevante do objeto `ecommerce` que será enviado ao GA4.
    *   **Exemplos de Variáveis GTM:**
        *   `dlv - transaction_id`: `ecommerce.transaction_id`
        *   `dlv - value`: `ecommerce.value`
        *   `dlv - currency`: `ecommerce.currency`
        *   `dlv - items`: `ecommerce.items`
3.  **Configuração da Tag de Evento GA4 `purchase` no GTM**: Criar uma nova tag no GTM com as seguintes configurações:
    *   **Tipo de Tag**: "Google Analytics: Evento do GA4"
    *   **Tag de Configuração**: Selecionar a tag de configuração GA4 previamente criada (ex: `GA4 - Configuração Base`)
    *   **Nome do Evento**: `purchase` (deve corresponder ao `event` no `dataLayer.push`)
    *   **Parâmetros do Evento**: Adicionar os parâmetros de e-commerce mapeando para as variáveis de Data Layer criadas.
        *   `transaction_id`: `{{dlv - transaction_id}}`
        *   `value`: `{{dlv - value}}`
        *   `currency`: `{{dlv - currency}}`
        *   `items`: `{{dlv - items}}`
4.  **Definição do Gatilho para a Tag `purchase`**: Criar um gatilho do tipo "Evento Personalizado" no GTM com o nome `purchase`. Este gatilho disparará a tag de evento GA4 sempre que o `dataLayer.push` com `event: "purchase"` for executado.
5.  **Publicação do Container GTM**: Publicar as alterações no Google Tag Manager.
6.  **Marcação do Evento como Conversão no GA4**: Na interface do GA4, ir em "Administrador" > "Eventos" e ativar a opção "Marcar como conversão" para o evento `purchase`.
7.  **Validação de Dados**: Utilizar o DebugView do GA4 para simular uma compra e verificar se o evento `purchase` está sendo recebido com todos os parâmetros corretos. Analisar os relatórios de "Monetização" > "Compras de e-commerce" no GA4 para confirmar a coleta de dados agregados.

### Workflow 2: Rastreamento de Leads (Envio de Formulário) no GA4

Este workflow aborda a configuração de rastreamento de conversão para envios de formulários de contato, orçamentos ou newsletter, sem a necessidade de um `dataLayer.push` customizado, usando recursos nativos do GTM.

1.  **Identificação do Evento de Envio de Formulário**: Determinar a forma mais confiável de identificar o sucesso do envio de um formulário. Pode ser:
    *   Um redirecionamento para uma página de "obrigado" (ex: `/obrigado-contato`).
    *   Um evento DOM (ex: `form submission`) que o GTM pode capturar.
    *   Um elemento de sucesso que aparece na página após o envio (ex: `div` com classe `.sucesso-contato`).
2.  **Criação do Gatilho de Envio de Formulário no GTM**:
    *   **Cenário A: Redirecionamento para Página de Obrigado**: Criar um gatilho do tipo "Visualização de Página" com a condição "Page Path" `contém` `/obrigado-contato`.
    *   **Cenário B: Envio de Formulário GTM (se o formulário for padrão HTML)**: Criar um gatilho do tipo "Envio de Formulário". Configurar "Verificar Validação" e adicionar condições específicas para o formulário (ex: "Page Path" `contém` `/contato` e "Form ID" `igual a` `form-contato-principal`).
    *   **Cenário C: Clique em Botão de Envio com Sucesso**: Criar um gatilho do tipo "Clique - Apenas Links" ou "Clique - Todos os Elementos" com condições específicas do botão (ex: "Click ID" `igual a` `btn-enviar-contato`) e, se necessário, combinar com uma "Visualização de Elemento" para o aviso de sucesso.
3.  **Configuração da Tag de Evento GA4 `generate_lead` no GTM**: Criar uma nova tag no GTM:
    *   **Tipo de Tag**: "Google Analytics: Evento do GA4"
    *   **Tag de Configuração**: Selecionar a tag de configuração GA4 (ex: `GA4 - Configuração Base`)
    *   **Nome do Evento**: `generate_lead` (nome padrão do GA4 para leads)
    *   **Parâmetros do Evento (Opcional, mas recomendado)**: Adicionar parâmetros para contextualizar o lead.
        *   `form_name`: `{{Page Path}}` ou um valor fixo como `Formulário de Contato Principal`
        *   `lead_source`: `Website`
        *   `lead_value`: `0` (ou um valor estimado se aplicável)
4.  **Associação do Gatilho à Tag**: Ligar o gatilho criado no passo 2 à tag de evento `generate_lead`.
5.  **Publicação do Container GTM**: Publicar as alterações no Google Tag Manager.
6.  **Marcação do Evento como Conversão no GA4**: Na interface do GA4, ir em "Administrador" > "Eventos" e ativar a opção "Marcar como conversão" para o evento `generate_lead`.
7.  **Validação de Dados**: Simular o preenchimento e envio do formulário, utilizando o DebugView do GA4 para verificar o disparo do evento `generate_lead` com os parâmetros corretos. Acompanhar os relatórios de "Engajamento" > "Conversões" no GA4 para ver os dados agregados.

---

## Templates

### Data Layer de E-commerce para Evento `add_to_cart` (GA4)

```javascript
window.dataLayer = window.dataLayer || [];
dataLayer.push({
  event: "add_to_cart",
  ecommerce: {
    items: [
      {
        item_id: "PROD-ABC-001",
        item_name: "Camiseta Dry Fit",
        currency: "BRL",
        price: 79.90,
        quantity: 1,
        item_brand: "FitnessWear",
        item_category: "Vestuário",
        item_variant: "Tamanho M, Cor Azul"
      }
    ]
  }
});
```

### Configuração de Tag de Evento GA4 (download_material) no GTM

```
Tipo de Tag: Google Analytics: Evento do GA4
Tag de Configuração: GA4 - Configuração Base (ID da sua propriedade G-XXXXXXXXX)
Nome do Evento: download_material
Parâmetros do Evento:
  - Nome: material_name, Valor: {{Click Text}}
  - Nome: material_category, Valor: Ebook Marketing Digital
  - Nome: download_page, Valor: {{Page Path}}
Gatilho:
  - Tipo: Clique - Apenas Links
  - Condições:
    - Click URL contém .pdf
    - Page Path contém /materiais-ricos/
```

---

## Checklist

- [x] Google Tag Manager instalado corretamente e funcionando no site.
- [x] Tag de Configuração GA4 criada no GTM com o ID da propriedade `G-`.
- [x] Eventos chave de conversão identificados e documentados (e.g., `purchase`, `generate_lead`, `sign_up`).
- [x] Data Layer implementado para eventos de e-commerce ou leads complexos, seguindo o esquema GA4.
- [x] Variáveis de Data Layer configuradas no GTM para extrair os dados necessários.
- [x] Tags de Evento GA4 criadas no GTM para cada conversão, com nomes e parâmetros corretos.
- [x] Gatilhos de GTM configurados especificamente para cada evento de conversão (e.g., Evento Personalizado, Envio de Formulário, Visualização de Página).
- [x] Eventos marcados como conversão na interface do Google Analytics 4.
- [x] Teste de ponta a ponta de cada conversão simulando a jornada do usuário e validando com DebugView do GA4.
- [x] Validação de dados de conversão nos relatórios do GA4 (Tempo Real, Conversões, Monetização).
- [x] Implementação do Consent Mode no GTM para conformidade com privacidade (se aplicável).
- [x] Documentação interna do setup de rastreamento de conversões (nomes de eventos, parâmetros, gatilhos).
- [x] Revisão da atribuição padrão do GA4 e avaliação de modelos alternativos para relatórios.
- [x] Configuração de exclusão de IP interno para evitar dados de teste nos relatórios.

---

## Métricas de Referência

| Métrica                         | Benchmark (E-commerce) | Benchmark (Lead Gen) | Meta Exemplo (E-commerce) | Meta Exemplo (Lead Gen) |
| :------------------------------ | :--------------------- | :------------------- | :------------------------ | :---------------------- |
| **Taxa de Conversão**           | 1.5% - 3.0%            | 5.0% - 12.0%         | 2.5%                      | 8.0%                    |
| **Receita por Usuário (RPU)**   | R$ 15.00 - R$ 60.00    | N/A                  | R$ 35.00                  | N/A                     |
| **Valor Médio do Pedido (AOV)** | R$ 100.00 - R$ 400.00  | N/A                  | R$ 250.00                 | N/A                     |
| **Custo por Aquisição (CPA)**   | R$ 20.00 - R$ 150.00   | R$ 50.00 - R$ 500.00 | R$ 80.00                  | R$ 200.00               |
| **Retorno sobre Anúncios (ROAS)** | 2.5x - 4.5x            | N/A                  | 3.5x                      | N/A                     |
| **Taxa de Conclusão de Funil**  | 10% - 25% (para cada etapa) | 15% - 30%            | 20%                       | 25%                     |

---

## Erros Comuns

1.  **Eventos de Conversão Duplicados**: Ocorre quando o mesmo evento é disparado por múltiplos métodos (ex: tag GA4 global e GTM para o mesmo evento `page_view`).
    *   **Como evitar**: Garantir que a tag de configuração GA4 no GTM é a única fonte primária de eventos base. Se um evento é configurado via GTM (ex: `purchase`), desabilitar qualquer rastreamento duplicado que a implementação global do GA4 possa tentar fazer automaticamente ou garantir que os gatilhos GTM são exclusivos. Usar o DebugView para identificar a origem duplicada.
2.  **Parâmetros de E-commerce Ausentes ou Incorretos no Data Layer**: `value`, `currency`, `items` ou `transaction_id` não são preenchidos ou estão com formato inválido (`string` ao invés de `number`).
    *   **Como evitar**: Seguir rigorosamente a documentação do esquema de e-commerce do GA4. Utilizar o `gtag.js` ou o GTM Data Layer Helper para validar a estrutura do `dataLayer.push`. Testar com o Console do Navegador (`dataLayer`) e o DebugView do GA4 para verificar os parâmetros enviados.
3.  **Conversões Não Aparecem no GA4 Após Configuração**: O evento está disparando no GTM, mas não é registrado como conversão no GA4.
    *   **Como evitar**: Verificar se o evento foi explicitamente marcado como conversão na interface do GA4 em "Administrador" > "Eventos". Confirmar se não há filtros de dados (filtros de IP, exclusão de bots) no GA4 que possam estar bloqueando os dados. Verificar se o nome do evento no GTM corresponde *exatamente* ao nome marcado no GA4 (case-sensitive).
4.  **Atribuição Incorreta devido a Modelos Padrão**: As campanhas de marketing podem não receber o crédito correto se o modelo de atribuição padrão (Last Click) do GA4 não se alinha à estratégia de marketing.
    *   **Como evitar**: Entender os modelos de atribuição disponíveis no GA4 (Data-Driven, Last Click, First Click, Linear, etc.). Analisar o relatório "Caminhos de Conversão" para visualizar como diferentes canais contribuem. Considerar usar o modelo "Data-Driven" se houver volume de dados suficiente para uma atribuição mais justa e granular.

---

## Dicas Avançadas

1.  **Implementação de User-ID para Jornadas Cross-Device**: Após um usuário fazer login no seu site, enviar um `user_id` persistente e não pessoalmente identificável para o GA4. Isso permite unificar a jornada do usuário através de diferentes dispositivos e sessões, proporcionando uma visão mais precisa do comportamento e da atribuição.
    *   **Exemplo**: `gtag('set', {'user_id': ' hashed_user_id_123 '});` ou via GTM com uma tag de configuração GA4.
2.  **Utilização do Measurement Protocol para Eventos Offline**: Integrar eventos que ocorrem fora do site (ex: vendas fechadas via call center, atualizações de CRM, pagamentos offline) diretamente ao GA4 usando a Measurement Protocol API. Isso fecha o ciclo de atribuição e oferece uma visão 360º das conversões.
    *   **Exemplo de requisição HTTP POST para o Measurement Protocol**:
        ```
        POST /mp/collect?api_secret=<YOUR_API_SECRET>&firebase_app_id=<YOUR_APP_ID> HTTP/1.1
        Host: www.google-analytics.com
        Content-Type: application/json
        {
          "client_id": "GA1.1.12345.67890",
          "events": [
            {
              "name": "offline_sale",
              "params": {
                "transaction_id": "CRM-00123",
                "value": 500.00,
                "currency": "BRL",
                "customer_segment": "High Value"
              }
            }
          ]
        }
        ```
3.  **Configuração de Audiências Preditivas no GA4**: Aproveitar os recursos de machine learning do GA4 para criar audiências baseadas em comportamento futuro, como "Compradores prováveis em 7 dias" ou "Usuários com churn provável". Essas audiências podem ser exportadas para plataformas de anúncios (Google Ads) para campanhas de remarketing altamente segmentadas.
4.  **Exploração e Otimização com o Modelo de Atribuição Baseado em Dados (DDA)**: Em vez de confiar apenas nos modelos "last click", que ignoram o crédito de canais de descoberta, o DDA distribui o crédito da conversão entre todos os pontos de contato da jornada do cliente. Analisar os relatórios de "Caminhos de Conversão" e "Comparação de Modelos" no GA4 para entender o impacto do DDA e otimizar o investimento em mídia de acordo com a contribuição real.
5.  **Conectar GA4 ao BigQuery para Análise Avançada**: Exportar os dados brutos do GA4 para o Google BigQuery. Isso permite realizar consultas SQL complexas, unir dados de conversão com outras fontes (CRM, custo de mídia, dados de estoque), criar modelos de atribuição personalizados e construir dashboards altamente detalhados no Looker Studio.
    *   **Exemplo de consulta SQL para valor de conversão por canal no BigQuery**:
        ```sql
        SELECT
          traffic_source.source,
          SUM(CASE WHEN event_name = 'purchase' THEN (SELECT value.int_value FROM UNNEST(event_params) WHERE key = 'value') ELSE 0 END) AS total_revenue
        FROM
          `seu-projeto-gcp.analytics_XXXXXXXXX.events_*`
        WHERE
          _TABLE_SUFFIX BETWEEN FORMAT_DATE('%Y%m%d', DATE_SUB(CURRENT_DATE(), INTERVAL 30 DAY)) AND FORMAT_DATE('%Y%m%d', CURRENT_DATE())
          AND event_name = 'purchase'
        GROUP BY
          1
        ORDER BY
          total_revenue DESC;
        ```