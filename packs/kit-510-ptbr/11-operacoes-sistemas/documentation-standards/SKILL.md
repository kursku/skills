---
name: documentation-standards
description: "Documentation Standards — Skill especializada para estabelecer, manter e auditar padrões de documentação operacional e técnica."
license: MIT
metadata:
  version: 1.0.0
  author: Cafe Code AI
  category: 11-operacoes-sistemas
  updated: 2026-03-01
risk: safe
---

# Documentation Standards

Esta skill capacita o Claude a atuar como um especialista em padronização de documentação, cobrindo criação, manutenção e governança de documentos operacionais.

---

## Keywords

SOPs, Manuais Operacionais, Guia de Estilo, Versionamento de Documentos, Auditoria de Documentação, Ciclo de Vida do Documento, Governança de Conteúdo, Padrões de Nomenclatura, Acessibilidade da Informação, Controle de Revisão, Matriz RACI, Docs-as-Code.

---

## Quick Start

1.  **Centralizar Repositório**: Designar e configurar um repositório central (e.g., Confluence, SharePoint, GitLab Wiki) para todos os documentos operacionais.
2.  **Publicar Guia de Estilo**: Criar e divulgar um Guia de Estilo para Documentação Interna, cobrindo formatação, linguagem e estrutura.
3.  **Adotar Modelo Padrão de SOP**: Implementar um template único para Standard Operating Procedures (SOPs) e treinamentos para seu uso.
4.  **Agendar Auditorias Regulares**: Definir uma frequência (e.g., semestral) para auditorias de conformidade e atualização de documentos críticos.
5.  **Implementar Controle de Versão**: Garantir que todos os documentos novos e revisados utilizem um sistema de controle de versão claro (e.g., v1.0, v1.1).

---

## Core Workflows

### Workflow 1: Criação e Aprovação de um SOP Padronizado

Este workflow detalha a jornada completa de um novo Standard Operating Procedure (SOP) desde sua concepção até a publicação e comunicação, garantindo aderência aos padrões.

1.  **Escopo e Levantamento Inicial**:
    *   **Ação**: O analista de processo ou líder de equipe (responsável pelo novo SOP) inicia o processo, definindo o objetivo, o escopo operacional e as interfaces com outros processos.
    *   **Exemplo**: Para um SOP de "Provisionamento de Nova Conta de Usuário em Active Directory", o escopo incluiria desde a requisição formal até a confirmação da criação, excluindo a configuração de permissões de sistemas específicos. A equipe de TI (Service Desk e Infraestrutura) é consultada para levantar os passos práticos e requisitos técnicos.

2.  **Rascunho e Adaptação ao Template**:
    *   **Ação**: O responsável pelo SOP utiliza o template padrão de SOP da organização, preenchendo as seções de Título, Código, Versão (sempre iniciar com 0.1 para rascunho), Data de Emissão, Autor, Revisor(es) e Aprovador(es) designados. O conteúdo do procedimento é detalhado passo a passo.
    *   **Exemplo**: O rascunho `SOP-IT-005-ProvisionamentoUsuarioAD.v0.1.md` é criado. O procedimento lista: "1. Receber solicitação via sistema X. 2. Acessar ADUC. 3. Criar conta com padrão NOME.SOBRENOME. 4. Definir senha temporária. 5. Notificar solicitante e usuário." Imagens ou capturas de tela pertinentes são incluídas para clareza.

3.  **Revisão por Pares e Validação Técnica**:
    *   **Ação**: O rascunho é enviado para revisores designados (membros da equipe que executam o processo ou especialistas no assunto) para feedback sobre precisão técnica, clareza e completude. Alterações são incorporadas e a versão é atualizada (e.g., v0.2, v0.3).
    *   **Exemplo**: O SOP v0.1 é enviado para João (Service Desk) e Maria (Infraestrutura). João sugere adicionar um passo para verificar a disponibilidade do nome de usuário. Maria aponta uma configuração de grupo padrão que deve ser aplicada. Essas sugestões são implementadas, resultando no `SOP-IT-005-ProvisionamentoUsuarioAD.v0.2.md`.

4.  **Aprovação Formal e Atribuição de Versão Final**:
    *   **Ação**: Após as revisões, o SOP é submetido ao aprovador formal (gerente da área, líder técnico ou comitê de governança). Uma vez aprovado, a versão é promovida para 1.0.
    *   **Exemplo**: O gerente de TI, Carlos, revisa o `SOP-IT-005-ProvisionamentoUsuarioAD.v0.2.md`. Após confirmar que todos os requisitos foram atendidos e o conteúdo está alinhado com as políticas da empresa, ele aprova o documento. O arquivo é renomeado para `SOP-IT-005-ProvisionamentoUsuarioAD.v1.0.md`.

5.  **Publicação e Comunicação**:
    *   **Ação**: O SOP v1.0 é publicado no repositório central de documentação. Uma comunicação formal é enviada à equipe afetada, informando sobre o novo SOP e sua localização. Treinamentos podem ser agendados, se necessário.
    *   **Exemplo**: O `SOP-IT-005-ProvisionamentoUsuarioAD.v1.0.md` é salvo na pasta `/SOPs/IT/` do Confluence. Um e-mail é enviado para a equipe de TI com o link direto para o SOP, mencionando as principais mudanças ou a introdução do novo procedimento.

### Workflow 2: Auditoria e Manutenção de Documentação Existente

Este workflow descreve o processo sistemático para garantir que a documentação existente permaneça precisa, relevante e em conformidade com os padrões.

1.  **Agendamento da Auditoria**:
    *   **Ação**: O gestor de qualidade ou responsável pela governança de documentação define o cronograma de auditoria, especificando quais documentos ou categorias serão revisados e a frequência (ex: crítica anual, operacional semestral).
    *   **Exemplo**: Em janeiro, é agendada uma auditoria semestral para todos os SOPs do departamento de Operações de TI. Um cronograma detalhado é criado, listando `SOP-IT-001`, `SOP-IT-002`, `SOP-HR-010`, etc., com datas de início e fim da revisão para cada um.

2.  **Verificação de Conformidade com o Guia de Estilo**:
    *   **Ação**: A equipe de auditoria (ou revisor designado) verifica cada documento em relação ao Guia de Estilo da organização. Isso inclui checar a estrutura do cabeçalho, formatação, uso da linguagem, convenções de nomenclatura de arquivos e legibilidade.
    *   **Exemplo**: Para o `SOP-IT-001-GestaoIncidentes.v2.0.md`, verifica-se se o título, código, versão e data de emissão estão no formato correto. Observa-se se a linguagem utiliza voz ativa, se os termos técnicos estão consistentemente capitalizados e se não há jargões excessivos não explicados. É identificado que o documento não possui a seção "Referências", que é um item obrigatório do guia.

3.  **Validação de Conteúdo com Equipe Operacional**:
    *   **Ação**: O conteúdo técnico e operacional do documento é validado com os usuários que executam o processo. Isso pode ser feito através de entrevistas, observações ou simulações. O objetivo é confirmar se o procedimento descrito ainda reflete a realidade da execução e se é eficiente.
    *   **Exemplo**: Para o `SOP-HR-010-ProcessoOnboarding.v1.1.md`, a auditoria entrevista os analistas de RH que realizam o onboarding e os novos colaboradores. Descobre-se que o passo "Envio do formulário de acesso ao sistema de ponto" foi automatizado por uma nova ferramenta, tornando o passo manual obsoleto.

4.  **Atualização e Revisão do Documento**:
    *   **Ação**: Com base nos achados da verificação de conformidade e validação de conteúdo, o documento é revisado. As não-conformidades de estilo são corrigidas, e o conteúdo é atualizado para refletir as práticas atuais. A versão do documento é incrementada (e.g., de v1.0 para v1.1).
    *   **Exemplo**: O `SOP-IT-001-GestaoIncidentes.v2.0.md` é atualizado para `SOP-IT-001-GestaoIncidentes.v2.1.md`, adicionando a seção "Referências" e corrigindo alguns erros de formatação. O `SOP-HR-010-ProcessoOnboarding.v1.1.md` é atualizado para `SOP-HR-010-ProcessoOnboarding.v1.2.md`, removendo o passo obsoleto do formulário manual e adicionando uma nota sobre a nova ferramenta.

5.  **Aprovação e Arquivamento de Versões Antigas**:
    *   **Ação**: O documento revisado passa por um ciclo de aprovação simplificado, se necessário, e a nova versão é publicada. Versões antigas são arquivadas conforme a política de retenção da empresa, mantendo um histórico acessível.
    *   **Exemplo**: As versões atualizadas são aprovadas pelos respectivos gerentes. As versões `SOP-IT-001-GestaoIncidentes.v2.0.md` e `SOP-HR-010-ProcessoOnboarding.v1.1.md` são movidas para uma pasta de "Histórico de Versões" ou marcadas como obsoletas no sistema de gestão documental, enquanto as novas versões são publicadas ativamente.

---

## Templates

### Modelo de Standard Operating Procedure (SOP)

```markdown
# [Título do SOP]: [Breve descrição do processo]

| Campo           | Detalhes                                                    |
| :-------------- | :---------------------------------------------------------- |
| **Código**      | SOP-[Departamento]-[Número Sequencial] (Ex: SOP-TI-001)     |
| **Versão**      | [Número da Versão - Ex: 1.0, 1.1, 2.0]                      |
| **Data Emissão**| [DD/MM/AAAA]                                                |
| **Autor(es)**   | [Nome(s) do(s) responsável(eis) pela criação]               |
| **Revisor(es)** | [Nome(s) do(s) responsável(eis) pela revisão técnica]       |
| **Aprovador(es)**| [Nome(s) do(s) gestor(es) ou comitê de aprovação]          |
| **Vigência**    | [DD/MM/AAAA] (Ex: 01/01/2024 - Válido por 12 meses)         |
| **Revisão Próxima**| [DD/MM/AAAA] (Ex: 01/01/2025)                             |

---

## 1. Objetivo

Descrever os passos padronizados para [descrever o propósito do SOP, o que ele busca alcançar].
*Exemplo: Descrever os passos padronizados para a criação e configuração inicial de novas contas de usuário no sistema Active Directory (AD) para colaboradores recém-contratados.*

## 2. Escopo

Este SOP se aplica a [quais processos, sistemas, equipes e/ou pessoas estão envolvidas].
*Exemplo: Este SOP se aplica à equipe de Service Desk e Infraestrutura de TI e abrange o processo de provisionamento de contas de usuário para todos os novos colaboradores, estagiários e terceiros que necessitem de acesso à rede corporativa e sistemas baseados em AD.*

## 3. Responsabilidades

| Papel/Departamento | Responsabilidades                                                                       |
| :----------------- | :-------------------------------------------------------------------------------------- |
| Analista de Service Desk | Receber requisição, executar criação da conta, notificar conclusão.                  |
| Analista de Infraestrutura | Suporte em caso de problemas técnicos, validação de configurações de segurança.      |
| Gerente de TI      | Aprovação final de contas com acessos especiais, auditoria de conformidade.            |

## 4. Pré-requisitos

*   Acesso administrativo ao Active Directory Users and Computers (ADUC).
*   Formulário "Solicitação de Acesso de Novo Colaborador" preenchido e aprovado pelo RH.
*   Conhecimento das políticas de nomenclatura e segurança de senhas da empresa.

## 5. Procedimento

Descrever os passos de forma clara, concisa e numerada. Utilize voz ativa.

1.  **Receber Solicitação**:
    *   Aguardar o recebimento do formulário "Solicitação de Acesso de Novo Colaborador" via sistema de chamados (Zendesk/Jira Service Management).
    *   Verificar se todos os campos obrigatórios estão preenchidos (Nome Completo, E-mail Corporativo, Departamento, Cargo, Data de Admissão).
    *   *Exemplo de Screenshot:* [Anexar imagem do formulário preenchido]

2.  **Acessar Active Directory Users and Computers (ADUC)**:
    *   Conectar-se ao servidor de domínio via RDP ou acessar console local.
    *   Abrir "Active Directory Users and Computers" (dsa.msc).

3.  **Criar Nova Conta de Usuário**:
    *   Navegar até a OU (Unidade Organizacional) correspondente ao departamento do novo colaborador (e.g., `Dominio.com/Empresa/Usuarios/Departamentos/TI`).
    *   Clicar com o botão direito na OU, selecionar `New > User`.
    *   Preencher os campos:
        *   `First name`: [Primeiro Nome do Colaborador]
        *   `Last name`: [Sobrenome do Colaborador]
        *   `User logon name`: [PrimeiroNome].[Sobrenome] (Ex: joao.silva)
        *   `User logon name (pre-Windows 2000)`: [PrimeiroNome].[Sobrenome]
    *   *Atenção:* Seguir a política de nomenclatura de usuários: `primeironome.sobrenome`.

4.  **Definir Senha Inicial**:
    *   Definir uma senha temporária complexa, seguindo a política de senhas da empresa (Ex: `Temp@2024!`).
    *   Marcar as opções:
        *   `User must change password at next logon`.
        *   `Password never expires` (SOMENTE para contas de serviço, não para usuários).
    *   *Evitar:* Reutilizar senhas ou usar senhas genéricas.

5.  **Configurar Membro de Grupos Padrão**:
    *   Na aba `Member Of`, adicionar os grupos de segurança padrão para o cargo e departamento.
    *   *Exemplo: Todos os usuários devem ser membros de "Domain Users" e "VPN-Access". Analistas de TI devem ser membros de "IT-Staff".*

6.  **Validar Criação da Conta**:
    *   Testar o login com a conta recém-criada em uma máquina de teste.
    *   Verificar se os acessos aos recursos de rede padrão estão funcionando.

7.  **Notificar RH e Usuário**:
    *   Atualizar o chamado no sistema, indicando a conclusão do provisionamento e a senha temporária.
    *   Enviar e-mail para o RH e, se aplicável, para o novo colaborador com instruções de primeiro acesso e alteração de senha.

## 6. Referências

*   [Link para Guia de Estilo de Documentação Interna](https://intranet.empresa.com/docs/guia-estilo)
*   [Link para Política de Segurança de Acesso](https://intranet.empresa.com/docs/politica-seguranca)
*   [Link para Matriz de Grupos de Segurança AD](https://intranet.empresa.com/docs/matriz-grupos-ad)

## 7. Histórico de Revisão

| Versão | Data         | Autor(es)      | Descrição da Mudança                                                                         |
| :----- | :----------- | :------------- | :------------------------------------------------------------------------------------------- |
| 0.1    | 05/01/2024   | João Silva     | Rascunho inicial.                                                                            |
| 0.2    | 12/01/2024   | Maria Souza    | Inclusão de verificação de disponibilidade de nome de usuário e configuração de grupo padrão.|
| 1.0    | 20/01/2024   | Carlos Santos  | Aprovação final e publicação.                                                                |
| 1.1    | 15/07/2024   | João Silva     | Atualização do link da Política de Segurança.                                                |
```

### Guia de Estilo para Documentação Interna

```markdown
# Guia de Estilo para Documentação Interna

---

## 1. Propósito

Este guia estabelece os padrões para a criação, revisão e manutenção de toda a documentação interna da [Nome da Empresa], garantindo consistência, clareza e facilidade de uso.

---

## 2. Estrutura Padrão do Documento

Todos os documentos devem seguir uma estrutura lógica e padronizada. O modelo de SOP fornecido é o padrão para procedimentos.

### 2.1. Cabeçalho

*   **Títulos**: Use o formato `# Título Principal`, `## Subtítulo`, `### Sub-subtítulo`.
*   **Campos de Metadados**: Todos os documentos críticos (SOPs, Políticas) DEVEM incluir uma tabela de metadados no início com: Código, Versão, Data Emissão, Autor(es), Revisor(es), Aprovador(es), Vigência, Próxima Revisão.
*   **Códigos de Documento**: Seguir o padrão `[Tipo]-[Departamento]-[Número Sequencial]`. Ex: `SOP-TI-001`, `POL-RH-005`, `MAN-FIN-002`.

### 2.2. Seções Obrigatórias (para SOPs e Manuais)

*   **Objetivo**: Declaração concisa do propósito do documento.
*   **Escopo**: O que o documento cobre e o que não cobre.
*   **Responsabilidades**: Quem é responsável por cada etapa ou aspecto.
*   **Pré-requisitos**: Condições ou recursos necessários antes de iniciar o procedimento.
*   **Procedimento**: Passos numerados e detalhados.
*   **Referências**: Links para documentos relacionados (políticas, outros SOPs, manuais de sistemas).
*   **Histórico de Revisão**: Tabela com Versão, Data, Autor, Descrição da Mudança.

---

## 3. Linguagem e Estilo

### 3.1. Clareza e Concisão

*   **Voz Ativa**: Utilize a voz ativa para descrever ações.
    *   *Evitar:* "A solicitação deve ser recebida pelo analista."
    *   *Preferir:* "O analista recebe a solicitação."
*   **Linguagem Objetiva**: Evite jargões desnecessários ou termos ambíguos. Se um termo técnico for essencial, defina-o na primeira ocorrência ou em um glossário.
*   **Frases Curtas**: Mantenha as frases diretas e fáceis de entender.

### 3.2. Termos e Acrônimos

*   **Definição**: Todos os acrônimos e termos técnicos devem ser definidos na primeira vez que aparecem no documento.
    *   *Exemplo: "Standard Operating Procedure (SOP)".*
*   **Consistência**: Use a mesma terminologia e capitalização para termos em todos os documentos.
    *   *Evitar:* "Active Directory" e "active directory" no mesmo documento.
    *   *Preferir:* "Active Directory" consistentemente.

---

## 4. Formatação

### 4.1. Textos

*   **Negrito**: Para enfatizar termos-chave, nomes de botões ou comandos.
*   **Itálico**: Para títulos de livros, nomes de sistemas ou termos em outro idioma.
*   **Listas**: Use listas numeradas para procedimentos sequenciais e listas com marcadores para itens não ordenados.

### 4.2. Imagens e Diagramas

*   **Qualidade**: Imagens devem ser claras, legíveis e relevantes.
*   **Legendas**: Todas as imagens e diagramas devem ter legendas descritivas.
*   **Contexto**: Incorpore imagens de forma que complementem o texto, não o substituam.
*   **Ferramentas**: Preferir Miro, Draw.io ou Lucidchart para diagramas complexos.

### 4.3. Código e Comandos

*   **Blocos de Código**: Use blocos de código (``` `linguagem` ... ```) para comandos, scripts ou trechos de código.
    *   *Exemplo:*
        ```powershell
        Get-ADUser -Filter 'Enabled -eq $true' | Select-Object Name, SamAccountName
        ```
*   **Comandos Inline**: Use `backticks` para comandos curtos ou nomes de variáveis no texto.
    *   *Exemplo: Execute o comando `ipconfig /all` no Prompt de Comando.*

---

## 5. Convenções de Nomenclatura de Arquivos

*   `[TipoDoc]-[Departamento]-[Número Sequencial]-[Breve Descrição].v[Versão].extensao`
    *   *Exemplos:*
        *   `SOP-TI-001-ProvisionamentoUsuarioAD.v1.0.md`
        *   `POL-RH-005-UsoEquipamentos.v2.1.pdf`
        *   `MAN-FIN-002-FechamentoCaixa.v1.0.docx`

---

## 6. Controle de Versão

*   **Sistema Semântico**: Utilizar versionamento semântico: `MAIOR.MENOR.PATCH`.
    *   `MAIOR` (1.0.0): Mudanças significativas, reestruturações, grandes atualizações de processo.
    *   `MENOR` (0.1.0): Novas funcionalidades, seções adicionadas, mudanças de médio impacto.
    *   `PATCH` (0.0.1): Correções de erros, pequenas edições, atualizações de links.
*   **Registro**: Manter um histórico de revisão detalhado em cada documento.

---

## 7. Acessibilidade

*   **Repositório Central**: Todos os documentos devem ser armazenados em um repositório centralizado de fácil acesso (Confluence, SharePoint, Intranet).
*   **Permissões**: As permissões de acesso devem ser configuradas para garantir que o público-alvo possa visualizar e, quando aplicável, editar os documentos.

---

## 8. Revisão e Aprovação

*   **Revisão Periódica**: Documentos críticos devem ser revisados anualmente ou a cada grande mudança de processo.
*   **Ciclo de Aprovação**: Seguir o fluxo de aprovação definido para cada tipo de documento.
```

---

## Checklist

- [x] O documento possui cabeçalho padrão com Título, Código, Versão, Data de Emissão, Autor(es), Revisor(es) e Aprovador(es) preenchidos?
- [x] O código do documento segue a convenção `[Tipo]-[Departamento]-[Número Sequencial]` (Ex: `SOP-TI-001`)?
- [x] O título e os subtítulos utilizam a hierarquia de `H1`, `H2`, `H3` corretamente?
- [x] A linguagem é clara, concisa e objetiva, utilizando voz ativa?
- [x] Todos os acrônimos e termos técnicos são definidos na primeira ocorrência?
- [x] O documento contém as seções obrigatórias (Objetivo, Escopo, Responsabilidades, Pré-requisitos, Procedimento, Referências, Histórico de Revisão)?
- [x] O procedimento é detalhado em passos numerados e sequenciais, fácil de seguir?
- [x] Imagens e diagramas são claros, relevantes e acompanhados de legendas descritivas?
- [x] Blocos de código ou comandos estão formatados corretamente (e.g., com `backticks` ou blocos de código)?
- [x] O nome do arquivo segue a convenção de nomenclatura (Ex: `SOP-TI-001-ProvisionamentoUsuarioAD.v1.0.md`)?
- [x] O histórico de revisão está atualizado e detalha as mudanças de cada versão?
- [x] O documento foi revisado por pares e aprovado pelos stakeholders designados antes da publicação?

---

## Métricas de Referência

| Métrica                                | Benchmark  | Meta       |
| :------------------------------------- | :--------- | :--------- |
| Taxa de Aderência a Padrões de Documento | 85%        | >95%       |
| Tempo Médio para Publicação de SOP (após rascunho) | 10 dias úteis | <7 dias úteis |
| Índice de Desatualização de Documentos Críticos | 15%        | <5%        |
| Número de Incidentes Causados por Documentação Incorreta | 3/mês      | <1/mês     |
| Pontuação Média de Feedback de Usuários (Clareza/Utilidade) | 3.8/5.0    | >4.2/5.0   |
| % de Documentos com Histórico de Revisão Completo | 70%        | >90%       |

---

## Erros Comuns

1.  **Documentação Obsoleta**: Muitas organizações falham em estabelecer um ciclo de vida de documento e revisões periódicas.
    *   **Como evitar**: Implemente um cronograma rigoroso de auditoria e revisão para todos os documentos críticos. Por exemplo, SOPs de TI devem ser revisados anualmente ou a cada mudança significativa no sistema/processo. O template de SOP já inclui "Revisão Próxima".
    *   **Exemplo**: O `SOP-FIN-003-FechamentoMensal.v1.0` está sendo usado, mas a equipe de contabilidade implementou um novo software que automatiza vários passos. Sem revisão, o SOP desatualizado causa retrabalho e confusão. Uma auditoria anual teria identificado a necessidade de atualização.

2.  **Falta de Padronização e Consistência**: Documentos criados por diferentes autores com estilos, formatos e terminologias variadas dificultam a compreensão e a busca por informações.
    *   **Como evitar**: Faça cumprir um Guia de Estilo de Documentação (como o template fornecido) e utilize templates padronizados para cada tipo de documento. Realize treinamentos e sessões de conscientização.
    *   **Exemplo**: Um novo analista precisa configurar um servidor, mas encontra manuais onde "servidor de aplicação" é chamado de "APP Server" em um, "Servidor AP" em outro, e "host de aplicação" em um terceiro, gerando ambiguidade e perda de tempo. A adesão ao Guia de Estilo asseguraria a terminologia consistente.

3.  **Acessibilidade Limitada ou Dispersa**: Documentos armazenados em locais diferentes (pastas pessoais, e-mails, nuvens não corporativas) ou com permissões restritivas impedem o acesso rápido e colaborativo.
    *   **Como evitar**: Utilize um repositório centralizado e único para toda a documentação, com uma estrutura de pastas lógica e permissões de acesso baseadas em grupos, garantindo que o público-alvo tenha acesso de leitura por padrão.
    *   **Exemplo**: O SOP de "Integração de Novos Fornecedores" está na pasta pessoal do gerente de compras no OneDrive, inacessível para a equipe de contas a pagar que precisa dele diariamente. A migração para um SharePoint com permissões de grupo resolveria o problema.

---

## Dicas Avançadas

1.  **Implementação de "Docs-as-Code"**: Gerencie sua documentação técnica e operacional como código, usando Markdown ou AsciiDoc em repositórios Git (e.g., GitLab, GitHub, Bitbucket). Isso permite controle de versão robusto, revisões via Pull Requests e integração contínua (CI/CD) para geração de HTML/PDF.
    *   **Exemplo Prático**: Uma equipe de DevOps mantém SOPs para implantação de serviços em um repositório GitLab. Cada alteração no SOP é um `merge request`, revisado por pares antes de ser incorporado e automaticamente compilado em um site