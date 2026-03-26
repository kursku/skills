---
name: process-documentation
description: "Process Documentation — Skill especializada para process documentation"
license: MIT
metadata:
  version: 1.0.0
  author: Cafe Code AI
  category: 11-operacoes-sistemas
  updated: 2026-03-01
risk: safe
---

# Process Documentation

Esta skill capacita o Claude a estruturar, criar e gerenciar documentação de processos operacionais padrão (SOPs) para otimizar a execução e garantir a conformidade em ambientes corporativos.

---

## Keywords

SOPs, Fluxogramas, Mapeamento de Processos, Documentação Operacional, Gestão da Qualidade, Padronização, Melhoria Contínua, Treinamento Operacional, ISO 9001, Descoberta de Processos, RACI, Gestão do Conhecimento.

---

## Quick Start

1.  Iniciar a captura de um processo observando a sequência de atividades da equipe de logística ao receber um pedido de compra, registrando cada etapa em um fluxo de trabalho básico.
2.  Modelar o processo "Onboarding de Novo Fornecedor" usando um fluxograma BPMN simples no Lucidchart, identificando swimlanes para Compras, Financeiro e Jurídico.
3.  Elaborar um rascunho de SOP para "Atendimento de Chamados Nível 1 de TI" detalhando as ações iniciais, ferramentas a serem usadas (e.g., Zendesk, TeamViewer) e critérios de escalonamento para Nível 2.
4.  Realizar uma validação inicial de um procedimento de "Backup Diário de Banco de Dados" com a equipe de DevOps, buscando clareza e precisão nas instruções de execução e recuperação.

---

## Core Workflows

### Workflow 1: Elaboração de um Procedimento Operacional Padrão (SOP) Detalhado

Este workflow descreve a criação de um SOP robusto, desde a descoberta até a implementação, garantindo que o processo seja compreendido e executado de forma consistente.

*   **Passo 1: Descoberta e Delimitação do Processo.**
    *   **Ação:** Iniciar com entrevistas estruturadas com colaboradores que executam o processo diariamente e com gestores que o supervisionam. Observar a execução "as-is" do processo. Delimitar claramente o início e o fim do processo, bem como suas interfaces com outros processos.
    *   **Exemplo:** Para o processo "Processamento de Reembolso de Despesas", iniciar com 3 entrevistas com colaboradores do departamento financeiro e 2 com gestores de área, além de acompanhar a submissão de 2 reembolsos reais no sistema. Delimitar o escopo desde a submissão da nota fiscal pelo colaborador até a efetivação do pagamento e arquivamento eletrônico.

*   **Passo 2: Mapeamento e Análise das Atividades.**
    *   **Ação:** Construir um fluxograma detalhado utilizando notação BPMN (Business Process Model and Notation) para visualizar a sequência de atividades, pontos de decisão, atores envolvidos (swimlanes) e sistemas/ferramentas utilizadas. Analisar o fluxo para identificar redundâncias, gargalos e oportunidades de melhoria.
    *   **Exemplo:** Construir um fluxograma para o processo de reembolso, identificando as tarefas como "Colaborador Submete Despesa", "Gestor Aprova Despesa", "Financeiro Audita Comprovantes", "Pagamento Efetivado". Registrar os pontos de decisão, como "Comprovante Válido?", e os sistemas envolvidos (e.g., SAP Concur, Sistema Bancário). Identificar que a etapa de "revisão manual de comprovantes" pelo gestor era um gargalo, sugerindo automatização de validação básica.

*   **Passo 3: Redação do SOP.**
    *   **Ação:** Redigir o SOP seguindo uma estrutura padrão, detalhando cada etapa do procedimento com clareza, objetividade e sem ambiguidades. Incluir seções como Objetivo, Escopo, Referências, Definições, Responsabilidades e o Procedimento passo a passo.
    *   **Exemplo:** Redigir o SOP para "Processamento de Reembolso de Despesas" (ver template abaixo). Para o "Procedimento", detalhar:
        1.  **Submissão:** O colaborador acessa o portal X, anexa a nota fiscal Y (formato PDF/JPG, limite 5MB), preenche o formulário de despesas Z, categorizando o gasto.
        2.  **Aprovação:** O gestor recebe notificação via e-mail corporativo, acessa o portal X, verifica os valores e aprova em até 24h úteis, garantindo conformidade com a política de gastos (Ex: "limite de refeição de R$ 150").
        3.  **Auditoria:** O departamento financeiro verifica a conformidade fiscal (CNPJ, data, valor) e a política interna. Se houver inconformidade (Ex: "NF duplicada"), o processo é devolvido ao gestor com feedback específico.

*   **Passo 4: Validação e Aprovação.**
    *   **Ação:** Apresentar o rascunho do SOP às partes interessadas (executores, gestores, auditores) para feedback e validação. Realizar uma simulação do processo com um caso real, se aplicável, para verificar a precisão das instruções. Incorporar sugestões e obter aprovação formal dos gestores responsáveis.
    *   **Exemplo:** Apresentar o rascunho do SOP à equipe financeira e aos gestores para feedback em uma reunião de 1 hora. Realizar uma simulação de submissão de despesa com um colaborador e acompanhamento até o pagamento. Incorporar sugestões como "adicionar exemplo de nota fiscal válida". Obter aprovação formal do Gerente Financeiro e do Diretor de Operações, registrando a versão e data de aprovação no cabeçalho do documento.

*   **Passo 5: Implementação e Treinamento.**
    *   **Ação:** Publicar o SOP em um local de fácil acesso (intranet, sistema de gestão de documentos) com controle de versão. Organizar sessões de treinamento para todos os colaboradores envolvidos na execução do processo.
    *   **Exemplo:** Publicar o SOP na intranet da empresa (e.g., SharePoint, Confluence) com controle de versão (PRO-FIN-001-V2.1). Organizar 2 sessões de treinamento online de 45 minutos para os 50 colaboradores da empresa, utilizando o SOP como material didático e realizando exercícios práticos de submissão e aprovação de despesas no sistema SAP Concur.

### Workflow 2: Otimização de Processo Existente via Documentação

Este workflow foca em como a documentação pode ser usada para identificar problemas em processos existentes e implementar melhorias.

*   **Passo 1: Identificação de Pontos Críticos.**
    *   **Ação:** Analisar dados de desempenho, feedback de clientes/equipe ou auditorias para identificar processos com baixa eficiência, alta taxa de erros ou insatisfação.
    *   **Exemplo:** Analisar o processo de "Atendimento ao Cliente via Chatbot" que apresenta alta taxa de escalonamento para atendentes humanos (45% das interações nos últimos 3 meses), resultando em Tempo Médio de Atendimento (TMA) elevado para a equipe humana (6min).

*   **Passo 2: Análise da Documentação Atual e Gap Analysis.**
    *   **Ação:** Revisar a documentação existente do processo (se houver) e compará-la com o fluxo real de trabalho e os dados coletados. Identificar lacunas na documentação ou inconsistências entre o que está documentado e o que é executado.
    *   **Exemplo:** Revisar a documentação existente do chatbot (fluxos de conversa, FAQs). Identificar que a documentação atual não cobre cenários de reclamações complexas sobre faturas e que as respostas para "alteração de plano" estão desatualizadas (referenciando um plano já descontinuado).

*   **Passo 3: Redesenho do Processo e Atualização da Documentação.**
    *   **Ação:** Com base na análise, redesenhar o processo para solucionar os pontos críticos. Atualizar ou criar nova documentação (SOPs, fluxogramas) que reflita o processo otimizado.
    *   **Exemplo:** Reestruturar os fluxos do chatbot para incluir um módulo de "Resolução de Problemas com Faturas", com perguntas guiadas para identificar o tipo de inconsistência (e.g., "valor incorreto", "cobrança duplicada"). Adicionar um passo para o chatbot tentar resolver problemas simples antes de escalar (Ex: "Você já tentou reiniciar seu modem?"). Atualizar as respostas para "alteração de plano" com as novas políticas e links diretos para o portal do cliente.

*   **Passo 4: Implementação e Monitoramento.**
    *   **Ação:** Implementar as alterações no processo e na documentação. Monitorar as métricas de desempenho para verificar a eficácia das melhorias.
    *   **Exemplo:** Implementar as novas regras e respostas no chatbot no dia 01/11. Monitorar as métricas de escalonamento e satisfação do cliente (CSAT) durante as primeiras 2 semanas. A meta é reduzir a taxa de escalonamento para 25% e o TMA da equipe humana em 1 minuto.

*   **Passo 5: Ciclo de Melhoria Contínua.**
    *   **Ação:** Estabelecer um cronograma para revisões periódicas do processo e de sua documentação. Coletar feedback contínuo para identificar novas oportunidades de otimização.
    *   **Exemplo:** Agendar revisões trimestrais para a documentação do chatbot e fluxos de atendimento. Coletar feedback contínuo dos atendentes humanos sobre os motivos de escalonamento e das novas demandas dos clientes (ex: "clientes perguntam muito sobre o novo serviço X"). Documentar todas essas alterações no histórico de revisões do SOP do chatbot (Ex: V2.3 - Adição de FAQ sobre Serviço X).

---

## Templates

### Template SOP (Procedimento Operacional Padrão)

```
Título do Documento: SOP - Processamento de Reembolso de Despesas
Código do Documento: PRO-FIN-001-V2.1
Versão: 2.1
Data de Emissão: 2024-10-26
Revisado Por: Ana Paula Silva (Gerente Financeiro)
Aprovado Por: Carlos Eduardo Santos (Diretor de Operações)

1. OBJETIVO
Padronizar o processo de solicitação, aprovação, auditoria e pagamento de reembolsos de despesas corporativas, garantindo conformidade com a política interna e agilidade no processamento.

2. ESCOPO
Este SOP aplica-se a todos os colaboradores da empresa X que incorram em despesas elegíveis para reembolso, desde a submissão da solicitação até a efetivação do pagamento pelo departamento financeiro. Exclui adiantamentos de viagem e despesas de cartão corporativo.

3. REFERÊNCIAS
3.1. Política de Reembolso de Despesas Corporativas (DOC-RH-005-V3.0)
3.2. Manual do Usuário do Sistema SAP Concur (SYS-FIN-002-V1.2)
3.3. Tabela de Limites de Despesas por Categoria (ANX-FIN-003-V1.0)

4. DEFINIÇÕES
4.1. Despesa Elegível: Gasto incorrido a serviço da empresa, conforme Política de Reembolso (Ex: alimentação em viagens a trabalho, transporte para reuniões externas, hospedagem).
4.2. Comprovante Fiscal: Documento oficial (Nota Fiscal, Recibo fiscalmente válido, Cupom Fiscal) que comprova a despesa.

5. RESPONSABILIDADES
5.1. Colaborador: Realizar a submissão de despesas de forma correta, anexando comprovantes válidos e dentro do prazo estipulado.
5.2. Gestor Imediato: Aprovar ou rejeitar as solicitações de despesas de sua equipe, verificando a conformidade com a política e a relevância do gasto.
5.3. Departamento Financeiro: Auditar as solicitações, processar o pagamento e arquivar os comprovantes eletronicamente, garantindo a integridade dos dados.

6. PROCEDIMENTO
6.1. Submissão da Despesa pelo Colaborador
    6.1.1. Acessar o sistema SAP Concur através do portal [https://concur.empresa.com.br].
    6.1.2. Criar uma nova solicitação de despesa, selecionando o tipo (Ex: "Viagem a Negócios", "Despesa Local", "Treinamento").
    6.1.3. Inserir os detalhes de cada despesa: data, valor (R$), descrição detalhada, centro de custo (Ex: "Vendas", "Marketing"), e projeto (se aplicável).
    6.1.4. Anexar o comprovante fiscal digitalizado (PDF ou JPG, tamanho máximo 5MB) para cada despesa. Certificar-se de que o comprovante está legível, contém CNPJ do emissor e data da despesa. Comprovantes ilegíveis serão rejeitados.
    6.1.5. Submeter a solicitação para aprovação do gestor imediato até o 5º dia útil do mês subsequente ao da despesa. Solicitações fora deste prazo podem ter o pagamento atrasado ou ser rejeitadas.

6.2. Aprovação pelo Gestor Imediato
    6.2.1. O gestor recebe uma notificação por e-mail (remetente: noreply@concur.com) sobre a nova solicitação.
    6.2.2. Acessar o SAP Concur, revisar os itens da solicitação e verificar a conformidade com a Política de Reembolso (DOC-RH-005-V3.0) e a Tabela de Limites (ANX-FIN-003-V1.0).
    6.2.3. Aprovar a solicitação se estiver conforme. Em caso de não conformidade, rejeitar e adicionar um comentário claro sobre o motivo da rejeição (Ex: "Comprovante ilegível, favor reenviar", "Despesa de almoço excedeu limite de R$150").
    6.2.4. O prazo para aprovação do gestor é de 2 dias úteis a partir da submissão do colaborador. Após este prazo, o sistema escalará a solicitação para o próximo nível hierárquico.

6.3. Auditoria e Pagamento pelo Departamento Financeiro
    6.3.1. Após a aprovação do gestor, o Departamento Financeiro acessa o SAP Concur para