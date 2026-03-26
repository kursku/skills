---
name: testimonial-request
description: "Testimonial Request — Skill especializada para testimonial request"
license: MIT
metadata:
  version: 1.0.0
  author: Cafe Code AI
  category: 02-email-automacao
  updated: 2026-03-01
risk: safe
---

# Testimonial Request

Esta skill capacita o Claude a criar e gerenciar sequências de email automatizadas altamente eficazes para solicitar depoimentos de clientes satisfeitos, otimizando a prova social para diversos negócios.

---

## Keywords

Depoimentos de Clientes, Prova Social, Feedback Automatizado, Solicitação de Testemunho, Email Marketing, Automação de CS, Pós-Venda, Funil de Depoimentos, NPS, Sucesso do Cliente, Conteúdo Gerado pelo Usuário, Avaliações Online.

---

## Quick Start

1.  **Segmentar Clientes Satisfeitos:** Identifique clientes com score NPS 9-10, que fizeram uma compra recente (últimos 30-90 dias) ou concluíram um marco de sucesso com seu produto/serviço.
2.  **Configurar Gatilho de Automação:** Defina um gatilho na sua ferramenta de automação (e.g., "30 dias após a conclusão do onboarding", "7 dias após o preenchimento de NPS 9-10", "15 dias após a renovação").
3.  **Personalizar o Email Inicial:** Use um dos templates fornecidos abaixo, personalizando com o nome do cliente, o produto/serviço utilizado e o benefício específico que ele obteve.
4.  **Criar Página de Destino Simples:** Garanta que o link do email direcione para uma página otimizada para depoimentos (formulário curto, opção de vídeo/texto, exemplos de depoimentos).
5.  **Monitorar e Otimizar:** Acompanhe as taxas de abertura, cliques e conversão da sequência, ajustando subject lines e o conteúdo dos emails conforme necessário.

---

## Core Workflows

### Workflow 1: Automação de Depoimentos Pós-Conclusão de Projeto/Serviço Premium

Este workflow é ideal para empresas que oferecem serviços de alto valor, consultorias ou produtos complexos com um ciclo de vida de cliente bem definido, onde o sucesso é mensurável.

**Passos Detalhados:**

1.  **Critério de Entrada:** O cliente concluiu um projeto/serviço premium há 30 dias E foi classificado como "Defensor" (NPS 9-10) em uma pesquisa de satisfação pós-projeto. Alternativamente, o gerente de contas marcou o cliente como "Sucesso do Caso".
2.  **Sequência de Email (Drip Campaign):**

    *   **Email 1 (Dia 0: Gatilho Ativado)**
        *   **Assunto:** Uma Pergunta Rápida sobre o [Nome do Projeto/Serviço] com a [Sua Empresa]
        *   **Conteúdo:** Foco em agradecer, relembrar o valor entregue e fazer uma solicitação direta, mas leve. Incluir um link claro para o formulário de depoimento.
        *   **Exemplo:**
            ```
            Olá [Nome do Cliente],

            Esperamos que esteja aproveitando ao máximo os resultados do nosso projeto de [Nome do Projeto/Serviço] que finalizamos recentemente! Foi um prazer enorme para a equipe da [Sua Empresa] trabalhar com você.

            Sua experiência é super importante para nós. Gostaríamos de saber, em poucas palavras, como o [Nome do Projeto/Serviço] impactou positivamente [Área Específica, e.g., "a produtividade da sua equipe" ou "o crescimento do seu negócio"].

            Se você puder compartilhar um rápido depoimento sobre sua experiência, isso nos ajudaria imensamente a inspirar outras empresas a alcançar resultados semelhantes. É super rápido, prometemos!

            Compartilhe seu depoimento aqui: [Link Direto para Formulário de Depoimento]

            Agradecemos muito sua parceria e seu tempo!

            Atenciosamente,

            [Seu Nome/Nome da Equipe]
            [Sua Empresa]
            ```

    *   **Email 2 (Dia 3: Follow-up Gentil)**
        *   **Assunto:** Re: Uma Pergunta Rápida sobre o [Nome do Projeto/Serviço] com a [Sua Empresa]
        *   **Conteúdo:** Lembrete suave, reforçando o valor do depoimento e talvez oferecendo ajuda para preencher.
        *   **Exemplo:**
            ```
            Olá [Nome do Cliente],

            Esperamos que esteja tudo ótimo por aí!

            Só queríamos fazer um rápido acompanhamento sobre nosso último email. Entendemos que você está ocupado, mas seu feedback sobre o projeto de [Nome do Projeto/Serviço] é realmente valioso para nós e para outros clientes em potencial.

            Se preferir, podemos até mesmo ajudar a rascunhar algumas ideias com base em seus resultados. Basta nos responder.

            Você pode compartilhar seu depoimento diretamente aqui: [Link Direto para Formulário de Depoimento]

            Muito obrigado pela sua consideração!

            Um abraço,

            [Seu Nome/Nome da Equipe]
            [Sua Empresa]
            ```

    *   **Email 3 (Dia 7: Última Chamada com Incentivo Opcional)**
        *   **Assunto:** Última Chamada: Seu Depoimento sobre o [Nome do Projeto/Serviço] + [Pequeno Incentivo Opcional]
        *   **Conteúdo:** Última tentativa, com um possível incentivo discreto (e.g., destaque no site, breve consultoria gratuita, desconto em próximo serviço).
        *   **Exemplo:**
            ```
            Olá [Nome do Cliente],

            Este é o nosso último convite para compartilhar sua experiência sobre o [Nome do Projeto/Serviço]. Seu depoimento não só nos ajuda a crescer, mas também valida o impacto real do nosso trabalho para outras empresas.

            Para agradecer pelo seu tempo, se você puder compartilhar seu depoimento até o final desta semana, teremos o prazer de [Oferecer um incentivo, e.g., "destacar seu caso de sucesso em nosso blog/redes sociais" ou "oferecer uma consultoria estratégica de 30 minutos gratuita"].

            Compartilhe seu depoimento agora: [Link Direto para Formulário de Depoimento]

            Agradecemos sua atenção!

            Atenciosamente,

            [Seu Nome/Nome da Equipe]
            [Sua Empresa]
            ```
3.  **Ação Pós-Depoimento:** Se o depoimento for enviado, o cliente é removido da sequência e recebe um email de agradecimento personalizado.

### Workflow 2: Solicitação de Avaliação para Produtos de Consumo Recorrente/SaaS

Este workflow é otimizado para clientes que usam produtos de forma contínua (SaaS, produtos de assinatura) e têm um relacionamento mais longo com a marca, focando em avaliações e estrelas.

**Passos Detalhados:**

1.  **Critério de Entrada:** Cliente está ativo há mais de 6 meses no plano [Nome do Plano/Produto] E tem um histórico de alto engajamento (e.g., logou X vezes no último mês, usou recurso Y com frequência) OU fez uma renovação recente.
2.  **Sequência de Email:**

    *   **Email 1 (Dia 0: Gatilho Ativado)**
        *   **Assunto:** Uma pergunta rápida sobre sua experiência com [Nome do Produto/Serviço]
        *   **Conteúdo:** Pedido direto de avaliação, mostrando a importância do feedback.
        *   **Exemplo:**
            ```
            Olá [Nome do Cliente],

            Esperamos que você esteja aproveitando ao máximo todas as funcionalidades do [Nome do Produto/Serviço]! Vemos que você tem sido um usuário fiel de [Recurso Específico, e.g., "nossa ferramenta de automação de emails"] e isso nos deixa muito felizes.

            Para continuarmos melhorando e servindo você ainda melhor, adoraríamos ouvir sua opinião sincera. Seu feedback é crucial para nós e para a comunidade de [Nome do Produto/Serviço].

            Você poderia nos dar alguns minutos para compartilhar sua avaliação? É super rápido e faz uma grande diferença!

            Avalie sua experiência aqui: [Link Direto para Página de Avaliação (e.g., Capterra, G2, App Store, ou formulário interno)]

            Muito obrigado por fazer parte da nossa jornada!

            Atenciosamente,

            Equipe [Nome do Produto/Serviço]
            ```

    *   **Email 2 (Dia 4: Lembrete com Exemplo de Impacto)**
        *   **Assunto:** Re: Uma pergunta rápida sobre sua experiência com [Nome do Produto/Serviço]
        *   **Conteúdo:** Lembrete suave, talvez com um breve exemplo de como outros feedbacks ajudaram a melhorar o produto.
        *   **Exemplo:**
            ```
            Olá [Nome do Cliente],

            Só um rápido lembrete sobre nossa solicitação de avaliação para o [Nome do Produto/Serviço].

            Seu feedback é o combustível para nossas inovações! Graças a avaliações como a sua, conseguimos implementar funcionalidades como [Exemplo de Funcionalidade Desenvolvida com Base em Feedback de Clientes, e.g., "o novo dashboard de relatórios"] e melhorar a experiência de todos.

            Sua avaliação de hoje pode inspirar a próxima grande melhoria!

            Compartilhe sua opinião: [Link Direto para Página de Avaliação]

            Agradecemos imensamente!

            Um abraço,

            Equipe [Nome do Produto/Serviço]
            ```
3.  **Ação Pós-Avaliação:** O cliente é removido da sequência. Se a avaliação for pública, um email de agradecimento e um convite para compartilhar a avaliação em outras redes sociais pode ser enviado.

---

## Templates

### Template 1: Email de Solicitação de Depoimento para Cliente B2B Satisfeito (Pós-Projeto)

```
Assunto: Sua Opinião Valiosa sobre o [Nome do Projeto] com a [Sua Empresa]

Olá [Nome do Cliente],

Esperamos que esteja tudo excelente por aí na [Nome da Empresa do Cliente]!

Estamos acompanhando os excelentes resultados que vocês têm colhido desde a conclusão do projeto de [Nome do Projeto] com a nossa equipe, há [Número] semanas. É sempre gratificante ver o impacto positivo do nosso trabalho, como o aumento de [Métrica Específica, e.g., "25% na taxa de conversão"] que vocês reportaram.

Para nós, esses sucessos são a melhor prova do nosso comprometimento. Gostaríamos muito de convidar você para compartilhar um breve depoimento sobre sua experiência com a [Sua Empresa] e o [Nome do Projeto]. Sua perspectiva é incrivelmente valiosa e pode inspirar outras empresas a alcançar resultados semelhantes.

Seria um depoimento de texto, vídeo ou áudio, o que for mais fácil para você! Temos um formulário simples que leva menos de 5 minutos para preencher:

👉 Compartilhe seu Depoimento: [Link Direto para o Formulário de Depoimento]

Agradecemos imensamente seu tempo e parceria.

Atenciosamente,

[Seu Nome]
[Seu Cargo]
[Sua Empresa]
[Seu Telefone/Website]
```

### Template 2: Email de Follow-up com Opção de Depoimento em Vídeo (Para Clientes Engajados)

```
Assunto: Re: Gostaríamos de ouvir sua história com [Nome do Produto/Serviço]!

Olá [Nome do Cliente],

Esperamos que esteja tendo um ótimo dia!

Este é apenas um rápido acompanhamento sobre nosso email anterior. Vemos que você tem sido um usuário bastante ativo do [Nome do Recurso Mais Usado pelo Cliente, e.g., "dashboard de análises avançadas"] no [Nome do Produto/Serviço], e isso é fantástico!

Seu feedback e sua história de sucesso são uma inspiração para nossa comunidade. Sabia que muitos de nossos clientes adoram compartilhar seus depoimentos em vídeo? É uma forma autêntica e impactante de mostrar como o [Nome do Produto/Serviço] realmente faz a diferença.

Se você se sentir confortável em compartilhar sua experiência em um vídeo curto (pode ser gravado diretamente do seu celular!), temos um link fácil para você:

🎥 Grave seu Vídeo Depoimento: [Link Direto para Ferramenta de Gravação de Vídeo Depoimento, e.g., Vocal Video, VideoAsk]

Ou, se preferir o formato de texto, nosso formulário ainda está disponível:
📝 Envie seu Depoimento em Texto: [Link Direto para o Formulário de Depoimento de Texto]

Muito obrigado por considerar! Sua voz é muito importante para nós.

Um abraço,

Equipe [Nome do Produto/Serviço]
```

---

## Checklist

- [x] Clientes segmentados com base em satisfação (NPS alto, sucesso comprovado).
- [x] Gatilho de automação configurado para o momento ideal do cliente.
- [x] Email inicial personalizado com nome, produto e benefício específico.
- [x] Assunto do email claro e convidativo, gerando curiosidade.
- [x] Call-to-Action (CTA) explícito e com link direto para a página de depoimento.
- [x] Página de destino otimizada para envio de depoimentos (formulário curto, fácil acesso).
- [x] Opções de formato de depoimento oferecidas (texto, vídeo, áudio), se aplicável.
- [x] Sequência de follow-up planejada para quem não respondeu ao primeiro email.
- [x] Email de agradecimento automático configurado para após o envio do depoimento.
- [x] Incentivo ético e alinhado ao negócio considerado (se houver).
- [x] Testes A/B para diferentes subject lines e CTAs.

---

## Métricas de Referência

| Métrica                         | Benchmark (Indústria) | Meta (Otimizada) |
|---------------------------------|-----------------------|------------------|
| Taxa de Abertura (Emails de Depoimento) | 30-45%                | 40-55%           |
| Taxa de Cliques (CTA para Formulário) | 10-20%                | 15-25%           |
| Taxa de Conversão (Depoimentos Recebidos) | 3-7%                  | 6-10%            |
| Tempo Médio de Resposta (Dias)  | 5-10 dias             | 3-7 dias         |
| NPS Médio dos Clientes Solicitados | 8-10                  | 9-10             |
| Taxa de Depoimentos em Vídeo    | 5-15%                 | 10-20%           |

---

## Erros Comuns

1.  **Solicitar Depoimento de Clientes Insatisfeitos**: Enviar pedidos de depoimento para toda a base de clientes sem segmentação de satisfação.
    *   **Como evitar**: Implementar pesquisas de NPS ou CSAT antes de qualquer solicitação. Clientes com NPS abaixo de 7 devem ser direcionados para um fluxo de "recuperação de cliente" em vez de depoimentos. Exemplo: Se o cliente deu NPS 6, o email deve ser "Como podemos melhorar sua experiência, [Nome do Cliente]?" e não "Compartilhe seu sucesso!".
2.  **Emails Genéricos Sem Personalização**: Usar um template de email único sem customização para o produto/serviço específico ou para o cliente individual.
    *   **Como evitar**: Utilizar campos dinâmicos na automação (nome do cliente, nome do produto/serviço adquirido, data da compra/conclusão). Mencionar um benefício específico que o cliente obteve. Exemplo: Em vez de "Fale sobre sua experiência", use "Como o [Produto X] ajudou a [resolver o problema Y da sua empresa]?".
3.  **Call-to-Action (CTA) Confuso ou Dificultoso**: O link para o depoimento não está claro, leva a uma página complexa ou exige muitos passos para preencher.
    *   **Como evitar**: O CTA deve ser um link direto e destacado para um formulário de depoimento simples, com poucas perguntas e campos obrigatórios. Exemplo: Em vez de "Clique aqui para feedback", use "Compartilhe seu Depoimento em 3 Minutos: [Link Direto]".

---

## Dicas Avançadas

1.  **Gatilhos Contextuais Profundos**: Em vez de apenas pós-compra, explore gatilhos baseados em uso de recursos-chave, atingimento de milestones dentro do produto (e.g., "cliente atingiu 1000 envios de email", "usuário completou o módulo X do curso"). Isso garante que a solicitação seja feita em um momento de pico de valor percebido.
2.  **Páginas de Destino Dinâmicas**: Crie landing pages de depoimentos que pré-preencham informações básicas do cliente (nome, produto) ou que apresentem perguntas específicas baseadas no segmento ou no problema que o produto resolveu para ele. Isso reduz o atrito e aumenta a relevância.
3.  **Incentivos Estratégicos e Escalonados**: Para depoimentos de alto valor (vídeo, estudo de caso), considere oferecer incentivos mais significativos, como um destaque em um estudo de caso publicado, um voucher para serviços premium ou uma doação para uma instituição de caridade em nome do cliente. Certifique-se de que a oferta seja clara e ética.
4.  **Reciclagem de Depoimentos**: Automatize a distribuição de depoimentos recebidos em outros canais. Um depoimento de texto pode ser transformado em um post para redes sociais, um carrossel no Instagram ou uma citação em uma página de vendas. Ferramentas de IA podem ajudar a extrair os pontos-chave.
5.  **Integração com Ferramentas de Video Testimonial**: Utilize plataformas como Vocal Video ou Vidyard que simplificam o processo de gravação de depoimentos em vídeo, oferecendo prompts e edição básica, tornando o processo fácil para o cliente e o resultado profissional para você. Inclua o link direto para estas plataformas na sua automação.