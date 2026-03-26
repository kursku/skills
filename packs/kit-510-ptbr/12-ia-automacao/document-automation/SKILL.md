---
name: document-automation
description: "Document Automation — Skill especializada para otimização de processos documentais"
license: MIT
metadata:
  version: 1.0.0
  author: Cafe Code AI
  category: 12-ia-automacao
  updated: 2026-03-01
risk: safe
---

# Document Automation

Esta skill capacita o Claude a projetar, implementar e otimizar soluções de automação de documentos usando IA, APIs e plataformas de low-code/no-code como Make e N8N.

---

## Keywords

`Automação de Documentos`, `Geração Dinâmica de Documentos`, `Extração Inteligente de Dados (IDP)`, `OCR`, `Processamento de Linguagem Natural (PLN)`, `Assinatura Eletrônica`, `Workflow de Documentos`, `RPA para Documentos`, `Gestão de Ciclo de Vida do Contrato (CLM)`, `APIs de Documentos`, `Make.com`, `N8N`, `Prompts para IA`, `Validação de Documentos`.

---

## Quick Start

1.  **Configurar um trigger de entrada de documentos**: Configure um webhook em Make.com (ou N8N) para receber dados de um formulário web (ex: Typeform, Google Forms) preenchido ou um novo arquivo em uma pasta monitorada (ex: Google Drive, Dropbox, e-mail).
2.  **Extrair e preparar dados-chave**: Utilize módulos de extração (ex: "Text Parser" em Make, "Function" em N8N) ou conectores de banco de dados (ex: Airtable, PostgreSQL) para coletar as informações necessárias que alimentarão o documento ou a extração.
3.  **Interagir com Claude para conteúdo/validação**: Envie os dados preparados para o Claude via API com um prompt detalhado, instruindo-o a gerar o corpo de um documento (ex: proposta, contrato) ou validar/normalizar dados extraídos.
4.  **Criar ou preencher o documento final**: Utilize o texto gerado pelo Claude (ou os dados validados) para preencher um template em um serviço como Google Docs API, DocuSign Gen, PandaDoc ou um gerador de PDF customizado.
5.  **Distribuir e arquivar de forma automatizada**: Envie o documento final para assinatura eletrônica (ex: DocuSign, Adobe Sign) e armazene-o automaticamente em um sistema de gestão documental (ex: SharePoint, Google Drive) ou CRM/ERP.

---

## Core Workflows

### Workflow 1: Automação de Geração de Propostas Comerciais Dinâmicas com Claude e Make.com

**Cenário**: Uma empresa de serviços de TI precisa gerar propostas comerciais personalizadas e detalhadas rapidamente para cada cliente, com base em dados do CRM e inputs específicos do vendedor.

**Passos detalhados**:

1.  **Trigger (Make.com)**: Um novo "Negócio" no estágio "Proposta Necessária" no HubSpot (ou outro CRM como Pipedrive, Salesforce) aciona um webhook do Make.com. O webhook recebe o `ID do Negócio`.
2.  **Coleta de Dados do CRM**:
    *   Módulo "HubSpot CRM - Get a Deal": Busca detalhes completos do negócio, incluindo `nome_cliente`, `cnpj_cliente`, `servicos_selecionados` (lista de IDs de serviços ou nomes), `valor_total_estimado`.
    *   Módulo "Google Sheets - Search Rows": Consulta uma planilha de "Catálogo de Serviços" para obter descrições detalhadas e preços unitários para cada `servico_selecionado`.
    *   Variáveis resultantes: `cliente_nome_fantasia`, `cliente_razao_social`, `cliente_cnpj`, `cliente_endereco`, `lista_de_servicos_detalhados` (com nome, descrição, preço).
3.  **Geração do Conteúdo da Proposta (Claude API)**:
    *   Módulo "HTTP - Make a request" no Make.com para a API do Claude (ex: `https://api.anthropic.com/v1/messages`).
    *   **Método**: `POST`
    *   **Headers**: `Content-Type: application/json`, `x-api-key: SEU_CLAUDE_API_KEY`, `anthropic-version: 2023-06-01`
    *   **Corpo (JSON)**:
        ```json
        {
          "model": "claude-3-opus-20240229",
          "max_tokens": 2000,
          "messages": [
            {
              "role": "user",
              "content": "Você é um redator de propostas comerciais persuasivo e formal para uma empresa de tecnologia focada em soluções de automação. Crie as seções 'Escopo dos Serviços', 'Investimento', 'Prazos de Entrega' e 'Condições Gerais' para uma proposta. Seja claro, conciso e destaque os benefícios para o cliente.\n\n**Dados do Cliente:**\nNome Fantasia: {{1.nome_fantasia}}\nRazão Social: {{1.razao_social}}\nCNPJ: {{1.cnpj}}\nEndereço: {{1.endereco}}\n\n**Serviços Selecionados e Detalhes:**\n{{2.lista_de_servicos_detalhados}} \n\n**Valor Total Estimado:** R$ {{1.valor_total_estimado}}\n\n**Instruções:**\n1. Comece com uma introdução calorosa e profissional, endereçando o cliente.\n2. Para 'Escopo dos Serviços', liste e descreva cada serviço selecionado, focando no valor que entrega.\n3. Para 'Investimento', apresente o valor total estimado e sugira condições de pagamento: 50% adiantado, 50% na conclusão da primeira fase.\n4. Para 'Prazos de Entrega', estime um prazo de 90 dias úteis para a implementação completa, com marcos de entrega para cada serviço.\n5. Para 'Condições Gerais', inclua uma cláusula padrão de confidencialidade e uma de validade da proposta de 30 dias.\n6. Termine com uma chamada para ação para agendamento da reunião de alinhamento."
            }
          ]
        }
        ```
    *   O Make.com capturará a resposta do Claude contendo o texto formatado da proposta.
4.  **Preenchimento do Template da Proposta (Google Docs API)**:
    *   Módulo "Google Docs - Create a Document from a Template": Usa um template pré-definido no Google Docs com placeholders como `{{NOME_CLIENTE}}`, `{{CONTEUDO_PROPOSTA}}`.
    *   O texto gerado pelo Claude preenche o placeholder `{{CONTEUDO_PROPOSTA}}`.
    *   O nome do cliente do CRM preenche `{{NOME_CLIENTE}}`.
5.  **Conversão para PDF e Assinatura Eletrônica**:
    *   Módulo "Google Docs - Convert a Document": Converte o documento preenchido para PDF.
    *   Módulo "DocuSign - Send an Envelope": Envia o PDF gerado para o e-mail do contato do cliente (extraído do CRM) e para o e-mail do gerente comercial para assinatura eletrônica.
    *   Configuração de um webhook de notificação do DocuSign para o Make.com para monitorar o status da assinatura.
6.  **Arquivamento e Notificação**:
    *   Módulo "Google Drive - Upload a File": Armazena a proposta final em PDF em uma pasta específica (ex: `/Propostas_Finalizadas/{{1.nome_cliente}}/`).
    *   Módulo "Slack - Create a Message": Notifica a equipe de vendas e o gerente comercial sobre o envio da proposta e seu status (ex: "Proposta para {{1.nome_cliente}} enviada para assinatura!").

### Workflow 2: Extração Inteligente de Dados de Notas Fiscais com N8N e Google Cloud Vision AI

**Cenário**: Uma equipe financeira recebe centenas de notas fiscais (NF-e) por e-mail mensalmente e precisa extrair dados como nome do fornecedor, CNPJ, valor total, data de emissão, data de vencimento e itens da fatura para registro no sistema ERP e conciliação.

**Passos detalhados**:

1.  **Trigger (N8N)**: "Email Read IMAP" node configurado para monitorar uma caixa de entrada específica (`faturas@suaempresa.com.br`) para novos e-mails com anexos PDF ou XML. Filtra por assunto que contenha "Nota Fiscal" ou "Fatura".
2.  **Armazenamento Temporário e Extração de Anexos**:
    *   "Split in Batches" node: Se houver múltiplos anexos, processa um por um.
    *   "Read Binary File" node: Lê o anexo PDF/XML.
    *   "Google Drive - Upload File" node: Faz upload do anexo para uma pasta temporária no Google Drive (`/NFE_Processamento/`).
3.  **Processamento OCR/IDP (Google Cloud Vision AI)**:
    *   "Google Cloud Vision - OCR Document" node: Configurado para processar o PDF do Google Drive.
    *   **Recursos**: `TEXT_DETECTION` para texto geral e `DOCUMENT_TEXT_DETECTION` para extração estruturada (se aplicável a layout de NF-e).
    *   **Saída**: JSON com o texto extraído e, em alguns casos, coordenadas de campos. Para NF-e no Brasil, o XML é preferível, mas o OCR é um fallback para PDFs não estruturados ou DANFEs.
4.  **Pré-processamento e Normalização de Dados (N8N Function Node)**:
    *   Um "Function" node em JavaScript para percorrer o JSON do Google Vision AI (ou o XML, se disponível), extrair campos específicos e aplicar regras de normalização.
    *   **Exemplo de código (simplificado para JSON de texto plano do OCR)**:
        ```javascript
        const visionOutput = $json.data.fullTextAnnotation.text;
        let extractedData = {
          fornecedor: '',
          cnpj_fornecedor: '',
          valor_total: 0,
          data_emissao: '',
          data_vencimento: ''
        };
        
        // Exemplo de regex para encontrar campos comuns
        const regexFornecedor = /(?:Razão Social|Nome Fornecedor):\s*(.+)/i;
        const regexCNPJ = /(?:\bCNPJ\b|\bCPF\b):\s*(\d{2}\.\d{3}\.\d{3}\/\d{4}-\d{2}|\d{3}\.\d{3}\.\d{3}-\d{2})/i;
        const regexValorTotal = /(?:Valor Total|Total a Pagar):\s*R\$\s*([\d\.,]+)/i;
        const regexDataEmissao = /(?:Data Emissão|Emitido Em):\s*(\d{2}\/\d{2}\/\d{4})/i;
        const regexDataVencimento = /(?:Data Vencimento|Vencimento Em):\s*(\d{2}\/\d{2}\/\d{4})/i;
        
        const lines = visionOutput.split('\n');
        for (const line of lines) {
          let match;
          if (!extractedData.fornecedor && (match = line.match(regexFornecedor))) {
            extractedData.fornecedor = match[1].trim();
          }
          if (!extractedData.cnpj_fornecedor && (match = line.match(regexCNPJ))) {
            extractedData.cnpj_fornecedor = match[1].trim();
          }
          if (!extractedData.valor_total && (match = line.match(regexValorTotal))) {
            extractedData.valor_total = parseFloat(match[1].replace(/\./g, '').replace(',', '.'));
          }
          if (!extractedData.data_emissao && (match = line.match(regexDataEmissao))) {
            extractedData.data_emissao = match[1].trim();
          }
          if (!extractedData.data_vencimento && (match = line.match(regexDataVencimento))) {
            extractedData.data_vencimento = match[1].trim();
          }
        }
        
        // Normalização de datas