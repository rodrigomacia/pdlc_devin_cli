---
name: rollout-status
description: Status de rollout em linguagem de negócio — favo 04
argument-hint: "<id>"
agent: builder-lead
model: sonnet
allowed-tools:
  - read
permissions:
  allow:
    - Read(colmeia/**)
---

@colmeia/04-construcao/modelo-rollout.md

ID: **$ARGUMENTS**

1. Ler `rollout-state.yaml`, `rollout-plan-$1.md`
2. Responder na sessão em linguagem Head: % clientes, segmentos ativos, fase, próxima decisão
3. Sem termos: pod, helm, terraform
