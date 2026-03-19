---
name: incident-response-plan
description: "Incident Response Plan — Skill especializada para incident response plan"
license: MIT
metadata:
  version: 1.0.0
  author: Cafe Code AI
  category: 11-operacoes-sistemas
  updated: 2026-03-01
---

# Incident Response Plan

Esta skill capacita o Claude a gerenciar e executar todas as fases de um plano de resposta a incidentes de segurança cibernética, desde a detecção até a lição aprendida.

---

## Keywords

Detecção de Incidente, Triage de Alertas, Contenção de Ameaças, Erradicação de Malware, Recuperação de Sistemas, Análise Forense Digital, Comunicação de Crise, Post-Mortem, Playbook de Resposta, SIEM, SOC, RTO, RPO, Vulnerabilidade, Threat Hunting.

---

## Quick Start

1.  **Monitoramento Ativo de Alertas**: Configure o SIEM (Security Information and Event Management) para disparar alertas críticos, como tentativas de login falhas excessivas no Active Directory ou tráfego de dados anômalo para IPs maliciosos conhecidos.
2.  **Triagem Inicial Rápida**: Avalie a severidade de um alerta (Ex: `CRÍTICO` para ransomware, `MÉDIO` para acesso não autorizado a recurso não sensível) e determine a equipe de resposta primária (Ex: Equipe de Segurança Nível 2).
3.  **Acionamento do Playbook Adequado**: Inicie o playbook específico para o tipo de incidente detectado (Ex: `PLAYBOOK-RANSOMWARE-V3.2` ou `PLAYBOOK-PHISHING-EMAIL-V1.0`).
4.  **Contenção Imediata**: Isole o sistema comprometido da rede corporativa ou da internet (Ex: desabilitar porta de switch, bloquear IP no firewall) para evitar a propagação.
5.  **Comunicação Essencial**: Notifique as partes interessadas internas (gestão de TI, jurídico, comunicação) conforme o plano de comunicação de incidentes pré-definido.

---

## Core Workflows

### Workflow 1: Detecção e Triage Inicial de Incidentes

Este workflow descreve os passos para identificar, verificar e classificar um potencial incidente de segurança, garantindo que a resposta seja iniciada de forma eficaz e rápida.

**Passos Detalhados:**

1.  **Coleta e Consolidação de Logs**:
    *   **Ação**: Garanta que logs de sistemas críticos (firewalls, IDS/IPS, servidores, endpoints, aplicações) estejam centralizados no SIEM (Ex: Splunk, Elastic SIEM).
    *   **Exemplo**: O SIEM recebe logs de `firewall-fw01` indicando `DENY` para `TCP/445` (SMB) de `10.10.1.50` para `192.168.1.100` em um volume 100x maior que o normal, e logs de `endpoint-pc123` mostrando execução de `powershell.exe -EncodedCommand ...`.
2.  **Análise de Alertas e Correlação**:
    *   **Ação**: O analista de SOC (Security Operations Center) revisa alertas gerados pelo SIEM ou por ferramentas de EDR (Endpoint Detection and Response) ou XDR.
    *   **Exemplo**: Um alerta do SIEM (`ID-SIEM-20240301-001`) é disparado: "Atividade de Ransomware Detectada em `SRV-FINANCEIRO-01`". O alerta correlaciona eventos de criptografia de arquivos em massa, renomeação de extensões `.locked`, e tentativas de comunicação com C2 (Command and Control) conhecidos.
3.  **Verificação e Validação do Incidente**:
    *   **Ação**: O analista investiga o alerta para confirmar se é um falso positivo ou um incidente real. Isso pode envolver acesso remoto ao sistema suspeito, análise de processos em execução, conexões de rede ativas e logs de sistema.
    *   **Exemplo**: O analista acessa `SRV-FINANCEIRO-01` via ferramenta de resposta remota (Ex: CrowdStrike Falcon, Carbon Black), verifica a pasta `C:\Financeiro\Relatorios` e encontra arquivos com a extensão `.locked_by_ransomware_group`, além de um arquivo `README_DECRYPT.txt`. O processo `evil.exe` está ativo e consumindo CPU. Confirmação: **Incidente real**.
4.  **Classificação e Priorização**:
    *   **Ação**: Classifique o incidente com base na sua gravidade (criticidade dos ativos afetados, impacto potencial), tipo (malware, acesso não autorizado, DDoS) e probabilidade de propagação.
    *   **Exemplo**:
        *   **Severidade**: `CRÍTICA` (Afeta servidor financeiro principal, dados sensíveis).
        *   **Tipo**: Ransomware.
        *   **Impacto**: `ALTO` (Interrupção de operações financeiras, perda de dados).
        *   **Prioridade**: `P1` (Resposta imediata, 24/7).
5.  **Documentação Inicial e Acionamento**:
    *   **Ação**: Registre o incidente no sistema de ticketing (Ex: Jira Service Management, ServiceNow) com todas as informações coletadas. Acione a equipe de resposta a incidentes (IRT) e o playbook correspondente.
    *   **Exemplo**: Um ticket (`INC-2024-03-01-001`) é criado com o título "Ransomware Ativo em SRV-FINANCEIRO-01". O `PLAYBOOK-RANSOMWARE-V3.2` é referenciado e a equipe de IRT é notificada via sistema de alerta (Ex: PagerDuty, Slack).

### Workflow 2: Contenção, Erradicação e Recuperação

Este workflow detalha as ações para limitar o impacto de um incidente, remover a ameaça e restaurar as operações de forma segura e eficiente.

**Passos Detalhados:**

1.  **Contenção Imediata**:
    *   **Ação**: Tome medidas rápidas para isolar o sistema comprometido e evitar a propagação da ameaça. Priorize a continuidade mínima de negócios quando possível, mas a segurança é primordial.
    *   **Exemplo**:
        *   **Isolamento de Rede**: Desconectar `SRV-FINANCEIRO-01` da rede corporativa (desabilitar porta do switch `SW-CORE-01` GE0/12, bloquear IP `192.168.1.100` no firewall `FW-PERIMETRO-01`).
        *   **Isolamento Lógico**: Suspender o acesso de usuários e serviços ao servidor (Ex: desabilitar conta de serviço `SVC_FINANCE` no AD).
        *   **Backup de Evidências**: Antes de qualquer mudança, crie uma imagem forense ou copie arquivos de log críticos do sistema comprometido para análise posterior. (Ex: `dd if=/dev/sda of=/mnt/forensics/srv-financeiro-01.img bs=4M conv=noerror,sync`).
2.  **Eradicação da Ameaça**:
    *   **Ação**: Remova completamente o malware, as portas de entrada (backdoors), e quaisquer artefatos do atacante dos sistemas afetados e de outros sistemas que possam ter sido comprometidos.
    *   **Exemplo**:
        *   **Remoção de Malware**: Utilizar ferramentas antivírus/EDR atualizadas para escanear e remover `evil.exe` e outros componentes do ransomware. Limpar arquivos de registro e tarefas agendadas criadas pelo atacante.
        *   **Remediação de Vulnerabilidades**: Identificar e corrigir a vulnerabilidade inicial que permitiu o ataque (Ex: aplicar patch `KB5034441` para vulnerabilidade de SMB no `SRV-FINANCEIRO-01`, reconfigurar permissões de compartilhamento de rede).
        *   **Troca de Credenciais**: Resetar todas as senhas de contas comprometidas e contas de serviço que tinham acesso ao servidor financeiro. Forçar redefinição de senhas para todos os usuários com acesso privilegiado.
3.  **Recuperação e Validação**:
    *   **Ação**: Restaure os sistemas e dados afetados de backups limpos, garantindo a integridade e a disponibilidade. Verifique que o sistema está seguro antes de reintegrá-lo à rede.
    *   **Exemplo**:
        *   **Restauração de Backup**: Restaurar `SRV-FINANCEIRO-01` a partir do último backup validado e limpo de `2024-02-29 23:00 BRT` (RTO de 4 horas para este sistema crítico).
        *   **Varredura Pós-Restauração**: Executar varreduras de segurança completas (antivírus, EDR, varredura de vulnerabilidades) no sistema restaurado para garantir que não há artefatos remanescentes do ataque.
        *   **Reintegração Controlada**: Reintegrar `SRV-FINANCEIRO-01` à rede de forma faseada, monitorando ativamente qualquer atividade suspeita por 24-48 horas após a reintegração.
        *   **Validação de Usuários**: Informar aos usuários afetados que podem acessar os sistemas e solicitar que verifiquem a integridade de seus dados essenciais.
4.  **Monitoramento Pós-Incidente**:
    *   **Ação**: Mantenha um monitoramento intensivo dos sistemas recuperados e de toda a rede para detectar qualquer sinal de atividade maliciosa persistente ou novos ataques.
    *   **Exemplo**: Configurar regras de SIEM adicionais para monitorar tentativas de acesso a `SRV-FINANCEIRO-01` de IPs externos, uso de contas de serviço, e alterações em pastas críticas do sistema por 7 dias após a recuperação.

---

## Templates

### Relatório de Incidente (Exemplo Preenchido)

```
RELATÓRIO DE INCIDENTE DE SEGURANÇA

Número do Incidente: INC-2024-03-01-001
Data e Hora da Detecção: 2024-03-01 10:15 BRT
Data e Hora do Início Estimado: 2024-03-01 09:30 BRT
Data e Hora da Resolução: 2024-03-01 17:45 BRT

Título do Incidente: Ataque de Ransomware em Servidor Financeiro Crítico

Status: Fechado - Lições Aprendidas Pendentes

Analista(s) Responsável(is): João Silva (Analista N2 SOC), Maria Souza (Eng. Segurança)
Equipes Envolvidas: Equipe de SOC, Equipe de Infraestrutura, Equipe de Redes, Departamento Financeiro, Jurídico.

1. Detalhes do Incidente:
   - Tipo de Incidente: Ransomware (Família: Conti/BlackCat - detectado por TTPs)
   - Ativos Afetados: SRV-FINANCEIRO-01 (IP: 192.168.1.100), Servidor de Arquivos (SMB)
   - Impacto Estimado: Indisponibilidade de sistemas financeiros por 8 horas, perda potencial de dados de 1 hora (entre o último backup e a detecção).
   - Dados Comprometidos: Arquivos da pasta C:\Financeiro\Relatorios (dados de clientes e transações).
   - Causa Raiz Potencial: Exploração de vulnerabilidade SMB (CVE-2021-44228) em porta exposta na DMZ (erro de configuração de firewall).

2. Linha do Tempo da Resposta:
   - 10:15 BRT: Alerta do SIEM "Atividade de Ransomware Detectada em SRV-FINANCEIRO-01" acionado.
   - 10:25 BRT: Analista João Silva inicia triagem, valida o incidente.
   - 10:40 BRT: Servidor SRV-FINANCEIRO-01 isolado da rede (porta SW-CORE-01 GE0/12 desabilitada).
   - 11:00 BRT: Equipe de IRT acionada, plano de comunicação iniciado.
   - 11:30 BRT: Imagem forense do disco C: de SRV-FINANCEIRO-01 iniciada.
   - 12:00 BRT: Confirmação de erradicação do malware por varredura de EDR.
   - 13:00 BRT: Início da restauração do backup limpo (2024-02-29 23:00 BRT).
   - 16:30 BRT: Restauração concluída, varredura de segurança pós-restauração.
   - 17:00 BRT: Reintegração gradual de SRV-FINANCEIRO-01 à rede.
   - 17:45 BRT: Verificação final de funcionalidade e segurança, incidente marcado como resolvido.

3. Medidas de Contenção, Erradicação e Recuperação:
   - Contenção: Desconexão física/lógica do servidor, bloqueio de IPs e domínios C2 no firewall.
   - Erradicação: Remoção do ransomware via EDR, aplicação de patch de segurança crítico (KB5034441).
   - Recuperação: Restauração completa do SRV-FINANCEIRO-01 a partir de backup validado.

4. Lições Aprendidas Iniciais:
   - Necessidade de revisão urgente das políticas de firewall na DMZ.
   - Aprimorar monitoramento de tráfego SMB para detectar anomalias mais cedo.
   - Testar rotineiramente a restauração de backups críticos para reduzir o RTO.
   - Treinamento adicional para equipe de infraestrutura sobre hardening de servidores.

5. Recomendações de Ações Corretivas:
   - Revisão completa e auditoria das regras de firewall da DMZ (Prazo: 7 dias).
   - Implementação de IPS/IDS com assinatura de SMB específicas (Prazo: 30 dias).
   - Execução de exercícios de recuperação de desastres para sistemas financeiros (Prazo: 60 dias).
   - Programa de hardening de servidores com foco em exposição de serviços (Prazo: 90 dias).
```

### Plano de Comunicação de Incidente (Exemplo Preenchido)

```
PLANO DE COMUNICAÇÃO DE INCIDENTE

Número do Incidente: INC-2024-03-01-001
Título do Incidente: Ataque de Ransomware em Servidor Financeiro Crítico

1. Equipe de Comunicação Primária:
   - Líder de Resposta a Incidentes: Maria Souza (maria.souza@empresa.com.br, ramal 1234)
   - Líder de TI/Infraestrutura: Carlos Santos (carlos.santos@empresa.com.br, ramal 5678)
   - Assessoria de Imprensa/Comunicação: Ana Lima (ana.lima@empresa.com.br, ramal 9012)
   - Jurídico/Compliance: Dr. Pedro Costa (pedro.costa@empresa.com.br, ramal 3456)
   - Alta Direção: CEO, CIO, CFO (contatos via Grupo de Alerta Crítico)

2. Canais de Comunicação:
   - Interno: Grupo de Chat "Alerta de Segurança Crítico" (Microsoft Teams), E-mail "Segurança Interna", PagerDuty.
   - Externo: Telefone, E-mail, Portal de Notícias da Empresa (se aplicável), Mídias Sociais (via Assessoria de Imprensa).

3. Modelos de Mensagens (Exemplos):

   a) **Comunicado Interno - Início do Incidente (Exclusivo para Equipes de Resposta)**
      ```
      Assunto: ALERTA DE INCIDENTE - SRV-FINANCEIRO-01 COMPROMETIDO

      Prezados,

      Detectamos um incidente de segurança CRÍTICO envolvendo o servidor SRV-FINANCEIRO-01. Ações de contenção estão em andamento.
      Detalhes iniciais: Atividade de ransomware detectada.
      Equipes acionadas: SOC, Infraestrutura, Redes.
      Aguardem novas atualizações. Não divulguem informações a não ser para pessoas com necessidade de saber.

      Atenciosamente,
      Equipe de Resposta a Incidentes
      ```

   b) **Comunicado Interno - Status para Liderança (Atualização)**
      ```
      Assunto: ATUALIZAÇÃO INCIDENTE INC-2024-03-01-001 - SRV-FINANCEIRO-01

      Prezados Líderes,

      O incidente de ransomware no SRV-FINANCEIRO-01 está sob controle. O servidor foi isolado e a erradicação do malware está em fase final.
      Estamos iniciando o processo de recuperação a partir de backup validado.
      Previsão de retorno do serviço financeiro: 17:00 BRT.
      Impacto estimado: Indisponibilidade de 8 horas. Investigação da causa raiz em andamento.

      Manteremos todos informados.

      Atenciosamente,
      Maria Souza - Líder de Resposta a Incidentes
      ```

   c) **Comunicado Interno - Usuários Afetados (Ex: Departamento Financeiro)**
      ```
      Assunto: IMPORTANTE: Indisponibilidade de Sistemas Financeiros

      Prezados,

      Informamos que os sistemas financeiros (acesso a SRV-FINANCEIRO-01) estão temporariamente indisponíveis devido a um problema técnico.
      Nossas equipes estão trabalhando intensamente para restaurar o serviço o mais rápido possível.
      Previsão de normalização: Hoje, até as 17:00 BRT.
      Pedimos desculpas pelo transtorno e agradecemos a compreensão.

      Atenciosamente,
      Departamento de TI
      ```

   d) **Comunicado Interno - Resolução do Incidente**
      ```
      Assunto: INCIDENTE RESOLVIDO: Sistemas Financeiros Normalizados

      Prezados,

      Informamos que o incidente que afetou os sistemas financeiros foi RESOLVIDO. O SRV-FINANCEIRO-01 está operacional e acessível.
      Todas as operações foram restauradas a partir do backup de 29/02/2024 23:00 BRT.
      Monitoramento intensivo será mantido nas próximas 24 horas.

      Agradecemos a colaboração e paciência de todos.

      Atenciosamente,
      Equipe de Resposta a Incidentes
      ```

4. Frequência de Comunicação:
   - Líder de Resposta a Incidentes para Equipes Internas: A cada 30-60 minutos ou quando houver atualização significativa.
   - Líder de Resposta a Incidentes para Alta Direção/Jurídico: A cada 2 horas ou conforme solicitado.
   - TI para Usuários Afetados: A cada 2-4 horas, ou quando houver uma previsão de tempo de restauração.

5. Pontos de Contato de Emergência:
   - João Silva (SOC) - Celular: +55 (11) 98765-4321
   - Maria Souza (Líder IRT) - Celular: +55 (11) 91234-5678
   - Plantão de Infraestrutura: 0800-123-4567

```

---

## Checklist

- [X] Log de todos os sistemas críticos centralizado em um SIEM.
- [X] Playbooks de resposta a incidentes atualizados e acessíveis.
- [X] Equipe de Resposta a Incidentes (IRT) com papéis e responsabilidades definidos.
- [X] Ferramentas de contenção (isolamento de rede, EDR) pré-configuradas e testadas.
- [X] Backups de dados críticos verificados e com plano de restauração testado.
- [X] Plano de comunicação de incidentes aprovado e contatos atualizados.
- [X] Ferramentas de análise forense (Ex: Volatility, Autopsy) prontas para uso.
- [X] Sistema de ticketing de incidentes configurado para rastreamento e documentação.
- [X] Treinamento regular da equipe de IRT com simulações de incidentes.
- [X] Monitoramento pós-incidente configurado para detecção de recorrências.

---

## Métricas de Referência

| Métrica               | Benchmark (Indústria) | Meta (Empresa XYZ) |
|-----------------------|-----------------------|--------------------|
| MTTR (Mean Time To Recover)     | < 4 horas             | < 2 horas          |
| MTTD (Mean Time To Detect)     | < 60 minutos          | < 30 minutos       |
| MTTA (Mean Time To Acknowledge) | < 30 minutos          | < 15 minutos       |
| RTO (Recovery Time Objective)   | < 8 horas             | < 4 horas          |
| RPO (Recovery Point Objective)  | < 4 horas             | < 1 hora           |
| Taxa de Falso Positivo        | < 10%                 | < 5%               |

---

## Erros Comuns

1.  **Falta de Isolamento Rápido**: Não isolar um sistema comprometido a tempo permite que a ameaça se propague, aumentando drasticamente o escopo e o custo do incidente.
    *   **Como evitar**: Defina políticas de isolamento automatizadas ou semi-automatizadas (Ex: EDR que isola endpoint ao detectar ransomware; script de firewall para bloquear IPs suspeitos) e treine a equipe para agir em menos de 15 minutos após a validação do incidente.
2.  **Restauração de Backup Contaminado**: Restaurar um sistema a partir de um backup que já estava comprometido ou que não foi validado como limpo, leva a uma reinfecção imediata.
    *   **Como evitar**: Implemente uma política de validação de backups (testes regulares de restauração em ambiente isolado, varredura antivírus no backup antes da restauração) e mantenha múltiplos pontos de recuperação em diferentes períodos.
3.  **Comunicação Ineficaz**: Falha em comunicar o status do incidente de forma clara e oportuna para as partes interessadas (liderança, jurídico, usuários) pode gerar pânico, desinformação e danos à reputação.
    *   **Como evitar**: Elabore um plano de comunicação detalhado com modelos de mensagens pré-aprovados e canais definidos para cada público. Realize simulados de incidentes incluindo o fluxo de comunicação para testar sua eficácia.

---

## Dicas Avançadas

1.  **Integração com Threat Intelligence Ativa**: Alimente seu SIEM e EDR com feeds de inteligência de ameaças (Ex: CISA, Mandiant, Recorded Future) em tempo real.
    *   **Exemplo Prático**: Se o feed de TI indicar novos IPs de Command and Control (C2) associados a uma campanha de ransomware, configure imediatamente regras no firewall para bloquear esses IPs e buscas proativas no SIEM para verificar se algum sistema interno tentou se comunicar com eles.
2.  **Automação da Resposta (SOAR)**: Utilize plataformas SOAR (Security Orchestration, Automation and Response) para automatizar tarefas repetitivas de contenção e coleta de evidências.
    *   **Exemplo Prático**: Ao detectar um alerta de phishing confirmado, um playbook SOAR pode automaticamente isolar o endpoint do usuário, bloquear o remetente e o URL malicioso no gateway de e-mail e firewall, e abrir um ticket para análise forense, tudo em segundos.
3.  **Exercícios de "Purple Teaming"**: Realize exercícios combinados de "Red Team" (simulando ataques) e "Blue Team" (respondendo aos ataques) para testar e aprimorar continuamente seu plano de resposta.
    *   **Exemplo Prático**: O Red Team tenta exfiltrar dados financeiros; o Blue Team (equipe de IR) deve detectar a atividade, conter a ameaça e analisar a cadeia de ataque. O Purple Team (facilitador) garante que as lições sejam aprendidas e os playbooks atualizados.
4.  **Integração de Análise Comportamental (UEBA)**: Adote soluções UEBA (User and Entity Behavior Analytics) para detectar anomalias no comportamento de usuários e entidades que podem indicar um comprometimento.
    *   **Exemplo Prático**: Um usuário administrativo que normalmente acessa servidores apenas durante o horário comercial e de um IP específico, passa a logar de um IP desconhecido às 3 da manhã e tenta acessar pastas financeiras. O UEBA detecta essa anomalia e gera um alerta de alta criticidade.
5.  **Criação de "Caça a Ameaças" (Threat Hunting)**: Não espere por alertas; ativamente procure por evidências de atividades maliciosas ocultas na sua rede.
    *   **Exemplo Prático**: Proativamente, um analista de segurança busca no SIEM por padrões de comunicação de rede incomuns (Ex: conexões SSH para IPs externos de servidores internos que não deveriam ter tais conexões), ou por processos executando com hashes conhecidos de malware em máquinas que não foram alertadas, usando IOCs (Indicators of Compromise) de relatórios recentes da indústria.

---