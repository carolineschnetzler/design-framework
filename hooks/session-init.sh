#!/bin/bash
# PureMath Design Framework — Session Initialization
# Runs on every SessionStart to load context and print status

FRAMEWORK_DIR="$(cd "$(dirname "$0")/.." && pwd)"
MEMORY_FILE="$FRAMEWORK_DIR/taste-profile.md"

echo "=== PureMath Design Framework ==="
echo ""

# Cross-project design memory
if [ -f "$MEMORY_FILE" ]; then
  echo "Design memory: loaded from taste-profile.md"
  OPINION_COUNT=$(grep -c "^- " "$MEMORY_FILE" 2>/dev/null || echo "0")
  echo "  ($OPINION_COUNT entries)"
else
  echo "Design memory: none found at taste-profile.md"
fi

echo ""

# Active projects
PROJECT_DIRS=$(ls -d "$FRAMEWORK_DIR/projects"/*/ 2>/dev/null)
if [ -n "$PROJECT_DIRS" ]; then
  echo "Projects:"
  for dir in $PROJECT_DIRS; do
    PROJECT_NAME=$(basename "$dir")
    STATUS=""
    [ -f "$dir/design-brief.md" ] && STATUS="$STATUS brief"
    [ -f "$dir/taste-profile.md" ] && STATUS="$STATUS taste"
    [ -f "$dir/design-state.md" ] && STATUS="$STATUS state"
    [ -f "$dir/design-system.md" ] && STATUS="$STATUS system"
    [ -f "$dir/handoff-spec.md" ] && STATUS="$STATUS handoff"
    if [ -n "$STATUS" ]; then
      echo "  - $PROJECT_NAME [$STATUS ]"
    else
      echo "  - $PROJECT_NAME [empty]"
    fi
  done
else
  echo "No projects found. Use /discover to start a new project."
fi

echo ""

# Latest audit
AUDIT_FILE="$FRAMEWORK_DIR/audit/latest-audit.md"
if [ -f "$AUDIT_FILE" ]; then
  AUDIT_DATE=$(head -5 "$AUDIT_FILE" | grep -oE '[0-9]{4}-[0-9]{2}-[0-9]{2}' | head -1)
  echo "Last audit: $AUDIT_DATE"
else
  echo "No audit history. Run /audit to check framework currency."
fi
