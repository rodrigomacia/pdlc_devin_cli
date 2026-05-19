---
name: prototipo-figma
description: Especifica protótipo Figma de jornada com anotações de hipótese — favo 02
argument-hint: "<id>"
agent: prototipador
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
    - Write(colmeia/02-discovery/_iniciativas/**/prototipo-spec.md)
    - Write(colmeia/02-discovery/_iniciativas/**/prototipo/**)
---

@colmeia/02-discovery/modelo-discovery.md
@colmeia/02-discovery/capacidades-tools.md
@colmeia/02-discovery/artefatos.md
@colmeia/_config/discovery-tools.md

ID: **$ARGUMENTS**

1. Ler `hipoteses.yaml` — apenas hipóteses com `status: strong` ou `iterate`
2. Se zero hipóteses elegíveis → parar (voltar para `gerar-hipoteses` / `testar-svm`)
3. Gerar `prototipo-spec.md`:
   - Fluxo principal: sequência de telas + transição
   - Fluxos alternativos: erro, sem dado, sem conexão
   - Cada tela com `hipotese_ref` e KPI alvo
   - Variantes A/B (se planejado para favo 03)
   - Anotações textuais por tela (o que se aprende)
4. Quando Figma MCP configurado: anexar URL Figma + frame raiz; quando não, deixar `[FORNECER URL FIGMA]`
5. Linguagem de experiência, **não** de implementação técnica (`DIS-FIG-01` se tela sem hipótese)
