---
favo: 03-experimentacao
versao: 2.0
skill_primaria: design-experimento
---

# Mapa Agentes ↔ Skills (favo 03)

| Skill | Agent | Subagent? |
|-------|-------|-----------|
| `experiments-backlog` | `experiment-lead` | Inline |
| `design-experimento` | `experiment-lead` | Inline |
| `registrar-resultado` | — | Inline |
| `decidir-experimento` | `experiment-lead` | `subagent: true` |

## Contrato experiment-lead

- **Input:** `{id}`, `feature-{id}.md`, `hipoteses.yaml`, `historias.yaml` (favo 02)
- **Output:** `experiments-backlog.md`, `experimento-{E}.md`, `decisao-experimentos.md`
- **Proibido:** critérios pós-resultado; SVM como evidência real; tipo `spike` como experimento de produto
