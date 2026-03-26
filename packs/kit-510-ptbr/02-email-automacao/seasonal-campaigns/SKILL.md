---
name: seasonal-campaigns
description: "Seasonal Campaigns — Skill especializada para criar e otimizar sequências de e-mail e automações para campanhas sazonais de alto impacto."
license: MIT
metadata:
  version: 1.0.0
  author: Cafe Code AI
  category: 02-email-automacao
  updated: 2026-03-01
risk: safe
---

# Seasonal Campaigns

Esta skill capacita o Claude a desenvolver e executar estratégias de e-mail marketing e automação específicas para datas comemorativas e picos sazonais, maximizando o ROI.

---

## Keywords

Black Friday Email Sequence, Natal Automação, Dia das Mães Nurturing, Páscoa Segmentação, Cyber Monday Funil, Valentine's Day Journey, Lançamento Coleção Verão, Back-to-School Automation, Engajamento Sazonal, Gatilhos Temporais, Retenção Pós-Campanha, Pré-lançamento Sazonal.

---

## Quick Start

1.  **Segmentar base de e-mails**: Crie segmentos de clientes com base no histórico de compras sazonais (ex: "Compraram Black Friday 2023", "Compraram Dia das Mães 2024").
2.  **Configurar automação de pré-lançamento**: Para um evento como o Natal, envie 3 e-mails teasers nos 15 dias anteriores, gerando expectativa e revelando ofertas exclusivas para quem interagir.
3.  **Implementar carrinho abandonado sazonal**: Ative uma sequência de 2 e-mails para produtos adicionados ao carrinho na semana do Dia dos Namorados, com um incentivo de frete grátis no segundo e-mail.
4.  **Agendar testes A/B de subject lines**: Para a campanha principal de Páscoa, teste "Ofertas de Páscoa: Ovos de Chocolate com 30% OFF!" vs. "Páscoa Feliz: Ganhe 2 ovos na compra de 1!" para otimizar abertura.

---

## Core Workflows

### Workflow 1: Automação de Black Friday com Segmentação de Engajamento e Gatilhos por Compra Anterior

Este workflow detalha a criação de uma sequência de e-mails automatizada para a Black Friday, utilizando segmentação avançada para maximizar a conversão em diferentes perfis de clientes.

*   **Passo 1: Segmentação Estratégica (30 dias antes da Black Friday)**
    *   **Segmento A: Compradores da Black Friday Ano Anterior (2023)**: Clientes que converteram na BF anterior.
    *   **Segmento B: Engajados Recentes (últimos 90 dias)**: Clientes que abriram 3+ e-mails ou clicaram em 1+ nos últimos 90 dias, mas não compraram na BF 2023.
    *   **Segmento C: Inativos Reativáveis (últimos 180+ dias)**: Clientes que não interagem há mais de 180 dias.
    *   **Regra de Exclusão**: Quem já está em outra automação de compra recente (últimos 7 dias) é pausado desta sequência.

*   **Passo 2: Sequência de Pré-aquecimento Personalizada (15 a 7 dias antes da Black Friday)**
    *   **Dia -15 (Segmento A)**: E-mail com acesso antecipado exclusivo. Subject: "Seu Acesso VIP à Black Friday: Ofertas Exclusivas Começam AGORA!"
    *   **Dia -12 (Segmento B)**: E-mail de geração de expectativa com teasers de categorias de produtos. Subject: "Prepare-se: A Black Friday Está Chegando com Ofertas Que Você Vai Amar!"
    *   **Dia -10 (Segmento C)**: E-mail de reengajamento com foco em valor. Subject: "Sentimos Sua Falta! Descontos Inéditos na Black Friday Para Você Voltar!"

*   **Passo 3: Disparo das Ofertas Principais e Urgência (3 dias antes até 1 dia após Black Friday)**
    *   **Dia -3 (Todos os Segmentos)**: "Black Friday Antecipada: 48h de Ofertas EXCLUSIVAS!" (Personalização de blocos de produtos baseada no histórico de navegação/compra).
    *   **Dia 0 (Black Friday)**:
        *   **9h (Todos)**: "AGORA: Black Friday AO VIVO! Até 70% OFF em Tudo!"
        *   **15h (Não Conversores do 9h)**: "Corra! Metade do Estoque Vendido na Black Friday!" (Gatilho de urgência por esgotamento de estoque).
        *   **20h (Não Conversores do 15h)**: Ativar automação de carrinho abandonado com lembrete "Sua Black Friday te espera! Últimas Horas!"
    *   **Dia +1 (Cyber Monday - Não Conversores da Black Friday)**: "ÚLTIMA CHANCE: Cyber Monday Prolongada! Descontos Finais!" (Foco em extensão de prazo).

*   **Passo 4: Pós-Campanha e Nurturing de Retenção (2 a 14 dias após Black Friday)**
    *   **Para Compradores**: E-mail de agradecimento com sugestão de produtos complementares (cross-sell/upsell) e convite ao programa de fidelidade. Subject: "Obrigado pela sua compra! Conheça nossos produtos para o verão."
    *   **Para Quem Abriu, mas Não Comprou**: E-mail de recuperação com um micro-desconto ou frete grátis para próxima compra. Subject: "Não Deu Tempo? Novidades e um Presente Para Você: 10% OFF na Próxima Compra!"
    *   **Para Quem Não Abriu**: Reenvio com subject line diferente (se aplicável, com limite de frequência) ou exclusão da sequência para evitar fadiga.

### Workflow 2: Campanha de Dia das Mães com Automação de Carrinho Abandonado e Recuperação de Não-Engajados

Este workflow foca em como maximizar vendas para o Dia das Mães, utilizando automações para recuperar carrinhos e reativar leads que mostraram interesse inicial.

*   **Passo 1: Lançamento da Coleção Dia das Mães (20 dias antes da data)**
    *   E-mail inicial para toda a base ativa, apresentando a nova coleção de produtos focados em "presentes perfeitos para sua mãe". Incluir links diretos para categorias como "Presentes para Mães Clássicas", "Presentes para Mães Modernas".
    *   Subject: "Sua Mãe Merece o Melhor: Descubra a Coleção Especial Dia das Mães!"

*   **Passo 2: Automação de Carrinho Abandonado Otimizada (15 dias antes até o Dia das Mães)**
    *   **Gatilho**: Usuário adiciona item da coleção Dia das Mães ao carrinho, mas não finaliza a compra em 2 horas.
    *   **E-mail 1 (2 horas após abandono)**: Lembrete do carrinho. Conteúdo: Imagens dos produtos abandonados, CTA para "Finalizar Compra". Subject: "Seu carrinho te espera! Presenteie sua mãe com amor."
    *   **E-mail 2 (24 horas após abandono)**: Incentivo para a compra. Conteúdo: Oferta de frete grátis ou 5% de desconto específico para a coleção Dia das Mães. Subject: "Ainda pensando no presente perfeito? Frete Grátis para o Dia das Mães!" (Válido por 48h).

*   **Passo 3: Recuperação de Não-Engajados (7 dias antes da data)**
    *   **Segmento**: Usuários que abriram o e-mail inicial da coleção Dia das Mães (Passo 1), mas não clicaram ou não converteram em compra até o momento.
    *   **E-mail**: Foco em urgência e soluções de última hora. Conteúdo: "Guia de Presentes de Última Hora para o Dia das Mães + Desconto Especial de 15% em produtos selecionados!" (Destacar entrega expressa).
    *   Subject: "Última Semana! Presentes Incríveis para o Dia das Mães com 15% OFF!"

*   **Passo 4: Pós-Campanha de Retenção e Feedback (1 dia após a data)**
    *   **Para Compradores**: E-mail de agradecimento e solicitação de feedback. Conteúdo: "Seu presente fez sucesso? Compartilhe sua experiência e ganhe 10% na próxima compra!" (Incentivo a reviews e próxima compra).
    *   **Para Não-Compradores**: E-mail de reengajamento focado em autoconsumo ou futuras necessidades. Conteúdo: "Não encontrou o presente ideal? Que tal algo para VOCÊ? Desconto exclusivo de 20% em nossa nova coleção!"
    *   Subject: "O Dia das Mães Passou, mas a Felicidade Continua! Um Presente Para Você."

---

## Templates

### Template: Email de Pré-lançamento Black Friday (Segmento A - Clientes VIP)

```
Assunto: Seu Acesso VIP à Black Friday: Ofertas Exclusivas Começam AGORA!
Pré-header: Para você, que é especial: Descontos de até 60% antes de todo mundo.

Olá, [Nome do Cliente]!

Como um dos nossos clientes mais valiosos, você merece um tratamento exclusivo.
A Black Friday ainda não chegou oficialmente, mas para você, ela já começou!

Temos o prazer de oferecer acesso antecipado às nossas melhores ofertas, com descontos de até 60% em categorias selecionadas e frete grátis em compras acima de R$199. Esta é a sua chance de garantir os produtos mais desejados antes que o estoque se esgote.

👉 ACESSE SUAS OFERTAS VIP AGORA: [Link para Landing Page VIP com URL personalizada com UTMs]

*   Descontos de até 60% em Eletrônicos
*   40% OFF em Moda Feminina e Masculina
*   30% OFF em Produtos para Casa

Esta oferta é válida por apenas 48 horas e exclusiva para você. Não perca a oportunidade de renovar o que ama com preços incríveis!

Boas compras,
Equipe [Nome da Empresa]
```

### Template: Email de Carrinho Abandonado (Dia das Mães) - Com Incentivo

```
Assunto: Seu presente de Dia das Mães te espera! Frete Grátis para Você!
Pré-header: Não deixe o amor para depois. Finalize sua compra e ganhe frete grátis.

Olá, [Nome do Cliente]!

Percebemos que você adicionou alguns itens especiais para o Dia das Mães ao seu carrinho, mas não finalizou a compra. Que tal garantir o presente perfeito para sua mãe com uma ajudinha extra?

Para te ajudar a celebrar essa data tão especial, estamos oferecendo FRETE GRÁTIS em sua compra!

[Imagem 1 do Produto Abandonado 1]
[Nome do Produto 1]
[Preço do Produto 1]

[Imagem 2 do Produto Abandonado 2]
[Nome do Produto 2]
[Preço do Produto 2]

Aproveite esta oportunidade para presentear sua mãe com muito carinho. O frete grátis é válido apenas nas próximas 24 horas.

👉 FINALIZAR MINHA COMPRA AGORA: [Link para Carrinho Recuperado com URL personalizada com UTMs]

Estamos à disposição para qualquer dúvida.
Com carinho,
Equipe [Nome da Empresa]
```

---

## Checklist

-   [ ] Segmentação por histórico de compra sazonal (ex: "Compradores BF 2023", "Compradores Natal 2023").
-   [ ] Configuração de gatilhos de automação para datas-chave da campanha (ex: 3 dias antes, no dia, 1 dia depois).
-   [ ] Criação de fluxo de boas-vindas específico para novos leads capturados durante o pico sazonal (ex: "Bem-vindo à nossa Black Friday!").
-   [ ] Agendamento de testes A/B para linhas de assunto e horários de envio em cada etapa da automação.
-   [ ] Implementação de e-mails de recuperação de carrinho abandonado com foco na urgência e incentivos sazonais.
-   [ ] Planejamento de sequência de e-mails de nurturing pós-campanha para compradores (upsell/cross-sell) e não-compradores (reengajamento).
-   [ ] Criação de blocos de conteúdo dinâmico nos e-mails baseados na segmentação (ex: produtos para "Mães Clássicas" vs. "Mães Modernas").
-   [ ] Definição de regras de exclusão para evitar sobrecarga de e-mails durante a campanha (ex: quem já comprou não recebe e-mails de oferta).
-   [ ] Preparação de landing pages dedicadas para cada campanha sazonal com UTMs específicos para rastreamento.
-   [ ] Automação de e-mails de agradecimento personalizados para cada campanha com sugestões de produtos complementares.
-   [ ] Análise de dados de campanhas sazonais anteriores para identificar padrões de comportamento e otimizar futuras estratégias.
-   [ ] Garantia de que todos os e-mails são responsivos e renderizam corretamente em diferentes dispositivos e clientes de e-mail.

---

## Métricas de Referência

| Métrica                      | Benchmark (E-commerce Geral) | Meta (Seasonal Campaigns) |
|------------------------------|------------------------------|---------------------------|
| Taxa de Abertura (TO)        | 15-25%                       | 28-35%                    |
| Taxa de Cliques (CTR)        | 2-4%                         | 5-8%                      |
| Taxa de Conversão (CR)       | 1-3%                         | 4-7%                      |
| Receita por E-mail Enviado (EPS) | R$ 0.10 - R$ 0.50            | R$ 0.60 - R$ 1.20         |
| Taxa de Abandono de Carrinho (CAR) | 60-80%                       | 40-55%                    |
| Retorno sobre Investimento (ROI) | 300-500%                     | 700-1000%+                |

---

## Erros Comuns

1.  **Segmentação Superficial**: Não diferenciar entre clientes VIP, novos leads e inativos, enviando a mesma mensagem para todos.
    *   **Como evitar**: Utilize dados históricos de compra, engajamento e navegação para criar micro-segmentos. Ex: Em vez de "Todos os leads", crie "Compradores BF 2023 > R$500" vs. "Leads sem compra, abriu 3+ emails nos últimos 60 dias". Isso permite comunicação ultra-personalizada.
2.  **Falta de Urgência Genuína ou Exagero na Frequência**: Usar "última chance" sem um prazo real ou bombardear a caixa de entrada dos usuários com mensagens repetitivas.
    *   **Como evitar**: Associe a urgência ao estoque limitado, ao término da data sazonal específica (ex: "Só até 23h59 de hoje, 24/11!") ou ao encerramento de um desconto claro. Configure limites de frequência na plataforma de automação (ex: máximo 2 e-mails por cliente por dia durante o pico).
3.  **Conteúdo Não Otimizado para Mobile**: E-mails que não se adaptam bem a dispositivos móveis, resultando em má experiência e abandono.
    *   **Como evitar**: Sempre visualize e teste seus e-mails em diferentes clientes de e-mail e tamanhos de tela (smartphone, tablet) antes do envio. Utilize templates responsivos e imagens otimizadas para carregamento rápido.
4.  **Desconsiderar o Pós-Venda Sazonal**: Encerrar a comunicação após a compra na data sazonal, perdendo oportunidades de retenção.
    *   **Como evitar**: Implemente automações de pós-compra que agradeçam o cliente, solicitem feedback (reviews), ofereçam produtos complementares ou convidem para programas de fidelidade. Ex: "Obrigado pela sua compra de Natal! Que tal um cupom de 15% para a próxima coleção?"

---

## Dicas Avançadas

1.  **Personalização Hiper-Segmentada com IA e Comportamento em Tempo Real**: Utilize ferramentas de automação que se integrem com IA para analisar o comportamento de navegação em tempo real. Se um cliente navegou por "presentes para homem" na semana anterior ao Dia dos Pais, destaque esses produtos nos e-mails da campanha, mesmo que a mensagem geral seja mais ampla.
2.  **Gatilhos de Reengajamento por Inatividade Pós-Pico Sazonal**: Crie uma automação que ative um e-mail de "Sentimos sua falta" 30 dias após o fim de uma grande campanha sazonal (ex: Black Friday) para clientes que não compraram ou não interagiram durante o pico. Ofereça um incentivo exclusivo (ex: frete grátis para a próxima compra) para um novo engajamento fora do período de alta.
3.  **Sequências de "Sneak Peek" com Geração de Expectativa Multi-Canal**: Para campanhas como lançamento de coleção de verão, envie uma série de 2-3 e-mails nos 10 dias anteriores ao lançamento oficial, mostrando pequenos detalhes dos produtos ("teaser"), criando buzz. Complemente com stories no Instagram e posts no Facebook que direcionem para uma landing page de pré-inscrição para acesso antecipado.
4.  **Automação de Feedback Pós-Compra Sazonal com Incentivo de Próxima Compra**: Após 7-14 dias da compra de um item sazonal (ex: um presente de Natal), envie um e-mail pedindo feedback sobre o produto e a experiência de compra, oferecendo um desconto de 10% ou um brinde na próxima compra como agradecimento. Isso ajuda na retenção, coleta de dados e geração de conteúdo para reviews.
5.  **Aproveitamento de Dados de Busca Interna do Site para Segmentação Dinâmica**: Integre os dados de busca interna do seu e-commerce com sua ferramenta de automação. Se um usuário buscou "vestido de festa junina" e não comprou, ative uma sequência de e-mails com produtos relevantes da categoria, dicas de looks para a festa e um cupom de desconto específico para itens juninos.