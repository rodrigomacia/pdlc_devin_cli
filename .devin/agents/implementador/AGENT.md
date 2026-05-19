---
name: implementador
description: Implementa tarefa no monorepo — código + testes
model: sonnet
subagent: true
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

Subagente favo 04. Skill `/implementar-tarefa`.

- Ler `colmeia/_config/construcao-monorepo.md` para root do repo
- Implementar conforme `spec-tecnica` + `tarefas.yaml`
- Incluir testes unit + functional da tarefa
- Atualizar `tarefas.yaml` status e `pr_ref`
- Framework colmeia não contém código de produto — trabalha no monorepo configurado
