---
name: retargeting-strategy
description: "Retargeting Strategy — Skill especializada para retargeting strategy"
license: MIT
metadata:
  version: 1.0.0
  author: Cafe Code AI
  category: 04-anuncios-trafego
  updated: 2026-03-01
risk: safe
---

# Retargeting Strategy

Esta skill capacita a criação e otimização de campanhas de retargeting altamente eficazes em plataformas como Meta Ads, Google Ads e TikTok Ads, focando em públicos de alto valor.

---

## Keywords

Retargeting, Remarketing, Públicos Personalizados, Audiências de Retargeting, Pixel de Rastreamento, Conversion API, Campanhas de Vendas, Recuperação de Carrinho, Cross-selling, Upselling, LTV, ROAS Otimizado.

---

## Quick Start

1.  **Verificar Implementação do Pixel/Tag:** Assegurar que o Meta Pixel, Google Tag (com Google Ads Tag e GA4) e TikTok Pixel estejam instalados corretamente em todas as páginas do site, com eventos de conversão (PageView, ViewContent, AddToCart, InitiateCheckout, Purchase) configurados e testados via Debug Mode.
2.  **Segmentar Audiências-Chave no Gerenciador:** Criar públicos de retargeting no Meta Business Suite e Google Ads com base em eventos específicos: visitantes dos últimos 7/14/30 dias, usuários que adicionaram ao carrinho mas não compraram nos últimos 3 dias, clientes que compraram há 60-90 dias.
3.  **Definir Orçamento de Retargeting:** Alocar 10-20% do orçamento total de mídia paga para campanhas de retargeting, priorizando grupos de maior intenção de compra, como "carrinhos abandonados".
4.  **Criar Anúncios Focados na Próxima Ação:** Desenvolver criativos e textos que abordem a objeção específica ou incentivem o próximo passo, como um desconto para finalização de compra ou apresentação de um produto complementar.

---

## Core Workflows

### Workflow 1: Recuperação de Carrinho Abandonado com Oferta Dinâmica (Meta Ads)

**Objetivo:** Converter usuários que adicionaram produtos ao carrinho mas não finalizaram a compra, utilizando anúncios dinâmicos de produtos e um incentivo de desconto.

1.  **Configuração do Evento `AddToCart` e `Purchase`:**
    *   **Ação:** Verificar no Gerenciador de Eventos do Meta Business Suite se os eventos `AddToCart` e `Purchase` estão sendo disparados corretamente. O `AddToCart` deve enviar o `content_ids` e `value` do produto. O `Purchase` deve enviar `content_ids`, `value` e `currency`.
    *   **Exemplo:** Um usuário adiciona um "Tênis Esportivo X" (ID: 123) ao carrinho, o pixel dispara `AddToCart` com `{content_ids: ['123'], value: 299.90, currency: 'BRL'}`.

2.  **Criação de Catálogo de Produtos (Se ainda não tiver):**
    *   **Ação:** Fazer upload de um catálogo de produtos via feed RSS/XML/CSV no Gerenciador de Comércio, garantindo que os IDs dos produtos no feed correspondam aos `content_ids` enviados pelo pixel.
    *   **Exemplo:** O catálogo deve ter um item com `id: 123`, `title: Tênis Esportivo X`, `price: 299.90`, `link: [URL do produto]`.

3.  **Criação do Público Personalizado "Carrinho Abandonado":**
    *   **Ação:** No Meta Business Suite, ir em "Públicos" -> "Criar Público Personalizado" -> "Site".
    *   **Configuração:**
        *   **Fonte:** Seu Pixel.
        *   **Eventos:** "Pessoas que adicionaram itens ao carrinho" (AddToCart).
        *   **Excluir:** "Pessoas que realizaram uma compra" (Purchase).
        *   **Retenção:** 3 dias.
        *   **Nome:** "Retargeting - Carrinho Abandonado 3D".
    *   **Exemplo:** Este público terá usuários que ativaram `AddToCart` nos últimos 3 dias, mas não ativaram `Purchase` no mesmo período.

4.  **Configuração da Campanha de Vendas (Advantage+ Shopping Campaign ou Conversões):**
    *   **Ação:** No Gerenciador de Anúncios, criar uma nova campanha.
    *   **Objetivo:** "Vendas" (Sales).
    *   **Tipo de Campanha:** "Advantage+ Shopping Campaign" (para otimização automática) ou "Campanha de Conversões" com otimização para "Compras".
    *   **Orçamento:** Orçamento Diário de R$ 50,00.
    *   **Público:** Selecionar o público personalizado "Retargeting - Carrinho Abandonado 3D".
    *   **Exemplo:**
        *   Campanha: `REC-CARRINHO-DPA-OFERTA-META`
        *   Conjunto de Anúncios: `PUBLICO-CARRINHO-3D-EXC-COMPRA`
        *   Orçamento: `Diário R$ 50,00`
        *   Otimização: `Compras`

5.  **Criação dos Anúncios Dinâmicos de Produto (DPA):**
    *   **Ação:** No nível do anúncio, selecionar "Formato" como "Carrossel" ou "Coleção" e "Tipo de Criativo" como "Anúncios Dinâmicos".
    *   **Configuração:** Vincular ao catálogo de produtos. Usar um modelo de texto com variável de produto e um incentivo de desconto.
    *   **Exemplo de Texto:**
        *   **Título:** "Sua compra está quase lá! 🛒"
        *   **Corpo:** "Percebemos que você adicionou {product.name} ao seu carrinho. Não perca! Use o cupom **VOLTA10** e ganhe 10% OFF na finalização. Clique e finalize agora!"
        *   **Call to Action:** "Comprar Agora"
        *   **Link:** `{product.link}` (o Meta Ads preencherá automaticamente com o link do produto abandonado)
    *   **Criativo:** O Meta Ads puxará automaticamente as imagens dos produtos do catálogo.

6.  **Monitoramento e Otimização:**
    *   **Ação:** Acompanhar métricas como ROAS, Custo por Compra, CTR, Frequência.
    *   **Exemplo:** Se o ROAS estiver abaixo de 3.0 após 5 dias, testar outro criativo, ajustar o desconto (ex: frete grátis em vez de 10% OFF), ou ampliar a retenção do público para 5 dias.

### Workflow 2: Retargeting de Engajamento para Lançamento de Produto (Google Ads - Display)

**Objetivo:** Aquecer e converter usuários que interagiram com conteúdo do site (blog posts, páginas de produto específicas) mas não converteram, preparando-os para um lançamento de produto ou oferta especial.

1.  **Configuração de Audiências no Google Analytics 4 (GA4):**
    *   **Ação:** No GA4, criar audiências baseadas em eventos e páginas visitadas.
    *   **Exemplo:**
        *   **Audiência 1:** "Visitantes de Blog - Produto X"
            *   **Condição:** `event_name = 'page_view'` E `page_location` contém `/blog/lancamento-produto-x`
            *   **Retenção:** 30 dias.
        *   **Audiência 2:** "Visitantes de Página de Produto - Categoria Y"
            *   **Condição:** `event_name = 'page_view'` E `page_location` contém `/produtos/categoria-y`
            *   **Retenção:** 60 dias.
    *   **Importante:** Garantir que o GA4 esteja vinculado à conta do Google Ads para que as audiências sejam importadas.

2.  **Criação da Campanha de Display no Google Ads:**
    *   **Ação:** No Google Ads, criar uma nova campanha.
    *   **Objetivo:** "Vendas" ou "Leads" (dependendo do estágio do lançamento). Para engajamento, "Tráfego do site" pode ser usado inicialmente.
    *   **Tipo de Campanha:** "Rede de Display" -> "Campanha de Display Padrão".
    *   **Orçamento:** Orçamento Diário de R$ 30,00.

3.  **Configuração do Grupo de Anúncios e Segmentação:**
    *   **Ação:** No grupo de anúncios, selecionar a segmentação por "Públicos".
    *   **Públicos:** Procurar e adicionar as audiências importadas do GA4: "Visitantes de Blog - Produto X" e "Visitantes de Página de Produto - Categoria Y".
    *   **Exclusões:** Excluir "Compradores (GA4)" ou "Clientes Recentes (lista de email)".
    *   **Exemplo:**
        *   Campanha: `RET-LANCAMENTO-PROD-Z-DISPLAY`
        *   Grupo de Anúncios: `PUBLICO-ENGAGEMENT-BLOG-PROD-X`
        *   Segmentação: `Público-alvo > Como eles interagiram com sua empresa > Visitantes de Blog - Produto X (GA4)`

4.  **Criação de Anúncios Responsivos de Display:**
    *   **Ação:** Fazer upload de imagens de alta qualidade (1.91:1 e 1:1), logotipos, e criar vários títulos e descrições.
    *   **Exemplo de Conteúdo:**
        *   **Título Curto (até 30 caracteres):** "Novo Produto Z Chegando!", "Descubra o Futuro!"
        *   **Título Longo (até 90 caracteres):** "Você viu nosso blog sobre o Produto Z? Prepare-se para a inovação!"
        *   **Descrição (até 90 caracteres):** "Seja um dos primeiros a conhecer o Produto Z. Inovação e performance esperam por você."
        *   **Nome da Empresa:** Sua Marca
        *   **URL Final:** `[URL da página de pré-lançamento/cadastro]`
        *   **Call to Action:** "Saiba Mais" / "Pré-cadastre-se"
    *   **Dica:** Os anúncios devem ser visualmente atraentes e alinhados com a identidade do produto a ser lançado.

5.  **Monitoramento e Otimização:**
    *   **Ação:** Acompanhar métricas de Display como