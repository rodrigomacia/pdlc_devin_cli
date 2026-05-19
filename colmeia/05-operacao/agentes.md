---
favo: 05-operacao
versao: 2.0
---

# Mapa Agentes ↔ Skills (favo 05)

## Operação contínua

| Skill | Agent |
|-------|-------|
| `/review-metricas` | `operador-lead` |
| `/postmortem` | `operador-lead` ⊂ |
| `/insight-para-discovery` | `operador-lead` |

## ERT — Emergency Response Team

```
                    ┌──────────────┐
                    │   ert-lead   │  Incident Commander
                    └──────┬───────┘
           ┌───────────────┼───────────────┐
           ▼               ▼               ▼
     ert-logger      ert-comm      ert-sme-produto + ert-sme-tech
```

| Skill | Agent |
|-------|-------|
| `/ert-abrir` | `ert-lead` |
| `/ert-comandar` | `ert-lead` |
| `/ert-registrar` | `ert-logger` ⊂ |
| `/ert-comunicar` | `ert-comm` ⊂ |
| `/ert-diagnosticar` | `ert-sme-produto` + `ert-sme-tech` ⊂ |
| `/ert-fechar` | `ert-lead` |

## Contrato ert-lead

- Único que muda status do incidente e prioriza ações
- Consulta visão 360° antes de decisões de mitigação
- Escala para Head apenas em sev1 ou impacto regulatório (config)

## Contrato SMEs

- **produto:** prod.*, voc.*, rollout, feature stories
- **tech:** monorepo paths, pipeline, AWS regions, integrações
