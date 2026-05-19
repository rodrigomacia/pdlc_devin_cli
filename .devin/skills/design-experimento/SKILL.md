---
name: design-experimento
description: Plano de experimento ligado a hipóteses e histórias — favo 03
argument-hint: "<id> [E-id]"
agent: experiment-lead
model: sonnet
allowed-tools:
  - read
  - edit
  - grep
  - glob
permissions:
  allow:
    - Read(colmeia/**)
    - Write(colmeia/03-experimentacao/_iniciativas/**)
---

@colmeia/03-experimentacao/artefatos.md
@colmeia/03-experimentacao/gates.md
@colmeia/00-nucleo/modelo-experimentacao-discovery.md

ID: **$1** | Experimento: **$2**

1. Ler `feature-$1.md`, `historias.yaml`, `hipoteses.yaml`, `prototipo-spec.md` em favo 02 — Gate 02 obrigatório
2. Ler `ost-$1.md` apenas como contexto complementar (não é entrada primária)
3. Criar/atualizar `experiments-backlog.md` a partir de hipóteses prioritárias
4. Se `$2`: criar `experimento-$2.md` com `hipotese_ref`, `historia_ids`, critérios **ANTES** da execução
5. Tipos permitidos: entrevista, prototipo, pretotype, ab — **não** spike
6. Parar → `/grill-me $1 experimento`

Proibido: resultados inventados; critérios pós-execução; confundir SVM com evidência real.
