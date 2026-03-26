---
name: influencer-ads-whitelisting
description: "Influencer Ads Whitelisting — Skill especializada para configurar, otimizar e gerenciar campanhas de influencer ads whitelisting em Meta Ads, Google Ads e TikTok Ads."
license: MIT
metadata:
  version: 1.0.0
  author: Cafe Code AI
  category: 04-anuncios-trafego
  updated: 2026-03-01
risk: safe
---

# Influencer Ads Whitelisting

Esta skill capacita o Claude a configurar, otimizar e gerenciar campanhas de Influencer Ads Whitelisting, utilizando acessos de parceiro em plataformas como Meta Ads, Google Ads e TikTok Ads para maximizar performance e escala de anúncios.

---

## Keywords

Whitelisting Influencer, Acesso de Parceiro Meta, TikTok Spark Ads, Google Ads Influencer, Collab Ads, Dark Posts Influencer, Otimização Whitelisting, Escalabilidade Influenciadores, Meta Business Suite Permissões, Branded Content TikTok, Anúncios com Identidade de Influenciador, Permissão de Anúncios Influencer.

---

## Quick Start

1.  **Obtenha o ID da Business Manager (BM)** do influenciador para Meta Ads ou o código Spark Ads para TikTok.
2.  **Envie solicitação de acesso de parceiro** (Meta Ads) ou importe o código (TikTok Ads) na sua conta de anúncios.
3.  **Crie a campanha** no Gerenciador de Anúncios, selecionando a identidade do influenciador no nível do anúncio.
4.  **Publique e monitore** as métricas de performance (ROAS, CTR, CPA) para otimização contínua.

---

## Core Workflows

### Workflow 1: Configuração de Whitelisting para Meta Ads (Facebook/Instagram)

Este workflow detalha o processo de obtenção de permissão e criação de campanhas de anúncios que aparecerão com a identidade de um influenciador no Facebook e Instagram, usando a Meta Business Manager (BM).

1.  **Verificação de Pré-requisitos com o Influenciador:**
    *   Confirme que o influenciador possui uma Meta Business Manager (BM) ativa.
    *   Assegure-se de que a página do Instagram e/ou Facebook do influenciador está vinculada à sua BM.
    *   Solicite o ID da BM do influenciador (ex: `ID: 1234567890`).

2.  **Solicitação de Acesso de Parceiro na Sua BM:**
    *   Na sua Meta Business Manager (ex: "BM Agência Digital X"), navegue até "Configurações do Negócio" > "Parceiros".
    *   Clique em "Adicionar" e selecione "Conceder a um parceiro acesso aos seus ativos".
    *   Insira o ID da BM do influenciador (ex: `1234567890`).
    *   Na próxima tela, selecione os ativos necessários para a colaboração:
        *   **Páginas:** Selecione a página do Instagram e/ou Facebook do influenciador (ex: "@influencer_top"). Conceda as permissões de "Anúncios" e "Conteúdo" (essenciais para criar e veicular anúncios com a identidade do influenciador).
        *   **Contas de Anúncio:** Geralmente não é necessário para whitelisting, mas pode ser concedido se houver necessidade de gerenciar diretamente a conta de anúncios do influenciador.
        *   **Pixels:** Se o influenciador tiver um pixel próprio e você precisar de dados ou permissão para escrever eventos, solicite acesso de "Gerenciar Pixel".
    *   Clique em "Salvar alterações". O influenciador receberá uma notificação em sua BM para aceitar o convite.

3.  **Criação da Campanha de Anúncios no Gerenciador da Sua BM:**
    *   No Gerenciador de Anúncios da sua BM, clique em "Criar" para iniciar uma nova campanha.
    *   **Objetivo da Campanha:** Para campanhas de e-commerce com whitelisting, selecione "Vendas". Para maior alcance e reconhecimento, "Reconhecimento" ou "Alcance".
    *   **Configuração do Conjunto de Anúncios:**
        *   Defina seu público-alvo (ex: "Mulheres, 25-45 anos, interesses em moda sustentável, Brasil").
        *   Orçamento (ex: `R$ 200,00/dia`) e programação.
        *   Posicionamentos: Recomenda-se "Posicionamentos Advantage+" para otimização automática.
    *   **Configuração do Anúncio (Nível do Anúncio):**
        *   Em "Identidade", selecione a página do Instagram/Facebook do influenciador (ex: "@influencer_top"). Este é o passo crucial para o whitelisting.
        *   **Formato do Anúncio:**
            *   **Usar Publicação Existente:** Selecione um post orgânico que o influenciador já publicou (ex: um Reels de review de produto). Isso capitaliza o engajamento e a prova social já existentes.
            *   **Criar Anúncio (Dark Post):** Crie um anúncio do zero que será veiculado apenas como anúncio, sem aparecer no feed orgânico do influenciador. Ideal para testes A/B de criativos mais comerciais.
        *   Adicione a chamada para ação (CTA, ex: "Comprar Agora") e o URL final da sua landing page (com parâmetros UTM para rastreamento: `?utm_source=metaads&utm_medium=influencer_top&utm_campaign=lancamento_produto`).
    *   Publique a campanha e inicie o monitoramento.

### Workflow 2: Otimização e Escalabilidade de Campanhas Whitelisted no TikTok Ads (Spark Ads)

Este workflow foca na utilização de Spark Ads do TikTok para impulsionar conteúdo de influenciadores, otimizando e escalando os resultados.

1.  **Obtenção de Código de Autorização (Spark Ads) do Influenciador:**
    *   **Pré-requisito:** O influenciador deve ter uma conta TikTok Business e o conteúdo (vídeo) já publicado ou pronto para ser publicado em seu perfil.
    *   **Passo 1.1:** O influenciador publica o vídeo no TikTok. Após a publicação, ele deve acessar o vídeo, clicar nos três pontos (...) e selecionar "Configurações do anúncio" (Ad settings).
    *   **Passo 1.2:** Ativar "Autorização de Anúncios" (Ad authorization) e gerar um código de autorização (ex: `789ABCDEF`). É fundamental definir um período de validade adequado (ex: 60 ou 90 dias) para a duração da campanha.
    *   **Passo 1.3:** O influenciador compartilha o código de autorização com a sua agência/marca.

2.  **Criação da Campanha no TikTok Ads Manager da Sua Marca:**
    *   Na conta do TikTok Ads Manager da sua agência/marca, crie uma nova campanha.
    *   **Objetivo da Campanha:** Para conversões, selecione "Vendas" ou "Geração de Leads".
    *   **Configuração do Conjunto de Anúncios:**
        *   Defina seu público-alvo (ex: "Homens e mulheres, 18-34 anos, interesse em gaming, Brasil").
        *   Orçamento (ex: `R$ 150,00/dia`) e programação.
    *   **Configuração do Anúncio (Nível do Anúncio):**
        *   Em "Detalhes do Anúncio", selecione "Usar publicação do TikTok" (Use TikTok post).
        *   Clique em "Inserir código de autorização" (Enter authorization code) e cole o código fornecido pelo influenciador (ex: `789ABCDEF`).
        *   O vídeo do influenciador será importado e aparecerá com o perfil dele como identidade do anúncio.
        *   Adicione o CTA (ex: "Comprar Agora", "Saiba Mais") e o URL de destino (com UTMs: `?utm_source=tiktokads&utm_medium=influencer_gamertop&utm_campaign=promocao_headset`).
    *   Publique a campanha.

3.  **Otimização e Estratégias de Escalabilidade:**
    *   **Análise de Performance Diária:** Monitore métricas como CPM, CPC, CTR, CVR e ROAS. Vídeos com CTR acima de 1.8% e ROAS > 2.5x são excelentes candidatos para escalabilidade.
    *   **Testes A/B de Públicos:** Crie conjuntos de anúncios duplicados para o mesmo conteúdo whitelisted, testando públicos distintos. Ex: um público de lookalikes 1% de compradores vs. um público de interesses amplos relacionados ao nicho do influenciador.
    *   **Aumento Gradual de Orçamento:** Para campanhas de alta performance, aumente o orçamento em 15-25% a cada 2-3 dias, evitando choques no algoritmo que podem desestabilizar a entrega.
    *   **Whitelisting Multi-Influenciador:** Colabore com 3-5 influenciadores simultaneamente para testar diferentes estilos de conteúdo e perfis de audiência. Invista mais nos que geram o melhor ROAS e menor CPA.

---

## Templates

### Template 1: Solicitação de Acesso de Parceiro Meta Business Suite (E-mail)

```
Assunto: Solicitação de Acesso de Parceiro BM para Collab Ads - [Nome da Marca] x [Nome do Influenciador]

Prezado(a) [Nome do Influenciador/Gerente],

Esperamos que este e-mail o encontre bem.

Em nome da [Nome da Marca], estamos muito animados com a nossa parceria e o potencial dos nossos próximos anúncios em conjunto. Para que possamos veicular anúncios de forma otimizada utilizando sua identidade no Facebook e Instagram (os famosos "Influencer Ads Whitelisting"), precisamos de acesso de parceiro à sua Meta Business Manager (BM).

Este acesso é seguro e nos permite criar campanhas no Gerenciador de Anúncios da [Nome da Marca] que aparecerão como se tivessem sido publicadas diretamente da sua página, mas com a capacidade de serem impulsionadas com orçamento pago e segmentação precisa.

Por favor, siga os passos abaixo para nos conceder acesso:
1. Acesse sua Meta Business Manager (business.facebook.com/overview).
2. Vá em "Configurações do Negócio" > "Solicitações" > "Recebidas".
3. Você deve encontrar uma solicitação de parceria da nossa BM, "BM Agência Alpha Marketing" (ID: 1234567890).
4. Aceite a solicitação.
5. Confirme que nossa BM tem acesso à sua Página do Instagram/Facebook ([Link para sua Página, ex: instagram.com/influencer_top_beauty]) com permissões de "Anúncios" e "Conteúdo".

Se tiver qualquer dúvida ou precisar de ajuda com os passos, por favor, não hesite em nos contatar via [Seu WhatsApp/Telefone].

Agradecemos imenso sua colaboração!

Atenciosamente,

[Seu Nome/Nome da Agência]
[Seu Cargo]
[Seu Contato]
```

### Template 2: Relatório de Performance Resumido (Influencer Whitelisting)

```
Relatório de Performance - Whitelisting [Nome do Influenciador] - [Período: 01/03 - 07/03/2024]

Campanha: Lançamento de Inverno 2024 - @ModaEstilo_Influencer
Plataforma: TikTok Ads
Objetivo: Vendas

----------------------------------------------------
Métricas Chave:
----------------------------------------------------
Investimento Total: R$ 4.800,00
Faturamento Gerado: R$ 19.200,00
ROAS (Retorno sobre Investimento em Anúncios): 4.0x
CPA (Custo por Aquisição): R$ 48,00

Impressões: 400.000
Alcance: 210.000
Cliques no Link: 8.000
CTR (Taxa de Cliques no Link): 2.0%
CPC (Custo por Clique no Link): R$ 0,60

Adições ao Carrinho: 320
Compras: 100
Taxa de Conversão (Compras/Cliques): 1.25%

----------------------------------------------------
Análise Rápida:
----------------------------------------------------
A campanha com o conteúdo da @ModaEstilo_Influencer no TikTok apresentou um ROAS de 4.0x, superando nossa meta de 3.0x. O CTR de 2.0% indica um forte apelo do criativo e da audiência engajada. O CPA de R$ 48,00 é altamente competitivo para o setor de moda. O vídeo "Look do Dia Inverno" gerou os melhores resultados.

----------------------------------------------------
Próximos Passos:
----------------------------------------------------
1. Aumentar orçamento da campanha em +20% (R$ 960/semana) para a próxima semana.
2. Criar um novo conjunto de anúncios com Lookalike 1% de Compradores do pixel da marca no TikTok.
3. Solicitar ao influenciador um novo código Spark Ads para o vídeo "Unboxing de Inverno" para teste A/B.
4. Testar um CTA diferente ("Garanta Seu Look") no vídeo de melhor performance.
```

---

## Checklist

- [x] Influenciador possui Meta Business Manager (BM) configurada e ativa?
- [x] Página do Instagram/Facebook do influenciador vinculada à BM dele?
- [x] ID da BM do influenciador coletado corretamente e salvo para referências futuras?
- [x] Solicitação de acesso de parceiro para a BM do influenciador enviada com permissões de "Anúncios" e "Conteúdo" para a página?
- [x] Influenciador aceitou a solicitação de parceria na sua BM e confirmou as permissões?
- [x] Para TikTok: Influenciador ativou "Autorização de Anúncios" e gerou o código Spark Ads com validade adequada?
- [x] Código Spark Ads do TikTok importado e validado