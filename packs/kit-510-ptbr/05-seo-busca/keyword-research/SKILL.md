---
name: keyword-research
description: "Keyword Research — Skill especializada para keyword research"
license: MIT
metadata:
  version: 1.0.0
  author: Cafe Code AI
  category: 05-seo-busca
  updated: 2026-03-01
risk: safe
---

# Keyword Research

Esta skill capacita o Claude a executar análises de palavra-chave aprofundadas, identificar oportunidades de tráfego orgânico e otimizar estratégias de conteúdo para SEO.

---

## Keywords

*   Análise de intenção de busca
*   Palavras-chave de cauda longa
*   Cluster de tópicos (Topic Clusters)
*   Gap de conteúdo (Content Gap Analysis)
*   Dificuldade de palavra-chave (KD)
*   Volume de busca orgânica
*   SERP features
*   Palavras-chave LSI (Latent Semantic Indexing)
*   Oportunidades PAA (People Also Ask)
*   Análise de concorrência orgânica
*   Mapeamento de jornada do cliente por keyword
*   Palavras-chave de marca (branded keywords)

---

## Quick Start

1.  **Identificar concorrentes diretos e indiretos relevantes para o nicho**: Utilizar buscas no Google como `site:amazon.com "melhor cafeteira"` ou `site:magazinevoce.com.br "melhor cafeteira"` para encontrar players com bom ranqueamento para termos importantes.
2.  **Extrair as top 100 palavras-chave ranqueadas dos 5 principais concorrentes**: Usar ferramentas como SEMrush (Organic Research -> Posições) ou Ahrefs (Site Explorer -> Organic Keywords) para exportar os dados de palavras-chave que geram tráfego para esses domínios.
3.  **Filtrar por palavras-chave com Volume de Busca > 500 e Dificuldade de Palavra-Chave (KD) < 40**: Aplicar esses filtros na planilha exportada para focar em oportunidades de médio/alto volume com competitividade moderada, facilitando o ranqueamento inicial.
4.  **Agrupar as palavras-chave filtradas por intenção de busca e tópicos semânticos**: Organizar as palavras-chave restantes em grupos temáticos (clusters) e determinar se a intenção é informacional (ex: "como fazer café"), comercial (ex: "melhores cafeteiras") ou transacional (ex: "comprar cafeteira expresso").

---

## Core Workflows

### Workflow 1: Análise de Gap de Conteúdo por Palavra-Chave com Ferramentas Profissionais

Este workflow visa identificar palavras-chave para as quais seus concorrentes ranqueiam bem, mas seu domínio não, revelando oportunidades diretas para criação ou otimização de conteúdo.

*   **Passo 1: Seleção de Concorrentes Chave para Análise**:
    *   Identifique 3 a 5 concorrentes diretos e indiretos que competem pelo mesmo público-alvo ou que ranqueiam para termos relevantes em seu nicho.
    *   **Exemplo**: Para um e-commerce de eletrônicos, os concorrentes podem ser `magazinevoce.com.br`, `zoom.com.br`, `buscape.com.br` e `kabum.com.br`.

*   **Passo 2: Coleta de Dados de Palavras-Chave Ranqueadas e Comparação**:
    *   Utilize a funcionalidade "Content Gap" ou "Keyword Gap" em ferramentas como SEMrush ou Ahrefs.
    *   Insira seu domínio principal (Ex: `meudominio.com.br`) como domínio-alvo e os domínios dos concorrentes identificados no Passo 1.
    *   Configure a ferramenta para mostrar palavras-chave onde os concorrentes ranqueiam (Ex: Top 10) e seu domínio *não ranqueia* ou ranqueia fora das 20 primeiras posições.
    *   **Exemplo**: No SEMrush, em "Gap de Palavras-Chave", coloque `meudominio.com.br` e adicione `magazinevoce.com.br`, `zoom.com.br`, `buscape.com.br`. Filtre para "meudominio.com.br" não ranquear nas top 20, e os concorrentes ranquearem nas top 10.

*   **Passo 3: Filtragem e Priorização de Oportunidades de Palavra-Chave**:
    *   Aplique filtros adicionais aos resultados:
        *   **Volume de Busca**: Mínimo de 300 buscas mensais.
        *   **Dificuldade de Palavra-Chave (KD)**: Máximo de 50 (para focar em termos alcançáveis).
        *   **Intenção de Busca**: Priorize termos com intenção comercial ou transacional, se a meta for vendas, ou informacional se a meta for autoridade.
    *   **Exemplo**: Palavras-chave filtradas: "melhor fone de ouvido bluetooth custo benefício" (Volume: 1.500, KD: 35), "promoção notebook gamer" (Volume: 4.000, KD: 42), "review tv 4k samsung" (Volume: 900, KD: 28).

*   **Passo 4: Análise Aprofundada da SERP e Intenção de Busca**:
    *   Para cada palavra-chave priorizada, realize uma busca manual no Google para analisar os 3-5 primeiros resultados.
    *   Observe o formato de conteúdo dominante (lista, review, comparativo, guia, página de produto), os recursos da SERP (Featured Snippets, PAA, vídeos) e a profundidade do conteúdo.
    *   **Exemplo**: Para "melhor fone de ouvido bluetooth custo benefício", a SERP mostra predominantemente artigos de listas e comparativos de blogs de tecnologia. A intenção é comercial/informacional.

*   **Passo 5: Geração de Ideias de Conteúdo e Mapeamento de Palavras-Chave**:
    *   Com base na análise, crie um plano de conteúdo detalhado para as palavras-chave identificadas.
    *   **Exemplo**: Para "melhor fone de ouvido bluetooth custo benefício", a ideia de conteúdo é "Guia Completo: Os Melhores Fones Bluetooth Custo-Benefício de 2024", incluindo uma tabela comparativa, review de cada modelo e seção de "Perguntas Frequentes". Para "promoção notebook gamer", criar uma página de categoria ou um artigo de "Melhores Ofertas de Notebook Gamer".

### Workflow 2: Otimização de Conteúdo Existente para Cobertura de Tópicos e Palavras-Chave Semânticas

Este workflow foca em melhorar o desempenho de páginas já existentes, expandindo sua relevância para um conjunto mais amplo de palavras-chave relacionadas e aprofundando a cobertura de tópicos.

*   **Passo 1: Identificação de Páginas com Potencial de Otimização**:
    *   No Google Search Console (GSC), navegue até "Resultados da Pesquisa" e filtre por páginas com boa quantidade de impressões, mas CTR baixo ou posição média entre 5 e 15.
    *   No Google Analytics 4 (GA4), identifique páginas com bom tráfego orgânico mas que podem ter um tempo na página ou engajamento abaixo do ideal.
    *   **Exemplo**: Uma página de blog "Como escolher um notebook para estudar" tem 10.000 impressões, posição média 8, mas CTR de 2.5%. Há potencial para melhorar.

*   **Passo 2: Análise de Palavras-Chave Relacionadas e LSI (Latent Semantic Indexing)**:
    *   No GSC, para a página identificada, veja as consultas que já a acionam.
    *   Use ferramentas como SEMrush Topic Research, AnswerThePublic ou o próprio Google (seção "Pesquisas relacionadas" e "People Also Ask" - PAA) para encontrar termos semanticamente relacionados e perguntas comuns.
    *   **Exemplo**: Para "notebook para estudar", termos relacionados podem ser "notebook leve para faculdade", "melhores marcas de notebook para estudante", "configuração ideal notebook estudo", "duração bateria notebook estudo", "notebook bom e barato para estudante".

*   **Passo 3: Análise da SERP para Cobertura de Tópicos dos Concorrentes**:
    *   Pesquise a palavra-chave principal (Ex: "notebook para estudar") no Google e analise os top 5 resultados.
    *   Identifique os subtópicos, seções e perguntas que esses conteúdos abordam e que seu conteúdo atual pode não cobrir adequadamente.
    *   **Exemplo**: Concorrentes cobrem seções como "Diferença entre SSD e HDD para estudo", "Recursos essenciais (webcam, microfone, portas USB)", "Software para estudantes", "Duração da bateria ideal para faculdade".

*   **Passo 4: Criação de um Briefing de Otimização de Conteúdo**:
    *   Documente as novas palavras-chave, subtópicos, perguntas PAA e áreas de aprofundamento a serem incorporadas no conteúdo existente.
    *   **Exemplo**:
        *   Adicionar seção: "Armazenamento: SSD vs. HDD para estudantes – Qual é melhor?"
        *   Expandir seção: "Duração da Bateria: Por que é crucial para estudos fora de casa"
        *   Incluir FAQ: "Qual o tamanho de tela ideal para um notebook de estudante?"
        *   Incorporar LSI: "notebook universitário", "laptop para ensino superior", "melhores notebooks para EAD".

*   **Passo 5: Implementação, Publicação e Monitoramento Contínuo**:
    *   Atualize o conteúdo da página, incorporando as novas informações de forma natural e útil para o leitor.
    *   Garanta que os novos termos e subtópicos sejam usados em headings (H2, H3), parágrafos e, se aplicável, na meta descrição.
    *   Monitore o desempenho da página no GSC para as novas palavras-chave, observando mudanças na posição média e no CTR. Use o "Comparar" no GSC para ver o antes e depois da otimização.

---

## Templates

### Matriz de Priorização de Palavras-Chave

```
| Palavra-Chave                          | Volume Busca (mensal) | Dificuldade KD (SEMrush/Ahrefs) | CPC Médio (R$) | Intenção de Busca | Tipo de Conteúdo Sugerido   | Prioridade (1-5) | Status      | Responsável  |
|----------------------------------------|-----------------------|---------------------------------|----------------|-------------------|-----------------------------|------------------|-------------|--------------|
| melhor cafeteira expresso              | 8.100                 | 58                              | 3,50           | Transacional      | Review/Comparativo de produto | 4                | Em Análise  | João Silva   |
| como limpar cafeteira Nespresso        | 1.900                 | 22                              | 0,80           | Informacional     | Guia Passo a Passo          | 5                | Agendado    | Maria Souza  |
| café moído na hora benefícios          | 720                   | 15                              | 0,50           | Informacional     | Artigo de Blog              | 3                | Concluído   | João Silva   |
| cafeteira expresso barata              | 4.400                 | 41                              | 2,10           | Comercial         | Lista de Produtos           | 4                | Em Produção | Pedro Alves  |
| diferença cafeteira italiana e francesa| 390                   | 8                               | 0,35           | Informacional     | FAQ/Explicação Detalhada    | 2                | Backlog     | Maria Souza  |
| comprar cafeteira automática           | 12.100                | 65                              | 4,10           | Transacional      | Página de Categoria         | 3                | Em Análise  | Pedro Alves  |
```

### Plano de Conteúdo por Cluster de Tópicos

```
| Tópico Principal (Pillar Content)        | Palavra-Chave Principal           | Conteúdo Principal Sugerido                                    | Palavras-Chave Secundárias/LSI                                            | URLs de Referência (Concorrentes)                                      | Status       |
|------------------------------------------|-----------------------------------|----------------------------------------------------------------|---------------------------------------------------------------------------|------------------------------------------------------------------------|--------------|
| **Guia Completo de Cafeteiras Expresso** | cafeteira expresso                | Artigo abrangente sobre tipos, funcionamento, como escolher.   | máquina expresso, café expresso caseiro, melhor marca cafeteira          | blogdocafe.com.br/melhor-cafeteira-expresso                            | Em Produção  |
|                                          |                                   |                                                                |                                                                           |                                                                        |              |
| **Subtópico 1: Melhores Modelos**        | melhor cafeteira expresso         | Review detalhado dos top 5 modelos com prós e contras.         | cafeteira expresso barata, cafeteira automática, preço cafeteira         | tecmundo.com.br/review-cafeteira-expresso                              | Agendado     |
|                                          |                                   |                                                                |                                                                           | zoom.com.br/cafeteira-expresso-barata                                  |              |
| **Subtópico 2: Manutenção e Limpeza**    | como limpar cafeteira Nespresso   | Guia passo a passo para limpeza e descalcificação.             | descalcificar cafeteira, problemas cafeteira, manutenção máquina café    | nespresso.com/br/pt/manutencao-maquina                                 | Concluído    |
|                                          |                                   |                                                                |                                                                           | forumdocafe.com.br/problemas-cafeteira                                 |              |
| **Subtópico 3: Tipos de Café**           | café moído na hora benefícios     | Artigo sobre moagem, frescor e impacto no sabor.               | diferença café torrado e moído, tipos de moagem, grãos de café           | cafejardim.com.br/beneficios-cafe-fresco                               | Em Revisão   |
|                                          |                                   |                                                                |                                                                           | blogdopadeiro.com.br/torrado-vs-moido                                  |              |
```

---

## Checklist

- [ ] Realizar análise de intenção de busca (informacional, navegacional, comercial, transacional) para cada palavra-chave priorizada.
- [ ] Mapear palavras-chave de cauda longa e semanticamente relacionadas para cada cluster de tópico principal.
- [ ] Verificar a Dificuldade de Palavra-Chave (KD) em ferramentas como SEMrush ou Ahrefs para filtrar oportunidades realistas de ranqueamento.
- [ ] Analisar as SERPs dos top 5 concorrentes para a palavra-chave principal para identificar lacunas de conteúdo e formatos de sucesso (ex: listas, guias, vídeos).
- [ ] Incorporar palavras-chave LSI (Latent Semantic Indexing) e termos semanticamente relacionados naturalmente no corpo do conteúdo.
- [ ] Otimizar títulos (H1, H2, H3) e meta descrições com a palavra-chave principal e termos adjacentes para melhorar CTR.
- [ ] Incluir perguntas da seção "People Also Ask" (PAA) do Google como subtítulos ou itens de FAQ no conteúdo.
- [ ] Monitorar o ranqueamento das palavras-chave priorizadas e o tráfego orgânico no Google Search Console e Google Analytics 4.
- [ ] Avaliar o Click-Through Rate (CTR) das páginas otimizadas para identificar oportunidades de melhoria em títulos e meta descrições.
- [ ] Revisar a canibalização de palavras-chave para evitar que múltiplas URLs do mesmo site compitam entre si pelo mesmo termo.
- [ ] Documentar o progresso da pesquisa e implementação das palavras-chave em uma matriz de planejamento.
- [ ] Identificar oportunidades de palavras-chave sazonais ou de tendência usando o Google Trends para planejar conteúdo futuro.

---

## Métricas de Referência

| Métrica                                | Benchmark (Média)        | Meta (Exemplo)           | Observações                                            |
|----------------------------------------|--------------------------|--------------------------|--------------------------------------------------------|
| Posição Média (GSC)                    | Top 20                   | Top 5                    | Para palavras-chave alvo após 3-6 meses de otimização. |
| CTR Orgânico (Top 10)                  | 3-5%                     | 8-12%                    | Para posições 1-3, espera-se CTR > 15%.               |
| Volume de Busca (para palavras-chave alvo)| > 100/mês (cauda longa)  | > 500/mês (posts médios) | Reflete o potencial de tráfego.                       |
| Keyword Difficulty (KD)                | < 60 (SEMrush/Ahrefs)    | < 40 (para novos posts)  | Indicador da dificuldade para ranquear.                |
| Tráfego Orgânico (Crescimento Anual)   | Crescimento de 10%       | Crescimento de 25%       | Avalia a performance geral da estratégia de SEO.       |
| % de Palavras-chave Ranqueadas (Top 10)| 15% (do total monitorado)| 30%                      | Mostra a eficácia da pesquisa em capturar visibilidade. |

---

## Erros Comuns

1.  **Focar exclusivamente em palavras-chave de alto volume e alta concorrência**: Priorizar apenas termos como "marketing digital" (Volume: 1M, KD: 90) sem uma base sólida de autoridade de domínio resulta em pouco ou nenhum ranqueamento.
    *   **Como evitar**: Combine palavras-chave de alto volume com termos de cauda longa e menor KD (ex: "estratégias de marketing digital para pequenas empresas" - Volume: 10K, KD: 45) para construir autoridade gradualmente e capturar tráfego mais qual