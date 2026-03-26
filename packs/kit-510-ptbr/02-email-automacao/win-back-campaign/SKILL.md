---
name: win-back-campaign
description: "Win Back Campaign — Skill especializada para win back campaign"
license: MIT
metadata:
  version: 1.0.0
  author: Cafe Code AI
  category: 02-email-automacao
  updated: 2026-03-01
risk: safe
---

# Win Back Campaign

Esta skill capacita o Claude a arquitetar, implementar e otimizar sequências de email automatizadas focadas em reativar clientes inativos, recuperando vendas perdidas e mitigando o churn.

---

## Keywords

reativação de clientes, automação de e-mail, clientes inativos, redução de churn, segmentação por inatividade, oferta de reengajamento, ciclo de vida do cliente, email marketing, jornada do cliente, retenção, engajamento, remarketing.

---

## Quick Start

1.  **Identifique o Limite de Inatividade**: Determine um período claro de inatividade (ex: 90 dias sem compra para e-commerce; 30 dias sem login para SaaS).
2.  **Crie o Segmento de Inativos**: Configure na plataforma de automação um segmento dinâmico para clientes que cruzam esse limite.
3.  **Defina a Oferta de Reengajamento**: Estabeleça um incentivo concreto (ex: 15% de desconto, frete grátis, acesso a recurso premium por tempo limitado) para a reativação.
4.  **Configure a Sequência de 3 Emails**: Projete uma automação com 3 emails disparados em intervalos estratégicos (Dia 0, Dia 3, Dia 7) focando na oferta e no valor.
5.  **Monitore e Otimize**: Lance a campanha e acompanhe as taxas de reabertura, cliques e, crucialmente, a taxa de reativação para ajustes contínuos.

---

## Core Workflows

### Workflow 1: Reativação de Clientes Inativos para E-commerce

Este workflow detalha a implementação de uma campanha de win-back para clientes que não realizaram compras em um período estendido, visando incentivá-los a retornar ao site e finalizar uma nova transação.

**Passos Detalhados:**

1.  **Segmentação de Inatividade de Compra**:
    *   **Ação**: Na plataforma de automação (ex: ActiveCampaign, RD Station Marketing), crie um segmento de público.
    *   **Critério**: Clientes que realizaram pelo menos uma compra no passado, mas não registraram nenhuma compra nos últimos 90 dias. Para clientes de alto valor (AOV > R$500), considere um período mais curto, como 60 dias. Exclua clientes que já estão em outra automação ou que já reativaram.
    *   **Exemplo**: Segmento "Inativos 90D+" com filtro "Data da última compra é maior que 90 dias atrás" E "Total de compras é maior que 0".

2.  **Definição da Oferta e Narrativa Central**:
    *   **Ação**: Escolha uma oferta com valor percebido.
    *   **Exemplo de Oferta**: "15% de desconto na próxima compra acima de R$100 + Frete Grátis" ou "R$50 de crédito para usar em qualquer produto".
    *   **Narrativa**: Foco em "sentimos sua falta", "novidades te esperando" e o benefício da oferta.

3.  **Criação da Sequência de E-mails Automatizada**:
    *   **Ferramenta**: Configure uma nova automação acionada pela entrada no segmento "Inativos 90D+".
    *   **Estrutura da Sequência (Exemplo de 3 emails):**
        *   **Email 1 (Dia 0 - Entrada na Automação): "Sentimos sua falta! Novidades te esperando..."**
            *   **Objetivo**: Relembrar a marca e o valor inicial.
            *   **Conteúdo**: Tom amigável, menção ao tempo sem interação. Apresentação sutil da oferta principal.
            *   **Call-to-Action (CTA)**: "Explorar Novidades" (link para categoria de lançamentos ou mais vendidos).
        *   **Email 2 (Dia 3 - Se não abriu o Email 1 OU não clicou): "Um presentinho para você voltar a nos visitar!"**
            *   **Objetivo**: Reforçar a oferta com senso de exclusividade.
            *   **Conteúdo**: Destaque para o benefício da oferta (desconto, frete grátis), mostrando produtos que podem ser comprados.
            *   **CTA**: "Resgatar Meu Desconto Agora" (link direto para uma página com o cupom aplicado ou para o carrinho).
        *   **Email 3 (Dia 7 - Se não abriu Email 1 ou 2 OU não clicou): "Última Chance: Seu presente expira em 24h!"**
            *   **Objetivo**: Criar urgência e converter.
            *   **Conteúdo**: Alerta de expiração da oferta, lembrete do valor e facilidade de uso do cupom.
            *   **CTA**: "Aproveitar Desconto Final" (link direto para a loja com o cupom pré-preenchido).

4.  **Configuração de Saída da Automação**:
    *   **Ação**: Garanta que o cliente seja removido da automação caso realize uma compra.
    *   **Exemplo**: Adicione um gatilho de saída "Se o cliente realizar uma compra". Isso evita que clientes já reativados recebam emails de "inativo".

### Workflow 2: Reativação de Assinantes Inativos para SaaS

Este workflow visa reengajar usuários de um serviço de assinatura (SaaS) que demonstraram inatividade em funcionalidades-chave ou que não utilizam o produto há um tempo, com o objetivo de demonstrar valor e evitar o cancelamento.

**Passos Detalhados:**

1.  **Detecção de Inatividade por Uso de Recurso**:
    *   **Ação**: Configure eventos de rastreamento na plataforma de análise (ex: Amplitude, Mixpanel) ou na própria ferramenta de automação.
    *   **Critério**: Usuários com assinatura ativa que não realizaram login nos últimos 30 dias OU não usaram uma funcionalidade crítica (ex: "Criar Relatório", "Publicar Post") nos últimos 15 dias.
    *   **Exemplo**: Segmento "Usuários de Risco" com filtro "Último login > 30 dias atrás" OU "Último uso da funcionalidade X > 15 dias atrás".

2.  **Análise de Motivos e Proposta de Valor**:
    *   **Ação**: Baseado em feedback anterior ou dados de uso, formule hipóteses para a inatividade (ex: dificuldade de uso, falta de conhecimento sobre recursos).
    *   **Proposta de Valor**: Não apenas um desconto, mas a oferta de uma solução ou valor adicional.
    *   **Exemplo de Oferta**: "Sessão gratuita de consultoria com um especialista", "Acesso a um novo recurso beta por 30 dias", "Upgrade gratuito para o próximo plano por um mês".

3.  **Criação da Sequência de E-mails Focada em Valor**:
    *   **Ferramenta**: Configure uma nova automação para o segmento "Usuários de Risco".
    *   **Estrutura da Sequência (Exemplo de 4 emails):**
        *   **Email 1 (Dia 0 - Entrada na Automação): "Sentimos sua falta! Podemos ajudar a otimizar [Nome da Funcionalidade Chave]?"**
            *   **Objetivo**: Reconectar, oferecer ajuda e relembrar o benefício central.
            *   **Conteúdo**: Personalização com o nome do usuário e menção a um recurso que talvez ele não esteja aproveitando.
            *   **CTA**: "Agendar uma Sessão de Ajuda Gratuita" (link para agendamento com o time de CS).
        *   **Email 2 (Dia 4 - Se não abriu o Email 1 OU não clicou): "Desbloqueie todo o potencial de [Nome do Produto] com este guia rápido!"**
            *   **Objetivo**: Fornecer conteúdo educacional e dicas práticas.
            *   **Conteúdo**: Destaque para um recurso subutilizado, com um link para um tutorial ou artigo de blog que mostre seu valor.
            *   **CTA**: "Ver Guia Agora" (link para artigo ou vídeo tutorial).
        *   **Email 3 (Dia 8 - Se não abriu Email 1 ou 2 OU não clicou): "Última Chance: Sua conta tem acesso a um benefício exclusivo!"**
            *   **Objetivo**: Apresentar a oferta de valor adicional com urgência.
            *   **Conteúdo**: Apresentação da oferta (ex: "Upgrade gratuito por 30 dias") e como ela resolve um problema comum ou gera mais valor.
            *   **CTA**: "Ativar meu Upgrade Gratuito" (link direto para a página de upgrade com o benefício aplicado).
        *   **Email 4 (Dia 12 - Se não abriu nenhum dos anteriores OU não clicou): "Feedback Importa: Como podemos melhorar [Nome do Produto] para você?"**
            *   **Objetivo**: Coletar feedback qualitativo e identificar a causa da inatividade, mesmo que não haja reativação.
            *   **Conteúdo**: Pesquisa rápida de feedback, com perguntas abertas sobre a experiência e sugestões.
            *   **CTA**: "Compartilhe seu Feedback" (link para pesquisa de 2 perguntas).

4.  **Integração com Suporte/CS**:
    *   **Ação**: Usuários que interagem com a oferta de consultoria são encaminhados diretamente para o time de Sucesso do Cliente.
    *   **Exemplo**: Após o agendamento da sessão, o CS recebe uma notificação com o histórico do usuário.

---

## Templates

### Template 1: E-mail de Reativação para E-commerce (Primeira Chamada)

```
Assunto: Sentimos sua falta! 💔 Temos novidades (e um presente!)

Olá [Nome do Cliente],

Faz um tempinho que não te vemos por aqui e sentimos sua falta! 😔

Muitas coisas incríveis chegaram na [Nome da Loja] desde a sua última visita. Novas coleções, produtos exclusivos e algumas promoções que você não vai querer perder.

Para te dar um empurrãozinho e celebrar seu retorno, preparamos um presente especial:

🎁 Use o cupom **VOLTEI15** e ganhe 15% de desconto na sua próxima compra acima de R$100! E tem mais: Frete Grátis para todo o Brasil.

É a oportunidade perfeita para descobrir o que há de novo e aproveitar seus favoritos.

👉 [Link para Categoria de Lançamentos ou Mais Vendidos]

Mal podemos esperar para te ver de volta!

Com carinho,
Equipe [Nome da Loja]
[Link para o Site da Loja]
[Link para Instagram da Loja]
```

### Template 2: E-mail de Reativação para SaaS (Oferta de Valor e Urgência)

```
Assunto: [Nome do Usuário], não perca seu acesso ao recurso [Nome do Recurso] - Última Chance!

Olá [Nome do Usuário],

Notamos que você não tem explorado totalmente o potencial do [Nome do Produto] ultimamente, e isso nos preocupou. Queremos garantir que você esteja extraindo o máximo valor da sua assinatura.

Identificamos que a funcionalidade "[Nome do Recurso Chave]" poderia ser um game-changer para [Benefício Específico do Recurso, ex: sua análise de dados, sua gestão de projetos]. Muitos de nossos clientes relatam um aumento de X% na produtividade ao utilizá-la.

Para te ajudar a redescobrir o [Nome do Produto] e experimentar o impacto de [Nome do Recurso Chave], temos uma oferta exclusiva que expira em 48 horas:

✨ Ative seu upgrade gratuito para o plano "Premium" por 30 dias! ✨

Com o plano Premium, você terá acesso ilimitado a:
- [Recurso Premium 1: ex: Relatórios Avançados]
- [Recurso Premium 2: ex: Suporte Prioritário]
- [Recurso Premium 3: ex: Integrações Exclusivas]

Não deixe essa oportunidade passar. Clique abaixo para ativar seu upgrade e ver como podemos impulsionar seus resultados:

🚀 [Botão: Ativar meu Upgrade Premium Gratuito Agora] (Link direto para a página de upgrade com o benefício aplicado)

Se precisar de ajuda ou tiver alguma dúvida, nossa equipe de suporte está pronta para te auxiliar.

Atenciosamente,
Time [Nome do Produto]
[Link para o Site do Produto]
```

---

## Checklist

- [X] Período de inatividade para segmentação definido (ex: 90 dias sem compra; 30 dias sem login).
- [X] Segmento de clientes inativos criado e validado na plataforma de automação.
- [X] Oferta de reengajamento (desconto, crédito, recurso extra, consultoria) selecionada e clara.
- [X] Sequência de 3 a 4 emails com conteúdo relevante, valor e CTAs claros desenvolvida.
- [X] Subject lines otimizadas para alta taxa de abertura e com gatilhos de curiosidade/urgência.
- [X] Exclusão automática de clientes que reativam da sequência em andamento configurada.
- [X] Links dos emails testados e direcionando corretamente para páginas de destino (landing pages, carrinho).
- [X] Teste A/B planejado para subject lines, horários de envio ou tipos de oferta.
- [X] Dashboard de monitoramento de métricas (TO, TC, Reativação, Receita) configurado.
- [X] Plano de follow-up para clientes que não reativaram após a sequência inicial.

---

## Métricas de Referência

| Métrica               | Benchmark (Indústria) | Meta (Win Back) |
|-----------------------|-----------------------|-----------------|
| Taxa de Abertura (TO) | 15-25%                | 20-30%          |
| Taxa de Cliques (TC)  | 1-3%                  | 2-5%            |
| Taxa de Reativação    | 0.5-2%                | 1-3%            |
| Receita Atribuída     | Variável              | > Custo Campanha|
| Custo por Reativação  | Variável              | < LTV Cliente   |
| Taxa de Churn Reduzida| 0.2-1% (impacto)      | 0.5-1.5%        |

---

## Erros Comuns

1.  **Oferta Irrelevante ou Inexistente**: Enviar emails de "sentimos sua falta" sem um incentivo tangível ou uma proposta de valor clara.
    *   **Como evitar**: Sempre inclua uma oferta irresistível (desconto significativo, frete grátis, acesso premium, serviço gratuito) que justifique o retorno do cliente e que seja relevante para seu histórico de compras/uso. Exemplo: para um cliente que comprava eletrônicos, um desconto em acessórios eletrônicos.
2.  **Sequência Única e Estática para Todos os Inativos**: Tratar todos os clientes inativos da mesma forma, ignorando o tempo de inatividade, o valor do cliente ou o motivo provável da inatividade.
    *   **Como evitar**: Segmente ainda mais os inativos. Crie fluxos diferentes para inativos de 30, 90 e 180 dias. Clientes VIP inativos podem receber uma oferta mais agressiva ou contato personalizado. Usuários de SaaS inativos por funcionalidade podem receber tutoriais específicos.
3.  **Não Remover Reativados da Sequência**: Continuar enviando emails de "win back" para clientes que já fizeram uma nova compra ou voltaram a usar o serviço.
    *   **Como evitar**: Configure gatilhos de saída claros na sua automação. Se um cliente realizar uma compra ou efetuar login (no caso de SaaS) após entrar na sequência, ele deve ser automaticamente removido e não receber os emails subsequentes. Isso evita irritação e mantém a comunicação relevante.

---

## Dicas Avançadas

1.  **Personalização Multicanal e Preditiva**: Além do email, considere integrar SMS para inativos de alto valor ou notificações push para usuários de aplicativo. Use modelos preditivos para identificar clientes com maior probabilidade de inatividade ANTES que ela ocorra, enviando ofertas de retenção proativas.
2.  **Testes A/B/n Robustos em Ofertas e Períodos**: Não teste apenas subject lines. Faça testes extensivos com diferentes ofertas (ex: 10% vs 15% vs frete grátis), diferentes intervalos de tempo entre emails (3, 5, 7 dias) e diferentes durações da campanha para maximizar a taxa de reativação.
3.  **Análise da Causa Raiz da Inatividade com Pesquisas**: No último email da sequência (ou como um follow-up para quem não reativou), inclua uma pesquisa rápida ("Por que você parou de usar?", "O que poderíamos ter feito diferente?"). Use ferramentas como Typeform ou Google Forms. Os insights coletados são cruciais para refinar o produto ou serviço e prevenir futuras inatividades.
4.  **Recuperação de Carrinho Abandonado Otimizada para Inativos**: Se um cliente inativo retornar ao site e abandonar um carrinho, ative uma sequência de recuperação de carrinho com uma oferta ainda mais agressiva ou um senso de urgência maior, já que o interesse foi demonstrado novamente.
5.  **Segmentação por Tipo de Produto/Serviço Consumido Anteriormente**: Para e-commerce, se o cliente costumava comprar uma categoria específica (ex: maquiagem), direcione a oferta de win-back para produtos dessa categoria ou lançamentos relacionados, aumentando a relevância e a chance de conversão.