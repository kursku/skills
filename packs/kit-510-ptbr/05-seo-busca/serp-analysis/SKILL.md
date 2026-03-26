---
name: serp-analysis
description: "Serp Analysis — Skill especializada para serp analysis"
license: MIT
metadata:
  version: 1.0.0
  author: Cafe Code AI
  category: 05-seo-busca
  updated: 2026-03-01
risk: safe
---

# Serp Analysis

Esta skill capacita o Claude a executar análises aprofundadas de Search Engine Results Pages (SERPs) para identificar padrões, intenção do usuário, lacunas de conteúdo e oportunidades de otimização.

---

## Keywords

Análise de SERP, Intenção de Busca, Feature Snippets, Pessoas Também Perguntam (PAA), Conteúdo Rankeado, Análise Competitiva SEO, Semântica de Busca, Otimização On-SERP, Tipos de Resultados SERP, Conteúdo Top-Ranking, Elementos da SERP, Rich Snippets, Autoridade de Domínio.

---

## Quick Start

1.  **Pesquisar Palavra-chave Alvo**: Acesse o Google em modo anônimo e deslogado, definindo uma localização geográfica específica (ex: "São Paulo") para a palavra-chave que deseja analisar (ex: "melhor software de edição de vídeo").
2.  **Captura da SERP Completa**: Utilize uma ferramenta de captura de tela que permita rolar a página para registrar *todos* os elementos visíveis na primeira página de resultados: anúncios, Feature Snippets, People Also Ask (PAA), Imagens, Vídeos, Local Pack e os 10 resultados orgânicos.
3.  **Identificar Top Resultados Orgânicos**: Liste as URLs, títulos e meta descrições dos 3 a 5 primeiros resultados orgânicos. Anote a presença de Rich Snippets (estrelas de avaliação, preço, disponibilidade).
4.  **Classificar Intenção de Busca**: Baseado no tipo de conteúdo predominante nos resultados orgânicos e nos elementos da SERP, classifique a intenção de busca como: informativa (guias, explicações), transacional (compra, inscrição), navegacional (ir para um site específico) ou comercial investigativa (reviews, comparações).

---

## Core Workflows

### Workflow 1: Análise Competitiva de Estrutura de Conteúdo na SERP

Este workflow visa desvendar como os concorrentes de topo estruturam seu conteúdo para atender à intenção de busca e identificar oportunidades para superá-los.

1.  **Seleção das URLs Competitivas**: Para a palavra-chave "melhor cafeteira expresso", identifique as 5 primeiras URLs orgânicas que dominam a SERP. Exemplo:
    *   `https://www.blogdecafe.com.br/guia-cafeteira-expresso`
    *   `https://www.eletroreviews.com.br/top-cafeteiras-expresso`
    *   `https://www.magazinecoffe.com.br/como-escolher-cafeteira`
    *   `https://www.tudodecafe.net/comparativo-expresso`
    *   `https://www.tecnocafes.com.br/melhores-maquinas-cafe`
2.  **Análise da Estrutura de Títulos**: Acesse cada uma dessas URLs e examine a hierarquia de títulos (H1, H2, H3). Anote os principais tópicos e sub-tópicos que cada artigo aborda.
    *   **Exemplo (blogdecafe.com.br)**:
        *   H1: "Guia Completo: Escolhendo a Melhor Cafeteira Expresso para Você"
        *   H2: "Tipos de Cafeteira Expresso"
            *   H3: "Automáticas"
            *   H3: "Manuais"
            *   H3: "Semi-Automáticas"
        *   H2: "Fatores Essenciais ao Comprar"
            *   H3: "Pressão em Bares"
            *   H3: "Capacidade do Reservatório"
            *   H3: "Moedor Integrado"
        *   H2: "Marcas Recomendadas"
3.  **Mapeamento de Tipos de Mídia e Engajamento**: Observe o tipo e a quantidade de mídia utilizada (imagens de alta qualidade, infográficos, vídeos incorporados, tabelas comparativas). Avalie se a mídia é relevante e agrega valor ao texto.
    *   **Exemplo**: `eletroreviews.com.br` utiliza um vídeo review de 5 minutos no topo da página e tabelas comparativas detalhadas, além de 8-10 imagens por produto. `magazinecoffe.com.br` usa apenas 3-4 imagens estáticas.
4.  **Avaliação da Profundidade e Abrangência**: Estime a contagem de palavras média dos artigos dos top 3-5. Identifique quais sub-tópicos são abordados consistentemente por todos e quais são negligenciados ou abordados de forma superficial.
    *   **Exemplo**: A maioria dos concorrentes aborda "tipos", "fatores de compra" e "marcas". Uma lacuna pode ser "manutenção e limpeza de cafeteiras expresso" ou "impacto do tipo de grão no expresso", que são tópicos de interesse para quem já possui ou planeja comprar uma máquina.
5.  **Identificação de Oportunidades**: Com base na análise, determine como seu conteúdo pode ser mais completo, mais bem estruturado ou oferecer uma perspectiva única.
    *   **Oportunidade**: Criar um guia que, além dos tópicos comuns, inclua uma seção detalhada sobre "Como Realizar a Manutenção Preventiva da Sua Cafeteira Expresso" com um infográfico.

### Workflow 2: Otimização para Feature Snippets e Pessoas Também Perguntam (PAA)

Este workflow foca em como estruturar conteúdo para capturar Feature Snippets e responder às perguntas frequentes da seção PAA.

1.  **Análise da SERP para Snippets e PAA**: Para a palavra-chave "como fazer café coado", observe a SERP.
    *   **Feature Snippet**: Identifique se há um Feature Snippet e qual seu formato (parágrafo, lista numerada/com marcadores, tabela). Anote a URL que o ocupa.
        *   **Exemplo**: A SERP exibe um Feature Snippet de *lista numerada* da URL `receitasdecafe.com.br/preparo-coado`.
    *   **Pessoas Também Perguntam (PAA)**: Expanda *todas* as perguntas da caixa PAA e registre as perguntas e suas respectivas respostas concisas.
        *   **Exemplo de PAA**:
            *   "Qual a proporção ideal de café e água?" (Resposta: 1:15 ou 1:10)
            *   "Qual a temperatura ideal da água para café coado?" (Resposta: 90°C a 96°C)
            *   "Quanto tempo demora para fazer um café coado?" (Resposta: 3 a 5 minutos)
            *   "Qual o melhor tipo de moagem para café coado?" (Resposta: Moagem média-fina)
2.  **Mapeamento de Conteúdo Existente vs. Oportunidades**: Compare as perguntas PAA e o conteúdo do Feature Snippet com o seu próprio conteúdo (ou o que você pretende criar).
    *   **Exemplo**: Seu artigo sobre café coado já menciona a proporção e a temperatura, mas as respostas estão em parágrafos longos, não otimizadas para snippets.
3.  **Reestruturação para Snippets de Parágrafo**: Para perguntas que resultam em snippets de parágrafo, crie um parágrafo conciso (40-60 palavras) que responda diretamente à pergunta, idealmente logo após a pergunta (usando H2 ou H3).
    *   **Exemplo (para "temperatura ideal")**:
        ```html
        <h2>Qual a temperatura ideal da água para café coado?</h2>
        <p>A temperatura ideal da água para o café coado está entre 90°C e 96°C. Água muito quente pode extrair sabores amargos e queimar o pó, enquanto água fria resulta em uma extração incompleta e um café fraco. Utilize um termômetro culinário para maior precisão e controle.</p>
        ```
4.  **Reestruturação para Snippets de Lista**: Para perguntas que pedem passos ou itens, formate o conteúdo como uma lista numerada ou com marcadores.
    *   **Exemplo (para "passos para café coado")**:
        ```html
        <h2>Como fazer café coado perfeito em 5 passos:</h2>
        <ol>
            <li>**Aqueça a água**: Leve a água a 90-96°C.</li>
            <li>**Moe o café**: Moagem média-fina, na hora.</li>
            <li>**Pré-infusão (bloom)**: Despeje um pouco de água sobre o pó e aguarde 30s.</li>
            <li>**Despeje o restante da água**: Lentamente, em movimentos circulares.</li>
            <li>**Sirva**: Aprecie seu café fresco.</li>
        </ol>
        ```
5.  **Revisão e Implementação**: Garanta que as respostas sejam claras, concisas e usem a linguagem natural da pergunta. Implemente essas otimizações no seu conteúdo e monitore a SERP.

---

## Templates

### Template de Análise Competitiva de SERP

```
## Análise de Concorrentes na SERP para "[PALAVRA-CHAVE ALVO]"

**Palavra-Chave Alvo**: melhores laptops para programadores 2024
**Data da Análise**: 2024-10-27
**Localização da Busca**: Brasil (modo anônimo)
**Intenção Predominante da SERP**: Comercial Investigativa (Reviews, Comparações, Guias de Compra)

| Posição | URL                                            | Título H1 Principal                                     | Estrutura Tópicos (H2/H3 Comuns)                                | Tipos de Mídia Dominantes         | Profundidade Est. (Palavras) | Destaques/Oportunidades |
|---------|------------------------------------------------|---------------------------------------------------------|-----------------------------------------------------------------|-----------------------------------|------------------------------|-------------------------|
| 1       | `techreview.com.br/laptops-programacao`        | "Os 10 Melhores Laptops para Programadores em 2024"     | Como Escolher, Processador, RAM, Armazenamento, Placa de Vídeo, Marcas | Imagens de produto, Tabelas Comparativas, Vídeo Review (YouTube) | 2800                         | Conteúdo muito atualizado, comparações detalhadas |
| 2       | `programadorpro.dev/laptop-ideal`              | "Laptop para Programador: Guia Definitivo de Compra"    | Requisitos Mínimos, Modelos Recomendados, Portabilidade, Bateria | Imagens de produto, Infográficos de especificações | 2500                         | Foco em performance e workflow do programador |
| 3       | `guiatech.net/melhor-notebook-dev`             | "Melhores Notebooks para Desenvolvedores em 2024"       | Dicas de Escolha, Desempenho, Preço, Sistemas Operacionais      | Imagens de produto, Gráficos de benchmark | 2000                         | Aborda sistemas operacionais (Linux, Windows, MacOS) |
| 4       | `hardwaremaster.blog/laptops-codificacao`      | "Top Laptops para Codificação e Desenvolvimento de Software" | Specs Essenciais, Comparativo de Modelos, Dicas de Otimização   | Imagens de produto               | 1800                         | Foco em hardware de ponta e otimização de sistema |

**Observações Gerais da SERP**:
*   A maioria dos resultados foca em listas de "melhores" e guias de compra detalhados.
*   Há uma forte presença de conteúdo atualizado anualmente ("2024").
*   Todos os top rankers utilizam imagens de produtos e tabelas comparativas. Vídeos são um diferencial.
*   Os tópicos comuns incluem processador, RAM, armazenamento, placa de vídeo, e tela.

**Oportunidades de Conteúdo**:
*   Criar um guia que inclua uma seção sobre "Configurações de Periféricos Essenciais para Programadores" (monitores externos, teclados ergonômicos).
*   Incluir uma ferramenta interativa ou quiz para ajudar a escolher o laptop ideal baseado nas necessidades do programador.
*   Abordar a questão da "sustentabilidade e reparabilidade" dos laptops, um tópico pouco explorado na SERP.
```

### Template de Otimização para Feature Snippet (Lista Numerada)

```
## Otimizando para Feature Snippet: "Como plantar tomate em vasos"

**Palavra-Chave Alvo**: como plantar tomate em vasos
**Tipo de Snippet Observado na SERP**: Lista Numerada

## Guia Completo: Como Plantar Tomate em Vasos e Ter uma Colheita Abundante

Cultivar tomates em vasos é uma excelente opção para quem tem pouco espaço, mas deseja desfrutar de frutos frescos em casa. Siga este passo a passo para um plantio bem-sucedido:

1.  **Escolha o Vaso Ideal**: Opte por vasos com pelo menos 30-40 cm de profundidade e diâmetro, com furos de drenagem. Vasos de barro ou plástico são adequados.
2.  **Prepare o Substrato**: Utilize uma mistura de terra vegetal rica em matéria orgânica, húmus de minhoca e areia, garantindo boa drenagem e nutrientes.
3.  **Selecione as Sementes ou Mudas**: Escolha variedades de tomateiro mais compactas, como 'Cereja' ou 'Italiano Anão', ideais para vasos. Se usar sementes, plante 2-3 por vaso e raleie após a germinação.
4.  **Plante a Muda**: Faça um pequeno buraco no centro do substrato e plante a muda, enterrando parte do caule para estimular o enraizamento. Regue imediatamente.
5.  **Posicionamento e Sol**: Coloque o vaso em um local que receba no mínimo 6 a 8 horas de sol direto por dia. Varandas e terraços ensolarados são perfeitos.
6.  **Regas Regulares**: Mantenha o solo úmido, mas não encharcado. Verifique a umidade da terra diariamente, regando pela manhã ou no final da tarde.
7.  **Adubação Periódica**: A cada 15-20 dias, adube com um fertilizante orgânico balanceado, rico em potássio, essencial para a frutificação.
8.  **Tutoria e Poda**: À medida que a planta cresce, use estacas ou grades para tutoriar o tomateiro. Realize podas de limpeza para remover galhos secos ou doentes.
```

---

## Checklist

-   [x] Realizar busca em modo anônimo e com localização geográfica segmentada.
-   [x] Registrar as URLs, títulos e meta descrições dos 10 primeiros resultados orgânicos.
-   [x] Identificar a intenção de busca predominante da SERP (informativa, transacional, navegacional, comercial investigativa).
-   [x] Mapear *todos* os elementos da SERP (Ads, Feature Snippets, Pessoas Também Perguntam, Carrosséis de Imagens/Vídeos, Local Pack, Top Stories).
-   [x] Analisar a estrutura de conteúdo (H1, H2, H3, `<strong>`) dos top 3-5 concorrentes para identificar padrões de tópicos.
-   [x] Avaliar a profundidade e abrangência dos tópicos abordados pelos concorrentes, buscando lacunas de conteúdo ou sub-tópicos negligenciados.
-   [x] Observar o tipo, qualidade e quantidade de mídia utilizada pelos concorrentes (imagens otimizadas, vídeos, infográficos, tabelas).
-   [x] Verificar a presença e o tipo de Schema Markup (estrelas de avaliação, FAQs, receitas) nos resultados orgânicos.
-   [x] Expandir todas as perguntas na seção "Pessoas Também Perguntam" (PAA) e registrar as perguntas e suas respostas.
-   [x] Analisar a autoridade de domínio e relevância temática dos concorrentes para a palavra-chave.
-   [x] Identificar padrões na linguagem e termos utilizados nos títulos e descrições para otimização de CTR.
-   [x] Avaliar se a SERP demonstra "Query Deserves Freshness" (QDF) ou "Query Deserves Diversity" (QDD).

---

## Métricas de Referência

| Métrica                         | Benchmark (Exemplo) | Meta (Exemplo) |
|---------------------------------|---------------------|----------------|
| Posição Média para KW Alvo      | 4.5                 | 1.5            |
| CTR para Posição #1             | 25-30%              | 35%            |
| % de SERPs com Feature Snippet  | 12%                 | 25%            |
| Share of Voice (Top 3)          | 30%                 | 45%            |
| Tempo na Página (Top 3 Concorr.)| 3:30 min            | 4:00 min       |
| Presença em PAA                 | 15%                 | 30%            |

---

## Erros Comuns

1.  **Análise Superficial da Intenção de Busca**: Focar apenas na palavra-chave e assumir a intenção sem analisar os resultados. Ex: Para "software CRM", o Google pode mostrar tanto reviews (comercial investigativa) quanto fornecedores (transacional). **Como evitar**: Analisar os *tipos de conteúdo* e *elementos da SERP* dos top 5-10 resultados para entender a intenção predominante que o Google serve. Se a maioria são listas de "melhores", a intenção é comercial investigativa.
2.  **Ignorar Elementos Não-Orgânicos da SERP**: Concentrar-se apenas nos links azuis e negligenciar anúncios, PAA, Imagens, Vídeos, Local Pack, que podem capturar atenção e cliques. Ex: Se a SERP para "receita de bolo de cenoura" tem um Feature Snippet de receita e carrossel de imagens, otimizar apenas para o link orgânico é insuficiente. **Como evitar**: Realizar uma captura de tela *completa* da SERP e analisar *todos* os elementos visíveis, identificando quais oportunidades de visibilidade existem além do ranking orgânico tradicional.
3.  **Não Considerar Contexto de Localização e Personalização**: Realizar a análise da SERP sem modo anônimo ou sem especificar uma localização, resultando em resultados personalizados ou irrelevantes. Ex: Uma busca por "restaurante italiano" em Brasília pode mostrar resultados muito diferentes de uma busca em São Paulo. **Como evitar**: Sempre usar o modo anônimo/privado do navegador e, se possível, ferramentas de simulação de localização para garantir uma visão imparcial e relevante da SERP para o público-alvo.

---

## Dicas Avançadas

1.  **Análise de "Query Deserves Freshness" (QDF)**: Para palavras-chave sensíveis ao tempo (ex: "melhores smartphones 2024", "notícias de inteligência artificial"), observe se a SERP é dominada por conteúdo publicado ou atualizado muito recentemente. Se sim, priorize a atualização contínua do seu conteúdo para se manter relevante e competitivo.
2.  **Mapeamento de Entidades e Tópicos Associados**: Além das palavras-chave, identifique as entidades (pessoas, organizações, conceitos) e tópicos relacionados que o Google associa à sua consulta, frequentemente visíveis em PAA, carrosséis de imagens ou mesmo nas próprias descrições dos resultados. Para "história do café", entidades como "Etiópia", "século XV", "comércio", "Arábia" devem ser abordadas.
3.  **Engajamento On-SERP e Otimização para CTR**: Analise como os títulos e meta descrições dos concorrentes de topo são formulados para atrair cliques. Perceba se o Google reescreve meta descrições. Mesmo se você não for o #1, um título e descrição mais persuasivos podem gerar um CTR maior. Utilize emojis (se apropriado para seu nicho), números, e CTAs claros na meta descrição.
4.  **Análise de Intent Shift e Evolução da SERP**: Monitore SERPs importantes ao longo do tempo para detectar mudanças na intenção de busca do Google. Uma SERP que era predominantemente informativa pode se tornar transacional (ex: Google exibe mais produtos e menos artigos de guia). Adapte sua estratégia de conteúdo e SEO para corresponder a essa nova intenção.
5.  **Exploração de SERPs de Baixo Volume, Alta Intent**: Para nichos específicos, analise SERPs de palavras-chave com baixo volume de busca, mas com alta intenção de compra ou conversão (ex: "software CRM para pequenas clínicas veterinárias"). Essas SERPs podem ter menos concorrência e maior probabilidade de Feature Snippets ou rankings rápidos.