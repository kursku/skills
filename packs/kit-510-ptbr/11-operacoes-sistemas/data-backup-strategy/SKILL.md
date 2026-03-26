---
name: data-backup-strategy
description: "Data Backup Strategy — Skill especializada para data backup strategy"
license: MIT
metadata:
  version: 1.0.0
  author: Cafe Code AI
  category: 11-operacoes-sistemas
  updated: 2026-03-01
risk: offensive
---

# Data Backup Strategy

Esta skill capacita o Claude a projetar, implementar e gerenciar estratégias robustas de backup de dados, garantindo resiliência e recuperação de desastres para ambientes de TI corporativos.

---

## Keywords

Estratégia de Backup, Recuperação de Desastres, RTO, RPO, Regra 3-2-1, Backup Imutável, Retenção de Dados, Criptografia de Backup, Teste de Restauração, Backup em Nuvem, Backup On-Premise, Replicação de Dados.

---

## Quick Start

1.  **Mapeie Ativos Críticos e Seus RTO/RPO**: Liste os sistemas e bases de dados essenciais (ex: ERP, CRM, Banco de Dados de Produção) e defina seus Objetivos de Tempo de Recuperação (RTO) e Objetivos de Ponto de Recuperação (RPO) aceitáveis (ex: ERP RTO < 4h, RPO < 1h; Servidor de Arquivos RTO < 24h, RPO < 4h).
2.  **Selecione a Metodologia de Backup**: Adote a regra 3-2-1 como padrão: no mínimo 3 cópias de dados, em 2 mídias diferentes, com 1 cópia off-site (ex: backup para NAS local, replicação para cloud e fita LTO).
3.  **Configure o Software de Backup**: Implemente a solução de backup (ex: Veeam Backup & Replication para VMs, AWS Backup para recursos AWS, Azure Backup para VMs Azure) para os ativos críticos, agendando execuções com base nos RPOs definidos (ex: backups incrementais a cada 30 minutos para bancos de dados, backups diários completos para servidores de arquivos).
4.  **Estabeleça Políticas de Retenção**: Configure a política de retenção para cada tipo de dado/servidor, alinhada com requisitos regulatórios e de negócios (ex: 7 dias diários, 4 semanas semanais, 12 meses mensais, 7 anos anuais para dados financeiros).
5.  **Programe Testes de Restauração Regulares**: Agende testes de restauração de forma periódica (ex: mensal para sistemas críticos, trimestral para sistemas secundários), validando a integridade e o tempo de recuperação dos backups.

---

## Core Workflows

### Workflow 1: Implementação de Estratégia de Backup 3-2-1 para Ambientes Híbridos

Este workflow detalha a aplicação da regra 3-2-1 para servidores virtuais e bancos de dados em um ambiente que combina infraestrutura on-premise e serviços de nuvem.

1.  **Classificação de Dados e Sistemas**:
    *   **Ação**: Identificar todos os servidores (físicos e virtuais), aplicações e bancos de dados. Classificá-los por criticidade (Tier 0: missão crítica, Tier 1: alta criticidade, Tier 2: média) e volume de dados.
    *   **Exemplo**: O servidor SQL Server de produção (ERP) é Tier 0, com 500GB de dados. Servidor de arquivos do departamento de marketing é Tier 1, com 2TB. Servidor de desenvolvimento é Tier 2, com 100GB.
2.  **Definição de RTO/RPO por Tier**:
    *   **Ação**: Para cada tier, definir os RTO e RPO máximos aceitáveis.
    *   **Exemplo**:
        *   Tier 0 (SQL Server): RTO < 2 horas, RPO < 15 minutos.
        *   Tier 1 (Servidor de Arquivos): RTO < 8 horas, RPO < 4 horas.
        *   Tier 2 (Desenvolvimento): RTO < 24 horas, RPO < 24 horas.
3.  **Configuração da Primeira Cópia (Primária)**:
    *   **Ação**: Implementar backups diários completos e incrementais/diferenciais frequentes para um armazenamento de alta performance no local (on-premise).
    *   **Exemplo**:
        *   Para VMs on-premise (Tier 0, 1, 2): Usar Veeam Backup & Replication para realizar backups incrementais a cada 1 hora para um Storage NAS (Network Attached Storage) local de alta velocidade, com retenção de 7 dias.
        *   Para bancos de dados (Tier 0): Configurar backups de log de transações a cada 15 minutos diretamente no SQL Server, salvando em um disco de alta performance.
4.  **Configuração da Segunda Cópia (Mídia Diferente)**:
    *   **Ação**: Replicar ou copiar os backups primários para uma mídia diferente, preferencialmente em outro local físico dentro da mesma rede ou datacenter, para proteção contra falhas do armazenamento primário.
    *   **Exemplo**:
        *   Para Veeam: Criar um Backup Copy Job que move os backups diários completos para um sistema de armazenamento de fitas LTO-8 semanalmente. Retenção de 4 semanas.
        *   Para SQL Server: Copiar os backups completos diários e de log de transações para um servidor de arquivos secundário via script de robocopy a cada 4 horas.
5.  **Configuração da Terceira Cópia (Off-site)**:
    *   **Ação**: Enviar uma cópia dos backups para um local geograficamente distinto, seja nuvem pública ou outro datacenter. Esta cópia protege contra desastres locais (incêndio, inundação).
    *   **Exemplo**:
        *   Para Veeam: Configurar um repositório de escala para nuvem (Cloud Tier) para arquivar os backups mais antigos (após 30 dias) para AWS S3 Glacier Deep Archive, com retenção de 7 anos para dados financeiros e 1 ano para outros.
        *   Para backups de arquivos críticos da nuvem (ex: AWS EC2, S3): Usar AWS Backup para criar backups diários e replicá-los para uma região AWS diferente (ex: de São Paulo para N. Virginia) com política de retenção de 90 dias.

### Workflow 2: Procedimento de Recuperação de Desastres Pós-Incidente de Ransomware

Este workflow detalha os passos para restaurar sistemas e dados após um ataque de ransomware que comprometeu servidores de arquivos e aplicações.

1.  **Contenção e Análise Preliminar**:
    *   **Ação**: Isolar os sistemas afetados da rede. Identificar a extensão do comprometimento e o vetor de ataque inicial.
    *   **Exemplo**: Desconectar fisicamente ou desativar interfaces de rede dos servidores Windows que tiveram arquivos criptografados. Analisar logs de firewall e EDR para identificar o processo malicioso e usuários comprometidos. Não tentar restaurar imediatamente.
2.  **Identificação do Ponto de Recuperação Limpo (RPO)**:
    *   **Ação**: Usar a solução de backup para navegar pelas versões de backup e encontrar a versão mais recente que *precede* o ataque de ransomware, garantindo que o backup não contenha o malware ou os arquivos criptografados.
    *   **Exemplo**: O incidente foi detectado às 10:00h. O ransomware começou a criptografar às 08:30h. O último backup incremental limpo foi concluído às 08:00h. Definir este ponto como o RPO alvo.
3.  **Preparação do Ambiente de Restauração**:
    *   **Ação**: Provisionar um ambiente isolado (rede separada, sem acesso à rede de produção) para a restauração. Isso evita a reinfecção ou a propagação do malware durante a restauração e verificação.
    *   **Exemplo**: Criar uma VLAN específica e um pool de recursos em um ambiente de virtualização (vSphere) sem conectividade com a rede corporativa.
4.  **Restauração de Sistemas Críticos**:
    *   **Ação**: Restaurar os servidores e bases de dados críticos afetados para o ambiente isolado, utilizando o backup identificado no passo 2.
    *   **Exemplo**:
        *   **Servidores Windows com arquivos criptografados**: Usar Veeam para fazer um Instant VM Recovery ou Full VM Restore do servidor de arquivos para o ambiente isolado, selecionando o ponto de restauração das 08:00h.
        *   **Bancos de Dados**: Restaurar o banco de dados SQL Server de produção para um servidor SQL limpo no ambiente isolado, aplicando os logs de transação até o RPO alvo.
5.  **Verificação e Validação Pós-Restauração**:
    *   **Ação**: No ambiente isolado, realizar testes funcionais, verificar a integridade dos dados e escanear os sistemas restaurados com ferramentas de segurança atualizadas para garantir que estão livres de ameaças.
    *   **Exemplo**: Acessar o servidor de arquivos restaurado, verificar a abertura de arquivos aleatórios, executar um scan completo com antivírus/EDR. Testar as funcionalidades básicas da aplicação restaurada (ex: ERP login, cadastro de itens).
6.  **Reconexão e Monitoramento**:
    *   **Ação**: Após a validação, reconectar os sistemas restaurados à rede de produção e iniciar monitoramento intensivo.
    *   **Exemplo**: Mover os VMs restaurados para a VLAN de produção, configurar monitoramento de performance e segurança. Comunicar a equipe de TI e usuários sobre a restauração bem-sucedida e monitorar logs de acesso e atividade.

---

## Templates

### Política de Retenção de Backup Corporativa

```
# Política de Retenção de Backup Corporativa

**Data de Revisão:** 2024-07-26
**Responsável:** Equipe de Operações de TI

## 1. Objetivo
Definir os períodos de retenção de backups para diferentes categorias de dados, garantindo conformidade regulatória, capacidade de recuperação de desastres e otimização de custos de armazenamento.

## 2. Categorias de Dados e Políticas de Retenção

| Categoria de Dados | Exemplo de Ativos | Frequência de Backup | Retenção Diária | Retenção Semanal | Retenção Mensal | Retenção Anual | Observações |
|--------------------|-------------------|----------------------|-----------------|------------------|-----------------|----------------|-------------|
| **Missão Crítica (Tier 0)** | ERP, CRM, Bancos de Dados de Produção, Sistemas Financeiros | A cada 15 min (logs), Diário (completo) | 14 dias | 8 semanas | 12 meses | 7 anos | Requisito SOX, LGPD. |
| **Alta Criticidade (Tier 1)** | Servidores de Arquivos (Compartilhados), Intranet, Servidores de E-mail | A cada 4 horas (incremental), Diário (completo) | 7 dias | 4 semanas | 6 meses | 3 anos | Requisito LGPD. |
| **Média Criticidade (Tier 2)** | Servidores de Desenvolvimento, Teste, Aplicações Internas Não Críticas | Diário (completo) | 3 dias | 2 semanas | 3 meses | 1 ano | |
| **Baixa Criticidade (Tier 3)** | Estações de Trabalho (usuários selecionados), Servidores de Relatórios | Semanal (completo) | N/A | 2 semanas | N/A | N/A | |

## 3. Localização dos Backups

*   **Primário (On-premise):** NAS de Alta Performance (primeiros 14 dias diários, 8 semanas semanais).
*   **Secundário (On-premise):** Fitas LTO-8 (mensais e anuais).
*   **Terciário (Off-site/Nuvem):** AWS S3 Glacier Deep Archive (anual, acima de 1 ano de retenção).

## 4. Revisão
Esta política será revisada anualmente ou conforme mudanças significativas nos requisitos de negócios ou regulatórios.
```

### Plano de Teste de Restauração de Backup

```
# Plano de Teste de Restauração de Backup

**Serviço/Sistema Alvo:** Servidor de Aplicação Web (Apache/PHP) - Produção
**ID do Servidor:** SRV-WEB-PROD-01
**Data do Teste:** 2024-07-29
**Engenheiro Responsável:** João Silva
**Ambiente de Teste:** VLAN de Recuperação (10.0.100.0/24), isolada da produção.

## 1. Detalhes do Cenário de Teste
*   **Objetivo:** Validar a capacidade de restauração completa do SRV-WEB-PROD-01 e seus dados para um ambiente isolado, simulando uma falha total do servidor.
*   **Tipo de Backup a ser Usado:** Último backup completo semanal (2024-07-27 02:00h).
*   **RTO Alvo:** 4 horas
*   **RPO Alvo:** 24 horas

## 2. Passos do Teste

| Passo | Descrição da Ação | Tempo Estimado | Status (Concluído/Falha) | Observações/Resultados |
|-------|-------------------|----------------|--------------------------|------------------------|
| 2.1   | Criar VM temporária no ambiente de teste, com especificações idênticas ao SRV-WEB-PROD-01 (vCPU, RAM, Disco). | 15 min | Concluído | VM "SRV-WEB-TEST-01" criada. |
| 2.2   | Iniciar processo de restauração completa (Full VM Restore) do backup de 27/07/2024 via Veeam para SRV-WEB-TEST-01. | 1h 30 min | Concluído | Restauração concluída em 1h 25min. |
| 2.3   | Ligar a VM restaurada (SRV-WEB-TEST-01) no ambiente isolado. | 5 min | Concluído | Servidor inicializou sem erros. |
| 2.4   | Acessar o servidor via console/RDP e verificar a inicialização dos serviços (Apache, PHP-FPM, MySQL). | 15 min | Concluído | Todos os serviços iniciados e respondendo. |
| 2.5   | Testar acesso à aplicação web via navegador dentro do ambiente de teste. Verificar funcionalidade de login, navegação e consulta de dados. | 30 min | Concluído | Aplicação web funcional, dados consistentes com o backup. |
| 2.6   | Simular upload de arquivo e verificação da persistência. | 10 min | Concluído | Upload bem-sucedido. |
| 2.7   | Executar script de validação de banco de dados (checksum/integridade). | 20 min | Concluído | Integridade do DB verificada. |
| 2.8   | Registrar o tempo total de recuperação (desde 2.1 até 2.7). | 5 min | Concluído | Tempo total: 2 horas 50 minutos. |

## 3. Resultados e Análise
*   **Tempo Total de Recuperação:** 2 horas 50 minutos.
*   **Conformidade RTO:** Dentro do RTO alvo de 4 horas.
*   **Conformidade RPO:** Dados consistentes com o backup, atingindo RPO de 24 horas.
*   **Problemas Encontrados:** Nenhum.
*   **Recomendações:** Manter frequência de teste. Considerar automatizar parte da validação pós-restauração.

## 4. Aprovação
**Gerente de TI:** [Assinatura]
```

---

## Checklist

- [x] Todos os ativos de dados críticos foram mapeados e categorizados (Tier 0, 1, 2).
- [x] RTO e RPO foram definidos para cada categoria de dados, alinhados com o negócio.
- [x] A regra 3-2-1 de backup está implementada para todos os dados críticos.
- [x] Backups primários (on-site) estão configurados e sendo executados conforme o agendamento.
- [x] Backups secundários (em mídia diferente, on-site ou off-site) estão replicados/copiados com sucesso.
- [x] Backups off-site (nuvem ou outro datacenter) estão configurados e transferidos regularmente.
- [x] Políticas de retenção de dados estão configuradas na solução de backup e documentadas.
- [x] A criptografia de ponta a ponta (em trânsito e em repouso) está ativada para todos os backups.
- [x] Testes de restauração são realizados periodicamente (mensal/trimestral) e documentados.
- [x] Monitoramento de sucesso/falha dos jobs de backup está ativo, com alertas para falhas.
- [x] A documentação do plano de recuperação de desastres (DRP) está atualizada e acessível off-line.
- [x] Credenciais de acesso e chaves de criptografia para restauração estão armazenadas de forma segura e acessível.

---

## Métricas de Referência

| Métrica | Benchmark | Meta | Observações |
|---------|-----------|------|-------------|
| **RTO (Objetivo de Tempo de Recuperação)** | 4 horas (médio) | < 2 horas (Tier 0) | Tempo máximo para restaurar serviço. |
| **RPO (Objetivo de Ponto de Recuperação)** | 1 hora (médio) | < 15 minutos (Tier 0) | Perda máxima aceitável de dados. |
| **Taxa de Sucesso de Backup** | > 95% | > 98% | Percentual de jobs de backup concluídos com sucesso. |
| **Tempo Médio de Restauração (MTTR)** | 2 horas | < 1 hora | Tempo médio para restaurar um item específico. |
| **Custo por GB Armazenado** | R$ 0,05/GB/mês (nuvem) | R$ 0,03/GB/mês | Otimização de custos de armazenamento. |
| **Idade Média do Backup Mais Antigo Testado** | 6 meses | 3 meses | Regularidade dos testes de restauração. |

---

## Erros Comuns

1.  **Não Testar Restaurações Regularmente**: Muitas empresas configuram backups, mas falham em testar a capacidade de restauração.
    *   **Como evitar**: Implementar um cronograma de testes de restauração mensal para sistemas críticos e trimestral para outros, documentando os resultados e corrigindo quaisquer falhas. **Exemplo**: Agendar um teste de restauração de um servidor de arquivos para uma VM isolada na primeira segunda-feira de cada mês.
2.  **Configurações Incorretas de Retenção**: Políticas de retenção mal definidas ou implementadas podem levar à falta de dados históricos necessários ou ao consumo excessivo de armazenamento.
    *   **Como evitar**: Alinhar as políticas de retenção com requisitos regulatórios (LGPD, SOX) e de negócios, e verificar se o software de backup está aplicando essas políticas corretamente. **Exemplo**: Se a LGPD exige 5 anos para dados de clientes, garantir que os backups com esses dados tenham retenção mínima de 5 anos, e não apenas 1 ano como padrão.
3.  **Dependência de um Único Local de Backup (Sem Off-site)**: Armazenar todas as cópias de backup no mesmo local físico ou lógico expõe a organização a perda total em caso de desastre local.
    *   **Como evitar**: Garantir a implementação da regra 3-2-1, com pelo menos uma cópia de backup armazenada geograficamente distante, seja em nuvem pública ou em um datacenter secundário. **Exemplo**: Além do NAS local, replicar backups diários para AWS S3 em uma região diferente ou para fitas LTO armazenadas em um cofre externo.

---

## Dicas Avançadas

1.  **Implementar Backups Imutáveis**: Utilize o recurso de imutabilidade (object lock) em armazenamentos em nuvem (ex: AWS S3 Object Lock, Azure Blob Immutable Storage) ou soluções on-premise para proteger backups contra exclusão ou modificação, mesmo por administradores com privilégios. Isso é crucial contra ransomware.
    *   **Exemplo Prático**: Configure políticas de backup para que os dados sejam gravados em um bucket S3 com Object Lock habilitado, impedindo que os arquivos sejam apagados ou sobrescritos por um período definido (ex: 90 dias), mesmo se as credenciais forem comprometidas.
2.  **Automação e Orquestração de DR**: Não dependa de processos manuais para recuperação de desastres. Invista em ferramentas de orquestração de DR que automatizem a sequência de inicialização de VMs, configurações de rede e validações pós-recuperação.
    *   **Exemplo Prático**: Use o VMware Site Recovery Manager (SRM) ou o Azure Site Recovery para criar planos de recuperação que, em caso de desastre, iniciam automaticamente VMs em um site secundário na ordem correta, reconfiguram IPs e executam scripts de validação.
3.  **Classificação de Dados e Backup Granular**: Adote uma estratégia de backup que se alinhe à classificação de dados, permitindo diferentes frequências e retenções com base na sensibilidade e criticidade. Além disso, utilize backups granulares para recuperação de itens específicos.
    *   **Exemplo Prático**: Para dados PII/PHI (informações pessoais/de saúde), configure backups de log de transação a cada 5 minutos. Para arquivos de projeto não confidenciais, backups diários são suficientes. Use ferramentas como Veeam Explorer para SQL Server para restaurar uma única tabela ou um registro específico, em vez de um banco de dados inteiro.
4.  **Verificação Contínua da Integridade do Backup**: Além dos testes de restauração, utilize tecnologias que verificam automaticamente a integridade dos backups (ex: Veeam SureBackup) antes mesmo de um teste manual.
    *   **Exemplo Prático**: Configure um job Veeam SureBackup para ligar automaticamente VMs a partir de backups, executar scripts de teste (ping, acesso web, serviços), e gerar um relatório diário, garantindo que os backups são inicializáveis e os dados acessíveis.
5.  **Segregação de Rede para Infraestrutura de Backup**: Mantenha a rede de backup fisicamente ou logicamente separada da rede de produção. Isso impede que um ataque na rede de produção comprometa a infraestrutura de backup.
    *   **Exemplo Prático**: Configure uma VLAN dedicada para os servidores de backup e seus repositórios, com regras de firewall restritivas que permitem apenas a comunicação necessária para os jobs de backup e gerenciamento, isolando-a de outros segmentos de rede corporativos.