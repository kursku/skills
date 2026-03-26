---
name: funnel-analysis
description: "Funnel Analysis — Skill especializada para identificar gargalos, otimizar fluxos de conversão e maximizar a performance de jornadas de usuário em plataformas digitais usando Google Analytics 4."
license: MIT
metadata:
  version: 1.0.0
  author: Cafe Code AI
  category: 15-analytics-dados
  updated: 2026-03-01
risk: safe
---

# Funnel Analysis

Esta skill capacita o Claude a dominar a análise de funis de conversão, desde a configuração no Google Analytics 4 (GA4) até a interpretação de dados e a proposição de otimizações acionáveis para melhorar as taxas de conversão.

---

## Keywords

Funil de Conversão, Análise de Funil, Google Analytics 4 (GA4), Explorações de Funil, Taxa de Drop-off, Otimização de Conversão, Atribuição Multicanal, Customer Journey Mapping, Segmentação de Usuários, Metas de Conversão, Etapas do Funil, Eventos GA4, User Journey, Retenção no Funil, CRO (Conversion Rate Optimization).

---

## Quick Start

1.  **Acessar a Biblioteca de Explorações no GA4**: No menu lateral esquerdo do GA4, navegar para "Explorar" (o ícone de um losango).
2.  **Criar uma Nova Exploração de Funil**: Clicar em "Galeria de modelos" e selecionar "Exploração de funil".
3.  **Configurar as Etapas do Funil com Eventos GA4**: Adicionar as etapas definindo eventos específicos (ex: `page_view` para visita à página inicial, `add_to_cart` para adição ao carrinho) e, se necessário, parâmetros adicionais (ex: `page_location` igual a '/checkout').
4.  **Analisar Taxas de Abandono e Conversão**: Observar as barras vermelhas (drop-off) e verdes (conversão) entre as etapas para identificar os maiores pontos de fricção na jornada.
5.  **Aplicar Segmentos para Insights Iniciais**: Usar segmentos pré-definidos (ex: "Tráfego de Pesquisa Orgânica", "Dispositivos Móveis") ou personalizados para ver como diferentes grupos de usuários se comportam no funil.

---

## Core Workflows

### Workflow 1: Construindo e Analisando um Funil de E-commerce no GA4

Este workflow detalha a criação e análise de um funil de e-commerce, focando em identificar gargalos e propor melhorias.

**Passos Detalhados:**

1.  **Definir as Etapas Críticas do Funil de E-commerce**:
    *   **Etapa 1: Visualização de Produto**: Usuário visita uma página de produto. Evento GA4: `view_item`.
    *   **Etapa 2: Adição ao Carrinho**: Usuário adiciona um produto ao carrinho. Evento GA4: `add_to_cart`.
    *   **Etapa 3: Início do Checkout**: Usuário clica para iniciar o processo de checkout. Evento GA4: `begin_checkout`.
    *   **Etapa 4: Informações de Envio**: Usuário preenche ou visualiza a etapa de informações de envio. Evento GA4: `add_shipping_info`.
    *   **Etapa 5: Informações de Pagamento**: Usuário preenche ou visualiza a etapa de informações de pagamento. Evento GA4: `add_payment_info`.
    *   **Etapa 6: Compra Concluída**: Usuário finaliza a compra. Evento GA4: `purchase`.

2.  **Criar a Exploração de Funil no GA4**:
    *   No GA4, navegar para "Explorar" > "Biblioteca de Explorações".
    *   Selecionar "Exploração de funil" (geralmente sob a galeria de modelos).
    *   Nomear a exploração como "Funil de Checkout E-commerce".

3.  **Configurar as Etapas na Interface da Exploração**:
    *   No painel "Configurações de guia", em "Etapas", clicar no ícone de lápis para editar.
    *   Adicionar cada etapa conforme definido no Passo 1, nomeando-as e selecionando o evento GA4 correspondente.
    *   **Exemplo de Configuração de Etapa**:
        *   **Etapa 1**: Nome "Visualização de Produto", Evento `view_item`.
        *   **Etapa 2**: Nome "Adição ao Carrinho", Evento `add_to_cart`.
        *   **Etapa 3**: Nome "Início do Checkout", Evento `begin_checkout`.
        *   **Etapa 4**: Nome "Informações de Envio", Evento `add_shipping_info`.
        *   **Etapa 5**: Nome "Informações de Pagamento", Evento `add_payment_info`.
        *   **Etapa 6**: Nome "Compra Concluída", Evento `purchase`.
    *   Certificar-se de que a opção "Funil aberto" está selecionada inicialmente para ver entradas em qualquer etapa.

4.  **Análise de Drop-off e Taxas de Conversão**:
    *   Observar o gráfico de barras do funil. Cada barra representa uma etapa e mostra o número de usuários que a atingiram. A linha entre as barras indica a taxa de drop-off (em vermelho) e a taxa de conversão (em verde) para a próxima etapa.
    *   **Exemplo de Análise**: Se a transição de "Início do Checkout" para "Informações de Envio" mostra um drop-off de 55%, isso indica um problema significativo nessa fase. Investigar o formulário de envio, custos de frete, ou exigência de login.
    *   **Métrica Chave**: Taxa de Conclusão do Funil (total de usuários na última etapa / total de usuários na primeira etapa). Ex: (1.500 `purchase` / 10.000 `view_item`) = 15%.

5.  **Segmentação para Identificar Padrões Específicos**:
    *   No painel "Configurações de guia", em "Segmentos", adicionar segmentos para comparar o comportamento.
    *   **Exemplos de Segmentos a Aplicar**:
        *   "Usuários de Dispositivos Móveis" vs. "Usuários de Desktop".
        *   "Novos Usuários" vs. "Usuários Recorrentes".
        *   "Tráfego Orgânico" vs. "Tráfego Pago (Google Ads)".
    *   **Insight Acionável**: Se o drop-off de "Informações de Pagamento" para "Compra Concluída" é 70% para usuários de mobile, mas apenas 20% para desktop, investigar a usabilidade do formulário de pagamento em dispositivos móveis.

### Workflow 2: Otimização de Funil Baseada em Insights de Atribuição

Este workflow foca em como usar dados de atribuição no GA4 para entender quais canais ou pontos de contato são mais eficazes em cada etapa do funil e otimizar estratégias de marketing.

**Passos Detalhados:**

1.  **Identificar a Etapa Crítica de Drop-off**:
    *   Utilizar a "Exploração de Funil" criada no Workflow 1 para pinpointar a etapa com a maior taxa de abandono.
    *   **Exemplo**: O drop-off entre "Adição ao Carrinho" (`add_to_cart`) e "Início do Checkout" (`begin_checkout`) é consistentemente alto, digamos, 60%.

2.  **Acessar o Relatório de Atribuição de Modelo de Dados no GA4**:
    *   Navegar para "Publicidade" > "Atribuição" > "Caminhos de Conversão".
    *   Selecionar o evento de conversão final (ex: `purchase`) e o período de tempo desejado.

3.  **Analisar Caminhos de Conversão Relacionados à Etapa Crítica**:
    *   No relatório "Caminhos de Conversão", filtrar os caminhos para incluir ou excluir a etapa crítica.
    *   **Exemplo**: Filtrar para ver os caminhos que *incluem* o evento `add_to_cart` mas *não* o `begin_checkout`. Isso revelará os canais que trazem usuários que abandonam entre essas duas etapas.
    *   Observar a sequência de canais (ex: Google Orgânico > Direto > Email) e a quantidade de conversões para cada caminho.

4.  **Cruzar Dados de Atribuição com Comportamento Específico**:
    *   Se o relatório de atribuição mostra que muitos usuários de `cpc` (Google Ads) iniciam o funil, mas têm uma taxa de conversão menor para a etapa `begin_checkout` comparado a usuários de `email`, isso é um insight.
    *   **Hipótese**: Talvez a página de destino (landing page) dos anúncios não esteja alinhada com a expectativa do usuário ao chegar no carrinho, ou a oferta não é tão clara para esse segmento.

5.  **Ação de Otimização Baseada em Atribuição**:
    *   **Exemplo de Ação**: Para o cenário acima, criar uma variante de landing page para os anúncios do Google Ads que pré-qualifique melhor o usuário sobre os custos de frete ou o processo de checkout, ou testar diferentes CTAs na página do carrinho.
    *   **Métrica de Avaliação**: Monitorar a Taxa de Conversão de `add_to_cart` para `begin_checkout` especificamente para o segmento `cpc` após a implementação das mudanças.
    *   **Outro Exemplo**: Se usuários de `social` convertem bem no topo do funil (`view_item` para `add_to_cart`), mas caem drasticamente no checkout, considerar campanhas de remarketing via social media focadas em recuperação de carrinho.

---

## Templates

### Template: Relatório de Análise de Funil para Reunião Executiva (Looker Studio/GA4)

```
# Relatório Executivo: Performance do Funil de E-commerce

## Período: Últimos 30 Dias (01/02/2026 - 01/03/2026)

## Sumário Executivo
- **Objetivo Primário:** Otimizar o funil de checkout para aumentar a Taxa de Conversão de compra.
- **Taxa de Conclusão do Funil (Visita > Compra):** 2.8% (vs. 2.5% no período anterior)
- **Receita Total Gerada:** R$ 125.000
- **Principal Gargalo Identificado:** Transição de "Informações de Envio" para "Informações de Pagamento".

## Visão Geral do Funil de Checkout
| Etapa              | Evento GA4           | Entradas (Usuários) | Taxa de Conversão para Próxima Etapa | Taxa de Drop-off para Próxima Etapa |
|--------------------|----------------------|--------------------|--------------------------------------|-------------------------------------|
| 1. Visualização Produto | `view_item`         | 50.000             | 35%                                  | 65%                                 |
| 2. Adição ao Carrinho   | `add_to_cart`       | 17.500             | 45%                                  | 55%                                 |
| 3. Início do Checkout   | `begin_checkout`    | 7.875              | 60%                                  | 40%                                 |
| 4. Informações de Envio | `add_shipping_info` | 4.725              | **30%**                              | **70%** (Gargalo Principal)         |
| 5. Informações de Pagamento | `add_payment_info` | 1.417              | 80%                                  | 20%                                 |
| 6. Compra Concluída     | `purchase`          | 1.133              | N/A                                  | N/A                                 |

## Análise do Gargalo: Informações de Envio > Informações de Pagamento (70% Drop-off)
- **Segmentação (Mobile vs. Desktop):**
    - Mobile: 85% de drop-off
    - Desktop: 50% de drop-off
- **Causas Potenciais Identificadas (via Hotjar/Pesquisa):**
    1.  Formulário de endereço complexo/lento em mobile.
    2.  Falta de clareza sobre opções de frete gratuito/expresso.
    3.  Mensagens de erro genéricas no preenchimento do CEP.

## Recomendações e Próximos Passos
1.  **Otimização do Formulário de Endereço (Mobile):** Implementar autocomplete para CEP e campos mais intuitivos. (Responsável: Dev Team, Prazo: 15/03)
2.  **Clareza no Frete:** Exibir claramente opções e custos de frete antes da etapa de pagamento. (Responsável: Marketing/Dev, Prazo: 10/03)
3.  **Teste A/B de Layout de Checkout:** Testar um checkout em uma única página vs. multi-etapas. (Responsável: CRO Specialist, Prazo: 30/03)
4.  **Monitoramento:** Acompanhar a taxa de drop-off dessa etapa semanalmente no GA4 para medir impacto.
```

### Template: Briefing para A/B Test de Otimização de Funil

```
# Briefing para A/B Test: Otimização da Etapa "Informações de Pagamento"

## 1. Contexto e Objetivo
- **Funil Alvo:** Funil de Checkout (Etapa 5: Informações de Pagamento).
- **Problema:** Alta taxa de drop-off (50%) na transição de "Informações de Pagamento" para "Compra Concluída" para usuários mobile nos últimos 30 dias.
- **Objetivo do Teste:** Reduzir o drop-off nessa etapa em 10% (de 50% para 45%) para usuários de dispositivos móveis.

## 2. Hipótese
"Se simplificarmos o formulário de pagamento e adicionarmos selos de segurança visíveis na etapa de 'Informações de Pagamento' para usuários mobile, a confiança aumentará e a taxa de drop-off diminuirá."

## 3. Variantes do Teste
- **Controle (A):** Versão atual da página de "Informações de Pagamento" (GA4 `add_payment_info`).
- **Variante (B):**
    1.  Formulário de cartão de crédito com campos auto-formatados e máscaras para mobile.
    2.  Exibição de selos de segurança (SSL, bandeiras de cartão) proeminentes abaixo do título da página.
    3.  Remoção de campos opcionais não essenciais.

## 4. Métricas de Sucesso
- **Métrica Primária:** Taxa de Conversão da Etapa `add_payment_info` para `purchase` (segmentado por mobile).
- **Métricas Secundárias:**
    - Tempo médio na página de "Informações de Pagamento" (mobile).
    - Taxa de Erro de Validação de Formulário na etapa de pagamento (mobile).
    - Receita por Usuário (RPU) dos usuários que passaram por essa etapa (mobile).

## 5. Segmentação e Período
- **Segmento:** Apenas usuários acessando via dispositivos móveis.
- **Duração do Teste:** 3 semanas ou até atingir significância estatística (ex: 95% de confiança).
- **Ferramenta de A/B Test:** Google Optimize (conectado ao GA4).

## 6. Recursos Necessários
- **Desenvolvimento:** Implementação das alterações na variante B.
- **Design:** Criação dos selos de segurança e revisão da UI do formulário.
- **Análise:** Configuração do experimento no Google Optimize e monitoramento no GA4.

## 7. Próximos Passos Pós-Teste
- Análise de resultados no GA4/Google Optimize.
- Implementação da variante vencedora (se houver significância).
- Documentação dos aprendizados para futuros testes.
```

---

## Checklist

-   [x] Mapear todas as etapas críticas do funil com eventos GA4 bem definidos e documentados.
-   [x] Validar a coleta de dados de cada evento do funil utilizando o DebugView do GA4 e relatórios em tempo real.
-   [x] Criar uma exploração de funil "fechado" no GA4 para analisar o fluxo linear e estrito das etapas.
-   [x] Criar uma exploração de funil "aberto" no GA4 para identificar como usuários entram em etapas intermediárias.
-   [x] Aplicar segmentos de usuários (ex: novos vs. recorrentes, desktop vs. mobile, canal de aquisição) à exploração de funil para análises detalhadas.
-   [x] Analisar o "tempo decorrido" entre as etapas do funil para identificar gargalos de processo ou UI/UX.
-   [x] Utilizar o relatório de "Caminhos de Conversão" do GA4 (em Publicidade > Atribuição) para entender a contribuição multicanal em cada etapa do funil.
-   [x] Configurar alertas personalizados no GA4 para grandes quedas na taxa de conversão do funil ou aumentos de drop-off.
-   [x] Comparar o desempenho do funil ao longo do tempo (ex: semana a semana, mês a mês) para identificar tendências e impactos de otimizações.
-   [x] Identificar as páginas de saída mais frequentes em cada etapa de drop-off para direcionar investigações de UX.

---

## Métricas de Referência

| Métrica                               | Benchmark (E-commerce) | Meta (E-commerce) |
|---------------------------------------|------------------------|-------------------|
| Taxa de Conversão (Visita > Compra)   | 1% - 3%                | 3% - 5%           |
| Drop-off (Visualização Produto > Add Carrinho) | 60% - 75%              | < 50%             |
| Drop-off (Add Carrinho > Início Checkout) | 40% - 55%              | < 35%             |
| Drop-off (Início Checkout > Compra)   | 20% - 35%              | < 15%             |
| Receita por Usuário (RPU)             | Varia muito por setor  | +20% (YoY)        |
| Tempo Médio no Funil (B2B Lead > Cliente) | 30 - 90 dias           | < 60 dias         |

---

## Erros Comuns

1.  **Eventos GA4 Mal Configurados ou Inconsistentes**: Definir etapas do funil com eventos genéricos (ex