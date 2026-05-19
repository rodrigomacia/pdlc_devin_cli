---
name: testar-svm
description: Roda Synthetic Validation Method em hipóteses com personas sintéticas — favo 02
argument-hint: "<id> [hipotese_id]"
agent: personas-sinteticas
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
    - Write(colmeia/02-discovery/_iniciativas/**/personas-sinteticas.yaml)
    - Write(colmeia/02-discovery/_iniciativas/**/svm/**)
    - Write(colmeia/02-discovery/_iniciativas/**/hipoteses.yaml)
---

@colmeia/02-discovery/modelo-discovery.md
@colmeia/02-discovery/capacidades-tools.md
@colmeia/02-discovery/artefatos.md
@colmeia/_config/discovery-tools.md

ID: **$ARGUMENTS**

1. Ler `hipoteses.yaml`, três visões e `_config/discovery-tools.md`
2. Construir/atualizar `personas-sinteticas.yaml`:
   - 5–10 personas por hipótese (configurável)
   - Cada persona derivada de frictions (VOC) + métricas (produto) + tendências (mercado)
   - Cobrir todos os segmentos relevantes da hipótese
3. Para cada hipótese (todas se `$2` ausente; senão apenas `$2`):
   - Simular reação de cada persona — capturar aceitação, objeções, perguntas, palavras
   - Pontuar `Strong | Iterate | Kill` por segmento
   - **TODA saída marcada `[SINTÉTICO]`** — senão `DIS-SVM-02`
4. Escrever `svm/svm-{hipotese_id}.md` por hipótese (template em `artefatos.md`)
5. Atualizar `hipoteses.yaml` — campo `status` (strong/iterate/kill) e `svm_ref`
6. Não substitui teste real (favo 03)
