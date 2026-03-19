---
name: employment-contract-digital
description: "Employment Contract Digital — Skill especializada para employment contract digital"
license: MIT
metadata:
  version: 1.0.0
  author: Cafe Code AI
  category: 07-juridico-compliance
  updated: 2026-03-01
---

# Employment Contract Digital

Esta skill capacita o Claude Code a elaborar, revisar e gerenciar contratos de trabalho em formato digital, garantindo conformidade legal e otimização de processos.

---

## Keywords

Contrato de Trabalho Digital, Assinatura Eletrônica, LGPD Contrato, eSocial Compliance, Cláusulas Digitais, Jornada Remota, Termo Aditivo Digital, Validade Jurídica Digital, Gestão Eletrônica Contratual, e-HR, Onboarding Digital, Conformidade Trabalhista

---

## Quick Start

1.  Iniciar o assistente com `claude-code chat --skill employment-contract-digital` para acesso às funcionalidades.
2.  Solicitar a criação de um contrato CLT para "Analista de Suporte Júnior - Híbrido", informando salário de R$ 3.200,00 e benefícios padrão.
3.  Revisar automaticamente as cláusulas de confidencialidade e proteção de dados para adequação à Lei Geral de Proteção de Dados (LGPD).
4.  Gerar o documento final em formato PDF para ser enviado para assinatura eletrônica via plataforma certificada (ex: DocuSign, Clicksign).
5.  Validar a conformidade das informações contratuais com as diretrizes de envio do eSocial para o evento S-2200 (Admissão).

---

## Core Workflows

### Workflow 1: Elaboração de Contrato de Trabalho CLT para Posição Híbrida/Remota com Cláusulas Digitais Específicas

Este workflow detalha a criação de um contrato de trabalho para um novo colaborador em regime híbrido ou remoto, incorporando as particularidades jurídicas e tecnológicas.

*   **Passo 1: Coleta e Estruturação de Dados Essenciais**
    *   **Ação**: Reunir todos os dados do empregado e da posição para a qual ele será contratado.
    *   **Dados Mínimos**:
        *   **Empregado**: Nome completo, CPF, RG, Endereço completo, Data de Nascimento, número da CTPS digital, PIS/PASEP.
        *   **Cargo**: Desenvolvedor Full Stack Sênior
        *   **Salário**: R$ 12.000,00 mensais
        *   **Modalidade**: Híbrida (3 dias escritório, 2 dias remoto)
        *   **Benefícios**: Plano de saúde Unimed Nacional, Vale-Refeição R$ 35,00/dia, Auxílio Home Office R$ 150,00/mês, Vale-Transporte (se aplicável aos dias presenciais).
        *   **Empresa**: Razão Social "InovaTech Soluções Digitais S.A.", CNPJ 12.345.678/0001-90, Endereço "Av. Paulista, 1000, 15º andar, São Paulo/SP".
    *   **Exemplo de Comando**: `claude-code create contract --type CLT --employee-data {json_data} --company-data {json_data} --position "Desenvolvedor Full Stack Sênior" --salary 12000 --modality Hibrida --benefits "Plano Saude, VR 35, Auxilio Home Office 150"`

*   **Passo 2: Geração da Estrutura Base do Contrato**
    *   **Ação**: Utilizar a skill para gerar a minuta padrão do contrato CLT com as informações fornecidas.
    *   **Exemplo de Saída Parcial**:
        ```markdown
        CONTRATO INDIVIDUAL DE TRABALHO
        Pelo presente instrumento particular de contrato individual de trabalho, de um lado, INOVATECH SOLUÇÕES DIGITAIS S.A., pessoa jurídica de direito privado, inscrita no CNPJ sob o nº 12.345.678/0001-90, com sede na Av. Paulista, 1000, 15º andar, São Paulo/SP, doravante denominada EMPREGADORA, e de outro lado, [Nome Completo do Empregado], brasileiro(a), [Estado Civil], [Profissão], portador(a) do RG nº [Número], CPF nº [Número], CTPS nº [Número]/[Série], PIS nº [Número], residente e domiciliado(a) na [Endereço Completo], doravante denominado(a) EMPREGADO(A), têm entre si justo e contratado o presente, mediante as cláusulas e condições seguintes:
        CLÁUSULA PRIMEIRA – DO OBJETO
        O EMPREGADO será admitido na função de Desenvolvedor Full Stack Sênior, para desempenhar as atividades inerentes ao cargo, de acordo com as diretrizes da EMPREGADORA.
        CLÁUSULA SEGUNDA – DA REMUNERAÇÃO E BENEFÍCIOS
        O EMPREGADO receberá o salário mensal de R$ 12.000,00 (doze mil reais), a ser pago até o 5º dia útil do mês subsequente ao vencido. Além do salário, fará jus aos seguintes benefícios: Plano de Saúde Unimed Nacional, Vale-Refeição de R$ 35,00 (trinta e cinco reais) por dia útil trabalhado e Auxílio Home Office de R$ 150,00 (cento e cinquenta reais) mensais.
        ```

*   **Passo 3: Inserção de Cláusulas Específicas para Modalidade Híbrida/Remota e Conformidade LGPD**
    *   **Ação**: Adicionar cláusulas detalhadas para reger o regime de trabalho e a proteção de dados.
    *   **Exemplo de Cláusula de Teletrabalho/Híbrido**: "Cláusula 7ª – Do Regime de Trabalho Híbrido: O Empregado exercerá suas atividades laborais predominantemente na modalidade híbrida, com 3 (três) dias de trabalho presencial na sede da Empregadora (Av. Paulista, 1000, São Paulo/SP) e 2 (dois) dias de trabalho remoto, podendo este regime ser alterado mediante prévia comunicação de 15 (quinze) dias, conforme o interesse da Empregadora e a necessidade do serviço. As despesas com internet e energia elétrica para o desempenho das atividades remotas são de responsabilidade do Empregado, sendo-lhe concedido o auxílio home office mensal de R$ 150,00 (cento e cinquenta reais) para custear parte destas despesas. A Empregadora fornecerá os equipamentos necessários (notebook, monitor) para o desempenho das atividades remotas, os quais deverão ser utilizados exclusivamente para fins profissionais e devolvidos ao término do contrato."
    *   **Exemplo de Cláusula de Proteção de Dados (LGPD)**: "Cláusula 10ª – Da Proteção de Dados e Confidencialidade: O Empregado se compromete a tratar todos os dados pessoais e informações confidenciais da Empregadora e de seus clientes em estrita conformidade com a Lei Geral de Proteção de Dados (Lei nº 13.709/2018) e a Política de Segurança da Informação da empresa, a qual declara ter lido e compreendido e que está disponível no portal interno. O Empregado consente com o tratamento de seus dados pessoais, incluindo os sensíveis (se aplicável), estritamente para fins de gestão de pessoal, cumprimento de obrigações legais e contratuais. É vedado ao Empregado, sob pena de responsabilidade civil e criminal, divulgar, reproduzir ou utilizar para fins diversos do trabalho qualquer informação sigilosa obtida em razão do contrato de trabalho."

*   **Passo 4: Geração de Termo de Ciência e Responsabilidade de Assinatura Eletrônica**
    *   **Ação**: Criar um adendo ou cláusula final que formalize a aceitação da assinatura eletrônica.
    *   **Exemplo de Comando**: `claude-code generate document --type "Termo de Ciencia Assinatura Eletronica" --contract-id 987654`
    *   **Exemplo de Texto Gerado**: "As partes, Empregador e Empregado, declaram-se cientes e concordam que o presente contrato de trabalho e seus eventuais aditivos, bem como demais documentos relacionados à relação de emprego, serão formalizados por meio de assinatura eletrônica, em conformidade com o disposto na Medida Provisória nº 2.200-2/2001 e na Lei nº 14.063/2020, possuindo plena validade jurídica e força probatória."

### Workflow 2: Revisão de Contrato Existente para Conformidade com Novas Legislações (LGPD) e eSocial

Este workflow foca na atualização de contratos antigos para garantir a conformidade com a LGPD e a correta alimentação dos eventos do eSocial, minimizando riscos trabalhistas.

*   **Passo 1: Carregamento do Contrato Existente para Análise**
    *   **Ação**: Importar um contrato de trabalho previamente digitalizado para que a skill possa analisá-lo.
    *   **Input**: Arquivo `.docx` ou `.pdf` de um contrato de trabalho de 2018 (anterior à LGPD).
    *   **Exemplo de Comando**: `claude-code load contract --path "contrato_antigo_fernanda_costa.docx" --contract-id FC321`

*   **Passo 2: Análise de Conformidade LGPD**
    *   **Ação**: Solicitar à skill a identificação de lacunas e sugestões de adaptação às exigências da LGPD.
    *   **Exemplo de Comando**: `claude-code analyze contract --for LGPD --contract-id FC321`
    *   **Saída Esperada (Sugestões)**:
        *   **Identificação**: Ausência de cláusula explícita sobre finalidade e base legal do tratamento de dados pessoais.
        *   **Sugestão**: Adicionar cláusula que detalhe a coleta, armazenamento e uso de dados do empregado (CPF, RG, endereço, dados bancários, etc.) para fins de execução do contrato de trabalho, cumprimento de obrigações legais (fiscais, previdenciárias) e gestão de RH, citando a LGPD. Incluir referência à Política de Privacidade da empresa.
        *   **Identificação**: Falta de menção sobre dados sensíveis (se houver).
        *   **Sugestão**: Se dados sensíveis (ex: atestados médicos) forem coletados, especificar base legal (ex: cumprimento de obrigação legal ou regulatória) e garantir que o tratamento seja estritamente necessário e limitado.

*   **Passo 3: Verificação de Impacto eSocial**
    *   **Ação**: Analisar se as informações presentes no contrato estão alinhadas com os requisitos dos eventos do eSocial, especialmente S-2200 (Admissão) e S-2206 (Alteração Contratual).
    *   **Exemplo de Comando**: `claude-code check compliance --for eSocial --contract-id FC321`
    *   **Saída Esperada (Alerta)**:
        *   **Alerta**: A jornada de trabalho especificada como "horário comercial" é muito vaga para o eSocial.
        *   **Recomendação**: Revisar para "Jornada de 44 (quarenta e quatro) horas semanais, de segunda a sexta-feira, das 09h00 às 18h00, com 1 (uma) hora de intervalo para refeição e descanso." Isso se alinha com o campo `codJornada` e `dscJornada` do evento S-2200.
        *   **Alerta**: Benefícios não detalhados individualmente.
        *   **Recomendação**: Discriminar Vale-Transporte, Vale-Refeição, Plano de Saúde com seus respectivos valores ou condições, para correta informação nos eventos S-2200/S-2206, evitando divergências.

*   **Passo 4: Geração de Termo Aditivo para Atualização**
    *   **Ação**: Com base nas análises, gerar um termo aditivo que incorpore as novas cláusulas e atualizações necessárias.
    *   **Exemplo de Comando**: `claude-code generate addendum --contract-id FC321 --updates LGPD_eSocial`
    *   **Exemplo de Saída Parcial (Termo Aditivo)**:
        ```markdown
        TERMO ADITIVO AO CONTRATO INDIVIDUAL DE TRABALHO
        Pelo presente instrumento particular de Termo Aditivo ao Contrato Individual de Trabalho celebrado em 01/03/2018, de um lado, INOVATECH SOLUÇÕES DIGITAIS S.A. e de outro lado, FERNANDA COSTA, as partes resolvem aditar o contrato original nas seguintes condições:
        CLÁUSULA PRIMEIRA – DA ADEQUAÇÃO À LGPD
        Fica incluída a Cláusula Décima Primeira – Da Proteção de Dados Pessoais, com a seguinte redação: "O Empregado [...]".
        CLÁUSULA SEGUNDA – DA JORNADA DE TRABALHO
        A Cláusula Terceira – Da Jornada de Trabalho passa a ter a seguinte redação: "A jornada de trabalho do Empregado será de 44 (quarenta e quatro) horas semanais, de segunda a sexta-feira, das 09h00 às 18h00, com 1 (uma) hora de intervalo para refeição e descanso."
        ```

*   **Passo 5: Validação Jurídica e Preparação para Assinatura Digital**
    *   **Ação**: Realizar uma revisão final da skill para coesão, clareza e preparar o documento para a assinatura digital, indicando os campos específicos para rubrica eletrônica.
    *   **Exemplo de Comando**: `claude-code validate and prepare for signature --document-id ADITIVO_FC321`

---

## Templates

### Termo Aditivo de Contrato de Trabalho – Adequação LGPD e Teletrabalho

```markdown
TERMO ADITIVO AO CONTRATO INDIVIDUAL DE TRABALHO – ADEQUAÇÃO LGPD E TELETRABALHO

Pelo presente instrumento particular de Termo Aditivo ao Contrato Individual de Trabalho celebrado em 05 de janeiro de 2020, de um lado, **TECH SOLUTIONS LTDA.**, pessoa jurídica de direito privado, inscrita no CNPJ sob o nº 00.111.222/0001-33, com sede na Rua da Inovação, 123, Centro, São Paulo/SP, CEP 01000-000, neste ato representada por seu sócio administrador, Sr. [Nome do Sócio], doravante denominada **EMPREGADORA**, e de outro lado, **MARIA SILVA**, brasileira, solteira, Analista de Sistemas, portadora do RG nº 12.345.678-9 SSP/SP, CPF nº 987.654.321-00, CTPS nº 000111/SP, residente e domiciliada na Rua das Flores, 456, Apto. 101, Bairro Jardim, Campinas/SP, CEP 13000-000, doravante denominada **EMPREGADA**, têm entre si, justo e contratado o presente aditivo, mediante as cláusulas e condições seguintes:

**CLÁUSULA PRIMEIRA – DO OBJETO DO ADITIVO**
O presente Termo Aditivo tem por objetivo adequar o contrato de trabalho original da EMPREGADA às disposições da Lei Geral de Proteção de Dados Pessoais (Lei nº 13.709/2018 – LGPD) e formalizar a transição para o regime de teletrabalho/híbrido.

**CLÁUSULA SEGUNDA – DA PROTEÇÃO DE DADOS PESSOAIS (LGPD)**
Fica incluída no contrato original a Cláusula Décima – Da Proteção de Dados Pessoais, com a seguinte redação:
"**Cláusula Décima – Da Proteção de Dados Pessoais:** A EMPREGADA, por este ato, consente com o tratamento de seus dados pessoais, incluindo os dados pessoais sensíveis (se aplicáveis), pela EMPREGADORA, estritamente para as seguintes finalidades: a) execução do contrato de trabalho e gestão de recursos humanos; b) cumprimento de obrigações legais e regulatórias (previdenciárias, fiscais, trabalhistas, etc.); c) oferta e gestão de benefícios (plano de saúde, vale-refeição, etc.); d) segurança do trabalho e medicina ocupacional. A EMPREGADORA compromete-se a tratar os dados pessoais da EMPREGADA em conformidade com a Lei nº 13.709/2018 (LGPD) e sua Política de Privacidade e Proteção de Dados, disponível para consulta no portal interno da empresa, garantindo a segurança e confidencialidade das informações. A EMPREGADA declara ter lido e compreendido a referida política."

**CLÁUSULA TERCEIRA – DO REGIME DE TELETRABALHO/HÍBRIDO**
Fica alterada a Cláusula Terceira – Da Jornada de Trabalho, que passa a ter a seguinte redação e que define o regime de teletrabalho para a EMPREGADA:
"**Cláusula Terceira – Do Regime de Teletrabalho/Híbrido:** A EMPREGADA exercerá suas atividades laborais na modalidade de teletrabalho (home office), de forma preponderante, em sua residência na Rua das Flores, 456, Apto. 101, Bairro Jardim, Campinas/SP, com a possibilidade de comparecimento presencial na sede da EMPREGADORA (Rua da Inovação, 123, São Paulo/SP) em até 2 (dois) dias por semana, mediante prévio agendamento ou convocação com antecedência mínima de 48 (quarenta e oito) horas, conforme necessidade do serviço. As despesas de infraestrutura para o teletrabalho (internet, energia elétrica) são de responsabilidade da EMPREGADA, sendo-lhe concedido um auxílio mensal de R$ 150,00 (cento e cinquenta reais)