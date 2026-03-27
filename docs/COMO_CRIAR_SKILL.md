# Como criar sua propria skill

Este guia ensina voce a escrever uma skill do zero. Ao final, voce tera um arquivo `SKILL.md` pronto para usar no Claude ou contribuir para este repositorio.

---

## O que e uma skill?

Uma skill e um arquivo de texto (`SKILL.md`) que da instrucoes especializadas ao Claude. Quando voce carrega uma skill, o Claude passa a agir como um especialista naquele assunto.

Pense assim:
- **Sem skill:** "Claude, avalia esse design pra mim" → resposta generica
- **Com skill (critique):** "Claude, /critique" → avaliacao profissional de 10 dimensoes com relatorio estruturado

A diferenca e que a skill diz **exatamente como** o Claude deve pensar, analisar e responder.

---

## Estrutura de uma skill

Todo arquivo `SKILL.md` tem duas partes:

### 1. Frontmatter (metadados)

Fica no topo do arquivo, entre `---`. Informa o nome, descricao e nivel de risco.

```yaml
---
name: minha-skill
description: Uma descricao clara do que a skill faz e quando usar.
risk: safe
---
```

**Campos obrigatorios:**

| Campo | O que e | Exemplo |
|-------|---------|---------|
| `name` | Nome em kebab-case (minusculo, separado por hifen) | `critique`, `meta-ads-campaign` |
| `description` | Frase curta explicando o que a skill faz (ate 200 caracteres) | "Avalia eficacia de design do ponto de vista de UX" |
| `risk` | Nivel de risco da skill | `none`, `safe`, `critical`, `offensive` |

**Campos opcionais:**

| Campo | O que e | Exemplo |
|-------|---------|---------|
| `user-invokable` | Se o usuario pode chamar com `/nome` | `true` |
| `args` | Argumentos que a skill aceita | ver exemplo abaixo |
| `source` | URL da fonte original | `https://github.com/...` |

**Niveis de risco:**

| Nivel | Quando usar | Exemplo |
|-------|-------------|---------|
| `none` | So gera texto, sem efeitos colaterais | Brainstorming, copywriting |
| `safe` | Le arquivos ou roda comandos seguros | Linter, analise de codigo |
| `critical` | Modifica arquivos, faz deploy, acessa APIs | Git push, deploy, envio de emails |
| `offensive` | Ferramentas de pentest/seguranca ofensiva | Scanner de vulnerabilidades |

### 2. Corpo (instrucoes)

Tudo que vem depois do frontmatter sao as instrucoes que o Claude vai seguir. E aqui que voce define **como** o Claude deve se comportar.

---

## Exemplo real: a skill "critique"

Vamos analisar a skill `critique` deste repositorio para entender cada parte.

### Frontmatter

```yaml
---
name: critique
description: Evaluate design effectiveness from a UX perspective. Assesses visual hierarchy, information architecture, emotional resonance, and overall design quality with actionable feedback.
user-invokable: true
args:
  - name: area
    description: The feature or area to critique (optional)
    required: false
risk: safe
---
```

O que aprendemos:
- `user-invokable: true` permite chamar com `/critique` no chat
- `args` define um argumento opcional (`area`) para focar a avaliacao
- `risk: safe` porque so analisa, nao modifica nada

### Corpo — as instrucoes

O corpo da skill `critique` segue esta estrutura:

**1. Introducao e papel:**
```
Conduct a holistic design critique, evaluating whether the interface
actually works—not just technically, but as a designed experience.
Think like a design director giving feedback.
```

Diz ao Claude **quem** ele e (diretor de design) e **o que** deve fazer (avaliacao holistica).

**2. Dimensoes de analise (10 secoes):**

Cada secao e um aspecto que o Claude deve avaliar:
- AI Slop Detection (detectar se parece feito por IA)
- Visual Hierarchy (hierarquia visual)
- Information Architecture (arquitetura de informacao)
- Emotional Resonance (ressonancia emocional)
- ...e mais 6 dimensoes

Cada dimensao tem **perguntas guia** que orientam a analise:
```markdown
### 2. Visual Hierarchy
- Does the eye flow to the most important element first?
- Is there a clear primary action? Can you spot it in 2 seconds?
```

**3. Formato de saida:**

Define exatamente como o relatorio deve ser estruturado:
- Anti-Patterns Verdict (pass/fail)
- Overall Impression (impressao geral)
- What's Working (o que funciona)
- Priority Issues (problemas prioritarios)
- Minor Observations (observacoes menores)
- Questions to Consider (perguntas provocativas)

**4. Regras de comportamento:**

No final, reforca o tom:
```
- Be direct—vague feedback wastes everyone's time
- Be specific—"the submit button" not "some elements"
- Prioritize ruthlessly—if everything is important, nothing is
```

---

## Criando sua skill do zero

Vamos criar uma skill simples juntos. Suponha que voce quer uma skill de **analise de landing page**.

### Passo 1: Defina o frontmatter

```yaml
---
name: analise-landing-page
description: Analisa landing pages identificando pontos de friccao, oportunidades de conversao e melhorias de copy. Gera relatorio com prioridades.
user-invokable: true
risk: none
---
```

### Passo 2: Defina o papel

Comece dizendo ao Claude quem ele e e como deve pensar:

```markdown
Voce e um especialista em CRO (Conversion Rate Optimization) com 10 anos
de experiencia analisando landing pages de alta conversao. Analise a
landing page fornecida como se estivesse fazendo uma consultoria de R$5.000.
```

**Dica:** Quanto mais especifico o papel, melhor o resultado. "Especialista em CRO com 10 anos" e melhor que "analista de marketing".

### Passo 3: Defina as dimensoes de analise

Liste cada aspecto que o Claude deve avaliar:

```markdown
## Analise da Landing Page

Avalie a pagina nas seguintes dimensoes:

### 1. Proposta de Valor (Above the Fold)
- A headline comunica o beneficio principal em menos de 5 segundos?
- O subtitulo explica como o produto/servico entrega esse beneficio?
- Existe uma imagem ou video que reforça a mensagem?

### 2. Copy e Persuasao
- A copy fala de beneficios ou de funcionalidades?
- Existe prova social (depoimentos, numeros, logos)?
- Os CTAs sao claros e orientados a acao?

### 3. Estrutura e Fluxo
- A pagina segue uma progressao logica?
- Existe conteudo demais antes do primeiro CTA?
- As secoes respondem as objecoes na ordem certa?
```

### Passo 4: Defina o formato de saida

Diga ao Claude exatamente como estruturar a resposta:

```markdown
## Relatorio

Estruture sua analise assim:

### Veredicto Rapido
Uma frase: a pagina converte ou perde visitantes? Nota de 1 a 10.

### O Que Funciona
2-3 pontos fortes com explicacao do por que funcionam.

### Problemas Prioritarios
Os 3-5 maiores problemas, ordenados por impacto na conversao:

Para cada problema:
- **O que:** descreva o problema
- **Por que importa:** como isso afeta a conversao
- **Como resolver:** sugestao concreta e acionavel

### Quick Wins
Mudancas que levam menos de 1 hora e podem melhorar a conversao.
```

### Passo 5: Adicione regras de comportamento

```markdown
**Regras:**
- Seja direto e honesto — feedback vago nao ajuda ninguem
- De sugestoes concretas, nao "considere explorar..."
- Priorize impacto na conversao acima de estetica
- Se a pagina estiver boa, diga isso — nao invente problemas
```

### Resultado final

O arquivo completo `SKILL.md` fica assim:

```markdown
---
name: analise-landing-page
description: Analisa landing pages identificando pontos de friccao, oportunidades de conversao e melhorias de copy. Gera relatorio com prioridades.
user-invokable: true
risk: none
---

Voce e um especialista em CRO (Conversion Rate Optimization) com 10 anos
de experiencia analisando landing pages de alta conversao. Analise a
landing page fornecida como se estivesse fazendo uma consultoria de R$5.000.

## Analise da Landing Page

Avalie a pagina nas seguintes dimensoes:

### 1. Proposta de Valor (Above the Fold)
- A headline comunica o beneficio principal em menos de 5 segundos?
- O subtitulo explica como o produto/servico entrega esse beneficio?
- Existe uma imagem ou video que reforça a mensagem?

### 2. Copy e Persuasao
- A copy fala de beneficios ou de funcionalidades?
- Existe prova social (depoimentos, numeros, logos)?
- Os CTAs sao claros e orientados a acao?

### 3. Estrutura e Fluxo
- A pagina segue uma progressao logica?
- Existe conteudo demais antes do primeiro CTA?
- As secoes respondem as objecoes na ordem certa?

## Relatorio

Estruture sua analise assim:

### Veredicto Rapido
Uma frase: a pagina converte ou perde visitantes? Nota de 1 a 10.

### O Que Funciona
2-3 pontos fortes com explicacao do por que funcionam.

### Problemas Prioritarios
Os 3-5 maiores problemas, ordenados por impacto na conversao:

Para cada problema:
- **O que:** descreva o problema
- **Por que importa:** como isso afeta a conversao
- **Como resolver:** sugestao concreta e acionavel

### Quick Wins
Mudancas que levam menos de 1 hora e podem melhorar a conversao.

**Regras:**
- Seja direto e honesto — feedback vago nao ajuda ninguem
- De sugestoes concretas, nao "considere explorar..."
- Priorize impacto na conversao acima de estetica
- Se a pagina estiver boa, diga isso — nao invente problemas
```

---

## Dicas para escrever skills melhores

### Seja especifico, nao generico

```
# Ruim
Voce e um especialista em marketing.

# Bom
Voce e um gestor de trafego pago com experiencia em Meta Ads para
e-commerce de moda, especializado em campanhas de ROAS acima de 4x.
```

### Use perguntas guia

Em vez de "analise o SEO", de perguntas que o Claude deve responder:

```
- O title tag tem a keyword principal nos primeiros 60 caracteres?
- A meta description tem um CTA claro?
- Existe apenas um H1 na pagina?
```

### Defina o formato de saida

O Claude segue instrucoes de formatacao muito bem. Diga exatamente como quer o resultado:

```
Para cada problema encontrado, use este formato:
- **Problema:** [descricao]
- **Impacto:** [alto/medio/baixo]
- **Solucao:** [acao concreta]
```

### Use tom imperativo

```
# Menos eficaz
Voce poderia analisar os titulos da pagina.

# Mais eficaz
Analise cada titulo da pagina. Para cada um, avalie clareza,
relevancia e apelo emocional.
```

### Adicione restricoes

Restricoes focam o Claude e evitam respostas genericas:

```
**Restricoes:**
- Maximo 5 problemas prioritarios (force priorizacao)
- Cada sugestao deve ser implementavel em menos de 2 horas
- Nao sugira redesign completo — foque em melhorias incrementais
```

---

## Testando sua skill

### No claude.ai

1. Va em **Personalizar** → **Habilidades** → **+**
2. Faca upload do seu `SKILL.md`
3. No chat, teste com um caso real
4. Ajuste as instrucoes com base no resultado

### Validacao automatica

Se for contribuir para este repositorio:

```bash
python3 scripts/catalog.py --issues-only    # verifica qualidade
python3 scripts/infer_risk.py --stats       # verifica classificacao de risk
python3 -m pytest scripts/test_*.py -v      # roda testes
```

---

## Publicando sua skill

### Neste repositorio

1. Faca um fork de [github.com/kursku/skills](https://github.com/kursku/skills)
2. Crie a pasta da sua skill: `packs/kit-510-ptbr/<categoria>/<nome-da-skill>/`
3. Adicione o `SKILL.md` dentro da pasta
4. Abra um Pull Request

### Apenas para voce

Se nao quiser publicar, basta fazer upload do `SKILL.md` em **Personalizar → Habilidades** no claude.ai. A skill fica disponivel em todos os seus chats.

---

## Checklist antes de publicar

- [ ] `name` em kebab-case e corresponde ao nome da pasta
- [ ] `description` clara, com ate 200 caracteres
- [ ] `risk` definido (none/safe/critical/offensive)
- [ ] Instrucoes especificas (nao genericas)
- [ ] Formato de saida definido
- [ ] Testada com pelo menos um caso real
- [ ] Sem informacoes sensiveis (senhas, API keys, dados pessoais)
