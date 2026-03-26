---
name: sprint-planning
description: "Sprint Planning — Skill especializada para planejamento de sprints ágeis"
license: MIT
metadata:
  version: 1.0.0
  author: Cafe Code AI
  category: 11-operacoes-sistemas
  updated: 2026-03-01
risk: safe
---

# Sprint Planning

Esta skill habilita o Claude a conduzir e otimizar sessões de Sprint Planning, garantindo alinhamento, estimativas realistas e um Product Backlog refinado para a próxima iteração.

---

## Keywords

Sprint Planning, Product Backlog Refinement, Sprint Goal, Capacity Planning, Story Points, Velocity, DoD (Definition of Done), PBI (Product Backlog Item), Scrum Team, Commitments, Stakeholder Alignment, Iteration Planning, Sprint Backlog.

---

## Quick Start

1.  **Confirmar Preparação:** Verifique se o Product Backlog está priorizado e refinado com PBIs "Ready" para as próximas 2-3 sprints, e se a Definition of Done (DoD) foi revisada.
2.  **Calcular Capacidade:** Estime a capacidade da Development Team para a sprint atual, considerando a Velocity média e ausências planejadas (ex: 80% da média de velocity de 30 Story Points resulta em 24 Story Points de capacidade).
3.  **Definir Sprint Goal:** Facilite a criação de um Sprint Goal claro e mensurável, alinhado com o Product Goal, que a equipe possa alcançar.
4.  **Selecionar PBIs:** Guie a Development Team na seleção dos Product Backlog Items (PBIs) que contribuem para o Sprint Goal, dentro da capacidade calculada, e detalhe-os em tarefas.
5.  **Compromisso Final:** Assegure que a equipe compreenda o Sprint Backlog e se comprometa com o Sprint Goal, tornando-o visível para todos.

---

## Core Workflows

### Workflow 1: Definição do "O QUÊ" e "POR QUÊ" da Sprint

Este workflow foca na parte inicial da Sprint Planning, onde o Product Owner e a Development Team estabelecem o objetivo e selecionam os itens prioritários.

*   **Passo 1: Reafirmação do Product Goal e Visão:** O Scrum Master inicia a sessão reafirmando o Product Goal atual e a visão do produto. O Product Owner (PO) então apresenta os Product Backlog Items (PBIs) de maior prioridade, focando no valor que entregam para o próximo incremento e como se alinham ao Product Goal.
    *   **Exemplo Prático:** O Scrum Master (SM) projeta o Product Goal: "Lançar o sistema de agendamento online completo até o final do Q3." O Product Owner (PO) começa: "Para atingir esse Product Goal, nossa próxima sprint precisa focar no módulo de cadastro de clientes. Os PBIs 'Desenvolver formulário de cadastro', 'Implementar validação de CPF' e 'Persistir dados de usuário' são essenciais para iniciar esta fase."
*   **Passo 2: Definição do Sprint Goal Provisório:** A Development Team, em conjunto com o PO, discute os PBIs prioritários e propõe um objetivo coeso para a sprint. Este Sprint Goal deve ser uma declaração clara do que a equipe pretende alcançar e por que é importante.
    *   **Exemplo Prático:** Após a apresentação do PO, a equipe discute: "Se focarmos no cadastro, podemos ter um Sprint Goal como 'Habilitar o registro inicial e verificação de dados para novos clientes via formulário web', criando a base para o onboarding."
*   **Passo 3: Seleção e Entendimento dos PBIs:** O PO detalha os PBIs pré-selecionados para a sprint. A Development Team faz perguntas para esclarecer requisitos, identificar dependências e discutir o "porquê" de cada item, garantindo que todos compreendam o escopo e os critérios de aceitação.
    *   **Exemplo Prático:** Para o PBI "Implementar validação de CPF", o Desenvolvedor Carlos pergunta: "A validação de CPF usará um serviço externo? Já temos as credenciais de API e a documentação?" O PO responde: "Sim, usaremos a API da Receita Federal; as credenciais estão no LastPass e a documentação foi anexada ao PBI."

### Workflow 2: Planejamento do "COMO" e Compromisso Final

Este workflow aborda a fase de detalhamento técnico, estimativa e formalização do compromisso da Development Team.

*   **Passo 1: Detalhamento e Estimativa dos PBIs Selecionados:** Para cada PBI selecionado que contribui para o Sprint Goal, a Development Team discute as tarefas técnicas necessárias para atingir a Definition of Done (DoD). Eles então estimam o esforço usando Story Points (para complexidade relativa) ou horas (para tarefas mais granulares), considerando complexidade, incerteza e tamanho.
    *   **Exemplo Prático:** Para o PBI "Desenvolver formulário de cadastro de usuário (8 Story Points)", as tarefas detalhadas pela equipe podem ser: "Criar mockups da UI (3h)", "Implementar front-end do formulário (12h)", "Desenvolver endpoint de API para cadastro (10h)", "Escrever testes unitários e de integração (6h)".
*   **Passo 2: Verificação da Capacidade da Equipe:** O Scrum Master ou um membro da equipe compara o total de Story Points ou horas estimados para os PBIs selecionados com a capacidade calculada da Development Team para a sprint. Se o total exceder a capacidade, a equipe negocia com o PO para ajustar o escopo (remover um PBI, dividir um PBI grande, etc.).
    *   **Exemplo Prático:** A Development Team calculou uma capacidade de 28 Story Points para a sprint, baseada na Velocity média de 30 SP e uma ausência de 1 dia de Diana. A soma dos PBIs selecionados totaliza 32 Story Points. O Desenvolvedor Eduardo sugere: "Para caber na nossa capacidade, teremos que adiar o PBI 'Adicionar validação de e-mail por regex', pois os demais são críticos para o Sprint Goal." O PO concorda.
*   **Passo 3: Criação do Sprint Backlog e Definição do Sprint Goal Final:** Os PBIs e suas tarefas detalhadas formam o Sprint Backlog. O Sprint Goal é finalizado e escrito de forma clara e visível para toda a equipe. O Sprint Backlog e o Sprint Goal representam o compromisso da Development Team para a sprint.
    *   **Exemplo Prático:** O Sprint Backlog é populado com os PBIs e tarefas. O Sprint Goal final é formalizado como: "Habilitar o formulário de cadastro de usuário com validação de CPF funcionando e persistência inicial de dados no banco de dados, permitindo a criação básica de novas contas." Este goal é então afixado em um quadro físico ou digital e comunicado.

---

## Templates

### Template: Ata de Sprint Planning

```
ATA DE SPRINT PLANNING

Data: 2024-03-01
Sprint: #15 - "Início do Cadastro de Clientes"
Duração da Sprint: 11/03/2024 a 22/03/2024 (10 dias úteis)
Participantes: Ana (PO), Bruno (SM), Carlos (Dev), Diana (Dev), Eduardo (Dev)
Local: Sala de Reuniões Alpha / Google Meet

1. Revisão do Product Goal e Visão:
   - Product Goal: Lançar o sistema de agendamento online completo até o final do Q3.
   - Visão: Simplificar e agilizar o processo de agendamento de serviços para nossos usuários e parceiros.

2. Sprint Goal Definido:
   - Habilitar o formulário de cadastro de usuário com validação de CPF funcionando e persistência inicial de dados no banco de dados, permitindo a criação básica de novas contas.

3. Capacidade da Equipe:
   - Velocity Média (Últimas 3 Sprints): 30 Story Points
   - Ajustes na Capacidade: Diana estará em treinamento por 1 dia (redução de ~2 SP).
   - Capacidade para Sprint #15: 28 Story Points

4. Product Backlog Items (PBIs) Selecionados para a Sprint Backlog:
   - PBI-0056: Desenvolver tela de cadastro de usuário (8 SP)
     - Tarefas: Criar mockups UI (3h), Implementar front-end (12h), Validar campos front-end (8h), Desenvolver serviço de criação de usuário (10h), Testes unitários front-end (4h), Testes unitários back-end (5h), Teste de integração (3h).
   - PBI-0057: Implementar validação de CPF via serviço externo (5 SP)
     - Tarefas: Integrar API de validação (6h), Tratar erros da API (4h), Testes de integração da API (3h).
   - PBI-0058: Persistir dados de usuário no banco de dados (8 SP)
     - Tarefas: Modelar entidade de usuário (2h), Criar CRUD básico (10h), Escrever testes de persistência (6h).
   - PBI-0059: Criar endpoint de login de usuário (7 SP)
     - Tarefas: Desenvolver API REST de login (8h), Implementar autenticação JWT (6h), Escrever testes de segurança (4h).

5. Total de Story Points Compromissados: 28 SP

6. Riscos e Impedimentos Identificados:
   - Dependência da API de validação de CPF: Monitorar uptime do serviço externo.
   - Complexidade na implementação de autenticação JWT: Reservar tempo para pesquisa e spike, se necessário.

7. Observações Adicionais:
   - Definition of Done (DoD) revisada e confirmada.
   - Próxima reunião: Daily Scrum amanhã, 11/03, às 09:30.
```

### Template: Sprint Backlog Item Detalhado

```
SPRINT BACKLOG ITEM DETALHADO

ID do PBI: PBI-0056
Título: Desenvolver tela de cadastro de usuário
Story Points: 8
Sprint Goal Relacionado: Habilitar o formulário de cadastro de usuário com validação de CPF e persistência de dados.
Descrição: Como novo usuário, quero preencher um formulário de cadastro com meus dados pessoais (nome completo, e-mail, CPF, senha) para criar uma conta no sistema, de modo que eu possa acessar funcionalidades futuras.
Critérios de Aceitação:
- O formulário deve conter campos para Nome Completo, E-mail, CPF e Senha.
- Todos os campos obrigatórios devem ter validação de preenchimento (campo vazio).
- O e-mail deve ser validado para formato padrão (ex: `usuario@dominio.com`).
- A senha deve ter no mínimo 8 caracteres, contendo pelo menos uma letra maiúscula, uma minúscula e um número.
- Após preenchimento válido e submissão, o usuário deve ser redirecionado para uma tela de confirmação de cadastro.
- Dados do usuário devem ser persistidos no banco de dados com sucesso.

Tarefas Detalhadas (com estimativa em horas e responsável):
- [ ] Criar mockups e wireframes da UI do formulário (3h) - Responsável: Diana
- [ ] Implementar front-end da tela de cadastro (HTML/CSS/JS) (12h) - Responsável: Carlos
- [ ] Implementar validação de campos no front-end (JavaScript) (8h) - Responsável: Eduardo
- [ ] Desenvolver serviço de criação de usuário no back-end (API REST) (10h) - Responsável: Carlos
- [ ] Escrever testes unitários para o front-end (4h) - Responsável: Diana
- [ ] Escrever testes unitários para o back-end (5h) - Responsável: Eduardo
- [ ] Realizar teste de integração do fluxo completo (front-end -> back-end -> DB) (3h) - Responsável: Carlos
```

---

## Checklist

- [x] O Product Backlog está priorizado, refinado e com PBIs "Ready" para a sprint?
- [x] A Definition of Done (DoD) foi revisada e compreendida por todos os membros da Development Team?
- [x] A capacidade da Development Team para a sprint foi calculada e comunicada, considerando ausências?
- [x] O Sprint Goal foi claramente definido, é mensurável, coeso e alinhado com o Product Goal?
- [x] Todos os PBIs selecionados para a sprint contribuem diretamente para o alcance do Sprint Goal?
- [x] Os PBIs selecionados foram detalhados em tarefas granulares e estimados pela Development Team?
- [x] A Development Team se comprometeu com o Sprint Goal e com o Sprint Backlog, entendendo o que será entregue?
- [x] Riscos, impedimentos e dependências internas/externas foram identificados e planos de mitigação foram discutidos?
- [x] O Sprint Backlog (PBIs e tarefas) e o Sprint Goal estão visíveis e acessíveis para toda a equipe?
- [x] O tempo limite (time-box) da Sprint Planning foi respeitado (ex: máximo 8h para uma sprint de 4 semanas)?

---

## Métricas de Referência

| Métrica                         | Benchmark     | Meta          |
|---------------------------------|---------------|---------------|
| Velocity (Story Points/Sprint)  | 25-35 SP      | 30 SP (estável) |
| Flutuação de Velocity (%)       | < 20%         | < 10%         |
| Itens Concluídos/Comprometidos (%) | > 80%         | > 95%         |
| Tempo médio de Refinamento (h/sprint) | 4-6h (para 2 semanas) | 4h (para 2 semanas) |
| PBIs "Spill-over" (não concluídos) | < 10%         | < 5%          |
| Satisfação da Equipe com Planning (1-5) | 3.5           | 4.0           |

---

## Erros Comuns

1.  **Excesso de Compromisso (Overcommitment)**: A Development Team seleciona mais PBIs do que sua capacidade real, movida por otimismo ou pressão externa, resultando em PBIs inacabados e desmotivação.
    *   **Como evitar:** Baseie a capacidade da equipe na Velocity média das últimas 3-5 sprints, descontando ausências planejadas (feriados, treinamentos). Use técnicas como Planning Poker para estimativas e respeite o julgamento da equipe sobre sua capacidade. Exemplo: Se a Velocity média é 30 Story Points, resistir à tentação de aceitar 40 SP sem uma justificativa robusta ou um aumento real de capacidade.
2.  **Sprint Goal Vago ou Inexistente**: A Sprint Planning termina sem um objetivo claro e unificador, transformando a sprint em uma coleção de tarefas desconexas. Isso dificulta a priorização durante a sprint e o alinhamento com o Product Goal.
    *   **Como evitar:** O Scrum Master deve facilitar a definição de um único Sprint Goal, conciso e mensurável, no início da planning. O goal deve ser um compromisso que a equipe pode alcançar. Exemplo: Em vez de "Fazer algumas melhorias", defina "Habilitar a busca por produtos com filtros de preço e categoria no e-commerce", garantindo um foco claro.
3.  **Falta de Refinamento Pré-Planning**: O Product Backlog chega à Sprint Planning com PBIs mal definidos, sem estimativas, ou com muitas dúvidas e dependências não resolvidas, consumindo tempo excessivo da planning com esclarecimentos.
    *   **Como evitar:** Dedique tempo contínuo ao Product Backlog Refinement (ex: 10% da capacidade da equipe semanalmente). O Product Owner deve garantir que os PBIs de alta prioridade estejam "Ready" (prontos para serem puxados) antes da Planning. Um PBI "Ready" tem descrição clara, critérios de aceitação, estimativa inicial e dependências identificadas.
4.  **PO Ausente ou Passivo**: O Product Owner não participa ativamente ou não está disponível para esclarecer dúvidas sobre os PBIs, levando a suposições incorretas e retrabalho.
    *   **Como evitar:** O PO é uma presença mandatória na Sprint Planning. Ele deve estar preparado para apresentar os PBIs, responder a perguntas e colaborar na definição do Sprint Goal. Exemplo: O PO deve ter revisado os PBIs e antecipado perguntas comuns da Development Team.

---

## Dicas Avançadas

1.  **"What if" Scenarios na Capacidade:** Durante a discussão e seleção dos PBIs, explore cenários de "e se" para gerenciar riscos de forma proativa. Exemplo: "E se a integração com a API externa (PBI-0057) atrasar ou falhar? Temos um plano de contingência ou um PBI de menor prioridade que podemos substituir?" Isso permite à equipe criar um plano mais robusto e flexível.
2.  **Time-Boxing Rigoroso e Fases Claras:** Divida a Sprint Planning em fases com time-boxes explícitos para manter o foco e otimizar o tempo. Por exemplo, 1 hora para definição do Sprint Goal e seleção inicial de PBIs, 2 horas para detalhamento técnico e estimativas. Exemplo: O Scrum Master anuncia: "Nos próximos 60 minutos, vamos focar exclusivamente na definição do Sprint Goal e na seleção dos PBIs que são essenciais para alcançá-lo. As tarefas e estimativas virão na próxima fase."
3.  **Definição de "Ready" (Definition of Ready - DoR):** Além da Definition of Done (DoD), estabeleça uma Definition of Ready (DoR) clara para os PBIs que podem ser levados para a Sprint Planning. Isso garante que os itens estejam suficientemente maduros. Exemplo de DoR: "Um PBI é 'Ready' se: tem descrição clara, critérios de aceitação definidos, foi estimado pela equipe, dependências externas identificadas e mitigadas, e não excede X Story Points."
4.  **Análise de Tendências de Velocity em vez de Ponto Fixo:** Em vez de usar a Velocity como um número estático, analise sua tendência ao longo do tempo. Uma Velocity em queda pode indicar problemas subjacentes na equipe (excesso de débitos técnicos, desmotivação, interrupções), que precisam ser endereçados, enquanto uma em ascensão pode permitir um compromisso ligeiramente maior. Exemplo: Se a Velocity caiu de 30 para 20 SP nas últimas 3 sprints, a equipe deve discutir as causas na Retrospective antes de se comprometer com 30 SP novamente.
5.  **Simulação de Tarefas Críticas:** Para PBIs de alta complexidade ou risco, a equipe pode realizar uma "simulação" mental ou um mini-spike durante a Planning. Em vez de apenas estimar, eles discutem os passos técnicos chave em maior profundidade, identificando potenciais gargalos ou soluções. Exemplo: Para um PBI de integração com um novo sistema, a equipe pode desenhar brevemente a arquitetura da solução no quadro branco, antes de detalhar as tarefas.