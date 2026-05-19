---
name: spec-tecnica
description: Spec técnica — monorepo nativo/web-ssg/bff/integrações — favo 04
argument-hint: "<id>"
agent: spec-tech-writer
subagent: true
model: sonnet
allowed-tools:
  - read
  - edit
permissions:
  allow:
    - Read(colmeia/**)
    - Write(colmeia/04-construcao/_iniciativas/**/spec-tecnica*.md)
---

@colmeia/04-construcao/modelo-monorepo.md
@colmeia/04-construcao/artefatos.md

ID: **$ARGUMENTS**

1. Ler spec-funcional + spec-nfr
2. Gerar `spec-tecnica-$1.md` — mapeamento por historia_id
3. Não atualizar resumo-head com jargão técnico
