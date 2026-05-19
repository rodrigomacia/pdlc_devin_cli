---
name: spec-funcional-writer
description: Spec funcional + resumo-head a partir de feature stories
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

Subagente favo 04. Skill `/spec-funcional`. Template: `colmeia/04-construcao/artefatos.md`.

- Input: `feature-{id}.md`, `historias.yaml` (favo 02)
- Zero jargão técnico em `resumo-head.md`
- Rastreabilidade historia_id / hipotese_ref / kr_ref
