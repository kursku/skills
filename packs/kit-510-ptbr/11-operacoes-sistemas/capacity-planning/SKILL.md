---
name: capacity-planning
description: "Capacity Planning — Skill especializada para capacity planning"
license: MIT
metadata:
  version: 1.0.0
  author: Cafe Code AI
  category: 11-operacoes-sistemas
  updated: 2026-03-01
risk: safe
---

# Capacity Planning

Esta skill capacita o Claude a projetar e otimizar a alocação de recursos humanos, tecnológicos e financeiros para atender demandas futuras de serviços e projetos, garantindo a sustentabilidade operacional e a qualidade do serviço.

---

## Keywords

Dimensionamento de Equipes, Previsão de Demanda, Otimização de Recursos, SLA, Roadmap Tecnológico, Análise de Gargalos, Modelagem de Cenários, Gerenciamento de Fluxo de Trabalho, Disponibilidade de Serviço, TCO, ROI de Infraestrutura, Gestão de Portfólio.

---

## Quick Start

1.  **Coletar dados de demanda histórica:** Reúna o volume de tickets de suporte e a utilização de CPU de servidores nos últimos 12 meses.
2.  **Identificar picos e tendências:** Analise os dados para detectar sazonalidades (ex: pico de Black Friday) e taxas de crescimento mensais.
3.  **Projetar demanda futura:** Com base em planos de negócio (ex: lançamento de 3 novos produtos), estime o aumento de tickets e requisições para os próximos 6 meses.
4.  **Calcular capacidade atual:** Determine a produtividade média de um analista (ex: 80 tickets/mês) e a carga máxima de um servidor (ex: 300 RPS).
5.  **Dimensionar recursos:** Compare a demanda projetada com a capacidade atual para identificar a necessidade de contratações ou provisionamento de infraestrutura (ex: 2 novos analistas, 3 instâncias de servidor adicionais).

---

## Core Workflows

### Workflow 1: Dimensionamento de Equipes de Suporte N2 para Crescimento de Clientes

Este workflow detalha o processo de dimensionamento da equipe de suporte de segundo nível (N2) em um cenário de crescimento projetado da base de clientes premium de uma empresa SaaS, visando manter o Acordo de Nível de Serviço (SLA).

1.  **Coleta de Dados Históricos de Demanda (últimos 12 meses):**
    *   **Demanda Média de Tickets N2/mês:** 800 tickets.
    *   **Base Média de Clientes Premium:** 4.000 clientes.
    *   **Taxa de Abertura de Ticket N2 por Cliente Premium:** 800 tickets / 4.000 clientes = 0.2 tickets/cliente/mês.
    *   **Tempo Médio de Resolução (TMR) N2:** 4 horas por ticket.
    *   **SLA para Resolução N2:** 8 horas para 80% dos tickets.
    *   **Capacidade Média de um Analista N2:** Considerando 160 horas úteis por mês e 4 horas por ticket, um analista resolve 160/4 = 40 tickets/mês. (Se a empresa tem foco em qualidade e complexidade, este número pode ser menor do que um cenário de N1)
    *   **Equipe Atual de N2:** 6 analistas.

2.  **Projeção de Demanda Futura (próximos 6 meses):**
    *   **Crescimento de Clientes Premium:** A área de Vendas e Marketing projeta um crescimento de 20% na base de clientes premium, passando de 4.000 para 4.800 clientes nos próximos 6 meses.
    *   **Demanda Projetada de Tickets N2:** 4.800 clientes * 0.2 tickets/cliente/mês = 960 tickets/mês.

3.  **Cálculo da Capacidade Necessária:**
    *   **Analistas N2 Necessários:** 960 tickets/mês / 40 tickets/analista/mês = 24 analistas. (Ajustando a capacidade por analista para ser realista com a complexidade N2, o número de analistas aumenta significativamente. Vamos ajustar a capacidade para 120 tickets/mês, o que seria mais coerente com um analista N2 que foca em eficiência e não apenas complexidade, ou seja, resolve casos mais simples rapidamente e os complexos levam mais tempo, mas a média é 120).
    *   **Reavaliando Capacidade Média de um Analista N2:** 120 tickets/mês.
    *   **Analistas N2 Necessários (Reavaliado):** 960 tickets/mês / 120 tickets/analista/mês = 8 analistas.
    *   **Gap de Capacidade:** 8 analistas necessários - 6 analistas atuais = 2 novos analistas N2.

4.  **Validação e Ajustes Finais:**
    *   **Inclusão de Buffer:** Para lidar com picos inesperados, ausências ou treinamentos, adicione um buffer de 15% à equipe. 8 analistas * 1.15 = 9.2 analistas. Arredonde para 10 analistas.
    *   **Plano de Contratação:** Iniciar processo seletivo para 4 novos analistas (6 atuais + 4 novos = 10), visando ter os novos colaboradores treinados e produtivos em 3 meses, antes que o pico de demanda se materialize completamente.
    *   **Impacto no SLA:** Com 10 analistas, a capacidade total será de 10 * 120 = 1200 tickets/mês. Isso proporciona uma folga de 240 tickets/mês acima da demanda projetada de 960 tickets, garantindo que o SLA de 8 horas para 80% dos tickets seja mantido ou até melhorado.

### Workflow 2: Otimização de Capacidade de Servidores para Nova Feature de Alto Tráfego

Este workflow aborda o planejamento da infraestrutura de servidores para o lançamento de uma nova feature que se espera gerar um volume significativo de requisições, garantindo que o sistema suporte a carga sem degradação de performance.

1.  **Análise da Demanda Atual e Histórica da Infraestrutura:**
    *   **Requisições por Segundo (RPS) Médio Atual:** 1.500 RPS.
    *   **RPS de Pico Atual (Horário de Maior Acesso):** 2.000 RPS.
    *   **Configuração Atual de Servidores Web:** 6 instâncias AWS t3.large em um Auto Scaling Group (ASG).
    *   **Utilização Média de Recursos no Pico:** 60% de CPU, 40% de RAM.
    *   **Latência Média da API:** 80ms.
    *   **Capacidade Por Instância:** Se 6 instâncias suportam 2.000 RPS, cada instância t3.large suporta aproximadamente 2.000 / 6 = 333 RPS com a configuração e carga atuais.

2.  **Estimativa de Carga da Nova Feature:**
    *   **Testes de Carga em Homologação:** A nova feature foi testada isoladamente em um ambiente de homologação. Uma instância t3.large suportou 100 RPS da nova feature com 70% de CPU e uma latência de 60ms. (Esta feature é mais intensiva em recursos que as features atuais).
    *   **Demanda Esperada da Nova Feature:** Projeção de negócio estima um adicional de 500 RPS de pico gerados especificamente por esta nova funcionalidade.

3.  **Cálculo da Capacidade Adicional Necessária:**
    *   **RPS Total Projetado (Pico):** 2.000 RPS (pico atual) + 500 RPS (nova feature) = 2.500 RPS.
    *   **Capacidade Necessária para Nova Feature (apenas):** 500 RPS / 100 RPS/instância (capacidade da feature) = 5 instâncias t3.large dedicadas à nova feature.
    *   **Capacidade Total Necessária (considerando carga combinada):**
        *   Se cada instância t3.large suporta 333 RPS (média das features atuais), e a nova feature é mais pesada (100 RPS/instância), precisamos de uma abordagem mais granular.
        *   Assumindo que as 6 instâncias atuais já estão no limite de 2.000 RPS com 60% CPU (o que dá 333 RPS/instância com um buffer de 40%).
        *   Para 2.500 RPS totais, e considerando a intensidade da nova feature, é mais seguro calcular a capacidade total requerida.
        *   Vamos calcular a "capacidade efetiva" por instância com a nova feature: digamos que uma instância ainda pode lidar com 333 RPS, mas o "custo" da nova feature é maior.
        *   **Revisão**: Um método mais robusto seria calcular o "número de unidades de processamento" (UP) necessárias. Se 6 instâncias fornecem "6 unidades", e 2000 RPS consomem 6 unidades, então 2500 RPS consumiriam 2500/2000 * 6 = 7.5 unidades.
        *   **Instâncias Necessárias:** 7.5 instâncias. Arredondar para 8 instâncias t3.large.
        *   **Necessidade de Adicionar:** 8 instâncias necessárias - 6 instâncias atuais = 2 novas instâncias t3.large.

4.  **Considerações de Resiliência e Automação:**
    *   **Configuração do Auto Scaling Group (ASG):** Configurar o ASG para ter um mínimo de 6 instâncias e um máximo de 10 instâncias.
    *   **Políticas de Escalabilidade:** Definir políticas para adicionar uma instância quando a utilização média de CPU do grupo exceder 75% por 5 minutos, e remover uma instância quando cair abaixo de 40% por 15 minutos.
    *   **Monitoramento Proativo:** Implementar alertas para tendências de latência da API acima de 120ms ou erros HTTP > 1%, indicando degradação de serviço antes da capacidade ser totalmente esgotada.
    *   **Revisão do Tipo de Instância:** Se a utilização de CPU ou RAM for consistentemente alta (acima de 85% no pico) mesmo com as novas instâncias, reavaliar a possibilidade de migrar para instâncias de maior porte (ex: t3.xlarge ou m5.large) que ofereçam melhor desempenho por unidade de custo.

---

## Templates

### Plano de Capacity Planning - Equipe de Desenvolvimento de Software

```markdown
# Plano de Capacity Planning - Equipe de Desenvolvimento de Software

**Título:** Plano de Capacity Planning para Equipe "Alpha" - Q3/2025
**Data:** 2025-06-15
**Responsável:** Gerente de Engenharia - João Silva
**Período de Planejamento:** Q3 2025 (Julho, Agosto, Setembro)

## 1. Cenário Atual (Q2 2025)

*   **Número de Desenvolvedores:** 8 (4 Back-end, 4 Front-end)
*   **Projetos em Andamento:**
    *   Refatoração Módulo de Pagamentos (Back-end) - 60% Concluído
    *   Dashboard de Análise de Vendas (Front-end) - 80% Concluído
    *   Melhorias UX/UI Portal do Cliente (Front-end) - 30% Concluído
*   **Produtividade Média (Features/Sprint):** 7 Features entregues por sprint (ciclo de 2 semanas)
*   **Capacidade de Story Points/Sprint:** 45 Story Points
*   **Tech Debt Acumulada:** Estimada em 120 Story Points (principalmente no módulo de pagamentos)

## 2. Projeção de Demanda (Q3 2025)

*   **Novos Projetos Prioritários:**
    *   **Projeto "Gateway de Integração de Terceiros":** Demanda 3 Back-end devs por 2 meses. Estimativa: 80 Story Points.
    *   **Projeto "Notificações Personalizadas":** Demanda 2 Front-end devs por 1.5 meses. Estimativa: 50 Story Points.
*   **Crescimento de Features/Manutenção:**
    *   Manutenção e pequenas melhorias: 20% da capacidade da equipe.
    *   Suporte a bugs críticos: 10% da capacidade da equipe.
*   **Redução de Tech Debt:** Objetivo de reduzir 30% da tech debt no trimestre.

## 3. Análise de Gap

*   **Capacidade Disponível (Q3):**
    *   Considerando 8 devs * 45 SP/sprint = 360 SP/mês (aproximadamente, sem considerar férias/afastamentos).
    *   Capacidade Total Q3: 360 SP/mês * 3 meses = 1080 Story Points.
*   **Demanda Projetada (Q3):**
    *   Gateway: 80 SP
    *   Notificações: 50 SP
    *   Manutenção/Melhorias (20% de 1080 SP): 216 SP
    *   Suporte a Bugs (10% de 1080 SP): 108 SP
    *   Redução de Tech Debt (30% de 120 SP): 36 SP
    *   **Total Demanda Q3:** 80 + 50 + 216 + 108 + 36 = 490 Story Points.

*   **Análise:** A capacidade de 1080 SP é teoricamente muito superior à demanda de 490 SP. Isso indica que a equipe atual tem folga ou os projetos futuros têm escopo limitado. No entanto, a alocação por tipo de desenvolvedor é crucial.
    *   **Back-end:** Demanda de Gateway (80 SP) + 10% de Tech Debt (36 SP * 0.5) + Manutenção/Bugs (216*0.5 + 108*0.5) = 80 + 18 + 108 + 54 = 260 SP.
        *   Capacidade de 4 Back-end devs = 4 * 45 SP/sprint * 3 meses = 540 SP. Folga significativa.
    *   **Front-end:** Demanda de Notificações (50 SP) + 10% de Tech Debt (36 SP * 0.5) + Manutenção/Bugs (216*0.5 + 108*0.5) = 50 + 18 + 108 + 54 = 230 SP.
        *   Capacidade de 4 Front-end devs = 4 * 45 SP/sprint * 3 meses = 540 SP. Folga significativa.

*   **Conclusão do Gap:** Não há gap de capacidade em termos de número de desenvolvedores. A equipe atual consegue absorver a demanda projetada para Q3. A folga identificada pode ser usada para acelerar a redução de Tech Debt ou iniciar um novo projeto de menor prioridade.

## 4. Plano de Ação

*   **Otimização de Processos:** Realizar workshop de otimização de fluxo de trabalho para identificar gargalos e aumentar a eficiência em 5%.
*   **Alocação de Projetos:**
    *   Designar 3 Back-end devs para o "Gateway de Integração de Terceiros" durante Julho e Agosto.
    *   Designar 2 Front-end devs para "Notificações Personalizadas" durante Julho e metade de Agosto.
    *   Alocar 1 Back-end dev e 1 Front-end dev para focar 50% do tempo na redução de Tech Debt (36 SP).
    *   Distribuir o restante da capacidade para manutenção e pequenas melhorias.
*   **Treinamentos:** Oferecer treinamento em "performance de APIs" para os desenvolvedores Back-end e "otimização de renderização React" para Front-end, utilizando a folga na capacidade.
*   **Revisão do Roadmap:** Propor à gerência de produto a inclusão de um projeto adicional de médio porte para Setembro, considerando a capacidade ociosa.

## 5. Métricas de Sucesso (Q3)

*   **Conclusão dos Projetos Prioritários:** "Gateway de Integração de Terceiros" e "Notificações Personalizadas" entregues até final de Setembro.
*   **Redução de Tech Debt:** Pelo menos 36 Story Points de Tech Debt eliminados.
*   **Produtividade:** Manter a média de 7 Features/Sprint ou aumentar para 8 Features/Sprint.
*   **Satisfação da Equipe:** Realizar pesquisa para garantir que a carga de trabalho está equilibrada.
```

### Relatório de Utilização de Recursos de Infraestrutura

```markdown
# Relatório de Utilização de Recursos de Infraestrutura

**Título:** Relatório Mensal de Capacity Planning - Infraestrutura AWS
**Data:** 2024-10-31
**Responsável:** Analista de Infraestrutura - Carla Mendes
**Período de Análise:** Outubro de 2024

## 1. Recursos Monitorados e Utilização Média/Pico

| Recurso (Tipo) | Serviço/Componente | Métrica | Utilização Média (Out) | Utilização Pico (Out) | Capacidade Total | Status |
|----------------|--------------------|---------|------------------------|-----------------------|------------------|--------|
| **Servidores Web (EC2)** | Cluster Frontend | CPU (%) | 45%                    | 78%                   | 10 Inst. t3.medium | ALERTA |
|                | Cluster API       | CPU (%) | 35%                    | 65%                   | 12 Inst. t3.medium | OK     |
|                | Cluster Frontend | RAM (%) | 55%                    | 70%                   | 10 Inst. t3.medium | OK     |
|                | Cluster API       | RAM (%) | 40%                    | 55%                   | 12 Inst. t3.medium | OK     |
| **Bancos de Dados (RDS)** | PostgreSQL Prod  | Conexões (%) | 60%                    | 85%                   | 500 Conexões     | ALERTA |
|                | PostgreSQL Prod  | CPU (%) | 30%                    | 50%                   | db.r5.large      | OK     |
| **Rede (ELB)** | Application LB     | Requisições/s | 1.800                  | 2.500                 | 3.000 RPS        | OK     |
| **Filas (SQS)** | Fila Processamento | Mensagens Visíveis | 100                    | 1.200                 | Ilimitado        | OK     |
| **Armazenamento (EBS)** | Volume de Logs     | Uso de Disco (%) | 75%                    | 80%                   | 500 GB           | ALERTA |

## 2. Análise de Tendências

*   **Cluster Frontend (EC2):** A utilização de CPU no pico aumentou de 65% para 78% em Outubro, com um crescimento médio de 5% mês a mês nos últimos 3 meses. Atingiu o limite de alerta (80%) em 3 ocasiões.
*   **PostgreSQL Prod (RDS):** O número de conexões atingiu 85% da capacidade máxima em horários de pico noturno. Aumento de 10% nas conexões médias em relação ao mês anterior.
*   **Volume de Logs (EBS):** O uso de disco está em 80%, indicando que em 2-3 semanas o volume atingirá 95% se o crescimento continuar no ritmo atual de 5% por semana.

## 3. Recomendações de Escalabilidade e Otimização

*   **Cluster Frontend (EC2):**
    *   **Ação Imediata:** Aumentar o limite máximo do Auto Scaling Group (ASG) de 10 para 12 instâncias t3.medium para absorver picos.
    *   **Médio Prazo:** Investigar otimizações de código na aplicação frontend para reduzir a carga de CPU por requisição. Considerar upgrade para instâncias t3.large se a otimização não for suficiente em 3 meses.
*   **PostgreSQL Prod (RDS):**
    *   **Ação Imediata:** Otimizar o pool de conexões da aplicação para reduzir o número de conexões ativas simultaneamente.
    *   **Médio Prazo:** Avaliar a necessidade de escalar o RDS para uma instância maior (ex: db.r5.xlarge) ou implementar um proxy de conexão (ex: PgBouncer) para gerenciar melhor as conexões e aliviar a pressão no banco de dados.
*   **Volume de Logs (EBS):**
    *   **Ação Imediata:** Expandir o volume de EBS de 500 GB para 7