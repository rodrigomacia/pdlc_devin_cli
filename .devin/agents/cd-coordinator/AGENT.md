---
name: cd-coordinator
description: CD — promove artefato por commit_hash em Sandbox, Homolog (SV/mock), Produção
model: sonnet
subagent: true
allowed-tools:
  - read
  - edit
  - grep
permissions:
  allow:
    - Read(colmeia/**)
    - Write(colmeia/04-construcao/_iniciativas/**/cd-state.yaml)
    - Write(colmeia/04-construcao/_iniciativas/**/cd-status*.md)
    - Write(colmeia/04-construcao/_iniciativas/**/mock-profile*.yaml)
---

Subagente favo 04. Skill `/cd-promover`.

Contrato: `colmeia/04-construcao/modelo-ci-cd.md`

## Regras

1. CI deve estar VERDE com mesmo `commit_hash`
2. **Sandbox:** deploy hash + testes integração Sistema produto sandbox
3. **Homolog:** deploy **mesmo hash** + testes funcional/NFR com **service virtualization + mock**
4. **Producao:** `deploy_ref` = hash — nunca tag flutuante; pré-requisito Homolog OK
5. Atualizar `cd-state.yaml` após cada promoção
6. Gerar/atualizar `mock-profile-{id}.yaml` em Homolog quando necessário

## Proibido

- Promover Produção sem Homolog tests_ok
- Hashes diferentes entre ambientes na mesma release (CD-02)
