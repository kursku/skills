---
name: crisis-legal-playbook
description: "Crisis Legal Playbook — Skill especializada para crisis legal playbook"
license: MIT
metadata:
  version: 1.0.0
  author: Cafe Code AI
  category: 07-juridico-compliance
  updated: 2026-03-01
risk: safe
---

# Crisis Legal Playbook

Esta skill capacita o Claude a atuar como um especialista em gestão de crises legais, fornecendo estratégias, workflows e templates para mitigar riscos jurídicos e reputacionais em cenários de emergência.

---

## Keywords

Violação de Dados, LGPD, Incidente de Segurança, Crise Reputacional, Compliance Digital, Notificação ANPD, Contencioso de Crise, Medidas Mitigatórias, Resposta a Incidentes, Cyber-riscos, Comunicação Legal, Auditoria de Crise.

---

## Quick Start

1.  **Ativar Equipe de Resposta Legal (ERL)**: Acionar imediatamente o time jurídico interno e/ou externo especializado em crise ao primeiro sinal de incidente (ex: suspeita de vazamento de dados, notificação regulatória, publicações difamatórias massivas).
2.  **Avaliação Preliminar do Escopo Jurídico**: Realizar uma análise rápida para classificar o incidente (ex: violação de dados pessoais, falha de compliance contratual, alegação de fraude) e identificar as leis aplicáveis (LGPD, CDC, leis setoriais).
3.  **Preservação de Evidências Digitais e Físicas**: Instruir a equipe técnica e operacional a coletar e proteger todos os registros relevantes, logs de sistema, comunicações e documentos sem alteração, garantindo a cadeia de custódia.
4.  **Bloqueio de Comunicações Externas Não Aprovadas**: Emitir um memorando interno proibindo qualquer comunicação pública ou com terceiros (imprensa, clientes, fornecedores) sobre o incidente sem prévia revisão e aprovação da ERL.

---

## Core Workflows

### Workflow 1: Resposta Imediata a Violação de Dados Pessoais (LGPD)

Este workflow detalha as etapas jurídicas essenciais para responder a uma violação de dados pessoais, desde a detecção até as notificações regulatórias e de titulares, focando na minimização de riscos de multas e ações judiciais.

1.  **Detecção e Confirmação da Violação**:
    *   **Ação**: A equipe de TI/Segurança da Informação detecta uma anomalia (ex: acesso não autorizado a banco de dados de clientes, exfiltração de 500.000 registros de e-mail e CPF).
    *   **Resposta Legal**: A ERL é notificada. A primeira ação é verificar a materialidade e a natureza dos dados comprometidos (ex: dados sensíveis, dados de menores, grande volume).
    *   **Exemplo**: O SOC reporta um incidente crítico às 03:00 de 15/05/2025, indicando que o servidor 'SRV_CRM_PROD' teve suas credenciais comprometidas e há logs de download de um arquivo `client_data_Q2_2025.csv` contendo nome, CPF, e-mail e histórico de compras de 750.000 clientes.

2.  **Análise de Risco e Impacto aos Titulares**:
    *   **Ação**: Em conjunto com a equipe de Segurança da Informação, avaliar o risco real e potencial para os titulares dos dados.
    *   **Resposta Legal**: Determinar se a violação pode acarretar risco ou dano relevante aos titulares (ex: fraude de identidade, discriminação, perda financeira). A LGPD exige notificação se houver risco ou dano relevante.
    *   **Exemplo**: A análise forense indica que os dados vazados incluem credenciais de acesso a outros serviços (se reutilizadas pelos usuários) e informações financeiras sensíveis. O risco de fraude é considerado ALTO para 30% dos titulares impactados.

3.  **Implementação de Medidas de Contenção e Remediação**:
    *   **Ação**: A equipe técnica implementa ações para conter a violação (ex: isolar servidor, resetar senhas, aplicar patches de segurança).
    *   **Resposta Legal**: A ERL garante que as ações de contenção e remediação estejam documentadas para futuras auditorias e que não comprometam a preservação de evidências. Ações devem ser compatíveis com a minimização de danos aos titulares.
    *   **Exemplo**: Servidor isolado, senhas de administradores alteradas. Início da varredura por backdoors. É instruído que logs de acesso e modificação sejam copiados para um ambiente seguro antes de qualquer limpeza de sistema.

4.  **Notificação à Autoridade Nacional de Proteção de Dados (ANPD)**:
    *   **Ação**: Preparar e submeter a comunicação à ANPD.
    *   **Resposta Legal**: Conforme Art. 48 da LGPD, a notificação à ANPD deve ser feita em prazo razoável, contendo a descrição da natureza dos dados afetados, as informações sobre os titulares envolvidos, as medidas de segurança utilizadas, os riscos e as medidas já adotadas ou a serem adotadas.
    *   **Exemplo**: A notificação à ANPD é enviada em até 72 horas úteis após a confirmação da violação, detalhando o incidente de 15/05/2025 no SRV_CRM_PROD, envolvendo 750.000 CPFs, nomes e e-mails, e as medidas de contenção (isolamento, alteração de credenciais) e remediação (monitoramento, oferta de suporte aos titulares).

5.  **Notificação aos Titulares dos Dados**:
    *   **Ação**: Elaborar e enviar comunicação direta aos indivíduos afetados.
    *   **Resposta Legal**: A comunicação deve ser clara, transparente, e orientar os titulares sobre as medidas que podem tomar para se protegerem. Deve incluir contatos para dúvidas e suporte. O canal de comunicação (e-mail, carta) deve ser seguro e eficaz.
    *   **Exemplo**: E-mails individuais são enviados aos 750.000 clientes afetados, informando sobre o vazamento, o tipo de dado comprometido, as medidas tomadas pela empresa e a recomendação de alteração de senhas em outros serviços, além de um canal de atendimento exclusivo para o incidente (0800-XXX-XXXX).

### Workflow 2: Gestão de Crise Reputacional com Implicações Legais

Este workflow aborda a gestão de crises que envolvem alegações públicas (mídia, redes sociais) com potencial impacto legal significativo (ex: processos por difamação, investigações regulatórias, perda de licenças).

1.  **Monitoramento e Detecção de Alerta Legal Reputacional**:
    *   **Ação**: Equipes de comunicação e relações públicas detectam um volume atípico de menções negativas nas redes sociais ou notícias em portais de grande alcance sobre um defeito de produto ou conduta inadequada de um executivo.
    *   **Resposta Legal**: A ERL é acionada para analisar o conteúdo das alegações (ex: são difamatórias? há base factual? implicam violação de lei ou contrato?). Classificar o risco jurídico (ex: risco de ação civil pública, investigação do Ministério Público, processo por danos morais).
    *   **Exemplo**: Em 20/06/2025, após um incidente envolvendo um produto X que resultou em ferimentos leves a um consumidor, posts no Twitter e Facebook com a hashtag #ProdutoXPerigoso viralizam, acusando a empresa de negligência e má-fé. A equipe de monitoramento de mídia notifica o departamento jurídico, que identifica potencial para ações indenizatórias e recall compulsório.

2.  **Avaliação Jurídica da Alegação e Coleta de Provas Internas**:
    *   **Ação**: A ERL, em conjunto com as áreas técnicas e de comunicação, examina a veracidade das alegações e coleta informações internas.
    *   **Resposta Legal**: Levantar documentos internos (ex: relatórios de testes de produto, históricos de compliance, atas de reunião) que possam refutar ou corroborar as alegações. Preparar defesa jurídica preliminar.
    *   **Exemplo**: O jurídico solicita imediatamente relatórios de controle de qualidade do Produto X dos últimos 12 meses, registros de reclamações anteriores e o manual de instruções do produto. Descobre-se que o lote específico do produto foi testado e aprovado, mas um lote subsequente apresentou falha em testes de estresse.

3.  **Estratégia de Comunicação Juridicamente Alinhada**:
    *   **Ação**: Desenvolver uma estratégia de comunicação que seja transparente, empática e, crucialmente, juridicamente segura.
    *   **Resposta Legal**: Toda comunicação externa (press releases, notas em redes sociais, entrevistas) deve ser revisada e aprovada pela ERL para evitar admissões de culpa, informações contraditórias ou que possam ser usadas contra a empresa em litígios futuros.
    *   **Exemplo**: O jurídico aprova um comunicado que expressa solidariedade ao consumidor afetado, informa que a empresa está investigando internamente o incidente e reforça o compromisso com a segurança e qualidade, sem admitir culpa pelo lote específico do produto X, mas anunciando uma revisão proativa de todos os lotes do produto no mercado.

4.  **Engajamento com Partes Interessadas e Reguladores**:
    *   **Ação**: A depender da gravidade e do tipo de crise, pode ser necessário dialogar proativamente com órgãos reguladores, associações de consumidores ou autoridades judiciais.
    *   **Resposta Legal**: Preparar briefings legais para reuniões com reguladores (ex: PROCON, ANVISA, Ministério Público). Apresentar o plano de ação da empresa e as medidas mitigatórias.
    *   **Exemplo**: O jurídico e a diretoria de comunicação agendam uma reunião com o PROCON para apresentar os resultados preliminares da investigação interna sobre o Produto X e o plano de ação, que inclui um recall voluntário do lote suspeito e a criação de um canal de atendimento especial.

5.  **Monitoramento Contínuo e Resposta a Novas Alegações/Desdobramentos**:
    *   **Ação**: Monitorar a repercussão da crise e os desdobramentos legais (ex: novas reclamações, intimações, ações judiciais).
    *   **Resposta Legal**: Ajustar a estratégia jurídica e de comunicação conforme novos fatos surgem. Preparar respostas a eventuais intimações ou citações.
    *   **Exemplo**: Após o recall, surge uma nova onda de posts alegando que a empresa já sabia do problema. O jurídico revisa a estratégia, preparando uma defesa robusta baseada nos relatórios de testes e na proatividade do recall voluntário, além de monitorar ações judiciais para apresentar defesas individualizadas.

---

## Templates

### Modelo de Notificação Preliminar de Incidente de Segurança (ANPD)

```
[Nome da Empresa/Organização]
[CNPJ da Empresa/Organização]
[Endereço da Sede]
[E-mail do DPO/Contato]
[Telefone do DPO/Contato]

À
Autoridade Nacional de Proteção de Dados (ANPD)
Protocolo de Notificação de Incidente de Segurança

Prezados Senhores,

Em conformidade com o Art. 48 da Lei Geral de Proteção de Dados Pessoais (Lei nº 13.709/2018 – LGPD), vimos por meio desta notificar formalmente a ocorrência de um incidente de segurança da informação em nossa infraestrutura.

1.  **Data e Hora da Detecção do Incidente**: 15 de Maio de 2025, às 03:15 BRT.
2.  **Natureza do Incidente**: Acesso não autorizado a banco de dados.
3.  **Dados Pessoais Afetados**:
    *   Nome completo
    *   CPF
    *   Endereço de e-mail
    *   Histórico de compras (produtos adquiridos, valores)
    *   Dados de contato telefônico
4.  **Número Estimado de Titulares Afetados**: Aproximadamente 750.000 (setecentos e cinquenta mil) clientes.
5.  **Medidas de Segurança Utilizadas antes do Incidente**: Firewall de borda, VPN para acesso administrativo, senhas fortes e rotação periódica, criptografia de dados em repouso (AES-256) no armazenamento principal.
6.  **Causas do Incidente (Análise Preliminar)**: Comprometimento de credenciais de acesso de um funcionário terceirizado, possivelmente via phishing, permitindo acesso indevido ao servidor SRV_CRM_PROD.
7.  **Medidas Adotadas para Conter e Mitigar o Incidente**:
    *   Isolamento imediato do servidor comprometido (15/05/2025, 03:45 BRT).
    *   Reset e reforço de todas as credenciais de acesso administrativas (15/05/2025, 04:30 BRT).
    *   Análise forense detalhada em andamento para identificar o vetor de ataque e extensão da exfiltração.
    *   Revisão de logs de segurança e auditoria interna de vulnerabilidades.
8.  **Riscos Relevantes para os Titulares**: Alto risco de fraude de identidade, golpes de phishing direcionados e uso indevido de dados pessoais para fins ilícitos, dada a natureza das informações vazadas.
9.  **Medidas Adotadas ou a Serem Adotadas em Relação aos Titulares**:
    *   Notificação individualizada aos titulares via e-mail a partir de 17/05/2025.
    *   Criação de um canal de atendimento exclusivo (0800-XXX-XXXX) e e-mail (privacidade@exemplo.com.br) para suporte e esclarecimentos.
    *   Recomendação explícita aos titulares para alterarem suas senhas em outros serviços e ativarem autenticação de dois fatores.
    *   Oferecimento de serviço de monitoramento de crédito por 12 meses, sem custo, para os titulares mais vulneráveis.

Permanecemos à disposição para quaisquer esclarecimentos adicionais e para cooperar integralmente com as investigações da ANPD.

Atenciosamente,

[Assinatura do DPO/Representante Legal]
[Nome Completo do DPO/Representante Legal]
[Cargo]
[Data]
```

### Modelo de Declaração Pública Inicial (Crise Reputacional)

```
[Logotipo da Empresa]

**COMUNICADO À IMPRENSA E AO PÚBLICO**

**[Nome da Cidade], [Data]** – [Nome da Empresa] vem a público para abordar as recentes informações e preocupações levantadas sobre [mencionar brevemente o tema da crise, ex: "o incidente envolvendo o Produto X" ou "alegações de falha em nosso serviço de internet"].

Primeiramente, expressamos nossa mais profunda solidariedade aos [mencionar partes afetadas, ex: "consumidores impactados pelo incidente com o Produto X" ou "nossos clientes que experimentaram interrupções no serviço"]. A segurança, a satisfação e a confiança de nossos [clientes/consumidores/parceiros] são a nossa prioridade máxima e o pilar de nossa operação.

Estamos levando [a situação/o incidente/as alegações] com a máxima seriedade e já iniciamos uma investigação interna rigorosa e abrangente para apurar todos os fatos. Nossas equipes de [mencionar áreas relevantes, ex: "engenharia, qualidade e jurídica"] estão trabalhando incansavelmente para entender as causas e implementar as ações necessárias.

É importante ressaltar que [Nome da Empresa] pauta suas operações pela [mencionar valores/compromissos, ex: "excelência, conformidade com as normas regulatórias e transparência"]. Assim que tivermos informações mais concretas e os resultados da nossa investigação, nos comprometemos a compartilhá-los de forma clara e responsável com o público e as autoridades competentes.

Enquanto isso, [mencionar ações imediatas da empresa, ex: "recomendamos que os consumidores que possuem o Produto X do lote 'ABC-123' se abstenham de utilizá-lo e entrem em contato com nosso SAC para orientações" ou "estamos trabalhando para restaurar a estabilidade total do serviço e nossos técnicos estão de plantão para atender todas as solicitações"].

Disponibilizamos o canal de atendimento [telefone/e-mail/link] para que [clientes/consumidores] possam tirar dúvidas e obter suporte direto.

Agradecemos a compreensão e reiteramos nosso compromisso inabalável com a qualidade e a segurança.

Atenciosamente,

[Nome do Porta-voz/Diretoria]
[Cargo]
[Nome da Empresa]
```

---

## Checklist

- [X] Ativar o comitê de crise legal, incluindo o DPO, CISO e advogados externos especializados.
- [X] Isolar o incidente imediatamente para evitar propagação e danos adicionais.
- [X] Preservar todas as evidências digitais e físicas relacionadas ao incidente, garantindo a cadeia de custódia.
- [X] Realizar uma análise de impacto regulatório e legal, identificando as leis e autoridades aplicáveis (LGPD, CDC, setoriais).
- [X] Definir a estratégia de comunicação interna e externa, com todas as mensagens revisadas e aprovadas pelo jurídico.
- [X] Preparar e submeter a notificação preliminar à ANPD em prazo razoável (até 72h úteis para incidentes de dados).
- [X] Elaborar e enviar as notificações aos titulares de dados afetados, com orientações claras e canais de suporte.
- [X] Monitorar continuamente a repercussão na mídia, redes sociais e novas reclamações/intimações.
- [X] Avaliar a necessidade de recall de produtos ou serviços, com base em análises de risco e requisitos regulatórios.
- [X] Documentar detalhadamente todas as ações tomadas, decisões, comunicações e análises para futuras auditorias e defesa legal.

---

## Métricas de Referência

| Métrica                                   | Benchmark (Indústria) | Meta (Empresa) |
|:------------------------------------------|:----------------------|:---------------|
| Tempo Médio para Detecção (MTTD)          | < 24 horas            | < 12 horas     |
| Tempo Médio para Resposta (MTTR)          | < 72 horas            | < 48 horas     |
| Percentual de Notificações à ANPD no Prazo | 95%                   | 100%           |
| Taxa de Reclamações Pós-Crise (1º mês)    | < 0.5% dos afetados   | < 0.2% dos afetados |
| Percentual de Incidentes com Multa Aplicada | < 5%                  | < 1%           |
| Tempo Médio para Resolução de Contencioso | < 18 meses            | < 12 meses     |

---

## Erros Comuns

1.  **Comunicar-se Precocemente Sem Alinhamento Jurídico**: Uma declaração impulsiva, como um tweet da diretoria negando veementemente um problema de produto antes de uma investigação completa, pode ser interpretada como má-fé ou admissão de culpa em um processo futuro. Evitar: Todas as comunicações públicas devem ser previamente validadas pela ERL para garantir precisão e evitar implicações legais negativas, focando em fatos confirmados e compromissos com a investigação.
2.  **Não Preservar Evidências de Forma Adequada**: Apagar logs de sistema ou formatar discos rígidos de servidores comprometidos na tentativa de "limpar" o incidente, inviabilizando a análise forense e a defesa jurídica. Evitar: Instruir a equipe técnica a seguir um protocolo rigoroso de preservação de evidências digitais (bit-a-bit), garantindo a cadeia de custódia e a integridade dos dados para futuras perícias e auditorias.
3.  **Subestimar a Abrangência Regulatória**: Acreditar que um incidente de dados afeta apenas a LGPD, ignorando outras leis setoriais (ex: Banco Central para fintechs, ANS para saúde) ou o Código de Defesa do Consumidor, que podem impor deveres adicionais de notificação e reparação. Evitar: Realizar uma análise jurídica multifacetada, envolvendo especialistas em diversas áreas do direito para identificar todas as obrigações regulatórias e legais aplicáveis ao tipo de incidente.

---

## Dicas Avançadas

1.  **Simulações de Mesa (Tabletop Exercises)**: Realizar anualmente exercícios de simulação de crise legal (ex: um vazamento de dados simulado ou uma acusação pública de fraude), envolvendo todas as equipes chave (jurídico, TI, comunicação, RH, alta gestão). Isso identifica lacunas no playbook e melhora o tempo de resposta sob pressão.
2.  **Preparação de Cenários de Pré-Crise (Pre-mortems)**: Antes de lançar um novo produto ou serviço, conduzir sessões de "pre-mortem" com a ERL para imaginar os piores cenários de crise legal que poderiam surgir e desenvolver planos de contingência proativos. Ex: "E se nosso novo app de saúde vazar dados sensíveis de pacientes? Quais cláusulas contratuais protegeriam a empresa?"
3.  **Uso Estratégico de Privilégio Advogado-Cliente**: Garantir que toda a comunicação e investigação interna relacionada a um incidente, especialmente as análises de vulnerabilidade e atribuição de culpa, sejam conduzidas sob o manto do privilégio advogado-cliente, envolvendo o jurídico desde o início para proteger informações sensíveis de serem usadas contra a empresa em litígios. Ex: Todas as comunicações sobre a investigação do incidente são enviadas para o e-mail do jurídico e marcadas como "Confidencial - Privilégio Advogado-Cliente".
4.  **Engajamento com White-Hat Hackers e Bug Bounty Programs**: Implementar programas de recompensa por bugs ou contratar hackers éticos para encontrar vulnerabilidades antes que atores maliciosos o façam. Isso não apenas fortalece a segurança, mas também demonstra proatividade e boa-fé em caso de incidentes futuros, servindo como atenuante em avaliações regulatórias.
5.  **Contratos de Resposta a Incidentes Pré-Negociados**: Manter contratos pré-negociados com empresas de forense digital, relações públicas de crise e escritórios de advocacia especializados em contencioso de crise. Isso reduz o tempo de ativação e garante acesso a expertise crítica durante a janela de resposta mais crucial, evitando a demora na fase de contratação.