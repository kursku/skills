---
name: automation-audit
description: "Automation Audit — Skill especializada para auditoria de automação"
license: MIT
metadata:
  version: 1.0.0
  author: Cafe Code AI
  category: 11-operacoes-sistemas
  updated: 2026-03-01
---

# Automation Audit

Esta skill capacita o Claude a conduzir auditorias de automação exaustivas, identificando ineficiências, riscos, falhas de conformidade e oportunidades de otimização em processos automatizados e suas plataformas subjacentes.

---

## Keywords

*   RPA Audit
*   BPMN Compliance
*   SLA Automação
*   Governança de Bots
*   Otimização de Processos
*   Risco Operacional Automação
*   Conformidade Regulatória (LGPD, SOX)
*   Desempenho de Bots
*   ROI Automação
*   Controles Internos Automação
*   Segurança Cibernética Automação
*   Análise de Exceções Automatizadas

---

## Quick Start

1.  **Mapear o Escopo Inicial da Automação**: Identificar os processos automatizados críticos a serem auditados (ex: "Processamento de Faturas", "Onboarding de Clientes", "Conciliação Financeira") e as plataformas (ex: UiPath Orchestrator, Blue Prism Control Room, Power Automate).
2.  **Coletar Documentação Essencial**: Reunir SOPs (Standard Operating Procedures), SDDs (Solution Design Documents), PDDs (Process Design Documents), logs de execução dos bots, matrizes de acesso e planos de contingência dos processos selecionados.
3.  **Agendar Entrevistas Chave**: Programar sessões com Product Owners da automação, desenvolvedores de bots, equipes de suporte de TI e usuários de negócio impactados para compreender o ciclo de vida, problemas e expectativas.
4.  **Preparar Ambiente de Análise de Dados**: Configurar acesso seguro aos sistemas de logs, bases de dados de desempenho e ferramentas de monitoramento para extração e análise de dados de execução dos bots.
5.  **Definir Critérios de Avaliação**: Estabelecer os benchmarks de desempenho (ex: taxa de sucesso de 98%), conformidade (ex: aderência à LGPD) e segurança (ex: uso de credenciais seguras) que serão aplicados durante a auditoria.

---

## Core Workflows

### Workflow 1: Auditoria de Desempenho e Eficiência de Automações RPA

Este workflow foca na avaliação da performance operacional de bots existentes, identificando gargalos, falhas e oportunidades de otimização para maximizar o ROI e a produtividade.

**Passos Detalhados:**

1.  **Coleta e Consolidação de Logs de Execução**:
    *   **Ação**: Acessar as plataformas de orquestração RPA (ex: UiPath Orchestrator, Blue Prism Control Room) ou sistemas de log centralizados (ex: Splunk, ELK Stack) para extrair logs de execução dos últimos 90 dias para os bots de "Processamento de Pedidos de Compra" e "Conciliação Bancária".
    *   **Exemplo Concreto**: Extrair dados de `Robot Logs` do Orchestrator, filtrando por mensagens de erro, tempo de execução e status final da transação para o bot `Bot_ProcessaPedido_v2.1`.
    *   **Dados a Coletar**: `Timestamp`, `RobotName`, `ProcessName`, `TransactionID`, `Status` (Success/Failed), `ErrorMessage`, `ExecutionDuration` (segundos).

2.  **Análise de Taxa de Exceções e Causas Raiz**:
    *   **Ação**: Calcular a taxa de exceções (transações falhas / total de transações) e categorizar os tipos de erros mais frequentes (ex: "Sistema indisponível", "Dados inválidos", "Elemento UI não encontrado").
    *   **Exemplo Concreto**: Para o `Bot_ProcessaPedido_v2.1`, identificar que 12% das transações falharam no último mês. Desses, 70% foram devido a "Elemento UI não encontrado" na tela de entrada do sistema ERP, sugerindo uma instabilidade no ambiente ou design frágil do bot.
    *   **Ferramentas**: Planilhas (Excel, Google Sheets), ferramentas de BI (Power BI, Tableau) para visualização e drill-down.

3.  **Avaliação do Tempo de Ciclo e Identificação de Gargalos**:
    *   **Ação**: Analisar o `ExecutionDuration` médio por transação para identificar etapas do processo que consomem mais tempo e comparar com o tempo esperado ou manual.
    *   **Exemplo Concreto**: O `Bot_ConciliaBancaria_v1.0` leva em média 180 segundos por conciliação, enquanto a análise revela que a etapa de "Download de Extrato Bancário" consome 90 segundos devido à lentidão do site do banco. Isso aponta um gargalo externo ou uma oportunidade de otimização na forma como o download é realizado (ex: API em vez de UI).

4.  **Sugestão de Otimizações e Ações Corretivas**:
    *   **Ação**: Com base nas análises, propor melhorias no design do bot, na infraestrutura, nos processos upstream ou nos sistemas integrados.
    *   **Exemplo Concreto**: Para o `Bot_ProcessaPedido_v2.1`, recomendar refatorar os seletores de UI para serem mais robustos ou implementar um mecanismo de retry com atraso. Para o `Bot_ConciliaBancaria_v1.0`, sugerir explorar uma integração via API com o banco para o download de extratos, reduzindo o tempo de execução em 50%.

### Workflow 2: Auditoria de Conformidade e Governança de Automações

Este workflow verifica se as automações estão em conformidade com políticas internas, regulamentações externas e melhores práticas de segurança e governança, mitigando riscos operacionais e de auditoria.

**Passos Detalhados:**

1.  **Verificação da Documentação de Governança e Operação**:
    *   **Ação**: Revisar a existência e atualização de documentos críticos como SOPs de automação, matrizes RACI para manutenção de bots, políticas de controle de acesso para credenciais de bots e planos de continuidade de negócios/DRP específicos para automações.
    *   **Exemplo Concreto**: Para o processo "Gerenciamento de Contas de Usuários", verificar se o `SOP_Bot_ProvisionaAcesso_v1.2` está assinado e atualizado nos últimos 6 meses e se ele descreve claramente os gatilhos, exceções e o processo de escalonamento. Constatar que a versão em uso é a 1.0, desatualizada em relação às novas políticas de LGPD.

2.  **Análise de Controles de Acesso e Segregação de Funções (SoD)**:
    *   **Ação**: Avaliar se as credenciais utilizadas pelos bots seguem o princípio do menor privilégio e se a criação, modificação e execução de bots possuem segregação de funções adequada entre desenvolvedores, operadores e analistas de negócio.
    *   **Exemplo Concreto**: Identificar que o `Bot_AprovaPagamento_v3.0` utiliza uma credencial com privilégios de administrador de sistema no ERP, quando apenas acesso a "Contas a Pagar" seria suficiente. Além disso, o mesmo desenvolvedor que criou o bot também tem permissão para implantá-lo em produção, violando o princípio de SoD.

3.  **Aderência a Normas Regulatórias (LGPD, SOX, etc.)**:
    *   **Ação**: Confirmar que os dados sensíveis processados ou armazenados pelas automações estão em conformidade com as leis aplicáveis (ex: LGPD para dados pessoais, SOX para controles financeiros). Isso inclui verificação de anonimização, criptografia e políticas de retenção de dados nos logs e sistemas intermediários.
    *   **Exemplo Con