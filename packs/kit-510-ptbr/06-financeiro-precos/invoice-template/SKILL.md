---
name: invoice-template
description: "Invoice Template — Skill especializada para invoice template"
license: MIT
metadata:
  version: 1.0.0
  author: Cafe Code AI
  category: 06-financeiro-precos
  updated: 2026-03-01
risk: offensive
---

# Invoice Template

Esta skill capacita o Claude a gerar, validar e otimizar modelos de faturas comerciais, garantindo conformidade fiscal, clareza financeira e eficiência na cobrança.

---

## Keywords

Fatura comercial, Nota fiscal de serviço, Nota fiscal de produto, Recibo de pagamento, Cobrança, Débito, Crédito, Impostos, IVA, ICMS, ISS, PIS, COFINS, IRRF, CSLL, Retenção, Prazo de pagamento, Condições de pagamento, Boleto, PIX, Transferência bancária, Proforma invoice, Recorrência, Desconto, Adiantamento, Remessa, Exportação, Importação.

---

## Quick Start

1.  **Gere uma fatura de serviço**: Solicite um modelo de fatura para consultoria de TI com retenção de impostos (ISS, PIS, COFINS, CSLL, IRRF) para o município de São Paulo.
2.  **Valide campos obrigatórios**: Verifique se um rascunho de fatura de venda de software contém todos os dados essenciais do emissor, tomador, descrição do produto e informações fiscais.
3.  **Crie uma fatura recorrente**: Desenvolva um template para cobrança mensal de assinatura de SaaS, incluindo período de referência e instruções de pagamento via PIX.
4.  **Otimize condições de pagamento**: Sugira termos de pagamento (ex: "30 dias líquidos") e adicione cláusulas de juros e multa por atraso.

---

## Core Workflows

### Workflow 1: Geração de Fatura de Serviço com Retenção de Impostos

Este workflow detalha a emissão de uma fatura para prestação de serviços no Brasil, considerando a aplicação e retenção de impostos federais e municipais.

1.  **Reunir Dados Essenciais do Serviço**:
    *   **Emissor**: Razão Social, CNPJ, Inscrição Municipal/Estadual, Endereço completo, Telefone, E-mail.
    *   **Tomador (Cliente)**: Razão Social, CNPJ, Inscrição Municipal/Estadual (se aplicável), Endereço completo, Contato (Nome, E-mail, Telefone).
    *   **Descrição do Serviço**: Detalhamento claro do serviço prestado (ex: "Consultoria em Implementação de Sistema CRM - Fase 1"), período de execução (ex: "01/10/2023 a 31/10/2023").
    *   **Valor Bruto**: Preço total do serviço (ex: R$ 12.000,00).

2.  **Identificar Impostos e Alíquotas Aplicáveis**:
    *   Para serviços, geralmente aplicam-se ISS (municipal) e, dependendo do regime tributário e atividade, PIS, COFINS, CSLL e IRRF (federais).
    *   **Exemplo (Empresa no Lucro Presumido, serviço de consultoria, cliente PJ):**
        *   ISS (Município de São Paulo): 5%
        *   PIS: 0,65%
        *   COFINS: 3%
        *   CSLL: 1%
        *   IRRF: 1,5%

3.  **Calcular Valores Retidos e Líquidos**:
    *   **ISS**: R$ 12.000,00 * 5% = R$ 600,00
    *   **PIS**: R$ 12.000,00 * 0,65% = R$ 78,00
    *   **COFINS**: R$ 12.000,00 * 3% = R$ 360,00
    *   **CSLL**: R$ 12.000,00 * 1% = R$ 120,00
    *   **IRRF**: R$ 12.000,00 * 1,5% = R$ 180,00
    *   **Total de Retenções**: R$ 600,00 + R$ 78,00 + R$ 360,00 + R$ 120,00 + R$ 180,00 = R$ 1.338,00
    *   **Valor Líquido a Receber**: R$ 12.000,00 - R$ 1.338,00 = R$ 10.662,00

4.  **Definir Condições de Pagamento**:
    *   **Prazo**: Ex: "30 dias líquidos" ou "Vencimento em 20/11/2023".
    *   **Forma**: Transferência bancária (dados da conta), PIX (chave), Boleto (link ou código de barras).
    *   **Penalidades**: Multa de 2% e juros de 1% ao mês por atraso.

5.  **Preencher o Template da Fatura**: Inserir todos os dados calculados e definidos no modelo de fatura. (Ver Template 1 na seção seguinte).

### Workflow 2: Otimização de Template de Fatura para Cobrança Recorrente

Este workflow foca na criação de um template de fatura para serviços ou produtos de assinatura, visando clareza e automação.

1.  **Padronizar Descrição do Item**:
    *   Para serviços recorrentes como SaaS, mensalidades de consultoria ou licenciamento de software, a descrição deve ser consistente.
    *   **Exemplo**: "Assinatura Mensal - Plano Gold - Software 'Gestão Pro' - Licença #AB1234".
    *   **Importante**: Sempre incluir o período de referência (ex: "Referente ao período de 01/11/2023 a 30/11/2023").

2.  **Configurar Informações do Ciclo de Cobrança**:
    *   **Frequência**: Mensal, Trimestral, Anual.
    *   **Data de Vencimento Padrão**: Definir um dia fixo do mês (ex: dia 10 de cada mês).
    *   **Data de Emissão**: Pode ser alguns dias antes do vencimento para dar tempo de processamento.

3.  **Incluir Detalhes do Contrato ou Plano**:
    *   Referenciar o contrato ou plano de assinatura para facilitar a auditoria e o entendimento do cliente.
    *   **Exemplo**: "Conforme Contrato de Assinatura nº 2023-005".

4.  **Otimizar Instruções de Pagamento para Recorrência**:
    *   **PIX**: Chave PIX (CNPJ/E-mail/Telefone) ou, preferencialmente, um QR Code PIX dinâmico que já inclua o valor e identificador da fatura para conciliação automática.
    *   **Boleto**: Gerar um link direto para o boleto bancário ou o código de barras para digitação.
    *   **Cartão de Crédito**: Link para página de pagamento seguro (se aplicável).
    *   **Exemplo**: "Efetue o pagamento via PIX (chave: 12.345.678/0001-90) ou acesse o boleto em [link_para_boleto]".

5.  **Adicionar Cláusula de Renegociação e Cancelamento**:
    *   Informar ao cliente como proceder em caso de dúvidas sobre a fatura, necessidade de renegociação ou desejo de cancelar o serviço.
    *   **Exemplo**: "Em caso de dúvidas ou para questões de suporte/cancelamento, entre em contato via [e-mail de suporte] ou [telefone]."

6.  **Automatizar a Geração e Envio**: O template deve ser compatível com sistemas que automatizam a emissão e envio por e-mail, garantindo que todas as informações dinâmicas (período, valor, vencimento) sejam preenchidas corretamente. (Ver Template 2 na seção seguinte).

---

## Templates

### Template 1: Fatura de Serviço (Consultoria em TI com Retenção)

```
[LOGOTIPO DA SUA EMPRESA]

FATURA DE SERVIÇO

NÚMERO DA FATURA: 202310-001
DATA DE EMISSÃO: 20/10/2023
DATA DE VENCIMENTO: 20/11/2023

Dados do Emissor:
-------------------
TECH SOLUTIONS CONSULTORIA LTDA
CNPJ: 12.345.678/0001-90
Inscrição Municipal: 1.234.567-8
Endereço: Av. Paulista, 1000, 15º Andar, Bela Vista, São Paulo - SP, CEP 01310-100
Telefone: (11) 98765-4321
E-mail: contato@techsolutions.com.br

Dados do Tomador (Cliente):
----------------------------
INOVAÇÃO DIGITAL S.A.
CNPJ: 98.765.432/0001-21
Inscrição Estadual: Isento
Endereço: Rua da Consolação, 500, 5º Andar, Consolação, São Paulo - SP, CEP 01302-000
Contato: Financeiro - financeiro@inovacaodigital.com.br

Descrição dos Serviços:
-----------------------
| Qtd. | Descrição do Item                           | Valor Unitário | Valor Total |
|------|---------------------------------------------|----------------|-------------|
| 1    | Consultoria em Implementação de Sistema CRM | R$ 12.000,00   | R$ 12.000,00|
|      | Período: 01/10/2023 a 31/10/2023            |                |             |

Resumo Financeiro:
------------------
Subtotal:                                       R$ 12.000,00

Impostos Retidos:
  ISS (5%):                                    - R$    600,00
  PIS (0,65%):                                 - R$     78,00
  COFINS (3%):                                 - R$    360,00
  CSLL (1%):                                   - R$    120,00
  IRRF (1,5%):                                 - R$    180,00
--------------------------------------------------------------
TOTAL DE RETENÇÕES:                             R$  1.338,00

VALOR LÍQUIDO A RECEBER:                        R$ 10.662,00

Condições de Pagamento:
-----------------------
*   Pagamento até: 20/11/2023
*   Forma de Pagamento: Transferência Bancária ou PIX

Dados Bancários para Transferência:
Banco: Banco do Brasil (001)
Agência: 1234-5
Conta Corrente: 67890-X
Favorecido: TECH SOLUTIONS CONSULTORIA LTDA
CNPJ: 12.345.678/0001-90

Chave PIX: 12.345.678/0001-90 (CNPJ)

Observações:
Em caso de atraso no pagamento, será aplicada multa de 2% e juros de 1% ao mês (pro-rata die) sobre o valor em aberto.
```

### Template 2: Fatura Recorrente (Assinatura SaaS)

```
[LOGOTIPO DA SUA EMPRESA]

FATURA DE ASSINATURA

NÚMERO DA FATURA: SAAS-202311-045
DATA DE EMISSÃO: 01/11/2023
DATA DE VENCIMENTO: 10/11/2023

Dados do Emissor:
-------------------
SAAS MASTER TECNOLOGIA LTDA
CNPJ: 45.678.901/0001-32
Inscrição Municipal: 2.345.678-9
Endereço: Rua da Inovação, 123, Sala 10, Centro, Belo Horizonte - MG, CEP 30130-100
Telefone: (31) 99876-5432
E-mail: financeiro@saasmaster.com.br

Dados do Tomador (Cliente):
----------------------------
SOLUÇÕES EMPRESARIAIS LTDA
CNPJ: 21.098.765/0001-43
Inscrição Estadual: Isento
Endereço: Av. Afonso Pena, 2000, 8º Andar, Funcionários, Belo Horizonte - MG, CEP 30130-000
Contato: financeiro@solucoesempresariais.com.br

Descrição dos Serviços:
-----------------------
| Qtd. | Descrição do Item                                 | Valor Unitário | Valor Total |
|------|---------------------------------------------------|----------------|-------------|
| 1    | Assinatura Mensal - Plano Gold - Software "Gestão Pro" | R$ 450,00      | R$ 450,00   |
|      | Licença #AB1234 - Referente ao período: 01/11/2023 - 30/11/2023 |                |             |
|      | Conforme Contrato de Assinatura nº 2023-005       |                |             |

Resumo Financeiro:
------------------
Subtotal:                                       R$ 450,00
Total de Impostos (incluído no valor):          R$   22,50 (ISS 5%)
--------------------------------------------------------------
VALOR TOTAL A PAGAR:                            R$ 450,00

Condições de Pagamento:
-----------------------
*   Pagamento até: 10/11/2023
*   Forma de Pagamento: PIX ou Boleto Bancário

Instruções de Pagamento:
------------------------
1.  **PIX (Recomendado)**: Utilize a chave CNPJ: 45.678.901/0001-32
    Ou escaneie o QR Code abaixo para pagamento rápido e automático:
    [Inserir QR Code PIX dinâmico aqui - Ex: Image URL ou placeholder para renderização]

2.  **Boleto Bancário**: Acesse e pague seu boleto clicando aqui:
    [https://link.para.boleto.saasmaster.com.br/SAAS-202311-045]

Observações:
Em caso de dúvidas sobre esta fatura ou para suporte, entre em contato com nosso time financeiro pelo e-mail financeiro@saasmaster.com.br ou telefone (31) 99876-5432.
```

---

## Checklist

-   [x] Todos os dados do emissor (razão social, CNPJ, endereço, contato) estão corretos e atualizados?
-   [x] Todos os dados do tomador (razão social/nome, CNPJ/CPF, endereço, contato) estão corretos?
-   [x] A descrição dos produtos/serviços é clara, detalhada e corresponde exatamente ao que foi entregue/contratado?
-   [x] Os valores unitários e totais de cada item estão calculados corretamente?
-   [x] Todas as alíquotas e valores de impostos (IVA, ICMS, ISS, PIS, COFINS, IRRF, CSLL, etc.) foram aplicadas e calculadas corretamente para o regime tributário e atividade?
-   [x] O valor total da fatura (bruto e líquido, se houver retenções) está correto e destacado?
-   [x] As condições de pagamento (prazo, forma, dados bancários/PIX/links) estão explícitas e sem ambiguidades?
-   [x] A data de emissão e a data de vencimento estão claramente indicadas e são compatíveis com os termos acordados?
-   [x] Existe um número de fatura único e sequencial para controle interno e fiscal?
-   [x] Para faturas recorrentes, o período de referência (ex: "Mês/Ano") está especificado?
-   [x] Para transações internacionais, a moeda está especificada e a cotação, se aplicável, foi referenciada?
-   [x] Cláusulas de juros, multa por atraso e política de cancelamento estão presentes, se aplicável?

---

## Métricas de Referência

| Métrica                         | Benchmark (Ideal) | Meta (Atingível) |
|---------------------------------|-------------------|------------------|
| Prazo Médio de Recebimento (PMR)| 30 dias           | 25 dias          |
| Taxa de Inadimplência           | < 3%              | < 1,5%           |
| Custo de Emissão de Fatura/unid.| R$ 0,50           | R$ 0,20          |
| Tempo Médio Emissão (manual)    | 15 minutos        | 5 minutos        |
| Taxa de Rejeição por Erro       | < 1%              | 0%               |
| % Faturas Pagas no Vencimento   | 90%               | 95%              |

---

## Erros Comuns

1.  **Dados Cadastrais do Cliente Incompletos ou Incorretos**:
    *   **Erro**: Emitir uma fatura com CNPJ desatualizado, endereço incompleto ou razão social divergente do cadastro da Receita Federal. Isso pode gerar recusa do pagamento ou problemas fiscais.
    *   **Como evitar**: Implementar um processo de validação de dados cadastrais no momento da criação do cliente ou antes da emissão da fatura. Utilizar APIs de consulta pública (ex: ReceitaWS para CNPJ) para garantir a veracidade e completude das informações. Ex: "Antes de emitir a fatura, consulte o CNPJ 98.765.432/0001-21 no site da Receita Federal para confirmar que a Razão Social 'INOVAÇÃO DIGITAL S.A.' e o endereço estão corretos."

2.  **Cálculo Inadequado de Impostos e Retenções**:
    *   **Erro**: Aplicar alíquotas de ISS incorretas para o município do prestador/tomador, esquecer retenções federais (PIS, COFINS, CSLL, IRRF) ou aplicar impostos sobre produtos em serviços e vice-versa.
    *   **Como evitar**: Manter-se atualizado com a legislação tributária ou utilizar sistemas de faturamento que integrem tabelas fiscais atualizadas. Para serviços, sempre verificar o regime tributário da sua empresa e do cliente, bem como o código de serviço municipal. Ex: "Para a consultoria de TI em São Paulo, o ISS é 5%, PIS 0,65%, COFINS 3%, CSLL 1% e IRRF 1,5% devem ser retidos sobre o valor bruto de R$ 12.000,00."

3.  **Descrição Genérica ou Insuficiente do Item Faturado**:
    *   **Erro**: Descrever um item da fatura como "Serviços Diversos" ou "Venda de Materiais", o que dificulta a classificação contábil para o cliente e pode gerar questionamentos fiscais.
    *   **Como evitar**: Ser o mais específico possível, detalhando o tipo de serviço (ex: "Desenvolvimento de Módulo de Pagamento - Sprint 3"), o período de referência (ex: "referente a Outubro/2023") e, para produtos, o SKU, quantidade e características. Ex: Em vez de "Software", usar "Licença de Software 'Gestão Pro' - Plano Gold - Período 01/11/2023 a 30/11/2023".

---

## Dicas Avançadas

1.  **Geração de Faturas Proforma para Exportação**: Utilize faturas proforma (pró-forma) para formalizar orçamentos em transações internacionais. Elas servem como um "rascunho" da fatura comercial, detalhando incoterms (ex: FOB, CIF), valores em moeda estrangeira (ex: USD), peso, dimensões e termos de pagamento, antes da efetivação da venda e emissão da fatura comercial final. Isso alinha expectativas e evita surpresas. Ex: "Ao cotar 1000 unidades de produto para um cliente na Alemanha, envie uma proforma invoice detalhando Incoterm EXW (Ex Works), preço em EUR, peso líquido/bruto e volume da carga."

2.  **Inclusão de QR Code PIX Dinâmico com Payload Completo**: Para agilizar a conciliação