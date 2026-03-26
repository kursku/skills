---
name: referral-program
description: "Referral Program — Skill especializada para referral program"
license: MIT
metadata:
  version: 1.0.0
  author: Cafe Code AI
  category: 08-lancamento-growth
  updated: 2026-03-01
risk: safe
---

# Referral Program

Esta skill capacita o Claude a projetar, implementar e otimizar programas de indicação de sucesso para impulsionar a aquisição e retenção de usuários.

---

## Keywords

Indicação de clientes, Marketing de referência, Growth Hacking, Aquisição de usuários, Retenção de clientes, Programa de afiliados, Viral loop, Incentivos de indicação, NPS (Net Promoter Score), Lifetime Value (LTV), Customer Acquisition Cost (CAC), Gamificação de referência, Coeficiente Viral.

---

## Quick Start

1.  **Defina o incentivo duplo**: Escolha recompensas tangíveis para o indicador e o indicado. Exemplo: "R$50 em crédito para quem indica, 10% de desconto na primeira compra para quem é indicado".
2.  **Crie a página de referência dedicada**: Desenvolva uma landing page clara e concisa para o programa, com um Call-to-Action (CTA) explícito como "Indique um Amigo e Ganhe!".
3.  **Implemente a geração de links únicos**: Configure um sistema que permita a cada usuário ter um link de indicação rastreável, como `meudominio.com/indique?ref=CODIGOUNICOUSUARIO123`.
4.  **Comunique o programa para a base engajada**: Envie um e-mail segmentado para seus clientes mais fiéis (NPS alto, compras recorrentes) anunciando o lançamento e os benefícios do programa.
5.  **Monitore as primeiras 50 indicações**: Acompanhe o funil de conversão das primeiras indicações para identificar rapidamente qualquer fricção ou gargalo na jornada do indicador ou do indicado.

---

## Core Workflows

### Workflow 1: Lançamento e Otimização de um Programa de Indicação Dupla

Este workflow detalha o processo para criar e lançar um programa de indicação que beneficie tanto o indicador quanto o indicado, maximizando a viralidade e a aquisição de clientes qualificados.

1.  **Análise de Capacidade e Segmentação da Base**:
    *   **Verificação de Pré-requisitos**: Antes de iniciar, valide se o produto ou serviço possui um Net Promoter Score (NPS) médio acima de 70. Um NPS alto indica satisfação do cliente e propensão a indicar. Se o NPS for inferior, foque primeiro na melhoria do produto.
    *   **Identificação de Promotores Chave**: Utilize dados do CRM para identificar os 20% de clientes com maior Lifetime Value (LTV) e maior frequência de compra nos últimos 6 meses. Exemplo: Para um e-commerce de moda, selecione clientes que gastaram mais de R$1.500 e fizeram 4+ compras nos últimos 12 meses. Esses são os primeiros a serem convidados.
2.  **Definição de Incentivos Assimétricos e Sustentáveis**:
    *   **Recompensas de Valor Real**: Escolha incentivos que realmente motivem a ação e sejam economicamente viáveis. Considere o Custo de Aquisição de Cliente (CAC) atual de outros canais.
    *   **Exemplos Concretos**:
        *   **SaaS B2B**: "O indicador ganha um mês grátis no plano Pro (valor R$180) e o indicado recebe 25% de desconto no primeiro ano de assinatura."
        *   **E-commerce B2C**: "O indicador recebe R$40 em crédito na próxima compra (válido por 90 dias) e o indicado ganha 20% de desconto na primeira compra acima de R$120."
    *   **Evite Canibalização**: Garanta que os descontos não comprometam excessivamente a margem de lucro. Teste diferentes percentuais para encontrar o ponto ideal.
3.  **Desenvolvimento da Infraestrutura Tecnológica de Rastreamento**:
    *   **Geração de Links Exclusivos**: Implemente um módulo no sistema (ou utilize plataformas como `ReferralCandy` ou `Extole`) que gere um link único para cada usuário, garantindo o rastreamento preciso. O link deve ser simples e reconhecível, ex: `app.minhaempresa.com/indique?code=JOSESILVA789`.
    *   **Automação de Distribuição de Recompensas**: Configure a automação para que as recompensas sejam creditadas instantaneamente ou após a validação da compra/cadastro do indicado. Isso é crucial para a satisfação do usuário.
    *   **Painel de Acompanhamento**: Crie um painel onde o cliente possa ver o status de suas indicações e recompensas pendentes/recebidas.
4.  **Criação e Posicionamento de Materiais de Divulgação**:
    *   **E-mail de Lançamento Segmentado**: Redija um e-mail claro e direto para os promotores identificados. Título: "Seu feedback importa: Indique um amigo e ganhe recompensas exclusivas!".
    *   **Página de Indicação Dedicada**: Desenvolva uma landing page detalhada que explique o programa, os benefícios e o processo passo a passo, incluindo FAQs. URL: `meudominio.com/programa-de-indicacao`.
    *   **Banners e Pop-ups In-App/Site**: Posicione CTAs visíveis em áreas de alta visibilidade, como na página de confirmação de compra, no perfil do usuário, ou em pop-ups contextuais após uma avaliação positiva.
    *   **Conteúdo para Redes Sociais**: Crie posts e stories com exemplos de como o programa funciona e os benefícios, incentivando o compartilhamento.
5.  **Lançamento Controlado e Monitoramento Inicial Detalhado**:
    *   **Piloto com Grupo Restrito**: Inicie o programa com um grupo menor (ex: 500-1000 clientes com maior LTV) para testar a funcionalidade, a clareza da comunicação e coletar feedback antes de expandir.
    *   **Acompanhamento de Métricas Chave (Primeiros 30 Dias)**:
        *   **Taxa de Compartilhamento (Share Rate)**: % de usuários elegíveis que compartilharam seu link. Meta: 8-15%.
        *   **Taxa de Conversão de Indicados (Referred Conversion Rate)**: % de indicados que realizaram a ação desejada (cadastro/compra). Meta: 15-30%.
        *   **Custo por Aquisição de Referência (CAC_Referral)**: Custo das recompensas dividido pelo número de novos clientes adquiridos via indicação. Compare com CAC de outros canais.
    *   **Iteração Rápida**: Com base nos dados e feedbacks iniciais, ajuste a comunicação, os incentivos ou o fluxo do programa para otimizar os resultados.

### Workflow 2: Otimização Contínua e Escala de um Programa de Indicação Existente

Este workflow foca em refinar e escalar um programa de indicação que já está em operação, utilizando dados e táticas avançadas para maximizar seu impacto.

1.  **Análise Aprofundada do Funil de Indicação**:
    *   **Mapeamento de Pontos de Fricção**: Utilize ferramentas de análise (Mixpanel, Google Analytics com UTMs, Hotjar) para visualizar o funil completo: Exposição ao programa > Clique para gerar link > Compartilhamento do link > Cliques no link compartilhado > Cadastro/Conversão do indicado > Reivindicação da recompensa.
    *   **Identificação de Gargalos**: Se o "Share Rate" é alto, mas a "Referred Conversion Rate" é baixa (ex: 12% de compartilhamento, mas apenas 3% de conversão do indicado), o problema pode estar na mensagem que o indicador usa, na landing page do indicado, ou na oferta para o indicado.
    *   **Exemplo de Ação**: Se muitos usuários geram links, mas poucos compartilham, simplifique o processo de compartilhamento ou reforce os benefícios do indicador na página de geração do link.
2.  **Testes A/B Constantes de Incentivos e Copywriting**:
    *   **Hipóteses de Incentivos**: Crie grupos de teste para diferentes combinações de recompensas.
        *   **Teste A**: Indicador R$60 crédito / Indicado 10% desconto.
        *   **Teste B**: Indicador 1 mês grátis / Indicado frete grátis.
    *   **Variações de Mensagem (Copywriting)**: Teste diferentes chamadas para ação e mensagens nos e-mails e banners do programa.
        *   **Copy 1**: "Indique e Ganhe Dinheiro Extra!"
        *   **Copy 2**: "Compartilhe o que você ama e receba recompensas exclusivas!"
    *   **Métricas de Sucesso**: Monitore não apenas o volume de indicações, mas também o LTV e a taxa de retenção dos clientes adquiridos por cada variação para garantir que a qualidade não seja sacrificada.
3.  **Segmentação Avançada para Reengajamento e Ativação**:
    *   **Segmentos de Comportamento**: Crie segmentos de usuários com base em sua interação com o programa:
        *   **Viram, mas não indicaram**: Envie um e-mail de lembrete com um caso de sucesso de indicação.
        *   **Indicaram, mas amigos não converteram**: Envie um e-mail com dicas para o amigo converter ou um lembrete para o amigo. Ex: "Seu amigo [Nome do Amigo] ainda não aproveitou o desconto! Que tal enviar uma mensagem de lembrete?".
        *   **Indicadores de Baixa Frequência**: Ofereça um bônus extra na próxima indicação para motivá-los.
    *   **Canais de Reengajamento**: Utilize e-mail marketing, notificações push, mensagens in-app e até SMS para alcançar esses segmentos em momentos oportunos.
4.  **Gamificação e Níveis de Recompensa para Escalada**:
    *   **Sistema de Níveis**: Introduza um sistema de níveis que recompense o volume e a qualidade das indicações.
        *   **Nível Bronze**: 1-2 indicações (recompensa padrão).
        *   **Nível Prata**: 3-5 indicações (recompensa padrão + bônus de R$20 ou um brinde).
        *   **Nível Ouro**: 6+ indicações (recompensa padrão + acesso antecipado a produtos ou maior porcentagem de comissão).
    *   **Leaderboards e Reconhecimento**: Crie um placar de líderes (leaderboard) para os maiores indicadores, oferecendo reconhecimento público (com permissão) ou prêmios exclusivos (ex: "Top 5 Indicadores do Mês ganham um ano de assinatura premium").
5.  **Integração Profunda com o Ciclo de Vida do Cliente**:
    *   **Pontos de Contato Estratégicos**: Posicione a oferta de indicação em momentos de alta satisfação do cliente:
        *   Após a primeira compra bem-sucedida e entrega do produto.
        *   Após a renovação de uma assinatura.
        *   Após o cliente dar um NPS 9 ou 10.
        *   Na página de confirmação de avaliação positiva do produto.
    *   **Automação Contextual**: Automatize e-mails de indicação para serem enviados 30 dias após a compra (período em que a satisfação ainda é alta e o produto já foi testado), ou após o cliente interagir com um recurso específico do produto.

---

## Templates

### E-mail de Lançamento de Programa de Indicação

```
Assunto: 🎉 Indique um Amigo e Ganhe R$40 na sua próxima compra!

Olá, [Nome do Cliente],

Sabemos que você valoriza a qualidade e os resultados que [Nome do Produto/Serviço] oferece. E por isso, queremos recompensá-lo por compartilhar essa experiência incrível!

Lançamos nosso novo Programa "Indique e Ganhe", onde você e seus amigos saem ganhando!

✨ **Como funciona é super simples:**
1.  **Você indica:** Compartilhe seu link exclusivo com amigos, familiares ou colegas que ainda não são nossos clientes.
2.  **Seu amigo ganha:** Ele recebe 20% de desconto na primeira compra acima de R$120 (ou no primeiro mês de assinatura) ao usar seu link.
3.  **Você ganha:** Assim que seu amigo fizer a primeira compra (ou ativar a assinatura), você recebe R$40 em crédito automaticamente para usar na sua próxima compra conosco!

É a sua chance de ajudar seus amigos a descobrir [Benefício Principal do Produto, ex: "soluções inteligentes para o dia a dia"] e ainda ser recompensado por isso!

Seu link exclusivo para indicar é:
👉 [LINK_EXCLUSIVO_USUARIO_AQUI]

Compartilhe agora e comece a ganhar!
[Botão: Indicar Agora]

Ou clique aqui para saber mais detalhes sobre o programa:
[LINK_PARA_PAGINA_DO_PROGRAMA]

Agradecemos por fazer parte da nossa comunidade e por ser um cliente tão especial!

Atenciosamente,
Equipe [Nome da Empresa]
[Site da Empresa] | [Redes Sociais]
```

### Mensagem Curta para Compartilhamento Social (WhatsApp/Redes)

```
Ei, [Nome do Amigo]!

Você precisa conhecer [Nome do Produto/Serviço da Empresa]! Eu uso e adoro [mencionar um benefício específico, ex: "como ele simplifica a gestão de projetos" ou "a qualidade dos produtos para casa"].

E o melhor: com este link exclusivo, você ganha 20% de desconto na primeira compra acima de R$120 (ou no primeiro mês de assinatura)!

Não perca essa chance!
👉 [LINK_EXCLUSIVO_USUARIO_AQUI]

Aproveite! 😉
```

---

## Checklist

- [ ] NPS médio da base de clientes validado acima de 70.
- [ ] Incentivos duplos (para indicador e indicado) definidos e validados financeiramente.
- [ ] Página de indicação (landing page) criada, com CTA claro e explicação do programa.
- [ ] Sistema de geração de links únicos e rastreáveis implementado e testado.
- [ ] Automação de atribuição e distribuição de recompensas configurada e funcional.
- [ ] E-mails de lançamento, banners e conteúdo para redes sociais desenvolvidos e segmentados.
- [ ] Dashboard de métricas essenciais (Share Rate, Conversion Rate, CAC_Referral, LTV_Referral) configurado.
- [ ] Plano de testes A/B para diferentes incentivos e mensagens elaborado.
- [ ] Estratégia de reengajamento para usuários que não indicaram ou cujos indicados não converteram definida.
- [ ] Termos e Condições do programa de indicação claros, justos e acessíveis.
- [ ] Integração do programa com pontos chave do ciclo de vida do cliente (pós-compra, NPS alto).
- [ ] Treinamento da equipe de suporte sobre as regras e solução de dúvidas do programa.

---

## Métricas de Referência

| Métrica                         | Benchmark (E-commerce) | Benchmark (SaaS B2C) | Benchmark (SaaS B2B) | Meta (Exemplo) |
| :------------------------------ | :--------------------- | :------------------- | :------------------- | :------------- |
| **Share Rate** (Taxa de Compartilhamento) | 5-15%                  | 10-25%               | 15-30%               | 18%            |
| **Referred Conversion Rate** (Taxa de Conversão de Indicados) | 10-25%                 | 15-35%               | 20-45%               | 28%            |
| **CAC_Referral** (Custo de Aquisição de Cliente por Indicação) | 30-70% menor que CAC geral | 40-80% menor que CAC geral | 50-90% menor que CAC geral | 55% menor      |
| **Referral Revenue Share** (Fatia da Receita de Indicação) | 8-20% da receita de aquisição | 12-28% da receita de aquisição | 15-35% da receita de aquisição | 20%            |
| **Viral Coefficient (K-factor)** | > 0.1 (bom)            | > 0.15 (muito bom)   | > 0.2 (excelente)    | 0.18           |
| **LTV de Clientes Indicados**   | 15-35% maior que LTV geral | 20-40% maior que LTV geral | 25-50% maior que LTV geral | 30% maior      |

---

## Erros Comuns

1.  **Incentivos pouco atraentes ou unilaterais**: Oferecer uma recompensa de baixo valor percebido, ou beneficiar apenas o indicador (ou apenas o indicado), desmotivando uma das partes.
    *   **Como evitar**: Implemente um sistema de incentivo duplo com valor relevante para ambos os lados. Exemplo: "Em vez de apenas R$20 para o indicador, ofereça R$40 para o indicador E 15% de desconto para o amigo, criando uma motivação recíproca."
2.  **Processo de indicação complexo ou com atrito**: A jornada para o cliente indicar um amigo é longa, confusa, ou o rastreamento das indicações falha, gerando desconfiança e abandono.
    *   **Como evitar**: Desenhe um fluxo de indicação com o mínimo de cliques possível (idealmente 1-2). Garanta que o sistema de links únicos e o rastreamento funcionem perfeitamente. Teste a jornada do usuário de ponta a ponta antes do lançamento. Exemplo: "O cliente deve poder copiar o link ou compartilhar diretamente via WhatsApp com um único clique, sem preencher formulários extensos."
3.  **Falta de promoção contínua e visibilidade do programa**: Lançar o programa uma única vez e esperar que ele se promova sozinho, resultando em baixa adesão ao longo do tempo.
    *   **Como evitar**: Promova ativamente o programa em múltiplos canais (e-mail marketing segmentado, banners no site/app, redes sociais, pop-ups contextuais) e em momentos estratégicos da jornada do cliente, como após uma compra bem-sucedida ou um feedback positivo. Exemplo: "Envie um e-mail de lembrete do programa a cada 45 dias para sua base de clientes fiéis."
4.  **Ignorar a qualidade do indicado em favor do volume**: Focar apenas no número de novas contas ou vendas geradas, sem avaliar o Lifetime Value (LTV) e a taxa de retenção dos clientes indicados.
    *   **Como evitar**: Monitore o LTV e a taxa de retenção dos clientes adquiridos via indicação. Se a qualidade for baixa, ajuste os critérios de elegibilidade do indicador, ou o público-alvo da comunicação do programa, para atrair indicados mais qualificados e que permaneçam mais tempo. Exemplo: "Se os indicados tendem a fazer apenas uma compra, teste um incentivo que promova a recorrência, como '20% de desconto na primeira compra e 10% na segunda'."

---

## Dicas Avançadas

1.  **Crie um "