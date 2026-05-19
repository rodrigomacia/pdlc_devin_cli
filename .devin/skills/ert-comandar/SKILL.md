---
name: ert-comandar
description: Incident Commander — coordena resposta ERT
argument-hint: "<id> <ref>"
agent: ert-lead
model: sonnet
allowed-tools:
  - read
  - edit
permissions:
  allow:
    - Read(colmeia/**)
    - Write(colmeia/05-operacao/_iniciativas/**/incidentes/**)
---

@colmeia/05-operacao/modelo-ert.md

ID: **$1** | Ref: **$2**

1. Ler incidente.yaml, visao-360.md, timeline
2. Atualizar `acoes.md` — prioridades, owners (agents)
3. Disparar SMEs e comm conforme severidade
