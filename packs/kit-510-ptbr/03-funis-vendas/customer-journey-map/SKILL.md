---
name: customer-journey-map
description: "Customer Journey Map — Skill especializada para customer journey map"
license: MIT
metadata:
  version: 1.0.0
  author: Cafe Code AI
  category: 03-funis-vendas
  updated: 2026-03-01
risk: safe
---

# Customer Journey Map

Esta skill capacita o Claude a desenvolver, analisar e otimizar mapas de jornada do cliente focados em funis de vendas digitais, desde a descoberta até a pós-compra.

---

## Keywords

Jornada do Cliente, Mapeamento de Experiência, Funil de Vendas, Touchpoints, Personas de Vendas, Dor do Cliente, Ganhos do Cliente, Otimização de Conversão, Emoções do Cliente, Pontos de Fricção, Canais de Interação, Pós-Venda, Retenção, Landing Pages.

---

## Quick Start

1.  **Selecione uma persona central**: Escolha "Ana, 32 anos, empreendedora digital buscando ferramentas de automação de marketing" para iniciar o mapeamento.
2.  **Liste os 3-5 macro-estágios iniciais da jornada**: Identifique "Consciência do Problema", "Busca por Soluções", "Avaliação de Ferramentas".
3.  **Enumere os touchpoints digitais para cada estágio**: Para "Busca por Soluções", inclua "Pesquisa Google ('melhor automação marketing')", "Anúncio no Instagram", "Postagem de blog sobre produtividade".
4.  **Identifique a principal dor e emoção em cada touchpoint**: No anúncio do Instagram, a dor pode ser "perda de tempo com tarefas manuais" e a emoção "frustração".
5.  **Proponha uma oportunidade de otimização**: Para o anúncio, "refinar copy para abordar diretamente a dor da perda de tempo com a promessa de automação eficiente".

---

## Core Workflows

### Workflow 1: Construção de um Mapa de Jornada para Lançamento de Curso Online

Este workflow detalha a criação de um Customer Journey Map (CJM) para um novo curso online de "Marketing Digital para Iniciantes", focando na conversão de leads frios em alunos.

**Passos Detalhados:**

1.  **Hipótese de Persona Detalhada**:
    *   **Ação**: Desenvolver uma persona robusta com dados demográficos, psicográficos, dores e objetivos relacionados ao curso.
    *   **Exemplo**:
        ```
        Persona: Mariana, A Iniciante Ambiciosa
        Idade: 28 anos
        Ocupação: Recém-formada em Administração, buscando transição de carreira para marketing digital.
        Renda: R$ 3.500/mês
        Dores: Falta de experiência prática, medo de investir em cursos caros e ineficazes, sobrecarga de informações online, não sabe por onde começar.
        Objetivos: Conquistar o primeiro emprego em marketing digital, construir um portfólio, aprender as bases do marketing de forma estruturada e prática.
        Canais preferidos: Instagram, LinkedIn, YouTube (tutoriais), blogs especializados.
        ```
2.  **Definição dos Estágios da Jornada e Ações do Cliente**:
    *   **Ação**: Mapear os estágios desde a "Descoberta" até a "Matrícula", listando as ações específicas da Mariana em cada um.
    *   **Exemplo**:
        *   **Descoberta**: Pesquisar "como começar no marketing digital" no Google, ver anúncio no Instagram.
        *   **Consideração**: Clicar em anúncio, acessar landing page do curso, assistir a um webinar gratuito, baixar e-book.
        *   **Decisão**: Comparar o curso com concorrentes, ler depoimentos, participar de grupo VIP no WhatsApp, tirar dúvidas com consultor.
        *   **Matrícula**: Realizar pagamento, receber e-mail de boas-vindas.
3.  **Identificação de Touchpoints e Pontos de Fricção**:
    *   **Ação**: Para cada ação, identificar o canal de interação (touchpoint) e os potenciais pontos de dor ou fricção.
    *   **Exemplo (Estágio: Consideração)**:
        *   **Ação**: Clicar em anúncio do Instagram.
        *   **Touchpoint**: Anúncio no feed do Instagram.
        *   **Fricção**: Copy do anúncio genérica, não destacando o diferencial para iniciantes. CTR esperado: 0.8%.
        *   **Ação**: Acessar landing page do curso.
        *   **Touchpoint**: Landing page de vendas.
        *   **Fricção**: Página carregando lentamente (>3s), proposta de valor confusa, falta de prova social visível. Taxa de rejeição esperada: 65%.
        *   **Ação**: Baixar e-book "Guia Rápido de Marketing Digital".
        *   **Touchpoint**: Formulário de lead na landing page.
        *   **Fricção**: Formulário longo (pedindo telefone e empresa), não alinhado com a promessa de "guia rápido". Taxa de conversão de formulário esperada: 12%.
4.  **Mapeamento de Emoções e Oportunidades**:
    *   **Ação**: Atribuir uma emoção predominante a cada touchpoint e propor oportunidades de melhoria.
    *   **Exemplo (Estágio: Consideração, Touchpoint: Landing Page)**:
        *   **Emoção Atual**: Confusão, Ceticismo ("Será que é para mim?").
        *   **Oportunidade**: A/B testar diferentes títulos na LP focando em "para iniciantes", adicionar seção de FAQ visível, incluir depoimentos de ex-alunos com perfis semelhantes à Mariana. Objetivo: Aumentar taxa de conversão da LP de 5% para 8%.
5.  **Criação de Ações Internas e Métricas**:
    *   **Ação**: Definir o que a equipe precisa fazer e quais métricas acompanhar para cada oportunidade.
    *   **Exemplo (Oportunidade: Otimizar Landing Page)**:
        *   **Ação Interna**: Revisar copy da LP, otimizar imagens e velocidade de carregamento, desenvolver novos CTAs.
        *   **Métrica**: Taxa de Conversão da Landing Page (Meta: 8%), Tempo de Carregamento da Página (Meta: <2s).

### Workflow 2: Otimização de Funil de Vendas Existente via CJM

Este workflow foca em usar um CJM para identificar e resolver gargalos em um funil de vendas B2B existente para um software SaaS de gestão de projetos.

**Passos Detalhados:**

1.  **Revisão de Dados de Funil Existente**:
    *   **Ação**: Analisar métricas de funil (Google Analytics, CRM) para identificar estágios com quedas significativas.
    *   **Exemplo**:
        *   **Funil Atual**:
            *   Visitas ao site: 10.000
            *   Downloads de material rico (e-book): 800 (8% de conversão)
            *   Solicitações de demonstração: 80 (10% dos downloads)
            *   Demonstrações realizadas: 60 (75% das solicitações)
            *   Testes gratuitos iniciados: 15 (25% das demonstrações)
            *   Assinaturas pagas: 3 (20% dos testes)
        *   **Gargalo Principal**: Queda acentuada entre "Demonstrações realizadas" e "Testes gratuitos iniciados" (de 60 para 15).
2.  **Mapeamento da Jornada do Gargalo**:
    *   **Ação**: Focar no estágio imediatamente anterior e posterior ao gargalo, detalhando ações, touchpoints e emoções.
    *   **Exemplo (Estágio: Pós-Demonstração / Pré-Teste Gratuito)**:
        *   **Ações do Cliente**: Participar da demo, receber e-mail de follow-up, tentar acessar o teste, buscar informações sobre preço.
        *   **Touchpoints**: E-mail de agendamento, reunião via Zoom, e-mail de follow-up pós-demo, página de cadastro para teste, página de preços.
3.  **Entrevistas com Clientes (Win/Loss Analysis)**:
    *   **Ação**: Conduzir entrevistas com clientes que *não* avançaram para o teste gratuito e com alguns que *avançaram*.
    *   **Exemplo**:
        *   **Insights (não avançaram)**: "A demo foi muito genérica, não mostrou como resolver *meu* problema específico." "O e-mail de follow-up parecia spam, com link para o teste pouco visível." "O processo de cadastro para o teste gratuito é muito burocrático, pede cartão de crédito imediatamente."
        *   **Insights (avançaram)**: "O vendedor foi excelente, personalizou a demo." "O link para o teste estava claro no e-mail."
4.  **Identificação de Dores e Oportunidades de Otimização**:
    *   **Ação**: Com base nas entrevistas e dados, identificar as dores reais e propor soluções.
    *   **Exemplo**:
        *   **Dor Identificada**: Falta de personalização na demo e fricção no acesso ao teste gratuito.
        *   **Oportunidades**:
            *   **Personalização da Demo**: Treinar equipe de vendas para solicitar informações pré-demo e personalizar o script. Meta: Aumentar taxa de "Demonstrações -> Testes" de 25% para 40%.
            *   **E-mail de Follow-up**: Refatorar o e-mail, tornando o CTA para o teste mais proeminente e explicando o valor do teste. Incluir um vídeo curto "Como começar seu teste".
            *   **Cadastro do Teste Gratuito**: Remover a exigência de cartão de crédito no primeiro passo, simplificar o formulário, adicionar um "tour guiado" inicial no produto.
5.  **Implementação e Monitoramento**:
    *   **Ação**: Implementar as mudanças e monitorar as métricas de conversão.
    *   **Exemplo**: Lançar novas versões de e-mail e página de cadastro, acompanhar a taxa de conversão de "Demonstrações realizadas" para "Testes gratuitos iniciados" semanalmente.

---

## Templates

### Segmento de Persona Detalhada para CJM

```
Nome da Persona: Lucas, O Gestor Ocupado
Idade: 45 anos
Ocupação: Gerente de Projetos em Agência de Marketing Digital
Renda: R$ 9.000/mês
Família: Casado, 2 filhos
Localização: São Paulo, SP
Formação: Pós-graduação em Gestão de Projetos
Dores Principais:
  - Dificuldade em visualizar o progresso de múltiplos projetos simultaneamente.
  - Perda de prazos devido a comunicação ineficiente entre equipes.
  - Ferramentas atuais (planilhas, e-mail) são arcaicas e demandam muito tempo manual.
  - Pressão para entregar resultados e otimizar a produtividade da equipe.
  - Medo de que a equipe não adote uma nova ferramenta complexa.
Objetivos:
  - Centralizar a comunicação e o gerenciamento de tarefas.
  - Reduzir o tempo gasto em reuniões de status.
  - Aumentar a transparência e a responsabilidade da equipe.
  - Implementar uma solução que seja intuitiva e fácil de usar.
  - Obter relatórios claros para apresentações à diretoria.
Canais Preferidos: LinkedIn (artigos, notícias), e-mail (newsletters de tecnologia), blogs de produtividade, eventos de gestão.
Citações Típicas: "Preciso de algo que realmente simplifique a vida da minha equipe, não que complique.", "O tempo é ouro, não posso perder com burocracia de ferramenta."
Frustrações: Falta de integração entre ferramentas, complexidade excessiva de softwares "avançados", resistência da equipe a mudanças.
Motivações de Compra: Economia de tempo, aumento da produtividade, redução de erros, melhoria na comunicação, escalabilidade da solução.
```

### Trecho de Customer Journey Map (Fase de Consideração - Software SaaS)

```
Estágio da Jornada: Consideração
Persona: Lucas, O Gestor Ocupado
Macro-objetivo do Cliente: Avaliar opções de software de gestão de projetos que resolvam suas dores de produtividade e comunicação.

| Ação do Cliente                  | Touchpoint Principal      | Emoções & Pensamentos                                | Dores & Frustrações                                | Oportunidades de Otimização                          | KPI Primário             | Meta             |
|----------------------------------|---------------------------|------------------------------------------------------|----------------------------------------------------|------------------------------------------------------|--------------------------|------------------|
| Clicar em Anúncio de Retargeting | Anúncio no LinkedIn       | Curiosidade, Reconhecimento ("Eles me conhecem!")    | Anúncio genérico não focado em gestão de equipes.  | Personalizar copy do anúncio para "Gestores de Equipe". | CTR do anúncio           | 1.5%             |
| Acessar Landing Page de Produto  | Landing Page de Vendas    | Esperança, Avaliação ("Será que é o que eu preciso?") | Carregamento lento (>3s), proposta de valor confusa. | Otimizar velocidade da LP, reforçar valor para equipes. | Taxa de Conversão da LP  | 8%               |
| Assistir Vídeo Institucional     | Vídeo na Landing Page     | Interesse, Visualização ("Parece fácil de usar.")    | Vídeo muito longo, não mostra casos de uso reais.  | Vídeo de 90s, focado em 3 casos de uso específicos.  | Taxa de Conclusão do Vídeo | 60%              |
| Ler Depoimentos de Clientes      | Seção de Depoimentos na LP| Confiança, Identificação ("Outros gestores usam!")   | Depoimentos muito curtos, sem contexto de resultado. | Adicionar depoimentos com problema->solução->resultado. | Tempo na página          | +15%             |
| Solicitar Demonstração Gratuita  | Formulário na LP          | Decisão, Expectativa ("Quero ver na prática.")        | Formulário complexo, pedindo informações excessivas. | Simplificar formulário (nome, e-mail, empresa, cargo). | Taxa de Preenchimento Formulário | 25%              |
```

---

## Checklist

- [x] O mapa de jornada foi construído com base em uma ou mais personas detalhadas e validadas?
- [x] Todos os estágios cruciais do funil de vendas (consciência, consideração, decisão, pós-compra) foram mapeados?
- [x] Cada touchpoint digital relevante (anúncios, LPs, e-mails, redes sociais, chat, etc.) foi identificado para cada estágio?
- [x] As ações, pensamentos e emoções do cliente foram registrados de forma específica em cada touchpoint?
- [x] Pelo menos 3 pontos de fricção ou dor foram identificados e detalhados em cada estágio crítico?
- [x] Foram propostas oportunidades de otimização claras e acionáveis para cada ponto de fricção encontrado?
- [x] Métricas específicas e metas de melhoria foram associadas a cada oportunidade de otimização?
- [x] As ações internas necessárias para implementar as otimizações foram definidas e atribuídas?
- [x] O mapa considera a jornada pós-compra, incluindo onboarding e retenção, se relevante para o produto/serviço?
- [x] Há um plano de coleta de feedback contínuo (pesquisas, entrevistas) para validar e atualizar o CJM?

---

## Métricas de Referência

| Métrica                         | Benchmark (Varejo Digital) | Meta (Otimizado) |
|---------------------------------|----------------------------|------------------|
| Taxa de Conversão de Landing Page | 2.35%                      | 5.0%             |
| CTR de Anúncios (Google Search) | 3.17%                      | 5.0%             |
| Taxa de Abertura de E-mail (Boas-vindas) | 50-80%                     | 70%              |
| Taxa de Rejeição de Landing Page | 40-60%                     | 35%              |
| Taxa de Abandono de Carrinho   | 70%                        | 55%              |
| Tempo Médio de Resolução de Suporte (Pós-venda) | 24 horas                   | 4 horas          |

---

## Erros Comuns

1.  **CJM Abstrato e Genérico**:
    *   **Erro**: Criar um mapa de jornada com estágios vagos como "Awareness" e "Purchase" sem detalhar as ações e touchpoints *específicos* da persona. Isso leva a insights pouco acionáveis.
    *   **Como evitar**: Sempre comece com uma persona bem definida e, para cada estágio, liste no mínimo 3-5 ações concretas que essa persona realizaria, e os respectivos canais (ex: "Pesquisar 'melhor software CRM' no Google" em vez de apenas "Pesquisa").
2.  **Foco Exclusivo no Funil de Vendas (Pré-compra)**:
    *   **Erro**: Ignorar completamente a jornada do cliente *após a compra*, perdendo oportunidades cruciais de retenção, upsell e advocacy.
    *   **Como evitar**: Estenda o CJM para incluir fases como "Onboarding", "Uso Ativo", "Suporte" e "Renovação/Recompra". Mapeie os touchpoints como e-mails de boas-vindas, tutoriais do produto, chat de suporte e pesquisas de satisfação pós-compra (NPS).
3.  **Mapa Baseado em Suposições Internas**:
    *   **Erro**: Desenvolver o CJM inteiramente a partir de brainstorms internos, sem validar as dores, emoções e comportamentos com dados reais ou feedback direto do cliente.
    *   **Como evitar**: Priorize a coleta de dados quantitativos (Analytics, Heatmaps, CRM) e qualitativos (entrevistas com clientes, pesquisas de satisfação, gravações de sessões de usuário) para embasar cada parte do mapa. Se uma dor é uma suposição, marque-a para validação.

---

## Dicas Avançadas

1.  **Mapeamento Bidirecional (Cliente-Empresa)**: Para cada ação do cliente, adicione uma coluna "Ação Interna da Empresa". Isso garante que haja uma resposta ou suporte adequado para cada etapa da jornada. Exemplo: Se o cliente "Acessa a página de preços", a "Ação Interna" pode ser "Disparar pop-up de oferta de consultoria gratuita após 30 segundos" ou "Notificar SDR para follow-up".
2.  **CJM de Objeções**: Crie um CJM específico para as objeções mais comuns em cada estágio do funil. Por exemplo, na fase de "Decisão", se a objeção é "Preço alto", mapeie os touchpoints (página de preços, chat), as emoções (dúvida, ceticismo) e as oportunidades (comparativo de valor, planos flexíveis, depoimentos de ROI).
3.  **Integração com Ferramentas de Automação**: Após mapear as oportunidades, traduza-as diretamente em ações nas ferramentas de automação de marketing e vendas. Por exemplo, se um cliente "abandona o carrinho", a oportunidade "enviar e-mail de recuperação de carrinho" deve ser configurada com 3 e-mails automatizados, com delays e copies específicos.
4.  **CJM Preditivo com IA**: Utilize dados históricos de jornada (clickstream, interações em CRM) para treinar modelos de IA que prevejam o próximo passo do cliente ou a probabilidade de conversão/churn. Isso permite intervenções proativas e personalizadas em pontos críticos da jornada, como oferecer um desconto especial para clientes com alta probabilidade de abandono.
5.  **CJM para Segmentos Específicos de Micro-Personas**: Em vez de apenas uma persona macro, crie CJMs para micro-segmentos (ex: "Lucas, o Gestor Ocupado que prefere vídeo" vs. "Lucas, o Gestor Ocupado que prefere texto detalhado"). Isso permite uma personalização ainda maior de mensagens, formatos e canais em touchpoints críticos, aumentando as taxas de conversão específicas para cada micro-persona.