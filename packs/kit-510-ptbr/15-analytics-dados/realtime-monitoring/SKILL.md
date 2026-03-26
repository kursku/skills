---
name: realtime-monitoring
description: "Realtime Monitoring — Skill especializada para realtime monitoring"
license: MIT
metadata:
  version: 1.0.0
  author: Cafe Code AI
  category: 15-analytics-dados
  updated: 2026-03-01
risk: safe
---

# Realtime Monitoring

Esta skill capacita o Claude a otimizar e executar tarefas de monitoramento de dados em tempo real utilizando o Google Analytics 4 (GA4), focando na detecção instantânea de tendências, anomalias e performance de campanhas para ações imediatas.

---

## Keywords

GA4 Realtime, Monitoramento em Tempo Real, Análise de Tráfego, Eventos GA4, Conversões Instantâneas, Atribuição Imediata, Depuração GA4, DebugView, Fluxo de Usuários, Campanhas ao Vivo, Alertas Personalizados GA4, Performance de Conteúdo.

---

## Quick Start

1.  **Acessar Relatório em Tempo Real no GA4**: Navegue para "Relatórios" > "Tempo Real" no painel do Google Analytics 4.
2.  **Verificar Usuários Ativos**: Observe o card "Usuários nos últimos 30 minutos" para a contagem atual de visitantes e suas localizações geográficas.
3.  **Filtrar por Dimensão Principal**: Utilize os cards "Usuários por Primeira fonte / médio", "Visualizações por título da página e nome da tela" ou "Eventos por nome do evento" para entender o comportamento instantâneo.
4.  **Analisar Eventos Chave**: No card "Eventos por nome do evento", identifique eventos de conversão (ex: `purchase`, `generate_lead`, `form_submission`) para monitorar o desempenho instantâneo das metas de negócio.

---

## Core Workflows

### Workflow 1: Monitoramento de Lançamento de Campanha de Marketing Digital

Este workflow detalha o acompanhamento da performance de uma nova campanha de marketing digital imediatamente após seu lançamento, utilizando os recursos de tempo real do GA4 para validação e otimização rápidas.

1.  **Preparação Pré-Lançamento**:
    *   **Configurar UTMs Específicas**: Assegure que todos os links da campanha (e-mail marketing, anúncios pagos, posts em redes sociais) contenham parâmetros UTM que permitam fácil identificação no GA4. Por exemplo: `utm_source=email_newsletter_julho`, `utm_medium=email`, `utm_campaign=lancamento_produto_x`, `utm_content=banner_topo`. A consistência é crucial.
    *   **Verificar Configuração de Eventos de Conversão**: Confirme que os eventos de conversão relevantes (e.g., `purchase`, `form_submission`, `add_to_cart`, `begin_checkout`) estão configurados corretamente e sendo acionados no ambiente de teste. Utilize o `DebugView` (Administrador > DebugView) para simular interações de usuário e verificar a coleta de eventos e seus parâmetros antes do lançamento oficial.

2.  **Monitoramento Imediato Pós-Lançamento**:
    *   **Acessar Relatório de Tempo Real**: Navegue para "Relatórios" > "Tempo Real" no GA4.
    *   **Filtrar por Campanhas Específicas**: No card "Usuários por Primeira fonte / médio" ou "Usuários por Campanha", clique no nome da campanha (ex: `lancamento_produto_x`) para isolar o tráfego gerado por ela. Se a campanha não aparecer imediatamente, aguarde alguns minutos, pois a latência é mínima, mas existe.
    *   **Analisar Tráfego e Comportamento**:
        *   **Localização Geográfica**: Verifique o card "Usuários por Cidade" para confirmar se o tráfego está vindo das regiões geográficas esperadas para a campanha. Desvios podem indicar segmentação incorreta da audiência.
        *   **Engajamento com Conteúdo**: Observe o card "Visualizações por título da página e nome da tela" para identificar quais páginas os usuários da campanha estão visitando e quais estão sendo ignoradas. Anomalias aqui (muitas visualizações de páginas de erro 404, por exemplo) indicam problemas de URL de destino.
        *   **Eventos Chave**: No card "Eventos por nome do evento", monitore a taxa de ocorrência de eventos importantes como `page_view`, `scroll`, `add_to_cart`, `begin_checkout`, e, crucialmente, os eventos de conversão configurados para a campanha. Um baixo volume de `scroll` pode indicar desinteresse no conteúdo da landing page.
    *   **Comparar com Baseline**: Se houver dados históricos de campanhas similares, compare o volume de tráfego e a taxa de eventos com campanhas anteriores de performance similar para identificar desvios positivos ou negativos rapidamente.

3.  **Ações e Otimização em Tempo Real**:
    *   **Detecção de Falhas de Link**: Se o tráfego da campanha for zero ou muito baixo, verifique imediatamente os links UTM na plataforma de anúncio. Se o tráfego estiver vindo, mas para páginas de erro, ajuste os URLs de destino na plataforma da campanha (Google Ads, Facebook Ads, etc.).
    *   **Problemas de Performance da Página**: Se houver alto volume de saídas imediatas (poucos eventos além de `page_view` e `session_start`), investigue a velocidade de carregamento da página, a clareza do call-to-action (CTA) ou a relevância do conteúdo. Ferramentas como PageSpeed Insights podem ajudar.
    *   **Otimização de Conteúdo**: Se uma página específica da campanha tiver alta visualização, mas baixo engajamento (poucos scrolls, cliques em CTAs), considere ajustar o conteúdo, o design ou a disposição dos elementos para melhorar a experiência do usuário e a conversão.
    *   **Escalar ou Pausar**: Com base nas conversões e no engajamento em tempo real, decida se a campanha precisa de mais investimento (se estiver performando bem) ou se deve ser pausada para ajustes significativos (se estiver com performance abaixo do esperado).

### Workflow 2: Identificação e Troubleshooting de Anomalias de Tráfego e Conversão

Este workflow visa detectar e diagnosticar rapidamente desvios inesperados no comportamento do usuário ou nas métricas de conversão, permitindo intervenções proativas para minimizar impactos negativos no negócio.

1.  **Monitoramento Contínuo de Métricas Chave**:
    *   **Configurar Insights Personalizados no GA4**: Embora não sejam *em tempo real* (processados diariamente), utilize "Insights Personalizados" (Administrador > Insights Personalizados) para receber alertas sobre mudanças significativas em métricas como "Total de Usuários", "Receita" ou "Eventos de Conversão" em períodos de 24 horas. Para detecção em tempo real, considere soluções externas.
    *   **Dashboards no Looker Studio com Dados GA4**: Crie dashboards dedicados no Looker Studio (anteriormente Google Data Studio) conectados ao GA4, configurando a taxa de atualização dos dados para o mínimo possível (geralmente 15 minutos). Inclua gráficos de linha para "Usuários Ativos", "Eventos de Conversão" e "Transações" para visualizar tendências e identificar anomalias rapidamente.
    *   **Definir Limiares de Alerta**: Estabeleça limites aceitáveis para métricas-chave. Por exemplo, uma queda de 50% nos "Usuários Ativos" em 10 minutos ou uma queda de 80% nos "Eventos de `purchase`" em 30 minutos em comparação com a média horária esperada.

2.  **Detecção de Anomalias no Relatório de Tempo Real**:
    *   **Queda Abrupta de Usuários**: Se o card "Usuários nos últimos 30 minutos" mostrar uma queda drástica (ex: de 200 para 5) em comparação com o volume esperado para o horário, isso pode indicar um problema grave (ex: site fora do ar, tag GA4 quebrada, problema de servidor, bloqueio de IP).
        *   **Ação Imediata**: Verifique a disponibilidade do site (ping, status do servidor), a implementação do GTM/GA4 (usando Tag Assistant), e logs de servidor para erros 5xx.
    *   **Pico Inesperado de Tráfego**: Um aumento súbito e sem explicação (ex: de 100 para 1000 usuários em minutos) pode ser tráfego de spam, um ataque de bot, ou uma menção viral não planejada.
        *   **Ação Imediata**: Utilize o card "Usuários por Primeira fonte / médio" e "Visualizações por título da página e nome da tela" para identificar a origem e o comportamento. Se for tráfego suspeito, configure filtros de IP (se relevante) ou utilize as funcionalidades de exclusão de tráfego interno do GA4 (Administrador > Configurações de Dados > Filtros de Dados).
    *   **Queda de Eventos de Conversão**: Se os eventos de conversão (ex: `purchase`, `generate_lead`) diminuírem significativamente (ex: de 10 por hora para 0) enquanto o tráfego geral se mantém, isso pode indicar um problema no funil de conversão ou no processo de checkout.
        *   **Ação Imediata**: Analise o "Fluxo de Usuários" no relatório de Tempo Real ou, para uma análise mais profunda e com maior latência, o "Relatório de Funil de Exploração" (Explorar > Análise de Funil) para identificar onde os usuários estão saindo. Verifique formulários, carrinhos de compra ou processos de checkout para erros ou mudanças recentes.

3.  **Utilização do `DebugView` para Diagnóstico Profundo**:
    *   **Ativar Modo Debug**: Adicione `?_dbg=1` ao URL do seu site, utilize o "Preview Mode" do Google Tag Manager (GTM) ou a extensão "Google Analytics Debugger" para forçar o envio de eventos para o `DebugView`.
    *   **Monitorar Eventos em Tempo Real**: No `DebugView` (Administrador > DebugView), observe o fluxo detalhado de eventos, parâmetros e propriedades do usuário em tempo real. Cada evento é listado cronologicamente, permitindo inspecionar todos os dados associados a cada interação.
    *   **Identificar Eventos Ausentes/Incorretos**: Se um evento de conversão não aparecer no `DebugView` após uma ação do usuário, significa que a tag não está disparando corretamente. Se os parâmetros estiverem errados (ex: `value` = 0 para uma compra), a coleta de dados será comprometida.
    *   **Diagnosticar Problemas de Atribuição**: Verifique os parâmetros de fonte/mídia (`_traffic_source.name`, `_traffic_source.medium`) para garantir que a atribuição está sendo capturada corretamente para cada sessão, validando se as UTMs estão sendo interpretadas como esperado.

---

## Templates

### Configuração de Lógica de Alerta de Queda de Tráfego (Exemplo Simulado para Automação Externa)

```
// Este template descreve a lógica para um alerta, dado que GA4 não possui alertas nativos em tempo real.
// Para implementar, você precisaria de uma ferramenta de automação (ex: Google Cloud Functions, Zapier)
// que monitore a API do GA4 (ou dados exportados para BigQuery) e dispare notificações.

// Tipo de Alerta: Queda drástica de usuários ativos
// Métrica Monitorada: activeUsers (da API do GA4 ou BigQuery export)
// Período de Avaliação: Últimos 10 minutos vs. Média da última hora (mesmo dia da semana)
// Limiar de Disparo: Se (activeUsers_ultimos_10_min < (activeUsers_media_ultima_hora * 0.4))
//                   OU se (activeUsers_ultimos_10_min = 0) por mais de 5 minutos consecutivos.
// Escopo: Tráfego de todo o site, ou segmentado por 'country' ou 'deviceCategory'.
// Frequência de Verificação: A cada 2 minutos.
// Ação em Caso de Disparo: Enviar notificação para o canal #analytics-alertas no Slack
//                          e e-mail para analytics@empresa.com.br.
// Conteúdo da Notificação:
//   "ALERTA GA4 - Queda Severa de Tráfego!
//   Data/Hora: 2024-07-26 14:15 BRT
//   Usuários Ativos (últimos 10 min): 8
//   Média Histórica (última hora, mesmo dia/horário): 210
//   Desvio: -96.19%
//   Causa Potencial: Verificar status do site, GTM e tags GA4.
//   Link Direto GA4 Tempo Real: https://analytics.google.com/analytics/web/#/p[SEU_ID_DA_PROPRIEDADE]/reports/realtime"
```

### Relatório de Eventos em Tempo Real para Monitoramento de Conversões E-commerce

```
// Guia de interpretação para a seção