---
name: implementar-tarefa
description: Implementa tarefa no monorepo — código + testes
argument-hint: "<id> <tarefa_id>"
agent: implementador
subagent: true
model: sonnet
allowed-tools:
  - read
  - edit
  - grep
  - glob
  - shell
permissions:
  allow:
    - Read(colmeia/**)
    - Write(**)
---

@colmeia/04-construcao/modelo-monorepo.md

ID: **$1** | Tarefa: **$2**

1. Implementar conforme specs + `tarefas.yaml`
2. Atualizar tarefa `status: pronto`, `pr_ref`
3. Quando **todas** tarefas prontas → próximo passo obrigatório: **`/review-pr $1`** (antes de `/ci-validar`)

Não chamar `/ci-validar` ou `/cd-promover` antes de review-pr aprovado.
