---
name: dynamic-ads
description: "Dynamic Ads — Skill especializada para dynamic ads"
license: MIT
metadata:
  version: 1.0.0
  author: Cafe Code AI
  category: 04-anuncios-trafego
  updated: 2026-03-01
risk: safe
---

# Dynamic Ads

Esta skill capacita o Claude a configurar, otimizar e solucionar problemas em campanhas de Dynamic Ads para e-commerce, focando em personalização e performance em Meta, Google e TikTok Ads.

---

## Keywords

Dynamic Product Ads, DPA, Feed de Produtos, Meta CAPI, Google Merchant Center, Catálogo de Produtos, Remarketing Dinâmico, Segmentação por Eventos, Otimização de ROAS, Exclusão de Compradores, Coleções Dinâmicas, Ad Sets Dinâmicos, DSA, Performance Max.

---

## Quick Start

1.  Validar e sincronizar o feed de produtos (XML/CSV) no Gerenciador de Comércio da Meta e Google Merchant Center, garantindo todos os campos obrigatórios.
2.  Implementar o Pixel/API de Conversões da Meta e Google Analytics 4 com eventos de e-commerce (`PageView`, `ViewContent`, `AddToCart`, `Purchase`) configurados com `content_ids` e `value` correspondentes ao feed.
3.  Criar uma campanha de Vendas (Meta) ou Maximizar Conversões (Google Performance Max) selecionando o objetivo de Catálogo/Feed de Produtos.
4.  Configurar o primeiro conjunto de anúncios para remarketing dinâmico, exibindo produtos visualizados ou adicionados ao carrinho nos últimos 7 dias, excluindo compradores recentes.

---

## Core Workflows

### Workflow 1: Configuração e Otimização de Dynamic Product Ads (DPA) em Meta Ads

Este workflow detalha a criação e otimização de campanhas de DPA na plataforma Meta (Facebook e Instagram), focando em remarketing e prospecção de vendas para e-commerce.

**Passo 1: Preparação e Validação do Catálogo de Produtos**
   - **Ação:** Assegurar que o feed de produtos (XML, CSV ou integração via API) esteja perfeitamente sincronizado com o Gerenciador de Comércio da Meta.
   - **Exemplo Concreto:** Verificar no Gerenciador de Comércio se o feed `https://seusite.com/feed-meta.xml` (gerado por Shopify, Loja Integrada, etc.) está sendo atualizado diariamente às 03:00 e se todos os 1.250 itens estão "Ativos" sem erros críticos. Validar que campos como `id`, `availability`, `price`, `image_link` e `link` estão preenchidos e corretos. Um erro comum é `id` duplicado ou `image_link` quebrado.

**Passo 2: Implementação e Teste do Pixel e API de Conversões**
   - **Ação:** Configurar o Pixel da Meta e a API de Conversões para rastrear eventos de e-commerce com os parâmetros corretos, especialmente `content_ids` e `value`.
   - **Exemplo Concreto:** No Gerenciador de Eventos da Meta, usar a ferramenta "Testar Eventos" para simular uma visita à página de produto (disparando `ViewContent` com `content_ids: ["PROD001"]`), adição ao carrinho (`AddToCart` com `content_ids: ["PROD001"], value: 199.99`) e compra (`Purchase` com `content_ids: ["PROD001"], value: 199.99, currency: "BRL"`). Confirmar que os `content_ids` correspondem exatamente aos IDs do catálogo. Implementar a API de Conversões para redundância no envio dos eventos de `Purchase`, com deduplicação configurada.

**Passo 3: Estruturação da Campanha de Vendas (Advantage+ Shopping Campaign)**
   - **Ação:** Criar uma campanha Advantage+ Shopping no Gerenciador de Anúncios, selecionando o catálogo de produtos para otimização.
   - **Exemplo Concreto:** Iniciar uma nova campanha, escolher o objetivo "Vendas" e, na seção "Catálogo", selecionar "Minha Loja Online - Catálogo Principal". Definir um orçamento diário de R$ 200. No nível do Ad Set, criar um conjunto para "Retargeting" com o público "Pessoas que adicionaram ao carrinho mas não compraram nos últimos 14 dias" e outro para "Prospecção" sem segmentação específica, deixando a inteligência da Meta atuar. Excluir o público de "Compradores nos últimos 90 dias" de ambos os Ad Sets.

**Passo 4: Criação de Anúncios Dinâmicos e Testes A/B**
   - **Ação:** Desenvolver criativos dinâmicos que exibem produtos relevantes do catálogo, testando diferentes formatos e sobreposições.
   - **Exemplo Concreto:** No nível do anúncio, selecionar "Anúncio de Catálogo" e escolher o formato "Carrossel". Adicionar um texto principal como "Últimas unidades do que você viu! Garanta já antes que acabe." e um título "dinâmico" como `{{product.name}} | {{product.price}}`. Configurar uma sobreposição de preço "Promoção" para itens com desconto ou "Frete Grátis" para produtos acima de R$150. Criar uma variação do anúncio usando o formato "Coleção" ou "Imagem Única Dinâmica" e comparar o ROAS gerado.

**Passo 5: Otimização de Lances e Monitoramento de Performance**
   - **Ação:** Ajustar as estratégias de lance e monitorar as métricas de performance para maximizar o Retorno sobre o Investimento em Anúncios (ROAS).
   - **Exemplo Concreto:** Para o Ad Set de remarketing, usar a estratégia de lance "Menor Custo" com um limite de ROAS mínimo de 3.0x. Para o Ad Set de prospecção, usar "Menor Custo" sem limite, visando escala. Monitorar o ROAS e o Custo por Compra (CPA) semanalmente. Se um Ad Set de remarketing apresentar ROAS abaixo de 2.5x por mais de 3 dias com gasto significativo (ex: R$100/dia), investigar a saturação do público ou a relevância dos produtos.

### Workflow 2: Implementação de Dynamic Search Ads (DSA) e Performance Max no Google Ads

Este workflow aborda a configuração e otimização de campanhas que utilizam dinamicamente o conteúdo do seu site ou feed de produtos para gerar anúncios no Google.

**Passo 1: Configuração do Feed de Páginas para Dynamic Search Ads (DSA)**
   - **Ação:** Criar uma campanha de DSA que utiliza o conteúdo do seu site para gerar automaticamente títulos e URLs de anúncios.
   - **Exemplo Concreto:** No Google Ads, iniciar uma nova campanha, selecionar "Pesquisa" e, em "Tipo de campanha", escolher "Dynamic Search Ads". Em "Segmentação dinâmica", selecionar "Usar um feed de páginas" e vincular o Google Merchant Center (se aplicável) ou inserir o URL do sitemap XML (`https://seusite.com/sitemap.xml`). Excluir páginas como `/contato`, `/politica-de-privacidade` e `/termos-de-uso` para evitar tráfego irrelevante.

**Passo 2: Definição de Alvos Dinâmicos e Descrições de Anúncio**
   - **Ação:** Criar alvos dinâmicos específicos para controlar quais páginas do seu site serão usadas para gerar anúncios.
   - **Exemplo Concreto:** No Grupo de Anúncios Dinâmicos, criar alvos como "URL contém `/categoria/tenis`" e "Título da Página contém 'Promoção'". Escrever duas linhas de descrição atraentes para os anúncios DSA, como "Encontre os melhores tênis com ofertas imperdíveis!" e "Entrega rápida e segura para todo o Brasil. Aproveite!". O título será gerado dinamicamente pelo Google com base no conteúdo da página.

**Passo 3: Integração com Campanha Performance Max (PMax)**
   - **Ação:** Utilizar o feed de produtos do Google Merchant Center em uma campanha PMax para alcançar clientes em toda a rede do Google (Pesquisa, Display, YouTube, Gmail, Discover).
   - **Exemplo Concreto:** Criar uma campanha Performance Max, vinculando o Google Merchant Center com o feed "Loja Online - Principal". No grupo de recursos, adicionar o "Sinal de Público" com "Públicos Personalizados" que incluam termos de pesquisa como "comprar tênis esportivo" e "promoção eletrônicos", e "Seus dados" incluindo "Visitantes do site nos últimos 30 dias" e "Clientes que adicionaram ao carrinho nos últimos 7 dias". A PMax usará o feed de produtos para criar anúncios dinâmicos em diferentes formatos.

**Passo 4: Otimização e Monitoramento de Termos de Pesquisa**
   - **Ação:** Analisar regularmente os termos de pesquisa que acionam os DSAs e PMax para adicionar palavras-chave negativas.
   - **Exemplo Concreto:** Acessar o relatório "Termos de pesquisa" para a campanha DSA. Se houver termos irrelevantes como "tênis usado" ou "empregos em [marca]", adicioná-los como palavras-chave negativas de correspondência exata ou de frase. Para PMax, embora não haja relatório de termos de pesquisa detalhado, monitorar a performance por categoria de produto e ajustar orçamentos ou feeds conforme necessário.

**Passo 5: Estratégias de Lance para Maximizar Conversões**
   - **Ação:** Configurar a estratégia de lance para otimizar o desempenho das campanhas dinâmicas.
   - **Exemplo Concreto:** Para a campanha DSA, utilizar "Maximizar Conversões" com um CPA alvo de R$ 25. Para a campanha PMax, usar "Maximizar Valor de Conversão" com um ROAS Alvo de 300%. Monitorar o custo por conversão e o valor de conversão para garantir que as metas de negócio estão sendo atingidas.

---

## Templates

### Template de Anúncio Dinâmico para Retargeting (Meta Ads)

```
Formato: Carrossel Dinâmico
Texto Principal: Não perca! Você viu esses produtos incríveis, e eles estão esperando por você.
Título Dinâmico: {{product.name}} | Apenas {{product.price}}
Descrição Dinâmica: Clique e descubra mais detalhes. Frete grátis em compras acima de R$199!
Call to Action: Comprar Agora
Imagens: Imagens do catálogo de produtos relevantes (geradas automaticamente)
Sobreposição (Opcional): Selo de "X% OFF" para produtos com promoção, ou "Últimas Unidades" para baixa disponibilidade.
```

### Template de Linha de Feed de Produtos (Google Merchant Center - CSV)

```csv
id,title,description,link,image_link,price,availability,condition,brand,gtin,mpn,item_group_id,google_product_category,custom_label_0,shipping(country:BR:service:Standard:price)
PROD101,Smart TV 50" 4K HDR Ultra Slim,Desfrute de cores vibrantes e nitidez 4K com a Smart TV de 50 polegadas. Design Ultra Slim com sistema operacional inteligente. Perfeita para sua sala.,https://www.seusite.com/smart-tv-50,https://www.seusite.com/images/tv50.jpg,2999.00 BRL,in stock,new,TechMaster,0123456789012,TM504K,TV_SMART,Eletrônicos > Televisores > TVs Smart,TVs_Premium,BR:::0.00 BRL
PROD102,Fone de Ouvido Bluetooth TWS Pro,Áudio imersivo e sem fio com o TWS Pro. Cancelamento de ruído ativo, bateria de longa duração e ajuste confortável para o dia todo.,https://www.seusite.com/fone-tws-pro,https://www.seusite.com/images/fone_tws.jpg,349.90 BRL,in stock,new,SoundWave,0987654321098,SWTWSPro,FONE_AUDIO,Eletrônicos > Áudio > Fones de Ouvido,Audio_Portatil,BR:::15.00 BRL
```

---

## Checklist

- [x] Feed de produtos validado e atualizado diariamente em todas as plataformas (Meta, Google Merchant Center, TikTok Catalog).
- [x] Pixel/API de Conversões implementado com `content_ids` e `value` correspondentes aos IDs do feed e testados via Eventos Manager.
- [x] Eventos de e-commerce (`ViewContent`, `AddToCart`, `Purchase`) configurados e disparando corretamente com dados relevantes.
- [x] Campanhas de Vendas (Meta) ou Performance Max (Google) ativas e vinculadas ao catálogo de produtos.
- [x] Ad Sets/Grupos de Anúncios para remarketing dinâmico configurados, excluindo compradores recentes (90 dias).
- [x] Testes A/B de criativos dinâmicos (formatos, textos, sobreposições) em andamento para otimização de CTR e ROAS.
- [x] Monitoramento regular de erros no feed de produtos (itens reprovados, avisos) e ações corretivas aplicadas.
- [x] Análise semanal dos termos de pesquisa (para DSA) e adição de palavras-chave negativas relevantes.
- [x] Otimização de lances e orçamentos baseada em performance (ROAS, CPA) e metas de negócio.
- [x] Segmentação de públicos avançada aplicada (ex: usuários que adicionaram ao carrinho mas não iniciaram checkout, clientes de alto valor).
- [x] Uso de regras de automação para pausar/ativar campanhas ou ad sets com base em métricas de performance (ex: ROAS < X).
- [x] Validação da atribuição de conversão (janela de 7 dias clique/1 dia visualização) para avaliar o impacto real dos Dynamic Ads.

---

## Métricas de Referência

| Métrica | Benchmark (E-commerce) | Meta (Otimizado) |
|---------|------------------------|------------------|
| ROAS (Retargeting DPA) | 3.0x - 5.0x            | > 5.0x           |
| ROAS (Prospecção DPA) | 1.5x - 2.5x            | > 2.5x           |
| CTR (DPA Meta)          | 0.8% - 1.5%            | > 1.5%           |
| CTR (DSA Google)        | 2.0% - 4.0%            | > 4.0%           |
| CPC (Médio)             | R$ 0.80 - R$ 2.50      | < R$ 1.50        |
| Taxa de Conversão (DPA) | 1.5% - 3.0%            | > 3.0%           |

---

## Erros Comuns

1.  **Feed de Produtos Desatualizado/Incorreto**: Anúncios exibem informações erradas (preços antigos, produtos esgotados, links quebrados), prejudicando a experiência do usuário e o ROAS.
    *   **Como evitar**: Configurar atualizações diárias ou em tempo real do feed e monitorar os relatórios de diagnóstico no Gerenciador de Comércio (Meta) ou Google Merchant Center. Implementar alertas automáticos para itens reprovados.
    *   **Exemplo**: Um produto com `availability: out of stock` no feed ainda aparece como disponível no anúncio, gerando cliques desperdiçados e frustração.

2.  **Eventos de Pixel/API de Conversões Incorretos ou Descasados**: O parâmetro `content_ids` enviado pelo Pixel/API não corresponde exatamente aos IDs do catálogo, impedindo que a plataforma personalize os anúncios dinâmicos corretamente.
    *   **Como evitar**: Usar a ferramenta "Testar Eventos" no Gerenciador de Eventos da Meta ou "DebugView" no GA4 para garantir que os IDs dos produtos no site correspondem precisamente aos IDs do feed. Desenvolver uma lógica de mapeamento robusta.
    *   **Exemplo**: O evento `ViewContent` envia `SKU123` mas o feed tem `PROD123` para o mesmo item, resultando em retargeting genérico em vez de específico ao produto.

3.  **Exclusão Inadequada de Compradores Recentes**: Anunciar produtos para clientes que já realizaram uma compra recente, desperdiçando orçamento em um público com menor probabilidade de recompra imediata do mesmo item.
    *   **Como evitar**: Criar um público personalizado de "Compradores (últimos 90 dias)" baseado no evento `Purchase` e excluí-lo de todas as campanhas de remarketing dinâmico e, em alguns casos, de prospecção.
    *   **Exemplo**: Um usuário que comprou um "Fone Bluetooth" ainda vê anúncios para o mesmo fone nas 24 horas seguintes, quando o foco deveria ser em upsell ou cross-sell.

---

## Dicas Avançadas

1.  **Segmentação por Valor de Cliente (LTV) com `custom_label`**: Utilize os campos `custom_label_0` a `custom_label_4` no seu feed para segmentar produtos por margem, preço ou categoria de alto valor. Isso permite exibir anúncios dinâmicos de produtos de maior lucratividade para públicos mais qualificados.
    *   **Exemplo Prático**: Marcar no feed produtos de "Alta Margem" em `custom_label_0` e criar um Ad Set de remarketing que visa apenas usuários que visualizaram produtos com `custom_label_0 = "Alta Margem"`, otimizando o ROAS.

2.  **Otimização de Carrossel Dinâmico com Cards Estáticos**: No Meta Ads, crie anúncios de carrossel dinâmicos que intercalam os produtos do seu catálogo com cards estáticos personalizados (ex: "Frete Grátis acima de R$X", "Testemunhos de Clientes", "Selo de Confiança"). Isso melhora o engajamento e a credibilidade.
    *   **Exemplo Prático**: Um carrossel exibe `Produto A`, seguido por um slide com "Mais de 10.000 clientes satisfeitos!", depois `Produto B`, e um slide com "Entrega Rápida em todo o Brasil".

3.  **Uso de Regras de Automação para Performance de Ad Sets**: Configure regras automatizadas para pausar ou ajustar lances em Ad Sets de remarketing dinâmico que não atingem um ROAS mínimo predefinido ou que excedem um CPA máximo.
    *   **Exemplo Prático**: `SE ROAS < 2.5 E Gasto > R$150 NOS ÚLTIMOS 3 DIAS, PAUSAR AD SET`. Isso evita o desperdício de orçamento em segmentos com baixo desempenho.

4.  **Audiências de Valor com Otimização de Valor (Meta Value Optimization)**: Em vez de otimizar para `Purchase` genérico, crie campanhas com o objetivo "Valor" para que o algoritmo da Meta busque usuários com maior probabilidade de gerar compras de alto valor, utilizando dados históricos de valor de compra do seu feed.
    *   **Exemplo Prático**: Uma campanha de Vendas otimizada para "Valor (ROAS)" com um ROAS alvo de 4.0x, incentivando a plataforma a priorizar usuários que tendem a gastar mais em cada transação.

5.  **Testes de Janela de Retargeting Dinâmico por Categoria de Produto**: Diferentes categorias de produtos podem ter ciclos de compra distintos. Teste janelas de remarketing dinâmico variadas (ex: 3 dias, 7 dias, 14 dias) em Ad Sets separados para categorias específicas para identificar o período ideal de reengajamento.
    *   **Exemplo Prático**: Para eletrônicos (decisão mais longa), um remarketing de 14 dias pode ser mais eficaz. Para roupas (decisão mais rápida), 7 dias pode gerar melhor ROAS, evitando saturação.