---
name: micro-budget-ads
description: "Micro Budget Ads — Skill especializada para planejar, executar e otimizar campanhas de anúncios com orçamentos reduzidos em Meta Ads, Google Ads e TikTok Ads."
license: MIT
metadata:
  version: 1.0.0
  author: Cafe Code AI
  category: 04-anuncios-trafego
  updated: 2026-03-01
risk: safe
---

# Micro Budget Ads

Essa skill capacita o Claude Code a planejar, executar e otimizar campanhas de anúncios pagas com orçamentos reduzidos (micro budget) em plataformas como Meta Ads, Google Ads e TikTok Ads, maximizando o ROI para pequenas empresas e startups.

---

## Keywords

Meta Ads Orçamento Pequeno, Google Ads Local Barato, TikTok Ads Iniciante, Campanha Digital Barata, ROI Pequenos Negócios, Otimização Diária Ads, Criativos Baixo Custo, Tráfego Orgânico Otimizado, CPC Reduzido, Segmentação Nicho Ads, Anúncios Performance Pequeno Orçamento, Teste A/B Economico.

---

## Quick Start

1.  **Selecione uma plataforma e objetivo**: Inicie com Meta Ads (Facebook/Instagram) com objetivo de `Tráfego` ou `Engajamento` para testar rapidamente a receptividade da sua oferta.
2.  **Defina um orçamento diário realista**: Configure um orçamento diário entre R$20 e R$50. Não pulverize este valor em múltiplas campanhas.
3.  **Crie 2-3 criativos simples e diretos**: Utilize imagens ou vídeos curtos com uma proposta de valor clara e um Call To Action (CTA) explícito como "Saiba Mais" ou "Compre Agora".
4.  **Monitore as métricas chave diariamente**: Verifique o CTR (Taxa de Cliques) e o CPC (Custo Por Clique) para identificar rapidamente criativos e segmentações de público que não estão performando bem.
5.  **Pause rapidamente o que não funciona**: Se um criativo ou conjunto de anúncios apresentar CTR abaixo de 0.8% no Meta Ads ou CPC significativamente acima da média após 24-48 horas, pause-o imediatamente para evitar desperdício de orçamento.

---

## Core Workflows

### Workflow 1: Lançamento de Produto Digital com R$30/dia no Meta Ads

Este workflow foca em validar um produto digital ou serviço online para um público específico com um orçamento muito limitado, priorizando cliques e engajamento.

1.  **Configuração da Campanha**:
    *   **Objetivo**: `Tráfego` (para uma landing page de pré-lançamento/lista de espera) ou `Engajamento` (para posts de lançamento no Instagram/Facebook que direcionam para um link na bio ou direct). O objetivo de tráfego é ideal para micro budgets para coletar dados de cliques e custo por clique.
    *   **Orçamento**: R$30/dia, configurado no nível da campanha (CBO - Campaign Budget Optimization).
    *   **Período**: Rodar por 5-7 dias para coletar dados iniciais.
2.  **Criação dos Conjuntos de Anúncios (Audiências)**:
    *   Crie 2-3 conjuntos de anúncios, cada um com uma segmentação de público distinta para testar qual responde melhor ao seu produto.
        *   **Conjunto A (Interesses Amplos)**: Interesses como "Empreendedorismo Digital", "Marketing de Afiliados", "Desenvolvimento Pessoal". Limite o público para evitar ser excessivamente amplo (ex: Brasil, 25-55 anos, interesses).
        *   **Conjunto B (Interesses Nichados)**: Interesses mais específicos relacionados ao seu produto. Ex: "Cursos Online", "Hotmart", "Eduzz", "Pequenas Empresas e Empreendedores".
        *   **Conjunto C (Lookalike - Opcional)**: Se você tiver uma lista de e-mails de clientes ou leads (mínimo de 1000), crie um Lookalike de 1% para testar. Se não, use outro conjunto de interesses.
3.  **Desenvolvimento de Criativos**:
    *   Crie 3-4 variações de anúncios (dentro de cada conjunto, o Meta Ads pode otimizar).
        *   **Formato**: 1 vídeo curto (15-30 segundos, estilo UGC - User Generated Content) e 2-3 imagens estáticas com texto sobreposto.
        *   **Conteúdo**: Foco em resolver uma dor específica do público-alvo ou destacar um benefício único do seu produto. Ex: "Cansado de vender pouco online? Aprenda a escalar com R$30/dia."
        *   **Call to Action (CTA)**: "Saiba Mais" ou "Inscreva-se Agora" são eficazes para micro budgets.
4.  **Otimização Diária (Primeiros 3 Dias)**:
    *   **Monitoramento**: Verifique o CPC e o CTR de cada criativo e conjunto de anúncios no Gerenciador de Anúncios.
    *   **Ação Rápida**: Pause criativos com CTR abaixo de 0.8% ou CPC 2x-3x maior que a média dos outros. Se um conjunto de anúncios não performar, pause-o e redistribua o orçamento para os que estão funcionando, ou teste uma nova segmentação.
    *   **Frequência**: Mantenha a frequência abaixo de 2.5. Se estiver subindo rapidamente, o público pode ser muito pequeno para o orçamento e criativos podem queimar rápido.
5.  **Ajustes Contínuos (Após 3 Dias)**:
    *   **Análise de Dados**: Avalie quais públicos e criativos geraram os cliques mais baratos e qualificados (se houver conversão, qual gerou mais conversões dentro do custo).
    *   **Refinamento**: Pause os públicos e criativos de pior desempenho. Se houver um que se destaca, duplique-o e teste uma pequena variação (ex: outro CTA, pequena mudança no texto principal).

### Workflow 2: Geração de Leads Locais no Google Ads com R$20/dia

Este workflow visa captar leads qualificados (chamadas ou formulários) para um negócio local com um orçamento apertado, focando em intenção de busca explícita.

1.  **Configuração da Campanha**:
    *   **Objetivo**: `Leads` (para formulário no site) ou `Chamadas Telefônicas` (usando uma extensão de chamada principal).
    *   **Orçamento**: R$20/dia, configurado no nível da campanha.
    *   **Tipo de Campanha**: Rede de Pesquisa (Search Network) exclusivamente. Desative a Rede de Display e parceiros de pesquisa no início para focar o orçamento.
    *   **Localização**: Segmentar especificamente a cidade, bairro ou um raio de poucos quilômetros do seu negócio. Ex: "São Paulo - Centro", "Campinas - Raio de 5km".
2.  **Pesquisa e Seleção de Palavras-Chave**:
    *   Foque em palavras-chave de cauda longa (long-tail) e com alta intenção, usando correspondência exata `[palavra-chave]` e de frase `"palavra-chave"`.
    *   **Exemplos**: `[eletricista residencial Campinas]`, `"encanador 24h Curitiba"`, `[reparo de telhado zona sul SP]`, `"clínica odontológica infantil Salvador"`.
    *   **Palavras-chave Negativas**: Crie uma lista robusta de palavras-chave negativas desde o início para evitar cliques irrelevantes. Ex: "grátis", "vagas", "curso", "download", "preço".
3.  **Criação dos Grupos de Anúncios**:
    *   Organize suas palavras-chave em grupos de anúncios temáticos (2-3 grupos, no máximo, para micro budgets). Cada grupo deve ter palavras-chave muito relacionadas.
        *   Ex: Grupo "Eletricista Residencial" com `[eletricista residencial Campinas]`, `"eletricista urgente Campinas"`.
        *   Ex: Grupo "Manutenção Elétrica" com `[manutenção elétrica predial Campinas]`, `"serviço elétrico Campinas"`.
4.  **Desenvolvimento de Anúncios de Texto Responsivos (RSA)**:
    *   Crie 2-3 RSAs por grupo de anúncios.
    *   **Headlines**: Inclua a palavra-chave principal, a localização e um benefício. Ex: "Eletricista Campinas Urgente", "Reparo Elétrico Rápido SP", "Orçamento Grátis - Zona Sul".
    *   **Descrições**: Complemente com mais detalhes e um forte CTA. Ex: "Profissionais qualificados para sua residência ou empresa. Atendimento 24h. Ligue Agora!"
    *   **Extensões de Anúncio**: Configure o máximo possível para aumentar a visibilidade e o espaço do anúncio:
        *   **Extensão de Chamada**: Número de telefone direto.
        *   **Extensão de Local**: Endereço do seu negócio.
        *   **Extensão de Snippet Estruturado**: Destaque serviços (ex: "Serviços: Instalações, Reparos, Manutenção").
        *   **Extensão de Frase de Destaque**: Benefícios (ex: "Atendimento Rápido", "Profissionais Certificados").
5.  **Otimização Semanal**:
    *   **Termos de Pesquisa**: Analise o relatório de termos de pesquisa. Adicione novas palavras-chave negativas e ajuste lances para as que geram tráfego irrelevante.
    *   **Lances**: Comece com lances automáticos (maximizar cliques) e, após algumas conversões, mude para maximizar conversões. Se quiser mais controle, use lances manuais para palavras-chave de alta performance.
    *   **Performance dos Anúncios**: Pause anúncios com CTR muito baixo e crie novas variações com headlines e descrições de melhor desempenho.
    *   **Horários de Exibição (Dayparting)**: Se seu negócio tem horários de pico, ajuste os lances ou a exibição dos anúncios para esses períodos para maximizar o ROI do pequeno orçamento.

---

## Templates

### Meta Ads - Anúncio de Imagem Única (Exemplo Produto Digital)

```
Headline: Desvende o Segredo dos Micro Empreendedores!
Primary Text: Cansado de orçamentos altos e resultados baixos? Nosso [Nome do Produto/Serviço] te ensina o passo a passo para escalar seu negócio online com apenas R$30/dia. Chega de achismo, clique e veja como é possível ter resultados reais com investimento mínimo!
Description: Resultados Reais, Investimento Mínimo.
Call to Action: Saiba Mais
URL: https://seusite.com/oferta-micro-budget
Image: [Link para imagem de pessoa comum celebrando um pequeno sucesso, ou um gráfico simples de crescimento]
```

### Google Ads - Lista de Palavras-Chave (Serviço Local)

```
// Grupo de Anúncios: Eletricista Residencial
[eletricista residencial São Paulo]
"eletricista 24h SP"
[instalação elétrica apartamento SP]
"manutenção elétrica zona sul"
[eletricista de emergência SP]

// Palavras-chave Negativas Essenciais
-gratis
-vagas
-curso
-assistir
-como fazer
-barato (se você não for o mais barato)
```

---

## Checklist

- [x] Objetivo da campanha alinhado com a fase do negócio (ex: Tráfego para validação, Leads para vendas).
- [x] Orçamento diário definido entre R$15-R$50 e concentrado em 1-2 campanhas no máximo.
- [x] Configuração correta do Pixel do Meta ou Tag de Conversão do Google Ads.
- [x] Público-alvo segmentado com no máximo 3-5 interesses/comportamentos no Meta Ads, ou keywords exatas/de frase no Google Ads.
- [x] Mínimo de 3 criativos (imagem/vídeo) diferentes e de alta qualidade (UGC ou profissional) por campanha/conjunto no Meta Ads.
- [x] Verificação diária do CPC, CTR e Frequência dos anúncios/conjuntos de anúncios.
- [x] Pausar criativos/conjuntos com CTR < 0.8% no Meta Ads ou CPC > 3x a média após 48h.
- [x] Adicionar 5-10 palavras-chave negativas semanalmente no Google Ads, baseado nos termos de pesquisa.
- [x] Frequência de exibição do anúncio abaixo de 2.5 no Meta Ads para evitar saturação do público.
- [x] Todas as extensões de anúncio relevantes (chamada, local, snippet) configuradas no Google Ads.
- [x] Testar no mínimo 2 CTAs (Call to Actions) diferentes por conjunto/grupo de anúncios.
- [x] Landing Page otimizada para mobile e com carregamento rápido.

---

## Métricas de Referência

| Métrica               | Benchmark (Micro Budget) | Meta (Otimizado)         |
| :-------------------- | :----------------------- | :----------------------- |
| CTR (Meta Ads)        | 0.8% - 1.5%              | > 1.8%                   |
| CTR (Google Search)   | 2.5% - 4.5%              | > 3.5%                   |
| CPC (Meta Ads)        | R$0.80 - R$2.80          | < R$1.80                 |
| CPC (Google Search)   | R$2.00 - R$9.00          | < R$6.00                 |
| CPM (Meta Ads)        | R$18.00 - R$40.00        | < R$30.00                |
| ROAS (e-commerce)     | 1.0x - 2.5x              | > 2.0x (desafio p/ micro) |
| Custo por Lead (CPL)  | R$8.00 - R$30.00         | < R$15.00                |

---

## Erros Comuns

1.  **Orçamento pulverizado**: Tentar anunciar em múltiplas plataformas (Meta, Google, TikTok) e com vários objetivos com apenas R$30/dia.
    *   **Como evitar**: Concentre seu orçamento em *uma* plataforma e *um* objetivo principal por vez. Ex: R$30/dia para tráfego no Meta Ads ou R$20/dia para leads no Google Ads.
2.  **Público-alvo muito amplo ou genérico**: Mirar em "todos no Brasil" ou "pessoas interessadas em negócios" com um orçamento limitado.
    *   **Como evitar**: Segmente por interesses muito específicos, localização exata (raio de 5km), ou utilize públicos lookalike de 1% se tiver uma lista de base. No Google Ads, use palavras-chave de cauda longa e correspondência exata.
3.  **Criativos genéricos e sem CTA claro**: Usar imagens de banco de imagens sem personalidade ou vídeos longos sem um Call To Action direto.
    *   **Como evitar**: Invista em criativos autênticos (UGC, fotos reais de produtos/serviços), com textos persuasivos e um CTA explícito e visível ("Saiba Mais", "Ligue Agora"). Teste variações.
4.  **Falta de monitoramento e otimização diária/semanal**: Deixar a campanha rodar por dias sem verificar as métricas de performance.
    *   **Como evitar**: Crie o hábito de verificar as métricas (CTR, CPC, Frequência) pelo menos 3 vezes por semana. Pause imediatamente o que não performa e duplique/escale o que está dando certo (mesmo que em micro escala).
5.  **Ausência de palavras-chave negativas (Google Ads)**: Deixar de adicionar termos irrelevantes, fazendo o orçamento ser gasto em cliques sem intenção de compra.
    *   **Como evitar**: Faça uma pesquisa inicial de negativas e revise o relatório de termos de pesquisa semanalmente para adicionar novos termos negativos. Ex: `[advogado trabalhista Campinas]` - adicione "-vagas", "-curso", "-gratis".

---

## Dicas Avançadas

1.  **Estratégia de CBO (Campaign Budget Optimization) no Meta Ads para Micro Orçamentos**: Mesmo com R$30/dia, utilize CBO. Crie 2-3 conjuntos de anúncios com segmentações distintas (ex: um lookalike, um de interesses específicos, um de retargeting de engajamento). O algoritmo do Meta distribuirá o orçamento entre eles, maximizando a performance onde houver mais potencial, sem que você precise ajustar manualmente.
2.  **Teste A/B Focado em Headlines e CTAs**: Em vez de testar audiências amplas (que demandam mais budget), com micro orçamentos, foque em testar variações de headlines e CTAs dentro dos mesmos criativos e públicos. Crie dois anúncios quase idênticos, mudando apenas a headline ou o CTA (ex: "Saiba Mais" vs. "Garanta o Seu"). Uma pequena melhoria no CTR pode significar um ganho significativo de cliques para seu orçamento.
3.  **Uso de Lances Manuais (CPC Otimizado) no Google Ads para nichos**: Para palavras-chave de alta conversão, mas de baixo volume de busca, considere configurar lances manuais ligeiramente acima do recomendado. Isso garante que seu anúncio apareça para buscas muito específicas, mesmo com orçamento reduzido, controlando o gasto por clique. Ex: Para `[manutenção de aquecedor a gás zona norte]`, um lance manual de R$12 pode garantir visibilidade para um lead valioso.
4.  **Remarketing Simples com Pequenos Orçamentos no Meta Ads**: Crie uma audiência personalizada de pessoas que interagiram com seu perfil ou posts nos últimos 7 ou 14 dias. Dedique um micro orçamento (ex: R$5-R$10/dia) exclusivamente para essa audiência. São pessoas que já demonstraram algum interesse e tendem a ter um CPC menor e maior taxa de conversão, otimizando o gasto.
5.  **Aproveitar o "Dayparting" e "Ad Scheduling" no Google Ads**: Para negócios locais ou serviços com horários de pico, configure seus anúncios para aparecerem apenas nos horários e dias da semana em que seu cliente-alvo está mais propenso a pesquisar e converter. Ex: Um restaurante delivery pode exibir anúncios apenas das 11h-14h e 18h-22h, otimizando seu R$20/dia para os momentos de maior demanda.