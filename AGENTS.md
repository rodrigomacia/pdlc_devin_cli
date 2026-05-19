# Regras — Framework de Produtação Digital

## Leitura

1. `colmeia/00-nucleo/catalogo-skills.md`
2. `colmeia/00-nucleo/ciclo-completo.md`
3. `fluxo.md` + `gates.md` do favo ativo

## Princípios

1. Skills produzem artefatos em `_iniciativas/{id}/` — não preencher produto fictício
2. Respeitar gates antes de handoff
3. Lacunas → `[FORNECER]` / `[RESULTADO: fornecer]`
4. `/orquestrar-producao` roteia o ciclo 01–05

## Skills (46)

- Favo 01 — **Plataforma OKR** (tool): `/sync-okr-plataforma`, `/desdobrar-okr`. Modelo: `colmeia/01-contexto-estrategico/modelo-okr.md`.
- Favo 02 — **Modelo Go-to-Market** (Head ponta-a-ponta): três visões → `/sintetizar-visoes` → `/gerar-hipoteses` → `/testar-svm` → `/prototipo-figma` → `/feature-stories` (`validacao_real: pendente`). Modelo: `colmeia/02-discovery/modelo-discovery.md`.
- Favo 03 — **Experimentação real:** `/design-experimento` → `/decidir-experimento` — `scale`→04 · `iterate/kill`→02. Modelo: `colmeia/00-nucleo/modelo-experimentacao-discovery.md`.
- Favo 04 — **SDD + CI/CD:** implementar → **`/review-pr` antes de CI/CD** → CD por `commit_hash` → rollout. Modelo: `colmeia/04-construcao/modelo-sdd.md`.

Ver `colmeia/00-nucleo/catalogo-skills.md`.

## Grill-me (transversal)

`/grill-me {id} {momento}` — adversário crítico **antes de cada decisão**. Obrigatório em hipóteses, feature e gates. Mapa: `colmeia/00-nucleo/grill-me.md`.

**Registro 100%:** após cada grill, `colmeia/_grill/{id}/registro-decisoes-grill.yaml` documenta **todas** as hipóteses/itens com decisão (continuar ou desconsiderar) e motivadores. Modelo: `colmeia/00-nucleo/modelo-registro-decisoes-grill.md`. Gates **G2.REG** / **G3.REG**.

## Config opcional

- `colmeia/_config/governanca.md` para `/governanca-check`
- `colmeia/_config/okr-plataforma.md` para sincronização OKR
- `colmeia/_config/discovery-tools.md` para VOC, analytics, personas sintéticas e Figma
- `colmeia/_config/construcao-monorepo.md` para monorepo, CI/CD e rollout

**Favo 04 — SDD + CI/CD:** specs → código → **CI** (hash, sem deploy) → **CD** Sandbox → Homolog (virtualização + mock) → Produção (apontamento `commit_hash`) → rollout canário com validação do Head.

**Favo 05 — ERT:** `/ert-*` — Incident Commander, Logger, Comm, SMEs (visão 360°).
