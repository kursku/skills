---
name: ecommerce-analytics
description: "Ecommerce Analytics — Skill especializada para ecommerce analytics"
license: MIT
metadata:
  version: 1.0.0
  author: Cafe Code AI
  category: 15-analytics-dados
  updated: 2026-03-01
risk: safe
---

# Ecommerce Analytics

Esta skill capacita o Claude a atuar como um analista de ecommerce, configurando, analisando e otimizando a performance de lojas online através de dados do Google Analytics 4 (GA4) e outras ferramentas.

---

## Keywords

Google Analytics 4, GA4, Ecommerce, Funil de Compra, Taxa de Conversão, ROAS, LTV, Atribuição, DataLayer, Enhanced Ecommerce, Eventos GA4, Explorações GA4, Looker Studio, Custo por Aquisição, Valor Médio do Pedido, Segmentação de Audiência.

---

## Quick Start

1.  **Verificar Configuração GA4 Enhanced Ecommerce**: Navegue em "Administrador" > "Configurações de dados" > "Coleta de dados" no GA4 e assegure que o tracking de ecommerce está ativo e que os eventos `view_item`, `add_to_cart`, `begin_checkout`, `purchase` estão sendo coletados corretamente.
2.  **Acessar Relatório de Monetização**: No GA4, vá para "Relatórios" > "Monetização" > "Visão geral" para uma análise rápida das receitas, transações e valor médio do pedido.
3.  **Criar Exploração de Funil de Compra**: Em "Explorar" > "Funil de exploração", configure um funil com os passos: `view_item` > `add_to_cart` > `begin_checkout` > `purchase` para identificar gargalos.
4.  **Avaliar Modelos de Atribuição**: No GA4, acesse "Publicidade" > "Modelos de atribuição" > "Comparação de modelos" para analisar a performance de canais sob diferentes perspectivas (ex: Último Clique vs. Baseado em Dados).

---

## Core Workflows

### Workflow 1: Análise Detalhada do Funil de Compra e Otimização de Produtos

Este workflow foca em identificar onde os usuários estão abandonando o funil de compra e quais produtos estão performando melhor ou pior, permitindo otimizações direcionadas.

**Passos Detalhados:**

1.  **Acessar Exploração de Funil de Compra no GA4**:
    *   No painel do Google Analytics 4, navegue até a seção "Explorar" no menu lateral esquerdo.
    *   Selecione "Funil de exploração" para criar um novo relatório ou abrir um existente.
    *   **Configuração do Funil**: Defina os passos sequenciais que representam a jornada de compra:
        *   Passo 1: `view_item` (Visualização de Item)
        *   Passo 2: `add_to_cart` (Adição ao Carrinho)
        *   Passo 3: `begin_checkout` (Início do Checkout)
        *   Passo 4: `purchase` (Compra)
    *   **Aplicação de Segmentos**: Adicione um segmento de "Usuários que visualizaram produtos da categoria 'Eletrônicos'" ou "Usuários que vieram de campanhas de Google Ads" para análises mais granulares.
    *   **Exemplo de Interpretação**: Se o funil mostra uma queda de 70% entre `add_to_cart` e `begin_checkout` para usuários mobile, isso indica um problema na experiência do carrinho ou na página de checkout em dispositivos móveis.

2.  **Identificar Produtos com Baixa Performance no Funil**:
    *   No mesmo relatório de funil de exploração, adicione a dimensão "Nome do item" (item_name) ou "ID do item" (item_id) como uma "Dimensão de detalhamento".
    *   **Análise por Produto**: Observe a taxa de abandono em cada etapa para produtos específicos. Um produto X pode ter alta visualização (`view_item`), mas baixa adição ao carrinho (`add_to_cart`), sugerindo problemas na descrição, imagens ou preço.
    *   **Exemplo de Ação**: Se o "Smartwatch Modelo Alpha" tem 1000 `view_item` mas apenas 50 `add_to_cart` (5% de taxa de adição), enquanto a média da loja é 15%, é preciso revisar a página do produto Alpha.

3.  **Analisar Relatório de Itens de Ecommerce (GA4)**:
    *   Navegue para "Relatórios" > "Monetização" > "Itens de ecommerce".
    *   **Métricas Chave**: Analise "Receita do item", "Visualizações do item", "Adições ao carrinho do item", "Taxa de compra do item".
    *   **Exemplo de Insights**: Um produto com alta "Visualização do item" e baixa "Taxa de compra do item" (ex: 10.000 visualizações, 0.5% de taxa de compra) indica que o produto é interessante, mas não convence na hora da compra. Compare com um produto de 1.000 visualizações e 5% de taxa de compra. O primeiro tem potencial de otimização maior.

4.  **Recomendações e Otimizações**:
    *   **Para gargalos no checkout**: Otimizar formulários, oferecer mais opções de pagamento, exibir custos de frete claramente no carrinho.
    *   **Para produtos com baixa adição ao carrinho**: Melhorar descrições de produtos, adicionar mais imagens de alta qualidade, incluir reviews de clientes, testar diferentes preços ou promoções.
    *   **Para produtos com alta visualização e baixa compra**: Revisar a proposta de valor na página do produto, comparar preços com concorrentes, adicionar garantias ou selos de segurança.

### Workflow 2: Análise de Atribuição de Receita e Otimização de Investimento em Marketing

Este workflow foca em entender como os diferentes canais de marketing contribuem para as vendas, permitindo alocar orçamentos de forma mais eficaz.

**Passos Detalhados:**

1.  **Acessar Relatório de Modelos de Atribuição (GA4)**:
    *   No GA4, vá para a seção "Publicidade" no menu lateral esquerdo.
    *   Selecione "Atribuição" > "Comparação de modelos".
    *   **Configuração de Modelos**: Compare pelo menos três modelos de atribuição para entender diferentes perspectivas de valor:
        *   **Último Clique**: O crédito total vai para o último canal que gerou a conversão.
        *   **Primeiro Clique**: O crédito total vai para o primeiro canal que iniciou a jornada.
        *   **Baseado em Dados (Data-Driven)**: O GA4 usa aprendizado de máquina para atribuir crédito fracionado a todos os canais no caminho da conversão, com base nos dados reais da sua propriedade.
    *   **Exemplo de Interpretação**: Se o Google Organic Search recebe 30% da receita no modelo de "Último Clique" mas 60% no modelo "Primeiro Clique", isso sugere que o SEO é excelente para atrair novos usuários no início da jornada, mesmo que outros canais (ex: Google Ads) fechem a venda.

2.  **Analisar Caminhos de Conversão (GA4)**:
    *   Dentro de "Publicidade" > "Atribuição", selecione "Caminhos de conversão".
    *   **Visualização de Sequências**: Este relatório mostra as sequências de canais que os usuários percorreram antes de converter.
    *   **Exemplo de Insights**: Identifique sequências comuns como "Google Organic > Direct > Email" ou "Social Media > Google Ads > Direct". Isso revela quais canais trabalham juntos e em que ordem. Se "Email" aparece frequentemente como o último clique em caminhos longos, a automação de email de remarketing pode ser muito eficaz.

3.  **Calcular ROAS por Canal (Return on Ad Spend)**:
    *   Exporte os dados de receita por canal (usando o modelo Baseado em Dados) do GA4 e os custos de investimento de cada canal (Google Ads, Facebook Ads, etc.).
    *   **Fórmula ROAS**: `ROAS = (Receita Gerada pelo Canal / Custo do Canal) * 100%`
    *   **Exemplo de Cálculo**: Se o Google Ads gerou R$ 10.000 em receita (modelo baseado em dados) com um custo de R$ 2.000, o ROAS é de (10.000 / 2.000) * 100% = 500%.
    *   **Interpretação**: Um ROAS de 500% significa que para cada R$ 1 investido, R$ 5 retornaram em receita. Compare isso com outros canais. Um ROAS de 150% para Facebook Ads pode ser bom se o canal for mais eficaz no topo do funil (primeiro clique).

4.  **Otimização de Orçamento com Base na Atribuição**:
    *   **Alocação Estratégica**: Invista mais em canais que demonstram alto ROAS no modelo Baseado em Dados e que contribuem significativamente para a receita.
    *   **Canais de Topo de Funil**: Não ignore canais com bom desempenho nos modelos de "Primeiro Clique", pois eles são cruciais para a aquisição de novos usuários. Ex: Se o Instagram orgânico tem alto "Primeiro Clique", considere investir em conteúdo para atrair novos públicos.
    *   **Canais de Fundo de Funil**: Reforce canais que aparecem como "Último Clique" em caminhos de conversão complexos, como campanhas de remarketing ou email marketing, pois eles são eficazes na finalização da venda.

---

## Templates

### Template de Configuração de Evento de Compra no DataLayer (GA4)

```javascript
window.dataLayer = window.dataLayer || [];
dataLayer.push({
  event: 'purchase',
  ecommerce: {
    transaction_id: 'TID-123456789', // ID único da transação
    affiliation: 'Loja Exemplo', // Nome da loja ou afiliado
    value: 125.99, // Valor total da compra (excluindo impostos e frete se aplicável)
    tax: 5.00, // Valor do imposto
    shipping: 10.00, // Valor do frete
    currency: 'BRL', // Moeda da transação
    coupon: 'VERAO2024', // Código do cupom aplicado, se houver
    items: [
      {
        item_id: 'SKU-001',
        item_name: 'Camiseta Básica Algodão',
        item_brand: 'Marca A',
        item_category: 'Vestuário',
        item_variant: 'Azul-M',
        price: 49.99,
        quantity: 2,
        coupon: 'DESCONTO10' // Cupom aplicado a este item, se diferente
      },
      {
        item_id: 'SKU-002',
        item_name: 'Calça Jeans Slim Fit',
        item_brand: 'Marca B',
        item_category: 'Vestuário',
        item_variant: 'Preto-G',
        price: 65.00,
        quantity: 1
      }
    ]
  }
});
```

### Template de Estrutura de Relatório Personalizado no Looker Studio para Performance de Produtos

```
Título: Performance de Produtos - Últimos 30 Dias

Página 1: Visão Geral da Performance de Produtos

  Gráfico 1: Tabela de Produtos por Receita
    Dimensão: Nome do Item (item_name)
    Métrica: Receita do Item (item_revenue)
    Métrica: Quantidade Vendida (item_quantity)
    Métrica: Preço Médio do Item (item_revenue / item_quantity)
    Filtro: Evento = 'purchase'
    Ordenação: Receita do Item (Decrescente)

  Gráfico 2: Top 10 Produtos por Taxa de Adição ao Carrinho
    Dimensão: Nome do Item (item_name)
    Métrica: Taxa de Adição ao Carrinho (add_to_cart_rate = (total_add_to_cart_events / total_view_item_events) * 100)
    Filtro: Evento IN ('view_item', 'add_to_cart')
    Ordenação: Taxa de Adição ao Carrinho (Decrescente)

  Gráfico 3: Gráfico de Barras - Receita por Categoria de Produto
    Dimensão: Categoria do Item (item_category)
    Métrica: Receita Total (total_revenue)

Página 2: Funil de Conversão por Produto

  Gráfico 1: Tabela de Funil de Conversão
    Linhas: Nome do Item (item_name)
    Colunas (Métricas de Funil):
      - Visualizações de Item (total_view_item_events)
      - Adições ao Carrinho (total_add_to_cart_events)
      - Inícios de Checkout (total_begin_checkout_events)
      - Compras (total_purchase_events)
      - Taxa de Conversão de Visualização para Compra ((total_purchase_events / total_view_item_events) * 100)
    Filtro: Data dos Últimos 30 Dias
    Ordenação: Compras (Decrescente)

  Gráfico 2: Funil de Barras Empilhadas - Abandono por Etapa
    Dimensão: Etapa do Funil (ex: 'view_item', 'add_to_cart', 'begin_checkout', 'purchase')
    Métrica: Contagem de Eventos
    Segmentação: Dispositivo (mobile, desktop)
```

---

## Checklist

- [x] Configuração correta de eventos `view_item`, `add_to_cart`, `begin_checkout`, `purchase` no GA4.
- [x] Verificação da passagem de parâmetros de `item_id`, `item_name`, `price`, `quantity` para cada item nos eventos de ecommerce.
- [x] Implementação de `transaction_id` único para prevenir duplicação de transações.
- [x] Monitoramento regular do relatório "Monetização > Visão Geral" no GA4 para anomalias.
- [x] Criação e análise de "Explorações de Funil" para identificar gargalos na jornada do cliente.
- [x] Análise de "Caminhos de Conversão" e comparação de "Modelos de Atribuição" para entender a contribuição de cada canal.
- [x] Segmentação de relatórios por dimensões como "Dispositivo", "Origem/Mídia" e "Categoria de Produto" para insights mais profundos.
- [x] Configuração de métricas personalizadas no GA4 (se necessário) para dados específicos do negócio.
- [x] Integração do GA4 com plataformas de anúncios (Google Ads, Search Console) para dados de custo e performance.
- [x] Criação de um dashboard de ecommerce no Looker Studio com as métricas mais relevantes.

---

## Métricas de Referência

| Métrica                         | Benchmark (Varejo Online Geral) | Meta (Otimizado) |
|---------------------------------|---------------------------------|------------------|
| Taxa de Conversão (GA4)         | 1.5% - 2.5%                     | 3.0% - 5.0%+     |
| Valor Médio do Pedido (AOV)     | R$ 150 - R$ 300                 | R$ 350+          |
| Taxa de Abandono de Carrinho    | 60% - 80%                       | < 50%            |
| Retorno sobre Investimento em Anúncios (ROAS) | 200% - 400%                     | 500%+            |
| Custo por Aquisição (CPA)       | Varia muito por nicho           | Menor que LTV/3  |
| Taxa de Adição ao Carrinho      | 8% - 15%                        | 20%+             |

---

## Erros Comuns

1.  **Duplicação de Transações no GA4**: Ocorre quando o evento `purchase` é disparado múltiplas vezes (ex: usuário recarregando a página de agradecimento).
    *   **Como evitar**: Implementar uma lógica no DataLayer ou Tag Manager para que o `transaction_id` seja verificado antes de disparar o evento, garantindo que cada ID de transação seja enviado apenas uma vez para o GA4. Um exemplo é armazenar o `transaction_id` em um cookie ou `sessionStorage` após o primeiro envio.

2.  **Tracking Incompleto do Funil de Ecommerce**: Faltam eventos como `add_to_cart` ou `begin_checkout`, impossibilitando a análise completa da jornada do cliente.
    *   **Como evitar**: Realizar um teste de ponta a ponta usando o "DebugView" do GA4. Simule uma compra completa e verifique se todos os eventos (view_item, add_to_cart, begin_checkout, purchase) e seus respectivos parâmetros de item estão sendo registrados corretamente na sequência. Ex: Verifique se `item_list_name` está presente em `view_item_list` e `item_name` em `view_item`.

3.  **Interpretação Equivocada dos Modelos de Atribuição**: Focar apenas no modelo "Último Clique" pode subvalorizar canais importantes para a descoberta e consideração.
    *   **Como evitar**: Sempre comparar múltiplos modelos (ex: Último Clique, Primeiro Clique, Linear, Baseado em Dados) no relatório "Comparação de Modelos" do GA4. Use o modelo "Baseado em Dados" como referência para entender a contribuição real de cada canal ao longo da jornada e alocar o orçamento de marketing de forma mais inteligente. Por exemplo, um canal de social media que inicia muitas jornadas pode ter um ROAS baixo no último clique, mas ser crucial para o funil.

---

## Dicas Avançadas

1.  **Implementação de User-ID e Cálculos de LTV**: Configure o User-ID no GA4 para unificar a jornada do usuário em diferentes dispositivos e sessões. Use os dados do User-ID para calcular o Lifetime Value (LTV) real dos clientes, segmentando-os por canal de aquisição e perfil demográfico. Isso permite identificar quais canais atraem clientes de maior valor a longo prazo, otimizando o investimento de aquisição.
2.  **Análise de Coortes para Retenção**: Utilize a "Exploração de Coortes" no GA4 para analisar a retenção de clientes por semana ou mês de aquisição. Isso revela a eficácia das estratégias de retenção pós-compra e identifica coortes de clientes que são mais propensas a recomprar. Por exemplo, uma coorte de usuários adquiridos em uma promoção específica pode ter uma retenção significativamente menor.
3.  **Integração com Ferramentas de BI (Looker Studio, Power BI)**: Exporte os dados do GA4 para um data warehouse (ex: BigQuery) e conecte-o a ferramentas de Business Intelligence como Looker Studio ou Power BI. Isso permite a criação de dashboards muito mais complexos e personalizados, combinando dados de GA4 com sistemas de CRM, custos de anúncios, e dados de estoque para uma visão 360º.
4.  **Uso de Audiências Preditivas no GA4**: Aproveite as audiências preditivas do GA4 (ex: "Compradores prováveis de 7 dias", "Churn provável de 7 dias") para criar campanhas de remarketing altamente segmentadas. Por exemplo, exporte uma audiência de "Compradores prováveis de 7 dias" para o Google Ads e Meta Ads para direcionar ofertas específicas e acelerar a conversão.
5.  **Análise de Produtos Complementares (Cross-sell/Up-sell)**: Além das métricas básicas, utilize relatórios personalizados (Explorações) para identificar quais produtos são frequentemente comprados juntos (cross-sell) ou quais produtos os clientes visualizam após comprar um item específico (up-sell). Isso informa estratégias de recomendação de produtos no site, email marketing e até mesmo a criação de bundles de produtos.