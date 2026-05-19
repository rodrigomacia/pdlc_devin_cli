---
favo: 00-nucleo
versao: 1.0
status: estavel
---

# Experimentação (03) × Discovery (02) × Rollout (04)

Evita confusão entre três momentos de validação.

## Favo 02 — Discovery

- **SVM** = filtro barato com personas sintéticas (`[SINTÉTICO]`)
- **Protótipo Figma** = experiência tangível
- **Feature stories** = pacote **candidato** (`validacao_real: pendente`)

Gate 02 libera handoff para **teste com clientes reais** — não para construção em escala.

## Favo 03 — Experimentação (clientes reais)

- Testa hipóteses do `hipoteses.yaml` e critérios das histórias
- Tipos: `entrevista`, `prototipo`, `pretotype`, `ab` (Head executa ou coordena)
- **`spike` removido** do fluxo Head — factibilidade técnica é agente (`implementador` em POC), não experimento de produto

Decisões:

| Decisão | Próximo passo |
|---------|----------------|
| `scale` | Atualizar feature `validacao_real: confirmada` → favo 04 |
| `iterate` / `pivot` | `/curar-contexto 03 02` → refinar discovery |
| `kill` | Encerrar iniciativa ou novo ciclo 01 |
| `defer` | Aguardar — não avançar gate |

## Favo 04 — Construção + CD + Rollout

- **Homolog:** qualidade automatizada (funcional + NFR) com SV/mock — **não** substitui favo 03
- **Produção canário:** Head valida KPIs com clientes reais **no ambiente produtivo**

## Regra

Não pular favo 03 se a hipótese nunca foi testada com cliente real (exceto política explícita do operador documentada).
