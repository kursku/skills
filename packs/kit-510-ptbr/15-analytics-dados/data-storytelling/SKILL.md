---
name: data-storytelling
description: "Data Storytelling — Skill especializada para data storytelling"
license: MIT
metadata:
  version: 1.0.0
  author: Cafe Code AI
  category: 15-analytics-dados
  updated: 2026-03-01
risk: safe
---

# Data Storytelling

Esta skill capacita o Claude a transformar dados brutos de Google Analytics em narrativas persuasivas e acionáveis para decisões de negócio.

---

## Keywords

Data Storytelling, GA4, Atribuição, Funil de Conversão, Dashboard Interativo, Narrativa de Dados, KPIs, Métricas Acionáveis, Visualização de Dados, Segmentação de Audiência, Customer Journey, Análise de Cohort, Looker Studio, BigQuery.

---

## Quick Start

1.  **Exportar Dados de Engajamento GA4**: Acesse o Google Analytics 4, navegue até "Relatórios > Engajamento > Visão geral" e exporte dados de eventos-chave (ex: `page_view`, `session_start`, `user_engagement`) para um arquivo CSV ou conecte via BigQuery para grandes volumes.
2.  **Identificar Anomalia ou Oportunidade**: Analise os dados brutos ou relatórios padrão do GA4 (ex: "Monetização > Compras e-commerce") para detectar um padrão interessante, como uma queda de 15% nas compras em dispositivos móveis ou um aumento súbito na taxa de abandono de carrinho.
3.  **Formular Hipótese Acionável**: Com base na anomalia, construa uma narrativa inicial sobre o "porquê" e o "e agora?". Exemplo: "A queda nas compras móveis pode ser devido a uma recente atualização do site que dificultou o checkout, e precisamos investigar a usabilidade."
4.  **Criar Prova Visual no Looker Studio**: Utilize o Looker Studio (Google Data Studio) para construir um gráfico simples que comprove o insight principal, como um gráfico de funil para o fluxo de compra móvel vs. desktop ou um gráfico de barras comparando taxas de conversão por período.
5.  **Apresentar a História com Recomendação**: Comunique a narrativa de forma concisa, focando no impacto para o negócio e na recomendação de ação clara, validada pelos dados do GA4.

---

## Core Workflows

### Workflow 1: Narrativa de Otimização de Funil de Checkout no GA4

Este workflow detalha como construir uma história de dados focada em otimizar o processo de checkout, utilizando dados específicos do Google Analytics 4.

**Passo 1: Identificação da Queda de Performance no Funil**
*   **Ação**: No GA4, navegue para "Explorações > Funil de Conversão". Configure um funil com os eventos `view_item`, `add_to_cart`, `begin_checkout`, `purchase`.
*   **Exemplo Concreto**: Observe uma queda de 28% na taxa de passagem do evento `add_to_cart` para `begin_checkout` nos últimos 7 dias em comparação com a média das 4 semanas anteriores. A taxa anterior era de 70%, e agora está em 42%.

**Passo 2: Coleta e Segmentação de Dados Complementares**
*   **Ação**: Utilize a exploração "Caminho do Usuário" no GA4, começando pelo evento `add_to_cart`. Segmente os usuários por dimensão `Dispositivo` (Mobile vs. Desktop) e `Origem / Mídia` (Ex: `google / cpc` vs. `direct / none`).
*   **Exemplo Concreto**: Descubra que a queda de 28% é quase inteiramente concentrada em usuários de `Mobile`, onde a taxa de passagem de `add_to_cart` para `begin_checkout` caiu de 65% para 35%. Em desktop, a queda é marginal, de 75% para 70%.
*   **Ação**: Exportar eventos `add_to_cart` e `begin_checkout` com parâmetros `item_name` e `item_category` para identificar se a queda está concentrada em produtos específicos.

**Passo 3: Construção da Hipótese Narrativa**
*   **Ação**: Formule uma hipótese clara que explique a anomalia e sirva como base para a história.
*   **Exemplo Concreto**: "A recente atualização do site impactou negativamente o fluxo de checkout para usuários móveis, resultando em uma queda de 28% na transição do carrinho para o início do processo de pagamento. A complexidade do formulário de endereço no mobile ou um problema de carregamento de imagens na página do carrinho são as principais suspeitas."

**Passo 4: Criação de Visualização de Suporte no Looker Studio**
*   **Ação**: Desenvolva um dashboard no Looker Studio (Google Data Studio) que visualize o problema de forma clara.
*   **Exemplo Concreto**: Crie um gráfico de funil mostrando a taxa de conversão por etapa do checkout, segmentado por `Dispositivo`. Adicione um gráfico de linha temporal para a taxa de passagem `add_to_cart` para `begin_checkout` nos últimos 30 dias, destacando a data da atualização do site. Inclua uma tabela com os `item_name` mais afetados pela queda.

**Passo 5: Refinamento da Mensagem e Call-to-Action**
*   **Ação**: Estruture a narrativa para o público-alvo, focando no impacto no negócio e na recomendação.
*   **Exemplo Concreto**: "Nossos dados do GA4 revelam uma queda alarmante de 28% na transição do carrinho para o checkout em dispositivos móveis, resultando em uma perda estimada de R$50.000 em receita na última semana. Esta queda coincide com a última atualização do site e afeta principalmente os produtos de categoria 'Eletrônicos'. É crucial que a equipe de UX/UI priorize uma auditoria completa do fluxo de checkout mobile, com foco na simplificação do formulário de endereço e na otimização do carregamento de imagens. Recomendamos um teste A/B para um fluxo de checkout simplificado no mobile, monitorando a métrica `taxa de conclusão de checkout` no GA4."

### Workflow 2: Atribuição de Campanhas e Impacto no LTV via GA4

Este workflow foca em como utilizar os modelos de atribuição do GA4 para contar uma história mais completa sobre o impacto das campanhas de marketing, além do último clique.

**Passo 1: Análise de Caminhos de Conversão**
*   **Ação**: No GA4, vá para "Publicidade > Caminhos de Conversão". Selecione o evento de conversão `purchase` e o modelo de atribuição "Baseado em dados".
*   **Exemplo Concreto**: Observe que enquanto o `google / cpc` (busca paga) é responsável por 60% das últimas interações, o `facebook / social` aparece em 35% das primeiras interações, mas apenas 5% das últimas. O `email / newsletter` aparece em 20% dos caminhos como uma interação intermediária.

**Passo 2: Comparação de Modelos de Atribuição**
*   **Ação**: Compare o modelo "Baseado em dados" com o "Último clique" e "Primeiro clique" para o evento `purchase` na mesma tela.
*   **Exemplo Concreto**: No modelo "Último Clique", o `google / cpc` recebe R$100.000 em receita. No "Primeiro Clique", o `facebook / social` recebe R$30.000. No "Baseado em dados", o `google / cpc` recebe R$80.000, o `facebook / social` R$15.000 e o `email / newsletter` R$10.000. Isso mostra a subestimação de canais de topo e meio de funil.

**Passo 3: Integração de Dados de Custo e Audiência**
*   **Ação**: Certifique-se de que os dados de custo de mídia foram importados para o GA4 via "Vinculações de produtos" (Google Ads, Search Console) ou "Importação de dados" (outras fontes). Crie uma audiência no GA4 para usuários que interagiram com `facebook / social` mas não converteram em 7 dias.
*   **Exemplo Concreto**: O custo mensal das campanhas de `facebook / social` é de R$10.000. Sem o modelo "Baseado em dados", o ROI pareceria negativo. A audiência "Interação Social sem Compra" tem 50.000 usuários.

**Passo 4: Criação de Visualização de Atribuição no Looker Studio**
*   **Ação**: Desenvolva um dashboard no Looker Studio que ilustre a contribuição de cada canal em diferentes pontos da jornada.
*   **Exemplo Concreto**: Crie um gráfico de barras empilhadas mostrando a receita atribuída por `Origem / Mídia` para os modelos "Último Clique" e "Baseado em Dados". Adicione um gráfico de dispersão mostrando o `CPA` vs. `Número de Primeiras Interações` para cada canal.

**Passo 5: Contando a História Acionável de Otimização de Budget**
*   **Ação**: Apresente a história para justificar um rebalanceamento de orçamento ou novas estratégias.
*   **Exemplo Concreto**: "Avaliando os caminhos de conversão e utilizando o modelo de atribuição 'Baseado em dados' do GA4, descobrimos que, embora o `google / cpc` seja o finalizador de vendas (R$80.000 de receita atribuída), o `facebook / social` é um catalisador crucial no topo do funil, contribuindo com R$15.000 de receita em interações iniciais que antes eram ignoradas pelo 'Último Clique'. Ignorar o `facebook / social` significaria perder 35% das primeiras interações dos usuários que eventualmente compram. Recomendamos realocar 10% do orçamento do `google / cpc` para campanhas de retargeting de alta intenção direcionadas à audiência 'Interação Social sem Compra' via Google Ads. Essa estratégia visa otimizar a transição do awareness gerado pelo social para a conversão, aumentando o ROI geral do marketing."

---

## Templates

### Template de Briefing para Storytelling de Dados

```
Título da Narrativa: Otimização da Experiência Mobile no Funil de Checkout
Objetivo Principal da História: Convencer a equipe de desenvolvimento e UX a priorizar a correção de problemas no checkout mobile.
Público-Alvo: Gerentes de Produto, Equipe de UX/UI, Head de E-commerce.
Métrica Chave (GA4): Taxa de abandono do evento 'begin_checkout' após 'add_to_cart' em dispositivos móveis.
Dados de Suporte (GA4):
- Relatório Base: Explorações > Funil de Conversão (passos: view_item, add_to_cart, begin_checkout, purchase)
- Segmentação: Dispositivo = 'mobile', Novas Aquisições vs. Usuários Recorrentes.
- Eventos: add_to_cart, begin_checkout, form_submit_error (se configurado).
- Dimensões: item_name, item_category, page_location (URL da página de checkout).
- Período: Últimos 7 dias comparados com as 4 semanas anteriores.
Insight Principal: Queda de 28% na taxa de passagem de 'add_to_cart' para 'begin_checkout' em mobile, resultando em R$50.000 de perda de receita semanal. Desktop manteve estabilidade.
Causa Raiz Potencial: Problemas de usabilidade no formulário de endereço mobile (ex: campos pequenos, teclado incorreto, validação de CEP demorada) ou carregamento lento de imagens no carrinho.
Recomendação de Ação: Conduzir testes de usabilidade com usuários mobile, simplificar o formulário de checkout mobile para o mínimo de campos, e otimizar o carregamento de imagens na página do carrinho.
Métricas para Monitorar Pós-Implementação: Taxa de conclusão de checkout mobile, receita de e-commerce mobile, tempo médio de engajamento na página de checkout.
```

### Template de Resumo Executivo para Análise de Atribuição e ROI

```
Assunto: Reavaliando o Impacto Real dos Canais de Marketing no GA4 (Modelo Baseado em Dados)
Para: Equipe de Marketing, Head de Vendas, CFO
Data: 2024-11-15
Resumo Executivo:
Nossa análise aprofundada de atribuição no GA4, utilizando o modelo "Baseado em dados", revela que o tráfego pago (Google Ads) continua sendo vital para as conversões de última interação (60% das `purchases`). No entanto, a contribuição dos canais de topo de funil foi subestimada. Campanhas de redes sociais (Facebook/Instagram) e email marketing (newsletters) desempenham papéis cruciais nas fases iniciais e intermediárias da jornada do cliente, sendo responsáveis por 35% e 20% das primeiras e intermediárias interações, respectivamente, que levam à compra. O reconhecimento dessas contribuições indiretas ajusta o ROI percebido e justifica investimentos mais equilibrados.
Principais Insights:
1.  **Paid Search (Google Ads)**: Impulsionador primário de conversões diretas, com CPA eficaz para o final do funil.
2.  **Social Media (Facebook/Instagram)**: Gerador de awareness e interesse no topo do funil; antes subestimado pelo modelo de Último Clique.
3.  **Email Marketing**: Canal estratégico de nutrição, atuando como um lembrete crucial no meio do funil.
Recomendações:
1.  **Otimizar Mix de Canais**: Ajustar o orçamento de marketing para refletir a contribuição real de cada canal, alocando mais recursos para fortalecer a presença de conteúdo nas redes sociais e em campanhas de email para nutrição de leads.
2.  **Retargeting Estratégico**: Criar audiências no GA4 para usuários que interagiram com campanhas sociais ou emails, mas não converteram, e direcionar campanhas de retargeting personalizadas no Google Ads e Facebook.
3.  **Monitoramento de LTV**: Acompanhar o Lifetime Value (LTV) dos clientes por caminho de atribuição inicial para entender o valor a longo prazo de diferentes fontes de aquisição, além da conversão imediata.
```

---

## Checklist

- [x] Identificar a principal métrica de negócio no GA4 que será o foco da história (ex: `purchase`, `lead_generation`, `add_to_cart`).
- [x] Selecionar um período de comparação relevante no GA4 (ex: "últimos 7 dias vs. 7 dias anteriores", "este mês vs. mês anterior").
- [x] Segmentar a audiência no GA4 (ex: por `Dispositivo`, `Origem / Mídia`, `País`, `Novos Usuários vs. Recorrentes`) para encontrar insights ocultos.
- [x] Utilizar as "Explorações" do GA4 (Funil de Conversão, Caminho do Usuário, Análise de Cohort) para diagnosticar anomalias ou tendências.
- [x] Coletar dados complementares de outras fontes (ex: CRM, dados de custo de campanha importados para o GA4 via API ou CSV) para enriquecer o contexto.
- [x] Formular uma hipótese clara ou um problema de negócio que a história de dados irá responder ou resolver.
- [x] Escolher a visualização de dados mais eficaz no Looker Studio (ou outra ferramenta) para comunicar o insight principal (ex: gráfico de funil para conversão, barras para comparação, linha para tendências).
- [x] Elaborar uma recomendação de ação concreta, mensurável e alinhada aos objetivos de negócio, baseada nos dados do GA4.
- [x] Personalizar a linguagem e o nível de detalhe da história para o público-alvo, evitando jargões técnicos desnecessários.
- [x] Praticar a apresentação da história, garantindo uma narrativa fluida e uma mensagem clara e impactante.

---

## Métricas de Referência

| Métrica GA4 | Benchmark (Médio do Mercado) | Meta (Otimizado) |
|:------------|:-----------------------------|:-----------------|
| Taxa de Conversão E-commerce (`purchase`) | 2.5% - 4.0%                 | 3.5% - 5.0%      |
| Taxa de Abandono de Carrinho (`begin_checkout` sem `purchase`) | 65% - 80%                   | 55% - 65%        |
| Taxa de Engajamento (sessões engajadas / total) | 40% - 60%                   | 50% - 70%        |
| Custo por Aquisição (CPA) (`purchase` via Google Ads) | Varia muito por setor (ex: R$50-R$200) | < 1/3 do LTV     |
| Lifetime Value (LTV) (cliente recorrente) | > CPA                         | 2-3x CPA         |
| Duração Média da Sessão Engajada | 60 - 90 segundos            | 90 - 120 segundos|

---

## Erros Comuns

1.  **Apresentar dados brutos sem contexto ou significado**: Mostrar um gráfico de linha de vendas com um pico sem explicar o que causou o aumento (ex: "Aqui estão as vendas do último mês.").
    *   **Como evitar**: Sempre contextualize as variações com eventos externos (lançamentos de produto, campanhas de marketing, feriados, ações da concorrência) ou internos (mudanças no site, promoções), utilizando anotações de data no Looker Studio ou comparando segmentos de tempo no GA4. Conecte cada dado a um evento ou fator externo que o influenciou.
2.  **Focar apenas no