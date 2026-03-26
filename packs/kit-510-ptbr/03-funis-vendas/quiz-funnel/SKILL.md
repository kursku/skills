---
name: quiz-funnel
description: "Quiz Funnel — Skill especializada para quiz funnel"
license: MIT
metadata:
  version: 1.0.0
  author: Cafe Code AI
  category: 03-funis-vendas
  updated: 2026-03-01
risk: safe
---

# Quiz Funnel

Esta skill capacita o Claude a projetar, otimizar e escalar funis de vendas baseados em quizzes interativos para qualificação e segmentação de leads.

---

## Keywords

Quiz interativo, Funil de qualificação, Geração de leads, Segmentação inteligente, Personalização de ofertas, CTA condicional, Automação de marketing, Engajamento de audiência, Lógica de ramificação, Landing page de quiz, Pós-quiz nurturing, Otimização de conversão, Gamificação de marketing, Retargeting de quiz.

---

## Quick Start

1.  **Escolher a ferramenta de quiz**: Selecionar uma plataforma como Typeform, Interact ou OpinionStage, considerando a lógica de ramificação e integração necessárias.
2.  **Definir o resultado final do quiz**: Estabelecer os 3-5 perfis de resultado que o quiz irá gerar (ex: "Seu Perfil de Investidor: Conservador, Moderado, Agressivo").
3.  **Elaborar as 5-7 perguntas chave**: Desenvolver as perguntas com opções de resposta que direcionem claramente para um dos perfis definidos, aplicando lógica de ramificação.
4.  **Criar a página de captura de e-mail**: Projetar uma etapa para solicitar nome e e-mail, seja antes ou depois da exibição dos resultados, prometendo valor adicional.
5.  **Configurar a sequência de e-mails de nutrição**: Desenvolver sequências de e-mails personalizadas para cada perfil de resultado, com ofertas alinhadas.

---

## Core Workflows

### Workflow 1: Design e Lançamento de Quiz Funnel para Coaching Financeiro

Este workflow detalha a criação de um funil de quiz para qualificar leads interessados em programas de coaching financeiro.

*   **Passo 1: Definição do Objetivo e Persona do Quiz**: O objetivo é aumentar a base de leads qualificados para o programa "Liberdade Financeira em 90 Dias". A persona-alvo são "Pessoas com renda fixa, entre 30-50 anos, que poupam, mas não investem ativamente, buscam segurança e crescimento moderado".
*   **Passo 2: Estrutura do Quiz "Qual é o Seu Estilo de Investidor?"**:
    *   **Pergunta 1 (Entendimento Básico)**: "Você já investe em algo além da poupança?" (Opções: Sim, Não, Não sei).
    *   **Pergunta 2 (Tolerância a Risco)**: "Como você reagiria se seu investimento perdesse 15% do valor em um mês?" (Opções: Entraria em pânico, Aguardaria a recuperação, Investiria mais).
    *   **Pergunta 3 (Horizonte de Tempo)**: "Para quando você planeja utilizar o dinheiro que está investindo?" (Opções: Curto prazo (<1 ano), Médio prazo (1-5 anos), Longo prazo (>5 anos)).
    *   **Pergunta 4 (Conhecimento Financeiro)**: "Você se sente confortável com termos como 'renda variável', 'inflação', 'diversificação'?" (Opções: Sim, Mais ou menos, Não).
    *   **Pergunta 5 (Objetivo Financeiro Principal)**: "Qual seu principal objetivo com investimentos?" (Opções: Aposentadoria tranquila, Comprar um imóvel, Gerar renda extra, Realizar um sonho de consumo).
*   **Passo 3: Lógica de Ramificação e Definição de Resultados**:
    *   **Resultado 1: "Investidor Conservador"**: Gerado por respostas como "Não" na P1, "Pânico" na P2, "Curto prazo" na P3. Oferta: E-book "Primeiros Passos para Investir com Segurança" + convite para webinar "Renda Fixa Descomplicada".
    *   **Resultado 2: "Investidor Moderado"**: Gerado por um mix de respostas, com "Aguardaria" na P2, "Médio prazo" na P3. Oferta: Guia "Construindo Sua Carteira Equilibrada" + convite para consultoria estratégica gratuita de 15 minutos.
    *   **Resultado 3: "Investidor Agressivo"**: Gerado por respostas como "Sim" na P1, "Investiria mais" na P2, "Longo prazo" na P3. Oferta: Curso "Acelerando Seus Ganhos com Ações" + convite para grupo VIP de discussões sobre mercado financeiro.
*   **Passo 4: Criação da Página de Resultados e Captura**: Antes de exibir o resultado, solicitar nome e e-mail. Exemplo de chamada para ação: "Descubra Seu Perfil de Investidor AGORA e receba um guia exclusivo para começar a investir com inteligência!". A página de resultados deve apresentar o perfil e um CTA claro para a oferta personalizada.
*   **Passo 5: Automação Pós-Quiz**: Integrar o quiz (via webhook ou integração nativa, ex: Typeform com ActiveCampaign). Disparar a sequência de e-mails personalizada para cada segmento (Conservador, Moderado, Agressivo) com base no resultado, entregando o material prometido e nutrindo o lead com conteúdo relevante.

### Workflow 2: Otimização e Escala de um Quiz Funnel Existente para E-commerce de Suplementos

Este workflow foca em aprimorar um quiz funil já em operação para um e-commerce, visando aumentar a taxa de conversão para venda e otimizar o Custo por Lead (CPL).

*   **Contexto Atual**: Um quiz "Qual o Melhor Suplemento para Seus Objetivos?" está ativo, mas a taxa de conversão (quiz para compra) é de 1.8%, e o CPL é de R$ 8,50. A taxa de conclusão do quiz (TCQ) é de 65%.
*   **Passo 1: Análise de Desempenho e Identificação de Gargalos**:
    *   **Métricas Coletadas**: TCQ: 65%. Taxa de Conversão para Lead (TCQ->L): 80% dos que completam deixam e-mail. Taxa de Conversão para Venda (TCQ->V): 1.8%. CPL: R$ 8,50.
    *   **Identificação de Problema**: Análise de funil mostra uma queda significativa de engajamento na pergunta 4 ("Você treina quantas vezes por semana?"), com muitos abandonos nessa etapa.
*   **Passo 2: Otimização da Experiência do Quiz**:
    *   **Ação 1**: Simplificar a pergunta 4 para "Qual sua frequência de treino?" com opções mais visuais e diretas (ex: Ícone de pessoa levantando peso + "1-2x/sem", "3-4x/sem", "5+x/sem").
    *   **Ação 2**: Adicionar barra de progresso visível e um incentivo na metade do quiz ("Quase lá! Descubra seu suplemento ideal para turbinar seus resultados!").
    *   **Ação 3**: Testar a posição da captura de e-mail. Atualmente, a captura é *antes* dos resultados. Criar um Teste A/B para comparar com a captura *depois* da exibição do resultado, com a promessa de "receba seu plano personalizado e 10% de desconto por e-mail".
*   **Passo 3: Aprimoramento da Oferta Pós-Quiz**:
    *   **Segmento "Ganho de Massa"**: Antes: "Compre Whey Protein". Novo: "Receba seu Kit Massa Muscular (Whey + Creatina) com 15% de desconto e frete grátis." (Adicionar urgência: "Oferta válida por 48h!").
    *   **Segmento "Perda de Peso"**: Antes: "Compre Termogênico". Novo: "Seu Plano Detox de 7 Dias + 20% OFF no Combo Queima Gordura (Termogênico + L-Carnitina)."
    *   **Ação**: Criar landing pages de oferta dedicadas para cada segmento, com depoimentos de clientes que se identificam com o perfil e prova social.
*   **Passo 4: Teste A/B Contínuo e Iteração**:
    *   **Teste**: Variar o CTA da página de resultados e os headlines dos e-mails de nutrição. Exemplo: Testar "Receba seu desconto agora!" vs. "Desbloqueie seu plano personalizado e desconto exclusivo!".
    *   **Monitoramento**: Acompanhar de perto as métricas otimizadas: TCQ, TCQ->L, TCQ->V, CPL e Retorno sobre Investimento (ROI).
*   **Passo 5: Retargeting Avançado e Qualificação de Vendas**:
    *   **Retargeting**: Criar audiências personalizadas no Google Ads/Facebook Ads para quem completou o quiz, mas não comprou. Exibir anúncios específicos que reforçam o resultado do quiz e a oferta personalizada. Exemplo: "Você descobriu que é um 'Ganho de Massa'? Não perca seu Kit Massa Muscular com 15% OFF!"
    *   **Qualificação**: Integrar os resultados detalhados do quiz com o CRM. Para leads com alta pontuação de qualificação (ex: "Ganho de Massa" com histórico de compra de suplementos), enviar um alerta para o time de vendas fazer um contato proativo com informações pré-qualificadas.

---

## Templates

### Script de Pergunta de Quiz (Exemplo: Ferramenta de Análise de Site)

```
Título da Pergunta: Qual o seu maior desafio atual com o desempenho do seu site?

Opções de Resposta:
[ ] Gerar mais tráfego orgânico (SEO)
[ ] Converter visitantes em leads/clientes (CRO)
[ ] Reduzir a taxa de rejeição e melhorar a experiência do usuário (UX)
[ ] Entender de onde vêm meus visitantes e como se comportam (Analytics)

Lógica de Ramificação:
- Se "Gerar mais tráfego orgânico (SEO)", direcionar para perguntas sobre palavras-chave, conteúdo e backlinks.
- Se "Converter visitantes em leads/clientes (CRO)", direcionar para perguntas sobre CTAs, formulários e landing pages.
- Se "Reduzir a taxa de rejeição e melhorar a experiência do usuário (UX)", direcionar para perguntas sobre velocidade do site, design responsivo e navegação.
- Se "Entender de onde vêm meus visitantes e como se comportam (Analytics)", direcionar para perguntas sobre Google Analytics, relatórios e métricas de funil.
```

### E-mail de Nutrição Pós-Quiz (Segmento "Empreendedor Iniciante - Dificuldade com Vendas")

```
Assunto: [Resultado do seu Quiz] Seu Guia Essencial para Vendas Simples e Lucrativas!

Olá [Nome do Lead],

Parabéns por completar o nosso quiz "Qual o seu Estágio no Empreendedorismo Digital?"!

Descobrimos que você se encaixa no perfil "Empreendedor Iniciante com Dificuldade em Vendas". Isso é super comum, e estamos aqui para ajudar a transformar essa realidade!

Muitos empreendedores nessa fase lutam para transformar seus produtos ou serviços em vendas consistentes. A boa notícia é que existe um caminho claro e direto para superar isso.

Para começar com o pé direito, preparamos um conteúdo exclusivo e gratuito, feito sob medida para você:

➡️ [LINK para o E-book] **E-book Gratuito: As 3 Estratégias de Vendas que Todo Iniciante Precisa Dominar**

Neste e-book prático, você vai aprender:
*   Como criar uma oferta irresistível, mesmo sem experiência prévia.
*   As táticas mais eficazes para atrair os primeiros clientes qualificados.
*   Como construir confiança e credibilidade online para fechar mais vendas.

Além disso, para dar um passo adiante e ter um plano personalizado, que tal agendar uma sessão estratégica gratuita de 15 minutos com um de nossos especialistas? Vamos mapear seus desafios específicos e indicar os próximos passos concretos para você.

🚀 [LINK para agendamento] **Agende sua Sessão Estratégica Gratuita Agora!**

Fique de olho em nossos próximos e-mails, teremos mais dicas valiosas e recursos para impulsionar suas vendas!

Um abraço e sucesso,
Equipe [Nome da Sua Empresa]
```

---

## Checklist

- [x] Objetivo principal do quiz definido (ex: qualificar leads para um programa de coaching).
- [x] Ferramenta de quiz escolhida e configurada para lógica de ramificação (ex: Interact, Typeform).
- [x] Título do quiz atraente e alinhado aos interesses da persona (ex: "Descubra Seu Perfil de Investidor").
- [x] Mínimo de 5 perguntas com opções de resposta claras e lógica de ramificação funcional.
- [x] Todos os caminhos do quiz levam a um resultado único e personalizado.
- [x] Página de captura de e-mail estrategicamente posicionada (antes ou depois do resultado, com teste A/B).
- [x] Página de resultados com um CTA claro e uma oferta específica para o perfil revelado.
- [x] Integração do quiz com a ferramenta de automação de marketing (CRM/e-mail, ex: ActiveCampaign).
- [x] Sequência de e-mails de nutrição personalizada para cada resultado do quiz.
- [x] Pixel de rastreamento (Facebook Pixel, Google Ads Tag) configurado nas páginas do quiz e resultados.
- [x] Design do quiz responsivo e otimizado para dispositivos móveis.
- [x] Teste completo do fluxo do quiz, desde a primeira pergunta até a entrega do e-mail pós-quiz.

---

## Métricas de Referência

| Métrica                         | Benchmark     | Meta          |
|---------------------------------|---------------|---------------|
| Taxa de Conclusão do Quiz (TCQ) | 70-85%        | > 80%         |
| Taxa de Conversão para Lead (Quiz -> Opt-in) | 40-60%        | > 55%         |
| Custo por Lead (CPL) via Quiz   | R$ 3 - R$ 15  | < R$ 5        |
| Taxa de Conversão para Venda (Lead -> Cliente) | 2-5%          | > 3.5%        |
| ROI do Funil de Quiz            | 150-300%      | > 250%        |
| Taxa de Abertura E-mail Pós-Quiz | 30-50%        | > 40%         |

---

## Erros Comuns

1.  **Quiz muito longo ou complexo**: **Como evitar**: Mantenha o quiz entre 5 e 8 perguntas, utilizando principalmente questões de múltipla escolha ou sim/não. Evite perguntas abertas que exigem muito esforço. Exemplo de correção: Em vez de "Descreva sua jornada de exercícios e dieta", use "Quantas vezes por semana você se exercita?" e "Qual seu principal objetivo atual (perder peso, ganhar massa, etc.)?".
2.  **Lógica de ramificação confusa ou inexistente**: **Como evitar**: Desenhe o fluxo completo do quiz em um mapa mental ou fluxograma antes de construí-lo na ferramenta. Garanta que cada resposta direcione para o próximo conjunto de perguntas ou para um resultado específico de forma lógica e consistente. Exemplo: Se a resposta à Pergunta 2 for "Iniciante em investimentos", a Pergunta 3 não deve ser sobre "Otimização avançada de carteiras de renda variável".
3.  **Oferta pós-quiz genérica ou desalinhada**: **Como evitar**: Cada resultado do quiz DEVE ter uma oferta (e-book, consultoria, produto, cupom) que resolva diretamente a dor ou necessidade específica do perfil revelado. Exemplo: Para o perfil "Investidor Conservador", oferecer um curso de ações de alto risco é um erro. A oferta correta seria um guia sobre investimentos em renda fixa ou um webinar sobre segurança financeira.
4.  **Captura de lead mal posicionada**: **Como evitar**: Testar se a captura de e-mail funciona melhor *antes* de revelar o resultado (com a promessa de "descubra seu perfil e receba um bônus!") ou *depois* da exibição do resultado (com a prova de valor: "você é um X! Receba o guia completo e um desconto exclusivo por e-mail!"). Geralmente, a captura *depois* do resultado tende a ter maior taxa de conversão, pois o usuário já recebeu valor.
5.  **Falta de acompanhamento e otimização**: **Como evitar**: Implemente pixels de rastreamento e integre o quiz a ferramentas de análise (Google Analytics, Hotjar). Monitore as métricas de conclusão, conversão e abandono do quiz. Realize testes A/B contínuos em títulos, perguntas, CTAs e ofertas para identificar o que funciona melhor.

---

## Dicas Avançadas

1.  **Personalização Extrema na Jornada do Cliente**: Use não apenas o resultado final do quiz, mas também as respostas individuais para personalizar toda a sequência de nutrição por e-mail, as landing pages de oferta e, se aplicável, o script de vendas. Exemplo: Se o quiz revelou "desafio com tráfego pago" e a resposta a uma pergunta específica foi "dificuldade em segmentar público", o e-mail seguinte pode abordar "5 erros comuns na segmentação de anúncios" e a landing page de oferta do produto deve destacar os benefícios para a segmentação de público.
2.  **Retargeting Baseado em Respostas Parciais**: Para usuários que iniciaram o quiz e abandonaram em uma determinada pergunta, crie audiências de retargeting segmentadas. Exiba anúncios que abordem diretamente a dor ou o tema da pergunta onde houve o abandono, incentivando a conclusão. Exemplo: Se abandonou na pergunta sobre "objetivos financeiros", o anúncio pode ser "Ainda não sabe onde quer chegar com seu dinheiro? Nosso quiz te ajuda a