---
name: vendor-agreement
description: "Vendor Agreement — Skill especializada para vendor agreement"
license: MIT
metadata:
  version: 1.0.0
  author: Cafe Code AI
  category: 07-juridico-compliance
  updated: 2026-03-01
---

# Vendor Agreement

Esta skill capacita o Claude a atuar como um especialista na elaboração, revisão, negociação e gestão de contratos de fornecimento, assegurando conformidade legal e minimizando riscos para a empresa.

---

## Keywords

Contrato de Fornecimento, Termos e Condições, SLA, LGPD, GDPR, Cláusula de Confidencialidade, Indenização, Rescisão Contratual, Due Diligence Fornecedor, Gestão de Riscos, Compliance Contratual, Propriedade Intelectual, DPA, Subprocessador, Governança de Terceiros, Cláusulas Anti-Corrupção.

---

## Quick Start

1.  **Gerar minuta de Vendor Agreement para SaaS**: Solicite um rascunho de contrato de fornecimento de software como serviço, incluindo obrigações de LGPD para o fornecedor.
2.  **Analisar cláusulas de SLA**: Carregue um contrato existente e peça uma análise das cláusulas de Service Level Agreement (SLA), identificando pontos de risco e sugestões de melhoria.
3.  **Avaliar conformidade LGPD em contrato de marketing**: Peça para revisar um contrato com agência de marketing digital, focando na adequação das cláusulas de tratamento de dados pessoais.
4.  **Criar checklist de due diligence para novo fornecedor**: Solicite um checklist detalhado para a avaliação de um potencial fornecedor de infraestrutura de TI, cobrindo aspectos jurídicos e de segurança.

---

## Core Workflows

### Workflow 1: Elaboração e Negociação de Contrato de Fornecimento de Software SaaS com Foco em LGPD

Este workflow detalha a criação de um contrato de fornecimento de software SaaS, com ênfase nas exigências da Lei Geral de Proteção de Dados (LGPD).

1.  **Coleta de Requisitos Iniciais e Partes**:
    *   **Ação**: Obtenha os dados completos do Contratante e do Fornecedor, incluindo razões sociais, CNPJs, endereços completos e dados dos representantes legais. Defina o escopo preliminar do software e os serviços associados.
    *   **Exemplo**:
        *   `Contratante`: **Tech Solutions Ltda.**, CNPJ: 12.345.678/0001-90, Endereço: Av. Paulista, 1000, São Paulo/SP. Representada por João Silva, Diretor Jurídico.
        *   `Fornecedor`: **CloudMaster S.A.**, CNPJ: 98.765.432/0001-00, Endereço: Rua da Nuvem, 500, Rio de Janeiro/RJ. Representada por Maria Souza, CEO.
        *   `Objeto`: Licença de uso do software "DataInsight Pro" (versão 3.0) e serviços de suporte Nível 2.

2.  **Definição do Escopo Detalhado e SLA**:
    *   **Ação**: Especifique minuciosamente as funcionalidades do software, os módulos inclusos, os limites de usuários/armazenamento, e os serviços de suporte. Crie um Anexo de SLA detalhado.
    *   **Exemplo**:
        *   `Software`: Licença de uso não exclusiva e intransferível do DataInsight Pro, com acesso a módulos de Business Intelligence e Relatórios Gerenciais.
        *   `SLA`:
            *   `Disponibilidade do Serviço`: 99.9% de uptime mensal.
            *   `Tempo de Resposta para Incidentes Críticos (P1)`: 2 horas.
            *   `Tempo de Resolução para Incidentes Críticos (P1)`: 8 horas.
            *   `Multa por Descumprimento de SLA`: 0.5% do valor mensal do contrato por cada ponto percentual abaixo da meta de disponibilidade, limitado a 5% do valor mensal.

3.  **Elaboração de Cláusulas de Proteção de Dados (DPA - Data Processing Addendum)**:
    *   **Ação**: Desenvolva um anexo específico (DPA) que determine os papéis (Controlador/Operador), finalidades do tratamento, tipos de dados pessoais envolvidos, medidas de segurança, direitos dos titulares e obrigações de notificação de incidentes.
    *   **Exemplo**:
        *   `Papéis`: Contratante como Controlador, Fornecedor como Operador.
        *   `Finalidade`: Processamento de dados de clientes do Contratante para fins de análise e geração de relatórios no DataInsight Pro.
        *   `Tipos de Dados`: Nome, CPF, e-mail, telefone, histórico de compras.
        *   `Medidas de Segurança`: Criptografia de dados em repouso e em trânsito (TLS 1.2+), controle de acesso baseado em função, auditorias de segurança anuais (SOC 2 Type II).
        *   `Incidentes`: Fornecedor deve notificar o Contratante em até 48 horas sobre qualquer incidente de segurança que possa impactar dados pessoais.

4.  **Inclusão de Cláusulas Essenciais Adicionais**:
    *   **Ação**: Garanta a presença de cláusulas de confidencialidade, propriedade intelectual, responsabilidade civil e indenização, condições de pagamento, vigência e rescisão, foro e legislação aplicável.
    *   **Exemplo**:
        *   `Confidencialidade`: Duração de 5 anos após o término do contrato.
        *   `Propriedade Intelectual`: O Fornecedor detém a PI do software; o Contratante detém a PI dos dados inseridos.
        *   `Indenização`: Limite de responsabilidade do Fornecedor ao valor anual do contrato, exceto em casos de dolo, fraude ou violação de dados pessoais.
        *   `Pagamento`: Mensal, via boleto, com vencimento no dia 5. Multa de 2% e juros de 1% ao mês por atraso.

5.  **Revisão Jurídica e Negociação**:
    *   **Ação**: Submeta a minuta para revisão interna (jurídico, área de TI, financeiro) e inicie a negociação com o Fornecedor, buscando equilibrar os interesses das partes.
    *   **Exemplo**: O jurídico do Contratante solicita a inclusão de uma cláusula de direito de auditoria para verificar a conformidade do Fornecedor com a LGPD a cada 18 meses. O Fornecedor contrapropõe que a auditoria seja realizada por um terceiro independente e com custos compartilhados.

### Workflow 2: Análise de Risco e Conformidade (LGPD/GDPR) em Contrato de Prestação de Serviços de Nuvem

Este workflow foca na avaliação de riscos e conformidade regulatória (LGPD/GDPR) de um contrato existente com um provedor de serviços de nuvem (IaaS/PaaS).

1.  **Identificação do Contexto e Tipo de Dados**:
    *   **Ação**: Determine quais serviços de nuvem estão sendo utilizados (ex: armazenamento, computação, banco de dados) e quais categorias de dados pessoais serão ou já estão sendo tratados pelo fornecedor.
    *   **Exemplo**:
        *   `Serviço`: Provedor de IaaS para hospedar aplicações internas e banco de dados de clientes.
        *   `Dados Tratados`: Dados de funcionários (holerites, dados cadastrais), dados de clientes (nome, e-mail, dados bancários). Categorias: Pessoais e Pessoais Sensíveis (se houver dados de saúde ou biometria).

2.  **Verificação de Cláusulas de Proteção de Dados Existentes**:
    *   **Ação**: Analise o contrato e seus anexos (DPA) para confirmar a existência e adequação das cláusulas de proteção de dados à LGPD e, se aplicável, à GDPR (casos de clientes na UE).
    *   **Exemplo**: O contrato atual possui uma cláusula genérica que "o Fornecedor cumprirá a legislação aplicável de proteção de dados". Isso é insuficiente. É necessário um DPA que detalhe:
        *   `Papéis`: Controladora (Empresa) e Operadora (Provedora de Nuvem).
        *   `Instruções`: O Provedor de Nuvem só pode processar dados conforme as instruções documentadas da Empresa.
        *   `Subprocessadores`: Requerimento de aprovação prévia para subcontratação e garantia de que subprocessadores sigam as mesmas obrigações.

3.  **Avaliação da Transferência Internacional de Dados**:
    *   **Ação**: Verifique onde os dados estão sendo armazenados e processados. Se houver transferência para países sem nível adequado de proteção, avalie as bases legais (Cláusulas Contratuais Padrão - SCCs, normas corporativas globais, etc.).
    *   **Exemplo**: Os servidores do provedor de nuvem estão localizados nos EUA. O contrato deve prever a adoção das Cláusulas Contratuais Padrão (SCCs) da Comissão Europeia ou garantir que o provedor tenha certificações como o Privacy Shield (se aplicável e atualizado) para assegurar a conformidade.

4.  **Análise das Medidas de Segurança e Auditoria**:
    *   **Ação**: Revise as cláusulas que descrevem as medidas de segurança técnicas e organizacionais do fornecedor. Verifique se há direito de auditoria ou se o fornecedor apresenta relatórios de certificações (ISO 27001, SOC 2).
    *   **Exemplo**: O contrato deve exigir que o provedor de nuvem implemente:
        *   `Criptografia`: Dados em repouso (AES-256) e em trânsito (TLS 1.3).
        *   `Controle de Acesso`: Baseado em privilégios mínimos e autenticação multifator.
        *   `Backups e Recuperação`: Plano de recuperação de desastres (DRP) com RTO de 4 horas e RPO de 1 hora.
        *   `Auditoria`: Direito da Empresa realizar auditorias de segurança anuais ou solicitar relatórios SOC 2 Type II e ISO 27001.

5.  **Revisão de Responsabilidades e Cláusulas de Saída**:
    *   **Ação**: Analise a limitação de responsabilidade, indenização e as cláusulas de saída (exit strategy) para garantir que a empresa esteja protegida em caso de incidentes ou término do contrato.
    *   **Exemplo**:
        *   `Responsabilidade`: Limitação de responsabilidade do provedor de nuvem não deve se aplicar a casos de dolo, fraude ou violação de dados pessoais.
        *   `Indenização`: O provedor deve indenizar a Empresa por perdas decorrentes de falhas de segurança que resultem em violação de dados.
        *   `Cláusula de Saída`: Em caso de rescisão, o provedor deve garantir a devolução segura de todos os dados da Empresa em formato compatível e auxiliar na migração para outro provedor por um período de 90 dias, sem custo adicional pela migração (apenas pelo consumo de recursos).

---

## Templates

### Cláusula de Confidencialidade Padrão para Vendor Agreement

```
CLÁUSULA QUINTA – CONFIDENCIALIDADE E PROTEÇÃO DE DADOS

5.1. As Partes reconhecem que, no curso da execução deste Contrato, terão acesso a informações confidenciais uma da outra, incluindo, mas não se limitando a, segredos comerciais, dados técnicos, estratégias de negócios, informações financeiras, dados de clientes, planos de marketing e quaisquer outras informações não públicas (“Informações Confidenciais”).

5.2. Cada Parte se compromete a manter em sigilo absoluto todas as Informações Confidenciais da outra Parte, abstendo-se de divulgá-las a terceiros não autorizados ou utilizá-las para qualquer propósito que não seja a execução deste Contrato. As Informações Confidenciais somente poderão ser acessadas por funcionários, agentes ou subcontratados que necessitem delas para o cumprimento de suas obrigações contratuais e que estejam igualmente vinculados por obrigações de confidencialidade não menos rigorosas que as aqui estabelecidas.

5.3. As obrigações de confidencialidade estabelecidas nesta Cláusula persistirão por um período de 5 (cinco) anos a contar da data de término ou rescisão deste Contrato, independentemente do motivo.

5.4. Excluem-se da obrigação de confidencialidade as informações que: (i) já eram de conhecimento público no momento da divulgação ou tornem-se públicas sem violação deste Contrato; (ii) já eram de posse da Parte receptora antes da divulgação pela Parte divulgadora; (iii) foram desenvolvidas independentemente pela Parte receptora; ou (iv) cuja divulgação seja exigida por lei ou ordem judicial, mediante prévia notificação à Parte divulgadora, sempre que possível.
```

### Cláusula de Proteção de Dados (LGPD) para Vendor Agreement (Operador)

```
CLÁUSULA SEXTA – PROTEÇÃO DE DADOS PESSOAIS (LGPD)

6.1. As Partes reconhecem que, para os fins deste Contrato, o Contratante atua como Controlador de Dados Pessoais e o Fornecedor atua como Operador de Dados Pessoais, conforme definido pela Lei nº 13.709/2018 (Lei Geral de Proteção de Dados – LGPD).

6.2. O Fornecedor se compromete a tratar os Dados Pessoais aos quais tiver acesso estritamente de acordo com as instruções documentadas do Contratante e para as finalidades específicas deste Contrato, não os utilizando para fins próprios ou diversos dos acordados.

6.3. O Fornecedor deverá implementar e manter medidas de segurança técnicas e organizacionais adequadas para proteger os Dados Pessoais contra acesso não autorizado, destruição, perda, alteração, comunicação ou qualquer forma de tratamento inadequado ou ilícito. Tais medidas incluem, mas não se limitam a, criptografia de dados em repouso e em trânsito, controle de acesso baseado em função, auditorias de segurança regulares e planos de contingência.

6.4. Em caso de incidente de segurança envolvendo Dados Pessoais, o Fornecedor deverá notificar o Contratante em até 48 (quarenta e oito) horas após tomar conhecimento do ocorrido, fornecendo todas as informações relevantes para que o Contratante possa cumprir suas obrigações perante a ANPD e os titulares dos dados.

6.5. O Fornecedor garantirá que seus colaboradores e quaisquer subprocessadores envolvidos no tratamento de Dados Pessoais estejam sujeitos a obrigações de confidencialidade e cumpram as disposições desta Cláusula. A subcontratação de qualquer subprocessador exige prévia e expressa autorização por escrito do Contratante.

6.6. Ao término ou rescisão deste Contrato, o Fornecedor deverá, a critério do Contratante, eliminar ou devolver todos os Dados Pessoais tratados, bem como quaisquer cópias existentes, salvo se houver exigência legal para sua retenção.

6.7. O Fornecedor indenizará o Contratante por quaisquer perdas, danos, multas ou sanções impostas por autoridades competentes, decorrentes de sua violação às obrigações de proteção de dados pessoais estabelecidas neste Contrato e na legislação aplicável.
```

---

## Checklist

-   [x] **Partes Contratantes**: Razão social, CNPJ, endereço e representantes legais de ambas as partes corretamente identificados?
-   [x] **Objeto e Escopo**: O objeto do contrato e o escopo dos produtos/serviços fornecidos estão detalhados e sem ambiguidades?
-   [x] **Preço e Condições de Pagamento**: Valores, prazos, formas de pagamento, multas por atraso e condições de reajuste definidos claramente?
-   [x] **Vigência e Rescisão**: Prazo de duração do contrato, condições de renovação automática e cláusulas de rescisão (com e sem justa causa) explicitadas?
-   [x] **SLA (Service Level Agreement)**: Níveis de serviço, métricas, penalidades por descumprimento e procedimentos de reporte e resolução de incidentes detalhados?
-   [x] **Confidencialidade**: Cláusulas robustas de confidencialidade, incluindo duração e exceções, para proteger informações estratégicas?
-   [x] **Proteção de Dados (LGPD/GDPR)**: O DPA (Data Processing Addendum) está presente, especifica papéis, finalidades, medidas de segurança, notificação de incidentes e obrigações de subprocessadores?
-   [x] **Propriedade Intelectual**: Definição clara sobre a titularidade e licenciamento de direitos de propriedade intelectual (software, conteúdo, etc.)?
-   [x] **Responsabilidade e Indenização**: Limites de responsabilidade, cenários de indenização e exclusões de responsabilidade bem delimitados?
-   [x] **Cláusulas Anticorrupção/Compliance**: Inclusão de disposições que assegurem a conformidade com leis anticorrupção (Ex: Lei nº 12.846/2013) e políticas de ética?
-   [x] **Foro e Legislação Aplicável**: Eleição de foro para dirimir conflitos e indicação da legislação aplicável ao contrato?
-   [x] **Assinaturas e Anexos**: Todas as partes assinaram eletronicamente ou fisicamente, e todos os anexos mencionados estão devidamente incorporados?

---

## Métricas de Referência

| Métrica                                | Benchmark              | Meta                   |
|:---------------------------------------|:-----------------------|:-----------------------|
| Tempo Médio de Negociação de Contrato  | 20-45 dias             | < 30 dias              |
| Taxa de Conformidade Contratual (LGPD) | > 90% (em auditoria)   | 100%                   |
| % de Contratos com SLA Definido        | 80% dos críticos       | 95% dos críticos       |
| Número de Aditivos/Contrato/Ano        | < 3                    | < 1                    |
| Custo de Não Conformidade (Multas LGPD)| R$ 0 (meta)            | R$ 0 (meta)            |
| Prazo Médio de Revisão Jurídica        | 5-10 dias úteis        | < 7 dias úteis         |

---

## Erros Comuns

1.  **Cláusulas de Proteção de Dados Genéricas ou Inexistentes**: Muitas empresas usam textos padrão que não se adaptam ao tipo específico de tratamento de dados, ou pior, não incluem nenhuma cláusula.
    *   **Como evitar**: Exija e negocie um DPA (Data Processing Addendum) específico, detalhando os papéis (Controlador/Operador), as finalidades do tratamento, os tipos de dados pessoais envolvidos, as medidas de segurança técnicas e organizacionais, as obrigações de notificação de incidentes e os direitos dos titulares.
    *   **Exemplo**: Em vez de "O Fornecedor cumprirá a LGPD", detalhe: "O Fornecedor, na qualidade de Operador, processará os dados pessoais exclusivamente para [finalidade específica, ex: gestão de folha de pagamento], implementando medidas como [criptografia de dados em repouso, MFA para acesso ao sistema]."

2.  **Escopo de Serviço Ambíguo ou Incompleto**: A falta de clareza no escopo gera disputas sobre o que o fornecedor deve entregar e o que está fora do contrato, levando a aditivos ou insatisfação.
    *   **Como evitar**: Detalhe o escopo com entregáveis concretos, marcos, prazos, responsabilidades de cada parte e explicitamente o que *não* está incluído. Use anexos para especificações técnicas se necessário.
    *   **Exemplo**: Em vez de "Serviços de desenvolvimento de software", especifique: "Desenvolvimento do módulo de 'Gestão de Estoque' para o ERP X, versão 2.0, com as funcionalidades A, B e C, entregáveis em 3 fases (planejamento, desenvolvimento, testes) com marcos definidos e aceite formal em cada fase. Exclui-se personalização da interface gráfica fora do padrão do ERP X."

3.  **Limitação de Responsabilidade Desequilibrada**: Cláusulas que limitam excessivamente a responsabilidade do fornecedor podem deixar o Contratante desprotegido em caso de falhas críticas, especialmente em violação de dados ou interrupção de serviço.
    *   **Como evitar**: Negocie limites de responsabilidade que sejam proporcionais ao risco e ao valor do contrato. Exclua da limitação de responsabilidade casos de dolo, fraude, negligência grave e, crucialmente, violações de dados pessoais.
    *   **Exemplo**: "A responsabilidade total do Fornecedor por quaisquer danos decorrentes deste Contrato será limitada ao valor anual do Contrato. Contudo, tal limitação não se aplicará a danos causados por dolo, fraude, negligência grave, violação de propriedade intelectual de terceiros ou violação das obrigações de proteção de dados pessoais estabelecidas na Cláusula Sexta."

---

## Dicas Avançadas

1.  **Utilização de Matrizes de Risco Contratual**: Desenvolva e utilize uma matriz de risco para cada novo Vendor Agreement, classificando riscos (legal, operacional, financeiro, reputacional, cibernético) e associando-os a cláusulas contratuais específicas. Isso permite uma negociação mais estratégica e focada em mitigar os pontos mais críticos.
    *   **Exemplo**: Para um fornecedor de serviços de cloud, um risco "Alto" de segurança cibernética (devido ao tratamento de dados sensíveis) exigiria cláusulas detalhadas sobre auditorias de segurança, certificações obrigatórias (ISO 27001, SOC 2 Type II), seguro cibernético e um DPA robusto com notificação imediata de incidentes.

2.  **Cláusulas de Auditoria e "Right to Audit" Detalhadas**: Não basta ter a cláusula. Especifique a frequência, escopo, tipo de auditoria (remota, no local), quem arca com os custos e o prazo para o fornecedor corrigir não conformidades. Isso é vital para a governança de terceiros e conformidade contínua.
    *   **Exemplo**: "O Contratante terá o direito de conduzir, ou de fazer com que um terceiro independente conduza, auditorias de segurança e conformidade de dados nas instalações do Fornecedor ou remotamente, uma vez a cada 18 (dezoito) meses, mediante aviso prévio de 30 (trinta) dias. Os custos da auditoria serão do Contratante, salvo se forem encontradas não conformidades graves, caso em que os custos de uma auditoria subsequente para verificar a remediação serão do Fornecedor."

3.  **Estratégia de Saída (Exit Strategy) Abrangente**: Planeje a descontinuidade do serviço desde a negociação inicial. Inclua cláusulas que detalhem o processo de transição, a devolução de dados em formatos interoperáveis, assistência na migração para um novo fornecedor ou internalização do serviço, e prazos para desativação de acessos.
    *   **Exemplo**: "Em caso de rescisão ou término do Contrato, o Fornecedor deverá, em até 30 (trinta) dias, devolver todos os dados do Contratante em formato CSV e JSON, garantindo a integridade e segurança. O Fornecedor deverá, ainda, prestar assistência razoável na migração dos serviços para um novo fornecedor indicado pelo Contratante por um período de até 90 (noventa) dias, mediante remuneração acordada à parte, ou sem custo adicional se a rescisão for por culpa do Fornecedor."

4.  **Integração com Políticas Internas de Compliance**: O Vendor Agreement deve refletir e exigir a conformidade do fornecedor com as políticas internas do Contratante (ex: Código de Conduta, Política de Segurança da Informação, Política Anticorrupção), garantindo alinhamento e mitigação de riscos reputacionais.
    *   **Exemplo**: "O Fornecedor declara e garante que cumprirá integralmente o Código de Conduta do Contratante, disponível em [URL], bem como todas as leis e regulamentos aplicáveis, incluindo as leis anticorrupção (ex: Lei nº 12.846/2013) e leis de proteção de dados. Qualquer violação destas políticas ou leis será considerada justa causa para rescisão imediata do Contrato."

5.  **Gerenciamento de Terceiros e Quarta Parte (Subprocessadores)**: Para contratos críticos, exija que o fornecedor detalhe sua cadeia de subprocessadores (