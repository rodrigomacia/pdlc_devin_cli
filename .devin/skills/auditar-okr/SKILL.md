---
name: auditar-okr
description: Audita OKR vs Gate 01 (subagente)
argument-hint: "<id>"
agent: auditor-okr
subagent: true
model: swe
allowed-tools:
  - read
  - grep
  - glob
---

@colmeia/01-contexto-estrategico/gates.md

Auditar artefatos em `colmeia/01-contexto-estrategico/_iniciativas/$1/`.

Parecer estruturado. Não editar arquivos.
