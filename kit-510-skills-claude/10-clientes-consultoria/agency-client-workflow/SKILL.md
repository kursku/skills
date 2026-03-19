---
name: agency-client-workflow
description: "Agency Client Workflow — Skill especializada para agency client workflow"
license: MIT
metadata:
  version: 1.0.0
  author: Cafe Code AI
  category: 10-clientes-consultoria
  updated: 2026-03-01
---

# Agency Client Workflow

Esta skill capacita o Claude a otimizar e executar fluxos de trabalho de agências, abrangendo o ciclo completo de vida do cliente, desde o onboarding estratégico até a retenção proativa e gestão de performance.

---

## Keywords

Onboarding de Cliente, Retenção de Cliente, Health Score, QBR (Quarterly Business Review), Relatório de Performance, Gestão de Expectativas, Upsell & Cross-sell, Feedback Loop, SLA (Service Level Agreement), Plano de Sucesso do Cliente, P&L do Cliente, Churn Prevention.

---

## Quick Start

1.  **Implementar SLA no Onboarding**: Após a assinatura do contrato, envie o SLA detalhado e agende uma reunião de kick-off em até 48 horas para alinhar expectativas e processos.
2.  **Agendar QBRs Proativas**: Configure um calendário de Quarterly Business Reviews (QBRs) para cada cliente, com a primeira agendada para 30-45 dias após o onboarding inicial.
3.  **Configurar Dashboard de Performance**: Utilize ferramentas como Looker Studio (antigo Google Data Studio) ou Power BI para criar um dashboard automatizado de performance do cliente, acessível e atualizado em tempo real.
4.  **Calcular Health Score Inicial**: Desenvolva e aplique um framework de Health Score para cada novo cliente em 30 dias, utilizando métricas como engajamento, performance e satisfação.

---

## Core Workflows

### Workflow 1: Onboarding de Cliente Estratégico e Configuração Inicial

Este workflow detalha os passos para integrar um novo cliente de agência, garantindo que as bases para uma parceria de sucesso sejam estabelecidas desde o início.

1.  **Acionamento Pós-Contrato (0-24h)**:
    *   **Ação**: Após a assinatura do contrato, o time de vendas aciona a equipe de Sucesso do Cliente via CRM (ex: HubSpot, Salesforce) e envia um e-mail de boas-vindas automático (ver Template 1).
    *   **Exemplo**: O CRM dispara uma notificação para o CSM responsável e cria uma tarefa "Agendar Kick-off [Nome do Cliente]".
2.  **Reunião de Kick-off (24-48h)**:
    *   **Ação**: O CSM agiliza o agendamento da reunião de kick-off, focando no alinhamento de expectativas, escopo detalhado, definição de KPIs SMART (Specific, Measurable, Achievable, Relevant, Time-bound) e apresentação da equipe.
    *   **Exemplo**: Em vez de "Aumentar vendas", definir "Aumentar leads qualificadas em 15% nos próximos 90 dias com Custo por Lead (CPL) abaixo de R$10".
3.  **Coleta de Acessos e Ferramentas (2-5 dias)**:
    *   **Ação**: Utilizar um formulário padronizado para solicitar todos os acessos necessários (Google Analytics, Google Ads, Meta Business Suite, CRM, plataformas de e-commerce, etc.).
    *   **Exemplo**: Fornecer um link seguro (LastPass Enterprise ou similar) ou formulário criptografado para o cliente inserir credenciais, evitando a troca por e-mail.
4.  **Configuração de Dashboards e Relatórios (5-10 dias)**:
    *   **Ação**: Criar o dashboard de performance inicial do cliente no Looker Studio, Power BI ou outra ferramenta, conectando todas as fontes de dados relevantes.
    *   **Exemplo**: O dashboard deve incluir métricas de tráfego, conversão, custo por resultado e ROI, atualizando automaticamente.
5.  **Definição do Plano de Comunicação e SLA (7-14 dias)**:
    *   **Ação**: Apresentar o Acordo de Nível de Serviço (SLA) para tempos de resposta, canais de comunicação (Slack para urgências, e-mail para não urgências) e frequência de relatórios e reuniões.
    *   **Exemplo**: "Respostas a e-mails em até 24h úteis; respostas a mensagens no Slack em até 4h úteis durante o horário comercial."

### Workflow 2: Ciclo de Gestão de Performance, Retenção e Health Score

Este workflow descreve o processo contínuo de monitoramento, análise e comunicação com o cliente para garantir sua satisfação e promover a retenção e o crescimento.

1.  **Monitoramento Contínuo e Coleta de Dados (Diário/Semanal)**:
    *   **Ação**: As equipes de operação monitoram diariamente as campanhas e projetos, e os dados são coletados automaticamente via conectores (Supermetrics, Funnel.io) para o dashboard.
    *   **Exemplo**: Verificação diária de anomalias em Google Ads (queda brusca de impressões, aumento de CPC) ou performance de conteúdo em mídias sociais.
2.  **Cálculo e Análise do Health Score (Mensal)**:
    *   **Ação**: O Health Score do cliente é recalculado mensalmente com base em uma ponderação de métricas: Performance (40%), Engajamento (25%), Satisfação (15%), Financeiro (10%), Feedback (10%).
    *   **Exemplo**: Um cliente com queda de 20% na performance, baixa participação nas reuniões e atraso de pagamento pode ter seu Health Score cair de 85 para 55, acionando um alerta de risco.
3.  **Preparação da QBR (10-15 dias antes da reunião)**:
    *   **Ação**: O CSM, com o apoio do time de operações, consolida os dados do trimestre, analisa tendências, identifica pontos de sucesso, áreas de melhoria e oportunidades de crescimento. Prepara a apresentação da QBR (ver Template 2).
    *   **Exemplo**: Identificar que o Custo por Aquisição (CPA) aumentou em 10% devido a novos concorrentes e propor testes A/B em novas segmentações.
4.  **Reunião de QBR (Trimestral)**:
    *   **Ação**: Apresentação dos resultados do trimestre, discussão de desafios, validação de novas estratégias e alinhamento do plano para o próximo trimestre. Foco em valor e parceria estratégica.
    *   **Exemplo**: Apresentar um ROI de 4:1 no último trimestre, discutir o impacto de mudanças no algoritmo do Instagram e propor um plano de investimento em TikTok para o próximo ciclo.
5.  **Pós-QBR e Plano de Ação (1-3 dias após a reunião)**:
    *   **Ação**: Enviar a ata da reunião com os próximos passos, responsabilidades e prazos. Atualizar o plano de trabalho e o CRM com as decisões.
    *   **Exemplo**: O CSM envia um e-mail com a ata, que inclui "Implementar testes A/B na landing page X até [Data]" e "Pesquisar novas palavras-chave para campanha Y até [Data]".
6.  **Gerenciamento de Riscos e Oportunidades**:
    *   **Ação**: Clientes com Health Score abaixo de 60 acionam um "Plano de Recuperação" (reuniões semanais, foco em quick wins). Clientes com Health Score acima de 80 e potencial de crescimento são alvo de estratégias de upsell/cross-sell.
    *   **Exemplo**: Para um cliente em risco, propor uma auditoria gratuita de SEO ou um plano de conteúdo para 3 meses para demonstrar valor extra. Para um cliente de alto potencial, apresentar um novo serviço de automação de marketing.

---

## Templates

### Email de Boas-Vindas Pós-Contrato

```
Assunto: Bem-vindo(a) à [Nome da Agência] – Sua jornada de sucesso começa agora!

Olá [Nome do Cliente],

É com grande entusiasmo que a equipe da [Nome da Agência] te dá as boas-vindas! Estamos muito felizes em tê-lo(a) conosco e animados para construir resultados incríveis juntos.

Meu nome é [Seu Nome], e serei seu(sua) Gerente de Sucesso do Cliente (CSM) dedicado(a). Serei seu principal ponto de contato e guia estratégico durante toda a nossa parceria.

Para darmos o pontapé inicial com o pé direito, gostaria de agendar nossa reunião de Kick-off em breve. Nesta reunião, vamos alinhar expectativas, detalhar o escopo do projeto, definir os KPIs que iremos monitorar e apresentar a equipe que estará envolvida no seu projeto.

Por favor, me informe qual o melhor horário e data para você nos próximos dias (sugerimos [Data 1] às [Hora 1] ou [Data 2] às [Hora 2]). A reunião deve durar aproximadamente 60 minutos.

Enquanto isso, você pode acessar nosso "Kit de Boas-Vindas" com informações úteis sobre como trabalhamos, nosso SLA e os próximos passos: [Link para Kit de Boas-Vindas].

Caso tenha qualquer dúvida antes da nossa reunião, pode me contatar diretamente por este e-mail.

Estamos ansiosos para começar!

Atenciosamente,

[Seu Nome]
Gerente de Sucesso do Cliente
[Nome da Agência]
[Telefone da Agência]
[Site da Agência]
```

### Pauta de Reunião QBR (Quarterly Business Review)

```
**Relatório de Performance - QBR**

**Data:** [Data da Reunião]
**Cliente:** [Nome do Cliente]
**Período Analisado:** [Ex: 01/01/2024 - 31/03/2024]
**Participantes Agência:** [Nome do CSM], [Nome do Especialista de Operações]
**Participantes Cliente:** [Nome do Diretor/Gerente de Marketing], [Nome do CEO/Proprietário]

---

**1. Abertura e Alinhamento da Agenda (5 min)**
    *   Boas-vindas e breve contextualização dos objetivos da QBR.
    *   Confirmação da pauta e expectativa para a reunião.

**2. Revisão de Performance do Último Trimestre (30 min)**
    *   **Resultados vs. Metas:**
        *   **KPI 1 (Ex: Leads Qualificadas):** [Meta: 1000] vs. [Resultado: 950] (95% da meta)
        *   **KPI 2 (Ex: Custo por Lead - CPL):** [Meta: R$12] vs. [Resultado: R$11,50] (5% abaixo da meta)
        *   **KPI 3 (Ex: Tráfego Orgânico):** [Meta: 50.000 visitas] vs. [Resultado: 55.000 visitas] (10% acima da meta)
    *   **Análise de Canais e Campanhas:**
        *   Performance do Google Ads (Ex: CTR médio de 4.5%, ROAS de 3.2:1)
        *   Performance de SEO (Ex: 5 palavras-chave ranqueando no Top 3)
        *   Performance de Mídias Sociais (Ex: Engajamento 15% acima da média do setor)
    *   **Insights e Aprendizados:**
        *   Otimização de lances em campanhas de busca gerou CPL mais baixo.
        *   Conteúdo de blog focado em "como fazer" performou 30% melhor em tráfego orgânico.
        *   Campanha de remarketing teve baixo ROAS devido a criativos saturados.

**3. Desafios e Próximos Passos (20 min)**
    *   **Desafios Identificados:**
        *   Aumento da concorrência em leilões de Google Ads para termos específicos.
        *   Dificuldade em obter materiais de aprovação do cliente em tempo hábil.
        *   Queda no engajamento de e-mail marketing devido à base antiga.
    *   **Recomendações e Plano de Ação para o Próximo Trimestre:**
        *   **Ação 1:** Testar novas estratégias de lances e segmentações no Google Ads para o termo X. **Responsável:** [Nome Agência], **Prazo:** [Data].
        *   **Ação 2:** Implementar um calendário de entregas de materiais com o cliente para 15 dias de antecedência. **Responsável:** [Nome Cliente], **Prazo:** Imediato.
        *   **Ação 3:** Segmentar base de e-mail marketing e reativar contatos inativos com oferta exclusiva. **Responsável:** [Nome Agência], **Prazo:** [Data].

**4. Oportunidades de Crescimento e Inovação (15 min)**
    *   **Discussão:**
        *   Explorar o potencial de [Novo Serviço/Canal, ex: TikTok Ads ou Marketing de Influência].
        *   Proposta de teste A/B em Landing Pages para aumentar taxa de conversão em 10%.
        *   Apresentação de um novo recurso do mercado que pode beneficiar o cliente.
    *   **Alinhamento:** Priorização e alocação de recursos para as oportunidades.

**5. Feedback e Encerramento (5 min)**
    *   Espaço para perguntas e feedback do cliente.
    *   Revisão rápida dos principais pontos de ação e próximos passos.
    *   Agradecimento pela parceria.

---
**Próxima QBR agendada para:** [Data da Próxima QBR]
```

---

## Checklist

- [x] SLA (Service Level Agreement) assinado e comunicado a todas as partes (agência e cliente).
- [x] Acessos a todas as plataformas do cliente (Google Analytics, Google Ads, CRM, Redes Sociais, etc.) concedidos e testados.
- [x] Reunião de Kick-off realizada com pauta definida, ata distribuída e KPIs SMART validados.
- [x] Dashboard de performance inicial configurado (Looker Studio/Power BI) e compartilhado com o cliente.
- [x] Cronograma de QBRs (Quarterly Business Reviews) agendado para o ano corrente.
- [x] Health Score do cliente inicial calculado e registrado no CRM.
- [x] Plano de comunicação (canais, frequência, responsáveis) definido e acordado formalmente.
- [x] Contatos de emergência e fluxo de escalonamento de problemas definidos para ambas as partes.
- [x] Pesquisa de satisfação (NPS ou CSAT) agendada para 90 dias após o onboarding.
- [x] Ferramenta de gestão de projetos (Asana, Monday, Trello) configurada para o cliente com tarefas iniciais.

---

## Métricas de Referência

| Métrica                      | Benchmark (Agências) | Meta (Exemplo) |
|------------------------------|----------------------|----------------|
| **Churn Rate (Anual)**       | < 5% (Excelente)     | 3%             |
| **LTV:CAC Ratio**            | > 3:1                | 4:1            |
| **NPS (Net Promoter Score)** | > 50 (Excelente)     | 65             |
| **Taxa de Upsell/Cross-sell**| 15-20%               | 18%            |
| **Client Health Score Médio**| > 75 (Saudável)      | 80             |
| **MRR (Monthly Recurring Revenue) por Cliente** | Varia, mas ter um benchmark interno | R$ 15.000 |

---

## Erros Comuns

1.  **Falta de Alinhamento de Expectativas no Início**: Frequentemente, agências falham em definir claramente o que será entregue, quais são os KPIs realistas e qual o papel do cliente na parceria.
    *   **Como evitar**: Realize um kick-off detalhado, use o template de pauta de QBR para definir KPIs SMART desde o primeiro mês e formalize o SLA. Exemplo: Em vez de "vamos aumentar suas vendas", defina "aumentaremos as solicitações de orçamento via site em 20% nos próximos 6 meses, com um CPL máximo de R$25".
2.  **Comunicação Reativa e Não Proativa**: Esperar que o cliente entre em contato com problemas em vez de antecipar e comunicar proativamente os resultados, desafios e planos.
    *   **Como evitar**: Implemente QBRs regulares e obrigatórias, utilize dashboards automatizados e configure alertas proativos para a equipe de Sucesso do Cliente quando métricas-chave do cliente (ex: queda de ROI, baixo engajamento nas plataformas) apresentarem desvios. Exemplo: Receber um alerta quando o ROAS de uma campanha cair abaixo de 2:1 por 3 dias consecutivos e enviar um e-mail ao cliente com um plano de ação em 24h.
3.  **Não Medir o Health Score do Cliente de Forma Consistente**: Sem um sistema claro de pontuação de saúde do cliente, é difícil identificar clientes em risco de churn ou com alto potencial de upsell antes que seja tarde demais.
    *   **Como evitar**: Desenvolva e implemente um framework de Health Score com métricas ponderadas (performance, comunicação, financeiro, satisfação) e atualize-o mensalmente. Integre isso ao CRM para que o CSM tenha visibilidade rápida. Exemplo: Um Health Score abaixo de 60% deve automaticamente gerar uma tarefa para o CSM agendar uma "reunião de recuperação" com o cliente em 48h.

---

## Dicas Avançadas

1.  **Implementar um "Voice of the Customer" (VoC) Program Estruturado**: Vá além do NPS. Crie um programa que colete feedback de forma contínua em múltiplos pontos de contato (onboarding, QBRs, encerramento de projeto) e utilize esses insights para refinar seus serviços e processos.
    *   **Exemplo Prático**: Use ferramentas como Typeform ou Qualtrics para enviar pesquisas curtas após cada QBR e ao final de cada projeto, perguntando sobre a qualidade da comunicação, entrega de resultados e satisfação geral. Análise esses dados para identificar padrões e implementar melhorias sistêmicas, como "treinamento de soft skills para CSMs" se o feedback sobre comunicação for baixo.
2.  **Desenvolver um Framework de Previsão de Churn com Machine Learning**: Para agências com grande volume de clientes, utilize dados históricos (performance, engajamento, tickets de suporte, pagamentos) para treinar um modelo de Machine Learning que preveja a probabilidade de churn de cada cliente.
    *   **Exemplo Prático**: Um modelo pode identificar que clientes que reduzem o engajamento em reuniões em 30% e têm uma queda de 15% no ROI nos últimos 2 meses têm 70% de chance de churn nos próximos 90 dias. Isso permite intervenção proativa do CSM com ofertas personalizadas ou planos de recuperação antes que o cliente decida sair.
3.  **Criar um Programa de Advocacy para Clientes Satisfeitos**: Transforme seus clientes mais leais e satisfeitos em defensores da sua marca, incentivando depoimentos, estudos de caso e indicações.
    *   **Exemplo Prático**: Identifique clientes com Health Score > 90 e NPS > 9 (Promotores). Ofereça um incentivo (ex: desconto no próximo serviço, convite para evento exclusivo) em troca de um vídeo-depoimento ou participação em um estudo de caso detalhado. Crie um programa de indicação com comissão para cada novo cliente trazido.
4.  **Automação Inteligente de Relatórios e Alertas de Performance**: Use APIs e ferramentas de automação (Zapier, Make.com) para ir além dos dashboards e criar alertas contextuais que acionam ações específicas da equipe.
    *   **Exemplo Prático**: Configure um Zapier para que, se o CPL de uma campanha do Google Ads exceder R$30 por mais de 24 horas, ele automaticamente envie uma notificação para o canal Slack do gerente de tráfego, crie uma tarefa no Asana para "Otimizar CPL na campanha X" e envie um e-mail informativo (não alarmista) para o cliente sobre o monitoramento e ações em andamento.
5.  **Segmentação de Clientes por Valor e Potencial (Tiers)**: Classifique seus clientes em diferentes "tiers" (ex: Platina, Ouro, Prata) com base no MRR, LTV e potencial de crescimento. Adapte o nível de serviço, frequência de contato e recursos dedicados a cada tier.
    *   **Exemplo Prático**: Clientes "Platina" (MRR > R$50k) recebem QBRs mensais, acesso direto ao CEO da agência e alocação de um time de especialistas dedicado. Clientes "Prata" (MRR < R$10k) podem ter QBRs trimestrais e acesso a um pool de especialistas, garantindo que o custo de atendimento seja proporcional ao valor do cliente.