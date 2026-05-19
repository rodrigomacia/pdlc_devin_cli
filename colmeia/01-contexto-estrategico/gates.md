---
favo: 01-contexto-estrategico
versao: 1.1
downstream:
  - ../02-discovery/gates.md
---

# Gate 01

## Checklist

- [ ] **G1.1** Um Objective outcome-based (L3)
- [ ] **G1.2** 2–4 KRs com **baseline, target, roof, moonshot** e prazo
- [ ] **G1.3** North Star referenciada (KR ou KPI com `is_north_star`)
- [ ] **G1.4** 3–5 métricas input (KPIs) com hipótese causal
- [ ] **G1.5** Tese de produto presente
- [ ] **G1.6** ≥ 3 hipóteses estratégicas para favo 02
- [ ] **G1.7** Cascata documentada em `okr-cascata.yaml` com `parent_ref`
- [ ] **G1.8** Handoff 01→02 gerado
- [ ] **G1.9** **Desdobramento:** soma de pesos `contribui` ≤ 100% por pai
- [ ] **G1.10** **Plataforma:** `sync push` OK ou exceção documentada (`OKR-SYNC-01`)

## Grill-me (obrigatório)

- [ ] **G1.G1** `/grill-me {id} okr-draft` — veredito ≠ `BLOQUEAR`
- [ ] **G1.G2** `/grill-me {id} okr-cascata` — veredito ≠ `BLOQUEAR`
- [ ] **G1.G3** `/grill-me {id} gate-01` — registrado em `gate-01-registro.md`

## Condicional

- [ ] **G1.X** `/governanca-check`

## Códigos de rejeição

| Código | Condição |
|--------|----------|
| OUT-01 | KR é só output |
| MET-01 | Baseline ausente |
| OKR-MET-01 | Qualquer uma das 4 metas ausente no KR |
| OKR-MET-02 | Ordem baseline/target/roof/moonshot incoerente |
| OKR-CAS-01 | Filho sem parent_ref |
| OKR-CAS-02 | Soma pesos > máximo configurado |
| OKR-SYNC-01 | Divergência local vs plataforma |
| STR-01 | Desalinhamento diretriz upstream |
| GOV-01 | Governança pendente |
