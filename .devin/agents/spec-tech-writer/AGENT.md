---
name: spec-tech-writer
description: Spec técnica — mapeamento monorepo BFF/Front/integrações
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
    - Write(colmeia/04-construcao/_iniciativas/**)
---

Subagente favo 04. Skill `/spec-tecnica`.

- `colmeia/04-construcao/modelo-monorepo.md`
- Mapear cada historia_id → camadas apps/bff/integrations
- Contratos em `packages/contracts`
