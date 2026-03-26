---
name: performance-review
description: "Skill especializada para Performance Review, capacitando o Claude a gerenciar ciclos de avaliação, feedback e desenvolvimento de equipes."
license: MIT
metadata:
  version: 1.0.0
  author: Cafe Code AI
  category: 11-operacoes-sistemas
  updated: 2026-03-01
risk: critical
---

# Performance Review

Esta skill capacita o Claude a atuar como um especialista em Performance Review, auxiliando na execução, análise e otimização de ciclos de avaliação de desempenho.

---

## Keywords

Avaliação de Desempenho, Feedback 360, Plano de Desenvolvimento Individual (PDI), Calibração de Performance, OKRs, KPIs, Metas SMART, Matriz 9-Box, Gerenciamento de Talentos, Entrevista de Feedback, Autoavaliação, Cultura de Performance.

---

## Quick Start

1.  **Inicie o Ciclo de Autoavaliação**: Peça aos colaboradores que preencham o formulário de autoavaliação anual, destacando conquistas e desafios nos últimos 12 meses.
2.  **Colete Feedback 360**: Envie convites de feedback para pares, subordinados e gestores diretos, focando em comportamentos e resultados observáveis.
3.  **Analise Dados e Prepare Avaliação**: Consolide autoavaliações e feedbacks, compare com metas SMART definidas e utilize a Matriz 9-Box para categorização inicial.
4.  **Conduza a Reunião de Calibração**: Apresente os casos à equipe de liderança para discutir e ajustar as avaliações, garantindo equidade e alinhamento.
5.  **Comunique Resultados e PDI**: Agende reuniões individuais para discutir a avaliação final, construir Planos de Desenvolvimento Individual (PDI) e estabelecer metas para o próximo período.

---

## Core Workflows

### Workflow 1: Ciclo de Avaliação 360 Graus para Desenvolvedores Sênior

Este workflow detalha a execução de um ciclo de avaliação de desempenho 360 graus focado em desenvolvedores sênior, desde a coleta de dados até a elaboração do PDI.

1.  **Definição de Critérios e Escalas (Semana 1)**:
    *   **Ação**: Colaborar com a liderança de engenharia para refinar os critérios de avaliação, focando em habilidades técnicas (ex: arquitetura de software, otimização de código), colaboração (ex: code reviews, mentoria) e impacto no negócio.
    *   **Exemplo**: Para um Desenvolvedor Sênior, os critérios incluem "Capacidade de Projetar Soluções Escaláveis" (escala: 1-5, onde 5 = especialista em arquitetura de microsserviços) e "Mentoria e Compartilhamento de Conhecimento" (escala: 1-5, onde 5 = mentor ativo de 3+ juniores).
    *   **Ferramenta**: Utilize uma planilha Google Sheets compartilhada para documentar e obter consenso nos critérios.

2.  **Distribuição da Autoavaliação (Semana 2)**:
    *   **Ação**: Enviar o formulário de autoavaliação aos desenvolvedores sênior via ferramenta de RH (ex: Workday, Gupy), solicitando que reflitam sobre suas conquistas, desafios e áreas de desenvolvimento.
    *   **Exemplo**: O formulário pede que o desenvolvedor mencione 3 projetos de maior impacto onde liderou tecnicamente e 2 áreas onde buscou aprimoramento, como "domínio de Kubernetes" ou "melhora em comunicação técnica".
    *   **Prazo**: 5 dias úteis para preenchimento.

3.  **Coleta de Feedback de Pares e Gestores (Semana 3-4)**:
    *   **Ação**: Solicitar feedback de 3-5 pares, 1-2 subordinados (se houver) e o gestor direto de cada desenvolvedor sênior. O feedback deve ser focado em comportamentos observáveis e exemplos concretos.
    *   **Exemplo**: Em vez de "Ele é um bom líder", solicitar "Descreva uma situação em que [Nome do Desenvolvedor] demonstrou liderança técnica no projeto X, e qual foi o resultado". Para o gestor, "Avalie o impacto da [Nome do Desenvolvedor] na redução de débitos técnicos no último trimestre, citando 2 exemplos".
    *   **Ferramenta**: Utilize a mesma ferramenta de RH para anonimizar feedback de pares e subordinados, mas não do gestor.

4.  **Análise e Consolidacão dos Dados (Semana 5)**:
    *   **Ação**: Consolidar a autoavaliação, o feedback 360 e os dados de performance (ex: tempo médio de resolução de bugs, frequência de pull requests aprovadas, aderência a prazos em projetos críticos) para cada desenvolvedor.
    *   **Exemplo**: Se a autoavaliação destaca "excelência em refatoração", mas o feedback de pares aponta "dificuldade em aceitar sugestões de melhoria em código", isso sinaliza uma área de discussão. Comparar com a média da equipe para "tempo de resolução de bugs" (benchmark: 24h) para identificar outliers.
    *   **Output**: Rascunho inicial da avaliação de desempenho e uma pré-classificação na Matriz 9-Box.

5.  **Elaboração do Plano de Desenvolvimento Individual (PDI) (Semana 6)**:
    *   **Ação**: Com base na avaliação consolidada, trabalhar com o desenvolvedor sênior na criação de um PDI SMART (Específico, Mensurável, Atingível, Relevante, Temporal).
    *   **Exemplo**: Para um desenvolvedor que precisa melhorar em "Mentoria", o PDI pode ser "Realizar 3 sessões de pair programming com desenvolvedores juniores por mês e documentar 1 tutorial técnico sobre um tópico avançado de frontend até o final do trimestre".
    *   **Recursos**: Identificar cursos, livros, projetos internos ou mentores para apoiar o desenvolvimento.

### Workflow 2: Condução de Reunião de Calibração de Performance

Este workflow aborda a preparação e execução de uma reunião de calibração para garantir justiça e consistência nas avaliações de desempenho de toda a equipe.

1.  **Preparação dos Materiais (2 dias antes da reunião)**:
    *   **Ação**: Compilar todas as avaliações preliminares (com pontuações e justificativas) e as classificações iniciais na Matriz 9-Box para cada colaborador que será discutido.
    *   **Exemplo**: Para o Analista de Marketing Júnior, João Silva, a avaliação preliminar do gestor é "Excede Expectativas" (3/5 na Matriz), com justificativas como "Campanha X gerou 25% mais leads que a meta". Para a Desenvolvedora Plena, Ana Souza, "Atende Expectativas" (2/5 na Matriz), com "Entrega consistente de features, mas com 10% de atraso em 2 projetos".
    *   **Ferramenta**: Um dashboard ou planilha consolidada que permita visualização rápida e comparação.

2.  **Definição da Agenda e Regras (1 dia antes da reunião)**:
    *   **Ação**: Distribuir a agenda da reunião aos participantes (gestores de equipe, RH, liderança sênior), reforçando o objetivo de calibração e as regras de engajamento (foco em evidências, respeito às divergências).
    *   **Exemplo**: Agenda: 1. Introdução e Relembrar Objetivo (10 min); 2. Revisão de Casos "Abaixo das Expectativas" (30 min); 3. Revisão de Casos "Atende Expectativas" (45 min); 4. Revisão de Casos "Excede Expectativas" (45 min); 5. Discussão de Limites da Matriz 9-Box e Casos de Fronteira (30 min); 6. Próximos Passos (10 min).
    *   **Regra**: "Toda avaliação deve ser sustentada por no mínimo 2 exemplos concretos de desempenho ou comportamento."

3.  **Apresentação e Discussão dos Casos (Durante a Reunião)**:
    *   **Ação**: Cada gestor apresenta brevemente seus colaboradores, focando nos dados de performance, autoavaliação e feedback 360. A discussão é aberta para os demais gestores questionarem e contribuírem com suas perspectivas.
    *   **Exemplo**: Gestor A apresenta João Silva como "Excede Expectativas". Gestor B (que colaborou com João em um projeto transversal) pode intervir: "Concordo com o impacto da campanha X, mas observei que João teve dificuldade em colaborar com a equipe de vendas na etapa de qualificação. Isso foi considerado na avaliação?".
    *   **Moderação**: O facilitador (RH/Liderança) garante que a discussão permaneça objetiva e focada em evidências.

4.  **Deliberação e Ajustes (Durante a Reunião)**:
    *   **Ação**: Com base na discussão e nas evidências, a equipe decide coletivamente se a classificação preliminar é justa e consistente. Se houver desvio padrão significativo entre gestores, são feitos ajustes para garantir equidade.
    *   **Exemplo**: Se 3 gestores classificam seus colaboradores como "Excede Expectativas" com base em 1-2 exemplos, e 1 gestor classifica o seu com a mesma rating mas com 5 exemplos robustos, pode-se decidir ajustar as expectativas para "Excede" ou reclassificar o último para "Supera Amplamente Expectativas" (se a matriz permitir).
    *   **Critério**: No máximo 10% dos colaboradores na categoria "Supera Amplamente Expectativas" para evitar inflação de notas.

5.  **Documentação das Decisões e Próximos Passos (Após a Reunião)**:
    *   **Ação**: Registrar todas as decisões de calibração, as justificativas para quaisquer alterações de rating e os próximos passos (ex: comunicação dos resultados, início da fase de PDI).
    *   **Exemplo**: Documentar "Ana Souza reclassificada de 'Atende' para 'Excede' devido à nova evidência de liderança em projeto de migração de banco de dados, conforme feedback do Gestor C".
    *   **Responsabilidade**: O RH é responsável por finalizar as avaliações e distribuí-las aos gestores para as reuniões de feedback.

---

## Templates

### Formulário de Autoavaliação Anual (Exemplo - Analista de Dados Sênior)

```
**Nome:** Maria Silva
**Cargo:** Analista de Dados Sênior
**Período da Avaliação:** 01/01/2023 - 31/12/2023
**Gestor(a):** Carlos Pereira

**1. Conquistas e Resultados (Quais foram suas principais realizações neste período e como elas contribuíram para os objetivos da empresa?)**
*   Liderei o projeto de otimização de dashboards de vendas, resultando em uma redução de 15% no tempo de carregamento e melhoria de 20% na usabilidade, conforme feedback da equipe de vendas.
*   Desenvolvi um novo modelo de previsão de churn que, após implementação, identificou 10% mais clientes em risco com 85% de precisão, superando a meta de 80%.
*   Ministrei 3 workshops internos sobre SQL avançado para a equipe júnior, capacitando 5 novos analistas a trabalhar de forma autônoma em queries complexas.

**2. Desafios e Aprendizados (Quais foram os maiores desafios enfrentados e o que você aprendeu com eles?)**
*   Desafio: Gerenciar expectativas de múltiplas partes interessadas em projetos com escopo ambíguo.
*   Aprendizado: Aprimorei minhas habilidades de comunicação proativa, realizando checkpoints semanais formais e documentando decisões para evitar retrabalho.
*   Desafio: Implementação de uma nova ferramenta de ETL (Apache Airflow) com curva de aprendizado íngreme.
*   Aprendizado: Dediquei horas extras para estudos e certificação, e agora sou o principal ponto de contato para a ferramenta na equipe.

**3. Áreas de Desenvolvimento (Em quais áreas você busca aprimoramento e quais recursos seriam úteis?)**
*   **Habilidade:** Liderança de Projeto (gestão de cronogramas e recursos para grandes iniciativas de dados).
*   **Recursos:** Curso de Certificação PMP (Project Management Professional), mentoria com o Head de Engenharia.
*   **Habilidade:** Modelagem de Dados para Data Lakehouse (domínio de Delta Lake, Iceberg).
*   **Recursos:** Participação em conferências da área, projetos internos com essas tecnologias.

**4. Feedback para o Gestor e Empresa (O que seu gestor ou a empresa poderiam fazer para apoiar seu desenvolvimento e performance?)**
*   Gostaria de ter mais oportunidades de liderar projetos de ponta a ponta, desde a concepção até a entrega final.
*   Sugiro a criação de uma comunidade de prática interna para Analistas de Dados Sênior, para troca de conhecimentos e resolução de problemas complexos.

**Data:** 15/12/2023
**Assinatura:** Maria Silva
```

### Plano de Desenvolvimento Individual (PDI) (Exemplo - Analista de Marketing Júnior)

```
**Nome do Colaborador:** João Silva
**Cargo:** Analista de Marketing Júnior
**Gestor(a):** Laura Mendes
**Data de Criação:** 20/01/2024
**Período do PDI:** Janeiro de 2024 a Junho de 2024

**1. Objetivo Geral de Desenvolvimento (O que o colaborador busca aprimorar?)**
Aprimorar habilidades de análise de dados de marketing para otimizar campanhas e demonstrar ROI de forma mais robusta.

**2. Metas SMART do PDI (Detalhes específicos e mensuráveis para atingir o objetivo)**

*   **Meta 1:** Aumentar a proficiência em Google Analytics 4 (GA4) para um nível avançado.
    *   **Ação:** Concluir o curso "Google Analytics 4 Certification" (online) até 29/02/2024.
    *   **Ação:** Apresentar uma análise de funil de conversão baseada em GA4 para a equipe de vendas até 31/03/2024.
    *   **Métrica:** Certificação GA4 concluída; Feedback positivo da equipe de vendas sobre a análise.
*   **Meta 2:** Desenvolver relatórios de performance de campanhas de mídia paga mais acionáveis.
    *   **Ação:** Padronizar 3 novos templates de relatórios de Google Ads e Facebook Ads, incluindo métricas de Custo por Lead (CPL) e Retorno sobre Investimento em Publicidade (ROAS), até 30/04/2024.
    *   **Ação:** Apresentar e defender uma proposta de otimização de campanha baseada nos novos relatórios, resultando em uma melhoria de 10% no ROAS até 31/05/2024.
    *   **Métrica:** 3 templates de relatórios implementados; Aumento de 10% no ROAS da campanha otimizada.

**3. Recursos e Suporte Necessários (O que o colaborador precisa para atingir as metas?)**
*   **Treinamento:** Acesso a plataforma de cursos online (ex: Coursera, Udemy) para cursos de GA4 e Excel avançado.
*   **Mentoria:** Sessões quinzenais de 30 minutos com o Analista de Dados Sênior, Maria Silva, para tirar dúvidas sobre modelagem e visualização de dados.
*   **Ferramentas:** Acesso irrestrito ao Google Analytics 4 e plataformas de mídia paga para prática e análise.

**4. Indicadores de Sucesso e Acompanhamento (Como o progresso será medido e monitorado?)**
*   Reuniões quinzenais de acompanhamento com a gestora Laura Mendes para revisar progresso nas ações e metas.
*   Revisão formal do PDI em 30/06/2024 para avaliar o atingimento das metas e definir próximos passos.

**Assinatura do Colaborador:** João Silva
**Assinatura do Gestor(a):** Laura Mendes
**Data:** 20/01/2024
```

---

## Checklist

- [ ] Definir e comunicar claramente os objetivos do ciclo de performance review aos colaboradores.
- [ ] Garantir que todos os colaboradores tenham metas SMART definidas e alinhadas aos objetivos da empresa.
- [ ] Distribuir o formulário de autoavaliação com antecedência mínima de 10 dias úteis.
- [ ] Coletar feedback 360 de no mínimo 3 avaliadores por colaborador (pares, gestores, subordinados).
- [ ] Revisar autoavaliações e feedbacks, identificando inconsistências e pontos de atenção antes da reunião de calibração.
- [ ] Realizar a reunião de calibração com a liderança para garantir equidade e eliminar vieses nas avaliações.
- [ ] Documentar todas as decisões e justificativas da calibração.
- [ ] Agendar e conduzir reuniões individuais de feedback de performance com todos os colaboradores.
- [ ] Elaborar um Plano de Desenvolvimento Individual (PDI) para cada colaborador, com metas e ações claras.
- [ ] Acompanhar o progresso dos PDIs mensalmente com os gestores.

---

## Métricas de Referência

| Métrica                                | Benchmark              | Meta                   |
| :------------------------------------- | :--------------------- | :--------------------- |
| Taxa de Conclusão de Autoavaliações    | > 90%                  | 95%                    |
| Taxa de Conclusão de Feedback 360      | > 85%                  | 90%                    |
| Percentual de Avaliações Entregues no Prazo | > 95%                  | 100%                   |
| Taxa de Engajamento com PDI (follow-up) | > 70% (2+ interações)  | 80% (3+ interações)    |
| Índice de Satisfação com Processo PR (NPS) | > 40 (Promotores)      | > 50 (Promotores)      |
| % de Colaboradores com Metas SMART     | > 80%                  | 95%                    |

---

## Erros Comuns

1.  **Viés de Recência (Recency Bias)**: Gestores tendem a focar em eventos recentes (últimos 2-3 meses) em detrimento de todo o período de avaliação.
    *   **Como evitar**: Implementar um sistema de feedback contínuo durante o ano, com notas de performance documentadas trimestralmente. Exemplo: Exigir que o gestor cite no mínimo 1 exemplo de cada trimestre para justificar a avaliação final.
2.  **Falta de Documentação e Exemplos Concretos**: Avaliações vagas sem evidências específicas dificultam o feedback e a defesa da classificação.
    *   **Como evitar**: Treinar gestores para registrar "diários de feedback" com observações e exemplos ao longo do ano. Exemplo: Para classificar "Atende Expectativas em Liderança", o gestor deve ter documentado "Em 15/09, liderou a resolução do incidente X, comunicando-se eficazmente com 3 equipes".
3.  **Inflação ou Deflação de Notas sem Calibração**: Gestores avaliam de forma muito branda ou muito rígida, criando inconsistências e injustiças entre as equipes.
    *   **Como evitar**: Realizar sessões de calibração obrigatórias com um comitê de liderança e RH, utilizando a Matriz 9-Box e critérios bem definidos. Exemplo: Durante a calibração, se um gestor classifica 80% da sua equipe como "Excede Expectativas", ele é questionado a apresentar evidências robustas e comparado com outros gestores que mantêm uma distribuição mais próxima da curva de campainha.

---

## Dicas Avançadas

1.  **Integre Performance Review com OKRs (Objectives and Key Results)**: Utilize os resultados dos OKRs como base sólida para a avaliação de desempenho. Se um colaborador alcançou 80% dos seus Key Results desafiadores, isso é uma métrica quantificável forte para sua performance.
    *   **Exemplo**: Para um Product Manager, se o KR era "Aumentar a taxa de adoção do recurso X de 20% para 40%", o resultado de 38% é um dado objetivo para discutir o "como" e o "porquê" na avaliação, e não apenas o "o quê".
2.  **Utilize a Matriz 9-Box para Gestão de Talentos**: Além de classificar performance, use a Matriz 9-Box (Performance vs. Potencial) para identificar talentos de alto potencial, colaboradores que precisam de desenvolvimento intensivo ou planos de sucessão.
    *   **Exemplo**: Um "Alto Potencial, Alta Performance" (top right da 9-Box) deve receber um PDI focado em liderança e projetos estratégicos, enquanto um "Baixo Potencial, Média Performance" pode precisar de um plano de desenvolvimento corretivo ou realocação.
3.  **Implemente o "Feedback Contínuo" como Complemento**: Não espere o ciclo anual. Incentive uma cultura de feedback constante (semanal ou quinzenal) através de ferramentas (ex: 15Five, Culture Amp) para resolver problemas em tempo real e construir um banco de evidências para a avaliação formal.
    *   **Exemplo**: Um desenvolvedor recebe feedback "precisa melhorar comunicação em stand-ups" na semana 3. Ele tem 49 semanas para demonstrar melhoria, e o gestor pode documentar essa evolução, tornando a avaliação final mais precisa e menos surpreendente.
4.  **Treinamento de Liderança em Comunicação de Feedback Construtivo**: Muitos gestores evitam dar feedback negativo. Invista em treinamentos práticos de role-playing para que a liderança saiba comunicar pontos de melhoria de forma empática, clara e focada no desenvolvimento.
    *   **Exemplo**: Em vez de "Seu código é ruim", o gestor aprende a dizer "Observei que nos últimos 3 code reviews, o tempo de revisão da sua feature Y foi 50% maior que a média devido à falta de comentários e padronização. Vamos revisar juntos as diretrizes de clean code?".
5.  **Análise de Dados Agregados do Ciclo de PR**: Após cada ciclo, analise os dados agregados: distribuição de ratings por departamento, vieses de gênero/raça/idade, taxas de conclusão de PDI. Use esses insights para refinar o processo de PR no próximo ano.
    *   **Exemplo**: Se a análise mostrar que mulheres são consistentemente avaliadas com notas mais baixas em "Proatividade" em um departamento, isso pode indicar um viés inconsciente, e o RH pode intervir com treinamentos de conscientização ou revisão de critérios.