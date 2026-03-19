---
name: client-satisfaction-survey
description: "Client Satisfaction Survey — Skill especializada para client satisfaction survey"
license: MIT
metadata:
  version: 1.0.0
  author: Cafe Code AI
  category: 10-clientes-consultoria
  updated: 2026-03-01
---

# Client Satisfaction Survey

Esta skill capacita o Claude a projetar, implementar e analisar pesquisas de satisfação de clientes para empresas de consultoria, gerando insights acionáveis para retenção e melhoria contínua.

---

## Keywords

NPS, CSAT, CES, Pesquisa de Satisfação, Feedback de Clientes, Jornada do Cliente, Análise de Sentimento, Retenção de Clientes, Consultoria B2B, Experiência do Cliente, Gestão de Clientes, Onboarding de Clientes.

---

## Quick Start

1.  Configure uma pesquisa de Net Promoter Score (NPS) no SurveyMonkey, direcionada aos clientes que concluíram projetos há 72 horas.
2.  Envie o convite para a pesquisa via e-mail automático, utilizando o template de convite fornecido, personalizado com o nome do cliente e do projeto.
3.  Monitore as respostas diariamente, focando em detratores (notas 0-6) para um follow-up imediato.
4.  Agende um contato telefônico com cada detrator em até 24 horas após a resposta para fechar o loop de feedback.

---

## Core Workflows

### Workflow 1: Implementação de Pesquisa Transacional Pós-Entrega de Projeto

Este workflow detalha a criação e lançamento de uma pesquisa de satisfação focada em um ponto específico da jornada do cliente, como a conclusão de um projeto de consultoria, visando feedback imediato sobre a experiência recente.

*   **Passo 1: Seleção da Métrica Principal e Ferramenta.**
    *   Para avaliar a lealdade e a probabilidade de recomendação pós-projeto, o Net Promoter Score (NPS) é a métrica mais eficaz. Escolha uma ferramenta robusta para gestão de pesquisas, como Qualtrics, SurveyMonkey ou Typeform, que permita automação e relatórios detalhados. Configure a questão principal "Em uma escala de 0 a 10, qual a probabilidade de você recomendar a [Nome da Consultoria] a um amigo ou colega?" como o ponto central do questionário.
    *   *Exemplo Concreto*: A Consultoria Alfa utiliza o NPS para medir a satisfação final. A pergunta é configurada em um painel do Qualtrics, garantindo a coleta de dados anonimizada e a categorização automática dos clientes em promotores, passivos e detratores.

*   **Passo 2: Definição do Gatilho e Timing de Envio.**
    *   A pesquisa transacional deve ser enviada em um momento estratégico, próximo à experiência avaliada, mas com um pequeno intervalo para o cliente processar os resultados. Um intervalo de 72 horas (3 dias) após a marcação da conclusão oficial do projeto no CRM (e.g., Salesforce, HubSpot) ou após a reunião de entrega final é ideal. Isso garante que a experiência ainda esteja fresca na memória do cliente.
    *   *Exemplo Concreto*: Após o status de um projeto na Consultoria Beta mudar de "Em Andamento" para "Concluído" no Salesforce, um gatilho automático é acionado para que o e-mail de convite para a pesquisa de NPS seja enviado ao contato principal do cliente 3 dias depois.

*   **Passo 3: Criação do Questionário Simplificado e Relevante.**
    *   Mantenha o questionário conciso e focado, evitando fadiga de pesquisa. Além da pergunta NPS, inclua no máximo duas perguntas abertas qualitativas e uma de esforço. Perguntas como "Qual o principal motivo para sua nota?" e "Quão fácil foi trabalhar com nossa equipe neste projeto? (Escala de 1 a 5)" coletam feedback valioso sem sobrecarregar o respondente.
    *   *Exemplo Concreto*: A Consultoria Gama desenvolveu um questionário com apenas 4 perguntas: NPS, "Qual o principal motivo?", "O que poderíamos ter feito diferente?" e "Qual o impacto do projeto para sua empresa?". A taxa de resposta aumentou de 15% para 28% após essa simplificação.

*   **Passo 4: Automação do Envio e Personalização.**
    *   Integre a ferramenta de pesquisa com seu CRM ou plataforma de automação de marketing. Isso permite que os convites sejam enviados automaticamente, com personalização do nome do cliente, nome do projeto e nome do consultor ou gerente de sucesso do cliente. O remetente do e-mail deve ser reconhecível e amigável (e.g., "Sucesso do Cliente @ [Nome da Consultoria]").
    *   *Exemplo Concreto*: O time de Sucesso do Cliente da Consultoria Delta configura um fluxo no HubSpot que, ao identificar a conclusão do projeto, envia um e-mail com o template pré-aprovado, contendo variáveis como `{{client.firstName}}` e `{{project.name}}`, garantindo que o convite pareça pessoal.

*   **Passo 5: Monitoramento Contínuo e Alertas de Feedback Negativo.**
    *   Configure dashboards e alertas na ferramenta de pesquisa. Monitore as respostas em tempo real, com atenção especial para notas baixas (detratores, 0-6). Alertas devem ser enviados imediatamente para o gerente de contas ou líder de equipe responsável, permitindo uma ação rápida.
    *   *Exemplo Concreto*: Se um cliente da Consultoria Épsilon atribui um NPS de 5, um alerta é enviado via Slack para o gerente de contas, que é instruído a contatar o cliente em até 4 horas para entender a insatisfação e buscar uma solução.

### Workflow 2: Análise de Dados e Plano de Ação para Melhoria Contínua

Este workflow descreve como transformar o feedback bruto das pesquisas em insights acionáveis e planos de melhoria concretos, garantindo que o ciclo de feedback seja fechado e resulte em ações reais.

*   **Passo 1: Segmentação e Cálculo Detalhado das Métricas.**
    *   Não se limite ao NPS geral. Calcule o NPS, CSAT e CES por segmentos de clientes (e.g., tamanho da empresa, indústria), por consultor ou equipe, por tipo de projeto (e.g., estratégia, implantação de software, treinamento) e por período (mensal, trimestral). Isso revela padrões e pontos específicos de melhoria.
    *   *Exemplo Concreto*: A Consultoria Zeta calcula o NPS trimestralmente, segmentando os resultados por cada um dos três diretores de consultoria e por projetos de "M&A" vs. "Otimização de Processos". Isso revelou que projetos de M&A tinham um NPS consistentemente mais baixo, indicando a necessidade de revisar a metodologia nessa área.

*   **Passo 2: Análise Qualitativa Aprofundada dos Comentários.**
    *   Utilize as respostas abertas para identificar temas recorrentes e o sentimento por trás do feedback. Crie categorias para os comentários (e.g., "Comunicação", "Prazo", "Qualidade da Entrega", "Custo-benefício", "Expertise da Equipe"). Ferramentas de análise de texto ou até mesmo uma análise manual com planilhas e codificação podem ser empregadas para quantificar a frequência desses temas.
    *   *Exemplo Concreto*: Ao analisar 200 comentários de detratores, a Consultoria Eta identificou que 65% mencionavam "atrasos na comunicação" e 40% "falta de alinhamento de expectativas". Esses temas tornaram-se prioridade para o plano de ação.

*   **Passo 3: Priorização de Melhorias e Criação de Plano de Ação.**
    *   Com base nos temas qualitativos e nas métricas segmentadas, priorize as áreas de melhoria. Crie um plano de ação claro com ações específicas, responsáveis e prazos. Um problema identificado por detratores deve ser tratado com urgência.
    *   *Exemplo Concreto*: Após identificar a "comunicação" como principal dor, a Consultoria Teta estabeleceu como ação "Implementar reuniões de status semanais obrigatórias com pauta e ata padronizadas em todos os projetos de consultoria", com "Gerentes de Projeto" como responsáveis e prazo de "30 dias para implementação".

*   **Passo 4: Fechamento do Loop (Closing the Loop) com Clientes.**
    *   Esta é a etapa mais crítica. Contate *todos* os detratores (NPS 0-6) em até 24-48 horas após a resposta para entender a fundo o problema, pedir desculpas e apresentar um plano de solução ou escalonar. Para passivos (NPS 7-8), agradeça e explore o que poderia ter melhorado a experiência. Para promotores (NPS 9-10), agradeça e explore oportunidades de depoimentos ou referências. O contato deve ser pessoal, preferencialmente por telefone.
    *   *Exemplo Concreto*: Um cliente da Consultoria Iota deu NPS 4 e criticou a "falta de proatividade". O gerente de contas ligou para o cliente, ouviu atentamente, reconheceu a falha e propôs um novo cronograma de comunicação com check-ins diários por uma semana, revertendo a percepção inicial.

*   **Passo 5: Monitoramento e Relatório de Progresso Contínuo.**
    *   Estabeleça uma rotina de revisão dos resultados da pesquisa (e.g., mensal ou trimestral) com a equipe de liderança. Apresente os resultados das métricas (NPS, CSAT), as tendências, o progresso das ações do plano de melhoria e o impacto nas métricas de retenção e churn. Ajuste as estratégias conforme novos feedbacks e resultados.
    *   *Exemplo Concreto*: A Consultoria Kappa realiza uma reunião mensal de "Customer Voice" onde o Head de Sucesso do Cliente apresenta o NPS do mês, os 3 principais temas de feedback, o status das ações de melhoria e compara com o NPS dos últimos 6 meses, buscando tendências e comprovando o ROI das iniciativas.

---

## Templates

### Email Convite para Pesquisa NPS Pós-Projeto

```
Assunto: Seu Feedback é Essencial para a [Nome da Consultoria] - Projeto [Nome do Projeto]

Prezado(a) [Nome do Cliente],

Esperamos que os resultados do projeto "[Nome do Projeto]" com a nossa equipe estejam contribuindo significativamente para seus objetivos.

Na [Nome da Consultoria], nosso compromisso é com a excelência e a sua satisfação. Para continuarmos aprimorando nossos serviços e entregando o máximo valor, sua perspectiva é fundamental.

Gostaríamos de convidá-lo(a) a dedicar apenas 2 a 3 minutos para compartilhar sua experiência recente conosco por meio de nossa pesquisa de satisfação. Seu feedback direto nos ajuda a identificar pontos fortes e áreas para melhoria contínua.

Por favor, clique no link abaixo para acessar a pesquisa:
[Link para a Pesquisa de Satisfação (ex: https://forms.gle/exemploABC123)]

Agradecemos imensamente sua colaboração e a confiança depositada em nossa consultoria.

Atenciosamente,

[Nome do Gerente de Sucesso do Cliente/Consultor Principal]
[Seu Cargo]
[Nome da Consultoria]
[Seu Telefone de Contato]
[Seu E-mail]
```

### Pesquisa de Satisfação Simplificada (NPS + Qualitativa)

```
Título da Pesquisa: Sua Experiência com a [Nome da Consultoria] - Projeto [Nome do Projeto Específico]

Prezado(a) [Nome do Cliente],

Agradecemos por dedicar seu tempo para nos ajudar a melhorar.

1. Em uma escala de 0 a 10, qual a probabilidade de você recomendar a [Nome da Consultoria] a um amigo ou colega?
   ( ) 0 - Muito Improvável
   ( ) 1
   ( ) 2
   ( ) 3
   ( ) 4
   ( ) 5
   ( ) 6
   ( ) 7 - Neutro
   ( ) 8
   ( ) 9 - Provável
   ( ) 10 - Muito Provável

2. Qual o principal motivo para a nota que você atribuiu? Por favor, seja o mais específico possível.
   [Caixa de texto livre, idealmente com limite de 500 caracteres]

3. Pensando em sua experiência com a equipe da [Nome da Consultoria] neste projeto, quão fácil foi interagir e obter o suporte necessário?
   ( ) Muito Difícil
   ( ) Difícil
   ( ) Neutro
   ( ) Fácil
   ( ) Muito Fácil

4. Há algo mais que você gostaria de nos dizer para que possamos melhorar ainda mais nossos serviços e sua experiência futura?
   [Caixa de texto livre, opcional]

Obrigado(a) novamente pelo seu valioso feedback!
```

---

## Checklist

- [ ] Selecionar a métrica de satisfação principal (NPS, CSAT, CES) de acordo com o objetivo da pesquisa e o ponto da jornada do cliente.
- [ ] Escolher e configurar a ferramenta de pesquisa (ex: Qualtrics, SurveyMonkey, Typeform) para automação e análise.
- [ ] Elaborar um questionário conciso (máximo 5 perguntas) com foco em dados acionáveis, incluindo perguntas abertas.
- [ ] Integrar o envio da pesquisa com o CRM ou sistema de gestão de projetos para automação e personalização.
- [ ] Definir o gatilho e o timing ideal para o envio da pesquisa (ex: 72 horas após a conclusão do projeto).
- [ ] Criar um e-mail de convite claro, personalizado e com um call-to-action direto para a pesquisa.
- [ ] Configurar alertas automáticos para respostas de detratores (NPS 0-6) ou CSAT/CES negativos.
- [ ] Estabelecer um processo de "fechamento do loop" com todos os clientes que responderam, especialmente os detratores, em até 24-48 horas.
- [ ] Desenvolver um plano de ação para os temas de feedback negativos mais recorrentes, com responsáveis e prazos definidos.
- [ ] Agendar revisões periódicas (mensais/trimestrais) dos resultados da pesquisa com a equipe de liderança para monitorar tendências e ajustar estratégias.

---

## Métricas de Referência

| Métrica | Benchmark (Consultoria B2B) | Meta (Interna) |
|---------|-----------------------------|----------------|
| NPS     | 40-60                       | >55            |
| CSAT    | 80-90%                      | >85%           |
| CES     | <2.5 (em escala 1-5)        | <2.0           |
| Taxa de Resposta | 20-35% (para pesquisas transacionais) | >25%           |
| % de Detratores | <15%                        | <10%           |
| % de Promotores | >55%                        | >60%           |

---

## Erros Comuns

1.  **Pesquisas Excessivamente Longas e Complexas**: Clientes B2B, especialmente executivos, têm tempo limitado. Uma pesquisa com 10+ perguntas ou com linguagem ambígua gera alta taxa de abandono e feedback superficial.
    *   *Como evitar*: Mantenha o questionário o mais conciso possível, focando nas métricas chave (NPS/CSAT/CES) e em 1-2 perguntas abertas que convidem a feedback qualitativo. *Exemplo*: Em vez de perguntar "Avalie a qualidade de cada um dos nossos 7 entregáveis do projeto X", utilize "Qual foi o aspecto mais valioso do projeto X e qual poderia ser melhorado?".

2.  **Não Agir Sobre o Feedback Recebido (Loop Aberto)**: Coletar feedback e não implementar ações ou não dar retorno aos clientes gera frustração e a percepção de que suas opiniões não importam, piorando a satisfação futura.
    *   *Como evitar*: Implemente um processo de "fechamento do loop" obrigatório. Para detratores, a equipe de Sucesso do Cliente deve contatá-los em até 24-48 horas para entender a fundo a insatisfação e propor soluções. Para passivos e promotores, um agradecimento personalizado e a exploração de oportunidades (depoimentos, referências) são essenciais. *Exemplo*: Se um cliente dá NPS 5 e comenta "o projeto atrasou sem comunicação prévia", o gerente de contas liga para ele no mesmo dia, pede desculpas, explica as ações corretivas e reestabelece um novo canal de comunicação pró-ativa.

3.  **Timing Inadequado do Envio da Pesquisa**: Enviar a pesquisa muito cedo (antes do cliente experimentar o valor total da consultoria) ou muito tarde (quando a memória da experiência já se diluiu) resulta em dados imprecisos ou irrelevantes.
    *   *Como evitar*: Defina pontos estratégicos na jornada do cliente para cada tipo de pesquisa. Para pesquisas transacionais, envie logo após um marco de valor (ex: 3 dias após a conclusão do projeto, 5 dias após o término do onboarding). Para pesquisas de relacionamento, envie anualmente. *Exemplo*: Uma pesquisa de onboarding deve ser enviada após a primeira semana de engajamento ativo, e não no momento da assinatura do