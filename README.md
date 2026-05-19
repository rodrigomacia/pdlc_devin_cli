# Ciclo de Produtação Digital — Framework de Skills

Framework open source para executar o ciclo completo de produtação digital via **Devin CLI** — sem conteúdo de produto versionado.

[![Documentação](https://img.shields.io/badge/docs-GitHub%20Pages-003882)](docs/index.html)
[![Skills](https://img.shields.io/badge/skills-46-orange)](#46-skills)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

## Ciclo (5 favos)

```
01 Contexto → 02 Discovery → 03 Experimentação → 04 Construção → 05 Operação
                                                              ↓
                                                         (loop → 02)
```

Mapa: [`colmeia/00-nucleo/ciclo-completo.md`](colmeia/00-nucleo/ciclo-completo.md)

## 46 skills

| Favo | Comandos |
|------|----------|
| 00 | `/orquestrar-producao`, `/curar-contexto` |
| 01 | `/sync-okr-plataforma`, `/draft-okr`, `/desdobrar-okr`, `/auditar-okr` |
| 02 | `/visao-mercado`, `/visao-produto`, `/visao-cliente`, `/sintetizar-visoes`, `/gerar-hipoteses`, `/testar-svm`, `/prototipo-figma`, `/feature-stories`, `/prep-entrevista` |
| 03 | `/experiments-backlog`, `/design-experimento`, `/registrar-resultado`, `/decidir-experimento` (clientes reais; `scale`→04) |
| 04 | SDD → `/review-pr` **antes** CI/CD → `/ci-validar` · `/cd-promover` · rollout · `/rollout-rollback` (ver catálogo) |
| 05 | `/review-metricas`, `/ert-abrir`, `/ert-comandar`, `/ert-registrar`, `/ert-comunicar`, `/ert-diagnosticar`, `/ert-fechar`, `/postmortem`, `/insight-para-discovery` |
| ∅ | `/grill-me` (adversário em cada decisão) · `/governanca-check` |

**Favo 02 — modelo Go-to-Market:** o Head de Produto (agente `discovery-lead`) atravessa discovery ponta-a-ponta. Demais agentes do favo são subagentes/tools (VOC, analytics, personas sintéticas, Figma, feature writer).

Catálogo: [`colmeia/00-nucleo/catalogo-skills.md`](colmeia/00-nucleo/catalogo-skills.md)

## Como começar

### Head de Produto (não técnico)

**Precisa clonar o repositório no dia a dia? Não.**  
Abra o Devin na pasta que a TI preparou e comece por:

```
/orquestrar-producao {nome-da-sua-iniciativa}
```

Guia completo em linguagem simples: **[GUIA-HEAD.md](GUIA-HEAD.md)** · [versão web](docs/guia-inicio.html)

### Setup único (TI / primeira vez)

Baixar o projeto **uma vez** e preparar conexões (OKR, analytics, VOC):

```bash
git clone https://github.com/rodrigomacia/pdlc_devin_cli.git
cd pdlc_devin_cli
./scripts/setup-devin-cli.sh
```

Detalhes: [docs/configuracao.html](docs/configuracao.html)

**Site:** [rodrigomacia.github.io/pdlc_devin_cli](https://rodrigomacia.github.io/pdlc_devin_cli)

## Estrutura

- `.devin/` — execução
- `colmeia/` — fluxo, gates, templates, mapa agentes
- `AGENTS.md` — regras do agente
- [`docs/index.html`](docs/index.html) — **portal de documentação** (GitHub Pages)
- [`docs/guia-inicio.html`](docs/guia-inicio.html) — guia de início rápido
- [`docs/configuracao.html`](docs/configuracao.html) — setup Devin CLI
- [`docs/apresentacao-executiva.html`](docs/apresentacao-executiva.html) — apresentação ao comitê executivo
- [`docs/fluxo-producao.html`](docs/fluxo-producao.html) — visão do framework (skills, agentes, tools)
- [`docs/fluxo-head-produto-devin.html`](docs/fluxo-head-produto-devin.html) — fluxo do Head de Produto conversando com Devin CLI (inclui grill-me)
