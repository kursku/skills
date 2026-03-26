---
name: sales-call-script
description: "Sales Call Script — Skill especializada para sales call script"
license: MIT
metadata:
  version: 1.0.0
  author: Cafe Code AI
  category: 03-funis-vendas
  updated: 2026-03-01
risk: none
---

# Sales Call Script

Essa skill capacita o Claude a gerar, otimizar e executar roteiros de chamadas de vendas eficazes, focando em prospecção, qualificação e fechamento para diversos cenários B2B e B2C.

---

## Keywords

Prospecção outbound, cold calling, discovery call, qualificação BANT, SPIN Selling, tratamento de objeções, fechamento de vendas, rapport, pitch de valor, follow-up, gatilhos mentais, cadência de vendas, CRM.

---

## Quick Start

1.  **Analise o ICP e a dor principal**: Detalhe o perfil do cliente ideal (ICP) e a dor mais latente que seu produto/serviço resolve, por exemplo, "SaaS B2B para SMBs com dificuldade em gestão de leads".
2.  **Estruture a abertura da chamada**: Crie uma frase de abertura que capture a atenção e justifique a ligação em 15 segundos, focando no benefício para o prospect, como "Descobrimos que a maioria dos gestores de vendas perde 30% do tempo em tarefas manuais, e temos uma solução para isso."
3.  **Desenvolva 3 perguntas de qualificação**: Elabore perguntas abertas que revelem orçamento, autoridade, necessidade e tempo (BANT), por exemplo, "Qual o maior desafio que sua equipe enfrenta hoje para converter leads em clientes?"
4.  **Prepare 2 respostas para objeções comuns**: Mapeie as objeções mais frequentes ("Não tenho tempo", "Está caro") e crie respostas concisas que reforcem o valor, por exemplo, para "Está caro": "Entendo, Sr. Silva. Nossos clientes relatam um ROI médio de 25% em 6 meses, o que rapidamente supera o investimento inicial. Podemos explorar como isso se aplica ao seu cenário específico?"
5.  **Defina o próximo passo claro**: Determine a ação seguinte desejada (agendamento de demo, envio de proposta, etc.) e como solicitá-la de forma natural, como "Com base no que conversamos, o próximo passo ideal seria agendarmos uma demonstração personalizada de 20 minutos. Você tem disponibilidade na quarta-feira às 14h ou quinta às 10h?"

---

## Core Workflows

### Workflow 1: Estruturação e Execução de Discovery Call B2B para SaaS de CRM

Este workflow detalha a criação e aplicação de um script para uma chamada de descoberta inicial com um potencial cliente B2B interessado em um software de CRM, visando qualificar a oportunidade e agendar uma demonstração.

**Passos Detalhados:**

1.  **Pré-chamada (Pesquisa Intensiva - 5 min)**
    *   **Ação**: Acessar LinkedIn do prospect, site da empresa, notícias recentes.
    *   **Exemplo**: O prospect, Ana Paula, é Gerente de Vendas na "Tech Solutions Ltda.". O site menciona expansão para novos mercados. No LinkedIn, ela compartilhou um artigo sobre "desafios na gestão de funil de vendas".
    *   **Resultado Esperado**: Identificar 1-2 pontos de conexão ou "gatilhos" para iniciar a conversa.

2.  **Abertura e Construção de Rapport (60-90 segundos)**
    *   **Ação**: Apresentação breve, contexto da chamada, busca de permissão e agendamento da pauta.
    *   **Exemplo de Script**:
        ```
        "Olá, Ana Paula! Aqui é o [Seu Nome] da [Sua Empresa]. Agradeço por atender. Vi no seu LinkedIn que você compartilhou um artigo super relevante sobre gestão de funil, e na Tech Solutions, a expansão para novos mercados parece ser uma prioridade. O motivo da minha ligação é que ajudamos empresas como a sua a otimizar a gestão de leads e acelerar o ciclo de vendas. Temos uns 15-20 minutos para entender se faz sentido para vocês? Minha ideia é ouvir um pouco sobre os desafios atuais e, se houver alinhamento, sugerir como podemos ajudar."
        ```
    *   **Foco**: Demonstrar que a pesquisa foi feita, respeito ao tempo do prospect.

3.  **Qualificação e Descoberta (SPIN Selling - 8-10 min)**
    *   **Ação**: Fazer perguntas abertas para entender a Situação, Problemas, Implicações e Necessidades de Solução do prospect.
    *   **Exemplo de Perguntas (Adaptado ao cenário da Ana Paula)**:
        *   **Situação**: "Ana, como vocês gerenciam hoje o pipeline de vendas na Tech Solutions, especialmente com a expansão para novos mercados?"
        *   **Problema**: "Quais os maiores desafios ou 'dores de cabeça' que sua equipe de vendas encontra nesse processo atual de gestão de leads ou acompanhamento de oportunidades?" (Ex: Perda de informações, dificuldade de priorização).
        *   **Implicação**: "E como esses desafios impactam os resultados da Tech Solutions? Por exemplo, o que acontece quando um lead valioso não é acompanhado adequadamente ou se o tempo de resposta é lento? Isso afeta a taxa de conversão ou o custo de aquisição?"
        *   **Necessidade de Solução**: "Se pudesse resolver um desses problemas imediatamente, qual seria? E o que uma solução ideal faria para sua equipe, no que diz respeito à gestão de vendas?"
    *   **Foco**: Ouvir ativamente, validar as dores, não apresentar o produto ainda.

4.  **Validação de Valor e Transição (2-3 min)**
    *   **Ação**: Resumir as dores identificadas e conectar brevemente com a capacidade da sua solução.
    *   **Exemplo de Script**:
        ```
        "Entendi, Ana. Pelo que você descreveu, a dificuldade em centralizar as informações dos leads, a demora no follow-up e a falta de visibilidade do funil são pontos críticos que impactam diretamente a produtividade da equipe e a conversão de vendas, especialmente com a necessidade de escala da Tech Solutions. Nosso CRM é desenhado justamente para resolver esses pontos, automatizando tarefas, centralizando dados e oferecendo dashboards em tempo real para o gestor. Isso ressoa com o que você busca?"
        ```
    *   **Foco**: Confirmar o entendimento e criar ponte para a demonstração.

5.  **Proposição do Próximo Passo (1-2 min)**
    *   **Ação**: Propor o agendamento de uma demonstração mais aprofundada, com data e hora.
    *   **Exemplo de Script**:
        ```
        "Com base em nossa conversa, acredito que uma demonstração personalizada, focada em como nosso CRM pode resolver especificamente esses desafios na Tech Solutions, seria o próximo passo mais produtivo. Teríamos cerca de 30-40 minutos para mostrar a ferramenta na prática. Você tem disponibilidade para um bate-papo na próxima terça-feira, às 10h, ou na quinta, às 15h?"
        ```
    *   **Foco**: Obter um compromisso claro e específico.

### Workflow 2: Tratamento de Objeções e Fechamento de Venda Consultiva

Este workflow foca em como um vendedor deve lidar com objeções comuns de preço e tempo durante uma chamada de fechamento para um serviço de consultoria em marketing digital, buscando obter o compromisso final.

**Passos Detalhados:**

1.  **Reafirmação do Valor Percebido (2 min)**
    *   **Ação**: Relembrar os benefícios e resultados discutidos em etapas anteriores, conectando-os às dores do cliente.
    *   **Exemplo de Script**:
        ```
        "Sr. Carlos, revisando nossa conversa, ficou claro que a [Nome da Empresa do Cliente] enfrenta dificuldades em gerar leads qualificados para seu novo produto, certo? E nossa proposta de consultoria, com a estratégia de inbound marketing e automação, visa justamente aumentar em 40% a geração desses leads em 6 meses, liberando sua equipe interna para focar no core business. Isso ainda faz sentido para vocês?"
        ```
    *   **Foco**: Reforçar o "porquê" da solução antes de discutir o "quanto".

2.  **Identificação e Validação da Objeção (1-2 min)**
    *   **Ação**: Ouvir a objeção, reformular para garantir entendimento e validar a objeção principal.
    *   **Exemplo de Objeção**: "Entendi o valor, mas o investimento é alto para nosso orçamento atual."
    *   **Exemplo de Script (para objeção de preço)**:
        ```
        "Compreendo perfeitamente, Sr. Carlos, que o investimento é uma consideração importante. Quando o senhor menciona 'alto para o orçamento atual', está se referindo especificamente ao valor total, à forma de pagamento ou ao impacto no fluxo de caixa no curto prazo?"
        ```
    *   **Foco**: Não contra-argumentar de imediato, mas aprofundar a raiz da objeção.

3.  **Estratégia para Objeção de Preço (5 min)**
    *   **Ação**: Desmembrar o valor, focar no ROI, comparar com o custo da inação ou apresentar opções.
    *   **Exemplo de Script**:
        ```
        "Sr. Carlos, vamos analisar o custo-benefício. Se nossa consultoria de R$15.000/mês resultar em 40% mais leads qualificados, e cada novo cliente para seu produto gera R$5.000 de receita, quantos clientes adicionais seriam necessários para cobrir o investimento e gerar lucro significativo? Além disso, qual o custo de NÃO ter esses leads? Quanto tempo e recursos sua equipe gasta hoje em prospecção ineficaz? Podemos também, se a questão for fluxo de caixa, discutir um plano de pagamento em fases, ou talvez iniciar com um escopo modular para um projeto piloto que valide o ROI rapidamente."
        ```
    *   **Foco**: Mudar a percepção de custo para investimento, monetizar a solução.

4.  **Estratégia para Objeção de Tempo ("Não tenho tempo agora") (3 min)**
    *   **Ação**: Validar a preocupação, mostrar como a solução economiza tempo futuro e criar senso de urgência.
    *   **Exemplo de Script**:
        ```
        "Sr. Carlos, entendo que a sua agenda é apertada, e tempo é um recurso valioso. É justamente por isso que a nossa consultoria foi desenhada: para otimizar o tempo da sua equipe, automatizando processos de marketing e liberando-os para atividades mais estratégicas. Quanto mais postergarmos, mais tempo sua equipe continuará gastando em tarefas manuais e menos leads qualificados serão gerados. Temos uma janela de oportunidade com o lançamento do seu novo produto. Que tal começarmos com um kick-off de apenas 1 hora na próxima semana para já colocarmos o plano em ação e começarmos a ver resultados em 30 dias?"
        ```
    *   **Foco**: Inverter a objeção, mostrando que a solução é a cura para a falta de tempo.

5.  **Fechamento (Direto ou Alternativo - 1-2 min)**
    *   **Ação**: Solicitar o compromisso ou apresentar opções de fechamento.
    *   **Exemplo de Script (após tratar objeções)**:
        ```
        "Sr. Carlos, com base no que conversamos, e considerando que o aumento de leads qualificados é uma prioridade, qual a melhor forma de prosseguirmos? Queremos iniciar o projeto ainda neste mês para aproveitar o momentum do lançamento do seu produto, ou prefere que a gente agende uma reunião para alinhar os termos contratuais na próxima quinta-feira?"
        ```
    *   **Foco**: Conduzir o cliente para a decisão final.

---

## Templates

### Template: Roteiro de Abertura de Cold Call (Venda de Ferramenta de Análise de Dados)

```
Olá, [Nome do Prospect]! Aqui é o [Seu Nome] da [Nome da Sua Empresa].
Tudo bem?
(Pausa para resposta)

O motivo da minha ligação é que percebemos que empresas como a [Nome da Empresa do Prospect], especialmente no setor de [Setor da Empresa do Prospect], frequentemente enfrentam desafios em [Problema Específico 1, ex: otimizar campanhas de marketing sem dados claros] e [Problema Específico 2, ex: identificar oportunidades de crescimento no mercado].

A [Nome da Sua Empresa] ajuda gestores a transformar dados brutos em insights acionáveis para [Benefício 1, ex: reduzir custos de aquisição de clientes] e [Benefício 2, ex: aumentar a taxa de retenção].

Temos cerca de 60 segundos para eu explicar brevemente como fazemos isso e entender se há alguma sinergia com os seus desafios atuais?
(Pausa para resposta)

Se sim: "Excelente! Para começar, como vocês tomam decisões estratégicas baseadas em dados hoje?"
Se não: "Sem problemas, agradeço a sua sinceridade. Tenha um ótimo dia!"
```

### Template: Tratamento de Objeção de Concorrência ("Já usamos o [Concorrente]")

```
Cliente: "Já usamos o [Nome do Concorrente] e estamos satisfeitos."

Vendedor: "Entendo perfeitamente, [Nome do Prospect]. O [Nome do Concorrente] é uma ferramenta conhecida no mercado. Muitos de nossos clientes atuais, inclusive, já utilizaram ou ainda utilizam o [Nome do Concorrente] antes de nos conhecer.

Pelo que conversamos, a sua maior prioridade é [Relembrar prioridade do cliente, ex: ter relatórios mais personalizáveis e suporte mais ágil]. O que nossos clientes nos dizem é que, embora o [Nome do Concorrente] seja bom para [Ponto forte do concorrente, ex: funções básicas], a [Nome da Sua Empresa] se destaca por [Diferencial 1 da sua empresa, ex: nossa IA preditiva que otimiza o forecast] e [Diferencial 2 da sua empresa, ex: nosso suporte técnico dedicado 24/7 que resolve 90% dos problemas em menos de 1 hora].

Você estaria aberto a uma breve demonstração de 15 minutos para ver como esses diferenciais podem se traduzir em [Benefício específico para o cliente, ex: uma redução de 15% nos erros de previsão e um aumento na satisfação da sua equipe]?"
```

---

## Checklist

- [X] Pesquisou o perfil do LinkedIn do prospect para identificar 2 pontos de conexão?
- [X] Definiu a dor principal do ICP que será abordada na abertura da chamada?
- [X] Criou uma abertura de chamada que justifica a ligação em no máximo 20 segundos?
- [X] Listou pelo menos 3 perguntas abertas para qualificação (SPIN/BANT)?
- [X] Mapeou 2-3 objeções mais prováveis do prospect e suas respectivas respostas?
- [X] Preparou um pitch de valor focado em benefícios específicos e mensuráveis?
- [X] Tem um próximo passo claro e específico para sugerir ao final da chamada (ex: demo, envio de proposta)?
- [X] Praticou a transição da etapa de descoberta para a proposição do próximo passo?
- [X] Tem em mente uma alternativa de fechamento caso o primeiro CTA seja recusado?
- [X] Analisou o melhor horário para ligar para o prospect com base no fuso horário e segmento?

---

## Métricas de Referência

| Métrica                         | Benchmark (Indústria) | Meta (Exemplo) |
|---------------------------------|-----------------------|----------------|
| Taxa de Conexão (Cold Call)     | 10% - 15%             | 18%            |
| Taxa de Qualificação (Discovery para Próxima Etapa) | 20% - 30%             | 35%            |
| Taxa de Conversão (Discovery para Fechamento) | 15% - 25%             | 28%            |
| Duração Média da Chamada (Discovery) | 15 - 20 minutos       | 18 minutos     |
| Taxa de Agendamento (Cold Call) | 3% - 5%               | 7%             |

---

## Erros Comuns

1.  **Falar demais e ouvir de menos**: Muitos vendedores dominam a conversa com o pitch do produto, em vez de fazer perguntas e ouvir as necessidades do cliente.
    *   **Como evitar**: Use a regra 80/20 (80% o cliente fala, 20% você) na fase de descoberta. Pratique o silêncio estratégico após uma pergunta. Exemplo: Após perguntar "Qual o maior desafio que sua equipe enfrenta hoje?", espere a resposta completa sem interrupções.
2.  **Não ter um próximo passo claro**: Terminar a chamada sem um compromisso definido, como "Te ligo semana que vem" ou "Vou te mandar um e-mail", que são vagos e facilmente ignorados.
    *   **Como evitar**: Sempre proponha um próximo passo específico, com data e hora. Exemplo: Em vez de "Te ligo semana que vem", diga "Podemos agendar uma demonstração de 30 minutos para quarta-feira às 15h ou quinta-feira às 10h?".
3.  **Não personalizar a abordagem**: Usar um script genérico para todos os prospects, sem considerar o contexto da empresa, o cargo do indivíduo ou os desafios específicos do setor.
    *   **Como evitar**: Faça pesquisa prévia (LinkedIn, site da empresa) e utilize as informações para personalizar a abertura e as perguntas de qualificação. Exemplo: Mencione uma notícia recente sobre a empresa do prospect na abertura da chamada para demonstrar que você fez sua "lição de casa".

---

## Dicas Avançadas

1.  **Técnica de Espelhamento e Enquadramento**: Espelhe a linguagem corporal (se em vídeo), tom de voz e palavras-chave do prospect para construir rapport inconscientemente. Enquadre a conversa na perspectiva do cliente, não na sua.
    *   **Exemplo Prático**: Se o prospect diz "Precisamos de agilidade no processo", responda "Agilidade é fundamental. Quando você pensa em agilidade, o que significa para sua operação?".
2.  **Utilizar Silêncio Estratégico**: Após fazer uma pergunta crucial ou apresentar uma objeção, faça uma pausa. O silêncio pressiona o prospect a preencher o vazio, revelando mais informações ou suas verdadeiras preocupações.
    *   **Exemplo Prático**: Depois de perguntar "Qual a sua principal objeção ao prosseguir?", permaneça em silêncio. A resposta subsequente será mais profunda.
3.  **Calibração de Voz e Ritmo**: Varie o tom, volume e ritmo da sua voz para manter o engajamento. Uma voz monótona é um convite ao desinteresse. Use um tom mais baixo e lento para pontos importantes e um tom mais alto e rápido para criar entusiasmo.
    *   **Exemplo Prático**: Para enfatizar um benefício chave, diminua o ritmo e o volume. Ao convidar para o próximo passo, pode-se usar um tom mais entusiástico.
4.  **Pré-chamada com Pesquisa Aprofundada via IA**: Utilize ferramentas de IA para analisar o site do prospect, notícias, relatórios financeiros e posts em redes sociais em segundos, gerando um resumo com pontos de dor e oportunidades de forma automatizada antes mesmo de discar.
    *   **Exemplo Prático**: Ferramenta de IA resume que "Empresa X busca reduzir custos operacionais em 15% no próximo trimestre e lançará novo produto em 2 meses, o que pode gerar pico de demanda no atendimento". Use essas informações para adaptar seu script antes da chamada.
5.  **Criação de Urgência e Escassez Genuínas**: Apresente razões legítimas para o prospect agir agora, como promoções por tempo limitado, vagas restritas, ou a perda de uma vantagem competitiva se demorar.
    *   **Exemplo Prático**: "Temos apenas 3 vagas restantes para o programa de implementação premium neste trimestre, que inclui suporte dedicado de um consultor sênior. Após isso, o próximo slot será em 3 meses. Isso é relevante para sua meta de lançamento do novo produto?"