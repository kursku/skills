---
name: project-management-setup
description: "Project Management Setup — Skill especializada para project management setup"
license: MIT
metadata:
  version: 1.0.0
  author: Cafe Code AI
  category: 11-operacoes-sistemas
  updated: 2026-03-01
risk: critical
---

# Project Management Setup

Esta skill capacita o Claude a configurar e otimizar projetos desde a iniciação, estabelecendo estruturas, processos e ferramentas essenciais para a gestão eficaz.

---

## Keywords

Project Charter, WBS (Estrutura Analítica do Projeto), Cronograma Base, Matriz RACI, Plano de Comunicação, Gestão de Riscos, Linha de Base, Escopo do Projeto, Stakeholder Engagement, Ferramentas PMO, Dicionário da WBS, Repositório de Documentos.

---

## Quick Start

1.  **Elaborar e Obter Aprovação do Project Charter**: Iniciar o documento com o nome do projeto (ex: "Implantação do ERP SAP S/4HANA"), patrocinador (ex: "Diretoria Financeira"), e objetivos SMART (ex: "Reduzir tempo de fechamento contábil em 20% até Q4 2025").
2.  **Mapear Stakeholders Primários**: Realizar uma sessão de brainstorming para identificar os principais interessados (ex: "Diretores, Gerentes de TI, Usuários Chave dos Módulos Financeiros, Fornecedor SAP") e iniciar um registro básico de interesse/influência.
3.  **Criar a Estrutura Analítica do Projeto (WBS) Nível 1 e 2**: Decompor o escopo em grandes entregas (ex: "Planejamento, Levantamento de Requisitos, Customização, Testes, Treinamento, Go-Live") e sub-entregas chave, utilizando software como MS Project ou Miro.
4.  **Configurar o Repositório de Documentos Centralizado**: Estabelecer a estrutura de pastas e permissões em uma ferramenta como SharePoint ou Confluence (ex: "01-Charter", "02-Escopo", "03-Cronograma", "04-Riscos", "05-Comunicações").
5.  **Agendar Reunião de Kick-off Interna**: Convocar a equipe principal do projeto e os stakeholders mais influentes para alinhar expectativas, revisar o Project Charter e a WBS inicial, e consolidar o comprometimento.

---

## Core Workflows

### Workflow 1: Definição e Detalhamento do Escopo e Cronograma Base

Este workflow descreve o processo de transformar a ideia do projeto em um escopo claro e um cronograma exequível, estabelecendo as bases para o monitoramento e controle.

1.  **Revisão do Project Charter e Declaração do Escopo**:
    *   **Ação**: O Gerente de Projeto (GP) revisa o Project Charter aprovado (ex: "Lançamento da Plataforma E-commerce B2B v2.0") para garantir que a visão, os objetivos e as entregas de alto nível estejam alinhados.
    *   **Exemplo**: O objetivo principal do charter é "Aumentar a receita em 15% através da nova plataforma e-commerce B2B em 12 meses". A declaração do escopo inicial seria "Desenvolvimento e implantação de uma plataforma e-commerce B2B com funcionalidades de catálogo de produtos, carrinho de compras, integração com ERP existente, gestão de pedidos e portal de clientes para autoatendimento".
    *   **Entrega**: Declaração do Escopo do Projeto.

2.  **Criação da Estrutura Analítica do Projeto (WBS) Detalhada**:
    *   **Ação**: Realizar sessões de brainstorming e decomposição com a equipe e especialistas no assunto para detalhar o escopo até o nível de pacotes de trabalho gerenciáveis.
    *   **Exemplo**: Para o projeto E-commerce B2B:
        *   Nível 1: Plataforma E-commerce B2B v2.0
            *   Nível 2: 1.0 Planejamento
                *   Nível 3: 1.1 Definição de Requisitos (funcionais e não funcionais)
                *   Nível 3: 1.2 Análise de Viabilidade Técnica
            *   Nível 2: 2.0 Desenvolvimento do Frontend
                *   Nível 3: 2.1 Design UI/UX
                *   Nível 3: 2.2 Implementação do Catálogo de Produtos
                *   Nível 3: 2.3 Implementação do Carrinho de Compras
            *   Nível 2: 3.0 Desenvolvimento do Backend
                *   Nível 3: 3.1 Integração com ERP (SAP)
                *   Nível 3: 3.2 Módulo de Gestão de Pedidos
            *   Nível 2: 4.0 Testes
                *   Nível 3: 4.1 Testes de Integração
                *   Nível 3: 4.2 Testes de Performance
                *   Nível 3: 4.3 Testes de Aceitação do Usuário (UAT)
            *   Nível 2: 5.0 Implantação e Go-Live
                *   Nível 3: 5.1 Configuração de Servidores
                *   Nível 3: 5.2 Treinamento de Usuários
                *   Nível 3: 5.3 Lançamento Oficial
    *   **Entrega**: WBS visual (diagrama ou lista hierárquica) e Dicionário da WBS (detalhando cada pacote de trabalho).

3.  **Desenvolvimento do Cronograma Base**:
    *   **Ação**: Com base na WBS, estimar durações das atividades, definir dependências lógicas e alocar recursos para criar o cronograma inicial. Identificar o caminho crítico.
    *   **Exemplo**: Usando MS Project: A atividade "2.1 Design UI/UX" (duração 3 semanas) deve ser concluída antes de "2.2 Implementação do Catálogo de Produtos". A "3.1 Integração com ERP" (duração 8 semanas) é uma atividade-chave no caminho crítico. O cronograma inicial indica um prazo total de 24 semanas para o projeto.
    *   **Entrega**: Cronograma do Projeto (Gantt Chart), Caminho Crítico, e uma Linha de Base aprovada para o cronograma.

### Workflow 2: Planejamento de Recursos, Comunicação e Riscos Iniciais

Este workflow estabelece como a equipe será organizada, como a comunicação será gerenciada e como os riscos serão identificados e mitigados no início do projeto.

1.  **Definição da Estrutura Organizacional e Matriz RACI**:
    *   **Ação**: Determinar os papéis e responsabilidades de cada membro da equipe e stakeholder chave para as principais entregas do projeto.
    *   **Exemplo**: Para o projeto "Lançamento da Plataforma E-commerce B2B v2.0":
        *   GP: Responsável pelo planejamento e execução geral.
        *   Analista de Negócios: Responsável pela coleta de requisitos.
        *   Desenvolvedores Frontend/Backend: Responsáveis pelo desenvolvimento.
        *   Equipe de QA: Responsável pelos testes.
        *   Gerente de Marketing: Consultado sobre requisitos de UI/UX.
        *   Diretor Comercial: Aprovador de entregas.
    *   **Entrega**: Organograma do Projeto e Matriz RACI para as 10-15 principais entregas/decisões.

2.  **Elaboração do Plano de Comunicação**:
    *   **Ação**: Definir como, quando, quem e para quem as informações do projeto serão comunicadas.
    *   **Exemplo**:
        *   **Relatório de Status Semanal**: Para equipe do projeto e stakeholders chaves. Frequência: Todas as segundas-feiras, 9h. Canal: E-mail e reunião de 30 min. Conteúdo: Progresso, próximos passos, bloqueios.
        *   **Relatório Executivo Mensal**: Para patrocinador e diretoria. Frequência: Primeira sexta-feira do mês. Canal: E-mail e reunião de 60 min. Conteúdo: Status geral, orçamento, riscos críticos, decisões estratégicas.
        *   **Ata de Reunião**: Para todas as reuniões formais. Frequência: Em até 24h após a reunião. Canal: E-mail e repositório.
    *   **Entrega**: Plano de Comunicação do Projeto.

3.  **Identificação e Registro Inicial de Riscos**:
    *   **Ação**: Realizar sessões de brainstorming com a equipe e especialistas para identificar potenciais eventos que possam impactar negativamente o projeto (ameaças) e positivamente (oportunidades).
    *   **Exemplo**:
        *   **Risco (Ameaça)**: "Atraso na integração com o ERP SAP devido à complexidade da API e falta de documentação."
            *   **Probabilidade**: Média (3/5)
            *   **Impacto**: Alto (4/5)
            *   **Plano de Mitigação**: "Alocar um consultor SAP sênior para a equipe de integração; iniciar a análise da API com 2 semanas de antecedência."
        *   **Risco (Oportunidade)**: "Disponibilidade de nova funcionalidade de IA no ERP que pode otimizar a gestão de estoque."
            *   **Probabilidade**: Média (3/5)
            *   **Impacto**: Alto (4/5)
            *   **Plano de Resposta**: "Realizar um estudo de viabilidade para incorporar a funcionalidade de IA no escopo, caso traga valor adicional significativo."
    *   **Entrega**: Registro de Riscos inicial (Risk Register).

---

## Templates

### Project Charter Simplificado

```
[NOME DO PROJETO]: Implantação do Sistema de Gestão de Frota Inteligente "FleetManager 360"

[DATA]: 15 de Outubro de 2024

[PATROCINADOR DO PROJETO]: Dr. Ricardo Almeida, Diretor de Operações Logísticas

[GERENTE DE PROJETO]: Ana Paula Costa, Gerente Sênior de Projetos

[OBJETIVOS DO PROJETO (SMART)]:
1.  **Reduzir em 15% os custos de combustível** da frota em até 12 meses após a implantação, através de rotas otimizadas e monitoramento em tempo real.
2.  **Aumentar em 10% a taxa de utilização** dos veículos em 6 meses, otimizando a alocação e reduzindo o tempo ocioso.
3.  **Melhorar em 20% a segurança da frota** (redução de acidentes e infrações) em 9 meses, com monitoramento de comportamento do motorista e alertas preventivos.
4.  **Automatizar em 80% o registro de manutenção** dos veículos em 3 meses, integrando o sistema com a oficina interna.

[ESCOPO DO PROJETO (ALTO NÍVEL)]:
O projeto consiste na seleção, aquisição, configuração e implantação do sistema "FleetManager 360" para toda a frota de 250 veículos da empresa. Inclui módulos de rastreamento GPS, otimização de rotas, telemetria de veículos, gestão de manutenção preventiva/corretiva e portal de relatórios gerenciais. Inclui treinamento para 150 motoristas e 15 coordenadores de frota.
Exclui: Desenvolvimento de hardware customizado; integração com sistemas de folha de pagamento.

[ENTREGAS PRINCIPAIS]:
1.  Documento de Requisitos de Negócio e Técnicos.
2.  Sistema "FleetManager 360" configurado e funcional.
3.  Base de Dados de Veículos e Motoristas migrada para o novo sistema.
4.  Manuais de Treinamento e Procedimentos Operacionais Padrão (SOPs).
5.  Equipe de Operações Logísticas e Motoristas treinados.
6.  Relatórios de Desempenho e Dashboards operacionais.

[ORÇAMENTO ESTIMADO]: R$ 750.000,00 (incluindo licenças, serviços de implantação e treinamento).

[PRAZO ESTIMADO]: 8 meses.

[CRITÉRIOS DE SUCESSO]:
*   Atingimento dos objetivos SMART estabelecidos.
*   Conformidade com o escopo e orçamento aprovados.
*   Satisfação dos usuários-chave > 85% em pesquisa pós-implantação.

[RISCOS INICIAIS (ALTO NÍVEL)]:
1.  Resistência à mudança por parte dos motoristas e equipes operacionais.
2.  Atraso na integração com sistemas legados de contabilidade.
3.  Problemas de cobertura de sinal GPS em áreas rurais.

[ASSINATURAS DE APROVAÇÃO]:
_________________________
Dr. Ricardo Almeida
Diretor de Operações Logísticas

_________________________
Ana Paula Costa
Gerente de Projeto
```

### Matriz RACI para Lançamento de Nova Funcionalidade (Módulo de Faturamento Recorrente)

```
[PROJETO]: Lançamento do Módulo de Faturamento Recorrente (MFR) v1.0
[DATA]: 20 de Novembro de 2024

| ATIVIDADE/ENTREGA              | GERENTE DE PRODUTO | GERENTE DE PROJETO | DESENVOLVEDOR LÍDER | ENGENHEIRO QA | ANALISTA DE NEGÓCIOS | GERENTE DE VENDAS |
|--------------------------------|--------------------|--------------------|---------------------|---------------|----------------------|-------------------|
| 1. Definição de Requisitos MFR | R                  | A                  | C                   | I             | I                    | C                 |
| 2. Design da Arquitetura MFR   | C                  | A                  | R                   | I             | I                    |                   |
| 3. Desenvolvimento do Backend  | I                  | C                  | R                   | I             |                      |                   |
| 4. Desenvolvimento do Frontend | I                  | C                  | R                   | I             |                      |                   |
| 5. Testes Unitários            |                    |                    | R                   | A             |                      |                   |
| 6. Testes de Integração        |                    |                    | C                   | R             |                      |                   |
| 7. Testes de Aceitação (UAT)   | I                  | C                  |                     | A             | R                    | C                 |
| 8. Criação de Documentação     | C                  | C                  | I                   |               | R                    |                   |
| 9. Treinamento da Equipe Vendas| C                  | C                  |                     |               | I                    | R                 |
| 10. Implantação em Produção    | C                  | R                  | A                   | I             |                      |                   |
| 11. Comunicação ao Cliente     | R                  | C                  |                     |               |                      | A                 |
```
Legenda: R = Responsável (Responsible), A = Aprovador (Accountable), C = Consultado (Consulted), I = Informado (Informed).

---

## Checklist

-   [x] Project Charter assinado e aprovado pela diretoria.
-   [x] WBS detalhada até o nível de pacotes de trabalho (mínimo 3 níveis).
-   [x] Dicionário da WBS preenchido para os principais pacotes de trabalho.
-   [x] Cronograma base (baseline) definido, com caminho crítico identificado e aprovado.
-   [x] Matriz RACI para as principais entregas e decisões do projeto.
-   [x] Plano de Comunicação com frequência, canais e públicos definidos.
-   [x] Registro de Riscos inicial com pelo menos 5 ameaças e 2 oportunidades, e planos de resposta básicos.
-   [x] Repositório de documentos do projeto (ex: SharePoint, Confluence) configurado com estrutura de pastas.
-   [x] Ferramenta de gestão de projetos (ex: Jira, Asana, MS Project) configurada com tarefas e atribuições iniciais.
-   [x] Reunião de kick-off do projeto realizada com a equipe principal e ata distribuída.
-   [x] Lista de Stakeholders primários identificada e mapa de interesse/influência inicial criado.
-   [x] Acordos de Nível de Serviço (SLAs) para suporte pós-implantação definidos.

---

## Métricas de Referência

| Métrica                      | Benchmark da Indústria | Meta do Projeto (Exemplo) |
|------------------------------|------------------------|---------------------------|
| Variação do Cronograma (SV)  | -5% a +5%              | -3% a +3%                 |
| Variação do Custo (CV)       | -5% a +5%              | -2% a +2%                 |
| Satisfação do Cliente/Usuário| > 80%                  | > 90%                     |
| Taxa de Conformidade do Escopo| > 95%                  | > 98%                     |
| Taxa de Defeitos Pós-Lançamento | < 2% (até 30 dias)     | < 1%                      |
| Eficiência da Alocação de Recursos | 75% - 90%          | 85%                       |

---

## Erros Comuns

1.  **Escopo Indefinido ou "Gold Plating"**: O projeto começa sem um escopo claro e aceita adições constantes de funcionalidades sem controle de mudança.
    *   **Como evitar**: Criar um Dicionário da WBS detalhado para cada pacote de trabalho, especificando entregas e critérios de aceitação. Implementar um processo formal de controle de mudanças, exigindo aprovação do comitê de mudança para qualquer alteração de escopo que impacte o cronograma ou orçamento.
    *   **Exemplo**: Durante o desenvolvimento de um aplicativo, a equipe de vendas solicita uma "funcionalidade de chat com IA". Em vez de aceitar imediatamente, o GP encaminha a solicitação para o processo de controle de mudanças, que analisará o impacto no prazo (estimado em +4 semanas), custo e prioridade, antes de qualquer decisão.

2.  **Falta de Engajamento dos Stakeholders**: Stakeholders chave são informados tardiamente ou não são envolvidos nas decisões críticas, resultando em insatisfação e resistência.
    *   **Como evitar**: Desenvolver um Mapa de Stakeholders detalhado no início do projeto, classificando-os por interesse e influência. Criar um Plano de Engajamento que defina reuniões regulares, workshops e canais de feedback específicos para cada grupo de stakeholders.
    *   **Exemplo**: Para um projeto de implantação de um novo ERP, realizar workshops semanais com os usuários-chave de cada departamento para coletar requisitos e validar protótipos, garantindo que suas expectativas sejam gerenciadas e que se sintam parte do processo.

3.  **Cronogramas Otimistas e Irrealistas**: As estimativas de duração das atividades são feitas de forma apressada, ignorando dependências e recursos limitados, levando a atrasos inevitáveis.
    *   **Como evitar**: Utilizar técnicas de estimativa mais robustas, como a Estimativa em Três Pontos (PERT) ou a Estimativa Análoga (baseada em projetos anteriores similares). Envolver a equipe técnica na estimativa das atividades em que são especialistas e adicionar reservas de contingência.
    *   **Exemplo**: Ao estimar a "Integração do Módulo Financeiro com o CRM", a equipe técnica estima 10 dias otimista, 15 dias mais provável e 25 dias pessimista. Usando PERT, a estimativa ponderada seria (10 + 4*15 + 25) / 6 = 15.8 dias. Além disso, adicionar uma reserva de contingência de 10% para imprevistos.

---

## Dicas Avançadas

1.  **Implementar um Dicionário da WBS Robusto com Critérios de Aceitação**: Para cada pacote de trabalho da WBS, além da descrição, adicione claramente os critérios de aceitação. Isso transforma a WBS em uma ferramenta de validação, não apenas de decomposição.
    *   **Exemplo Prático**: Para o pacote de trabalho "Implementação do Carrinho de Compras" do projeto E-commerce, o dicionário da WBS deve incluir: "O carrinho deve permitir adicionar/remover itens, exibir subtotal/total, impostos e frete. Critério de Aceitação: Todos os campos devem ser editáveis, o cálculo do total deve ser preciso em 100%, e o carrinho deve persistir por 72h para usuários logados."

2.  **Adotar um Sistema de Gestão de Mudanças Formal desde o Início**: Não espere as mudanças acontecerem. Estabeleça um Change Control Board (CCB) e um formulário padronizado para solicitações de mudança, com campos para impacto no escopo, cronograma, custo e justificativa.
    *   **Exemplo Prático**: Uma solicitação para "adicionar pagamento via Pix" no projeto de E-commerce é formalizada. O CCB (composto por GP, Patrocinador e Gerente de Produto) avalia que a mudança adiciona 2 semanas ao cronograma e R$15.000 ao orçamento, mas traz um potencial de aumento de 5% nas vendas. A decisão é tomada com base nesses dados, não apenas no "querer".

3.  **Utilizar Análise de Valor Agregado (EVA) como Ferramenta de Monitoramento de Setup**: Comece a coletar dados de custo real e progresso físico desde as primeiras atividades de planejamento para ter uma visão precoce do desempenho do projeto.
    *   **Exemplo Prático**: Após 2 meses de um projeto de 10 meses com orçamento de R$100.000 (R$10.000/mês), o Custo Real (AC) é R$22.000. O Valor Planejado (PV) para 2 meses seria R$20.000. Se apenas 80% do trabalho planejado para esses 2 meses foi concluído (Valor Agregado - EV = 0.8 * R$20.000 = R$16.000), o GP já pode identificar um atraso no cronograma (SV = -R$4.000) e estouro de orçamento (CV = -R$6.000) nas fases iniciais.

4.  **Criar um Plano de Transição Detalhado para Operações**: Um projeto não termina no "Go-Live". Planeje a passagem de bastão para a equipe de operações e suporte, incluindo documentação, treinamentos e contratos de manutenção.
    *   **Exemplo Prático**: No projeto de implantação do FleetManager 360, o plano de transição inclui a criação de SOPs para uso diário do sistema pelos motoristas e coordenadores, um manual de troubleshooting para a equipe de TI e um cronograma de reuniões de acompanhamento trimestrais nos primeiros 6 meses pós-implantação com a equipe de operações.

5.  **Estabelecer um "Project War Room" (Físico ou Virtual)**: Um espaço centralizado onde informações cruciais do projeto (cronograma, WBS, riscos, dashboards) são visualizadas e atualizadas em tempo real, promovendo transparência e colaboração.
    *   **Exemplo Prático**: Em um ambiente híbrido, utilize um Miro Board ou Mural compartilhado com links para a WBS no Jira, o cronograma no MS Project Online, e um dashboard de Power BI com métricas de desempenho. A equipe pode acessar, comentar e contribuir a qualquer momento, e as reuniões de status usam este ambiente como ponto focal.
---