---
name: rollout-expandir
description: Expande rollout para próximo segmento — favo 04
argument-hint: "<id> <segmento>"
agent: rollout-coordinator
subagent: true
model: sonnet
allowed-tools:
  - read
  - edit
permissions:
  allow:
    - Read(colmeia/**)
    - Write(colmeia/04-construcao/_iniciativas/**/rollout*)
---

@colmeia/04-construcao/modelo-rollout.md

ID: **$1** | Segmento: **$2**

1. Exigir `validacao-head-$1.md` com APROVAR_EXPANSAO (ROL-01)
2. Expandir segmento $2 via feature flags
3. Atualizar `rollout-state.yaml`
4. Head pode revalidar com `/validar-rollout-head` entre expansões
