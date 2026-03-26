---
name: data-retention-policy
description: "Data Retention Policy — Skill especializada para data retention policy"
license: MIT
metadata:
  version: 1.0.0
  author: Cafe Code AI
  category: 07-juridico-compliance
  updated: 2026-03-01
risk: critical
---

# Data Retention Policy

Esta skill capacita o Claude a elaborar, implementar e auditar políticas de retenção de dados, garantindo conformidade legal e gestão eficiente do ciclo de vida da informação.

---

## Keywords

LGPD, GDPR, Retenção de Dados, Descarte Seguro, Compliance Digital, Ciclo de Vida do Dado, Prazos Legais, Classificação de Dados, Privacidade de Dados, Auditoria de Dados, Gestão de Registros, Eliminação de Dados.

---

## Quick Start

1.  Inventariar e classificar todos os tipos de dados processados pela organização.
2.  Identificar as bases legais e requisitos regulatórios (ex: LGPD, CTN) para cada categoria de dado.
3.  Definir prazos de retenção específicos para cada tipo de dado, com justificativa clara.
4.  Estabelecer e documentar os métodos seguros de descarte de dados expirados.
5.  Comunicar formalmente a política de retenção a todas as partes interessadas internas.

---

## Core Workflows

### Workflow 1: Elaboração e Documentação da Política de Retenção de Dados

Este workflow detalha a criação de uma política de retenção de dados robusta e legalmente defensável, desde o mapeamento inicial até a documentação final.

1.  **Mapeamento e Classificação Abrangente de Dados Processados:**
    *   **Ação:** Realizar um inventário completo de todos os dados coletados, armazenados e processados pela organização, abrangendo sistemas, bancos de dados, arquivos físicos e digitais, e-mails e backups.
    *   **Exemplo:** "Identifique dados de clientes (nome, CPF, endereço, histórico de compras), dados financeiros (faturas, comprovantes de pagamento), dados de RH (currículos, holerites, dados de saúde ocupacional) e dados de log (endereço IP, data/hora de acesso, ações do usuário). Classifique cada item como 'Dados Pessoais Comuns', 'Dados Pessoais Sensíveis', 'Dados Corporativos Confidenciais', etc."
    *   **Ferramenta:** Utilize ferramentas de Data Discovery and Classification (DDC) como Microsoft Purview ou OneTrust DataDiscovery para automatizar a varredura e categorização em ambientes complexos.

2.  **Análise de Requisitos Legais, Regulatórios e Contratuais:**
    *   **Ação:** Para cada categoria de dado mapeada, pesquisar e identificar as leis, regulamentos e obrigações contratuais que impõem prazos de retenção ou descarte.
    *   **Exemplo:** "Para dados de clientes no Brasil, consulte a Lei Geral de Proteção de Dados (LGPD, Lei nº 13.709/2018, Art. 7º e Art. 16). Para dados financeiros, a Circular nº 3.978 do Banco Central do Brasil. Para dados fiscais, o Código Tributário Nacional (CTN, Lei nº 5.172/1966, Art. 173). Prazos comuns incluem 5 anos para notas fiscais, 20 anos para prontuários médicos (Lei nº 13.787/2018), 6 meses para logs de acesso (Marco Civil da Internet, Lei nº 12.965/2014, Art. 15)."
    *   **Consideração:** Verifique também contratos com clientes e fornecedores que possam ter cláusulas específicas sobre retenção e descarte.

3.  **Definição Detalhada dos Prazos de Retenção e Bases Legais:**
    *   **Ação:** Para cada tipo de dado, estabelecer um prazo de retenção específico e documentar a base legal correspondente, bem como a finalidade da retenção.
    *   **Exemplo:**
        *   "Dados de cadastro de clientes (nome, CPF, e-mail): 5 anos após o término da relação contratual. Base legal: Cumprimento de obrigação legal ou regulatória (ex: Código de Defesa do Consumidor, LGPD Art. 7º, II) e Exercício regular de direitos em processo (LGPD Art. 7º, VI)."
        *   "Dados de candidatos não contratados: 6 meses após o término do processo seletivo. Base legal: Legítimo Interesse (LGPD Art. 7º, IX), para fins de reavaliação ou defesa em questionamentos, com descarte seguro posterior."
        *   "Dados de logs de transações financeiras: 10 anos. Base legal: Cumprimento de obrigação legal ou regulatória (ex: Lei nº 9.613/98 - Lei de Lavagem de Dinheiro)."

4.  **Elaboração dos Procedimentos de Descarte Seguro e Irreversível:**
    *   **Ação:** Definir os métodos técnicos e operacionais para a eliminação segura e irreversível dos dados quando o prazo de retenção expirar.
    *   **Exemplo:**
        *   "Para dados digitais: Utilizar sobrescrita de dados (data wiping) com padrões reconhecidos (ex: DoD 5220.22-M), desmagnetização para mídias magnéticas, ou destruição física do suporte (ex: fragmentação de discos rígidos). Para dados em nuvem, confirmar as políticas de descarte do provedor."
        *   "Para dados físicos: Incineração, trituração ou fragmentação certificada (ex: DIN 66399 P-4 ou superior). O processo deve incluir a verificação por duas pessoas e registro formal."

5.  **Documentação Formal e Aprovação da Política:**
    *   **Ação:** Compilar todas as informações em um documento formal intitulado "Política de Retenção e Descarte de Dados". O documento deve ser claro, objetivo e acessível.
    *   **Exemplo:** "A política deve incluir escopo, categorias de dados, prazos, bases legais, procedimentos de descarte, responsabilidades, e processo de revisão. O documento final deve ser aprovado pela alta direção, DPO (Encarregado de Dados) e, se aplicável, pelo Comitê de Privacidade. A versão 1.0.0 foi aprovada em 15/03/2024 pelo Conselho Administrativo e DPO."

### Workflow 2: Implementação e Monitoramento Contínuo da Retenção de Dados

Este workflow aborda a aplicação prática da política de retenção, garantindo sua execução e revisão contínua.

1.  **Integração Tecnológica e Automação de Processos:**
    *   **Ação:** Implementar as regras de retenção nos sistemas de TI existentes, buscando automatizar o máximo possível os processos de marcação, arquivamento e descarte de dados.
    *   **Exemplo:** "Configure políticas de retenção no Microsoft 365 (e.g., para Exchange Online, SharePoint, OneDrive) para e-mails e documentos. Utilize funcionalidades de Information Lifecycle Management (ILM) em sistemas ERP (ex: SAP ILM) e CRM para gerenciar o ciclo de vida dos dados de clientes. Desenvolva scripts para identificar e remover automaticamente dados de logs após 6 meses em servidores de aplicação."
    *   **Tecnologia:** Explore ferramentas de arquivamento de dados e módulos de gerenciamento de dados inativos para mover dados para armazenamento de baixo custo antes do descarte.

2.  **Treinamento e Conscientização Regular da Equipe:**
    *   **Ação:** Realizar treinamentos periódicos e campanhas de conscientização para todos os colaboradores que manipulam dados, reforçando a importância da política de retenção e seus procedimentos.
    *   **Exemplo:** "Ministrar sessões de treinamento anuais para equipes de vendas, RH, TI e jurídico, com foco em cenários práticos como 'Onde armazenar documentos de RH?', 'Quando um e-mail de cliente pode ser apagado?' e 'Como solicitar o descarte de dados antigos'. Distribua um guia rápido de consulta sobre os prazos e contatos para dúvidas."
    *   **Impacto:** Reduz significativamente erros humanos e o risco de retenção indevida ou descarte prematuro.

3.  **Auditoria e Verificação Periódica da Conformidade:**
    *   **Ação:** Estabelecer um cronograma de auditorias internas e externas para verificar a aplicação efetiva da política de retenção de dados e identificar possíveis desvios.
    *   **Exemplo:** "Realize auditorias internas semestrais. Verifique amostras de dados em sistemas chave para confirmar se os prazos de retenção estão sendo aplicados corretamente. Revise os logs de descarte para garantir que todas as eliminações foram registradas e executadas conforme o procedimento. Simule um incidente de vazamento para avaliar a capacidade de identificar e isolar dados dentro e fora do prazo de retenção."
    *   **Metodologia:** Utilize frameworks como ISO 27001 ou NIST para estruturar as auditorias.

4.  **Processo de Resposta a Solicitações de Titulares e Incidentes:**
    *   **Ação:** Desenvolver procedimentos claros para atender a solicitações de titulares de dados (ex: direito à exclusão) e para gerenciar incidentes relacionados à retenção (ex: dados retidos indevidamente ou descartados prematuramente).
    *   **Exemplo:** "Para solicitações de exclusão (LGPD Art. 18, IV), o processo deve incluir a verificação da identidade do solicitante, a identificação dos dados em questão e a avaliação da existência de bases legais que justifiquem a retenção (ex: cumprimento de obrigação legal). Em caso de dados retidos indevidamente, o protocolo é: descarte imediato, registro da falha e análise de causa raiz para evitar recorrências."
    *   **Ferramenta:** Utilize um sistema de gestão de solicitações de titulares (DSAR - Data Subject Access Request) para rastrear e gerenciar os prazos de resposta.

5.  **Revisão e Atualização Contínua da Política:**
    *   **Ação:** Estabelecer um processo formal para revisão e atualização periódica da política de retenção, levando em conta mudanças na legislação, nos processos de negócio e nas tecnologias.
    *   **Exemplo:** "A política deve ser revisada anualmente ou sempre que houver novas regulamentações (ex: decisões da ANPD, novas leis setoriais), aquisições de empresas, lançamento de novos produtos/serviços que alterem a coleta de dados, ou mudanças significativas na arquitetura de TI. A última revisão da política de 2023 incorporou as diretrizes da ANPD sobre relatórios de impacto à proteção de dados."

---

## Templates

### Seção de Prazos de Retenção da Política de Dados

```
### Seção 5. Prazos de Retenção e Fundamentação Legal

A [Nome da Organização S.A.] estabelece os seguintes prazos de retenção para as principais categorias de dados, fundamentados nas bases legais aplicáveis conforme a Lei Geral de Proteção de Dados (LGPD) e outras legislações pertinentes:

| Categoria de Dados | Exemplos de Dados | Base Legal (LGPD) | Prazo de Retenção | Observações |
|--------------------|-------------------|-------------------|-------------------|-------------|
| **Dados de Clientes Ativos** | Nome, CPF, Endereço, E-mail, Histórico de Compras, Dados de Pagamento | Execução de Contrato (Art. 7º, V) | Durante toda a relação contratual | Essencial para a prestação do serviço/venda do produto. |
| **Dados de Clientes Inativos (Pós-Contratual)** | Nome, CPF, Contrato, Histórico de Faturamento | Cumprimento de Obrigação Legal/Regulatória (Art. 7º, II), Exercício Regular de Direitos (Art. 7º, VI) | 5 anos após o término da relação contratual | Necessário para defesa em processos consumeristas (CDC) ou tributários (CTN, Art. 173). |
| **Dados de Funcionários (Pós-Vínculo Empregatício)** | Holerites, Ficha de Registro, Atestados Médicos, Informações Previdenciárias | Cumprimento de Obrigação Legal/Regulatória (Art. 7º, II), Exercício Regular de Direitos (Art. 7º, VI) | 20 anos após o desligamento | Indispensável para processos trabalhistas e previdenciários (Lei nº 8.213/91). |
| **Dados Contábeis e Fiscais** | Notas Fiscais (entrada/saída), Livros Contábeis, Comprovantes de Pagamento | Cumprimento de Obrigação Legal/Regulatória (Art. 7º, II) | 5 anos (CTN, Art. 173), podendo ser 10 anos para previdenciário | Prazo para fiscalização e auditoria da Receita Federal e órgãos fiscais. |
| **Dados de Log de Acesso** | Endereço IP, Data e Hora de Acesso, Ações Realizadas no Sistema | Cumprimento de Obrigação Legal/Regulatória (Art. 7º, II), Legítimo Interesse (Art. 7º, IX) | 6 meses (Marco Civil da Internet, Art. 15) | Para fins de segurança da informação, rastreabilidade e prevenção de fraudes. |
| **Dados de Candidatos (Não Contratados)** | Currículos, Cartas de Apresentação, Avaliações de Entrevistas | Legítimo Interesse (Art. 7º, IX) | 6 meses após o encerramento do processo seletivo | Para fins de reavaliação em futuras vagas ou defesa em questionamentos de processo seletivo. |
| **Dados de Marketing (Leads)** | Nome, E-mail, Telefone, Histórico de Interação | Consentimento (Art. 7º, I), Legítimo Interesse (Art. 7º, IX) | 1 ano após