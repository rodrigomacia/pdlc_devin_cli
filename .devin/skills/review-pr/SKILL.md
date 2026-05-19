---
name: review-pr
description: Revisão de PR — obrigatória antes de CI/CD
argument-hint: "<id> [ref]"
agent: reviewer
subagent: true
model: sonnet
allowed-tools:
  - read
  - grep
  - edit
permissions:
  allow:
    - Read(colmeia/**)
    - Write(colmeia/04-construcao/_iniciativas/**/review-pr*.md)
---

@colmeia/04-construcao/gates.md
@colmeia/04-construcao/modelo-sdd.md

ID: **$1** | Ref: **$2**

1. Operador fornece diff/PR ou path — ler mudanças no monorepo config
2. Gerar `review-pr-{ref}.md` — veredito APROVADO | APROVADO COM RESSALVAS | REPROVADO
3. Se REPROVADO: parar pipeline — não `/ci-validar` (BLD-PR-01)
4. Se APROVADO: próximo `/ci-validar $1`

Posição no fluxo: **após** `implementar-tarefa`, **antes** de qualquer CD.
