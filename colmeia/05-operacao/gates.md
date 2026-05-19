---
favo: 05-operacao
versao: 1.0
upstream:
  - ../04-construcao/gates.md
downstream:
  - ../02-discovery/gates.md
---

# Gate 05 — Loop operacional

Valida que operação alimenta discovery — não bloqueia deploy.

## Checklist (por período de review)

- [ ] **G5.1** `metricas-review-{periodo}.md` com KR/North Star do favo 01 referenciados
- [ ] **G5.2** Desvio vs meta classificado (no_track | at_risk | off_track) — dados do operador
- [ ] **G5.3** Incidentes relevantes têm `postmortem-*.md` ou justificativa de skip
- [ ] **G5.4** `insights-discovery.md` com ≥ 1 oportunidade nova ou repriorizada
- [ ] **G5.5** Handoff 05→02 quando insights exigem discovery

## Grill-me

- [ ] **G5.G1** `/grill-me {id} metricas` — veredito registrado
- [ ] **G5.G2** `/grill-me {id} insights` — quando handoff 05→02

## Códigos

| Código | Condição |
|--------|----------|
| OPS-01 | Métricas sem vínculo ao OKR |
| OPS-02 | Insight sem evidência operacional |
| OPS-03 | Postmortem obrigatório pendente (se política operador) |
