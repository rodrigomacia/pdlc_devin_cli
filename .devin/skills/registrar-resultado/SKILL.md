---
name: registrar-resultado
description: Registra resultado de experimento executado — favo 03
argument-hint: "<id> <E-id>"
allowed-tools:
  - read
  - edit
permissions:
  allow:
    - Read(colmeia/03-experimentacao/_iniciativas/**)
    - Write(colmeia/03-experimentacao/_iniciativas/**)
---

@colmeia/03-experimentacao/artefatos.md

ID: **$1** | Experimento: **$2**

1. Abrir `colmeia/03-experimentacao/_iniciativas/$1/experimento-$2.md`
2. Se ausente: erro — rodar `/design-experimento` primeiro
3. Preencher seção **Resultado** só com dados fornecidos pelo operador na sessão
4. Se operador não forneceu dados: `[RESULTADO: fornecer]` — não inventar
5. Atualizar status → `concluido` e linha no `experiments-backlog.md`

Não alterar critérios de decisão já definidos.
