---
name: inventory-management
description: "Inventory Management — Skill especializada para inventory management"
license: MIT
metadata:
  version: 1.0.0
  author: Cafe Code AI
  category: 11-operacoes-sistemas
  updated: 2026-03-01
risk: caution
---

# Inventory Management

Esta skill capacita o Claude a otimizar processos de estoque, desde a previsão de demanda até a auditoria física, garantindo a disponibilidade de produtos e a redução de custos operacionais.

---

## Keywords

Gestão de Estoque, Controle de Inventário, Previsão de Demanda, KPIs de Estoque, Auditoria Cíclica, Ponto de Pedido, Giro de Estoque, Custo de Manutenção, Obsoleto, FIFO/LIFO, WMS, OTIF.

---

## Quick Start

1.  **Configurar Ponto de Pedido (ROP) para SKU crítico**: Para o SKU "Parafuso M6x20mm", com lead time de 5 dias e demanda diária média de 500 unidades, e estoque de segurança de 2500 unidades, defina o ROP em (5 * 500) + 2500 = 5000 unidades. Quando o estoque atingir 5000, um novo pedido é disparado automaticamente pelo sistema de gestão.
2.  **Realizar Contagem Cíclica diária**: Selecionar 5 SKUs da categoria A (maior valor/rotatividade) e realizar a contagem física no armazém, comparando com o saldo do sistema. Registrar e investigar desvios maiores que 2% imediatamente.
3.  **Analisar Relatório de Giro de Estoque**: Gerar um relatório mensal de SKUs com giro de estoque inferior a 2 vezes por ano, como "Componente X-123". Propor ações corretivas como promoção direcionada ou devolução ao fornecedor para liberar capital.
4.  **Otimizar Layout de Armazém para Picking**: Mover os 10 SKUs mais requisitados nos últimos 30 dias para as primeiras posições das prateleiras do corredor principal do armazém 1, reduzindo o tempo de picking em 15% e o desgaste dos operadores.

---

## Core Workflows

### Workflow 1: Otimização do Ponto de Pedido (ROP) e Estoque de Segurança (SS)

Este workflow detalha o cálculo e a implementação de parâmetros de ressuprimento para evitar rupturas e excessos de estoque.

1.  **Coleta de Dados Históricos de Demanda:**
    *   **Ação**: Para o SKU "Bateria de Lítio 18650", coletar os últimos 12 meses de vendas diárias do sistema ERP.
    *   **Exemplo**: Demanda Média Diária: 150 unidades/dia. Desvio Padrão da Demanda Diária: 25 unidades/dia.
2.  **Determinação do Lead Time do Fornecedor:**
    *   **Ação**: Obter o lead time médio e o desvio padrão das entregas do fornecedor para o SKU.
    *   **Exemplo**: Fornecedor A leva 7 dias (Lead Time Médio) com um desvio padrão de 1 dia (Desvio Padrão do Lead Time) para entregar as Baterias de Lítio 18650.
3.  **Cálculo do Estoque de Segurança (SS):**
    *   **Fórmula**: `SS = Z * sqrt(Lead Time Médio * (Desvio Padrão Demanda)^2 + Demanda Média^2 * (Desvio Padrão Lead Time)^2)`
        *   Onde Z é o fator de serviço (para 95% de nível de serviço, Z = 1.645).
    *   **Exemplo**: `SS = 1.645 * sqrt(7 * (25^2) + 150^2 * (1^2)) = 1.645 * sqrt(7 * 625 + 22500 * 1) = 1.645 * sqrt(4375 + 22500) = 1.645 * sqrt(26875) = 1.645 * 163.93 ≈ 270 unidades`. Arredondar para o próximo número inteiro.
4.  **Cálculo do Ponto de Pedido (ROP):**
    *   **Fórmula**: `ROP = (Demanda Média Diária * Lead Time Médio) + Estoque de Segurança`
    *   **Exemplo**: `ROP = (150 unidades/dia * 7 dias) + 270 unidades = 1050 + 270 = 1320 unidades`.
5.  **Implementação e Monitoramento:**
    *   **Ação**: Configurar o sistema WMS/ERP para gerar automaticamente um alerta de ressuprimento ou uma sugestão de ordem de compra quando o estoque de "Bateria de Lítio 18650" atingir 1320 unidades.
    *   **Monitoramento**: Monitorar semanalmente a acurácia da previsão e ajustar ROP/SS se a cobertura de estoque ou o nível de serviço (fill rate) caírem abaixo de 90%.

### Workflow 2: Execução de Auditoria Cíclica de Estoque

Este workflow estabelece um processo contínuo de contagem de estoque para manter a acurácia sem a interrupção de um inventário total anual.

1.  **Classificação ABC dos Itens:**
    *   **Ação**: Utilizar o relatório de vendas e valor de estoque do ERP para classificar os SKUs.
    *   **Exemplo**:
        *   **Classe A (Alto Valor/Giro)**: 20% dos itens que representam 80% do valor (ex: "Smartphones X", "Notebooks Y", "Smart TVs Z").
        *   **Classe B (Médio Valor/Giro)**: 30% dos itens, 15% do valor (ex: "Fones de ouvido Bluetooth", "Caixas de som portáteis").
        *   **Classe C (Baixo Valor/Giro)**: 50% dos itens, 5% do valor (ex: "Cabos USB", "Adaptadores de tomada").
2.  **Definição da Frequência de Contagem:**
    *   **Ação**: Atribuir frequências de contagem baseadas na classificação ABC.
    *   **Exemplo**:
        *   Itens Classe A: Contagem diária de 5-10 SKUs aleatórios.
        *   Itens Classe B: Contagem semanal de 10-15 SKUs aleatórios.
        *   Itens Classe C: Contagem mensal de 20-30 SKUs aleatórios.
3.  **Geração da Lista de Contagem:**
    *   **Ação**: O sistema WMS gera uma lista de SKUs para contagem aleatória.
    *   **Exemplo**: O WMS gera uma lista de 8 SKUs da Classe A para contagem na manhã de 15/03/2025: "Smartphone X Plus (Cor Azul)", "Notebook Y Pro (16GB RAM)", "Smart TV Z 55 Polegadas".
4.  **Contagem Física e Registro:**
    *   **Ação**: A equipe de estoque realiza a contagem física e registra no sistema.
    *   **Exemplo**: A equipe conta fisicamente 120 unidades de "Smartphone X Plus (Cor Azul)" na localização A-01-03. O sistema WMS indica 123 unidades.
5.  **Reconciliação e Análise de Desvios:**
    *   **Ação**: Comparar a contagem física com o registro do sistema.
    *   **Exemplo**: O desvio de -3 unidades de "Smartphone X Plus (Cor Azul)" é registrado. Se o desvio percentual (3/123 = 2.4%) for maior que a tolerância definida (ex: 2%), investigar a causa raiz (erro de picking, recebimento, extravio). Ajustar o estoque no sistema após aprovação da gerência.
6.  **Relatório e Ações Corretivas:**
    *   **Ação**: Gerar um relatório mensal de acurácia de estoque por classe de item.
    *   **Exemplo**: Se a acurácia da Classe A cair abaixo de 98.5%, revisar processos de recebimento e expedição ou intensificar treinamentos para a equipe.

---

## Templates

### Relatório Mensal de Indicadores de Estoque

```
Relatório Mensal de Indicadores de Estoque - Março/2025

Empresa: Tech Solutions S.A.
Responsável: Ana Paula Costa - Analista de Estoque
Data: 01/04/2025

---

1.  **Giro de Estoque (ISR):**
    *   Valor Atual: 7.2 vezes/ano
    *   Meta: 8.0 vezes/ano
    *   Status: Abaixo da Meta
    *   SKUs de Baixo Giro (Exemplos > 12 meses sem movimento):
        *   SKU: Mouse Gamer Z-Pro | Última Venda: 01/02/2024 | Quantidade em Estoque: 25
        *   SKU: Teclado Mecânico K-900 | Última Venda: 15/01/2024 | Quantidade em Estoque: 18
    *   Ações Propostas:
        *   Promoção de 20% no Mouse Gamer Z-Pro durante o mês de abril.
        *   Negociação de devolução do Teclado Mecânico K-900 com o fornecedor Eletrônicos Premium.

2.  **Acurácia de Estoque Físico vs. Sistema (PIA):**
    *   Valor Atual: 98.7%
    *   Meta: 99.5%
    *   Status: Abaixo da Meta
    *   Desvios Principais (Últimas 5 auditorias cíclicas):
        *   SKU: Cabo HDMI 2.0 (10m) | Desvio: +5 unidades | Causa: Erro de recebimento (divergência NF vs. físico)
        *   SKU: Adaptador USB-C p/ HDMI | Desvio: -3 unidades | Causa: Divergência de picking (item errado retirado)
    *   Ações Propostas:
        *   Treinamento reforçado para equipe de recebimento sobre conferência dupla.
        *   Revisão do processo de picking para incluir dupla checagem por SKU.

3.  **Custo de Manutenção de Estoque (Holding Cost):**
    *   Valor Atual: R$ 15.200,00
    *   Percentual sobre o Valor Médio do Estoque: 22%
    *   Meta: 20%
    *   Status: Acima da Meta
    *   Principais Componentes de Custo: Armazenagem (45%), Seguro (25%), Obsolescência (20%).
    *   Ações Propostas:
        *   Otimização do layout do armazém para reduzir espaço ocioso em 10%.
        *   Revisão de contratos de seguro para buscar melhores condições.

4.  **Nível de Serviço (Fill Rate):**
    *   Valor Atual: 97.2%
    *   Meta: 98.5%
    *   Status: Abaixo da Meta
    *   Principais Causas de Ruptura de Estoque (Stock-outs):
        *   SKU: Placa de Vídeo RTX-3060 | Causa: Atraso do fornecedor (entrega com 5 dias de atraso)
        *   SKU: Processador i7-12700K | Causa: Previsão de demanda subestimada (pico inesperado de vendas)
    *   Ações Propostas:
        *   Implementar monitoramento proativo de fornecedores críticos com alertas de atraso.
        *   Revisar e ajustar os parâmetros de previsão de demanda para itens de alto impacto, utilizando dados de campanhas de marketing futuras.

---

**Observações Adicionais:**
*   A equipe de estoque iniciou o treinamento "Boas Práticas de Armazenagem" para reduzir avarias.
*   Planejamento para implementar um sistema de identificação por RFID para itens de alto valor no próximo trimestre.
```

### Ordem de