# Anatomia de uma Skill - Entendendo a Estrutura

**Quer entender como as skills funcionam por dentro?** Este guia detalha cada parte de um arquivo de skill.

---

## 📁 Estrutura Básica de Pastas

```
skills/
└── my-skill-name/
    ├── SKILL.md              ← Obrigatório: A definição principal da skill
    ├── examples/             ← Opcional: Arquivos de exemplo
    │   ├── example1.js
    │   └── example2.py
    ├── scripts/              ← Opcional: Scripts auxiliares
    │   └── helper.sh
    ├── templates/            ← Opcional: Templates de código
    │   └── template.tsx
    ├── references/           ← Opcional: Documentação de referência
    │   └── api-docs.md
    └── README.md             ← Opcional: Documentação adicional
```

**Regra principal:** Apenas o `SKILL.md` é obrigatório. Todo o resto é opcional!

---

## Estrutura do SKILL.md

Todo arquivo `SKILL.md` tem duas partes principais:

### 1. Frontmatter (Metadados)

### 2. Conteúdo (Instruções)

Vamos detalhar cada parte:

---

## Parte 1: Frontmatter

O frontmatter fica no topo do arquivo, entre `---`:

```markdown
---
name: my-skill-name
description: "Breve descrição do que esta skill faz"
---
```

### Campos Obrigatórios

#### `name`

- **O que é:** O identificador da skill
- **Formato:** lowercase-com-hifens
- **Deve corresponder:** Exatamente ao nome da pasta
- **Exemplo:** `stripe-integration`

#### `description`

- **O que é:** Resumo em uma frase
- **Formato:** String entre aspas
- **Tamanho:** Mantenha abaixo de 200 caracteres (o validador exige isso)
- **Exemplo:** `"Stripe payment integration patterns including checkout, subscriptions, and webhooks"`

### Campos Opcionais

Algumas skills incluem metadados adicionais:

```markdown
---
name: my-skill-name
description: "Breve descrição"
risk: "safe" # none | safe | critical | offensive (veja QUALITY_BAR.md)
source: "community"
tags: ["react", "typescript"]
date_added: "2024-01-15"
---
```

#### `date_added`

- **O que é:** A data em que a skill foi criada ou adicionada à coleção
- **Formato:** `YYYY-MM-DD` (formato de data ISO 8601)
- **Propósito:** Ajuda a rastrear versionamento de skills e contribuições da comunidade
- **Obrigatório:** Não (opcional, mas recomendado)
- **Exemplo:** `date_added: "2024-01-15"`
- **Nota:** Pode ser gerenciado automaticamente com o script `scripts/manage_skill_dates.py`

---

## Parte 2: Conteúdo

Após o frontmatter vem o conteúdo da skill. Aqui está a estrutura recomendada:

### Seções Recomendadas

#### 1. Título (H1)

```markdown
# Título da Skill
```

- Use um título claro e descritivo
- Geralmente corresponde ou expande o nome da skill

#### 2. Visão Geral

```markdown
## Overview

Uma breve explicação do que esta skill faz e por que ela existe.
2 a 4 frases é o ideal.
```

#### 3. Quando Usar

```markdown
## When to Use This Skill

- Use quando precisar de [cenário 1]
- Use ao trabalhar com [cenário 2]
- Use quando o usuário perguntar sobre [cenário 3]
```

**Por que isso importa:** Ajuda a IA a saber quando ativar esta skill

#### 4. Instruções Principais

```markdown
## How It Works

### Step 1: [Ação]

Instruções detalhadas...

### Step 2: [Ação]

Mais instruções...
```

**Este é o coração da skill** - passos claros e acionáveis

#### 5. Exemplos

```markdown
## Examples

### Example 1: [Caso de Uso]

\`\`\`javascript
// Código de exemplo
\`\`\`

### Example 2: [Outro Caso de Uso]

\`\`\`javascript
// Mais código
\`\`\`
```

**Por que exemplos importam:** Eles mostram à IA exatamente como deve ser uma boa saída

#### 6. Boas Práticas

```markdown
## Best Practices

- ✅ Faça isso
- ✅ Também faça isso
- ❌ Não faça isso
- ❌ Evite isso
```

#### 7. Armadilhas Comuns

```markdown
## Common Pitfalls

- **Problema:** Descrição
  **Solução:** Como resolver
```

#### 8. Skills Relacionadas

```markdown
## Related Skills

- `@other-skill` - Quando usar esta ao invés
- `@complementary-skill` - Como estas funcionam juntas
```

---

## Escrevendo Instruções Eficazes

### Use Linguagem Clara e Direta

**❌ Ruim:**

```markdown
You might want to consider possibly checking if the user has authentication.
```

**✅ Bom:**

```markdown
Check if the user is authenticated before proceeding.
```

### Use Verbos de Ação

**❌ Ruim:**

```markdown
The file should be created...
```

**✅ Bom:**

```markdown
Create the file...
```

### Seja Específico

**❌ Ruim:**

```markdown
Set up the database properly.
```

**✅ Bom:**

```markdown
1. Create a PostgreSQL database
2. Run migrations: `npm run migrate`
3. Seed initial data: `npm run seed`
```

---

## Componentes Opcionais

### Diretório de Scripts

Se sua skill precisar de scripts auxiliares:

```
scripts/
├── setup.sh          ← Automação de setup
├── validate.py       ← Ferramentas de validação
└── generate.js       ← Geradores de código
```

**Referencie-os no SKILL.md:**

```markdown
Execute o script de setup:
\`\`\`bash
bash scripts/setup.sh
\`\`\`
```

### Diretório de Exemplos

Exemplos reais que demonstram a skill:

```
examples/
├── basic-usage.js
├── advanced-pattern.ts
└── full-implementation/
    ├── index.js
    └── config.json
```

### Diretório de Templates

Templates de código reutilizáveis:

```
templates/
├── component.tsx
├── test.spec.ts
└── config.json
```

**Referencie no SKILL.md:**

```markdown
Use este template como ponto de partida:
\`\`\`typescript
{{#include templates/component.tsx}}
\`\`\`
```

### Diretório de Referências

Documentação externa ou referências de API:

```
references/
├── api-docs.md
├── best-practices.md
└── troubleshooting.md
```

---

## Diretrizes de Tamanho

### Skill Mínima Viável

- **Frontmatter:** name + description
- **Conteúdo:** 100-200 palavras
- **Seções:** Visão Geral + Instruções

### Skill Padrão

- **Frontmatter:** name + description
- **Conteúdo:** 300-800 palavras
- **Seções:** Visão Geral + Quando Usar + Instruções + Exemplos

### Skill Completa

- **Frontmatter:** name + description + campos opcionais
- **Conteúdo:** 800-2000 palavras
- **Seções:** Todas as seções recomendadas
- **Extras:** Scripts, exemplos, templates

**Regra geral:** Comece pequeno, expanda com base no feedback

---

## Boas Práticas de Formatação

### Use Markdown de Forma Eficaz

#### Blocos de Código

Sempre especifique a linguagem:

```markdown
\`\`\`javascript
const example = "code";
\`\`\`
```

#### Listas

Use formatação consistente:

```markdown
- Item 1
- Item 2
  - Sub-item 2.1
  - Sub-item 2.2
```

#### Ênfase

- **Negrito** para termos importantes: `**importante**`
- _Itálico_ para ênfase: `*ênfase*`
- `Código` para comandos/código: `` `código` ``

#### Links

```markdown
[Texto do link](https://example.com)
```

---

## ✅ Checklist de Qualidade

Antes de finalizar sua skill:

### Qualidade do Conteúdo

- [ ] Instruções são claras e acionáveis
- [ ] Exemplos são realistas e úteis
- [ ] Sem erros de digitação ou gramática
- [ ] Precisão técnica verificada

### Estrutura

- [ ] Frontmatter é YAML válido
- [ ] Nome corresponde ao nome da pasta
- [ ] Seções estão organizadas logicamente
- [ ] Headings seguem a hierarquia (H1 → H2 → H3)

### Completude

- [ ] Visão geral explica o "por quê"
- [ ] Instruções explicam o "como"
- [ ] Exemplos mostram o "o quê"
- [ ] Edge cases são abordados

### Usabilidade

- [ ] Um iniciante conseguiria seguir
- [ ] Um especialista acharia útil
- [ ] A IA consegue interpretar corretamente
- [ ] Resolve um problema real

---

## 🔍 Análise de Exemplo Real

Vamos analisar uma skill real: `brainstorming`

```markdown
---
name: brainstorming
description: "You MUST use this before any creative work..."
---
```

**Análise:**

- ✅ Nome claro
- ✅ Descrição forte com urgência ("MUST use")
- ✅ Explica quando usar

```markdown
# Brainstorming Ideas Into Designs

## Overview

Help turn ideas into fully formed designs...
```

**Análise:**

- ✅ Título claro
- ✅ Visão geral concisa
- ✅ Explica a proposta de valor

```markdown
## The Process

**Understanding the idea:**

- Check out the current project state first
- Ask questions one at a time
```

**Análise:**

- ✅ Dividido em fases claras
- ✅ Passos específicos e acionáveis
- ✅ Fácil de seguir

---

## Padrões Avançados

### Lógica Condicional

```markdown
## Instructions

If the user is working with React:

- Use functional components
- Prefer hooks over class components

If the user is working with Vue:

- Use Composition API
- Follow Vue 3 patterns
```

### Revelação Progressiva

```markdown
## Basic Usage

[Instruções simples para casos comuns]

## Advanced Usage

[Padrões complexos para usuários avançados]
```

### Referências Cruzadas

```markdown
## Related Workflows

1. First, use `@brainstorming` to design
2. Then, use `@writing-plans` to plan
3. Finally, use `@test-driven-development` to implement
```

---

## Métricas de Eficácia

Como saber se sua skill é boa:

### Teste de Clareza

- Alguém sem conhecimento do tema conseguiria seguir?
- Existe alguma instrução ambígua?

### Teste de Completude

- Cobre o caminho feliz (happy path)?
- Lida com edge cases?
- Cenários de erro são abordados?

### Teste de Utilidade

- Resolve um problema real?
- Você usaria isso no seu dia a dia?
- Economiza tempo ou melhora a qualidade?

---

## Aprendendo com Skills Existentes

### Estude Estes Exemplos

**Para Iniciantes:**

- `skills/brainstorming/SKILL.md` - Estrutura clara
- `skills/git-pushing/SKILL.md` - Simples e focada
- `skills/copywriting/SKILL.md` - Bons exemplos

**Para Avançados:**

- `skills/systematic-debugging/SKILL.md` - Completa
- `skills/react-best-practices/SKILL.md` - Múltiplos arquivos
- `skills/loki-mode/SKILL.md` - Workflows complexos

---

## 💡 Dicas Importantes

1. **Comece pela seção "When to Use"** - Isso clarifica o propósito da skill
2. **Escreva os exemplos primeiro** - Eles ajudam a entender o que você está ensinando
3. **Teste com uma IA** - Veja se realmente funciona antes de submeter
4. **Peça feedback** - Peça para outros revisarem sua skill
5. **Itere** - Skills melhoram com o tempo baseado no uso

---

## Erros Comuns a Evitar

### ❌ Erro 1: Vago Demais

```markdown
## Instructions

Make the code better.
```

**✅ Correção:**

```markdown
## Instructions

1. Extract repeated logic into functions
2. Add error handling for edge cases
3. Write unit tests for core functionality
```

### ❌ Erro 2: Complexo Demais

```markdown
## Instructions

[5000 palavras de jargão técnico denso]
```

**✅ Correção:**
Divida em múltiplas skills ou use revelação progressiva

### ❌ Erro 3: Sem Exemplos

```markdown
## Instructions

[Instruções sem nenhum exemplo de código]
```

**✅ Correção:**
Adicione pelo menos 2-3 exemplos realistas

### ❌ Erro 4: Informação Desatualizada

```markdown
Use React class components...
```

**✅ Correção:**
Mantenha as skills atualizadas com as melhores práticas atuais

---

## 🎯 Próximos Passos

1. **Leia 3-5 skills existentes** para ver diferentes estilos
2. **Experimente o template de skill** do CONTRIBUTING.md
3. **Crie uma skill simples** sobre algo que você domina
4. **Teste** com seu assistente de IA
5. **Compartilhe** via Pull Request

---

**Lembre-se:** Todo especialista já foi iniciante. Comece simples, aprenda com o feedback e melhore com o tempo! 🚀
