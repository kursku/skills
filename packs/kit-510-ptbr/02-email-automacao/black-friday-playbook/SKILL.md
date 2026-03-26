---
name: black-friday-playbook
description: "Black Friday Playbook — Skill especializada para criar e otimizar campanhas de e-mail marketing da Black Friday, desde o planejamento até o pós-venda."
license: MIT
metadata:
  version: 1.0.0
  author: Cafe Code AI
  category: 02-email-automacao
  updated: 2026-03-01
risk: safe
---

# Black Friday Playbook

Esta skill capacita o Claude a criar e executar campanhas de e-mail marketing de alta performance para a Black Friday, desde a pré-venda até o pós-evento, com foco em automação, segmentação e conversão.

---

## Keywords

Automação Black Friday, Sequência de E-mail BF, Segmentação RFM, Abandono de Carrinho BF, Nurturing Pós-BF, Pré-venda Black Friday, Subject Lines BF, Ofertas Exclusivas BF, Engajamento E-mail, Fluxo de Resgate BF, Upsell BF, Last Chance BF.

---

## Quick Start

1.  **Gerar sequência de aquecimento**: Solicitar e-mails de teaser e contagem regressiva para os 5 dias que antecedem a Black Friday para uma lista de "Leads Engajados".
2.  **Criar automação de abandono de carrinho**: Desenvolver um fluxo de 3 e-mails para carrinhos abandonados com itens de valor acima de R$150, incluindo um incentivo de desconto progressivo.
3.  **Desenvolver e-mail de última chance**: Elaborar um e-mail com temporizador de escassez e oferta final para produtos de alta margem, a ser enviado 4 horas antes do fim da promoção.
4.  **Revisar subject lines**: Sugerir 5 opções de subject lines de alta conversão para um e-mail de "Desconto Relâmpago" focado em produtos de tecnologia.
5.  **Configurar segmentação pós-BF**: Estruturar uma segmentação de compradores da Black Friday para campanhas de upsell/cross-sell e uma para não-compradores para reengajamento.

---

## Core Workflows

### Workflow 1: Sequência de Aquecimento e Antecipação Pré-Black Friday

Este workflow visa construir expectativa e segmentar a audiência antes do pico de vendas da Black Friday, garantindo que os leads mais qualificados estejam prontos para comprar.

**Passos Detalhados:**

1.  **Segmentação Inicial (15 dias antes da BF):**
    *   **Grupo A (Engajados):** Clientes que abriram 3+ e-mails nos últimos 60 dias ou fizeram uma compra nos últimos 12 meses.
    *   **Grupo B (Inativos):** Clientes que não abriram e-mails nos últimos 90 dias, mas compraram há mais de 12 meses.
    *   **Grupo C (Novos Leads):** Leads capturados nos últimos 30 dias que ainda não compraram.
2.  **Cronograma de Envio (7 a 3 dias antes da BF):**
    *   **D-7 (E-mail 1 - Teaser da Exclusividade):** Enviar para Grupo A e C. Foco em construir curiosidade sobre ofertas "nunca antes vistas" ou "descontos recordes". Incluir um CTA para "Se Inscrever na Lista VIP para Acesso Antecipado".
        *   *Exemplo Subject Line:* "Preparado para o INESQUECÍVEL? Algo GRANDE está chegando! 🚀"
        *   *Conteúdo:* Foco no valor, não no desconto. "Imagine ter acesso às ofertas mais cobiçadas antes de todo mundo... Este ano, a Black Friday será diferente."
    *   **D-5 (E-mail 2 - Valor e Benefício):** Enviar para Grupo A e C (que não se inscreveram na lista VIP). Detalhar os *tipos* de produtos/categorias que terão descontos, sem revelar os preços exatos. Reforçar o CTA para a "Lista VIP".
        *   *Exemplo Subject Line:* "Seu desejo é uma ordem! As categorias mais amadas com descontos épicos na BF! 🎁"
        *   *Conteúdo:* "Prepare-se para renovar sua casa, seu guarda-roupa ou sua tecnologia. Nossas ofertas Black Friday cobrirão [Categoria 1], [Categoria 2] e muito mais. Não perca!"
    *   **D-3 (E-mail 3 - Contagem Regressiva e Urgência):** Enviar para todos os grupos, incluindo o B para tentar reativá-los com a urgência. Incluir um temporizador visual (se a plataforma permitir) e um link direto para a página de "Pré-Black Friday" ou "Em Breve".
        *   *Exemplo Subject Line:* "🚨 72 Horas para o MAIOR EVENTO do ano! Sua chance de economizar de verdade!"
        *   *Conteúdo:* "A contagem regressiva começou! Faltam apenas 3 dias para a Black Friday. Quem estiver na nossa lista VIP terá acesso 24h antes. Clique aqui para garantir sua vaga e não ficar de fora."
3.  **Ação Pós-Envio:** Monitorar taxas de abertura e cliques. Aqueles que clicarem nos CTAs da "Lista VIP" são marcados como "Interessados BF VIP" para receberem e-mails de acesso antecipado.

### Workflow 2: Automação de Abandono de Carrinho Otimizada para Black Friday

Este workflow é crucial para resgatar vendas perdidas durante o período de alta demanda da Black Friday, utilizando incentivos estratégicos e urgência.

**Passos Detalhados:**

1.  **Gatilho de Automação:** Cliente adiciona um item ao carrinho e não finaliza a compra em 30 minutos.
2.  **Segmentação por Valor de Carrinho:**
    *   **Carrinho < R$100:** Foco em lembrete e prova social.
    *   **Carrinho R$100-R$300:** Lembrete com pequeno incentivo de frete ou cupom.
    *   **Carrinho > R$300:** Lembrete com incentivo de desconto percentual ou frete grátis + presente.
3.  **Sequência de E-mails (3 e-mails):**
    *   **E-mail 1 (1 hora após abandono): Lembrete Neutro e Ajuda**
        *   *Para todos os segmentos.*
        *   *Subject Line:* "Seu carrinho ainda está esperando por você! [Nome do Produto] te aguarda!"
        *   *Conteúdo:* "Percebemos que você deixou alguns itens incríveis no seu carrinho. Houve algum problema? Estamos aqui para ajudar!" Incluir imagens dos produtos abandonados e CTA para "Retornar ao Carrinho".
    *   **E-mail 2 (6 horas após abandono): Incentivo Estratégico**
        *   *Para Carrinhos R$100-R$300 e > R$300.*
        *   *Subject Line:* "A Black Friday é AGORA! Não perca sua chance de [Nome do Produto] com um PLUS!"
        *   *Conteúdo (Exemplo para Carrinho > R$300):* "Sabemos que a Black Friday é um mar de ofertas, mas seus itens selecionados são especiais! Que tal um cupom de 10% OFF EXTRA para finalizar sua compra AGORA? Use o código **BFRESGATE10**." Incluir CTA "Finalizar Compra com Desconto".
        *   *Conteúdo (Exemplo para Carrinho R$100-R$300):* "Seus produtos estão quase lá! Para facilitar, oferecemos frete grátis para você finalizar a compra hoje. Clique e aproveite!"
    *   **E-mail 3 (24 horas após abandono): Urgência e Escassez (Última Chance BF)**
        *   *Para todos os segmentos que ainda não converteram.*
        *   *Subject Line:* "ÚLTIMAS HORAS para garantir seus itens da Black Friday! ⏳"
        *   *Conteúdo:* "Esta é sua última chance de aproveitar as ofertas da Black Friday nos produtos que você selecionou. Os descontos e o estoque são limitados! O cupom **BFRESGATE10** expira em 2 horas!" (Se aplicável, adicionar temporizador). Incluir CTA "Garanta Agora!".
4.  **Ação Pós-Envio:** Se o cliente finalizar a compra, removê-lo imediatamente desta automação. Se não, marcar para futuras campanhas de reengajamento pós-BF.

---

## Templates

### E-mail de Pré-Venda Exclusiva Black Friday

```
Assunto: 🤫 Você está na lista VIP! Acesso ANTECIPADO à Black Friday começa em 24h!

Olá, [Nome do Cliente],

É com grande entusiasmo que anunciamos: a Black Friday da [Nome da Empresa] está prestes a começar, e você, como membro VIP, terá acesso exclusivo 24 horas antes do público geral!

Amanhã, [Data da Pré-Venda], a partir das [Horário], você poderá navegar e garantir os produtos mais desejados com descontos que farão história. Prepare-se para ofertas imperdíveis em [Mencionar 2-3 categorias principais, ex: Eletrônicos, Moda e Casa].

Estamos falando de:
🔥 Até 70% OFF em produtos selecionados
📦 Frete Grátis para compras acima de R$299
🎁 Brindes exclusivos nas primeiras 500 compras VIP

Para acessar suas ofertas exclusivas, basta clicar no botão abaixo a partir de amanhã [Data da Pré-Venda], [Horário]:

👉 [Link Direto para a Página de Pré-Venda VIP]

Lembre-se: As melhores ofertas voam! Este é o seu momento de comprar sem pressa e garantir os melhores itens antes que esgotem.

Fique de olho em sua caixa de entrada amanhã!

Atenciosamente,

Equipe [Nome da Empresa]
[Link para o Site da Empresa]
[Link para o Instagram]
```

### E-mail de Última Chance Black Friday

```
Assunto: ⏰ Última Chamada! A Black Friday da [Nome da Empresa] termina em [X] horas!

Olá, [Nome do Cliente],

O relógio está correndo! As ofertas espetaculares da Black Friday da [Nome da Empresa] estão chegando ao fim. Você tem apenas algumas horas para aproveitar os descontos incríveis em todo o nosso site.

[IMAGEM DE UM TEMPORIZADOR DE CONTAGEM REGRESSIVA EM TEMPO REAL]

Não deixe para depois os produtos que você tanto quer. Esta é a sua última oportunidade de economizar até 70% em [Mencionar 2-3 categorias, ex: tecnologia, beleza e artigos esportivos].

Se você deixou algo no carrinho, este é o momento de finalizar sua compra. Seus favoritos estão esperando!

💥 Descontos que encerram hoje à meia-noite
🚀 Frete rápido para todo o Brasil
🔒 Compra segura e facilitada

Clique agora e garanta seus produtos antes que seja tarde demais:

🛒 [Link Direto para a Página da Black Friday]

Não perca! A Black Friday só acontece uma vez por ano.

Um abraço,

Equipe [Nome da Empresa]
[Link para o Site da Empresa]
[Link para o Facebook]
```

---

## Checklist

- [x] Segmentação da base de leads por comportamento (engajamento, histórico de compras) concluída.
- [x] Cronograma de e-mails pré-BF, BF e pós-BF definido e agendado.
- [x] Fluxos de automação de abandono de carrinho com incentivos específicos da BF revisados e ativos.
- [x] Testes A/B para subject lines, CTAs e layouts de e-mail agendados e executados.
- [x] Páginas de destino (landing pages) otimizadas para Black Friday com carregamento rápido e mobile-first.
- [x] Backup da base de e-mails e automações realizado antes do período de pico.
- [x] Temporizadores de escassez (countdown timers) e barras de progresso de estoque implementados nos e-mails chave.
- [x] Sequência de e-mails de pós-compra (agradecimento, pesquisa de satisfação, upsell/cross-sell) configurada.
- [x] Monitoramento de métricas (TA, CTR, TC, Receita por E-mail) em tempo real ativado para ajustes rápidos.
- [x] Plano de contingência para falhas de automação ou picos de tráfego excessivo.

---

## Métricas de Referência

| Métrica               | Benchmark (Geral) | Meta (Black Friday) |
|-----------------------|-------------------|---------------------|
| Taxa de Abertura (TA) | 18% - 22%         | 25% - 35%           |
| CTR (Click-Through Rate) | 2% - 3%           | 4% - 8%             |
| Taxa de Conversão (TC) | 0.5% - 1.5%       | 2% - 5%             |
| Receita por E-mail (RPE) | R$0.50 - R$1.50   | R$2.00 - R$5.00     |
| Taxa de Abandono de Carrinho | 65% - 75%         | 55% - 65%           |
| Taxa de Reengajamento (Pós-BF) | 10% - 15%         | 18% - 25%           |

---

## Erros Comuns

1.  **Enviar e-mails genéricos para toda a base**: Ignorar a segmentação resulta em mensagens irrelevantes.
    *   **Como evitar**: Antes de qualquer envio, segmentar a base por comportamento recente (aberturas, cliques), histórico de compras (valor, categoria) e dados demográficos. *Exemplo: Não enviar a mesma oferta de eletrônicos para um cliente que só compra maquiagem. Criar um e-mail específico de "BF Beauty Deals" para esse segmento.*
2.  **Não testar as automações antes do pico**: Fluxos quebrados ou e-mails com erros causam perda de vendas e reputação.
    *   **Como evitar**: Criar um "cliente teste" e simular todo o percurso de cada automação (abandono de carrinho, sequência de boas-vindas pós-BF, etc.) com antecedência. *Exemplo: Adicionar um item ao carrinho com o e-mail de teste e verificar se os 3 e-mails da sequência de abandono chegam no tempo certo e com os links corretos.*
3.  **Ignorar o pós-venda e o relacionamento pós-Black Friday**: Focar apenas na venda imediata e esquecer o ciclo de vida do cliente.
    *   **Como evitar**: Configurar uma sequência de nutrição pós-compra que agradeça, solicite feedback, ofereça suporte e apresente produtos complementares ou de upsell, mantendo o relacionamento e incentivando a recompra. *Exemplo: Enviar um e-mail 7 dias após a compra com "Esperamos que esteja amando seu [Produto comprado]! Que tal complementar com [Produto relacionado] com um desconto de 15% para você?"*

---

## Dicas Avançadas

1.  **Segmentação Dinâmica por Comportamento em Tempo Real**: Utilize dados de navegação e adição ao carrinho em tempo real para disparar ofertas ultra-personalizadas. *Exemplo: Se um cliente visualiza 5 vezes uma categoria específica de calçados em 2 horas, enviar um e-mail 30 minutos depois com "Notamos seu interesse em [Tipo de Calçado]. Que tal 10% OFF nos seus modelos favoritos para a Black Friday?"*.
2.  **Personalização Hiper-Relevante com Dados Históricos**: Integre o histórico de compras e preferências do cliente para criar e-mails que parecem feitos sob medida. *Exemplo: Para um cliente que sempre compra livros de fantasia, o e-mail da BF pode ser "A Black Friday dos seus sonhos chegou: Descontos épicos em sagas de fantasia que você vai amar!" com banners de livros de autores específicos que ele já comprou.*
3.  **Uso de Temporizadores em Tempo Real e Barras de Progresso de Estoque**: Aumente a urgência com elementos visuais dinâmicos que mostram o tempo restante para o fim de uma oferta ou a quantidade de estoque de um produto. *Exemplo: No e-mail de "Última Chance", ter um GIF ou elemento de imagem que mostra o temporizador diminuindo a cada segundo ou uma barra "X% Vendido" para produtos específicos.*
4.  **Sequências de Reengajamento para Compradores de BF Inativos**: Crie automações para clientes que fizeram sua única compra na Black Friday anterior e não voltaram. *Exemplo: Enviar uma pesquisa de satisfação 6 meses após a BF passada, seguida de um cupom de "retorno" para reativar esses clientes antes da próxima BF ou outras datas sazonais.*
5.  **Teste de Sender Name para Otimização de Abertura**: Além de subject lines, teste diferentes nomes de remetente (Sender Name) para ver qual gera mais confiança e aberturas durante o período de alta concorrência da Black Friday. *Exemplo: Testar "Nome da Empresa", "Nome da Empresa | Ofertas BF" ou "Seu Amigo da [Nome da Empresa]" para e-mails de aquecimento.*