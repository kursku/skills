---
name: payment-terms
description: "Payment Terms — Skill especializada para payment terms"
license: MIT
metadata:
  version: 1.0.0
  author: Cafe Code AI
  category: 06-financeiro-precos
  updated: 2026-03-01
risk: safe
---

# Payment Terms

Esta skill capacita o Claude a otimizar a gestão de termos de pagamento, focando na maximização do fluxo de caixa, mitigação de riscos de inadimplência e manutenção de relacionamentos comerciais saudáveis.

---

## Keywords

Prazo de Pagamento, Net 30/60/90, Desconto por Antecipação, Multa por Atraso, Juros de Mora, Capital de Giro, Risco de Crédito, Fluxo de Caixa, Inadimplência, Cláusulas Contratuais, Ciclo de Recebimento, Days Sales Outstanding (DSO), Custo de Capital, Fatoring.

---

## Quick Start

1.  **Analisar perfil de crédito do cliente**: Antes de qualquer negociação, consultar Serasa Experian (Ex: Score de crédito 0-1000) e histórico de pagamentos anteriores.
2.  **Propor termos de pagamento iniciais**: Para um novo cliente B2B com score de 750, sugerir "Net 30" (pagamento em 30 dias líquidos) como padrão.
3.  **Estabelecer incentivos/penalidades**: Oferecer 2% de desconto para pagamento em 10 dias ou aplicar multa de 2% mais juros de 1% ao mês sobre atrasos.
4.  **Formalizar os termos**: Inserir os termos de pagamento de forma explícita na proposta comercial, contrato de serviço e fatura.
5.  **Monitorar vencimentos**: Configurar lembretes automáticos para 5 dias antes do vencimento e no dia do vencimento da fatura.

---

## Core Workflows

### Workflow 1: Definição e Negociação Estratégica de Termos de Pagamento

Este workflow detalha o processo de estabelecer e negociar termos de pagamento que equilibram o risco, o fluxo de caixa e a competitividade.

1.  **Avaliação do Risco de Crédito e Segmentação de Clientes**:
    *   **Coletar Dados**: Obter informações de crédito do cliente (Score Serasa/SPC, histórico de pagamentos com outros fornecedores via referências comerciais).
    *   **Segmentar Clientes**:
        *   **Alto Risco (Score < 400)**: Exigir pagamento antecipado (100% adiantado) ou 50% adiantado e 50% no momento da entrega, com garantias.
        *   **Médio Risco (Score 400-700)**: Oferecer "Net 15" ou "Net 30" com análise de volume.
        *   **Baixo Risco (Score > 700)**: Oferecer "Net 30" ou "Net 45", com possibilidade de "Net 60" para grandes volumes e histórico comprovado.
    *   **Exemplo Prático**: Uma empresa de software vende uma licença de R$50.000. Para um cliente com Score Serasa de 820 e histórico de 3 anos sem atrasos, propõe "Net 45". Para outro cliente, novo, com Score 550, exige 30% adiantado (R$15.000) e o restante em "Net 30" (R$35.000).

2.  **Cálculo do Custo de Capital e Impacto nos Termos**:
    *   **Determinar o Custo de Capital de Giro**: Considerar a taxa SELIC atual (ex: 10,75% ao ano) e adicionar um spread de risco da empresa (ex: 3% ao ano) para obter um custo de capital de 13,75% ao ano, ou 1.14% ao mês. Este é o custo de "financiar" o cliente.
    *   **Impacto no Markup e Margem**:
        *   **Markup**: `(Preço de Venda - Custo) / Custo`. Se o custo de um produto é R$100 e o preço de venda é R$150, o markup é 50%.
        *   **Margem de Lucro**: `(Preço de Venda - Custo) / Preço de Venda`. No exemplo acima, (R$150 - R$100) / R$150 = 33,33%.
        *   **Custo do Prazo**: Se um prazo "Net 60" custa 2.28% do valor da fatura (1.14% * 2 meses), um produto de R$10.000 terá um custo de R$228 apenas pelo prazo. Este custo deve ser embutido no preço ou considerado na margem.
    *   **Exemplo de Negociação de Desconto**: Para uma fatura de R$10.000 com prazo "Net 60", a empresa oferece 3% de desconto (R$300) para pagamento em "Net 15". O cliente economiza R$300 e a empresa antecipa R$9.700, reduzindo seu custo de capital. Se o custo do capital para 45 dias (60-15) é de R$256 (R$10.000 * 1.14% * 1.5 meses), o desconto de R$300 é ligeiramente maior, mas o ganho no fluxo de caixa pode justificar.

3.  **Elaboração de Cláusulas Contratuais e Propostas**:
    *   **Detalhar Prazos**: "Pagamento em 30 (trinta) dias corridos a contar da data de emissão da Nota Fiscal."
    *   **Condições de Desconto**: "Desconto de 2% (dois por cento) para pagamentos realizados em até 10 (dez) dias corridos da data da fatura."
    *   **Penalidades por Atraso**: "Multa de 2% (dois por cento) sobre o valor total em atraso, acrescido de juros de mora de 1% (um por cento) ao mês (pro rata die) e atualização monetária pelo IPCA/IBGE."
    *   **Exemplo de Ponto de Equilíbrio**: Uma empresa precisa vender 500 unidades de um produto por mês para cobrir seus custos fixos e variáveis. Se a concessão de prazos de pagamento muito longos reduz o fluxo de caixa e impede a produção dessas 500 unidades, os termos de pagamento impactam diretamente o ponto de equilíbrio (`Custos Fixos / (Preço de Venda por Unidade - Custos Variáveis por Unidade)`).

### Workflow 2: Gestão de Cobrança e Otimização do Ciclo de Recebimento

Este workflow foca na gestão proativa e reativa de contas a receber para minimizar a inadimplência e acelerar o ciclo de caixa.

1.  **Monitoramento Ativo de Contas a Receber**:
    *   **Sistema de Gestão**: Utilizar um ERP (Ex: Totvs, SAP, Omie) ou uma planilha de controle de contas a receber com datas de vencimento, valores, e status de pagamento.
    *   **Relatórios de Aging**: Gerar relatórios que categorizam faturas por tempo de vencimento (Ex: 0-30 dias, 31-60 dias, >90 dias).
    *   **Exemplo de Relatório**:
        | Cliente | Fatura | Valor (R$) | Vencimento | Status | Dias Atraso |
        |---------|--------|------------|------------|--------|-------------|
        | Alfa Ltda | 2024/001 | 5.000,00 | 2024-03-10 | Em Atraso | 15          |
        | Beta S.A. | 2024/002 | 12.000,00 | 2024-03-25 | A Vencer | -           |
        | Gama Ind. | 2024/003 | 8.000,00 | 2024-02-15 | Pago     | -           |

2.  **Estratégias de Comunicação de Cobrança**:
    *   **Lembretes Pré-Vencimento**: Enviar e-mails ou SMS 5 dias antes do vencimento e no dia do vencimento.
    *   **Notificações Pós-Vencimento**:
        *   **D+1 a D+5**: Email amigável lembrando sobre o atraso.
        *   **D+6 a D+15**: Email com menção às cláusulas de multa e juros.
        *   **D+16 a D+30**: Ligação telefônica e e-mail mais incisivo, propondo renegociação.
    *   **Cálculo de Multa e Juros**: Para uma fatura de R$5.000,00 com 15 dias de atraso, aplicando multa de 2% e juros de 1% ao mês:
        *   `Multa = R$5.000,00 * 0.02 = R$100,00`
        *   `Juros de Mora = R$5.000,00 * (0.01 / 30) * 15 = R$25,00`
        *   `Total Devido = R$5.000,00 + R$100,00 + R$25,00 = R$5.125,00`

3.  **Análise de Rentabilidade da Cobrança e Renegociação**:
    *   **Avaliar LTV (LifeTime Value) vs. CAC (Customer Acquisition Cost)**:
        *   `LTV = Valor Médio da Compra * Frequência de Compra * Vida Útil do Cliente`
        *   `CAC = Custo Total de Marketing e Vendas / Número de Novos Clientes`
        *   Se um cliente inadimplente tem um LTV alto e um bom histórico geral, vale a pena investir mais na renegociação para retê-lo, talvez abatendo parte dos juros em troca de um pagamento imediato.
    *   **Exemplo de Renegociação**: Cliente com fatura de R$10.000 em atraso há 60 dias, com juros e multa totalizando R$10.400. Propõe pagar R$9.800 à vista. A empresa calcula que o custo de adquirir um novo cliente com o mesmo LTV é R$1.500. Aceitar R$9.800 significa uma perda de R$200, mas evita o custo de R$1.500 de um novo cliente e mantém o relacionamento. A decisão é positiva.
    *   **Opções de Renegociação**: Parcelamento da dívida, desconto em juros e multas para pagamento à vista, troca por produtos/serviços.

---

## Templates

### Cláusula de Termos de Pagamento em Contrato de Prestação de Serviços

```markdown
**CLÁUSULA QUINTA – DOS PAGAMENTOS E CONDIÇÕES**

5.1. O CONTRATANTE efetuará o pagamento dos serviços descritos na Cláusula Primeira, conforme condições comerciais acordadas e detalhadas na Proposta Comercial nº [NÚMERO_PROPOSTA] e nas Notas Fiscais/Faturas emitidas pela CONTRATADA.

5.2. O prazo padrão para pagamento será de **30 (trinta) dias corridos** a contar da data de emissão da Nota Fiscal de Prestação de Serviços.

5.3. Em caso de atraso no pagamento, incidirá sobre o valor devido:
    a) Multa moratória de **2% (dois por cento)** sobre o valor total em aberto.
    b) Juros de mora de **1% (um por cento) ao mês**, calculados pro rata die.
    c) Atualização monetária pelo Índice Nacional de Preços ao Consumidor Amplo (IPCA/IBGE) desde a data de vencimento até a data do efetivo pagamento.

5.4. A CONTRATADA poderá, a seu exclusivo critério, oferecer descontos por antecipação de pagamento, conforme condições a serem negociadas e expressamente formalizadas por escrito.

5.5. O não pagamento de qualquer valor devido por mais de 15 (quinze) dias após o vencimento, após notificação da CONTRATADA, implicará na suspensão imediata da prestação dos serviços até a regularização da pendência, sem prejuízo da cobrança dos valores em atraso e dos encargos moratórios.
```

### E-mail de Lembrete Pré-Vencimento (5 Dias Antes)

```markdown
**Assunto: Lembrete de Pagamento - Fatura [NÚMERO DA FATURA] - Vencimento em 5 dias**

Prezado(a) [NOME DO CLIENTE],

Esperamos que esteja tudo bem!

Este é um lembrete amigável de que sua fatura [NÚMERO DA FATURA], no valor de R$ [VALOR DA FATURA], referente aos serviços de [DESCRIÇÃO BREVE DOS SERVIÇOS/PRODUTOS], vencerá em 5 dias, no dia **[DATA DE VENCIMENTO]**.

Para sua conveniência, segue o link para visualização e pagamento da fatura: [LINK PARA FATURA/PORTAL DO CLIENTE]
(Anexo: [NOME DO ARQUIVO DA FATURA].pdf)

Caso já tenha efetuado o pagamento, por favor, desconsidere este e-mail. Agradecemos a sua parceria e estamos à disposição para qualquer dúvida.

Atenciosamente,

[SEU NOME/NOME DA EMPRESA]
[SEU TELEFONE]
[SEU E-MAIL]
```

---

## Checklist

- [x] Avaliar o histórico de crédito do novo cliente (Serasa Experian/SPC) antes de definir os termos.
- [x] Segmentar clientes e aplicar políticas de prazos de pagamento diferenciadas (ex: Net 15, Net 30, Net 60).
- [x] Incluir claramente os termos de pagamento, multas e juros em propostas e contratos.
- [x] Calcular o custo de capital de giro e o impacto de prazos de 30, 60 e 90 dias no fluxo de caixa.
- [x] Estabelecer multas e juros por atraso conforme legislação vigente (Código Civil, SELIC + spread).
- [x] Configurar lembretes de pagamento automáticos (5 dias antes, no vencimento, 3 dias após).
- [x] Treinar a equipe de vendas sobre a importância da negociação e formalização dos termos de pagamento.
- [x] Analisar o Days Sales Outstanding (DSO) mensalmente e compará-lo com metas internas e benchmarks do setor.
- [x] Ter um plano de renegociação de dívidas claro para clientes de alto LTV.
- [x] Considerar a oferta de descontos por antecipação de pagamento com base no custo de capital.

---

## Métricas de Referência

| Métrica                      | Benchmark (Mercado B2B Brasil) | Meta (Empresa)         |
|------------------------------|--------------------------------|------------------------|
| **Days Sales Outstanding (DSO)** | 35 a 55 dias                   | 30 dias                |
| **Percentual de Inadimplência** | 1,5% a 3,0% (sobre faturamento) | Inferior a 1,0%        |
| **Custo Médio de Capital (WACC)** | 12% a 18% a.a.                 | SELIC + 3% a.a.        |
| **Taxa de Desconto por Antecipação** | 1% a 3% (para 15-30 dias)      | 2% para Net 10         |
| **LTV:CAC Ratio**            | 3:1 ou superior                | 4:1 ou superior        |

---

## Erros Comuns

1.  **Não formalizar os termos de pagamento**: Confiar em acordos verbais ou em minutas incompletas leva a disputas e atrasos. Para evitar, sempre inclua os termos detalhados em propostas, contratos e faturas, com assinaturas ou aceite digital. Ex: "A fatura foi enviada por e-mail, mas o cliente alega não ter visto as condições." Solução: Exigir "De acordo" explícito no e-mail ou sistema.
2.  **Conceder prazos longos sem avaliar o risco de crédito**: Oferecer "Net 90" a um cliente novo ou com score baixo aumenta drasticamente o risco de inadimplência. Para evitar, utilize ferramentas de análise de crédito (Serasa, SPC) e exija garantias ou adiantamento para perfis de alto risco. Ex: Cliente novo pediu Net 60, foi concedido e atrasou 120 dias. Solução: Para novos clientes, iniciar com Net 30 e monitorar o primeiro pagamento.
3.  **Não cobrar juros e multas por atraso**: A ausência de penalidades incentiva a inadimplência e prejudica o fluxo de caixa. Para evitar, aplique consistentemente as multas e juros previstos em contrato e comunique claramente ao cliente. Ex: Empresa nunca cobrou juros, e os clientes passaram a atrasar sabendo que não haveria custo extra. Solução: Enviar comunicação reforçando a política de juros e multa e aplicá-la rigorosamente.
4.  **Não ter uma política clara de renegociação**: A falta de diretrizes para clientes inadimplentes pode resultar na perda de clientes valiosos ou na prolongação de dívidas irrecuperáveis. Para evitar, estabeleça alçadas e condições para parcelamento, descontos e abatimentos, focando no LTV do cliente. Ex: Cliente com 5 anos de parceria atrasou devido a uma crise. Solução: Oferecer um plano de parcelamento flexível, talvez com abatimento de juros, para manter o relacionamento.

---

## Dicas Avançadas

1.  **Fatoring ou Securitização de Recebíveis Dinâmicos**: Em vez de apenas vender faturas, explore plataformas que permitem vender recebíveis seletivamente, conforme a necessidade de caixa. Ex: Vender uma fatura de R$ 50.000 (Net 60) por R$ 48.500 (deságio de 3%) para cobrir uma despesa urgente, liberando capital antes do prazo usual.
2.  **Modelagem de Fluxo de Caixa com Simulação de Prazos**: Utilize ferramentas de modelagem financeira (Excel, Power BI) para simular o impacto de diferentes cenários de prazos de pagamento (ex: 20% dos clientes pagam em Net 15, 60% em Net 30, 20% em Net 60) no seu fluxo de caixa mensal. Isso permite projeções mais precisas de capital de giro necessário.
3.  **Incentivos para Pagamento Antecipado Progressivos**: Em vez de um único desconto, crie uma escala. Ex: Fatura de R$10.000 (Net 60). Ofereça 4% de desconto para pagamento em 7 dias, 2,5% para pagamento em 15 dias, e 1% para pagamento em 30 dias. Isso maximiza a chance de antecipação.
4.  **Contratos de Garantia e Seguros de Crédito**: Para vendas de alto valor ou clientes de médio/alto risco, exija garantias reais (aval, fiança bancária) ou contrate seguros de crédito. Ex: Venda de equipamento de R$200.000 para um cliente novo. Exigir uma carta de fiança de R$50.000 pode mitigar o risco de inadimplência.
5.  **Análise de KPIs de Adimplência por Segmento de Produto/Serviço**: Monitore o DSO e a taxa de inadimplência não apenas por cliente, mas também por tipo de produto ou serviço. Isso pode revelar que certos produtos ou serviços atraem clientes com maior tendência a atrasar, permitindo ajustar a política de termos especificamente para esses segmentos. Ex: Serviços de consultoria tendem a ter DSO de 40 dias, enquanto venda de software pode ter DSO de 25 dias.