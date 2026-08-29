#!/bin/bash
# Design Framework — session initialization.
# Prints framework status. Intentionally terse: this is orientation, not a report.

FRAMEWORK_DIR="$(cd "$(dirname "$0")/.." && pwd)"
MEMORY_FILE="$FRAMEWORK_DIR/taste-profile.md"

echo "=== Design Framework ==="
echo ""

if [ -f "$MEMORY_FILE" ]; then
  COUNT=$(grep -c "^- " "$MEMORY_FILE" 2>/dev/null || echo 0)
  echo "Design memory: taste-profile.md ($COUNT entries)"
else
  echo "Design memory: none yet"
fi
echo ""

PROJECT_DIRS=$(ls -d "$FRAMEWORK_DIR/projects"/*/ 2>/dev/null)
if [ -n "$PROJECT_DIRS" ]; then
  echo "Projects:"
  for dir in $PROJECT_DIRS; do
    STATUS=""
    [ -f "$dir/design-brief.md" ]  && STATUS="$STATUS brief"
    [ -f "$dir/taste-profile.md" ] && STATUS="$STATUS taste"
    [ -f "$dir/design-state.md" ]  && STATUS="$STATUS state"
    [ -f "$dir/design-system.md" ] && STATUS="$STATUS system"
    [ -f "$dir/prototype.json" ]   && STATUS="$STATUS prototype"
    STACK=$(python3 -c "import json,sys;print(json.load(open('$dir/prototype.json')).get('stack',''))" 2>/dev/null)
    [ -n "$STACK" ] && STACK=" ($STACK)"
    echo "  - $(basename "$dir")$STACK [${STATUS:- empty} ]"
  done
else
  echo "No projects yet. Use /discover to start one."
fi
echo ""

# Vendor currency. The framework defers to vendor skills, so knowing they're
# present and current matters more than anything this repo documents about them.
PLUGINS=~/.claude/plugins/installed_plugins.json
if [ -f "$PLUGINS" ]; then
  python3 - "$PLUGINS" << 'PY' 2>/dev/null
import json, sys, datetime
d = json.load(open(sys.argv[1])).get("plugins", {})
rows = []
for name, installs in d.items():
    for i in installs:
        upd = (i.get("lastUpdated") or "")[:10]
        rows.append(f"  - {name.split('@')[0]} {i.get('version','?')} (updated {upd or 'unknown'})")
if rows:
    print("Vendor skills installed:")
    print("\n".join(sorted(set(rows))))
PY
  echo ""
fi

# Structural self-check. Silent when clean; the whole point is that rot
# announces itself instead of sitting here for months.
if [ -x "$FRAMEWORK_DIR/doctor.py" ]; then
  "$FRAMEWORK_DIR/doctor.py" --quiet || true
fi

AUDIT_FILE="$FRAMEWORK_DIR/audit/latest-audit.md"
if [ -f "$AUDIT_FILE" ]; then
  echo "Last framework audit: $(head -5 "$AUDIT_FILE" | grep -oE '[0-9]{4}-[0-9]{2}-[0-9]{2}' | head -1)"
else
  echo "No framework audit yet. Run /audit to check currency."
fi
