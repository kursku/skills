---
name: referral-email
description: "Referral Email — Skill especializada para referral email"
license: MIT
metadata:
  version: 1.0.0
  author: Cafe Code AI
  category: 02-email-automacao
  updated: 2026-03-01
risk: safe
---

# Referral Email

Esta skill capacita o Claude a criar e otimizar sequências de email de indicação altamente eficazes, transformando clientes satisfeitos em promotores ativos da marca.

---

## Keywords

Email de indicação, programa de referência, referral marketing, boca a boca digital, viralização, automação de indicação, incentivos, recompensas, embaixadores da marca, NPS, cliente satisfeito, funil de indicação, programa de fidelidade.

---

## Quick Start

1.  Segmentar base de clientes: Filtrar promotores (NPS 9-10) ou clientes com engajamento consistente por mais de 6 meses e LTV acima da média.
2.  Definir estrutura de incentivos: Determinar a recompensa para o indicador (ex: R$50 de crédito) e para o indicado (ex: 15% de desconto na primeira compra).
3.  Configurar gatilho da automação: Iniciar sequência de email de indicação 7 dias após uma compra bem-sucedida ou a conclusão de um marco de engajamento.
4.  Desenvolver landing page de resgate: Criar uma página exclusiva para o indicado inserir seu código ou email e receber a oferta, garantindo rastreamento preciso.
5.  Implementar sistema de rastreamento: Garantir que cada indicação seja registrada, seu status atualizado e a recompensa do indicador seja distribuída automaticamente após a conversão.

---

## Core Workflows

### Workflow 1: Automação de Convite para Indicação Pós-Experiência Positiva

Este workflow foca em convidar clientes que demonstraram satisfação recente para se tornarem promotores, aproveitando o pico de engajamento e contentamento.

**Passos detalhados:**

1.  **Gatilho da Automação**: Um cliente realiza uma compra e, após 7 dias da entrega do produto ou da conclusão do serviço, não registra nenhuma reclamação ou, alternativamente, responde a uma pesquisa de satisfação com NPS 9 ou 10.
2.  **Segmentação**: Apenas clientes que se encaixam no perfil de "promotor" (NPS 9-10) ou com histórico de alto LTV (Lifetime Value) e múltiplas interações positivas com a marca. Excluir clientes com histórico de suporte recente ou insatisfação.
3.  **Email 1 (Convite para Indicação)**: Enviado 7 dias após o gatilho.
    *   **Assunto**: "Amamos ter você! Que tal compartilhar essa experiência e ser recompensado?" ou "Sua opinião é valiosa! Que tal transformá-la em benefício para você e seus amigos?"
    *   **Corpo**:
        *   Personalização: "Olá, [Nome do Cliente],"
        *   Agradecimento e Reconhecimento: "Sua satisfação é nossa prioridade e ficamos muito felizes em saber que você teve uma ótima experiência com [Nome do Produto/Serviço]."
        *   Introdução ao Programa: "Sabemos que você adora [Nome da Sua Marca] e pensamos: por que não compartilhar essa paixão e ainda ser recompensado por isso?"
        *   Detalhes do Incentivo (Indicador): "Indique um amigo e, quando ele fizer a primeira compra, você ganha R$50 de crédito para usar em sua próxima compra."
        *   Detalhes do Incentivo (Indicado): "Seu amigo também ganha! Ele receberá 15% de desconto na primeira compra."
        *   CTA Claro: "É simples! Clique aqui para gerar seu link de indicação exclusivo e começar a compartilhar: [Link para Landing Page de Indicação]"
        *   Informações Adicionais: "Você pode acompanhar suas indicações e recompensas diretamente em seu painel."
4.  **Email 2 (Lembrete - Se não clicou no Email 1)**: Enviado 3 dias após o Email 1, caso o cliente não tenha aberto ou clicado no link de indicação.
    *   **Assunto**: "Não perca a chance de presentear um amigo (e a si mesmo!)" ou "Seu link de indicação exclusivo te espera!"
    *   **Corpo**: Reafirma os benefícios de forma concisa e reforça o CTA. "Sabemos que a vida é corrida, mas queríamos lembrar você da oportunidade de presentear seus amigos com [Desconto/Benefício] em [Nome da Sua Marca] e ainda ser recompensado com R$50 de crédito!"
5.  **Email 3 (Última Chamada - Se não clicou no Email 1 ou 2, e há prazo)**: Enviado 7 dias após o Email 1, se o programa tiver um prazo ou se o incentivo for limitado.
    *   **Assunto**: "Última chance: Compartilhe [Nome da Sua Marca] e ganhe sua recompensa!"
    *   **Corpo**: Cria senso de urgência. "Esta é a sua última oportunidade para aproveitar nossa oferta especial de indicação. O benefício de R$50 de crédito para você e 15% de desconto para seu amigo expira em [Data/Prazo]."

### Workflow 2: Sequência de Follow-up e Notificação de Recompensa por Indicação Convertida

Este workflow garante que o indicador seja constantemente atualizado sobre o status de suas indicações e receba sua recompensa de forma transparente.

**Passos detalhados:**

1.  **Gatilho da Automação**: Um amigo indicado pelo cliente realiza a primeira compra, convertendo-se em um novo cliente.
2.  **Email 1 (Confirmação de Indicação Registrada)**: Enviado instantaneamente após o cliente submeter uma indicação através da landing page.
    *   **Assunto**: "Sua indicação para [Nome do Amigo] foi registrada!" ou "Obrigado por indicar um amigo!"
    *   **Corpo**:
        *   Agradecimento: "Muito obrigado por indicar [Nome do Amigo] para [Nome da Sua Marca]!"
        *   Próximos Passos: "Já entramos em contato com [Nome do Amigo] para que ele possa aproveitar o desconto de 15% na primeira compra."
        *   Expectativa de Recompensa: "Manteremos você informado sobre o status da indicação e, assim que [Nome do Amigo] finalizar a compra, seu crédito de R$50 será automaticamente adicionado à sua conta."
3.  **Email 2 (Notificação de Indicação Convertida e Recompensa)**: Enviado instantaneamente após o amigo indicado realizar a compra.
    *   **Assunto**: "Boas notícias: [Nome do Amigo] aproveitou sua indicação! Sua recompensa espera por você!" ou "Parabéns! Sua recompensa de indicação chegou!"
    *   **Corpo**:
        *   Confirmação de Sucesso: "Ótimas notícias, [Nome do Cliente]! Seu amigo [Nome do Amigo] realizou a primeira compra em [Nome da Sua Marca], graças à sua indicação!"
        *   Detalhes da Recompensa: "Como prometido, um crédito de R$50 foi adicionado à sua conta. Você já pode utilizá-lo em sua próxima compra conosco."
        *   Como Usar: "O crédito será aplicado automaticamente no checkout ou você pode vê-lo em seu painel de cliente aqui: [Link para Painel do Cliente]"
        *   Agradecimento Final: "Seu apoio é fundamental para nós. Continue indicando e ganhando!"
4.  **Email 3 (Lembrete de Recompensa Disponível - Opcional)**: Enviado 14 dias após o Email 2, se o crédito de recompensa ainda não tiver sido utilizado.
    *   **Assunto**: "Seu crédito de R$50 de indicação ainda te espera!"
    *   **Corpo**: "Lembramos que você tem um crédito de R$50 disponível em sua conta, resultado da indicação bem-sucedida de [Nome do Amigo]. Não deixe de usá-lo em sua próxima compra!"

---

## Templates

### Email de Convite Inicial para Indicação

```
Assunto: Amamos ter você! Que tal compartilhar essa experiência e ser recompensado?

Olá, Camila,

Sua satisfação é nossa prioridade e ficamos muito felizes em saber que você teve uma ótima experiência com a sua nova "Caixa de Assinatura Premium de Cafés".

Sabemos que você adora os cafés especiais da Cafe Code e pensamos: por que não compartilhar essa paixão e ainda ser recompensada por isso?

Estamos lançando nosso exclusivo Programa de Indicação!

Como funciona? É simples:
1. Você indica um amigo para a Cafe Code.
2. Seu amigo ganha 15% de desconto na primeira assinatura.
3. Assim que ele fizer a primeira compra, você ganha R$50 de crédito para usar em sua próxima caixa!

É simples! Clique no botão abaixo para gerar seu link de indicação exclusivo e começar a compartilhar:

[Botão: Gerar meu Link de Indicação Agora]
[Link para: https://www.cafecode.com.br/indicar?ref=camila123]

Você pode acompanhar suas indicações e recompensas diretamente em seu painel de cliente.

Obrigado por fazer parte da nossa comunidade!

Com carinho,
Equipe Cafe Code
```

### Email de Notificação de Recompensa por Indicação Convertida

```
Assunto: Boas notícias: João aproveitou sua indicação! Sua recompensa espera por você!

Olá, Camila,

Ótimas notícias! Seu amigo João realizou a primeira compra na Cafe Code, graças à sua indicação!

Muito obrigado por espalhar o amor por cafés especiais!

Como prometido, um crédito de R$50 foi adicionado à sua conta. Você já pode utilizá-lo em sua próxima compra conosco.

Para ver seu crédito e utilizá-lo, basta acessar sua conta:
[Link para: https://www.cafecode.com.br/minha-conta]

Seu crédito será aplicado automaticamente no checkout de sua próxima assinatura.

Seu apoio é fundamental para nós. Continue indicando e ganhando!

Um abraço,
Equipe Cafe Code
```

---

## Checklist

- [x] Incentivo claro e atrativo para indicador e indicado definido (ex: R$50 crédito para um, 15% desconto para outro).
- [x] Página de destino (landing page) otimizada para o indicado com formulário de resgate fácil.
- [x] Sistema de rastreamento de indicações configurado e funcionando, com atribuição correta.
- [x] Automação de convite à indicação segmentada para clientes satisfeitos (NPS 9-10 ou alto LTV).
- [x] Sequência de follow-up para notificar o indicador sobre o status da indicação (registrada, convertida).
- [x] Mecanismo de distribuição automatizada das recompensas validado e testado.
- [x] Assuntos de email que geram curiosidade e destacam o benefício imediato para o remetente.
- [x] Chamada para ação (CTA) única e clara nos emails de convite para gerar o link de indicação.
- [x] Testes A/B em assuntos, CTAs e diferentes tipos de incentivos (ex: crédito vs. produto grátis).
- [x] Cláusulas claras sobre o programa de indicação (termos e condições) visíveis na landing page.

---

## Métricas de Referência

| Métrica                                | Benchmark        | Meta             |
|----------------------------------------|------------------|------------------|
| Taxa de Conversão de Indicação         | 10-20%           | 25%+             |
| Taxa de Participação no Programa       | 5-15%            | 20%+             |
| LTV (Lifetime Value) de Clientes Indicados | 10-25% > Clientes comuns | 30%+ > Clientes comuns |
| Custo de Aquisição por Indicação (CAC) | 60-80% < Outros canais | 90% < Outros canais |
| Taxa de Abertura (Email de Convite)    | 20-30%           | 35%+             |
| Taxa de Cliques (Email de Convite)     | 5-10%            | 12%+             |

---

## Erros Comuns

1.  **Incentivos pouco atraentes ou desequilibrados**: Oferecer algo de baixo valor ou recompensar apenas um lado (indicador ou indicado) diminui drasticamente a motivação.
    *   **Como evitar**: Pesquisar o que realmente motiva sua base de clientes. Em vez de "10% de desconto" genérico, oferecer "R$50 de crédito" para o indicador e "1 mês grátis" para o indicado, alinhando com o valor percebido do seu produto ou serviço.
2.  **Processo de indicação complicado ou manual**: Exigir muitos passos para indicar ou depender de validação manual atrasa a experiência e frustra o usuário.
    *   **Como evitar**: Simplificar ao máximo. Fornecer um link único de indicação onde o amigo só precisa inserir o email para resgatar a oferta. Automatizar a validação e a distribuição das recompensas.
3.  **Falta de comunicação pós-indicação**: O indicador não recebe atualizações sobre o status de suas indicações ou quando a recompensa será liberada.
    *   **Como evitar**: Implementar uma sequência de emails informando o status da indicação (recebida, em análise, convertida, recompensa enviada). Ex: "Sua indicação para João foi registrada e estamos em contato!" e depois "Boas notícias: João aproveitou sua indicação! Sua recompensa espera por você!".
4.  **Não segmentar a base de clientes para o convite**: Enviar o convite para indicação indiscriminadamente para toda a base, incluindo clientes insatisfeitos ou pouco engajados.
    *   **Como evitar**: Focar nos clientes com maior probabilidade de indicar, como promotores (NPS 9-10), clientes com alto LTV ou que acabaram de ter uma experiência positiva recente. Ex: Somente clientes que interagiram com seu produto nos últimos 3 meses e não registraram reclamações no período.

---

## Dicas Avançadas

1.  **Gamificação Progressiva no Programa de Indicação**: Não apenas ofereça uma recompensa única. Crie níveis ou tiers para indicadores (ex: "Embaixador Prata", "Embaixador Ouro") com recompensas crescentes, bônus exclusivos e reconhecimento público (ex: menção em newsletter, acesso antecipado a produtos).
2.  **Testes A/B Multivariados nos Incentivos**: Vá além de testar apenas a quantia. Teste tipos de incentivo (crédito na loja vs. doação para caridade em nome do cliente vs. produto físico exclusivo), formatos (fixo vs. percentual) e a proporção de divisão entre indicador/indicado (ex: R$50/R$50 vs. R$70/R$30).
3.  **Integração Direta com Pesquisas de Satisfação (NPS)**: Configure um fluxo onde clientes que respondem com NPS 9 ou 10 são imediatamente direcionados para a página de indicação no final da pesquisa, ou recebem o email de convite poucas horas depois, enquanto a experiência positiva ainda está fresca na memória.
4.  **Criação de um Portal do Embaixador Personalizado**: Desenvolva uma área logada onde o indicador pode acompanhar em tempo real o status de todas as suas indicações, gerar novos links personalizados, ver o total de recompensas acumuladas e até mesmo compartilhar diretamente em redes sociais com mensagens pré-aprovadas.
5.  **Personalização Extrema na Mensagem de Indicação**: Utilize dados do CRM para ir além do nome do cliente. Faça referência direta à experiência específica que ele teve com o produto ou serviço. Ex: "Já que você amou a sua 'Caixa de Assinatura Premium de Cafés' de março, que tal compartilhar essa experiência única com um amigo e ganhar uma recompensa?" Isso torna a mensagem mais autêntica e relevante.