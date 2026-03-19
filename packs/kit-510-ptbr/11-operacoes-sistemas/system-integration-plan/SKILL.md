---
name: system-integration-plan
description: "System Integration Plan — Skill especializada para system integration plan"
license: MIT
metadata:
  version: 1.0.0
  author: Cafe Code AI
  category: 11-operacoes-sistemas
  updated: 2026-03-01
---

# System Integration Plan

Este plano detalha a estratégia, arquitetura, fases de teste e implantação necessárias para conectar e garantir a interoperabilidade eficiente entre diferentes sistemas de software.

---

## Keywords

Integração de Sistemas, Middleware, APIs REST, ETL, Mapeamento de Dados, Teste de Integração, Go-Live, Rollback, ESB, Microsserviços, Migração de Dados, Governança de APIs, iPaas, Orquestração de Serviços.

---

## Quick Start

1.  **Análise de Gaps e Requisitos dos Sistemas**: Inicie documentando os sistemas de origem e destino (ex: ERP, CRM, E-commerce, Legado), identificando as funcionalidades críticas e os fluxos de dados que precisam ser integrados. Por exemplo, para integrar o ERP (SAP) com o CRM (Salesforce), mapeie entidades como `Clientes`, `Pedidos` e `Faturas` e seus respectivos ciclos de vida.
2.  **Desenho da Arquitetura de Integração**: Esboce a solução técnica, escolhendo entre abordagens como iPaaS (ex: MuleSoft, Azure Integration Services), barramentos de serviço (ESB) ou APIs ponto a ponto. Defina os protocolos de comunicação (REST, SOAP, Kafka) e os formatos de dados (JSON, XML). Considere a segurança e a resiliência desde o início.
3.  **Mapeamento de Dados Detalhado**: Elabore um documento rigoroso de mapeamento de campos entre os sistemas de origem e destino, especificando transformações, regras de negócio e validações para cada atributo. Por exemplo, mapear `cliente.id` do sistema A para `account.externalId` no sistema B, com uma regra de prefixo "CLI_".
4.  **Elaboração do Plano de Testes Abrangente**: Defina cenários de teste unitário, de integração, de volume, de performance e de aceitação do usuário (UAT), com casos de teste específicos para fluxos de negócio como "Criação de um novo pedido no CRM deve resultar em um registro correspondente no ERP com status 'pendente'".
5.  **Plano de Implantação e Rollback**: Detalhe os passos para o "go-live", incluindo janelas de manutenção, sequência de ativação dos componentes, e um plano claro para reverter a implantação em caso de falha crítica. Isso assegura a continuidade operacional e minimiza riscos.

---

## Core Workflows

### Workflow 1: Projeto e Desenvolvimento da Arquitetura de Integração

Este workflow foca na concepção técnica e na construção dos componentes que permitirão a comunicação entre os sistemas.

1.  **Identificação e Análise de Sistemas Envolvidos**: Liste todos os sistemas de origem e destino, suas versões, tecnologias subjacentes, APIs disponíveis (ou a falta delas) e os fluxos de dados críticos. Exemplo: Integrar um `Sistema de Gestão de Estoque Legado (base de dados SQL Server sem API)` com uma `Plataforma E-commerce (Shopify com REST Admin API)` e um `ERP (Totvs Protheus com Web Services SOAP)`.
2.  **Definição dos Padrões de Integração**: Avalie requisitos de latência, volume de dados, real-time vs. batch, e transacionalidade para selecionar o padrão mais adequado. Para `atualização de estoque do Legado para Shopify`, um padrão assíncrono via fila de mensagens (Azure Service Bus ou AWS SQS) pode ser ideal para desacoplar os sistemas. Para `consulta de status de pedido do Shopify para Protheus`, um serviço síncrono via API REST (com um wrapper para o SOAP do