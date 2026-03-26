---
name: retention-playbook
description: "Retention Playbook — Skill especializada para retention playbook"
license: MIT
metadata:
  version: 1.0.0
  author: Cafe Code AI
  category: 08-lancamento-growth
  updated: 2026-03-01
risk: safe
---

# Retention Playbook

Esta skill capacita o Claude a projetar e executar estratégias de retenção de usuários, otimizando o lifetime value (LTV) e a lealdade do cliente através de playbooks acionáveis.

---

## Keywords

LTV, Churn Rate, Activation Rate, Retention Curve, Engajamento, Onboarding, Customer Success, Feedback Loop, Personalização, Gamificação, Reativação, Cohort Analysis.

---

## Quick Start

1.  **Analisar Cohort e Retenção D7**: Calcule a taxa de retenção D7 para todos os usuários que se registraram em 15/05/2024. Ex: Se 1000 usuários se registraram, e 320 retornaram no D7, a retenção D7 é de 32%.
2.  **Segmentar Usuários por Ação Chave**: Separe os usuários que completaram a primeira compra em menos de 24h daqueles que não. Ex: "Usuários ativados" (primeira compra) versus "Usuários não ativados".
3.  **Lançar Campanha de Reengajamento Focada**: Envie um e-mail com "20% de desconto na sua próxima compra" para os 15% dos usuários "não ativados" que visitaram o site mais de 3 vezes, mas não finalizaram a compra.
4.  **Coletar Feedback Proativo**: Implemente uma pesquisa NPS para 100% dos usuários que realizaram 3 ou mais compras e estão ativos há mais de 60 dias, visando identificar promotores e detratores.

---

## Core Workflows

### Workflow 1: Otimização do Onboarding para Aumento da Retenção D7

Este workflow foca em guiar novos usuários rapidamente para o "Aha! Moment" do produto, solidificando o valor inicial e aumentando a probabilidade de retenção de curto prazo.

1.  **Identificação do "Aha! Moment" Crucial**:
    *   **Ação**: Analisar dados de comportamento dos usuários retidos vs. churners.
    *   **Exemplo Concreto**: Para um aplicativo de finanças, usuários que conectam 2 ou mais contas bancárias nos primeiros 3 dias e categorizam 5 transações têm uma taxa de retenção D7 de 45%, enquanto os que só conectam 1 conta têm 18%. O "Aha! Moment" é a conexão de múltiplas contas e a categorização inicial.
2.  **Mapeamento da Jornada Inicial Essencial**:
    *   **Ação**: Desenhar os 3 a 5 passos mais críticos que levam ao "Aha! Moment", eliminando fricção.
    *   **Exemplo Concreto**:
        *   Passo 1: Cadastro e Verificação de E-mail.
        *   Passo 2: Conexão da Primeira Conta Bancária.
        *   Passo 3: Conexão da Segunda Conta Bancária (ou mais).
        *   Passo 4: Categorização de 5 Transações.
        *   Passo 5: Visualização do Painel de Gastos Consolidado.
3.  **Implementação de Gatilhos de Engajamento Personalizados**:
    *   **Ação**: Utilizar notificações in-app, push notifications e e-mails para guiar o usuário em cada passo crítico.
    *   **Exemplo Concreto**:
        *   **Após Cadastro (In-app)**: "Bem-vindo! Conecte sua primeira conta bancária em menos de 2 minutos para começar a organizar suas finanças." (Botão: "Conectar Agora").
        *   **Após Conexão da 1ª Conta (Push D1)**: "Ótimo trabalho! Conecte sua segunda conta para uma visão financeira completa e ganhe 50 pontos de fidelidade."
        *   **Após Conexão da 2ª Conta (E-mail D2)**: "Suas finanças estão ganhando forma! Comece a categorizar suas transações para ver onde seu dinheiro está indo. [Link para Categorizar]".
4.  **Medição e Iteração Constante**:
    *   **Ação**: Acompanhar o Activation Rate para o "Aha! Moment" e a Retention D7 para diferentes cohorts, realizando testes A/B.
    *   **Exemplo Concreto**: A/B testar um onboarding com tour guiado para os primeiros 3 passos versus um onboarding com mensagens mais curtas. Se o tour guiado aumentar o Activation Rate em 15% e a Retention D7 em 5%, implementá-lo amplamente.

### Workflow 2: Estratégia de Reengajamento para Usuários em Risco de Churn

Este workflow visa identificar e reativar usuários que demonstram sinais de inatividade ou desengajamento, antes que eles churnem completamente, protegendo o LTV.

1.  **Definição Clara de Usuário "Em Risco"**:
    *   **Ação**: Estabelecer critérios de comportamento que indicam uma alta probabilidade de churn.
    *   **Exemplo Concreto**: Um usuário é considerado "em risco" se:
        *   Não logou nos últimos 7 dias E
        *   Não abriu nenhum e-mail de marketing nas últimas 3 campanhas E
        *   Não realizou nenhuma ação chave (ex: compra, criação de conteúdo) nos últimos 15 dias.
2.  **Segmentação de Usuários em Risco por Potencial de LTV**:
    *   **Ação**: Agrupar usuários em risco com base em seu histórico de valor (LTV) ou potencial, para personalizar a abordagem de reativação.
    *   **Exemplo Concreto**:
        *   **Segmento A (Alto LTV)**: Usuários com LTV > R$500, mas inativos.
        *   **Segmento B (Médio LTV)**: Usuários com LTV entre R$100-R$500, inativos.
        *   **Segmento C (Baixo LTV)**: Usuários com LTV < R$100, inativos.
3.  **Criação de Campanhas de Reativação Personalizadas**:
    *   **Ação**: Desenvolver mensagens e ofertas específicas para cada segmento, focando em valor relevante.
    *   **Exemplo Concreto**:
        *   **Segmento A (Alto LTV)**: E-mail com "Sentimos sua falta! Como agradecimento pela sua fidelidade, use este cupom para 25% de desconto em sua próxima compra. Válido por 48h." (Cupom: VOLTE25VIP).
        *   **Segmento B (Médio LTV)**: Push notification com "Novidades! Lançamos recursos que você pediu: [Nome da Feature 1] e [Nome da Feature 2]. Venha conferir!"
        *   **Segmento C (Baixo LTV)**: SMS com "Seu saldo de 150 pontos de recompensa expira em 3 dias! Use-os agora em nossa loja. [Link Curto]".
4.  **Análise de Efetividade e Otimização Contínua**:
    *   **Ação**: Monitorar as taxas de abertura, cliques e, o mais importante, a taxa de reativação (usuários que retornam à atividade) e o LTV subsequente dos usuários reativados.
    *   **Exemplo Concreto**: Se a campanha SMS para o Segmento C tiver uma taxa de reativação de 12% e o LTV médio dos reativados for de R$80 nos próximos 30 dias, ela é considerada um sucesso e pode ser replicada ou otimizada.

---

## Templates

### Email de Reengajamento para Usuário Inativo (30 dias)

```
Assunto: Sentimos sua falta, [Nome do Usuário]! Uma oferta especial te espera.

Olá [Nome do Usuário],

Percebemos que faz um tempinho que você não nos visita e gostaríamos de saber se há algo em que podemos ajudar.

Durante sua última visita, você demonstrou interesse em [Nome do Produto/Categoria de Interesse]. Para te dar um empurrãozinho, preparamos algo especial:

Ganhe 20% de desconto em qualquer produto da categoria [Nome da Categoria de Interesse]!

Use o código: RETORNO20
Válido por 7 dias.

[Botão: Explorar Oferta Agora] (Link para a categoria de interesse ou página de novos produtos)

Temos muitas novidades e recursos que podem te interessar, como [Mencionar uma nova funcionalidade ou coleção].

Esperamos te ver em breve!

Atenciosamente,
A Equipe [Nome da Sua Empresa]
```

### Roteiro de Pesquisa NPS para Identificação de Detratores

```
Título da Pesquisa: Ajude-nos a Melhorar! Sua opinião é muito importante.

Olá [Nome do Usuário],

Na [Nome da Sua Empresa], estamos sempre buscando aprimorar sua experiência. Para nos ajudar nisso, gostaríamos de fazer uma pergunta rápida.

1. Em uma escala de 0 a 10, o quanto você recomendaria [Nome do Produto/Serviço] para um amigo ou colega?
   [Botões de 0 a 10]

Se você nos deu uma nota de 0 a 6 (Detrator):
2. Poderia nos contar o principal motivo da sua nota? O que poderíamos fazer para melhorar sua experiência?
   [Caixa de texto livre]

3. Houve alguma experiência específica (positiva ou negativa) que influenciou sua nota?
   [Caixa de texto livre]

Se você nos deu uma nota de 7 ou 8 (Neutro):
2. O que precisaríamos fazer para que você nos desse uma nota 9 ou 10?
   [Caixa de texto livre]

Se você nos deu uma nota de 9 ou 10 (Promotor):
2. O que você mais gosta em [Nome do Produto/Serviço]?
   [Caixa de texto livre]

Agradecemos imensamente seu tempo e feedback!

[Botão: Enviar Resposta]
```

---

## Checklist

-   [x] Mapear o "Aha! Moment" principal do produto para novos usuários.
-   [x] Implementar uma sequência de e-mails ou notificações no onboarding para guiar o usuário ao "Aha! Moment".
-   [x] Definir critérios claros e mensuráveis para identificar usuários "em risco de churn" (ex: inatividade > 7 dias, baixo engajamento).
-   [x] Segmentar usuários em risco de churn com base em seu LTV histórico ou potencial.
-   [x] Criar e automatizar 3-5 variantes de campanhas de reengajamento (e-mail, push, SMS) para segmentos específicos.
-   [x] Configurar dashboards para monitorar a taxa de retenção por cohort (D1, D7, D30, D90) e Activation Rate.
-   [x] Realizar pesquisas de feedback regulares (NPS, CSAT) com usuários ativos para identificar pontos de dor e valor.
-   [x] Implementar um sistema de monitoramento de saúde do cliente (Customer Health Score) baseado em uso de features, frequência e tempo de sessão.
-   [x] Desenvolver um programa de fidelidade ou gamificação para recompensar o uso contínuo e engajamento.
-   [x] Analisar o churn por causa raiz (ex: preço, usabilidade, falta de suporte) através de pesquisas de saída.

---

## Métricas de Referência

| Métrica               | Benchmark (Média da Indústria) | Meta (Aspiracional) |
|-----------------------|--------------------------------|---------------------|
| Retention Rate D7     | 25-35%                         | 40-45%              |
| Retention Rate D30    | 10-15%                         | 20-25%              |
| Churn Rate Mensal     | 3-5% (SaaS B2C) / 0.5-2% (SaaS B2B) | <2% (B2C) / <0.5% (B2B) |
| LTV:CAC Ratio         | 3:1                            | >4:1                |
| Activation Rate (primeira ação chave) | 60-70%                         | 75-80%              |
| Taxa de Reativação    | 8-12%                          | 15-20%              |

---

## Erros Comuns

1.  **Ignorar o "Aha! Moment" na jornada inicial**: Não guiar o usuário de forma explícita e rápida para o valor principal do produto.
    *   **Exemplo**: Um aplicativo de edição de fotos que exige que o usuário explore vários menus antes de encontrar a função "filtros mágicos", que é seu principal diferencial e o motivo pelo qual a maioria dos usuários se cadastra. Muitos desistem antes de descobrir.
    *   **Como evitar**: Mapear o "Aha! Moment" e simplificar o caminho até ele com tutoriais interativos, mensagens in-app e automações que incentivam a primeira ação de valor.

2.  **Mensagens de reengajamento genéricas para todos os usuários inativos**: Enviar a mesma oferta ou notificação para segmentos de usuários com históricos e potenciais de LTV muito diferentes.
    *   **Exemplo**: Mandar um e-mail "Volte para a plataforma!" com um cupom de 10% para um usuário que já gastou R$1000 e está inativo, e também para um usuário que nunca fez uma compra. A oferta é insuficiente para o primeiro e pode ser genérica para o segundo.
    *   **Como evitar**: Segmentar usuários inativos por comportamento, valor e tempo de inatividade, criando mensagens e ofertas personalizadas (ex: desconto maior para alto LTV, destaque de novas funcionalidades para quem usava bastante uma feature específica).

3.  **Não fechar o loop de feedback**: Coletar feedback de usuários (NPS, pesquisas) mas não ter um processo claro para analisar, agir sobre as sugestões e comunicar as mudanças.
    *   **Exemplo**: Uma empresa recebe consistentemente feedback de detratores sobre a complexidade da interface, mas nenhuma melhoria significativa é implementada, e os usuários não são informados que suas sugestões foram consideradas.
    *   **Como evitar**: Criar um comitê de feedback, priorizar itens de melhoria com base no impacto e esforço, e comunicar ativamente aos usuários as mudanças implementadas, mostrando que suas vozes são ouvidas.

---

## Dicas Avançadas

1.  **Personalização Hiper-segmentada por Nível de Engajamento Preditivo**: Vá além de "ativo/inativo". Crie segmentos dinâmicos como "super-usuário", "usuário ocasional", "usuário em risco (preditivo)", "usuário dorminhoco" com base em modelos de Machine Learning que preveem o comportamento futuro.
    *   **Exemplo Prático**: Um modelo de ML identifica usuários com 80% de chance de churn nas próximas 2 semanas devido a uma queda na frequência de login e interação com features específicas. Estes usuários recebem uma oferta altamente personalizada (ex: "Desconto de 30% na sua assinatura premium, só para você, [Nome do Usuário], por ser um usuário valioso") antes mesmo de se tornarem inativos.

2.  **Gamificação Estratégica Orientada a Metas de Retenção**: Implemente sistemas de pontos, distintivos, níveis e tabelas de classificação que não apenas recompensam o uso, mas direcionam o usuário a explorar funcionalidades que comprovadamente aumentam o LTV.
    *   **Exemplo Prático**: Um aplicativo de produtividade oferece um distintivo "Mestre da Organização" ao usuário que cria 5 projetos, convida 3 colaboradores e conclui 10 tarefas. Cada uma dessas ações é um indicador de retenção. Pontos são acumulados para resgatar "dicas de produtividade premium" ou acesso antecipado a novas features.

3.  **Criação de Comunidades de Usuários e Programas de Embaixadores**: Fomente um senso de pertencimento e valor através de fóruns, grupos sociais exclusivos ou programas onde usuários fiéis se tornam embaixadores.
    *   **Exemplo Prático**: Um software SaaS cria um grupo privado no Slack para seus 500 usuários mais ativos e influentes. Neste grupo, eles recebem acesso antecipado a betas de features, sessões de Q&A com o CEO e são incentivados a compartilhar conhecimento. Esses usuários se tornam defensores da marca, aumentando a retenção por meio do engajamento social e do valor comunitário.

4.  **Recuperação de Churn com Ciclo de Feedback e Oferta de Reengajamento Dinâmica**: Para usuários que cancelaram, implemente um e-mail com pesquisa de saída. Use as respostas para acionar ofertas de reengajamento específicas e altamente relevantes.
    *   **Exemplo Prático**: Usuário cancela assinatura. Recebe e-mail com pesquisa "Por que você cancelou?". Se a resposta for "Preço", automaticamente recebe uma oferta de "3 meses com 50% de desconto para experimentar nossas novas features". Se for "Falta de Tempo", recebe um e-mail com "Recursos para otimizar seu tempo com [Nome do Produto]".

5.  **Customer Health Score Dinâmico com Intervenções Proativas**: Desenvolva um sistema de pontuação de "saúde do cliente" que combine múltiplos fatores (frequência de uso, uso de features chave, tempo de sessão, tickets de suporte, NPS) para atribuir uma pontuação de 0 a 100.
    *   **Exemplo Prático**: Se o "Customer Health Score" de um usuário cair abaixo de 70, um alerta é disparado. Para scores entre 50-70, o usuário recebe uma notificação in-app com "Dicas para aproveitar [Nome do Produto] ao máximo". Para scores abaixo de 50, o time de Customer Success entra em contato proativamente com uma oferta de suporte personalizado ou uma pesquisa para entender os problemas.