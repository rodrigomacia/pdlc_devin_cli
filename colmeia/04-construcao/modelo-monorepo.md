---
favo: 04-construcao
versao: 1.0
tags: [monorepo, bff, frontend, aws, integracoes]
---

# Modelo de monorepo — referência SDD

Configuração operacional: [`colmeia/_config/construcao-monorepo.md`](../_config/construcao-monorepo.md)

O Head **não gerencia** esta estrutura — agents e `/spec-tecnica` mapeiam histórias para camadas.

## Visão para o Head (uma frase por camada)

| Camada | O que o cliente percebe |
|--------|-------------------------|
| **App nativo** | Experiência no celular (iOS/Android) |
| **Web (SSG)** | Telas web dentro do app (webview) — mesma jornada do protótipo Figma |
| **BFF** | Orquestra dados e regras — o app não fala direto com sistemas legados |
| **Integrações** | Conexão padronizada com **Sistema produto** (conta, cartão, etc.) |
| **Infra AWS** | Disponibilidade em **múltiplas regiões** — resiliência |

## Estrutura lógica

```
{monorepo-root}/
├── apps/
│   ├── mobile-native/          # iOS + Android (nativo)
│   ├── web-ssg/                # React SSG — webview
│   └── bff/                    # Golang — API para apps
├── packages/
│   ├── design-system/          # UI compartilhada web + tokens nativos
│   ├── contracts/              # OpenAPI / eventos — contrato BFF ↔ apps
│   └── observability/          # métricas, traces (ligação favo 05)
├── integrations/
│   ├── sistema-produto/        # adaptadores padronizados
│   └── {dominio}/              # extensões por domínio
├── infra/
│   ├── terraform/              # AWS multi-região
│   ├── pipelines/              # CI/CD — testes automatizados
│   └── rollout/                # flags segmentação cliente
└── docs/
    └── sdd/{iniciativa_id}/    # specs runtime (espelho ou symlink)
```

## Mapeamento spec técnica → paths

| Tipo de história | Camadas típicas |
|------------------|-----------------|
| Nova tela / jornada | `web-ssg`, `mobile-native`, `bff` |
| Nova regra de negócio | `bff`, `integrations/sistema-produto` |
| Novo dado de produto | `integrations/*`, contratos |
| SLO / escala / DR | `infra/terraform`, `infra/pipelines` |
| Segmentação rollout | `infra/rollout`, feature flags |

## AWS multi-região (agents)

- Active-active ou active-passive conforme `_config`
- Dados: residência e replicação documentados em `spec-nfr`
- BFF stateless; sessão conforme política do banco

## Integrações Sistema produto

Padrão único de adaptador:

```yaml
integration:
  id: int-{dominio}-{nn}
  sistema_produto: "{nome}"
  operacao: read | write | event
  contrato: packages/contracts/{nome}.yaml
  idempotencia: true
  timeout_ms: [FORNECER]
  circuit_breaker: true
```

## CI × CD (segregados)

| Fase | Doc |
|------|-----|
| CI (build + commit_hash) | [modelo-pipeline.md](./modelo-pipeline.md) |
| CD Sandbox · Homolog · Produção | [modelo-ci-cd.md](./modelo-ci-cd.md) |

Head recebe `ci-status-{id}.md` e `cd-status-head-{id}.md` — não executa pipelines.
