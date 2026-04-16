---
name: design-review
description: "Run a multi-perspective design critique against the brief, taste, and accessibility standards. Use when the user says /review, 'does this work', 'what's wrong with this', 'check this design', 'give me feedback', or as a final check before handoff."
---

# Design Review Workflow

Triggered by `/review` or when the user asks for feedback on a design.

---

## Purpose

Run a structured critique from three perspectives: design quality, usability, and accessibility. Each perspective is handled by a specialized agent. The review produces actionable findings, not vague opinions.

---

## Process

### Step 1: Gather Context

Before dispatching reviewers, load:
- The project's `design-brief.md` (principles, direction, success criteria)
- The project's `taste-profile.md` (aesthetic standards)
- The project's `design-state.md` (past decisions and their rationale)
- The screen(s) to review (the user specifies which, or default to the most recent work)

### Step 2: Dispatch Reviewers (in parallel)

Run all three agents simultaneously — they don't depend on each other:

**design-critic** — Evaluates against the brief and taste:
- Does the design solve the stated problem?
- Does it match the taste profile's emotional target and craft standards?
- Are the principles reflected in the design decisions?
- Is the design internally consistent?
- What's missing (states, edge cases, flows)?

**heuristic-evaluator** — Evaluates usability:
- Nielsen's heuristics applied to the specific design
- Task flow analysis for key user journeys
- Cognitive load assessment
- Learnability and efficiency for the target users

**accessibility-reviewer** — Evaluates compliance and inclusivity:
- WCAG 2.1 AA compliance
- Color contrast ratios against actual tokens
- Keyboard navigation and focus order
- Screen reader readiness
- Information not conveyed by color alone

### Step 3: Synthesize Findings

Collect all three reviews and organize by priority:

1. **Critical** — Must fix. Accessibility failures, structural problems, major usability issues.
2. **Major** — Should fix. Taste mismatches, significant usability friction, missing states.
3. **Minor** — Could fix. Polish, edge cases, optimization opportunities.

De-duplicate where multiple reviewers flagged the same issue. Note when reviewers disagree — that's useful signal.

### Step 4: Present to the user

Present the synthesized review with:
- Overall assessment (one sentence)
- Critical findings first
- For each finding: what, where, why it matters, suggested direction
- Strengths worth preserving
- Any disagreements between reviewers

---

## Output

A review summary presented to the user. Not written to a file unless the user asks — reviews are conversation, not documentation.

If the user approves fixes, those get executed by the appropriate agent (design-lead for visual changes, content-writer for copy, etc.) and recorded in `design-state.md`.

---

## When to Run

- After generating screens, before handoff
- When the user wants a second opinion on their design direction
- When something feels off but they can't pinpoint why
- As a final check before `/handoff`
