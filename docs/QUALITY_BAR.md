# 🏆 Padrão de Qualidade & Validação

Para transformar as **Skills para Claude** de uma coleção de scripts em uma plataforma confiável, toda skill precisa atender a um padrão específico de qualidade e segurança.

## O Selo "Validada" ✅

Uma skill recebe o selo "Validada" apenas se passar nestas **5 verificações automatizadas**:

### 1. Integridade dos Metadados

O frontmatter do `SKILL.md` precisa ser um YAML válido e conter:

- `name`: Em kebab-case, correspondendo ao nome da pasta.
- `description`: Até 200 caracteres, com proposta de valor clara.
- `risk`: Um entre `[none, safe, critical, offensive]`. Use `scripts/infer_risk.py` para classificar automaticamente.
- `source`: URL da fonte original (ou "self" se for original).

### 2. Gatilhos Claros ("Quando usar")

A skill PRECISA ter uma seção indicando explicitamente quando deve ser acionada.

- **Bom**: "Use quando o usuário pedir para debugar um componente React."
- **Ruim**: "Essa skill ajuda com código."
Headings aceitos: `## When to Use`, `## Use this skill when`, `## When to Use This Skill`.

### 3. Segurança & Classificação de Risco

Toda skill precisa declarar seu nível de risco:

- 🟢 **none**: Apenas texto/raciocínio (ex.: Brainstorming).
- 🔵 **safe**: Lê arquivos, executa comandos seguros (ex.: Linter).
- 🟠 **critical**: Modifica estado, deleta arquivos, faz push para produção (ex.: Git Push).
- 🔴 **offensive**: Ferramentas de pentest/Red Team. **PRECISA** ter aviso de "Uso Autorizado Apenas".

### 4. Exemplos Prontos para Usar

Pelo menos um bloco de código ou exemplo de interação que o usuário (ou agente) possa utilizar imediatamente.

### 5. Limitações Explícitas

Uma lista de edge cases conhecidos ou coisas que a skill _não consegue_ fazer.

- _Exemplo_: "Não funciona no Windows sem WSL."

---

## Níveis de Suporte

Também categorizamos as skills por quem as mantém:

| Nível         | Selo | Significado                                                  |
| :------------ | :--- | :----------------------------------------------------------- |
| **Oficial**   | 🟣   | Mantida pela equipe principal. Alta confiabilidade.          |
| **Comunidade**| ⚪   | Contribuída pelo ecossistema. Suporte por melhor esforço.    |
| **Verificada**| ✨   | Skill da comunidade que passou por revisão manual detalhada. |

---

## Como Validar Sua Skill

Use os scripts do repositório para validar:

```bash
python3 scripts/catalog.py --issues-only    # listar problemas de qualidade
python3 scripts/infer_risk.py --stats       # verificar classificacao de risk
python3 -m pytest scripts/test_*.py -v      # rodar testes
```
