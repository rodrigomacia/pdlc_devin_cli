---
name: grill-me
description: Adversário crítico — questiona artefato antes de decisão do Head de Produto
argument-hint: "<id> <momento>"
agent: grill-me
subagent: true
model: sonnet
allowed-tools:
  - read
  - grep
  - glob
  - edit
permissions:
  allow:
    - Read(colmeia/**)
    - Write(colmeia/_grill/**)
---

@colmeia/00-nucleo/grill-me.md
@colmeia/02-discovery/modelo-discovery.md
@colmeia/01-contexto-estrategico/modelo-okr.md

Iniciativa: **$1** | Momento: **$2**

## 1. Resolver artefato-alvo

| Momento | Artefato(s) a ler |
|---------|-------------------|
| `okr-draft` | `01-contexto-estrategico/_iniciativas/$1/okr-*.md`, `tese-produto.md` |
| `okr-cascata` | `okr-cascata.yaml`, OKR draft |
| `gate-01` | Parecer auditor + cascata + OKR |
| `oportunidades` | `02-discovery/_iniciativas/$1/oportunidades.md`, `mapa-evidencias.md`, 3 visões |
| `hipoteses` | `hipoteses.yaml`, `oportunidades.md`, `mapa-evidencias.md` |
| `svm` | `svm/svm-*.md`, `personas-sinteticas.yaml`, `hipoteses.yaml` |
| `prototipo` | `prototipo-spec.md`, `hipoteses.yaml` |
| `feature` | `feature-$1.md`, `historias.yaml`, `prototipo-spec.md` |
| `gate-02` | feature + hipóteses + último grill `hipoteses` se existir |
| `experimento` | `03-experimentacao/_iniciativas/$1/experimento-*.md` |
| `decisao-exp` | `decisao-experimentos.md`, experimentos com resultado |
| `gate-03` | decisão + feature stories origem |
| `spec-funcional` | `spec-funcional-$1.md`, `resumo-head.md`, feature stories |
| `tarefas` | `tarefas.yaml`, specs |
| `ci` | `ci-status-$1.md`, `deploy-manifest-*.yaml`, `cd-state.yaml` |
| `pipeline` | alias de `ci` |
| `cd-homolog` | `cd-state.yaml` homolog.tests, `mock-profile-$1.yaml` |
| `rollout-head` | `validacao-head-$1.md`, `rollout-state.yaml` |
| `release` | `04-construcao/_iniciativas/$1/release-plan.md` |
| `gate-04` | pipeline + validacao-head + `review-pr-*.md` |
| `metricas` | `05-operacao/_iniciativas/$1/metricas-review-*.md`, OKR |
| `insights` | `insights-discovery.md` |

Se artefato ausente → veredito `BLOQUEAR` + skill sugerida para produzir.

## 2. Interrogatório (por momento)

### `hipoteses` (mínimo 8 perguntas)

- A intervenção é distinta do outcome desejado?
- Qual evidência **de qual visão** sustenta cada "porque"?
- O que observaríamos se a hipótese estiver **errada**?
- O segmento é específico demais ou está diluindo sinal?
- Confiança alta sem 3 visões → questionar `GRILL-WISH-01`
- KR referenciado: a hipótese move esse KR ou outro adjacente?

### `oportunidades`

- Aparece em ≥2 visões com mesmo segmento?
- Não é artefato de viés de canal único?
- Oportunidade ≠ solução disfarçada?

### `svm`

- Resultado marcado `[SINTÉTICO]`?
- Strong baseado em reações LLM ou em padrão das 3 visões?
- Próximo passo é protótipo ou voltar visões?

### `feature`

- História agrupada por valor, não por tela técnica?
- Critério de aceitação observável pelo cliente?
- Alguma história sem `hipotese_ref`?

### `okr-draft` / `okr-cascata`

- 4 metas em ordem baseline < target < roof < moonshot?
- KR mensurável no ciclo trimestral?
- Filho contribui mensuravelmente ao pai?

### `decisao-exp` / `metricas`

- Decisão sustentada por número fornecido pelo operador (não inventado)?
- Risco de confundir correlação com causalidade?

## 3. Output

Escrever `colmeia/_grill/$1/grill-$2-{YYYYMMDD}.md` com template de `grill-me.md`:

- Veredito
- Perguntas (numeradas)
- Lacunas
- Contradições
- Decisões para o Head
- Skills sugeridas se REFINAR/BLOQUEAR

## 4. Parar e aguardar

Após escrever o grill, **parar**. O Head responde na sessão Devin CLI antes da próxima skill.

Não executar skills downstream automaticamente.
