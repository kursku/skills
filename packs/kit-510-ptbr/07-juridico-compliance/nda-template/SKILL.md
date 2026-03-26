---
name: nda-template
description: "Nda Template — Skill especializada para nda template"
license: MIT
metadata:
  version: 1.0.0
  author: Cafe Code AI
  category: 07-juridico-compliance
  updated: 2026-03-01
risk: critical
---

# Nda Template

Esta skill capacita o Claude a elaborar, revisar e gerenciar acordos de não divulgação (NDA) com conformidade legal e clareza contratual.

---

## Keywords

Acordo de confidencialidade, segredo comercial, informações proprietárias, não divulgação, cláusulas de sigilo, vigência de NDA, jurisdição em contratos, quebra de contrato, proteção de dados, due diligence, non-compete, non-solicitation.

---

## Quick Start

1.  **Identifique as Partes**: Nome completo e qualificação (CNPJ, endereço) da Parte Divulgadora e da Parte Receptora.
2.  **Liste as Informações Essenciais**: Enumere os tipos de informações a serem protegidas (ex: dados financeiros, P&D, listas de clientes, estratégias).
3.  **Defina o Propósito da Divulgação**: Especifique o motivo pelo qual as informações serão compartilhadas (ex: avaliação de investimento, negociação de parceria, desenvolvimento de projeto).
4.  **Determine a Vigência do Sigilo**: Estabeleça o período em que a confidencialidade deve ser mantida (ex: 5 anos a partir da data de assinatura).
5.  **Selecione a Jurisdição Aplicável**: Escolha o foro e a lei que regerão o contrato para resolução de disputas (ex: Comarca de São Paulo, Estado de São Paulo, Brasil).

---

## Core Workflows

### Workflow 1: Elaboração de NDA Unilateral para Prospecção de Investimento

Este workflow detalha a criação de um NDA onde uma única parte (a startup) está divulgando informações confidenciais para potenciais investidores.

1.  **Coleta de Dados das Partes**:
    *   **Divulgadora**: Obter razão social completa, CNPJ, endereço da sede, nome e cargo do representante legal da startup. Ex: "Startup Inovadora Ltda., CNPJ 00.000.000/0001-00, com sede na Av. Paulista, 1000, São Paulo/SP, representada por seu Diretor Presidente, [Nome do Diretor]".
    *   **Receptora**: Obter razão social completa, CNPJ, endereço da sede, nome e cargo do representante legal do fundo de investimento ou investidor anjo. Ex: "Fundo Capital Ventures S.A., CNPJ 11.111.111/0001-11, com sede na Rua Faria Lima, 2000, São Paulo/SP, representada por seu Diretor de Investimentos, [Nome do Diretor]".

2.  **Definição das "Informações Confidenciais"**:
    *   Listar explicitamente o que constitui informação confidencial para a startup.
    *   **Exemplo**: "Informações Confidenciais incluem, mas não se limitam a: planos de negócios, projeções financeiras, modelos de precificação, listas de clientes e prospects, propriedade intelectual (patentes pendentes, segredos de software), resultados de pesquisa e desenvolvimento, estratégias de marketing, dados de valuation, termos de captação anteriores, e quaisquer outras informações, técnicas ou comerciais, marcadas como confidenciais ou que, pela sua natureza, deveriam ser consideradas confidenciais."

3.  **Especificação do Propósito da Divulgação**:
    *   Clarificar o motivo exato pelo qual as informações estão sendo compartilhadas.
    *   **Exemplo**: "O propósito da divulgação das Informações Confidenciais é exclusivamente para a Parte Receptora avaliar uma potencial oportunidade de investimento na Parte Divulgadora ('Propósito Permitido')."

4.  **Estabelecimento de Obrigações de Confidencialidade**:
    *   Detalhar como a Parte Receptora deve proteger as informações.
    *   **Exemplo**: "A Parte Receptora compromete-se a: (a) manter as Informações Confidenciais em sigilo absoluto; (b) não utilizar as Informações Confidenciais para qualquer outro fim que não o Propósito Permitido; (c) limitar o acesso às Informações Confidenciais apenas aos seus diretores, funcionários e consultores que necessitem conhecê-las para o Propósito Permitido e que estejam vinculados a obrigações de confidencialidade de escopo similar ou mais restritivo."

5.  **Definição da Vigência e Exceções**:
    *   Determinar o período de sigilo e as condições sob as quais as informações não são mais consideradas confidenciais.
    *   **Exemplo de Vigência**: "As obrigações de confidencialidade estabelecidas neste Acordo terão vigência de 5 (cinco) anos a partir da Data de Assinatura."
    *   **Exemplo de Exceções**: "As obrigações de confidencialidade não se aplicarão a informações que: (a) eram de conhecimento público antes da divulgação; (b) tornaram-se públicas sem violação deste Acordo; (c) foram recebidas de terceiros sem violação de obrigação de confidencialidade; (d) foram desenvolvidas independentemente pela Parte Receptora."

6.  **Cláusulas de Retorno/Destruição e Não Solicitação**:
    *   Garantir a devolução ou eliminação das informações após o término do propósito.
    *   **Exemplo de Retorno/Destruição**: "Após a conclusão do Propósito Permitido ou a pedido da Parte Divulgadora, a Parte Receptora deverá, imediatamente, devolver ou destruir todas as Informações Confidenciais, incluindo cópias, e certificar tal ato por escrito."
    *   **Exemplo de Não Solicitação (Opcional)**: "Durante a vigência deste Acordo e por mais 1 (um) ano após, a Parte Receptora compromete-se a não solicitar, direta ou indiretamente, a contratação de quaisquer funcionários ou colaboradores da Parte Divulgadora com quem tenha tido contato em virtude deste Acordo."

7.  **LGPD/GDPR e Conformidade**:
    *   Se o NDA envolver dados pessoais, incluir cláusulas de conformidade.
    *   **Exemplo**: "As Partes reconhecem que, na medida em que dados pessoais sejam compartilhados sob este Acordo, estes serão tratados em conformidade com a Lei Geral de Proteção de Dados (Lei nº 13.709/2018) e o Regulamento Geral de Proteção de Dados da União Europeia (GDPR), quando aplicável. A Parte Receptora atuará como operadora de dados, tratando-os apenas para o Propósito Permitido e sob as instruções da Parte Divulgadora."

### Workflow 2: Revisão e Adaptação de NDA Bilateral para Parceria Estratégica

Este workflow foca na análise de um NDA onde ambas as partes divulgam e recebem informações, comum em joint ventures ou projetos colaborativos.

1.  **Análise da Definição de "Informações Confidenciais"**:
    *   Verificar se a definição é equilibrada e abrange adequadamente as informações de ambas as partes.
    *   **Ação**: Confirmar que a linguagem é neutra e protege igualmente os ativos de ambas as empresas. Ex: "Informações Confidenciais significam quaisquer informações proprietárias ou confidenciais, técnicas, comerciais, financeiras, de marketing, operacionais, estratégicas, dados de clientes, propriedade intelectual, segredos de negócio, planos de desenvolvimento, know-how, software, códigos-fonte, algoritmos, ou outros dados e materiais, divulgados por uma Parte ('Parte Divulgadora') à outra Parte ('Parte Receptora') para o 'Propósito Permitido'."

2.  **Avaliação do Propósito da Divulgação**:
    *   Garantir que o propósito seja mutuamente benéfico e específico para a parceria.
    *   **Ação**: Assegurar que o Propósito Permitido reflita o escopo da parceria e não permita uso indevido. Ex: "O propósito da divulgação das Informações Confidenciais é a avaliação e execução de uma potencial parceria estratégica para o desenvolvimento conjunto de [Nome do Projeto/Produto]."

3.  **Revisão das Obrigações de Confidencialidade e Uso**:
    *   Verificar se as obrigações são recíprocas e claras para ambas as partes.
    *   **Ação**: Confirmar que as restrições de uso e acesso são as mesmas para ambas as Partes Receptoras. Ex: "Cada Parte Receptora se compromete a usar as Informações Confidenciais da Parte Divulgadora estritamente para o Propósito Permitido e a não reproduzir, distribuir, vender, licenciar, sublicenciar ou divulgar tais informações a terceiros sem prévia autorização escrita da Parte Divulgadora."

4.  **Análise dos Prazos de Vigência e Exceções**:
    *   Verificar se os períodos de sigilo são razoáveis e se as exceções se aplicam equitativamente.
    *   **Ação**: Comparar a vigência proposta (ex: 3 anos) com a duração esperada do projeto e o ciclo de vida das informações. Certificar que as exceções (informações públicas, desenvolvidas independentemente) são claras.

5.  **Cláusulas de Não Concorrência ou Não Solicitação (se aplicável)**:
    *   Se houver, analisar a razoabilidade e legalidade de cláusulas adicionais que restringem a atuação das partes.
    *   **Ação**: Avaliar o escopo geográfico, temporal e material dessas cláusulas. **Exemplo de Não Solicitação**: "Durante a vigência deste Acordo e por um período de 12 (doze) meses após seu término, nenhuma Parte poderá, direta ou indiretamente, solicitar ou contratar funcionários da outra Parte que tenham tido acesso às Informações Confidenciais da Parte Divulgadora no âmbito deste Acordo."

6.  **Cláusulas de Indenização e Medidas Corretivas**:
    *   Garantir que haja mecanismos claros para lidar com a quebra do acordo.
    *   **Ação**: Verificar a existência de previsão para medidas cautelares (liminares) e indenização por perdas e danos. Ex: "As Partes reconhecem que a quebra das obrigações de confidencialidade pode causar danos irreparáveis e concordam que a Parte Divulgadora terá direito a buscar medidas liminares, além de quaisquer outros recursos legais ou equitativos, incluindo indenização por perdas e danos."

---

## Templates

### NDA Unilateral Simplificado (Exemplo Completo)

```markdown
**ACORDO DE CONFIDENCIALIDADE UNILATERAL**

Pelo presente instrumento particular, de um lado:

**PARTE DIVULGADORA:**
**[NOME COMPLETO DA EMPRESA DIVULGADORA]**, sociedade limitada, inscrita no CNPJ sob o nº [00.000.000/0001-00], com sede na [ENDEREÇO COMPLETO DA EMPRESA DIVULGADORA, incluindo cidade e estado], neste ato representada por seu [CARGO], [NOME DO REPRESENTANTE LEGAL], [NACIONALIDADE], [ESTADO CIVIL], [PROFISSÃO], portador(a) do RG nº [00.000.000-0] e CPF nº [000.000.000-00].

E de outro lado:

**PARTE RECEPTORA:**
**[NOME COMPLETO DA EMPRESA RECEPTORA]**, sociedade limitada, inscrita no CNPJ sob o nº [11.111.111/0001-11], com sede na [ENDEREÇO COMPLETO DA EMPRESA RECEPTORA, incluindo cidade e estado], neste ato representada por seu [CARGO], [NOME DO REPRESENTANTE LEGAL], [NACIONALIDADE], [ESTADO CIVIL], [PROFISSÃO], portador(a) do RG nº [11.111.111-1] e CPF nº [111.111.111-11].

As Partes acima identificadas, doravante denominadas individualmente como "Parte" e conjuntamente como "Partes", celebram o presente Acordo de Confidencialidade ("Acordo"), que se regerá pelas cláusulas e condições seguintes:

**CLÁUSULA PRIMEIRA – DO OBJETO E PROPÓSITO**
1.1. O presente Acordo tem como objeto proteger as informações confidenciais da Parte Divulgadora que serão compartilhadas com a Parte Receptora.
1.2. O propósito da divulgação e o uso das Informações Confidenciais pela Parte Receptora são exclusivamente para a avaliação de uma potencial oportunidade de **investimento em tecnologia na Parte Divulgadora** ("Propósito Permitido").

**CLÁUSULA SEGUNDA – DAS INFORMAÇÕES CONFIDENCIAIS**
2.1. Para os fins deste Acordo, "Informações Confidenciais" significam quaisquer informações, dados, documentos, materiais, ideias, conceitos, know-how, segredos de negócio, planos de negócio, projeções financeiras, estratégias de marketing, listas de clientes, informações técnicas, protótipos, softwares, códigos-fonte, invenções, processos, fórmulas, dados de pesquisa e desenvolvimento, bem como quaisquer outras informações de natureza proprietária ou confidencial, sejam elas divulgadas de forma escrita, oral, visual, eletrônica ou por qualquer outro meio, antes ou após a data de assinatura deste Acordo, e que sejam relacionadas à Parte Divulgadora.
2.2. As Informações Confidenciais incluem, mas não se limitam a, aquelas marcadas como "Confidencial" ou que, pela sua natureza, deveriam ser razoavelmente consideradas confidenciais.

**CLÁUSULA TERCEIRA – DAS OBRIGAÇÕES DA PARTE RECEPTORA**
3.1. A Parte Receptora compromete-se a:
    a) Manter as Informações Confidenciais em sigilo absoluto, não as divulgando a terceiros.
    b) Utilizar as Informações Confidenciais exclusivamente para o Propósito Permitido.
    c) Limitar o acesso às Informações Confidenciais apenas aos seus diretores, funcionários e consultores que necessitem conhecê-las para o Propósito Permitido e que estejam vinculados a obrigações de confidencialidade de escopo similar ou mais restritivo.
    d) Empregar o mesmo grau de cuidado que utiliza para proteger suas próprias informações confidenciais, mas nunca inferior a um grau razoável de cuidado.

**CLÁUSULA QUARTA – DAS EXCEÇÕES À CONFIDENCIALIDADE**
4.1. As obrigações de confidencialidade estabelecidas neste Acordo não se aplicarão a informações que a Parte Receptora possa comprovar, por meio de prova documental:
    a) Já eram de domínio público antes da sua divulgação pela Parte Divulgadora;
    b) Tornaram-se de domínio público sem violação deste Acordo pela Parte Receptora;
    c) Foram legitimamente recebidas de terceiros sem violação de qualquer obrigação de confidencialidade;
    d) Foram desenvolvidas independentemente pela Parte Receptora sem o uso das Informações Confidenciais da Parte Divulgadora;
    e) Devam ser divulgadas por força de lei, ordem judicial ou regulatória, mediante prévia notificação à Parte Divulgadora, quando legalmente permitido.

**CLÁUSULA QUINTA – DA VIGÊNCIA**
5.1. Este Acordo entrará em vigor na data de sua assinatura pelas Partes e as obrigações de confidencialidade permanecerão válidas por um período de **5 (cinco) anos** a contar da referida data.

**CLÁUSULA SEXTA – DA DEVOLUÇÃO OU DESTRUIÇÃO**
6.1. Após a conclusão do Propósito Permitido ou a pedido da Parte Divulgadora, a Parte Receptora deverá, imediatamente, devolver ou destruir todas as Informações Confidenciais recebidas, incluindo cópias, notas e resumos, e certificar tal ato por escrito à Parte Divulgadora, no prazo de 10 (dez) dias úteis a contar do pedido.

**CLÁUSULA SÉTIMA – DA PROPRIEDADE INTELECTUAL**
7.1. Todas as Informações Confidenciais e os direitos de propriedade intelectual a elas inerentes permanecerão sendo de propriedade exclusiva da Parte Divulgadora. Nenhuma licença ou direito é concedido ou implícito por este Acordo.

**CLÁUSULA OITAVA – DA INDENIZAÇÃO**
8.1. A Parte Receptora será responsável por indenizar a Parte Divulgadora por quaisquer perdas, danos, custos e despesas (incluindo honorários advocatícios) decorrentes da violação das obrigações de confidencialidade previstas neste Acordo.

**CLÁUSULA NONA – DA LGPD**
9.1. As Partes reconhecem que, na medida em que dados pessoais sejam compartilhados sob este Acordo, estes serão tratados em conformidade com a Lei Geral de Proteção de Dados (Lei nº 13.709/2018). A Parte Receptora se compromete a tratar tais dados pessoais apenas para o Propósito Permitido e sob as instruções da Parte Divulgadora.

**CLÁUSULA DÉCIMA – DO FORO**
10.1. As Partes elegem o foro da Comarca de **São Paulo, Estado de São Paulo**, Brasil, para dirimir quaisquer dúvidas ou litígios decorrentes deste Acordo, com renúncia expressa a qualquer outro, por mais privilegiado que seja.

E, por estarem assim justas e contratadas, as Partes assinam o presente Acordo em 2 (duas) vias de igual teor e forma, na presença das duas testemunhas abaixo, para que produza seus efeitos legais.

[CIDADE], [DIA] de [MÊS] de [ANO].

---

**PARTE DIVULGADORA**
[Assinatura do Representante Legal]
[Nome do Representante Legal]
[Cargo]

---

**PARTE RECEPTORA**
[Assinatura do Representante Legal]
[Nome do Representante Legal]
[Cargo]

---

**TESTEMUNHAS:**

1. ____________________________
   Nome: [Nome da Testemunha 1]
   CPF: [000.000.000-00]

2. ____________________________
   Nome: [Nome da Testemunha 2]
   CPF: [000.000.000-00]
```

### Cláusula de Vigência Detalhada e Retorno/Destruição

```markdown
**CLÁUSULA QUINTA – DA VIGÊNCIA E DO TÉRMINO DAS OBRIGAÇÕES**
5.1. Este Acordo entrará em vigor na Data de Assinatura e permanecerá válido até que o Propósito Permitido seja alcançado ou descontinuado.
5.2. Não obstante o término do Acordo principal, as obrigações de confidencialidade da Parte Receptora relativas às Informações Confidenciais terão uma vigência independente de 7 (sete) anos a partir da data de cada divulgação específica das Informações Confidenciais.
5.3. As obrigações de confidencialidade relacionadas a segredos de negócio que, por sua natureza, não se tornam de domínio público (ex: algoritmos proprietários não patenteados, listas de clientes estratégicas) permanecerão em vigor por tempo indeterminado, enquanto tais informações mantiverem seu status de segredo de negócio.

**CLÁUSULA SEXTA – DO RETORNO E DESTRUIÇÃO DAS INFORMAÇÕES**
6.1. No término da vigência deste Acordo, ou a qualquer momento mediante solicitação por escrito da Parte Divulgadora, a Parte Receptora deverá, no prazo máximo de 15 (quinze) dias úteis:
    a) Devolver à Parte Divulgadora todos os documentos, materiais e mídias contendo Informações Confidenciais, bem como todas as cópias, anotações, resumos, extratos ou reproduções de qualquer forma; ou
    b) Destruir, de forma segura e irrecuperável, todas as Informações Confidenciais em seu poder, incluindo dados eletrônicos e cópias em qualquer formato, e certificar por escrito a Parte Divulgadora sobre a completa destruição, mediante declaração assinada por um representante legal.
6.2. A Parte Receptora poderá reter uma cópia de cada Informação Confidencial para fins de conformidade com exigências legais ou regulatórias, desde que tal retenção seja comunicada à Parte Divulgadora e que as cópias retidas permaneçam sujeitas às obrigações de confidencialidade deste Acordo.
```

---

## Checklist

- [x] Confirmação da identificação completa e correta de todas as partes (razão social, CNPJ, endereço, representantes).
- [x] Definição clara e abrangente de "Informações Confidenciais", incluindo exemplos específicos do domínio.
- [x] Especificação inequívoca do "Propósito Permitido" para a divulgação das informações.
- [x] Estabelecimento do prazo de vigência das obrigações de confidencialidade (ex: 5 anos, vitalício para segredos comerciais).
- [x] Inclusão de cláusulas de exceção à confidencialidade (ex: informações públicas, recebidas de terceiros).
- [x] Previsão para o retorno ou destruição das Informações Confidenciais ao término do acordo ou a pedido.
- [x] Eleição de foro e lei aplicável para resolução de disputas (ex: Comarca de São Paulo).
- [x] Cláusula de indenização por perdas e danos em caso de quebra do acordo.
- [x] Verificação da conformidade com a Lei Geral de Proteção de Dados (LGPD), se houver tratamento de dados pessoais.
- [x] Inclusão de cláusula de não solicitação de funcionários ou não concorrência, se pertinente ao escopo.

---

## Métricas de Referência

| Métrica                                | Benchmark              | Meta                   |
|:---------------------------------------|:-----------------------|:-----------------------|
| Tempo médio de negociação de NDA       | 5 dias úteis           | 3 dias úteis           |
| Taxa de conformidade em cláusulas LGPD | 95%                    | 100%                   |
| Nível de clareza da definição de IC*   | 4.0 (escala 1-5)       | 4.5                    |
| Incidência de quebras de NDA           | < 1% ao ano            | 0%                     |
| Percentual de NDAs arquivados digitalmente | 90%                    | 100%                   |
| Avaliação jurídica externa do modelo NDA | "Bom" ou superior      | "Excelente"            |

*IC = Informações Confidenciais

---

## Erros Comuns

1.  **Definição vaga de "Informações Confidenciais"**: Isso pode levar a disputas sobre o que deveria ser protegido.
    *   **Como evitar**: Inclua uma lista não exaustiva de tipos de informações (financeiras, técnicas, comerciais) e especifique que informações marcadas como confidenciais ou que, pela sua natureza, deveriam ser assim consideradas, estão incluídas. Ex: "Informações Confidenciais incluem, mas não se limitam a: planos estratégicos, dados de clientes, algoritmos de software e projeções financeiras, bem como quaisquer informações marcadas como 'Confidencial' ou que razoavelmente seriam consideradas confidenciais."

2.  **Não especificar o Propósito da Divulgação**: A ausência de um propósito claro permite o uso indevido das informações.
    *   **Como evitar**: Sempre defina o objetivo específico do compartilhamento. Ex: "O propósito da divulgação é exclusivamente para a análise de uma potencial fusão/aquisição entre as Partes, e para nenhum outro fim."

3.  **Prazos de vigência irrealistas ou ausentes**: Um NDA sem prazo ou com prazo inadequado pode ser ineficaz ou excessivamente oneroso.
    *   **Como evitar**: Estabeleça prazos razoáveis para a natureza das informações (ex: 5 anos para informações comerciais, indeterminado para segredos de negócio que não se tornam públicos) e inclua um mecanismo de prorrogação se necessário.

4.  **Ausência de cláusula de retorno/destruição de informações**: Sem essa cláusula, a Parte Receptora pode alegar ter o direito de manter as informações.
    *   **Como evitar**: Inclua uma cláusula explícita exigindo a devolução ou destruição de todas as cópias das Informações Confidenciais após o término do acordo ou a pedido. Ex: "Ao final da vigência do presente Acordo, ou a qualquer momento mediante solicitação da Parte Divulgadora, a Parte Receptora deverá destruir todas as Informações Confidenciais em seu poder e certificar a destruição por escrito."

5.  **Não considerar a LGPD/GDPR quando dados pessoais estão envolvidos**: A falha pode resultar em multas pesadas.
    *   **Como evitar**: Se o NDA envolve dados pessoais, inclua uma cláusula de conformidade com a LGPD (e GDPR, se aplicável), definindo os papéis (controlador/operador) e as obrigações de cada parte. Ex: "As Partes comprometem-se a tratar quaisquer dados pessoais compartilhados em estrita conformidade com a LGPD, garantindo a segurança e confidencialidade dos dados durante todo o processo."

---

## Dicas Avançadas

1.  **Uso de NDAs de "Curta Forma" para Triagem Inicial**: Para prospecções iniciais ou contatos preliminares onde o volume de informações confidenciais a ser divulgado é pequeno, utilize um NDA mais conciso e menos complexo. Isso agiliza o processo sem comprometer a proteção essencial. Ex: um NDA de uma página focando apenas na definição de IC, propósito e vigência de 1 ano.

2.  **Cláusula de "Standstill" em M&A**: Em negociações de fusões e aquisições, considere adicionar uma cláusula de "Standstill" ao NDA. Esta cláusula proíbe a Parte Receptora de adquirir ações da Parte Divulgadora sem consentimento, fazer ofertas públicas não solicitadas ou influenciar a gestão, protegendo a Divulgadora de "hostile takeovers" durante a due diligence.

3.  **Gerenciamento Centralizado de NDAs e Versionamento**: Implemente um sistema de gerenciamento de contratos (CLM) para armazenar todos os NDAs, controlar suas vigências, versões e partes envolvidas. Isso é crucial para empresas com alto volume de acordos e facilita auditorias e renovações. Ex: Utilizar softwares como DocuSign CLM ou Ironclad para rastrear status e datas de expiração.

4.  **Cláusulas de Auditoria e Conformidade Tecnológica**: Para NDAs envolvendo informações altamente sensíveis ou propriedade intelectual em desenvolvimento, inclua o direito da Parte Divulgadora de auditar os sistemas da Parte Receptora para verificar a conformidade com as obrigações de segurança e confidencialidade. Ex: "A Parte Divulgadora poderá, mediante aviso prévio razoável, auditar os sistemas e instalações da Parte Receptora para verificar o cumprimento das obrigações de proteção das Informações Confidenciais."

5.  **Considerar Leis Específicas de Segredo Comercial**: Além do NDA, esteja ciente das proteções legais para segredos comerciais (no Brasil, Lei de Propriedade Industrial, Lei nº 9.279/96). O NDA complementa, mas não substitui, as proteções intrínsecas a um segredo de negócio bem gerenciado. Certifique-se de que a empresa mantém as informações confidenciais com medidas de segurança adequadas para que possam ser consideradas segredo comercial sob a lei.