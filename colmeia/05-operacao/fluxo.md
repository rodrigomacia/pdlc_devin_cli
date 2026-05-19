---
favo: 05-operacao
versao: 2.0
skill_primaria: review-metricas
---

# Fluxo — Operação + ERT (favo 05)

Modelo ERT: [modelo-ert.md](./modelo-ert.md)

## Operação contínua

```mermaid
flowchart LR
  H[Handoff 04→05] --> M[/review-metricas/]
  M --> G1[/grill-me metricas/]
  G1 --> RS[/rollout-status se ativo/]
  RS --> P[/postmortem se incidente/]
  P --> I[/insight-para-discovery/]
  I --> G2[/grill-me insights/]
  G2 --> D[Favo 02 visões]
```

## Fluxo ERT (incidente)

```mermaid
flowchart TB
  T[Alerta / Head reporta] --> A[/ert-abrir/]
  A --> C[/ert-comandar/]
  C --> R[/ert-registrar/]
  C --> CM[/ert-comunicar/]
  C --> D[/ert-diagnosticar produto + tech/]
  D --> C
  C --> F[/ert-fechar/]
  F --> PM[/postmortem/]
```

## Passos ERT

| # | Skill | Output |
|---|-------|--------|
| 1 | `/ert-abrir {id} {ref}` | `incidentes/{ref}/incidente.yaml` |
| 2 | `/ert-comandar {id} {ref}` | `acoes.md` — plano de resposta |
| 3 | `/ert-registrar {id} {ref}` | `timeline.md` |
| 4 | `/ert-comunicar {id} {ref}` | `comunicacoes.md` |
| 5 | `/ert-diagnosticar {id} {ref}` | `visao-360.md` |
| 6 | Loop comandar até resolvido | — |
| 7 | `/ert-fechar {id} {ref}` | `fechamento.md` |
| 8 | `/postmortem {id} {ref}` | aprendizado |
| 9 | `/insight-para-discovery {id}` | loop 02 |

## Parâmetros

- Severidade e segmentos: operador ou alerta MCP
- Métricas: não inventar — `prod.*` ou `[DADO AUSENTE]`
