---
name: quality-assurance-checklist
description: "Quality Assurance Checklist — Skill especializada para quality assurance checklist"
license: MIT
metadata:
  version: 1.0.0
  author: Cafe Code AI
  category: 11-operacoes-sistemas
  updated: 2026-03-01
---

# Quality Assurance Checklist

Esta skill capacita o Claude a criar, aplicar e otimizar checklists de garantia de qualidade, garantindo conformidade, mitigação de riscos e padronização em operações e projetos.

---

## Keywords

Checklist de QA, Garantia de Qualidade, Controle de Qualidade, Testes de Software, Conformidade Regulatória, Auditoria de Processos, Verificação de Lançamento, Validação Operacional, Mitigação de Riscos, Padronização SOPs, Gerenciamento de Defeitos, Teste de Aceitação.

---

## Quick Start

1.  **Selecione o domínio**: Determine se o checklist será para software (Ex: lançamento de feature), processo (Ex: onboarding de cliente), ou hardware (Ex: inspeção de linha de produção).
2.  **Identifique os pontos críticos**: Liste as funcionalidades, etapas ou componentes essenciais que demandam validação rigorosa para o domínio escolhido.
3.  **Preencha um template existente**: Utilize o `Template de Checklist de Lançamento de Software` ou `Template de Registro de Não Conformidade` como base, adaptando itens e critérios.
4.  **Execute a validação**: Aplique o checklist item a item, documentando `PASS`, `FAIL` ou `N/A` para cada critério.
5.  **Analise não conformidades**: Registre e priorize qualquer falha encontrada utilizando o template de Não Conformidade para acompanhamento e resolução.

---

## Core Workflows

### Workflow 1: Criação e Aplicação de Checklist para Lançamento de Software

Este workflow detalha a construção e execução de um checklist para garantir a qualidade de uma nova funcionalidade ou sistema antes do deploy em produção.

1.  **Definição do Escopo da Validação (Pré-lançamento)**:
    *   **Exemplo**: Lançamento da funcionalidade "Pagamento Recorrente" no sistema de e-commerce.
    *   **Ação**: Identificar módulos impactados (frontend, backend, banco de dados, integração com gateway de pagamento, notificação por email).
    *   **Critério de Sucesso**: Todos os módulos relevantes são listados e seus pontos de integração são mapeados.
2.  **Elaboração dos Critérios de Teste (Design)**:
    *   **Exemplo**: Para "Pagamento Recorrente".
    *   **Ação**: Criar itens específicos:
        *   `[ ] Fluxo de assinatura inicial via cartão de crédito (frontend)`
        *   `[ ] Processamento do primeiro pagamento (backend/gateway)`
        *   `[ ] Geração de fatura para recorrência (backend/banco de dados)`
        *   `[ ] Notificação de cobrança bem-sucedida (email service)`
        *   `[ ] Notificação de falha de cobrança e retentativa (email service/backend)`
        *   `[ ] Cancelamento da assinatura pelo usuário (frontend/backend)`
        *   `[ ] Reativação da assinatura (frontend/backend)`
        *   `[ ] Validação de dados de cartão (integração PCI DSS)`
        *   `[ ] Teste de carga com 500 transações simultâneas (performance)`
    *   **Critério de Sucesso**: Itens são atomizados, mensuráveis e cobrem casos de uso primários e secundários, incluindo cenários de erro.
3.  **Execução do Checklist (Testes)**:
    *   **Exemplo**: Um QA Lead executa o checklist contra o ambiente de staging.
    *   **Ação**: Para cada item, registrar o status (`PASS`, `FAIL`, `N/A`) e adicionar observações detalhadas.
        *   `[X] Fluxo de assinatura inicial via cartão de crédito (frontend) - PASS. Testado com Visa e Mastercard.`
        *   `[ ] Processamento do primeiro pagamento (backend/gateway) - FAIL. Erro 500 ao processar pagamento com cartão virtual. Defeito #APP-456 registrado.`
    *   **Critério de Sucesso**: Todos os itens aplicáveis são testados e resultados documentados, com referências a defeitos abertos para falhas.
4.  **Revisão e Aprovação (Sign-off)**:
    *   **Exemplo**: Após correções, o QA Lead e Product Owner revisam o checklist atualizado.
    *   **Ação**: Confirmar que todos os itens `FAIL` foram corrigidos e retestados com sucesso, ou que os riscos de `FAIL` remanescentes são aceitáveis.
    *   **Critério de Sucesso**: Todos os itens críticos para o lançamento estão `PASS` ou `N/A` com justificativa, e as partes interessadas aprovam o deploy.

### Workflow 2: Auditoria de Processo com Checklist de Conformidade

Este workflow descreve o uso de um checklist para auditar a adesão de uma equipe ou processo a um Procedimento Operacional Padrão (POP) ou regulamentação específica.

1.  **Seleção do POP/Regulamentação e Escopo da Auditoria**:
    *   **Exemplo**: Auditoria do processo de "Onboarding de Novos Clientes" para conformidade com o POP `POP-CLI-001` e LGPD.
    *   **Ação**: Obter o `POP-CLI-001` e a lista de requisitos da LGPD aplicáveis ao onboarding.
    *   **Critério de Sucesso**: Documentos de referência estão disponíveis e o escopo (Ex: 10 últimos onboards) está definido.
2.  **Criação do Checklist de Auditoria**:
    *   **Exemplo**: Para `POP-CLI-001` e LGPD no onboarding.
    *   **Ação**: Transformar cada etapa do POP e cada requisito LGPD em um item verificável.
        *   `[ ] Termo de Consentimento LGPD assinado e arquivado digitalmente? (POP-CLI-001, Seção 3.1.2)`
        *   `[ ] Coleta de dados mínimos essenciais ao serviço? (LGPD, Art. 6º, Inc. I - Finalidade)`
        *   `[ ] Orientação sobre Política de Privacidade fornecida? (POP-CLI-001, Seção 3.1.3)`
        *   `[ ] Documentos de identificação verificados e validados? (POP-CLI-001, Seção 3.2.1)`
        *   `[ ] Confirmação de cadastro enviada ao cliente em até 24h? (POP-CLI-001, Seção 3.3.1)`
    *   **Critério de Sucesso**: Checklist cobre todas as etapas críticas do POP e os requisitos regulatórios, com referências cruzadas.
3.  **Execução da Auditoria e Coleta de Evidências**:
    *   **Exemplo**: Um auditor revisa 5 registros de onboarding de clientes aleatórios do último mês.
    *   **Ação**: Para cada registro de cliente, marcar o status e registrar evidências (capturas de tela, IDs de documentos, logs).
        *   `[X] Termo de Consentimento LGPD assinado e arquivado digitalmente? - PASS. Evidência: Anexo 'TERMO_CLI_20230815.pdf' no CRM, ID 12345.`
        *   `[ ] Coleta de dados mínimos essenciais ao serviço? - FAIL. Evidência: Campo 'Estado Civil dos Pais' coletado, não previsto pelo POP nem essencial. Não Conformidade #AUDIT-001.`
    *   **Critério de Sucesso**: Todos os itens do checklist são verificados para cada amostra, com evidências documentadas para `PASS` e `FAIL`.
4.  **Relatório de Não Conformidades e Plano de Ação**:
    *   **Exemplo**: Consolidação dos resultados da auditoria.
    *   **Ação**: Gerar um relatório detalhado com todas as não conformidades, suas evidências, o impacto potencial e recomendações de ações corretivas.
        *   **Não Conformidade #AUDIT-001**: Coleta de dados excessiva ('Estado Civil dos Pais'). **Impacto**: Risco de multa LGPD. **Ação Proposta**: Remover campo do formulário de onboarding, treinar equipe de vendas.
    *   **Critério de Sucesso**: Relatório claro, objetivo e acionável, com responsabilidades e prazos para as ações corretivas.

---

## Templates

### Template de Checklist de Lançamento de Software

```
# Checklist de Lançamento de Software - [Nome do Projeto/Feature] - [Versão]

**Data de Geração:** 2024-03-10
**Responsável:** [Nome do QA Lead]
**Ambiente:** Staging/Produção
**Status Final:** [Aprovado para Lançamento / Bloqueado]

---

## Fase 1: Pré-Lançamento (Ambiente de Staging)

### 1.1 Testes Funcionais
- [X] Todas as funcionalidades principais (CRUD) operacionais?
  - Observações: [Ex: Módulo de Pagamento Recorrente, Criação, Leitura, Atualização, Deleção de assinaturas testadas com sucesso.]
- [X] Casos de borda e cenários de erro tratados corretamente?
  - Observações: [Ex: Tentativa de pagamento com saldo insuficiente, cartão expirado. Mensagens de erro claras.]
- [X] Integrações com sistemas externos (APIs de pagamento, CRM) funcionando?
  - Observações: [Ex: Integração com Stripe e Hubspot validada. Dados sincronizados corretamente.]

### 1.2 Testes Não Funcionais
- [X] Performance (tempo de resposta, carga) dentro dos SLAs?
  - Observações: [Ex: Latência de 150ms para 100 usuários simultâneos, conforme SLA de 200ms.]
- [X] Segurança (OWASP Top 10) auditada e corrigida?
  - Observações: [Ex: Scans de segurança automatizados não encontraram vulnerabilidades críticas. Teste de injeção SQL negativo.]
- [X] Compatibilidade com navegadores (Chrome, Firefox, Edge) e dispositivos (Desktop, Mobile)?
  - Observações: [Ex: UI responsiva testada em Chrome 120, Firefox 123, Edge 121, iOS 17, Android 14.]

## Fase 2: Pós-Lançamento (Monitoramento Inicial em Produção)

### 2.1 Validação em Produção
- [ ] Funcionalidades críticas operacionais em produção?
  - Observações: [Ex: Primeiro pagamento recorrente processado com sucesso. Status: Aguardando verificação.]
- [ ] Logs de erro e alertas monitorados (zero erros críticos)?
  - Observações: [Ex: Dashboards de Grafana/Datadog acompanhados. Nenhum erro 5xx reportado nas primeiras 2 horas.]
- [ ] Métricas de negócio (conversão, uso) acompanhadas?
  - Observações: [Ex: Taxa de conversão do novo fluxo de assinatura monitorada. Primeiras 100 assinaturas com 95% de sucesso.]

---
**Aprovações:**
- QA Lead: [Assinatura Digital/Nome] - [Data]
- Product Owner: [Assinatura Digital/Nome] - [Data]
- DevOps/Engenharia: [Assinatura Digital/Nome] - [Data]
```

### Template de Registro de Não Conformidade

```
# Registro de Não Conformidade - [ID: NC-PROJ-XXXX]

**Data de Registro:** 2024-03-10
**Registrado Por:** [Nome do QA/Auditor]
**Sistema/Processo Afetado:** Sistema E-commerce - Módulo de Pagamento Recorrente
**Referência do Checklist:** Checklist de Lançamento de Software - v1.0, Item 1.1.2 (Cenários de Erro)
**Status:** [Aberto / Em Análise / Em Correção / Validado / Fechado]
**Prioridade:** [Crítica / Alta / Média / Baixa] - Ex: Crítica

---

## Descrição da Não Conformidade

**Título:** Falha ao processar pagamento com cartão virtual em cenário de retentativa.
**Detalhes:** Ao simular uma falha temporária no gateway de pagamento para um cartão virtual e acionar o mecanismo de retentativa, o sistema gerou um erro 500 em vez de uma mensagem de erro tratada ou nova tentativa. O log indica `NullPointerException` ao tentar acessar a propriedade 'card_token' na segunda tentativa.
**Passos para Reproduzir:**
1.  Acessar ambiente de Staging.
2.  Iniciar fluxo de assinatura com cartão virtual de teste.
3.  Simular falha no gateway de pagamento na primeira tentativa (status HTTP 503).
4.  Observar a retentativa automática do sistema.
5.  Verificar logs do backend para o erro 500 e `NullPointerException`.
**Evidências Anexadas:**
-   Screenshot_Erro500_CartaoVirtual.png
-   Backend_Log_NullPointerException.txt
-   Video_Reproducao_NC-PROJ-001.mp4

## Análise e Impacto

**Causa Raiz (Proposta):** O tratamento de erro no módulo de retentativa não valida a existência do 'card_token' se o gateway retornar um erro diferente do esperado na primeira tentativa, levando ao `NullPointerException`.
**Impacto Potencial:** Perda de receita devido a falhas em pagamentos recorrentes, frustração do cliente, degradação da experiência do usuário.
**Escopo:** Afeta todos os pagamentos recorrentes que dependem de retentativas em cenários de falha parcial do gateway.

## Ações Corretivas

**Responsável:** [Nome do Desenvolvedor/Equipe de Engenharia]
**Prazo:** 2024-03-15
**Ação Proposta:**
1.  Implementar validação de `card_token` antes de reprocessar o pagamento.
2.  Adicionar tratamento de exceção específico para `NullPointerException` neste fluxo.
3.  Criar teste unitário e de integração para o cenário de retentativa com cartão virtual.
4.  Realizar re-teste da funcionalidade em ambiente de Staging.

---
**Validação da Correção (Pelo QA):**
-   Data de Validação: [Data]
-   Status da Validação: [Aprovado / Rejeitado]
-   Observações: [Ex: Reteste executado com sucesso. Erro 500 não reproduzido. `NullPointerException` corrigido.]
```

---

## Checklist

- [X] **Escopo definido**: O objetivo e os limites da validação estão claramente estabelecidos (ex: "Validação de deploy da versão 3.2.1").
- [X] **Critérios objetivos**: Cada item do checklist possui um critério de sucesso mensurável e inequívoco (ex: "Tempo de carregamento da página inicial < 2 segundos").
- [X] **Responsáveis atribuídos**: Cada seção ou item crítico tem um responsável claro para execução e/ou aprovação.
- [X] **Evidências documentadas**: Há um processo para anexar e/ou referenciar evidências (logs, screenshots, IDs de casos de teste) para cada item.
- [X] **Revisão por pares**: O checklist foi revisado por pelo menos um colega ou stakeholder antes da execução inicial.
- [X] **Atualização periódica**: O checklist é revisado e atualizado a cada ciclo de desenvolvimento ou mudança de processo (mínimo trimestral).
- [X] **Tratamento de não conformidades**: Existe um processo claro para registrar, priorizar e acompanhar a resolução de itens `FAIL`.
- [X] **Treinamento da equipe**: A equipe que executa o checklist está treinada nos procedimentos e ferramentas associadas.
- [X] **Integração com ferramentas**: O uso do checklist está integrado com ferramentas de gerenciamento de projetos (Jira, Asana) ou CI/CD, se aplicável.
- [X] **Métricas de desempenho**: Os resultados do checklist contribuem para métricas de qualidade (ex: taxa de aprovação no primeiro passe).

---

## Métricas de Referência

| Métrica                      | Benchmark (Ideal) | Meta (Aceitável) |
|------------------------------|-------------------|------------------|
| **Taxa de Passagem (First Pass Rate)** | > 95%             | > 80%            |
| **Densidade de Defeitos (Defect Density)** | < 0.5 defeitos/KLOC | < 1.0 defeitos/KLOC |
| **Defeitos Escapados (Escaped Defects)** | < 0.1 defeitos/KLOC | < 0.2 defeitos/KLOC |
| **Tempo Médio para Detecção (MTTD)** | < 1 dia           | < 3 dias         |
| **Tempo Médio para Resolução (MTTR)** | < 4 horas (Crítico) | < 12 horas (Crítico) |
| **Cobertura de Teste (Test Coverage)** | > 85%             | > 70%            |

---

## Erros Comuns

1.  **Checklists Excessivamente Genéricos**: **Problema**: Itens como "Testar funcionalidade" são vagos e não fornecem direções claras. **Como evitar**: Quebrar cada item em sub-itens específicos e acionáveis, com critérios de sucesso explícitos. Ex: Em vez de "Testar login", use "Verificar login com credenciais válidas", "Verificar login com credenciais inválidas", "Testar recuperação de senha".
2.  **Não Atualizar Checklists Regularmente**: **Problema**: Checklists desatualizados não refletem as mudanças no produto ou processo, levando a lacunas na qualidade. **Como evitar**: Agendar revisões trimestrais para todos os checklists. Após cada grande lançamento ou alteração de POP, realizar uma revisão imediata e formal do checklist relacionado, adicionando ou removendo itens conforme necessário.
3.  **Foco Exclusivo em Aspectos Técnicos**: **Problema**: Ignorar a experiência do usuário ou requisitos de negócio pode resultar em um produto tecnicamente sólido, mas impopular ou ineficaz. **Como evitar**: Incluir itens específicos de usabilidade (Ex: "Navegação intuitiva em todos os fluxos críticos"), acessibilidade (Ex: "Conformidade com WCAG 2.1 AA para áreas públicas") e validação de requisitos de negócio (Ex: "Taxa de conversão do funil de compra mantida acima de X% após a mudança").

---

## Dicas Avançadas

1.  **Integração com Pipeline CI/CD**: Automatize a execução de partes do seu checklist que podem ser verificadas via testes automatizados (unitários, integração, E2E) dentro do pipeline de Integração Contínua/Entrega Contínua. **Exemplo**: Um item como "Todos os testes automatizados passaram" pode ser um gate no Jenkins/GitLab CI, bloqueando o deploy se falhar, e um item como "Código está formatado com Prettier" pode ser validado por um linter pré-commit.
2.  **Checklists Dinâmicos Baseados em Risco**: Em vez de um checklist estático, crie regras que geram itens de validação com base no nível de risco de uma alteração. **Exemplo**: Uma alteração em um módulo financeiro crítico pode disparar automaticamente um checklist de segurança e conformidade mais extenso, enquanto uma mudança de layout acionaria um checklist de UI/UX mais leve.
3.  **Gamificação da Execução de Checklists**: Incentive a adesão e a qualidade na execução de checklists através de elementos de gamificação. **Exemplo**: Atribua pontos por completar checklists, identificar não conformidades críticas ou contribuir com melhorias nos checklists existentes, com um leaderboard para visibilidade e reconhecimento da equipe.
4.  **Uso de IA para Sugestão de Itens**: Implemente modelos de IA (como o próprio Claude) para analisar descrições de novas funcionalidades ou POPs e sugerir automaticamente itens para o checklist, com base em padrões de checklists anteriores e melhores práticas do domínio. **Exemplo**: Ao descrever "Implementação de módulo de chat ao vivo", a IA sugere itens como "Verificar envio de mensagens em tempo real", "Testar notificações de nova mensagem", "Validar histórico de conversas".
5.  **Checklists de Pós-mortem (Post-Mortem Checklists)**: Após um incidente grave em produção, utilize um checklist específico para garantir que todas as etapas da análise de causa raiz, plano de ação e lições aprendidas sejam devidamente documentadas e implementadas. **Exemplo**: Itens como "Causa raiz identificada e documentada?", "Ações corretivas preventivas definidas?", "Conhecimento compartilhado com a equipe?", "Monitoramento para reincidência configurado?".