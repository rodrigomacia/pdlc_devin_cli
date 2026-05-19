---
favo: 04-construcao
versao: 2.2
---

# Gate 04

Aprovador: **Head de Produto (Go-to-Market)**.

## Pré-requisitos

- [ ] **G4.0** Gate 03 — decisão **`scale`** em `decisao-experimentos.md`
- [ ] **G4.0b** `feature-{id}.md` — `validacao_real: confirmada`

## SDD

- [ ] **G4.1** `spec-funcional-{id}.md` + `resumo-head.md` — rastreável às histórias
- [ ] **G4.2** `spec-nfr-{id}.yaml`
- [ ] **G4.3** `spec-tecnica-{id}.md`
- [ ] **G4.4** `tarefas.yaml` — 100% histórias com `entregavel: codigo`
- [ ] **G4.5** Tarefas `status: pronto`

## Qualidade (antes de CD)

- [ ] **G4.6** `/review-pr` — veredito ≠ REPROVADO (**antes** de CI/CD) — BLD-PR-01
- [ ] **G4.7** `ci-status-{id}.md` — CI **VERDE** + artefato `commit_hash`

## CD

- [ ] **G4.8** Sandbox CD OK
- [ ] **G4.9** Homolog CD OK — funcional + NFR com SV/mock
- [ ] **G4.10** `/grill-me cd-homolog` ≠ BLOQUEAR
- [ ] **G4.11** Produção `deploy_ref` = `commit_hash`
- [ ] **G4.12** Mesmo hash nos três ambientes

## Grill-me

- [ ] **G4.G1** `spec-funcional` · **G4.G2** `tarefas` · **G4.G3** `ci` · **G4.G4** `cd-homolog` · **G4.G5** `rollout-head` · **G4.G6** `gate-04`

## Rollout

- [ ] **G4.13** Canário executado
- [ ] **G4.14** `validacao-head` — APROVAR_EXPANSAO ou expansão documentada
- [ ] **G4.15** `release-plan` + `rollout-plan` + `deploy-manifest-{hash}`
- [ ] **G4.16** Handoff 04→05
