---
name: feedback-survey-email
description: "Feedback Survey Email — Skill especializada para feedback survey email"
license: MIT
metadata:
  version: 1.0.0
  author: Cafe Code AI
  category: 02-email-automacao
  updated: 2026-03-01
risk: safe
---

# Feedback Survey Email

Esta skill capacita o Claude a criar, otimizar e implementar sequências de email eficazes para coleta de feedback pós-interação ou pós-compra, maximizando as taxas de resposta e a qualidade dos insights.

---

## Keywords

Email de Pesquisa, Feedback de Cliente, NPS (Net Promoter Score), CSAT (Customer Satisfaction Score), CES (Customer Effort Score), Automação de Feedback, Pós-compra, Pós-interação, Email Transacional, Taxa de Resposta, Segmentação de Feedback, Análise de Sentimento.

---

## Quick Start

1.  **Configuração do Gatilho Pós-Serviço**: Configure a automação para disparar o email de feedback 24 horas após a marcação de "chamado resolvido" no sistema de help desk (ex: Zendesk, Freshdesk).
2.  **Integração da Métrica Principal**: Opte por coletar CSAT para serviços de suporte ao cliente, incorporando a pergunta "Como você avaliaria a assistência que recebeu?" com opções de 1 a 5 estrelas diretamente no corpo do email.
3.  **Criação do Email Convite Direto**: Elabore o email com um Subject Line claro como "Sua opinião é valiosa! Conte-nos sobre sua experiência com o suporte da [Nome da Empresa]". Inclua o link ou as opções de resposta para a pesquisa CSAT de forma destacada.
4.  **Sequência de Lembrete Otimizada**: Programe um email de lembrete 3 dias após o envio inicial, direcionado apenas aos clientes que não responderam. Use um Subject Line como "Ainda queremos sua opinião sobre o atendimento da [Nome da Empresa]".
5.  **Monitoramento e Ação Imediata**: Acompanhe diariamente as respostas CSAT negativas (1 ou 2 estrelas) e estabeleça um protocolo para que a equipe de Sucesso do Cliente entre em contato em até 4 horas para entender e tentar resolver a insatisfação.

---

## Core Workflows

### Workflow 1: Automação de Feedback Pós-Compra para SaaS B2B

Este workflow foca em coletar o Net Promoter Score (NPS) e feedback qualitativo de novos clientes B2B após o período inicial de uso do produto, visando identificar promotores e áreas de melhoria.

1.  **Gatilho da Automação**: Acionamento automático 7 dias após a data de "Conta Ativada" (status no CRM ou plataforma de gerenciamento de clientes). Esse atraso permite que o novo usuário explore o software e tenha uma experiência inicial consolidada.
2.  **Segmentação Inicial**: Excluir clientes que já foram convidados para uma pesquisa de NPS nos últimos 120 dias para evitar fadiga de pesquisa. Focar apenas em novos clientes que concluíram o onboarding.
3.  **Email 1 (Dia 0 - Pós-gatilho)**:
    *   **Assunto**: "Ajude-nos a aprimorar o [Nome do Produto]! Sua visão é essencial."
    *   **Conteúdo**: Convite amigável e profissional, explicando como o feedback contribui para o desenvolvimento do produto. A primeira pergunta (NPS) é integrada no corpo do email ou um link direto para um formulário externo (ex: Typeform, SurveyMonkey) com a pergunta NPS e mais 3-5 perguntas de múltipla escolha ou abertas sobre a experiência de onboarding, facilidade de uso e valor percebido.
    *   **Exemplo de Corpo**:
        ```
        Olá [Nome do Cliente],

        Esperamos que esteja aproveitando ao máximo o [Nome do Produto] e que sua equipe esteja colhendo os benefícios de nossa solução.

        Para garantir que continuemos desenvolvendo a melhor ferramenta para você e para o mercado B2B, gostaríamos de pedir 2 minutos do seu tempo para compartilhar sua experiência inicial conosco. Seu feedback é a bússola que orienta nossas melhorias.

        Em uma escala de 0 a 10, qual a probabilidade de você recomendar o [Nome do Produto] a um amigo ou colega do setor?

        [Botão: Responder à Pesquisa (Link para formulário)]

        Desde já, muito obrigado por sua colaboração e por fazer parte da comunidade [Nome da Empresa]!

        Atenciosamente,

        A Equipe de Produto [Nome da Empresa]
        ```
4.  **Email 2 (Dia 3 - Lembrete)**:
    *   **Condição**: Enviado exclusivamente para clientes que abriram o Email 1, mas não clicaram no link da pesquisa, ou não abriram o Email 1.
    *   **Assunto**: "Lembrete: Sua opinião sobre o [Nome do Produto] ainda é muito importante!"
    *   **Conteúdo**: Reforçar a importância do feedback, talvez mencionando uma melhoria recente que foi implementada com base em sugestões de clientes.
    *   **Exemplo de Corpo**:
        ```
        Oi [Nome do Cliente],

        Vimos que você ainda não teve a chance de compartilhar sua opinião sobre o [Nome do Produto].

        Na [Nome da Empresa], acreditamos que o sucesso de nossos clientes é o nosso sucesso. Seu feedback é a ferramenta mais poderosa que temos para continuar evoluindo e construindo um produto que atenda perfeitamente às necessidades da sua empresa.

        Levará apenas alguns minutos. Clique aqui para nos ajudar a melhorar:

        [Botão: Compartilhar Minha Experiência (Link para o mesmo formulário)]

        Agradecemos sua atenção e colaboração!

        Com os melhores cumprimentos,

        A Equipe [Nome da Empresa]
        ```
5.  **Análise e Ação**: Integrar as respostas NPS com o CRM. Clientes com NPS 9-10 (Promotores) são marcados para contato pela equipe de Marketing para solicitação de depoimentos, estudos de caso ou referências. Clientes com NPS 0-6 (Detratores) são imediatamente encaminhados para a equipe de Sucesso do Cliente para um follow-up proativo e personalizado, visando entender as insatisfações e oferecer soluções.

### Workflow 2: Coleta de CSAT para Atendimento ao Cliente (E-commerce)

Este workflow visa medir a satisfação do cliente com o atendimento prestado pela equipe de suporte de um e-commerce, permitindo a identificação rápida de problemas e a melhoria contínua do serviço.

1.  **Gatilho da Automação**: Disparo automático 30 minutos após a mudança de status do ticket de suporte para "Resolvido" na ferramenta de help desk (ex: Zendesk, Freshdesk). O pequeno atraso garante que o cliente teve tempo de verificar a resolução.
2.  **Segmentação**: Excluir tickets que foram reabertos em menos de 12 horas após a resolução inicial, pois indicam um problema não solucionado. Priorizar interações onde o problema foi de fato encerrado.
3.  **Email 1 (Dia 0 - Pós-resolução)**:
    *   **Assunto**: "Sua avaliação do atendimento da [Nome da Loja] (Pedido #[Número do Pedido])"
    *   **Conteúdo**: Direto e objetivo, com a pergunta CSAT ("Como você avaliaria a assistência que recebeu?") e opções de resposta clicáveis (estrelas ou escala numérica) diretamente no corpo do email para maximizar a taxa de resposta.
    *   **Exemplo de Corpo**:
        ```
        Olá [Nome do Cliente],

        Confirmamos que seu chamado referente ao Pedido #[Número do Pedido] foi resolvido com sucesso por nossa equipe.

        Sua satisfação é a nossa prioridade na [Nome da Loja] e, para nos ajudar a aprimorar continuamente nossos serviços, gostaríamos de saber:

        Como você avaliaria a assistência que recebeu de nossa equipe?
        (Basta clicar na sua resposta abaixo)

        [Link para avaliar com 5 Estrelas - Excelente]
        [Link para avaliar com 4 Estrelas - Bom]
        [Link para avaliar com 3 Estrelas - Regular]
        [Link para avaliar com 2 Estrelas - Ruim]
        [Link para avaliar com 1 Estrela - Péssimo]

        Seu feedback é muito importante para nós e nos ajuda a garantir a melhor experiência de compra!

        Atenciosamente,

        A Equipe de Suporte [Nome da Loja]
        ```
4.  **Análise e Follow-up Imediato**: Respostas negativas (1 ou 2 estrelas) devem gerar um alerta automático (ex: Slack, email) para o gerente da equipe de suporte em tempo real. Este gerente deve entrar em contato com o cliente em até 2 horas para entender a causa da insatisfação e buscar uma solução proativa, transformando uma experiência negativa em uma oportunidade de fidelização. Respostas positivas (4 ou 5 estrelas) são compiladas para avaliação de desempenho individual da equipe e reconhecimento.

---

## Templates

### Email de Pesquisa NPS Pós-Onboarding (SaaS B2B)

```
Assunto: Sua opinião sobre o [Nome do Produto] é valiosa para nós!

Olá [Nome do Cliente],

Esperamos que você esteja aproveitando ao máximo o [Nome do Produto] e que ele já esteja gerando valor para a sua empresa.

Para garantir que continuemos desenvolvendo a melhor ferramenta possível para atender às suas necessidades, gostaríamos de pedir 2 minutinhos do seu tempo para compartilhar sua experiência inicial conosco.

Seu feedback é a chave para moldar as futuras melhorias e funcionalidades do [Nome do Produto].

Em uma escala de 0 a 10, qual a probabilidade de você recomendar o [Nome do Produto] a um amigo ou colega de profissão?

[Link para Pesquisa de Feedback (Ex: Formulário Typeform/SurveyMonkey com a pergunta NPS e 3-4 perguntas de follow-up)]

Desde já, muito obrigado pela sua colaboração e por nos ajudar a crescer!

Atenciosamente,

A Equipe [Nome da Empresa]
[Link para o Site da Empresa]
```

### Email de Coleta CSAT Pós-Atendimento (E-commerce)

```
Assunto: Avalie seu atendimento da [Nome da Loja] (Pedido #[Número do Pedido])

Olá [Nome do Cliente],

Confirmamos que seu chamado de suporte referente ao Pedido #[Número do Pedido] foi resolvido com sucesso por nossa equipe.

Na [Nome da Loja], sua satisfação com nosso atendimento é fundamental. Para nos ajudar a aprimorar continuamente nossos serviços, gostaríamos de saber:

Como você avaliaria a assistência que recebeu de nossa equipe de suporte?
(Basta clicar na sua resposta abaixo. É rápido e nos ajuda muito!)

[Link para avaliar com 5 Estrelas - Excelente]
[Link para avaliar com 4 Estrelas - Bom]
[Link para avaliar com 3 Estrelas - Regular]
[Link para avaliar com 2 Estrelas - Ruim]
[Link para avaliar com 1 Estrela - Péssimo]

Seu feedback é extremamente importante para nós!

Atenciosamente,

A Equipe de Suporte [Nome da Loja]
[Link para a Central de Ajuda da Loja]
```

---

## Checklist

-   [ ] O gatilho da automação de feedback está configurado para o momento ideal pós-interação (ex: 7 dias pós-compra de SaaS, 30 min pós-resolução de ticket)?
-   [ ] O Subject Line é claro, conciso e indica o propósito do email, gerando curiosidade e relevância (ex: "Sua opinião sobre [Produto]")?
-   [ ] A primeira pergunta da pesquisa (NPS, CSAT ou CES) está integrada no corpo do email para reduzir o atrito e aumentar a taxa de resposta inicial?
-   [ ] Existe uma sequência de lembretes (mínimo 1) configurada para quem não respondeu ao email inicial, com um intervalo de 2-3 dias?
-   [ ] A pesquisa é concisa, contendo no máximo 5-7 perguntas relevantes e pode ser preenchida em menos de 3 minutos?
-   [ ] As respostas da pesquisa são automaticamente segmentadas (promotores, neutros, detratores para NPS; satisfeitos/insatisfeitos para CSAT) para permitir ações direcionadas?
-   [ ] Há um plano de follow-up proativo e rápido para detratores ou clientes insatisfeitos (ex: contato da equipe de Sucesso do Cliente em até 24h)?
-   [ ] Os dados de feedback são integrados a um CRM ou plataforma de análise para insights contínuos e acompanhamento do histórico do cliente?
-   [ ] A frequência de envio de pesquisas para o mesmo cliente é controlada (ex: máximo uma pesquisa de NPS a cada 90 ou 120 dias para evitar sobrecarga)?
-   [ ] O email de pesquisa inclui uma breve e transparente explicação sobre como o feedback do cliente será utilizado para gerar melhorias?

---

## Métricas de Referência

| Métrica                      | Benchmark | Meta   |
|------------------------------|-----------|--------|
| Taxa de Abertura (Emails)    | 20-30%    | 35%    |
| Taxa de Clique (CTA Pesquisa)| 10-15%    | 18%    |
| Taxa de Resposta da Pesquisa | 10-20%    | 25%    |
| Net Promoter Score (NPS)     | 30-50     | 60     |
| Customer Satisfaction Score (CSAT)| 75-85%    | 90%    |
| Customer Effort Score (CES)  | 1.5-2.5   | 1.0 (escala de 1-7, menor é melhor) |

---

## Erros Comuns

1.  **Excesso de Perguntas na Pesquisa**: Pesquisas que são muito longas (mais de 7 perguntas ou que levam mais de 3 minutos para responder) resultam em altas taxas de abandono e menor qualidade dos dados coletados.
    *   **Como evitar**: Priorize as métricas essenciais (NPS, CSAT, CES) e limite o número de perguntas de follow-up. Utilize lógica condicional no formulário da pesquisa para exibir perguntas adicionais apenas quando relevantes, com base nas respostas anteriores do usuário.
2.  **Envio no Momento Inadequado**: Disparar o email de feedback imediatamente após uma interação complexa ou antes do cliente ter tempo suficiente para experimentar o produto/serviço pode gerar respostas precipitadas ou imprecisas, baseadas em uma impressão incompleta.
    *   **Como evitar**: Configure atrasos estratégicos na automação (ex: 24h após a resolução de um ticket para CSAT, 7 dias após a ativação de um produto para NPS) para permitir que o cliente tenha uma perspectiva mais completa e uma opinião formada antes de responder.
3.  **Falta de Follow-up para Detratores**: Coletar feedback negativo de clientes insatisfeitos (detratores ou CSAT baixo) e não agir sobre ele piora a percepção do cliente sobre a empresa e anula o propósito principal da pesquisa.
    *   **Como evitar**: Implemente um sistema de alerta imediato para respostas negativas (NPS 0-6, CSAT 1-2 estrelas). Designe um responsável (ex: equipe de Sucesso do Cliente ou gerente de suporte) para entrar em contato proativamente com o cliente em um prazo máximo de 24 horas, buscando entender o problema e oferecer uma solução.

---

## Dicas Avançadas

1.  **Personalização Contextual do Convite**: Além do nome do cliente, personalize o email de feedback com detalhes específicos da interação. Por exemplo, para CSAT de suporte, mencione o nome do agente que atendeu ou o tipo de problema resolvido (Ex: "Como foi o atendimento do João sobre seu problema de login?"). Isso aumenta a relevância e a taxa de resposta.
2.  **A/B Testes Contínuos em Elementos-Chave**: Realize A/B testes sistemáticos em diferentes aspectos do email: variações no Subject Line (ex: focado em urgência vs. valor), diferentes calls-to-action (botão versus links de texto, ícones de estrelas versus texto), e até mesmo os horários de envio. Monitore as taxas de abertura, clique e resposta para otimizar continuamente a performance.
3.  **Integração de Feedback em Tempo Real com Dashboards Acionáveis**: Conecte os resultados das pesquisas diretamente a um dashboard em tempo real (ex: Power BI, Tableau, Google Data Studio) que exiba NPS/CSAT por segmento de cliente, produto, equipe de suporte ou agente. Isso permite que as equipes identifiquem tendências, pontos críticos e tomem ações corretivas de forma ágil e baseada em dados.
4.  **Loop Fechado de Feedback com Notificação de Ação**: Para clientes que fornecem feedback específico (seja positivo com sugestões ou negativo), configure uma automação para enviar um email de follow-up posterior (ex: 30-60 dias depois) informando sobre as melhorias ou ações que foram implementadas com base nas sugestões deles. Ex: "Lembramos do seu feedback sobre a funcionalidade de relatórios em [Nome do Produto]. Informamos que a versão Y já inclui as melhorias sugeridas e novas opções de visualização!". Isso demonstra que o feedback é valorizado e gera impacto.
5.  **Micro-pesquisas Contextuais no Produto/Serviço**: Em vez de depender apenas de emails, implemente micro-pesquisas de uma ou duas perguntas em momentos estratégicos dentro da jornada do cliente no produto ou serviço. Por exemplo, um pequeno popup no aplicativo após o usuário usar uma funcionalidade chave pela primeira vez, ou uma pesquisa de CES integrada diretamente no widget de chat de suporte após a interação ser encerrada. Isso coleta feedback de forma menos intrusiva e mais contextual.