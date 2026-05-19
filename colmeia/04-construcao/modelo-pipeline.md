---
favo: 04-construcao
versao: 2.0
tags: [ci, pipeline, testes, seguranca]
---

# CI — Integração Contínua (somente)

> **CD segregado:** Sandbox · Homolog (SV/mock) · Produção (hash) — ver [modelo-ci-cd.md](./modelo-ci-cd.md).

A pipeline **CI não faz deploy** em Sandbox, Homolog ou Produção. Ela produz **artefato imutável** `artifact:{commit_hash}`.

## Estágios obrigatórios (CI)

| Estágio | Tipo | Bloqueia CI? |
|---------|------|--------------|
| **lint + SAST** | Segurança | Sim |
| **unit** | Unitário | Sim |
| **contract** | Contrato (estático) | Sim |
| **build** | Artefato tag = `commit_hash` | Sim |
| **smoke** | Smoke mínimo (opcional) | Configurável |

## O que NÃO roda no CI (vai para CD Homolog)

| Teste | Onde |
|-------|------|
| Funcional jornada completa | CD Homolog + SV/mock |
| Integração Sistema produto | CD Sandbox (real sandbox) |
| NFR performance | CD Homolog |
| NFR segurança dinâmica | CD Homolog |

## Saída (`ci-status-{id}.md`)

```markdown
# CI — {id} — {commit_hash}

## Semáforo CI
VERDE | VERMELHO

## Artefato
commit_hash: {hash}
artifact_id: art-{hash}

## Para o Head
- Código passou nos testes automáticos de qualidade: {sim|não}
- Pronto para promover a ambientes de teste (CD): {sim|não}
```

## Skill

`/ci-validar {id}` — primário  
`/pipeline-validar {id}` — alias (mesmo comportamento)

## Códigos

| Código | Estágio |
|--------|---------|
| CI-01 | Artefato sem commit_hash |
| CI-02 | Estágio bloqueante falhou |
| PIPE-SEC-01 | SAST fail (legado) |
| PIPE-UNIT-01 | Cobertura abaixo do mínimo |
