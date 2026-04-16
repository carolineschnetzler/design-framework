---
name: handoff
description: "Produce an engineering-ready handoff spec compatible with the Backend Engineer's chatbot-pm sprint system. Use when the user says /handoff, 'get this ready for the Frontend Engineer', 'prepare for engineering', 'write the spec', or when approved designs need to move to implementation."
---

# Handoff Workflow

Triggered by `/handoff` or when the user says to prepare work for engineering (the Frontend Engineer).

---

## Purpose

Produce a handoff spec so complete that the Frontend Engineer can implement without asking design questions. Every ambiguity left in the spec becomes a Slack thread later. The spec format is compatible with the Backend Engineer's chatbot-pm sprint system.

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

The **design-builder** writes `projects/<name>/handoff-spec.md` in a format compatible with the Backend Engineer's chatbot-pm task system. Each spec contains one or more tasks, each structured as:

```
## Task: [Title]

**Component:** chatbot-server (or other target)
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
- `projects/<name>/handoff-spec.md` formatted for chatbot-pm
- Design decisions documented in `design-state.md`

---

## Integration with chatbot-pm

The Backend Engineer's sprint system expects tasks with:
- Component assignment (where the work happens)
- Type classification
- Priority level
- Success criteria as a checklist
- Figma node references for direct linking

The handoff spec matches this format so tasks can be imported directly into a sprint.
