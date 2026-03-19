---
name: rag-implementation
description: "Rag Implementation — Skill especializada para rag implementation"
license: MIT
metadata:
  version: 1.0.0
  author: Cafe Code AI
  category: 12-ia-automacao
  updated: 2026-03-01
---

# Rag Implementation

Capacita o Claude a projetar, implementar e otimizar sistemas de Retrieval Augmented Generation (RAG) em fluxos de trabalho de automação e chatbots, conectando LLMs a bases de conhecimento externas e atualizadas.

---

## Keywords

RAG, Vector Database, Embeddings, Chunking, Retrieval, Generation, LLM Integration, Semantic Search, Context Window, Pinecone, ChromaDB, Weaviate, LangChain, LlamaIndex, Prompt Engineering, N8N, Make.com, API.

---

## Quick Start

1.  **Escolha e Configure o Banco de Dados Vetorial**: Selecione um provedor como ChromaDB (local/auto-hospedado) ou Pinecone (nuvem).
2.  **Prepare a Base de Conhecimento**: Colete documentos (PDFs, Markdown, HTML, CSV) e implemente um script Python para segmentação (chunking) e geração de embeddings.
3.  **Ingestão de Dados**: Envie os chunks com seus embeddings para o banco de dados vetorial.
4.  **Fluxo de Consulta RAG**: Receba uma pergunta do usuário, gere seu embedding, consulte o banco vetorial para recuperar os chunks mais relevantes.
5.  **Geração de Resposta**: Combine os chunks recuperados com a pergunta do usuário em um prompt estruturado para o LLM.

---

## Core Workflows

### Workflow 1: Implementação de RAG com ChromaDB e Make.com para Chatbot de Suporte

Este workflow detalha a criação de um chatbot de suporte que responde a perguntas usando uma base de conhecimento interna armazenada no ChromaDB, orquestrado via Make.com.

**Passos Detalhados:**

1.  **Configuração do ChromaDB**:
    *   **Instalação (se local)**: `pip install chromadb`
    *   **Criação de Coleção**:
        ```python
        import chromadb
        from chromadb.utils import embedding_functions

        # Cliente persistente para armazenar dados localmente
        client = chromadb.PersistentClient(path="./chroma_db")
        
        # Usar um modelo de embedding de HuggingFace via sentence-transformers
        # Certifique-se de que 'sentence-transformers' está instalado: pip install sentence-transformers
        ef = embedding_functions.SentenceTransformerEmbeddingFunction(model_name="all-MiniLM-L6-v2")

        collection_name = "faq_suporte_tecnico"
        try:
            collection = client.get_collection(name=collection_name, embedding_function=ef)
            print(f"Coleção '{collection_name}' já existe.")
        except:
            collection = client.create_collection(name=collection_name, embedding_function=ef)
            print(f"Coleção '{collection_name}' criada.")
        ```

2.  **Ingestão de Documentos (Exemplo de script Python)**:
    *   Suponha que você tenha um diretório `docs/` com arquivos `.md`.
    *   **Script `ingest_docs.py`**:
        ```python
        import os
        import chromadb
        from chromadb.utils import embedding_functions
        from langchain.text_splitter import RecursiveCharacterTextSplitter

        client = chromadb.PersistentClient(path="./chroma_db")
        ef = embedding_functions.SentenceTransformerEmbeddingFunction(model_name="all-MiniLM-L6-v2")
        collection = client.get_collection(name="faq_suporte_tecnico", embedding_function=ef)

        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=500,
            chunk_overlap=100,
            length_function=len,
            separators=["\n\n", "\n", " ", ""]
        )

        doc_dir = "data/docs_suporte/" # Ex: "data/docs_suporte/politica_reembolso.md"
        documents_to_add = []
        metadatas_to_add = []
        ids_to_add = []
        
        for i, filename in enumerate(os.listdir(doc_dir)):
            if filename.endswith(".md"):
                filepath = os.path.join(doc_dir, filename)
                with open(filepath, 'r', encoding='utf-8') as f:
                    content = f.read()
                    
                chunks = text_splitter.split_text(content)
                for j, chunk in enumerate(chunks):
                    documents_to_add.append(chunk)
                    metadatas_to_add.append({"source": filename, "chunk_id": f"{filename}-{j}"})
                    ids_to_add.append(f"{filename.replace('.md', '')}-{j}")

        if documents_to_add:
            collection.add(
                documents=documents_to_add,
                metadatas=metadatas_to_add,
                ids=ids_to_add
            )
            print(f"Adicionados {len(documents_to_add)} chunks ao ChromaDB.")
        else:
            print("Nenhum documento para adicionar.")
        ```
    *   **Execução**: `python ingest_docs.py` (garanta que o diretório `data/docs_suporte/` exista com seus arquivos).

3.  **Configuração do Make.com (Cenário de Automação)**:
    *   **Módulo 1: Webhook Custom (Entrada)**: Recebe a pergunta do usuário do chatbot.
        *   **Configuração**: Crie um Webhook Custom. Copie o endereço do webhook.
        *   **Exemplo de Payload de Teste**:
            ```json
            {
              "question": "Como faço para solicitar um reembolso?"
            }
            ```
    *   **Módulo 2: HTTP - Make a request (Para executar script Python local)**:
        *   Para simular o acesso ao ChromaDB, você precisaria de um servidor Python intermediário ou executar o script Python diretamente em um ambiente que o Make.com possa chamar (e.g., um serviço na nuvem, ou um servidor local exposto via ngrok).
        *   **Exemplo (simplificado, assumindo um endpoint API)**:
            *   **URL**: `http://seu_servidor_rag:5000/query_rag`
            *   **Method**: `POST`
            *   **Headers**: `Content-Type: application/json`
            *   **Body (JSON)**:
                ```json
                {
                  "query": "{{1.question}}"
                }
                ```
            *   O servidor `seu_servidor_rag` teria um endpoint que:
                1.  Recebe a `query`.
                2.  Gera o embedding da `query`.
                3.  Consulta o ChromaDB para os top `k` chunks (e.g., `k=3`).
                4.  Retorna os chunks em formato de texto.
                *   **Exemplo de endpoint Flask (`rag_api.py`)**:
                    ```python
                    from flask import Flask, request, jsonify
                    import chromadb
                    from chromadb.utils import embedding_functions

                    app = Flask(__name__)
                    client = chromadb.PersistentClient(path="./chroma_db")
                    ef = embedding_functions.SentenceTransformerEmbeddingFunction(model_name="all-MiniLM-L6-v2")
                    collection = client.get_collection(name="faq_suporte_tecnico", embedding_function=ef)

                    @app.route('/query_rag', methods=['POST'])
                    def query_rag():
                        data = request.json
                        query = data.get('query')
                        if not query:
                            return jsonify({"error": "Query parameter is missing"}), 400

                        results = collection.query(
                            query_texts=[query],
                            n_results=3 # Recupera os 3 chunks mais relevantes
                        )
                        
                        retrieved_docs = results['documents'][0] if results['documents'] else []
                        context_str = "\n\n".join(retrieved_docs)
                        
                        return jsonify({"context": context_str})

                    if __name__ == '__main__':
                        app.run(host='0.0.0.0', port=5000)
                    ```
                    *   **Execução**: `python rag_api.py` (e use ngrok para expor se estiver local: `ngrok http 5000`)
    *   **Módulo 3: Claude - Create a Completion**:
        *   **Model**: `claude-3-sonnet-20240229` (ou outro modelo Claude)
        *   **Prompt**: Use o template de prompt RAG e insira o contexto do Módulo 2 e a pergunta do Módulo 1.

### Workflow 2: Otimização de RAG para Redução de Latência e Aumento de Precisão

Este workflow foca em refinar um sistema RAG existente para melhorar seu desempenho.

**Passos Detalhados:**

1.  **Estratégias de Chunking Avançadas**:
    *   **Chunking Semântico**: Em vez de tamanhos fixos, divida o texto em partes que representam ideias completas, usando técnicas como `SentenceTransformers` para agrupar sentenças semanticamente próximas ou `LlamaIndex` para nós de documentos.
    *   **Hierarchical Chunking**: Crie chunks menores para busca detalhada e chunks maiores para contexto geral, recuperando ambos e priorizando o detalhe.
    *   **Overlap Otimizado**: Experimente overlaps de 10-20% do tamanho do chunk para garantir que o contexto não seja cortado abruptamente. Por exemplo, chunk de 512 tokens com 50 tokens de overlap.

2.  **Re-ranking de Documentos Recuperados**:
    *   **Problema**: A busca por similaridade de cosseno pode trazer documentos semanticamente próximos, mas não os mais diretamente relevantes para a pergunta.
    *   **Solução**: Após recuperar os `N` chunks iniciais (e.g., N=10), use um modelo de re-ranking (e.g., Cohere Rerank API, `cross-encoder/ms-marco-TinyBERT-L-2-v2`) para classificar esses `N` chunks e selecionar os `K` mais relevantes (e.g., K=3) para enviar ao LLM.
    *   **Exemplo de integração (Python, após `results` do ChromaDB)**:
        ```python
        from sentence_transformers import CrossEncoder

        model = CrossEncoder('cross-encoder/ms-marco-TinyBERT-L-2-v2')
        
        query = "Como faço para redefinir minha senha?"
        retrieved_docs = ["doc1_sobre_login", "doc2_sobre_recuperacao", "doc3_sobre_seguranca"] # Exemplo de docs do ChromaDB
        
        # Cria pares (pergunta, documento) para o re-ranker
        sentence_pairs = [[query, doc] for doc in retrieved_docs]
        
        # Obtém scores de relevância
        rerank_scores = model.predict(sentence_pairs)
        
        # Ordena os documentos com base nos scores
        ranked_docs = sorted(zip(rerank_scores, retrieved_docs), key=lambda x: x[0], reverse=True)
        
        # Seleciona os top K documentos para o LLM
        top_k_docs = [doc for score, doc in ranked_docs[:3]]
        print(f"Documentos re-rankeados para o LLM: {top_k_docs}")
        ```

3.  **Cache de Embeddings e Respostas**:
    *   Para perguntas frequentes, armazene em cache os embeddings das perguntas e, se possível, as respostas geradas pelo LLM.
    *   **Tecnologia**: Redis, Memcached ou um simples dicionário em memória para casos de uso menos exigentes.
    *   **Exemplo**: Antes de consultar o ChromaDB, verifique se o embedding da `query` ou a `query` em si está no cache. Se sim, use o resultado cacheado para reduzir latência e custos.

4.  **Monitoramento e Testes A/B**:
    *   Monitore continuamente a latência da recuperação (tempo para obter chunks) e da geração (tempo para o LLM responder).
    *   Implemente testes A/B para comparar diferentes estratégias de chunking, modelos de embedding ou algoritmos de re-ranking, avaliando a qualidade da resposta e a performance. Use métricas como Recall@k e MRR (Mean Reciprocal Rank).

---

## Templates

### Template de Prompt para Geração RAG Otimizada

```
Você é um assistente de IA especializado em fornecer respostas claras e concisas baseadas em informações factuais.

INSTRUÇÕES:
1. Use EXCLUSIVAMENTE as informações contidas no CONTEXTO fornecido para formular sua resposta.
2. Não adicione informações externas ou faça suposições.
3. Se o CONTEXTO não contiver informações suficientes para responder à PERGUNTA, responda: "Não tenho informações suficientes para responder a essa pergunta com base no contexto fornecido."
4. Mantenha a resposta concisa e direta ao ponto.

CONTEXTO:
- Documento 1: "A política de reembolso para produtos digitais permite o estorno total em até 7 dias após a compra, desde que o produto não tenha sido baixado ou acessado por completo. Após 7 dias, não há reembolso."
- Documento 2: "Para solicitar um reembolso, o cliente deve enviar um e-mail para suporte@empresa.com.br com o número do pedido e o motivo da solicitação. O processamento pode levar até 5 dias úteis."
- Documento 3: "Produtos físicos têm uma política de devolução de 30 dias, exigindo que o item esteja em sua embalagem original e sem sinais de uso."

PERGUNTA:
Qual é o procedimento para solicitar um reembolso de um produto digital?

RESPOSTA:
```

### Template de Configuração de Webhook no Make.com para RAG

```json
{
  "event": "message.received",
  "payload": {
    "session_id": "sess_xyz789",
    "user_id": "user_123ab",
    "question": "Como posso resetar minha senha de administrador?",
    "metadata": {
      "origin": "chatbot_website",
      "timestamp": "2024-07-20T10:30:00Z",
      "priority": "normal"
    }
  }
}
```

---

## Checklist

- [x] Fontes de dados para RAG claramente definidas e acessíveis (APIs, bancos de dados, documentos).
- [x] Estratégia de chunking (tamanho, overlap, tipo de divisor) otimizada para o domínio.
- [x] Modelo de embedding escolhido (e.g., `text-embedding-ada-002`, `all-MiniLM-L6-v2`) e sua performance validada.
- [x] Banco de dados vetorial (Pinecone, ChromaDB, Weaviate) configurado, escalável e indexado.
- [x] Pipeline de ingestão de dados (ETL para embeddings) automatizado e resiliente.
- [x] Função de recuperação implementada com busca por similaridade de cosseno e filtro de metadados.
- [x] Template de prompt de geração RAG formatado com instruções explícitas sobre o uso do contexto.
- [x] Mecanismo de tratamento para cenários onde o contexto não contém a resposta ("Não sei").
- [x] Monitoramento de latência e custo por consulta RAG em ambiente de produção.
- [x] Implementação de re-ranking dos documentos recuperados para maior precisão.
- [x] Estratégias de cache (embeddings, respostas) para otimização de performance e custo.
- [x] Fluxo de feedback do usuário para contínuo refinamento da base de conhecimento e do RAG.

---

## Métricas de Referência

| Métrica                      | Benchmark (Bom) | Meta (Excelente) |
|------------------------------|-----------------|------------------|
| **Recall@5 (Recuperação)**   | 0.85            | 0.95             |
| **Latência Média da Resposta** | < 2.0 segundos  | < 1.0 segundos   |
| **Custo por Consulta RAG**   | < $0.01         | < $0.005         |
| **Taxa de Respostas Irrelevantes** | < 5%            | < 2%             |
| **Taxa de Alucinação (Hallucination Rate)** | < 3%            | < 1%             |
| **MRR (Mean Reciprocal Rank)** | 0.70            | 0.85             |

---

## Erros Comuns

1.  **Chunking Inadequado**: Contexto fragmentado demais (perdendo sentido) ou grande demais (diluindo a informação relevante e excedendo o limite de tokens do LLM).
    *   **Como evitar**: Experimentar tamanhos de chunk entre 256 e 1024 tokens com overlaps de 10-20% (`RecursiveCharacterTextSplitter` é uma boa base). Para documentos estruturados, usar divisores baseados em títulos ou seções. Exemplo: Testar chunks de 512 tokens com overlap de 50 tokens e comparar com 1024 tokens sem overlap.
2.  **Embeddings de Baixa Qualidade ou Inadequados**: O modelo de embedding escolhido não representa bem a semântica do domínio, resultando em recuperação de chunks irrelevantes.
    *   **Como evitar**: Utilizar modelos de embedding robustos e treinados em grandes volumes de texto (e.g., `OpenAI text-embedding-ada-002`, `E5-large-v2`). Para domínios muito específicos, considerar finetuning de um modelo de embedding ou usar modelos `cross-encoder` para re-ranking. Exemplo: Trocar `all-MiniLM-L6-v2` por `text-embedding-ada-002` da OpenAI para textos em inglês ou multilingual.
3.  **Prompt RAG Mal Formatado ou Ambíguo**: O LLM ignora o contexto fornecido ou alucina por falta de instruções claras.
    *   **Como evitar**: Incluir instruções explícitas no prompt para que o LLM use APENAS o contexto fornecido e trate a ausência de informações de forma específica. Exemplo: "Use EXCLUSIVAMENTE o CONTEXTO fornecido. Se a resposta não estiver no contexto, responda 'Não encontrei a resposta no contexto disponível'."
4.  **Latência Excessiva na Recuperação**: O processo de consulta ao banco de dados vetorial é lento, prejudicando a experiência do usuário.
    *   **Como evitar**: Otimizar o banco de dados vetorial (escalar recursos, usar índices eficientes como HNSW), implementar cache para embeddings de perguntas frequentes ou para os chunks recuperados. Exemplo: Utilizar um serviço de cache como Redis para armazenar resultados de consultas recentes por 10 minutos.

---

## Dicas Avançadas

1.  **RAG com Re-ranking Híbrido**: Combine a busca por similaridade vetorial (semântica) com um algoritmo de re-ranking baseado em palavras-chave (e.g., BM25) ou um modelo de re-ranking neural (e.g., Cohere Rerank API, `cross-encoder/ms-marco-TinyBERT-L-2-v2`). Primeiro, recupere um número maior de chunks (e.g., 20) via vetores, depois re-rankeie-os para selecionar os 3-5 mais relevantes para o prompt do LLM. Isso melhora a precisão significativamente.
2.  **Multi-hop RAG e Geração de Sub-perguntas**: Para perguntas complexas que exigem informações de múltiplos documentos ou uma cadeia de raciocínio, o LLM pode ser instruído a gerar sub-perguntas com base na pergunta original. Cada sub-pergunta aciona uma nova busca RAG, e os resultados são combinados para uma resposta final mais completa. Exemplo: "Quais são os requisitos de hardware para o software X e qual o custo de licenciamento anual?" pode se transformar em duas consultas RAG separadas.
3.  **Adaptação de Chunking por Tipo de Conteúdo**: A estratégia de segmentação não deve ser universal. Documentos estruturados (e.g., PDFs com seções, tabelas, figuras) podem se beneficiar de extratores específicos que respeitam a hierarquia do documento, enquanto textos planos podem usar segmentação baseada em sentenças ou parágrafos. Ferramentas como `LlamaParse` (para PDFs) ou `Unstructured.io` são úteis aqui. Exemplo: Para um manual técnico em PDF, use um parser que extraia seções inteiras como chunks, mantendo a coerência temática.
4.  **Aproveitamento de Metadados para Filtragem Pré-Recuperação**: Armazene metadados ricos (autor, data, tipo de documento, departamento) junto com seus chunks no banco vetorial. Use esses metadados para filtrar os resultados da busca por similaridade ANTES de enviá-los ao LLM. Isso é crucial para controlar o escopo da resposta. Exemplo: Para uma pergunta sobre "política de RH", filtre os chunks para `{"departamento": "RH"}` antes da busca vetorial.
5.  **Feedback Loop Contínuo com Avaliação Humana (Human-in-the-Loop)**: Implemente um sistema onde usuários possam dar feedback sobre a qualidade das respostas (e.g., "útil" / "não útil"). Use esses dados para identificar falhas no RAG (chunks irrelevantes, alucinações) e direcionar aprimoramentos, como re-rotulagem de dados para finetuning de embeddings ou ajuste de prompts. Exemplo: Se uma resposta for marcada como "não útil", registre a pergunta, a resposta e os chunks que foram usados para análise manual.