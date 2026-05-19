---
favo: 00-nucleo
skill: orquestrar-producao
---

# Skill: Orquestrar Produção

**Comando:** `/orquestrar-producao {id}`

## Função

Determinar favo atual, lacunas de artefatos vs `gates.md`, e sequência de skills.

Regras de roteamento: [modelo-experimentacao-discovery.md](./modelo-experimentacao-discovery.md) · ordem favo 04: [ciclo-completo.md](./ciclo-completo.md)

## Não faz

- Gerar conteúdo de produto
- Aprovar gates

## Output (markdown na conversa ou arquivo opcional)

```markdown
## Orquestração — {id}
### Favo atual
### Artefatos presentes / faltantes
### Próximas skills (ordem)
### Lacunas [FORNECER]
```

## Implementação

`.devin/skills/orquestrar-producao/SKILL.md`
