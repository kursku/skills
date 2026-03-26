---
name: ab-test-analysis
description: "Ab Test Analysis — Skill especializada para ab test analysis"
license: MIT
metadata:
  version: 1.0.0
  author: Cafe Code AI
  category: 15-analytics-dados
  updated: 2026-03-01
risk: safe
---

# Ab Test Analysis

Essa skill capacita o Claude Code a planejar, executar e analisar experimentos A/B complexos, utilizando dados do Google Analytics 4 para otimização de performance.

---

## Keywords

Teste A/B, GA4, Análise Estatística, Significância, Mínimo Efeito Detectável (MDE), Intervalo de Confiança, Validação de Hipótese, Segmentação de Audiência, Atribuição de Conversão, Otimização CRO, Hipótese Nula, Poder Estatístico.

---

## Quick Start

1.  Definir a hipótese de teste e a métrica primária no plano de experimento, como "Mudar o CTA de 'Saiba Mais' para 'Comprar Agora' aumentará a taxa de cliques (CTR) em 10%".
2.  Configurar um parâmetro de evento personalizado `ab_variant` no GA4 (via GTM ou código) para registrar qual variação (ex: `original`, `variacao_b`) o usuário visualizou em eventos chave como `page_view` ou `click`.
3.  Implementar o teste utilizando uma ferramenta de A/B testing (ex: Google Optimize, VWO), garantindo uma distribuição aleatória de tráfego de 50/50 para as variações.
4.  Monitorar o volume de dados e anomalias nas explorações de "Tempo Real" e "DebugView" do GA4 para assegurar que os eventos `ab_variant` estão sendo coletados corretamente para ambas as variações.
5.  Calcular a significância estatística e o intervalo de confiança para a métrica primária utilizando os dados exportados do GA4, apenas após atingir o tamanho amostral predefinido.

---

## Core Workflows

### Workflow 1: Configuração e Coleta de Dados de Experimento A/B no GA4

Este workflow detalha a preparação técnica no Google Analytics 4 para um experimento A/B, garantindo que os dados coletados sejam fidedignos e segmentáveis.

1.  **Definição da Hipótese e Métricas Operacionais:**
    *   **Exemplo:** "Hipótese: A inclusão de um selo de 'Frete Grátis' na página de produto aumentará a taxa de adição ao carrinho (ATC) em 7%, sem impactar negativamente a taxa de conversão final."
    *   **Métrica Primária:** Taxa de `add_to_cart` (event_count do evento `add_to_cart` / total_users na página de produto).
    *   **Métricas Secundárias:** Taxa de Conversão (`purchase` / total_users), `ecommerce_purchase_revenue`.
    *   **Mínimo Efeito Detectável (MDE):** Definir o menor efeito que seria considerado importante para a empresa, ex: 5% de aumento na taxa de `add_to_cart`.

2.  **Configuração de Parâmetros de Evento Personalizados no GA4:**
    *   **Passo A: Via Google Tag Manager (GTM):**
        *   Crie uma Variável de Camada de Dados (Data Layer Variable) no GTM chamada `abTestVariant` que será preenchida pela ferramenta de A/B testing (ex: `original`, `selo_frete`).
        *   Em todas as Tags de Evento GA4 relevantes (ex: `page_view`, `add_to_cart`, `purchase`), adicione um novo "Parâmetro do Evento".
        *   **Nome do Parâmetro:** `ab_variant`
        *   **Valor do Parâmetro:** `{{abTestVariant}}` (referenciando a variável do GTM).
        *   Certifique-se de que a ferramenta de A/B testing (ex: Google Optimize) empurra o valor correto para a `dataLayer` como `window.dataLayer.push({'event': 'optimize.activate', 'abTestVariant': 'selo_frete'});` quando a variação é ativada.
    *   **Passo B: Registro do Parâmetro como Dimensão Personalizada no GA4:**
        *   No GA4, vá em `Administrador` -> `Configurações de dados` -> `Definições personalizadas`.
        *   Crie uma nova "Dimensão personalizada".
        *   **Nome da dimensão:** `Variação AB` (ou similar)
        *   **Escopo:** Evento
        *   **Nome do parâmetro do evento:** `ab_variant` (deve ser idêntico ao configurado no GTM/código).
        *   Isso permitirá segmentar relatórios e explorações pelo parâmetro `ab_variant`.

3.  **Criação de Audiências para Análise Pós-Teste (Opcional, mas Recomendado):**
    *   No GA4, vá em `Administrador` -> `Exibição de dados` -> `Audiências`.
    *   Crie uma nova audiência para cada variação:
        *   **Audiência "Controle - Sem Selo":** Usuários com o evento `page_view` e parâmetro `ab_variant` = `original`.
        *   **Audiência "Variação - Com Selo":** Usuários com o evento `page_view` e parâmetro `ab_variant` = `selo_frete`.
    *   Essas audiências podem ser usadas em "Explorações" para análises mais aprofundadas do comportamento específico de cada grupo.

4.  **Validação da Coleta de Dados:**
    *   Use o "DebugView" do GA4 (`Administrador` -> `Configurações de dados` -> `DebugView`) para verificar em tempo real se os eventos `page_view` e `add_to_cart` estão sendo disparados com o parâmetro `ab_variant` correto para ambas as variações do teste.
    *   Monitore o relatório de "Tempo Real" para identificar o tráfego inicial e garantir que ambas as variações estão recebendo usuários.

### Workflow 2: Análise Estatística e Interpretação de Resultados A/B com GA4

Este workflow descreve como analisar os dados coletados no GA4, aplicar testes estatísticos e interpretar os resultados para tomar decisões embasadas.

1.  **Exportação de Dados para Análise:**
    *   No GA4, vá em `Explorações` -> `Formato livre`.
    *   Configure a exploração com as seguintes dimensões e métricas:
        *   **Dimensões:** `Variação AB` (a dimensão personalizada criada), `Nome do evento`, `Data`.
        *   **Métricas:** `Total de usuários`, `Eventos`.
    *   Filtre a exploração pelo `Nome do evento` da sua métrica primária (ex: `add_to_cart`) e pelo período do teste.
    *   Exporte os dados para CSV ou conecte o GA4 ao BigQuery para extração programática, o que é ideal para grandes volumes ou automação.
    *   **Exemplo de Tabela de Dados Exportada (simplificada):**
        ```
        Data         | ab_variant | Nome do evento  | Total de usuários | Eventos
        -------------------------------------------------------------------------
        2024-07-01   | original   | page_view       | 1000              | 1000
        2024-07-01   | original   | add_to_cart     | 80                | 80
        2024-07-01   | variacao_b | page_view       | 1050              | 1050
        2024-07-01   | variacao_b | add_to_cart     | 95                | 95
        ...
        ```

2.  **Cálculo do Tamanho Amostral e Duração Necessária:**
    *   Antes de iniciar a análise, confirme se o tamanho amostral mínimo foi atingido para cada variação.
    *   Use uma calculadora de A/B online (ex: Optimizely, Evan Miller) ou um script Python/R.
    *   **Inputs:** Taxa de base da métrica primária (ex: 8% ATC), MDE (ex: 7% relativo, o que seria 0.56pp), significância (ex: 95%, alpha=0.05), poder estatístico (ex: 80%).
    *   **Output Exemplo:** Para uma taxa base de 8% e MDE de 7% (0.56pp), seriam necessários aproximadamente 25.000 usuários únicos por variação.
    *   Verifique se a duração do teste abrangeu pelo menos um ciclo de negócios completo (ex: 7 ou 14 dias) para mitigar efeitos de sazonalidade.

3.  **Análise Estatística:**
    *   **Passo A: Calcular as Taxas:**
        *   **Controle:** `Taxa ATC = (Eventos 'add_to_cart' na variação original) / (Total de usuários na variação original)`
        *   **Variação B:** `Taxa ATC = (Eventos 'add_to_cart' na variação B) / (Total de usuários na variação B)`
    *   **Passo B: Teste de Hipótese (Ex: Teste Z para proporções):**
        *   Utilize uma ferramenta estatística (Python com `scipy.stats`, R, ou calculadora online) para comparar as duas proporções.
        *   **Exemplo (Python):**
            ```python
            from statsmodels.stats.proportion import proportions_ztest
            count_original = 2000 # Cliques ATC original
            nobs_original = 25000 # Usuarios original
            count_variant = 2275 # Cliques ATC variacao_b
            nobs_variant = 25000 # Usuarios variacao_b

            # Calculo do p-value
            stat, pval = proportions_ztest([count_original, count_variant], [nobs_original, nobs_variant])
            print(f"P-value: {pval:.4f}")

            # Calculo do Intervalo de Confiança para a diferença
            from statsmodels.stats.proportion import confint_proportions_2indep
            lower, upper = confint_proportions_2indep(count_original, nobs_original, count_variant, nobs_variant, compare='diff')
            print(f"Intervalo de Confiança (95%) para a diferença: [{lower:.4f}, {upper:.4f}]")
            ```
        *   **Resultado Exemplo:** `P-value: 0.008`, `Intervalo de Confiança (95%) para a diferença: [0.003, 0.015]` (ou seja, [0.3pp, 1.5pp] de aumento).

4.  **Interpretação e Decisão:**
    *   **Significância Estatística:** Se o `p-value` for menor que o nível de significância (geralmente 0.05), rejeite a hipótese nula. Isso significa que a diferença observada não é devido ao acaso.
    *   **Magnitude do Efeito:** Verifique se a diferença observada é maior que o MDE definido no início. Um resultado estatisticamente significativo, mas com um efeito muito pequeno, pode não ser worth a implementação.
    *   **Intervalo de Confiança:** Analise se o intervalo de confiança da diferença inclui o zero. Se não incluir, a diferença é significativa. O intervalo também dá uma estimativa da verdadeira magnitude do efeito.
    *   **Métricas Secundárias:** Avalie as métricas secundárias no GA4 (`purchase`, `ecommerce_purchase_revenue`) utilizando as audiências criadas ou as explorações. Garanta que a otimização da métrica primária não prejudicou outras métricas importantes.
    *   **Exemplo de Decisão:** "Com um p-value de 0.008 (abaixo de 0.05) e um aumento de 0.9pp na taxa de ATC (de 8% para 8.9%), o que representa um ganho de 11.25% relativo e está acima do MDE de 7%, a variação 'Com Selo Frete Grátis' é estatisticamente superior. As métricas de conversão final e receita não apresentaram degradação. Recomendamos implementar a variação."

---

## Templates

### Plano de Experimento A/B - Selo de Frete Grátis

```
# Plano de Experimento A/B - Selo de Frete Grátis

**Data:** 2024-07-26
**Responsável:** Equipe de Otimização de Conversão

## 1. Objetivo
Validar se a inclusão de um selo visual de "Frete Grátis" na página de produto aumenta a taxa de adição ao carrinho (ATC) sem impactar negativamente a taxa de conversão final.

## 2. Hipótese
*   **H0 (Nula):** A exibição do selo "Frete Grátis" na página de produto NÃO terá um impacto estatisticamente significativo na taxa de ATC.
*   **H1 (Alternativa):** A exibição do selo "Frete Grátis" na página de produto AUMENTARÁ a taxa de ATC em pelo menos 7%.

## 3. Variações
*   **Controle (A):** Página de produto sem o selo "Frete Grátis".
*   **Variação (B):** Página de produto com um selo "Frete Grátis" posicionado abaixo do preço do produto.

## 4. Métricas
*   **Métrica Primária:** Taxa de Adição ao Carrinho (ATC) (event_count do evento 'add_to_cart' / total_users na página de produto).
*   **Métricas Secundárias:** Taxa de Conversão (purchase / total_users na página de produto), Receita por Usuário (ecommerce_purchase_revenue / total_users), Cliques em "Comprar Agora" (click_comprar_agora / total_users).

## 5. Segmento Alvo
100% do tráfego web que acessa as páginas de produto.

## 6. Configuração GA4
*   Parâmetro de evento `ab_variant` (valores: `original`, `selo_frete`) para eventos `page_view`, `add_to_cart`, `purchase`.
*   Dimensão personalizada `Variação AB` configurada no GA4.
*   Audiências `Controle - Sem Selo` e `Variação - Com Selo` criadas para análise pós-teste.

## 7. Critérios de Sucesso e Parada
*   Aumento estatisticamente significativo da Taxa de ATC (p < 0.05).
*   Aumento da Taxa de ATC maior ou igual ao MDE de 7% (relativo).
*   Tamanho amostral mínimo atingido (ex: 25.000 usuários únicos por variação).
*   Duração mínima do teste: 14 dias (2 ciclos de negócios completos).
*   Nenhuma degradação estatisticamente significativa nas métricas secundárias.

## 8. Ferramentas
Google Optimize (implementação), Google Analytics 4 (coleta e monitoramento), Python/R ou Planilha (análise estatística).
```

### Relatório de Análise de Experimento A/B - Selo de Frete Grátis

```
# Relatório de Análise de Experimento A/B - Selo de Frete Grátis

**Data da Análise:** 2024-08-15
**Período do Teste:** 2024-07-28 a 2024-08-11 (14 dias)
**Status:** Concluído

## 1. Resumo Executivo
O experimento para