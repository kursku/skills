---
name: escalation-matrix
description: "Escalation Matrix — Skill especializada para criação, gestão e otimização de matrizes de escalada para incidentes e problemas críticos."
license: MIT
metadata:
  version: 1.0.0
  author: Cafe Code AI
  category: 11-operacoes-sistemas
  updated: 2026-03-01
---

# Escalation Matrix

Esta skill capacita o Claude a projetar, implementar e otimizar matrizes de escalada robustas, garantindo a resposta eficiente a incidentes e a resolução de problemas críticos.

---

## Keywords

Matriz de Escalada, Gestão de Incidentes, SLAs, MTTR, Runbooks, Severidade de Impacto, Notificação de Crise, Suporte Nível 1, Suporte Nível 2, Suporte Nível 3, On-Call, Operações de TI, Problemas Críticos.

---

## Quick Start

1.  **Categorize Eventos Críticos**: Identifique cenários que exigem escalada, como "Indisponibilidade de Serviço Crítico P1" ou "Reclamação de Cliente VIP com Risco de Churn".
2.  **Defina Níveis de Severidade**: Padronize as classificações de impacto (ex: P1-Crítico, P2-Alto, P3-Médio) com critérios claros para cada.
3.  **Mapeie Níveis de Resposta**: Associe cada nível de severidade a camadas de equipe (ex: N1 Suporte, N2 Engenharia, N3 Gerência) e seus tempos-limite de resposta.
4.  **Configure Canais de Notificação**: Estabeleça métodos de alerta para cada nível (ex: PagerDuty para L2, Slack para L3, E-mail para stakeholders executivos).
5.  **Documente e Treine**: Crie SOPs detalhados e realize sessões de treinamento para todas as equipes envolvidas na matriz.

---

## Core Workflows

### Workflow 1: Criação de Matriz de Escalada para Incidentes de TI de Alta Severidade (P1/P2)

Este workflow detalha a construção de uma matriz para assegurar a rápida resposta e resolução de falhas sistêmicas críticas.

1.  **Identificação de Gatilhos e Classificação de Severidade**:
    *   **Gatilho Exemplo P1**: Indisponibilidade total do sistema de processamento de pagamentos. Critério: Mais de 50% das transações falhando por mais de 5 minutos.
    *   **Gatilho Exemplo P2**: Degradação severa da performance do CRM. Critério: Tempo de resposta do CRM > 5 segundos para 30% dos usuários por mais de 15 minutos.
    *   **Impacto P1**: Paralisação financeira, perda de receita imediata, alto risco reputacional.
    *   **Impacto P2**: Redução da produtividade das equipes de vendas e suporte, insatisfação do cliente, risco de perda de oportunidades.
2.  **Definição das Camadas de Escalada e Responsabilidades**:
    *   **Nível 1 (L1 - Suporte/Monitoramento)**: Equipe de Operações de TI.
        *   **Ação**: Confirmação do incidente via ferramentas de monitoramento (Datadog, Grafana), triagem inicial, verificação de runbooks básicos.
        *   **Tempo para Resposta (SLA)**: P1: 5 minutos; P2: 15 minutos.
        *   **Tempo para Escalada (SLO)**: P1: 10 minutos sem progresso; P2: 30 minutos sem progresso.
    *   **Nível 2 (L2 - Especialistas Técnicos)**: Equipe de Engenharia de Software ou Infraestrutura (on-call).
        *   **Ação**: Análise aprofundada da causa raiz, execução de runbooks avançados, aplicação de workarounds ou correções emergenciais.
        *   **Tempo para Resposta (SLA)**: P1: 15 minutos; P2: 45 minutos.
        *   **Tempo para Escalada (SLO)**: P1: 30 minutos sem resolução; P2: 90 minutos sem resolução.
    *   **Nível 3 (L3 - Gerência de TI/Líderes)**: Gerente de Operações, Diretor de TI.
        *   **Ação**: Alocação de recursos adicionais, tomada de decisões estratégicas (ex: rollback, failover para DR), comunicação com a alta direção e stakeholders externos.
        *   **Tempo para Resposta (SLA)**: P1: 10 minutos; P2: 30 minutos.
        *   **Tempo para Escalada (SLO)**: P1: 60 minutos sem resolução; P2: 180 minutos sem resolução.
    *   **Nível 4 (L4 - Alta Direção/Comitê de Crise)**: CIO, CTO, CEO.
        *   **Ação**: Aprovação de planos de contingência de alto custo/impacto, comunicação pública, gestão de crise corporativa.
3.  **Configuração de Notificações e Canais**:
    *   **L1 -> L2**: Sistema de on-call (PagerDuty/Opsgenie) com alerta sonoro no celular e chamada automática após 10 minutos (P1) ou 30 minutos (P2) de não reconhecimento/resolução.
    *   **L2 -> L3**: Mensagem no canal Slack #incidents-p1-critical ou #incidents-p2-high para o grupo de Gerência de TI, seguido de e-mail automático após 30 minutos (P1) ou 90 minutos (P2).
    *   **L3 -> L4**: Chamada telefônica direta pelo Gerente de Operações para CIO/CTO, e-mail para grupo de C-level, após 60 minutos (P1) ou 180 minutos (P2) sem resolução no L3.
4.  **Criação de Canais de Comunicação Dedicados**:
    *   **Interno**: Canal de Slack temporário para cada incidente P1/P2 (ex: #inc-20240725-001-erp-down), reunindo todas as equipes envolvidas.
    *   **Externo**: Atualização de página de status pública (ex: status.suaempresa.com) a cada 30 minutos em caso de P1, com comunicação via e-mail para clientes afetados.

### Workflow 2: Gestão Proativa de Problemas Críticos de Cliente com Risco de Churn

Este workflow foca em antecipar e resolver a insatisfação de clientes de alto valor antes que resultem em perda de negócios.

1.  **Identificação de Gatilhos de Insatisfação Crítica**:
    *   **Gatilho Exemplo**: Cliente VIP (ARR > R$ 500k) com CSAT abaixo de 3/5 ou 2+ chamados de suporte abertos simultaneamente por mais de 48 horas.
    *   **Impacto**: Perda de receita recorrente, dano à reputação, impacto em métricas de retenção.
2.  **Definição de Níveis de Escalada e Responsabilidades**:
    *   **Nível 1 (L1 - Gerente de Conta/CSM)**: Customer Success Manager (CSM) ou Gerente de Conta.
        *   **Ação**: Contato proativo com o cliente para entender a insatisfação, coordenação interna com equipes de suporte/produto para priorização.
        *   **Tempo para Ação (SLA)**: 4 horas após o gatilho.
        *   **Tempo para Escalada (SLO)**: 24 horas sem plano de ação ou progresso significativo.
    *   **Nível 2 (L2 - Liderança de CS/Vendas)**: Diretor de Customer Success, VP de Vendas.
        *   **Ação**: Intervenção direta com o cliente, oferta de soluções estratégicas ou compensações (ex: créditos, serviços adicionais), alocação de equipe técnica dedicada.
        *   **Tempo para Ação (SLA)**: 8 horas após a escalada.
        *   **Tempo para Escalada (SLO)**: 48 horas sem resolução satisfatória ou reversão da insatisfação.
    *   **Nível 3 (L3 - C-level)**: CEO, COO, CCO.
        *   **Ação**: Contato pessoal com o cliente, decisões de negócio de alto nível (ex: renegociação de contrato, mudanças na estratégia de produto), comunicação pública em caso de grande impacto.
3.  **Estabelecimento de Prazos e Modos de Ação**:
    *   **L1 -> L2**: Notificação automática via Salesforce Service Cloud ou Zendesk para o Diretor de CS após 24 horas sem um plano de ação documentado ou após o cliente expressar desejo de cancelar.
    *   **L2 -> L3**: E-mail detalhado do Diretor de CS para o C-level com histórico do cliente, ações tomadas e risco de churn, acionado após 48 horas sem reversão da insatisfação no L2.
4.  **Documentação e Acompanhamento Contínuo**:
    *   Todos os detalhes da escalada, interações com o cliente e planos de ação devem ser registrados no CRM (ex: Salesforce) com campos específicos para "Status de Escalada" e "Risco de Churn".
    *   Reunião semanal de "Revisão de Clientes Críticos" com a liderança de CS e Vendas para acompanhar o progresso dos clientes escalados.

---

## Templates

### Template de Matriz de Escalada de Incidentes de TI

```
| Gatilho do Incidente | Severidade | Impacto no Negócio | Tempo p/ Resposta (SLA) | Tempo p/ Resolução (SLO) | Nível 1 - Responsável/Ação | Nível 2 - Responsável/Ação | Nível 3 - Responsável/Ação | Métodos de Notificação |
|----------------------|------------|--------------------|-------------------------|--------------------------|----------------------------|----------------------------|----------------------------|------------------------|
| Falha total de Autenticação | P1 (Crítico) | Indisponibilidade de acesso para TODOS os usuários. Perda de receita imediata. | 5 minutos                 | 30 minutos               | Analista L1: Triagem inicial, coleta logs. | Engenheiro Backend Sênior: Análise causa, rollback/patch. | Gerente de Operações: Decisão de failover, comunicação executiva. | PagerDuty, Slack @oncall-ops, SMS, Telefone |
| Lentidão crítica do Banco de Dados | P2 (Alto) | Degradação de performance > 70% em funcionalidades chave. Experiência do usuário severamente afetada. | 15 minutos                | 120 minutos              | Analista L1: Verificação de métricas DB, reinício de serviços não-críticos. | DBA Sênior: Otimização de queries, escalonamento de recursos DB. | Diretor de TI: Aprovação de infraestrutura adicional, comunicação interna. | Slack #incidents-p2, E-mail p/ ti-lideranca |
| Erros intermitentes na API de Terceiros | P3 (Médio) | 15% das integrações com parceiros falham. Impacto em relatórios e automações. | 30 minutos                | 240 minutos              | Analista L1: Validação de credenciais, teste de conectividade. | Desenvolvedor Backend: Debugging da integração, contato com terceiro. | Coordenador de Suporte: Acompanhamento, definição de workaround. | E-mail p/ equipe-dev, Slack #integracoes |
```

### Template de Notificação de Escalada (Email)

```
Assunto: [URGENTE] ESCALADA CRÍTICA: Incidente P1 - Indisponibilidade do Sistema de Pagamentos (ID: INC-P1-20240725-001)

Prezados,

Informamos que o incidente de criticidade P1 "Indisponibilidade total do Sistema de Pagamentos" (ID: INC-P1-20240725-001) atingiu o tempo limite de resolução para a equipe de Nível 2.

A escalada para o Nível 3 (Gerência de Operações) foi acionada automaticamente às 14:35 BRT.
O impacto atual é a paralisação completa das transações financeiras e a impossibilidade de processar vendas, resultando em perda de receita estimada em R$ 10.000/hora.

Solicitamos o apoio imediato da Gerência de Operações para alocação de recursos adicionais, tomada de decisões estratégicas (ex: ativação de plano de contingência secundário) e coordenação da comunicação executiva.

**Próxima atualização em 15 minutos (14:50 BRT).**
Por favor, juntem-se ao canal de comunicação dedicado no Slack: #inc-20240725-001-pagamentos

Atenciosamente,

Equipe de Operações de TI
[Nome do Contato de Plantão L2]
[Telefone de Contato]
```

---

## Checklist

-   [x] Gatilhos de escalada claramente definidos para cada cenário crítico.
-   [x] Níveis de severidade (P1, P2, P3...) padronizados e compreendidos por todas as equipes.
-   [x] Responsáveis por cada nível de escalada nomeados e com contatos atualizados (incluindo on-call).
-   [x] Tempos de resposta (SLA) e resolução (SLO) estabelecidos e realistas para cada nível de severidade.
-   [x] Métodos de notificação (automáticos e manuais) configurados, testados e redundantes.
-   [x] Canais de comunicação dedicados para cada tipo de escalada (Slack, e-mail, telefone, ferramenta de on-call).
-   [x] Procedimentos de comunicação com stakeholders internos e externos (clientes, imprensa) documentados.
-   [x] Rotinas de treinamento e simulação da matriz de escalada (tabletop exercises) realizadas periodicamente.
-   [x] Processo de revisão pós-incidente (post-mortem) estabelecido para melhoria contínua da matriz.
-   [x] Ferramentas de suporte (ticketing, monitoramento, pager) integradas à matriz de escalada.

---

## Métricas de Referência

| Métrica                      | Benchmark            | Meta                 |
|------------------------------|----------------------|----------------------|
| MTTR (Mean Time To Resolve) P1 | < 60 minutos         | < 30 minutos         |
| Tempo Médio de Escalada (TME) | < 15 minutos         | < 10 minutos         |
| Taxa de Re-escalada          | < 5%                 | < 2%                 |
| % de Incidentes Resolvidos no Nível 1 | > 60%                | > 75%                |
| Número de Escaladas P1/mês   | < 5                  | < 2                  |
| CSAT de Clientes Escalados   | > 7 (escala 1-10)    | > 8 (escala 1-10)    |

---

## Erros Comuns

1.  **Gatilhos Ambíguos**: A ausência de critérios claros para acionar uma escalada leva a decisões inconsistentes ou tardias.
    *   **Como evitar**: Em vez de "Escalar se o problema for grave", defina "Escalar se o serviço essencial estiver 50% indisponível por mais de 5 minutos, afetando mais de 20% dos usuários".
2.  **Contatos Desatualizados**: Listas de contato e responsáveis on-call desatualizadas resultam em escaladas para pessoas erradas ou indisponíveis.
    *   **Como evitar**: Implemente uma rotina de revisão mensal da matriz, incluindo telefones e e-mails, e utilize ferramentas de on-call que gerenciem agendas e substituições (ex: PagerDuty, Opsgenie).
3.  **Falta de Ownership Claro entre Níveis**: A responsabilidade de um incidente se perde entre os níveis, com equipes esperando que outras resolvam.
    *   **Como evitar**: Para cada nível de escalada, defina explicitamente as ações esperadas e os limites de sua responsabilidade. Exemplo: "L1 é responsável pela triagem e execução de runbooks básicos. Se o runbook não resolver em 10 minutos, o L2 assume a propriedade completa da investigação."

---

## Dicas Avançadas

1.  **Escalada Preditiva com IA/ML**: Utilize algoritmos de Machine Learning para analisar dados históricos de incidentes e telemetria, prevendo a probabilidade de um problema escalar antes que atinja os gatilhos definidos.
    *   **Exemplo Prático**: Um modelo pode identificar um padrão de uso de CPU e latência de rede que, em 80% dos casos passados, levou a um incidente P1, acionando um alerta de pré-escalada para o Nível 2 antes mesmo do impacto ser sentido pelos usuários.
2.  **Matrizes Dinâmicas por Contexto**: Crie sub-matrizes de escalada para diferentes serviços, clientes ou períodos críticos (ex: Black Friday, fechamento de mês), ajustando SLAs, SLOs e equipes envolvidas.
    *   **Exemplo Prático**: Para o serviço de e-commerce durante a Black Friday, o SLA de resposta para um incidente P1 pode ser reduzido de 5 para 2 minutos, e o Nível 3 inclui o Diretor Comercial e o CEO diretamente no ciclo de notificação inicial.
3.  **Simulações de Desastre e Tabletop Exercises**: Realize simulações periódicas de cenários de falha crítica (ex: queda de datacenter, ataque DDoS) envolvendo todos os níveis da matriz, testando a comunicação, tomada de decisão e eficácia dos runbooks.
    *   **Exemplo Prático**: Uma simulação de "falha total do provedor de nuvem" pode revelar gargalos na comunicação entre Níveis 2 e 3 e a necessidade de um canal de comunicação de emergência fora da infraestrutura principal.
4.  **Feedback Loop Contínuo via Post-Mortem Automatizado**: Integre os resultados de análises post-mortem (causa raiz, ações corretivas) diretamente na revisão da matriz de escalada, ajustando gatilhos e responsabilidades automaticamente.
    *   **Exemplo Prático**: Após um incidente P2 onde o tempo de escalada do L1 para o L2 foi 20% maior que o SLO, o sistema propõe uma revisão do critério de escalada ou um treinamento adicional para a equipe L1 na execução de um runbook específico.
5.  **Integração com Ferramentas de Orquestração de Resposta**: Conecte a matriz de escalada a ferramentas de automação que disparam ações corretivas (ex: reiniciar serviço, reverter deployment, isolar componente) ao atingir um determinado nível.
    *   **Exemplo Prático**: Quando um incidente P1 é escalado para o Nível 2, a ferramenta de orquestração (ex: Rundeck, Ansible Tower) pode automaticamente acionar um runbook para tentar um rollback do último deployment ou provisionar recursos adicionais na nuvem.