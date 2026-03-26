---
name: course-pricing-model
description: "Course Pricing Model — Skill especializada para course pricing model"
license: MIT
metadata:
  version: 1.0.0
  author: Cafe Code AI
  category: 13-cursos-educacao
  updated: 2026-03-01
risk: safe
---

# Course Pricing Model

Esta skill capacita o Claude a desenvolver e implementar estratégias de precificação de cursos online, considerando valor percebido, análise de mercado, estrutura de custos e modelos de assinatura.

---

## Keywords

Precificação de cursos, Modelo de assinatura, Preço de lançamento, Bundling de cursos, Precificação por valor, Custo de aquisição de cliente (CAC), Lifetime Value (LTV), Análise de concorrência, Estratégias de upsell/downsell, Fremium, Tiered pricing, Dynamic pricing, Garantia de satisfação, Ponto de equilíbrio.

---

## Quick Start

1.  **Mapear Custos Essenciais**: Liste todos os custos fixos (plataforma, ferramentas de email, edição) e variáveis (marketing, comissão de afiliados, suporte) envolvidos na produção e entrega do curso "Desenvolvimento Web com Django".
2.  **Analisar Preços Concorrentes**: Pesquise os preços de 3 a 5 cursos de desenvolvimento web com Django ou frameworks similares no mercado, observando seus diferenciais e propostas de valor.
3.  **Definir Valor da Transformação**: Estabeleça o resultado concreto que o aluno alcançará com o curso "Desenvolvimento Web com Django" (ex: "Construir um e-commerce funcional em 30 dias") e qual o valor percebido dessa transformação para ele.
4.  **Calcular Ponto de Equilíbrio**: Com base nos custos e no preço sugerido, determine quantas vendas do curso são necessárias para cobrir todos os investimentos iniciais.
5.  **Escolher Modelo Inicial**: Selecione uma abordagem de precificação: preço único (R$ 597), assinatura mensal (R$ 49/mês para acesso a múltiplos cursos) ou um modelo tiered (básico R$ 397, premium R$ 797).

---

## Core Workflows

### Workflow 1: Construção de Estratégia de Precificação por Valor Percebido

Este workflow foca em precificar um curso com base no valor que ele entrega ao aluno, e não apenas nos custos de produção.

1.  **Identificar o Público-Alvo e suas Dores/Desejos**:
    *   **Ação**: Detalhe quem é o aluno ideal do curso "Gestão de Projetos Ágeis com Scrum e Kanban" e quais problemas ele enfrenta ou o que ele deseja alcançar.
    *   **Exemplo**: Aluno: Gerentes de projeto júnior e líderes de equipe com dificuldade em organizar fluxos de trabalho. Dor: Projetos atrasados, equipe desmotivada, falta de visibilidade do progresso. Desejo: Entregar projetos no prazo, aumentar produtividade, obter reconhecimento.
2.  **Quantificar a Transformação e o Resultado Tangível**:
    *   **Ação**: Descreva em termos concretos o benefício final do curso e, se possível, quantifique o impacto financeiro ou de tempo.
    *   **Exemplo**: O aluno será capaz de "reduzir em 20% o tempo de entrega de projetos" e "aumentar a satisfação da equipe em 30%", resultando em "promoção ou aumento salarial de até R$1.500/mês".
3.  **Pesquisar Alternativas do Cliente (Custo da Não-Ação)**:
    *   **Ação**: Entenda como o público-alvo resolve (ou não resolve) o problema sem seu curso e qual o custo disso.
    *   **Exemplo**: Alternativas: Contratar consultoria (R$5k-R$10k), gastar meses tentando aprender sozinho (perda de tempo e produtividade), continuar com projetos falhos (perda de receita para a empresa). O custo da não-ação pode ser de R$2k-R$5k/mês em oportunidades perdidas.
4.  **Criar Matriz de Valor e Justificativa de Preço**:
    *   **Ação**: Estruture uma matriz que conecte dores, soluções, benefícios e a justificativa para um preço premium.
    *   **Exemplo**:
        | Dor do Aluno | Solução do Curso | Benefício Tangível | Justificativa de Preço |
        | :----------- | :--------------- | :----------------- | :--------------------- |
        | Projetos atrasados | Módulos de Scrum e Kanban | Redução de 20% no tempo de entrega | Economia de R$2k/mês em retrabalho |
        | Equipe desmotivada | Técnicas de facilitação | Aumento de 30% na satisfação | Melhor retenção de talentos |
        | **Preço Sugerido Final**: R$ 1.297 (justificado pelo retorno de R$2.000+ mensais para o aluno).
5.  **Definir Preço Base e Estratégias de Lançamento**:
    *   **Ação**: Com base na matriz de valor, estabeleça o preço e planeje como ele será introduzido no mercado (early bird, lançamento, preço cheio).
    *   **Exemplo**: Preço base de R$1.297. Lançamento "Early Bird" a R$897 para os primeiros 100 alunos, seguido de preço de lançamento a R$1.097 e, por fim, o preço cheio de R$1.297.

### Workflow 2: Implementação de Modelo de Assinatura (Tiered Pricing) para Portfólio de Cursos

Este workflow detalha a criação de um modelo de assinatura com diferentes níveis de acesso para um catálogo de cursos, maximizando o LTV.

1.  **Mapear Portfólio de Cursos e Níveis de Complexidade**:
    *   **Ação**: Liste todos os cursos disponíveis na plataforma (ex: "Academia de Marketing Digital") e classifique-os por nível (iniciante, intermediário, avançado) e tema.
    *   **Exemplo**:
        *   Nível Iniciante: "Fundamentos de SEO", "Introdução ao Tráfego Pago"
        *   Nível Intermediário: "Google Ads Avançado", "Meta Ads para E-commerce"
        *   Nível Avançado: "Automação de Marketing", "Análise de Dados com Google Analytics 4"
        *   Cursos Bônus/Especiais: "Mentorias Semanais", "Templates de Campanhas"
2.  **Definir Camadas (Tiers) e Proposta de Valor de Cada uma**:
    *   **Ação**: Crie 2-3 níveis de assinatura, cada um com um conjunto claro de benefícios e um preço correspondente.
    *   **Exemplo**:
        *   **Tier 1: Essencial (R$ 49/mês)**: Acesso a todos os cursos iniciantes, comunidade básica.
        *   **Tier 2: Premium (R$ 99/mês)**: Acesso a todos os cursos (iniciante, intermediário, avançado), comunidade avançada, 1 mentoria em grupo mensal.
        *   **Tier 3: VIP (R$ 199/mês)**: Acesso a todos os cursos, comunidade VIP, 4 mentorias em grupo mensais, acesso a cursos bônus exclusivos, suporte prioritário.
3.  **Configurar Plataforma e Ferramentas de Pagamento**:
    *   **Ação**: Garanta que a plataforma EAD (Hotmart Club, Teachable, Thinkific) e o gateway de pagamento (Stripe, PagSeguro) suportam a venda de assinaturas e a gestão dos diferentes tiers.
    *   **Exemplo**: Configurar planos de assinatura no Hotmart, vincular os conteúdos aos respectivos tiers, testar o processo de pagamento e cancelamento.
4.  **Desenvolver Estratégias de Upsell e Retenção**:
    *   **Ação**: Crie fluxos para incentivar alunos do Tier Essencial a migrarem para o Premium e para reter assinantes em todos os níveis.
    *   **Exemplo**:
        *   **Upsell**: Alunos do Tier Essencial recebem emails com depoimentos de sucesso de quem migrou para o Premium, acesso gratuito temporário a um módulo avançado.
        *   **Retenção**: Conteúdo novo mensal em todos os tiers, desafios de engajamento, webinars exclusivos, suporte rápido.
5.  **Monitorar Métricas de Assinatura**:
    *   **Ação**: Acompanhe o CAC, LTV, Churn Rate (taxa de cancelamento) e MRR (Receita Recorrente Mensal) para otimizar o modelo.
    *   **Exemplo**: Observar que o churn do Tier Essencial é alto. Investigar o motivo (falta de conteúdo novo?) e ajustar a oferta ou a estratégia de retenção para esse tier.

---

## Templates

### Análise de Precificação Competitiva - Curso de Edição de Vídeo Profissional

```
Análise de Precificação Competitiva - Curso: Edição de Vídeo Profissional com Adobe Premiere

Concorrente A: "Dominando o Premiere Pro" (Plataforma X)
Curso Similar: Foca em iniciantes, 15 horas de aula.
Preço: R$ 349,00
Diferenciais (seu curso vs. concorrente):
- Melhor: Módulos avançados de color grading e motion graphics, projeto final prático com feedback.
- Pior: Menos aulas focadas em fundamentos básicos, assumimos algum conhecimento prévio.
- Neutro: Qualidade de produção de vídeo similar, acesso vitalício.
Observações: Foco em público mais amplo, oferece garantia de 7 dias, promoções frequentes.

Concorrente B: "Masterclass de Edição para Youtubers" (Plataforma Y)
Curso Similar: Foco em criação de conteúdo para YouTube, 10 horas de aula.
Preço: R$ 197,00
Diferenciais (seu curso vs. concorrente):
- Melhor: Mais abrangente para diversas finalidades (cinema, marketing, YouTube), instrutor com experiência em grandes produtoras.
- Pior: Preço mais alto pode afastar quem busca um curso muito específico e barato.
- Neutro: Material complementar (presets, arquivos de prática) similar.
Observações: Preço de entrada baixo, usa gatilhos de escassez (contagem regressiva) para promoções relâmpago.

Concorrente C: "Formação Completa em Pós-Produção" (Plataforma Z)
Curso Similar: Abrange Premiere, After Effects e DaVinci Resolve, 50 horas de aula.
Preço: R$ 997,00 (pacote)
Diferenciais (seu curso vs. concorrente):
- Melhor: Foco exclusivo e aprofundado no Premiere, o que pode ser menos intimidador.
- Pior: Não inclui outros softwares de edição, o que pode ser um ponto negativo para quem busca um "tudo em um".
- Neutro: Certificação de conclusão.
Observações: Público profissional, preço elevado mas com valor percebido de "formação completa".

Conclusão para Meu Curso ("Edição de Vídeo Profissional com Adobe Premiere"):
- Preço Médio do Mercado (cursos Premiere): R$ 273,00 (apenas A e B)
- Gap de Valor (Seu Curso): Nosso curso oferece um aprofundamento técnico superior e módulos avançados que os cursos mais baratos não cobrem, justificando um preço mais alto que a média. Comparado ao pacote mais caro, nosso foco no Premiere oferece especialização.
- Sugestão de Preço Inicial: R$ 597,00 (justificado pelos diferenciais de módulos avançados, feedback em projeto e instrutor experiente).
```

### Plano de Lançamento com Precificação Dinâmica - Curso de Marketing para Infoprodutores

```
Plano de Lançamento com Precificação Dinâmica - Curso: Marketing para Infoprodutores Descomplicado

Fase 1: Pré-Lançamento (Early Bird para Lista VIP)
- Duração: 5 dias (Ex: 01/08 - 05/08)
- Preço: R$ 297,00
- Desconto: 60% do preço final
- Gatilho: Acesso exclusivo para quem se cadastrou na lista de espera ou participou do workshop gratuito.
- Benefícios Exclusivos: Acesso a 3 aulas bônus de "Copywriting para Vendas", grupo VIP no Telegram com o instrutor, 1 sessão de tira-dúvidas ao vivo.

Fase 2: Lançamento Oficial (Primeira Semana Aberta)
- Duração: 7 dias (Ex: 06/08 - 12/08)
- Preço: R$ 497,00
- Desconto: 33% do preço final
- Gatilho: Abertura das inscrições para o público geral, com bônus por tempo limitado.
- Benefícios: Acesso completo ao curso, comunidade no Discord, templates editáveis de planos de marketing.

Fase 3: Preço Padrão (Evergreen)
- Duração: Contínuo (a partir de 13/08)
- Preço: R$ 747,00
- Desconto: Nenhum (preço cheio)
- Gatilho: Disponibilidade constante do curso.
- Benefícios: Acesso completo ao curso, comunidade no Discord, templates editáveis.

Estratégias de Upsell/Downsell:
- Upsell: Após a compra do curso principal, oferecer "Pacote de Mentoria Individual (3 sessões)" por R$ 997,00 ou "Acesso a todos os meus cursos por 1 ano" por R$ 1.500,00.
- Downsell: Para quem não comprou o curso completo na Fase 2, oferecer um "Mini-Curso de Tráfego Pago para Infoprodutores" (Módulo 3 do curso principal) por R$ 97,00, com a opção de abater esse valor na compra do curso completo posteriormente.
```

---

## Checklist

-   [x] Custos fixos e variáveis de produção e marketing do curso mapeados detalhadamente?
-   [x] Análise de precificação de pelo menos 3 concorrentes diretos e indiretos concluída?
-   [x] Proposta de valor única (UVP) e transformação do curso claramente articuladas para o público-alvo?
-   [x] Ponto de equilíbrio (break-even point) calculado para o volume de vendas inicial desejado?
-   [x] Modelo de precificação primário escolhido e justificado (preço único, assinatura, tiered, freemium)?
-   [x] Estratégia de lançamento desenhada com gatilhos de escassez/urgência (early bird, bônus por tempo limitado)?
-   [x] Plano de upsell e downsell para otimizar o LTV e atender diferentes perfis de cliente?
-   [x] Plataforma EAD e gateway de pagamento configurados para suportar o modelo de precificação escolhido?
-   [x] Política de reembolso, garantia de satisfação e termos de uso do curso definidos e comunicados?
-   [x] Estratégias de retenção (para assinaturas) ou de recompra (para cursos únicos) planejadas?
-   [x] Análise SWOT (Forças, Fraquezas, Oportunidades, Ameaças) específica para a precificação do curso realizada?
-   [x] Metas de CAC e LTV definidas e acompanháveis para o curso?

---

## Métricas de Referência

| Métrica | Benchmark (Mercado EAD BR) | Meta (Seu Curso) |
| :------------------------------ | :------------------------- | :--------------- |
| **CAC (Custo de Aquisição de Cliente)** | R$ 50 - R$ 300 (orgânico/quente), R$ 200 - R$ 800 (pago/frio) | R$ 150 |
| **LTV (Lifetime Value)** | 3x - 5x o CAC (para assinaturas); 1.5x - 2x o ticket médio (cursos únicos) | R$ 600 |
| **Taxa de Conversão da Página de Vendas** | 1% - 5% (tráfego frio); 5% - 15% (tráfego quente/orgânico) | 3% |
| **Taxa de Churn (Assinatura Mensal)** | 5% - 15% (bons resultados); 15% - 30% (médio) | 8% |
| **Ticket Médio (Preço de Venda)** | R$ 97 - R$ 1997 (grande variação por nicho/valor) | R$ 497 |
| **MRR (Monthly Recurring Revenue)** | Varia muito por escala, mas busca-se crescimento de 10-20% ao mês | R$ 10.000 (após 6 meses) |

---

## Erros Comuns

1.  **Precificar apenas por custo de produção**: Este erro ignora completamente o valor que o curso entrega ao aluno e o que o mercado está disposto a pagar.
    *   **Como evitar**: Concentre-se na transformação e no resultado final que o aluno alcançará. Se um curso de "Investimentos Inteligentes" pode gerar R$5.000 de lucro mensal para o aluno, seu preço pode ser de R$997 ou mais, mesmo que os custos de produção sejam baixos. O valor não está na hora de gravação, mas no retorno do investimento do aluno.
2.  **Copiar o preço do concorrente sem diferenciar a oferta**: Simplesmente replicar o preço de um concorrente sem considerar seus próprios diferenciais e custos leva à subvalorização ou à não competitividade.
    *   **Como evitar**: Realize uma análise SWOT para a sua oferta e identifique seus pontos fortes e fracos em relação aos concorrentes. Se seu curso tem mentorias exclusivas, comunidade ativa e certificação reconhecida, justifique um preço mais alto. Exemplo: Concorrente cobra R$197, mas seu curso com suporte premium e material bônus pode ser R$397.
3.  **Não testar diferentes pontos de preço ou modelos**: Acreditar que existe um "preço perfeito" único sem experimentação impede a otimização de lucro e a descoberta de novas oportunidades.
    *   **Como evitar**: Adote uma abordagem de precificação dinâmica. Comece com um preço "early bird", depois um preço de lançamento e, por fim, o preço cheio. Utilize testes A/B em páginas de vendas para diferentes faixas de preço ou ofereça bundles em momentos específicos para medir a elasticidade da demanda. Exemplo: Lançar a R$597 com bônus e, após 30 dias, testar a R$497 com menos bônus para ver qual estratégia maximiza receita.

---

## Dicas Avançadas

1.  **Micro-precificação de Módulos (Tripwire)**: Ofereça módulos ou aulas específicas do curso principal a um preço muito baixo (R$27-R$97) como um produto de entrada (tripwire). O objetivo é converter leads frios em clientes e, em seguida, fazer upsell do curso completo.
    *   **Exemplo**: Vender o "Módulo 1: Primeiros Passos em X" do seu curso de "Programação para Iniciantes" por R$37. Após a compra, o aluno recebe uma série de emails oferecendo o curso completo de R$697 com um desconto exclusivo.
2.  **Precificação Baseada em Performance ou Resultados Garantidos**: Para cursos de alto valor percebido, especialmente em nichos de carreira ou negócios, ofereça uma garantia de resultado tangível. Isso justifica um preço premium.
    *   **Exemplo**: Curso "Como Lançar seu Primeiro Infoproduto em 30 Dias". Preço: R$1.997. Garantia: "Se você seguir todo o método e não fizer sua primeira venda em 30 dias, devolvemos seu dinheiro e te damos mais R$500". Essa garantia eleva a confiança e o valor percebido.
3.  **Modelos de "Pay What You Want" (PWYW) para Conteúdo Complementar**: Utilize o modelo PWYW para e-books, templates ou mini-cursos de menor valor, especialmente em lançamentos ou para construir prova social inicial.
    *   **Exemplo**: Lançar um "Guia Completo de Ferramentas de IA para Criadores de Conteúdo" e permitir que os primeiros 200 compradores paguem o que quiserem (com um valor mínimo sugerido de R$9,90). Isso gera buzz e aquisição de leads qualificados.
4.  **Integração de Precificação com Gamificação e Progressão**: Conceda descontos progressivos ou acesso a tiers mais elevados (em modelos de assinatura) com base na conclusão de módulos, engajamento na comunidade ou atingimento de metas de aprendizado.
    *   **Exemplo**: Alunos que completam 75% do curso "Marketing Digital Avançado" recebem um cupom de 30% para o próximo curso ou um mês grátis do Tier Premium da plataforma de assinatura.
5.  **Análise de Elasticidade de Preço via Testes A/B Multivariados**: Vá além dos testes A/B simples. Utilize ferramentas que permitam testar múltiplas variáveis de preço, bônus e mensagens de venda simultaneamente para identificar a combinação mais lucrativa.
    *   **Exemplo**: Em vez de apenas testar R$497 vs R$597, teste:
        *   Versão A: R$497 + Bônus X
        *   Versão B: R$597 + Bônus Y
        *   Versão C: R$547 (sem bônus, com garantia estendida)
        Analise qual versão oferece o maior ROI em termos de receita por visita.