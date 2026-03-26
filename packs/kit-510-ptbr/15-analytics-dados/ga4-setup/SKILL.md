---
name: ga4-setup
description: "Ga4 Setup — Skill especializada para ga4 setup"
license: MIT
metadata:
  version: 1.0.0
  author: Cafe Code AI
  category: 15-analytics-dados
  updated: 2026-03-01
risk: safe
---

# Ga4 Setup

Esta skill capacita o Claude a configurar, validar e otimizar implementações do Google Analytics 4, cobrindo desde a instalação básica até eventos personalizados e relatórios avançados.

---

## Keywords

GA4, Google Analytics 4, Implementação GA4, Configuração de Eventos, Propriedades Personalizadas, Dimensões Personalizadas, Métricas Personalizadas, DebugView, GTM, Google Tag Manager, Consent Mode, Stream de Dados, Fluxo de Dados, Conversões GA4, Modelagem de Conversões, BigQuery GA4.

---

## Quick Start

1.  **Criar Propriedade GA4 e Stream de Dados:** Acesse o painel de administração do Google Analytics, crie uma nova propriedade GA4 e configure um stream de dados para a web, informando a URL do seu site (ex: `https://www.minhaloja.com.br`). Copie o ID de Medição (ex: `G-XXXXXXXXXX`).
2.  **Instalar Tag Base GA4 via GTM:** No Google Tag Manager, crie uma nova tag do tipo "Configuração do GA4". Insira o ID de Medição copiado e configure-a para disparar em "Todas as Páginas" (ou `Page View`).
3.  **Ativar Google Signals:** No Admin GA4, navegue até "Configurações de Dados" > "Coleta de Dados" e ative o Google Signals para habilitar recursos de remarketing, relatórios demográficos e modelagem de dados.
4.  **Validar Instalação com DebugView:** Publique seu contêiner GTM. No GA4, navegue até "Administrador" > "DebugView". No seu navegador, use a extensão "Google Analytics Debugger" ou adicione `?_gl=1` à URL do seu site para ver os eventos em tempo real no DebugView e confirmar que a tag base está disparando.

---

## Core Workflows

### Workflow 1: Configuração de Eventos Personalizados e Dimensões/Métricas Personalizadas para E-commerce

Este workflow detalha a implementação de um evento de "Adicionar ao Carrinho" com parâmetros específicos e como transformá-los em dimensões e métricas personalizadas no GA4 para relatórios.

**Cenário:** Rastrear cliques no botão "Adicionar ao Carrinho" em uma loja online, capturando o SKU do produto, nome do produto e o preço unitário.

**Passos Detalhados:**

1.  **Implementação da Camada de Dados (dataLayer) no Site:**
    *   O desenvolvedor do site deve garantir que, ao clicar no botão "Adicionar ao Carrinho", os dados do produto sejam enviados para o `dataLayer`.
    *   **Exemplo de Código (JavaScript no site):**
        ```javascript
        <button id="addToCartButton" onclick="
            dataLayer.push({
                'event': 'add_to_cart_custom',
                'ecommerce': {
                    'currency': 'BRL',
                    'items': [{
                        'item_id': 'SKU12345',
                        'item_name': 'Camisa Polo Premium',
                        'price': 89.90,
                        'quantity': 1
                    }]
                }
            });
        ">Adicionar ao Carrinho</button>
        ```
    *   Neste exemplo, o evento é `add_to_cart_custom`. Os parâmetros estão aninhados sob `ecommerce.items[0]`.

2.  **Configuração de Variáveis de Camada de Dados no GTM:**
    *   No GTM, crie as seguintes variáveis do tipo "Variável da Camada de Dados":
        *   `dl_item_id`: `ecommerce.items.0.item_id`
        *   `dl_item_name`: `ecommerce.items.0.item_name`
        *   `dl_price`: `ecommerce.items.0.price`
        *   `dl_currency`: `ecommerce.currency`
        *   `dl_quantity`: `ecommerce.items.0.quantity`

3.  **Criação da Tag de Evento GA4 no GTM:**
    *   Crie uma nova Tag no GTM do tipo "Evento do GA4".
    *   **Tag de Configuração:** Selecione a tag de configuração GA4 já existente (ex: `GA4 - Configuração Base`).
    *   **Nome do Evento:** Use `add_to_cart_custom` (exatamente como definido no `dataLayer`).
    *   **Parâmetros do Evento:** Adicione os seguintes parâmetros:
        *   `item_id`: `{{dl_item_id}}`
        *   `item_name`: `{{dl_item_name}}`
        *   `price`: `{{dl_price}}`
        *   `currency`: `{{dl_currency}}`
        *   `quantity`: `{{dl_quantity}}`
    *   **Acionamento:** Crie um novo acionador do tipo "Evento Personalizado" com o nome `add_to_cart_custom`.

4.  **Registro de Dimensões e Métricas Personalizadas no GA4:**
    *   No Admin do GA4, vá para "Configurações de Dados" > "Definições Personalizadas".
    *   **Crie Dimensões Personalizadas:**
        *   Clique em "Criar Dimensão Personalizada".
        *   **Nome da Dimensão:** `ID do Produto`
        *   **Escopo:** Evento
        *   **Nome do Parâmetro do Evento:** `item_id`
        *   Repita para `Nome do Produto` (`item_name`) e `Moeda` (`currency`).
    *   **Crie Métricas Personalizadas:**
        *   Clique em "Criar Métrica Personalizada".
        *   **Nome da Métrica:** `Preço Unitário`
        *   **Escopo:** Evento
        *   **Nome do Parâmetro do Evento:** `price`
        *   **Unidade de Medida:** Moeda (BRL)
        *   Repita para `Quantidade` (`quantity`), com Unidade de Medida "Padrão".

5.  **Validação e Publicação:**
    *   Use o "Modo de Depuração" do GTM para testar se a tag de evento dispara corretamente e se os parâmetros estão sendo enviados.
    *   Verifique o "DebugView" do GA4 para confirmar a chegada do evento `add_to_cart_custom` com todos os parâmetros.
    *   Publique o contêiner GTM. Após algumas horas, os dados começarão a aparecer nos relatórios do GA4, e as dimensões e métricas personalizadas estarão disponíveis em "Explorações".

### Workflow 2: Configuração de Conversões e Relatórios de Atribuição no GA4

Este workflow foca em como definir um evento como conversão e analisar seu desempenho usando os modelos de atribuição do GA4.

**Cenário:** Marcar o evento `purchase` (compra finalizada) como uma conversão e analisar os caminhos que levaram a essa conversão.

**Passos Detalhados:**

1.  **Verificar Evento `purchase` (ou outro evento de conversão):**
    *   O evento `purchase` geralmente é um evento recomendado pelo GA4 e, se implementado via `dataLayer` e GTM (seguindo a estrutura de e-commerce do GA4), já virá com parâmetros como `transaction_id`, `value`, `currency`, `items`.
    *   **Exemplo de `dataLayer` para `purchase`:**
        ```javascript
        dataLayer.push({
          'event': 'purchase',
          'ecommerce': {
            'transaction_id': 'T_12345',
            'value': 120.50,
            'currency': 'BRL',
            'tax': 10.00,
            'shipping': 5.00,
            'items': [{
              'item_id': 'SKU12345',
              'item_name': 'Camisa Polo Premium',
              'price': 89.90,
              'quantity': 1
            }, {
              'item_id': 'SKU67890',
              'item_name': 'Calça Jeans Confort',
              'price': 30.60,
              'quantity': 1
            }]
          }
        });
        ```
    *   Certifique-se de que este evento esteja sendo enviado corretamente ao GA4 (via Tag de Evento GA4 no GTM com nome `purchase` e parâmetros de e-commerce).

2.  **Marcar o Evento como Conversão no GA4:**
    *   No painel Admin do GA4, navegue até "Configurações de Dados" > "Eventos".
    *   Encontre o evento `purchase` na lista (ou o evento que você deseja marcar como conversão, ex: `form_submit`, `lead_generated`).
    *   Alterne a chave na coluna "Marcar como conversão" para ativá-lo.
    *   Se o evento não aparecer na lista (pode levar algumas horas após a primeira ocorrência), você pode criá-lo manualmente em "Configurações de Dados" > "Conversões" > "Novo evento de conversão" e inserir o nome exato do evento (ex: `purchase`).

3.  **Configuração do Modelo de Atribuição:**
    *   No Admin do GA4, vá para "Configurações da Atribuição".
    *   **Modelo de Atribuição para Relatórios (não relacionados a conversão):** Selecione o modelo padrão para a maioria dos relatórios (ex: "Baseado em dados" é o recomendado).
    *   **Janela de Lookback para Conversões de Aquisição:** Defina o período para eventos de "primeira interação" (ex: 30 dias para aquisição de usuários).
    *   **Janela de Lookback para Outros Eventos de Conversão:** Defina o período para eventos de "qualquer interação" (ex: 90 dias para conversões posteriores).
    *   **Exemplo:** Manter "Baseado em dados" como padrão, 30 dias para aquisição e 90 dias para outros eventos.

4.  **Análise de Relatórios de Atribuição:**
    *   Após algumas horas/dias de coleta de dados, navegue até "Publicidade" no menu lateral esquerdo.
    *   **Relatório "Caminhos da Conversão":**
        *   Selecione o evento de conversão `purchase`.
        *   Analise os caminhos que os usuários percorrem antes da compra, identificando sequências de canais (ex: busca orgânica -> email -> direta -> compra).
        *   Filtre por tipo de usuário, data, ou outras dimensões para insights mais específicos.
    *   **Relatório "Comparação de Modelos":**
        *   Compare o impacto de diferentes modelos de atribuição (ex: "Baseado em dados" vs. "Último clique") na contagem de conversões e na receita associada a cada canal. Isso ajuda a entender como cada canal contribui ao longo da jornada do cliente.
        *   **Exemplo de Comparação:**
            *   Canal "Organic Search": "Baseado em dados" (350 conversões, R$35.000) vs. "Último clique" (280 conversões, R$28.000). Isso indica que a busca orgânica frequentemente inicia a jornada, mas não é sempre o último ponto de contato.
            *   Canal "Direct": "Baseado em dados" (180 conversões, R$18.000) vs. "Último clique" (250 conversões, R$25.000). Isso sugere que o acesso direto é muitas vezes o ponto final da conversão, mesmo que outros canais tenham contribuído antes.

5.  **Otimização:** Use os insights dos relatórios de atribuição para realocar orçamentos de marketing e otimizar campanhas, focando nos canais que contribuem mais para a jornada completa do cliente, não apenas no último clique.

---

## Templates

### Template GTM - Tag de Evento GA4 (add_to_cart_custom)

```json
{
  "accountId": "GTM-XXXXXXX",
  "containerId": "GTM-XXXXXXX",
  "containerVersionId": "1",
  "fingerprint": "1234567890",
  "tag": [
    {
      "accountId": "GTM-XXXXXXX",
      "containerId": "GTM-XXXXXXX",
      "tagId": "3",
      "name": "GA4 - Evento - add_to_cart_custom",
      "type": "GA4_EVENT",
      "parameter": [
        {
          "type": "TAG_REFERENCE",
          "key": "measurementId",
          "value": "gtm.GA4_Configuration_Tag"
        },
        {
          "type": "TEMPLATE",
          "key": "eventName",
          "value": "add_to_cart_custom"
        },
        {
          "type": "MAP",
          "key": "eventParameters",
          "value": [
            {
              "type": "TEMPLATE",
              "key": "item_id",
              "value": "{{dl_item_id}}"
            },
            {
              "type": "TEMPLATE",
              "key": "item_name",
              "value": "{{dl_item_name}}"
            },
            {
              "type": "TEMPLATE",
              "key": "price",
              "value": "{{dl_price}}"
            },
            {
              "type": "TEMPLATE",
              "key": "currency",
              "value": "{{dl_currency}}"
            },
            {
              "type": "TEMPLATE",
              "key": "quantity",
              "value": "{{dl_quantity}}"
            }
          ]
        }
      ],
      "firingTriggerId": ["2"],
      "blockTriggerId": ["2"],
      "priority": 0
    }
  ]
}
```

### Template GTM - Variável de Camada de Dados (dl_item_id)

```json
{
  "accountId": "GTM-XXXXXXX",
  "containerId": "GTM-XXXXXXX",
  "containerVersionId": "1",
  "fingerprint": "1234567890",
  "variable": [
    {
      "accountId": "GTM-XXXXXXX",
      "containerId": "GTM-XXXXXXX",
      "variableId": "2",
      "name": "dl_item_id",
      "type": "DLV",
      "parameter": [
        {
          "type": "TEMPLATE",
          "key": "name",
          "value": "ecommerce.items.0.item_id"
        },
        {
          "type": "BOOLEAN",
          "key": "defaultValue",
          "value": "false"
        }
      ]
    }
  ]
}
```

---

## Checklist

- [x] Propriedade GA4 criada e stream de dados web configurado.
- [x] ID de Medição GA4 (`G-XXXXXXXXXX`) configurado corretamente na Tag de Configuração do GA4 no GTM.
- [x] Tag de Configuração do GA4 disparando em todas as páginas e validada via DebugView.
- [x] Google Signals ativado para coleta de dados e modelagem.
- [x] Retenção de dados ajustada para 14 meses (ou período desejado) em "Configurações de Dados".
- [x] Exclusão de tráfego interno configurada via filtros de IP no GA4 e variável GTM para `debug_mode`.
- [x] Pelo menos 3 eventos personalizados críticos (ex: `add_to_cart`, `form_submit`, `lead_generated`) configurados via GTM e validados.
- [x] Pelo menos 2 dimensões personalizadas de escopo de evento (ex: `item_name`, `user_type`) registradas no GA4.
- [x] Pelo menos 1 métrica personalizada de escopo de evento (ex: `price`, `quantity`) registrada no GA4.
- [x] Eventos de conversão marcados corretamente (ex: `purchase`, `generate_lead`) e validados em "Relatórios > Conversões".
- [x] Configurações de atribuição (modelo e janelas de lookback) revisadas e ajustadas.
- [x] Integração com Google Ads e/ou outras plataformas (ex: Search Console) estabelecida.
- [x] Consent Mode implementado ou revisado para conformidade com privacidade (LGPD/GDPR).

---

## Métricas de Referência

| Métrica                         | Benchmark Típico (E-commerce) | Meta Personalizada (Exemplo) |
|---------------------------------|-------------------------------|------------------------------|
| Taxa de Engajamento             | >50%                          | 65%                          |
| Visualizações de Página/Sessão  | 3 - 5                         | 4.5                          |
| Taxa de Conversão de E-commerce | 1% - 3%                       | 2.8%                         |
| Receita Média por Usuário (ARPU)| R$ 50 - R$ 200                | R$ 120                       |
| Taxa de Eventos de Conversão    | 5% - 15%                      | 10%                          |
| Tempo Médio de Engajamento      | 60s - 180s                    | 150s                         |

---

## Erros Comuns

1.  **ID de Medição incorreto na Tag de Configuração GA4 no GTM**: Muitas vezes, o ID `G-XXXXXXXXXX` é digitado incorretamente ou um ID antigo de uma propriedade Universal Analytics (`UA-XXXXXXXXX-X`) é usado.
    *   **Como evitar:** Sempre copie e cole o ID de Medição diretamente da seção "Admin GA4 > Stream de Dados > Detalhes do Stream de Web". Verifique no DebugView se o `_measurement_id` no hit é o correto.
2.  **Parâmetros de eventos personalizados não aparecem nos relatórios do GA4**: Mesmo que os parâmetros sejam enviados via GTM e visíveis no DebugView, eles não estarão disponíveis como dimensões ou métricas em "Explorações" ou relatórios padrão.
    *   **Como evitar:** É obrigatório registrar cada parâmetro de evento relevante como uma "Definição Personalizada" (Dimensão Personalizada ou Métrica Personalizada) no Admin do GA4 em "Configurações de Dados" > "Definições Personalizadas".
3.  **Filtragem de tráfego interno não funciona**: A configuração de filtros de IP no GA4 é ativada, mas o tráfego de IPs internos ainda aparece nos relatórios.
    *   **Como evitar:** Além de criar o filtro de IP no GA4 (Admin > Configurações de Dados > Filtros de Dados), é necessário que o GTM (ou código direto) envie um parâmetro `traffic_type` com o valor `internal` para os hits originados desses IPs. No GTM, crie uma variável de Lookup Table para o IP do visitante e um acionador de inicialização que adicione `traffic_type: internal` à tag de configuração GA4 apenas para esses IPs.
4.  **Eventos de e-commerce duplicados**: Disparar eventos de e-commerce (ex: `purchase`, `add_to_cart`) tanto pelo `gtag('event', ...)` direto quanto pelo GTM usando tags de evento GA4.
    *   **Como evitar:** Escolha uma única metodologia de implementação: ou tudo via `gtag()` (se a equipe de desenvolvimento tiver controle total e preferir) ou tudo via GTM (que oferece mais flexibilidade e controle para equipes de marketing). Se usar GTM, certifique-se de que o `dataLayer` esteja configurado corretamente e que as tags GTM sejam as únicas a enviar dados para o GA4.

---

## Dicas Avançadas

1.  **Implementação de Consent Mode v2 para Conformidade Avançada**: Para sites que operam sob LGPD ou GDPR, utilize o Consent Mode v2 para ajustar dinamicamente o comportamento das tags do GA4 com base no consentimento do usuário. Isso permite coletar dados agregados e modelados mesmo para usuários que recusam cookies de análise, mantendo a conformidade. Configure variáveis no GTM para `ad_storage`, `analytics_storage`, `ad_user_data`, `ad_personalization`.
2.  **Uso de GTM Server-Side para Privacidade e Performance**: Migre a coleta de dados GA4 para um contêiner de servidor no Google Tag Manager. Isso permite centralizar a coleta de dados, sanitizar informações sensíveis (PII) antes de enviar para o GA4, otimizar o carregamento do lado do cliente e ter maior controle sobre os dados enviados.
3.  **Explorações de Funil de Eventos para Análise de Jornada de Usuário**: Vá além dos relatórios padrão usando "Explorações > Funil de Eventos" para visualizar a progressão dos usuários através de etapas específicas da jornada.
    *   **Exemplo Prático:** Crie um funil para "Compra de Produto": `view_item` (visualizou produto) -> `add_to_cart` (adicionou ao carrinho) -> `begin_checkout` (iniciou checkout) -> `purchase` (comprou). Isso revela gargalos e taxas de abandono em cada etapa, permitindo otimizações focadas.
4.  **Integração GA4 com BigQuery para Análise de Dados Brutos**: Configure a exportação contínua de dados brutos do GA4 para o Google BigQuery (Admin > Integrações de Produto > Vinculação com o BigQuery). Isso possibilita análises SQL complexas, junção de dados do GA4 com outras fontes (CRM, ERP) e a criação de dashboards personalizados em ferramentas de BI como o Looker Studio ou Tableau, usando dados não agregados.
5.  **Configuração e Uso de `user_id` para Jornadas Cross-Device**: Implemente o `user_id` para usuários autenticados, enviando-o como um parâmetro de evento para *todos* os eventos do GA4. Isso permite que o GA4 unifique as sessões de um único usuário em diferentes dispositivos e navegadores, proporcionando uma visão mais precisa da jornada completa do cliente, desde a primeira interação até a conversão final, independentemente do dispositivo. Certifique-se de que o `user_id` não seja PII direta, mas um identificador persistente e anônimo.