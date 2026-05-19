---
config: construcao-monorepo
versao: 2.0
status: template
---

# Configuração — Monorepo, CI e CD

Skills do favo 04 leem este arquivo. Modelo: [modelo-ci-cd.md](../04-construcao/modelo-ci-cd.md).

## Repositório

```yaml
monorepo:
  root: "[FORNECER — path ou URL do repo]"
  default_branch: main
  sdd_docs_path: "docs/sdd"
```

## CI (Integração Contínua) — segregado do CD

```yaml
ci:
  mcp: "[FORNECER — GitHub Actions / GitLab / Jenkins]"
  workflow: "[FORNECER — .github/workflows/ci.yml]"
  trigger: [pull_request, push]
  artifact:
    registry: "[FORNECER — ECR / GCR / etc.]"
    tag_policy: commit_hash    # obrigatório — nunca latest em promoção
  cobertura_minima_unit: 80
  stages: [lint, sast, unit, contract, build]
```

## CD (Entrega Contínua) — três ambientes

```yaml
cd:
  mcp: "[FORNECER]"
  promotion_order: [sandbox, homolog, producao]
  require_same_commit_hash: true

  sandbox:
    cluster: "[FORNECER]"
    sistema_produto_endpoint: "[FORNECER — sandbox real]"
    post_deploy_tests: [integration-smoke, historia-critical-path]
    auto_promote_to_homolog: false   # após verde manual ou skill

  homolog:
    cluster: "[FORNECER]"
    service_virtualization:
      enabled: true
      provider: "[FORNECER — WireMock / Mountebank / Hoverfly]"
      recordings_path: "infra/sv-recordings"
    mocks:
      profile_path: "integrations/sistema-produto/mocks"
      profile_per_iniciativa: true
    post_deploy_tests:
      - functional-historias
      - nfr-perf
      - nfr-security
      - contract-vs-mocks

  producao:
    deploy_model: commit_hash_pointer   # apontamento imutável
    cluster: "[FORNECER — multi-region]"
    regions: ["sa-east-1", "us-east-1"]
    dr_mode: active-active | active-passive
    rollback:
      strategy: redeploy_previous_hash
      previous_hash_retention: 10
    rollout:
      provider: "[FORNECER — LaunchDarkly / AppConfig]"
      segmentacao_fonte: "[FORNECER — CDP]"
```

## AWS multi-região (Produção)

```yaml
aws:
  primary_region: "[FORNECER]"
  regions: ["sa-east-1", "us-east-1"]
```

## Integrações Sistema produto

```yaml
sistema_produto:
  contratos_path: "packages/contracts"
  sandbox_endpoint: "[FORNECER]"
  homolog_mode: service_virtualization_and_mock
  producao_endpoint: "[FORNECER]"
```

## Segurança

```yaml
security:
  sast: "[FORNECER]"
  dependency_scan: "[FORNECER]"
  secrets_scan: true
  dast_homolog: "[FORNECER — opcional pós-deploy homolog]"
```
