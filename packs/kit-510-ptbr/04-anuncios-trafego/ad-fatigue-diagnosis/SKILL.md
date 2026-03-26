---
name: ad-fatigue-diagnosis
description: "Ad Fatigue Diagnosis — Skill especializada para ad fatigue diagnosis"
license: MIT
metadata:
  version: 1.0.0
  author: Cafe Code AI
  category: 04-anuncios-trafego
  updated: 2026-03-01
risk: safe
---

# Ad Fatigue Diagnosis

Esta skill capacita o Claude a identificar, analisar e prescrever soluções para a fadiga de anúncios em campanhas de Meta Ads, Google Ads e TikTok Ads, otimizando a performance e o custo por resultado.

---

## Keywords

Fadiga de anúncios, Ad Fatigue, Frequência de Exibição, CTR Decrescente, CPM Crescente, Custo por Resultado Aumentando, Meta Ads, Google Ads, TikTok Ads, Otimização de Criativos, Rotação de Anúncios, Segmentação de Público, CPA Elevado, ROAS em Queda, Diagnóstico de Relevância.

---

## Quick Start

1.  **Monitorar Frequência de Exibição**: Verifique a coluna "Frequência" em Meta Ads ou TikTok Ads. Frequências médias superiores a 3.0 em 7 dias para públicos frios, ou 5.0 para públicos quentes, acendem um alerta.
2.  **Analisar Tendência de CTR e Custo**: Compare a Taxa de Cliques (CTR) e o Custo por Ação (CPA/CPL) dos últimos 7 dias com os 7 dias anteriores. Queda de CTR superior a 20% e aumento de CPA superior a 15% são fortes indicadores de fadiga.
3.  **Verificar Feedback e Relevância**: Acesse os relatórios de "Qualidade do Ranking" (Meta Ads) ou "Score de Qualidade" (Google Ads). Leia os comentários dos anúncios para identificar menções como "anúncio repetido" ou "chato", validando a fadiga.
4.  **Preparar Novos Ativos**: Inicie imediatamente a criação de novos criativos (imagens, vídeos, copy) e explore novas segmentações de público para testes.

---

## Core Workflows

### Workflow 1: Diagnóstico Preditivo de Ad Fatigue por Frequência e Engajamento

**Contexto**: Campanhas com performance ainda estável, mas com sinais incipientes de saturação de público e risco de fadiga iminente. O objetivo é intervir antes que as métricas de resultado final (CPA, ROAS) sejam severamente impactadas.

**Passo 1: Monitoramento Avançado da Frequência de Exibição**
*   **Ação**: Acesse o painel de Meta Ads (ou Google Ads/TikTok Ads) e adicione a coluna "Frequência" no nível de "Conjunto de Anúncios" (Ad Set). Exporte os dados para uma planilha para análise histórica.
*   **Exemplo Prático**: Para uma campanha no Meta Ads com um público de prospecção (frio) de 1 milhão de pessoas, se a "Frequência" média nos últimos 7 dias atingir 2.8, isso já é um sinal amarelo. Para um público de remarketing de 100 mil pessoas, uma "Frequência" de 4.5 em 7 dias indica alto risco de saturação.
*   **Limiar de Alerta**: Frequência > 2.5 em 7 dias para públicos frios (prospecção) ou > 4.0 em 7 dias para públicos quentes (remarketing) exige atenção imediata.

**Passo 2: Análise Combinada de CTR, Frequência e Taxa de Conclusão de Vídeo**
*   **Ação**: Compare a "Frequência" com a "Taxa de Cliques (CTR)" e, para criativos em vídeo, a "Taxa de Conclusão de Vídeo (75% ou 100%)".
*   **Exemplo Prático**: Um anúncio em Google Display Ads que há 30 dias tinha Frequência 1.8 e CTR 0.9%, e agora apresenta Frequência 3.5 e CTR 0.6%, mostra clara fadiga. Em TikTok Ads, um vídeo que antes tinha 40% de conclusão a 75% e agora tem 18% com frequência alta, indica desinteresse.
*   **Métrica de Referência**: Queda de CTR > 15% em conjunto com aumento de Frequência > 10% (comparando os últimos 7 dias com os 7 dias anteriores) é um forte preditor. Queda de 50% na taxa de conclusão de vídeo também.

**Passo 3: Verificação da Qualidade do Feedback e Diagnóstico de Relevância (Meta Ads / Google Ads)**
*   **Ação**: Em Meta Ads, navegue até o nível do anúncio e verifique o "Diagnóstico de Relevância" (qualidade, engajamento, conversão). Em Google Ads, observe o "Score de Qualidade" das palavras-chave e a relevância do anúncio.
*   **Exemplo Prático**: Um anúncio no Meta Ads com "Qualidade do Ranking" abaixo da média e "Taxa de Engajamento do Ranking" abaixo da média, associado a comentários negativos recorrentes como "Não aguento mais ver isso", confirma a fadiga e a percepção de irrelevância pelo público. Um Score de Qualidade de 3/10 em Google Ads para termos de alta relevância também é um sinal.
*   **Ação Imediata**: Priorize a criação de criativos totalmente novos e com abordagens de mensagem distintas para os anúncios com pior diagnóstico de relevância.

### Workflow 2: Otimização Reativa de Campanhas com Ad Fatigue Confirmada

**Contexto**: Campanha com performance em declínio acentuado (ROAS caindo, CPL/CPA subindo rapidamente) e diagnóstico de fadiga já confirmado pelos indicadores do Workflow 1. O objetivo é reverter a tendência de queda e otimizar rapidamente.

**Passo 1: Rotação Agressiva e Teste de Novos Criativos**
*   **Ação**: Pause os anúncios com pior performance (maior frequência, menor CTR, maior CPA) e ative imediatamente um novo conjunto de criativos.
*   **Exemplo Prático**: Em uma campanha de Meta Ads, um vídeo A teve Frequência 6.1 e CTR 0.5% nos últimos 15 dias, enquanto um vídeo B (novo) está com Frequência 1.5 e CTR 2.8%. Pause o vídeo A, e lance 3-4 novas variações (ex: vídeo com outro ângulo, imagem estática com depoimento, carrossel de benefícios) para o mesmo conjunto de anúncios, permitindo que a plataforma otimize a entrega para os mais engajantes.
*   **Estratégia**: Mantenha sempre um "pool" de 3-5 criativos frescos e não relacionados diretamente aos anteriores para cada conjunto de anúncios com alto risco de fadiga. A cada 7-10 dias, avalie a performance e substitua os de menor desempenho.

**Passo 2: Reengenharia de Públicos-Alvo e Exclusões**
*   **Ação**: Se o público estiver saturado, expanda-o ou crie novos segmentos radicalmente diferentes. Implemente exclusões rigorosas.
*   **Exemplo Prático**: Para Google Ads, se um público de "Interesses Afins" estiver mostrando alta frequência e alto CPC, adicione novos interesses relacionados, mas também crie um público personalizado por intenção com novas palavras-chave de cauda longa e crie um público de exclusão para quem já visitou a página de agradecimento (compra/lead) nos últimos 90 dias. No Meta Ads, crie um "Lookalike" 1% com base nos conversores mais recentes (últimos 7 dias) e exclua todos que interagiram com a página ou anúncios nos últimos 30 dias.
*   **Ação Específica**: Para campanhas de remarketing, refine a janela de segmentação (ex: de 30 para 7 dias) e aumente a agressividade das exclusões de quem já converteu ou se engajou repetidamente sem converter.

**Passo 3: Ajuste Tático de Orçamento e Estratégia de Lances**
*   **Ação**: Reduza o orçamento para conjuntos de anúncios com fadiga severa e realoque para novos conjuntos com públicos e criativos frescos. Considere ajustar a estratégia de lances.
*   **Exemplo Prático**: Um conjunto de anúncios no TikTok Ads que antes gerava leads a R$12, agora gera a R$45 com Frequência 7.0. Reduza o orçamento diário de R$150 para R$50 e crie um novo conjunto com criativos e públicos que ainda não foram explorados, destinando os R$100 restantes para este novo conjunto.
*   **Consideração**: Em plataformas com lances automáticos (Target CPA, ROAS Alvo), a fadiga pode levar a um aumento do lance para "forçar" a entrega. Considere testar lances manuais ou semi-automáticos (Custo Máximo) em um novo conjunto para ter mais controle sobre o custo, especialmente em fase de recuperação.

---

## Templates

### Relatório de Análise de Ad Fatigue

```
## Relatório de Análise de Ad Fatigue - [Nome da Campanha/Ad Set]

**Data da Análise:** 2024-11-05
**Período Analisado:** Últimos 30 dias vs. 30 dias anteriores (2024-10-06 a 2024-11-05)

**1. Diagnóstico Principal:**
*   **Campanha/Ad Set:** "Meta Ads - Venda de Ebook Marketing para Pequenas Empresas - Público Frio"
*   **Plataforma:** Meta Ads
*   **Status Geral:** Fadiga Moderada a Alta. Queda acentuada de CTR e aumento de CPL, com alta frequência.

**2. Métricas Chave Observadas:**
*   **Frequência Média (Últimos 7 dias):** 4.1 (+32% vs. período anterior)
*   **Frequência Média (Últimos 30 dias):** 7.8 (+20% vs. período anterior)
*   **CTR Média (Últimos 7 dias):** 0.65% (-40% vs. período anterior)
*   **Custo por Lead (CPL) (Últimos 7 dias):** R$ 22.80 (+65% vs. período anterior)
*   **CPM (Últimos 7 dias):** R$ 28.50 (+25% vs. período anterior)
*   **Taxa de Conclusão Vídeo (75%) (Últimos 7 dias):** 15% (-55% vs. período anterior)
*   **Comentários/Feedback:** Aumento de comentários como "Já vi esse anúncio mil vezes!", "Irrelevante pra mim", "Chato". Diagnóstico de Relevância (Meta Ads): "Qualidade do Ranking" e "Taxa de Engajamento do Ranking" abaixo da média.

**3. Criativos Afetados:**
*   **ID do Criativo 1:** [VIDEO_ID_456789] - Vídeo "Depoimento Cliente Satisfeito"
    *   **Frequência:** 4.8
    *   **CTR:** 0.58%
    *   **CPL:** R$ 25.00
    *   **Observações:** Principal gerador de feedback negativo e pior performance de conclusão de vídeo.
*   **ID do Criativo 2:** [IMAGE_ID_123456] - Imagem "Infográfico 5 Dicas Marketing"
    *   **Frequência:** 3.9
    *   **CTR:** 0.72%
    *   **CPL:** R$ 20.50
    *   **Observações:** Performance em declínio, mas ainda com algum engajamento residual.

**4. Público Afetado:**
*   **Nome do Público:** "Interesses: Empreendedorismo, Pequenas Empresas, Marketing Digital (Brasil)" - Tamanho: 9.2M
*   **Observações:** A alta frequência e a queda de engajamento indicam que a parcela mais responsiva deste público está saturada com os criativos atuais.

**5. Recomendações Imediatas:**
*   Pausar imediatamente o Criativo [VIDEO_ID_456789].
*   Duplicar o Ad Set e testar 4 novos criativos (2 vídeos, 2 imagens estáticas) focados em novos ângulos (ex: "Economia de Tempo", "Aumento de Vendas", "Ferramentas Essenciais").
*   Criar um novo público Lookalike 1% baseado nos leads gerados nos últimos 14 dias (para o novo Ad Set).
*   Reduzir orçamento do Ad Set atual em 40% e alocar em um novo Ad Set com os novos criativos e público.
*   Implementar exclusão de quem interagiu com anúncios nos últimos 7 dias no Ad Set original.
*   Monitorar Frequência, CTR e CPL diariamente nos próximos 7 dias nos novos Ad Sets.
```