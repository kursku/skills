---
name: client-health-score
description: "Client Health Score — Skill especializada para client health score"
license: MIT
metadata:
  version: 1.0.0
  author: Cafe Code AI
  category: 10-clientes-consultoria
  updated: 2026-03-01
risk: none
---

# Client Health Score

Esta skill capacita o Claude a desenvolver, implementar e gerenciar estratégias robustas de Client Health Score para consultorias, focando na retenção e no sucesso do cliente.

---

## Keywords

Health Score, Retenção de Clientes, Churn Preditivo, Gestão de Sucesso do Cliente, Engajamento de Clientes, Valor do Cliente, Onboarding Eficaz, Reporting de Performance, Consultoria B2B, Estratégia de Upsell, Satisfação do Cliente, Planos de Ação.

---

## Quick Start

1.  **Mapear Pontos de Contato Essenciais:** Liste todas as interações do cliente com a consultoria, desde o onboarding até reuniões de revisão estratégica, workshops, e suporte técnico.
2.  **Identificar Indicadores-Chave de Engajamento:** Selecione métricas tangíveis como frequência de reuniões, abertura de e-mails, uso de plataformas (se aplicável), e entrega de relatórios.
3.  **Definir Escala de Pontuação Inicial:** Atribua um peso percentual a cada indicador, somando 100%, e estabeleça uma escala de 0 a 100 para o score geral.
4.  **Coletar Dados Iniciais:** Utilize o CRM ou planilhas para registrar os dados dos últimos 30 dias para 5-10 clientes representativos, calculando seus scores iniciais.
5.  **Classificar Clientes por Nível de Risco:** Agrupe os clientes em faixas como "Alto Risco" (0-40), "Atenção" (41-70) e "Saudável" (71-100) para visualização imediata.

---

## Core Workflows

### Workflow 1: Implementação e Monitoramento Contínuo de um Health Score Preditivo

Este workflow detalha a construção e a manutenção de um sistema de Client Health Score que não apenas reflete a situação atual, mas também antecipa riscos e oportunidades para clientes de consultoria.

**Passos Detalhados:**

1.  **Definição do Propósito do Score:**
    *   **Ação:** Esclarecer o objetivo primário do Client Health Score.
    *   **Exemplo:** "O objetivo é reduzir a taxa de churn em clientes de consultoria de marketing digital em 15% nos próximos 12 meses, identificando proativamente clientes insatisfeitos e oportunidades de expansão."

2.  **Seleção e Ponderação de Indicadores:**
    *   **Ação:** Escolher métricas específicas e atribuir pesos baseados na sua relevância para o sucesso e retenção do cliente.
    *   **Exemplo:**
        *   **Uso da Solução/Plataforma (se houver):** 20% (Ex: Frequência de login, funcionalidades utilizadas).
        *   **Engajamento com Consultor:** 25% (Ex: Frequência de reuniões agendadas vs. realizadas, taxa de resposta a e-mails).
        *   **Realização de Metas Acordadas (KPIs do projeto):** 35% (Ex: Atingimento de 80% das metas de tráfego, ROI de campanhas).
        *   **Satisfação (NPS/CSAT):** 10% (Ex: Último NPS > 7, CSAT > 4).
        *   **Renovação de Contrato/Upsell:** 10% (Ex: Discussões proativas sobre renovação, propostas de novos projetos).
    *   **Cálculo:** Cada indicador é pontuado de 0 a 10, multiplicado pelo peso e somado para o score final (0-100).

3.  **Integração de Dados e Automação:**
    *   **Ação:** Conectar fontes de dados (CRM, ferramentas de marketing, sistemas de BI) para coleta automática e cálculo do score.
    *   **Exemplo:** Integrar dados do HubSpot (interações), Google Analytics (uso da plataforma do cliente), e planilhas de KPI do projeto via Power BI para um painel de controle diário.
    *   **Configuração de Alertas:** Definir alertas automáticos no CRM (ex: Pipedrive, Salesforce) para quando um cliente atinge um score abaixo de 50, notificando o consultor responsável e o gerente de sucesso do cliente.

4.  **Definição de Faixas de Ação:**
    *   **Ação:** Estabelecer limites para cada nível de "saúde" do cliente e as ações correspondentes.
    *   **Exemplo:**
        *   **0-40 (Crítico):** Ação imediata: Reunião de emergência com o cliente, plano de recuperação de 7 dias, escalada para diretoria.
        *   **41-70 (Atenção):** Ação: Reunião de alinhamento proativa, revisão de escopo, oferta de treinamento adicional, envio de relatório de valor.
        *   **71-85 (Saudável):** Ação: Monitoramento contínuo, discussões sobre oportunidades de upsell/cross-sell.
        *   **86-100 (Promotor):** Ação: Solicitar depoimento, estudo de caso, indicação para novos clientes, reconhecimento público.

5.  **Revisão e Otimização Periódica:**
    *   **Ação:** Avaliar a eficácia do modelo de score e ajustá-lo com base nos resultados de retenção e feedback.
    *   **Exemplo:** A cada trimestre, analisar a correlação entre o health score e a taxa de churn/renovação. Se clientes com score 60 ainda estiverem fazendo churn, revisar os pesos ou adicionar novos indicadores.

### Workflow 2: Estratégias de Intervenção para Clientes com Health Score em Declínio

Este workflow foca nas ações proativas e reativas que uma consultoria deve tomar quando o Client Health Score de um cliente começa a apresentar sinais de declínio, visando a recuperação e a minimização do churn.

**Passos Detalhados:**

1.  **Detecção do Declínio e Análise Inicial:**
    *   **Ação:** O sistema de monitoramento detecta uma queda significativa no health score (ex: de 75 para 55 em uma semana).
    *   **Exemplo:** O dashboard de health score no Power BI mostra uma seta vermelha descendente para "Cliente Indústria X". O consultor acessa o histórico para verificar quais indicadores específicos caíram (ex: "Realização de Metas Acordadas" e "Engajamento com Consultor").

2.  **Coleta de Informações Qualitativas:**
    *   **Ação:** Realizar contato direto com o cliente para entender a causa raiz do declínio, evitando suposições.
    *   **Exemplo:** O consultor agenda uma chamada rápida com o ponto focal do Cliente Indústria X. Pergunta sobre desafios recentes, mudanças internas na equipe do cliente, percepção de valor dos serviços da consultoria, ou se há alguma expectativa não atendida.

3.  **Desenvolvimento de um Plano de Ação Personalizado:**
    *   **Ação:** Criar um plano de recuperação focado nas necessidades identificadas, com objetivos claros e prazos.
    *   **Exemplo:** Para o Cliente Indústria X, o plano pode incluir:
        *   **Objetivo:** Aumentar o score de "Realização de Metas" de 4 para 7 em 30 dias.
        *   **Ação 1:** Reunião estratégica focada em otimização de campanhas (18/09).
        *   **Ação 2:** Treinamento intensivo de 2 horas para a equipe interna do cliente sobre a ferramenta X (25/09).
        *   **Ação 3:** Envio de relatório semanal de progresso com foco nos KPIs críticos (a partir de 22/09).
        *   **Responsáveis:** Consultor Sênior (Ação 1, 3), Especialista de Produto (Ação 2).

4.  **Execução do Plano e Comunicação Contínua:**
    *   **Ação:** Implementar as ações do plano e manter o cliente informado sobre o progresso.
    *   **Exemplo:** O consultor executa as reuniões, o treinamento é ministrado e os relatórios semanais são enviados. A cada interação, o consultor reforça o valor entregue e pergunta sobre a percepção do cliente.

5.  **Monitoramento da Evolução do Health Score e Feedback:**
    *   **Ação:** Acompanhar de perto a evolução do health score e solicitar feedback sobre a eficácia das intervenções.
    *   **Exemplo:** O score do Cliente Indústria X é monitorado diariamente. Após 15 dias, o score de "Realização de Metas" subiu para 6, e o de "Engajamento" para 8. O consultor pergunta ao cliente como ele percebeu as últimas ações e se o valor da consultoria está mais claro. Se o score não melhorar, escalar para a gestão para uma revisão completa da conta.

---

## Templates

### Relatório Mensal de Health Score (Exemplo para Cliente "TechSolutions S.A.")

```markdown
# Relatório Mensal de Health Score - TechSolutions S.A.

**Período:** Agosto de 2024
**Consultor Responsável:** Ana Paula Martins
**Data de Emissão:** 02 de Setembro de 2024

---

## Score Geral de Saúde do Cliente: 78/100 (Saudável)
**Tendência:** Estável (Mês Anterior: 77/100)

---

## Detalhamento dos Indicadores

| Indicador | Pontuação (0-10) | Peso (%) | Contribuição para Score | Observações |
|:------------------------------------|:----------------:|:--------:|:------------------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------|
| Uso da Plataforma de Automação (MKT) | 8                | 20%      | 16                      | Aumento de 15% na frequência de login e uso de novas funcionalidades de segmentação. |
| Engajamento com a Consultoria       | 9                | 25%      | 22.5                    | Todas as reuniões agendadas realizadas; feedbacks rápidos e proativos. |
| Atingimento de Metas de Projeto     | 7                | 35%      | 24.5                    | Meta de leads qualificados atingida em 92%; meta de conversão em 88%. Houve um ligeiro atraso em uma campanha. |
| Satisfação (NPS/CSAT)               | 8                | 10%      | 8                       | Último CSAT registrou 4.2/5. Cliente demonstrou satisfação na reunião de follow-up. |
| Potencial de Renovação/Expansão     | 7                | 10%      | 7                       | Discussões iniciais sobre expansão para automação de vendas. |
| **Total**                           |                  | **100%** | **78**                  | |

---

## Análise de Destaques e Pontos de Atenção

**Destaques:**
*   **Engajamento Robusto:** A equipe da TechSolutions S.A. mantém um alto nível de engajamento, participando ativamente das discussões e implementando as recomendações.
*   **Aumento de Uso da Plataforma:** Observamos uma maior exploração da plataforma de automação, indicando que o valor da ferramenta está sendo percebido e utilizado.

**Pontos de Atenção:**
*   **Atingimento de Metas:** Apesar de bom, a meta de conversão ficou ligeiramente abaixo do esperado devido a um atraso na aprovação de peças criativas.

---

## Recomendações e Próximos Passos

1.  **Reunião de Otimização de Campanha (10/09):** Agendaremos uma sessão de 1 hora para revisar as campanhas em andamento e otimizar o processo de aprovação de conteúdo.
2.  **Proposta de Expansão (15/09):** Apresentaremos uma proposta detalhada para a integração da automação de vendas, alinhada às discussões iniciais de expansão.
3.  **Acompanhamento Diário:** Monitoramento contínuo dos resultados das campanhas para garantir o atingimento pleno das metas no próximo mês.

---

**Comentários Adicionais:** A TechSolutions S.A. continua sendo um parceiro estratégico. Nosso foco é garantir que todas as metas sejam superadas e que o valor da nossa consultoria seja maximizado.
```

### Script de Reunião de Alinhamento para Cliente em Risco (Exemplo para Cliente "VarejoConecta Ltda.")

```markdown
# Script de Reunião de Alinhamento - Cliente VarejoConecta Ltda.

**Contexto:** Cliente com Health Score em declínio (de 65 para 48) nas últimas duas semanas, principalmente devido a baixo engajamento e resultados abaixo do esperado em campanhas de e-mail marketing.
**Data:** 15 de Outubro de 2024
**Horário:** 10:00 AM
**Participantes:**
*   **Consultoria:** João Silva (Consultor Sênior), Camila Costa (Gerente de Sucesso do Cliente)
*   **VarejoConecta:** Roberto Almeida (Gerente de Marketing), Patrícia Nunes (Analista de E-mail Marketing)

---

## Agenda da Reunião (45 minutos)

1.  **Boas-vindas e Abertura (5 min)**
    *   João: "Olá, Roberto e Patrícia. Agradecemos a disponibilidade para esta reunião. Nosso objetivo hoje é alinhar expectativas e identificar oportunidades para fortalecer nossa parceria e, principalmente, os resultados para a VarejoConecta."

2.  **Revisão do Status Atual e Contexto (10 min)**
    *   Camila: "Como vocês sabem, acompanhamos de perto a performance e o engajamento com nossa consultoria. Nosso sistema de Health Score, que mede a saúde da parceria, indicou uma queda nos últimos dias. Especificamente, notamos uma diminuição na performance das campanhas de e-mail marketing e no engajamento geral. Gostaríamos de entender a perspectiva de vocês sobre isso."
    *   *Pausar para ouvir o cliente.*

3.  **Identificação de Desafios e Feedback do Cliente (15 min)**
    *   João: "Com base em nossa análise, percebemos que as taxas de abertura e clique das últimas campanhas de e-mail estão abaixo da média histórica, e que as reuniões de acompanhamento foram reagendadas algumas vezes. Roberto, Patrícia, existe algo específico que esteja impactando a equipe de vocês ou as campanhas? Há alguma expectativa que não estamos atendendo plenamente?"
    *   *Escuta ativa, fazer perguntas abertas, registrar pontos-chave.*
    *   *Exemplos de feedback esperados: "Temos tido problemas com a aprovação de conteúdo interno", "A equipe está sobrecarregada", "Não estamos vendo o ROI esperado da consultoria no e-mail marketing".*

4.  **Proposta de Plano de Ação e Próximos Passos (10 min)**
    *   Camila: "Compreendemos os pontos levantados. Para reverter essa situação e garantir que a VarejoConecta alcance seus objetivos, propomos o seguinte plano de ação com metas claras:"
        *   **Ação 1: Workshop de Otimização de E-mail Marketing:** Realizaremos um workshop de 2 horas na próxima semana (22/10) com a equipe de vocês para revisar as melhores práticas de segmentação, personalização e copy, com foco em aumentar as taxas de abertura e clique em 15%.
        *   **Ação 2: Reuniões de Alinhamento Semanais:** Voltaremos com nossas reuniões semanais de 30 minutos, todas as quartas-feiras às 14h, para garantir o acompanhamento próximo e a agilidade nas aprovações.
        *   **Ação 3: Relatório de Valor Focado:** Enviaremos um relatório quinzenal mais detalhado, destacando o impacto direto das nossas ações nos resultados de vendas e engajamento da VarejoConecta.
    *   João: "O que vocês acham dessas propostas? Há algo que gostariam de ajustar ou adicionar?"
    *   *Obter concordância do cliente.*

5.  **Fechamento e Próximos Encontros (5 min)**
    *   Camila: "Excelente. Então, para resumir: workshop dia 22/10, reuniões semanais às quartas, relatório quinzenal. Nosso objetivo é ver o Health Score da VarejoConecta retornar à faixa 'Saudável' (acima de 70) em 30 dias. Agradecemos a confiança e estamos à disposição para qualquer dúvida."
    *   João: "Enviaremos o convite para o workshop e o primeiro relatório detalhado ainda hoje. Contem conosco."
```

---

## Checklist

- [X] Identificar e listar todos os pontos de contato do cliente com a consultoria (reuniões, e-mails, relatórios, treinamentos).
- [X] Definir a lista final de indicadores que compõem o Client Health Score (mínimo 5, máximo 10).
- [X] Atribuir pesos percentuais a cada indicador, garantindo que a soma total seja 100%.
- [X] Estabelecer a metodologia de pontuação para cada indicador (ex: 0-10, 1-5 estrelas).
- [X] Definir as faixas de score (ex: Crítico, Atenção, Saudável, Promotor) e os gatilhos de alerta para cada uma.
- [X] Configurar a coleta de dados automatizada dos indicadores via CRM, BI ou outras ferramentas.
- [X] Criar um painel de controle (dashboard) visível para toda a equipe de consultoria e gestão.
- [X] Desenvolver um playbook de intervenção com ações específicas para cada faixa de risco do health score.
- [X] Treinar a equipe de consultores sobre como interpretar o health score e executar os planos de ação.
- [X] Agendar revisões trimestrais do modelo de health score para garantir sua relevância e eficácia.

---

## Métricas de Referência

| Métrica                         | Benchmark (Consultoria B2B) | Meta (Consultoria de Sucesso) |
|:--------------------------------|:----------------------------|:------------------------------|
| Taxa de Churn Anual             | 5% - 8%                     | < 3%                          |
| Net Promoter Score (NPS)        | 40 - 60                     | > 70                          |
| Client Lifetime Value (LTV)     | 3x - 5x CAC                 | > 6x CAC                      |
| Taxa de Renovação de Contrato   | 80% - 85%                   | > 95%                         |
| Taxa de Upsell/Cross-sell       | 15% - 25%                   | > 35%                         |
| Tempo Médio para Valor (TTV)    | 60 - 90 dias                | < 30 dias                     |

---

## Erros Comuns

1.  **Focar Exclusivamente em Dados Quantitativos**: Muitos modelos de health score ignoram o feedback qualitativo, como comentários diretos do cliente em reuniões, e-mails ou pesquisas abertas. Um cliente pode ter um bom uso da plataforma (quantitativo), mas estar insatisfeito com o suporte (qualitativo).
    *   **Como evitar**: Implementar pesquisas de satisfação curtas e frequentes, realizar reuniões de check-in sem pauta comercial e registrar todos os feedbacks qualitativos no CRM, atribuindo um peso a eles no score final.
    *   **Exemplo**: Um cliente com score de engajamento alto (reuniões frequentes) mas com um NPS recente de 6. A ação deve ser investigar a causa da insatisfação, não apenas celebrar o engajamento.

2.  **Modelo de Score Estático e Rígido**: Um health score que não se adapta à evolução do serviço, do cliente ou do mercado rapidamente se torna obsoleto. Necessidades e prioridades mudam.
    *   **Como evitar**: Realizar revisões trimestrais ou semestrais do modelo de health score, ajustando pesos, adicionando ou removendo indicadores com base nos resultados de retenção, feedback da equipe de consultoria e tendências do setor.
    *   **Exemplo**: Se a consultoria lançar um novo serviço ou plataforma, um novo indicador de "Adoção da Nova Funcionalidade" deve ser rapidamente adicionado ao modelo de score, com um peso inicial relevante.

3.  **Ausência de Planos de Ação Claros e Automatizados**: Ter um health score é inútil se a equipe não souber exatamente o que fazer quando um cliente entra em uma faixa de risco. A falta de um playbook de intervenção leva à paralisia ou a ações inconsistentes.
    *   **Como evitar**: Desenvolver um "playbook de sucesso do cliente" detalhado para cada faixa de score (Crítico, Atenção), com scripts de reunião, templates de e-mail, próximos passos definidos e responsáveis. Automatizar a criação de tarefas no CRM quando um cliente atinge um determinado score.
    *   **Exemplo**: Quando o score de um cliente cai para "Atenção", o CRM automaticamente gera uma tarefa para o consultor agendar uma "Reunião de Alinhamento Proativa" e sugere um template de pauta focado em valor e desafios.

---

## Dicas Avançadas

1.  **Segmentação de Health Score por Tier de Cliente:** Nem todo cliente tem a mesma complexidade ou valor para a consultoria. Desenvolva modelos de health score ligeiramente diferentes para clientes Enterprise, Mid-Market e SMB, ponderando indicadores que são mais críticos para cada segmento (ex: para Enterprise, "Engajamento da C-Level" pode ter peso maior).
    *   **Exemplo Prático:** Para clientes Enterprise, incluir "Participação em Comitês Estratégicos" como um indicador de alto peso. Para SMBs, focar mais em "Atingimento de Metas de Curto Prazo" e "Engajamento com Materiais de Suporte".

2.  **Previsão Preditiva de Churn Baseada em Declínio de Score:** Utilize a série histórica do health score para identificar padrões de declínio que historicamente precederam o churn. Ferramentas de análise de dados podem usar regressão logística ou modelos de Machine Learning para prever a probabilidade de churn com base na velocidade e profundidade da queda do score.
    *   **Exemplo Prático:** Se 80% dos clientes que tiveram uma queda de 20 pontos no health score em 30 dias fizeram churn nos 60 dias seguintes, automatize um alerta de "Alto Risco de Churn" com ações de intervenção mais agressivas.

3.  **Correlação do Health Score com a Rentabilidade do Cliente:** Cruza os dados do Client Health Score com as métricas de rentabilidade (margem de lucro, custo de atendimento) para entender se clientes "saudáveis" são de fato os mais rentáveis e se clientes "em risco" estão consumindo mais recursos do que geram. Isso ajuda a priorizar intervenções e a otimizar a alocação de recursos da consultoria.
    *   **Exemplo Prático:** Descobrir que clientes com score > 80 têm uma margem de lucro 15% maior. Ou que clientes em "Crítico" consomem 3x mais horas de suporte, justificando uma intervenção mais rápida para estabilizá-los ou reavaliar a parceria.

4.  **Uso de IA para Sugestão de Próximos Passos:** Integre o health score com um sistema de IA (como o próprio Claude) para sugerir automaticamente as melhores ações de intervenção com base no perfil do cliente, histórico de interações e os indicadores específicos que estão em baixa.
    *   **Exemplo Prático:** Quando um cliente entra na faixa "Atenção" devido a baixo "Engajamento com Consultor", a IA sugere: "Agendar reunião de revisão estratégica com foco em resultados (usar Template X)", "Enviar case study relevante da indústria (usar Template Y)", e "Oferecer treinamento extra sobre funcionalidade Z".

5.  **Gamificação do Health Score Internamente:** Crie um sistema de reconhecimento ou competição saudável entre os consultores ou equipes de sucesso do cliente com base na melhoria dos health scores de suas carteiras. Isso incentiva a proatividade e o foco no sucesso do cliente.
    *   **Exemplo Prático:** Publicar um ranking mensal dos consultores com a maior "Taxa de Recuperação de Score" (clientes que saíram da faixa de risco) ou "Maior Aumento Médio de Score" na carteira, com bônus ou reconhecimento para os melhores desempenhos.