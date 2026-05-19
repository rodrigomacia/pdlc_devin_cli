---
name: gerar-hipoteses
description: Gera hipóteses testáveis a partir da síntese — favo 02
argument-hint: "<id>"
agent: discovery-lead
model: sonnet
allowed-tools:
  - read
  - grep
  - glob
  - edit
permissions:
  allow:
    - Read(colmeia/**)
    - Write(colmeia/02-discovery/_iniciativas/**/hipoteses.yaml)
---

@colmeia/02-discovery/modelo-discovery.md
@colmeia/02-discovery/artefatos.md

ID: **$ARGUMENTS**

1. Ler `oportunidades.md`, `mapa-evidencias.md`, `ost-$1.md`
2. Para cada oportunidade priorizada, gerar hipóteses com enunciado padrão:

   > Acreditamos que [intervenção] para [segmento] resultará em [mudança em KR/KPI]
   > porque [insight das visões]. Saberemos quando [sinal mensurável].

3. Cada hipótese carrega: `hipotese_id`, `oportunidade_ref`, `enunciado`, `segmento`, `kr_ref`, `risco` (valor/usabilidade/viabilidade/factibilidade/regulatorio), `confianca`, `status: nova`
4. Escrever em `colmeia/02-discovery/_iniciativas/$1/hipoteses.yaml` (template em `artefatos.md`)
5. Sem evidência da síntese para uma hipótese → não gerar
6. **Parar.** Próximo passo obrigatório: `/grill-me $1 hipoteses` — não avançar para SVM sem veredito ≠ BLOQUEAR
