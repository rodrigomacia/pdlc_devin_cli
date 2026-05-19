---
name: experiments-backlog
description: Gera backlog de experimentos a partir de hipoteses.yaml — favo 03
argument-hint: "<id>"
agent: experiment-lead
model: sonnet
allowed-tools:
  - read
  - edit
permissions:
  allow:
    - Read(colmeia/**)
    - Write(colmeia/03-experimentacao/_iniciativas/**/experiments-backlog.md)
---

@colmeia/03-experimentacao/artefatos.md

ID: **$ARGUMENTS**

1. Ler `hipoteses.yaml`, `feature-$ARGUMENTS.md`, `historias.yaml` (favo 02)
2. Gerar `03-experimentacao/_iniciativas/$ARGUMENTS/experiments-backlog.md`
3. Uma linha por hipótese prioritária com `hipotese_ref` e `historia_id` sugerida
4. Tipos sugeridos (sem spike)
