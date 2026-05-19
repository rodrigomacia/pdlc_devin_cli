---
name: rollout-rollback
description: Rollback em Produção — reaponta deploy_ref para hash anterior
argument-hint: "<id> [motivo]"
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
    - Write(colmeia/04-construcao/_iniciativas/**/cd-state.yaml)
---

@colmeia/04-construcao/modelo-rollout.md
@colmeia/04-construcao/modelo-ci-cd.md

ID: **$1** | Motivo: **$2** (Head reprovou canário / incidente / etc.)

1. Ler `cd-state.yaml`, `validacao-head-$1.md`, `rollout-state.yaml`
2. Reapontar `producao.deploy_ref` → `deploy_anterior_ref`
3. Atualizar `rollout-state.yaml` fase e segmentos
4. Registrar em `validacao-head` ou novo `rollback-{data}.md` — linguagem Head
5. Recomendar `/ert-abrir` se incidente em produção
6. **Não** expandir até nova validação Head
