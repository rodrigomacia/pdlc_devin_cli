#!/usr/bin/env bash
# setup-devin-cli.sh — Configura o Ciclo de Produtação Digital para Devin CLI
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT"

RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m'

info()  { echo -e "${BLUE}→${NC} $*"; }
ok()    { echo -e "${GREEN}✓${NC} $*"; }
warn()  { echo -e "${YELLOW}!${NC} $*"; }
fail()  { echo -e "${RED}✗${NC} $*" >&2; exit 1; }

echo ""
echo "═══════════════════════════════════════════════════════════"
echo "  Ciclo de Produtação Digital — Setup Devin CLI"
echo "═══════════════════════════════════════════════════════════"
echo ""

# ── 1. Devin CLI instalado ─────────────────────────────────────────────────
if command -v devin >/dev/null 2>&1; then
  DEVIN_VER="$(devin --version 2>/dev/null || devin version 2>/dev/null || echo 'instalado')"
  ok "Devin CLI encontrado ($DEVIN_VER)"
else
  warn "Devin CLI não encontrado no PATH."
  echo ""
  echo "  Instale em: https://cli.devin.ai"
  echo "  macOS/Linux: curl -fsSL https://cli.devin.ai/install.sh | bash"
  echo ""
  if [[ -t 0 ]] && [[ "${SKIP_DEVIN_CHECK:-}" != "1" ]]; then
    read -r -p "  Continuar setup da estrutura local mesmo assim? [s/N] " CONT
    [[ "${CONT,,}" == "s" || "${CONT,,}" == "sim" ]] || fail "Instale o Devin CLI e execute novamente."
  else
    warn "Continuando sem Devin CLI (modo não interativo)."
  fi
fi

# ── 2. Estrutura .devin ──────────────────────────────────────────────────────
[[ -d .devin/skills ]] || fail "Pasta .devin/skills ausente. Execute na raiz do repositório."
[[ -d .devin/agents ]] || fail "Pasta .devin/agents ausente."

SKILL_COUNT="$(find .devin/skills -name 'SKILL.md' 2>/dev/null | wc -l | tr -d ' ')"
AGENT_COUNT="$(find .devin/agents -name 'AGENT.md' 2>/dev/null | wc -l | tr -d ' ')"
ok "$SKILL_COUNT skills · $AGENT_COUNT agents"

[[ -f .devin/config.json ]] || fail ".devin/config.json ausente"
if [[ ! -f .devin/config.local.json ]]; then
  cp .devin/config.local.json.example .devin/config.local.json
  ok "Criado .devin/config.local.json (edite MCP e segredos)"
else
  ok ".devin/config.local.json já existe"
fi

# ── 3. Runtime colmeia (artefatos de execução) ───────────────────────────────
RUNTIME_DIRS=(
  "colmeia/01-contexto-estrategico/_iniciativas"
  "colmeia/02-discovery/_iniciativas"
  "colmeia/03-experimentacao/_iniciativas"
  "colmeia/04-construcao/_iniciativas"
  "colmeia/05-operacao/_iniciativas"
  "colmeia/_handoffs"
  "colmeia/_grill"
)

for d in "${RUNTIME_DIRS[@]}"; do
  mkdir -p "$d"
  touch "$d/.gitkeep"
done
ok "Pastas runtime (_iniciativas, _handoffs, _grill)"

# ── 4. Config templates colmeia/_config ──────────────────────────────────────
CONFIG_FILES=(
  "colmeia/_config/okr-plataforma.md"
  "colmeia/_config/discovery-tools.md"
  "colmeia/_config/construcao-monorepo.md"
)
for f in "${CONFIG_FILES[@]}"; do
  if [[ -f "$f" ]]; then
    if grep -q '\[FORNECER' "$f" 2>/dev/null; then
      warn "$f — ainda contém placeholders [FORNECER]"
    fi
  else
    warn "Ausente: $f"
  fi
done

OPTIONAL_GOV="colmeia/_config/governanca.md"
if [[ ! -f "$OPTIONAL_GOV" ]]; then
  cat > "$OPTIONAL_GOV" << 'EOF'
---
config: governanca
versao: 1.0
status: opcional
---

# Governança (opcional)

Ative com `/governanca-check {id} {favo}` quando políticas internas exigirem checklist extra.
EOF
  ok "Criado $OPTIONAL_GOV (opcional)"
fi

# ── 5. AGENTS.md na raiz ─────────────────────────────────────────────────────
[[ -f AGENTS.md ]] || fail "AGENTS.md ausente na raiz do projeto"
ok "AGENTS.md presente"

# ── 6. Verificação de skills críticas ────────────────────────────────────────
CRITICAL_SKILLS=(
  orquestrar-producao
  grill-me
  feature-stories
  decidir-experimento
  review-pr
  ci-validar
)
MISSING=0
for s in "${CRITICAL_SKILLS[@]}"; do
  if [[ ! -f ".devin/skills/$s/SKILL.md" ]]; then
    warn "Skill crítica ausente: $s"
    MISSING=$((MISSING + 1))
  fi
done
[[ $MISSING -eq 0 ]] && ok "Skills críticas do ciclo verificadas"

# ── 7. Documentação (opcional) ───────────────────────────────────────────────
if [[ "${1:-}" == "--with-docs" ]] || [[ "${BUILD_DOCS:-}" == "1" ]]; then
  info "Gerando site de documentação..."
  bash "$ROOT/scripts/build-docs-site.sh"
fi

# ── Resumo ───────────────────────────────────────────────────────────────────
echo ""
echo "═══════════════════════════════════════════════════════════"
echo -e "  ${GREEN}Setup concluído${NC}"
echo "═══════════════════════════════════════════════════════════"
echo ""
echo "  Próximos passos:"
echo ""
echo "  1. Edite colmeia/_config/okr-plataforma.md"
echo "  2. Edite colmeia/_config/discovery-tools.md"
echo "  3. Edite colmeia/_config/construcao-monorepo.md"
echo "  4. Configure MCP em .devin/config.local.json"
echo "  5. Na pasta do projeto: devin"
echo "  6. Primeiro comando: /orquestrar-producao {id-da-iniciativa}"
echo ""
echo "  Documentação local: docs/index.html"
echo "  Guia: docs/guia-inicio.html"
echo ""
echo "  Publicar GitHub Pages:"
echo "    bash scripts/build-docs-site.sh"
echo "    git push  (workflow .github/workflows/pages.yml)"
echo ""
