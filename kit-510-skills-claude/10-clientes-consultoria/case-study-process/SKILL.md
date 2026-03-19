---
name: case-study-process
description: "Case Study Process — Skill especializada para case study process"
license: MIT
metadata:
  version: 1.0.0
  author: Cafe Code AI
  category: 10-clientes-consultoria
  updated: 2026-03-01
---

# Case Study Process

Esta skill capacita o Claude a orquestrar a identificação, coleta de dados, redação e publicação de histórias de sucesso de clientes, transformando-as em ativos de marketing e vendas.

---

## Keywords

Narrativa de sucesso, prova social, estudo de caso, coleta de depoimentos, impacto mensurável, storytelling corporativo, ROI do cliente, validação de solução, ativos de vendas, marketing de conteúdo B2B, jornada do cliente, retenção, engajamento do cliente.

---

## Quick Start

1.  **Filtrar Base de Clientes para Sucesso Exemplar**: Identificar clientes com projetos concluídos há 3-12 meses, NPS acima de 8, e que superaram métricas-chave do projeto em pelo menos 15%. Consultar o CRM (e.g., Salesforce) por clientes com "Status: Concluído", "Saúde do Cliente: Verde" e "MRR > R$ 15.000".
2.  **Validar Potencial Internamente**: Agendar reunião de 15 minutos com o Gerente de Projeto/CSM responsável para confirmar o impacto, a abertura do cliente e a disponibilidade de dados quantitativos. Priorizar clientes com resultados financeiros ou operacionais claros e comprováveis.
3.  **Elaborar Roteiro de Entrevista Focado em Resultados**: Criar um script com perguntas que explorem o "Antes vs. Depois" e quantifiquem o valor gerado. Exemplo: "Como o desafio X impactava sua operação antes da nossa solução? Qual foi a melhora percentual em Y após a implementação?"
4.  **Solicitar Aprovação para Entrevista**: Enviar e-mail pré-aprovado ao cliente, mencionando o desejo de celebrar seu sucesso e oferecer um material de valor mútuo. Propor 3 horários para uma conversa de 30-45 minutos e solicitar permissão para gravar.

---

## Core Workflows

### Workflow 1: Identificação e Qualificação de Clientes para Case Study

Este workflow detalha o processo de pinpointing os clientes ideais e a validação interna para iniciar a criação de um case study, garantindo alinhamento e dados robustos.

1.  **Gatilho**: Equipe de Vendas solicita material de prova social para um novo segmento, Marketing busca conteúdo para uma campanha específica, ou o Time de Sucesso do Cliente identifica um "cliente campeão".
2.  **Consulta ao CRM/Plataforma de Sucesso do Cliente**:
    *   **Critérios de Filtragem**:
        *   `Status do Projeto`: "Concluído" nos últimos 6-18 meses.
        *   `Saúde do Cliente (Health Score)`: "Verde" ou "Campeão" (e.g., 90-100 pontos em um score de 100).
        *   `NPS/CSAT`: Média acima de 8/5 nos últimos 12 meses.
        *   `Faturamento Recorrente Anual (ARR)`: Mínimo de R$ 30.000 (para relevância de mercado e valor de contrato).
        *   `Módulos/Soluções Utilizadas`: Pelo menos 2 módulos da nossa suíte para demonstrar amplitude e profundidade da parceria.
        *   `Setor de Atuação`: Alinhado com setores estratégicos atuais ou emergentes.
    *   **Exemplo Prático**: No Salesforce, filtrar por "Oportunidades Ganhas", "Data de Fechamento: nos últimos 18 meses", "Valor do Contrato > R$ 30k", e "Conta: Health Score = Verde". Exportar lista de 15-20 clientes promissores.
3.  **Análise Preliminar de Impacto Interno**:
    *   **Ação**: Revisar relatórios de pós-implementação, QBRs (Quarterly Business Reviews), notas de reuniões do CSM/Gerente de Projeto e registros de suporte.
    *   **Foco**: Identificar menções a resultados tangíveis e quantificáveis, como "redução de X% no tempo de processamento", "aumento de Y% na satisfação do usuário final", "economia de Z reais em custos operacionais", "melhora de A% na retenção de clientes do cliente".
    *   **Exemplo**: Cliente "TechInovação S.A." relatou uma redução de 25% no tempo de ciclo de desenvolvimento de software e uma economia anual de R$ 80.000 em licenças e horas extras, conforme o relatório da QBR de Q3. O CSM também mencionou um aumento de 15% na produtividade da equipe.
4.  **Briefing com Gerente de Projeto/CSM**:
    *   **Objetivo**: Confirmar a história de sucesso, a abertura do cliente para participar e a disponibilidade de dados detalhados.
    *   **Perguntas-Chave**:
        *   "O cliente TechInovação S.A. estaria aberto a participar de um case study, considerando o sucesso que obtiveram?"
        *   "Você consegue validar a redução de 25% no tempo de ciclo de desenvolvimento e a economia de R$ 80.000? Existem outros KPIs relevantes que podemos destacar, como o aumento de 15% na produtividade?"
        *   "Qual foi o principal desafio que o cliente enfrentou antes da nossa solução e como ele se sente agora?"
        *   "Quem seria o contato ideal para a entrevista (e.g., Diretor de TI, Head de Operações, CEO) e qual a melhor forma de abordá-lo?"
    *   **Saída**: Lista de 3-5 clientes qualificados com validação interna, pontos de contato recomendados e uma visão inicial dos resultados a serem explorados.

### Workflow 2: Condução da Entrevista e Estruturação da Narrativa do Case Study

Este workflow foca na extração eficiente de informações do cliente e na organização dos dados para construir uma narrativa convincente e baseada em evidências.

1.  **Gatilho**: Cliente qualificado e aprovado internamente para entrevista, com consentimento prévio para gravação.
2.  **Preparação do Roteiro de Entrevista Personalizado**:
    *   **Ação**: Basear-se no Template de Roteiro (vide seção Templates), adaptando as perguntas aos desafios específicos, soluções implementadas e resultados potenciais para o cliente em questão (conforme apurado no Workflow 1).
    *   **Foco**: Perguntas abertas que incentivem histórias e exemplos concretos, mas com follow-ups que busquem dados quantitativos e específicos.
    *   **Exemplo**: Para TechInovação S.A., incluir: "Antes da nossa plataforma, como a gestão de projetos impactava o moral da equipe e a entrega de prazos?", seguido de "Você teria alguma métrica sobre o aumento na produtividade ou redução de retrabalho após a implementação? Qual era o percentual/valor antes e depois?"
3.  **Realização da Entrevista**:
    *   **Ferramentas**: Google Meet/Zoom com gravação ativada (com consentimento explícito do cliente no início da chamada), ferramenta de transcrição (e.g., Otter.ai ou recurso nativo do Zoom).
    *   **Duração**: 30-45 minutos, pontualmente.
    *   **Técnica