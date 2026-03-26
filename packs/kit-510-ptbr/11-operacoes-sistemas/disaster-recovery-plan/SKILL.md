---
name: disaster-recovery-plan
description: "Disaster Recovery Plan — Skill especializada para elaboração, implementação e gestão de planos de recuperação de desastres (DRP) para infraestruturas e aplicações críticas."
license: MIT
metadata:
  version: 1.0.0
  author: Cafe Code AI
  category: 11-operacoes-sistemas
  updated: 2026-03-01
risk: safe
---

# Disaster Recovery Plan

Esta skill capacita o Claude a atuar como um especialista em Disaster Recovery Plan (DRP), guiando na criação, validação e execução de estratégias robustas para assegurar a continuidade operacional após incidentes severos.

---

## Keywords

Recuperação de Desastres, DRP, RTO, RPO, Continuidade de Negócios, BIA, Análise de Impacto, Plano de Contingência, Teste de Recuperação, Infraestrutura Crítica, Resiliência Cibernética, Gestão de Crises, Failover, Backup e Restauração.

---

## Quick Start

1.  **Identificar Ativos Críticos**: Liste os 5 sistemas e dados mais essenciais para a operação, como o sistema de ERP, CRM e banco de dados de clientes, e seus respectivos proprietários.
2.  **Estabelecer RTO/RPO**: Defina o Tempo de Recuperação Objetivo (RTO) e o Ponto de Recuperação Objetivo (RPO) para cada ativo crítico. Ex: ERP: RTO 4h, RPO 15min.
3.  **Avaliar Cenários de Desastre**: Considere desastres como falha total do datacenter primário, ataque ransomware massivo ou indisponibilidade da rede principal, e o impacto em seus ativos.
4.  **Iniciar Documentação Simplificada**: Esboce um plano inicial com equipe de recuperação, procedimentos básicos de failover e localização de backups para o sistema de e-commerce.

---

## Core Workflows

### Workflow 1: Elaboração e Implementação de um Plano de Recuperação de Desastres (DRP) Abrangente

Este workflow detalha a criação de um DRP robusto, focando em passos práticos para garantir que todos os componentes críticos sejam cobertos e que o plano seja executável.

1.  **Análise de Impacto no Negócio (BIA) Detalhada**:
    *   **Ação**: Colaborar com líderes de negócio para mapear processos críticos e seus sistemas de suporte.
    *   **Exemplo**: Para o processo de "Processamento de Pedidos Online", identifique o sistema de e-commerce (frontend), banco de dados de produtos e clientes, sistema de pagamento e integração com logística.
    *   **Saída**: Documento BIA listando processos, sistemas, RTO (4 horas) e RPO (15 minutos) e MAA (Tempo Máximo Aceitável de Indisponibilidade: 8 horas) para cada sistema.
2.  **Identificação de Equipe de Resposta a Desastres (ERT)**:
    *   **Ação**: Nomear líderes e membros da equipe com responsabilidades claras.
    *   **Exemplo**: Líder de TI (coordenador geral), Arquiteto de Infraestrutura (recuperação de servidores), Administrador de Banco de Dados (restauração de dados), Líder de Segurança (resposta a incidentes cibernéticos), Gerente de Comunicações (comunicação externa/interna).
    *   **Saída**: Lista de ERT com contatos, papéis e responsabilidades primárias e secundárias.
3.  **Definição da Estratégia de Recuperação**:
    *   **Ação**: Escolher a abordagem de recuperação para cada sistema com base em RTO/RPO e custo.
    *   **Exemplo**:
        *   **Sistema ERP (RTO 4h, RPO 15min)**: Ambiente de recuperação "Hot Site" com replicação síncrona de dados para um datacenter secundário.
        *   **Sistema de RH (RTO 24h, RPO 4h)**: Backup diário para nuvem, ambiente de recuperação "Cold Site" (infraestrutura sob demanda).
    *   **Saída**: Documento de Estratégia de Recuperação detalhando as soluções técnicas (replicação, backup, virtualização, nuvem) e os locais de recuperação (DRP-site).
4.  **Desenvolvimento de Procedimentos Detalhados de Recuperação**:
    *   **Ação**: Criar manuais passo a passo para a recuperação de cada sistema crítico.
    *   **Exemplo**:
        *   **Procedimento para ERP**:
            1.  Ativar datacenter secundário.
            2.  Verificar status da replicação de dados.
            3.  Executar script de failover do banco de dados (SQL Server AlwaysOn).
            4.  Direcionar tráfego para os servidores de aplicação no site secundário via DNS/Load Balancer.
            5.  Validar integridade dos dados e funcionalidade da aplicação com testes de fumaça.
            6.  Notificar equipes de negócio sobre a ativação.
    *   **Saída**: Manuais técnicos detalhados com comandos, configurações e verificações.
5.  **Plano de Comunicação e Testes**:
    *   **Ação**: Elaborar um plano de comunicação de crise e agendar testes regulares.
    *   **Exemplo**:
        *   **Comunicação**: Modelos de e-mail para clientes, fornecedores e equipe interna. Canais de comunicação alternativos (WhatsApp Business, rádio).
        *   **Teste**: Agendar teste de failover do ERP para o ambiente secundário, anual, com simulação de desastre total no site primário.
    *   **Saída**: Plano de comunicação de crise e cronograma de testes de DRP.

### Workflow 2: Teste, Manutenção e Ativação de um DRP

Este workflow foca em garantir que o DRP esteja sempre atualizado e funcional, cobrindo desde a validação periódica até a resposta real a um desastre.

1.  **Planejamento e Execução de Testes de DRP**:
    *   **Ação**: Realizar testes periódicos, simulando cenários de desastre.
    *   **Exemplo**:
        *   **Teste Anual de Failover Total (ERP)**:
            1.  Simular indisponibilidade do datacenter primário.
            2.  Ativar o DRP conforme os procedimentos documentados para o ERP.
            3.  Medir o RTO real e verificar o RPO após a recuperação.
            4.  Validar a funcionalidade completa do ERP no ambiente secundário por 4 horas.
            5.  Realizar o rollback para o ambiente primário (se aplicável e planejado).
        *   **Teste de Recuperação de Dados (Banco de Dados de Clientes)**:
            1.  Selecionar um subset de dados.
            2.  Simular perda de dados específicos.
            3.  Executar procedimento de restauração de backup para um ambiente isolado.
            4.  Verificar a integridade dos dados restaurados.
    *   **Saída**: Relatório de Teste de DRP (conforme template abaixo) com RTO/RPO alcançados e lições aprendidas.
2.  **Revisão e Atualização Contínua do DRP**:
    *   **Ação**: Manter o DRP atualizado com as mudanças na infraestrutura, aplicações e processos.
    *   **Exemplo**:
        *   **Trimestral**: Revisar lista de contatos da ERT, fornecedores críticos e acordos de nível de serviço (SLAs).
        *   **Semestral**: Atualizar procedimentos de recuperação para sistemas que sofreram upgrades significativos (ex: migração de banco de dados para nova versão, adição de novo módulo no ERP).
        *   **Pós-incidente/Pós-teste**: Integrar lições aprendidas e ajustar o plano imediatamente.
    *   **Saída**: Registro de controle de versões do DRP, com data da última revisão e alterações.
3.  **Treinamento e Conscientização da Equipe**:
    *   **Ação**: Treinar a ERT e equipes de TI e negócios relevantes nos procedimentos do DRP.
    *   **Exemplo**:
        *   **Simulado de Mesa (Tabletop Exercise)**: Para a ERT, simular um ataque cibernético e discutir as etapas de resposta, comunicação e recuperação, sem tocar em sistemas reais.
        *   **Treinamento Técnico**: Sessões práticas para administradores de sistema e DBA sobre failover e restauração.
    *   **Saída**: Relatórios de treinamento e lista de participantes.
4.  **Ativação do DRP em Cenário de Desastre Real**:
    *   **Ação**: Executar o DRP quando um desastre declarado exceder os limites operacionais aceitáveis.
    *   **Exemplo**:
        *   **Declaração de Desastre**: Indisponibilidade total do datacenter primário devido a falha elétrica generalizada por mais de 2 horas.
        *   **Passos**:
            1.  Líder de TI declara o desastre, ativa a ERT.
            2.  Equipe de comunicações emite alertas internos e externos.
            3.  Equipe de infraestrutura executa os procedimentos de failover para o ERP no site secundário.
            4.  Equipe de banco de dados verifica a consistência dos dados.
            5.  Equipe de segurança monitora anomalias no ambiente secundário.
            6.  Equipe de negócios valida a funcionalidade crítica.
            7.  Monitoramento contínuo da recuperação e do ambiente secundário.
    *   **Saída**: Registro de incidentes, relatório pós-incidente, lições aprendidas.

---

## Templates

### Plano de Recuperação de Desastres (DRP) Simplificado - Sistema de Gestão de Clientes (CRM)

```markdown
# Plano de Recuperação de Desastres (DRP) - Sistema CRM

**Versão:** 1.2
**Data da Última Revisão:** 2024-08-15
**Autor:** Equipe de Infraestrutura

## 1. Escopo do Plano

Este DRP abrange a recuperação do sistema de Gestão de Clientes (CRM) baseado em nuvem (SaaS), incluindo seu banco de dados e integrações críticas com o sistema de e-mail marketing.

## 2. Metas de Recuperação

*   **RTO (Tempo de Recuperação Objetivo):** 8 horas
*   **RPO (Ponto de Recuperação Objetivo):** 4 horas (dados perdidos aceitáveis)
*   **MAA (Tempo Máximo Aceitável de Indisponibilidade):** 16 horas

## 3. Equipe de Resposta a Desastres (ERT)

| Função                   | Nome           | Telefone Principal | Telefone Alternativo | E-mail Principal       |
| :----------------------- | :------------- | :----------------- | :------------------- | :--------------------- |
| Líder de TI              | João Silva     | (11) 98765-4321    | (11) 91234-5678      | joao.silva@empresa.com |
| Administrador de CRM     | Maria Oliveira | (11) 97654-3210    | (11) 90987-6543      | maria.o@empresa.com    |
| Líder de Vendas          | Pedro Santos   | (11) 96543-2109    | (11) 90876-5432      | pedro.s@empresa.com    |

## 4. Cenários de Desastre e Estratégias

### Cenário A: Indisponibilidade Total do Provedor de SaaS do CRM

*   **Descrição:** O provedor do CRM (ex: Salesforce, HubSpot) sofre uma interrupção regional ou global.
*   **Estratégia:**
    1.  **Confirmação:** Verificar status do provedor através de seus canais oficiais (status page, redes sociais).
    2.  **Comunicação:** Notificar a equipe de vendas e marketing sobre a indisponibilidade. Comunicar aos clientes via e-mail marketing (se o sistema de e-mail for independente) sobre os canais alternativos de contato.
    3.  **Dados:** Acessar o último backup exportado do CRM (exportação diária para bucket S3).
    4.  **Operação Temporária:** Utilizar planilhas Google Sheets para registrar novos leads e atividades de vendas críticas durante a interrupção.
    5.  **Recuperação:** Monitorar a recuperação do provedor. Após o retorno, importar dados temporários do Google Sheets para o CRM.

### Cenário B: Corrupção de Dados no CRM (Ataque Lógico/Erro Humano)

*   **Descrição:** Dados críticos de clientes são acidentalmente deletados ou corrompidos.
*   **Estratégia:**
    1.  **Isolamento:** Identificar a extensão da corrupção.
    2.  **Restauração:** Entrar em contato com o suporte do provedor SaaS para iniciar a restauração de um ponto de recuperação anterior (se disponível e dentro do RPO). Caso contrário, utilizar o backup exportado para S3.
    3.  **Validação:** Após a restauração, verificar a integridade dos dados críticos com a equipe de vendas.
    4.  **Análise Post-Mortem:** Identificar a causa raiz para evitar recorrência.

## 5. Procedimentos de Comunicação (Interna e Externa)

*   **Interna:** Grupo de WhatsApp "Crise CRM", e-mail para `ti@empresa.com` e `vendas@empresa.com`.
*   **Externa:** E-mail para clientes afetados via Mailchimp (se independente), mensagem no site institucional.

## 6. Localização de Documentos e Backups

*   **DRP Completo:** Compartilhamento de arquivos da empresa (Google Drive - pasta "DRP").
*   **Backups CRM:** Amazon S3 bucket `s3://empresa-backups-crm/` (acesso restrito).

## 7. Cronograma de Testes

*   **Tipo de Teste:** Teste de Mesa (Tabletop Exercise)
*   **Frequência:** Anual
*   **Próximo Teste:** 2025-02-01

---
```

### Relatório Pós-Incidente de DRP

```markdown
# Relatório Pós-Incidente de DRP - Falha no Sistema de E-commerce

**Número do Incidente:** DRP-ECO-20240901-001
**Data e Hora do Incidente:** 2024-09-01 10:30 BRT
**Data e Hora da Declaração do Desastre:** 2024-09-01 11:00 BRT
**Data e Hora da Recuperação Total:** 2024-09-01 15:45 BRT
**Duração Total da Indisponibilidade:** 5h 15min

## 1. Visão Geral do Incidente

Uma falha elétrica generalizada no datacenter primário (São Paulo) resultou na indisponibilidade total do sistema de e-commerce e de seu banco de dados de produtos e clientes. O DRP para o sistema de e-commerce foi ativado.

## 2. Metas vs. Resultados da Recuperação

| Métrica | Meta (DRP) | Resultado Real | Desvio |
| :------ | :--------- | :------------- | :----- |
| **RTO** | 4h         | 4h 45min       | +45min |
| **RPO** | 15min      | 10min          | -5min  |
| **MAA** | 8h         | 5h 15min       | -2h 45min |

*   **Observação:** O RTO excedeu a meta em 45 minutos devido a um problema inesperado na sincronização inicial do cache da aplicação no ambiente secundário.

## 3. Linha do Tempo da Resposta

*   **10:30:** Falha de energia detectada no datacenter primário.
*   **10:45:** Notificação de falha de todos os serviços no datacenter primário.
*   **11:00:** Líder de TI declara desastre e ativa a ERT.
*   **11:15:** Equipe de infraestrutura inicia procedimentos de failover para o site secundário (Rio de Janeiro).
*   **12:30:** Banco de dados de e-commerce recuperado e online no site secundário.
*   **13:15:** Aplicação de e-commerce online no site secundário, mas com cache de produtos lento.
*   **14:00:** Identificado e resolvido problema de sincronização de cache (reinício de serviço específico).
*   **14:30:** Validação completa da funcionalidade do e-commerce pela equipe de vendas.
*   **15:45:** Recuperação total declarada, comunicação enviada a stakeholders.

## 4. Lições Aprendidas

*   **Positivo:** A equipe de banco de dados executou o procedimento de recuperação do SGBD de forma eficiente, atingindo um RPO melhor que o esperado.
*   **Negativo:** A etapa de validação da sincronização de cache de aplicação não estava suficientemente detalhada no DRP para o ambiente secundário. Isso resultou no atraso do RTO.
*   **Melhoria:** O plano de comunicação externa foi rápido, mas a comunicação interna sobre o status do cache da aplicação poderia ter sido mais transparente entre as equipes.

## 5. Ações Corretivas e Preventivas

1.  **Atualizar DRP:** Adicionar uma etapa detalhada de validação e sincronização do cache da aplicação no procedimento de recuperação do e-commerce (Responsável: Arquiteto de Infraestrutura; Prazo: 2024-09-15).
2.  **Treinamento:** Realizar um treinamento focado em validação pós-failover para a equipe de aplicação e infraestrutura (Responsável: Líder de TI; Prazo: 2024-10-01).
3.  **Monitoramento:** Implementar métricas de monitoramento de performance do cache no ambiente secundário (Responsável: Equipe de DevOps; Prazo: 2024-10-30).
4.  **Revisão do SLA:** Avaliar a possibilidade de um SLA mais rigoroso com o provedor de datacenter para tempo de resposta em falhas elétricas (Responsável: Gerente de Contratos; Prazo: 2024-11-15).

---
```

---

## Checklist

- [X] Declaração de Desastre formalizada e comunicada à ERT.
- [X] Equipe de Resposta a Desastres (ERT) acionada e responsabilidades distribuídas.
- [X] Acesso ao ambiente de recuperação secundário estabelecido e verificado.
- [X] Procedimentos de failover e restauração para sistemas críticos iniciados.
- [X] Validação da integridade dos dados e funcionalidade das aplicações recuperadas.
- [X] Comunicação interna sobre o status da recuperação e previsão de normalização.
- [X] Comunicação externa (clientes/parceiros) sobre o incidente e planos de contingência.
- [X] Monitoramento contínuo do ambiente recuperado para anomalias.
- [X] Registro detalhado de todas as ações tomadas e tempos de resposta.
- [X] Plano de rollback ou retorno ao ambiente primário avaliado (se aplicável).

---

## Métricas de Referência

| Métrica | Benchmark (Indústria) | Meta (Empresa) |
| :------ | :-------------------- | :------------- |
| **RTO** | 4-8 horas para sistemas críticos | 4 horas |
| **RPO** | 15-60 minutos para dados críticos | 15 minutos |
| **MTTR (Mean Time To Recover)** | 4-24 horas | 6 horas |
| **MAA (Maximum Acceptable Outage)** | 8-24 horas | 12 horas |
| **Taxa de Sucesso em Testes de DRP** | >95% de sistemas recuperados | 100% |
| **Tempo de Atualização de DRP** | Anual ou a cada grande mudança | Trimestral |

---

## Erros Comuns

1.  **DRP Desatualizado**: **Problema**: O DRP é criado e nunca mais revisado. Quando um desastre ocorre, os procedimentos e contatos estão defasados, levando a atrasos críticos. **Como evitar**: Estabeleça um cronograma de revisão trimestral para o DRP, integrando-o ao processo de gerenciamento de mudanças de TI. Exemplo: Após a migração do banco de dados do ERP para uma nova versão, atualize imediatamente os scripts de failover e restauração no DRP.
2.  **Falta de Testes Regulares ou Testes Incompletos**: **Problema**: O plano existe, mas nunca é testado ou os testes são apenas "de papel". Isso gera falsa sensação de segurança. **Como evitar**: Implemente testes periódicos (anual para failover total, trimestral para recuperação de dados), incluindo simulações realistas e medição de RTO/RPO. Exemplo: Em vez de apenas ler o procedimento, execute um failover real do sistema de e-mail para o site secundário, garantindo que os usuários possam enviar e receber e-mails.
3.  **Foco Apenas em Tecnologia, Ignorando o Negócio**: **Problema**: O DRP se concentra apenas em servidores e redes, sem considerar o impacto nos processos de negócio, comunicação e pessoas. **Como evitar**: Inicie o DRP com uma Análise de Impacto no Negócio (BIA) abrangente, envolvendo líderes de negócio para definir prioridades e estratégias de comunicação de crise. Exemplo: Além de restaurar o sistema de faturamento, o DRP deve incluir um plano para informar clientes sobre atrasos e uma equipe de call center alternativa.

---

## Dicas Avançadas

1.  **Integração DRP com BCP (Business Continuity Plan)**: Garanta que o DRP técnico esteja alinhado com o BCP da organização. O DRP recupera os sistemas, o BCP garante que os processos de negócio possam continuar. Exemplo: Se o DRP recupera o sistema de vendas em 4 horas, o BCP deve detalhar como a equipe de vendas opera nessas 4 horas e como retoma as atividades após a recuperação.
2.  **Automação de Failover e Restauração**: Invista em ferramentas de orquestração e automação para reduzir o tempo de recuperação e minimizar erros manuais. Scripts bem testados podem executar sequências complexas de recuperação. Exemplo: Utilize ferramentas como Ansible ou Terraform para provisionar infraestrutura de recuperação e scripts de PowerShell para automatizar a ativação de máquinas virtuais e bancos de dados em um ambiente de nuvem secundário.
3.  **DRaaS (Disaster Recovery as a Service)**: Considere provedores de DRaaS para sistemas não críticos ou para complementar sua infraestrutura on-premise. Isso pode reduzir custos e complexidade de manutenção. Exemplo: Para o sistema de gestão de documentos (não crítico, RTO 24h), contrate um serviço de DRaaS que replique os dados para a nuvem e permita a ativação de VMs sob demanda, evitando o investimento em um site secundário físico.
4.  **Simulados de Mesa e Exercícios de Crise**: Além dos testes técnicos, realize exercícios de crise com a alta gerência e a ERT para testar a tomada de decisão, comunicação e coordenação sob pressão. Exemplo: Simule um vazamento de dados massivo e discuta as ações da equipe, as declarações à imprensa e a ativação do DRP em uma sala de reuniões, sem tocar em sistemas reais.
5.  **DRP Baseado em Nuvem (Cloud-Native DRP)**: Para ambientes nativos da nuvem, explore as capacidades de recuperação nativas do provedor (AWS, Azure, GCP). Isso inclui replicação entre regiões, snapshots automáticos e grupos de auto-scaling. Exemplo: Configurar um ambiente de produção no AWS com replicação de RDS para uma região secundária e um plano de CloudFormation para recriar a infraestrutura de aplicação completa em caso de desastre regional.
---