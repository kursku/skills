---
name: seo-analytics
description: "Seo Analytics — Skill especializada para seo analytics"
license: MIT
metadata:
  version: 1.0.0
  author: Cafe Code AI
  category: 15-analytics-dados
  updated: 2026-03-01
risk: safe
---

# Seo Analytics

Capacita o Claude a realizar análises de SEO aprofundadas usando dados do Google Analytics 4 e Google Search Console, identificando oportunidades de otimização e gerando relatórios acionáveis para melhorar o desempenho orgânico.

---

## Keywords

Google Analytics 4, GA4, Google Search Console, GSC, SEO técnico, SERP, Core Web Vitals, análise de tráfego orgânico, atribuição de conversão, rank tracking, otimização de conteúdo, análise de funil, Looker Studio, relatórios personalizados GA4, métricas SEO, eventos GA4, dimensões personalizadas.

---

## Quick Start

1.  **Conectar GA4 ao Google Search Console (GSC)**: No painel de administração do GA4, em "Configurações do produto" > "Vinculações com o Google", vincule a propriedade GA4 à propriedade correspondente do GSC para habilitar os relatórios de pesquisa orgânica.
2.  **Configurar Eventos de Conversão Essenciais**: Implementar e marcar como conversão no GA4 eventos como `form_submit`, `purchase`, `generate_lead` ou `contact_us` para monitorar o impacto direto do SEO nas metas de negócio.
3.  **Criar Exploração de Páginas Orgânicas Críticas**: No GA4, acesse "Explorar" > "Em branco", use "Página e tela" como dimensão e "Sessões orgânicas" como métrica, segmentando para ver o desempenho de URLs de alto valor.
4.  **Monitorar Core Web Vitals (CWV) no GSC**: Navegue até "Core Web Vitals" no GSC para identificar URLs com problemas de LCP, FID e CLS, priorizando as correções para as páginas mais importantes para o SEO.
5.  **Configurar um Dashboard Simples no Looker Studio**: Crie um dashboard básico puxando dados do GA4 (tráfego orgânico, conversões) e GSC (impressões, cliques, CTR, posição média) para uma visão consolidada do desempenho SEO.

---

## Core Workflows

### Workflow 1: Análise de Desempenho de Conteúdo Orgânico para Otimização e Expansão

Este workflow detalha como identificar páginas de conteúdo com alto potencial de otimização ou expansão baseada em dados de comportamento do usuário e desempenho de busca.

1.  **Coleta Inicial de Dados no GA4**:
    *   Acesse o GA4 e navegue até "Relatórios" > "Engajamento" > "Páginas e telas".
    *   Adicione a "Dimensão Secundária" "Grupo de Canais padrão da sessão".
    *   Filtre a tabela para exibir apenas "Organic Search".
    *   Exporte os dados para o Google Sheets ou CSV, incluindo "Visualizações", "Sessões", "Taxa de Engajamento", "Tempo médio de engajamento" e "Taxa de rejeição" (se configurada via GTM/propriedade personalizada).

2.  **Coleta de Dados Complementares no GSC**:
    *   Acesse o Google Search Console e vá para "Resultados da Pesquisa".
    *   Aplique um filtro de "Página" para as URLs identificadas no passo 1.
    *   Exporte os dados de "Cliques", "Impressões", "CTR" e "Posição média" para essas mesmas URLs no período correspondente.

3.  **Análise e Identificação de Oportunidades**:
    *   **Identificação de Alto Tráfego/Baixo Engajamento**: No Google Sheets, cruze os dados. Procure URLs com **alto volume de visualizações/sessões orgânicas (Ex: > 5.000 visualizações/mês)**, mas com **baixa taxa de engajamento (< 50%)** ou **alto tempo médio de engajamento curto (< 45 segundos)**.
        *   *Exemplo Prático*: A página `/blog/guia-completo-seo-2024` tem 15.000 visualizações orgânicas, mas a taxa de engajamento é de 42% e o tempo médio é de 30 segundos. Isso indica que os usuários chegam, mas não se engajam profundamente.
        *   *Ação Sugerida*: Otimizar o conteúdo com sub-títulos, imagens, vídeos, CTAs mais claros, melhorar a legibilidade, ou adicionar seções de perguntas frequentes.
    *   **Identificação de Baixo CTR/Alta Posição**: Analise URLs que aparecem na **primeira página do Google (posição média 1-10)**, mas com **CTR abaixo da média para essa posição (Ex: < 3% para posições 4-6)**.
        *   *Exemplo Prático*: A página `/servicos/consultoria-seo` tem posição média 5, mas CTR de apenas 2.1%.
        *   *Ação Sugerida*: Otimizar o título (Title Tag) e a descrição (Meta Description) no HTML para torná-los mais atraentes e relevantes para a busca do usuário. Considerar uso de Rich Snippets.
    *   **Identificação de Posição Média Baixa/Alto Potencial**: Encontre URLs com **posição média entre 11 e 20** que recebem um bom volume de impressões.
        *   *Exemplo Prático*: A página `/blog/ferramentas-analise-seo` tem posição média 12 com 80.000 impressões/mês.
        *   *Ação Sugerida*: Melhorar o conteúdo existente, construir links internos e externos, e buscar palavras-chave relacionadas de cauda longa para reforçar a relevância e autoridade da página.

4.  **Priorização e Plano de Ação**:
    *   Priorize as oportunidades com base no volume de tráfego, potencial de conversão e facilidade de implementação.
    *   Crie um plano de ação detalhado para cada URL identificada, especificando as otimizações de conteúdo, SEO técnico ou de links que serão realizadas.

### Workflow 2: Análise de Atribuição de Conversão Orgânica e Otimização de Funil

Este workflow foca em entender como a busca orgânica contribui para as conversões e como otimizar o funil de vendas baseado nesses insights.

1.  **Verificação de Configuração de Conversões no GA4**:
    *   Acesse o GA4 e vá para "Administrador" > "Eventos".
    *   Confirme que os eventos de conversão (e.g., `purchase`, `generate_lead`, `form_submit`) estão marcados como "Conversão".
    *   Verifique se os valores de conversão, se aplicável, estão sendo coletados corretamente.

2.  **Análise dos Caminhos de Conversão**:
    *   Navegue até "Publicidade" > "Atribuição" > "Caminhos de conversão".
    *   Selecione a conversão principal que deseja analisar (e.g., "purchase").
    *   Observe os "Caminhos de Canal" que incluem "Organic Search".
    *   *Exemplo Prático*: Para a conversão "generate_lead", 60% dos caminhos que terminam em conversão tiveram "Organic Search" em algum ponto. Desses, 30% tiveram "Organic Search" como primeiro toque, e 20% como último toque.
    *   *Insight*: Isso indica que a busca orgânica é crucial tanto na fase de descoberta quanto na decisão final do usuário.

3.  **Comparação de Modelos de Atribuição**:
    *   Acesse "Publicidade" > "Atribuição" > "Comparação de modelos".
    *   Selecione a mesma conversão.
    *   Compare o "Organic Search" em diferentes modelos de atribuição: "Último Clique" (padrão do GA4), "Primeiro Clique", "Linear" e "Baseado em Posição".
    *   *Exemplo Prático*:
        *   "Último Clique": Organic Search = 120 conversões.
        *   "Primeiro Clique": Organic Search = 180 conversões.
        *   "Linear": Organic Search = 150 conversões.
        *   "Baseado em Posição": Organic Search = 165 conversões.
    *   *Insight*: O modelo "Primeiro Clique" atribui mais conversões ao SEO, sugerindo que o conteúdo orgânico desempenha um papel significativo em iniciar a jornada do cliente, mesmo que outro canal finalize a conversão.

4.  **Criação de Exploração de Funil para Otimização**:
    *   Vá para "Explorar" > "Em branco".
    *   Crie um "Funil de exploração" com os seguintes passos (exemplo para e-commerce):
        *   Passo 1: Sessão orgânica em `/blog/review-produto-x` (página de topo de funil)
        *   Passo 2: Visualização de `/categoria/produto-x` (página de categoria/produto)
        *   Passo 3: Adição ao carrinho
        *   Passo 4: Compra
    *   *Exemplo Prático*: O funil mostra uma queda de 70% entre o Passo 1 e o Passo 2 para usuários orgânicos.
    *   *Ação Sugerida*: Otimizar o CTA na página do blog `review-produto-x` ou melhorar a relevância do conteúdo para direcionar mais usuários para a página de produto.

5.  **Otimização Baseada em Insights de Atribuição e Funil**:
    *   Se o SEO é forte no primeiro toque, invista em conteúdo de topo de funil (blog posts, guias) para atrair novos usuários.
    *   Se o SEO é forte no último toque, otimize páginas de produto/serviço e landing pages com foco em conversão (CTAs claros, prova social).
    *   Use os insights do funil para identificar gargalos e otimizar a experiência do usuário em cada etapa.

---

## Templates

### Relatório de Desempenho SEO Mensal (Looker Studio - Resumo)

```
# Relatório Mensal de Desempenho SEO - [Nome da Empresa]
**Período:** 01/01/2024 - 31/01/2024 (vs. 01/12/2023 - 31/12/2023)

---

## 1. Visão Geral do Tráfego Orgânico (GA4)

| Métrica GA4              | Valor Atual | Variação Mês-a-Mês |
|--------------------------|-------------|--------------------|
| Usuários Orgânicos       | 58.700      | +15%               |
| Sessões Orgânicas        | 65.200      | +12%               |
| Visualizações de Página Orgânicas | 185.000     | +10%               |
| Taxa de Engajamento Orgânica | 62%         | +2pp               |
| Tempo Médio de Engajamento | 00:01:15    | +5s                |

## 2. Desempenho da Pesquisa (GSC)

| Métrica GSC              | Valor Atual | Variação Mês-a-Mês |
|--------------------------|-------------|--------------------|
| Cliques Orgânicos        | 22.500      | +18%               |
| Impressões Orgânicas     | 980.000     | +8%                |
| CTR Orgânico Médio       | 2.29%       | +0.2pp             |
| Posição Média Orgânica   | 15.3        | -1.5 (Melhora)     |

## 3. Conversões Orgânicas (GA4)

| Métrica GA4              | Valor Atual | Variação Mês-a-Mês |
|--------------------------|-------------|--------------------|
| Conversões de Lead (Orgânico) | 350         | +25%               |
| Taxa de Conversão de Lead (Orgânico) | 0.53%       | +0.1pp             |
| Receita Orgânica (se aplicável) | R$ 25.000   | +30%               |

---

## Top 5 Páginas Orgânicas por Visualizações (GA4)

1.  `/blog/guia-seo-avancado`: 18.200 visualizações
2.  `/servicos/auditoria-seo`: 15.500 visualizações
3.  `/blog/ferramentas-analytics`: 12.100 visualizações
4.  `/contato`: 9.800 visualizações
5.  `/cases`: 7.500 visualizações

## Top 5 Consultas Orgânicas por Cliques (GSC)

1.  "consultoria seo preço": 1.500 cliques
2.  "o que é seo analytics": 1.200 cliques
3.  "auditoria seo gratuita": 950 cliques
4.  "melhores ferramentas seo": 880 cliques
5.  "como fazer seo no site": 720 cliques

---

## Próximos Passos e Recomendações:

*   **Otimização de Conteúdo**: Revisar `/blog/ferramentas-analytics` para melhorar a taxa de engajamento (atualmente 48%) com vídeos e exemplos práticos.
*   **Expansão de Palavras-chave**: Criar novo conteúdo focado em "ferramentas de análise de concorrentes" e "relatórios personalizados GA4" para capturar mais buscas de cauda longa.
*   **Melhoria de CTR**: Testar novas meta descrições para a consulta "consultoria seo preço" para aumentar o CTR, atualmente em 3.5% (posição 3).
*   **Core Web Vitals**: Priorizar otimizações de LCP para a página `/servicos/auditoria-seo` que apresenta problemas, afetando 15% dos usuários móveis.
```

### Configuração de Dimensão Personalizada no GA4 (via GTM)

```javascript
// Passo 1: Configurar a Dimensão Personalizada no GA4
//   Acesse GA4 > Administrador > Configurações de dados > Definições personalizadas.
//   Clique em "Criar dimensões personalizadas".
//   Nome da dimensão: "Tipo de Conteúdo"
//   Escopo: Evento
//   Descrição: "Indica o tipo de conteúdo da página (Blog, Produto, Serviço)"
//   Parâmetro do evento: "content_type" (este será o nome do parâmetro que enviaremos)

// Passo 2: Implementar o envio do parâmetro "content_type" via Google Tag Manager (GTM)
//   Crie uma variável de Camada de Dados para extrair o tipo de conteúdo (ex: do URL ou de um elemento na página).
//   Exemplo de Data Layer Push em uma página de blog, executado antes da tag de configuração do GA4:

    <script>
      window.dataLayer = window.dataLayer || [];
      window.dataLayer.push({
        'event': 'set_content_type',
        'content_type': 'Blog Post' // Ou 'Product Page', 'Service Page', etc.
      });
    </script>

//   No GTM, na tag de configuração do GA4 (GA4 - Config):
//     Em "Campos a Definir", adicione uma linha:
//       Nome do Campo: content_type
//       Valor: {{Variável de Camada de Dados - content_type}} (crie uma variável de camada de dados com o nome 'content_type')

// Passo 3: Criar um Evento Personalizado no GTM (Opcional, se o content_type for ativado por um evento específico)
//   Tipo de Tag: Google Analytics: Evento GA4
//   Tag de Configuração: GA4 - Config
//   Nome do Evento: page_view_with_type (ou qualquer nome relevante)
//   Parâmetros do Evento:
//     Nome do parâmetro: content_type
//     Valor do parâmetro: {{Variável de Camada de Dados - content_type}}
//   Acionamento: Page View - Window Loaded (ou um acionador mais específico, se houver lógica para definir o tipo de conteúdo)

// Benefício: Agora você pode usar "Tipo de Conteúdo" como uma dimensão em seus relatórios de exploração do GA4 para analisar o desempenho orgânico por tipo de conteúdo (Ex: Quais blogs geram mais sessões orgânicas e conversões?).
```

---

## Checklist

- [x] Validar a vinculação do GA4 com o Google Search Console.
- [x] Confirmar que os eventos de conversão primários estão configurados e marcados como conversão no GA4.
- [x] Criar um segmento de "Tráfego Orgânico" no GA4 para análises detalhadas.
- [x] Implementar ou verificar as Core Web Vitals no GSC para URLs críticas.
- [x] Configurar um relatório de exploração de funil no GA4 para a jornada do usuário orgânico até a conversão.
- [x] Analisar a contribuição do canal "Organic Search" nos relatórios de "Caminhos de Conversão" e "Comparação de Modelos" do GA4.
- [x] Verificar a indexação e cobertura de páginas importantes no relatório "Indexação > Páginas" do GSC.
- [x] Configurar alertas personalizados no GA4 para quedas significativas de tráfego orgânico ou conversões.
- [x] Realizar uma auditoria de links internos em páginas de alto desempenho orgânico para otimizar o fluxo de PageRank e relevância.
- [x] Mapear palavras-chave de alto volume/intenção de busca para páginas de destino específicas, verificando se há lacunas de conteúdo.

---

## Métricas de Referência

| Métrica                   | Benchmark (Varia por setor) | Meta (Exemplo) |
|---------------------------|-----------------------------|----------------|
| CTR Orgânica Média (GSC)  | 3% - 8% (Posição 1-5)       | > 5%           |
| Posição Média Orgânica (GSC) | Top 10 (páginas importantes) | Top 3          |
| Taxa de Engajamento Orgânica (GA4) | > 55%                       | > 65%          |
| Taxa de Conversão Orgânica (GA4) | 1.0% - 3.0%                 | > 1.8%         |
| Tempo Médio de Engajamento (Orgânico) | > 60 segundos               | > 90 segundos  |
| LCP (Largest Contentful Paint) (GSC) | < 2.5 segundos              | < 1.8 segundos |

---

## Erros Comuns

1.  **Não segmentar dados orgânicos no GA4**: Analisar métricas como "Visualizações de Página" ou "Sessões" sem aplicar o filtro "Organic Search" ou segmento de tráfego orgânico distorce a performance real do SEO, misturando dados de tráfego pago, direto, referência, etc.
    *   **Como evitar**: Sempre utilize a dimensão "Grupo de Canais padrão da sessão" e filtre por "Organic Search" em relatórios padrões, ou crie um segmento de "Tráfego Orgânico" para aplicar em explorações e relatórios personalizados.
    *   *Exemplo*: Um relatório de "Páginas e Telas" mostrando 100.000 visualizações pode parecer bom, mas se apenas 30.000 são orgânicas, o SEO tem um impacto menor do que o aparente.

2.  **Ignorar a atribuição de primeiro clique para SEO**: Focar apenas no modelo de "Último Clique" para avaliar o SEO pode subestimar significativamente o valor da busca orgânica, especialmente para conteúdos de topo de funil que introduzem o usuário ao site antes de uma conversão posterior via outro canal.
    *   **Como evitar**: Utilize os relatórios de "Caminhos de Conversão" e "Comparação de Modelos" do GA4. Compare o desempenho do "Organic Search" sob modelos como "Primeiro Clique" e "Baseado em Posição" para entender seu papel na descoberta e na jornada completa do cliente.
    *   *Exemplo*: Se o "Organic Search" contribui com 25% das conversões no modelo de "Último Clique", mas 40% no modelo de "Primeiro Clique", o investimento em conteúdo que atrai novos usuários via busca orgânica é mais valioso do que apenas a métrica de "último toque" sugere.

3.  **Não cruzar dados do GA4 com o GSC**: Analisar apenas o GA4 (comportamento pós-clique) ou apenas o GSC (visibilidade pré-clique) fornece uma visão incompleta da performance SEO. A desconexão impede a identificação de oportunidades de otimização de conteúdo e de SERP.
    *   **Como evitar**: Garanta que o GA4 esteja vinculado ao GSC e utilize os relatórios de "Aquisição > Pesquisa Orgânica do Google" no GA4. Para análises mais profundas, exporte e cruze manualmente dados de ambos (ex: páginas com alta impressão/baixa CTR no GSC + baixo engajamento no GA4 = otimização de meta-descrição e conteúdo).
    *   *Exemplo*: Uma página com 100.000 impressões no GSC, mas apenas 1% de CTR e 500 cliques no GA4, seguida por uma baixa taxa de engajamento no GA4, indica que a página aparece na busca, mas não atrai cliques eficazes ou não satisfaz a intenção do usuário após o clique.

---

## Dicas Avançadas

1.  **Criação de Audiências Preditivas para Retargeting SEO**: No GA4, crie audiências preditivas (ex: "Usuários prováveis de comprar nos próximos 7 dias" ou "Usuários prováveis de abandonar") e, em seguida, refine essas audiências adicionando um filtro para "Primeira sessão" = "Organic Search". Use essas audiências no Google Ads para campanhas de retargeting altamente segmentadas, oferecendo conteúdo ou ofertas específicas para usuários orgânicos com alta intenção ou em risco de churn.
    *   *Exemplo Prático*: Criar uma audiência de "Compradores prováveis" que chegaram via busca orgânica para um blog post sobre "melhores notebooks para programação" e direcionar anúncios de retargeting para páginas de produtos de notebooks.

2.  **Análise de Contribuição de Conteúdo por Cluster de Tópicos**: Implemente uma dimensão personalizada no GA4 chamada "Cluster de Tópicos" (via GTM, extraindo do URL, tags internas ou campo de categoria).