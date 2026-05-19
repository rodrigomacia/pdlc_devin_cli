---
favo: 02-discovery
versao: 2.0
upstream:
  - ../01-contexto-estrategico/gates.md
downstream:
  - ../03-experimentacao/gates.md
---

# Gate 02

Validado pelo **Head de Produto (Go-to-Market)**. Aprovação única — sem comitê externo no fluxo padrão.

## Checklist obrigatório

### Ancoragem no OKR
- [ ] **G2.1** Outcome do discovery = KR ou KPI da Plataforma OKR (favo 01)

### Três visões
- [ ] **G2.2** `visao-mercado.md` presente, com segmentação
- [ ] **G2.3** `visao-produto.md` presente — inclui ao menos funil, dead/rage click, tempo e cohort
- [ ] **G2.4** `visao-cliente.md` presente — ao menos 2 canais VOC com citações marcadas por canal
- [ ] **G2.5** `mapa-evidencias.md` rastreia cada oportunidade até visão(s) de origem

### Síntese e hipóteses
- [ ] **G2.6** Oportunidade priorizada com evidência em **≥ 2 das 3 visões**
- [ ] **G2.7** `hipoteses.yaml` — cada hipótese com `kr_ref`, `segmento`, `risco`, `confianca`

### SVM
- [ ] **G2.8** Toda hipótese que segue ao protótipo passou por `/testar-svm` — resultado `Strong` ou `Iterate` documentado
- [ ] **G2.9** `personas-sinteticas.yaml` versionado e marcado `[SINTÉTICO]`

### Protótipo e feature
- [ ] **G2.10** `prototipo-spec.md` com referência de hipótese por tela
- [ ] **G2.11** `feature-{id}.md` com:
  - Outcome (KR/KPI)
  - Hipóteses validadas
  - Histórias **agrupadas por valor + segmento**
  - Critérios de aceitação em linguagem de cliente
  - `validacao_real: pendente` (confirmação no favo 03)
- [ ] **G2.12** Handoff 02→03 gerado

### Grill-me (obrigatório)
- [ ] **G2.G1** `/grill-me {id} hipoteses` — veredito ≠ `BLOQUEAR`
- [ ] **G2.G2** `/grill-me {id} feature` — veredito ≠ `BLOQUEAR`
- [ ] **G2.G3** `/grill-me {id} gate-02` — veredito registrado em `gate-02-registro.md`
- [ ] **G2.REG** `registro-decisoes-grill.yaml` — **100%** hipóteses em `hipoteses.yaml` com decisão + motivadores após grills `hipoteses`, `svm`, `feature` (nenhum item sem linha; desconsideradas com `motivadores_nao_continuar`)

### Condicional
- [ ] **G2.R1** `/governanca-check` se política exigir
- [ ] **G2.R2** Validação Analytics — funil alinhado ao KR

## Códigos de rejeição

| Código | Condição |
|--------|----------|
| DIS-01 | Outcome desligado do OKR |
| DIS-VIS-01 | Menos de 3 visões |
| DIS-VIS-02 | Visão sem segmentação |
| DIS-EVID-01 | Oportunidade sem evidência rastreável |
| DIS-SVM-01 | Hipótese no protótipo sem SVM |
| DIS-SVM-02 | SVM apresentado como cliente real |
| DIS-FIG-01 | Tela do protótipo sem `hipotese_ref` |
| DIS-STORY-01 | História sem valor/segmento |
| DIS-STORY-02 | História com decisão técnica embutida |
| GOV-01 | Governança pendente |
| GRILL-REG-01 | Registro sem cobertura 100% dos itens |
| GRILL-REG-02 | Desconsiderar sem motivadores_nao_continuar |
| GRILL-REG-03 | Continuar/scale sem motivadores_continuar |

## Aprovador

| Papel | Obrigatório |
|-------|-------------|
| Head de Produto (Go-to-Market) | Sim — único aprovador padrão |
