---
name: spec-nfr-writer
description: Spec não funcional — SLO, segurança, regulação
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

Subagente favo 04. Skill `/spec-nao-funcional`.

- `resumo_head` em YAML — parágrafo para Head
- Alinhar `metricas_discovery` com favo 02
- Multi-região AWS conforme `_config/construcao-monorepo.md`
