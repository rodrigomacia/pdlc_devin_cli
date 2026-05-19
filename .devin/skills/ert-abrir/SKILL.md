---
name: ert-abrir
description: Abre incidente ERT — favo 05
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
@colmeia/05-operacao/artefatos.md

ID: **$1** | Ref: **$2**

1. Criar `05-operacao/_iniciativas/$1/incidentes/$2/incidente.yaml`
2. Designar ert-lead como commander
3. Recomendar sequência: `/ert-comandar` → `/ert-registrar` → `/ert-diagnosticar`
