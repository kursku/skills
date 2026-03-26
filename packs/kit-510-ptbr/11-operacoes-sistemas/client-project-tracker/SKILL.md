---
name: client-project-tracker
description: "Client Project Tracker — Skill especializada para gerenciar e monitorar projetos de clientes"
license: MIT
metadata:
  version: 1.0.0
  author: Cafe Code AI
  category: 11-operacoes-sistemas
  updated: 2026-03-01
risk: caution
---

# Client Project Tracker

Esta skill capacita o Claude a atuar como um gerente de projetos para clientes, otimizando o monitoramento, a comunicação e a entrega de marcos, garantindo visibilidade total e alinhamento contínuo desde o kick-off até a entrega final.

---

## Keywords

Gestão de Projetos, Monitoramento de Clientes, Relatórios de Progresso, Marcos de Projeto, KPIs de Cliente, Comunicação com Stakeholders, Alocação de Recursos, Gestão de Expectativas, Cronograma de Projeto, Rastreamento de Entregas, Gerenciamento de Riscos, Feedback do Cliente, SOPs de Projeto, Change Request.

---

## Quick Start

1.  **Inicialize o Projeto**: Preencha o template "Ficha de Projeto Cliente" com os dados iniciais do novo projeto.
2.  **Configure o Cronograma**: Popule a ferramenta de gestão de projetos (Jira, Asana) com as tarefas e marcos definidos no escopo.
3.  **Estabeleça a Comunicação**: Agende a reunião de kick-off com o cliente e defina a frequência e o formato dos relatórios de progresso semanais.
4.  **Monitore a Alocação**: Verifique semanalmente o registro de horas da equipe no projeto para identificar desvios.
5.  **Prepare o Primeiro Relatório**: Utilize o template "Relatório Semanal de Progresso" para comunicar o status ao cliente.

---

## Core Workflows

### Workflow 1: Monitoramento Semanal de Progresso do Projeto Cliente

Este workflow detalha o processo para acompanhar e reportar o status de um projeto de cliente regularmente, garantindo transparência e detecção precoce de desvios.

1.  **Coletar Atualizações de Status da Equipe (Segunda-feira, 9h00)**:
    *   **Ação**: Realizar stand-up meeting diário ou coletar atualizações via ferramenta de gestão de projetos (e.g., Slack, Jira).
    *   **Exemplo**: A equipe de desenvolvimento reporta que o "Módulo de Autenticação de Usuário" está 80% concluído e o "Módulo de Pagamentos" iniciou, mas há uma dependência de API externa.
2.  **Atualizar Painel de Controle do Projeto (Segunda-feira, 11h00)**:
    *   **Ação**: Inserir o progresso das tarefas e marcos na ferramenta de rastreamento (e.g., Asana, Trello, Jira).
    *   **Exemplo**: No Jira, o status da tarefa "Desenvolver API de Autenticação" muda para "Em Revisão" e a tarefa "Integrar Gateway de Pagamento" para "Em Andamento". O percentual de conclusão geral do projeto é atualizado automaticamente.
3.  **Analisar Desvios de Cronograma e Orçamento (Terça-feira, 14h00)**:
    *   **Ação**: Comparar o progresso atual com o planejado, identificando tarefas atrasadas ou estouros de horas.
    *   **Exemplo**: O "Módulo de Pagamentos" está projetado para atrasar em 3 dias devido à dependência externa. A equipe já utilizou 25% do orçamento total, mas apenas 20% do escopo foi entregue, indicando um possível desvio.
4.  **Preparar Relatório de Progresso para o Cliente (Quarta-feira, 10h00)**:
    *   **Ação**: Compilar as informações relevantes (marcos atingidos, atividades da semana, próximas atividades, desafios) no template "Relatório Semanal de Progresso".
    *   **Exemplo**: Gerar um relatório destacando que o "Marco 1: Prototipagem UX/UI Aprovada" foi concluído na semana anterior, e que o desafio principal é a espera da documentação da API de pagamento do cliente.
5.  **Enviar Relatório e Agendar Feedback (Quarta-feira, 16h00)**:
    *   **Ação**: Enviar o relatório ao contato do cliente e sugerir um horário para a reunião de alinhamento ou para coletar feedback.
    *   **Exemplo**: Enviar e-mail com o relatório anexo e a frase: "Gostaríamos de agendar uma breve call de 15 minutos na quinta-feira às 10h para discutir o progresso e o desafio com a API de pagamento. Por favor, confirme sua disponibilidade."

### Workflow 2: Gestão de Solicitações de Mudança de Escopo (Change Request)

Este workflow descreve o processo estruturado para lidar com solicitações de mudança de escopo do cliente, minimizando impactos negativos e garantindo a aprovação formal.

1.  **Registrar Solicitação de Mudança (Imediatamente ao receber)**:
    *   **Ação**: Documentar a solicitação do cliente em um registro formal de "Change Request" ou na ferramenta de gestão de projetos.
    *   **Exemplo**: O cliente envia um e-mail solicitando a "Adição de um painel de relatórios gerenciais personalizáveis para o admin". Registrar isso como CR-005: "Painel de Relatórios Personalizados".
2.  **Avaliar Impacto (dentro de 24-48h)**:
    *   **Ação**: A equipe técnica e de projeto avalia o impacto da mudança no cronograma, orçamento, recursos e qualidade do projeto.
    *   **Exemplo**: A equipe estima que a funcionalidade de "Relatórios Personalizados" exigirá 80 horas de desenvolvimento adicionais, resultando em um acréscimo de R$ 8.000,00 e um atraso de 10 dias na entrega final do projeto.
3.  **Formalizar Proposta de Mudança para o Cliente (dentro de 72h)**:
    *   **Ação**: Preparar um documento formal (ou usar o template "Proposta de Mudança de Escopo") detalhando a solicitação, os impactos e as opções.
    *   **Exemplo**: Apresentar ao cliente a opção de incluir a funcionalidade com o custo e prazo adicionais, ou a opção de adiar outras funcionalidades menos críticas para acomodar a nova sem alteração de prazo/custo total.
4.  **Obter Aprovação ou Rejeição do Cliente (dentro de 5 dias úteis)**:
    *   **Ação**: Apresentar a proposta ao cliente e obter sua decisão formal por escrito (e-mail ou assinatura).
    *   **Exemplo**: O cliente revisa a proposta e responde por e-mail: "Aprovamos a adição do painel de relatórios personalizados com os custos e prazos adicionais propostos. Por favor, prossigam."
5.  **Atualizar Plano de Projeto e Contrato (imediatamente após aprovação)**:
    *   **Ação**: Ajustar o cronograma, orçamento, alocação de recursos e, se necessário, o contrato ou aditivo.
    *   **Exemplo**: No cronograma, as tarefas para "Desenvolvimento Painel Relatórios" são adicionadas, e a data de entrega final é atualizada de 15/12/2024 para 25/12/2024. O orçamento total é ajustado de R$ 120.000 para R$ 128.000.

---

## Templates

### Ficha de Projeto Cliente

```
Nome do Projeto: Lançamento Plataforma E-commerce "Moda Urbana"
Cliente: Estilo Urbano Ltda.
Gerente de Projeto: Ana Silva
Data de Início: 2024-08-01
Data de Entrega Prevista: 2024-12-15
Escopo Principal: Desenvolvimento de e-commerce customizado com integração de pagamentos, gestão de estoque e módulo de CRM básico.
Marcos Principais:
- Marco 1: Prototipagem UX/UI Aprovada (2024-09-01)
- Marco 2: Desenvolvimento Back-end (APIs) Concluído (2024-10-20)
- Marco 3: Desenvolvimento Front-end Concluído (2024-11-25)
- Marco 4: Testes de Qualidade e Integração (2024-12-05)
- Marco 5: Go-Live (2024-12-15)
Orçamento Aprovado: R$ 120.000,00
Orçamento Utilizado (Atual): R$ 18.000,00 (15%)
Status Atual: Em Andamento - Fase de Desenvolvimento Back-end
Riscos Identificados: Atraso na entrega de conteúdo pelo cliente, dependência de API de terceiros instáveis.
Próximos Passos: Reunião de alinhamento técnico com equipe do cliente sobre integração de estoque (2024-08-25).
Observações: Necessidade de validação urgente do fluxo de checkout pelo cliente.
```

### Relatório Semanal de Progresso do Projeto

```
Relatório de Progresso - Projeto "Moda Urbana"
Semana: 19/08/2024 - 23/08/2024
Gerente de Projeto: Ana Silva
Data do Relatório: 2024-08-23

Sumário Executivo:
A equipe avançou na definição das APIs de catálogo de produtos e usuários. O protótipo inicial da página de produtos foi aprovado internamente. Identificamos um pequeno atraso na entrega de requisitos detalhados de integração de pagamentos pelo cliente, que está sendo gerenciado.

Marcos Atingidos na Semana:
- Definição da arquitetura de microsserviços para catálogo de produtos.
- Aprovação interna do wireframe da página de produtos e listagem.

Atividades Principais da Semana:
- Desenvolvimento das APIs de produtos (70% concluído).
- Reuniões de alinhamento com equipe de UX/UI para detalhamento das telas de carrinho e checkout.
- Revisão de segurança inicial para módulo de autenticação.

Próximas Atividades (Semana 26/08/2024 - 30/08/2024):
- Finalizar APIs de produtos e iniciar APIs de usuários.
- Iniciar desenvolvimento do módulo de gestão de estoque.
- Reunião com cliente para detalhamento da integração de pagamentos (2024-08-27, 10h00).

Desafios e Bloqueadores:
- Atraso na entrega de especificações detalhadas para integração de gateway de pagamento (aguardando cliente, impacto estimado: 3 dias de atraso no módulo de pagamentos).
- Necessidade de alocar mais 10 horas de UX para refinar fluxo de checkout complexo.

Status Geral do Projeto: Verde (No prazo e orçamento, com atenção a um risco menor no módulo de pagamentos)
Orçamento Utilizado: R$ 18.000,00 (15% do total)
Horas Registradas na Semana: 120 horas
Horas Totais Registradas: 250 horas
```

---

## Checklist

-   [x] Validar escopo inicial com o cliente em reunião formal de kick-off.
-   [x] Criar cronograma detalhado com marcos de entrega e dependências.
-   [x] Alocar recursos da equipe para cada tarefa principal e subsistema.
-   [x] Configurar ferramenta de rastreamento de tarefas (e.g., Jira, Asana) com todos os itens do backlog.
-   [x] Estabelecer frequência e formato de relatórios de progresso ao cliente.
-   [x] Definir e comunicar processo formal para gestão de mudanças de escopo (Change Requests).
-   [x] Realizar reuniões semanais de stand-up com a equipe para alinhamento e detecção de bloqueadores.
-   [x] Coletar feedback do cliente formalmente após cada entrega de marco ou sprint review.
-   [x] Monitorar desvios de orçamento e cronograma através de dashboards em tempo real.
-   [x] Manter um registro de riscos e problemas (Issues Log) atualizado semanalmente.
-   [x] Conduzir reunião pós-projeto para lições aprendidas (post-mortem).
-   [x] Obter aprovação formal do cliente para a entrega final do projeto.

---

## Métricas de Referência

| Métrica                      | Benchmark (Indústria) | Meta (Empresa) |
|------------------------------|-----------------------|----------------|
| Taxa de Conclusão no Prazo   | 75%                   | 90%            |
| Desvio de Orçamento          | < 15%                 | < 5%           |
| Satisfação do Cliente (NPS)  | 60                    | 75+            |
| Taxa de Retrabalho (horas)   | < 20%                 | < 10%          |
| Nº de Mudanças de Escopo p/ Projeto | < 3                   | < 1            |
| Utilização de Recursos       | 70%                   | 85%            |

---

## Erros Comuns

1.  **Falta de Alinhamento de Expectativas Iniciais**: O cliente espera funcionalidades ou um nível de detalhe que não foi explicitamente acordado no escopo contratado.
    *   **Como evitar**: No kick-off do projeto, revisar e obter assinatura no Documento de Escopo Detalhado (DED), listando explicitamente o que está INCLUÍDO e o que está EXCLUÍDO. Exemplo: "O DED para o projeto 'Moda Urbana' não inclui integração com ERP legados, apenas com o sistema de estoque especificado."
2.  **Comunicação Inconsistente ou Insuficiente**: O cliente não recebe atualizações regulares, sente-se no escuro sobre o progresso e é pego de surpresa por problemas ou atrasos.
    *   **Como evitar**: Implementar um plano de comunicação com o cliente, definindo reuniões semanais de 30 minutos para alinhamento e relatórios de progresso quinzenais por e-mail. Exemplo: "Relatório de Progresso enviado toda sexta-feira às 17h via e-mail e disponível no portal do cliente, com call de follow-up às terças-feiras."
3.  **Gestão Reativa de Riscos**: Problemas ou bloqueadores surgem sem aviso prévio, causando atrasos significativos e impactando o orçamento.
    *   **Como evitar**: Manter um Registro de Riscos do Projeto (Risk Log), atualizado semanalmente. Identificar potenciais problemas (e.g., 'dependência de API de terceiros instável', 'rotatividade da equipe do cliente') e definir planos de mitigação (e.g., 'desenvolver mock de API para testes internos', 'treinar um segundo contato do cliente').

---

## Dicas Avançadas

1.  **Projeção de Escopo Incremental (Sprints com Cliente)**: Em vez de um escopo fixo e rígido, dividir as entregas em ciclos curtos (sprints quinzenais) com demonstrações ao cliente ao final de cada sprint. Isso permite que o cliente veja o progresso, forneça feedback contínuo e permite ajustes de prioridade no backlog sem grandes impactos no planejamento geral. Ex: "Após a sprint 3, o cliente solicitou priorizar a melhoria do filtro de busca na listagem de produtos antes do módulo de avaliações, ajustamos o backlog da próxima sprint para refletir essa nova prioridade sem alterar a data de entrega final."
2.  **Automação de Relatórios de Status e KPIs**: Integrar a ferramenta de gestão de projetos (Jira, Asana, Monday.com) com ferramentas de Business Intelligence (Power BI, Google Data Studio, Tableau). Isso permite gerar automaticamente dashboards de progresso do projeto, uso de orçamento, horas alocadas e conclusão de tarefas em tempo real, eliminando o trabalho manual de compilação. Ex: "O dashboard de horas por tarefa e progresso de marcos é atualizado a cada 4 horas, eliminando a necessidade de relatórios manuais e permitindo que o cliente acesse o status a qualquer momento."
3.  **Matriz RACI Expandida para Stakeholders do Cliente**: Utilizar a matriz RACI (Responsible, Accountable, Consulted, Informed) para definir claramente os papéis e responsabilidades de cada membro da equipe do cliente em relação às entregas e decisões do projeto. Isso evita gargalos de aprovação e garante que as pessoas certas estejam envolvidas no momento certo. Ex: "O Diretor de Marketing do cliente é 'Aprovador' para wireframes de UI e cópias de texto, mas apenas 'Consultado' para decisões de arquitetura de banco de dados, onde o CTO do cliente é 'Aprovador'."
4.  **Gestão Proativa de Débitos Técnicos com o Cliente**: Comunicar abertamente sobre débitos técnicos que podem surgir durante o desenvolvimento, explicando seu impacto potencial na manutenibilidade, escalabilidade ou futuras funcionalidades. Negociar tempo para refatoração ou inclusão no roadmap de forma transparente. Ex: "Para manter o prazo da entrega do MVP, optamos por uma solução temporária no módulo de estoque. Recomendaremos 5 dias de refatoração na fase 2 para garantir a escalabilidade e a performance a longo prazo, isso será documentado no plano de roadmap."
5.  **Criação de um "War Room" Virtual ou Canal de Resposta Rápida**: Manter um canal de comunicação dedicado e de baixa fricção (e.g., um canal específico no Slack ou Microsoft Teams) com membros chave da equipe do cliente e do projeto. Este canal é exclusivo para resolução rápida de dúvidas, bloqueadores ou decisões urgentes, evitando a burocracia de e-mails extensos. Ex: "O cliente postou uma dúvida crítica sobre um fluxo de login no canal #projeto-moda-urbana e obteve uma resposta e solução em 15 minutos, evitando um bloqueio de desenvolvimento de um dia inteiro que ocorreria via e-mail."