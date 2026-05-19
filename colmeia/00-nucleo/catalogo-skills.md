---
favo: 00-nucleo
versao: 3.0
status: estavel
tags: [skills, catalogo, devin]
---

# Catálogo de Skills — Ciclo de Produtação

Contrato: **entrada → saída → gate**. Sem contexto de produto no repositório.

## 00 — Orquestração

| Comando | Entrada | Saída |
|---------|---------|-------|
| `/orquestrar-producao {id}` | ID | Plano de skills + lacunas |
| `/curar-contexto {de} {para} {id}` | 01–05, ID | `colmeia/_handoffs/handoff-*.md` |

## 01 — Contexto Estratégico

| Comando | Entrada | Saída | Agent |
|---------|---------|-------|-------|
| `/sync-okr-plataforma {id} pull\|push` | Config MCP, cascata | snapshot / ids plataforma | `sync-okr` |
| `/draft-okr {id} [tipo]` | Diretriz, baselines | `okr-*.md`, `tese-produto.md` | `estrategista-okr` |
| `/desdobrar-okr {id}` | OKR + nó pai L2 | `okr-cascata.yaml` | `desdobrador-okr` |
| `/auditar-okr {id}` | Draft + cascata | Parecer Gate 01 | `auditor-okr` ⊂ |

**Tool principal:** Plataforma OKR — OKR/KR/KPI em todos os níveis; metas **baseline · target · roof · moonshot**. Ver `colmeia/01-contexto-estrategico/modelo-okr.md`.

## 02 — Discovery

Modelo Go-to-Market: **Head de Produto = `discovery-lead`** ponta-a-ponta. Demais agentes são subagentes (tools).

| Comando | Entrada | Saída | Agent |
|---------|---------|-------|-------|
| `/visao-mercado {id}` | OKR + segmentos | `visao-mercado.md` | `market-researcher` ⊂ |
| `/visao-produto {id}` | OKR + jornada-alvo | `visao-produto.md` | `product-analytics` ⊂ |
| `/visao-cliente {id}` | OKR + canais VOC | `visao-cliente.md` | `voc-analyst` ⊂ |
| `/sintetizar-visoes {id}` | 3 visões | `oportunidades.md`, `ost-{id}.md`, `mapa-evidencias.md` | `discovery-lead` |
| `/gerar-hipoteses {id}` | Síntese | `hipoteses.yaml` | `discovery-lead` |
| `/testar-svm {id} [hip]` | Hipóteses + 3 visões | `personas-sinteticas.yaml`, `svm-{hip}.md` | `personas-sinteticas` ⊂ |
| `/prototipo-figma {id}` | Hipóteses Strong | `prototipo-spec.md` | `prototipador` ⊂ |
| `/feature-stories {id}` | Protótipo + hipóteses | `feature-{id}.md`, `historias.yaml` | `feature-writer` ⊂ |
| `/prep-entrevista {id} [O?]` | OST/oportunidade | `roteiros/roteiro-*.md` | — |

**Tools chave:** VOC (transcrição, app store, suporte, social), Analytics (funil, dead/rage click, loops, tempo, cohort), Personas sintéticas (SVM), Figma. Ver `colmeia/02-discovery/modelo-discovery.md` e `colmeia/02-discovery/capacidades-tools.md`.

## 03 — Experimentação (clientes reais)

Entrada: **feature candidata** + `hipoteses.yaml` + protótipo (Gate 02). Ver [modelo-experimentacao-discovery.md](./modelo-experimentacao-discovery.md).

| Comando | Entrada | Saída | Agent |
|---------|---------|-------|-------|
| `/experiments-backlog {id}` | `hipoteses.yaml`, feature | `experiments-backlog.md` | `experiment-lead` |
| `/design-experimento {id} [E]` | Feature + hipóteses | `experimento-{E}.md` | `experiment-lead` |
| `/registrar-resultado {id} {E}` | Dados do operador | Atualiza experimento | — |
| `/decidir-experimento {id}` | Experimentos concluídos | `decisao-experimentos.md` + roteamento favo | `experiment-lead` ⊂ |

## 04 — Construção (SDD)

Head aprova `resumo-head.md` e valida rollout — **não lê código**. Modelo: [modelo-sdd.md](../04-construcao/modelo-sdd.md).

| Comando | Entrada | Saída | Agent |
|---------|---------|-------|-------|
| `/spec-funcional {id}` | Feature stories (02) | `spec-funcional`, `resumo-head` | `spec-funcional-writer` ⊂ |
| `/spec-nao-funcional {id}` | Spec funcional | `spec-nfr-{id}.yaml` | `spec-nfr-writer` ⊂ |
| `/spec-tecnica {id}` | Specs | `spec-tecnica-{id}.md` | `spec-tech-writer` ⊂ |
| `/decompor-tarefas {id}` | Specs | `tarefas.yaml` | `task-decomposer` ⊂ |
| `/implementar-tarefa {id} {t}` | Tarefa | Código no monorepo | `implementador` ⊂ |
| `/review-pr {id} [ref]` | diff/PR | `review-pr-*.md` — **antes de CI/CD** | `reviewer` ⊂ |
| `/ci-validar {id} [hash]` | CI (sem deploy) | `ci-status`, `deploy-manifest-{hash}` | `pipeline-guardian` ⊂ |
| `/cd-promover {id} sandbox\|homolog\|producao [hash]` | CD | `cd-state.yaml` | `cd-coordinator` ⊂ |
| `/cd-status {id}` | — | `cd-status-head` | `builder-lead` |
| `/pipeline-validar {id}` | Alias CI | idem `ci-validar` | `pipeline-guardian` ⊂ |
| `/rollout-canario {id} [seg]` | CD prod + hash | `rollout-state` | `rollout-coordinator` ⊂ |
| `/validar-rollout-head {id}` | Métricas produção | `validacao-head` | `builder-lead` |
| `/rollout-expandir {id} {seg}` | Aprovação Head | `rollout-state` | `rollout-coordinator` ⊂ |
| `/rollout-rollback {id} [motivo]` | Reprovação canário | `cd-state`, `rollout-state` | `rollout-coordinator` ⊂ |
| `/rollout-status {id}` | — | Resumo negócio | `builder-lead` |
| `/prep-release {id}` | CI verde + review-pr | `release-plan`, rollout plan | `builder-lead` |

Monorepo: nativo + React SSG + BFF Go + AWS multi-região. CI/CD: [modelo-ci-cd.md](../04-construcao/modelo-ci-cd.md) — Sandbox · Homolog (SV/mock) · Produção (`commit_hash`).

## 05 — Operação + ERT

| Comando | Entrada | Saída | Agent |
|---------|---------|-------|-------|
| `/review-metricas {id}` | Valores atuais | `metricas-review-*.md` | `operador-lead` |
| `/rollout-status {id}` | — | Status rollout | `builder-lead` |
| `/ert-abrir {id} {ref}` | Alerta | `incidente.yaml` | `ert-lead` |
| `/ert-comandar {id} {ref}` | — | `acoes.md` | `ert-lead` |
| `/ert-registrar {id} {ref}` | Evento | `timeline.md` | `ert-logger` ⊂ |
| `/ert-comunicar {id} {ref}` | — | `comunicacoes.md` | `ert-comm` ⊂ |
| `/ert-diagnosticar {id} {ref}` | — | `visao-360.md` | SMEs ⊂ |
| `/ert-fechar {id} {ref}` | — | `fechamento.md` | `ert-lead` |
| `/postmortem {id} {ref}` | Incidente | `postmortem-*.md` | `operador-lead` ⊂ |
| `/insight-para-discovery {id}` | Ops | `insights-discovery.md` | `operador-lead` |

ERT: [modelo-ert.md](../05-operacao/modelo-ert.md) — operação 100% IA, visão 360°.

⊂ = subagente (`subagent: true`)

## Transversal

| Comando | Entrada | Saída | Agent |
|---------|---------|-------|-------|
| `/grill-me {id} {momento}` | Artefato da etapa anterior | Perguntas + veredito + `registro-decisoes-grill.yaml` (100% itens) | `grill-me` ⊂ |
| `/governanca-check {id} {favo}` | `_config/governanca.md` opcional | Checklist | `guardiao-governanca` ⊂ |

**Grill-me — momentos:** … · `spec-funcional` · `tarefas` · `pipeline` · `rollout-head` · `release` · `gate-04` · … Ver [grill-me.md](./grill-me.md) · Registro 100%: [modelo-registro-decisoes-grill.md](./modelo-registro-decisoes-grill.md).

## Matriz Skill → Gate

| Gate | Skills |
|------|--------|
| 01 | `draft-okr` → **grill** `okr-draft` → `desdobrar-okr` → **grill** `okr-cascata` → `auditar-okr` → **grill** `gate-01` → sync push |
| 02 | visões → síntese → **grill** `oportunidades` → hipóteses → **grill** `hipoteses` → svm → **grill** `svm` → protótipo → **grill** `prototipo` → feature → **grill** `feature` + `gate-02` |
| 03 | backlog → `design-experimento` → **grill** `experimento` → resultado → `decidir-experimento` → **grill** `decisao-exp` + `gate-03` → 04 ou 02 |
| 04 | SDD → implementar → **review-pr** → **grill** `gate-04-pre` → CI → **grill** `ci` → prep-release → CD sandbox/homolog → **grill** `cd-homolog` → CD prod (hash) → canário → **grill** `rollout-head` → expandir/rollback → gate-04 |
| 05 | métricas → ERT → postmortem → insights → loop 02 |

## Ciclo completo (ordem de referência)

Ver [ciclo-completo.md](./ciclo-completo.md)

## Lacunas — skill deve parar

| Favo | Lacuna |
|------|--------|
| 01 | Diretriz, baselines, ciclo |
| 02 | Gate 01 / OKR · tools VOC/analytics ausentes (parar com `[DADO AUSENTE]`) · 3 visões obrigatórias antes de hipóteses |
| 03 | Gate 02 / feature candidata (`validacao_real: pendente`) |
| 04 | Gate 03 **`scale`** + `validacao_real: confirmada` · review-pr antes de CI · monorepo config · segmento canário (Head) |
| 05 | Valores de métricas (operador) |
