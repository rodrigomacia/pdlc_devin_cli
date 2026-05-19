---
name: ert-fechar
description: Fecha incidente ERT — favo 05
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

1. Exigir visao-360.md (ERT-04)
2. Gerar `fechamento.md`, status=resolvido em incidente.yaml
3. Recomendar `/postmortem $1 $2` → `/insight-para-discovery $1`
