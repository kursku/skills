---
name: user-feedback-loop
description: "User Feedback Loop — Skill especializada para user feedback loop"
license: MIT
metadata:
  version: 1.0.0
  author: Cafe Code AI
  category: 08-lancamento-growth
  updated: 2026-03-01
risk: safe
---

# User Feedback Loop

Esta skill capacita o Claude a projetar e implementar sistemas eficientes de coleta e ação sobre o feedback do usuário, otimizando produtos para retenção e crescimento.

---

## Keywords

*   Loop de Feedback Contínuo
*   NPS (Net Promoter Score)
*   CES (Customer Effort Score)
*   CSAT (Customer Satisfaction Score)
*   Entrevistas de Usuário Qualitativas
*   Testes de Usabilidade Moderados
*   Surveys In-App Contextuais
*   Análise de Cohort de Feedback
*   Priorização de Features baseada em Feedback
*   Ciclo de Desenvolvimento Ágil
*   Engajamento Pós-Feedback

---

## Quick Start

1.  **Implementar pop-up de NPS contextualizado:** Após 7 dias de uso ativo ou 3 sessões concluídas, exibir um modal de NPS in-app com campo aberto para o usuário justificar a nota.
2.  **Configurar webhook para feedback negativo (NPS 0-6):** Disparar alerta no Slack para o time de produto/suporte revisar e agendar contato proativo com o usuário em até 24h.
3.  **Agendar 5 entrevistas de usuário semanais:** Priorizar usuários que deram feedback crítico ou que são novos no produto (primeiros 30 dias) para entender suas dores e motivações.
4.  **Criar quadro Kanban "Feedback to Action":** Organizar todos os inputs de feedback em um backlog priorizado por impacto e esforço, com status (Recebido, Analisado, Em Desenvolvimento, Lançado).

---

## Core Workflows

### Workflow 1: Implementação de um Loop de Feedback Quantitativo Pós-Onboarding

Este workflow detalha a coleta de feedback quantitativo em um momento crucial da jornada do usuário, o onboarding, para identificar e resolver fricções iniciais.

*   **Passo 1: Definição do Gatilho e Métrica:** Escolher o momento ideal para a pesquisa. Exemplo concreto: 7 dias após a ativação (primeiro login bem-sucedido) para usuários do plano Pro da ferramenta de gestão de projetos "TaskFlow". As métricas principais serão o CES (Customer Effort Score) e CSAT (Customer Satisfaction Score).
*   **Passo 2: Criação da Pesquisa In-App:** Usar uma ferramenta como Typeform, Qualaroo ou Hotjar para criar um modal discreto, exibido apenas uma vez por usuário. Perguntas específicas: "Quão fácil foi completar sua primeira tarefa de projeto em TaskFlow? (1-7, sendo 1 muito difícil e 7 muito fácil)", "Sua experiência inicial com TaskFlow atendeu às suas expectativas? (1-5 estrelas)", "Qual funcionalidade você mais precisou nos primeiros dias e não encontrou ou teve dificuldade em usar?".
*   **Passo 3: Coleta e Segmentação:** Coletar os dados e segmentar os usuários com base nas pontuações.
    *   Para CES: 1-3 (dificuldade alta), 4-5 (neutro), 6-7 (fácil).
    *   Para CSAT: 1-2 estrelas (muito insatisfeito), 3 (neutro), 4-5 (satisfeito).
    *   Segmentar também por tipo de usuário (ex: "Criador de Projeto", "Membro de Equipe") e uso de features específicas.
*   **Passo 4: Análise e Ação (Exemplo Real):**
    *   **Cenário:** A pesquisa revela que 35% dos novos usuários do plano Pro deram CES 1-3 e CSAT 1-2. A análise dos campos abertos indica que a maior dor é "dificuldade em configurar integrações com Jira/Slack" e "não consigo encontrar o botão de convidar equipe facilmente".
    *   **Ação:** O time de produto prioriza a criação de um "Guia Rápido de Integrações Essenciais" com vídeo tutorial curto e a reformulação do botão "Convidar Equipe" para um local mais proeminente e com um tooltip explicativo. O time de CX entra em contato proativo com os 35% de usuários com CES baixo para oferecer suporte personalizado e coletar mais insights qualitativos.
    *   **Resultado Esperado:** Redução de 18% na taxa de churn de novos usuários nos primeiros 30 dias após a implementação das melhorias e aumento de 25% no CES para a próxima coorte de onboarding.

### Workflow 2: Condução de Entrevistas de Usuário Qualitativas para Validação de Hipótese

Este workflow foca em aprofundar o entendimento de um problema específico através de conversas diretas com usuários, validando ou invalidando hipóteses de produto.

*   **Passo 1: Formulação da Hipótese:** "Usuários do módulo 'Relatórios Avançados' do TaskFlow não estão encontrando valor na funcionalidade de 'Exportação Agendada' devido à complexidade da configuração, resultando em baixa adoção (menos de 5% de uso semanal) e uso de workarounds manuais."
*   **Passo 2: Recrutamento de Participantes:** Selecionar 8-10 usuários ativos do módulo de Relatórios Avançados, com histórico de uso da funcionalidade de exportação (se houver) ou que explicitamente não a usam. Utilizar Intercom ou e-mail segmentado para convidá-los, oferecendo um voucher de R$75 como incentivo. Priorizar perfis diversos (ex: gerentes de projeto, analistas de dados).
*   **Passo 3: Elaboração do Roteiro de Entrevista:** Criar um roteiro semiestruturado para guiar a conversa.
    *   Introdução (5 min): Boas-vindas, explicação do objetivo ("entender o uso de relatórios para melhorias"), consentimento para gravação.
    *   Exploração Geral (15 min): "Como você usa os relatórios hoje no TaskFlow?", "Quais são suas maiores dores ou desafios ao compartilhar dados de projeto com sua equipe ou stakeholders?".
    *   Detalhes da Hipótese (20 min): "Você já notou a funcionalidade de 'Exportação Agendada'? Se sim, como foi sua experiência ao tentar usá-la? O que achou fácil ou difícil? Se não, por que você acha que não a utilizou?" "Quais informações você esperaria configurar em uma exportação agendada?".
    *   Teste de Conceito (10 min): Apresentar um wireframe ou protótipo de uma interface simplificada para agendamento de exportações. "O que você acha disso? É mais fácil de entender? Você usaria isso?".
    *   Fechamento (5 min): Perguntas abertas ("Há algo mais que eu deveria saber sobre isso?"), agradecimento.
*   **Passo 4: Análise e Síntese:** Transcrever e analisar as entrevistas, buscando padrões, citações-chave e pontos de dor recorrentes.
    *   **Cenário Real:** 7 de 8 usuários mencionaram que a interface atual para agendamento era "intimidadora", "cheia de campos desnecessários" e "não intuitiva". O protótipo simplificado foi bem recebido por 6 usuários, que afirmaram que "com essa interface, eu definitivamente tentaria usar". Citações como "Eu só quero que o relatório vá para o e-mail toda segunda-feira, não quero configurar FTP" foram recorrentes.
    *   **Ação:** O time de produto valida a hipótese. Prioriza a reformulação da interface de "Exportação Agendada" para uma versão mais intuitiva, com foco nas opções mais usadas (e-mail, Slack, periodicidade) e um fluxo guiado passo a passo, removendo complexidades desnecessárias.
    *   **Resultado Esperado:** Aumento de 20% na adoção da funcionalidade de 'Exportação Agendada' nos 3 meses seguintes ao lançamento da nova interface, e redução de chamados de suporte relacionados a essa funcionalidade.

---

## Templates

### Roteiro de Entrevista de Usuário (Validação de Hipótese)

```
**Título da Entrevista:** Validação de Usabilidade da Exportação Agendada de Relatórios em TaskFlow
**Data:** 2024-10-27
**Entrevistador:** Ana Silva (Product Manager)
**Participante:** [Nome do Participante]
**Contexto:** Usuário ativo do módulo de Relatórios Avançados de TaskFlow.
**Hipótese a Validar:** A baixa adoção da Exportação Agendada se deve à complexidade da interface de configuração.

**Objetivos:**
1.  Entender as dores atuais do usuário com o compartilhamento de relatórios.
2.  Identificar barreiras no uso da funcionalidade de Exportação Agendada.
3.  Obter feedback sobre um protótipo simplificado da interface.

**Roteiro:**

**1. Introdução (5 min)**
    *   Boas-vindas e agradecimento pela participação.
    *   Explicação do objetivo: "Estamos buscando entender como podemos melhorar a forma como você compartilha relatórios em TaskFlow para que seja mais eficiente."
    *   Consentimento para gravação (áudio/tela) e garantia de anonimato. "Não há respostas certas ou erradas; sua perspectiva é o que nos importa."

**2. Exploração Geral (15 min)**
    *   "Como você usa os relatórios do TaskFlow hoje? Poderia me descrever um cenário típico de como você extrai e compartilha dados?"
    *   "Quais são os principais desafios ou dores que você enfrenta ao extrair e compartilhar dados de projeto com sua equipe ou stakeholders?"
    *   "Você já precisou enviar relatórios para outras pessoas regularmente, em uma base semanal ou mensal? Como você faz isso atualmente?"

**3. Detalhes da Hipótese (20 min)**
    *   "Você já notou a funcionalidade de 'Exportação Agendada' dentro dos relatórios do TaskFlow? (Mostrar tela, se necessário)"
    *   *Se tentou usar:* "Como foi sua experiência ao tentar agendar uma exportação? O que achou fácil ou difícil? Lembra-se de algum momento de frustração?"
    *   *Se não tentou usar:* "Por que você acha que não utilizou essa funcionalidade até agora? O que te impediria de usar uma funcionalidade que agendasse automaticamente o envio de relatórios?"
    *   "Quais informações ou configurações seriam mais importantes para você ao agendar uma exportação de relatório (ex: formato, destinatários, frequência)?"

**4. Teste de Conceito (10 min)**
    *   "Tenho um protótipo de uma nova interface para agendamento de exportações. Gostaria de sua opinião inicial sobre ela."
    *   [Apresentar protótipo ou wireframe simplificado da funcionalidade de agendamento]
    *   "O que você acha dessa abordagem? Ela é mais clara ou fácil de entender que a atual?"
    *   "Se você visse essa interface implementada, você tentaria usar a funcionalidade de agendamento? Por quê/Por que não?"
    *   "Há algo que você mudaria, adicionaria ou removeria aqui para torná-la ainda melhor para você?"

**5. Fechamento (5 min)**
    *   "Alguma outra observação ou ideia sobre relatórios e compartilhamento de dados em TaskFlow que não abordamos?"
    *   "Há algo que não perguntamos, mas que você considera importante para nós sabermos?"
    *   Agradecimento e informações sobre próximos passos (ex: "Seu feedback nos ajudará a priorizar melhorias").
```

### Template de E-mail para Seguimento Pós-NPS Negativo

```
**Assunto:** Um rápido contato sobre sua experiência recente com TaskFlow

**Prezado(a) [Nome do Usuário],**

Gostaríamos de agradecer por ter dedicado seu tempo para responder à nossa pesquisa de satisfação recente sobre o TaskFlow. Notamos que sua experiência, com base na pontuação que você nos deu (NPS 0-6), não foi totalmente positiva, e sentimos muito por isso.

Seu feedback é extremamente valioso para nós, pois nos ajuda a identificar áreas específicas onde podemos e precisamos melhorar.

Gostaríamos muito de entender melhor o que aconteceu ou qual foi o ponto de fricção. Você estaria disponível para uma breve conversa de 15 minutos com um de nossos especialistas em produto na próxima semana? Poderíamos agendar para **[Sugestão de Data e Hora 1 - ex: Quarta-feira, 30 de Outubro, às 14h BRT]** ou **[Sugestão de Data e Hora 2 - ex: Quinta-feira, 31 de Outubro, às 10h BRT]**?

Ou, se preferir, poderia nos dar mais detalhes sobre sua experiência respondendo diretamente a este e-mail? Sua perspectiva é crucial para fazermos as melhorias certas.

Aguardamos seu retorno para que possamos transformar sua experiência.

Atenciosamente,

[Seu Nome/Nome da Equipe de Produto]
Equipe TaskFlow
```

---

## Checklist

- [ ] Definir gatilhos contextuais específicos para feedback (ex: após a 3ª ação-chave, 7 dias de uso, conclusão de uma tarefa crítica).
- [ ] Implementar ao menos um canal de feedback passivo (ex: widget "Ajuda/Feedback" persistente no canto da tela).
- [ ] Segmentar todos os feedbacks coletados por tipo de usuário (novo, ativo, churn, inativo) e plano (free, básico, pro, enterprise).
- [ ] Criar um processo claro e documentado de triagem e priorização de feedback (ex: "Impacto no Usuário vs. Esforço de Desenvolvimento").
- [ ] Agendar entrevistas qualitativas semanais com um mínimo de 3-5 usuários de perfis diversos para aprofundar insights.
- [ ] Fechar o loop com usuários que deram feedback crítico (agradecer, informar sobre ações tomadas ou próximas).
- [ ] Medir a taxa de resposta e a qualidade do feedback coletado por cada canal (ex: NPS in-app vs. email).
- [ ] Integrar dados de feedback com métricas de produto e de negócio (ex: correlacionar NPS baixo com taxa de churn de coortes).
- [ ] Comunicar internamente os insights do feedback e as ações resultantes para toda a equipe de produto, engenharia e vendas/marketing.
- [ ] Realizar testes A/B em implementações de feedback para otimizar o formato, o momento e o conteúdo das pesquisas.

---

## Métricas de Referência

| Métrica                         | Benchmark (SaaS B2B) | Meta (TaskFlow) |
|---------------------------------|----------------------|-----------------|
| NPS (Net Promoter Score)        | 30-50                | > 45            |
| CSAT (Customer Satisfaction Score)| 75-85%               | > 80%           |
| CES (Customer Effort Score)     | < 3 (escala 1-7)     | < 2.5           |
| Taxa de Resposta (Surveys In-App)| 5-15%                | > 10%           |
| Feedback Positivo/Negativo      | 70% Positivo         | > 75% Positivo  |
| Tempo Médio p/ Fechar Loop (Crítico)| 48-72 horas          | < 24 horas      |

---

## Erros Comuns

1.  **Coletar feedback sem um plano de ação claro**: Receber centenas de inputs e não ter um processo definido para analisá-los e agir, resultando em "feedback graveyard" e frustração interna.
    *   **Como evitar**: Antes de lançar qualquer ferramenta de feedback, defina as equipes responsáveis pela análise, priorização e execução, e estabeleça SLAs (Service Level Agreements) para cada etapa. Exemplo: Alertas de feedback negativo no Slack com responsável designado e prazo de 24h para contato inicial.
2.  **Focar apenas em feedback positivo ou negativo extremo**: Ignorar a "zona cinzenta" de usuários neutros (promotores passivos no NPS, CSAT 3 estrelas) que podem ter insights valiosos ou estar à beira do churn.
    *   **Como evitar**: Ativamente buscar feedback de usuários com CSAT/NPS neutro (notas 7-8 no NPS, 3 estrelas no CSAT). Agende entrevistas com eles para entender suas hesitações, necessidades não atendidas e o que os faria se tornarem promotores.
3.  **Não fechar o loop com os usuários**: Solicitar feedback e nunca informar o usuário sobre as ações tom