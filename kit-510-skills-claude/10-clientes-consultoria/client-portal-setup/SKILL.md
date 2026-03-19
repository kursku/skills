---
name: client-portal-setup
description: "Client Portal Setup — Skill especializada para client portal setup"
license: MIT
metadata:
  version: 1.0.0
  author: Cafe Code AI
  category: 10-clientes-consultoria
  updated: 2026-03-01
---

# Client Portal Setup

Capacita o Claude a configurar e otimizar portais de clientes, focando em eficiência, comunicação e engajamento para empresas de consultoria.

---

## Keywords

cliente, portal, consultoria, onboarding, relatórios, comunicação, acesso, segurança, automação, engajamento, retenção, health score

---

## Quick Start

1.  **Listar funcionalidades essenciais**: Priorize recursos como acesso a relatórios mensais de performance, biblioteca de documentos (contratos, propostas), e um canal de comunicação direto.
2.  **Selecionar plataforma**: Avalie e escolha uma solução SaaS (ex: Clinked, Huddle, Accelo) ou um desenvolvimento customizado, considerando custo, escalabilidade e requisitos de segurança.
3.  **Configurar estrutura e permissões**: Crie uma hierarquia de pastas lógica (ex: "Projetos Ativos", "Financeiro", "Comunicações") e defina permissões de acesso por cliente e usuário.
4.  **Criar template de convite**: Desenvolva um e-mail padrão para convidar clientes ao portal, explicando os benefícios e fornecendo instruções claras de acesso.
5.  **Realizar teste piloto**: Convide um cliente interno ou um "beta user" para testar todas as funcionalidades, coletar feedback e refinar a experiência antes do lançamento geral.

---

## Core Workflows

### Workflow 1: Planejamento e Seleção da Plataforma de Portal de Clientes

Este workflow detalha o processo de identificação das necessidades e a escolha da tecnologia adequada para o portal do cliente.

1.  **Determinar requisitos funcionais e não-funcionais específicos**:
    *   **Funcionais**: Acesso seguro a relatórios de progresso (ex: Power BI dashboards), upload e download de documentos (contratos, minutas de reunião), chat em tempo real com o gerente de conta, agendamento de reuniões, biblioteca de FAQs, sistema de tickets de suporte.
    *   **Não-funcionais**: Conformidade com LGPD/GDPR, autenticação de dois fatores (2FA), capacidade para 500+ usuários, integração via API com CRM (Salesforce) e ferramenta de BI (Tableau), tempo de atividade de 99,9%, responsividade mobile.
    *   **Exemplo**: Para uma consultoria financeira, a capacidade de clientes acessarem extratos e relatórios de investimento personalizados, com criptografia de ponta a ponta, é crucial.

2.  **Avaliar opções de plataformas SaaS vs. desenvolvimento customizado**:
    *   **Plataformas SaaS (Clinked, Huddle, Accelo, Monday.com com Workspaces)**: Analisar funcionalidades pré-prontas, modelos de precificação (por usuário, por volume de dados), facilidade de implementação, suporte técnico e roadmap de recursos futuros.
    *   **Desenvolvimento Customizado**: Considerar o custo inicial e de manutenção, tempo de desenvolvimento, flexibilidade para funcionalidades muito específicas, e a necessidade de equipe interna de desenvolvimento.
    *   **Exemplo**: Uma consultoria de TI com requisitos de integração complexos pode preferir um desenvolvimento customizado, enquanto uma consultoria de marketing pode se beneficiar da agilidade de um SaaS como Clinked.

3.  **Validar a experiência do usuário (UX) em demonstrações e testes**:
    *   Agendar demonstrações com fornecedores selecionados, focando na facilidade de navegação para um cliente sem conhecimento técnico.
    *   Pedir acesso a ambientes de teste ou "sandboxes" para simular o uso por diferentes perfis de clientes (ex: executivo, analista).
    *   **Exemplo**: Durante a demo do Huddle, verificar se um cliente pode facilmente encontrar o último relatório de campanha sem precisar de ajuda, e se o upload de um arquivo é intuitivo.

4.  **Selecionar a plataforma e negociar termos contratuais**:
    *   Com base na avaliação, escolher a plataforma que melhor atende aos requisitos e ao orçamento.
    *   Negociar preços por volume, suporte prioritário, SLAs (Service Level Agreements) para tempo de atividade e resposta a incidentes, e cláusulas de privacidade de dados.
    *   **Exemplo**: Ao fechar com Clinked, garantir que o plano "Premier" inclua o número de usuários ativos esperados e que a cláusula de proteção de dados esteja alinhada com as políticas internas da consultoria.

### Workflow 2: Configuração, Onboarding e Manutenção Contínua do Portal

Este workflow abrange a implementação prática do portal e a gestão da experiência do cliente.

1.  **Estruturar o ambiente do portal com base em projetos e equipes de clientes**:
    *   Criar áreas de trabalho dedicadas para cada cliente ou projeto ativo.
    *   Definir uma estrutura de pastas padrão para consistência (ex: `/ClienteX/Proposta`, `/ClienteX/Contrato`, `/ClienteX/Relatorios/2024-01-Mensal`).
    *   **Exemplo**: Para um cliente com múltiplos projetos, criar uma seção "Projetos Ativos" e dentro dela subseções "Projeto Alpha - Status", "Projeto Beta - Documentação".

2.  **Configurar permissões de acesso granulares para clientes e equipes internas**:
    *   Garantir que cada cliente veja apenas seus próprios dados e projetos.
    *   Permitir que usuários da equipe do cliente (ex: CEO vs. Gerente de Projeto) tenham diferentes níveis de acesso (leitura, edição, upload).
    *   Definir papéis para a equipe interna (ex: Gerente de Conta tem acesso total ao cliente, Consultor Júnior tem acesso apenas ao seu projeto).
    *   **Exemplo**: O CEO do Cliente Y pode visualizar todos os relatórios financeiros, mas apenas a Gerente de Projetos do Cliente Y pode fazer upload de feedback sobre entregas.

3.  **Desenvolver e implementar um processo de onboarding estruturado para novos clientes no portal**:
    *   Enviar o "Convite de Acesso ao Portal do Cliente" (ver Template abaixo) no momento certo do onboarding do cliente.
    *   Incluir um "Guia Rápido de Uso do Portal" (ver Template abaixo) e, opcionalmente, um vídeo tutorial de 2-3 minutos que demonstre as principais funcionalidades.
    *   Agendar uma breve sessão de "tour guiado" ao vivo, se o cliente preferir.
    *   **Exemplo**: Após a assinatura do contrato, o gerente de conta envia o e-mail de convite com um link para o vídeo de onboarding e um convite para uma sessão de 15 minutos para tirar dúvidas.

4.  **Integrar o portal com sistemas internos existentes da consultoria**:
    *   Conectar o portal ao CRM para sincronização de dados de contato e histórico de interações.
    *   Integrar com ferramentas de Business Intelligence (BI) para exibir relatórios dinâmicos.
    *   Sincronizar com ferramentas de gestão de projetos (Jira, Asana) para updates de status.
    *   **Exemplo**: Usar a API do portal para puxar automaticamente os dados de "horas faturáveis" do sistema de gestão de projetos e exibi-los em um dashboard de faturamento no portal.

5.  **Monitorar a utilização do portal, coletar feedback e realizar melhorias contínuas**:
    *   Acompanhar métricas como taxa de adoção, frequência de login, documentos mais acessados, e tempo médio de resposta a tickets.
    *   Realizar pesquisas de satisfação (NPS) trimestralmente sobre a experiência do portal.
    *   Implementar um ciclo de feedback onde as sugestões dos clientes são revisadas e priorizadas para futuras atualizações do portal.
    *   **Exemplo**: Se a métrica de "downloads de relatórios financeiros" for baixa, investigar se o acesso é complicado ou se o conteúdo não é claro, e ajustar o layout ou o processo de geração.

---

## Templates

### Convite de Acesso ao Portal do Cliente

```
Assunto: Bem-vindo(a) ao Portal do Cliente [Nome da Consultoria] - Seu Acesso Exclusivo!

Prezado(a) [Nome do Cliente],

É com grande satisfação que convidamos você para acessar o Portal do Cliente [Nome da Consultoria], seu novo ponto central para todas as informações e colaborações relacionadas aos nossos projetos.

Desenvolvido para otimizar nossa comunicação e oferecer transparência, o portal permite que você:
*   Acesse relatórios de progresso e dashboards de performance em tempo real.
*   Visualize e faça download de documentos importantes (propostas, contratos, atas de reunião).
*   Comunique-se diretamente com sua equipe de consultoria através de um canal seguro.
*   Gerencie agendamentos e acompanhe o status das suas solicitações.

Para começar, por favor, clique no link abaixo para ativar sua conta e definir sua senha:
[Link de Acesso Único para Ativação da Conta: https://portal.consultoria.com/ativar/XYZ123ABC]

Seu nome de usuário inicial é: [email@cliente.com.br]

Recomendamos que você assista ao nosso breve vídeo de boas-vindas e consulte o "Guia Rápido de Uso do Portal" que está disponível na seção "Primeiros Passos" após o login.

Estamos confiantes de que o Portal do Cliente [Nome da Consultoria] aprimorará significativamente nossa parceria. Em caso de dúvidas, não hesite em contatar [Nome do Gerente de Conta] pelo e-mail [email_gerente@consultoria.com].

Atenciosamente,

Equipe [Nome da Consultoria]
[Telefone da Consultoria]
[Website da Consultoria]
```

### Guia Rápido de Uso do Portal

```
# Guia Rápido de Uso do Portal do Cliente [Nome da Consultoria]

Bem-vindo(a) ao seu espaço exclusivo! Este guia ajudará você a navegar e utilizar as principais funcionalidades do nosso portal.

## 1. Primeiro Acesso e Login

*   **Ativação**: Clique no link de ativação recebido por e-mail ([Link de Exemplo: https://portal.consultoria.com/ativar/XYZ123ABC]).
*   **Definir Senha**: Crie uma