# Design State — [Project Name]

> Created: [date]
> Last updated: [date]

This file is the running record of design decisions, open questions, and design debt for the project — the *why* behind the work that Figma can't store. Agents append to it after design work; the user can also update it directly.

**Screen inventory is NOT tracked here.** Figma is the source of truth for what screens exist, what their node IDs are, and what state they're in. Skills and agents pull frame inventory live from the Figma file (via `figma.json`'s `fileKey` and page node IDs), never from a static doc that drifts.

---

## Current Status

[One sentence: where the project is right now.]

---

## Decisions Log

[Append-only. Each entry records a design decision with date, what was decided, and why. This is the project's institutional memory — future agents and the user reference this to understand why things are the way they are.]

### [Date]
**Decision:** [What was decided]
**Why:** [Rationale — which principle, taste signal, or constraint drove this]
**Alternatives considered:** [What else was on the table]

---

## Open Questions

[Design questions that haven't been resolved yet. Each should name who can answer it.]

- [ ] [Question] — *Waiting on: [the user / research / engineering input]*

---

## Design Debt

[Things that are known to be imperfect but were accepted for now. Each should describe what the ideal state would be and why it wasn't done yet.]

- [ ] [What's imperfect] — *Ideal: [what it should be]. Reason deferred: [why]*

---

## Taste Calibrations

[Notes from the user on how the output feels vs. how it should feel. These feed into taste profile updates.]

- [Date]: [the user's feedback and how it was addressed]

---

## Retrospective

[Filled in by the /retro workflow at project end.]

---

> **This file is not the engineering changelog.** Decisions and their rationale live here. What an implementing engineer needs to pick up lives in `design-changes.md`, written only via `/changelog` on explicit request. Keeping them separate matters: this file is for understanding *why*, that one is for building *what*.
