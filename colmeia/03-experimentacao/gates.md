---
favo: 03-experimentacao
versao: 2.0
---

# Gate 03

## Checklist

- [ ] **G3.1** `experiments-backlog.md` alinhado a **`hipoteses.yaml`** e histórias prioritárias
- [ ] **G3.2** Top hipóteses têm experimento com `hipotese_ref` e critérios pré-definidos
- [ ] **G3.3** Cada experimento executado tem critério de decisão **antes** da execução
- [ ] **G3.4** `decisao-experimentos.md` com veredito e **próximo favo** explícito
- [ ] **G3.5** ≥ 1 decisão `scale` com evidência **de cliente real** (não SVM)
- [ ] **G3.6** Se `scale`: `feature-{id}.md` → `validacao_real: confirmada`
- [ ] **G3.7** Handoff gerado (03→04 ou 03→02)

## Grill-me

- [ ] **G3.G1** `/grill-me experimento` ≠ BLOQUEAR
- [ ] **G3.G2** `/grill-me decisao-exp` ≠ BLOQUEAR
- [ ] **G3.G3** `/grill-me gate-03` registrado
- [ ] **G3.REG** `registro-decisoes-grill.yaml` — **100%** experimentos do backlog + hipóteses ligadas com decisão (`scale`/`iterate`/`kill`/`defer`) e motivadores

## Códigos

| Código | Condição |
|--------|----------|
| EXP-01 | Critério de sucesso ausente |
| EXP-02 | Decisão sem resultado |
| EXP-03 | Scale sem evidência mínima |
| EXP-04 | Scale sem `validacao_real: confirmada` na feature |
| GOV-01 | Governança pendente |
| GRILL-REG-01 | Registro incompleto pós grill |
| GRILL-REG-02 | Kill/defer sem motivadores_nao_continuar |

## Decisões

`scale` → 04 · `iterate`/`pivot`/`kill` → 02 · `defer` → aguardar
