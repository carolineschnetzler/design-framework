#!/bin/bash
# PostToolUse hook for the prototype workflow.
# Guards the *translation* path: files that are supposed to be faithful translations
# of a design, not authored from scratch.
#
# Which paths are guarded is declared per project in projects/<name>/prototype.json:
#
#   { "hostProjectPath": "~/project",          // ~ is expanded
#     "stack": "react-vite",
#     "mode": "translate",                     // or "prototype-first" to disable the check
#     "verbatimPaths": ["src/screens/*.tsx"] } // globs, relative to hostProjectPath
#
# A project with no verbatimPaths guards nothing. That is a valid choice — say so
# in prototype.json rather than leaving the hook pointed at a directory nobody uses.
#
# Exit 0 = pass. Exit 2 = blocking violation (stderr is shown to the model).

set -u
FRAMEWORK_DIR="$(cd "$(dirname "$0")/.." && pwd)"
INPUT=$(cat)

read -r TOOL FILE_PATH <<<"$(printf '%s' "$INPUT" | python3 -c "
import sys, json
d = json.load(sys.stdin)
print(d.get('tool_name',''), d.get('tool_input',{}).get('file_path',''))
" 2>/dev/null)"

[ "$TOOL" = "Write" ] || [ "$TOOL" = "Edit" ] || exit 0
[ -n "${FILE_PATH:-}" ] && [ -f "$FILE_PATH" ] || exit 0

# Does this file fall under a guarded path of any registered project?
GUARDED=$(FRAMEWORK_DIR="$FRAMEWORK_DIR" FILE_PATH="$FILE_PATH" python3 << 'PY'
import os, json, glob, fnmatch
fw, target = os.environ["FRAMEWORK_DIR"], os.path.realpath(os.environ["FILE_PATH"])
for cfg in glob.glob(os.path.join(fw, "projects", "*", "prototype.json")):
    try:
        d = json.load(open(cfg))
    except Exception:
        continue
    if d.get("mode") == "prototype-first":
        continue
    host = d.get("hostProjectPath", "")
    if not host:
        continue
    host = os.path.realpath(os.path.expanduser(host))   # ~ is accepted in project configs
    if not target.startswith(host + os.sep):
        continue
    rel = os.path.relpath(target, host)
    for pat in d.get("verbatimPaths", []):
        if fnmatch.fnmatch(rel, pat):
            print(os.path.basename(os.path.dirname(cfg)))
            raise SystemExit
PY
)
[ -n "$GUARDED" ] || exit 0

VIOLATIONS=()

# 1 — Source traceability. Design-tool exports carry per-element source node attributes.
if ! grep -q 'data-node-id=' "$FILE_PATH"; then
  VIOLATIONS+=("MISSING source node attributes. Files on a guarded translation path must come from the design tool's design-context output, which annotates every element with its source node. Authoring from scratch is not translation. If this file is genuinely authored, it belongs outside the guarded paths — or the project is prototype-first and should say so in prototype.json.")
fi

# 2 — Header naming the source.
if ! head -10 "$FILE_PATH" | grep -qi 'translation of .* node'; then
  VIOLATIONS+=("MISSING source header. The first lines must name the source node and the date it was pulled, e.g. '// Verbatim translation of Figma node 4030:8305 (Initial-Chat). // Pulled 2026-08-28.'")
fi

# 3 — Raw values outside the token fallback pattern var(--token, #fallback).
TOTAL_HEX=$(grep -oE '#[0-9a-fA-F]{3,8}' "$FILE_PATH" | wc -l | tr -d ' ')
HEX_IN_VAR=$(grep -oE 'var\(--[a-zA-Z0-9_-]+,[[:space:]]*#[0-9a-fA-F]{3,8}' "$FILE_PATH" | wc -l | tr -d ' ')
RAW_HEX=$(( TOTAL_HEX - HEX_IN_VAR ))
if [ "$RAW_HEX" -gt 3 ]; then
  VIOLATIONS+=("$RAW_HEX raw value(s) outside the var(--token, #fallback) pattern. Raw values on a translation path mean authored styling, not translation. Bind to the project's tokens.")
fi

[ ${#VIOLATIONS[@]} -eq 0 ] && exit 0

{
  echo ""
  echo "=== PROTOTYPE DRIFT CHECK FAILED ==="
  echo "Project: $GUARDED"
  echo "File:    $FILE_PATH"
  echo ""
  i=1
  for v in "${VIOLATIONS[@]}"; do echo "$i. $v"; echo ""; i=$((i+1)); done
  echo "Per the prototype skill: translate the design tool's output with token-name and asset substitutions only."
  echo "If this work is genuinely authored or prototype-first, say so explicitly and record it in prototype.json —"
  echo "do not work around the check. An unenforced rule and a silently bypassed rule are the same thing."
  echo ""
} >&2
exit 2
