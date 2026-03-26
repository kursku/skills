---
name: client-service-agreement
description: "Client Service Agreement — Skill especializada para client service agreement"
license: MIT
metadata:
  version: 1.0.0
  author: Cafe Code AI
  category: 07-juridico-compliance
  updated: 2026-03-01
risk: critical
---

# Client Service Agreement

Esta skill capacita o Claude a elaborar, revisar e otimizar Client Service Agreements (CSAs) com foco em clareza, proteção jurídica e conformidade regulatória, especialmente LGPD/GDPR.

---

## Keywords

Acordo de Serviço, Contrato de Prestação de Serviços, SLA, Termos de Serviço, Responsabilidades Contratuais, Escopo de Serviços, Remuneração, Propriedade Intelectual, Confidencialidade, Rescisão Contratual, LGPD, Compliance Digital, Limitação de Responsabilidade, Jurisdição, Foro, Gestão de Contratos.

---

## Quick Start

1.  Forneça o nome completo das partes (Contratante e Contratado), CNPJs/CPFs e endereços para qualificação inicial e correta.
2.  Descreva o objeto principal do serviço, indicando entregáveis específicos, prazos e métricas de sucesso esperadas.
3.  Especifique o modelo de precificação (ex: fixo mensal de R$ 7.500,00, hora trabalhada R$ 180,00, projeto por R$ 35.000,00) e a forma de pagamento (boleto bancário, transferência eletrônica com PIX).
4.  Indique se há necessidade de cláusulas específicas de LGPD para tratamento de dados pessoais (ex: Contratado atuará como operador de dados pessoais da Contratante).
5.  Defina a duração do contrato (prazo determinado de 12 meses renováveis, prazo indeterminado com aviso prévio de 60 dias para rescisão).

---

## Core Workflows

### Workflow 1: Elaboração de um Client Service Agreement Inicial

Este workflow guia a criação de um CSA robusto, partindo de informações básicas fornecidas pelo usuário, garantindo que os elementos essenciais e de conformidade sejam incorporados desde o início.

**Passo a Passo:**

1.  **Coleta de Dados Essenciais das Partes e Objeto:**
    *   **Ação:** Solicitar ao usuário dados completos da Contratante (razão social, CNPJ, endereço completo, nome do representante legal, CPF) e da Contratada (razão social, CNPJ, endereço completo, nome do representante legal, CPF). Obter uma descrição clara e concisa do serviço a ser prestado, incluindo objetivos e entregas esperadas.
    *   **Exemplo de Input:**
        *   **Contratante:** "Indústria Alfa Ltda., CNPJ 05.123.456/0001-78, Rua das Palmeiras, 150, Centro, Belo Horizonte/MG, CEP 30160-000. Representante: Dr. Roberto Carlos Pires, CPF 123.456.789-00."
        *   **Contratada:** "Agência Marketing Digital Solutions S.A., CNPJ 10.987.654/0001-21, Avenida Brasil, 2000, Bairro Jardim, São Paulo/SP, CEP 01430-000. Representante: Sra. Juliana Mendes, CPF 987.654.321-00."
        *   **Objeto:** "Criação e gestão de campanhas de marketing digital para o lançamento do produto 'Eco-Limp', abrangendo Google Ads, Facebook Ads e Instagram Ads, com duração de 4 meses, visando 25% de aumento nas vendas online do produto no período."

2.  **Estruturação das Cláusulas Fundamentais:**
    *   **Ação:** Redigir as cláusulas de Qualificação das Partes, Objeto, Prazo de Vigência, Remuneração e Condições de Pagamento, com base nos dados fornecidos, assegurando clareza e precisão.
    *   **Exemplo de Output (Cláusula de Remuneração):**
        *   "**CLÁUSULA QUARTA – DA REMUNERAÇÃO E CONDIÇÕES DE PAGAMENTO**
            4.1. Pelos serviços descritos na Cláusula Segunda, a CONTRATANTE pagará à CONTRATADA o valor mensal fixo de R$ 12.000,00 (doze mil reais), totalizando R$ 48.000,00 (quarenta e oito mil reais) pelo período de 4 (quatro) meses.
            4.2. O pagamento será efetuado em 4 (quatro) parcelas iguais, sendo a primeira no ato da assinatura deste Contrato e as demais até o 5º (quinto) dia útil dos meses subsequentes. O pagamento será realizado mediante transferência bancária para a conta corrente indicada pela CONTRATADA (Banco Itaú, Agência 1234, Conta Corrente 56789-0) ou via boleto bancário emitido pela CONTRATADA."

3.  **Inclusão de Cláusulas de Conformidade (LGPD/GDPR):**
    *   **Ação:** Incorporar cláusulas mandatórias sobre tratamento de dados pessoais, confidencialidade, segurança da informação e responsabilidades em caso de incidentes, em estrita conformidade com a Lei Geral de Proteção de Dados (LGPD) e, se aplicável, o GDPR.
    *   **Exemplo de Output (Cláusula de LGPD):**
        *   "**CLÁUSULA SEXTA – DA PROTEÇÃO DE DADOS PESSOAIS E CONFIDENCIALIDADE**
            6.1. As Partes se comprometem a cumprir integralmente a Lei nº 1