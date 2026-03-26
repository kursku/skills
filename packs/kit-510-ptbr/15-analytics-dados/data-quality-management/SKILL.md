---
name: data-quality-management
description: "Data Quality Management — Skill especializada para garantir a integridade, consistência e confiabilidade dos dados coletados no Google Analytics 4 (GA4)."
license: MIT
metadata:
  version: 1.0.0
  author: Cafe Code AI
  category: 15-analytics-dados
  updated: 2026-03-01
risk: safe
---

# Data Quality Management

Esta skill equipa o Claude com a expertise para auditar, monitorar e corrigir proativamente problemas de qualidade de dados no Google Analytics 4, assegurando relatórios precisos para decisões estratégicas.

---

## Keywords

Validação de Dados GA4, Consistência de Eventos, Atribuição Duplicada, Auditoria de Configuração GA4, Limpeza de Dados Web, Discrepância de Métricas, Monitoramento de Fluxo de Dados, Integridade de Parâmetros, Qualidade de User-ID, Exclusões de Referência, DebugView GA4, BigQuery Export.

---

## Quick Start

1.  **Verificação Inicial de Tags**: Abra uma página do site com o Google Tag Assistant e confirme a ativação da tag de configuração do GA4 (G-XXXXXXXXX) e dos principais eventos `page_view`.
2.  **Monitoramento em Tempo Real**: Acesse o relatório "Tempo real" no GA4 e simule interações cruciais (e.g., adição ao carrinho, compra) para verificar se os eventos e seus parâmetros são coletados imediatamente.
3.  **Análise de DebugView**: Utilize o "DebugView" no GA4 para inspecionar a estrutura de eventos e parâmetros enviados por um dispositivo de teste, buscando inconsistências em nomes ou tipos de dados.
4.  **Conferência de Volume de Sessões**: Compare o número de sessões no relatório "Aquisição > Visão geral" do GA4 com o tráfego registrado pelo servidor web (e.g., Nginx, Apache) ou CDN, identificando divergências acima de 5%.
5.  **Auditoria de Self-Referrals**: No relatório "Aquisição > Tráfego", filtre por `session_source / session_medium` contendo o próprio domínio do site ou gateways de pagamento não configurados como exclusões de referência.

---

## Core Workflows

### Workflow 1: Validação de Eventos e Parâmetros no GA4

Este workflow foca em garantir que os eventos críticos e seus parâmetros customizados estejam sendo coletados de forma completa, precisa e consistente no GA4.

**Passos Detalhados:**

1.  **Seleção de Eventos Críticos**: Identifique 3-5 eventos GA4 de alta importância para o negócio (e.g., `purchase`, `add_to_cart`, `lead_submission`, `page_view` para páginas chave).
    *   **Exemplo**: Para um e-commerce, os eventos críticos são `purchase`, `add_to_cart`, `view_item_list`.
2.  **Definição de Parâmetros Obrigatórios**: Para cada evento crítico, liste os parâmetros que *devem* estar presentes e seus formatos esperados.
    *   **Exemplo para `purchase`**:
        *   `transaction_id` (string, único, não nulo)
        *   `value` (number, >0)
        *   `currency` (string, e.g., 'BRL')
        *   `items` (array de objetos, cada objeto com `item_id`, `item_name`, `price`, `quantity`)
    *   **Exemplo para `add_to_cart`**:
        *   `items` (array de objetos, com `item_id`, `item_name`, `price`, `quantity`)
3.  **Configuração de Teste com GTM Preview**:
    *   Acesse o Google Tag Manager (GTM) e inicie o "Modo de Visualização" (Preview Mode).
    *   Navegue pelo site, executando as ações que disparam os eventos críticos.
    *   No GTM Debugger, para cada evento disparado, inspecione a tag GA4 configurada para ele.
    *   **Verificação**: Confirme se todos os parâmetros obrigatórios estão sendo enviados com os valores corretos e no formato esperado. Preste atenção a casos onde um parâmetro deveria ser um número mas é enviado como string, ou vice-versa.
    *   **Exemplo Prático**: Ao adicionar um produto ao carrinho, verifique no GTM Debugger se o evento `add_to_cart` foi disparado e se o array `items` contém os detalhes do produto (ID, nome, preço, quantidade) conforme o schema esperado.
4.  **Validação com GA4 DebugView**:
    *   Após a etapa anterior, acesse o relatório "DebugView" no GA4.
    *   Filtre pelo seu dispositivo de teste.
    *   **Verificação**: Observe os eventos críticos à medida que aparecem. Clique em cada evento para expandir e verificar os parâmetros associados. Confirme a presença dos parâmetros obrigatórios e seus valores.
    *   **Exemplo Prático**: No DebugView, ao realizar uma compra, localize o evento `purchase`. Expanda-o e certifique-se de que `transaction_id`, `value` e `currency` estão presentes e com os dados corretos que você inseriu no site durante o teste.
5.  **Auditoria com BigQuery Export (para grandes volumes)**:
    *   Se o GA4 estiver integrado ao BigQuery, execute consultas SQL para analisar a qualidade dos dados em larga escala.
    *   **Exemplo de Query**:
        ```sql
        SELECT
            event_name,
            COUNT(1) AS total_events,
            COUNTIF(param.value.string_value IS NULL) AS null_transaction_id,
            COUNTIF(param.value.int_value IS NULL AND param.value.double_value IS NULL) AS null_value
        FROM
            `project_id.dataset_id.events_*`,
            UNNEST(event_params) AS param
        WHERE
            event_name = 'purchase'
            AND _TABLE_SUFFIX = FORMAT_DATE('%Y%m%d', CURRENT_DATE('-1 days')) -- Dados de ontem
            AND param.key IN ('transaction_id', 'value')
        GROUP BY
            event_name
        ```
    *   **Análise**: Esta query ajudaria a identificar quantos eventos `purchase` tiveram `transaction_id` ou `value` nulos no dia anterior, indicando falhas na coleta.

### Workflow 2: Auditoria de Configuração e Consistência de Atribuição no GA4

Este workflow garante que as configurações administrativas do GA4 estejam otimizadas para a qualidade dos dados e que a atribuição de marketing seja confiável.

**Passos Detalhados:**

1.  **Revisão de Fluxos de Dados (Data Streams)**:
    *   No GA4, vá em "Administrador" > "Fluxos de dados".
    *   **Verificação**: Confirme que apenas os fluxos de dados necessários estão ativos (e.g., um para web, um para iOS, um para Android). Verifique se não há fluxos duplicados apontando para o mesmo site/app, o que causaria duplicação de dados.
    *   **Exemplo**: Certifique-se de que não existem dois fluxos de dados web para `meudominio.com.br` com IDs de medição diferentes, ambos coletando dados para a mesma propriedade.
2.  **Configuração de Medição Aprimorada (Enhanced Measurement)**:
    *   Dentro de cada fluxo de dados web, verifique as configurações de "Medição aprimorada".
    *   **Verificação**: Avalie se os eventos automáticos (e.g., `scroll`, `video_progress`, `file_download`) são relevantes. Desative aqueles que geram ruído desnecessário ou que já são coletados via GTM de forma mais controlada.
    *   **Exemplo**: Se você já tem um evento `file_download` customizado via GTM com parâmetros específicos, desative o `file_download` da medição aprimorada para evitar duplicação.
3.  **Exclusões de Referência (Referral Exclusions)**:
    *   No fluxo de dados web, vá em "Configurações de tag" > "Listar referências indesejadas".
    *   **Verificação**: Adicione todos os gateways de pagamento (e.g., `mercadopago.com.br`, `paypal.com`, `pagseguro.com.br`), subdomínios de login (e.g., `login.meudominio.com.br`), e o próprio domínio principal. Isso previne que essas fontes sejam indevidamente atribuídas como "referral".
    *   **Exemplo Prático**: Se um usuário faz uma compra e é redirecionado para `pagseguro.com.br` e depois volta ao site, sem a exclusão, o PagSeguro seria registrado como a fonte da conversão, o que é incorreto.
4.  **Janelas de Atribuição e Modelos (Attribution Settings)**:
    *   No GA4, vá em "Administrador" > "Configurações de atribuição".
    *   **Verificação**: Revise a janela de lookback para "Eventos de aquisição" (e.g., `first_open`, `first_visit`) e "Outros eventos de conversão". O padrão de 30 e 90 dias geralmente é adequado, mas certifique-se de que se alinha à jornada do cliente.
    *   **Verificação**: O modelo de atribuição padrão (e.g., "Baseado em dados") é geralmente o mais recomendado. Confirme se não foi alterado para um modelo menos ideal para o contexto do negócio (e.g., "Último clique direto").
    *   **Exemplo**: Se o ciclo de vendas é longo, uma janela de lookback de 90 dias para aquisição é mais realista do que 30 dias.
5.  **Filtragem de Tráfego Interno/Desenvolvedor**:
    *   No GA4, vá em "Administrador" > "Configurações de dados" > "Filtros de dados".
    *   **Verificação**: Crie e ative filtros para excluir tráfego interno (IPs da empresa) e tráfego de desenvolvedores. Isso remove dados irrelevantes que distorcem as métricas reais do usuário.
    *   **Exemplo**: Crie um filtro de tráfego "Interno" com `IP address` correspondendo a `(192\.168\.\d{1,3}\.\d{1,3})|(10\.\d{1,3}\.\d{1,3}\.\d{1,3})` e salve-o como ativo.

---

## Templates

### Relatório de Discrepância de Dados GA4

```
## Relatório de Qualidade de Dados GA4 - [Data da Auditoria]

**Responsável pela Auditoria:** [Seu Nome/Equipe]
**Período Analisado:** [Início] a [Fim]

---

### Sumário Executivo

Breve descrição das principais descobertas e impacto nos relatórios.

### Problemas Encontrados

| Métrica/Evento/Parâmetro | Valor Esperado (Referência) | Valor Real GA4 | Discrepância (%) | Causa Potencial | Ação Corretiva Proposta | Status |
|---------------------------|-----------------------------|----------------|------------------|-------------------|-------------------------|--------|
| Sessões (GA4 vs Servidor) | 100.000                     | 92.000         | 8%               | Problema de consentimento de cookies ou bloqueio de adblock | Revisar implementação de CMP e verificar triggers GTM | Aberto |
| Evento `purchase` (Total) | 2.500                       | 2.450          | 2%               | Pequenas perdas de conexão ou adblockers, dentro da margem aceitável | Monitorar tendência, não requer ação imediata | Fechado |
| Parâmetro `transaction_id` (Nulos em `purchase`) | 0                           | 50             | N/A              | Falha na extração do ID da transação no GTM ou erro backend | Auditar camada de dados e variáveis GTM para `transaction_id` | Aberto |
| Self-referrals (meudominio.com.br) | 0                           | 120            | N/A              | Domínio principal não excluído da lista de referências indesejadas | Adicionar `meudominio.com.br` em Exclusões de Referência | Aberto |
| Evento `view_item` (Duplicado) | 1 por produto visualizado | 2 por produto  | 100%             | Trigger GTM disparando duas vezes para o mesmo evento | Ajustar condição de trigger no GTM para evitar dupla ativação | Aberto |

### Recomendações Prioritárias

1.  Prioridade Alta: Revisar a implementação do Consent Mode e os triggers GTM para o evento `page_view` para mitigar a perda de sessões.
2.  Prioridade Média: Investigar a origem dos valores nulos para `transaction_id` nos eventos de compra.
3.  Prioridade Média: Adicionar `meudominio.com.br` e `gatewaysdepagamento.com` à lista de exclusões de referência do GA4.

---

### Checklist de Auditoria de Configuração GA4 (Data Quality)

```
## Checklist de Auditoria GA4 - Qualidade de Dados e Configuração

**Data da Auditoria:** [Data]
**Propriedade GA4:** [ID da Propriedade - G-XXXXXXXXX]
**Auditor:** [Nome do Auditor]

---

### Seção 1: Fluxos de Dados e Coleta

- [X]  **1.1 Fluxos de Dados:** Todos os fluxos (Web, iOS, Android) configurados são relevantes e não há duplicações?
- [X]  **1.2 Tag GA4:** A tag de configuração (G-XXXXXXX) está corretamente implementada via GTM/direta? (Verificado com Tag Assistant)
- [X]  **1.3 Medição Aprimorada:** Eventos automáticos de medição aprimorada estão ativados/desativados conforme a necessidade, sem duplicação com eventos GTM?
- [X]  **1.4 Consent Mode:** O Google Consent Mode v2 está implementado e operacional, respeitando o consentimento do usuário?
- [ ]  **1.5 User-ID:** O User-ID está sendo coletado de forma consistente para usuários logados, e a visualização de relatórios por User-ID está configurada?
- [X]  **1.6 Eventos Customizados:** Todos os eventos e parâmetros customizados críticos estão sendo coletados com nomes e tipos de dados consistentes?

### Seção 2: Atribuição e Filtragem

- [X]  **2.1 Exclusões de Referência:** Todos os gateways de pagamento, subdomínios de login e o próprio domínio principal estão na lista de exclusões de referência?
- [X]  **2.2 Modelos de Atribuição:** O modelo de atribuição padrão (ex: Baseado em dados) e as janelas de lookback estão alinhados com a estratégia de negócio?
- [X]  **2.3 Filtros de Dados:** Filtros para tráfego interno (IPs da empresa) e tráfego de desenvolvedores estão configurados e ativos?
- [ ]  **2.4 Limiares de Dados:** Os limites de dados (data thresholds) estão configurados de forma a não ocultar informações críticas desnecessariamente?

### Seção 3: BigQuery Export e Integrações

- [ ]  **3.1 BigQuery Export:** A exportação de dados para o BigQuery está configurada e funcionando corretamente para auditorias avançadas?
- [ ]  **3.2 Outras Integrações:** Integrações com Google Ads, Search Console, etc., estão ativas e enviando/recebendo dados corretamente?

### Observações Adicionais:

[Quaisquer notas ou descobertas que não se encaixam nos itens acima.]

---
```

---

## Checklist

- [X] Verificar a implementação da tag de configuração GA4 (G-XXXXXXXXX) em todas as páginas via Google Tag Assistant.
- [X] Comparar o volume de `page_view` ou `sessions` no GA4 com logs do servidor ou outras ferramentas de análise (ex: Cloudflare Analytics), buscando discrepâncias >5%.
- [X] Auditar a consistência dos nomes e tipos de dados de parâmetros customizados em eventos chave (e.g., `item_id` como string, `value` como número).
- [X] Configurar e ativar filtros de dados no GA4 para excluir IPs internos da empresa e tráfego de desenvolvedores.
- [X] Monitorar o relatório de aquisição para identificar `self-referrals` (o próprio domínio ou gateways de pagamento) e adicioná-los às exclusões de referência.
- [X] Revisar as configurações de Medição Aprimorada (Enhanced Measurement) em cada fluxo de dados para evitar duplicação ou coleta de eventos irrelevantes.
- [X] Validar se o `user_id` está sendo coletado de forma consistente e única para usuários autenticados em todas as plataformas (web/app).
- [X] Verificar o impacto do Consent Mode (modo de consentimento) na coleta de dados, assegurando que o consentimento esteja sendo respeitado sem perdas excessivas de dados essenciais.
- [X] Executar testes de ponta a ponta para eventos de conversão críticos (e.g., `purchase`, `lead_submission`) usando o DebugView do GA4 para verificar a coleta de dados completa e correta.
- [X] Checar a janela de lookback e o modelo de atribuição padrão nas "Configurações de Atribuição" para garantir alinhamento com a estratégia de marketing.

---

## Métricas de Referência

| Métrica | Benchmark (Meta) | Meta (Exemplo Real) |
|---------------------------------------------|--------------------|---------------------|
| Discrepância de Sessões GA4 vs. Servidor Web | < 2%               | 1.5%                |
| Taxa de Eventos Críticos Duplicados         | < 0.1%             | 0.05%               |
| % de Campos Obrigatórios Nulos em Eventos   | < 0.5%             | 0.2%                |
| Taxa de Self-Referrals no Tráfego de Aquisição | < 1%               | 0.8%                |
| % de Eventos com Parâmetros Malformatados   | < 0.2%             | 0.1%                |
| Duração Média da Sessão (Anomalia de Queda/Pico) | Varia (monitorar +/- 10%) | +/- 7%              |

---

## Erros Comuns

1.  **Duplicação de Eventos GA4**: Ocorre quando um evento (ex: `page_view`, `add_to_cart`) é disparado por um trigger do GTM e também pela Medição Aprimorada (Enhanced Measurement) do GA4.
    *   **Como evitar**: Desative os eventos automáticos na Medição Aprimorada que já são controlados via GTM. Se um evento customizado no GTM for disparado por um trigger muito amplo (e.g., `Page View - All Pages`), refine as condições do trigger para ser mais específico (e.g., `Page View - Some Pages` onde a URL contém `/carrinho/`).
2.  **Dados de Atribuição Incorretos por Self-Referrals**: Ocorre quando gateways de pagamento ou subdomínios de login são registrados como a origem do tráfego, em vez de manter a origem original da sessão.
    *   **Como evitar**: Adicione todos os domínios de gateways de pagamento (ex: `pagseguro.com.br`, `mercadopago.com.br`) e todos os subdomínios do seu próprio site que não deveriam ser fontes de tráfego (ex: `login.meudominio.com.br`, `app.meudominio.com.br`) à lista de "Exclusões de Referência" nas configurações do fluxo de dados GA4.
3.  **Métricas de Engajamento Infladas/Subestimadas**: Eventos como `scroll` ou `session_start` podem ser excessivamente sensíveis ou mal configurados, levando a métricas enganosas de engajamento.
    *   **Como evitar**: Para `scroll`, ajuste o limiar de rolagem nas configurações da Medição Aprimorada ou desative-o e crie um evento customizado no GTM com um limiar mais realista (e.g., 90%). Para `session_start`, garanta que o consentimento de cookies esteja funcionando corretamente, pois o bloqueio de `analytics_storage` pode impedir a coleta de `session_start` e distorcer a contagem de sessões.
4.  **Inconsistência de `transaction_id`**: Falha na extração ou envio de um `transaction_id` único para eventos de `purchase`, dificultando a reconciliação com sistemas de backend e a desduplicação de transações.
    *   **Como evitar**: Garanta que o `transaction_id` esteja disponível na camada de dados (dataLayer) logo após a compra. Use uma variável de camada de dados no GTM para capturá-lo e enviá-lo como um parâmetro para o evento `purchase`. Implemente validação para garantir que o `transaction_id` seja sempre preenchido e que seja um valor único e consistente com o sistema de e-commerce.

---

## Dicas Avançadas

1.  **Monitoramento de Anomalias com BigQuery e Looker Studio**: Configure a exportação de dados do GA4 para o BigQuery. Crie consultas SQL para identificar desvios significativos nas métricas chave (e.g., queda abrupta de `page_view`, pico incomum de `user_engagement`) usando funções como `AVG()` e `STDDEV()` sobre períodos anteriores. Visualize esses alertas em um dashboard no Looker Studio, disparando notificações automatizadas via BigQuery Scheduled Queries e Cloud Functions se os limites forem excedidos.
2.  **Schema de Dados GA4 e Dicionário de Eventos**: Desenvolva e mantenha um "Data Dictionary" detalhado para todos os eventos e parâmetros customizados do GA4. Isso inclui o nome do evento, descrição, parâmetros esperados (com tipo de dado, formato, exemplos), e a página/condição de disparo. Este documento serve como fonte única de verdade e facilita a padronização e auditoria, por exemplo, definindo que `item_id` deve ser sempre uma string e `item_price` um float.
3.  **Validação Automatizada de Dados via GA4 Data API**: Utilize a GA4 Data API (ou Google Analytics Admin API) para construir scripts (Python, Node.js) que automaticamente buscam volumes de dados (ex: total de `page_view` por dia, número de `purchase` com `transaction_id` nulo) e os comparam com benchmarks históricos ou com dados de outras fontes (ex: CRM, logs do servidor). Isso permite identificar problemas de forma proativa antes que afetem relatórios importantes.
4.  **Implementação de um Data Layer Consistente**: Adote uma estratégia robusta de `dataLayer` no site que siga um schema pré-definido. Isso garante que os dados necessários para o GA4 (e outras ferramentas de marketing) estejam sempre disponíveis de forma estruturada e consistente, reduzindo a chance de erros de extração no GTM. Por exemplo, ter um objeto `ecommerce` padrão para detalhes do produto e transações em todas as páginas relevantes.
5.  **Testes A/B para Qualidade de Dados**: Ao implementar novas tags GA4 ou fazer alterações significativas, utilize ferramentas de teste A/B (ex: Google Optimize, Split.io) para direcionar uma pequena porcentagem do tráfego para a nova implementação e monitorar a qualidade dos dados apenas para esse segmento. Isso permite validar a integridade da coleta antes de um lançamento completo, minimizando o risco de contaminação de dados na propriedade principal.