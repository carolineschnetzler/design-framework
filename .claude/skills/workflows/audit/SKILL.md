---
name: audit
description: "Check framework against latest Claude Code and Figma MCP capabilities, report what could be adopted. Use when the user says /audit, 'is the framework up to date', 'check for new features', or triggered automatically by the biweekly scheduled agent."
---

# Audit Workflow

Triggered by `/audit`, at the end of `/retro`, or by the biweekly scheduled agent.

---

## Purpose

The design agent landscape moves fast. This workflow checks whether the framework is using the latest capabilities and identifies improvements worth adopting. It's a self-maintenance mechanism.

---

## Process

### Step 1: Check Claude Code Capabilities

Search for recent updates to:
- **Sub-agent features** — New frontmatter options, model routing, tool restrictions
- **Hook events** — New event types beyond SessionStart, PostToolUse, Stop
- **Skill architecture** — Changes to how skills are structured or loaded
- **Tool additions** — New built-in tools available to agents
- **Scheduled agents** — New scheduling capabilities or cron features
- **Memory and persistence** — Changes to how context persists across sessions

### Step 2: Check Figma MCP Capabilities

Search for recent updates to:
- **New MCP tools** — Tools beyond the current set (use_figma, get_design_context, get_variable_defs, etc.)
- **Plugin API updates** — New Figma Plugin API features available through use_figma
- **Variable system** — New variable types, collection features, mode capabilities
- **Component features** — New property types, slot improvements, variant capabilities
- **Dev mode and handoff** — New features that affect engineering handoff

### Step 3: Check Design Agent Practices

Search for:
- **Design agent frameworks** — Other approaches to AI-assisted design workflows
- **Figma automation patterns** — New techniques for programmatic Figma editing
- **Design system management** — New approaches to token architecture, component governance

### Step 4: Compare Against Framework

For each finding, evaluate:
- **Is this relevant?** Does it address something the framework does or should do?
- **Is it adopted already?** Check if the framework already uses this capability
- **What would change?** Which files would need updating (agents, skills, hooks, settings)
- **Is it worth it?** Does the improvement justify the maintenance cost?

### Step 5: Report

Write findings to `audit/latest-audit.md` (create the directory if needed):

```
# Framework Audit — [Date]

## New Capabilities Found
- [Capability] — [What it does] — [Which framework files it affects]

## Recommended Updates
- [Update] — [Why] — [Effort: low/medium/high]

## Deferred
- [Capability] — [Why it's not worth adopting yet]

## No Changes Needed
- [Area] — Framework is current
```

Present key findings to the user. They decide which updates to pursue.

---

## Output

- `audit/latest-audit.md` with findings and recommendations
- Key findings presented to the user

---

## Scheduled Execution

When run by the biweekly scheduled agent:
- Run the full audit process
- Write the report to `audit/latest-audit.md`
- If critical improvements are found (security, breaking changes), flag them prominently
- the user reviews on their next session
