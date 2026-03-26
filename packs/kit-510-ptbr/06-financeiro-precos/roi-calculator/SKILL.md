---
name: roi-calculator
description: "Roi Calculator — Skill especializada para roi calculator"
license: MIT
metadata:
  version: 1.0.0
  author: Cafe Code AI
  category: 06-financeiro-precos
  updated: 2026-03-01
risk: critical
---

# Roi Calculator

Esta Skill capacita o Claude a calcular, analisar e otimizar o Retorno sobre o Investimento (ROI) de projetos, campanhas de marketing e aquisições, fornecendo projeções financeiras detalhadas e recomendações estratégicas.

---

## Keywords

ROI, Retorno sobre Investimento, Cálculo de ROI, Análise Financeira, Projeção de Ganhos, Custos de Projeto, Payback Period, LTV/CAC, Margem de Lucro, Break-even Point, Otimização de Investimento, Métricas de Marketing.

---

## Quick Start

1.  Obtenha o custo total do investimento (ex: R$ 50.000 para a aquisição de uma nova máquina de produção).
2.  Estime os ganhos diretos e indiretos gerados pelo investimento (ex: R$ 80.000 em aumento de capacidade produtiva e redução de falhas em um ano).
3.  Aplique a fórmula `ROI = ((Ganhos - Custos) / Custos) * 100%` para obter a porcentagem de retorno.
4.  Compare o ROI calculado com a Taxa Mínima de Atratividade (TMA) da empresa ou benchmarks do setor (ex: um ROI de 60% versus uma TMA de 15%).
5.  Utilize o resultado para justificar a alocação de capital ou ajustar o escopo do investimento.

---

## Core Workflows

### Workflow 1: Cálculo de ROI para Campanha de Marketing Digital

Este workflow detalha o processo para determinar a eficácia financeira de uma campanha de marketing digital, focando em custos e receitas diretas.

*   **Passo 1: Levantar Custos Totais da Campanha.**
    *   **Ação:** Liste e some todos os gastos diretos e indiretos associados à campanha.
    *   **Exemplo:**
        *   Anúncios Google Ads: R$ 10.000
        *   Design de criativos e vídeos: R$ 2.000
        *   Assinatura de ferramenta de automação de marketing (período da campanha): R$ 500
        *   Horas da equipe de marketing (alocadas exclusivamente): R$ 2.500
        *   **Custo Total da Campanha:** R$ 10.000 + R$ 2.000 + R$ 500 + R$ 2.500 = **R$ 15.000**

*   **Passo 2: Quantificar Ganhos Gerados pela Campanha.**
    *   **Ação:** Identifique e monetize os resultados diretos da campanha, como vendas ou leads convertidos.
    *   **Exemplo:**
        *   50 conversões de vendas diretas atribuídas à campanha.
        *   Ticket médio por venda: R$ 500
        *   **Receita Bruta Gerada:** 50 * R$ 500 = **R$ 25.000**
        *   Adicionalmente, 200 novos leads gerados com potencial de conversão futuro (considerar LTV médio ou valor de lead).

*   **Passo 3: Aplicar a Fórmula de ROI.**
    *   **Ação:** Utilize a fórmula padrão para calcular o retorno percentual.
    *   **Fórmula:** `ROI = ((Ganhos - Custos) / Custos) * 100%`
    *   **Cálculo:** `ROI = ((R$ 25.000 - R$ 15.000) / R$ 15.000) * 100%`
    *   `ROI = (R$ 10.000 / R$ 15.000) * 100% = 66.67%`

*   **Passo 4: Analisar o Período de Payback.**
    *   **Ação:** Determine em quanto tempo o investimento inicial será recuperado.
    *   **Exemplo:** Se os ganhos de R$ 25.000 foram gerados em 1 mês, e o custo foi R$ 15.000, o investimento foi recuperado dentro do período da campanha. Se a campanha fosse contínua e gerasse R$ 5.000 de lucro por mês, o payback seria R$ 15.000 / R$ 5.000 = 3 meses.

*   **Passo 5: Propor Otimizações com base no ROI.**
    *   **Ação:** Com base no ROI obtido, sugira melhorias.
    *   **Exemplo:** Um ROI de 66.67% é positivo. Para otimizar ainda mais, considere testar novos canais de mídia para reduzir o Custo por Aquisição (CPA) ou otimizar a página de destino para aumentar a taxa de conversão, buscando um ROI superior a 80%.

### Workflow 2: Análise de Viabilidade Financeira para Aquisição de Software (SaaS)

Este workflow foca na avaliação do ROI para a implementação de uma nova ferramenta de software, considerando custos recorrentes e benefícios de produtividade/economia.

*   **Passo 1: Detalhar Custos de Implementação e Operação Anual.**
    *   **Ação:** Liste todos os custos iniciais e recorrentes para adquirir e manter o software.
    *   **Exemplo:**
        *   Licença anual SaaS: R$ 12.000
        *   Treinamento inicial da equipe: R$ 3.000
        *   Serviços de consultoria para integração: R$ 5.000
        *   Horas internas de TI para suporte e manutenção (estimado anual): R$ 2.000
        *   **Custo Total 1º Ano:** R$ 12.000 + R$ 3.000 + R$ 5.000 + R$ 2.000 = **R$ 22.000**

*   **Passo 2: Estimar Benefícios Anuais (Economia e Aumento de Produtividade).**
    *   **Ação:** Quantifique os ganhos resultantes da implementação do software, como automação, redução de erros ou otimização de tempo.
    *   **Exemplo:**
        *   Automação de tarefas manuais: Economia de 20 horas/mês para 2 funcionários. Considerando custo/hora de R$ 50 por funcionário: (20 horas * 2 funcionários * R$ 50/hora * 12 meses) = R$ 24.000/ano.
        *   Redução de erros operacionais: Estimado em R$ 3.000/ano em retrabalho e perdas.
        *   **Ganhos Anuais Totais Estimados:** R$ 24.000 + R$ 3.000 = **R$ 27.000**

*   **Passo 3: Calcular o ROI Anual.**
    *   **Ação:** Aplique a fórmula de ROI para o primeiro ano de operação.
    *   **Cálculo:** `ROI = ((R$ 27.000 - R$ 22.000) / R$ 22.000) * 100%`
    *   `ROI = (R$ 5.000 / R$ 22.000) * 100% = 22.73%`

*   **Passo 4: Projetar ROI em Múltiplos Anos.**
    *   **Ação:** Considere que alguns custos (treinamento, consultoria) são pontuais, melhorando o ROI em anos subsequentes.
    *   **Exemplo (2º Ano):**
        *   Custo Anual (apenas licença e suporte interno): R$ 12.000 + R$ 2.000 = R$ 14.000
        *   Ganhos Anuais: R$ 27.000
        *   `ROI 2º Ano = ((R$ 27.000 - R$ 14.000) / R$ 14.000) * 100% = (R$ 13.000 / R$ 14.000) * 100% = 92.86%`

*   **Passo 5: Apresentar a Análise de Sensibilidade.**
    *   **Ação:** Simule o ROI sob diferentes cenários de custos e ganhos para entender a robustez do investimento.
    *   **Exemplo:**
        *   Cenário Otimista: Ganhos 10% maiores, Custos 5% menores.
        *   Cenário Pessimista: Ganhos 10% menores, Custos 5% maiores.
        *   Se no cenário pessimista o ROI cair para -5%, o risco é alto e o projeto precisa de reavaliação.

---

## Templates

### Planilha de Cálculo de ROI Simplificado

```
# Análise de Retorno sobre Investimento
Projeto/Campanha: Lançamento de Novo Aplicativo Mobile "FitLife"

## Custos do Investimento
Custo de Desenvolvimento do Aplicativo (equipe interna): R$ 180.000
Custo de Marketing e Lançamento (campanhas de aquisição): R$ 70.000
Custo de Servidores e Infraestrutura (1º ano): R$ 20.000
--------------------------------------------------
Custo Total do Investimento (C): R$ 270.000

## Ganhos Gerados pelo Investimento
Receita Incremental (1º Ano) - Assinaturas Premium e Compras In-App: R$ 450.000
Economia de Custos (ex: redução de atendimento manual por FAQ no app): R$ 10.000
--------------------------------------------------
Ganhos Totais (G): R$ 460.000

## Cálculo do ROI
Fórmula: ROI = ((G - C) / C) * 100%
ROI = ((R$ 460.000 - R$ 270.000) / R$ 270.000) * 100%
ROI = (R$ 190.000 / R$ 270.000) * 100%
ROI = 70.37%

## Análise Adicional
Período de Payback Estimado: 0.58 anos (aproximadamente 7 meses, considerando ganhos lineares)
Decisão: O projeto "FitLife" demonstra um ROI muito atrativo e um payback rápido, indicando alta viabilidade.
```

### Proposta de Investimento com Projeção de ROI

```
# Proposta de Investimento: Modernização do Parque Fabril (Máquinas CNC)

## 1. Descrição do Projeto
O projeto consiste na aquisição e instalação de duas máquinas CNC de última geração para substituir equipamentos antigos. O objetivo é aumentar a precisão, reduzir o tempo de produção e diminuir o desperdício de matéria-prima.

## 2. Custos do Investimento
Aquisição de 2 Máquinas CNC (Modelo X2000): R$ 300.000
Custos de Instalação e Calibração: R$ 30.000
Treinamento Operacional para Equipe (10 técnicos): R$ 15.000
Licenças de Software CAD/CAM (anuais, 1º ano): R$ 5.000
--------------------------------------------------
Custo Total do Investimento: R$ 350.000

## 3. Benefícios e Ganhos Projetados (Anual)
Aumento da Capacidade Produtiva (20% a mais de peças/mês): R$ 120.000
Redução de Desperdício de Matéria-Prima (15% menos sucata): R$ 40.000
Redução de Custos de Manutenção (equipamentos novos): R$ 15.000
Redução de Horas Extras de Operação (maior eficiência): R$ 25.000
--------------------------------------------------
Ganhos Anuais Totais Estimados: R$ 200.000

## 4. Projeção de ROI (Primeiro Ano)
ROI = ((Ganhos Anuais - Custo Total) / Custo Total) * 100%
ROI = ((R$ 200.000 - R$ 350.000) / R$ 350.000) * 100%
ROI = (-R$ 150.000 / R$ 350.000) * 100%
ROI = -42.86%  (Negativo no primeiro ano devido ao alto custo inicial)

## 5. Análise do Payback Period (Considerando ganhos anuais futuros)
Custos iniciais pontuais (instalação, treinamento) não se repetem.
Ganhos Anuais a partir do 2º ano (com licenças anuais de R$ 5.000): R$ 200.000 - R$ 5.000 = R$ 195.000 (lucro anual após 1º ano)
Payback Period = (Custo Total - Lucro 1º Ano) / Lucro Anual Pós 1º Ano
Payback Period = (R$ 350.000 - (R$ 200.000 - R$ 5.000)) / R$ 195.000
Payback Period = R$ 155.000 / R$ 195.000 = 0.79 anos (aproximadamente 9.5 meses após o 1º ano, totalizando 1 ano e 9.5 meses)

## 6. Conclusão e Recomendação
Apesar do ROI negativo no primeiro ano, o projeto apresenta um payback de menos de 2 anos e gera um lucro anual consistente de R$ 195.000 a partir do segundo ano. Os benefícios estratégicos em qualidade e eficiência justificam o investimento de longo prazo. Recomenda-se a aprovação.
```

---

## Checklist

- [x] Validação de todas as fontes de custo, incluindo aquisição, instalação, treinamento, licenças e manutenção.
- [x] Quantificação rigorosa de todos os ganhos (aumento de receita, economia de custos, produtividade, redução de perdas).
- [x] Consideração do valor do dinheiro no tempo para projetos com duração superior a um ano (utilizando VPL ou TIR).
- [x] Inclusão de custos de oportunidade, avaliando o que se deixa de ganhar ao investir neste projeto em detrimento de outro.
- [x] Análise de cenários (otimista, realista, pessimista) para os ganhos e custos projetados.
- [x] Cálculo do Payback Period para determinar o tempo de recuperação do investimento.
- [x] Comparação do ROI calculado com a Taxa Mínima de Atratividade (TMA) da empresa ou benchmarks do setor.
- [x] Revisão das premissas por uma segunda parte independente para identificar vieses ou omissões.
- [x] Documentação clara de todas as premissas e fontes de dados utilizadas no cálculo do ROI.
- [x] Apresentação dos riscos associados ao não alcance do ROI projetado e planos de mitigação.

---

## Métricas de Referência

| Métrica               | Benchmark (geral)                                         | Meta (para projetos de alto impacto)                     |
| :-------------------- | :-------------------------------------------------------- | :------------------------------------------------------- |
| ROI (Retorno)         | 15% - 25% (para a maioria dos investimentos)              | > 30% (indicando forte potencial de crescimento)         |
| Payback Period        | < 2 anos (para investimentos de capital)                  | < 12 meses (para campanhas de marketing ou SaaS)         |
| LTV:CAC (Marketing)