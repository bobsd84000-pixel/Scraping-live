#!/usr/bin/env bash
# Usage: ./install.sh            -> global (~/.claude, tous les projets)
#        ./install.sh <dossier>  -> un projet précis (<dossier>/.claude)
set -euo pipefail

SRC="$(cd "$(dirname "$0")" && pwd)"
DEST="${1:+$1/.claude}"
DEST="${DEST:-$HOME/.claude}"

mkdir -p "$DEST/agents" "$DEST/commands"
cp "$SRC"/agents/*.md "$DEST/agents/"
cp "$SRC"/commands/*.md "$DEST/commands/"

echo "Installé dans $DEST"
echo "Agents   : $(cd "$SRC/agents" && ls *.md | sed 's/\.md$//' | tr '\n' ' ')"
echo "Commandes: $(cd "$SRC/commands" && ls *.md | sed 's/\.md$/ /;s/^/\//' | tr -d '\n')"
