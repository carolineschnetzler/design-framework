#!/bin/bash
# Design Framework — install
#
# Symlinks this framework's agents and skills into ~/.claude/ so they load in EVERY
# session, not only when Claude Code is started from this directory.
#
# Symlinks rather than copies: the repo stays the single source of truth, and an
# edit here takes effect immediately with no re-install step.
#
#   ./install.sh              install or refresh
#   ./install.sh --uninstall  remove only the links this script created
#   ./install.sh --status     show what is linked

set -euo pipefail
FRAMEWORK_DIR="$(cd "$(dirname "$0")" && pwd)"
CLAUDE_DIR="$HOME/.claude"
MODE="${1:-install}"

is_ours() { [ -L "$1" ] && [[ "$(readlink "$1")" == "$FRAMEWORK_DIR"/* ]]; }

case "$MODE" in
--status)
  echo "Framework: $FRAMEWORK_DIR"; echo
  echo "Linked agents:"
  for f in "$CLAUDE_DIR"/agents/*.md; do [ -e "$f" ] && is_ours "$f" && echo "  $(basename "$f" .md)"; done
  echo "Linked skills:"
  for d in "$CLAUDE_DIR"/skills/*; do [ -e "$d" ] && is_ours "$d" && echo "  $(basename "$d")"; done
  exit 0 ;;

--uninstall)
  n=0
  for f in "$CLAUDE_DIR"/agents/*.md "$CLAUDE_DIR"/skills/*; do
    [ -e "$f" ] || continue
    if is_ours "$f"; then rm "$f"; n=$((n+1)); fi
  done
  echo "Removed $n link(s). Files inside $FRAMEWORK_DIR were not touched."
  exit 0 ;;
esac

mkdir -p "$CLAUDE_DIR/agents" "$CLAUDE_DIR/skills"

echo "Installing from $FRAMEWORK_DIR"
echo

# --- Agents -------------------------------------------------------------
echo "Agents:"
for src in "$FRAMEWORK_DIR"/.claude/agents/*.md; do
  name="$(basename "$src")"
  dest="$CLAUDE_DIR/agents/$name"
  if [ -e "$dest" ] && ! is_ours "$dest"; then
    echo "  SKIP  ${name%.md} — a file already exists there that this framework did not create"
    continue
  fi
  ln -sfn "$src" "$dest"
  echo "  link  ${name%.md}"
done
echo

# --- Skills -------------------------------------------------------------
# Skills are discovered as <skills-root>/<name>/SKILL.md, so each skill
# directory is linked by the skill's own name regardless of how it is
# grouped inside the repo.
echo "Skills:"
while IFS= read -r skillfile; do
  dir="$(dirname "$skillfile")"
  name="$(grep -m1 '^name:' "$skillfile" | sed 's/^name:[[:space:]]*//' | tr -d '"' | tr -d "'")"
  [ -n "$name" ] || name="$(basename "$dir")"
  dest="$CLAUDE_DIR/skills/$name"
  if [ -e "$dest" ] && ! is_ours "$dest"; then
    echo "  SKIP  $name — something already exists there that this framework did not create"
    continue
  fi
  ln -sfn "$dir" "$dest"
  echo "  link  $name"
done < <(find "$FRAMEWORK_DIR/.claude/skills" -name SKILL.md | sort)
echo

# --- Report anything that will never load -------------------------------
loose=$(find "$CLAUDE_DIR/skills" -maxdepth 1 -name '*.md' 2>/dev/null | wc -l | tr -d ' ')
if [ "$loose" -gt 0 ]; then
  echo "Note: $loose loose .md file(s) sit directly in $CLAUDE_DIR/skills/."
  echo "Skills load as <name>/SKILL.md, so those never load. Left alone — review and remove them yourself:"
  find "$CLAUDE_DIR/skills" -maxdepth 1 -name '*.md' -exec basename {} \; | sed 's/^/  /'
  echo
fi

cat <<'EOF'
Done. The agents and skills above are now available in every Claude Code session.

Hooks are deliberately NOT installed globally. They are project-scoped in
.claude/settings.json and run when you work from this directory or a directory
that inherits it — a canvas standards check on every design write, and a drift
check on the paths each project declares. Installing them globally would run
them against unrelated work.
EOF
