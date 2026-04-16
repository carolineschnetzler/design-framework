# Handoff Spec — [Project Name]

> Created: [date]
> Prepared by: design-builder agent
> Figma file: [link]

---

## Overview

[1-2 sentences: what's being handed off and the scope of work for engineering.]

---

## Task: [Title]

**Component:** chatbot-server
**Type:** feature | enhancement | fix
**Priority:** high | medium | low

### Description

[What to build and why. Enough context that the Frontend Engineer understands the intent, not just the pixels.]

### Success Criteria

- [ ] [Specific, testable criterion]
- [ ] [Criterion]
- [ ] [Criterion]

### Design Decisions

[Decisions from design-state.md that affect implementation. Why something is the way it is — not just what it looks like.]

- [Decision and rationale]

### Tokens

[Exact semantic variable names from the Figma file. Engineering maps these to CSS/code tokens.]

| Property | Semantic Token | Dark Value | Light Value |
|----------|---------------|------------|-------------|
| Background | `background/card` | | |
| Text | `text/primary` | | |
| Border | `border/subtle` | | |
| Spacing (padding) | `spacing/card-padding` | | |

### Figma References

| Element | Node ID | Link |
|---------|---------|------|
| [Screen name] | [node ID] | [figma.com/design/...?node-id=...] |
| [Component name] | [node ID] | [figma.com/design/...?node-id=...] |

### Interaction Specs

[Non-obvious interactions, state transitions, or motion specs. If it's just a click → new page, no need to document. If there's a transition, timing, or conditional behavior, document it.]

| Interaction | Trigger | Animation | Duration | Easing |
|------------|---------|-----------|----------|--------|
| [e.g., Panel expand] | [click] | [height 0→auto, opacity 0→1] | [200ms] | [ease-out] |

### Edge Cases

[What happens when things aren't ideal.]

- **Empty state:** [What to show when there's no data]
- **Error state:** [What to show on failure]
- **Overflow:** [What happens when content exceeds expected length]
- **Loading:** [What to show during async operations]

---

[Repeat "## Task:" blocks for additional tasks in this handoff.]
