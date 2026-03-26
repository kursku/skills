---
name: launch-day-checklist
description: "Launch Day Checklist — Skill especializada para launch day checklist"
license: MIT
metadata:
  version: 1.0.0
  author: Cafe Code AI
  category: 08-lancamento-growth
  updated: 2026-03-01
risk: safe
---

# Launch Day Checklist

Esta skill capacita o Claude a guiar você através das etapas críticas e estratégias de execução para um lançamento de produto bem-sucedido, focando em growth, aquisição e retenção.

---

## Keywords

Lançamento de Produto, Growth Hacking, Aquisição de Usuários, Retenção, Dia D, Go-Live, Monitoramento Pós-Lançamento, Funil de Conversão, Testes A/B, Estratégia de Comunicação, Performance Web, Escalabilidade, Métricas de Lançamento, Incident Response.

---

## Quick Start

1.  **Valide a infraestrutura de monitoramento**: Confirme que todas as ferramentas de analytics (Google Analytics 4, Mixpanel), performance (New Relic, Datadog), e logs (Sentry, ELK) estão ativas e recebendo dados de ambiente de produção 30 minutos antes do "Go-Live".
2.  **Execute purga de cache global**: Imediatamente antes do lançamento, purgue o cache de CDN (ex: Cloudflare, Akamai) para garantir que a versão mais recente do site/aplicativo seja entregue aos usuários. Use comandos como `curl -X POST "https://api.cloudflare.com/client/v4/zones/{zone_id}/purge_cache"` com o `Purge Everything`.
3.  **Ative campanhas de aquisição pré-agendadas**: Verifique se as campanhas de Google Ads, Meta Ads, e e-mail marketing programadas para o lançamento estão ativas e com orçamentos corretos no momento exato do "Go-Live".
4.  **Monitore o funil de ativação em tempo real**: Abra dashboards de ferramentas como Mixpanel ou Amplitude e acompanhe a taxa de conclusão dos primeiros passos críticos do usuário (ex: cadastro, primeira ação, primeira compra) nos primeiros 15 minutos pós-lançamento.
5.  **Comunique ao time de suporte**: Envie um lembrete final ao time de suporte (via Slack ou e-mail) com os links para os FAQs atualizados e os canais de escalonamento para problemas urgentes.

---

## Core Workflows

### Workflow 1: Preparação Final e Go-Live Estratégico

Este workflow detalha as ações críticas a serem executadas nas últimas horas e minutos antes do lançamento, garantindo uma transição suave para o ambiente de produção.

**Passos Detalhados:**

1.  **D-3h: Verificação de Escalabilidade e Resiliência (Warm-up)**
    *   **Ação:** Realizar um "warm-up" dos servidores e serviços de backend, simulando uma carga crescente de usuários. Embora testes de carga completos sejam pré-lançamento, este é um teste final de prontidão.
    *   **Exemplo Concreto:** Utilizar ferramentas como Apache JMeter ou k6 para enviar um fluxo constante de requisições GET e POST para endpoints críticos como `/signup`, `/login`, `/products` por 30 minutos, monitorando CPU, RAM e latência via Datadog. Observar picos de latência acima de 200ms ou uso de CPU superior a 70% como alertas críticos.
    *   **Critério de Sucesso:** Nenhum erro 5xx e latência média abaixo de 150ms durante o warm-up.

2.  **D-1h: Última Revisão de Conteúdo e SEO**
    *   **Ação:** Uma equipe dedicada (marketing/SEO) deve fazer uma varredura final no site/app, verificando links quebrados, imagens ausentes, meta descrições, títulos e tags H1/H2. Confirmar que o `robots.txt` permite a indexação das páginas de lançamento e que todos os redirecionamentos (301/302) estão funcionando corretamente.
    *   **Exemplo Concreto:** Usar Screaming Frog SEO Spider para rastrear as 50 URLs mais críticas do novo produto e verificar a ausência de erros 404/5xx, duplicidade de títulos e meta descrições. Confirmar que as URLs canônicas estão configuradas corretamente para evitar problemas de SEO.

3.  **D-30min: Ativação de A/B Tests e Personalização**
    *   **Ação:** Ativar os experimentos A/B ou personalizações de experiência do usuário que foram pré-configurados para o lançamento. Isso pode incluir diferentes CTAs, layouts de landing page ou fluxos de onboarding.
    *   **Exemplo Concreto:** No Optimizely ou VWO, ativar o experimento "CTA_Launch_VariantA" versus "CTA_Launch_VariantB" que testa a cor do botão de compra principal (verde vs. laranja) e o experimento "Onboarding_Flow_v2" que introduz um novo passo de gamificação. Garantir que a segmentação correta (ex: novos usuários de campanhas pagas) esteja aplicada.

4.  **D-10min: Purga Global de Cache e DNS Propagation Check**
    *   **Ação:** Executar a purga final de CDN e verificar se as mudanças de DNS (se houver) já estão propagadas globalmente.
    *   **Exemplo Concreto:** Executar `purge everything` no painel da Cloudflare. Usar ferramentas como `whatsmydns.net` ou `dig @8.8.8.8 nomedodominio.com.br` para confirmar que os registros A, CNAME e outros estão apontando para os IPs corretos do novo ambiente de produção em diversas localidades.

5.  **D-0min: Go-Live e Confirmação de Serviços Essenciais**
    *   **Ação:** Pressionar o botão de "lançamento" (se for uma plataforma ou feature toggle) ou anunciar o lançamento através dos canais de comunicação. Imediatamente após, verificar a funcionalidade dos serviços mais críticos.
    *   **Exemplo Concreto:**
        *   **Login/Cadastro:** Um membro da equipe tenta se cadastrar e logar com sucesso.
        *   **Fluxo de Compra/Ativação:** Outro membro completa uma compra simulada ou o fluxo de ativação principal do produto.
        *   **Integrações Chave:** Confirmação de que o sistema de pagamento (Stripe/PagSeguro) e o CRM (Salesforce/HubSpot) estão recebendo dados corretamente.
        *   **Monitoramento:** Confirmar que os dashboards de métricas críticas (DAU, Activation Rate) estão populando com dados em tempo real.

### Workflow 2: Monitoramento Pós-Lançamento e Resposta Rápida

Este workflow foca nas atividades cruciais de monitoramento e resposta a incidentes imediatamente após o lançamento, essencial para mitigar problemas e otimizar a experiência do usuário.

**Passos Detalhados:**

1.  **H+0 a H+2: Monitoramento de Tráfego e Performance em Tempo Real**
    *   **Ação:** Observar os dashboards de analytics (GA4, Mixpanel) e performance (Datadog, New Relic) para anomalias no tráfego, picos de erro, latência elevada e gargalos. Focar na performance das páginas mais acessadas e nos funis críticos.
    *   **Exemplo Concreto:**
        *   **GA4:** Acompanhar "Usuários em tempo real" para verificar origem do tráfego e comportamento inicial. Criar um relatório em tempo real para "Eventos" para ver se os eventos de `page_view`, `add_to_cart`, `purchase` estão sendo disparados corretamente.
        *   **Datadog:** Focar nos gráficos de "Response Time by Endpoint" e "Error Rate by Service". Alertas para picos de latência acima de 300ms ou taxa de erro 5xx acima de 1%.
        *   **Sentry/LogRocket:** Monitorar logs de erro em tempo real para identificar exceções não tratadas ou JavaScript errors no frontend que possam indicar problemas na experiência do usuário. Priorizar erros com mais de 10 ocorrências por minuto.

2.  **H+1: Análise do Funil de Ativação e Conversão**
    *   **Ação:** Revisar as taxas de conversão dos funis críticos (ex: cadastro -> primeira ação, visita -> compra) usando ferramentas de Product Analytics. Comparar com benchmarks e metas pré