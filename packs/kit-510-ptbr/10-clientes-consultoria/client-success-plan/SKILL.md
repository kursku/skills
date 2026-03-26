---
name: client-success-plan
description: "Client Success Plan — Skill especializada para client success plan"
license: MIT
metadata:
  version: 1.0.0
  author: Cafe Code AI
  category: 10-clientes-consultoria
  updated: 2026-03-01
risk: critical
---

# Client Success Plan

Esta skill capacita Claude a elaborar, executar e gerenciar Planos de Sucesso do Cliente, focando na retenção e expansão em contextos de consultoria, garantindo que o valor prometido seja entregue e percebido.

---

## Keywords

Retenção de Clientes, Onboarding Consultivo, Health Score, QBR (Quarterly Business Review), Plano de Sucesso, Churn Prevention, Upsell Estratégico, Engajamento Pós-Venda, Gestão de Expectativas, Relatório de Valor, KPIs de Sucesso, Customer Journey Consulting.

---

## Quick Start

1.  **Coletar Dados Contratuais Iniciais**: Revisar o escopo do projeto, termos do contrato, e a proposta de valor original para o cliente `TechSolutions S.A.`, que contratou a consultoria de otimização de infraestrutura.
2.  **Mapear Stakeholders e Objetivos**: Identificar o patrocinador executivo `(Diretor de TI - João Silva)` e os principais usuários, alinhando os objetivos de negócio específicos `(redução de 15% nos custos de cloud)` com os entregáveis da consultoria.
3.  **Estruturar o Primeiro Health Score**: Definir os indicadores para o cliente `TechSolutions S.A.`, ponderando `40% atingimento de KPIs técnicos`, `30% engajamento do time do cliente`, `20% satisfação reportada (CSAT)` e `10% riscos operacionais`.
4.  **Agendar Cadência de Comunicação**: Inserir no calendário as reuniões de acompanhamento semanais com a equipe técnica e a QBR trimestral com a diretoria do cliente para os próximos 12 meses.

---

## Core Workflows

### Workflow 1: Estruturação e Onboarding do Plano de Sucesso Consultivo

Este workflow detalha a criação e implementação inicial de um Plano de Sucesso, garantindo que a consultoria se alinhe às expectativas de valor do cliente desde o primeiro contato pós-venda.

1.  **Revisão Aprofundada do Acordo Comercial**:
    *   **Ação**: Analisar o contrato assinado com o cliente `Logística Ágil Ltda.`, focando na proposta de valor, escopo de serviço `(otimização da cadeia de suprimentos)` e métricas de sucesso originalmente apresentadas ao time de vendas.
    *   **Exemplo**: Para `Logística Ágil`, a proposta mencionava "redução de 7% nos custos de transporte em 6 meses". O Plano de Sucesso deve transformar isso em um KPI mensurável e com marcos claros.
2.  **Identificação e Mapeamento de Stakeholders Chave**:
    *   **Ação**: Realizar entrevistas internas com a equipe de vendas e consultores seniores envolvidos no pré-venda para identificar todos os contatos do cliente, seus papéis `(Diretor de Operações, Gerente de Frota)` e seus interesses no projeto.
    *   **Exemplo**: Descobrir que o `Gerente de Frota, Carlos Alberto`, é o principal usuário impactado e que a `Diretora de Operações, Patrícia Souza`, é a decisora final e patrocinadora do projeto. Ambos precisam ser endereçados no plano de comunicação.
3.  **Definição Colaborativa de KPIs de Sucesso**:
    *   **Ação**: Agendar uma reunião de "Alinhamento de Sucesso" com os stakeholders do cliente, utilizando o script do Template 1 para validar e refinar os KPIs que realmente representam valor para o negócio deles.
    *   **Exemplo**: Para `Logística Ágil`, além da "redução de custos de transporte", o cliente pode sugerir "redução de 15% nos atrasos de entrega" como um KPI adicional de alto impacto, que não estava inicialmente explícito.
4.  **Elaboração do Plano de Comunicação e Cadência**:
    *   **Ação**: Definir a frequência e o formato das interações `(reuniões semanais de status, QBRs trimestrais, relatórios mensais de progresso)` e os responsáveis por cada comunicação tanto do lado da consultoria quanto do cliente.
    *   **Exemplo**: Reunião semanal de 30 min com o `Gerente de Frota` para updates técnicos; QBR de 90 min a cada 3 meses com a `Diretora de Operações` e o `Diretor Financeiro` para revisão de valor e ROI.
5.  **Configuração Inicial do Health Score**:
    *   **Ação**: Implementar o sistema de pontuação de saúde do cliente com base nos KPIs definidos, engajamento e feedback.
    *   **Exemplo**: Se o KPI de "redução de custos" está no caminho certo (+20 pontos), o `Gerente de Frota` participa ativamente das reuniões (+15 pontos), e o CSAT inicial foi 9/10 (+20 pontos).

### Workflow 2: Monitoramento Contínuo e Reporting de Valor

Este workflow descreve a manutenção do Plano de Sucesso, garantindo que o valor seja continuamente percebido pelo cliente e que a consultoria esteja sempre à frente de potenciais problemas ou oportunidades.

1.  **Coleta e Análise Regular de Dados de Desempenho**:
    *   **Ação**: Estabelecer processos para coletar dados dos KPIs definidos `(custos de transporte, atrasos na entrega)` de forma consistente, preferencialmente automatizada, e analisá-los semanalmente.
    *   **Exemplo**: Integrar planilhas de custos de transporte fornecidas pela `Logística Ágil` em um dashboard interno, comparando com a linha de base e a meta, detectando desvios de 2% acima do esperado.
2.  **Atualização Contínua do Health Score do Cliente**:
    *   **Ação**: Com base na análise de dados, engajamento em reuniões, feedback qualitativo e utilização dos entregáveis da consultoria, atualizar o Health Score `(pontuação de 0 a 100)` do cliente `Logística Ágil` a cada duas semanas.
    *   **Exemplo**: O Health Score do cliente caiu de 85 para 70 porque o `Gerente de Frota` cancelou duas reuniões seguidas e os dados de atraso de entrega não foram fornecidos no prazo. Isso aciona um alerta interno.
3.  **Preparação e Execução de Quarterly Business Reviews (QBRs)**:
    *   **Ação**: Compilar um relatório de valor detalhado (vide Template 2) que demonstre o progresso dos KPIs, o ROI alcançado e os próximos passos estratégicos. Conduzir a QBR com a liderança do cliente.
    *   **Exemplo**: Apresentar à `Diretora de Operações` da `Logística Ágil` um slide mostrando a redução de 4.5% nos custos de transporte nos primeiros 3 meses, projetando 8% ao final do projeto e sugerindo uma fase 2 para otimização de rotas.
4.  **Identificação Proativa de Riscos e Oportunidades**:
    *   **Ação**: Durante as análises e interações, procurar por sinais de desengajamento `(pouca participação em reuniões)`, insatisfação `(feedback negativo em pesquisas)` ou novas necessidades de negócio do cliente `(expansão para novos mercados)`.
    *   **Exemplo**: Perceber que a `Logística Ágil` está planejando expandir para o Nordeste, o que pode gerar uma nova demanda por consultoria em logística regional (oportunidade de upsell) ou causar desafios na infraestrutura atual (risco).
5.  **Feedback Loop e Ajustes do Plano**:
    *   **Ação**: Utilizar o feedback das QBRs e o monitoramento contínuo para ajustar o Plano de Sucesso, seja revisando KPIs, alterando a cadência de comunicação ou propondo novas fases do projeto.
    *   **Exemplo**: Após a QBR, a `Logística Ágil` solicita que o foco mude ligeiramente para "sustentabilidade da frota", adicionando um KPI de "redução de emissões de CO2" ao plano.

---

## Templates

### Script para Reunião de Kick-off de Sucesso (Consultoria)

```
**Cliente:** Inovatech S.A.
**Projeto:** Transformação Digital para Otimização de Processos Internos
**Consultor Líder:** Ana Silva
**Data:** 05/10/2025
**Participantes Cliente:**
    *   Carlos Mendes (Diretor de Operações) - Patrocinador Executivo
    *   Mariana Costa (Gerente de Projetos Internos) - Ponto Focal Diário
    *   Equipe de Processos (3 membros)
**Participantes Consultoria:**
    *   Ana Silva (Líder de Sucesso do Cliente)
    *   João Pereira (Consultor Técnico Sênior)

**Agenda da Reunião (90 min):**

1.  **Boas-Vindas e Apresentações (5 min):**
    *   Ana Silva: "Bom dia, Carlos e equipe. É um prazer iniciarmos este projeto crucial para a Inovatech. Sou Ana Silva, sua Líder de Sucesso na [Nome da Consultoria]."
    *   Rodada rápida de apresentações, incluindo papel e expectativa inicial de cada um.

2.  **Revisão do Escopo e Objetivos do Projeto (15 min):**
    *   João Pereira: "Conforme proposta, nosso objetivo é otimizar os processos de [Ex: aprovação de despesas e onboarding de novos colaboradores] utilizando a plataforma X. Queremos reduzir em 20% o tempo médio desses processos em 4 meses."
    *   Carlos Mendes: "Sim, e para nós, a redução de erros e a melhoria da experiência do colaborador são igualmente importantes."

3.  **Validação dos KPIs de Sucesso (20 min):**
    *   Ana Silva: "Para garantir que estamos entregando valor, propomos monitorar: 1) Tempo Médio de Aprovação de Despesas; 2) Tempo Médio de Onboarding; 3) Taxa de Erros nos Processos Otimizados; 4) Nível de Satisfação do Colaborador (CSAT pós-processo). Há outros indicadores cruciais para a Inovatech?"
    *   Mariana Costa: "Talvez a 'taxa de uso da nova ferramenta' seja relevante para garantir a adoção."
    *   Ana Silva: "Excelente ponto! Vamos incluir."

4.  **Estrutura do Plano de Sucesso e Health Score (15 min):**
    *   Ana Silva: "Nosso Plano de Sucesso foca na sua experiência contínua. Teremos reuniões de acompanhamento semanais com a Mariana e sua equipe, e reuniões trimestrais de revisão de valor (QBR) com você, Carlos. O Health Score do projeto será atualizado a cada duas semanas, considerando o progresso dos KPIs, engajamento e feedback."

5.  **Definição da Cadência de Comunicação (10 min):**
    *   Ana Silva: "Sugiro reuniões semanais de status às terças-feiras às 10h, e a primeira QBR em 15 de janeiro de 2026. Vocês concordam?"
    *   Carlos Mendes: "Perfeito. As terças são boas."

6.  **Próximos Passos e Responsabilidades (15 min):**
    *   João Pereira: "Nossa equipe irá preparar o ambiente de teste e o cronograma detalhado para a fase 1 até o final desta semana. Precisaremos que a equipe de processos da Inovatech agende as sessões de levantamento de requisitos com a Mariana."
    *   Mariana Costa: "Confirmado. Vou coordenar internamente."

7.  **Sessão de Perguntas e Respostas (10 min):**
    *   Ana Silva: "Alguma dúvida ou ponto que queiram adicionar?"
    *   Carlos Mendes: "Não, o plano está claro e alinhado. Animado para ver os resultados!"

**Objetivo da Reunião Atingido:** Alinhamento de expectativas, validação de KPIs, estabelecimento de cadência e definição dos primeiros passos.
```

### Relatório de Valor Trimestral (QBR) - Exemplo de Seção de Desempenho

```
**Relatório de Valor Trimestral (QBR) - T3/2025**

**Cliente:** Alpha Consultoria S.A.
**Projeto:** Otimização de Processos de Recrutamento e Seleção
**Período Avaliado:** Julho - Setembro 2025
**Consultor Líder de Sucesso:** Lucas Costa

---

**Seção 1: Resumo Executivo e Destaques do Trimestre**

*   **Status Geral do Projeto:** No caminho certo para atingir 90% das metas anuais.
*   **Valor Principal Entregue:** Redução de 22% no Tempo Médio de Contratação (TMC) para posições-chave, impactando diretamente a agilidade da Alpha Consultoria em preencher vagas críticas.
*   **Próximos Passos Prioritários:** Foco na automação da triagem de currículos e na implementação de um novo módulo de feedback de entrevistas até o final do T4.

---

**Seção 2: Desempenho dos KPIs de Sucesso (Julho - Setembro 2025)**

| KPI de Sucesso                    | Linha de Base (Q2/2025) | Meta para o Projeto (Q4/2025) | Desempenho Atual (Q3/2025) | Variação vs. Base | Status      | Impacto no Negócio                                            |
| :-------------------------------- | :---------------------- | :---------------------------- | :------------------------- | :---------------- | :---------- | :------------------------------------------------------------ |
| **Tempo Médio de Contratação (TMC)** | 45 dias                 | 35 dias                       | **35 dias**                | -22%              | ✅ No Alvo  | Aumento da capacidade de preencher vagas estratégicas rapidamente. |
| **Custo por Contratação (CPC)**   | R$ 3.500,00             | R$ 3.000,00                   | **R$ 3.200,00**            | -8.6%             | 🟡 Em Progresso | Economia de R$ 300,00 por contratação, totalizando R$ 7.500,00 no trimestre (25 contratações). |
| **Taxa de Aceitação de Ofertas**  | 80%                     | 85%                           | **82%**                    | +2.5%             | ✅ No Alvo  | Redução na necessidade de reabrir processos seletivos.        |
| **Índice de Qualidade das Contratações (3 meses)** | N/A                     | 8.0 (escala 1-10)             | **7.5**                    | N/A               | 🟡 Em Progresso | Feedback positivo inicial dos gestores sobre novos colaboradores. |

**Análise do Desempenho:**
*   **TMC:** Atingimos a meta de 35 dias um trimestre antes do previsto, principalmente pela otimização das etapas de triagem e entrevistas iniciais.
*   **CPC:** Houve uma redução significativa, mas ainda precisamos trabalhar na negociação de taxas de plataformas de recrutamento para atingir a meta total.
*   **Qualidade das Contratações:** O índice inicial de 7.5 é promissor, com espaço para melhoria através de um treinamento mais robusto para os gestores sobre o novo processo de feedback.

---

**Seção 3: Próximos Passos e Recomendações (Q4/2025)**

1.  **Ação:** Implementar o módulo de automação de triagem de currículos para reduzir o CPC em mais 5%.
    *   **Responsável:** Equipe de Consultoria (João P.) e Equipe de RH da Alpha (Laura M.).
    *   **Prazo:** 30 de Outubro de 2025.
2.  **Ação:** Lançar o novo formulário padronizado de feedback de entrevistas para elevar o Índice de Qualidade das Contratações.
    *   **Responsável:** Equipe de Consultoria (Ana S.) e Gestores da Alpha.
    *   **Prazo:** 15 de Novembro de 2025.
3.  **Ação:** Reavaliar o SLA com plataformas de recrutamento para otimizar os custos.
    *   **Responsável:** Equipe de RH da Alpha (Laura M.) com suporte da Consultoria.
    *   **Prazo:** 30 de Novembro de 2025.

---
```

---

## Checklist

-   [x] Validar os KPIs de sucesso do cliente `(Ex: redução de custos de cloud em 15%)` com o patrocinador executivo `(Diretor de TI da TechSolutions)`.
-   [x] Agendar todos os touchpoints recorrentes `(reuniões semanais, QBRs trimestrais)` para os próximos 6 meses no calendário compartilhado.
-   [x] Documentar os riscos potenciais para a entrega de valor `(Ex: falta de dados do cliente, mudança de prioridade interna)` e planos de mitigação.
-   [x] Configurar o sistema de Health Score do cliente `(Ex: ponderação de KPIs, engajamento e satisfação)` e definir a frequência de atualização `(quinzenal)`.
-   [x] Preparar a agenda e os materiais para a próxima QBR `(Ex: Relatório de Valor com ROI explícito)` com pelo menos 1 semana de antecedência.
-   [x] Implementar um processo formal para coletar feedback do cliente `(Ex: pesquisa CSAT após marcos importantes do projeto ou NPS anual)`.
-   [x] Mapear oportunidades de upsell ou cross-sell `(Ex: nova fase do projeto, consultoria em outra área)` baseadas no progresso do Plano de Sucesso.
-   [x] Garantir que o plano de comunicação contempla todos os stakeholders relevantes `(executivos, gerentes, usuários finais)`.
-   [x] Estabelecer um "Plano de Ação para Clientes em Risco" para Health Scores abaixo de 60, incluindo a escalada interna e contato com o cliente.
-   [x] Realizar uma revisão interna trimestral da satisfação do cliente e do desempenho da consultoria no Plano de Sucesso.

---

## Métricas de Referência

| Métrica                      | Benchmark da Indústria (Consultoria) | Meta Interna (para Clientes de Consultoria) |
| :--------------------------- | :----------------------------------- | :------------------------------------------ |
| **Client Churn Rate Anual**  | < 10%                                | < 5%                                        |
| **Expansion Revenue Rate**   | > 15%                                | > 20%                                       |
| **Client Lifetime Value (CLTV)** | Variável (Ex: 3-5x CAC)              | Aumentar 10% anualmente                     |
| **Time to First Value (TTFV)** | < 45 dias                            | < 30 dias                                   |
| **Net Promoter Score (NPS)** | > 40                                 | > 50                                        |
| **Customer Satisfaction (CSAT)** | > 85%                                | > 90%                                       |

---

## Erros Comuns

1.  **Focar Apenas em Entregáveis Técnicos, Ignorando o Valor Estratégico Percebido**:
    *   **Exemplo**: O consultor `João` entrega um relatório técnico impecável sobre a performance de servidores, mas não traduz como isso impacta a receita ou a agilidade do cliente `(Ex: "redução de 15% no downtime dos sistemas críticos, economizando R$ 50.000/mês em perdas de produtividade")`.
    *   **Como Evitar**: Cada comunicação ou relatório deve explicitamente vincular o entregável técnico a um benefício de negócio, usando a linguagem e os KPIs da liderança do cliente. Nas QBRs, sempre comece e termine com o "valor percebido" e o "impacto no ROI".

2.  **Não Ter um Patrocinador Executivo Claro do Lado do Cliente para Validação de Valor**:
    *   **Exemplo**: Todas as reuniões de progresso são realizadas com gerentes intermediários, e as decisões de renovação ou expansão ficam estagnadas porque o `Diretor de Operações` do cliente `(Alpha Consultoria)` não tem visibilidade clara do impacto estratégico da consultoria.
    *   **Como Evitar**: Desde o kick-off, identifique e estabeleça um relacionamento direto com o patrocinador executivo. Garanta que ele esteja presente nas QBRs e receba um resumo executivo focado no ROI entregue, mesmo que não participe das reuniões diárias. Crie um canal direto para ele.

3.  **Falta de Cadência Formal de Comunicação e Relatórios de Progresso, Resultando em Surpresas**:
    *   **Exemplo**: O cliente `Inovatech S.A.` só recebe atualizações sobre o projeto quando solicita ou quando surge um problema, sem um cronograma pré-definido de reuniões ou relatórios, levando a uma percepção de falta de controle e valor.
    *   **Como Evitar**: Implemente uma cadência de comunicação rigorosa, conforme definido no Plano de Sucesso: reuniões semanais de status com a equipe operacional, relatórios mensais de progresso e QBRs trimestrais com a liderança. Nunca deixe o cliente "adivinhar" o que está acontecendo.

---

## Dicas Avançadas

1.  **Implementar um "Early Warning System" Proativo para Clientes em Risco**:
    *   **Exemplo**: Monitore indicadores comportamentais como `(1) declínio na participação do cliente em reuniões agendadas`, `(2) atrasos na entrega de dados solicitados`, `(3) aumento no tempo de resposta a e-mails`, ou `(4) feedback indireto de outros consultores sobre desengajamento`. Se dois ou mais desses sinais aparecerem para o cliente `Beta Serviços`, acione automaticamente um alerta para o Líder de Sucesso e a gerência. Isso permite intervenções antes que o problema se agrave.
2.  **Transformar QBRs em Sessões de Co-criação de Valor, Não Apenas Relatórios**:
    *   **Exemplo**: Em vez de apenas apresentar slides sobre o que a consultoria fez, reserve tempo na QBR para que o próprio cliente `(Ex: Diretor de Marketing da StartUp X)` apresente seus desafios atuais e como a consultoria pode ajudar a endereçá-los em futuras fases. Incentive a discussão sobre o roadmap de crescimento do cliente e como a consultoria pode se alinhar, transformando a reunião em uma sessão estratégica colaborativa.
3.  **Mapear a "Jornada de Valor" do Cliente Pós-Onboarding para Identificar Oportunidades de Expansão**:
    *   **Exemplo**: Após a conclusão da fase inicial de otimização de processos para a `Indústria Delta`, crie um mapa da jornada de valor que o cliente ainda pode buscar `(Ex: expansão para novos mercados, digitalização de outros departamentos, implementação de IA)`. Proativamente, apresente soluções para esses "próximos passos de valor" antes mesmo que o cliente perceba a necessidade, posicionando a consultoria como um parceiro estratégico de longo prazo.
4.  **Criar um "Client Advisory Board" com Clientes Estratégicos**:
    *   **Exemplo**: Convide 3-5 clientes de consultoria mais estratégicos `(Ex: TechSolutions, Alpha Consultoria, Indústria Delta)` para um conselho consultivo semestral. O objetivo é coletar feedback direto sobre a oferta de serviços, validar novas ideias de produtos/serviços e promover networking entre os clientes. Isso não apenas fornece insights valiosos, mas também fortalece o senso de comunidade e parceria, aumentando a lealdade e a probabilidade de referências.
5.  **Utilizar "Storytelling de Sucesso" em Todas as Interações**:
    *   **Exemplo**: Ao invés de apenas citar números na QBR com a `Logística Ágil`, conte a história de como a redução de 7% nos custos de transporte permitiu que eles investissem na modernização da frota, resultando em menos avarias e maior satisfação do cliente final. Personalize o impacto, conectando os resultados da consultoria aos objetivos mais amplos e aspiracionais do cliente.