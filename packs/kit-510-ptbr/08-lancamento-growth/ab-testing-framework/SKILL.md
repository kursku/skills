---
name: ab-testing-framework
description: "Ab Testing Framework — Skill especializada para projetar, executar e analisar experimentos A/B complexos para otimização de produtos e growth."
license: MIT
metadata:
  version: 1.0.0
  author: Cafe Code AI
  category: 08-lancamento-growth
  updated: 2026-03-01
risk: safe
---

# Ab Testing Framework

Capacita o Claude a projetar, executar e analisar experimentos A/B complexos para otimização de produtos e growth, garantindo decisões baseadas em dados robustos e impactantes.

---

## Keywords

Teste A/B, Teste Multivariado (MVT), Otimização de Conversão (CRO), Hipótese de Experimento, Variância, Nível de Significância (p-valor), Poder Estatístico, Tamanho da Amostra, Mínimo Efeito Detectável (MED), Janela de Observação, Segmentação de Usuários, Métricas de Guarda, Backtesting, Personalização Dinâmica.

---

## Quick Start

1.  **Formule uma Hipótese Específica**: Defina o que será testado, o resultado esperado e o porquê. Ex: "Ao mudar a cor do botão 'Adicionar ao Carrinho' de cinza para laranja na página de produto, esperamos um aumento de 15% nas adições ao carrinho porque a cor laranja cria maior contraste e urgência visual."
2.  **Calcule o Tamanho da Amostra e Duração**: Utilize uma calculadora de A/B testing (e.g., Optimizely, VWO) para determinar quantos usuários são necessários por variante, considerando a taxa de conversão atual (baseline), o Mínimo Efeito Detectável (MED), poder estatístico (80%) e significância (95%). Ex: Para uma baseline de 5% e MED de 10%, são necessários ~4.000 usuários por variante.
3.  **Implemente o Experimento**: Utilize uma plataforma de A/B testing (e.g., Google Optimize, VWO, Optimizely, LaunchDarkly) para criar as variantes e direcionar o tráfego de forma aleatória e balanceada (e.g., 50/50 ou 33/33/33).
4.  **Monitore Métricas de Guarda**: Acompanhe métricas cruciais que não são o foco principal, mas podem ser impactadas negativamente. Ex: Se o teste foca em cliques, monitore a taxa de churn ou tempo na página para garantir que o aumento de cliques não vem à custa da experiência geral.
5.  **Analise e Tome Decisão**: Após a duração pré-calculada, avalie os resultados estatísticos (p-valor, intervalo de confiança) para determinar se a variante de teste superou o controle de forma significativa. Não finalize o teste prematuramente.

---

## Core Workflows

### Workflow 1: Otimizando a Taxa de Ativação em um Produto SaaS

Este workflow detalha o processo para melhorar a taxa de ativação de novos usuários em um produto SaaS, focando na primeira experiência.

1.  **Identificação da Oportunidade**:
    *   **Análise de Funil**: Observar que 45% dos usuários que completam o cadastro não realizam a "primeira ação de valor" (ex: criar o primeiro projeto, convidar um colega) nos primeiros 7 dias. A taxa de ativação atual é de 30%.
    *   **Pesquisa Qualitativa**: Entrevistas com usuários recém-cadastrados revelam confusão sobre o "próximo passo" após o login.
2.  **Formulação da Hipótese**:
    *   **Hipótese**: "Para *novos usuários cadastrados*, se *implementarmos um tour guiado interativo (tooltip series) nos 3 principais recursos do produto na primeira sessão*, então *esperamos um aumento de 20% na taxa de ativação (primeiro projeto criado em 7 dias)* porque *isso reduzirá a barreira inicial e direcionará o usuário para a ação de valor principal*."
3.  **Definição de Métricas**:
    *   **Métrica Primária**: Taxa de ativação (percentual de novos usuários que criam o primeiro projeto em 7 dias). Baseline: 30%.
    *   **Métricas Secundárias**: Taxa de conclusão do tour guiado, tempo para a primeira ação, churn rate em 30 dias.
4.  **Cálculo do Tamanho da Amostra e Duração**:
    *   **Baseline**: 30%
    *   **Mínimo Efeito Detectável (MED)**: 20% de aumento relativo, ou seja, de 30% para 36% (+6 pontos percentuais).
    *   **Poder Estatístico**: 80%
    *   **Nível de Significância**: 95% (p < 0.05)
    *   **Cálculo**: Usando uma calculadora de A/B, seriam necessários aproximadamente 2.500 usuários por variante.
    *   **Duração**: Se o produto recebe 500 novos usuários por dia, o teste deve rodar por 10 dias (5.000 usuários / 500 usuários/dia = 10 dias) para garantir que cada variante tenha a amostra necessária. Adicionar alguns dias para capturar o ciclo completo de 7 dias da métrica de ativação. Duração total: 14 dias.
5.  **Implementação do Experimento**:
    *   **Ferramenta**: Usar VWO ou Optimizely para criar duas variantes:
        *   **Controle (A)**: Experiência atual de onboarding.
        *   **Teste (B)**: Experiência com o tour guiado.
    *   **Distribuição**: Dividir 50% do tráfego de novos usuários para A e 50% para B.
    *   **QA**: Testar rigorosamente a implementação para garantir que o tour guiado funcione corretamente e não haja vieses técnicos.
6.  **Análise e Decisão**:
    *   **Monitoramento**: Acompanhar as métricas primárias e secundárias diariamente, mas *sem tomar decisões prematuras*.
    *   **Após 14 dias**: Coletar e analisar os dados.
        *   **Resultados**:
            *   Controle (A): Taxa de ativação de 30.5% (n=2480)
            *   Teste (B): Taxa de ativação de 37.2% (n=2510)
            *   Delta: +6.7 pontos percentuais (+22% relativo)
            *   p-valor: 0.008.
            *   Intervalo de Confiança (95%): [4.1%, 9.3%] para o aumento absoluto.
    *   **Decisão**: Com p-valor < 0.05, a diferença é estatisticamente significativa. A variante B será implementada permanentemente.

### Workflow 2: Otimizando o Funil de Checkout para E-commerce

Este workflow foca em reduzir o abandono do carrinho e aumentar a taxa de conversão final em um e-commerce.

1.  **Identificação da Oportunidade**:
    *   **Análise de Funil**: O passo "Informações de Envio" no checkout tem uma taxa de abandono de 25%, a mais alta do funil após o carrinho. A taxa de conversão geral do checkout (do carrinho à compra) é de 40%.
    *   **Feedback de Usuários**: Clientes relatam que a quantidade de campos e a necessidade de criar uma conta são frustrantes.
2.  **Formulação da Hipótese**:
    *   **Hipótese**: "Para *usuários na etapa 'Informações de Envio' do checkout*, se *oferecermos a opção de 'Checkout como Convidado' e simplificarmos o formulário de endereço removendo campos opcionais (ex: complemento)*, então *esperamos um aumento de 10% na taxa de conclusão do checkout* porque *isso reduzirá o atrito e a exigência de dados desnecessários*."
3.  **Definição de Métricas**:
    *   **Métrica Primária**: Taxa de conclusão do checkout (percentual de usuários que chegam à página de confirmação de compra após iniciar o checkout). Baseline: 40%.
    *   **Métricas Secundárias**: Taxa de criação de conta (para monitorar se o checkout como convidado impacta negativamente), Valor Médio do Pedido (AOV), Churn rate de clientes.
4.  **Cálculo do Tamanho da Amostra e Duração**:
    *   **Baseline**: 40%
    *   **Mínimo Efeito Detectável (MED)**: 10% de aumento relativo, ou seja, de 40% para 44% (+4 pontos percentuais).
    *   **Poder Estatístico**: 80%
    *   **Nível de Significância**: 95% (p < 0.05)
    *   **Cálculo**: Aproximadamente 5.000 usuários por variante que iniciam o checkout.
    *   **Duração**: Se o e-commerce tem 1.000 inícios de checkout por dia, o teste deve rodar por 10 dias (10.000 / 1.000 = 10 dias). Duração total: 10-14 dias para cobrir um ciclo de vendas semanal.
5.  **Implementação do Experimento**:
    *   **Ferramenta**: Utilizar LaunchDarkly ou Optimizely para gerenciar a feature flag e dividir o tráfego.
    *   **Variantes**:
        *   **Controle (A)**: Checkout atual (obrigatório criar conta, formulário completo).
        *   **Teste (B)**: Checkout como convidado e formulário simplificado.
    *   **Distribuição**: 50% para A, 50% para B.
    *   **QA**: Testar o fluxo completo de compra em ambas as variantes, incluindo diferentes métodos de pagamento e dispositivos.
6.  **Análise e Decisão**:
    *   **Monitoramento**: Acompanhar abandono de carrinho, taxa de conclusão e AOV.
    *   **Após 14 dias**:
        *   **Resultados**:
            *   Controle (A): Taxa de conclusão de 40.2% (n=4950)
            *   Teste (B): Taxa de conclusão de 46.5% (n=5050)
            *   Delta: +6.3 pontos percentuais (+15.7% relativo)
            *   p-valor: 0.001.
            *   Intervalo de Confiança (95%): [3.8%, 8.8%] para o aumento absoluto.
            *   Métrica Secundária (Criação de Conta): A taxa de criação de conta caiu em 12% na variante B, mas o AOV permaneceu estável.
    *   **Decisão**: A variante B é estatisticamente superior na taxa de conclusão do checkout e o impacto na criação de conta é aceitável, dado o ganho na conversão. Implementar a variante B.

---

## Templates

### Template de Hipótese de Experimento A/B

```
Para [USUÁRIOS/SEGMENTO ESPECÍFICO], se [EXECUTAMOS ESTA ALTERAÇÃO/VARIANTE], então [ESPERAMOS ESTE RESULTADO MENSURÁVEL] porque [RAZÃO/INSIGHT/DADO QUE JUSTIFICA A ALTERAÇÃO].

Exemplo Preenchido:
Para *novos visitantes da página de checkout mobile*, se *removemos o campo 'CPF' como obrigatório e o tornamos opcional*, então *esperamos um aumento de 7% na taxa de conclusão do checkout mobile* porque *a exigência de dados pessoais no primeiro contato gera atrito e desconfiança*.
```

### Template de Relatório de Experimento A/B (Resumo Executivo)

```
Título do Experimento: Otimização da Página de Preços para Planos Enterprise
ID do Experimento: AB-2024-Q1-003
Período de Execução: 05/02/2024 - 19/02/2024
Responsável: Equipe de Growth
Status: Concluído - Vitória

Hipótese: Alterar a hierarquia visual dos planos na página de preços, destacando o plano "Enterprise" com um selo "Mais Popular" e um botão CTA maior, aumentará as solicitações de demo para este plano em 12%.

Variantes Testadas:
- Controle (A): Página de preços padrão.
- Teste (B): Página de preços com destaque para o plano Enterprise (selo "Mais Popular", CTA maior).

Métrica Primária: Taxa de Cliques no Botão "Solicitar Demo" do Plano Enterprise.
Baseline (Controle A): 2.8%
Resultado (Teste B): 3.5%
Delta (B vs A): +0.7 pontos percentuais (equivalente a +25% relativo)
Significância Estatística (p-valor): 0.003 (Estatisticamente Significativo, p < 0.05)
Intervalo de Confiança (95%): [0.4%, 1.0%] no aumento absoluto da taxa de cliques.

Métricas Secundárias:
- Taxa de Cliques nos outros planos: Redução de 5% no plano "Pro", estável no "Basic".
- Taxa de Conversão para Sales Qualified Leads (SQL): Aumento de 18% para o plano Enterprise.

Tamanho da Amostra por Variante: 8.500 visitantes únicos.
Duração Necessária (calculada): 12 dias.
Duração Real: 14 dias.

Decisão: Implementar a variante B.
Justificativa: A variante B demonstrou um aumento estatisticamente significativo na métrica primária e um impacto positivo na métrica secundária de SQLs, validando a hipótese.

Próximos Passos:
1. Implementar a variante B permanentemente na página de preços.
2. Analisar o impacto no ciclo de vendas e fechamento de negócios para os leads Enterprise gerados.
3. Considerar um novo teste para otimizar o formulário de solicitação de demo.
```

---

## Checklist

- [x] Hipótese clara, mensurável e testável formulada?
- [x] Métrica primária e secundária (guardrail metrics) definidas e rastreáveis?
- [x] Baseline da métrica primária coletada e validada?
- [x] Mínimo Efeito Detectável (MED) definido para o teste?
- [x] Tamanho da amostra calculado com poder estatístico (mínimo 80%) e nível de significância (95%) adequados?
- [x] Duração do teste (janela de observação) estabelecida para cobrir ciclos completos de usuários e evitar sazonalidade?
- [x] Variantes implementadas corretamente na ferramenta de A/B testing?
- [x] QA (Quality Assurance) completo realizado nas variantes (funcionalidade, UX, rastreamento) para evitar vieses?
- [x] Segmentação de usuários para o teste definida e isolada de outros experimentos em andamento?
- [x] Plano de análise pós-teste e critérios de decisão pré-definidos?
- [x] Plano de contingência para reverter o teste em caso de impactos negativos severos nas métricas de guarda?

---

## Métricas de Referência

| Métrica                      | Benchmark (Indústria)        | Meta (Exemplo)               |
|------------------------------|------------------------------|------------------------------|
| Taxa de Conversão (E-commerce) | 1.5% - 3.0%                  | 3.5%                         |
| Taxa de Cliques (CTA)        | 5% - 15%                     | 18%                          |
| Activation Rate (SaaS)       | 20% - 40% (primeira ação)    | 45%                          |
| Retention Rate (30 dias)     | 25% - 35% (produtos digitais) | 40%                          |
| p-valor (Significância)      | < 0.05                       | < 0.01 (para alta confiança) |
| Poder Estatístico            | 80%                          | 90%                          |
| Taxa de Abandono (Checkout)  | 60% - 75%                    | 50%                          |

---

## Erros Comuns

1.  **Finalizar o Teste Prematuramente (Peeking)**: Interromper um experimento assim que a significância estatística é atingida, ignorando a duração calculada.
    *   **Como evitar**: Defina a duração do teste com base no cálculo do tamanho da amostra e no ciclo de negócios, e adira a ela. Acompanhe os resultados, mas não tome decisões antes do tempo, pois isso aumenta a chance de falsos positivos (erro Tipo I). Ex: Um teste projetado para 14 dias que é parado no dia 5 porque "já deu significativo" pode estar apenas pegando uma flutuação aleatória.
2.  **Testar Múltiplas Variáveis em um Único Experimento A/B**: Alterar vários elementos (ex: cor do botão, texto, imagem) entre o controle e a variante de teste.
    *   **Como evitar**: Se deseja testar o impacto de múltiplos elementos combinados, utilize um Teste Multivariado (MVT) que analisa a interação entre as variáveis. Para testes A/B simples, altere apenas uma variável por vez ou crie variantes distintas com combinações específicas, mas saiba que atribuir o sucesso a um elemento específico será difícil. Ex: Em vez de mudar cor E texto do CTA, faça um teste para cor e, se significativo, um segundo teste para texto.
3.  **Não Considerar Efeitos de Rede ou Sazonalidade**: Lançar um teste que não abrange um ciclo de negócios completo (ex: apenas dias de semana, ou durante um feriado atípico).
    *   **Como evitar**: Calcule a duração do teste para incluir pelo menos um ciclo semanal completo (7 dias) e, idealmente, múltiplos ciclos se o comportamento do usuário variar significativamente por dia da semana ou mês. Para produtos com alta dependência de rede (ex: plataformas sociais), a interação entre usuários pode enviesar os resultados se a divisão for por usuário. Considere "Switchback Testing" ou "Cluster-based Testing" para mitigar esses efeitos em certos cenários.

---

## Dicas Avançadas

1.  **Utilize Guardrail Metrics para Mitigar Riscos**: Além da métrica primária e secundária da hipótese, monitore métricas de saúde do produto (ex: taxa de churn, tempo na página, LTV) que não são o foco do teste, mas que poderiam ser negativamente impactadas. Isso garante que a otimização de uma métrica não prejudique a saúde geral do negócio. Ex: Um teste que aumenta a taxa de cliques no CTA pode estar levando a cliques de baixa qualidade, resultando em maior abandono posteriormente.
2.  **Análise de Segmentos Pós-Teste (Subgroup Analysis)**: Mesmo que o resultado geral de um teste não seja estatisticamente significativo, analise o desempenho das variantes em segmentos específicos da sua base de usuários (ex: usuários mobile vs desktop, novos vs recorrentes, diferentes demografias). Pode ser que a variante tenha um impacto significativo para um subgrupo, revelando insights valiosos para personalização. Ex: A variante B pode não ter melhorado a conversão geral, mas aumentou em 20% a conversão para usuários de iOS.
3.  **Implemente um Framework de Orquestração de Testes**: Mantenha um registro centralizado de todos os testes A/B ativos e planejados. Isso evita a sobreposição de testes na mesma página ou funil, que pode levar a resultados conflitantes ou viesados. Ferramentas como LaunchDarkly ou sistemas internos de gerenciamento de experimentos são cruciações para gerenciar dependências e prioridades.
4.  **Teste de Hipóteses Nulas (B/A Testing)**: Antes de lançar um teste A/B com uma nova variante, execute um teste A/A (ou B/A, onde B é apenas uma cópia de A) para validar sua infraestrutura de testes. Isso confirma que seu sistema de A/B testing está dividindo o tráfego aleatoriamente e coletando dados de forma imparcial, sem vieses técnicos inerentes. Se o teste A/A mostrar uma diferença significativa, há um problema na configuração.
5.  **Considere Testes Baseados em Valor (Value-based Testing)**: Em vez de focar apenas em taxas de conversão ou cliques, priorize testes que impactam diretamente o valor gerado para o negócio (ex: Receita Média por Usuário (ARPU), Lifetime Value (LTV)). Embora mais complexos e demorados, esses testes fornecem insights mais profundos sobre o impacto financeiro real das suas otimizações. Ex: Um teste que aumenta ligeiramente o preço de um plano pode reduzir a taxa de conversão, mas se o ARPU por cliente convertido aumentar significativamente, o teste pode ser um sucesso.