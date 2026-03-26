---
name: referral-system
description: "Referral System — Skill especializada para referral system"
license: MIT
metadata:
  version: 1.0.0
  author: Cafe Code AI
  category: 03-funis-vendas
  updated: 2026-03-01
risk: safe
---

# Referral System

Esta skill capacita o Claude a projetar, implementar e otimizar sistemas de indicação para alavancar a aquisição de clientes e reduzir o CAC, integrando-o diretamente a funis de vendas existentes e otimizando a viralidade do produto.

---

## Keywords

Programa de indicação, Marketing de referência, CAC (Custo de Aquisição de Cliente), LTV (Lifetime Value), Viralidade, Incentivos de indicação, Embaixadores da marca, Funil de referência, Engajamento do referente, Rastreamento de indicações, Modelagem de recompensas, Segmentação de referências, Ciclo de feedback de indicação, Taxa de conversão de referido, Aquisição orgânica.

---

## Quick Start

1.  **Modele o Incentivo Duplo**: Defina a recompensa para o referente e para o referido. Ex: "Ofereça 1 mês grátis do plano Pro ao referente e 20% de desconto nos primeiros 3 meses da assinatura Pro para o referido, após a primeira conversão paga."
2.  **Crie Link de Indicação Único**: Implemente um sistema para gerar um link exclusivo para cada cliente ativo, acessível em sua área de usuário. Ex: "Desenvolva uma funcionalidade no painel do cliente em `app.seuservico.com/indique` que exibe `seuservico.com/convite?ref=CODIGOUNICO` e botões de compartilhamento direto (WhatsApp, e-mail)."
3.  **Desenhe a Jornada do Referido**: Otimize a experiência do usuário que clica no link de indicação. Ex: "Garanta que o link de indicação direcione para uma landing page dedicada (`seuservico.com/desconto`) que automaticamente aplique o desconto prometido ou pré-preencha um campo de código promocional no formulário de cadastro."
4.  **Configure o Rastreamento de Conversão**: Implemente um sistema robusto para monitorar cliques, cadastros e conversões de vendas atribuíveis às indicações. Ex: "Utilize uma ferramenta de referral marketing integrada ao CRM para registrar o `ref_id`, `status` (clicado, cadastrado, pago) e o `valor_da_transacao` de cada referido."
5.  **Comunique o Programa no Pós-Compra**: Integre a divulgação do programa de indicação em pontos de contato estratégicos. Ex: "Inclua um convite explícito na página de confirmação de compra e no e-mail de agradecimento, como 'Gostou? Convide um amigo e ganhe R$50!'"

---

## Core Workflows

### Workflow 1: Implementação de um Programa de Indicação Dupla para SaaS B2C com Foco em LTV

Este workflow detalha a criação e lançamento de um programa de indicação para um software como serviço (SaaS) B2C, com o objetivo de atrair usuários de alto LTV através de incentivos duplos e rastreamento rigoroso.

**Meta Específica:** Aumentar a aquisição de novos assinantes pagantes em 20% via indicações no próximo trimestre, garantindo que o LTV dos indicados seja pelo menos 15% superior à média geral.

**Passos Detalhados:**

1.  **Análise de Cliente Ideal para Indicação:**
    *   **Ação:** Identifique os clientes existentes com maior LTV, maior engajamento com o produto (uso de funcionalidades premium, tempo de sessão) e histórico de satisfação.
    *   **Exemplo Concreto:** "Analise dados do CRM para identificar os 20% de clientes que permanecem ativos por mais de 12 meses, usam 3+ funcionalidades avançadas e têm um NPS superior a 9. Estes serão os 'embaixadores' iniciais."
    *   **Dados:** LTV médio atual: R$800. Meta LTV de indicados: R$920.

2.  **Modelagem e Teste de Recompensa Dupla:**
    *   **Ação:** Projete um sistema de recompensa que beneficie tanto o referente quanto o referido, com foco em valor percebido.
    *   **Exemplo Concreto:** "Para o referente: 1 mês grátis do plano 'Premium' (valor R$99) por cada indicação que converter em assinante pagante. Para o referido: 25% de desconto nos primeiros 6 meses do plano 'Premium' (reduz a mensalidade de R$99 para R$74,25)."
    *   **Teste:** "Realize uma pesquisa qualitativa com 50 clientes do segmento 'embaixador' para validar a atratividade da recompensa. Ajuste se a percepção de valor for baixa (ex: aumentar desconto para 30% ou adicionar um bônus de setup)."

3.  **Desenvolvimento da Plataforma de Indicação (In-App):**
    *   **Ação:** Crie uma seção intuitiva dentro do aplicativo ou painel do cliente para gerenciar indicações.
    *   **Exemplo Concreto:** "Implemente uma aba 'Indique e Ganhe' no menu principal do usuário. Esta aba deve conter:
        *   Um link de indicação único (ex: `app.meuservice.com/ref/SEUCODIGO`).
        *   Botões de compartilhamento direto para WhatsApp, E-mail e LinkedIn, com textos pré-formatados.
        *   Um mini-dashboard mostrando 'Indicações Enviadas', 'Indicações Aceitas', 'Indicações Convertidas' e 'Recompensas Recebidas/Pendentes'."
    *   **Tecnologia:** Integração com plataformas como ReferralCandy ou um módulo customizado no backend.

4.  **Criação de Landing Page Otimizada para Referidos:**
    *   **Ação:** Desenvolva uma página de destino específica para os cliques nos links de indicação.
    *   **Exemplo Concreto:** "A landing page `meuservice.com/convite-especial` deve:
        *   Detectar automaticamente o `ref_id` do URL e exibir uma mensagem como 'Você foi convidado por [Nome do Referente]!'.
        *   Destacar claramente o benefício de 25% de desconto.
        *   Ter um CTA proeminente 'Experimente o Premium com Desconto' que leva a um formulário de cadastro pré-preenchido com o código de desconto ou um campo oculto para o `ref_id`."
        *   Incluir depoimentos de usuários e prova social.

5.  **Automação do Fluxo de Recompensas e Comunicação:**
    *   **Ação:** Configure gatilhos para entregar recompensas e comunicar o status.
    *   **Exemplo Concreto:**
        *   "Quando um referido realizar a primeira assinatura paga, o sistema deve automaticamente creditar 1 mês grátis do plano 'Premium' na conta do referente."
        *   "Enviar e-mail para o referente: '🎉 Boas notícias! Seu amigo [Nome do Referido] ativou a assinatura! Você ganhou 1 mês grátis do plano Premium. Aproveite!'"
        *   "Enviar e-mail para o referido: 'Bem-vindo ao [Nome do SaaS]! Seu desconto de 25% foi aplicado. Conte com a gente!'"

6.  **Lançamento e Promoção Contínua:**
    *   **Ação:** Comunique o programa de forma estratégica e contínua.
    *   **Exemplo Concreto:** "Lance o programa com um e-mail segmentado para os 'embaixadores' identificados na etapa 1. Posteriormente:
        *   Banners rotativos na área do usuário.
        *   Pop-ups de saída para usuários engajados após uma sessão longa.
        *   Mencione o programa nos e-mails de onboarding e newsletters mensais."

7.  **Monitoramento e Otimização:**
    *   **Ação:** Rastreie métricas chave e ajuste o programa.
    *   **Exemplo Concreto:** "Monitore a 'Taxa de Conversão de Referidos' (clique -> cadastro -> pago), 'LTV dos Clientes Indicados' vs. 'LTV de Clientes Orgânicos', e 'CAC via Indicação'. Se o LTV dos indicados estiver abaixo da meta, considere ajustar a segmentação de embaixadores ou o tipo de incentivo para atrair perfis mais qualificados."

### Workflow 2: Otimização de um Programa de Indicação para E-commerce B2C com Foco em AOV e Re-compra

Este workflow visa refinar um programa de indicação existente em um e-commerce, focando em aumentar o valor médio do pedido (AOV) e a taxa de re-compra dos clientes indicados.

**Meta Específica:** Aumentar o AOV dos clientes indicados em 10% (de R$150 para R$165) e a taxa de re-compra em 7% (de 25% para 32%) nos próximos 4 meses.

**Passos Detalhados:**

1.  **Análise de Performance Atual do Programa:**
    *   **Ação:** Avalie os dados históricos do programa de indicação.
    *   **Exemplo Concreto:** "Extraia relatórios do sistema de referral para identificar:
        *   AOV médio dos referidos vs. AOV médio de outros canais.
        *   Taxa de re-compra dos referidos.
        *   Quais produtos ou categorias são mais (e menos) indicados.
        *   Segmentos de clientes que mais indicam e o perfil dos seus referidos."
    *   **Dados:** AOV atual de referidos: R$150. Taxa de re-compra de referidos: 25%.

2.  **Segmentação de Referentes e Recompensas Personalizadas:**
    *   **Ação:** Crie diferentes níveis de recompensa com base no LTV e comportamento de compra dos referentes.
    *   **Exemplo Concreto:** "
        *   **Referentes 'Top Clientes' (LTV > R$1000, 5+ compras):** Vouchers de R$75 para cada indicação convertida + acesso antecipado a lançamentos.
        *   **Referentes 'Compradores Frequentes' (3-4 compras):** Vouchers de R50 para cada indicação convertida.
        *   **Referentes 'Novos Clientes' (1-2 compras):** Vouchers de R$30 para cada indicação convertida."
    *   **Objetivo:** Incentivar os melhores clientes a indicarem, potencialmente atraindo referidos de perfil similar.

3.  **Otimização do Incentivo para Referidos (Foco em AOV):**
    *   **Ação:** Ajuste a recompensa inicial do referido para estimular um valor de pedido maior.
    *   **Exemplo Concreto:** "Em vez de um desconto fixo de 10%, ofereça: 'Ganhe R$50 de desconto na sua primeira compra acima de R$200 + Frete Grátis'. Isso encoraja o referido a aumentar o carrinho para atingir o valor mínimo e aproveitar o frete."
    *   **Teste:** "Realize um A/B test com 50% dos referidos recebendo a oferta antiga e 50% a nova, monitorando o AOV e a taxa de conversão."

4.  **Estratégias de Re-engajamento para Referidos Convertidos (Foco em Re-compra):**
    *   **Ação:** Desenvolva um fluxo de e-mail marketing pós-primeira compra para referidos.
    *   **Exemplo Concreto:** "
        *   **Dia 7 após 1ª compra:** E-mail com 'Sugestões de produtos complementares' + 'Cupom de 10% OFF para sua próxima compra'.
        *   **Dia 30 após 1ª compra:** E-mail 'Não nos esqueça!' com lista de desejos baseada em navegação e um lembrete do programa de indicação (eles também podem indicar agora!).
        *   **Dia 60 após 1ª compra:** E-mail 'Seu voucher está esperando!' com um incentivo de re-compra de R$25, válido por 7 dias."

5.  **A/B Testing de Mensagens e Criativos nos Canais de Indicação:**
    *   **Ação:** Teste diferentes abordagens de comunicação para o programa.
    *   **Exemplo Concreto:** "
        *   **Página de Indicação:** Teste CTAs como 'Indique e Ganhe Agora!' vs. 'Seja um Embaixador e Seja Recompensado!'.
        *   **Textos de Compartilhamento Social:** Teste 'Adoro os produtos da [Nome da Loja]! Use meu link para ganhar R$50 de desconto: [LINK]' vs. 'Ajude um amigo a economizar e ganhe R$50 para você! Clique: [LINK]'."

6.  **Integração do Programa em Pontos de Contato Pós-Compra:**
    *   **Ação:** Garanta que o programa de indicação seja visível após a experiência de compra.
    *   **Exemplo Concreto:** "
        *   **Email de Confirmação de Pedido:** Inclua um banner no rodapé: 'Satisfeito com sua compra? Indique um amigo e ganhe R$50!'.
        *   **Embalagem do Produto:** Adicione um cartão físico com um QR Code para a página de indicação e um breve convite."

---

## Templates

### E-mail de Lançamento de Programa de Indicação (SaaS)

```
Assunto: 🎉 Indique um Amigo para [Nome do SaaS] e Ganhe 1 Mês Grátis do Plano Premium!

Olá [Nome do Cliente],

Sabemos que você adora usar o [Nome do SaaS] para [Benefício Principal, ex: gerenciar seus projetos com eficiência]. Que tal compartilhar essa experiência e ser recompensado por isso?

Estamos lançando nosso novo Programa de Indicação! Agora, você pode ajudar seus amigos a descobrir a potência do [Nome do SaaS] e, de quebra, ganhar benefícios incríveis.

**Como funciona:**

1.  **Compartilhe Seu Link:** Acesse sua área de indicação em [Link para a Área de Indicação do Cliente] e copie seu link exclusivo.
2.  **Seu Amigo se Cadastra:** Quando seu amigo usar seu link para se cadastrar e assinar o plano Premium, ele ganha **25% de desconto nos primeiros 6 meses!**
3.  **Você Ganha:** Assim que seu amigo se tornar um assinante pagante do plano Premium, você ganha **1 Mês Grátis do Plano Premium** na sua própria conta!

É uma situação ganha-ganha!

**Seu Link de Indicação Exclusivo:**
[Link de Indicação Único do Cliente, ex: https://app.seuservice.com/ref/SEUCODIGO]

Compartilhe com seus colegas, amigos ou qualquer pessoa que você ache que se beneficiaria do [Nome do SaaS].

Acesse sua área de indicação para começar e acompanhar seus ganhos:
[Link para a Área de Indicação do Cliente]

Termos e condições aplicáveis.

Um abraço,
Equipe [Nome do SaaS]
[Link para o Site do SaaS]
```

### Texto para Compartilhamento Social (E-commerce)

```
**Opção 1 (Foco no Amigo):**
"Descobri a loja perfeita para [Tipo de Produto, ex: moda sustentável]! A [Nome da Loja] tem produtos incríveis e sustentáveis. Use meu link e ganhe R$50 de desconto na sua primeira compra acima de R$200 + Frete Grátis! ✨ #ModaConsciente #Desconto [Link de Indicação Único do Cliente]"

**Opção 2 (Foco no Benefício Duplo):**
"Amando minhas novas peças da [Nome da Loja]! 😍 Quer um desconto? Use meu link e você ganha R$50 na primeira compra (acima de R$200) + Frete Grátis, e eu também ganho um presentinho! Win-win! 😉 [Link de Indicação Único do Cliente] #ComprasOnline #IndiqueEganhe"

**Opção 3 (Curto e Direto para WhatsApp/Stories):**
"Conhece a [Nome da Loja]? Produtos top e agora com desconto pra você! Use meu link e ganhe R$50 na sua primeira compra: [Link de Indicação Único do Cliente] #Desconto #Shopping"
```

---

## Checklist

- [x] Definição clara do modelo de recompensa (dupla, única, escalonada).
- [x] Geração automatizada de links de indicação únicos por cliente.
- [x] Landing page otimizada para referidos, com pré-preenchimento de dados ou aplicação automática de desconto.
- [x] Sistema de rastreamento robusto para atribuição de indicações (cliques, cadastros, conversões).
- [x] Automação para entrega de recompensas aos referentes e referidos.
- [x] Canais de comunicação definidos para promover o programa de forma contínua (e-mail, in-app, social).
- [x] Dashboard de acompanhamento para clientes (referentes) visualizarem suas indicações e ganhos.
- [x] Página de FAQ detalhada sobre o funcionamento e elegibilidade do programa de indicação.
- [x] Termos e Condições do programa acessíveis, claros e juridicamente revisados.
- [x] Plano para re-engajamento de referentes inativos (clientes que não indicaram ou pararam de indicar).
- [x] Análise periódica do LTV e AOV dos clientes indicados vs. clientes orgânicos.
- [x] Implementação de testes A/B para otimizar incentivos, mensagens e criativos.

---

## Métricas de Referência

| Métrica                         | Benchmark (SaaS B2C) | Meta (SaaS B2C) | Benchmark (E-commerce) | Meta (E-commerce) |
|---------------------------------|----------------------|-----------------|------------------------|-------------------|
| Taxa de Conversão de Indicados  | 10-25%               | 30%             | 5-15%                  | 20%               |
| Participação no Programa        | 5-15% (da base ativa)| 20%             | 3-10%                  | 15%               |
| CAC via Indicação (Custo/Aquisição) | 20-50% menor que outros canais | 60% menor       | 15-40% menor           | 50% menor         |
| LTV de Clientes Indicados       | 10-25% maior que orgânicos | 30% maior       | 5-15% maior            | 20% maior         |
| AOV de Clientes Indicados       | N/A                  | N/A             | 5-10% maior que orgânicos | 15% maior        |
| Número médio de indicações por referente | 1.5-3                 | 4               | 1-2                    | 2.5               |

---

## Erros Comuns

1.  **Recompensa Não Atraente ou Incompatível**: Oferecer um incentivo que não gera valor real ou não se alinha ao perfil do público, como um desconto mínimo para um produto de alto valor.
    *   **Como evitar**: Pesquise o valor percebido do seu produto/serviço e o perfil do seu cliente. Para um SaaS de R$500/mês, um desconto de R$10 é irrisório. Ofereça um mês grátis (R$500) ou um percentual significativo (20-30%). Para e-commerce, vouchers de R$50-R$100 para compras acima de R$200 são mais eficazes do que 5% de desconto.

2.  **Processo de Indicação Complicado e Não Intuitivo**: Exigir que o referente ou o referido preencha formulários longos, insira códigos manualmente ou passe por muitas etapas para concluir a indicação ou resgatar a recompensa.
    *   **Como evitar**: Simplifique ao máximo. Crie um link de compartilhamento de um clique e uma landing page que auto-aplica o benefício ou pré-preenche o formulário. A automação deve ser invisível para o usuário, garantindo uma jornada fluida.

3.  **Falta de Rastreamento Preciso e Atribuição de Indicações**: Não ter um sistema confiável para monitorar quem indicou quem, quando a conversão ocorreu e qual o status da recompensa, levando a erros na atribuição e insatisfação.
    *   **Como evitar**: Invista em uma ferramenta de referral marketing dedicada (ex: ReferralCandy, Ambassador) ou desenvolva um sistema interno robusto com códigos de referência únicos (IDs), UTMs para cliques e integração com o CRM e sistema de vendas para rastrear cada etapa da jornada do referido, desde o clique até a conversão e o LTV.

4.  **Comunicação Ineficaz ou Inconsistente do Programa**: Lançar o programa de indicações e não promovê-lo continuamente através de múltiplos canais, fazendo com que os clientes se esqueçam de sua existência.
    *   **Como evitar**: Integre a comunicação do programa em diversos pontos de contato: e-mails de boas-vindas, e-mails pós-compra/uso, pop-ups no site/app, seção dedicada na área do cliente, banners rotativos e postagens regulares em redes sociais. Crie um calendário editorial para a promoção do