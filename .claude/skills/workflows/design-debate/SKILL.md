---
name: design-debate
description: "Explore competing design directions with structured evidence and trade-offs. Use when the user says 'I'm torn between', 'which approach is better', 'should we do X or Y', 'compare these options', or is unsure between two or more valid directions."
---

# Design Debate Workflow

Triggered when the user is torn between directions, or when a design decision has high stakes and deserves structured exploration before committing.

---

## Purpose

Surface the best direction by making competing approaches argue their case. This isn't about generating options for the sake of variety — it's about stress-testing directions that each have genuine merit.

---

## Process

### Step 1: Frame the Debate

Clarify with the user:
- What decision is being made (layout approach, interaction model, information architecture, visual direction, etc.)
- What directions are being considered (they may have 2-3 in mind, or ask you to propose them)
- What criteria matter most for this decision (align with brief principles, taste, technical feasibility, user needs)

### Step 2: Build the Case for Each Direction

For each direction, dispatch agents as needed:

**design-critic** — Evaluates each direction against the brief and principles. Which direction best serves the stated problem and users?

**heuristic-evaluator** — Evaluates usability trade-offs. Which direction is more learnable, efficient, or forgiving?

**design-scout** — If relevant, researches how the industry handles this decision. What's the convention? What evidence exists?

**design-scout** — If relevant, finds reference implementations of each direction to ground the discussion.

Each direction gets:
- **The case for** — Why this direction is the right choice, with evidence
- **The case against** — What you'd give up, what risks it introduces
- **Who it serves best** — Which user segments or scenarios benefit
- **Taste alignment** — How well it matches the taste profile

### Step 3: Compare

Present a structured comparison:
- Side-by-side summary of strengths and weaknesses
- Where the directions agree (these aspects don't need debate)
- Where they diverge (these are the real decision points)
- The recommendation, if the evidence clearly favors one direction
- If the evidence is balanced, say so — don't manufacture a false winner

### Step 4: the user Decides

Present the comparison and let the user choose. They may:
- Pick a direction
- Combine elements from multiple directions
- Reject all and reframe the problem
- Ask for one direction to be prototyped before deciding

Record the decision and rationale in `design-state.md`.

---

## Output

A structured comparison presented to the user. The decision and its rationale recorded in `projects/<name>/design-state.md`.

---

## When NOT to Use This

- For low-stakes decisions (padding, icon choice) — just make a call
- When the user has a clear preference — don't debate what's already decided
- When the brief or principles clearly point to one answer — just cite the principle
