---
name: lookalike-audiences
description: "Lookalike Audiences — Skill especializada para lookalike audiences"
license: MIT
metadata:
  version: 1.0.0
  author: Cafe Code AI
  category: 04-anuncios-trafego
  updated: 2026-03-01
risk: safe
---

# Lookalike Audiences

Essa skill capacita o Claude a criar, otimizar e analisar Lookalike Audiences em Meta Ads, Google Ads e TikTok Ads para impulsionar a performance de campanhas.

---

## Keywords

Lookalike Audience, Públicos Semelhantes, Audiências Semelhantes, Expansão de Público, LLA, Audiências Personalizadas, Seed Audience, Otimização de Alcance, Meta Ads Lookalike, Google Ads Similar Audiences, TikTok Lookalike, Escalada de Audiência, Retorno sobre Investimento.

---

## Quick Start

1.  **Crie Audiência Personalizada de Origem**: No Meta Ads, crie uma "Audiência Personalizada" de "Clientes (lista)" ou "Tráfego do Site (compradores dos últimos 60 dias)". No Google Ads, crie uma "Audiência de Remarketing" de "Compradores" no GA4. No TikTok Ads, use uma "Audiência Personalizada" de "Engajamento (interação com vídeos)".
2.  **Gere a Lookalike**: A partir da audiência personalizada de origem, crie a Lookalike. Defina o percentual (1% para Meta/TikTok, Google gera automaticamente) e a localização (ex: Brasil).
3.  **Configure Conjunto de Anúncios**: Crie um novo conjunto de anúncios com a Lookalike Audience, selecionando um objetivo de campanha alinhado (ex: "Vendas" para Lookalike de compradores). Exclua a audiência de origem para evitar sobreposição.
4.  **Monitore e Otimize**: Lance a campanha e acompanhe métricas como ROAS, CPA e CTR. Se a Lookalike performar bem, considere aumentar o orçamento ou testar percentuais maiores.

---

## Core Workflows

### Workflow 1: Criação e Teste de Lookalike para Meta Ads (Facebook/Instagram)

Este workflow detalha a criação, configuração e teste de Lookalike Audiences no Gerenciador de Anúncios da Meta, focando em performance de vendas.

**Passo 1: Seleção e Criação da Audiência de Origem (Seed Audience)**
*   **Ação**: Acesse o "Gerenciador de Eventos" e o "Públicos" no Meta Business Suite.
*   **Exemplo Concreto**:
    *   **Origem de Dados**: Pixel do Facebook (ou API de Conversões).
    *   **Tipo de Audiência Personalizada**: "Tráfego do Site" ou "Lista de Clientes".
    *   **Critério de Tráfego do Site**: "Pessoas que concluíram a compra" (evento `Purchase`).
    *   **Refinamento**: "Valor Total Gasto" >= R$150, "Período de Retenção" = 60 dias.
    *   **Nome da Audiência**: "Compradores_AltoValor_60D". Garanta que esta audiência tenha no mínimo 1.000 usuários ativos.

**Passo 2: Configuração da Lookalike Audience**
*   **Ação**: No "Públicos", clique em "Criar Público" e selecione "Público Semelhante".
*   **Exemplo Concreto**:
    *   **Origem do Público**: Selecione a audiência personalizada "Compradores_AltoValor_60D".
    *   **Localização do Público**: Brasil.
    *   **Tamanho do Público**: Crie três públicos separados para teste:
        *   "Público Semelhante 1% de Compradores_AltoValor_60D"
        *   "Público Semelhante 2% de Compradores_AltoValor_60D"
        *   "Público Semelhante 1-3% de Compradores_AltoValor_60D" (para testar um range)

**Passo 3: Estrutura da Campanha de Teste com LLAs**
*   **Ação**: Crie uma nova campanha no Gerenciador de Anúncios.
*   **Exemplo Concreto**:
    *   **Objetivo da Campanha**: "Vendas".
    *   **Otimização de Orçamento da Campanha (CBO)**: Ativado, com orçamento diário de R$ 300.
    *   **Conjunto de Anúncios 1**:
        *   **Nome**: "LLA_1pct_Compradores_HV"
        *   **Público**: Incluir "Público Semelhante 1% de Compradores_AltoValor_60D".
        *   **Exclusão**: Excluir a audiência personalizada "Compradores_AltoValor_60D" para evitar sobreposição.
        *   **Idade/Gênero**: 25-55 anos, Todos os gêneros.
        *   **Posicionamentos**: Advantage+ Placements.
        *   **Otimização para**: Conversões (Compra).
    *   **Conjunto de Anúncios 2**:
        *   **Nome**: "LLA_2pct_Compradores_HV"
        *   **Público**: Incluir "Público Semelhante 2% de Compradores_AltoValor_60D".
        *   **Exclusão**: Excluir "Compradores_AltoValor_60D".
        *   **Demográficos/Posicionamentos/Otimização**: Mesmos do Conjunto 1.
    *   **Conjunto de Anúncios 3**:
        *   **Nome**: "LLA_1-3pct_Compradores_HV"
        *   **Público**: Incluir "Público Semelhante 1-3% de Compradores_AltoValor_60D".
        *   **Exclusão**: Excluir "Compradores_AltoValor_60D".
        *   **Demográficos/Posicionamentos/Otimização**: Mesmos do Conjunto 1.
    *   **Anúncios**: Utilize 2-3 criativos de alta performance em cada conjunto de anúncios.

**Passo 4: Análise e Otimização**
*   **Ação**: Monitore o desempenho no painel de relatórios da Meta Ads.
*   **Exemplo Concreto**: Após 7-10 dias de veiculação:
    *   Compare o ROAS (Retorno sobre Investimento em Anúncios) e CPA (Custo por Aquisição) de cada conjunto de anúncios.
    *   Se "LLA_1pct_Compradores_HV" apresentar ROAS de 4.5 e CPA de R$25, enquanto "LLA_2pct_Compradores_HV" tem ROAS de 3.0 e CPA de R$40, e "LLA_1-3pct_Compradores_HV" tem ROAS de 3.8 e CPA de R$30:
        *   **Escalar**: Aumente o orçamento alocado para "LLA_1pct_Compradores_HV" (o CBO fará isso automaticamente se for o melhor, mas você pode mover para uma nova campanha com orçamento dedicado).
        *   **Testar**: Crie uma nova LLA de 1% a partir de uma audiência personalizada de "Compradores que adicionaram ao carrinho mas não compraram nos últimos 30 dias" para expandir os testes.
        *   **Otimizar Criativo**: Se um conjunto de anúncios tiver bom CPA mas CTR baixo, teste novos criativos para melhorar a relevância.

### Workflow 2: Otimização de Lookalike para Google Ads (Audiências Semelhantes) e TikTok Ads

Este workflow aborda a utilização de Audiências Semelhantes no Google Ads e a criação de Lookalikes no TikTok Ads, com foco em diferentes objetivos.

**Passo 1: Configuração da Audiência de Origem para Google Ads (Remarketing GA4)**
*   **Ação**: Conecte sua conta do Google Analytics 4 (GA4) ao Google Ads e configure a coleta de dados.
*   **Exemplo Concreto**:
    *   No GA4, vá em "Administrador" > "Configurações de Dados" > "Coleta de Dados" e ative "Sinais do Google".
    *   Crie uma audiência no GA4:
        *   **Nome**: "Compradores_GA4_30D"
        *   **Eventos**: `purchase`
        *   **Período de Retenção**: 30 dias.
    *   Certifique-se de que esta audiência seja exportada para o Google Ads. O Google Ads automaticamente gerará uma "Audiência Semelhante a Compradores_GA4_30D" quando a audiência de origem tiver mais de 1.000 usuários ativos.

**Passo 2: Aplicação de Audiências Semelhantes no Google Ads**
*   **Ação**: Utilize a Audiência Semelhante em campanhas de Display, Discovery, Vídeo ou Pesquisa.
*   **Exemplo Concreto**:
    *   **Campanha de Display/Discovery/Vídeo**:
        *   **Tipo de Segmentação**: "Segmentação".
        *   **Audiência**: Adicione "Audiência Semelhante a Compradores_GA4_30D".
        *   **Objetivo**: Direcionar tráfego qualificado para páginas de produto ou ofertas.
    *   **Campanha de Pesquisa (RSLA - Remarketing Lists for Search Ads)**:
        *   **Tipo de Segmentação**: "Observação".
        *   **Audiência**: Adicione "Audiência Semelhante a Compradores_GA4_30D".
        *   **Ajuste de Lance**: Defina um ajuste de lance positivo (ex: +20%) para usuários que se enquadram nesta audiência, aumentando a chance de seus anúncios aparecerem para eles.

**Passo 3: Criação de Lookalike para TikTok Ads (Engajamento)**
*   **Ação**: No TikTok Ads Manager, vá em "Ativos" > "Audiências" e crie uma "Audiência Personalizada" de origem.
*   **Exemplo Concreto**:
    *   **Tipo de Audiência Personalizada**: "Engajamento".
    *   **Critério**: "Pessoas que assistiram a 75% ou mais de qualquer vídeo" nos últimos 90 dias.
    *   **Nome da Audiência**: "Engajamento_Video_75pct_90D".
    *   **Criação da Lookalike**: A partir desta audiência, clique em "Criar Público Semelhante".
    *   **Similaridade**: Escolha "Baixa (1%)" para maior precisão, ou "Média (1-5%)" para equilibrar alcance e similaridade.
    *   **Localização**: Brasil.

**Passo 4: Estrutura da Campanha TikTok Ads com LLA de Engajamento**
*   **Ação**: Crie uma nova campanha no TikTok Ads Manager.
*   **Exemplo Concreto**:
    *   **Objetivo da Campanha**: "Geração de Leads" ou "Conversões" (para um produto de baixo ticket).
    *   **Configuração do Conjunto de Anúncios**:
        *   **Público**: Inclua a "Público Semelhante de Engajamento_Video_75pct_90D (1%)".
        *   **Exclusão**: Exclua a audiência personalizada "Engajamento_Video_75pct_90D".
        *   **Demográficos**: Idade 18-34, Gênero Todos.
        *   **Interesses**: Adicione interesses relevantes como "Comércio Eletrônico", "Moda e Acessórios" (se aplicável) para refinar, especialmente para LLAs de 3%+.
        *   **Otimização para**: Geração de Leads ou Conclusão de Compra.
    *   **Anúncios**: Use vídeos curtos e dinâmicos, nativos do TikTok, com CTAs claros e diretos.

**Passo 5: Monitoramento e Otimização Contínua**
*   **Ação**: Analise o desempenho das Audiências Semelhantes no Google Ads e das Lookalikes no TikTok Ads.
*   **Exemplo Concreto**:
    *   **Google Ads**: Se a "Audiência Semelhante a Compradores_GA4_30D" em campanha de pesquisa está gerando conversões 30% mais baratas que o público genérico, aumente o ajuste de lance para +30% ou crie um conjunto de anúncios separado com lances mais agressivos focado exclusivamente nela.
    *   **TikTok Ads**: Se a LLA de engajamento está trazendo leads a um custo aceitável, teste uma LLA de 1-5% para aumentar o volume, ou crie uma LLA de "Compradores (Evento de Otimização de Compra)" para um objetivo de vendas diretas.

---

## Templates

### Template de Estrutura de Campanha Meta Ads com LLAs

```
Campanha: Vendas - LLA Principal
Objetivo: Vendas
Estratégia de Lance: Custo Mais Baixo
Otimização: CBO (Otimização de Orçamento da Campanha)
Orçamento Diário: R$ 600,00

Conjunto de Anúncios 1: LLA 1% Compradores (LTV Alto - 90 dias)
  Público: Lookalike 1% de "Audiência Personalizada - Compradores LTV Alto - 90D"
  Exclusões: "Audiência Personalizada - Compradores LTV Alto - 90D"
  Localização: Brasil
  Idade: 25-55
  Gênero: Todos
  Idiomas: Português (Brasil)
  Posicionamentos: Advantage+ Placements
  Otimização para: Conversões (Compra)
  Janela de Conversão: 7 dias após o clique ou 1 dia após a visualização

Conjunto de Anúncios 2: LLA 2% Visitantes (Páginas de Produto - 30 dias)
  Público: Lookalike 2% de "Audiência Personalizada - Visitantes PagProd - 30D"
  Exclusões: "Audiência Personalizada - Visitantes PagProd - 30D"
  Localização: Brasil
  Idade: 25-55
  Gênero: Todos
  Idiomas: Português (Brasil)
  Posicionamentos: Advantage+ Placements
  Otimização para: Conversões (Compra)
  Janela de Conversão: 7 dias após o clique ou 1 dia após a visualização

Conjunto de Anúncios 3: LLA 1-3% Engajamento Instagram (180 dias)
  Público: Lookalike 1-3% de "Audiência Personalizada - Engajamento IG - 180D"
  Exclusões: "Audiência Personalizada - Engajamento IG - 180D"
  Localização: Brasil
  Idade: 25-55
  Gênero: Todos
  Idiomas: Português (Brasil)
  Posicionamentos: Advantage+ Placements
  Otimização para: Conversões (Compra)
  Janela de Conversão: 7 dias após o clique ou 1 dia após a visualização
```

### Template de Análise de Desempenho de LLA

```
Relatório de Desempenho - Lookalike Audiences (Meta Ads)

Período: 01/04/2024 - 30/04/2024
Campanha: Vendas - LLA Principal
Objetivo da Campanha: ROAS > 3.5x, CPA < R$30,00

| Conjunto de Anúncios                  | Gastos (R$) | Impressões   | Cliques (CTR) | Conversões (CPA) | Valor Conversão (ROAS) |
|---------------------------------------|-------------|--------------|---------------|------------------|------------------------|
| LLA 1% Compradores LTV Alto           | 2.800,00    | 220.000      | 5.060 (2,30%) | 98 (R$ 28,57)    | 14.700,00 (5,25)       |
| LLA 2% Visitantes PagProd             | 1.800,00    | 160.000      | 2.560 (1,60%) | 38 (R$ 47,37)    | 6.460,00 (3,59)        |
| LLA 1-3% Engajamento Instagram        | 1.400,00    | 110.000      | 1.540 (1,40%) | 22 (R$ 63,64)    | 3.300,00 (2,36)        |
| Controle: Público Aberto (Interesses) | 1.200,00    | 150.000      | 1.800 (1,20%) | 15 (R$ 80,00)    | 1.800,00 (1,50)        |

Recomendação:
- Escalada Imediata: Aumentar o orçamento do "LLA 1% Compradores LTV Alto" em 50% devido ao excelente ROAS e CPA.
- Otimização Criativa: Para "LLA 2% Visitantes PagProd", testar novos criativos com foco em benefícios do produto para tentar elevar o CTR e a taxa de conversão, buscando um CPA abaixo de R$40.
- Pausar/Reavaliar: "LLA 1-3% Engajamento Instagram" e "Controle: Público Aberto" estão com ROAS e CPA fora da meta. Pausar o "Controle" e reavaliar a LLA de Engajamento, talvez criando uma nova LLA de "visualizadores de vídeo de 95%".
```

---

## Checklist

- [x] Audiência de origem (seed) com no mínimo 1.000 usuários ativos e homogêneos (ex: apenas compradores ou leads qualificados).
- [x] Testar diferentes tamanhos de Lookalike (ex: 1%, 2%, 5%, 1-3%, 3-6%, 6-10%) para encontrar o equilíbrio entre similaridade e alcance.
- [x] Excluir a audiência de origem da Lookalike no conjunto de anúncios para evitar sobreposição e impacto na mensuração.
- [x] Segmentar geograficamente a Lookalike para o público relevante (ex: apenas Brasil, ou estados específicos).
- [x] Alinhar o objetivo da campanha (ex: Vendas, Geração de Leads) com o comportamento da audiência de origem da Lookalike (ex: LLA de compradores para vendas).
- [x] Testar criativos específicos para cada LLA, considerando o nível de familiaridade esperado do público.
- [x] Implementar CBO (Campaign Budget Optimization) ou ABO (Ad Set Budget Optimization) para testar múltiplas LLAs na mesma campanha eficientemente.
- [x] Monitorar ROAS, CPA, CTR e Taxa de Conversão específicos por LLA para otimização contínua de lances e orçamentos.
- [x] Atualizar as audiências de origem dinamicamente (via Pixel, API de Conversões, feed de clientes) para manter a relevância da Lookalike.