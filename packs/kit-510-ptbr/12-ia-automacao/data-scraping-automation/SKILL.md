---
name: data-scraping-automation
description: "Data Scraping Automation — Skill especializada para projetar, implementar e otimizar automações de extração de dados web e estruturados."
license: MIT
metadata:
  version: 1.0.0
  author: Cafe Code AI
  category: 12-ia-automacao
  updated: 2026-03-01
risk: safe
---

# Data Scraping Automation

Esta skill capacita o Claude a projetar, implementar e otimizar automações de extração de dados web e estruturados, integrando ferramentas de automação e IA.

---

## Keywords

web scraping, automação de dados, Make.com, N8N, Zapier, APIs de scraping, seletores CSS, XPath, extração estruturada, tratamento de CAPTCHA, proxy rotation, Playwright, Puppeteer, BeautifulSoup, extração de texto, normalização de dados.

---

## Quick Start

1.  **Analisar `robots.txt` e Termos de Serviço**: Verificar permissões para scraping no domínio alvo, por exemplo, acessando `https://www.exemplo.com/robots.txt`.
2.  **Identificar Seletores**: Usar o inspetor de elementos do navegador para mapear seletores CSS ou XPath de itens como `div.produto-titulo` ou `//span[@class='preco']`.
3.  **Configurar Webhook de Ingestão**: Criar um endpoint de webhook em Make.com (módulo "Webhooks > Custom Webhook") ou N8N (nó "Webhook") para receber os dados extraídos, por exemplo, `https://hook.us1.make.com/abcdef12345`.
4.  **Desenvolver Script de Extração**: Implementar um script Python com Playwright para navegar e extrair dados, enviando-os para o webhook. Exemplo: `page.goto("https://www.exemplo.com/produtos"); dados = page.locator(".item-info").all_inner_texts(); requests.post(webhook_url, json={"data": dados})`.
5.  **Processamento e Armazenamento**: No Make/N8N, após receber os dados via webhook, utilizar módulos para processar (ex: "Parse JSON", "Text Parser") e armazenar (ex: "Google Sheets > Add a Row", "Airtable > Create a Record").

---

## Core Workflows

### Workflow 1: Extração de Preços de E-commerce com Monitoramento Contínuo

Este workflow detalha a automação da extração de preços de produtos de um site de e-commerce e seu monitoramento contínuo.

1.  **Definição do Alvo e Análise Estrutural**:
    *   **Alvo**: `https://www.mercadolivre.com.br/tenis-masculino-nike/lista#D[A:tenis%20masculino%20nike]`
    *   **Análise**: Utilizar o inspetor de elementos do navegador (F12) para identificar os seletores CSS para o nome do produto (`h2.ui-search-item__title`), preço (`span.andes-money-amount__fraction`), e URL do produto (`a.ui-search-item__group__element`). Notar que a paginação é baseada em parâmetros de URL como `_Desde_49`.
2.  **Desenvolvimento do Scraper com Playwright (Python)**:
    *   Criar um script Python utilizando Playwright para headless browser automation. O script deve:
        *   Navegar para a URL inicial.
        *   Iterar pelas páginas de resultados (simulando clique em "Próxima página" ou manipulando o parâmetro `_Desde_`).
        *   Para cada produto, extrair o título, preço e URL.
        *   Tratar eventuais pop-ups ou carregamentos assíncronos (AJAX).
        *   Montar um objeto JSON com os dados de cada produto.
        *   Enviar o objeto JSON para um webhook de ingestão.

    ```python
    # Exemplo de trecho de scraper Python com Playwright
    from playwright.sync_api import sync_playwright
    import requests
    import json

    webhook_url = "https://hook.us1.make.com/abcdef12345" # Seu webhook do Make.com

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page(user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36")
        page.goto("https://www.mercadolivre.com.br/tenis-masculino-nike/lista#D[A:tenis%20masculino%20nike]", wait_until="networkidle")

        all_products_data = []
        for _ in range(3): # Limita a 3 páginas para exemplo
            products = page.locator("li.ui-search-layout__item").all()
            for product in products:
                try:
                    title = product.locator("h2.ui-search-item__title").text_content().strip()
                    price = product.locator("span.andes-money-amount__fraction").text_content().strip()
                    product_url = product.locator("a.ui-search-item__group__element").get_attribute("href")
                    all_products_data.append({
                        "titulo": title,
                        "preco": float(price.replace('.', '').replace(',', '.')), # Convertendo para float
                        "url": product_url
                    })
                except Exception as e:
                    print(f"Erro ao extrair produto: {e}")
            
            # Tenta ir para a próxima página
            next_button = page.locator("li.andes-pagination__button.andes-pagination__button--next")
            if next_button.is_visible():
                next_button.click()
                page.wait_for_load_state("networkidle")
            else:
                break
        
        browser.close()
        
        # Envia os dados para o webhook
        if all_products_data:
            response = requests.post(webhook_url, json={"produtos": all_products_data})
            print(f"Dados enviados ao webhook. Status: {response.status_code}")
        else:
            print("Nenhum dado para enviar.")
    ```
3.  **Configuração de Webhook de Ingestão (Make.com)**:
    *   No Make.com, criar um novo cenário.
    *   Primeiro módulo: "Webhooks" > "Custom Webhook". Copiar o endereço gerado (ex: `https://hook.us1.make.com/abcdef12345`).
    *   Segundo módulo: "Iterator" para iterar sobre a lista de produtos recebida no array `produtos`.
    *   Terceiro módulo: "Google Sheets" > "Add a Row" para inserir cada produto em uma planilha. Mapear os campos `titulo`, `preco`, `url` para as colunas da planilha.
4.  **Agendamento e Execução**:
    *   **Scraper**: O script Python pode ser agendado para rodar em um servidor VPS usando `cronjob` (ex: `0 9 * * * python3 /caminho/do/script.py`).
    *   **Make.com**: O cenário do Make.com é acionado automaticamente pelo webhook.

### Workflow 2: Coleta de Artigos de Notícias via API e Análise Semântica com Claude

Este workflow utiliza uma API de notícias para coletar artigos e o Claude para resumir e extrair informações chave.

1.  **Utilização de API de Notícias**:
    *   **Fonte**: NewsAPI.org. Registrar-se para obter uma `API Key`.
    *   **Requisição**: Fazer uma requisição GET para a API buscando notícias sobre "inteligência artificial" em português do Brasil.
    *   Exemplo de URL da API: `https://newsapi.org/v2/everything?q=inteligencia%20artificial&language=pt&sortBy=publishedAt&apiKey=SUA_API_KEY`
2.  **Filtro e Seleção de Tópicos (N8N/Make.com)**:
    *   No N8N, usar o nó "HTTP Request" para chamar a NewsAPI.
    *   Usar um nó "Set" ou "Code" para filtrar os resultados, mantendo apenas artigos com `source.name` de veículos específicos (ex: "TecMundo", "Canaltech") e `description` com mais de 100 caracteres.
    *   Iterar sobre os artigos filtrados.
3.  **Envio de Conteúdo para Claude para Resumo e Análise**:
    *   Para cada artigo, extrair o `title`, `url` e `content` (ou `description`).
    *   Utilizar um nó "HTTP Request" (N8N) ou "Make an API Call" (Make.com) para enviar o `content` do artigo ao Claude (`anthropic.com/v1/messages`).
    *   **Prompt para Claude**:
        ```
        Você é um analista de dados especializado em sumarização e extração de entidades.
        Recebi o seguinte artigo de notícias:

        Título: {{ $json.title }}
        URL: {{ $json.url }}
        Conteúdo:
        {{ $json.content }}

        Por favor, faça o seguinte:
        1. Crie um resumo conciso do artigo em 3-5 sentenças.
        2. Liste as 3-5 entidades principais (pessoas, organizações, locais, tecnologias) mencionadas no artigo.
        3. Identifique o sentimento geral do artigo (Positivo, Negativo, Neutro).
        4. Sugira 2-3 tags relevantes para categorizar este artigo.

        Formato de saída (JSON):
        {
          "resumo": "...",
          "entidades_principais": ["entidade1", "entidade2", ...],
          "sentimento": "...",
          "tags": ["tag1", "tag2", ...]
        }
        ```
4.  **Armazenamento e Alerta**:
    *   Após receber a resposta JSON do Claude, usar um nó "Google Sheets" > "Add a Row" para armazenar o título, URL original, o resumo, entidades, sentimento e tags em uma planilha.
    *   Opcionalmente, usar um nó "Slack" > "Send Message" para enviar um alerta com o resumo de artigos muito relevantes (ex: sentimento "Negativo" para a palavra-chave "inteligência artificial").

---

## Templates

### Template de Prompt para Normalização de Dados Scrapados

```
Você é um especialista em processamento e normalização de dados brutos de web scraping.
Recebi o seguinte bloco de texto/HTML extraído de uma página de produto.
Minha tarefa é extrair e estruturar os dados chave em um formato JSON limpo.

Conteúdo bruto:
```html
<div class="product-detail">
    <h1 class="product-name">Smart TV Samsung Neo QLED 55" 4K</h1>
    <span class="product-price">R$ 4.999,00</span>
    <p class="product-description">A melhor experiência visual com tecnologia Neo QLED. Processador Neural Quantum 4K.</p>
    <ul class="product-specs">
        <li>Tamanho: 55 polegadas</li>
        <li>Resolução: 3840 x 2160 (4K)</li>
        <li>Marca: Samsung</li>
        <li>Modelo: QN55QN90CAGXZD</li>
    </ul>
    <div class="availability out-of-stock">Sem estoque</div>
</div>
```

Por favor, extraia as seguintes informações e formate-as como um objeto JSON.
- `nome_produto`: (string)
- `preco`: (float, use ponto como separador decimal)
- `descricao`: (string)
- `especificacoes`: (objeto com chaves como "Tamanho", "Resolução", "Marca", "Modelo")
- `disponibilidade`: (string, "Em estoque" ou "Sem estoque")

Se um campo não for encontrado, use `null`.

```json
{
  "nome_produto": "Smart TV Samsung Neo QLED 55\" 4K",
  "preco": 4999.00,
  "descricao": "A melhor experiência visual com tecnologia Neo QLED. Processador Neural Quantum 4K.",
  "especificacoes": {
    "Tamanho": "55 polegadas",
    "Resolução": "3840 x 2160 (4K)",
    "Marca": "Samsung",
    "Modelo": "QN55QN90CAGXZD"
  },
  "disponibilidade": "Sem estoque"
}
```

### Template de Configuração de Webhook (Make.com)

```
{
  "webhookId": "abcdef12345",
  "data": {
    "produtos": [
      {
        "titulo": "Tênis Nike Air Zoom Pegasus 40",
        "preco": 699.99,
        "url": "https://www.mercadolivre.com.br/tenis-nike-air-zoom-pegasus-40/p/MLB25000000"
      },
      {
        "titulo": "Tênis Nike Revolution 6 Next Nature",
        "preco": 349.99,
        "url": "https://www.mercadolivre.com.br/tenis-nike-revolution-6-next-nature/p/MLB25000001"
      }
    ],
    "timestamp": "2024-03-01T10:30:00Z"
  }
}
```
*Este template representa o payload JSON que um script de scraping enviaria para um webhook do Make.com. No Make, o módulo "Webhooks > Custom Webhook" iria expor este formato, e os dados seriam acessíveis via `{{1.data.produtos[]}}` para iteração.*

---

## Checklist

- [x] Verificar `robots.txt` e Termos de Serviço do site alvo para conformidade.
- [x] Identificar padrões de bloqueio do site (CAPTCHA, IP Ban, detecção de headless browser).
- [x] Selecionar a ferramenta de scraping adequada (Playwright, Puppeteer, BeautifulSoup, Scrapy, Apify, Octoparse) com base na complexidade e dinamicidade da página.
- [x] Mapear seletores CSS ou XPath robustos para todos os dados relevantes, considerando mudanças futuras na estrutura HTML.
- [x] Implementar tratamento de paginação, carregamento assíncrono (AJAX) e redirecionamentos.
- [x] Utilizar proxies rotativos (ex: Bright Data, Oxylabs) para evitar bloqueios de IP, se necessário.
- [x] Adicionar `user-agents` variados e `headers` HTTP para simular diferentes navegadores e requisições legítimas.
- [x] Implementar mecanismos de retry com backoff exponencial para requisições falhas.
- [x] Estruturar o payload de dados de forma consistente (JSON) para envio via webhook ou API.
- [x] Validar a integridade, completude e formato dos dados extraídos antes do armazenamento final.
- [x] Configurar logs e alertas para monitorar a saúde e eventuais falhas do scraper.

---

## Métricas de Referência

| Métrica                      | Benchmark (Médio) | Meta (Otimizado) |
|------------------------------|-------------------|------------------|
| Taxa de Sucesso de Extração  | 95-98%            | 99%+             |
| Latência Média por Requisição| 800-2500 ms       | 300-1000 ms      |
| Custo por Registro Extraído  | R$ 0.005 - R$ 0.08| R$ 0.001 - R$ 0.02|
| Volume Diário de Registros   | 5.000 - 50.000    | 100.000+         |
| Frequência de Quebra de Scraper| 1-2x / mês      | <1x / mês        |

---

## Erros Comuns

1.  **Bloqueio de IP ou CAPTCHA Recorrente**: **Como evitar**: Não utilizar proxies rotativos ou usar um número insuficiente de proxies de baixa qualidade. Scrapers sem `user-agents` variados ou que não simulam comportamento humano (ex: sem atrasos aleatórios entre requisições) são facilmente detectados. Solução: Implementar pool de proxies residenciais ou datacenter de alta qualidade, rotacionar `user-agents` a cada requisição, adicionar atrasos aleatórios (`time.sleep(random.uniform(2, 5))`) e integrar serviços de resolução de CAPTCHA (ex: 2Captcha, Anti-Captcha) em caso de desafios.
2.  **Dados Incompletos ou Incorretos**: **Como evitar**: Seletores CSS/XPath desatualizados ou muito genéricos que não capturam os elementos exatos ou que quebram com pequenas alterações no layout do site. Solução: Validar seletores frequentemente, usar seletores mais específicos (ex: `div[data-testid="product-price"]` em vez de `span.price`), e implementar validações pós-extração para verificar a presença e o formato dos dados esperados.
3.  **Performance Lenta e Consumo Excessivo de Recursos**: **Como evitar**: Não otimizar requisições HTTP, usar navegadores headless sem `networkidle` ou `domcontentloaded` adequados, ou processar grandes volumes de dados em uma única thread. Solução: Utilizar bibliotecas HTTP leves como `httpx` para APIs, otimizar `wait_until` no Playwright/Puppeteer, e considerar paralelização ou distribuição da carga de scraping usando ferramentas como Scrapy (Python) ou arquiteturas baseadas em filas (RabbitMQ, Kafka) com workers em nuvem (AWS Lambda, Google Cloud Functions).

---

## Dicas Avançadas

1.  **Captura de Eventos de Rede com Playwright/Puppeteer**: Em vez de fazer parsing do HTML, intercepte as requisições XHR (AJAX) que o navegador faz para carregar os dados. Muitos sites carregam dados dinamicamente via APIs internas. Use `page.on('request', ...)` e `page.on('response', ...)` para capturar payloads JSON diretamente, sendo mais rápido e menos propenso a quebras de layout. Exemplo: `page.route("**/api/products", lambda route: route.abort())` para bloquear requisições irrelevantes e `page.on("response", lambda response: print(response.json()))` para capturar as relevantes.
2.  **Web Scraping Distribuído com Cloud Functions**: Para escalar extrações de grande volume, use Google Cloud Functions, AWS Lambda ou Azure Functions. Cada função pode ser acionada por um evento (ex: fila de mensagens) e executar uma tarefa de scraping específica para uma URL. Isso permite processamento paralelo e sem servidor, pagando apenas pelo tempo de execução. Configure um Pub/Sub (GCP) ou SQS (AWS) para gerenciar as URLs a serem raspadas.
3.  **Técnicas de Anti-Bot Evasão Avançadas**: Além de proxies e `user-agents`, implemente `headless-stealth` (para Puppeteer/Playwright) para simular um navegador real, manipule o `navigator.webdriver` e outros atributos JavaScript que sites usam para detectar bots. Considere também simular movimentos do mouse e scrolls com `page.mouse.move()` ou `page.evaluate(() => window.scrollBy(0, 100))`.
4.  **Uso de IA para Extração Semiestruturada e Resiliência**: Alimente grandes blocos de HTML ou texto para o Claude com prompts avançados que instruam a IA a identificar e extrair entidades mesmo sem seletores fixos. Isso é extremamente útil para sites com layouts variáveis ou onde os seletores mudam constantemente. Claude pode "entender" o contexto e extrair `preço`, `nome_produto`, `descrição` mesmo que o HTML mude, aumentando a resiliência do scraper.
5.  **Monitoramento Ativo de Alterações Estruturais**: Crie um sistema que periodicamente raspa uma página de referência e compara o hash do HTML ou o count de elementos chaves (ex: número de itens de produto) com uma versão anterior. Se houver uma alteração significativa, dispare um alerta para o time de desenvolvimento, indicando uma possível quebra no scraper antes que os dados parem de fluir.