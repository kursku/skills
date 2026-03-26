---
name: social-listening
description: "Social Listening — Skill especializada para social listening"
license: MIT
metadata:
  version: 1.0.0
  author: Cafe Code AI
  category: 09-redes-sociais
  updated: 2026-03-01
risk: safe
---

# Social Listening

Esta skill capacita o Claude a executar tarefas de social listening, monitorando conversas, identificando tendências e analisando o sentimento de marca nas principais redes sociais para gerar insights acionáveis.

---

## Keywords

Monitoramento de Marca, Análise de Sentimento, Tendências Sociais, Insights do Consumidor, Gestão de Crises (Social), Benchmarking Competitivo, Influenciadores Digitais, Métricas de Engajamento, Segmentação de Audiência, Reputação Online, Volume de Menções, Alcance Potencial.

---

## Quick Start

1.  **Configurar Termos-Chave**: Implementar monitoramento em ferramentas como Brandwatch ou Sprinklr com termos-chave da marca "Café Aurora", seus produtos "Café Aurora Gourmet", "Café Aurora Espresso" e principais concorrentes como "Café do Ponto" e "3 Corações".
2.  **Agendar Relatórios de Menções**: Configurar relatórios semanais automatizados para coletar dados de volume e sentimento de menções no Instagram, Twitter/X e TikTok, buscando picos e variações significativas.
3.  **Analisar Tendências de Conteúdo**: Utilizar o painel de tópicos emergentes para identificar os 5 principais temas e formatos (ex: Reels, Shorts) que geram mais engajamento em "café especial" no YouTube e Instagram.
4.  **Identificar Oportunidades de Engajamento**: Rastrear menções de usuários que buscam recomendações de café ou receitas em comunidades do Facebook e grupos de LinkedIn para interagir proativamente.
5.  **Criar Dashboard de Performance**: Desenvolver um dashboard interativo (ex: Power BI, Google Looker Studio) que consolide métricas de menções, sentimento e share of voice, atualizado diariamente.

---

## Core Workflows

### Workflow 1: Análise de Sentimento e Reação à Crise em Tempo Real

Este workflow detalha a detecção, análise e resposta a menções negativas ou crises de reputação nas redes sociais.

1.  **Configuração de Monitoramento Pró-ativo para Crises**:
    *   **Termos de Crise**: Configurar escuta para combinações do nome da marca com palavras-chave negativas como "Café Aurora + problema", "Café Aurora + reclamação", "Café Aurora + defeito", "Café Aurora + intoxicação", "Café Aurora + fraude", incluindo erros de digitação comuns (ex: "CafeAurora").
    *   **Canais Prioritários**: Foco em Twitter/X (velocidade de propagação), Instagram (impacto visual), Reclame Aqui (via integração, se possível) e comentários em grandes portais de notícias.
    *   **Alertas Instantâneos**: Configurar alertas de email e Slack para qualquer menção que combine a marca com esses termos, ou para picos de volume de menções negativas que excedam 200% da média horária em um período de 30 minutos. Exemplo: Um aumento de 5 para 50 menções negativas sobre "Café Aurora lote estragado" em uma hora.

2.  **Detecção de Anomalias de Volume e Sentimento**:
    *   **Monitoramento Contínuo**: Acompanhar o dashboard de social listening em tempo real. Identificar rapidamente menções com alto potencial de viralização, como posts de perfis com grande número de seguidores (acima de 10k) ou menções que geram alto engajamento (mais de 50 curtidas e 10 comentários em 15 minutos).
    *   **Classificação Automática e Manual**: Utilizar a inteligência artificial da ferramenta para pré-classificar o sentimento (negativo, neutro, positivo), mas ter um analista para revisar e confirmar o sentimento das menções críticas, garantindo a precisão contextual.

3.  **Triagem e Priorização de Menções Críticas**:
    *   **Avaliar Impacto**: Classificar as menções negativas por potencial de dano (alto, médio, baixo) com base no alcance do autor, engajamento gerado e gravidade da acusação.
    *   **Ação Imediata**: Acionar a equipe de comunicação e jurídico para as menções de alto impacto. Exemplo: Um vídeo no TikTok com 500k visualizações alegando que um produto do Café Aurora causou um problema de saúde.

4.  **Elaboração e Execução de Resposta Rápida**:
    *   **Template de Resposta Inicial (Twitter/X)**: "Olá, @[Usuário]! Lamentamos muito a sua experiência com o Café Aurora. Sua satisfação é nossa prioridade. Por favor, envie-nos uma Mensagem Direta (DM) com detalhes sobre o lote do produto e seu contato para que nossa equipe possa investigar e oferecer o suporte necessário. Agradecemos sua compreensão."
    *   **Resposta Personalizada**: Adaptar a resposta conforme a especificidade da reclamação, sempre direcionando para um canal de atendimento privado (DM, e-mail, telefone) para resolver a questão em profundidade e evitar escalada pública.
    *   **Acompanhamento**: Registrar todas as interações e o status da resolução no sistema de CRM ou gestão de crises.

5.  **Monitoramento Pós-Crise e Análise de Recuperação**:
    *   **Acompanhar Sentimento**: Monitorar a evolução do sentimento e volume de menções após a resposta. O objetivo é ver uma diminuição das menções negativas e um aumento das neutras/positivas ou o fim da discussão.
    *   **Relatório Pós-Crise**: Gerar um relatório detalhado com a linha do tempo da crise, ações tomadas, impacto (número de menções, alcance, sentimento) e lições aprendidas para futuras prevenções.

### Workflow 2: Identificação de Tendências de Conteúdo e Oportunidades de Engajamento por Plataforma

Este workflow foca em usar o social listening para informar a estratégia de conteúdo, adaptando-a às nuances de cada plataforma.

1.  **Monitoramento de Hashtags e Termos-Chave por Plataforma para Tendências**:
    *   **Instagram**: Monitorar #caféespecial, #coffeeloversbrasil, #receitascomcafe. Observar os Reels e Carrosséis que viralizam, identificando estéticas, músicas e narrativas visuais.
    *   **TikTok**: Rastrear #dicasdecafe, #baristatok, #cafecriativo. Prestar atenção aos áudios em alta, formatos de desafio e tutoriais rápidos (ex: "Como fazer café cremoso em 30s").
    *   **YouTube**: Acompanhar "review de cafeteiras", "melhores grãos de café", "história do café". Analisar vídeos longos que geram mais tempo de exibição e Shorts com dicas rápidas.
    *   **LinkedIn**: Monitorar "sustentabilidade no café", "inovação na indústria cafeeira", "mercado de café". Foco em artigos de opinião, posts com dados do setor e discussões profissionais.
    *   **Twitter/X**: Seguir "notícias café", "preço do café", "debate café". Identificar discussões em tempo real, enquetes e memes que se relacionam com o tema.

2.  **Análise de Engajamento, Formatos Ideais e Algoritmos por Plataforma**:
    *   **Instagram**:
        *   **Formatos**: Reels (9:16, 15-90s, para tutoriais e entretenimento), Carrosséis (1080x1080, até 10 fotos, para storytelling e dicas), Stories (9:16, até 15s por slide, para interações rápidas).
        *   **Horários Ideais**: Terça a Quinta, 9h-11h e 18h-20h (picos de engajamento para marcas de alimentos).
        *   **Algoritmo**: Prioriza engajamento (curtidas, comentários, salvamentos, compartilhamentos), relevância do conteúdo para o usuário (interações passadas) e atualidade. Usa palavras-chave em legendas e hashtags.
    *   **TikTok**:
        *   **Formatos**: Vídeos curtos (9:16, 7-15s, para tendências e humor), com músicas e sons em alta.
        *   **Horários Ideais**: Segunda a Sexta, 13h-17h (picos de engajamento para o público jovem).
        *   **Algoritmo ("Para Você")**: Prioriza tempo de exibição, interações (curtidas, comentários, compartilhamentos), sons populares, uso de hashtags e localização. Busca introduzir novos criadores.
    *   **YouTube**:
        *   **Formatos**: Vídeos longos (16:9, >8min, para tutoriais completos e reviews), Shorts (9:16, <60s, para dicas rápidas e bastidores).
        *   **Horários Ideais**: Quarta a Sexta, 14h-16h (picos de visualização no meio da semana e antes do fim de semana).
        *   **Algoritmo**: Prioriza tempo de exibição, taxa de cliques, satisfação do espectador (curtidas, comentários, compartilhamentos) e consistência na publicação.
    *   **LinkedIn**:
        *   **Formatos**: Artigos (para conteúdo aprofundado), Posts com fotos (1.91:1 ou 1:1, para notícias e insights), Vídeos curtos (16:9, <3min, para entrevistas e comunicados).
        *   **Horários Ideais**: Terça a Quinta, 10h-12h (horários comerciais de maior atividade profissional).
        *   **Algoritmo**: Prioriza relevância para a rede profissional, engajamento (comentários, compartilhamentos), tempo de leitura de artigos e posts com "dwell time" alto.
    *   **Twitter/X**:
        *   **Formatos**: Tweets (texto + imagem 16:9 ou 1:1), Enquetes, Spaces (para discussões ao vivo).
        *   **Horários Ideais**: Segunda a Sexta, 10h-13h (picos de notícias e interação durante o horário comercial).
        *   **Algoritmo**: Prioriza novidade, engajamento rápido (curtidas, retweets), relevância do tópico e interações com perfis seguidos.

3.  **Identificação de Gaps de Conteúdo e Oportunidades**:
    *   Analisar os tópicos mais buscados ou engajadores que a marca ainda não aborda. Ex: "Como fazer café com leite vegetal" é um tema em alta no Instagram e TikTok, mas a marca ainda não tem conteúdo sobre isso.
    *   Identificar conteúdos da concorrência que performam bem e entender o porquê, buscando ângulos únicos para a marca. Ex: Um tutorial de "Latte Art" de um concorrente teve 1M de views no YouTube; a marca pode criar um com um barista renomado.

4.  **Geração de Ideias de Conteúdo com Templates Específicos**:
    *   **Instagram Reel (Tutorial Rápido)**: "3 Dicas Essenciais para um Café Coado Perfeito: Moagem Média, Água a 92°C, Proporção 1:10."
    *   **TikTok (Desafio de Engajamento)**: "Desafio #MeuRitualComAurora: Mostre seu momento favorito com Café Aurora usando este áudio! Os 3 melhores ganham kit especial."
    *   **YouTube (Análise Aprofundada)**: "Review Completo: Comparativo das 5 Melhores Cafeteiras de Cápsula para o seu Café Aurora - Qual vale a pena?"
    *   **LinkedIn (Artigo de Liderança de Pensamento)**: "A Ascensão do Café Sustentável no Brasil: Desafios e Oportunidades para a Indústria e o Consumidor."
    *   **Twitter/X (Enquete Interativa)**: "Qual seu método de preparo de café favorito para começar o dia? A) Expresso B) Coado C) Prensa Francesa D) Aeropress #CafeAurora #EnqueteDoCafe"

---

## Templates

### Relatório Semanal de Social Listening (Sumário Executivo)

```
Relatório Semanal de Social Listening - 01/07 a 07/07/2024

Marca Monitorada: Café Aurora
Período: 01 de Julho a 07 de Julho de 2024

Sumário Executivo:
O volume total de menções sobre "Café Aurora" foi de 1.250 (vs. 1.100 na semana anterior, +13.6%).
O sentimento geral manteve-se predominantemente positivo (72%), com um leve aumento de menções neutras (20%) e estável de negativas (8%).
A principal plataforma de discussão foi o Instagram (45% das menções), seguido pelo Twitter/X (30%).

Insights Chave:
1.  **Pico de Engajamento**: O post sobre a nova embalagem sustentável no Instagram (@CafeAuroraOficial) gerou 350 curtidas e 80 comentários, com sentimento 90% positivo, destacando o interesse do público em iniciativas ecológicas.
2.  **Trending Topic (Twitter/X)**: Houve uma discussão sobre "melhor café para inverno", onde "Café Aurora" foi mencionado 50 vezes, sugerindo oportunidade para conteúdo sazonal.
3.  **Feedback Negativo Específico**: 15 menções no Reclame Aqui (monitorado via integração) sobre "problemas na entrega do e-commerce" para compras feitas entre 25/06 e 30/06. Necessário encaminhamento para logística.
4.  **Oportunidade de Influência**: Identificados 3 perfis no TikTok com bom engajamento falando sobre "receitas com café gelado" que não mencionaram a marca. Perfis: @BaristaGelado (50k seg), @CafeNaVibe (30k seg), @ReceitasDeCafeFacil (45k seg).

Recomendações:
*   Criar conteúdo para Instagram e TikTok focado em receitas de café para o inverno e café gelado, destacando a nova embalagem sustentável.
*   Investigar e resolver os problemas de entrega no e-commerce para os lotes afetados.
*   Avaliar contato com os influenciadores de TikTok identificados para parcerias.
```

### Template de Alerta de Crise (Exemplo de Mensagem de Slack)

```
🚨 ALERTA DE CRISE SOCIAL - URGENTE 🚨

**Data/Hora:** 08/07/2024, 10:35 BRT
**Marca Monitorada:** Café Aurora
**Tipo de Alerta:** Pico de Menções Negativas (Crítico)
**Plataforma Principal:** Twitter/X
**Termos Acionadores:** "Café Aurora lote", "Café Aurora estragado", "reclamação Café Aurora"

**Volume de Menções (Última Hora):** 120 menções (vs. média de 5/h, +2300%)
**Sentimento Predominante:** 95% Negativo
**Assunto Principal:** Reclamações de consumidores sobre um lote específico de café (Lote 12345) com sabor alterado, com fotos e vídeos sendo compartilhados.
**Exemplo de Tweet de Alto Impacto:**
"Absurdo! O @CafeAuroraoficial me vendeu um café estragado! Lote 12345. Cheiro e gosto horríveis. Nunca mais! #CafeAurora #Reclamacao"
(Link: https://twitter.com/userXYZ/status/1234567890)

**Impacto Potencial:** Alto. Risco de viralização e danos à reputação.
**Ações Imediatas Sugeridas:**
1.  Acionar equipe de PR/Comunicação e Jurídico.
2.  Verificar internamente o Lote 12345 (produção, controle de qualidade, distribuição).
3.  Preparar um comunicado inicial/resposta padrão para Twitter/X, direcionando para DM.
4.  Monitorar menções em outras plataformas (Instagram, Reclame Aqui) e Google Alerts.

**Anexos:** Screenshot do dashboard de monitoramento com o pico de menções (se disponível).
```

---

## Checklist

- [x] Definir termos-chave de monitoramento para marca, produtos, concorrentes e indústria (ex: "Café Aurora", "Café do Ponto", "café especial", "sustentabilidade café").
- [x] Configurar alertas para picos de volume e sentimentos negativos em tempo real (ex: alerta Slack para >10 menções negativas/hora).
- [x] Analisar o volume de menções e o sentimento líquido (positivo, neutro, negativo) em todas as plataformas monitoradas.
- [x] Identificar os principais tópicos e tendências de discussão relevantes para a marca e o setor de café.
- [x] Mapear influenciadores e vozes-chave que mencionam a marca ou o setor (ex: baristas,