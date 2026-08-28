# Design Brief — [Project Name]

> Created: [date]
> Last updated: [date]

---

## Problem Statement

[One paragraph. What are we solving and why does it matter? Be specific and falsifiable — if you can't tell whether the design solved this, the statement is too vague.]

---

## Users

### Primary Users
- **Who:** [Role, title, or segment]
- **Context:** [When and where they use this — device, environment, time pressure, expertise level]
- **Goal:** [What they're trying to accomplish]
- **Frustrations:** [What gets in their way today]

### Secondary Users (if applicable)
- **Who:**
- **Context:**
- **Goal:**

---

## Design Principles

[3-5 principles. Each must be opinionated enough to create a trade-off — if everyone would agree with it, it's not a principle.]

1. **[Principle name]** — [One sentence description]. *Trade-off: [what you're giving up or deprioritizing].*
2. **[Principle name]** — [One sentence description]. *Trade-off: [what you're giving up or deprioritizing].*
3. **[Principle name]** — [One sentence description]. *Trade-off: [what you're giving up or deprioritizing].*

---

## Direction

### Recommended Approach
[What approach to take and why. Be specific about the interaction model, information architecture, or design strategy.]

### Alternatives Considered
[What other approaches were on the table and why they were set aside.]

### Trade-offs Accepted
[What this direction gives up. What would need to be true for this to be the wrong choice.]

---

## Constraints

- **Technical:** [Platform limitations, existing architecture, performance requirements]
- **Business:** [Timeline, budget, stakeholder requirements, compliance]
- **Design:** [Existing design system, brand guidelines, accessibility requirements]

---

## Design Systems

[Most products have more than one. A product app and its marketing surfaces usually diverge in type and color, and they should. A physical product has a print system and a web system. If this project genuinely has one, say so and delete the table.]

| Surface | System | Source of truth |
|---|---|---|
| [which surfaces] | [system name] | [doc] |
| [which surfaces] | [system name] | [doc] |

**What they share:** [Name every shared value exhaustively. Usually one accent color and nothing else. "They share the palette" is not an answer.]

**Pick the system by surface, then adhere strictly.** Never use one system's faces or palette inside the other's surfaces. The usual sanctioned exception is a real product screenshot inside a marketing layout: the screenshot keeps product styling, the frame around it uses brand styling.

**Within the chosen system, no values outside what its doc defines.** If a token or style doesn't exist for what the design needs, flag it — do not improvise. Cross-project taste informs preferences but does not override either system.

### Project-Specific Design Decisions

[Decisions that override or specialize the cross-project taste profile. Radius, material treatment, button style, theme — anything that would be wrong on a different product belongs here, not in cross-project memory.]

- **[Decision]** — [why, and what it overrides]

---

## Success Criteria

[How will we know this design worked? List specific, observable outcomes.]

- [ ] [Criterion — something you can point to and say "yes, this happened" or "no, it didn't"]
- [ ] [Criterion]
- [ ] [Criterion]
