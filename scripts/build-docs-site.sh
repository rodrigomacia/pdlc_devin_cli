#!/usr/bin/env bash
# build-docs-site.sh — Monta docs/ para GitHub Pages (HTML + espelho colmeia)
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT"

echo "→ Montando site em docs/ ..."

python3 "$ROOT/scripts/generate-catalogo-html.py"

# Espelho da colmeia (markdown de referência no Pages)
rm -rf docs/colmeia
mkdir -p docs/colmeia

rsync -a \
  --exclude '_iniciativas/*' \
  --exclude '_iniciativas/**' \
  colmeia/ docs/colmeia/

# AGENTS na raiz do site
cp AGENTS.md docs/AGENTS.md

# Contagem para validação
SKILLS="$(find .devin/skills -name 'SKILL.md' | wc -l | tr -d ' ')"
AGENTS="$(find .devin/agents -name 'AGENT.md' | wc -l | tr -d ' ')"

cat > docs/_site-meta.json << EOF
{
  "generated": "$(date -u +%Y-%m-%dT%H:%M:%SZ)",
  "skills": $SKILLS,
  "agents": $AGENTS,
  "version": "1.0.0"
}
EOF

echo "✓ docs/colmeia/ ($(find docs/colmeia -name '*.md' | wc -l | tr -d ' ') arquivos .md)"
echo "✓ docs/AGENTS.md"
echo "✓ Site pronto para GitHub Pages (pasta /docs)"
