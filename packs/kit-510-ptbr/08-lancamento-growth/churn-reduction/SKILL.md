---
name: churn-reduction
description: "Churn Reduction — Skill especializada para prever, mitigar e reduzir a evasão de clientes, otimizando a retenção e o LTV."
license: MIT
metadata:
  version: 1.0.0
  author: Cafe Code AI
  category: 08-lancamento-growth
  updated: 2026-03-01
risk: none
---

# Churn Reduction

Esta skill capacita o Claude a implementar estratégias avançadas para identificar, prever e mitigar a evasão de clientes (churn), otimizando a retenção e o LTV.

---

## Keywords

Evasão de clientes, retenção SaaS, LTV, NRR, churn preditivo, health score do cliente, reengajamento de usuários, campanhas de win-back, análise de cohort, CSAT, NPS, fricção do cliente, sticky features, funil de retenção.

---

## Quick Start

1.  Configure um painel de monitoramento diário para a taxa de churn e engajamento das funcionalidades "core" dos últimos 7 dias.
2.  Extraia dados dos últimos 30 dias de clientes que cancelaram, focando em padrões de uso e suporte imediatamente antes do churn.
3.  Desenvolva uma campanha de e-mail automatizada para clientes que não logaram há 14 dias, oferecendo um recurso-chave pouco explorado.
4.  Implemente uma pesquisa de saída obrigatória com campo aberto para coletar feedback direto e categorizável sobre o motivo do cancelamento.

---

## Core Workflows

### Workflow 1: Análise Preditiva e Intervenção Proativa de Churn

Este workflow detalha a criação de um sistema para identificar clientes em risco de churn *antes* que eles cancelem, permitindo intervenções proativas e personalizadas.

-   **Passo 1: Coleta e Unificação de Dados Relevantes (D+0)**
    Integre dados de múltiplas fontes para criar uma visão 360° do cliente. Isso inclui dados de uso do produto (frequência de login, funcionalidades utilizadas, tempo de sessão, número de projetos/tarefas criadas), histórico de suporte (número de tickets, tipo de problema, CSAT), dados de faturamento (ciclo de pagamento, upgrades/downgrades, atrasos), e dados demográficos/firmográficos.
    *Exemplo:* Para um SaaS de gestão de projetos, colete dados sobre o número de projetos ativos, usuários ativos por conta, frequência de uso do chat interno da plataforma, relatórios gerados e histórico de pagamentos. Se um cliente que pagava mensalmente mudou para trimestral, isso é um sinal.

-   **Passo 2: Modelagem Preditiva de Risco de Churn (D+1 a D+7)**
    Utilize técnicas de machine learning (como Regressão Logística, Random Forest ou XGBoost) para construir um modelo que preveja a probabilidade de churn de cada cliente. As features do modelo podem incluir: queda de 30% no uso semanal de uma funcionalidade crítica, aumento de 2 tickets de suporte em 7 dias, atraso no pagamento, baixa adesão a funcionalidades "core" (ex: menos de 30% dos usuários que deveriam usar uma funcionalidade chave não a utilizam). Atribua um "Health Score" (0-10) para cada cliente, onde 0 é alto risco e 10 é baixo risco.
    *Exemplo de regra para Health Score simplificado:* `(0.4 * %UsoFuncionalidadesChave) + (0.3 * %PontualidadePagamento) + (0.2 * CSATMedio) - (0.1 * NumTicketsSuporteUltimos30Dias)`. Clientes com score abaixo de 6 são automaticamente classificados como "em risco".

-   **Passo 3: Acionamento de Planos de Sucesso do Cliente (D+8)**
    Clientes com Health Score abaixo do limiar pré-definido (ex: 6) são categorizados como "em risco". O time de Customer Success (CS) deve ser alertado via CRM/Slack e acionar um playbook de intervenção específico, adaptado ao motivo provável do risco.
    *Exemplo de Plano de Ação para Cliente A (SaaS B2B, Health Score 5.5):*
    1.  **Notificação Interna (D+8, 9h):** Alerta via sistema de CRM para o gerente de contas: "Cliente A (Empresa X) em risco de churn. Queda de 40% no uso da funcionalidade de relatórios avançados na última semana e 2 tickets de suporte abertos."
    2.  **Análise Detalhada (D+8, 10h):** O gerente de contas revisa o histórico de uso e suporte do Cliente A. Identifica que a equipe do Cliente A tem usado menos a funcionalidade de relatórios desde a última atualização do sistema.
    3.  **Contato Proativo (D+8, 14h):** E-mail personalizado do CS: "Olá [Nome do Ponto de Contato], notamos uma diminuição no uso dos relatórios avançados em sua conta. Houve alguma dificuldade com a nova interface ou na extração de dados específicos? Gostaria de agendar uma sessão rápida de 15 minutos para mostrar as melhorias e como otimizar seus dashboards?"
    4.  **Oferta de Valor (D+9):** Se o cliente aceitar, agendar um treinamento focado em como extrair o máximo da funcionalidade de relatórios pós-atualização. Caso contrário, enviar um guia em PDF ou vídeo tutorial focado em como usar a nova interface.

-   **Passo 4: Monitoramento e Ajuste (Contínuo)**
    Monitore a taxa de sucesso das intervenções (aumento do Health Score, reengajamento em funcionalidades chave). Ajuste os gatilhos do Health Score, os playbooks de CS e os modelos preditivos conforme os resultados.
    *Exemplo:* Se a taxa de resposta aos e-mails proativos para clientes em risco de churn por "dificuldade de uso" for baixa, teste diferentes linhas de assunto, ofereça um webinar exclusivo ou utilize um canal de contato alternativo (ex: ligação telefônica ou WhatsApp).

### Workflow 2: Estratégias de Reengajamento para Usuários Inativos

Este workflow foca em como reativar usuários que já demonstraram sinais claros de inatividade, mas ainda não churnaram formalmente.

-   **Passo 1: Segmentação de Usuários Inativos (D+0)**
    Classifique usuários que não realizaram uma ação-chave (login, uso de funcionalidade principal, compra) por um período específico, que varia de acordo com o produto. Segmente por:
    -   **Inativos Recentes (7-14 dias):** Ainda há chance de reativação com mensagens de lembrete e valor.
    -   **Inativos Moderados (15-45 dias):** Requer mais incentivo e valor adicionado.
    -   **Dormantes (46-90 dias):** Campanhas de "win-back" ou "última chance" mais agressivas.
    Considere também segmentar por tipo de plano (premium vs. gratuito), LTV projetado, e funcionalidades usadas anteriormente.
    *Exemplo:* Para um aplicativo de fitness, "inativo" significa não registrar um treino por 7 dias. Segmentar por tipo de plano (premium vs. gratuito) e último tipo de treino (musculação, corrida) é crucial para personalizar a mensagem.

-   **Passo 2: Criação de Campanhas de Reengajamento Personalizadas (D+1 a D+7)**
    Desenvolva mensagens e ofertas que ressoem com o segmento de inatividade e o motivo provável da saída. Utilize múltiplos canais (e-mail, push notification, SMS, in-app messages).
    *Exemplo para Inativos Recentes (7-14 dias, app de fitness, plano gratuito):*
    -   **Canal:** Notificação push no app e e-mail.
    -   **Mensagem Push (D+7):** "Sentimos sua falta, [Nome]! 🏃‍♀️ Seu desafio semanal está esperando. Que tal um treino rápido hoje para retomar o ritmo?"
    -   **E-mail (D+8):** "Não desista dos seus objetivos! 💪 Vimos que você não logou nos últimos dias. Queremos te ajudar a voltar à rotina. Responda a este e-mail com seu principal obstáculo e te daremos uma dica personalizada para superá-lo!"
    *Exemplo para Inativos Moderados (15-45 dias, SaaS de design, plano pago):*
    -   **Canal:** E-mail e, se não houver resposta, contato do CS (para planos de maior valor).
    -   **E-mail (D+15):** "Novidades no [Nome da Ferramenta]! ✨ Lançamos o recurso 'Colaboração em Tempo Real' que simplifica o trabalho em equipe e otimiza a revisão de projetos. Pensamos que você e sua equipe iriam adorar. Veja um vídeo rápido [Link para vídeo tutorial de 2 min]."
    -   **Oferta de Valor (D+20, se não houver reengajamento):** "Para te ajudar a experimentar, sua conta foi atualizada para o plano Pro por 7 dias, sem custo. Aproveite os recursos extras e veja como eles podem acelerar seus projetos!"

-   **Passo 3: Execução e Testes A/B (D+8 em diante)**
    Lance as campanhas e monitore as métricas de engajamento (taxa de abertura, cliques, logins, uso da funcionalidade chave). Otimize continuamente através de testes A/B com diferentes linhas de assunto, CTAs, ofertas, criativos e horários de envio.
    *Exemplo:* Testar "Seu treino te espera!" vs. "Volte a queimar calorias!" na notificação push. Analisar qual variante gera maior taxa de cliques e reativação.

-   **Passo 4: Análise e Feedback