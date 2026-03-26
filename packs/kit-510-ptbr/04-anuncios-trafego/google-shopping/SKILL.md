---
name: google-shopping
description: "Google Shopping — Skill especializada para google shopping"
license: MIT
metadata:
  version: 1.0.0
  author: Cafe Code AI
  category: 04-anuncios-trafego
  updated: 2026-03-01
risk: safe
---

# Google Shopping

Esta skill capacita o Claude a planejar, configurar e otimizar campanhas de Google Shopping, desde a criação do feed de produtos até a análise de ROAS e estratégias avançadas.

---

## Keywords

Google Shopping, Merchant Center, Feed de Produtos, Campanhas PMax, Otimização de Lances, ROAS, CPC, CTR, Estratégias de Lances, Google Ads, Anúncios de Produto, SKU, GTIN, Atributos de Produto.

---

## Quick Start

1.  Crie e configure sua conta no Google Merchant Center, verificando a propriedade do domínio.
2.  Gere e envie um feed de produtos XML ou CSV válido para o Merchant Center, garantindo que todos os atributos obrigatórios estejam preenchidos.
3.  Vincule o Google Merchant Center à sua conta do Google Ads para permitir a criação de campanhas de Shopping.
4.  Crie uma campanha Performance Max (PMax) no Google Ads, selecionando o tipo de objetivo "Vendas" e incluindo o feed de produtos como fonte de inventário.
5.  Defina um orçamento diário inicial (ex: R$ 100,00) e uma estratégia de lances focada em "Maximizar o valor da conversão" com um ROAS Alvo (ex: 300%) para começar a otimizar o retorno.

---

## Core Workflows

### Workflow 1: Criação e Otimização do Feed de Produtos no Google Merchant Center

Este workflow detalha o processo de preparar, enviar e otimizar o feed de produtos, a base para qualquer campanha de Google Shopping.

*   **Passo 1: Preparação dos Dados do Produto.**
    Reúna todos os dados essenciais para cada produto: `id` (SKU exclusivo), `title` (título descritivo), `description` (descrição detalhada), `link` (URL da página do produto), `image_link` (URL da imagem principal), `price` (preço com moeda, ex: `99.90 BRL`), `availability` (disponibilidade, ex: `in stock`, `out of stock`), `brand` (marca do produto), `gtin` (código de barras global, ex: EAN/UPC), `condition` (condição, ex: `new`, `used`), e `google_product_category` (categoria padronizada do Google).
    *   **Exemplo:** Para um smartphone, o `title` deve ser "Smartphone Samsung Galaxy S23 Ultra 256GB Preto", não apenas "Celular". O `price` deve incluir a moeda `5999.00 BRL`.

*   **Passo 2: Escolha do Formato e Geração do Feed.**
    Selecione o formato de feed mais adequado: XML (para grandes volumes de produtos com atualizações frequentes), CSV (para volumes menores ou gerenciamento via planilhas), ou Planilhas Google (para fácil colaboração). Para e-commerce com mais de 500 produtos, XML é o mais recomendado. Utilize plugins de e-commerce (Shopify, WooCommerce) que geram feeds automaticamente ou ferramentas de terceiros como o DataFeedWatch.
    *   **Exemplo:** Um e-commerce com 5.000 produtos deve usar um feed XML gerado por um plugin ou sistema ERP, com o URL do feed sendo `https://www.minhaloja.com.br/feed-produtos.xml`.

*   **Passo 3: Envio e Agendamento do Feed no Merchant Center.**
    No Google Merchant Center, navegue até "Produtos" > "Feeds". Clique no botão azul "+" para adicionar um novo feed. Selecione o país e idioma alvo (ex: Brasil, Português). Nomeie o feed (ex: "Feed Principal Loja X"). Escolha o método de entrada "Busca Programada" e insira o URL do seu feed XML/CSV. Configure um agendamento diário para um horário de baixo tráfego no site (ex: 03:00 BRT) para garantir que o feed esteja sempre atualizado.
    *   **Exemplo:** Configurar uma busca programada para `https://www.minhaloja.com.br/feed-produtos.xml` às 03:00 BRT, sete dias por semana.

*   **Passo 4: Monitoramento e Correção de Erros no Diagnóstico.**
    Após o envio, acesse a seção "Diagnóstico" no Merchant Center. Priorize a correção de itens reprovados (erros críticos que impedem a exibição dos anúncios) e, em seguida, os avisos (problemas que podem limitar o desempenho). Erros comuns incluem "Preço inconsistente", "Link de imagem inválido" ou "Atributo GTIN ausente".
    *   **Exemplo:** Se um produto é reprovado com "Preço incompatível", revise o `price` no seu feed e no site para garantir que sejam idênticos (ex: R$ 199.99 no feed e R$ 199.99 no site).

*   **Passo 5: Otimização de Atributos do Feed para Melhor Desempenho.**
    Refine os atributos `title`, `description` e `google_product_category` para melhorar a relevância dos anúncios. Inclua palavras-chave relevantes nos títulos e descrições, pensando em como os usuários pesquisam. Utilize os atributos `custom_label_0` a `custom_label_4` para segmentação interna (ex: "margem-alta", "promo-verao").
    *   **Exemplo:** Mudar um `title` de "Camisa Social" para "Camisa Social Masculina Slim Fit Algodão Azul Marinho" para ser mais específico e atrair pesquisas qualificadas.

### Workflow 2: Estruturação e Otimização de Campanhas Performance Max (PMax) para E-commerce

Este workflow orienta na criação e otimização de campanhas PMax, o formato mais recente e automatizado para Google Shopping.

*   **Passo 1: Criação da Campanha Performance Max.**
    No Google Ads, clique em "+ Nova Campanha", selecione "Vendas" como objetivo. Escolha "Performance Max" como tipo de campanha. Desmarque a opção "Encontrar novos clientes" se o foco for inicialmente em remarketing ou clientes existentes, ou mantenha-a marcada se a aquisição de novos clientes for prioritária.
    *   **Exemplo:** Iniciar uma PMax com objetivo de "Vendas" para um novo e-commerce de moda fitness.

*   **Passo 2: Configuração de Orçamento e Lances Inteligentes.**
    Defina um orçamento diário realista para a campanha (ex: `R$ 250,00`). Para a estratégia de lances, selecione "Maximizar o valor da conversão". Para otimização de ROAS, marque a caixa "Definir um ROAS Alvo" e insira um valor (ex: `300%`). Se a campanha for nova e não tiver histórico de conversões, inicie sem um ROAS Alvo por 2-3 semanas para permitir que o algoritmo colete dados.
    *   **Exemplo:** Uma campanha de eletrônicos com um ROAS Alvo de 350% para garantir que cada R$1 gasto gere R$3,50 em receita.

*   **Passo 3: Construção de Grupos de Ativos (Asset Groups) Estratégicos.**
    Crie Grupos de Ativos que segmentem produtos ou categorias lógicas. Para cada grupo, adicione múltiplos títulos (até 15, curtos e longos), descrições (até 5), imagens (até 20, com tamanhos variados como 1200x1200 e 1200x628), vídeos (até 5, opcional, mínimo 10 segundos) e um URL final relevante (ex: `https://www.minhaloja.com.br/smartphones`).
    *   **Exemplo:** Um Grupo de Ativos para "Smartphones Samsung" deve ter títulos como "Samsung Galaxy em Oferta", "Smartphones Samsung com Desconto", descrições sobre funcionalidades e imagens de diferentes modelos Galaxy.

*   **Passo 4: Fornecimento de Sinais de Público (Audience Signals).**
    Adicione sinais de público para guiar o algoritmo da PMax. Inclua suas listas de remarketing (ex: "Visitantes do site 30 dias", "Carrinhos abandonados"), listas de clientes (upload de CRM), e públicos personalizados (ex: "Pessoas que pesquisaram 'melhores smart tvs 2024'"). Isso acelera a fase de aprendizado da campanha.
    *   **Exemplo:** Adicionar uma lista de remarketing de "Compradores nos últimos 90 dias" e um público personalizado de "Interessados em Tênis de Corrida" para uma campanha de calçados esportivos.

*   **Passo 5: Monitoramento e Otimização Contínua da PMax.**
    Monitore o desempenho da campanha através dos relatórios de Grupos de Ativos e Insights. Pause grupos de ativos com baixo desempenho (ROAS abaixo do alvo). Aumente o orçamento para campanhas com ROAS positivo e potencial de escala. Ajuste o ROAS Alvo gradualmente (ex: de 300% para 320% se o desempenho for consistente). Use as "Exclusões de URL" nas configurações da campanha para evitar que a PMax anuncie produtos esgotados ou de baixo valor.
    *   **Exemplo:** Se o Grupo de Ativos "Calçados Infantis" apresenta ROAS de 150% enquanto o alvo é 300%, pause-o e investigue os criativos ou produtos incluídos. Se "Tênis Esportivos Masculinos" está com 400%, considere aumentar o orçamento geral da campanha.

---

## Templates

### Template de Item de Feed de Produto (CSV)

```csv
id,title,description,link,image_link,price,availability,brand,gtin,condition,google_product_category,custom_label_0,shipping,shipping_weight
SKU1001,Smartphone Samsung Galaxy S23 Ultra 256GB Preto,Experimente a inovação com o Galaxy S23 Ultra. Câmera de 200MP, S Pen integrada e bateria de longa duração.,https://www.minhaloja.com.br/galaxy-s23-ultra,https://www.minhaloja.com.br/imagens/s23ultra.jpg,5999.00 BRL,in stock,Samsung,7891234560000,new,Eletrônicos > Celulares e Acessórios > Celulares,premium,BR:::Standard:0.00 BRL,0.2kg
SKU1002,Smart TV LG OLED C2 55 polegadas 4K,A mais avançada tecnologia OLED com processador Alpha 9 Gen5 AI. Perfeita para cinema e games.,https://www.minhaloja.com.br/tv-lg-c2,https://www.minhaloja.com.br/imagens/lg-c2.jpg,4500.00 BRL,in stock,LG,7891234560001,new,Eletrônicos > Televisores > TVs OLED,destaque,BR:::Standard:0.00 BRL,15.0kg
SKU1003,Fone de Ouvido Bluetooth JBL Wave Buds Preto,Experimente a liberdade sem fios com o JBL Wave Buds. Graves potentes e até 32 horas de bateria.,https://www.minhaloja.com.br/jbl-wave-buds,https://www.minhaloja.com.br/imagens/jbl-buds.jpg,299.00 BRL,in stock,JBL,7891234560002,new,Eletrônicos > Áudio > Fones de Ouvido,acessorios,BR:::Standard:0.00 BRL,0.05kg
```

### Template de Ativos de Texto para Grupo de Ativos PMax

```
URL Final: https://www.minhaloja.com.br/celulares-e-smartphones/samsung
Nome da Empresa: Minha Loja Tech

Títulos Curtos (até 30 caracteres, mínimo 3):
1. Galaxy S23 Ultra
2. Samsung em Oferta
3. Celulares Samsung
4. Novo Galaxy S24

Títulos Longos (até 90 caracteres, mínimo 5):
1. Smartphone Samsung Galaxy S24 Ultra - Lançamento
2. Compre Samsung Galaxy com Desconto e Frete Grátis
3. Os Melhores Celulares Samsung Você Encontra Aqui
4. Tecnologia de Ponta: Galaxy S23 e S24 em Promoção
5. Explore a Linha Completa de Smartphones Samsung

Descrições (até 90 caracteres, mínimo 2):
1. Tecnologia Samsung na palma da sua mão.
2. Descontos exclusivos em toda linha Galaxy.
3. Entrega rápida e segura para todo Brasil.
4. Celulares Samsung com garantia oficial.

Descrições Longas (até 360 caracteres, mínimo 1):
1. Descubra a inovação dos smartphones Samsung Galaxy. Encontre modelos como S23 Ultra, S24 e Z Fold 5 com preços imperdíveis, condições de pagamento facilitadas e entrega rápida. Aproveite as melhores ofertas em tecnologia mobile.
2. A Minha Loja Tech é sua fonte para os mais recentes lançamentos Samsung. De câmeras avançadas a processadores ultrarrápidos, tenha a melhor experiência com seu novo Galaxy. Compre online com segurança e suporte especializado.
```

---

## Checklist

- [ ] Conta do Google Merchant Center configurada, verificada e com informações comerciais completas.
- [ ] Feed de produtos XML/CSV enviado, agendado para atualizações diárias e sem erros críticos no Diagnóstico.
- [ ] Google Merchant Center vinculado à conta do Google Ads.
- [ ] Acompanhamento de conversões configurado corretamente no Google Ads, incluindo valor de conversão.
- [ ] Campanha Performance Max criada com objetivo "Vendas" e feed de produtos selecionado.
- [ ] Estratégia de lances "Maximizar o valor da conversão" com ROAS Alvo definido (ou sem, se em fase de aprendizado).
- [ ] Grupos de Ativos (Asset Groups) segmentados por categoria, marca ou margem de lucro, com múltiplos títulos, descrições e imagens de alta qualidade.
- [ ] Sinais de Público (Audience Signals) adicionados (listas de remarketing, listas de clientes, públicos personalizados).
- [ ] URL final expandida desativada na PMax, se houver URLs específicas a serem promovidas.
- [ ] Monitoramento diário do Diagnóstico do Merchant Center para identificar e corrigir novos erros de produtos.
- [ ] Análise semanal do relatório de "Grupos de Ativos" e "Insights" da PMax para otimização de desempenho.
- [ ] Exclusão de URLs de produtos esgotados ou de baixo desempenho nas configurações da campanha PMax.

---

## Métricas de Referência

| Métrica | Benchmark (E-commerce Brasil) | Meta (Otimizado) |
|---------|-------------------------------|-------------------|
| ROAS | 200% - 300% (2x - 3x)         | 350% - 500%+      |
| CTR   | 0.8% - 1.5%                   | 1.8% - 3.0%+      |
| CPC   | R$ 0.50 - R$ 2.50             | R$ 0.30 - R$ 1.80 |
| Taxa de Conversão | 0.8% - 2.0%                   | 2.5% - 4.0%+      |
| Custo por Aquisição (CPA) | R$ 30.00 - R$ 100.00          | R$ 15.00 - R$ 50.00 |
| Valor Médio do Pedido (AOV) | R$ 150.00 - R$ 500.00         | R$ 200.00 - R$ 700.00 |

---

## Erros Comuns

1.  **Feed de produtos desatualizado ou com inconsistências**: Leva à reprovação de produtos, exibição de preços errados ou anúncios de produtos esgotados, gerando má experiência e desperdício de orçamento. **Como evitar**: Configure um agendamento diário para o feed no Merchant Center e monitore a seção "Diagnóstico" regularmente. Implemente automação para que as informações do feed reflitam o estoque e preços do site em tempo real. Exemplo: Um feed que não atualiza o status de `availability` quando um produto fica `out of stock`, resultando em cliques pagos para um produto indisponível.
2.  **Imagens de produtos que violam as diretrizes**: Imagens com texto promocional, logotipos, marca d'água ou fundos coloridos não brancos são frequentemente reprovadas. **Como evitar**: Utilize imagens de alta resolução (mínimo 800x800 pixels), com fundo branco puro ou transparente, sem texto, logos ou bordas adicionais. Exemplo: Uma imagem com a palavra "PROMOÇÃO!" inserida no canto superior é reprovada, exigindo uma imagem limpa do produto.
3.  **Falta de ROAS Alvo em campanhas PMax após a fase de aprendizado**: Deixar a PMax em "Maximizar o valor da conversão" sem ROAS Alvo por um período prolongado (após 30+ conversões) pode levar a gastos excessivos em conversões de baixo valor, prejudicando a lucratividade. **Como evitar**: Após 2-3 semanas de coleta de dados e ao menos 30 conversões, adicione um ROAS Alvo realista (ex: 250%) com base no desempenho inicial para otimizar o lucro e controlar o gasto.
4.  **Títulos e descrições genéricas no feed de produtos**: Títulos como "TV" ou "Camiseta" não fornecem informações suficientes para o Google ou para o usuário, resultando em menor relevância e CTR. **Como evitar**: Crie títulos e descrições ricos em palavras-chave, detalhando marca, modelo, cor, tamanho e características relevantes. Exemplo: Em vez de "TV", use "Smart TV LG OLED C2 55 polegadas 4K HDR".

---

## Dicas Avançadas

1.  **Utilize Atributos Personalizados (`custom_label`) para Segmentação de Produtos**: