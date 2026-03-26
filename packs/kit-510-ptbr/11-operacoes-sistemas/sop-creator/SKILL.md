---
name: sop-creator
description: "Sop Creator — Skill especializada para sop creator"
license: MIT
metadata:
  version: 1.0.0
  author: Cafe Code AI
  category: 11-operacoes-sistemas
  updated: 2026-03-01
risk: critical
---

# Sop Creator

Esta skill capacita Claude a atuar como um especialista em criação, otimização e implementação de Procedimentos Operacionais Padrão (SOPs), garantindo clareza e eficiência em processos empresariais.

---

## Keywords

SOP, Procedimento Operacional Padrão, Documentação de Processos, Fluxograma de Processos, Mapeamento de Processos, Instrução de Trabalho, Otimização de Processos, Governança de Processos, Treinamento Operacional, Padronização, Gestão da Qualidade, Checklist Operacional, Processos Internos, Delegação de Tarefas, Melhoria Contínua.

---

## Quick Start

1.  Inicie um novo SOP para um processo chave: `claudecode run sop-creator --task "Criar SOP para Embarque de Pedidos E-commerce"`
2.  Mapeie o fluxo de trabalho atual: `claudecode run sop-creator --task "Desenvolver fluxograma detalhado para processo de Reembolso de Cliente"`
3.  Elabore a seção de Responsabilidades para o SOP: `claudecode run sop-creator --task "Detalhar responsabilidades do Analista de Suporte no SOP de Atendimento ao Cliente Nível 1"`
4.  Gere um template completo para um novo procedimento: `claudecode run sop-creator --task "Gerar template completo para novo SOP de Onboarding de Colaborador"`
5.  Otimize um SOP existente: `claudecode run sop-creator --task "Revisar e otimizar o SOP de 'Controle de Qualidade na Entrada de Matéria-Prima' após feedback da produção"`

---

## Core Workflows

### Workflow 1: Criação de SOP para Processo Crítico de Negócio

Este workflow guia a construção de um SOP robusto e funcional para um processo essencial da organização, desde a concepção até a publicação.

1.  **Passo 1: Identificação e Delimitação do Escopo do Processo.**
    *   **Ação:** Delimitar precisamente o início e o fim do processo, e quais atividades ele abrange.
    *   **Exemplo:** Para o processo de "Recebimento de Mercadorias no Almoxarifado", o escopo vai desde a chegada do caminhão do fornecedor no pátio da empresa até o registro final da entrada no sistema ERP, excluindo o processo de separação para estoque.
    *   **Ferramentas:** Brainstorming com stakeholders, Matriz RACI preliminar.

2.  **Passo 2: Mapeamento Detalhado do Fluxo Atual (As-Is).**
    *   **Ação:** Observar, entrevistar executantes e documentar cada etapa, decisões, pontos de controle e handoffs.
    *   **Exemplo:** Desenvolver um fluxograma com swimlanes distintas para "Recebimento", "Conferência", "Qualidade" e "Administração", detalhando cada ação, como "Conferir Nota Fiscal (NF) com Pedido de Compra (PC)", "Verificar integridade da embalagem", "Registrar divergências no Sistema X".
    *   **Ferramentas:** Software de fluxograma (Lucidchart, Miro), observação direta (Gemba Walk), entrevistas semiestruturadas.

3.  **Passo 3: Elaboração da Estrutura do SOP.**
    *   **Ação:** Definir as seções padrão do documento para garantir clareza e padronização.
    *   **Exemplo:** Um SOP para "Fechamento Mensal Contábil" deve ter as seguintes seções: Título, Código do SOP (ex: FIN-003), Versão (ex: 2.1), Data de Vigência, Objetivo (ex: "Assegurar o fechamento contábil mensal dentro do prazo e com precisão"), Escopo, Responsabilidades (ex: "Analista Contábil 1: Conciliações Bancárias; Analista Contábil 2: Lançamentos de Despesas"), Definições, Procedimento Detalhado, Fluxograma, Documentos de Referência, Registros, Histórico de Revisões.

4.  **Passo 4: Redação do Procedimento Detalhado.**
    *   **Ação:** Descrever cada passo de forma clara, sequencial, com verbos de ação e especificando o que, como, quando e quem.
    *   **Exemplo:** Em vez de "Verificar o produto", redigir "Conferir o código SKU do produto recebido com o código da Nota Fiscal (campo F.4.1) e com o Pedido de Compra (linha 2, coluna SKU). Se houver divergência, preencher o Formulário de Não Conformidade (FNC-001) e notificar o Gerente de Compras." Incluir capturas de tela seções críticas do sistema, se aplicável.

5.  **Passo 5: Validação e Teste do SOP.**
    *   **Ação:** Revisar o documento com especialistas, simular o processo ou realizar um piloto com o SOP em mãos.
    *   **Exemplo:** Solicitar a um colaborador júnior que execute o processo de "Manutenção Preventiva de Equipamento X" seguindo exclusivamente o SOP. Registrar todos os pontos de dúvida, ambiguidade ou etapas faltantes, ajustando o documento conforme necessário.

6.  **Passo 6: Aprovação Formal e Publicação.**
    *   **Ação:** Obter a aprovação final dos gestores e stakeholders relevantes e disponibilizar o SOP em um repositório acessível.
    *   **Exemplo:** Após aprovação do Gerente de Operações e do Diretor da Qualidade, publicar o SOP "REC-001/V2.0 - Recebimento de Mercadorias" no portal de documentos internos (SharePoint) e enviar um comunicado por e-mail para a equipe do almoxarifado e compras, informando sobre a nova versão e onde encontrá-la.

### Workflow 2: Otimização e Revisão de SOP Existente

Este workflow foca em aprimorar SOPs já implementados, garantindo que permaneçam relevantes, eficientes e em conformidade.

1.  **Passo 1: Análise de Desempenho e Coleta de Feedback.**
    *   **Ação:** Reunir dados de KPIs, relatórios de não conformidades, sugestões de usuários e auditorias internas/externas relacionadas ao SOP.
    *   **Exemplo:** Analisar relatórios de atrasos na entrega dos últimos 3 meses para o "SOP de Processamento de Pedidos" e compilar feedback dos atendentes sobre dificuldades em etapas específicas, como a verificação de estoque.

2.  **Passo 2: Identificação de Gargalos e Pontos de Melhoria.**
    *   **Ação:** Utilizar ferramentas de análise para pinpointar as causas-raiz de ineficiências ou erros no processo.
    *   **Exemplo:** Realizar um diagrama de Ishikawa para o "SOP de Tratamento de Reclamações de Clientes" e descobrir que a principal causa dos atrasos é a dependência de aprovação manual para reembolsos de baixo valor.

3.  **Passo 3: Proposta de Alterações (To-Be).**
    *   **Ação:** Desenvolver soluções e modificações para o processo, visando simplificação, automação ou melhoria da qualidade.
    *   **Exemplo:** Propor a implementação de um limite de alçada automática para reembolsos de até R$100,00 no sistema CRM, eliminando a necessidade de aprovação gerencial para essas ocorrências, no "SOP de Tratamento de Reclamações".

4.  **Passo 4: Atualização do Documento e Controle de Versão.**
    *   **Ação:** Incorporar as mudanças propostas no SOP, registrando-as no histórico de revisões e atualizando a versão e data de vigência.
    *   **Exemplo:** No SOP "SAC-002 - Tratamento de Reclamações", na seção 4.3 "Procedimento de Reembolso", alterar o item 4.3.2 para "Para valores até R$100,00, o agente de atendimento pode aprovar o reembolso diretamente no sistema. Acima deste valor, seguir o fluxo de aprovação gerencial (ver Anexo B)." Incrementar a versão de 1.1 para 1.2.

5.  **Passo 5: Treinamento e Comunicação das Mudanças.**
    *   **Ação:** Capacitar todas as equipes impactadas pelas alterações e comunicar as novas diretrizes de forma eficaz.
    *   **Exemplo:** Realizar um treinamento online de 1 hora para a equipe de atendimento ao cliente sobre as novas alçadas de reembolso no "SOP SAC-002" e distribuir um resumo executivo das principais mudanças por e-mail corporativo.

6.  **Passo 6: Monitoramento Pós-Implementação.**
    *   **Ação:** Acompanhar de perto os KPIs e coletar feedback adicional para validar a eficácia das otimizações.
    *   **Exemplo:** Monitorar a redução do tempo médio de resolução (TMR) para reclamações de baixo valor nos 30 dias seguintes à implementação do "SOP SAC-002 V1.2", buscando uma queda de 20% no TMR para esses casos.

---

## Templates

### Template de SOP Padrão - Emissão de Nota Fiscal de Venda

```markdown
**SOP: Emissão de Nota Fiscal de Venda**

**Código:** VEN-005
**Versão:** 3.1
**Data de Vigência:** 15/03/2024
**Elaborado Por:** Departamento Fiscal
**Aprovado Por:** Gerência Comercial, Gerência Fiscal
**Próxima Revisão:** 15/03/2025

**1. Objetivo**
Assegurar que todas as Notas Fiscais de Venda sejam emitidas de forma correta, dentro dos prazos legais e em conformidade com os pedidos de venda e a legislação fiscal vigente, minimizando erros e retrabalhos.

**2. Escopo**
Este SOP aplica-se a todo o processo de emissão de Nota Fiscal Eletrônica (NF-e) para vendas de produtos e serviços, desde a aprovação do pedido de venda até a transmissão e arquivamento da NF-e. Exclui-se a emissão de notas fiscais de devolução ou complemento.

**3. Responsabilidades**
*   **Assistente Comercial:** Inserir e aprovar pedidos no sistema ERP.
*   **Analista Fiscal:** Revisar dados fiscais, emitir e transmitir a NF-e.
*   **Gerente Comercial:** Aprovar pedidos com condições especiais.

**4. Definições**
*   **NF-e:** Nota Fiscal Eletrônica.
*   **ERP:** Enterprise Resource Planning (Sistema de Gestão Integrado).
*   **CFOP:** Código Fiscal de Operações e Prestações.

**5. Procedimento Detalhado**

**5.1. Recebimento e Aprovação do Pedido de Venda**
    1.  **Assistente Comercial:** Receber o pedido de venda do cliente (via e-mail ou sistema CRM).
    2.  **Assistente Comercial:** Inserir os dados do pedido (itens, quantidades, valores, cliente, forma de pagamento) no módulo de Vendas do ERP (Ex: Totvs Protheus, tela 'PV001').
    3.  **Assistente Comercial:** Conferir os dados inseridos com o pedido original.
    4.  **Assistente Comercial:** Se o pedido envolver condições especiais (desconto acima de 10%, prazo de pagamento estendido), encaminhar para aprovação do Gerente Comercial via sistema.
    5.  **Gerente Comercial:** Aprovar ou reprovar o pedido com condições especiais no ERP.
    6.  **Assistente Comercial:** Após aprovação, alterar o status do pedido para "Aprovado para Faturamento" no ERP.

**5.2. Emissão da Pré-Nota Fiscal**
    1.  **Analista Fiscal:** Acessar o módulo Fiscal do ERP (Ex: Totvs Protheus, tela 'NF-e Faturamento').
    2.  **Analista Fiscal:** Selecionar os pedidos com status "Aprovado para Faturamento" para a emissão da pré-nota.
    3.  **Analista Fiscal:** Conferir os dados da pré-nota:
        *   Dados do Cliente (Razão Social, CNPJ/CPF, Endereço, Inscrição Estadual).
        *   Itens do Pedido (Descrição, Quantidade, Valor Unitário, Valor Total).
        *   Dados Fiscais (CFOP, NCM, Alíquotas de ICMS, PIS, COFINS, IPI).
    4.  **Analista Fiscal:** Verificar se há impostos retidos (ISS, IRRF, CSLL) conforme natureza da operação e cliente.
    5.  **Analista Fiscal:** Gerar a pré-nota fiscal no sistema.

**5.3. Transmissão da NF-e**
    1.  **Analista Fiscal:** Validar a pré-nota no validador fiscal do ERP.
    2.  **Analista Fiscal:** Corrigir quaisquer inconsistências apontadas pelo validador.
    3.  **Analista Fiscal:** Transmitir a NF-e para a Sefaz.
    4.  **Analista Fiscal:** Aguardar o retorno da Sefaz com a autorização de uso.
    5.  **Analista Fiscal:** Em caso de rejeição, analisar o motivo, corrigir e retransmitir. Se o problema persistir por mais de 2 horas, acionar o suporte de TI.

**5.4. Impressão e Arquivamento**
    1.  **Analista Fiscal:** Após autorização, imprimir o DANFE (Documento Auxiliar da Nota Fiscal Eletrônica) em 2 vias (1 para o cliente, 1 para arquivo físico, se aplicável).
    2.  **Analista Fiscal:** Salvar o arquivo XML da NF-e em rede compartilhada (Ex: \\Servidor\NF-e\2024\Março).
    3.  **Analista Fiscal:** Anexar o DANFE físico ao pedido de venda correspondente para arquivo.

**6. Fluxograma**
[Diagrama de Fluxo de Processo da Emissão de NF-e, utilizando símbolos BPMN, com swimlanes para Assistente Comercial e Analista Fiscal.]

**7. Documentos de Referência**
*   Lei nº 5.172/1966 (Código Tributário Nacional)
*   Manual de Orientação do Contribuinte (MOC) da NF-e
*   Tabela de CFOPs
*   Política de Descontos da Empresa

**8. Registros**
*   Pedidos de Venda Aprovados (ERP)
*   Pré-Notas Fiscais (ERP)
*   Arquivos XML das NF-e Autorizadas (Rede compartilhada)
*   DANFEs Impressos (Arquivo físico, se aplicável)

**9. Histórico de Revisões**
| Versão | Data         | Descrição da Alteração                                     |
| :----- | :----------- | :--------------------------------------------------------- |
| 1.0    | 01/01/2021   | Criação do SOP inicial.                                    |
| 2.0    | 10/06/2022   | Inclusão da etapa de validação de impostos retidos.        |
| 3.0    | 05/11/2023   | Atualização de tela do ERP e inclusão de nova regra de CFOP. |
| 3.1    | 15/03/2024   | Pequena correção na descrição do passo 5.1.4.              |
```

### Template de Instrução de Trabalho Detalhada - Limpeza de Filtro de Ar Condicionado

```markdown
**INSTRUÇÃO DE TRABALHO: Limpeza de Filtro de Ar Condicionado Tipo Split (Modelo X)**

**Código:** MAN-IT-002
**Versão:** 1.0
**Data de Emissão:** 01/02/2024
**Setor:** Manutenção Predial
**Equipamento:** Ar Condicionado Split, Modelo X (Todos os equipamentos da empresa)
**Frequência:** Mensal ou conforme indicação do sistema de monitoramento de performance.

**1. Objetivo**
Garantir a limpeza eficaz dos filtros de ar condicionado tipo Split Modelo X para otimizar a qualidade do ar, manter a eficiência energética do equipamento e prolongar sua vida útil.

**2. Ferramentas e EPIs Necessários**
*   Escada de segurança (se necessário)
*   Luvas de proteção
*   Máscara de proteção (PFF2)
*   Óculos de segurança
*   Pano limpo e seco
*   Aspirador de pó com bico fino
*   Água corrente
*   Detergente neutro (opcional, para filtros muito sujos)
*   Balde (se for lavar o filtro em local distante de pia)

**3. Procedimento Detalhado**

**3.1. Preparação**
    1.  **Desligar:** Desligar o ar condicionado na tomada ou disjuntor para garantir total segurança elétrica.
    2.  **Posicionar Escada:** Posicionar a escada de forma estável e segura, se o equipamento estiver em altura.
    3.  **Colocar EPIs:** Vestir luvas, máscara e óculos de segurança.

**3.2. Remoção dos Filtros**
    1.  **Abrir Painel:** Com cuidado, abrir a tampa frontal do ar condicionado, levantando-a suavemente até que trave na posição aberta.
    2.  **Desencaixar Filtros:** Localizar os filtros de ar (geralmente duas telas retangulares). Desencaixá-los puxando-os para baixo ou para fora, seguindo a indicação do manual do equipamento (ver figura 1.1).
    3.  **Inspecionar:** Inspecionar os filtros quanto a danos (rasgos, deformações) e grau de sujidade.

**3.3. Limpeza dos Filtros**
    1.  **Remoção de Poeira Grossa (Seco):** Utilizar o aspirador de pó com bico fino para remover a poeira e sujeira mais grossa de ambos os lados do filtro.
    2.  **Lavagem (Opcional, para sujeira persistente):**
        *   Se os filtros estiverem muito sujos ou engordurados, lavá-los em água corrente fria.
        *   Aplicar uma pequena quantidade de detergente neutro e esfregar suavemente com as mãos ou uma escova macia (evitar escovas abrasivas).
        *   Enxaguar completamente para remover todo o sabão.
    3.  **Secagem:** Deixar os filtros secar completamente à sombra, em local arejado, antes de recolocá-los. NUNCA expor ao sol direto ou utilizar fontes de calor, pois pode deformar o material. Garantir que não haja umidade.

**3.4. Recolocação dos Filtros**
    1.  **Encaixar:** Após a secagem completa, encaixar os filtros de volta nas suas posições originais no ar condicionado, garantindo que estejam firmemente presos.
    2.  **Fechar Painel:** Fechar a tampa frontal do equipamento.
    3.  **Ligar:** Ligar o ar condicionado na tomada ou disjuntor.
    4.  **Testar:** Ligar o equipamento por 5 minutos para verificar o funcionamento normal e a ausência de ruídos estranhos.

**4. Registros**
*   Ficha de Manutenção Preventiva (MAN-REG-001): Registrar data da limpeza, nome do técnico, observações e próxima data prevista.

**5. Figuras de Referência**
*   **Figura 1.1:** Ilustração de como abrir o painel frontal e remover os filtros.
*   **Figura 1.2:** Exemplo de filtro sujo versus filtro limpo.
```

---

## Checklist

- [x] Escopo do processo claramente definido e acordado com stakeholders.
- [x] Todas as etapas do processo mapeadas e sequenciadas logicamente.
- [x] Responsabilidades de cada função ou pessoa explicitamente atribuídas (Matriz RACI incluída ou referenciada).
- [x] Termos técnicos, siglas e abreviações incomuns definidos em um glossário dentro do SOP.
- [x] Critérios de entrada e saída (inputs/outputs) de cada etapa especificados.
- [x] Pontos de decisão e caminhos alternativos (se aplicável) documentados com clareza.
- [x] Documentos de referência, formulários e sistemas associados listados e acessíveis.
- [x] Métricas de desempenho (KPIs) para monitoramento da eficácia do processo estabelecidas.
- [