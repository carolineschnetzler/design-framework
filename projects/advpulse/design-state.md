# Design State — AdvPulse

> Created: 2026-04-06
> Last updated: 2026-04-06

---

## Current Status

Core screen designs established. 8 screens cover the primary user flow from initial chat through results, workspace, and firm detail. Component library is extensive with full state coverage on most controls.

---

## Screens Designed

| Screen | Status | Figma Node ID | Notes |
|--------|--------|---------------|-------|
| InitialChat | approved | 152:805 | Full-screen chat, greeting + prompt pills |
| AgenticChat - Progress | approved | 195:7546 | Full-screen, agentic progress card |
| AgenticChat - Intake | approved | 363:8495 | Full-screen, intake form card (tall/scrollable) |
| RecoFirms - Progress | approved | 12:796 | Split panel, results table + chat |
| RecoFirms - Intake | approved | 374:5450 | Split panel, intake card + results table |
| Workspace | approved | 108:492 | Split panel, notifications + activity timeline |
| Firm Detail | approved | 12:894 | Split panel, firm card + data viz |
| Current Chat UI Design | reference | 528:6830 | Extended chat flow reference (4788x5146) |

---

## Decisions Log

### 2026-03-20
**Decision:** Two-layout system — full-screen chat (Side Nav) for initial interaction, split-panel (Top Nav + ChatPanel + Content) for data views
**Why:** Chat-only felt limiting for data-heavy results. Dashboard-only lost the NL query advantage. Hybrid serves both modes.
**Alternatives considered:** Single layout with collapsible chat, three-panel layout

### 2026-03-20
**Decision:** Ghost/outline buttons as default style (transparent bg, colored border)
**Why:** Matches the dark theme aesthetic — solid buttons felt too heavy on dark backgrounds. Ghost style keeps the interface light.
**Alternatives considered:** Solid primary buttons, minimal text-only buttons

### 2026-03-20
**Decision:** Brand green (#18dd65) for AI-executed actions, success green (#2eff7d) for completion states
**Why:** Users need to distinguish between "AI did this" and "this is done." Two greens serve different semantic purposes.
**Alternatives considered:** Single green for both, blue for AI actions

### 2026-03-20
**Decision:** AgenticCard as the primary AI progress visualization (not inline status messages)
**Why:** Cards contain the complexity of multi-step AI processes. Inline messages would clutter the chat with progress noise.
**Alternatives considered:** Inline progress indicators, separate progress panel

---

## Open Questions

- [ ] How should the query management / saved queries view work? — *Waiting on: design direction*
- [ ] Light mode token values — existing dark mode tokens have semantic names, light mode values TBD — *Waiting on: design session*
- [ ] Mobile/responsive behavior — current designs are desktop-only (1440px) — *Waiting on: product roadmap*

---

## Design Debt

- [ ] Current Chat UI Design frame (528:6830) is 4788x5146 — massive reference frame, not a production screen. Needs to be broken into individual designed screens. *Ideal: each chat state as its own screen. Reason deferred: reference frame was useful during initial design exploration.*
- [ ] Some component state coverage is incomplete (e.g., Dropdown Pill states) — *Ideal: full state matrix for every component. Reason deferred: prioritized primary flow screens first.*

---

## Taste Calibrations

[To be populated during taste session]

---

## Retrospective

[To be filled by /retro at project end]
