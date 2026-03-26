---
name: expense-tracker-template
description: "Expense Tracker Template — Skill especializada para expense tracker template"
license: MIT
metadata:
  version: 1.0.0
  author: Cafe Code AI
  category: 06-financeiro-precos
  updated: 2026-03-01
risk: safe
---

# Expense Tracker Template

Esta skill permite ao Claude gerenciar, categorizar e analisar despesas de forma estruturada, utilizando templates e workflows práticos para um controle financeiro apurado.

---

## Keywords

gastos, despesas, orçamento, controle financeiro, fluxo de caixa, categorização de despesas, análise de gastos, planilha de despesas, monitoramento financeiro, custos fixos, custos variáveis, previsão de gastos, saúde financeira, relatórios de despesas.

---

## Quick Start

1.  **Definir Categorias Iniciais**: Estabelecer categorias macro como "Moradia", "Transporte", "Alimentação", "Lazer" para iniciar o registro.
2.  **Registrar a Primeira Despesa**: Inserir uma despesa recente (ex: "Almoço", R$ 45,00, Categoria "Alimentação", Data "2024-07-26").
3.  **Configurar Despesas Recorrentes**: Identificar e pré-preencher despesas mensais fixas como aluguel (R$ 2.500,00) ou assinatura de software (R$ 89,90).
4.  **Gerar Resumo Semanal**: Agrupar as despesas registradas nos últimos 7 dias para identificar rapidamente os principais gastos do período.
5.  **Revisar Limites de Gastos**: Comparar os gastos de uma categoria específica (ex: "Lazer") com um limite autoimposto (ex: R$ 500,00/mês).

---

## Core Workflows

### Workflow 1: Registro Detalhado e Categorização Inteligente de Despesas

Este workflow capacita o Claude a registrar cada despesa com precisão, atribuindo-a à categoria e subcategoria corretas, o que é fundamental para uma análise financeira robusta. O objetivo é garantir que cada transação seja capturada com metadados relevantes.

1.  **Coleta de Dados da Transação**:
    *   **Input**: Recebe os detalhes brutos de uma despesa.
    *   **Exemplo**: "Paguei R$ 120,00 no supermercado no dia 25/07/2024 usando Pix. Comprei itens de mercearia e produtos de limpeza."
2.  **Identificação de Atributos Essenciais**:
    *   **Ação**: Extrair `Data`, `Valor`, `Forma de Pagamento`, `Descrição` e `Observações`.
    *   **Exemplo**:
        *   `Data`: 2024-07-25
        *   `Valor`: 120.00
        *   `Forma de Pagamento`: Pix
        *   `Descrição`: Supermercado
        *   `Observações`: Itens de mercearia e produtos de limpeza
3.  **Sugestão e Atribuição de Categoria e Subcategoria**:
    *   **Ação**: Com base na `Descrição` e `Observações`, o Claude sugere e atribui a categoria e subcategoria mais adequadas. Se houver dúvida, solicita confirmação.
    *   **Exemplo**:
        *   `Categoria Sugerida`: Alimentação
        *   `Subcategoria Sugerida`: Compras de Supermercado
        *   **Confirmação**: "Deseja confirmar 'Alimentação > Compras de Supermercado' para esta despesa?"
4.  **Registro no Template de Despesas**:
    *   **Ação**: Insere os dados formatados em uma nova linha do template de registro de despesas.
    *   **Exemplo de Saída (linha da planilha)**:
        `2024-07-25 | Supermercado | Alimentação | Compras de Supermercado | 120.00 | Pix | Itens de mercearia e produtos de limpeza`

### Workflow 2: Análise Periódica e Projeção de Gastos

Este workflow permite ao Claude realizar análises agregadas de despesas em períodos definidos e projetar gastos futuros, auxiliando na tomada de decisões financeiras e no planejamento orçamentário.

1.  **Definição do Período de Análise**:
    *   **Input**: Define o intervalo de tempo para a análise (ex: "mês de julho", "último trimestre").
    *   **Exemplo**: "Quero analisar as despesas de Julho de 2024."
2.  **Agregação de Despesas por Categoria**:
    *   **Ação**: Soma todos os valores de despesas para cada categoria e subcategoria dentro do período.
    *   **Exemplo (dados brutos agregados)**:
        *   Alimentação: R$ 850,00
        *   Transporte: R$ 320,00
        *   Moradia: R$ 2.800,00
        *   Lazer: R$ 450,00
3.  **Comparação com Orçamento (se disponível)**:
    *   **Ação**: Se houver um orçamento pré-definido, compara o `Realizado` com o `Orçado` para cada categoria.
    *   **Exemplo**:
        *   Categoria: Alimentação | Orçado: R$ 900,00 | Realizado: R$ 850,00 | Diferença: R$ 50,00 (economia)
4.  **Identificação de Maiores Gastos e Tendências**:
    *   **Ação**: Destaca as categorias com os maiores gastos e identifica padrões de aumento ou redução.
    *   **Exemplo**: "A categoria 'Moradia' representa 55% do total das despesas de Julho. 'Lazer' teve um aumento de 15% em relação ao mês anterior, impulsionado por uma viagem de fim de semana."
5.  **Projeção de Gastos Futuros**:
    *   **Ação**: Com base em dados históricos (mínimo 3 meses), projeta os gastos esperados para os próximos meses, ajustando para despesas sazonais ou conhecidas.
    *   **Fórmula Simples**: `Média Mensal = (Soma dos Gastos dos Últimos N Meses) / N`
    *   **Exemplo**: "Com base nos últimos 3 meses, a projeção para 'Alimentação' é de R$ 870,00/mês. Em Setembro, espera-se um aumento de R$ 150,00 em 'Educação' devido à matrícula em um curso."

---

## Templates

### Template de Registro de Despesas Diárias (Planilha)

```
Data        | Descrição              | Categoria     | Subcategoria          | Valor (R$) | Forma de Pgto | Observações
------------|------------------------|---------------|-----------------------|------------|---------------|------------------------------------------------
2024-07-01  | Aluguel                | Moradia       | Habitação             | 2500.00    | Boleto        | Vencimento dia 05
2024-07-03  | Assinatura Netflix     | Lazer         | Entretenimento        | 55.90      | Cartão Créd.  | Plano premium
2024-07-05  | Supermercado Pão Bom   | Alimentação   | Compras de Supermerc. | 185.75     | Débito        | Compras da semana
2024-07-08  | Gasolina Posto X       | Transporte    | Combustível           | 110.00     | Cartão Créd.  | Tanque cheio
2024-07-12  | Almoço Restaurante Y   | Alimentação   | Refeição Fora         | 48.50      | Pix           | Encontro com cliente
2024-07-15  | Energia Elétrica       | Moradia       | Contas de Consumo     | 210.30     | Boleto        | Consumo Junho
2024-07-19  | Uber para aeroporto    | Transporte    | Aplicativos           | 72.00      | Cartão Créd.  | Viagem de negócios
2024-07-22  | Consulta Médica        | Saúde         | Consultas             | 250.00     | Pix           | Consulta de rotina
2024-07-25  | Livro "Economia Fácil" | Educação      | Livros                | 79.90      | Cartão Créd.  | Para estudo
```

### Template de Resumo Mensal de Despesas por Categoria (Planilha)

```
Mês/Ano: Julho/2024

Categoria         | Orçado (R$) | Realizado (R$) | Diferença (R$) | % do Total Realizado
------------------|-------------|----------------|----------------|----------------------
Moradia           | 2800.00     | 2710.30        | 89.70          | 47.9%
Alimentação       | 900.00      | 870.50         | 29.50          | 15.4%
Transporte        | 400.00      | 385.00         | 15.00          | 6.8%
Lazer             | 500.00      | 455.90         | 44.10          | 8.1%
Saúde             | 200.00      | 250.00         | -50.00         | 4.4%
Educação          | 100.00      | 79.90          | 20.10          | 1.4%
Outros            | 300.00      | 150.00         | 150.00         | 2.6%
------------------|-------------|----------------|----------------|----------------------
TOTAL             | 5300.00     | 4901.60        | 398.40         | 100.0%
```

---

## Checklist

- [x] Categorias e subcategorias de despesas estão claramente definidas (ex: Moradia > Aluguel, Alimentação > Compras de Supermercado).
- [x] Todas as despesas, independentemente do valor, são registradas no template.
- [x] Despesas recorrentes (aluguel, assinaturas) estão pré-configuradas para registro automático.
- [x] Notas e observações adicionais são incluídas para contexto em cada registro de despesa.
- [x] O método de pagamento (Pix, crédito, débito, dinheiro) é sempre especificado.
- [x] Orçamento mensal para cada categoria de despesa foi estabelecido e é monitorado.
- [x] O resumo mensal de despesas é gerado e analisado para identificar desvios do orçamento.
- [x] Conciliação de despesas com extratos bancários e faturas de cartão de crédito é realizada semanalmente.
- [x] Tendências de gastos por categoria são revisadas trimestralmente para ajustes no orçamento.
- [x] Despesas sazonais (ex: IPVA, matrícula escolar) são antecipadas e planejadas no orçamento.

---

## Métricas de Referência

| Métrica                        | Benchmark (Pessoal/Doméstico) | Meta (Exemplo) |
|--------------------------------|-------------------------------|----------------|
| % de Renda Gasta               | 50-70%                        | < 60%          |
| % de Despesas Fixas sobre Total| 40-60%                        | < 50%          |
| % de Despesas Variáveis sobre Total | 20-40%                        | < 30%          |
| Razão Dívida/Renda             | < 36% (excluindo hipoteca)    | < 25%          |
| Economia Mensal (R$)           | 10-20% da renda líquida       | R$ 1.500,00    |
| Custo por Refeição Fora (R$)   | R$ 30 - R$ 80                 | < R$ 50,00     |

---

## Erros Comuns

1.  **Categorização Genérica ou Inconsistente**: Despesas são agrupadas de forma muito ampla (ex: tudo como "Outros") ou sob categorias que mudam a cada registro.
    *   **Como evitar**: Crie uma lista padronizada de categorias e subcategorias (ex: "Transporte > Combustível", "Transporte > Manutenção") e utilize-a rigorosamente. Para novas despesas, adicione uma nova subcategoria se necessário, mas evite criar categorias principais desnecessariamente.
2.  **Omissão de Pequenas Despesas**: O "cafézinho" diário, a balinha ou a gorjeta são ignorados por serem de baixo valor, mas somam-se a quantias significativas ao longo do mês.
    *   **Como evitar**: Desenvolva o hábito de registrar *toda* e qualquer saída de dinheiro, por menor que seja. Utilize aplicativos de rastreamento rápido ou faça um registro ao final do dia com todas as pequenas despesas acumuladas. Um valor de R$ 5,00 por dia útil, por exemplo, representa R$ 110,00 em um mês com 22 dias úteis.
3.  **Falta de Revisão Periódica**: O registro das despesas é feito, mas a análise dos dados acumulados é negligenciada, perdendo a oportunidade de identificar padrões e tomar decisões.
    *   **Como evitar**: Agende um tempo fixo na sua semana (ex: 30 minutos na sexta-feira) ou no seu mês (ex: 1 hora no primeiro dia útil) para revisar o resumo de despesas, comparar com o orçamento e analisar as tendências. Isso permite ajustar o curso antes que os gastos saiam do controle.

---

## Dicas Avançadas

1.  **Regra 50/30/20 Aplicada**: Utilize o rastreador de despesas para alocar sua renda em 50% para `Necessidades` (Moradia, Alimentação básica), 30% para `Desejos` (Lazer, Refeições fora, Compras não essenciais) e 20% para `Poupança/Dívidas` (Investimentos, Quitação de dívidas). Monitore ativamente se suas categorias de despesa se encaixam nessas proporções.
2.  **Análise de Custo por Unidade ou Frequência**: Além do valor total, registre métricas contextuais para despesas recorrentes. Ex: "Custo por litro de gasolina", "Custo por refeição em casa", "Custo por viagem de aplicativo". Isso permite comparações mais justas e identificação de eficiências.
    *   **Exemplo**: Observar que o "Custo por refeição em casa" é R$ 15,00 versus R$ 45,00 "Custo por refeição fora" pode incentivar mais preparo em casa.
3.  **Projeção de Cenários "E se..."**: Utilize os dados históricos para simular o impacto de mudanças nas despesas.
    *   **Exemplo**: "E se eu reduzir minhas despesas com 'Lazer' em 20%? Quanto eu economizaria em 6 meses? `(Gasto Lazer Mensal * 0.20) * 6`". Ou "E se o preço do combustível subir 10%? Qual o impacto no meu orçamento de 'Transporte'?".
4.  **Sistema de "Envelopes Digitais"**: Aloque mentalmente (ou fisicamente em contas separadas) um valor específico para certas categorias de gastos variáveis no início do mês.
    *   **Exemplo**: "Tenho R$ 500 para 'Lazer' este mês. Cada despesa de lazer é abatida desse 'envelope', e quando ele zera, não há mais gastos nessa categoria até o próximo mês." Isso ajuda a controlar gastos impulsivos.
5.  **Cálculo de Custo de Oportunidade para Grandes Despesas**: Para compras de alto valor, avalie não apenas o custo direto, mas o que aquele dinheiro *poderia render* se investido.
    *   **Exemplo**: Comprar um carro de R$ 80.000,00 versus investir esse valor a 1% ao mês. O custo de oportunidade mensal seria R$ 800,00 de juros não recebidos, além da depreciação e manutenção.

---