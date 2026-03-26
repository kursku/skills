---
name: video-course-production
description: "Video Course Production — Skill especializada para video course production"
license: MIT
metadata:
  version: 1.0.0
  author: Cafe Code AI
  category: 13-cursos-educacao
  updated: 2026-03-01
risk: safe
---

# Video Course Production

Capacita o Claude Code a planejar, produzir e otimizar cursos em vídeo de alta qualidade, desde a concepção do roteiro até a análise de engajamento pós-lançamento.

---

## Keywords

Roteirização para vídeo, Captação de áudio profissional, Edição não-linear, Chroma key, Microlearning, Storyboard, Plataforma EAD, Engajamento de vídeo, Pós-produção audiovisual, Autoria de cursos, SCORM, Gamificação em vídeo.

---

## Quick Start

1.  **Estruturar Micro-Módulos**: Dividir o conteúdo do primeiro módulo em segmentos de 5-10 minutos, focando em um único conceito por vídeo.
2.  **Configurar OBS Studio**: Ajustar resolução de gravação para 1080p (1920x1080), 29.97 FPS, e bitrate de 6000 kbps para H.264 MP4.
3.  **Gravar Áudio de Referência**: Testar o microfone condensador USB (ex: HyperX QuadCast) com ganho em -12dB para evitar picos de áudio.
4.  **Exportar Versão Bruta**: Após gravação, exportar o vídeo em formato MP4 com as configurações originais para iniciar a edição.

---

## Core Workflows

### Workflow 1: Roteirização e Pré-produção Estruturada de Módulos

Este workflow detalha a criação de um roteiro robusto e a preparação técnica antes da gravação para garantir eficiência e qualidade.

**Passos Detalhados:**

1.  **Segmentação de Conteúdo para Microlearning (7-12 min por vídeo)**:
    *   **Ação**: Analisar o tópico do módulo (ex: "Fundamentos de Python para Ciência de Dados") e identificar sub-tópicos que podem ser abordados em vídeos independentes de 7 a 12 minutos.
    *   **Exemplo**: O módulo "Fundamentos de Python" pode ser dividido em "Variáveis e Tipos de Dados (8 min)", "Estruturas Condicionais (10 min)", "Laços de Repetição (9 min)". Cada um terá um objetivo de aprendizagem claro e específico.
    *   **Evitar**: Abordar múltiplos conceitos complexos em um único vídeo, o que leva à sobrecarga cognitiva e baixa retenção.

2.  **Desenvolvimento de Roteiro Narrativo e Visual**:
    *   **Ação**: Para cada vídeo-aula, criar um roteiro detalhado que inclua fala do apresentador, ações na tela (capturas, slides), b-rolls, chamadas para ação (CTAs) e a duração estimada de cada bloco.
    *   **Exemplo**:
        ```
        [0:00-0:30] INTRO (Música + Logo)
        [0:30-1:00] GANCHO: "Você sabia que 70% dos erros de programação vêm de tipagem incorreta?"
        [1:00-3:00] TÓPICO 1: Variáveis (Explicação Conceitual + Exemplo de Código em PyCharm)
        [3:00-5:00] TÓPICO 2: Tipos de Dados (Integer, Float, String, Boolean - Demonstração de "type()")
        [5:00-6:30] TÓPICO 3: Conversão de Tipos (int(), str(), float() - Caso de uso: input do usuário)
        [6:30-7:00] REVISÃO RÁPIDA: Slide com 3 bullet points dos conceitos chave.
        [7:00-7:30] CTA: "Pratique no Colab! Link na descrição. Próxima aula: Estruturas Condicionais!"
        [7:30-8:00] OUTRO (Música + Créditos)
        ```
    *   **Foco**: Manter a linguagem clara, direta e conversacional. Integrar exemplos práticos e demonstrações visuais consistentemente.

3.  **Preparação do Ambiente de Gravação e Equipamentos**:
    *   **Ação**: Montar o setup de gravação, garantindo iluminação, áudio e vídeo de qualidade profissional.
    *   **Exemplo**:
        *   **Iluminação**: Configurar um esquema de três pontos (Key Light: softbox de 60W a 45 graus; Fill Light: anel de LED de 30W a 90 graus, menos intenso; Back Light: pequena LED de 15W para separar o apresentador do fundo).
        *   **Áudio**: Usar um microfone de lapela (ex: Rode SmartLav+) ou condensador USB (ex: Blue Yeti) com Pop Filter. Testar níveis de áudio para que o pico não exceda -6dB e o RMS fique entre -12dB e -9dB.
        *   **Câmera**: Câmera DSLR (ex: Canon T7i) com lente 50mm f/1.8, configurada em 1080p, 29.97 FPS, ISO 400, shutter speed 1/60s, abertura f/4.0. Focar manualmente nos olhos do apresentador.
        *   **Fundo**: Fundo neutro ou chroma key bem iluminado, sem sombras.
    *   **Objetivo**: Minimizar problemas técnicos na pós-produção, economizando tempo e garantindo consistência visual e sonora.

### Workflow 2: Pós-produção Otimizada e Estratégias de Engajamento para EAD

Este workflow aborda a fase de edição, masterização e as táticas para maximizar a retenção e a interação dos alunos com o conteúdo em vídeo.

**Passos Detalhados:**

1.  **Edição Não-Linear Eficiente e Dinâmica (DaVinci Resolve / Premiere Pro)**:
    *   **Ação**: Importar todas as mídias (vídeo principal, b-rolls, slides, áudio limpo) para a linha do tempo. Realizar cortes rápidos, remover pausas > 1.0 segundo e "uhms" ou "ahs".
    *   **Exemplo**: Utilizar a função "Remove Gaps" ou "Ripple Delete" após cortar trechos indesejados. Inserir b-rolls de 3-5 segundos sobre a fala para ilustrar conceitos (ex: ao falar de "variáveis", mostrar animações de caixas de armazenamento).
    *   **Melhoria**: Aplicar transições sutis (ex: "Cross Dissolve" de 0.5s) apenas quando necessário para mudar de cena ou tópico. Evitar transições extravagantes.

2.  **Masterização de Áudio Profissional**:
    *   **Ação**: Processar o áudio captado para atingir clareza, volume consistente e ausência de ruídos.
    *   **Exemplo**:
        1.  **Redução de Ruído**: Usar um plugin de Noise Reduction (ex: iZotope RX) para eliminar ruído de fundo persistente (ex: -15dB de redução).
        2.  **Normalização**: Ajustar o volume para -6dB RMS com pico em -3dB.
        3.  **Compressão**: Aplicar um compressor com ratio de 3:1, threshold em -18dB e attack/release rápidos para nivelar o volume da fala.
        4.  **Equalização**: Realçar frequências entre 2-4 kHz para clareza vocal e cortar baixas frequências abaixo de 80 Hz para eliminar "boominess".
    *   **Impacto**: Áudio de alta qualidade aumenta a percepção de profissionalismo e reduz a fadiga auditiva do aluno, impactando diretamente a taxa de conclusão.

3.  **Otimização de Vídeo para Plataformas EAD e Engajamento Interativo**:
    *   **Ação**: Exportar o vídeo final com configurações ideais para streaming e integrar elementos interativos ou gamificados.
    *   **Exemplo**:
        *   **Exportação**: H.264, MP4, 1080p, 29.97 FPS, bitrate variável de 4-8 Mbps (dependendo da complexidade do vídeo). Isso garante qualidade visual com tamanho de arquivo gerenciável.
        *   **Legendas**: Gerar e revisar legendas no formato SRT. Carregá-las junto com o vídeo.
        *   **Elementos de Engajamento**:
            *   **Quizzes Interativos**: Integrar um quiz de múltipla escolha de 3 perguntas na marca de 4:00 minutos usando recursos da plataforma (ex: Hotmart Sparkle, Teachable).
            *   **Bônus/Downloads**: Mencionar e disponibilizar materiais complementares (planilhas, códigos-fonte) na descrição ou seção de recursos.
            *   **Gamificação**: Implementar badges ou pontos para conclusão de módulos ou participação em fóruns de discussão.
            *   **Discussão**: Propor uma pergunta aberta no final do vídeo para incentivar comentários na seção de perguntas e respostas da plataforma.
    *   **Resultado**: Aumentar a interação do aluno e a taxa de retenção do conteúdo através de feedback imediato e recursos adicionais.

---

## Templates

### Template de Roteiro de Aula em Vídeo

```
MÓDULO 3: Fundamentos de Edição de Vídeo com DaVinci Resolve
AULA 1: Interface e Fluxo de Trabalho (Duração Estimada: 8 min)

[0:00-0:15] INTRO (Música tema + Logo Skill | Locutor: "Bem-vindo à aula de DaVinci Resolve!")
[0:15-0:45] GANCHO (Vídeo Abertura: "Você quer criar vídeos que impressionam? O DaVinci Resolve é sua ferramenta secreta, e hoje vamos desvendá-la.")
[0:45-1:30] TÓPICO 1: Visão Geral da Interface (Tela dividida: locutor + captura de tela do DaVinci com áreas destacadas)
    - Explicar áreas-chave: Media Pool, Cut, Edit, Fusion, Color, Fairlight, Deliver.
    - Demonstração rápida de navegação entre as páginas.
[1:30-3:00] TÓPICO 2: Importando Mídia (Captura de tela, passo a passo, arrastando arquivos para Media Pool)
    - Arrastar e soltar arquivos de vídeo, áudio e imagem.
    - Criar "bins" (pastas) para organização de projetos e mídias.
    - Exemplo: Importar "video_aula_bruto.mp4", "audio_limpo.wav", "logo_skill.png".
[3:00-5:30] TÓPICO 3: Linha do Tempo e Cortes Básicos (Prática guiada na página Edit)
    - Adicionar clipes à linha do tempo principal.
    - Ferramentas de corte rápido (Blade tool, atalho B).
    - Mover e reorganizar clipes.
    - Utilizar os atalhos JKL para reprodução e navegação.
    - Exemplo: Cortar uma pausa de 2 segundos no meio da fala.
[5:30-7:00] REVISÃO RÁPIDA (Slide com bullet points dos tópicos abordados: Interface, Importação, Linha do Tempo, Cortes)
[7:00-7:45] PRÓXIMOS PASSOS / CTA (Locutor: "Na próxima aula, vamos adicionar transições e efeitos básicos. Baixe o projeto desta aula na descrição para praticar!")
[7:45-8:00] ENCERRAMENTO (Música tema + Créditos | Logo Skill)
```

### Template de Checklist de Qualidade de Vídeo Final

```
CHECKLIST DE QUALIDADE DO VÍDEO FINAL - MÓDULO 3 / AULA 1

[X] Resolução 1920x1080p (Full HD) ou superior (confere)
[X] Taxa de quadros 29.97 FPS ou 25 FPS (consistente em todo o vídeo)
[X] Áudio limpo, sem ruídos de fundo perceptíveis ou clipping
[X] Níveis de áudio entre -12dB e -6dB (pico máximo em -3dB)
[X] Sincronização labial perfeita entre áudio e vídeo em todas as cenas
[X] Iluminação adequada, sem sombras duras no rosto do apresentador ou fundo
[X] Cores equilibradas, sem saturação ou desaturação excessiva (correção de cor aplicada)
[X] Edição fluida, sem cortes abruptos, pulos ou transições desnecessárias
[X] Legendas (SRT) revisadas, sem erros ortográficos e sincronizadas (se aplicável)
[X] Marca d'água ou logo da Skill posicionada corretamente e com transparência adequada
[X] Chamadas para ação (CTAs) claras, visíveis e bem temporizadas (ex: link para material extra)
[X] Mídia de apoio (slides, b-rolls, gráficos) relevante, de alta qualidade e com boa legibilidade
[X] Sem erros de digitação em textos na tela, slides ou legendas
[X] Tamanho final do arquivo otimizado para streaming (ex: ~100MB para 8 min H.264 em 1080p)
[X] Nome do arquivo padronizado (ex: Modulo03_Aula01_InterfaceDaVinci.mp4)
```

---

## Checklist

-   [ ] Áudio limpo e sem ruído de fundo perceptível.
-   [ ] Níveis de áudio consistentes, entre -12dB e -6dB.
-   [ ] Iluminação com três pontos (key, fill, back light) bem balanceada.
-   [ ] Resolução de vídeo 1920x1080p (Full HD) ou superior.
-   [ ] Sincronização labial perfeita entre áudio e vídeo.
-   [ ] Roteiro revisado e ensaiado para fluidez da apresentação.
-   [ ] Inserção de b-rolls e recursos visuais para ilustrar pontos-chave.
-   [ ] Chamadas para ação (CTAs) claras e estrategicamente posicionadas.
-   [ ] Exportação final em H.264 MP4 com bitrate otimizado para streaming.
-   [ ] Legendas (SRT) geradas, revisadas e sincronizadas.

---

## Métricas de Referência

| Métrica                        | Benchmark da Indústria (EAD) | Meta (Skill Aplicada) |
|--------------------------------|------------------------------|-----------------------|
| Taxa de Conclusão de Curso     | 10-15%                       | > 25%                 |
| Retenção de Conteúdo por Módulo | 50-60%                       | > 70%                 |
| Engajamento (Comentários/Quiz) | 5-10% dos alunos             | > 15% dos alunos      |
| NPS (Net Promoter Score)       | 30-40                        | > 50                  |
| Tempo Médio de Visualização    | 60-70% da duração total      | > 80% da duração total|
| Taxa de Erros em Quizzes       | 20-30%                       | < 15%                 |

---

## Erros Comuns

1.  **Áudio Inaudível ou com Ruído Excessivo**: O principal fator de desistência em cursos em vídeo.
    *   **Como evitar**: Sempre testar o microfone antes da gravação, monitorar com fones de ouvido durante, e aplicar técnicas de masterização de áudio (redução de ruído, compressão, equalização) na pós-produção. Exemplo: Um áudio com "chiado" constante a -30dB deve ser tratado com noise reduction de pelo menos 10dB.

2.  **Conteúdo Denso Demais em Vídeos Longos**: Gera fadiga e baixa retenção.
    *   **Como evitar**: Adotar a metodologia de microlearning, dividindo o conteúdo em vídeos de 7-12 minutos, focados em um único conceito. Exemplo: Em vez de um vídeo de 30 minutos sobre "Introdução ao Marketing Digital", criar três vídeos de 10 minutos: "O que é Marketing Digital?", "Pilares do Marketing de Conteúdo" e "Métricas Essenciais".

3.  **Falta de Chamadas para Ação (CTAs)**: Impede a interação e a prática do aluno.
    *   **Como evitar**: Integrar CTAs claras e específicas no roteiro e na edição. Exemplo: Ao final de um vídeo sobre código, "Baixe o código-fonte na descrição e tente replicar!" ou "Deixe suas dúvidas nos comentários abaixo, responderei pessoalmente!". Isso direciona o aluno para a próxima etapa.

---

## Dicas Avançadas

1.  **Utilização Estratégica de B-rolls Contextuais**: Além de ilustrar, b-rolls podem quebrar a monotonia visual. Em vez de apenas uma captura de tela, use um b-roll de 5 segundos mostrando alguém usando o software de forma produtiva para gerar aspiração.
2.  **Masterização de Áudio com Compressão Multibanda**: Para um controle mais refinado do áudio, aplique compressão multibanda em vez de um compressor simples. Isso permite nivelar frequências específicas (ex: controlar booms em baixas frequências e sibilância em altas) sem afetar o resto do espectro, resultando em um som mais polido e profissional.
3.  **A/B Testing de Miniaturas de Vídeo e Títulos**: Em plataformas que permitem, teste diferentes miniaturas (thumbnails) e títulos para suas aulas. Uma miniatura com contraste alto e texto claro (ex: "PYTHON PARA INICIANTES" em fonte grande) e um título que gera curiosidade (ex: "Desvende Python em 10 Minutos!") podem aumentar a taxa de cliques em 20-30%.
4.  **Criação de Quizzes Adaptativos**: Desenvolva quizzes que ajustam a dificuldade ou o tipo de pergunta com base no desempenho anterior do aluno. Se o aluno erra uma questão sobre um conceito, o próximo quiz pode incluir mais perguntas sobre esse conceito específico, reforçando o aprendizado de forma personalizada.
5.  **Análise de Mapas de Calor e Retenção de Audiência**: Utilize ferramentas de análise de vídeo (como as oferecidas por plataformas como Vimeo Business ou Hotmart Analytics) para identificar exatamente em que ponto os alunos estão abandonando o vídeo. Se houver uma queda brusca de 40% aos 5 minutos, investigue o conteúdo ou a apresentação naquele ponto para otimização futura.