---
name: review-metricas
description: Review de métricas vs OKR — favo 05
argument-hint: "<id> [periodo]"
model: sonnet
allowed-tools:
  - read
  - grep
  - glob
  - edit
permissions:
  allow:
    - Read(colmeia/**)
    - Write(colmeia/05-operacao/_iniciativas/**)
---

@colmeia/05-operacao/artefatos.md
@colmeia/05-operacao/gates.md

ID: **$1** | Período: **$2** ou `[FORNECER]`

1. Ler OKR em `colmeia/01-contexto-estrategico/_iniciativas/$1/okr-*.md`
2. Operador fornece valores atuais — **não inventar**
3. Gerar `metricas-review-{periodo}.md`
4. Classificar status: no_track | at_risk | off_track (só se operador deu meta e atual)
