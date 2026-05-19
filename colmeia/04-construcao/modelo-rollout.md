---
favo: 04-construcao
versao: 1.0
tags: [rollout, canario, segmentacao, head]
---

# Rollout — cliente a cliente com validação do Head

## Princípio

Rollout ocorre **somente em Produção**, após promoção CD:

`CI verde` → `Sandbox` → `Homolog (SV/mock)` → **`/cd-promover producao {commit_hash}`** → canário.

1. **CD Produção** — deploy por **apontamento `commit_hash`** (artefato imutável)
2. **Canário** — primeiro segmento de clientes (Head)
3. **Validação Head** — métricas discovery em produção
4. **Expansão** — segmentos adicionais (Head)

Ver [modelo-ci-cd.md](./modelo-ci-cd.md).

## Fases

```
CI(hash H) → CD sandbox(H) → CD homolog(H) → CD producao(H) → CANARIO → HEAD_VALIDA → EXPANDIR → 100%
```

| Fase | Skill | Quem decide |
|------|-------|-------------|
| Canário | `/rollout-canario {id}` | Head define `segmento_canario` |
| Validação | `/validar-rollout-head {id}` | Head aprova/reprova com métricas |
| Expansão | `/rollout-expandir {id} {segmento}` | Head define próximo segmento |
| Status | `/rollout-status {id}` | Head consulta (linguagem negócio) |

## Artefatos

- `rollout-plan-{id}.md` — plano em linguagem Head
- `rollout-state.yaml` — estado técnico (segmentos, %, regiões)
- `validacao-head-{id}.md` — decisão do Head pós-canário

## Métricas em produção (paridade discovery)

Durante canário e expansão, coletar via `prod.*` e `voc.*`:

- Funil, tempo jornada, loops, dead/rage click
- Cohort do segmento exposto
- VOC do segmento (reviews, central) — se volume permitir

Comparar **segmento exposto** vs **holdout** (controle).

## Segmentação

Usar mesmas dimensões de `colmeia/_config/discovery-tools.md`:

- Segmento de cliente
- Cohort, canal, device
- Feature flag por `cliente_id` / `segmento_id`

## Decisões do Head (template)

```yaml
validacao_head:
  iniciativa: {id}
  segmento_canario: {seg}
  periodo: {inicio..fim}
  veredito: aprovar_expansao | iterar | rollback
  kpis_observados:
    - kr_ref: ...
      resultado: ...
  proximo_segmento: {seg} | null
```

## Rollback

- **Produção:** reapontar `deploy_ref` para `deploy_anterior_ref` (hash anterior)
- Automático se health check pós-deploy falhar
- **Manual** se Head reprovar canário

Skill `/rollout-rollback {id}` — documenta em `rollout-state.yaml` e `cd-state.yaml`.

## Códigos

| Código | Condição |
|--------|----------|
| ROL-01 | Expansão sem `validar-rollout-head` aprovado |
| ROL-02 | Segmento canário sem definição |
| ROL-03 | Métricas insuficientes para decisão Head |
| ROL-04 | Produção sem `deploy_ref` = commit_hash |
| ROL-05 | Rollout antes de Homolog CD verde |
