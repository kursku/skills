---
name: tiktok-ads
description: "Tiktok Ads — Skill especializada para tiktok ads"
license: MIT
metadata:
  version: 1.0.0
  author: Cafe Code AI
  category: 04-anuncios-trafego
  updated: 2026-03-01
risk: safe
---

# Tiktok Ads

Esta skill capacita o Claude a criar, otimizar e analisar campanhas de anúncios no TikTok Ads, focando em performance e resultados reais para e-commerce e geração de leads.

---

## Keywords

Campanhas TikTok Ads, Otimização de ROAS, Conversões no TikTok, TikTok Pixel, Spark Ads, Video Ads TikTok, Públicos Personalizados TikTok, Lançamento de Produto TikTok, Geração de Leads TikTok, Análise de Métricas TikTok, Estratégias de Lances TikTok, Criativos Virais TikTok.

---

## Quick Start

1.  **Instalação do TikTok Pixel**: Implemente o pixel base e eventos de conversão (ViewContent, AddToCart, InitiateCheckout, CompletePayment) no seu site via GTM ou diretamente no código.
2.  **Criação da Primeira Campanha de Conversão**: Configure uma campanha com objetivo "Conversões no site" direcionada a um evento de "CompletePayment" para e-commerce ou "Lead" para captação.
3.  **Configuração de Ad Group (Conjunto de Anúncios)**: Escolha posicionamentos automáticos, um orçamento diário de R$50-R$100 e segmentação por interesses amplos (ex: "Moda e Acessórios", "Beleza e Cuidados Pessoais") ou use públicos personalizados de visitantes do site dos últimos 30 dias.
4.  **Upload de Criativos Nativos**: Adicione 3-5 vídeos curtos (15-60s) em formato vertical (9:16) com legendas claras e uma chamada para ação direta, utilizando músicas em alta no TikTok.
5.  **Monitoramento Inicial e Ajuste de Lances**: Monitore o CPC e CPA nos primeiros 24-48h; se o CPA estiver muito alto, revise os criativos ou ajuste o lance para "Custo Alvo" com um valor 10-20% abaixo do seu CPA máximo aceitável.

---

## Core Workflows

### Workflow 1: Criação de Campanha de Conversão de Alta Performance para E-commerce

Este workflow detalha a construção de uma campanha focada em vendas diretas para um produto de e-commerce, visando maximizar o Retorno sobre o Investimento Publicitário (ROAS).

1.  **Estrutura da Campanha**:
    *   **Nível Campanha**:
        *   **Objetivo**: Selecione "Website Conversions" (Conversões no site).
        *   **Nome da Campanha**: `PRODUTO_NOME_VENDA_CONVERSAO_DDMM` (ex: `TENIS_URBANO_VENDA_CONVERSAO_2508`).
        *   **Otimização de Orçamento de Campanha (CBO)**: Desligue inicialmente para ter controle granular nos ad groups.
    *   **Nível Ad Group (Conjunto de Anúncios)**: Crie 2-3 ad groups distintos para testar públicos.
        *   **Nome do Ad Group**: `PRODUTO_NOME_PUBLICO_TIPO` (ex: `TENIS_URBANO_INTERESSES_AMPLOS`, `TENIS_URBANO_LOOKALIKE_COMPRADORES`).
        *   **Tipo de Promoção**: `Website`.
        *   **Pixel do TikTok**: Selecione o pixel configurado.
        *   **Evento de Otimização**: `Complete Payment` (ou `Purchase`).
        *   **Posicionamentos**: `Automático` (permite que o TikTok otimize para melhores resultados, incluindo Pangle Network).
        *   **Tipos de Criativos**: `Dynamic Creative` (para que o TikTok teste combinações de criativos automaticamente).
        *   **Segmentação (Audience)**:
            *   **Ad Group 1 (Interesses Amplos)**:
                *   **Localização**: `Brasil`.
                *   **Gênero**: `Todos`.
                *   **Idade**: `18-55+`.
                *   **Interesses**: Adicione 3-5 interesses amplos relacionados ao produto (ex: "Moda e Estilo", "Esportes", "Compras Online").
                *   **Comportamento**: `Interação de vídeo` (últimos 7 dias) em categorias relevantes (ex: "Moda", "Beleza").
            *   **Ad Group 2 (Lookalike de Compradores)**:
                *   **Localização**: `Brasil`.
                *   **Gênero**: `Todos`.
                *   **Idade**: `18-55+`.
                *   **Público Personalizado (Custom Audience)**: Exclua "Compradores nos últimos 30 dias" para evitar impactar quem já converteu.
                *   **Público Similar (Lookalike Audience)**: Crie um público de `1%` similar aos `Complete Payment` dos últimos `90 dias`.
        *   **Orçamento e Agenda**:
            *   **Orçamento Diário**: R$70-R$100 por Ad Group.
            *   **Agenda**: `Rodar Continuamente`.
        *   **Estratégia de Lance e Otimização**:
            *   **Objetivo de Otimização**: `Conversão`.
            *   **Estratégia de Lance**: `Lowest Cost` (Custo Mais Baixo). Inicie com esta opção para coletar dados. Após 3-5 dias e mais de 20 conversões, considere mudar para `Cost Cap` (Limite de Custo) com um valor 10-20% acima do CPA ideal.
    *   **Nível Ad (Anúncio)**: Crie 3-5 anúncios por Ad Group.
        *   **Formato**: `Single Video`.
        *   **Criativo**:
            *   **Vídeos**: 15-60 segundos, formato vertical (9:16), alta resolução, com legendas. Use vídeos no estilo UGC (User-Generated Content) ou demonstrações rápidas do produto. Ex: Vídeo de "antes e depois" de um tênis sendo limpo ou estilizado.
            *   **Música**: Use músicas populares do TikTok que se encaixem no nicho.
            *   **Texto Principal (Ad Text)**: `Descubra o Tênis Urbano [Nome do Produto]! Estilo e conforto para o seu dia a dia. Frete grátis por tempo limitado! 👟✨`
            *   **Chamada para Ação (CTA)**: `Compre Agora`, `Saiba Mais`.
        *   **URL de Destino**: Página do produto específica no seu e-commerce.

### Workflow 2: Otimização de Campanhas Ativas com Baixo ROAS (Abaixo de 1.5x)

Este workflow detalha as etapas para melhorar o desempenho de campanhas que estão gastando orçamento, mas entregando um ROAS insatisfatório.

1.  **Análise Inicial de Dados (24-48h)**:
    *   **Relatórios**: Acesse o TikTok Ads Manager, selecione a campanha e analise métricas por `Ad` (criativo), `Ad Group` (público) e `Campanha`.
    *   **Métricas Chave**: Observe `CPM` (Custo por Mil Impressões), `CTR` (Taxa de Cliques), `CPC` (Custo por Clique), `CPA` (Custo por Aquisição) e `ROAS`.
    *   **Identificação de Gargalos**:
        *   `CPM alto, CTR baixo`: Problema de criativo ou relevância do público. O público não está engajando com o anúncio.
        *   `CTR bom, CPA alto`: O clique é barato, mas a conversão é cara. Problema na página de destino, na oferta ou na qualificação do público.
        *   `ROAS baixo em Ad Group específico`: Indica que aquele público não é rentável.
2.  **Ações de Otimização no Nível Ad (Criativo)**:
    *   **Pausa de Criativos de Baixo Desempenho**: Identifique anúncios com `CTR abaixo de 0.6%` e `ROAS abaixo de 1.0x` após acumular pelo menos 5.000 impressões. Pause-os.
    *   **Upload de Novos Criativos (Refresh)**: Crie 2-3 novos vídeos com abordagens diferentes (ex: depoimento de cliente, humor, foco em um benefício específico). Teste novos ganchos nos primeiros 3 segundos e chamadas para ação.
    *   **Teste de Spark Ads**: Se você tem criadores de conteúdo ou influenciadores, utilize a funcionalidade Spark Ads para impulsionar seus vídeos diretamente da conta deles, aumentando a autenticidade e o engajamento.
3.  **Ações de Otimização no Nível Ad Group (Público e Oferta)**:
    *   **Revisão de Segmentação**:
        *   **Exclusão de Públicos Não Qualificados**: Se o `CPA` estiver alto em um Ad Group de interesses, adicione exclusões para públicos que já converteram ou que demonstraram baixo valor (ex: visitantes do blog que não interagiram com produtos).
        *   **Refinamento de Interesses/Comportamentos**: Teste interesses mais nichados ou combine interesses com comportamentos de vídeo específicos (ex: "assistiu até o final vídeos de moda").
        *   **Teste de Lookalikes Diferentes**: Experimente lookalikes de 1% e 3% de eventos de `AddToCart` ou `InitiateCheckout`, que são públicos mais quentes do que apenas visitantes do site.
    *   **Ajuste de Orçamento e Lances**:
        *   **Redistribuição de Orçamento**: Pause Ad Groups com `ROAS abaixo de 1.0x` ou `CPA muito acima da meta` e realoque o orçamento para Ad Groups que estão performando bem (ex: `ROAS acima de 2.0x`).
        *   **Estratégia de Lance (se já tiver dados)**: Se a campanha tem pelo menos 20 conversões e o `CPA` está consistente, teste a estratégia `Cost Cap` (Limite de Custo). Defina o limite de custo em 10-15% acima do seu `CPA alvo` para dar ao sistema espaço para otimizar.
4.  **Otimização da Página de Destino**:
    *   **Velocidade de Carregamento**: Verifique o tempo de carregamento da página do produto/oferta. Páginas lentas aumentam a taxa de rejeição.
    *   **Clareza da Oferta**: Certifique-se de que a proposta de valor, preço e CTA são extremamente claros e visíveis em dispositivos móveis.
    *   **Prova Social**: Adicione avaliações de clientes, selos de segurança e garantia.

---

## Templates

### Briefing de Campanha TikTok Ads para Lançamento de Produto

```
**NOME DA CAMPANHA:** Lançamento Coleção Cápsula Verão 2024 - [Nome da Marca]
**OBJETIVO DA CAMPANHA:** Conversões no Site (Vendas)
**PRODUTO/SERVIÇO PROMOVIDO:** Coleção Cápsula de Vestidos Leves e Acessórios de Praia
**PÚBLICO-ALVO:**
  - **Demografia:** Mulheres, 20-45 anos, Brasil
  - **Interesses:** Moda e Estilo, Viagens, Praia, Verão, Compras Online, Beleza e Cuidados Pessoais
  - **Comportamentos:** Interação de vídeo (últimos 7 dias) em "Moda" e "Viagens"
  - **Públicos Personalizados:** Lookalike 1% de Compradoras dos últimos 90 dias; Exclusão de Compradoras dos últimos 7 dias.
**ORÇAMENTO DIÁRIO:** R$ 150 (Total de R$ 4.500 para 30 dias)
**DURAÇÃO DA CAMPANHA:** 01/10/2024 - 31/10/2024
**MÉTRICAS DE SUCESSO:**
  - ROAS: Acima de 2.5x
  - CPA (Custo por Aquisição): Máximo R$ 30
  - CTR: Acima de 0.8%
**MENSAGEM CHAVE:** Vista a leveza e o estilo do verão. Coleção exclusiva para você brilhar!
**CALL TO ACTION (CTA):** Compre Agora / Saiba Mais
**URL DE DESTINO:** [link_da_colecao_no_site.com.br]
**IDEIAS DE CRIATIVOS (Vídeos):**
  1.  **UGC (User-Generated Content):** Influenciadora desfilando com os vestidos em cenário de praia/piscina, mostrando detalhes e leveza do tecido.
  2.  **Demonstração Rápida:** Transições rápidas de looks com diferentes peças da coleção, com trilha sonora de verão e texto na tela com benefícios (ex: "Tecido respirável", "Perfeito para o dia a dia").
  3.  **"Get Ready With Me":** Vídeo mostrando o processo de escolha de um look da coleção para um evento de verão, com acessórios.
**OBSERVAÇÕES:** Priorizar vídeos com música em alta no TikTok e legendas para acessibilidade.
```

### Roteiro de Anúncio em Vídeo Curto para TikTok (Formato UGC)

```
**PRODUTO:** Kit de Skincare Anti-Acne "Pele Renovada"
**DURAÇÃO ALVO:** 25-30 segundos
**OBJETIVO:** Gerar interesse e cliques para a página do produto.
**ÁUDIO:** Música popular do TikTok com batida animada, depois fade para voz do narrador.
**CENA 1 (0-3s): Gancho - Problema Comum**
  - **Visual:** Pessoa (atuando) olhando no espelho com expressão de frustração, close em uma espinha. Texto na tela: "Cansada de espinhas?"
  - **Voz Off:** "Você também sofre com a acne que insiste em aparecer?"
**CENA 2 (3-10s): Apresentação da Solução - Produto em Destaque**
  - **Visual:** Transição rápida para as mãos segurando o Kit "Pele Renovada" de forma atraente, mostrando os frascos.
  - **Voz Off:** "Conheça o Kit Pele Renovada! A solução completa para uma pele livre de acne e radiante."
**CENA 3 (10-20s): Demonstração e Benefícios**
  - **Visual:** Pessoa aplicando os produtos do kit na pele (lavando o rosto, aplicando sérum, creme), com close na textura e absorção. Transições rápidas de "antes e depois" de uma pele melhor.
  - **Voz Off:** "Com ingredientes naturais e tecnologia avançada, nosso kit limpa profundamente, reduz inflamações e previne novas espinhas. Veja a diferença!"
**CENA 4 (20-25s): Prova Social / Chamada para Ação**
  - **Visual:** Pequeno trecho de depoimento de cliente (texto na tela ou áudio curto) ou shot de avaliações 5 estrelas. Pessoa sorrindo, com a pele limpa.
  - **Voz Off:** "Milhares de pessoas já transformaram suas peles. Não perca tempo!"
**CENA 5 (25-30s): CTA Final**
  - **Visual:** Tela final com o kit, logo da marca, e texto GRANDE: "Pele Renovada. Clique em 'Compre Agora'!" Botão CTA animado.
  - **Voz Off:** "Clique em 'Compre Agora' e conquiste a pele dos seus sonhos!"
**TEXTO PRINCIPAL DO ANÚNCIO:** "Diga adeus à acne! ✨ O Kit Pele Renovada é seu aliado para uma pele impecável. Resultados visíveis em poucas semanas! #PeleRenovada #Skincare #AntiAcne #TikTokBeleza"
**URL DE DESTINO:** [link_da_pagina_do_produto.com.br]
```

---

## Checklist

- [x] TikTok Pixel base e eventos de conversão (ViewContent, AddToCart, CompletePayment) instalados e verificados.
- [x] Campanha com objetivo "Website Conversions" ou "Lead Generation" configurada.
- [x] Evento de otimização selecionado (ex: "Complete Payment", "Lead").
- [x] Orçamento diário definido (mínimo R$50 por Ad Group para iniciar).
- [x] Segmentação de público-alvo configurada (interesses, lookalikes, exclusões).
- [x] Mínimo de 3-5 criativos em vídeo (9:16) por Ad Group, com legendas e CTA claros.
- [x] Teste de posicionamentos "Automáticos" ativado para explorar Pangle e outros.
- [x] Estratégia de lance inicial "Lowest Cost" selecionada para aprendizado.
- [x] Monitoramento diário de CPM, CTR, CPC, CPA e ROAS iniciado.
- [x] URL de destino verificada para carregamento rápido e otimização mobile.
- [x] Exclusão de público de compradores recentes (últimos 7-30 dias) para campanhas de aquisição.
- [x] Configuração de Dynamic Creative ativada para permitir que o TikTok teste variações de ad copy e criativos.

---

## Métricas de Referência

| Métrica | Benchmark (E-commerce Brasil) | Meta (Otimizado) |
|---------|-------------------------------|------------------|
| CTR     | 0.6% - 1.0%                   | 1.2% - 2.5%      |
| CPC     | R$ 0.80 - R$ 1.50             | R$ 0.50 - R$ 1.00|
| CPM     | R$ 12.00 - R$ 25.00           | R$ 8.00 - R$ 18.00|
| CPA     | R$ 40.00 - R$ 100.00          | R$ 20.00 - R$ 50.00|
| ROAS    | 1.5x - 2.5x                   | 3.0x - 5.0x      |
| Taxa de Conversão | 0.8% - 1.5%           | 1.8% - 3.0%      |

---

## Erros Comuns

1.  **Não Usar o TikTok Pixel Corretamente**: Muitas vezes, o pixel é instalado, mas os eventos de conversão não são configurados ou são configurados de forma errada (ex: "CompletePayment" disparando no carrinho).
    *   **Como evitar**: Utilize a ferramenta "TikTok Pixel Helper" (extensão do Chrome) para verificar se todos os eventos de conversão estão disparando corretamente em cada etapa do funil do seu site. Teste cada evento manualmente (adicionar ao carrinho, iniciar checkout, finalizar compra).
2.  **Criativos Não Nativos ao TikTok**: Anúncios que parecem comerciais tradicionais ou que não seguem o estilo de vídeo curto e autêntico da plataforma (sem legendas, formato horizontal, edição lenta).
    *   **Como evitar**: Crie vídeos com edição dinâmica, ganchos nos primeiros 3 segundos, legendas claras, trilhas sonoras em alta e no formato vertical (9:16). Pense em conteúdo que se misture organicamente com o feed do usuário, como vídeos UGC, tutoriais rápidos ou desafios. Ex: Um anúncio de roupa mostrando "5 maneiras de usar esta peça" em vez de um modelo estático.
3.  **Segmentação de Público Muito Restrita ou Muito Ampla**: Públicos muito pequenos limitam o alcance e encarecem o CPM, enquanto públicos excessivamente amplos gastam dinheiro em pessoas não qualificadas.
    *   **Como evitar**: Comece com uma segmentação por interesses amplos combinada com comportamentos de vídeo e localização. Após coletar dados (pelo menos 50 conversões), crie públicos Lookalike de 1-3% de seus melhores clientes ou de eventos de AddToCart/InitiateCheckout. Exclua públicos que não são relevantes ou que já converteram para evitar desperdício de orçamento.

---

## Dicas Avançadas

1.  **Teste de Múltiplos Ganchos de Vídeo**: Crie 3-5 variações do mesmo anúncio, alterando apenas os primeiros 3-5 segundos (o "gancho"). Um gancho forte é crucial para prender a atenção no TikTok. Ex: Para um produto de beleza, teste ganchos como "Meu segredo para pele perfeita", "Pare de gastar dinheiro à toa!" e "Você nunca mais vai sofrer com...".
2.  **Utilize Spark Ads para Autenticidade**: Colabore com criadores de conteúdo e utilize a funcionalidade Spark Ads para impulsionar seus vídeos diretamente da conta deles. Isso aumenta a prova social, a autenticidade e, muitas vezes, o engajamento e a taxa de conversão, pois os usuários confiam mais em conteúdo vindo de criadores.
3.  **Otimização por Conteúdo Gerado pelo Usuário (UGC)**: Incentive ou crie campanhas com vídeos que simulam conteúdo gerado por usuários. O TikTok valoriza a espontaneidade. Use depoimentos, reviews "desempacotando" o produto, ou vídeos de pessoas usando o produto em situações reais, com uma linguagem informal e genuína.
4.  **Estratégia de Retargeting Dinâmico com Catálogo**: Configure um catálogo de produtos no TikTok Ads Manager e use campanhas de retargeting dinâmico para mostrar anúncios personalizados de produtos que os usuários visualizaram, adicionaram ao carrinho ou iniciaram o checkout em seu site, mas não converteram. Isso tem um ROAS geralmente muito alto.
5.  **Teste de Estratégias de Lances "Cost Cap" (Limite de Custo)**: Após a campanha acumular um volume significativo de conversões (mais de 50), mude a estratégia de lance de "Lowest Cost" para "Cost Cap". Defina o limite de custo em 10-20% acima do seu CPA alvo. Isso permite controlar o custo por aquisição, enquanto o algoritmo ainda busca otimizar, sem ser tão restritivo quanto um "Bid Cap" (Limite de Lance).