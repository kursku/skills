---
name: ai-image-generation
description: "Ai Image Generation — Skill especializada para ai image generation, com foco em automação, APIs e prompts avançados para geração de imagens."
license: MIT
metadata:
  version: 1.0.0
  author: Cafe Code AI
  category: 12-ia-automacao
  updated: 2026-03-01
risk: safe
---

# Ai Image Generation

Esta skill capacita o Claude a gerar, refinar e automatizar a criação de imagens através de modelos de IA, integrando-se com APIs e plataformas de automação.

---

## Keywords

Stable Diffusion, Midjourney, DALL-E 3, Text-to-Image, Image-to-Image, Negative Prompt, CFG Scale, Seed, LoRA, ControlNet, Inpainting, Outpainting, Upscaling, API REST, Webhook, Make.com, N8N, Prompt Engineering, Diffusion Models, AnimateDiff.

---

## Quick Start

1.  **Escolha do Modelo Base**: Selecione um modelo de geração (e.g., SDXL, Midjourney V6, DALL-E 3) apropriado para o estilo e detalhe desejados.
2.  **Construção do Prompt Inicial**: Desenvolva um prompt descritivo detalhado, especificando assunto, estilo, iluminação e composição, como "Uma paisagem urbana cyberpunk neon, estilo Blade Runner, luzes roxas e azuis, chuva, reflexos no asfalto molhado, drone voando, perspectiva de baixo para cima."
3.  **Definição de Parâmetros**: Configure o `aspect ratio` (e.g., 16:9 para paisagens), `CFG Scale` (7-10 para maior aderência ao prompt), e aplique um `negative prompt` inicial (e.g., "low quality, blurry, disfigured").
4.  **Geração e Análise Visual**: Execute a geração da imagem e avalie artefatos, fidelidade ao prompt e qualidade estética; ajuste os parâmetros ou o prompt conforme necessário.
5.  **Refinamento e Variações**: Utilize o `seed` da imagem promissora para gerar variações ou aplique técnicas como `img2img` com um `denoising strength` baixo (0.3-0.5) para pequenas alterações.

---

## Core Workflows

### Workflow 1: Automatizando Geração de Imagens de Produtos para E-commerce com Stable Diffusion API

Este workflow descreve a integração de um sistema de e-commerce com uma API de Stable Diffusion (ex: Leonardo.ai, Stability AI API) para gerar imagens consistentes de produtos automaticamente quando um novo item é adicionado ou atualizado.

**Passos Detalhados:**

1.  **Configuração do Trigger**: No Make.com (ou N8N), configure um webhook ou um módulo de banco de dados para escutar novos produtos ou atualizações em uma tabela SQL, Google Sheets ou plataforma de e-commerce (Shopify, WooCommerce).
    *   **Exemplo Make.com**: Módulo "Webhooks" > "Custom webhook" ou módulo "MySQL" > "Watch new rows".
    *   **Dados de Entrada**: `product_id`, `product_name`, `product_description`, `color`, `material`, `category`.
2.  **Construção Dinâmica do Prompt**: Utilize os dados do produto para construir um prompt detalhado e um negative prompt.
    *   **Exemplo de Prompt (Make.com/N8N)**: Concatene campos de texto:
        ```
        "Um [material] [color] [product_name] de alta qualidade, isolado em um fundo branco limpo, iluminação de estúdio profissional, detalhes nítidos, perspectiva de 45 graus, fotografia de produto de e-commerce."
        ```
    *   **Exemplo de Negative Prompt**:
        ```
        "low quality, blurry, ugly, watermark, text, signature, bad anatomy, deformed, disfigured, poor lighting, dark, shadow, multiple objects, messy background, pixelated"
        ```
3.  **Chamada à API de Geração de Imagens**: Configure um módulo HTTP para fazer uma requisição POST à API de Stable Diffusion.
    *   **URL da API (Exemplo Leonardo.ai)**: `https://cloud.leonardo.ai/api/v1/generations`
    *   **Headers**:
        ```json
        {
          "Authorization": "Bearer SEU_API_KEY",
          "Content-Type": "application/json"
        }
        ```
    *   **Corpo da Requisição (JSON)**:
        ```json
        {
          "prompt": "{{dynamic_prompt_from_step_2}}",
          "negative_prompt": "{{dynamic_negative_prompt_from_step_2}}",
          "modelId": "6bef9f1b-29cb-40c7-b9df-32afdce17ccb", // ID do modelo SDXL
          "width": 1024,
          "height": 1024,
          "num_images": 1,
          "guidance_scale": 7,
          "seed": -1,
          "presetStyle": "PHOTOGRAPHY",
          "public": false
        }
        ```
4.  **Processamento da Resposta e Download**: A API retornará um JSON com o status da geração e, após concluída, as URLs das imagens.
    *   **Exemplo de Resposta (sucesso)**:
        ```json
        {
          "sdGenerationJob": {
            "generationId": "...",
            "status": "COMPLETE",
            "outputs": [
              {
                "id": "...",
                "imageUrl": "https://cdn.leonardo.ai/users/....png",
                "nsfw": false
              }
            ]
          }
        }
        ```
    *   Extraia `outputs[0].imageUrl`.
5.  **Armazenamento e Atualização**: Baixe a imagem para um armazenamento (S3, Google Cloud Storage, CDN) e salve a URL no campo `image_url` do produto no seu banco de dados ou plataforma de e-commerce.
    *   **Exemplo Make.com**: Módulo "HTTP" > "Get a file" (para download), Módulo "Google Drive" > "Upload a file" ou "MySQL" > "Update a row".

### Workflow 2: Criação de Variações de Imagem para Campanhas de Marketing com Midjourney via Discord Webhook

Este workflow utiliza Midjourney para gerar variações criativas de uma imagem base para diferentes formatos de campanha, orquestrando prompts via Discord e processando os resultados.

**Passos Detalhados:**

1.  **Geração da Imagem Base no Midjourney**: Interaja diretamente com o bot do Midjourney no Discord para gerar a imagem inicial.
    *   **Prompt de Exemplo**: `/imagine prompt: Um dragão majestoso voando sobre um castelo medieval em ruínas ao pôr do sol, estilo pintura a óleo, épico, dramático --ar 16:9 --v 6.0`
    *   Após a geração, selecione uma das 4 variações (U1, U2, U3 ou U4) que servirá como base para as próximas iterações.
2.  **Extração do Job ID e Seed (Opcional, mas útil)**: Para maior controle, use `/show <job_id>` ou `/info` para obter o `seed` da imagem escolhida.
3.  **Configuração do Discord Webhook (Entrada para Automação)**: Crie um webhook no seu servidor Discord para receber comandos de prompts de um sistema externo (Make/N8N). Isso permite enviar prompts programaticamente para o canal do Midjourney (se configurado com o bot).
    *   **URL do Webhook**: `https://discord.com/api/webhooks/SEU_ID/SEU_TOKEN`
4.  **Automação para Geração de Variações (Make/N8N)**:
    *   **Trigger**: Inicie o fluxo manualmente ou com um agendador.
    *   **Módulo HTTP (POST para Discord Webhook)**: Envie um prompt modificado usando o `seed` da imagem base e parâmetros diferentes.
        *   **Corpo da Requisição (JSON)**:
            ```json
            {
              "content": "/imagine prompt: Um dragão majestoso voando sobre um castelo medieval em ruínas ao amanhecer, estilo aquarela, cores vibrantes, atmosfera sonhadora, com o mesmo dragão e castelo da imagem com seed {{seed_da_imagem_base}} --seed {{seed_da_imagem_base}} --style raw --ar 4:3 --v 6.0"
            }
            ```
        *   Repita este passo com diferentes prompts para gerar variações para diferentes formatos (ex: `--ar 9:16` para stories, `--ar 1:1` para posts).
5.  **Monitoramento e Coleta de Imagens**: Monitore o canal do Discord ou use uma integração avançada (se disponível via API de terceiros ou bot customizado) para detectar e baixar as novas imagens geradas pelo Midjourney.
6.  **Pós-processamento e Distribuição**: Redimensione, otimize e adicione marcas d'água se necessário. Distribua as imagens para as plataformas de marketing (Buffer, Hootsuite, diretamente para APIs de redes sociais).

---

## Templates

### Prompt para Geração de Imagem de Produto (Calçado)

```
Um tênis de corrida futurista da marca "VortexStride", cor azul cobalto com detalhes em laranja fluorescente, solado robusto com amortecimento visível, atacadores cinzas. O tênis está em um pedestal minimalista branco, com iluminação de estúdio suave, fundo gradiente cinza claro para branco. Perspectiva frontal ligeiramente angular, foco nítido nos detalhes do material e textura. Fotografia de produto de alta resolução, estilo clean e moderno.

Negative Prompt: desfocado, borrado, baixo contraste, cores escuras, sujo, arranhado, tênis velho, vários tênis, marca d'água, texto, fundo desordenado, sombra pesada.
```

### Prompt para Geração de Imagem Estilizada (Cena Fantástica)

```
Uma floresta encantada densa e mística ao anoitecer, árvores antigas com musgo bioluminescente, um rio serpenteando com águas cristalinas refletindo a luz das fadas flutuantes. Uma névoa suave e etérea paira sobre o chão da floresta. Estilo de arte digital fantástica, cores profundas e saturadas, iluminação mágica e dramática, detalhes intrincados na folhagem. Resolução 4K, atmosfera serena e misteriosa.

Negative Prompt: realidade, fotografia, feio, desfigurado, borrado, pixelado, artefato, baixo detalhe, luz plana, escuridão total, fadas com rosto humano, galhos mortos, lixo.
```

---

## Checklist

- [x] O prompt principal é detalhado e evita ambiguidades?
- [x] Um `negative prompt` foi aplicado para eliminar características indesejadas (e.g., artefatos, texto)?
- [x] O `aspect ratio` da imagem está otimizado para o uso final (e.g., 1:1 para feed, 9:16 para stories)?
- [x] O `CFG Scale` foi ajustado (tipicamente 7-12) para equilibrar a aderência ao prompt e a criatividade do modelo?
- [x] O `seed` foi fixado ou gerenciado para consistência em séries de imagens ou variações?
- [x] Existem modelos LoRA, embeddings ou estilos específicos carregados para influenciar o resultado estético?
- [x] A imagem foi submetida a um processo de `upscaling` (e.g., com ESRGAN, SwinIR) para aumentar a resolução?
- [x] Foram exploradas variações da imagem gerada (V1, V2, V3, V4, Remix no Midjourney, ou ajuste de `seed`/`denoising` em SD)?
- [x] A imagem final foi inspecionada para artefatos visuais, distorções ou inconsistências lógicas?
- [x] Os metadados da imagem (PNG Info) foram revisados para entender os parâmetros de geração e facilitar a reprodução?
- [x] Em fluxos de automação, a API retorna um status de sucesso e a URL da imagem é persistida?
- [x] Foi implementado um mecanismo de fallback ou retry para falhas na API de geração de imagens?

---

## Métricas de Referência

| Métrica                         | Benchmark (SDXL/Midjourney) | Meta (Otimizado)          |
|---------------------------------|-----------------------------|---------------------------|
| **Fidelidade ao Prompt (Human)**| 3.5/5 estrelas              | 4.5/5 estrelas            |
| **Qualidade Perceptual (Human)**| 3.8/5 estrelas              | 4.7/5 estrelas            |
| **Tempo de Geração/Imagem**     | 10-30 segundos (API)        | 5-15 segundos (API)       |
| **Custo por Imagem**            | $0.01 - $0.05               | $0.005 - $0.02            |
| **Taxa de Artefatos Visíveis**  | < 5%                        | < 1%                      |
| **Consistência de Estilo**      | 80% (em série)              | 95% (com LoRA/ControlNet) |

---

## Erros Comuns

1.  **Prompts Vagos ou Ambíguos**: Geram imagens inconsistentes, com elementos inesperados ou sem aderência ao tema.
    *   **Como evitar**: Seja extremamente descritivo, use adjetivos específicos, defina o estilo (e.g., "fotorealismo", "pintura a óleo"), a iluminação (e.g., "luz suave de estúdio", "luz dourada do pôr do sol") e a composição (e.g., "plano fechado", "perspectiva aérea"). Use listas de características para clareza.
2.  **Uso Inadequado do CFG Scale**: Um `CFG Scale` muito baixo (1-4) resulta em imagens que ignoram o prompt; muito alto (15+) pode levar a artefatos e distorções.
    *   **Como evitar**: Mantenha o `CFG Scale` entre 7 e 12 para a maioria dos casos. Experimente valores nessa faixa, aumentando-o ligeiramente se a imagem não estiver seguindo o prompt ou diminuindo-o se estiver com muitos artefatos.
3.  **Não Utilizar Negative Prompts**: Imagens com elementos indesejados, como dedos extras, olhos desalinhados, texto aleatório, ou qualidade inferior.
    *   **Como evitar**: Sempre inclua um `negative prompt` robusto com termos como "low quality, blurry, ugly, disfigured, text, watermark, bad anatomy, deformed, pixelated, jpeg artifacts". Adapte-o para cada cenário específico (e.g., "pessoas, carros" se o foco é paisagem).

---

## Dicas Avançadas

1.  **Iteração com Img2Img e Denoising Strength**: Para refinar uma imagem existente sem alterar drasticamente sua estrutura, use-a como entrada para `img2img` com um `denoising strength` baixo (0.2-0.5). Isso permite aplicar pequenas mudanças de prompt ou estilo enquanto mantém a composição original.
    *   **Exemplo**: Gerar uma imagem inicial de um carro. Usar `img2img` com `denoising strength: 0.3` e um novo prompt "carro vermelho metálico, reflexos de luz, estilo cyberpunk" para mudar a cor e adicionar detalhes sem alterar o modelo do carro.
2.  **Uso de ControlNet para Composição Precisa**: Implemente ControlNet para guiar a pose, a profundidade ou a estrutura da imagem gerada. Modelos como `Canny`, `OpenPose` ou `Depth` são essenciais para manter a consistência visual em séries.
    *   **Exemplo de Automação**: Um fluxo que recebe uma imagem de silhueta (Canny) ou um esqueleto (OpenPose) de um personagem e gera variações de roupas ou ambientes, mantendo a pose exata.
3.  **Treinamento e Aplicação de LoRAs/Embeddings Customizados**: Para consistência de personagens, objetos ou estilos específicos, treine seus próprios LoRAs (Low-Rank Adaptation) ou Textual Inversions (Embeddings). Integre o carregamento desses modelos na sua chamada de API.
    *   **Exemplo de Prompt com LoRA**: `Um [nome_personagem_treinado_lora] em uma armadura medieval, batalha épica, estilo [estilo_treinado_embedding]. <lora:personagem_x:0.8> <ti:estilo_y>`
4.  **Prompt Blending para Conceitos Híbridos**: Combine prompts de diferentes conceitos para criar imagens únicas, seja através de pesos (`(conceito A:1.2) e (conceito B:0.8)`) ou concatenando ideias.
    *   **Exemplo**: "Um robô samurai, estilo [arte_japonesa], com elementos de [ficção_científica], floresta de cerejeiras, névoa."
5.  **AnimateDiff para Geração de Vídeos Curtos**: Para ir além de imagens estáticas, explore AnimateDiff ou ferramentas similares que permitem transformar prompts de texto ou imagens em animações curtas e consistentes, ideal para micro-conteúdos de redes sociais.
    *   **Automação**: Gerar uma série de imagens com pequenas variações de pose/expressão e então usar AnimateDiff ou um script de FFmpeg para compilar em um GIF/vídeo curto.