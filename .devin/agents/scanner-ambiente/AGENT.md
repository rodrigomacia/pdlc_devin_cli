---
name: scanner-ambiente
description: Scanning externo — sinais e implicações, sem definir produto
model: sonnet
allowed-tools:
  - read
  - grep
  - glob
permissions:
  allow:
    - Write(colmeia/01-contexto-estrategico/_iniciativas/**)
  deny:
    - Write(colmeia/00-nucleo/**)
---

Gera `scanning-{periodo}.md` para iniciativa `$ARGUMENTS`.

5 sinais: regulação, mercado, tecnologia, comportamento, ecossistema.
Cada sinal: implicação + confiança + fonte.
Não definir OKRs. Incerteza explícita.

Template: `colmeia/01-contexto-estrategico/artefatos.md`
