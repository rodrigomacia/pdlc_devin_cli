---
favo: 03-experimentacao
versao: 2.0
---

# Templates — favo 03

## experiments-backlog.md

```markdown
# Backlog — {id}

| ID | hipotese_ref | historia_id | Tipo | Status | Decisão |
|----|--------------|-------------|------|--------|---------|
| E1 | hip-1 | h-1.1 | prototipo | planejado | |
```

## experimento-{E}.md

```yaml
---
experimento: {E}
hipotese_ref: hip-{n}
historia_ids: [h-1.1]
kr_ref: {kr_id}
---
```

```markdown
## Hipótese
{copiar de hipoteses.yaml}

## Tipo
entrevista | prototipo | pretotype | ab

## Critérios (ANTES da execução)
| Sinal | Sucesso | Falha |

## Resultado
{[RESULTADO: fornecer]}

## Decisão
scale | iterate | pivot | kill | defer
```

## decisao-experimentos.md

```markdown
# Decisões — {id}

| Exp | Decisão | Evidência (cliente real) | Próximo favo | Handoff |
|-----|---------|--------------------------|--------------|---------|
| E1 | scale | ... | 04 | curar-contexto 03 04 |
```

## Atualização feature (se scale)

Em `02-discovery/.../feature-{id}.md` frontmatter:

```yaml
validacao_real: confirmada
experimentos_ref: [E1, E2]
```
