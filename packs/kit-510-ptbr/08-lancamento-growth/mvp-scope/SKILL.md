---
name: mvp-scope
description: "Mvp Scope — Skill especializada para mvp scope"
license: MIT
metadata:
  version: 1.0.0
  author: Cafe Code AI
  category: 08-lancamento-growth
  updated: 2026-03-01
risk: safe
---

# Mvp Scope

Esta skill capacita o Claude a definir, priorizar e validar o escopo mínimo viável de um produto, maximizando o aprendizado e minimizando o desperdício em lançamentos de growth.

---

## Keywords

Escopo Mínimo Viável, RICE Scoring, Priorização de Features, Validação de Hipóteses, Early Adopters, Taxa de Ativação, Retenção, Product-Market Fit, Testes A/B, Funil de Ativação, Desinvestimento, Growth Hacking.

---

## Quick Start

1.  **Formular Hipótese de Valor:** Articular claramente o problema que o produto resolve para um segmento específico e como a solução proposta entrega valor. Ex: "Ajudar freelancers a gerenciar propostas mais rápido para fechar 20% mais negócios."
2.  **Mapear Jornada Crítica do Usuário:** Desenhar os 3-5 passos essenciais que o usuário precisa executar para experimentar o valor central do produto. Ex: Cadastro > Criação da primeira proposta > Envio da proposta.
3.  **Priorizar Features RICE:** Aplicar a metodologia RICE (Reach, Impact, Confidence, Effort) para ranquear as funcionalidades que compõem a jornada crítica, focando naquelas com maior impacto e menor esforço.
4.  **Definir Métrica de Sucesso do MVP:** Escolher uma única métrica primária que valide a hipótese de valor. Ex: "50% dos usuários que criam uma proposta a enviam nos primeiros 7 dias."
5.  **Comunicar Escopo Negativo:** Listar explicitamente o que *não* faz parte do MVP para evitar desvios e expectativas desalinhadas com stakeholders.

---

## Core Workflows

### Workflow 1: Priorização de Features com RICE para MVP

Este workflow detalha o processo de seleção das funcionalidades mais críticas para o Escopo Mínimo Viável (MVP), garantindo que o produto entregue o valor essencial com o menor investimento inicial.

1.  **Identificação de Problemas Centrais do Usuário:**
    *   **Ação:** Conduzir 5-10 entrevistas aprofundadas com potenciais usuários do segmento-alvo ou analisar dados de feedback de produtos existentes (ex: pesquisas NPS, tickets de suporte).
    *   **Exemplo:** Um grupo de freelancers relata consistentemente a dificuldade em "rastrear o status de múltiplas propostas enviadas" e "personalizar rapidamente templates de propostas". Estes são os problemas-raiz a serem resolvidos.
2.  **Brainstorming de Soluções/Features e Geração de Ideias:**
    *   **Ação:** Em uma sessão de 60 minutos com equipe multidisciplinar (produto, design, engenharia), gerar no mínimo 20 ideias de funcionalidades que abordam os problemas identificados. Não há julgamento nesta fase.
    *   **Exemplo:** Para "rastrear status": notificação de leitura, painel de controle com status, integração com CRM. Para "personalizar templates": editor drag-and-drop, biblioteca de blocos reutilizáveis.
3.  **Avaliação RICE para Cada Feature Proposta:**
    *   **Ação:** Para cada feature, atribuir uma pontuação (1 a 10 para I, C; número de usuários para R; horas ou dias para E) e calcular RICE = (Reach * Impact * Confidence) / Effort.
        *   **Reach (Alcance):** Quantos usuários serão afetados pela feature em um período (ex: 1 mês)? (Ex: 1000 usuários/mês)
        *   **Impacto:** Quanto essa feature impacta a métrica primária do MVP? (Ex: 3 = Massivo, 2 = Alto, 1 = Médio, 0.5 = Baixo, 0.25 = Mínimo)
        *   **Confiança:** Qual a certeza de que essa feature terá o impacto esperado? (Ex: 100% = Alta, 80% = Média, 50% = Baixa)
        *   **Esforço:** Quantas "pessoa-semanas" são necessárias para construir a feature (ex: 0.5 = 1 dia, 1 = 1 semana, 4 = 1 mês)?
    *   **Exemplo de Pontuação:**
        *   **Feature: Painel de Controle de Propostas:** R: 800 usuários/mês, I: 2 (Alto), C: 80% (0.8), E: 3 semanas. RICE = (800 * 2 * 0.8) / 3 = 426.67
        *   **Feature: Editor Drag-and-Drop de Templates:** R: 500 usuários/mês, I: 3 (Massivo), C: 60% (0.6), E: 8 semanas. RICE = (500 * 3 * 0.6) / 8 = 112.5
4.  **Definição do Escopo Core e Descarte:**
    *   **Ação:** Selecionar as features com maior pontuação RICE que, juntas, resolvem o problema central do usuário e permitem a validação da hipótese de valor com o menor número de funcionalidades. Features abaixo de um limite de pontuação ou que não são essenciais para a jornada crítica são descartadas do MVP.
    *   **Exemplo:** O "Painel de Controle de Propostas" é priorizado para o MVP, enquanto o "Editor Drag-and-Drop" é movido para uma fase posterior devido ao alto esforço e menor RICE inicial, mesmo com alto impacto.
5.  **Documentação do Escopo Negativo:**
    *   **Ação:** Criar uma lista explícita de funcionalidades que *não* serão desenvolvidas no MVP, comunicando-a a todos os stakeholders. Isso gerencia expectativas e evita "feature creep".
    *   **Exemplo:** "O MVP não incluirá: integração com calendários externos, faturamento automático, chat embutido para propostas."

### Workflow 2: Validação de Hipóteses com Landing Page & Early Adopters

Este workflow foca em validar a proposta de valor do MVP antes mesmo de sua construção completa, usando técnicas de baixo custo e alta velocidade para coletar feedback real e dados de interesse.

1.  **Formulação da Hipótese de Valor Clara e Testável:**
    *   **Ação:** Escrever uma frase concisa que articule o segmento de cliente, o problema, a solução proposta e o benefício único.
    *   **Exemplo:** "Acreditamos que freelancers iniciantes (segmento) têm dificuldade em criar propostas profissionais rapidamente (problema). Ofereceremos uma ferramenta de geração de propostas com templates pré-aprovados (solução) para ajudá-los a fechar mais clientes em menos tempo (benefício)."
2.  **Construção de Landing Page Minimalista para Teste de Demanda:**
    *   **Ação:** Criar uma página única com a proposta de valor do MVP, um vídeo explicativo (opcional), e um Call-to-Action (CTA) claro para "Inscrever-se na Lista de Espera" ou "Solicitar Acesso Antecipado". Utilizar ferramentas como Webflow, Carrd ou Leadpages.
    *   **Exemplo:** Uma landing page que destaca "Crie Propostas Vencedoras em Minutos!" com um formulário de e-mail e a promessa de "acesso beta exclusivo".
3.  **Execução de Campanha de Aquisição de Early Adopters:**
    *   **Ação:** Direcionar tráfego qualificado para a landing page usando anúncios pagos (Google Ads, LinkedIn Ads segmentado por "freelancer", "empreendedor individual") ou posts orgânicos em comunidades relevantes (grupos de Facebook, Reddit, Slack).
    *   **Exemplo:** Campanha no LinkedIn segmentada para "Designers Gráficos Freelancers" com o título "Cansado de propostas genéricas? Beta para ferramenta que dobra suas chances!".
4.  **Definição e Análise de Métricas de Validação da Demanda:**
    *   **Ação:** Monitorar a Taxa de Conversão da Landing Page (número de inscrições / número de visitantes) e o Custo por Aquisição (CPA) de e-mail.
    *   **Exemplo:** Se a taxa de conversão da LP for inferior a 5% com um CPA acima de R$10 para um produto de assinatura de R$29/mês, isso pode indicar baixo interesse ou desalinhamento da proposta. Meta inicial: 10-15% de conversão.
5.  **Condução de Entrevistas de Validação com Early Adopters:**
    *   **Ação:** Contatar os primeiros 10-20 inscritos na lista de espera para entrevistas de 30 minutos, focando em seus problemas atuais, como eles os resolvem hoje, e a percepção de valor da solução proposta. O objetivo é entender se a solução ressoa e se estão dispostos a pagar.
    *   **Exemplo:** Perguntar: "Como você gerencia o envio de propostas hoje? Quais são as maiores frustrações? Quanto você pagaria por uma ferramenta que resolvesse X, Y e Z?"
6.  **Análise de Feedback e Decisão de Pivô/Persistência:**
    *   **Ação:** Consolidar os insights das entrevistas e os dados da landing page. Se houver forte validação (alta conversão, feedback positivo sobre a dor e a solução), persistir no desenvolvimento do MVP. Caso contrário, considerar um pivô na proposta de valor ou no segmento-alvo.
    *   **Exemplo:** Se 80% dos entrevistados confirmam a dor e expressam interesse em pagar, e a LP converteu 12%, a hipótese é validada. Se 60% acham a dor "não tão grande" e a LP converteu 3%, um pivô é necessário.

---

## Templates

### Documento de Escopo MVP Simplificado

```markdown
# Documento de Escopo MVP: Gerenciador de Propostas para Freelancers

**Data:** 2024-10-27
**Versão:** 1.0

## 1. Problema a Ser Resolvido

Freelancers gastam tempo excessivo na criação e acompanhamento manual de propostas, resultando em perda de oportunidades de negócio e dificuldade em escalar. A falta de profissionalismo nas propostas também pode impactar a percepção de valor.

## 2. Hipótese de Valor Principal

Acreditamos que uma ferramenta simplificada de criação e gestão de propostas, com templates profissionais e acompanhamento de status, ajudará freelancers a fechar mais negócios, economizando 2 horas por semana na gestão de propostas.

## 3. Segmento de Usuário Alvo

Freelancers autônomos (designers, redatores, consultores) com até 3 anos de experiência, faturando entre R$2.000 e R.000/mês, buscando otimizar processos e profissionalizar sua comunicação.

## 4. Funcionalidades Essenciais do MVP (Jornada Crítica)

1.  **Cadastro e Login de Usuário:** Acesso seguro à plataforma.
2.  **Criação de Proposta:**
    *   Seleção de template base (3 opções pré-definidas).
    *   Edição de texto simples (título, descrição, itens de serviço, preço).
    *   Adição de logo do freelancer.
3.  **Visualização e Envio de Proposta:**
    *   Gerar PDF da proposta.
    *   Compartilhamento de link da proposta para o cliente.
4.  **Painel de Acompanhamento de Propostas:**
    *   Listagem de propostas enviadas.
    *   Status básico: "Enviado", "Visualizado", "Aceito", "Rejeitado".
    *   Notificação simples quando a proposta é visualizada.

## 5. Métricas de Sucesso do MVP

*   **Métrica Primária:** Taxa de envio de propostas: 40% dos usuários que criam uma proposta a enviam para um cliente nos primeiros 7 dias.
*   **Métrica Secundária:** Taxa de visualização: 70% das propostas enviadas são visualizadas pelos clientes.
*   **Feedback Qualitativo:** 80% dos early adopters reportam economia de tempo na criação de propostas.

## 6. O Que NÃO Faz Parte do MVP (Escopo Negativo)

*   Editor avançado de arrastar e soltar (drag-and-drop).
*   Integração com CRMs ou sistemas de faturamento.
*   Chat embutido para comunicação com clientes.
*   Geração automática de contratos.
*   Análise de dados avançada sobre propostas (ex: taxa de aceitação por serviço).
*   Múltiplos usuários por conta.
```

### Matriz de Priorização RICE (Exemplo Preenchido)

```markdown
# Matriz de Priorização RICE para MVP: Gerenciador de Propostas

| Feature                                     | Reach (Usuários/mês) | Impacto (1-3) | Confiança (0.5-1.0) | Esforço (Pessoa-semanas) | RICE Score | Prioridade |
| :------------------------------------------ | :------------------: | :-----------: | :-----------------: | :----------------------: | :--------: | :--------: |
| **1. Cadastro e Login Simples**             | 1000                 | 1             | 1.0                 | 1                        | 1000       | Essencial  |
| **2. Criação de Proposta c/ Templates**     | 900                  | 2             | 0.9                 | 2                        | 810        | Essencial  |
| **3. Compartilhamento Link & PDF**          | 850                  | 2             | 0.9                 | 1                        | 1530       | Essencial  |
| **4. Painel de Acompanhamento (Status)**    | 700                  | 2             | 0.8                 | 2                        | 560        | Essencial  |
| 5. Notificação de Visualização de Proposta  | 600                  | 1             | 0.7                 | 0.5                      | 840        | Alta       |
| 6. Editor Drag-and-Drop de Propostas        | 500                  | 3             | 0.6                 | 8                        | 112.5      | Baixa      |
| 7. Integração com Calendário (Agendamento)  | 300                  | 1             | 0.5                 | 3                        | 50         | Descartado |
| 8. Geração de Relatórios Financeiros        | 200                  | 0.5           | 0.6                 | 4                        | 15         | Descartado |
| 9. Biblioteca de Clientes                   | 400                  | 1             | 0.8                 | 1.5                      | 213        | Média      |
```

---

## Checklist

- [x] O problema central do usuário está claramente articulado e validado por pesquisa?
- [x] A hipótese de valor do MVP é específica, mensurável e testável?
- [x] O segmento de usuário-alvo é bem definido e acessível para feedback?
- [x] A jornada crítica do usuário (core loop) foi mapeada com os passos mínimos?
- [x] Todas as features incluídas no MVP foram priorizadas usando uma metodologia como RICE ou MoSCoW?
- [x] Existe uma única métrica primária de sucesso do MVP com um target claro?
- [x] O "escopo negativo" (o que não será construído no MVP) foi explicitamente documentado e comunicado?
- [x] Há um plano claro para coletar feedback de early adopters imediatamente após o lançamento do MVP?
- [x] A equipe está alinhada quanto à visão do MVP como uma ferramenta de aprendizado, não um produto final?
- [x] Os recursos alocados (tempo, pessoas) são realistas para o escopo definido?

---

## Métricas de Referência

| Métrica                         | Benchmark (Indústria SAAS B2B) | Meta para MVP (Exemplo) |
| :------------------------------ | :----------------------------- | :---------------------- |
| **Taxa de Ativação (24h)**      | 20-30%                         | 40%                     |
| **Taxa de Retenção (D7)**       | 15-25%                         | 30%                     |
| **Taxa de Conversão LP (Beta)** | 5-10%                          | 12%                     |
| **Custo por Aquisição (CPA)**   | R$50-R$200                     | R$75                    |
| **Net Promoter Score (NPS)**    | >30                            | >45                     |
| **Tempo para Primeira Ação (TTFA)** | < 5 minutos                  | < 2 minutos             |

---

## Erros Comuns

1.  **Escopo Inflacionado ("Feature Creep")**: Aumentar continuamente o número de funcionalidades do MVP antes do lançamento, transformando-o em um "Produto Mínimo Viável".
    *   **Como evitar**: Implementar a matriz RICE rigorosamente, descartando features com baixo RICE. Explicar a equipe que cada adição atrasa o aprendizado e aumenta o risco. Se um stakeholder pedir uma feature extra, perguntar: "Qual feature do escopo atual devemos remover para acomodar esta, mantendo o prazo do MVP?"
2.  **Ignorar Feedback de Early Adopters**: Lançar o MVP e não ter um canal estruturado para coletar e agir sobre o feedback dos primeiros usuários, perdendo a oportunidade de validação.
    *   **Como evitar**: Integrar ferramentas de feedback (ex: Intercom, Typeform) diretamente no MVP. Agendar entrevistas de 15 minutos com os 10-20 primeiros usuários ativos para entender suas dores e ganhos. Ex: "Percebemos que você usou a feature X. O que você esperava que ela fizesse que não fez?"
3.  **Focar em Soluções, Não em Problemas**: Construir um produto com base em suposições sobre o que o usuário quer, em vez de validar os problemas reais que ele enfrenta.
    *   **Como evitar**: Iniciar sempre com a formulação da hipótese de problema e validá-la antes de pensar na solução. Durante as entrevistas, focar 80% do tempo em entender o problema do usuário e apenas 20% na solução proposta. Ex: Em vez de perguntar "Você usaria um painel de propostas?", perguntar "Como você se sente ao ter que verificar o status de cada proposta manualmente?"

---

## Dicas Avançadas

1.  **Técnica de "Fumaça e Espelhos" (Concierge ou Mágico de Oz)**: Antes de construir qualquer software, simule a funcionalidade chave manualmente. Ex: Para testar a ideia de um "gerador de propostas", um membro da equipe pode criar as propostas manualmente para os primeiros clientes, validando o valor antes de investir em código. Isso permite coletar feedback real sobre o *output* sem o *input* de engenharia.
2.  **Loop de Feedback Contínuo e Semanal**: Estabelecer um ritual de feedback semanal com early adopters. A cada semana, lançar uma pequena melhoria baseada no feedback anterior e coletar novas reações. Isso cria um ciclo virtuoso de construção-medição-aprendizado rápido e mantém o MVP vivo e relevante. Ex: Toda sexta-feira, enviar um e-mail com "Esta semana, adicionamos X. O que você achou?"
3.  **Desinvestir em Features Não Validadas**: Ter a coragem de remover funcionalidades que, mesmo após lançadas no MVP, não geram engajamento ou não resolvem um problema real para os usuários. Isso libera recursos e simplifica o produto. Ex: Se a "notificação de visualização de proposta" no Painel de Acompanhamento é ignorada por 90% dos usuários, considerar removê-la para simplificar a UI e o código.
4.  **A/B Testes de Proposta de Valor na Landing Page**: Antes mesmo do MVP, testar diferentes mensagens de valor na landing page. Criar 2-3 versões da página com CTA idêntico, mas com diferentes copy e títulos, e direcionar tráfego para cada uma para ver qual gera maior taxa de conversão. Isso otimiza a mensagem para o lançamento. Ex: Testar "Crie Propostas 2x Mais Rápido" vs. "Feche Mais Clientes Com Propostas Profissionais".
5.  **Análise de "Jobs To Be Done" (JTBD)**: Em vez de focar apenas em funcionalidades, entender os "trabalhos" que o usuário está tentando realizar. O MVP deve ajudar o usuário a "contratar" seu produto para fazer um "trabalho" melhor. Ex: O freelancer não quer um "gerador de propostas", ele quer "conquistar clientes de forma mais eficiente e profissional". O MVP deve ser a melhor ferramenta para esse "job".