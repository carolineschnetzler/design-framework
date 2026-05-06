#!/bin/bash
# PostToolUse hook for the figma-to-prototype workflow.
# Runs on Write/Edit. Catches drift on prototype screen files written outside the verbatim-paste pipeline.
# Exit 0 = pass. Exit 2 = blocking violation (Claude Code shows stderr to the model).

set -u

# Read the JSON payload Claude Code sends on stdin.
INPUT=$(cat)

# Extract tool_name and file_path from the JSON. Use Python for robust parsing.
TOOL=$(printf '%s' "$INPUT" | python3 -c "import sys,json; d=json.load(sys.stdin); print(d.get('tool_name',''))" 2>/dev/null)
FILE_PATH=$(printf '%s' "$INPUT" | python3 -c "import sys,json; d=json.load(sys.stdin); print(d.get('tool_input',{}).get('file_path',''))" 2>/dev/null)

# Only check Write/Edit operations.
if [ "$TOOL" != "Write" ] && [ "$TOOL" != "Edit" ]; then
  exit 0
fi

# Only check prototype screen files. Match common host-project paths.
case "$FILE_PATH" in
  */advpulse-prototype/src/screens/*.tsx) ;;
  */prototype/src/screens/*.tsx) ;;
  *) exit 0 ;;
esac

# Skip if the file no longer exists (rare race; PostToolUse fires after the write).
if [ ! -f "$FILE_PATH" ]; then
  exit 0
fi

VIOLATIONS=()

# Check 1 — data-node-id attributes (proves MCP-derived). Required for screens.
if ! grep -q 'data-node-id=' "$FILE_PATH"; then
  VIOLATIONS+=("MISSING data-node-id attributes. Screen files must come from mcp__figma__get_design_context output, which returns these attributes on every element. Authoring screens from scratch is not allowed in default mode. If the user explicitly invoked authoring mode, this file should be in src/components/, not src/screens/.")
fi

# Check 2 — Verbatim header comment (declares the source Figma node).
if ! head -10 "$FILE_PATH" | grep -q 'Verbatim translation of Figma node'; then
  VIOLATIONS+=("MISSING verbatim header comment. First lines of every prototype screen must declare the source Figma node, e.g.: '// Verbatim translation of Figma node 4030:8305 (Initial-Chat). // Pulled via mcp__figma__get_design_context on 2026-05-06.'")
fi

# Check 3 — Raw hex values outside var() fallback patterns.
# MCP output uses the pattern var(--token-name, #1c1c1c). Hex inside that pattern is fine.
# Hex outside that pattern (e.g., bg-[#1c1c1c] or color: #1c1c1c standalone) signals authored styling.
# Strategy: count all hex occurrences, then count hex inside var(...,#...) patterns. Flag if difference is significant.
TOTAL_HEX=$(grep -oE '#[0-9a-fA-F]{3,8}' "$FILE_PATH" | wc -l | tr -d ' ')
HEX_IN_VAR=$(grep -oE 'var\(--[a-zA-Z0-9_-]+,\s*#[0-9a-fA-F]{3,8}' "$FILE_PATH" | wc -l | tr -d ' ')
RAW_HEX=$((TOTAL_HEX - HEX_IN_VAR))

if [ "$RAW_HEX" -gt 3 ]; then
  VIOLATIONS+=("$RAW_HEX raw hex value(s) outside var() fallback patterns. Design tokens must use var(--token-name, #fallback). Raw hex outside this pattern indicates authored styling, not MCP-derived translation.")
fi

# Pass if no violations.
if [ ${#VIOLATIONS[@]} -eq 0 ]; then
  exit 0
fi

# Print violations to stderr for the model to see.
{
  echo ""
  echo "=== PROTOTYPE DRIFT CHECK FAILED ==="
  echo "File: $FILE_PATH"
  echo ""
  i=1
  for v in "${VIOLATIONS[@]}"; do
    echo "$i. $v"
    echo ""
    i=$((i + 1))
  done
  echo "Per the figma-to-prototype skill: paste mcp__figma__get_design_context output verbatim, swap only CSS-var names and asset components, never author screens from scratch. If the user explicitly requested authored content, that work belongs in src/components/ (and should be clearly flagged in your response as authored)."
  echo ""
} >&2

# Exit 2 = blocking error. The model sees the stderr output and is expected to correct.
exit 2
