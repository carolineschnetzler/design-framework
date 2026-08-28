---
name: handoff
description: "Produce an engineering-ready handoff spec in the format the project declares. Use when the user says /handoff, 'get this ready for engineering', 'prepare for the dev', 'write the spec', or when approved designs need to move to implementation."
---

# Handoff Workflow

Triggered by `/handoff` or when the user says to prepare work for engineering (the Frontend Engineer).

---

## Purpose

Produce a handoff spec so complete that the implementing engineer never has to ask a design question. Every ambiguity left in the spec becomes a Slack thread later.

**The format is declared per project.** Read `handoffTarget` from the project's `project.json` — a sprint or issue tracker, a PR description, a plain markdown spec, or an ongoing changelog. Match what the receiving engineer actually reads. A perfect spec in a format nobody opens is not a handoff.

---

## Process

### Step 1: Production Cleanup

Dispatch the **design-builder** agent to audit and clean the Figma file:
- Verify all component instances are connected (no detached copies)
- Verify all values bound to semantic variables
- Verify auto layout integrity across all frames
- Clean up layer naming
- Verify state variants are complete for all interactive elements
- Fix any issues found

### Step 2: Final Review

If `/review` hasn't been run recently, run a lightweight check:
- **accessibility-reviewer** confirms WCAG AA compliance
- **design-critic** confirms brief alignment

Flag any critical findings to the user before proceeding.

### Step 3: Write the Handoff Spec

The **design-builder** writes `projects/<name>/handoff-spec.md`. Where the project's `handoffTarget` names a tracker, shape each task to that tracker's fields. The default structure:

```
## Task: [Title]

**Component:** <the repo or service where the work happens>
**Type:** feature | enhancement | fix
**Priority:** high | medium | low

### Description
[What to build and why — enough context for the engineer to understand intent]

### Success Criteria
- [ ] [Specific, testable criterion]
- [ ] [Another criterion]
- [ ] [...]

### Design Decisions
[Key decisions from design-state.md that affect implementation]

### Tokens
[Exact semantic variable names used — e.g., background/card, text/primary, spacing/card-padding]

### Figma References
- Screen: [name] — node ID: [id], link: [figma URL]
- Component: [name] — node ID: [id]

### Interaction Specs
[Any non-obvious interactions, state transitions, or motion specs from the motion-designer]

### Edge Cases
[Empty states, error states, overflow behavior, responsive breakpoints]
```

### Step 4: The User Reviews

Present the handoff spec. They may:
- Approve it for the Frontend Engineer
- Add context or constraints
- Flag tasks that need splitting or combining
- Deprioritize certain tasks

---

## Output

- A production-ready Figma file (cleaned by design-builder)
- `projects/<name>/handoff-spec.md` in the project's declared handoff format
- Design decisions documented in `design-state.md`

---

## Two things engineers actually need that specs usually omit

**Behaviour a static frame cannot show.** What defaults to what, what is disabled and when, what happens on the second run, what a sort applies to, what decays over time. This is the part that cannot be inferred from looking at the design, and it is the part most often missing.

**Contradictions, named as contradictions.** Where two screens disagree, say so and say which is right — or that it is unresolved. "These disagree, worth settling before you build it" is more useful than a confident spec that is wrong on one of them.

---

## Ongoing changes vs. a handoff

A handoff is a one-time package for a body of work. A running log of individual changes is a different thing and belongs in `/changelog`, which is **opt-in only** — never append to it as part of this workflow.
