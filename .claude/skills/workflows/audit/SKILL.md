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
- **Agent and skill frontmatter** — new or renamed fields. A field this framework uses that Claude Code no longer recognises fails **silently**, so check the current field reference rather than assuming.
- **Memory and persistence** — Changes to how context persists across sessions

### Step 2: Check vendor capabilities

The framework deliberately does not restate vendor APIs, so this step checks whether the framework is still *pointing at the right things* — not whether it has copied them correctly.

- **Installed plugin versions.** Read `~/.claude/plugins/installed_plugins.json` for the current version and `lastUpdated` of each design-related plugin. Compare against what the framework's skills reference by name.
- **Skills that shipped since.** List the skills each installed plugin now provides. If a vendor now ships a skill covering something this framework documents itself, **that framework file should shrink or be deleted**, not kept in sync.
- **Tool names referenced anywhere in this repo.** Grep for `mcp__` across the framework. Every hit is a maintenance liability. Confirm each still exists, and question whether it needs naming at all.
- **Guidance changes.** Check the vendor's current documentation for changes to the recommended integration path — remote vs local servers, skills installation, rules files.

The finding to look hardest for: **something this framework explains that the vendor now explains better.** That is a deletion, and deletions are the highest-value output of this audit.

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
