---
name: web-analytics-audit
description: "Web Analytics Audit — Skill especializada para web analytics audit"
license: MIT
metadata:
  version: 1.0.0
  author: Cafe Code AI
  category: 15-analytics-dados
  updated: 2026-03-01
risk: safe
---

# Web Analytics Audit

Esta skill capacita o Claude a realizar auditorias completas de web analytics, focando em configurações, coleta de dados, relatórios, dashboards e atribuição no Google Analytics 4, garantindo a integridade e utilidade dos dados.

---

## Keywords

GA4 auditoria, coleta de dados, atribuição, relatórios personalizados, GTM, dimensões personalizadas, métricas, dashboards, fluxo de usuário, eventos GA4, data stream, consent mode.

---

## Quick Start

1.  **Verificação inicial da instalação GA4**: Acesse o site em modo de depuração (debug view) no GA4 para confirmar a coleta de eventos `page_view` e `session_start` em tempo real.
2.  **Auditoria de eventos cruciais**: Revise os 5 principais eventos de conversão (ex: `purchase`, `generate_lead`) no relatório "Eventos" do GA4 para verificar volumes e consistência de parâmetros.
3.  **Comparação de tráfego**: Compare os dados de `users` e `sessions` do relatório "Aquisição de tráfego" do GA4 com os logs do servidor ou Google Search Console para identificar discrepâncias.
4.  **Revisão de relatórios padrão**: Navegue pelos relatórios de "Aquisição de usuários", "Engajamento" e "Monetização" para identificar anomalias ou falta de dados.
5.  **Checagem de conversões**: Verifique se os eventos de conversão mais importantes para o negócio estão marcados corretamente no GA4 e se estão sendo registrados.

---

## Core Workflows

### Workflow 1: Auditoria de Configuração e Coleta de Dados GA4

Este workflow detalha a verificação da infraestrutura de coleta de dados do GA4, garantindo que os dados brutos sejam precisos e completos.

**Passos Detalhados:**

1.  **Verificação do Snippet de Instalação GA4 (GTM)**:
    *   **Ação**: Inspecione o código-fonte da página principal e de páginas de conversão (ex: checkout, página de obrigado) para identificar o container do Google Tag Manager (GTM). Use a extensão "Tag Assistant Companion" no Chrome.
    *   **Exemplo**: O Tag Assistant deve mostrar o GTM Container ID (ex: `GTM-XXXXXXX`) e o GA4 Configuration Tag disparando `page_view`.
    *   **Erro Comum**: Instalação duplicada do GA4 (via GTM e hardcoded), levando à duplicação de eventos e métricas.
    *   **Solução**: Remover a instalação redundante, mantendo apenas o método via GTM para centralização.

2.  **Auditoria de Eventos Automáticos e Aprimorados**:
    *   **Ação**: No Debug View do GA4, navegue por algumas páginas do site e execute interações básicas (scroll, click em link externo, download de arquivo).
    *   **Exemplo**: Confirme que `page_view`, `session_start`, `first_visit`, `scroll`, `click` (para links externos) e `file_download` estão sendo coletados com seus parâmetros padrão (`page_location`, `page_title`, etc.).
    *   **Verificação de `ignore_referrer`**: Para evitar auto-referência, verifique se o parâmetro `ignore_referrer` está configurado corretamente para o domínio principal nas configurações do Data Stream do GA4.

3.  **Validação de Eventos Personalizados e Parâmetros**:
    *   **Ação**: Para eventos críticos (ex: `add_to_cart`, `lead_form_submit`, `product_view`), use o Debug View e o relatório "Eventos" para garantir que estão sendo disparados com os parâmetros esperados.
    *   **Exemplo**: Para um evento `add_to_cart`, inspecione se os parâmetros `item_id`, `item_name`, `value`, `currency` e `quantity` estão presentes e com valores corretos.
    *   **Template de Verificação de Eventos (ver seção Templates)**.

4.  **Auditoria de Dimensões e Métricas Personalizadas**:
    *   **Ação**: No GA4, vá em `Administrar > Configurações de dados > Definições personalizadas`. Verifique se as dimensões personalizadas criadas (ex: `user_segment`, `author_name`, `product_category_level2`) estão mapeadas para os parâmetros de evento corretos e se estão sendo populadas nos relatórios.
    *   **Exemplo**: Uma dimensão personalizada `Tipo de Assinante` deve estar mapeada para o parâmetro `subscriber_type` de um evento `subscription_status_update`.
    *   **Erro Comum**: Parâmetro enviado via GTM com nome diferente do mapeado no GA4.

5.  **Exclusão de Tráfego Interno e Bots**:
    *   **Ação**: Em `Administrar > Configurações de dados > Filtros de dados`, verifique se um filtro para tráfego interno está ativo e se a lista de IPs da empresa, agências e desenvolvedores está atualizada.
    *   **Exemplo**: Filtro com nome "Internal Traffic" e método "Exclude" com regras de endereço IP.
    *   **Ação**: Em `Administrar > Configurações de dados > Configurações de dados > Coleta de dados`, garanta que a opção "Ativar a coleta de dados a partir de todos os usuários engajados" (para consent mode) e "Filtragem de bot" estão ativas.

### Workflow 2: Auditoria de Relatórios, Dashboards e Atribuição

Este workflow foca na usabilidade dos dados coletados, na precisão dos relatórios e na configuração dos modelos de atribuição para tomada de decisão.

**Passos Detalhados:**

1.  **Consistência dos Relatórios Padrão**:
    *   **Ação**: Compare dados de relatórios como "Aquisição de tráfego" e "Visão geral do engajamento" com períodos anteriores (mês a mês, ano a ano) para identificar quedas ou picos inesperados.
    *   **Exemplo**: Uma queda súbita de 30% em "Sessões" pode indicar um problema na coleta ou um filtro aplicado incorretamente.
    *   **Verificação**: Assegure-se de que os eventos de conversão marcados estão aparecendo nos relatórios de "Conversões" e de "Aquisição" como esperado.

2.  **Análise de Relatórios Exploratórios e Funis**:
    *   **Ação**: Crie um relatório exploratório de "Funil de exploração" para uma jornada crítica do usuário (ex: Visita > Adiciona ao Carrinho > Checkout > Compra).
    *   **Exemplo**: Um funil para e-commerce:
        *   Passo 1: `page_view` (página de produto)
        *   Passo 2: `add_to_cart`
        *   Passo 3: `begin_checkout`
        *   Passo 4: `purchase`
    *   **Análise**: Identifique os passos com maior drop-off (>40% de saída) e investigue as possíveis causas (problemas de UX, lentidão, bugs).

3.  **Auditoria dos Modelos de Atribuição**:
    *   **Ação**: Em `Administrar > Atribuição > Configurações de atribuição`, verifique o modelo padrão de atribuição (recomenda-se "Baseado em dados").
    *   **Exemplo**: No relatório "Modelos de Atribuição" (em `Publicidade`), compare as métricas de conversão para diferentes modelos (Último Clique, Primeiro Clique, Linear, Baseado em Dados) para entender como os canais estão sendo creditados.
    *   **Análise**: Se o "Último Clique" supervaloriza um canal e o "Baseado em Dados" mostra uma distribuição mais equilibrada, isso sugere que outros canais contribuem significativamente na jornada.

4.  **Dashboards e Visualização de Dados**:
    *   **Ação**: Revise os dashboards existentes (no GA4, Looker Studio ou outras ferramentas) para garantir que as métricas e dimensões exibidas são relevantes, precisas e atualizadas.
    *   **Exemplo**: Um dashboard de e-commerce deve incluir "Receita Total", "Taxa de Conversão de Compra", "Produtos Mais Vendidos" e "Custo por Aquisição (CPA)".
    *   **Verificação**: Assegure-se de que não há discrepâncias entre os dados nos dashboards e os relatórios brutos do GA4.

5.  **Análise de Fluxo de Usuário e Jornada**:
    *   **Ação**: Utilize a "Exploração de caminho" para entender as rotas que os usuários tomam antes de converter ou sair do site.
    *   **Exemplo**: Descobrir que usuários que visitam a página "Sobre Nós" antes de converter têm uma taxa de conversão 15% maior.
    *   **Insight**: Isso pode indicar que a página "Sobre Nós" é um fator de confiança importante na jornada.

---

## Templates

### Checklist de Auditoria de Eventos GA4

```
## Checklist de Auditoria de Eventos GA4

| Evento (Nome GA4)   | Parâmetros Essenciais                                     | Tipo de Parâmetro | Exemplo de Valor      | Status (Coletado/Erro/Não Implementado) | Notas e Recomendações                                                                                                      |
|--------------------|----------------------------------------------------------|-------------------|-----------------------|-----------------------------------------|----------------------------------------------------------------------------------------------------------------------------|
| page_view          | page_location, page_title, engagement_time_msec          | string, string, int | https://site.com/home | Coletado                                | OK. Coleta básica funcionando.                                                                                             |
| session_start      | (automático)                                             | -                 | -                     | Coletado                                | OK. Sessões sendo iniciadas.                                                                                               |
| first_visit        | (automático)                                             | -                 | -                     | Coletado                                | OK. Novos usuários sendo identificados.                                                                                    |
| add_to_cart        | items (item_id, item_name, price, quantity), value, currency | array, float, string  | [{'item_id':'SKU123','item_name':'Camisa Azul','price':50.0,'quantity':1}], 50.0, BRL | Erro                                    | Parâmetro 'value' está sendo enviado como string. Deve ser float. Corrigir no GTM.                                        |
| purchase           | transaction_id, value, currency, tax, shipping, items    | string, float, string, float, float, array | T12345, 120.0, BRL, 10.0, 5.0, [...] | Coletado                                | OK. Dados de compra completos.                                                                                             |
| generate_lead      | form_id, form_name, method                               | string, string, string | contato_form, Contato Geral, Email | Coletado                                | OK. Leads sendo registrados.                                                                                               |
| video_start        | video_url, video_title, video_provider                   | string, string, string | youtube.com/abc, Meu Vídeo, YouTube | Não Implementado                        | Implementar para vídeos incorporados para analisar engajamento de conteúdo multimídia.                                     |
| view_item_list     | item_list_name, items (item_id, item_name, price)        | string, array     | Resultados Busca, [...] | Coletado                                | OK. Análise de desempenho de listas de produtos.                                                                           |
| user_segment_update| user_segment                                             | string            | premium_customer      | Erro                                    | Parâmetro 'user_segment' não está sendo enviado para usuários logados. Verificar camada de dados (dataLayer).             |
```

### Plano de Ação de Otimização GA4

```
## Plano de Ação de Otimização GA4

| ID | Achado da Auditoria                                           | Recomendação Detalhada                                                                                                                                                                                           | Prioridade (Alta/Média/Baixa) | Responsável      | Prazo Estimado | Status         | Observações                                                                        |
|----|---------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------|------------------|----------------|----------------|------------------------------------------------------------------------------------|
| 01 | Evento `add_to_cart` está enviando `value` como string.       | Ajustar a tag de evento `add_to_cart` no GTM para garantir que o parâmetro `value` seja enviado como tipo `Number` (float) para cálculos precisos de monetização.                                            | Alta                          | Desenvolvedor Web | 2024-07-15     | Em Andamento   | Impacta relatórios de monetização e atribuição.                                    |
| 02 | Falta de rastreamento para interações com vídeos incorporados. | Implementar tags no GTM para rastrear eventos `video_start`, `video_progress` (25%, 50%, 75%) e `video_complete`, incluindo parâmetros como `video_url`, `video_title` e `video_provider`.                  | Média                         | Analista de Dados | 2024-08-01     | Pendente       | Essencial para entender o engajamento com conteúdo multimídia.                     |
| 03 | Discrepância de 15% nos usuários entre GA4 e Search Console.  | Investigar possíveis bloqueios de cookies, problemas de cache ou exclusões de tráfego que possam estar afetando a contagem de usuários no GA4. Verificar também a implementação do Consent Mode.               | Alta                          | Especialista GA4  | 2024-07-20     | Em Andamento   | Pode indicar perda de dados ou configuração incorreta do Consent Mode.             |
| 04 | Relatórios de atribuição mostram 90% das conversões no "Último Clique". | Recomendar a adoção do modelo de atribuição "Baseado em Dados" como padrão nas configurações do GA4 para uma visão mais equitativa da contribuição dos canais ao longo da jornada do cliente.          | Média                         | Analista de Dados | 2024-07-25     | Concluído      | Fornecerá insights mais precisos sobre o ROI de marketing.                         |
| 05 | Dimensão personalizada `user_segment` não está populada.      | Coordenar com a equipe de desenvolvimento para expor o `user_segment` na `dataLayer` para usuários autenticados, e então criar uma variável GTM e mapear a dimensão personalizada no GA4.                  | Alta                          | Desenvolvedor Back | 2024-08-10     | Pendente       | Crucial para segmentação e personalização de relatórios por tipo de usuário.       |
| 06 | Nenhum filtro de exclusão de tráfego interno configurado.     | Criar e ativar um filtro de dados no GA4 para excluir IPs internos (escritórios, agências, VPNs) a fim de garantir que os dados de tráfego sejam representativos dos usuários externos.                  | Alta                          | Especialista GA4  | 2024-07-10     | Concluído      | Evita que o tráfego de funcionários contamine os dados de desempenho.              |
```

---

## Checklist

-   [x] Verificar o snippet de instalação do GA4 no código-fonte ou GTM para garantir uma única e correta implementação.
-   [x] Confirmar a coleta dos eventos automáticos `page_view`, `session_start` e `first_visit` no Debug View do GA4.
-   [x] Auditar a configuração de todos os eventos personalizados e seus parâmetros essenciais (ex: `item_id`, `value`, `currency` para e-commerce).
-   [x] Validar a criação e o mapeamento de dimensões e métricas personalizadas no GA4, assegurando que os dados estão sendo populados.
-   [x] Revisar as configurações de exclusão de tráfego interno (IPs) e garantir que a lista esteja atualizada.
-   [x] Analisar a consistência dos dados de tráfego (usuários, sessões) comparando o GA4 com outras fontes (ex: Google Search Console, CRM).
-   [x] Verificar a configuração correta de metas/conversões (eventos marcados como conversão) e se estão alinhadas aos objetivos de negócio.
-   [x] Auditar a integridade dos dados em relatórios padrão (Aquisição, Engajamento, Monetização) em busca de anomalias ou lacunas.
-   [x] Conferir os modelos de atribuição configurados e seus impactos nos relatórios de conversão, recomendando "Baseado em dados" se apropriado.
-   [x] Revisar a implementação de e-commerce tracking (eventos `view_item`, `add_to_cart`, `purchase`) para garantir a captura de todos os detalhes da transação.
-   [x] Verificar a configuração do Google Signals e Consent Mode para garantir conformidade com privacidade e coleta de dados otimizada.

---

## Métricas de Referência

| Métrica                      | Benchmark (GA4) | Meta (GA4)   |
|------------------------------|-----------------|--------------|
| Taxa de Rejeição (Bounce Rate) | < 30%           | < 20%        |
| Taxa de Conversão E-commerce | 1.5% - 3%       | > 3.5%       |
| Tempo Médio de Engajamento   | > 60 segundos   | > 90 segundos|
| % Usuários Engajados         | > 60%           | > 75%        |
| CPA (Custo por Aquisição)    | R$50 - R$150    | < R$70       |
| Receita por Usuário          | R$5 - R$20      | > R$25       |

---

## Erros Comuns

1.  **Configuração Duplicada do GA4**: Ocorre quando o código base do GA4 é implementado via Google Tag Manager e também diretamente no código-fonte do site.
    *   **Como evitar**: Utilize apenas um método de implementação, preferencialmente via GTM para maior flexibilidade e controle. No GTM, use a tag de "Configuração do GA4" uma única vez para disparar o evento `page_view`.
2.  **Eventos Personalizados sem Parâmetros Essenciais**: Eventos importantes como `add_to_cart` ou `generate_lead` são disparados, mas não incluem parâmetros cruciais (ex: `item_id`, `value`, `form_id`). Isso limita a análise granular.
    *   **Como evitar**: Planeje cuidadosamente quais parâmetros são relevantes para cada evento. Sempre inclua identificadores únicos (IDs), valores monetários e descrições contextuais. Utilize o Debug View para verificar a presença e o formato correto dos parâmetros.
3.  **Filtragem Incorreta ou Ausente de Tráfego Interno**: O tráfego de funcionários, agências ou bots não é excluído, contaminando os dados com atividades não representativas.
    *   **Como evitar**: Mantenha uma lista atualizada de endereços IP internos e configure um filtro de dados de exclusão no GA4 em `Administrar > Configurações de dados > Filtros de dados`. Além disso, ative a "Filtragem de bot" nas configurações do stream de dados.
4.  **Discrepâncias de Dados entre GA4 e Outras Fontes (Ex: CRM, Google Ads)**: Divergências nos números de conversão ou receita entre sistemas, dificultando a tomada de decisão.
    *   **Como evitar**: Implemente o rastreamento de `transaction_id` para todas as compras e use o `client_id` ou `user_id` para integrar dados entre plataformas. Realize reconciliações regulares e verifique as configurações de modelo de atribuição em todas as ferramentas.
5.  **Configuração Incorreta ou Ausente do Consent Mode**: Não respeitar as preferências de consentimento do usuário, resultando em subcoleta de dados ou não conformidade com regulamentações como LGPD/GDPR.
    *   **Como evitar**: Implemente o Google Consent Mode v2 via GTM, ajustando o comportamento das tags GA4 com base nas escolhas de consentimento do usuário. Teste com ferramentas de consentimento (CMP) para garantir que as tags se ajustam corretamente.

---

## Dicas Avançadas

1.  **Uso de BigQuery Export (GA4)**: Para análises de dados mais complexas e união com fontes externas (CRM, dados offline), configure o BigQuery Export do GA4. Isso permite consultar dados brutos do GA4 usando SQL.
    *   **Exemplo Prático**: Juntar dados de `purchase` do GA4 com dados de `customer_lifetime_value` do CRM no BigQuery para identificar segmentos de clientes mais valiosos e otimizar campanhas de marketing.
2.  **Monitoramento de Data Streams com GTM Server-Side**: Mover a coleta de dados para um servidor próprio (via GTM Server-Side) oferece maior controle, segurança e resiliência a bloqueadores de anúncios e mudanças no navegador.
    *   **Exemplo Prático**: Enviar dados de eventos para GA4, Facebook CAPI e um sistema de e-mail marketing a partir de um único ponto no servidor, garantindo que os dados sejam consistentes e completos em todas as plataformas, mesmo se o navegador bloquear scripts de terceiros.
3.  **Customização Avançada de Relatórios Exploratórios com User-ID**: Implemente o `user_id` para usuários logados para unificar suas jornadas em diferentes dispositivos. Use essa dimensão personalizada em relatórios de "Exploração de caminho" ou "Funil de exploração".
    *   **Exemplo Prático**: Criar um funil de conversão que rastreia a jornada de um usuário específico, desde a primeira visita em um celular até a compra final em um desktop, permitindo uma análise holística do comportamento do cliente.
4.  **Análise de Cluster e Segmentação de Usuários**: Utilize técnicas de clusterização (ex: RFM - Recência, Frequência, Valor Monetário) fora do GA4 (com dados exportados para BigQuery ou Python) para identificar segmentos de usuários com comportamentos distintos.
    *   **Exemplo Prático**: Descobrir que usuários que visitam o site 3+ vezes por semana e interagem com 5+ páginas (alta frequência, alto engajamento) têm uma taxa de conversão 2x maior. Isso pode direcionar esforços de retenção e personalização.
5.  **Auditoria de Qualidade de Dados com Ferramentas Externas**: Além do Debug View do GA4, utilize ferramentas como o "dataLayer checker" ou scripts personalizados para validar a estrutura da `dataLayer` e o envio de hits.
    *   **Exemplo Prático**: Desenvolver um script Python que simula a navegação no site e verifica se os eventos esperados estão sendo disparados com os parâmetros corretos, alertando sobre quaisquer desvios do plano de tagueamento.
6.  **Otimização de Limites de Dados do GA4**: Esteja ciente dos limites de cardinalidade para dimensões personalizadas e exportação de dados para BigQuery. Para sites com alto volume, planeje a agregação de dados ou o uso de `sampling` (amostragem) consciente.
    *   **Exemplo Prático**: Se uma dimensão personalizada tem muitos valores únicos (ex: `product_name`), pode ser melhor usar `product_id` e juntar com um catálogo de produtos externo para evitar o problema `(other)` nos relatórios.