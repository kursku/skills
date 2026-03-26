---
name: knowledge-base-setup
description: "Knowledge Base Setup — Skill especializada para knowledge base setup"
license: MIT
metadata:
  version: 1.0.0
  author: Cafe Code AI
  category: 11-operacoes-sistemas
  updated: 2026-03-01
risk: safe
---

# Knowledge Base Setup

Esta skill capacita o Claude a arquitetar, implementar e otimizar bases de conhecimento para processos operacionais e suporte, transformando informações dispersas em recursos acessíveis e acionáveis.

---

## Keywords

Base de Conhecimento, Gestão do Conhecimento, SOPs Digitais, Documentação Operacional, Content Strategy, Taxonomia de Conteúdo, Workflow KB, Engajamento do Usuário, Governança de Conteúdo, Melhoria Contínua, Suporte Interno, Autonomia Operacional.

---

## Quick Start

1.  **Mapear Prioridades:** Inicie identificando os 5 processos internos mais questionados ou que causam maior gargalo na equipe (ex: onboarding de novos colaboradores, configuração de VPN, solicitação de reembolso, abertura de chamado de TI, processo de férias).
2.  **Escolher Ferramenta:** Selecione uma plataforma robusta e escalável para abrigar a KB, como Confluence, Notion, SharePoint Online, Zendesk Guide ou Freshservice Solutions. Para equipes pequenas, Google Sites ou Slab podem ser suficientes.
3.  **Estrutura Inicial:** Defina uma taxonomia de conteúdo com pelo menos 3 categorias principais e 2 subcategorias para cada (ex: `Recursos Humanos/Admissão`, `Tecnologia/Infraestrutura`, `Financeiro/Despesas`).
4.  **Criar Conteúdo Piloto:** Desenvolva 3 artigos completos para os processos prioritários usando um template de SOP padronizado. Ex: "SOP: Processo de Solicitação de Férias", "Guia: Configuração de Acesso VPN", "FAQ: Uso do Sistema de Reembolso".
5.  **Designar Embaixadores:** Nomeie 2-3 colaboradores-chave de diferentes áreas para testar, validar e fornecer feedback inicial sobre a usabilidade e relevância do conteúdo da KB.

---

## Core Workflows

### Workflow 1: Estruturação e Criação de Conteúdo da KB para Processos Operacionais

Este workflow detalha a criação sistemática de artigos e SOPs para a base de conhecimento, garantindo padronização e relevância.

**Passos Detalhados:**

1.  **Identificação de Temas Críticos (0-1 dia):**
    *   **Ação:** Reúna-se com líderes de equipe (RH, TI, Operações) para identificar os 10 processos que mais geram dúvidas ou demandam tempo de suporte. Foque em processos repetitivos e de alto volume.
    *   **Exemplo:** A equipe de TI reporta 20 chamados/semana sobre "Configuração de Ambiente de Desenvolvimento". A equipe de RH tem 15 perguntas/semana sobre "Benefícios Flexíveis". Estes são candidatos a artigos de KB.
2.  **Definição da Taxonomia e Template (1-2 dias):**
    *   **Ação:** Crie uma estrutura de categorias e subcategorias lógica e intuitiva. Desenvolva um template padrão para todos os artigos/SOPs, que inclua seções como `Título`, `Propósito`, `Pré-requisitos`, `Passos Detalhados`, `Resultados Esperados`, `Responsável`, `FAQ` e `Data da Última Revisão`.
    *   **Exemplo:**
        *   **Categorias:** `RH`, `TI`, `Financeiro`, `Operações`, `Marketing`.
        *   **Subcategorias RH:** `Admissão`, `Benefícios`, `Férias`, `Desligamento`.
        *   **Template SOP:** Ver seção "Templates".
3.  **Designação de Donos de Conteúdo (0.5 dia):**
    *   **Ação:** Para cada tema crítico ou categoria de conteúdo, designe um "dono" (content owner) da área responsável. Este será o especialista que criará o rascunho e manterá o conteúdo atualizado.
    *   **Exemplo:** O Analista Sênior de RH, Maria Silva, é a dona dos artigos de `RH/Benefícios`. O Coordenador de TI, João Santos, é o dono dos artigos de `TI/Infraestrutura`.
4.  **Criação do Artigo/SOP (2-5 dias por artigo):**
    *   **Ação:** O dono do conteúdo cria o rascunho do artigo ou SOP na ferramenta de KB, seguindo o template definido. Inclua capturas de tela, vídeos curtos e listas numeradas para clareza. Use linguagem clara e objetiva.
    *   **Exemplo:** João Santos cria o artigo "Configuração de Acesso VPN para Colaboradores Remotos" com 7 passos, incluindo screenshots do cliente VPN e dicas de troubleshooting. Maria Silva cria o "SOP: Solicitação de Reembolso de Despesas" com o formulário anexado e regras de aprovação.
5.  **Revisão, Aprovação e Publicação (1-2 dias por artigo):**
    *   **Ação:** O rascunho é enviado para revisão por um segundo especialista da área e, se aplicável, por um revisor de compliance ou qualidade. Após aprovação, o artigo é publicado e indexado corretamente.
    *   **Exemplo:** O artigo de VPN de João é revisado pelo Gerente de TI e, uma vez aprovado, é publicado na categoria `TI/Infraestrutura` com tags como `VPN`, `Acesso Remoto`, `Segurança`.

### Workflow 2: Manutenção e Melhoria Contínua da Base de Conhecimento

Este workflow garante que a KB permaneça atualizada, relevante e eficaz ao longo do tempo.

**Passos Detalhados:**

1.  **Coleta de Feedback Contínuo (Diário/Semanal):**
    *   **Ação:** Implemente mecanismos de feedback direto nos artigos (ex: "Este artigo foi útil? Sim/Não", campo de comentários). Monitore termos de busca que não retornam resultados.
    *   **Exemplo:** Após ler o artigo "Como Solicitar Atestado Médico", o colaborador clica em "Não" na pergunta de utilidade e escreve "Não encontrei informações sobre atestados de acompanhante". Isso gera um alerta para o dono do conteúdo de RH.
2.  **Análise de Métricas de Desempenho (Mensal):**
    *   **Ação:** Revise relatórios da plataforma de KB sobre visualizações de página, tempo médio na página, taxa de artigos úteis, termos de busca mais frequentes, buscas sem resultados e artigos mais antigos sem revisão.
    *   **Exemplo:** Relatório revela que "Processo de Onboarding" é o artigo mais acessado, mas tem uma taxa de "Não útil" de 30%. O artigo "Procedimento de Backup de Dados" não é acessado há 6 meses e foi criado há 2 anos.
3.  **Agendamento e Execução de Revisões Periódicas (Trimestral/Semestral):**
    *   **Ação:** Estabeleça um cronograma de revisão para cada categoria ou artigo crítico. Defina uma política, ex: SOPs operacionais críticos revisados trimestralmente; guias gerais anualmente. Donos de conteúdo são notificados automaticamente.
    *   **Exemplo:** A cada trimestre, o sistema notifica João Santos que os artigos da categoria `TI/Infraestrutura` precisam ser revisados. Ele verifica se as configurações de VPN ou os URLs de sistemas mudaram.
4.  **Atualização e Arquivamento de Conteúdo (Conforme Necessário):**
    *   **Ação:** Com base no feedback, métricas ou mudanças nos processos, os donos de conteúdo atualizam os artigos. Conteúdo obsoleto deve ser movido para um arquivo ou despublicado, com redirecionamento se aplicável.
    *   **Exemplo:** A política de reembolso da empresa mudou. Maria Silva atualiza o "SOP: Solicitação de Reembolso de Despesas", adiciona uma nova versão e arquiva a versão antiga. Um artigo sobre "Software Legado X" é despublicado e um link para o novo software é adicionado.
5.  **Comunicação de Atualizações (Semanal/Mensal):**
    *   **Ação:** Comunique as principais atualizações e novos conteúdos da KB para os colaboradores através de canais internos (ex: newsletter, Slack, Teams). Isso aumenta o engajamento e a conscientização sobre os recursos disponíveis.
    *   **Exemplo:** Uma newsletter interna destaca "Novo artigo: Guia Completo de Benefícios Flexíveis" e "Atualização importante no SOP de Solicitação de Férias".

---

## Templates

### Template de SOP para Base de Conhecimento

```markdown
# SOP: Processo de Onboarding de Novo Colaborador (v.2.1)

**Data de Publicação:** 2023-10-26
**Última Revisão:** 2024-03-15
**Responsável:** Equipe de Recursos Humanos
**Categoria:** RH > Admissão

## 1. Propósito

Este Procedimento Operacional Padrão (SOP) descreve os passos para garantir um processo de onboarding eficiente e padronizado para todos os novos colaboradores da empresa, desde a aceitação da proposta até os primeiros 30 dias de trabalho, visando a integração e produtividade acelerada.

## 2. Escopo

Aplica-se a todos os novos colaboradores (CLT, PJ, Estagiários) e aos departamentos de RH, TI, Departamento Pessoal e Gestores diretos.

## 3. Pré-requisitos

*   Vaga aprovada e proposta aceita pelo candidato.
*   Documentação completa do novo colaborador entregue ao DP.
*   Acesso ao sistema de gestão de RH (ex: HCM Senior).
*   Licenças de software e equipamentos de TI solicitados com 7 dias de antecedência.

## 4. Passos Detalhados

### Fase 1: Antes do Primeiro Dia (D-7 a D-1)

1.  **RH:** Envio do kit de boas-vindas digital com cronograma de onboarding e informações essenciais da empresa (Manual do Colaborador, Código de Conduta).
    *   *Ferramenta:* E-mail padrão de boas-vindas do sistema de RH.
2.  **TI:** Configuração da estação de trabalho (notebook, monitor, teclado, mouse), criação de contas de e-mail e acesso aos sistemas internos (Slack, Google Workspace, CRM, ERP).
    *   *Verificar:* Testar todos os acessos antes do primeiro dia.
3.  **Gestor:** Envio de mensagem de boas-vindas personalizada e agendamento da primeira reunião 1:1 para o dia de início.
    *   *Exemplo:* "Bem-vindo(a) à equipe [Nome do time]! Estou animado(a) para tê-lo(a) conosco. Nossa primeira conversa será às 09:30 no dia [Data]."

### Fase 2: Primeiro Dia (D1)

1.  **RH:** Boas-vindas presencial/online, apresentação do plano de onboarding e tour virtual/físico pelas instalações. Entrega do crachá.
    *   *Duração:* 2 horas.
2.  **TI:** Colaborador valida acesso a todos os sistemas com o suporte de TI.
    *   *Ação:* Seguir o checklist de validação de acessos.
3.  **Gestor:** Reunião 1:1, apresentação à equipe, alinhamento de expectativas e primeiras tarefas.
    *   *Documento:* Plano de 30/60/90 dias para o novo colaborador.

### Fase 3: Primeira Semana (D2 a D7)

1.  **RH:** Apresentação detalhada dos benefícios e políticas da empresa. Agendamento do Treinamento de Cultura e Valores.
    *   *Ferramenta:* Plataforma de e-learning interna.
2.  **Gestor:** Acompanhamento diário, feedback inicial e introdução aos projetos e stakeholders-chave.

## 5. Resultados Esperados

*   Colaborador integrado à equipe em até 30 dias.
*   Acesso a sistemas e ferramentas funcionando em até 24h.
*   Redução de 20% no tempo de ramp-up do novo colaborador.

## 6. FAQ

*   **P: Onde solicito o equipamento de TI para um novo colaborador?**
    *   **R:** Abra um chamado no portal de TI com 7 dias úteis de antecedência, selecionando a categoria "Requisição de Equipamento".
*   **P: Qual o prazo para o RH enviar o kit de boas-vindas?**
    *   **R:** O kit digital é enviado no mínimo 3 dias antes do início do colaborador.

## 7. Anexos

*   [Link para] Checklist de Validação de Acessos TI
*   [Link para] Modelo de Plano de 30/60/90 Dias
*   [Link para] Manual do Colaborador
```

### Template de Artigo de Solução de Problemas

```markdown
# Artigo: Como Resolver o Erro "Acesso Negado" ao Acessar o Drive Compartilhado (v.1.2)

**Data de Publicação:** 2023-11-01
**Última Revisão:** 2024-02-20
**Responsável:** Equipe de TI
**Categoria:** TI > Suporte > Drives de Rede

## 1. Problema

Usuários recebem a mensagem de erro "Acesso Negado" ou "Você não tem permissão para acessar este recurso" ao tentar abrir pastas ou arquivos em drives compartilhados (ex: `\\servidor\compartilhamento_financeiro`).

## 2. Causas Comuns

*   Permissões de rede incorretas ou ausentes.
*   Credenciais de login desatualizadas.
*   Mapeamento de drive incorreto ou desconectado.
*   Problemas temporários de conexão com a rede.

## 3. Solução

Siga os passos abaixo em ordem para tentar resolver o problema:

### Passo 1: Verificar Conexão de Rede

1.  Certifique-se de que seu computador está conectado à rede interna (cabo ou Wi-Fi corporativo) ou à VPN, se estiver trabalhando remotamente.
2.  Tente acessar outros recursos de rede (ex: intranet, outro drive compartilhado menos restrito) para verificar a conectividade geral.

### Passo 2: Reiniciar o Computador

1.  Um simples reinício pode resolver problemas temporários de autenticação ou conectividade.
2.  Salve todo o seu trabalho e reinicie o computador.

### Passo 3: Mapear o Drive Novamente (Se Aplicável)

1.  Abra o "Explorador de Arquivos" (atalho: `Windows + E`).
2.  Clique com o botão direito em "Este Computador" ou "Rede" e selecione "Mapear unidade de rede...".
3.  Verifique se o caminho da pasta está correto (ex: `\\servidor\nome_do_compartilhamento`).
4.  Certifique-se de que a opção "Conectar usando credenciais diferentes" *NÃO* está marcada, a menos que você esteja usando credenciais específicas para aquele drive.
5.  Clique em "Concluir". Se solicitar credenciais, use seu login e senha da rede.

### Passo 4: Limpar Credenciais Antigas

1.  Pressione `Windows + R`, digite `control keymgr.dll` e pressione Enter.
2.  Na janela "Gerenciador de Credenciais", clique em "Credenciais do Windows".
3.  Procure por credenciais relacionadas ao servidor ou drive de rede que está dando problema (ex: `servidor.dominio.local`).
4.  Clique na credencial e selecione "Remover".
5.  Reinicie o computador e tente acessar o drive novamente. O sistema solicitará novas credenciais se necessário.

### Passo 5: Verificar Permissões (Apenas para Administradores de TI)

1.  Acesse o servidor de arquivos via RDP ou console.
2.  Navegue até a pasta compartilhada.
3.  Clique com o botão direito na pasta, selecione "Propriedades" > "Compartilhamento" > "Permissões Avançadas" e "Segurança".
4.  Verifique se o usuário ou grupo do qual o usuário faz parte possui as permissões NTFS e de compartilhamento adequadas (ex: `Leitura`, `Gravação`).

## 4. Próximos Passos

Se nenhum dos passos acima resolver o problema, abra um chamado no portal de TI informando:
*   Seu nome de usuário.
*   O caminho exato do drive ou pasta que você está tentando acessar.
*   Os passos que você já tentou e os resultados.
*   Qualquer mensagem de erro exata que aparece.
```

---

## Checklist

- [x] Taxonomia inicial definida (mínimo 3 categorias e 2 subcategorias por categoria).
- [x] Template padrão de artigo/SOP aprovado e disponível para uso.
- [x] Ferramenta de KB selecionada, configurada e com permissões de acesso gerenciadas.
- [x] Processo de criação de conteúdo (rascunho, revisão, aprovação) documentado e comunicado.
- [x] Mecanismo de feedback para usuários da KB implementado (ex: botões de "útil/não útil", comentários).
- [x] Plano de comunicação interna para lançamento e promoções da KB desenvolvido e agendado.
- [x] Responsáveis pela manutenção e atualização de conteúdo (donos de conteúdo) designados para as categorias principais.
- [x] Política de arquivamento ou desativação de conteúdo obsoleto criada.
- [x] Métricas de desempenho da KB (ex: uso, relevância, termos de busca) definidas e com monitoramento configurado.
- [x] Cronograma de revisão periódica de conteúdo estabelecido e comunicado aos donos de conteúdo.

---

## Métricas de Referência

| Métrica                         | Benchmark (Indústria) | Meta (Empresa) |
|---------------------------------|-----------------------|----------------|
| **Taxa de Sucesso de Busca**    | 80%                   | 90%            |
| **Taxa de Artigos Úteis**       | 75%                   | 85%            |
| **Tempo Médio para Encontrar Info** | 5 minutos             | 2 minutos      |
| **Número de Artigos Atualizados/Mês** | 10                    | 15             |
| **Redução de Chamados de Suporte** | 15%                   | 25%            |
| **Taxa de Colaboradores Ativos na KB** | 60%                   | 80%            |

---

## Erros Comuns

1.  **Conteúdo Desatualizado e Irrelevante**: Manter artigos com informações antigas ou processos que não existem mais. Isso erode a confiança na KB.
    *   **Como evitar**: Implementar um sistema de "donos de conteúdo" que são responsáveis pela revisão periódica (ex: trimestral) de seus artigos. Ex: Um SOP de "Configuração de Software X v1.0" não foi atualizado após a migração para a v2.0, gerando confusão. A solução é ter um alerta automático para o dono do conteúdo revisar o SOP a cada 90 dias.
2.  **Estrutura de Navegação Confusa**: Categorização ilógica, falta de tags ou uma hierarquia profunda demais, dificultando que os usuários encontrem o que precisam.
    *   **Como evitar**: Definir uma taxonomia clara e consistente antes de criar o conteúdo. Realizar testes de usabilidade com usuários reais e usar mapas de calor para entender seus padrões de navegação. Ex: Informações sobre RH espalhadas em "Administrativo", "Pessoas" e "Benefícios" sem uma lógica clara; evitar com uma taxonomia unificada e um glossário de termos.
3.  **Falta de Engajamento e Promoção**: A KB é criada, mas os colaboradores não sabem que existe ou não são incentivados a usá-la, continuando a usar canais tradicionais de suporte.
    *   **Como evitar**: Lançar a KB com uma campanha de comunicação interna robusta (e-mails, workshops, vídeos). Integrar a KB com ferramentas de comunicação (ex: um bot no Slack que pesquisa na KB). Ex: Usuários continuam abrindo chamados de TI para perguntas básicas porque não sabem que a KB existe; evitar com workshops de introdução e botões de feedback explícitos.

---

## Dicas Avançadas

1.  **Implementar um Sistema de Gamificação de Conteúdo**: Incentive a criação e atualização de conteúdo recompensando os colaboradores. Ex: Crie um "Ranking de Especialistas" que destaque os colaboradores que mais contribuem com artigos úteis, ou ofereça pontos/crachás virtuais para revisões e sugestões. Isso fomenta a colaboração e a qualidade.
2.  **Integrar a KB com Chatbots Internos**: Desenvolva ou configure um chatbot (ex: no Slack, Teams) que possa pesquisar diretamente na KB para responder a perguntas frequentes. Ex: Um colaborador pergunta "Como solicito reembolso?" no Slack e o bot responde com o link direto para o SOP de reembolso na KB, reduzindo a carga de trabalho do suporte.
3.  **Utilizar Análise de Sentimento em Feedbacks**: Além de apenas "útil/não útil", use ferramentas de PNL para analisar comentários e feedbacks dos usuários. Isso pode revelar frustrações ou pontos de dor específicos que precisam de atenção, permitindo otimizações mais precisas. Ex: Comentários como "linguagem muito técnica" ou "faltam exemplos práticos" são identificados, direcionando revisões de estilo.
4.  **Criar um "Glossário de Termos Corporativos" Dedicado**: Além das categorias de SOPs, tenha uma seção fundamental para definir siglas, jargões e termos internos específicos da empresa. Isso é crucial para o onboarding de novos colaboradores e para garantir que todos falem a mesma "língua". Ex: Um novo colaborador pode não saber o que significa "OKR", "CAC" ou "SLA"; o glossário oferece definições rápidas e padronizadas.
5.  **Realizar Auditorias de Conteúdo Semestrais Focadas em Lacunas e Redundâncias**: Vá além da simples revisão. Uma auditoria profunda identifica onde o conteúdo está faltando (lacunas), onde há informações duplicadas ou conflitantes (redundâncias) e onde o conteúdo não está alinhado com os objetivos estratégicos da empresa. Ex: A auditoria revela 3 artigos diferentes sobre o mesmo tópico de "política de viagens", cada um com informações ligeiramente diferentes; a ação é consolidá-los em um único artigo mestre.