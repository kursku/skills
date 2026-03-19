---
name: tool-stack-audit
description: "Tool Stack Audit — Skill especializada para auditar e otimizar o conjunto de ferramentas tecnológicas de uma organização."
license: MIT
metadata:
  version: 1.0.0
  author: Cafe Code AI
  category: 11-operacoes-sistemas
  updated: 2026-03-01
---

# Tool Stack Audit

Esta skill capacita o Claude Code a realizar auditorias completas de tool stack, identificando redundâncias, otimizando custos e melhorando a eficiência operacional das ferramentas tecnológicas.

---

## Keywords

Inventário de software, Otimização de licenças, Gestão de ferramentas SaaS, Análise de TCO (Custo Total de Propriedade), Shadow IT, Automação de processos, Segurança de aplicações, Integração de sistemas, Governança de TI, Produtividade da equipe, Consolidação de ferramentas, Compliance de software.

---

## Quick Start

1. **Inicie o Inventário de Ferramentas:** Solicite ao Claude Code a criação de uma planilha inicial para mapear todas as ferramentas em uso, incluindo SaaS, on-premise e desenvolvimentos internos.
2. **Coleta de Dados de Uso e Custo:** Envie ao Claude Code relatórios de custos de licenças e dados de telemetria de uso das ferramentas para análise inicial.
3. **Identifique Overlaps Funcionais:** Peça ao Claude Code para cruzar as ferramentas inventariadas e apontar áreas onde há funcionalidades duplicadas ou sobrepostas.
4. **Gere Recomendações de Otimização:** Com base nos dados fornecidos, instrua o Claude Code a propor ferramentas para descontinuação, consolidação ou substituição, visando redução de custos e aumento de eficiência.

---

## Core Workflows

### Workflow 1: Mapeamento e Inventário Detalhado de Ferramentas

Este workflow foca na criação de uma visão abrangente e detalhada de todas as ferramentas tecnológicas utilizadas pela organização, seus propósitos, proprietários e custos.

**Passos Detalhados:**

1.  **Descoberta Abrangente:**
    *   **Ação:** O Claude Code solicita acesso a sistemas de gestão de ativos de TI (CMDB), faturas de fornecedores de SaaS (ex: AWS Billing, Microsoft Azure Cost Management), extratos de cartões corporativos, listas de software instalados em estações de trabalho (via ferramentas MDM como Intune ou Jamf) e entrevistas com líderes de departamento.
    *   **Exemplo:** "Claude, analise os últimos 12 meses de faturas da Conta AWS `123456789012` e da subscrição Azure `XYZ-ABC-789` para identificar serviços recorrentes. Paralelamente, solicite aos gerentes de projeto uma lista de ferramentas SaaS ativas que não aparecem nessas faturas, como Trello ou Asana."
2.  **Classificação e Categorização Funcional:**
    *   **Ação:** Cada ferramenta é categorizada por sua função principal (CRM, ERP, RH, BI, Desenvolvimento, Colaboração, etc.) e sua criticidade para o negócio (essencial, estratégica, de suporte, periférica).
    *   **Exemplo:** "Claude, para a ferramenta `Salesforce Sales Cloud`, categorize-a como `CRM` e `Essencial`. Para `Miro`, categorize como `Colaboração` e `Estratégica`. Para `Notion`, `Gestão de Conhecimento` e `Suporte`."
3.  **Atribuição de Proprietário e Orçamento:**
    *   **Ação:** Identificar o departamento ou indivíduo responsável pela ferramenta (proprietário de negócio) e o centro de custo associado, registrando o custo anual de licenciamento e manutenção.
    *   **Exemplo:** "Para `Jira Software`, o proprietário é `Departamento de Engenharia`, centro de custo `C001 - P&D`. Custo anual de licenças: `R$ 85.000,00`. Para `HubSpot Marketing Hub`, proprietário `Departamento de Marketing`, centro de custo `C002 - Marketing`. Custo anual: `R$ 120.000,00`."
4.  **Avaliação de Utilização e Adoção:**
    *   **Ação:** Coletar dados de telemetria de uso (número de usuários ativos, frequência de uso, recursos mais acessados) fornecidos pelos próprios softwares ou ferramentas de monitoramento.
    *   **Exemplo:** "Claude, analise os relatórios de uso do Slack para os últimos 3 meses: `1.500 usuários ativos de 2.000 licenças`, `85% de canais ativos`. Para o Microsoft Teams: `800 usuários ativos de 2.000 licenças`, `20% de canais ativos`. Para o Miro: `300 usuários ativos de 500 licenças`, `60% de uso semanal`."
5.  **Mapeamento de Integrações:**
    *   **Ação:** Documentar as integrações existentes entre as ferramentas, identificando dependências e fluxos de dados.
    *   **Exemplo:** "Registrar que `Salesforce` integra com `Zendesk` para suporte ao cliente e com `Mailchimp` para campanhas de e-mail. `Jira` integra com `Confluence` para documentação e `Bitbucket` para controle de versão."

### Workflow 2: Análise de Redundância e Otimização de Licenças

Este workflow visa identificar ferramentas com funcionalidades sobrepostas e oportunidades de otimização de custos através da consolidação ou desativação de licenças subutilizadas.

**Passos Detalhados:**

1.  **Identificação de Overlaps Funcionais:**
    *   **Ação:** O Claude Code compara as funcionalidades primárias e secundárias das ferramentas dentro da mesma categoria ou categorias relacionadas para detectar redundâncias.
    *   **Exemplo:** "Claude, ao comparar `Trello` e `Jira Work Management`, observei que ambos oferecem gestão de tarefas e kanban boards. A equipe de Marketing usa Trello para gestão de conteúdo, enquanto a de Engenharia usa Jira para sprints. Ambos poderiam ser consolidados no Jira para padronização e redução de licenças."
    *   **Exemplo:** "Detectei que `Zoom` e `Google Meet` são usados para videoconferências por diferentes equipes, apesar do Google Meet já fazer parte do pacote Google Workspace que a empresa já paga."
2.  **Análise de Custo-Benefício por Licença:**
    *   **Ação:** Calcular o custo por usuário ativo para ferramentas similares e comparar a proposta de valor, funcionalidades específicas e nível de adoção.
    *   **Exemplo:** "Custo/usuário/mês do `Trello Business Class` é `R$ 30,00` para 100 usuários, totalizando `R$ 3.000,00`. Custo/usuário/mês do `Jira Work Management` (já existente no pacote Atlassian) é efetivamente `R$ 0,00` para usuários adicionais, considerando a licença enterprise. A migração representaria uma economia direta."
3.  **Avaliação de Recursos Subutilizados:**
    *   **Ação:** Analisar relatórios de uso para identificar licenças pagas que não estão sendo ativamente utilizadas ou recursos premium que não são explorados.
    *   **Exemplo:** "Claude, verifiquei que 200 das 500 licenças do `Microsoft 365 E3` não tiveram login nos últimos 90 dias. Das licenças ativas, apenas 10% usam o `Power BI Pro`, indicando possível superdimensionamento."
4.  **Proposta de Consolidação/Descontinuação:**
    *   **Ação:** O Claude Code gera um relatório detalhado com recomendações para desativar ferramentas redundantes, consolidar licenças ou renegociar contratos, com estimativa de economia e impacto.
    *   **Exemplo:** "Recomendação: Descontinuar `Trello Business Class` e migrar projetos de marketing para `Jira Work Management`. Economia anual estimada: `R$ 36.000,00`. Impacto: Padronização de ferramentas de gestão de projetos. Recomendação: Reduzir 200 licenças não utilizadas do `Microsoft 365 E3`. Economia anual estimada: `R$ 48.000,00`."
5.  **Plano de Transição e Comunicação:**
    *   **Ação:** Desenvolver um plano de migração de dados e um cronograma de comunicação para as equipes afetadas pela mudança de ferramentas.
    *   **Exemplo:** "Para a descontinuação do Trello, criar um plano de 4 semanas: Semana 1 - Comunicação inicial; Semana 2 - Treinamento para Jira; Semana 3 - Migração de dados; Semana 4 - Desativação. Designar um champion em cada equipe para apoiar a transição."

---

## Templates

### Matriz de Inventário de Ferramentas

```
# Matriz de Inventário de Ferramentas - Q1 2024

| Ferramenta                 | Categoria           | Proprietário Negócio | Centro de Custo | Custo Anual (R$) | Licenças Contratadas | Licenças Ativas | % Utilização | Redundância Potencial | Integrações Chave  | Data Última Revisão | Notas                                      |
|----------------------------|---------------------|----------------------|-----------------|------------------|----------------------|-----------------|--------------|-----------------------|--------------------|---------------------|--------------------------------------------|
| Salesforce Sales Cloud     | CRM                 | Vendas               | C001            | 250.000,00       | 150                  | 145             | 96%          | Baixa                 | Zendesk, Mailchimp | 2024-01-15          | Ferramenta estratégica para Vendas.        |
| HubSpot Marketing Hub      | Marketing Automação | Marketing            | C002            | 120.000,00       | 50                   | 48              | 96%          | Baixa                 | Salesforce         | 2024-01-15          | Usado para inbound marketing.              |
| Jira Software              | Gestão Projetos     | Engenharia           | C003            | 85.000,00        | 200                  | 190             | 95%          | Média (com Trello)    | Confluence, Bitbucket| 2024-01-15          | Padrão para desenvolvimento de software.   |
| Trello Business Class      | Gestão Tarefas      | Marketing            | C002            | 12.000,00        | 100                  | 70              | 70%          | Alta (com Jira)       | Slack              | 2024-01-15          | Equipe de Marketing usa para gestão de conteúdo. |
| Slack Enterprise Grid      | Comunicação Interna | TI                   | C004            | 90.000,00        | 500                  | 480             | 96%          | Baixa                 | Jira, Google Drive | 2024-01-15          | Comunicação primária da empresa.           |
| Microsoft 365 E3           | Produtividade       | TI                   | C004            | 240.000,00       | 500                  | 300             | 60%          | Média (com Zoom)      | Teams, OneDrive    | 2024-01-15          | Inclui Outlook, Word, Excel, PowerPoint.   |
| Zoom Pro                   | Videoconferência    | Vendas               | C001            | 18.000,00        | 50                   | 35              | 70%          | Alta (com Google Meet)| Calendly           | 2024-01-15          | Usado principalmente para reuniões externas. |
| Google Meet (via GWS)      | Videoconferência    | TI                   | C004            | 0,00             | 500                  | 400             | 80%          | Alta (com Zoom)       | Google Calendar    | 2024-01-15          | Incluso no Google Workspace.               |
| Miro Business              | Colaboração Visual  | P&D                  | C003            | 15.000,00        | 50                   | 40              | 80%          | Baixa                 | Jira, Slack        | 2024-01-15          | Ferramenta essencial para brainstorming.   |
```

### Relatório de Análise de Redundância e Otimização

```
# Relatório de Análise de Redundância e Otimização - Q1 2024

**Data da Análise:** 2024-03-01
**Responsável:** Equipe de Operações de TI

---

## 1. Ferramentas em Análise para Otimização

| Categoria              | Ferramenta 1            | Ferramenta 2            |
|------------------------|-------------------------|-------------------------|
| Gestão de Projetos     | Trello Business Class   | Jira Work Management    |
| Videoconferência       | Zoom Pro                | Google Meet (via M365)  |
| Produtividade/Email    | Microsoft 365 E3        | Google Workspace (GWS)  |

---

## 2. Detalhamento e Recomendações

### 2.1. Gestão de Projetos: Trello vs. Jira Work Management

*   **Justificativa da Redundância:** Ambas as ferramentas oferecem funcionalidades de gestão de tarefas, kanban e acompanhamento de projetos. A equipe de Marketing utiliza Trello, enquanto outras equipes (Engenharia, Produto) utilizam Jira. A padronização traria ganhos de colaboração e integração.
*   **Ferramenta Recomendada para Manter:** Jira Work Management (já amplamente utilizado, maior integração com o ecossistema Atlassian).
*   **Ferramenta Recomendada para Descontinuar:** Trello Business Class.
*   **Impacto Estimado:**
    *   **Economia Anual:** R$ 12.000,00 (Custo do Trello).
    *   **Produtividade:** Aumento da padronização de processos, facilidade de colaboração interdepartamental, redução da curva de aprendizado para novos colaboradores.
    *   **Riscos:** Possível resistência inicial da equipe de Marketing, necessidade de plano de migração de dados.
*   **Ações Sugeridas:**
    *   Criar plano de migração de boards e dados do Trello para Jira.
    *   Oferecer treinamento específico para a equipe de Marketing no Jira Work Management.
    *   Definir cronograma de desativação do Trello.

### 2.2. Videoconferência: Zoom Pro vs. Google Meet

*   **Justificativa da Redundância:** A empresa já possui o Google Workspace, que inclui o Google Meet. O Zoom Pro é mantido por equipes específicas de Vendas para chamadas externas, mas o Google Meet oferece funcionalidades equivalentes para a maioria dos casos de uso.
*   **Ferramenta Recomendada para Manter:** Google Meet (já incluso no Google Workspace, custo marginal zero).
*   **Ferramenta Recomendada para Descontinuar:** Zoom Pro.
*   **Impacto Estimado:**
    *   **Economia Anual:** R$ 18.000,00 (Custo do Zoom Pro).
    *   **Produtividade:** Simplificação do stack de ferramentas, redução de senhas e logins.
    *   **Riscos:** Possível perda de funcionalidades muito específicas do Zoom (ex: salas de breakout avançadas, relatórios de webinar detalhados, dependendo do plano).
*   **Ações Sugeridas:**
    *   Avaliar criticamente a necessidade de funcionalidades avançadas do Zoom que o Google Meet não atende.
    *   Treinar a equipe de Vendas no uso das funcionalidades do Google Meet.
    *   Definir um período de transição e desativar as licenças do Zoom.

### 2.3. Otimização de Licenças Microsoft 365 E3

*   **Justificativa da Redundância:** Análise de uso mostrou que 200 das 500 licenças de Microsoft 365 E3 não são utilizadas há mais de 90 dias, e muitos usuários ativos não exploram os recursos premium (ex: Power BI Pro, Advanced Threat Protection).
*   **Ação Recomendada:** Reduzir o número de licenças E3 para 300 e reavaliar a necessidade de planos E3 para usuários que não utilizam os recursos avançados, considerando a migração para planos mais básicos como Microsoft 365 Business Standard para alguns usuários.
*   **Impacto Estimado:**
    *   **Economia Anual:** R$ 96.000,00 (200 licenças * R$ 40/mês * 12 meses).
    *   **Produtividade:** Otimização do investimento em software.
    *   **Riscos:** Necessidade de comunicação clara para usuários afetados pela mudança de plano.
*   **Ações Sugeridas:**
    *   Identificar os 200 usuários inativos e desprovisionar suas licenças.
    *   Realizar pesquisa de uso para identificar usuários que podem migrar para planos mais baratos.
    *   Renegociar contrato com a Microsoft para refletir o novo número de licenças.

---

## Checklist

- [X] Inventário completo de todas as ferramentas ativas (SaaS, on-premise, customizadas).
- [X] Classificação de cada ferramenta por categoria funcional e criticidade para o negócio.
- [X] Atribuição de proprietário de negócio e centro de custo para cada ferramenta.
- [X] Coleta de dados de custo anual de licenciamento e manutenção por ferramenta.
- [X] Análise de dados de telemetria de uso (licenças ativas vs. contratadas, frequência de uso).
- [X] Mapeamento de integrações e dependências entre as ferramentas.
- [X] Identificação de ferramentas com funcionalidades sobrepostas e potencial de redundância.
- [X] Cálculo do custo por usuário/licença para ferramentas comparáveis.
- [X] Avaliação de recursos premium subutilizados em pacotes de software.
- [X] Proposta de descontinuação/consolidação de ferramentas com estimativa de economia.
- [X] Criação de um plano de migração de dados e comunicação para cada mudança.
- [X] Avaliação de riscos de segurança e conformidade para cada ferramenta.

---

## Métricas de Referência

| Métrica                         | Benchmark (Empresas similares) | Meta Interna Anual |
|---------------------------------|--------------------------------|--------------------|
| Custo Total de Ferramentas / Colaborador (anual) | R$ 3.000 - R$ 5.000        | R$ 3.500           |
| Taxa de Redundância de Ferramentas | < 10%                          | 5%                 |
| % de Otimização de Custos (anual) | 5% - 15%                       | 10%                |
| Taxa de Adoção de Ferramentas Chave | > 85%                          | 90%                |
| Índice de Shadow IT             | < 5%                           | 2%                 |
| Tempo Médio de Provisionamento de Ferramentas | < 2 dias                       | 1 dia              |

---

## Erros Comuns

1.  **Ignorar o "Shadow IT"**: Muitas equipes adquirem e utilizam ferramentas sem o conhecimento ou aprovação formal da TI, resultando em custos ocultos, riscos de segurança e redundâncias.
    *   **Como evitar**: Implementar processos de descoberta proativos (análise de faturas, monitoramento de rede) e criar um canal fácil para as equipes registrarem novas ferramentas, incentivando a conformidade. Exemplo: "Em vez de banir ferramentas não aprovadas, crie um 'Programa de Ferramentas Aprovadas' e um 'Formulário de Pedido de Nova Ferramenta' que inclua análise de segurança e custo pela TI."
2.  **Focar Apenas no Custo**: Uma auditoria que prioriza apenas a redução de custos pode levar à desativação de ferramentas essenciais para a produtividade ou inovação, causando atrito com as equipes e impactos negativos na operação.
    *   **Como evitar**: Equilibrar a análise de custo com a avaliação de valor, impacto na produtividade, funcionalidades exclusivas e feedback dos usuários. Exemplo: "Antes de desativar o Figma, que tem um custo considerável, consulte a equipe de Design para entender seu impacto na velocidade de prototipagem e colaboração, mesmo que haja alternativas mais baratas."
3.  **Não Envolver os Usuários Finais**: A falta de engajamento dos usuários que utilizam as ferramentas diariamente pode resultar em recomendações impraticáveis, baixa adesão às novas ferramentas e resistência às mudanças.
    *   **Como evitar**: Conduzir entrevistas, pesquisas e workshops com usuários de diferentes departamentos para entender seus fluxos de trabalho, pontos de dor e necessidades reais. Exemplo: "Ao considerar a consolidação de ferramentas de comunicação, organize sessões de feedback com representantes de cada departamento para entender como Slack e Teams são usados e quais funcionalidades são críticas para eles."

---

## Dicas Avançadas

1.  **Análise de Interoperabilidade e APIs**: Além da funcionalidade, avalie a capacidade das ferramentas de se integrarem via APIs robustas. Ferramentas que se integram bem podem criar fluxos de trabalho mais eficientes, mesmo que tenham um custo individual mais alto.
    *   **Exemplo Prático**: "Priorize ferramentas que ofereçam APIs RESTful bem documentadas e suporte a webhooks, como `monday.com` ou `Asana`, para permitir a construção de automações personalizadas com sistemas como `Zapier` ou `Make (ex-Integromat)`, mesmo que tenham um custo ligeiramente superior a alternativas sem API aberta."
2.  **Modelagem de TCO (Custo Total de Propriedade)**: Vá além do custo da licença. Inclua custos de implementação, treinamento, suporte, manutenção, integrações, migração de dados e o tempo da equipe de TI/negócio dedicado à ferramenta.
    *   **Exemplo Prático**: "Ao comparar um CRM SaaS com uma solução on-premise, o SaaS pode ter uma licença anual mais alta, mas o TCO do on-premise pode ser muito maior devido a servidores, DBAs, consultores de implementação e manutenção contínua."
3.  **Auditoria de Conformidade Regulatória e Segurança**: Para ferramentas que processam dados sensíveis (LGPD/GDPR), verifique certificações (ISO 27001, SOC 2 Type II), políticas de privacidade, termos de serviço e localização dos data centers.
    *   **Exemplo Prático**: "Para qualquer ferramenta de RH ou folha de pagamento como `Workday` ou `ADP`, exija evidências de conformidade com a LGPD, relatórios de auditoria de segurança e verifique as cláusulas de processamento de dados para garantir que atendem aos requisitos internos e regulatórios."
4.  **Automação do Monitoramento de Uso e Custos**: Implemente ferramentas de Software Asset Management (SAM) ou scripts personalizados para monitorar automaticamente o uso de licenças e os custos, alertando sobre subutilização ou picos de gastos.
    *   **Exemplo Prático**: "Configure um script Python para extrair dados de uso de APIs de ferramentas como `Okta` (para autenticação/uso de apps) e `Cloudability` (para custos de nuvem), gerando um relatório semanal que destaca licenças inativas há mais de 60 dias ou aumentos de custo acima de 10% no último mês."