---
name: red-flag-detection
description: "Red Flag Detection — Skill especializada para red flag detection"
license: MIT
metadata:
  version: 1.0.0
  author: Cafe Code AI
  category: 10-clientes-consultoria
  updated: 2026-03-01
---

# Red Flag Detection

Esta skill capacita o Claude a identificar proativamente sinais de alerta em clientes de consultoria para mitigar riscos de churn, insatisfação e perda de receita.

---

## Keywords

*   Prevenção de Churn
*   Client Health Score
*   Desengajamento do Cliente
*   Scope Creep
*   Desalinhamento de Expectativas
*   Relatórios de Progresso
*   Feedback Negativo
*   Métricas de Engajamento
*   Retenção de Clientes
*   Sinais de Risco
*   Valor Percebido
*   Escalação de Clientes

---

## Quick Start

1.  **Configure Monitoramento de Frequência de Interação**: Implemente um sistema para registrar e alertar sobre quedas na frequência de reuniões executivas e operacionais em 20% ou mais no último mês.
2.  **Automatize o Tracking de Abertura de Relatórios**: Utilize ferramentas de e-mail marketing ou um portal do cliente para monitorar a taxa de abertura de relatórios de progresso mensais, sinalizando quedas abaixo de 50%.
3.  **Implemente Pesquisas de Satisfação Pós-Entrega**: Automatize o envio de micro-pesquisas (ex: CSAT, NPS) após a conclusão de cada milestone ou entrega principal.
4.  **Monitore Menções de Concorrentes**: Configure alertas de busca (ex: Google Alerts, ferramentas de social listening) para o nome do cliente em conjunto com nomes de concorrentes diretos da consultoria.

---

## Core Workflows

### Workflow 1: Análise Preditiva de Churn por Comportamento de Engajamento

Este workflow foca em identificar clientes em risco de churn ou insatisfação através da observação de mudanças sutis no padrão de engajamento e interação.

*   **Passo 1: Monitoramento da Frequência de Interação Executiva**:
    *   **Ação**: Utilize o CRM (ex: Salesforce, HubSpot) para registrar todas as reuniões agendadas e realizadas com stakeholders chave do cliente (Sponsor, Diretores, Gerentes). Configure um dashboard para exibir a frequência de interações ao longo do tempo.
    *   **Exemplo Concreto**: Cliente "Alfa Solutions" tinha uma média de 3 reuniões semanais com o Sponsor nos últimos 6 meses. No último mês, essa média caiu para 1 reunião a cada duas semanas. A participação do Sponsor em reuniões operacionais também diminuiu de 80% para 30%.
    *   **Red Flag**: Queda de 50% ou mais na frequência de reuniões com stakeholders executivos ou redução significativa na sua participação ativa.

*   **Passo 2: Análise da Consumo de Entregáveis e Informações**:
    *   **Ação**: Monitore a taxa de abertura de e-mails com relatórios de progresso, acesso ao portal do cliente (se houver) para download de documentos, e visualização de dashboards de BI compartilhados.
    *   **Exemplo Concreto**: Para o Cliente "Beta Tech", a taxa de abertura do relatório de desempenho mensal via e-mail era consistentemente de 85%. Nos últimos dois meses, essa taxa caiu para 35%. O acesso ao portal de documentos também mostra uma diminuição de 60% nas visualizações de novos materiais.
    *   **Red Flag**: Queda sustentada de 40% ou mais na taxa de abertura de comunicações críticas ou no consumo de informações relevantes do projeto.

*   **Passo 3: Detecção de Delegação Excessiva ou Distanciamento**:
    *   **Ação**: Observe mudanças no padrão de quem participa das reuniões, quem toma decisões e quem responde às comunicações.
    *   **Exemplo Concreto**: O Cliente "Gamma Corp" costumava ter o Diretor de Marketing como principal ponto de contato e decisor. Agora, ele delegou a maioria das interações e decisões para um analista júnior, e suas respostas por e-mail demoram mais de 72 horas, quando antes eram 24 horas.
    *   **Red Flag**: Transferência de responsabilidades chave para níveis hierárquicos inferiores sem comunicação prévia ou aumento significativo no tempo de resposta de decisores.

*   **Passo 4: Ação Proativa e Reunião de Alinhamento**:
    *   **Ação**: Ao identificar uma ou mais Red Flags, o gerente de conta deve agendar imediatamente uma reunião de "Alinhamento Estratégico" com o Sponsor, não como uma reunião de "problemas", mas de "garantia de valor".
    *   **Exemplo Concreto**: Para "Alfa Solutions", o gerente de conta enviou um e-mail com o título "Alinhamento Estratégico: Garantindo o Máximo Valor para Alfa Solutions" e agendou uma reunião para discutir os próximos passos e oportunidades, sem mencionar diretamente as Red Flags iniciais, mas com o objetivo de reengajar e entender a situação.

### Workflow 2: Identificação de Desalinhamento de Expectativas em Entregas

Este workflow visa detectar onde as expectativas do cliente podem estar se desviando da realidade das entregas, prevenindo frustrações e atritos.

*   **Passo 1: Monitoramento de Feedback Qualitativo e Expressões de Frustração**:
    *   **Ação**: Colete e analise comentários verbais em reuniões, e-mails e anotações. Procure por frases que indiquem insatisfação ou questionamento do valor.
    *   **Exemplo Concreto**: Em e-mails do Cliente "Delta Holdings", as frases "Não estamos vendo o ROI esperado", "As funcionalidades entregues são úteis, mas não resolvem nosso problema central", e "Precisamos de algo mais robusto" começaram a aparecer com frequência. Em reuniões, a equipe do cliente demonstrava menos entusiasmo e fazia perguntas mais críticas.
    *   **Red Flag**: Aumento de 25% na ocorrência de termos negativos ou de questionamento de valor em comunicações registradas.

*   **Passo 2: Análise de Solicitações de Mudança de Escopo (Scope Creep) Não Faturadas**:
    *   **Ação**: Registre todas as solicitações de alteração ou adição de escopo, comparando-as com o que foi contratado. Verifique se há um volume crescente de solicitações não formalizadas ou não faturadas.
    *   **Exemplo Concreto**: O Cliente "Epsilon Services" inicialmente contratou um projeto de otimização de campanhas de Google Ads. Nas últimas três semanas, solicitou três vezes a inclusão de otimizações para Facebook Ads sem discussão de aditivo contratual, ou pediu relatórios customizados que demandam 10+ horas de trabalho adicionais por mês.
    *   **Red Flag**: Mais de 2 solicitações de alteração de escopo que excedem 5% do esforço inicial do projeto sem formalização de aditivo contratual no último mês.

*   **Passo 3: Comparação de KPIs Reportados vs. Expectativa Inicial e Reuniões de Revisão**:
    *   **Ação**: Revise periodicamente o documento de Proposta/Contrato com os KPIs acordados. Compare os resultados reportados nos relatórios de progresso com as metas iniciais. Realize reuniões de "Revisão de Valor" a cada 3 meses.
    *   **Exemplo Concreto**: O Cliente "Zeta Systems" contratou para uma "redução de custo operacional de 20% em 6 meses". Após 4 meses, os relatórios mostram uma redução de apenas 8%. Em uma reunião de revisão, o cliente expressou que "a expectativa era de um impacto muito maior a esta altura".
    *   **Red Flag**: Discrepância de 50% ou mais entre o progresso atual dos KPIs e a meta proporcional ao tempo decorrido no projeto.

*   **Passo 4: Desenvolvimento e Implementação de um Plano de Recuperação**:
    *   **Ação**: Crie um plano de ação detalhado para re-alinhar as expectativas, ajustar o escopo (se necessário e faturado), e comunicar um caminho claro para atingir o valor prometido.
    *   **Exemplo Concreto**: Para "Delta Holdings", foi proposta uma sessão de workshop intensivo para revalidar os problemas centrais e adaptar as soluções, resultando em um aditivo contratual para um módulo extra de "Análise de Sentimento do Cliente" que realmente endereçava a dor primária não totalmente coberta inicialmente.

---

## Templates

### Template de Relatório de Health Score do Cliente

```
Relatório de Health Score do Cliente

**Cliente:** Omega Corp
**Data:** 15/10/2025
**Analista:** Ana Paula Silva
**Período de Análise:** Últimos 90 dias

**1. Métricas de Engajamento:**
*   **Frequência de Reuniões Executivas (Sponsor):** 1/mês (Meta: 2/mês) - Amarelo (Queda de 50% vs. média anterior)
*   **Taxa de Abertura de Relatórios Mensais:** 35% (Meta: 70%) - Vermelho (Queda de 55% vs. média anterior)
*   **Participação em Workshops/Treinamentos:** 1/4 (Meta: 3/4) - Amarelo
*   **Tempo Médio de Resposta do Cliente:** 48h (Meta: 24h) - Amarelo

**2. Métricas de Valor Percebido e Satisfação:**
*   **ROI Projetado vs. Realizado (até o momento):** 60% (Meta: 90%) - Amarelo (Valor entregue ainda não claro)
*   **Feedback Qualitativo (Últimas Interações):** "Processo lento", "Resultados não tangíveis", "Esperava mais velocidade" - Vermelho
*   **NPS (Última Pesquisa, 01/09/2025):** 4 (Meta: 8+) - Vermelho (Detrator)
*   **Número de Solicitações de "Scope Creep" Não Faturadas:** 3 - Amarelo

**3. Métricas de Risco e Estabilidade:**
*   **Atrasos Críticos em Entregas (Nº de Ocorrências):** 1 (de 5 milestones) - Amarelo (Atraso de 7 dias na entrega X)
*   **Contato com Concorrentes (Monitorado):** Sim (mencionado em notícia local sobre evento) - Vermelho
*   **Mudança de Sponsor/Decisor Chave:** Sim (Novo Diretor de TI assumiu há 2 semanas) - Amarelo
*   **Orçamento do Projeto (Utilização vs. Plano):** 70% utilizado, 50% do projeto concluído - Amarelo (Possível estouro ou desaceleração)

**Health Score Total (Escala 1-5, onde 1=Crítico, 5=Excelente):** 2.1/5 (Vermelho)

**Análise Sumária:**
O cliente Omega Corp apresenta múltiplos sinais de alerta. O engajamento diminuiu drasticamente, o valor percebido é baixo, e há riscos iminentes de insatisfação e possível churn. A mudança de liderança e o contato com concorrentes agravam a situação.

**Ações Recomendadas (Urgentes):**
1.  **Reunião Imediata com o Novo Diretor de TI:** Agendar um alinhamento estratégico para entender suas prioridades e expectativas.
2.  **Plano de Ação de Valor Imediato:** Propor uma entrega rápida e de alto impacto nos próximos 15 dias para demonstrar valor tangível.
3.  **Revisão Detalhada de KPIs:** Re-avaliar e comunicar de forma transparente o progresso dos KPIs, ajustando expectativas se necessário.
4.  **Re-engajamento da Equipe Cliente:** Propor um workshop interativo para revitalizar o entusiasmo e a participação.
```

### Script de Reunião de Alinhamento Estratégico para Cliente em Risco

```
Assunto: Reunião de Alinhamento Estratégico: Otimizando o Sucesso com [Nome do Cliente]

**Participantes:**
*   [Nome do Sponsor Cliente] (Ex: João Silva, Diretor de Marketing)
*   [Nome Gerente de Conta] (Ex: Mariana Costa)
*   [Nome Consultor Líder] (Ex: Rafael Mendes)
**Data:** 20/10/2025
**Horário:** 10:00 AM
**Local:** Chamada de Vídeo (Zoom)

**Agenda Sugerida:**

**1. Abertura e Contexto (5 min)**
    *   **Mariana:** "Bom dia, João. Agradecemos muito seu tempo. Nosso objetivo hoje é realizar um alinhamento estratégico para garantir que o projeto [Nome do Projeto, ex: Otimização de Processos Internos] esteja no caminho certo para entregar o máximo valor para [Nome do Cliente] e para seus objetivos em [Área chave, ex: redução de custos operacionais]."
    *   "Queremos garantir que estamos totalmente conectados com suas prioridades atuais e que nossa parceria continue gerando resultados excepcionais."

**2. Revisão Rápida dos Pontos Positivos e Conquistas (10 min)**
    *   **Rafael:** "João, gostaria de destacar os avanços significativos que tivemos em [Ponto Positivo 1, ex: Mapeamento de 80% dos processos críticos] e o sucesso da implementação do [Ponto Positivo 2, ex: Novo sistema de gestão de tarefas para a equipe de vendas]. O feedback inicial da sua equipe sobre [Ponto Positivo 2] tem sido muito bom."
    *   "Esses resultados são fruto do nosso trabalho conjunto e do engajamento da sua equipe."

**3. Discussão de Observações e Oportunidades de Otimização (20 min)**
    *   **Mariana:** "João, nos últimos tempos, percebemos que a frequência de nossas reuniões de alinhamento executivo diminuiu um pouco [ou: o tempo de resposta em algumas decisões tem sido mais longo / a participação em certos workshops]. Gostaríamos de entender se há alguma mudança de prioridade interna em [Nome do Cliente] ou se há algo que possamos ajustar em nossa abordagem para otimizar a forma como nos engajamos e garantimos que você esteja sempre atualizado e com as decisões rápidas."
    *   "Além disso, em relação ao [Entregável X, ex: Relatório de Impacto do Q3], tivemos alguns feedbacks que indicavam que o valor esperado talvez não estivesse totalmente claro. Poderia nos dar mais detalhes sobre o que está faltando ou o que poderíamos fazer para tornar o impacto mais evidente e tangível para você e sua liderança?"
    *   "Houve alguma mudança no cenário de mercado ou nos objetivos estratégicos de [Nome do Cliente] que devemos estar cientes para refinar nosso foco?"

**4. Propostas de Ações e Próximos Passos (15 min)**
    *   **Rafael:** "Com base em nossa conversa, e para garantir que superemos suas expectativas, sugiro algumas ações. Poderíamos [Proposta 1, ex: Agendar uma sessão de imersão de 2 horas focada exclusivamente no ROI do projeto para sua liderança, com dados atualizados] e [Proposta 2, ex: Implementar um dashboard de KPIs semanal simplificado para a equipe executiva, com os 3 indicadores mais críticos para você]."
    *   "Gostaríamos de discutir qual seria a melhor forma de prosseguir para garantir que suas expectativas sejam totalmente atendidas e que o valor do nosso trabalho seja maximizado."
    *   "Há algo mais que possamos fazer, ou alguma ideia que você tenha, para fortalecer ainda mais nossa parceria?"

**5. Encerramento (5 min)**
    *   **Mariana:** "João, agradecemos muito sua honestidade e abertura. Sua perspectiva é fundamental para nós. Nosso compromisso é total com o sucesso de [Nome do Cliente]. Enviaremos um resumo dos próximos passos acordados em breve."
    *   "Manteremos o contato e daremos o suporte necessário para que alcancemos os resultados que você espera."
```

---

## Checklist

- [x] Frequência de reuniões com o sponsor principal estável (mínimo mensal)?
- [x] Taxa de abertura de relatórios de progresso ou acesso a dashboards acima de 60%?
- [x] Feedback qualitativo (e-mails, reuniões) predominantemente positivo ou neutro?
- [x] Nenhuma solicitação de "scope creep" significativa não faturada ou formalizada?
- [x] Nenhum atraso crítico em entregas ou milestones do projeto nos últimos 30 dias?
- [x] Health Score do cliente calculado (se aplicável) acima de 3.5/5?
- [x] Nenhum contato direto ou menção do cliente com concorrentes monitorado?
- [x] Sponsor principal ainda ativamente engajado e tomando decisões chave?
- [x] Orçamento do projeto sendo utilizado conforme o planejado sem fricções?
- [x] Nenhum aumento significativo no tempo de resposta do cliente para informações críticas?
- [x] Equipe do cliente expressando satisfação com a qualidade da comunicação?
- [x] Ausência de escaladas formais ou reclamações diretas nos últimos 90 dias?

---

## Métricas de Referência

| Métrica                         | Benchmark (Consultoria B2B) | Meta (Aspiracional) |
|---------------------------------|-----------------------------|---------------------|
| Health Score do Cliente         | > 3.5/5 (Amarelo)           | > 4.2/5 (Verde)     |
| Taxa de Churn Anual             | < 15%                       | < 5%                |
| Frequência de Reuniões Exec.    | Mín. 1/mês                  | Mín. 2/mês          |
| NPS (Net Promoter Score)        | > 50% (Promotores)          | > 70% (Promotores)  |
| % Entregas Atrasadas            | < 10%                       | < 2%                |
| Tempo Médio de Resposta Cliente | < 48 horas                  | < 24 horas          |

---

## Erros Comuns

1.  **Ignorar pequenas mudanças no comportamento do cliente**: Pequenos atrasos em respostas de e-mail, menor engajamento em reuniões, ou delegação para níveis hierárquicos menores podem ser os primeiros sinais de insatisfação.
    *   **Como evitar**: Implementar um sistema de monitoramento de engajamento no CRM que registre a frequência e qualidade das interações. Configurar alertas para desvios de padrões estabelecidos. Ex: Um alerta dispara quando o tempo médio de resposta do Sponsor excede 48 horas por três semanas consecutivas.
2.  **Focar apenas em métricas financeiras**: Um projeto pode estar pagando em dia, mas o cliente pode estar insatisfeito com o valor percebido ou a qualidade das entregas, procurando alternativas silenciosamente.
    *   **Como evitar**: Desenvolver e utilizar um Health Score multifacetado que inclua não apenas a pontualidade dos pagamentos, mas também métricas de engajamento, valor percebido, feedback qualitativo e uso de entregáveis. Ex: O Health Score do cliente "TechSolutions" era 4/5 (verde) no quesito financeiro, mas 2/5 (vermelho) no quesito engajamento e feedback.
3.  **Não documentar e re-alinhar expectativas constantemente**: A falta de um registro claro do escopo inicial, dos KPIs acordados e das solicitações de mudança pode levar a disputas sobre o que foi prometido e o que foi entregue.
    *   **Como evitar**: Manter um registro detalhado do contrato, Declaração de Trabalho (SOW), KPIs acordados e todas as solicitações de mudança formalizadas (Change Requests). Realizar reuniões trimestrais de "Revisão de Valor e Escopo" para re-validar e ajustar expectativas. Ex: Para o Cliente "RetailFlow", cada alteração de escopo foi formalizada com um aditivo contratual, evitando discussões sobre horas extras não previstas.

---

## Dicas Avançadas

1.  **Análise de Sentimento em Comunicações**: Utilize ferramentas de Processamento de Linguagem Natural (NLP) para analisar o tom e o sentimento de e-mails, transcrições de reuniões e feedback em texto. Isso pode revelar frustrações ou preocupações antes que sejam verbalizadas diretamente. Ex: Detectar um aumento de 30% no uso de palavras como "frustrado", "preocupado", "desapontado" em comunicações do cliente.
2.  **Mapeamento de Stakeholders e Análise de Influência**: Crie um mapa dinâmico de stakeholders do cliente, identificando seus níveis de influência, engajamento e atitude em relação ao projeto. Monitore mudanças na estrutura organizacional ou a entrada de novos decisores que possam ter visões diferentes. Ex: Um novo Diretor de Vendas pode questionar o investimento em um projeto de marketing digital que ele não iniciou.
3.  **Projeção de Churn via Análise de Cohorts**: Agrupe clientes por características semelhantes (indústria, tamanho, serviço contratado) e analise o histórico de churn desses cohorts. Identifique padrões de comportamento em clientes atuais que se assemelham a clientes que churnaram no passado. Ex: Clientes de SaaS no setor de saúde, com menos de 100 usuários ativos e que reduziram o uso em 20% nos últimos 3 meses, têm uma taxa de churn de 40% em 6 meses.
4.  **Implementação de um "Early Warning System" com Triggers Automatizados**: Configure alertas em ferramentas de CRM, BI ou automação de marketing que disparam notificações para o gerente de conta quando uma Red Flag específica é acionada. Ex: Um alerta automático é enviado quando o NPS de um cliente cai abaixo de 6, ou quando não há interação registrada com o Sponsor há mais de 30 dias.
5.  **Criação de um "Playbook de Recuperação" para cada tipo de Red Flag**: Desenvolva planos de ação específicos e pré-aprovados para as Red Flags mais comuns. Isso inclui scripts de reunião, templates de e-mail, recursos de valor agregado para apresentar e um cronograma de ações para uma resposta rápida e consistente da equipe de consultoria. Ex: Um playbook para "Cliente com baixo engajamento" incluiria um script de reunião de alinhamento estratégico e uma proposta de workshop de valor imediato.