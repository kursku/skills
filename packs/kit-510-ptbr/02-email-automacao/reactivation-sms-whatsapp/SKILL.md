---
name: reactivation-sms-whatsapp
description: "Reactivation Sms Whatsapp — Skill especializada para reactivation sms whatsapp"
license: MIT
metadata:
  version: 1.0.0
  author: Cafe Code AI
  category: 02-email-automacao
  updated: 2026-03-01
risk: safe
---

# Reactivation Sms Whatsapp

Esta skill fornece um guia prático e acionável para criar e executar campanhas de reativação de clientes via SMS e WhatsApp, focando em clientes inativos ou com carrinho abandonado.

---

## Keywords

reativação de clientes, SMS marketing, WhatsApp marketing, abandono de carrinho, automação de mensagens, clientes inativos, segmentação de inativos, jornada do cliente, ofertas de reengajamento, recuperação de vendas, opt-in para mensagens, LGPD para marketing direto.

---

## Quick Start

1.  **Identificar Segmento de Inativos**: Selecione clientes que não realizaram compras nos últimos 90 dias ou que abandonaram um carrinho há mais de 48 horas.
2.  **Criar Oferta Irresistível**: Desenvolva uma oferta de alto valor percebido, como "20% OFF + Frete Grátis" ou "Brinde exclusivo na próxima compra".
3.  **Redigir Mensagens Diretas**: Crie mensagens concisas para SMS (até 160 caracteres) e WhatsApp (com emojis e um CTA claro), focando na oferta e na urgência.
4.  **Configurar Automação**: Implemente a sequência de mensagens na plataforma de automação (ex: Twilio, Zenvia, Manychat) com gatilhos e delays específicos.
5.  **Testar e Monitorar**: Envie testes para um grupo restrito e acompanhe as métricas de entrega, abertura, cliques e conversão em tempo real para otimização contínua.

---

## Core Workflows

### Workflow 1: Reativação de Clientes Inativos (90+ dias) com Oferta Estratégica

Este workflow é ideal para trazer de volta clientes que não interagem ou compram há um período significativo, aproveitando o baixo custo e alta taxa de abertura de SMS/WhatsApp.

**Passos Detalhados:**

1.  **Segmentação de Base**:
    *   **Critério Principal**: Clientes sem nenhuma compra nos últimos 90 dias.
    *   **Critério Secundário (Refinamento)**: Clientes que, apesar de inativos, abriram ao menos 3 e-mails ou visitaram o site 2+ vezes nos últimos 6 meses (demonstrando algum interesse latente). Exclua clientes que se descadastraram ou bloquearam comunicações anteriores.
    *   **Exemplo**: "Segmentar clientes que compraram pela última vez há mais de 90 dias, mas que possuem um histórico de LTV (Lifetime Value) acima de R$300 e não estão na lista de bloqueio de SMS."

2.  **Definição da Oferta**:
    *   **Objetivo**: Criar um incentivo forte o suficiente para quebrar a inércia.
    *   **Tipos de Oferta**: Desconto progressivo (ex: 15% na primeira compra, 20% na segunda), frete grátis, brinde exclusivo, acesso antecipado a lançamentos.
    *   **Exemplo**: "Oferta de 20% de desconto na próxima compra, cumulativo com frete grátis para compras acima de R$150. Validade de 72 horas para gerar urgência."

3.  **Criação da Mensagem e Sequência (SMS -> WhatsApp Fallback)**:
    *   **Dia 0 - Mensagem SMS (Primeira Tentativa)**:
        *   **Conteúdo**: Direto, com oferta clara e link rastreável.
        *   **Exemplo**: "Sentimos sua falta na [NomeEmpresa]! 😔 Use o cupom VOLTE20 e ganhe 20% OFF + frete grátis na sua proxima compra. Valido por 72h! 👉 [LinkOfertaPersonalizado]"
        *   **Link**: Use um encurtador de URL com rastreamento (ex: Bitly, utm_source=sms_reativacao, utm_medium=sms, utm_campaign=inativos90dias).
    *   **Dia 2 - Mensagem WhatsApp (Se SMS não gerar clique/conversão)**:
        *   **Gatilho**: Cliente que recebeu o SMS, mas não clicou no link nem realizou a compra em 48 horas.
        *   **Conteúdo**: Mais pessoal, com emojis e reforçando a oferta e a urgência.
        *   **Exemplo**: "Oi [NomeCliente], tudo bem? 👋 Vimos que vc deixou de aproveitar o desconto de 20% + frete grátis na [NomeEmpresa]! Seu cupom VOLTE20 ainda esta ativo por mais 24h. Nao perca! 😉 [LinkOfertaPersonalizado]"
        *   **Consentimento**: Certifique-se de que o cliente deu consentimento prévio para receber mensagens via WhatsApp.

4.  **Automação e Agendamento**:
    *   Configure a automação para disparar o SMS no Dia 0, geralmente entre 10h e 17h (horário local do cliente).
    *   Crie uma condição para aguardar 48 horas. Se o cliente não clicou no link do SMS ou não converteu, disparar a mensagem de WhatsApp.
    *   Use um período de "do not disturb" para não enviar mensagens de madrugada.

### Workflow 2: Recuperação de Carrinho Abandonado Imediata via WhatsApp

Este workflow foca em clientes com alta intenção de compra, usando a agilidade do WhatsApp para converter rapidamente carrinhos abandonados.

**Passos Detalhados:**

1.  **Gatilho de Abandono**:
    *   **Condição**: Um cliente adiciona produtos ao carrinho e abandona a sessão por mais de 60 minutos (ou 30 minutos para produtos de alta demanda/estoque limitado) sem finalizar a compra.
    *   **Critério de Valor**: Apenas para carrinhos com valor total acima de R$100 para otimizar o ROI da campanha.
    *   **Exemplo**: "Disparar automação quando o valor do carrinho for >= R$120 e o cliente permanecer inativo por 45 minutos após adicionar o último item."

2.  **Primeira Mensagem de Lembrete (1 hora após abandono)**:
    *   **Objetivo**: Lembrete amigável e direto, oferecendo um pequeno incentivo para finalizar.
    *   **Conteúdo**:
        *   **Exemplo**: "Olá [NomeCliente], seus itens incríveis da [NomeEmpresa] ainda estão te esperando! ✨ Complete sua compra agora em [LinkCarrinhoPersonalizado] e ganhe 5% OFF com o cupom CARRINHO5. Não perca! 😉"
        *   **Link**: Direto para o carrinho do cliente, preenchido com os itens abandonados.
    *   **Atenção**: Esteja ciente das políticas do WhatsApp Business sobre mensagens transacionais vs. promocionais. Mensagens de recuperação de carrinho com desconto podem ser consideradas promocionais.

3.  **Segunda Mensagem de Urgência (24 horas após abandono, se não houver conversão)**:
    *   **Gatilho**: Cliente que recebeu a primeira mensagem de WhatsApp, mas não finalizou a compra em 24 horas.
    *   **Objetivo**: Reforçar a urgência e o valor dos itens, ou adicionar um incentivo um pouco maior.
    *   **Conteúdo**:
        *   **Exemplo**: "Ei [NomeCliente], seus produtos de decoração 🛋️ estão quase esgotando! Não deixe para depois. Use seu cupom CARRINHO5 para 5% OFF e finalize sua compra em [LinkCarrinhoPersonalizado] antes que seja tarde! ⏳"
        *   **Variação de Oferta**: Para carrinhos de alto valor, considere aumentar o desconto para 10% ou oferecer frete grátis se o cliente não respondeu à primeira.

4.  **Automação e Agendamento**:
    *   Configure a automação para disparar a primeira mensagem 60 minutos após o abandono.
    *   Crie uma condição para aguardar 24 horas. Se o cliente não converteu, disparar a segunda mensagem.
    *   Utilize um intervalo de tempo para envio (ex: 9h às 20h) para evitar mensagens fora de hora.

---

## Templates

### SMS de Reativação com Oferta de Desconto

```
Olá [NomeCliente], seu café favorito te espera! ☕ Use o cupom CAFEVOLTA e ganhe 15% OFF na sua proxima compra de graos especiais na [NomeEmpresa]. Valido por 48h! 👉 [LinkOferta]
```

### WhatsApp de Recuperação de Carrinho com Urgência

```
Oi [NomeCliente], seus livros📚 estão quase esgotando! Vimos que vc deixou alguns no carrinho. Finalize sua compra em [LinkCarrinho] em ate 12h e garanta seus titulos antes que esgotem. Nao perca!
```

---

## Checklist

- [x] Segmentar clientes inativos por tempo (ex: 90+ dias sem compra) e engajamento prévio.
- [x] Definir oferta de reativação (ex: desconto progressivo, frete grátis, brinde) com validade clara.
- [x] Criar copy de SMS concisa e impactante (máx. 160 caracteres), com CTA e link rastreável.
- [x] Criar copy de WhatsApp mais pessoal, com emojis, CTA claro e link direto para o carrinho/oferta.
- [x] Garantir que todos os links de ofertas e carrinhos estejam funcionando e sejam personalizados.
- [x] Verificar e obter consentimento explícito dos clientes para envio de mensagens via WhatsApp (LGPD).
- [x] Configurar automação com gatilhos de tempo e comportamento para SMS e WhatsApp.
- [x] Realizar testes de envio para garantir que as mensagens, links e cupons funcionem perfeitamente.
- [x] Monitorar métricas de entrega, abertura, cliques (CTR) e conversão em tempo real.
- [x] Ter um plano de contingência para gerenciar respostas e dúvidas recebidas via WhatsApp.

---

## Métricas de Referência

| Métrica                      | Benchmark (Indústria) | Meta (para Campanhas de Reativação) |
|------------------------------|-----------------------|-------------------------------------|
| Taxa de Entrega SMS          | 95-98%                | > 97%                               |
| Taxa de Abertura WhatsApp    | 70-90%                | > 80%                               |
| Taxa de Cliques SMS (CTR)    | 5-10%                 | > 8%                                |
| Taxa de Cliques WhatsApp (CTR)| 15-30%                | > 20%                               |
| Taxa de Conversão Reativação | 2-5%                  | > 3%                                |
| Custo por Reativação (CPR)   | < 20% do LTV médio    | < 15% do LTV médio                  |

---

## Erros Comuns

1.  **Mensagens Genéricas sem Oferta Clara**: Enviar "Sentimos sua falta, volte a comprar!" sem um incentivo concreto.
    *   **Como evitar**: Sempre inclua uma oferta irresistível e explícita. Em vez de "Volte a comprar conosco", diga "Use CUPOM20OFF e ganhe 20% OFF na sua próxima compra de vinhos!".
2.  **Ignorar Consentimento e Políticas de Mensageria**: Enviar WhatsApp para quem não optou ou usar templates que violam as políticas do WhatsApp Business.
    *   **Como evitar**: Certifique-se de que o cliente deu consentimento explícito (opt-in) para receber mensagens via WhatsApp. Utilize templates aprovados pelo WhatsApp ou restrinja o conteúdo promocional a notificações.
3.  **Links Quebrados ou Cupons Inválidos**: Disparar uma campanha em massa com um link que não funciona ou um código de cupom que não é reconhecido.
    *   **Como evitar**: Sempre teste o link e o cupom em um ambiente de teste ou com um pequeno grupo de usuários internos antes do disparo oficial da campanha. Verifique a validade e a URL de destino.
4.  **Frequência Excessiva de Mensagens**: Bombardear o cliente com múltiplas mensagens de reativação em um curto espaço de tempo.
    *   **Como evitar**: Respeite intervalos mínimos entre as mensagens (ex: 48h para carrinho, 7 dias para inativos). Use automações para controlar a frequência e evitar sobrecarga de comunicação.

---

## Dicas Avançadas

1.  **Personalização Dinâmica por Histórico de Compra**: Use dados do último produto comprado ou categoria preferida para tornar a oferta ultra-relevante.
    *   **Exemplo**: Para um cliente que comprou câmeras, "Olá [NomeCliente], suas fotos pedem uma nova lente! 📸 Temos 15% OFF nas lentes que você ama. [LinkOfertaLentes]".
2.  **Testes A/B Multivariados e Segmentação de Ofertas**: Não teste apenas o texto, mas também o tipo de oferta (desconto vs. frete grátis vs. brinde) e o timing do envio para diferentes segmentos.
    *   **Exemplo**: Segmentar clientes de alto LTV para receber "Frete Grátis + Brinde Exclusivo" e clientes de LTV médio para "20% OFF", e comparar as taxas de conversão.
3.  **Automação Multi-canal com Fallback Inteligente**: Comece com o canal de maior engajamento (WhatsApp, se consentido). Se não houver resposta em X horas, tente SMS. Se ainda não houver resposta, envie um e-mail.
    *   **Exemplo**: "Se cliente não abrir WhatsApp em 6h, disparar SMS. Se SMS não tiver clique em 24h, enviar e-mail com a mesma oferta, mas um assunto diferente."
4.  **Análise Preditiva de Churn para Reativação Proativa**: Integre com modelos de Machine Learning que preveem clientes com alta probabilidade de se tornarem inativos ANTES que o churn ocorra.
    *   **Exemplo**: Clientes identificados com 80% de chance de churn nos próximos 30 dias recebem uma campanha de "engajamento proativo" via WhatsApp com conteúdo exclusivo ou oferta de "mimo".
5.  **Utilização de Rich Media no WhatsApp para Engajamento**: Além de texto, explore o envio de imagens (banners de oferta), GIFs ou pequenos vídeos que mostram os produtos ou o benefício da oferta.
    *   **Exemplo**: Em uma recuperação de carrinho de roupas, envie um GIF de uma modelo vestindo um dos itens do carrinho com a legenda "Essa peça te esperando! ✨".