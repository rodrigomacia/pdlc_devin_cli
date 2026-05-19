---
name: cd-promover
description: CD — promove commit_hash para sandbox, homolog (SV/mock) ou producao
argument-hint: "<id> <sandbox|homolog|producao> [commit_hash]"
agent: cd-coordinator
subagent: true
model: sonnet
allowed-tools:
  - read
  - edit
permissions:
  allow:
    - Read(colmeia/**)
    - Write(colmeia/04-construcao/_iniciativas/**)
---

@colmeia/04-construcao/modelo-ci-cd.md
@colmeia/_config/construcao-monorepo.md

ID: **$1** | Ambiente: **$2** | Hash: **$3** ou de `cd-state.yaml`

## Pré-condições

- `ci_status: verde` e hash definido (CD-01)
- **sandbox:** após CI
- **homolog:** após sandbox `tests_ok`
- **producao:** após homolog `tests_ok` + mesmo hash (CD-02, ROL-05)

## Por ambiente

### sandbox
- Deploy `deploy_ref: {hash}` no cluster sandbox
- Rodar testes integração com **Sistema produto sandbox** (endpoint real não-prod)
- Atualizar `cd-state.yaml` → `sandbox.status: tests_ok`

### homolog
- Deploy **mesmo hash**
- Ativar **virtualização de serviços + mock** (`mock-profile-{id}.yaml`)
- Rodar: funcional (histórias) · NFR perf · NFR security · contract vs mocks
- Atualizar `homolog.tests.*` e `status: tests_ok`
- Parar → `/grill-me $1 cd-homolog`

### producao
- Apontar deploy: `deploy_ref: {hash}` (CD-03 — obrigatório)
- Registrar `deploy_anterior_ref` para rollback
- **Não** iniciar canário aqui — usar `/rollout-canario` depois
- Atualizar `cd-state.yaml` → `producao.status: deployed`

## Output

- `cd-state.yaml`
- `cd-status-head-$1.md` (seção ambientes em linguagem Head)
