---
favo: 04-construcao
versao: 2.0
skill_primaria: spec-funcional
---

# Mapa Agentes ↔ Skills (favo 04)

**Head de Produto = `builder-lead`** — orquestra SDD e rollout; não lê código.

```
                    ┌─────────────────────────┐
                    │ builder-lead (Head GTM) │
                    └───────────┬─────────────┘
        ┌───────────┼───────────┼───────────┬──────────────┐
        ▼           ▼           ▼           ▼              ▼
  spec-funcional  spec-nfr   spec-tech   task-decomposer  rollout-coordinator
     writer ⊂      writer ⊂   writer ⊂        ⊂               ⊂
        │           │           │           │              │
        └───────────┴───────────┴───────────┴──────────────┘
                              implementador ⊂
                              pipeline-guardian ⊂
                              reviewer ⊂
```

| Skill | Agent | Sub? |
|-------|-------|------|
| `/spec-funcional` | `spec-funcional-writer` | ⊂ |
| `/spec-nao-funcional` | `spec-nfr-writer` | ⊂ |
| `/spec-tecnica` | `spec-tech-writer` | ⊂ |
| `/decompor-tarefas` | `task-decomposer` | ⊂ |
| `/implementar-tarefa` | `implementador` | ⊂ |
| `/ci-validar` / `/pipeline-validar` | `pipeline-guardian` | ⊂ |
| `/cd-promover` | `cd-coordinator` | ⊂ |
| `/cd-status` | `builder-lead` | — |
| `/rollout-canario` | `rollout-coordinator` | ⊂ |
| `/validar-rollout-head` | `builder-lead` | — |
| `/rollout-expandir` | `rollout-coordinator` | ⊂ |
| `/rollout-status` | `builder-lead` | — |
| `/prep-release` | `builder-lead` | — |
| `/review-pr` | `reviewer` | ⊂ |

## Contratos resumidos

- **spec-funcional-writer:** linguagem cliente; gera `resumo-head.md`
- **spec-tech-writer:** monorepo + integrações; nunca expor jargão ao Head
- **implementador:** entrega código + testes no monorepo config
- **pipeline-guardian:** CI apenas — artefato com commit_hash
- **cd-coordinator:** promove hash imutável Sandbox → Homolog (SV/mock) → Produção
- **rollout-coordinator:** executa flags/segmentos; Head valida métricas
