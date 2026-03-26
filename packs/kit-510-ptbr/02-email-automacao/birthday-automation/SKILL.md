---
name: birthday-automation
description: "Birthday Automation — Skill especializada para birthday automation"
license: MIT
metadata:
  version: 1.0.0
  author: Cafe Code AI
  category: 02-email-automacao
  updated: 2026-03-01
risk: safe
---

# Birthday Automation

Esta skill capacita o Claude a projetar, implementar e otimizar campanhas de email automatizadas para aniversariantes, focando em engajamento e conversão.

---

## Keywords

automação aniversário, email marketing, CRM, segmentação data, fluxo de email, oferta exclusiva, voucher aniversário, engajamento cliente, personalização, jornada do cliente, celebração, gatilho data.

---

## Quick Start

1.  Confirmar a existência e o formato padronizado do campo `data_nascimento` no CRM.
2.  Configurar o gatilho da automação para disparar 7 dias antes ou no dia do aniversário.
3.  Elaborar um mínimo de três emails específicos: pré-aniversário, dia do aniversário e pós-aniversário.
4.  Criar um voucher ou oferta exclusiva e dinâmica, com validade definida para o período da campanha.
5.  Realizar um teste completo da jornada do cliente, utilizando um contato de teste com data de aniversário próxima.

---

## Core Workflows

### Workflow 1: Implementação de Sequência de Aniversário com Oferta Exclusiva

Este workflow detalha a criação de uma campanha de aniversário automatizada, desde a preparação dos dados até o disparo da sequência de emails com um benefício exclusivo.

*   **Passo 1: Preparação de Dados e Segmentação no CRM**
    Garanta que o campo `data_nascimento` (ou equivalente) esteja presente em seu sistema de CRM/automação de marketing (ex: ActiveCampaign, RD Station, HubSpot) e que os dados estejam em um formato consistente (preferencialmente `AAAA-MM-DD` ou `MM-DD`). Crie um segmento dinâmico que identifique os contatos cuja data de aniversário seja nos próximos 7 dias ou no dia atual.
    *   _Exemplo Concreto:_ No ActiveCampaign, configure um segmento "Aniversariantes Próximos" com a condição "Data de Aniversário é nos próximos 7 dias". No RD Station, utilize "Data de Aniversário é igual a hoje" para o email do dia D e "Data de Aniversário é em 7 dias" para o email de pré-aniversário.

*   **Passo 2: Configuração do Gatilho e Estrutura da Automação**
    Crie uma automação que se inicia 7 dias antes do aniversário do contato. Defina os passos sequenciais para os disparos de email.
    *   _Exemplo Concreto:_
        *   **Gatilho:** "Data de Aniversário - 7 dias antes".
        *   **Ação 1 (D-7):** Enviar Email 1 (Pré-aniversário - "Contagem Regressiva").
        *   **Ação 2 (D-3):** Aguardar 4 dias.
        *   **Ação 3 (D-0):** Enviar Email 2 (Dia do Aniversário - "Presente Exclusivo").
        *   **Ação 4 (D+7):** Aguardar 7 dias.
        *   **Ação 5 (D+7):** Enviar Email 3 (Pós-aniversário - "Última Chance").
        *   **Condição de Saída:** Se o contato realizar uma compra utilizando o cupom de aniversário, ele deve sair da automação para evitar emails irrelevantes.

*   **Passo 3: Criação da Oferta e Geração de Voucher Dinâmico**
    Defina a oferta de aniversário (ex: 15% de desconto, frete grátis, brinde). Utilize plataformas de e-commerce (ex: Shopify, WooCommerce) ou de cupons (ex: Vindi) para gerar códigos de voucher dinâmicos e rastreáveis.
    *   _Exemplo Concreto:_ Crie um cupom `ANIVER15` que oferece 15% de desconto em todo o site, válido por 15 dias. Se sua plataforma permitir, gere um cupom único por cliente (ex: `ANIVER_{{contact.id}}`) para rastreamento individual e para evitar uso indevido. Crie um link que já aplique o cupom automaticamente na loja (ex: `www.suaempresa.com.br/carrinho?coupon=ANIVER15`).

*   **Passo 4: Design e Conteúdo dos Emails Personalizados**
    Elabore os três emails com foco em personalização, utilizando placeholders como `{{contact.first_name}}`.

    *   _Exemplo (Assunto Email 2 - Dia do Aniversário):_ 🎉 Feliz Aniversário, {{contact.first_name}}! Seu presente especial te espera!
    *   _Exemplo (Corpo Email 2):_ Olá {{contact.first_name}}, a equipe da [Nome da Empresa] deseja a você um dia espetacular! Para celebrar, presenteamos você com 15% de desconto em todo o nosso site. Use o código **ANIVER15** aqui: [link do site com cupom pré-aplicado]. Válido por 15 dias.

*   **Passo 5: Teste Completo e Monitoramento**
    Antes de ativar, envie a sequência para um email de teste configurado com uma data de aniversário próxima. Verifique todos os links, a aplicação do cupom e a personalização. Após o lançamento, monitore continuamente as métricas de abertura, cliques, resgate da oferta e receita atribuída.

### Workflow 2: Recuperação de Carrinho para Aniversariantes com Oferta Ativa

Este workflow foca em reengajar aniversariantes que receberam a oferta, abandonaram um carrinho e ainda não converteram, maximizando o uso do benefício.

*   **Passo 1: Identificação de Carrinhos Abandonados e Status da Oferta**
    Integre sua plataforma de e-commerce com o sistema de automação para identificar contatos que abandonaram um carrinho. Ao mesmo tempo, monitore o status da oferta de aniversário: se o cupom foi gerado, enviado e se ainda é válido, e se o cliente já realizou uma compra com ele.
    *   _Exemplo Concreto:_ Configure um webhook do Shopify que envia eventos de carrinho abandonado para o HubSpot. No HubSpot, crie uma propriedade personalizada `cupom_aniversario_usado` (true/false) e `data_validade_cupom`.

*   **Passo 2: Segmentação de Aniversariantes Não Convertidos com Carrinho Abandonado**
    Crie um segmento altamente específico que inclua contatos que: 1) estão na automação de aniversário, 2) receberam o email de oferta, 3) abandonaram um carrinho nas últimas 24-48 horas, 4) não realizaram uma compra com o cupom de aniversário, e 5) o cupom ainda está dentro do período de validade.
    *   _Exemplo Concreto:_ Segmento "Aniversariantes C.A. com Oferta Ativa": (Está na automação "Aniversário" E Recebeu email "Dia do Aniversário" E Abandonou carrinho nos últimos 2 dias E `cupom_aniversario_usado` é Falso E `data_validade_cupom` é Maior que Hoje).

*   **Passo 3: Criação de Email de Recuperação Otimizado**
    Desenvolva um email de recuperação de carrinho que lembre o aniversariante tanto do carrinho abandonado quanto da oferta de aniversário exclusiva. O tom deve ser de ajuda e lembrete, não de cobrança.
    *   _Exemplo Concreto:_
        *   **Assunto:** Seu presente de aniversário ainda te espera, {{contact.first_name}}! (E seu carrinho também!)
        *   **Corpo:** Olá {{contact.first_name}}, notamos que você deixou alguns itens incríveis no seu carrinho. Lembramos que seu presente de aniversário – 15% OFF com o código ANIVER15 – ainda está ativo! Não perca a chance de usar seu desconto. Conclua sua compra agora: [link para o carrinho recuperado].

*   **Passo 4: Automação de Recuperação Condicional**
    Crie uma automação separada para recuperação de carrinho. Adicione uma condição para que este email específico seja disparado apenas para o segmento "Aniversariantes C.A. com Oferta Ativa". O disparo deve ocorrer aproximadamente 24 horas após o abandono do carrinho. Inclua uma condição de saída caso o contato finalize a compra.
    *   _Exemplo Concreto:_ Gatilho: "Contato abandonou carrinho". Condição: "Contato pertence ao segmento 'Aniversariantes C.A. com Oferta Ativa'". Ação: "Aguardar 24 horas". Ação: "Enviar Email de Recuperação de Aniversário". Condição de Saída: "Fez uma compra".

*   **Passo 5: Análise de Desempenho e Iteração**
    Monitore a taxa de abertura, cliques e, crucialmente, a taxa de recuperação de carrinho para este segmento específico de aniversariantes. Compare com a taxa de recuperação geral de carrinhos para avaliar a eficácia da oferta de aniversário como um impulsionador. Ajuste o texto do email, o timing ou até mesmo a oferta se os resultados não forem satisfatórios.

---

## Templates

### Email de Aniversário com Oferta Exclusiva (Dia D)

```
Assunto: 🎉 Feliz Aniversário, {{contact.first_name}}! Seu presente especial está aqui!

Olá {{contact.first_name}},

A equipe da [Nome da Sua Empresa] quer celebrar um dia muito especial: O SEU ANIVERSÁRIO!

Esperamos que seu dia seja repleto de alegria e momentos inesquecíveis. Para deixar tudo ainda melhor, temos um presente exclusivo para você:

🎁 **15% DE DESCONTO** em qualquer produto do nosso site!

É a nossa forma de agradecer por fazer parte da nossa comunidade. Use o código abaixo no checkout:

**ANIVER15**

Clique aqui para resgatar seu presente agora:
[Link para o Site com cupom pré-aplicado, ex: www.suaempresa.com.br/aniversario?coupon=ANIVER15]

*Válido por 15 dias a partir de hoje. Não cumulativo com outras promoções.*

Um abraço e um feliz aniversário,
A Equipe [Nome da Sua Empresa]
[Link para o Blog da Empresa] | [Link para Instagram] | [Link para Facebook]
[Endereço da Empresa]
```

### Email de Pré-Aniversário (D-7)

```
Assunto: 🎂 Contagem regressiva para seu dia especial, {{contact.first_name}}!

Olá {{contact.first_name}},

Falta apenas uma semana para o seu aniversário! Por aqui, já estamos animados para celebrar essa data tão importante.

Fique de olho na sua caixa de entrada no dia {{contact.birthday_day}}/{{contact.birthday_month}}, pois teremos uma surpresa especial e exclusiva para você.

Enquanto isso, que tal dar uma olhada nas nossas novidades e já ir montando sua lista de desejos?

[Link para Lançamentos/Promoções]

Estamos ansiosos para celebrar com você!

Com carinho,
A Equipe [Nome da Sua Empresa]
```

---

## Checklist

- [x] Campo `data_nascimento` configurado e preenchido no CRM.
- [x] Formato de data padronizado (`AAAA-MM-DD` ou `MM-DD`) em todos os registros.
- [x] Segmento de aniversariantes criado e atualizado automaticamente para o período da automação.
- [x] Gatilho da automação configurado para disparar na data correta (D-7, D-0, D+7).
- [x] Emails da sequência (pré, dia, pós) com conteúdo personalizado e relevante.
- [x] Oferta de aniversário (voucher/desconto) criada, validada e com regras claras.
- [x] Link de resgate da oferta funcionando e testado em diferentes dispositivos.
- [x] Condições de saída da automação (ex: após compra com cupom) configuradas e ativas.
- [x] Rastreamento de conversão da campanha de aniversário ativado e integrado com analytics.
- [x] Teste completo da jornada do cliente aniversariante, do email ao checkout.

---

## Métricas de Referência

| Métrica                         | Benchmark (Indústria) | Meta (para otimização) |
|---------------------------------|-----------------------|------------------------|
| Taxa de Abertura (Emails Aniv.) | 25-35%                | 30%                    |
| Taxa de Clique (CTR)            | 5-10%                 | 8%                     |
| Taxa de Conversão (Resgate Oferta) | 8-15%                 | 10%                    |
| Receita Atribuída por Email (RPE) | R$0.50 - R$2.00       | R$1.20                 |
| Lifetime Value (LTV) Aniversariantes | 15-25% maior que não aniversariantes | 20% maior |

---

## Erros Comuns

1.  **Dados de Aniversário Incompletos ou Inconsistentes**: Falta do campo `data_nascimento` ou dados em formatos variados (ex: `DD/MM/AAAA`, `MM-DD`, `AAAA-MM-DD`) que impedem a segmentação correta.
    *   **Como evitar**: Implementar validação rigorosa na coleta de dados (formulários, onboarding) e realizar rotinas de limpeza e padronização periódica no CRM. Prefira o formato ISO 8601 (`AAAA-MM-DD`) para consistência.

2.  **Oferta Genérica ou Não Atraente**: Proporcionar um desconto insignificante (ex: 5% OFF) ou uma oferta que não se alinha ao histórico de compras ou preferências do cliente.
    *   **Como evitar**: Ofereça um benefício real e perceptível (ex: 15-20% OFF, frete grátis, brinde com valor agregado). Se possível, utilize dados de compra anteriores para personalizar a oferta para categorias de produtos que o cliente já demonstrou interesse.

3.  **Timing Inadequado do Disparo**: Enviar o email do dia do aniversário muito cedo (ex: 00:01h) ou muito tarde, perdendo o impacto do momento, ou disparar a oferta após a data de validade.
    *   **Como evitar**: Programe o email do dia D para ser enviado entre 9h e 11h da manhã, quando a maioria das pessoas já está ativa e verificando emails. Implemente emails de pré-aniversário (D-7) e pós-aniversário (D+7) como lembretes, garantindo que a validade da oferta cubra todo o período da comunicação.

---

## Dicas Avançadas

1.  **Segmentação Preditiva por Valor de LTV**: Utilize modelos preditivos para identificar aniversariantes com alto potencial de Lifetime Value (LTV). Para esses clientes, ofereça um bônus ainda mais exclusivo (ex: 25% OFF + frete grátis, acesso antecipado a lançamentos ou um presente físico simbólico) para reforçar a lealdade e maximizar o ROI.

2.  **Multi-canalidade na Celebração**: Vá além do email. No dia do aniversário, envie um SMS personalizado com um lembrete do voucher ou uma notificação push no aplicativo da sua marca. "Feliz Aniversário, {{contact.first_name}}! Seu desconto de 15% te espera no app. Não perca!". Isso aumenta a visibilidade e a chance de resgate.

3.  **Gatilho de Engajamento Pós-Aniversário Condicional**: Se o cliente usou a oferta, acione uma automação de agradecimento com sugestões de produtos complementares. Se não usou, configure um último lembrete "Última chance de usar seu presente!" 2 dias antes do vencimento do cupom, criando um senso de urgência sem ser agressivo.

4.  **Pesquisa de Satisfação Pós-Resgate**: Após a compra com o voucher de aniversário, envie um email pedindo feedback sobre a experiência de compra e a usabilidade do desconto. Isso não só mostra que você valoriza a opinião do cliente, mas também fornece insights valiosos para otimização futura da campanha e identificação de dores.

5.  **Gamificação da Oferta de Aniversário**: Em vez de um desconto direto, crie uma experiência interativa no site onde o aniversariante pode "ganhar" seu desconto (ex: um "raspadinha virtual" ou "girar a roleta" para 10%, 15% ou 20% OFF). Isso aumenta o engajamento, a percepção de valor e a diversão, tornando a oferta mais memorável.