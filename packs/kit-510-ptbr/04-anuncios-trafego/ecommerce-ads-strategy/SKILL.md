---
name: ecommerce-ads-strategy
description: "Ecommerce Ads Strategy — Skill especializada para ecommerce ads strategy"
license: MIT
metadata:
  version: 1.0.0
  author: Cafe Code AI
  category: 04-anuncios-trafego
  updated: 2026-03-01
risk: safe
---

# Ecommerce Ads Strategy

Esta skill capacita o Claude a desenvolver, implementar e otimizar estratégias de anúncios pagas altamente eficazes para e-commerces em Meta Ads, Google Ads e TikTok Ads.

---

## Keywords

ROAS Otimização, CBO Meta Ads, PMax Google Ads, Lookalikes Avançados, Retargeting Dinâmico, LTV Cliente, Estratégia Funil TOFU MOFU BOFU, Teste A/B Criativos, Segmentação Comportamental, Bid Strategy CPA, GA4 Integração.

---

## Quick Start

1.  **Configurar GA4 e API de Conversões:** Implementar GA4 para rastreamento de eventos de e-commerce (PageView, ViewItem, AddToCart, Purchase) e configurar a API de Conversões do Meta para redundância de dados.
2.  **Estruturar Campanha PMax (Google Ads):** Criar uma campanha Performance Max focada em vendas, alimentando-a com feeds de produto do Merchant Center, grupos de ativos específicos e sinais de público-alvo (listas de clientes, visitantes do site).
3.  **Lançar Campanha de Vendas (Meta Ads):** Iniciar uma campanha com objetivo de Vendas, utilizando Otimização de Orçamento de Campanha (CBO), com ad sets segmentados por público-alvo (ex: Lookalikes 1-3% de compradores) e criativos dinâmicos de produto.
4.  **Ativar Campanha de Tráfego Direcionado (TikTok Ads):** Desenvolver uma campanha de Vendas/Conversão no TikTok Ads, segmentando por interesses específicos do nicho do produto (ex: "beleza natural", "jogos eletrônicos") e usando vídeos curtos e autênticos.

---

## Core Workflows

### Workflow 1: Escalonamento de Campanhas de Vendas em Meta Ads com CBO

**Objetivo:** Aumentar o volume de vendas mantendo o ROAS (Retorno sobre o Investimento em Anúncios) e o CPA (Custo por Aquisição).

**Passos:**

1.  **Análise de Desempenho Atual:** Avaliar ad sets com ROAS > 3.0 e CPA < R$ 50,00 nos últimos 7 dias. Identificar criativos (vídeos, imagens) e públicos (interesses, Lookalikes) de alta performance que demonstram consistência.
2.  **Duplicação Seletiva para CBO:** Duplicar os ad sets vencedores e seus criativos em uma nova campanha, ativando a Otimização de Orçamento de Campanha (CBO). Iniciar a nova campanha com um orçamento 20-30% maior que a soma dos orçamentos dos ad sets originais. Exemplo: Se três ad sets gastavam R$ 100/dia cada e tinham bom desempenho, a nova campanha CBO pode começar com R$ 360-390/dia.
3.  **Expansão de Público com Lookalikes Avançados:** Adicionar novos ad sets na campanha CBO utilizando públicos Lookalike de 1-3% ou 1-5% baseados em "Compradores nos últimos 90 dias" ou "Adicionou ao Carrinho nos últimos 30 dias". Testar diferentes fontes de dados (pixel, listas de clientes via Customer Match).
4.  **Testes A/B de Criativos Novas Variações:** Dentro dos ad sets duplicados, pausar criativos com CTR (Click-Through Rate) < 1.0% e iniciar testes A/B com 2-3 novas variações de vídeos de UGC (User Generated Content) ou carrosséis de produtos com propostas de valor claras (ex: frete grátis, desconto progressivo). Exemplo: Testar vídeo A (depoimento cliente) vs. vídeo B (demonstração de uso) para o ad set "Lookalike 1% Compradores".
5.  **Monitoramento e Otimização Diária:** Acompanhar o ROAS e o CPA em nível de ad set e campanha. Se um ad set estiver performando abaixo da meta (ex: ROAS < 2.0) por 3 dias consecutivos, reduzir seu lance, diminuir seu orçamento (se CBO permitir) ou pausá-lo. O CBO realocará o orçamento para os ad sets de melhor desempenho. Exemplo: Ad set "Interesses em Moda Feminina" com ROAS de 1.8 por 3 dias, pausar e focar nos Lookalikes de alta performance.

### Workflow 2: Otimização de Campanha Google Performance Max (PMax) para ROAS

**Objetivo:** Maximizar o retorno sobre o investimento em anúncios no Google Ads, utilizando as capacidades de automação da PMax.

**Passos:**

1.  **Auditoria e Atualização de Sinais de Público-Alvo:** Verificar a relevância e atualização dos sinais de público (audience signals). Incluir listas de remarketing (compradores, adicionou ao carrinho, visitantes do site), listas de clientes (CRM) e segmentos personalizados com termos de pesquisa de alta intenção (ex: "comprar [nome do produto]", "melhor [tipo de produto]"). Remover listas desatualizadas ou com baixo volume.
2.  **Otimização de Grupos de Ativos:** Analisar o desempenho dos ativos (títulos, descrições, imagens, vídeos) dentro de cada grupo de ativos. Substituir ativos com status "Baixo" ou "Bom" por novos ativos com potencial para "Melhor" ou "Excelente". Exemplo: Trocar uma imagem genérica por uma foto de alta qualidade do produto em uso, ou um vídeo estático por um vídeo dinâmico de unboxing.
3.  **Exclusão de Termos de Pesquisa Negativos (via Suporte/Conta Manager):** Embora o PMax seja automatizado, é crucial solicitar exclusões de termos de pesquisa irrelevantes ou de baixo desempenho através do representante do Google ou via suporte, especialmente para evitar tráfego de termos de marca concorrente, termos informacionais não-transacionais ou pesquisas com intenção negativa. Exemplo: Excluir "review", "grátis", "problemas [nome da marca]" se não forem objetivos.
4.  **Ajuste de Valor da Conversão (Para LTV):** Se o e-commerce tiver um LTV (Lifetime Value) claro por cliente ou categoria de produto, ajustar o valor de conversão para refletir o LTV médio do primeiro pedido, em vez apenas do valor da compra inicial. Isso permite ao Smart Bidding otimizar para clientes mais valiosos a longo prazo. Exemplo: Se o pedido médio é R$ 150, mas o LTV é R$ 300, configurar o valor de conversão como R$ 300 para essa conversão específica.
5.  **Revisão e Otimização Contínua do Feed de Produtos (Merchant Center):** Garantir que o feed de produtos esteja impecável e sempre atualizado: imagens de alta qualidade, títulos descritivos com palavras-chave, descrições detalhadas, atributos de categoria corretos, preços atualizados e disponibilidade em estoque. Produtos sem estoque, com erros ou com informações incompletas no feed podem impactar negativamente o PMax.

---

## Templates

### Meta Ads - Estrutura de Campanha TOFU/MOFU/BOFU

```
Campanha: [NOME_DA_LOJA] - Vendas - [Mês/Ano] - [Objetivo Principal: Ex: Aquisição Nova | Retargeting]

Objetivo: Vendas (Conversão: Compra)
Otimização de Orçamento de Campanha (CBO): Ativada
Orçamento Diário: R$ 500,00 (Exemplo: Ajustar conforme necessidade e ROAS meta)

Ad Set 1 (TOFU - Topo de Funil: Consciência/Descoberta)
  Público: Lookalike 1-3% (Visitantes 180 dias) + Interesses Amplos (ex: "Moda Sustentável", "Culinária Vegana", "Tecnologia Wearable")
  Exclusões: Compradores (90 dias)
  Posicionamentos: Automáticos (Recomendado para CBO)
  Otimização para: Compras
  Criativos: 3-5 vídeos curtos (UGC, unboxing, storytelling), 2-3 imagens estáticas com proposta de valor clara.
  Copy: Foco em problema-solução, curiosidade, inovação do produto.
  CTA: Saiba Mais, Comprar Agora.

Ad Set 2 (MOFU - Meio de Funil: Consideração)
  Público: Visitantes do site (30 dias) - Excluir Compradores (90 dias)
           Adicionou ao Carrinho (7 dias) - Excluir Compradores (90 dias)
           Público de Engajamento (Instagram/Facebook 90 dias)
  Exclusões: Compradores (90 dias)
  Posicionamentos: Automáticos
  Otimização para: Compras
  Criativos: 2-3 carrosséis de produtos (com diferentes ângulos/benefícios), 1-2 vídeos de demonstração de produto, prova social.
  Copy: Foco em benefícios específicos, diferenciais, depoimentos de clientes, garantia.
  CTA: Comprar Agora, Ver Produtos.

Ad Set 3 (BOFU - Fundo de Funil: Conversão/Retargeting)
  Público: Adicionou ao Carrinho (30 dias) - Excluir Compradores (90 dias)
           Iniciou Checkout (14 dias) - Excluir Compradores (90 dias)
           Visualizou Produto (30 dias) - Excluir Compradores (90 dias)
  Exclusões: Compradores (90 dias)
  Posicionamentos: Automáticos
  Otimização para: Compras
  Criativos: 2-3 imagens/vídeos dinâmicos de produto (DPA), 1 imagem com oferta de frete grátis/cupom de desconto por tempo limitado, urgência.
  Copy: Urgência, escassez, prova social final, CTA direto para compra.
  CTA: Comprar Agora, Finalizar Compra.
```

### Google Ads - Títulos e Descrições para PMax (Grupo de Ativos)

```
Grupo de Ativos: Roupas Esportivas Premium

Títulos (15-30 caracteres - Mínimo 3, ideal 5+):
- Roupas Esportivas Premium
- Conforto e Performance
- Treine com Estilo
- Frete Grátis Acima de R$199
- Linha Fitness Exclusiva
- Leggings de Alta Compressão
- Tops Esportivos Respiráveis
- Novidades Chegando!
- Compre Online Já
- Desconto na Primeira Compra

Títulos Longos (30-90 caracteres - Mínimo 1, ideal 3+):
- Roupas Esportivas Premium para Alta Performance e Conforto Duradouro.
- Eleve seu Treino com Nossa Coleção Exclusiva de Fitness Feminina e Masculina.
- Desfrute de Frete Grátis em Pedidos de Roupas Esportivas Acima de R$199 em Todo Brasil.

Descrições (60-90 caracteres - Mínimo 2, ideal 4+):
- Materiais tecnológicos e design moderno para seu melhor desempenho.
- Encontre o look perfeito para sua atividade física com conforto e estilo.
- Variedade em cores e tamanhos. Compre online e receba rápido no seu endereço!
- Conforto e estilo unidos para sua rotina de exercícios. Qualidade garantida.
- Loja online de roupas fitness com as melhores marcas e preços.
```

---

## Checklist

- [x] GA4 configurado com eventos de e-commerce (PageView, ViewItem, AddToCart, Purchase) e e-commerce tracking aprimorado.
- [x] API de Conversões do Meta implementada e validada para redundância e qualidade de dados.
- [x] Feed de produtos do Google Merchant Center atualizado, otimizado e sem erros para Google Ads (PMax e Shopping).
- [x] Públicos de remarketing (visitantes, carrinho abandonado, visualizou produto) e Lookalikes (compradores, adicionou ao carrinho) criados e atualizados no Meta Ads e TikTok Ads.
- [x] Campanha PMax com grupos de ativos completos (vídeos, imagens, títulos, descrições) e sinais de público relevantes.
- [x] Testes A/B de criativos (vídeos, imagens, copies) rodando ativamente para identificar os vencedores em Meta/TikTok Ads.
- [x] Orçamento alocado estrategicamente entre as etapas do funil (TOFU/MOFU/BOFU) para maximizar o ROAS geral.
- [x] Regras automatizadas de otimização (pausar anúncios de baixo ROAS, ajustar lances) configuradas no Meta Ads.
- [x] Dashboard de métricas (ROAS, CPA, LTV, CTR, Taxa de Conversão) monitorado diariamente no Google Analytics e plataformas de anúncios.
- [x] Estratégia de lances configurada para maximizar valor de conversão (ex: ROAS Alvo no Google Ads, Menor Custo com ROAS Mínimo no Meta Ads).

---

## Métricas de Referência

| Métrica | Benchmark (e-commerce geral) | Meta (e-commerce de alta performance) |
|---------|------------------------------|--------------------------------------|
| ROAS    | 2.5x                         | 3.5x - 5.0x                          |
| CTR (Meta/TikTok) | 1.0%                         | 1.5% - 2.5%                          |
| CTR (Google Search) | 3.0%                         | 5.0% - 8.0%                          |
| CPC (Custo por Clique) | R$ 1.50 - R$ 3.00            | R$ 0.80 - R$ 2.00                    |
| CPA (Custo por Aquisição) | R$ 50.00 - R$ 100.00         | R$ 20.00 - R$ 40.00                  |
| Taxa Conversão (Ecommerce) | 1.5% - 2.5%                  | 3.0% - 5.0%                          |
| LTV:CAC Ratio | 2:1                          | 3:1 ou superior                      |

---

## Erros Comuns

1.  **Não usar API de Conversões do Meta**: Confiar apenas no pixel do Meta resulta em perda de dados e otimização imprecisa, especialmente com as restrições de privacidade (iOS 14+). **Como evitar**: Implementar a API de Conversões do Meta com eventos do servidor, priorizando a qualidade dos dados enviados. Exemplo: Configurar o envio de eventos de "Purchase" e "AddToCart" diretamente do servidor do e-commerce para o Meta, complementando os dados do pixel.
2.  **Ignorar a otimização do Feed de Produtos no Google Ads**: Um feed de produtos desatualizado, com imagens de baixa qualidade, informações incompletas ou erros no Google Merchant Center, limita severamente o desempenho das campanhas Performance Max e Shopping. **Como evitar**: Otimizar o feed de produtos semanalmente. Garantir imagens de alta resolução, títulos descritivos com palavras-chave relevantes, descrições detalhadas, atributos de categoria corretos, preços atualizados e disponibilidade em estoque. Exemplo: Adicionar atributos como "cor", "tamanho", "marca", "gênero" e "tipo de material" para cada item.
3.  **Escalar orçamento de forma abrupta sem validação de ROAS**: Aumentar o orçamento de uma campanha em 50% ou mais de uma única vez, sem um histórico consistente de ROAS, pode diluir rapidamente o desempenho e gerar custos desnecessários. **Como evitar**: Escalar gradualmente, aumentando o orçamento em 15-20% a cada 2-3 dias, monitorando de perto o ROAS e o CPA. Se o ROAS cair significativamente, diminuir o orçamento e focar na otimização de criativos e públicos. Exemplo: Uma campanha com ROAS 3.0 em R$200/dia pode ser escalada para R$240/dia e ser monitorada por 48h antes de um novo aumento.

---

## Dicas Avançadas

1.  **Segmentação por LTV (Lifetime Value) para Retargeting**: Criar públicos personalizados no Meta Ads com base no LTV dos clientes (valor total gasto). Priorizar remarketing para clientes de alto LTV com ofertas exclusivas, programas de fidelidade ou produtos complementares de ticket médio elevado. Exemplo: Criar um público de "Clientes VIP" que gastaram mais de R$ 500 nos últimos 12 meses e direcionar anúncios de pré-lançamento de produtos premium ou cross-sell de itens de maior margem.
2.  **Uso de Smart Bidding no Google Ads com valores de conversão ajustados**: Em vez de apenas otimizar para "Compras" com valor fixo, ajustar o valor de cada conversão no Google Ads para refletir a margem de lucro real ou o LTV estimado por produto/categoria. Isso permite ao Smart Bidding priorizar vendas mais lucrativas. Exemplo: