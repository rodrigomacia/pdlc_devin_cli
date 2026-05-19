---
favo: 04-construcao
versao: 1.0
status: estavel
tags: [ci, cd, sandbox, homolog, producao, commit-hash, service-virtualization]
---

# CI × CD — segregação e três ambientes

**CI** (Integração Contínua) e **CD** (Entrega Contínua) são pipelines **distintos**. O artefato que trafega no CD é **imutável** e identificado pelo **`commit_hash`**.

```
┌─────────────────────────────────────────────────────────────────┐
│  CI — por commit/PR (não deploya em Produção)                   │
│  lint · SAST · unit · contract · build → artefato:{commit_hash} │
└───────────────────────────────┬─────────────────────────────────┘
                                │ artefato imutável
        ┌───────────────────────┼───────────────────────┐
        ▼                       ▼                       ▼
   ┌─────────┐            ┌───────────┐         ┌─────────────┐
   │ SANDBOX │            │ HOMOLOG   │         │  PRODUÇÃO   │
   │   CD    │            │    CD     │         │     CD      │
   └─────────┘            └───────────┘         └─────────────┘
```

O Head vê **status por ambiente** em linguagem de negócio — não workflows YAML.

---

## CI — Integração Contínua

| Atributo | Regra |
|----------|--------|
| **Gatilho** | Push / PR no monorepo |
| **Deploy** | **Não** promove a Produção |
| **Saída** | Artefato versionado `artifact:{commit_hash}` |
| **Skill** | `/ci-validar {id}` (alias: `/pipeline-validar`) |

### Estágios CI (obrigatórios)

| Estágio | Tipo | Ambiente de execução |
|---------|------|----------------------|
| lint + SAST | Segurança | Runner CI |
| unit | Unitário | Runner CI |
| contract | Contrato BFF ↔ apps | Runner CI |
| build | Artefato imutável | Registry com tag = **commit_hash** |

Testes funcionais **pesados** e **NFR** de integração rodam no CD (Homolog), não no CI — exceto smoke mínimo se configurado.

---

## CD — Entrega Contínua

| Atributo | Regra |
|----------|--------|
| **Entrada** | CI **VERDE** + `commit_hash` explícito |
| **Promoção** | Mesmo hash atravessa Sandbox → Homolog → Produção |
| **Proibido** | Deploy em Produção com tag `latest` sem hash |
| **Skill** | `/cd-promover {id} {ambiente} [commit_hash]` |

`ambiente`: `sandbox` | `homolog` | `producao`

---

## Ambiente 1 — Sandbox

| Dimensão | Definição |
|----------|-----------|
| **Objetivo** | Integração early com **Sistema produto sandbox** (endpoints reais de não-prod) |
| **Dados** | Sintéticos ou sandbox regulado |
| **Deploy CD** | Aponta `deploy_ref: {commit_hash}` no cluster sandbox |
| **Testes pós-deploy** | Integração BFF ↔ Sistema produto sandbox; smoke das histórias |
| **Quem valida** | Automático — Head não precisa atuar |

```yaml
cd:
  sandbox:
    deploy_ref: "{commit_hash}"
    sistema_produto: sandbox_endpoint
    integracao: real-sandbox
```

---

## Ambiente 2 — Homologação

| Dimensão | Definição |
|----------|-----------|
| **Objetivo** | Validação completa **sem depender** de disponibilidade de backends reais |
| **Base** | **Virtualização de Serviços** + **Mock** de Sistema produto |
| **Deploy CD** | `deploy_ref: {commit_hash}` — mesmo artefato do CI |
| **Testes pós-deploy** | Funcional (jornadas/histórias) · NFR perf · NFR segurança · contract contra mocks |

### Virtualização e mock

| Mecanismo | Uso |
|-----------|-----|
| **Service Virtualization (SV)** | Simula comportamento de Sistema produto com contratos gravados |
| **Mock** | Respostas determinísticas para cenários de teste (happy path, erro, timeout) |
| **Perfis** | `mock-profile-{iniciativa}.yaml` — mapeia operação → stub |

```yaml
homolog:
  deploy_ref: "{commit_hash}"
  service_virtualization:
    enabled: true
    provider: "[FORNECER — Mountebank / WireMock / etc.]"
  mocks:
    sistema_produto_profile: "mock-profile-{id}"
    contract_validation: true
```

**Gate CD Homolog:** funcional + NFR verdes contra SV/mock antes de qualquer Produção.

---

## Ambiente 3 — Produção

| Dimensão | Definição |
|----------|-----------|
| **Objetivo** | Clientes reais — rollout segmentado |
| **Deploy** | **Apontamento por `commit_hash`** — registro imutável do que está no ar |
| **Rollout** | Canário → validação Head → expansão por segmento |
| **Rollback** | Reapontar `deploy_ref` para hash anterior conhecido |

```yaml
cd:
  producao:
    deploy_ref: "{commit_hash}"      # obrigatório — nunca omitir
    deploy_anterior_ref: "{hash}"    # rollback
    rollout:
      fase: canario | expansao | completo
      segmentos: []
```

Produção **não** reexecuta suite completa de Homolog — confia na promoção do mesmo hash + health checks + métricas discovery.

---

## Ordem de promoção CD

```
CI VERDE (hash H)
  → /cd-promover {id} sandbox H
  → testes integração sandbox OK
  → /cd-promover {id} homolog H
  → testes funcional + NFR (SV/mock) OK
  → /grill-me {id} cd-homolog
  → /cd-promover {id} producao H
  → /rollout-canario {id}        # segmento Head
  → /validar-rollout-head {id}
  → /rollout-expandir …
```

---

## Artefatos runtime

| Arquivo | Conteúdo |
|---------|----------|
| `ci-status-{id}.md` | Semáforo CI + `commit_hash` |
| `cd-state.yaml` | Estado por ambiente + `deploy_ref` |
| `deploy-manifest-{hash}.yaml` | Artefato, imagens, checksums |

## Saída para o Head (`cd-status-head-{id}.md`)

```markdown
# Entrega — {id}

## Versão em promoção
Commit: `{hash}` (imutável — mesma em todos os ambientes aprovados)

## Ambientes
| Ambiente | Status | O que significa para o cliente |
| Sandbox | OK | Integração interna validada |
| Homolog | OK | Jornadas testadas com simulação de sistemas |
| Produção | Canário 5% segmento X | Clientes reais no grupo piloto |

## Próxima decisão do Head
{validar canário / aprovar expansão}
```

## Skills

| Skill | Fase |
|-------|------|
| `/ci-validar {id}` | CI |
| `/cd-promover {id} sandbox\|homolog\|producao [hash]` | CD |
| `/cd-status {id}` | Consulta Head (todos ambientes) |

`/pipeline-validar` permanece como **alias** de `/ci-validar` (retrocompat).

## Códigos

| Código | Condição |
|--------|----------|
| CI-01 | Build sem tag commit_hash |
| CI-02 | Estágio CI bloqueante falhou |
| CD-01 | Promover sem CI verde |
| CD-02 | Hash diferente entre ambientes na mesma release |
| CD-03 | Produção sem deploy_ref hash |
| CD-HOM-01 | Homolog — funcional falhou contra SV/mock |
| CD-HOM-02 | Mock profile desatualizado vs contrato |
| CD-SBX-01 | Sandbox — integração Sistema produto falhou |

## Referências

- CI detalhe: [modelo-pipeline.md](./modelo-pipeline.md)
- Rollout Produção: [modelo-rollout.md](./modelo-rollout.md)
- Config: [construcao-monorepo.md](../_config/construcao-monorepo.md)
