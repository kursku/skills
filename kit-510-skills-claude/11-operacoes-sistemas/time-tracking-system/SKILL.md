---
name: time-tracking-system
description: "Time Tracking System — Skill especializada para time tracking system"
license: MIT
metadata:
  version: 1.0.0
  author: Cafe Code AI
  category: 11-operacoes-sistemas
  updated: 2026-03-01
---

# Time Tracking System

Esta skill capacita o Claude a projetar, implementar e otimizar sistemas de controle de tempo para equipes e projetos, garantindo precisão na alocação de recursos e conformidade operacional.

---

## Keywords

Gestão de tempo, timesheet, controle de horas, produtividade da equipe, alocação de recursos, faturamento por hora, conformidade trabalhista, relatórios de tempo, automação de registro, monitoramento de projetos.

---

## Quick Start

1.  **Definir Estrutura de Projetos e Tarefas:** Configure no sistema de time tracking as categorias de projetos (ex: "Desenvolvimento", "Consultoria", "Suporte") e as tarefas associadas (ex: "Análise", "Codificação", "Reunião de Cliente").
2.  **Cadastrar Colaboradores e Taxas:** Inclua todos os membros da equipe, atribuindo-lhes funções específicas e, se aplicável, suas taxas horárias para faturamento interno ou externo.
3.  **Instruir sobre Registro Diário:** Oriente a equipe a registrar o tempo em suas respectivas tarefas e projetos de forma diária e granular, preferencialmente ao concluir cada bloco de trabalho.
4.  **Configurar Ciclo de Aprovação Semanal:** Estabeleça um fluxo onde os timesheets são submetidos pelos colaboradores às sextas-feiras e aprovados pelos gerentes até a segunda-feira seguinte.
5.  **Gerar Relatório de Horas Faturáveis:** Execute um relatório semanal consolidado para identificar as horas faturáveis por cliente e projeto, comparando-as com as estimativas iniciais.

---

## Core Workflows

### Workflow 1: Implementação e Configuração Inicial de um Sistema de Time Tracking

Este workflow detalha a configuração de um novo sistema de controle de tempo, desde a seleção da ferramenta até a definição de políticas de uso, garantindo que a base esteja sólida para a operação diária.

1.  **Seleção da Ferramenta Adequada:**
    *   **Passo:** Avaliar as necessidades da organização em termos de funcionalidades (integração com ERP, faturamento, gestão de projetos), escalabilidade e custo.
    *   **Exemplo:** Para uma agência de marketing que fatura por hora, "Harvest" ou "Toggl Track" são boas opções pela facilidade de uso e relatórios de faturamento. Para empresas com projetos complexos e desenvolvimento de software, "Jira Tempo" ou "ClickUp" oferecem integração mais profunda.
    *   **Ação Claude:** "Com base na sua descrição de equipe de 15 desenvolvedores e 5 designers que precisam integrar tempo com Jira e faturamento, recomendo o Jira Tempo. Ele permite vincular horas diretamente às issues do Jira e tem módulos de faturamento robustos."

2.  **Estruturação de Projetos e Tarefas:**
    *   **Passo:** Criar uma taxonomia clara para projetos, fases e tarefas, garantindo que o registro de tempo seja granular o suficiente para análises e faturamento, mas não excessivamente complexo.
    *   **Exemplo:**
        *   **Projeto:** "Desenvolvimento App Mobile v2.0"
        *   **Fase:** "Design UI/UX", "Desenvolvimento Frontend", "Desenvolvimento Backend", "QA e Testes"
        *   **Tarefas (sob Design UI/UX):** "Criação de Wireframes", "Prototipagem de Alta Fidelidade", "Revisão com Cliente A"
    *   **Ação Claude:** "Para o Projeto 'Migração de CRM Legado', sugiro a seguinte estrutura de tarefas: 'Análise de Requisitos (20h)', 'Modelagem de Dados (30h)', 'Desenvolvimento de APIs (80h)', 'Migração de Dados Históricos (40h)', 'Testes de Integração (30h)', 'Treinamento de Usuários (15h)'."

3.  **Configuração de Usuários e Permissões:**
    *   **Passo:** Cadastrar todos os colaboradores, atribuindo-lhes funções (Colaborador, Gerente de Projeto, Administrador) e definindo as taxas horárias padrão ou específicas.
    *   **Exemplo:** João Silva (Desenvolvedor Sênior, R$150/hora), Maria Souza (Designer Pleno, R$90/hora), Carlos Santos (Gerente de Projeto, R$180/hora). Gerentes podem aprovar timesheets, colaboradores apenas registrar.
    *   **Ação Claude:** "Configure um perfil 'Desenvolvedor' com permissão para registrar tempo em qualquer projeto e 'Gerente de Projeto' com permissão para aprovar timesheets de sua equipe e visualizar relatórios de custo."

4.  **Definição de Regras de Arredondamento e Faturamento:**
    *   **Passo:** Estabelecer políticas de arredondamento de tempo (ex: para os 5 ou 15 minutos mais próximos) e regras de faturamento (ex: tempo mínimo faturável, horas extras).
    *   **Exemplo:** Todas as entradas de tempo são arredondadas para o quarto de hora mais próximo. Registros abaixo de 15 minutos para tarefas específicas de suporte são agrupados e faturados como um bloco mínimo de 30 minutos.
    *   **Ação Claude:** "Implemente arredondamento de tempo para os 10 minutos mais próximos. Para chamados de suporte técnico, qualquer tempo registrado abaixo de 10 minutos deve ser automaticamente arredondado para 10 minutos para fins de faturamento."

### Workflow 2: Gestão Diária de Horas e Aprovação de Timesheets

Este workflow abrange as operações diárias de registro de tempo pelos colaboradores e o processo de revisão e aprovação pelos gerentes, garantindo a precisão e a tempestividade dos dados.

1.  **Registro Diário de Atividades:**
    *   **Passo:** Os colaboradores registram suas horas trabalhadas nas tarefas e projetos correspondentes, utilizando a ferramenta de time tracking.
    *   **Exemplo:**
        *   **Colaborador:** Ana Paula (Desenvolvedora)
        *   **Dia:** 2024-10-27
        *   **Entradas:**
            *   09:00 - 12:00: Projeto "Lançamento CRM", Tarefa "Codificação Módulo de Relatórios" (3h)
            *   13:00 - 15:30: Projeto "Manutenção Sistema Legado", Tarefa "Correção Bug #1234" (2.5h)
            *   15:30 - 17:00: Projeto "Treinamento Interno", Tarefa "Participação em Workshop Python" (1.5h)
    *   **Ação Claude:** "Oriente o colaborador a detalhar as descrições de tempo, por exemplo, 'Codificação Módulo de Relatórios - Implementação de filtros de data' ao invés de apenas 'Codificação'."

2.  **Submissão de Timesheets:**
    *   **Passo:** Ao final da semana, os colaboradores revisam e submetem seus timesheets para aprovação.
    *   **Exemplo:** Na sexta-feira, Ana Paula verifica seu timesheet semanal no Harvest, corrige qualquer erro e clica em "Submit Week for Approval".
    *   **Ação Claude:** "Configure lembretes automáticos no sistema para todos os colaboradores que não submeteram seus timesheets até sexta-feira às 17h."

3.  **Revisão e Aprovação por Gerentes:**
    *   **Passo:** Gerentes de projeto ou líderes de equipe revisam os timesheets de seus subordinados, verificando a precisão, a alocação de tempo e a conformidade com as políticas.
    *   **Exemplo:** Carlos Santos (Gerente de Projeto) recebe uma notificação de timesheet pendente de Ana Paula. Ele analisa as entradas, compara com o progresso das tarefas e as estimativas. Ele pode aprovar, rejeitar com feedback ou solicitar ajustes. Se Ana registrou 10h em uma tarefa estimada para 2h, Carlos pede uma justificativa.
    *   **Ação Claude:** "Ao detectar uma discrepância de 20% ou mais entre o tempo registrado e o estimado para uma tarefa, o sistema deve automaticamente sinalizar o timesheet para revisão manual com um campo obrigatório para justificativa."

4.  **Correções e Rejeições:**
    *   **Passo:** Em caso de rejeição, o gerente fornece feedback detalhado e o colaborador ajusta o timesheet e o ressubmete.
    *   **Exemplo:** Carlos rejeita o timesheet de Ana com o comentário: "Por favor, detalhe mais as horas gastas no bug #1234, especificando as sub-tarefas de análise e correção." Ana ajusta e ressubmete.
    *   **Ação Claude:** "Crie um template de e-mail automático para rejeição de timesheet que inclua o nome do colaborador, a semana em questão e um campo para o gerente preencher com o motivo da rejeição e as ações esperadas."

---

## Templates

### Estrutura de Projeto e Tarefas para Time Tracking

```
Projeto: [Nome do Projeto]
  Código Interno: [PROJ-XXX]
  Cliente: [Nome do Cliente / Interno]
  Gerente de Projeto: [Nome do Gerente]
  Data Início: [DD/MM/AAAA]
  Data Fim Prevista: [DD/MM/AAAA]
  Budget Total (Horas): [XXXX]
  Budget Total (Valor): [R$ XXXXX.XX]

  Fases do Projeto:
  - Fase: [Nome da Fase, ex: Planejamento, Desenvolvimento, Testes, Implementação]
    Código da Fase: [FAS-YYY]
    Responsável: [Nome do Líder da Fase]
    Horas Estimadas: [HHH]
    Tarefas (dentro da Fase):
    - Tarefa: [Nome da Tarefa, ex: Análise de Requisitos, Codificação Módulo X, Reunião de Kick-off]
      Código da Tarefa: [TAR-ZZZ]
      Tipo de Atividade: [Desenvolvimento, Reunião, Documentação, Suporte, Administrativo]
      Horas Estimadas: [HH]
      Prioridade: [Alta, Média, Baixa]
      Observações: [Breve descrição ou link para documentação]
    - Tarefa: [Nome da Tarefa]
      ...
  - Fase: [Próxima Fase]
    ...
```

### Relatório Semanal de Horas Trabalhadas (Gerencial)

```
RELATÓRIO SEMANAL DE HORAS TRABALHADAS

Período: [DD/MM/AAAA] a [DD/MM/AAAA]
Gerente Responsável: [Nome do Gerente]
Data de Geração: [DD/MM/AAAA HH:MM]

| Colaborador     | Projeto                     | Tarefa                         | Horas Registradas | Status Timesheet | Horas Faturáveis | Horas Não Faturáveis | % Utilização |
|-----------------|-----------------------------|--------------------------------|-------------------|------------------|------------------|----------------------|--------------|
| Ana Paula (Dev) | Lançamento CRM              | Codificação Módulo Relatórios  | 18.00             | Aprovado         | 18.00            | 0.00                 | 90%          |
| Ana Paula (Dev) | Manutenção Sistema Legado   | Correção Bug #1234             | 12.00             | Aprovado         | 12.00            | 0.00                 | -            |
| João Silva (Dev)| Lançamento CRM              | Testes de Integração Backend   | 20.00             | Aprovado         | 20.00            | 0.00                 | 80%          |
| Maria Souza (Dsgn)| Website Corporativo v3.0  | Prototipagem UI/UX             | 25.00             | Aprovado         | 25.00            | 0.00                 | 100%         |
| Equipe Total    |                             |                                | 75.00             |                  | 75.00            | 0.00                 | 92%          |

Observações:
- Verificar justificativas para horas não faturáveis.
- Acompanhar projetos com desvio significativo de horas em relação ao estimado.
```

---

## Checklist

- [x] Definir uma política clara de registro de tempo para toda a organização.
- [x] Escolher e implementar uma ferramenta de time tracking que se integre aos sistemas existentes (ERP, gestão de projetos).
- [x] Cadastrar todos os colaboradores, suas funções e taxas horárias no sistema.
- [x] Criar uma estrutura padronizada de projetos, fases e tarefas para toda a organização.
- [x] Configurar regras de arredondamento de tempo e políticas de horas extras.
- [x] Estabelecer um ciclo de submissão e aprovação de timesheets (ex: semanal, quinzenal).
- [x] Treinar todos os colaboradores sobre o uso correto da ferramenta e a importância do registro preciso.
- [x] Configurar alertas e lembretes para timesheets não enviados ou pendentes de aprovação.
- [x] Definir um processo para auditoria e correção de discrepâncias nos registros de tempo.
- [x] Gerar relatórios periódicos de horas trabalhadas, faturáveis e não faturáveis para análise de desempenho e custo.

---

## Métricas de Referência

| Métrica                      | Benchmark da Indústria | Meta Interna |
|------------------------------|------------------------|--------------|
| Taxa de Conformidade Timesheet | > 95%                  | 98%          |
| Tempo Médio Aprovação Timesheet | < 24 horas             | < 12 horas   |
| % Horas Faturáveis (Serviços) | > 70%                  | 75%          |
| Desvio Tempo Estimado vs. Real | < 20%                  | < 10%        |
| Custo Médio por Hora (Equipe) | R$ 120 - R$ 250/hora   | R$ 150/hora  |
| Utilização da Equipe          | 80-90%                 | 85%          |

---

## Erros Comuns

1.  **Falta de Granularidade no Registro**: Colaboradores registram "Trabalho Geral no Projeto X" por 8 horas, dificultando a análise de produtividade e faturamento detalhado.
    *   **Como evitar**: Implementar uma taxonomia de tarefas clara e obrigar o preenchimento de subtarefas ou descrições detalhadas. Exemplo: Em vez de "Reunião Cliente", use "Reunião de Alinhamento - Projeto Alpha - Discussão de Requisitos".
2.  **Registro Atrasado e Impreciso**: A equipe registra as horas de toda a semana na sexta-feira, resultando em estimativas imprecisas e esquecimentos.
    *   **Como evitar**: Reforçar a importância do registro diário ou em tempo real. Utilizar lembretes automáticos diários (ex: notificação push às 17h) e integração com calendários para pré-preencher eventos.
3.  **Não Vincular Tempo a Entregáveis ou Metas**: O time tracking se torna uma obrigação burocrática sem valor estratégico, pois não há conexão com o progresso real do projeto ou os objetivos de negócio.
    *   **Como evitar**: Integrar a ferramenta de time tracking com o sistema de gestão de projetos (Jira, Asana). Isso permite que o tempo seja registrado diretamente em tarefas específicas com estimativas e progresso, mostrando o impacto do tempo na entrega de valor.
4.  **Rejeição de Timesheets sem Feedback Construtivo**: Gerentes rejeitam timesheets sem fornecer um motivo claro ou orientação para correção, gerando frustração e repetição de erros.
    *   **Como evitar**: Treinar gerentes para fornecer feedback específico e acionável. Exemplo: "Rejeitado. Por favor, detalhe as 4 horas em 'Suporte Geral' especificando quais chamados foram atendidos e o tempo dedicado a cada um."

---

## Dicas Avançadas

1.  **Automação Inteligente de Registro**: Implementar integrações com ferramentas de produtividade (Google Calendar, Outlook Calendar, Slack) para automaticamente sugerir entradas de tempo baseadas em reuniões, e-mails ou status de trabalho. Por exemplo, o sistema pode pré-preencher 1 hora para "Reunião de Sprint Planning" se o evento estiver no calendário.
2.  **Análise Preditiva de Esforço**: Utilizar dados históricos de time tracking para refinar estimativas de projetos futuros. Analisar o desvio entre tempo estimado e real em tarefas semelhantes para ajustar orçamentos e cronogramas de forma mais precisa, prevendo gargalos.
3.  **Gamificação para Engajamento**: Criar um sistema de pontos ou emblemas para incentivar o registro pontual e preciso. Por exemplo, "Mestre do Tempo" para quem submete o timesheet no prazo por 12 semanas consecutivas, ou "Detalhista Proativo" para quem adiciona descrições ricas.
4.  **Integração com Business Intelligence (BI)**: Exportar dados de time tracking para plataformas de BI (Power BI, Tableau) para criar dashboards personalizados. Isso permite análises multidimensionais sobre rentabilidade por cliente, desempenho por colaborador, e alocação de recursos em tempo real, além de identificar tendências de custo e produtividade.
5.  **Configuração de Alertas de Desvio em Tempo Real**: Configurar o sistema para enviar alertas automáticos aos gerentes quando um colaborador excede 80% do tempo estimado para uma tarefa, permitindo intervenção precoce para reavaliar o escopo ou realocar recursos antes que o projeto saia do orçamento.