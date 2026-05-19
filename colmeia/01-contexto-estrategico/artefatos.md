---
favo: 01-contexto-estrategico
versao: 1.0
tags: [templates]
---

# Templates — favo 01

Copiar para `colmeia/01-contexto-estrategico/_iniciativas/{id}/`. **Não preencher com dados fictícios no repo.**

## okr-{ciclo}.md

```yaml
---
favo: 01-contexto-estrategico
iniciativa: {id}
ciclo: {ciclo}
tipo_iniciativa: core | exploratorio | hibrido
status: rascunho
upstream: []
downstream: []
---
```

```markdown
# OKR — {id} — {ciclo}

## Cascata
| Nível | Objective | Fonte |
|-------|-----------|-------|
| {nível} | {texto ou [FORNECER]} | {ref} |

## Objective
{[FORNECER]}

## Key Results

| KR | Métrica | Baseline | Target | Roof | Moonshot | Prazo | Tipo | parent_ref |
|----|---------|----------|--------|------|----------|-------|------|------------|
| KR1 | | | | | | | leading/lagging | |

> **Target** = meta comprometida do ciclo. **Roof** = stretch realista. **Moonshot** = aspiração.
> Ordem: ver [modelo-okr.md](./modelo-okr.md).

## KPIs (acompanhamento)

| KPI | KR pai | Baseline | Target | Roof | Moonshot | Frequência |
|-----|--------|----------|--------|------|----------|------------|
| KPI1 | KR? | | | | | semanal |

## North Star
**Métrica:** {[FORNECER]}
**Definição:** {[FORNECER]}

### Inputs
| Input | Hipótese causal | KR |
|-------|-----------------|-----|

## Hipóteses estratégicas (→ favo 02)
1.
2.
3.
```

## tese-produto.md

```markdown
# Tese — {id}

## Job to be done
{[FORNECER]}

## Segmento / fora de escopo
{[FORNECER]}

## Ligação OKR
{[FORNECER]}
```

## scanning-{periodo}.md

```markdown
# Scan — {id} — {periodo}

| # | Sinal | Categoria | Implicação | Confiança | Fonte |
|---|-------|-----------|------------|-----------|-------|
```

## okr-cascata.yaml

Artefato canônico para `/desdobrar-okr` e `/sync-okr-plataforma`.

```yaml
iniciativa: {id}
ciclo: {ciclo}
plataforma_ref: null  # preenchido após push

nos:
  - id: obj-L3-{id}
    tipo: objective
    nivel: L3
    titulo: "[FORNECER]"
    parent_ref: obj-L2-{parent}  # KR ou objective pai
    tipo_vinculo: contribui
    peso: 0.0  # 0-1

  - id: kr-L3-1
    tipo: kr
    objective_id: obj-L3-{id}
    metrica_id: "[FORNECER]"
    parent_ref: kr-L2-{parent}
    tipo_vinculo: contribui
    peso: 0.25
    baseline: null
    target: null
    roof: null
    moonshot: null
    direcao: higher_is_better  # ou lower_is_better

  - id: kpi-L3-1
    tipo: kpi
    kr_id: kr-L3-1
    baseline: null
    target: null
    roof: null
    moonshot: null
    frequencia: semanal
    is_north_star_input: false

north_star:
  ref: kr-L3-1  # ou kpi
```

## sync-okr-log.md

```markdown
# Sync Plataforma OKR — {id} — {data}

| Operação | Nós | Status | id_plataforma |
|----------|-----|--------|---------------|
| pull | | ok / erro | |
| push | | ok / erro | |
```

## gate-01-registro.md

```markdown
# Gate 01 — {id}
Status: APROVADO | RESSALVAS | REPROVADO
Checklist: ver gates.md
```
