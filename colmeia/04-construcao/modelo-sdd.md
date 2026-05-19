---
favo: 04-construcao
versao: 2.1
status: estavel
tags: [sdd, spec-driven, head-transparente]
---

# Modelo SDD — Specification-Driven Development

O Head de Produto **não precisa ler código**. Ele aprova **especificações em linguagem de negócio** e **valida rollout em produção** com as mesmas métricas do discovery.

## Princípio

```
Feature (03 scale) → Spec → Tarefas → Código → review-pr → CI → CD → Rollout canário
                              ↑ oculto              ↑ antes de deploy
```

## Camadas de especificação

| Camada | Artefato | Audiência | Skill |
|--------|----------|-----------|-------|
| **Funcional** | `spec-funcional-{id}.md` + `resumo-head.md` | Head + negócio | `/spec-funcional` |
| **Não funcional** | `spec-nfr-{id}.yaml` + resumo Head | Head (resumo) + eng | `/spec-nao-funcional` |
| **Técnica** | `spec-tecnica-{id}.md` | Agents / implementação | `/spec-tecnica` |
| **Tarefas** | `tarefas.yaml` | Agents | `/decompor-tarefas` |
| **Código** | monorepo (paths em config) | Pipeline | `/implementar-tarefa` |

## Pré-requisito favo 04

Gate 03 com decisão **`scale`** e `decisao-experimentos.md` apontando favo 04.  
Feature do favo 02 deve estar `validacao_real: confirmada` (após experimentação real).

## Fluxo SDD (sequência)

1. `/spec-funcional {id}` — de `feature-{id}.md` + `historias.yaml` (favo 02, pós-scale)
2. `/grill-me {id} spec-funcional`
3. `/spec-nao-funcional {id}`
4. `/spec-tecnica {id}`
5. `/grill-me {id} tarefas` — após `/decompor-tarefas` (passo 6)
6. `/decompor-tarefas {id}`
7. Loop: `/implementar-tarefa {id} {tarefa_id}`
8. **`/review-pr {id}`** — antes de qualquer CD (BLD-PR-01)
9. `/ci-validar {id}` → artefato `commit_hash`
10. `/grill-me {id} ci`
11. `/prep-release {id}` — plano de rollout + hash (antes do canário)
12. `/grill-me {id} release`
13. `/cd-promover {id} sandbox [hash]`
14. `/cd-promover {id} homolog [hash]` — SV + mock
15. `/grill-me {id} cd-homolog`
16. `/cd-promover {id} producao [hash]`
17. `/rollout-canario {id}`
18. `/validar-rollout-head {id}`
19. `/grill-me {id} rollout-head`
20. `/rollout-expandir {id} {segmento}` (ou `/rollout-rollback` se reprovado)
21. `/grill-me {id} gate-04` → Gate 04

## Códigos

| Código | Condição |
|--------|----------|
| SDD-01 | Spec sem `historia_id` |
| SDD-02 | Tarefa sem spec de origem |
| SDD-03 | CD promovido sem CI verde ou sem review-pr |
| SDD-04 | Rollout canário sem validação Head |
| SDD-05 | NFR crítico falhou em Homolog CD |
| BLD-PR-01 | review-pr ausente ou REPROVADO antes de CI/CD |

## Dupla validação com cliente (clareza)

| Fase | O quê | Onde |
|------|-------|------|
| Protótipo / pretotype com clientes reais | Valida hipótese antes de construir | **Favo 03** |
| Testes automatizados SV/mock | Valida implementação sem backend prod | **CD Homolog** |
| Canário em Produção | Valida KPI com clientes reais no ar | **Rollout** |

Ver [modelo-experimentacao-discovery.md](../00-nucleo/modelo-experimentacao-discovery.md).
