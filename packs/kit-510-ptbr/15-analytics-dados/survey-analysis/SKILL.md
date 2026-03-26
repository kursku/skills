---
name: survey-analysis
description: "Survey Analysis — Skill especializada para survey analysis"
license: MIT
metadata:
  version: 1.0.0
  author: Cafe Code AI
  category: 15-analytics-dados
  updated: 2026-03-01
risk: safe
---

# Survey Analysis

Esta skill capacita o Claude a integrar e analisar dados de pesquisas com métricas do Google Analytics 4, correlacionando feedback qualitativo com comportamento quantitativo do usuário para otimizar jornadas e decisões de produto.

---

## Keywords

NPS (Net Promoter Score), CSAT (Customer Satisfaction Score), CES (Customer Effort Score), Google Analytics 4 (GA4), Dimensões Personalizadas GA4, Métricas Personalizadas GA4, Eventos GA4, Explorações GA4, Funil de Conversão, Atribuição de Marketing, Feedback de Usuário, Pesquisa de Abandono, Segmentação de Audiência, Análise Pós-Compra.

---

## Quick Start

1.  **Configurar GTM para Captura de Feedback**: Implemente tags no Google Tag Manager para disparar eventos GA4 e coletar dados de pesquisas (e.g., envio de formulário de NPS) como eventos e parâmetros, mapeando o score para um parâmetro como `nps_score`.
2.  **Criar Dimensões Personalizadas no GA4**: Registre os parâmetros de pesquisa (e.g., `nps_score`, `reason_for_churn`) como dimensões personalizadas de escopo de usuário ou evento no GA4 para que os dados sejam visíveis nos relatórios.
3.  **Segmentar Usuários por Feedback**: Crie segmentos de audiência no GA4 (e.g., "Promotores NPS", "Detratores NPS") usando as dimensões personalizadas para analisar o comportamento específico de cada grupo.
4.  **Construir Relatório de Exploração de Funil**: Utilize a ferramenta de "Explorações" no GA4 para construir um funil de conversão e aplicar os segmentos de feedback, identificando onde promotores e detratores divergem na jornada.
5.  **Correlacionar com Fontes de Atribuição**: Compare os segmentos de feedback com os dados de atribuição no GA4 para entender quais canais de marketing atraem usuários com maior satisfação ou menor intenção de churn.

---

## Core Workflows

### Workflow 1: Análise de Impacto do NPS na Retenção e Engajamento via GA4

Este workflow detalha a integração de dados de NPS com o GA4 para identificar padrões comportamentais de promotores e detratores e otimizar estratégias de retenção.

1.  **Configuração da Pesquisa NPS e Coleta de Dados**:
    *   **Ferramenta**: Utilize uma ferramenta de pesquisa como Typeform, Qualtrics, SurveyMonkey ou uma solução in-house.
    *   **Disparo**: Configure a pesquisa para ser disparada 7 dias após a primeira compra ou 30 dias após o cadastro, dependendo do ciclo de vida do produto.
    *   **Integração GTM/GA4**:
        *   Ao submeter a pesquisa, envie um evento para o GA4 via Google Tag Manager (GTM).
        *   Exemplo de configuração no GTM:
            *   **Tipo de Tag**: `Google Analytics: Evento GA4`
            *   **Nome do Evento**: `nps_survey_submit`
            *   **Parâmetros do Evento**:
                *   `nps_score`: `{{NPS_Score_Variable}}` (variável do GTM que captura o valor do NPS, e.g., de um campo de formulário)
                *   `user_id`: `{{GA4_User_ID}}` (se disponível para matching)
                *   `feedback_type`: `NPS`
        *   No GA4, registre `nps_score` como uma **Dimensão Personalizada** de `Escopo do evento` (Nome: `nps_score`, Nome do parâmetro do evento: `nps_score`).

2.  **Criação de Segmentos de Audiência no GA4**:
    *   Acesse `Administrador` > `Visualização de dados` > `Audiências` no GA4.
    *   Crie três novas audiências baseadas na dimensão personalizada `nps_score`:
        *   **Audiência 1: Promotores NPS**: `nps_score` é MAIOR OU IGUAL A `9`.
        *   **Audiência 2: Passivos NPS**: `nps_score` é MAIOR OU IGUAL A `7` E MENOR OU IGUAL A `8`.
        *   **Audiência 3: Detratores NPS**: `nps_score` é MENOR OU IGUAL A `6`.
    *   Estas audiências permitirão segmentar relatórios e explorações.

3.  **Análise Comportamental com "Explorações" (GA4)**:
    *   Vá para `Explorar` no menu lateral esquerdo do GA4.
    *   Crie uma nova `Exploração de Funil` ou `Exploração de Caminho`.
    *   **Exploração de Funil**:
        *   Defina os passos do funil (e.g., `page_view /carrinho`, `add_to_cart`, `begin_checkout`, `purchase`).
        *   Aplique os segmentos "Promotores NPS", "Passivos NPS" e "Detratores NPS" ao funil.
        *   **Insight Esperado**: Observar se os Promotores têm uma taxa de conclusão do funil significativamente maior que os Detratores, ou se os Detratores abandonam em etapas específicas (e.g., `checkout`).
        *   **Exemplo**: Promotores têm 85% de conclusão de compra, Detratores apenas 30%, com a maior queda na etapa de `pagamento`.

4.  **Correlação com Métricas de Engajamento e Retenção**:
    *   Crie uma `Exploração de Tabela` ou `Formato livre`.
    *   **Linhas**: `Audiência` (Promotores, Passivos, Detratores).
    *   **Colunas/Métricas**: `Sessões por usuário`, `Tempo médio de engajamento`, `Taxa de rejeição`, `Receita por usuário`, `Eventos de engajamento por usuário`.
    *   **Insight Esperado**: Promotores tendem a ter maior `Sessões por usuário`, `Tempo médio de engajamento` e `Receita por usuário` em comparação com Detratores.
    *   **Exemplo**: Promotores gastam em média R$500/mês, interagem com 15 páginas/sessão. Detratores gastam R$100/mês, interagem com 3 páginas/sessão.

5.  **Análise de Atribuição (Relatórios de Publicidade)**:
    *   Acesse `Publicidade` > `Atribuição` > `Caminhos de conversão` no GA4.
    *   Filtre os relatórios pelas conversões desejadas (e.g., `purchase`).
    *   Aplique a comparação de segmentos (Promotores vs. Detratores).
    *   **Insight Esperado**: Identificar se determinados canais de marketing (e.g., Pesquisa Paga, Mídias Sociais) atraem proporcionalmente mais Promotores ou Detratores. Isso pode informar o ajuste do investimento em canais para atrair usuários de maior valor.
    *   **Exemplo**: `Display Ads` trazem muitos Detratores, enquanto `Email Marketing` e `Pesquisa Orgânica` são fortes em Promotores.

### Workflow 2: Otimização de Funis com Insights de Pesquisas de Abandono (Exit Surveys)

Este workflow foca em utilizar dados de pesquisas de saída para entender as razões do abandono e otimizar funis de conversão no GA4.

1.  **Implementação da Pesquisa de Abandono**:
    *   **Disparo**: Configure um pop-up ou modal de pesquisa de saída (exit-intent survey) para aparecer quando um usuário demonstra intenção de sair de uma página crítica do funil (e.g., carrinho de compras, checkout, página de inscrição).
    *   **Perguntas-chave**: "Qual o principal motivo para você não concluir sua ação hoje?", com opções como "Preço alto", "Processo complicado", "Falta de informação", "Comparando preços", "Problema técnico". E um campo de texto livre.
    *   **GTM/GA4**:
        *   Ao submeter a pesquisa, envie um evento GA4, e.g., `exit_survey_submit`.
        *   Inclua parâmetros como `reason_for_exit` (capturando a opção selecionada) e `page_abandoned` (URL da página onde a pesquisa foi preenchida).
        *   No GA4, registre `reason_for_exit` e `page_abandoned` como **Dimensões Personalizadas** de `Escopo do evento`.

2.  **Identificação de Pontos de Abandono no GA4**:
    *   No GA4, vá para `Explorar` e crie uma `Exploração de Funil`.
    *   **Funil**: Mapeie o funil de conversão relevante (e.g., `Visualização Produto` -> `Adicionar ao Carrinho` -> `Iniciar Checkout` -> `Comprar`).
    *   Identifique as etapas com maior `taxa de abandono`.
    *   **Exemplo**: A maior queda ocorre entre `Iniciar Checkout` e `Adicionar Informações de Envio`, com 60% de abandono.

3.  **Correlação de Dados da Pesquisa com Abandono do Funil**:
    *   Crie uma `Exploração de Tabela` ou `Formato livre`.
    *   **Linhas**: `reason_for_exit` (dimensão personalizada da pesquisa).
    *   **Colunas/Métricas**: `Taxa de abandono` (para a etapa específica do funil), `Usuários`, `Sessões`.
    *   **Filtro**: `page_abandoned` contém `checkout` (para focar na página de checkout).
    *   **Insight Esperado**: Identificar quais razões de saída estão mais associadas aos usuários que abandonam em etapas críticas do funil.
    *   **Exemplo**: Para a etapa `Iniciar Checkout`, 40% dos abandonos são atribuídos a "Preço alto" e 30% a "Processo complicado".

4.  **Priorização de Otimizações**:
    *   Com base na correlação, priorize as otimizações. Se "Processo complicado" é a principal razão para abandono no checkout, investigue a complexidade dos formulários, número de campos, clareza das instruções.
    *   Se "Preço alto" for dominante, considere opções de frete, descontos ou comparativos de valor.
    *   **Exemplo**: Ação prioritária é simplificar o formulário de `Adicionar Informações de Envio` e adicionar um indicador de progresso no checkout.

5.  **Monitoramento Pós-Otimização no GA4**:
    *   Após implementar as mudanças (e.g., simplificação do formulário de checkout), monitore a `taxa de abandono` daquela etapa específica do funil no GA4.
    *   Utilize anotações no GA4 ou Google Sheets para registrar a data da implementação.
    *   **Métricas de Sucesso**: Diminuição da `taxa de abandono` na etapa `Adicionar Informações de Envio`, aumento da `taxa de conversão` do funil geral.
    *   **Exemplo**: A taxa de abandono na etapa `Adicionar Informações de Envio` caiu de 60% para 45% após a otimização.

---

## Templates

### Script de Pesquisa de Satisfação Pós-Compra (CSAT)

```markdown
# Pesquisa de Satisfação Pós-Compra

Olá [Nome do Cliente],

Esperamos que esteja satisfeito com sua recente compra em nossa loja! Seu feedback é muito importante para continuarmos melhorando. Levará apenas 1 minuto.

1.  **No geral, qual o seu nível de satisfação com a sua experiência de compra em nosso site hoje?**
    *   [ ] Muito Insatisfeito (1)
    *   [ ] Insatisfeito (2)
    *   [ ] Neutro (3)
    *   [ ] Satisfeito (4)
    *   [ ] Muito Satisfeito (5)

2.  **Qual foi o principal fator que influenciou sua resposta acima?**
    *   [ ] Facilidade de navegação no site
    *   [ ] Qualidade dos produtos
    *   [ ] Preço e custo-benefício
    *   [ ] Velocidade e custo do frete
    *   [ ] Atendimento ao cliente
    *   [ ] Opções de pagamento
    *   [ ] Outro (por favor, especifique): [Campo de texto livre]

3.  **O que poderíamos ter feito para tornar sua experiência ainda melhor?**
    [Campo de texto livre para sugestões]

4.  **Você recomendaria nossa loja a um amigo ou colega?**
    *   [ ] Sim
    *   [ ] Não
    *   [ ] Talvez

Agradecemos sinceramente seu tempo e feedback!

[Link para Política de Privacidade]
```

### Plano de Ação Baseado em Insight de Survey e GA4

```markdown
# Plano de Ação - Otimização de Funil de Checkout

**Data:** 2024-10-27
**Responsável:** Equipe de Produto e Marketing Digital

**Insight da Pesquisa:** 35% dos usuários que abandonaram o checkout mencionaram "Processo de pagamento complicado" ou "Muitos campos para preencher" nas pesquisas de saída (Exit Survey).

**Dados GA4 Correlacionados:**
*   **Relatório:** Exploração de Funil - Funil de Checkout.
*   **Etapa Crítica:** "Adicionar Informações de Envio e Pagamento" tem uma taxa de abandono de 55%.
*   **Segmento Detratores:** Usuários classificados como "Detratores NPS" têm uma taxa de abandono de 70% nesta etapa, comparado a 30% dos "Promotores NPS".
*   **Dispositivo:** Abandono é 15% maior em dispositivos móveis nesta etapa.

**Causa Provável:** Formulário de checkout longo e não otimizado para mobile, exigindo muitas informações desnecessárias ou com campos confusos.

**Ações Propostas:**

1.  **Simplificar Formulário de Envio:**
    *   **Ação:** Reduzir o número de campos obrigatórios no formulário de envio. Consolidar campos (e.g., "Endereço Linha 1" e "Linha 2" em um único campo inteligente).
    *   **Responsável:** Equipe de Desenvolvimento
    *   **Prazo:** 2024-11-15
    *   **Métrica de Sucesso (GA4):** Redução da taxa de abandono na etapa "Adicionar Informações de Envio" em 10%. Aumento da Taxa de Conversão de Checkout em 5%.

2.  **Otimização Mobile do Checkout:**
    *   **Ação:** Implementar design responsivo e teclados otimizados para cada tipo de campo no checkout mobile (e.g., teclado numérico para telefone/CEP).
    *   **Responsável:** Equipe de UI/UX e Desenvolvimento
    *   **Prazo:** 2024-11-30
    *   **Métrica de Sucesso (GA4):** Redução da taxa de abandono mobile na etapa "Adicionar Informações de Envio" em 12%.

3.  **Adicionar Indicador de Progresso:**
    *   **Ação:** Incluir um indicador visual de progresso (e.g., "Passo 1 de 3") no topo do formulário de checkout para reduzir a percepção de complexidade.
    *   **Responsável:** Equipe de UI/UX e Desenvolvimento
    *   **Prazo:** 2024-11-20
    *   **Métrica de Sucesso (GA4):** Aumento do tempo médio de engajamento na página de checkout e redução da taxa de rejeição.

**Monitoramento:** Acompanhamento semanal das métricas de funil no GA4, com relatórios de Exploração de Funil segmentados por dispositivo e audiência (NPS).

**Próximos Passos:** Realizar testes A/B nas alterações implementadas para validar a eficácia.
```

---

## Checklist

- [x] Dados de pesquisa (NPS, CSAT, Exit Survey) configurados para serem enviados como eventos e parâmetros para o GA4 via GTM.
- [x] Dimensões personalizadas criadas no GA4 para cada parâmetro relevante da pesquisa (e.g., `nps_score`, `reason_for_exit`).
- [x] Audiências de GA4 segmentadas com base nas respostas da pesquisa (e.g., Promotores, Detratores, Usuários que citaram "preço alto").
- [x] Relatórios de "Explorações" (Funil, Caminho, Formato Livre) criados no GA4 para analisar o comportamento de cada segmento de feedback.
- [x] Métricas de engajamento e retenção (e.g., sessões por usuário, tempo médio de engajamento, receita por usuário) comparadas entre os segmentos de feedback.
- [x] Correlação entre as razões de abandono (pesquisa) e os pontos de queda no funil de conversão (GA4) identificada.
- [x] Dados de atribuição no GA4 analisados para entender quais canais atraem usuários com diferentes perfis de feedback.
- [x] Plano de ação detalhado com base nos insights de pesquisa e GA4, incluindo métricas de sucesso monitoráveis no GA4.
- [x] Implementação de testes A/B para validar otimizações derivadas dos insights da pesquisa.
- [x] Monitoramento contínuo das métricas-chave no GA4 pós-implementação das otimizações.

---

## Métricas de Referência

| Métrica                      | Benchmark (Varejo Online) | Meta (Otimizado)          |
|------------------------------|---------------------------|---------------------------|
| NPS (Net Promoter Score)     | 10-30                     | 40-60+                    |
| CSAT (Customer Satisfaction) | 75-85% (4-5 estrelas)     | 90%+ (4-5 estrelas)       |
| CES (Customer Effort Score)  | 4.0-5.0 (escala 1-7)      | 6.0-7.0 (escala 1-7)      |
| Taxa de Abandono de Carrinho | 60-75%                    | 45-55%                    |
| Taxa de Conclusão de Checkout| 25-40%                    | 50-60%+                   |
| Receita por Usuário (Promotor)| 2x - 3x Detrator          | 3.5x+ Detrator            |

---

## Erros Comuns

1.  **Não Integrar Dados Qualitativos com Quantitativos**: **Erro**: Coletar dados de pesquisa (qualitativos) e analisar métricas do GA4 (quantitativos) de forma isolada, sem correlação. Isso impede a compreensão holística do "porquê" por trás do "o quê". **Como evitar**: Sempre configure dimensões personalizadas no GA4 para os dados de pesquisa e crie segmentos. Utilize as ferramentas de "Explorações" do GA4 para cruzar esses dados, por exemplo, analisando a taxa de rejeição de Detratores NPS em páginas específicas.
2.  **Perguntas de Pesquisa Ambíguas ou Tendenciosas**: **Erro**: Fazer perguntas como "Você não gostou do nosso novo recurso, não é?" que induzem a uma resposta específica ou usar termos técnicos que os usuários não entendem. **Como evitar**: Utilize uma linguagem clara e neutra. Teste suas pesquisas com um pequeno grupo antes do lançamento total. Por exemplo, em vez de "Nosso chatbot melhorou sua experiência?", pergunte "Qual foi sua experiência com nosso chatbot?".
3.  **Ignorar o Contexto do Dispositivo/Canal na Análise**: **Erro**: Analisar o feedback de pesquisa de forma agregada, sem considerar se o usuário estava no desktop, mobile, ou qual canal de marketing o trouxe. Isso pode mascarar problemas específicos de experiência. **Como evitar**: Sempre que possível, capture o `device_category` e a `source/medium` do GA4 junto com o feedback da pesquisa. Ao analisar no GA4, segmente por essas dimensões para identificar se, por exemplo, "Processo complicado" é um problema predominante apenas para usuários mobile vindos de campanhas de social media.

---

## Dicas Avançadas

1.  **Análise de Sentimento de Respostas Abertas**: Implemente ferramentas de processamento de linguagem natural (NLP) para analisar automaticamente as respostas de texto livre das pesquisas. Isso permite identificar rapidamente temas emergentes, o tom emocional (positivo, negativo, neutro) e a intensidade do sentimento, priorizando os problemas mais críticos ou os elogios mais frequentes, que podem ser posteriormente validados com métricas de eventos GA4.
2.  **Modelagem Preditiva de Churn com Dados Híbridos**: Combine os scores de NPS/CSAT com eventos de comportamento do GA4 (e.g., `last_purchase_date`, `time_since_last_session`, `page_views_per_session`) em modelos de Machine Learning. Isso pode prever com maior precisão quais usuários têm alta probabilidade de churn antes mesmo de cancelarem, permitindo ações proativas de retenção.
3.  **Cross-Device User Journey com Feedback**: Utilize o User-ID no GA4 (se implementado) para rastrear a jornada de usuários através de múltiplos dispositivos. Combine isso com o feedback de pesquisa para entender se a satisfação ou insatisfação está ligada a uma experiência fragmentada ou inconsistente entre dispositivos, impactando a atribuição de marketing de longo prazo.
4.  **Segmentação Dinâmica de Audiências para Personalização**: Crie audiências GA4 avançadas que combinam dados de pesquisa (e.g., "Promotores NPS que visitaram a página X, mas não converteram") e utilize-as para campanhas de remarketing altamente personalizadas. Por exemplo, um promotor que visitou uma nova categoria de produto pode receber um e-mail com ofertas exclusivas para essa categoria, enquanto um detrator que teve problemas no checkout pode receber uma oferta de suporte ou um desconto especial para reengajamento.
5.  **Testes A/B com Base em Micro-Insights de Feedback**: Em vez de apenas testar grandes mudanças, use feedback de pesquisa para gerar hipóteses para micro-testes. Se 5% dos usuários mencionaram "dificuldade em encontrar a política de troca", crie um teste A/B para aprimorar a visibilidade desse link no rodapé ou na página do produto, e monitore o impacto na taxa de conversão do funil e no CSAT geral.