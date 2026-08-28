# Design State — AdvPulse

> Created: 2026-04-06
> Last updated: 2026-05-13

---

## Purpose

This file tracks **design decisions, open questions, and design debt** — the *why* behind the work that Figma can't store.

**Screen inventory is NOT tracked here.** Figma is the source of truth for what screens exist, what their node IDs are, and what state they're in. Skills and agents must pull frame inventory live from the Figma file (via `figma.json`'s `fileKey` and page node IDs), never from a static doc that drifts.

---

## Decisions Log

### 2026-08-06
**Decision:** The product has **two query modes side by side under one toggle**: **Search** (the renamed Prospect Search, six steps, unchanged behaviour) and **Agent** (advanced reasoning, no steps). "Prospect Search" and "List Builder" are retired names everywhere in copy and code.
**Why:** The two modes answer the same question at different cost and depth. Putting them under one toggle on one query surface keeps that a choice about the request, not a choice about which product area to be in.
**Alternatives considered:** Separate nav items per mode (rejected — reintroduces the Explorer/List-Builder split the redesign removed); Agent as an escalation inside the Search flow (rejected — Agent is not step-based, so it cannot live inside a step).
**Supporting decisions:**
- The toggle signals **cost as relative weight (a three-dot meter), never as a number**, alongside a one-line capability description.
- Switching mode clears the run below but keeps the query text, so the same request can be sent the other way without retyping.
- Sidebar history holds **both** modes, agent entries marked with a small `Agent` label. History is a list of a person's past work; splitting it by mode would hide half of it.

### 2026-08-06
**Decision:** The Agent working view is a **sequential log of backend checkpoints** (research / consolidate / next step), not a spinner or a progress bar. Results accumulate into the same firm and contact tables Search uses, with an early emit so a long run puts rows on the table before it can be interrupted.
**Why:** The backend writes state at each step, so the run genuinely knows what it just did and genuinely does not know how far along it is. A progress bar would be inventing the second thing; a spinner would be discarding the first.
**Alternatives considered:** Percentage progress bar (rejected — no honest denominator); collapsed "thinking" summary (rejected — the reasoning trace is the product's evidence story).

### 2026-08-06
**Decision:** One **app-level wallet indicator** in the side-nav footer, directly above the account row: a percentage bar of balance remaining, **no raw numbers by default** (they appear on hover). Neutral above 10%, error-colored at or below 10%. At or below 5% **in Agent mode only**, the bar carries "Low balance. Agent runs may not complete."
**Why:** This is a wallet that depletes, not a per-action price list — the redesign removed per-step credit costs on purpose. A percentage answers "can I keep working" without turning every screen into an invoice. Placing it above the account row ties the balance to the context that owns it (personal wallet vs org allocation).
**Alternatives considered:** Raw credit count in the rail (rejected — reads as an invoice and re-imports the accounting the redesign removed); indicator in the page header (rejected — it is app state, not page state).

### 2026-08-06
**Decision:** Running out mid-agent-run **pauses the run in place** and shows a **persistent inline card**, not a toast. Checkpoints and partial results stay on screen. Two equal-weight actions: "Add credits" and "Set up auto top-up". For an org member the primary becomes **"Request credits from admin"**, reusing the cap-reached modal pattern, with a note that auto top-up is an admin setting.
**Why:** The run is not going to resume on its own, so the message cannot be dismissible. Equal weight is deliberate: paying now and never landing here again are both correct answers, and neither should be pushed.
**Alternatives considered:** Toast (rejected — dismissible, and the state persists); killing the run and discarding partial results (rejected — the work was paid for).

### 2026-07-31
**Decision:** Prospect Search history auto-saves every search, and re-running an identical query **replaces** its earlier entry rather than appending a duplicate. The sidebar is a list of distinct searches, most recent first.
**Why:** History is a way back into past work, not an audit log of activity. A literal log fills the sidebar with repeats of the same query and buries the distinct searches that make it useful.
**Alternatives considered:** Literal append-only history (rejected — duplicates crowd out distinct searches); no history at all (rejected — the brief requires auto-save with no explicit save action).
**Scope:** Applies to the Prospect Search redesign, which replaces List Builder. Matching is on normalized query text.

### 2026-06-30
**Decision:** AdvPulse is documented as **two separate design systems** — **Product UI** (the app) and **Brand / Marketing** (logo, website, pitch, social, print, email). Product UI = Sora/DM Sans/Fragment Mono on the dark token system (`design-system.md`). Brand = Playfair Display/Plus Jakarta Sans/IBM Plex Mono with the Pulse/Deep Teal/Ink/Mist/Paper palette (`brand-guidelines.md`, sourced from the Brand & Style Guide). The two share only the green `#18DD65` (Pulse = `color/green/500`).
**Why:** The brand/marketing work and the product app had clearly diverged in type and color but the divergence was undocumented, so it read as drift. Naming them as two intentional systems with a per-surface selection rule stops the app and marketing from bleeding into each other.
**Alternatives considered:** Converge the two onto one type system (rejected — the editorial brand voice and the dense product UI have different jobs; forcing one would weaken both); leave undocumented (rejected — invited accidental mixing).
**Cross-system rule:** The one sanctioned exception to "never mix" is a real product screenshot embedded in a marketing layout (e.g. partner "Platform Preview") — screenshot stays Product UI, surrounding frame is Brand.

### 2026-05-13
**Decision:** Universal focus ring = 1px stroke bound to `border/tertiary`, `strokeAlign: INSIDE` — applied to every keyboard-focusable component that lacks its own component-scoped focus token
**Why:** Matched the existing pattern across button/primary, dropdown-pill, and other components that already used `#fafafa` / gray/50 for their focus borders. Avoids token bloat (no new component-scoped focus tokens added for the 17 components newly getting Focus state). Originally tried `border/active` (brand green) — wrong choice; the system's pattern is white/near-white, not brand. Corrected before shipping.
**Alternatives considered:** Per-component focus tokens (rejected — 30+ new tokens for no value); brand-green ring via `border/active` (rejected — does not match shipped pattern)

### 2026-05-13
**Decision:** Top-level components get `layoutAlign = STRETCH`; variants inside component sets get `layoutSizingHorizontal = FILL`
**Why:** Standalone components on a page canvas cannot have `FILL` set directly (Figma rejects: "FILL can only be set on children of auto-layout frames"). `STRETCH` is the equivalent hint that propagates to instances placed in auto-layout parents. Applied to Top Nav, Settings Sections, Settings Avatar Row, DropdownLists, Pill Side Scroll, Range Display, Session Card, RangeSlider Full, and component-set variants for Settings Nav Item, Settings Input Field, Dropdown Item.
**Alternatives considered:** Leave components FIXED and rely on instance-level overrides — rejected because it requires per-instance work and drifts over time

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

- [ ] Some component state coverage is incomplete (e.g., Dropdown Pill states) — *Ideal: full state matrix for every component. Reason deferred: prioritized primary flow screens first.* Note: significant Focus-state expansion completed 2026-05-13 (24 new variants across 14 components).
- [ ] **File Upload, Prompt Suggestion, List Item** are singleton components without state variants — converting to component sets with Default/Hover/Focus/Disabled was out of scope on 2026-05-13. Address when these elements next get touched.
- [ ] **RangeSlider Focus** — currently no component-level Focus variant. A frame-wide ring is incorrect (only the thumb is keyboard-focusable). Proper fix: thumb-level focus ring on the dual-handle-slider element.
- [ ] **Chat Item variant naming** — uses placeholder `Property 1=Variant2` instead of semantic `State=Hover`. Rename when the component is next edited.
- [ ] **Search component** uses `State=Active` where every other input uses `State=Focus`. Naming inconsistency.

---

## Taste Calibrations

[To be populated during taste session]

---

## Retrospective

[To be filled by /retro at project end]
