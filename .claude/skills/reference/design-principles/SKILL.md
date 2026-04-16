---
name: design-principles
description: How to apply a project's design principles when making decisions. Load when evaluating design choices, resolving trade-offs, critiquing work, or when an agent needs to justify a decision against the project brief.
---

# Design Principles Reference

This skill is loaded by agents when they need to make or evaluate design decisions. It teaches agents how to USE principles, not what the principles are — those live in each project's `design-brief.md`.

---

## What Principles Are For

Principles resolve ambiguity. When there are two valid design directions, principles tell you which one to pick. A principle that doesn't create a trade-off isn't a principle — it's a platitude.

---

## How to Apply Principles

### Before making a design decision:
1. Read the project's `design-brief.md` and find the stated principles
2. Identify which principles are relevant to this specific decision
3. If two principles conflict, note the tension and check `design-state.md` for precedent — the user may have already resolved this tension on a previous decision

### When evaluating a design:
1. For each major design choice, identify which principle supports it
2. Flag choices that don't map to any principle — they may be arbitrary
3. Flag choices that violate a principle — they need justification or correction

### When principles conflict:
- Name the tension explicitly: "Principle A suggests X, Principle B suggests Y"
- Check if the project has established a priority order (some briefs do)
- If no precedent exists, present both options to the user with the trade-off articulated
- Record the user's resolution in `design-state.md` so future decisions can reference it

---

## Common Traps

- **Retrofitting** — Don't pick a design direction and then find a principle to justify it. Apply principles forward: principle → decision.
- **Over-applying** — Not every pixel needs a principle citation. Principles guide structural and strategic decisions, not whether padding should be 16px or 20px.
- **Ignoring tension** — When principles conflict, the easy move is to ignore one. The right move is to name the conflict and let the user resolve it.
- **Generic principles** — If the project's principles are too generic to create trade-offs ("be simple," "be intuitive"), flag this to the user during `/discover`. Good principles are opinionated.

---

## Where Principles Live

- **Project principles**: `projects/<name>/design-brief.md` (under the Principles section)
- **Cross-project strong opinions**: `taste-profile.md` (these function as meta-principles across all projects)
- **Decision precedents**: `projects/<name>/design-state.md` (past resolutions of principle conflicts)
- **UX laws and heuristics**: `references/ux-laws.md` — Established UX principles (Gestalt laws, cognitive load, flow, memory, decision-making) with actionable rules. Consult when evaluating layouts, information architecture, interaction patterns, or when justifying a design decision.
- **UX patterns — bad vs. good**: `references/ux-patterns-bad-vs-good.md` — Applied examples of common mistakes and their fixes: scan patterns, action placement, type scaling, label elimination, spacing, borders, overlapping. Consult before finalizing any layout.
