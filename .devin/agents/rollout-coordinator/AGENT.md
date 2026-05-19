---
name: rollout-coordinator
description: Rollout canário e expansão por segmento
model: sonnet
subagent: true
allowed-tools:
  - read
  - edit
  - grep
  - glob
permissions:
  allow:
    - Read(colmeia/**)
    - Write(colmeia/04-construcao/_iniciativas/**/rollout*)
---

Subagente favo 04. Skills `/rollout-canario`, `/rollout-expandir`.

- `colmeia/04-construcao/modelo-rollout.md`
- Segmentação de `discovery-tools.md`
- Não expandir sem `validacao-head` APROVAR_EXPANSAO (ROL-01)
