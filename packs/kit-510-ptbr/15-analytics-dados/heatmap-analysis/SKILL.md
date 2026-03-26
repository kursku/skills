---
name: heatmap-analysis
description: "Heatmap Analysis — Skill especializada para análise de mapas de calor, otimizando a experiência do usuário e conversões através da visualização do comportamento no site."
license: MIT
metadata:
  version: 1.0.0
  author: Cafe Code AI
  category: 15-analytics-dados
  updated: 2026-03-01
risk: safe
---

# Heatmap Analysis

Esta skill capacita o Claude a atuar como um analista de Heatmap especialista, capaz de interpretar dados visuais de comportamento do usuário para identificar gargalos, otimizar interfaces e impulsionar métricas de negócios, integrando insights com o Google Analytics 4.

---

## Keywords

Click Maps, Scroll Maps, Move Maps, Rage Clicks, Dead Clicks, Heatmap Tools, Hotjar, Microsoft Clarity, Smartlook, Fullstory, UX Optimization, Conversion Rate Optimization (CRO), Google Analytics 4 (GA4), User Behavior, Page Experience, Form Analytics, Session Recording, A/B Testing, User Journey, Content Engagement, Above the Fold.

---

## Quick Start

1.  **Instalar Ferramenta:** Selecionar e integrar o código de rastreamento de uma ferramenta de heatmap (ex: Hotjar, Microsoft Clarity) no Google Tag Manager (GTM) para todas as páginas do domínio `www.seusite.com.br`.
2.  **Priorizar Páginas:** Identificar URLs com alta taxa de rejeição ou baixa conversão no GA4 (ex: `/carrinho`, `/checkout`, `/landing-page-oferta-x`).
3.  **Coletar Dados:** Aguardar no mínimo 7 dias para coletar volume suficiente de sessões (idealmente >1000) nas páginas prioritárias.
4.  **Analisar Scroll Maps:** Avaliar a porcentagem de rolagem para identificar onde os usuários param de interagir ou perdem interesse, focando em páginas de conteúdo longo ou landing pages.
5.  **Analisar Click Maps:** Identificar elementos não clicáveis recebendo cliques (dead clicks) e áreas de baixo engajamento em botões de Call-to-Action (CTAs).

---

## Core Workflows

### Workflow 1: Otimização de Landing Pages com Heatmaps de Cliques e Scroll para CRO

**Contexto:** Uma landing page de um SaaS (`https://www.meusite.com.br/lp-demo-gratis`) possui uma taxa de conversão de cliques no botão "Solicitar Demo" de 2.5%, enquanto a média do setor é 5%. O objetivo é identificar barreiras de engajamento e otimizar a conversão.

**Ferramentas:** Hotjar (ou Microsoft Clarity) para heatmaps, Google Analytics 4 para métricas de funil e segmentação.

**Passos Detalhados:**

1.  **Configuração e Coleta de Dados:**
    *   Verificar se o código de rastreamento do Hotjar está ativo para `https://www.meusite.com.br/lp-demo-gratis`.
    *   Assegurar que dados foram coletados por pelo menos 10 dias, com um volume mínimo de 1500 sessões.
2.  **Análise de Click Map:**
    *   Acessar o relatório de Click Map para a URL `https://www.meusite.com.br/lp-demo-gratis`.
    *   **Exemplo Concreto:** Observar que 40% dos cliques na parte superior da página (acima da dobra) estão em uma imagem decorativa do produto que não é clicável (dead click), e apenas 15% dos cliques ocorrem no botão "Solicitar Demo" que está visível. Outra observação: um pequeno ícone de "saiba mais" abaixo do título recebe 8% dos cliques, desviando a atenção do CTA principal.
    *   **Insight:** Usuários estão procurando interatividade em elementos não interativos e estão sendo distraídos por elementos secundários.
3.  **Análise de Scroll Map:**
    *   Acessar o relatório de Scroll Map para a mesma URL.
    *   **Exemplo Concreto:** O mapa mostra que 70% dos usuários rolam apenas até 50% da página, e apenas 30% chegam ao formulário de contato, que está posicionado a 1200px da parte superior. A dobra média para desktop é de 650px e para mobile é de 400px.
    *   **Insight:** Conteúdo crítico e o formulário de conversão estão abaixo da dobra para a maioria dos usuários, resultando em baixa visibilidade.
4.  **Correlação com GA4:**
    *   No GA4, navegar até `Relatórios > Engajamento > Páginas e telas`. Filtrar pela URL `/lp-demo-gratis`.
    *   Verificar a `Taxa de rejeição` (alta, ex: 65%) e o `Tempo médio de engajamento` (baixo, ex: 45 segundos).
    *   Segmentar por dispositivo (`Relatórios > Tecnologia > Detalhes tecnológicos`) e comparar scroll maps para desktop e mobile, buscando discrepâncias visuais ou de engajamento.
5.  **Identificação de Oportunidades e Hipóteses:**
    *   **Problema 1 (Click Map):** Distração por elementos não clicáveis e baixo engajamento no CTA principal.
        *   **Hipótese:** Remover interatividade falsa na imagem do produto e aumentar o destaque visual do botão "Solicitar Demo" aumentará os cliques no CTA.
    *   **Problema 2 (Scroll Map):** Conteúdo e formulário crítico abaixo da dobra.
        *   **Hipótese:** Reposicionar o formulário de contato acima da dobra (ou em uma seção mais visível) e resumir o conteúdo inicial aumentará a visibilidade e a interação com o formulário.
6.  **Recomendação e Próximos Passos:**
    *   Criar duas variantes para um teste A/B:
        *   **Variante A:** Otimização do Click Map (imagem não clicável, destaque do CTA).
        *   **Variante B:** Otimização do Scroll Map (formulário acima da dobra).
    *   Rodar testes A/B usando Google Optimize ou ferramenta similar, monitorando a `taxa de cliques no CTA` e a `taxa de submissão do formulário` como métricas primárias no GA4.

### Workflow 2: Análise de Funil de Checkout com Gravações de Sessão e Heatmaps para Redução de Abandono

**Contexto:** Um e-commerce (`www.minhaloja.com.br`) tem uma taxa de abandono de 30% no estágio de "Informações de Pagamento" do checkout, conforme funil configurado no GA4. O objetivo é identificar pontos de atrito específicos.

**Ferramentas:** Smartlook (ou Fullstory) para gravações de sessão e heatmaps, Google Analytics 4 para métricas de funil e eventos.

**Passos Detalhados:**

1.  **Definição do Funil no GA4:**
    *   Confirmar o funil de eventos no GA4: `add_to_cart > begin_checkout > add_shipping_info > add_payment_info > purchase`.
    *   Identificar que o evento `add_payment_info` para `purchase` tem a maior queda.
2.  **Configuração de Gravação e Heatmaps:**
    *   Assegurar que o Smartlook está configurado para gravar sessões e gerar heatmaps para as URLs do checkout, especialmente `https://www.minhaloja.com.br/checkout/pagamento`.
    *   Garantir a coleta de dados por 14 dias, com foco em sessões que chegam ao estágio de `add_payment_info`.
3.  **Análise de Gravações de Sessão Segmentadas:**
    *   No Smartlook, filtrar sessões de usuários que visitaram `https://www.minhaloja.com.br/checkout/pagamento` mas *não* concluíram a compra (evento `purchase`).
    *   **Exemplo Concreto:** Assistir a 20-30 gravações de sessões de abandono. Observar usuários tentando repetidamente inserir o número do cartão de crédito, clicando no botão "Finalizar Pedido" sem sucesso, ou rolando a página rapidamente após um erro de validação. Identificar "rage clicks" no botão "Finalizar Pedido" ou "u-turns" (voltar à página anterior).
    *   **Insight:** Existem problemas na validação do formulário ou na comunicação de erros, causando frustração e abandono.
4.  **Análise de Click Map e Form Analytics:**
    *   Acessar o Click Map para `https://www.minhaloja.com.br/checkout/pagamento`.
    *   **Exemplo Concreto:** O Click Map mostra muitos cliques em "dead areas" próximas aos campos de cartão de crédito, sugerindo que usuários estão tentando interagir com algo que não é um campo. O Form Analytics (se disponível no Smartlook) revela que o campo "Número do Cartão" tem uma taxa de abandono de campo de 18% e o campo "CVV" tem 12%.
    *   **Insight:** A interface do formulário de pagamento pode ser confusa, e os usuários podem ter dificuldades em entender onde e como inserir as informações.
5.  **Análise de Scroll Map:**
    *   Acessar o Scroll Map para a mesma URL.
    *   **Exemplo Concreto:** O mapa indica que a seção de "Termos e Condições" e o link para a "Política de Privacidade" (que são obrigatórios para finalizar a compra) estão abaixo da dobra para 60% dos usuários, com uma queda acentuada de visibilidade após 800px.
    *   **Insight:** Informações cruciais ou elementos de confiança que poderiam reduzir a ansiedade do usuário estão sendo ignorados.
6.  **Identificação de Oportunidades e Hipóteses:**
    *   **Problema 1 (Gravações/Click Map/Form Analytics):** Frustração no preenchimento do formulário de pagamento e erros de validação.
        *   **Hipótese:** Melhorar a validação em tempo real dos campos de cartão, fornecer mensagens de erro mais claras e otimizar o layout do formulário (ex: agrupar campos) reduzirá a taxa de abandono.
    *   **Problema 2 (Scroll Map):** Baixa visibilidade de termos e links de privacidade.
        *   **Hipótese:** Reposicionar os links de "Termos e Condições" e "Política de Privacidade" para uma área mais visível (acima da dobra ou próximo ao botão de finalizar pedido) aumentará a confiança e reduzirá o abandono.
7.  **Recomendação e Monitoramento:**
    *   Implementar as melhorias no formulário e no posicionamento dos links.
    *   Monitorar a `taxa de abandono do estágio 'add_payment_info'` no GA4 e a `taxa de conversão de compra` pós-implementação. Comparar métricas de engajamento na página de pagamento no GA4.

---

## Templates

### Relatório de Análise de Heatmap e Recomendações

```
**Relatório de Análise de Heatmap - [Nome do Projeto]**

**Data da Análise:** 2024-07-25
**Analista:** Claude AI
**Ferramenta Utilizada:** Hotjar, Google Analytics 4

---

**1. URL Analisada:** https://www.meusite.com.br/lp-oferta-especial-julho
**Período de Dados:** 2024-07-01 a 2024-07-24 (24 dias)
**Volume de Sessões:** 3.870

**2. Problemas Identificados (Heatmap + GA4):**

*   **Tipo de Heatmap:** Click Map
    *   **Evidência:** 35% dos cliques na dobra superior ocorrem em uma imagem do produto que não é clicável. O CTA principal "Baixar Ebook Grátis" recebe apenas 10% dos cliques nessa área.
    *   **Correlação GA4:** Baixa taxa de cliques no evento `generate_lead` (1.2%) e alta taxa de rejeição (58%) para esta página.
*   **Tipo de Heatmap:** Scroll Map
    *   **Evidência:** 68% dos usuários rolam apenas até 60% da página, e o formulário de download do ebook está posicionado a 1100px (abaixo da dobra para a maioria dos dispositivos).
    *   **Correlação GA4:** Tempo médio de engajamento de 55 segundos, indicando que muitos usuários não interagem com o conteúdo completo.
*   **Tipo de Heatmap:** Move Map (opcional)
    *   **Evidência:** Movimento intenso do mouse sobre um bloco de texto com bullet points que lista benefícios, mas sem interatividade clara.
    *   **Correlação GA4:** Não há evento de clique configurado para este bloco, impossibilitando medição direta no GA4.

**3. Recomendações e Hipóteses:**

*   **Recomendação 1 (Click Map):** Remover o link falso da imagem do produto ou torná-la clicável para uma página de detalhes. Aumentar o contraste e o tamanho do botão "Baixar Ebook Grátis".
    *   **Hipótese:** Otimizar a clareza do CTA principal e remover distrações não interativas aumentará a taxa de cliques no CTA em 20%.
*   **Recomendação 2 (Scroll Map):** Reposicionar o formulário de download do ebook para a metade superior da página (entre 500px e 700px) e resumir o conteúdo introdutório para priorizar a conversão.
    *   **Hipótese:** Aumentar a visibilidade do formulário de conversão resultará em um aumento de 15% na taxa de preenchimento.
*   **Recomendação 3 (Move Map):** Transformar os bullet points de benefícios em um acordeão ou seção expansível para engajar mais usuários ou adicionar um CTA secundário.
    *   **Hipótese:** Adicionar interatividade aos benefícios pode aumentar o tempo de engajamento na página em 10 segundos.

**4. Prioridade das Ações:**

1.  Otimização do CTA principal e remoção de "dead clicks" (Alta)
2.  Reposicionamento do formulário (Alta)
3.  Adição de interatividade nos benefícios (Média)

**5. Próximos Passos:**

*   Criar variantes A/B para as recomendações 1 e 2.
*   Configurar testes A/B no Google Optimize.
*   Monitorar eventos de `form_submit` e `generate_lead` no GA4.

---
```

### Briefing para Teste A/B Baseado em Heatmap

```
**Briefing de Teste A/B - Otimização de Página de Produto**

**Data:** 2024-07-25
**Responsável:** Equipe de CRO

---

**1. URL Alvo do Teste:** https://www.minhaloja.com.br/produto/tenis-corrida-x
**Período do Teste:** 3 semanas

**2. Problema Identificado (Evidência Heatmap + GA4):**

*   **Heatmap (Click Map):** O botão "Adicionar ao Carrinho" (CTA principal) tem uma taxa de cliques de 18%, enquanto a imagem de "Avaliações de Clientes" (elemento secundário) recebe 12% dos cliques e desvia a atenção. Há também "rage clicks" no botão de seleção de tamanho, indicando dificuldade de uso.
*   **Heatmap (Scroll Map):** A seção de "Produtos Relacionados" e "FAQ" estão abaixo da dobra para 75% dos usuários, mas o scroll map mostra que o engajamento cai drasticamente após a visualização da descrição do produto (queda de 50% de usuários entre 800px e 1200px).
*   **GA4:** Taxa de conversão de "Adicionar ao Carrinho" de 8.5%, abaixo da média de 12% para produtos similares. Taxa de saída de 25% na página do produto.

**3. Hipótese do Teste:**

*   **Hipótese Central:** Aumentar o destaque e a usabilidade do CTA principal "Adicionar ao Carrinho" e melhorar a experiência de seleção de tamanho, combinado com um posicionamento estratégico de informações complementares, aumentará a taxa de "Adicionar ao Carrinho" e reduzirá a taxa de saída.

**4. Variantes Propostas:**

*   **Variante Original (Controle):** Layout atual da página de produto.
*   **Variante A (Otimização CTA e Usabilidade):**
    *   Aumentar o tamanho e contraste do botão "Adicionar ao Carrinho".
    *   Remover destaque visual da imagem de "Avaliações de Clientes" (ou movê-la).
    *   Redesenhar o seletor de tamanho para ser mais intuitivo (ex: botões maiores, feedback visual).
*   **Variante B (Otimização de Conteúdo e Scroll):**
    *   Implementar todas as mudanças da Variante A.
    *   Mover a seção "FAQ" para acima da dobra, próxima à descrição do produto.
    *   Reduzir o número de "Produtos Relacionados" visíveis inicialmente para evitar sobrecarga.

**5. Métricas Primárias de Sucesso (Monitoradas no GA4):**

*   Taxa de Conversão do evento `add_to_cart`.
*   Taxa de saída da página `/produto/tenis-corrida-x`.

**6. Métricas Secundárias:**

*   Taxa de engajamento (eventos de clique no seletor de tamanho).
*   Tempo médio de engajamento na página.
*   Scroll Depth (porcentagem de rolagem).

---
```

---

## Checklist

- [x] O código de rastreamento da ferramenta de heatmap (ex: Hotjar, Clarity) está instalado corretamente via GTM em todas as páginas-chave.
- [x] Volume de tráfego suficiente (mínimo 1000 sessões, idealmente >2500) coletado para garantir significância estatística.
- [x] Análise de Click Maps realizada para identificar "dead clicks", "rage clicks" e áreas de alto/baixo engajamento.
- [x] Análise de Scroll Maps para avaliar a profundidade de rolagem e a visibilidade de conteúdo, CTAs e formulários críticos.
- [x] Análise de Move Maps (se disponível) para entender o padrão de atenção e movimento do mouse na página.
- [x] Correlação dos insights do heatmap com métricas de engajamento do GA4 (ex: taxa de rejeição, tempo médio na página, eventos de interação).
- [x] Segmentação dos heatmaps por tipo de dispositivo (desktop, mobile, tablet) e/ou fonte de tráfego para identificar padrões específicos.
- [x] Gravação de sessões (se disponível) para contextualizar padrões de heatmap, observar frustrações e pontos de atrito em tempo real.
- [x] Geração de hipóteses claras e testáveis para otimização (ex: teste A/B) baseadas nos dados do heatmap.
- [x] Documentação das descobertas, insights e recomendações em um relatório estruturado.
- [x] Plano de ação definido para implementar as otimizações e monitorar os resultados no GA4.
- [x] Avaliação da conformidade com privacidade de dados (GDPR/LGPD) na coleta de dados de heatmap e gravação de sessões.

---

## Métricas de Referência

| Métrica                         | Benchmark (Exemplo E-commerce) | Meta (Exemplo E-commerce)     |
|:--------------------------------|:-------------------------------|:------------------------------|
| Taxa de Cliques em CTA Principal | 10-15%                         | >20%                          |
| Porcentagem de Rolagem (75%)    | >50%                           | >65%                          |
| Taxa de Abandono de Formulário  | 20-30%                         | <15%                          |
| Rage Clicks por Sessão          | <0.5 cliques                   | 0 cliques                     |
| Taxa de Conversão (Página)      | 2-5%                           | >6%                           |
| Tempo Médio na Página           | 90-120 segundos                | >150 segundos                 |

---

## Erros Comuns

1.  **Analisar Heatmaps com Baixo Volume de Dados**: Conclusões baseadas em poucos dados (ex: <500 sessões por URL) são estatisticamente irrelevantes e podem levar a otimizações ineficazes.
    *   **Como evitar**: Garanta um período de coleta de dados de pelo menos 7 a 14 dias para cada URL analisada, visando um mínimo de 1000 sessões. Utilize o GA4 para monitorar o volume de tráfego antes de iniciar a análise de heatmap.
2.  **Não Segmentar a Análise por Dispositivo**: O comportamento do usuário e o layout visual variam drasticamente entre desktop, tablet e mobile. Um heatmap para desktop não reflete a experiência mobile.
    *   **Como evitar**: Sempre segmente os heatmaps por tipo de dispositivo. Ferramentas como Hotjar e Clarity permitem essa segmentação. Considere que a dobra e a forma de interação são diferentes para cada plataforma.
3.  **Focar Apenas em Cliques e Ignorar Scrolls/Movimentos**: Apenas analisar onde os usuários clicam é insuficiente. A profundidade de rolagem (scroll) e o movimento do mouse (move maps) fornecem insights cruciais sobre atenção e engajamento com o conteúdo.
    *   **Como evitar**: Combine a análise de Click Maps com Scroll Maps para entender o que é visto e ignorado. Use Move Maps para inferir áreas de atenção e gravação de sessões para contextualizar movimentos e frustrações.
4.  **Não Correlacionar com Métricas Quantitativas do GA4**: Heatmaps mostram o "onde" e "como", mas não o "quantos" ou "porquê" em escala. Sem o GA4, é difícil quantificar o impacto de um problema de UX em métricas de negócio.
    *   **Como evitar**: Sempre relacione os insights visuais do heatmap com métricas de engajamento (taxa de rejeição, tempo na página), eventos (cliques em CTAs, preenchimento de formulários) e conversões no GA4 para validar a magnitude do problema e o impacto potencial da solução.

---

## Dicas Avançadas

1.  **Segmentação de Heatmaps por Eventos ou Dimensões Personalizadas do GA4**: Use as funcionalidades de integração da sua ferramenta de heatmap para filtrar mapas por eventos específicos (ex: usuários que adicionaram um item ao carrinho mas não compraram) ou dimensões personalizadas do GA4 (ex: usuários logados, clientes recorrentes, usuários que vieram de uma campanha específica). Isso revela padrões de comportamento muito específicos para públicos-alvo relevantes.
    *   **Exemplo Prático**: No Hotjar, crie um filtro para sessões onde o evento `add_to_cart` foi acionado, mas o evento `purchase` não foi, e então analise o click map da página de checkout para identificar onde esses usuários frustrados clicam.
2.  **Análise de "Rage Clicks" e "Dead Clicks" em Gravações de Sessão**: Ferramentas avançadas de heatmap com gravação de sessão (ex: Fullstory, Smartlook) identificam automaticamente "rage clicks" (cliques repetidos e rápidos na mesma área) e "dead clicks" (cliques em elementos não interativos). Analisar as gravações de sessões com esses marcadores contextualiza a frustração do usuário e aponta diretamente para problemas de usabilidade ou bugs.
    *   **Exemplo Prático**: Filtrar gravações de sessão no Smartlook para "rage clicks" na página de produto `https://www.minhaloja.com.br/produto/camiseta-x`. Observar que usuários clicam repetidamente na imagem principal do produto, esperando uma galeria de imagens que não existe ou não é óbvia.
3.  **Heatmaps de Formulário (Form Analytics)**: Para formulários complexos (checkouts, cadastros), vá além dos heatmaps de clique/scroll e utilize as funcionalidades de Form Analytics da sua ferramenta. Analise métricas como tempo gasto por campo, abandono de campo, campos com maior erro e reenvios. Isso revela exatamente onde os usuários enfrentam dificuldades no preenchimento.
    *   **Exemplo Prático**: No Hotjar Form Analytics para o formulário de checkout, identificar que o campo "CEP" tem uma taxa de abandono de 25% e um tempo médio de preenchimento de 15 segundos, sugerindo um problema de validação ou falta de auto-preenchimento.
4.  **Teste A/B com Comparação de Heatmaps**: Ao rodar testes A/B baseados em insights de heatmap, utilize ferramentas que permitam comparar os heatmaps das diferentes variantes (controle vs. variante A). Isso oferece uma poderosa visualização de como as mudanças implementadas alteram o comportamento de clique e rolagem, complementando as métricas de conversão do GA4.
    *   **Exemplo Prático**: Após um teste