# Design State — AdvPulse

> Created: 2026-04-06
> Last updated: 2026-08-28

---

## Purpose

This file tracks **design decisions, open questions, and design debt** — the *why* behind the work that Figma can't store.

**Screen inventory is NOT tracked here.** Figma is the source of truth for what screens exist, what their node IDs are, and what state they're in. Skills and agents must pull frame inventory live from the Figma file (via `figma.json`'s `fileKey` and page node IDs), never from a static doc that drifts.

---

## Decisions Log

### 2026-08-28
**Decision:** When a Search query asks for reasoning Search cannot do, **Step 2 shows an inline nudge offering Agent** — primary "Switch to Agent", secondary "Continue with Search". The classification is a **field on the existing query-parse response, not a second model call**, so it costs no extra credits, and it appears only at Step 2, never live while typing.
**Why:** Step 2 is before Confirm search, so switching costs the user nothing. Riding on a request already being made is what makes the suggestion free; classifying per keystroke would be a real cost for a hint.
**Alternatives considered:** Live suggestion while typing (rejected — per-keystroke classification is expensive and interrupts composition); a separate classifier call (rejected — a second charge to tell someone they picked the wrong mode is hostile); blocking the run (rejected — Search results are still valid for the filterable part of the query, so this is advisory).

### 2026-08-28
**Decision:** **The step description belongs to the active step only.** A completed step collapses to its own summary plus Edit, so `Description` is hidden on `State=Complete`.
**Why:** A completed step's instruction was describing actions you can no longer take. The summary already says what happened.
**Alternatives considered:** Keeping the description throughout (rejected — it reads as an instruction, not a record).

### 2026-08-28
**Decision:** The firm table header gains a **select-all checkbox with an indeterminate state**, and **rows default to unchecked**. `Get contacts` is disabled while nothing is selected.
**Why:** The select cell shipped defaulting to checked, so every firm table rendered fully selected the moment results appeared — a destructive default for a paid step. Indeterminate is needed because partial selection is the common case, not the edge case.
**Open contradiction:** The Agent tables inherit the same header and render all-unchecked, which contradicts the earlier decision that export defaults to the newest batch checked. Unresolved.

### 2026-08-28
**Decision:** **`Question Header` replaces the composer on every Agent screen that has a run.** A first run in flight shows query and meta only; the finished run adds Edit and Re-run.
**Why:** A paused run with six checkpoints sat under a composer still showing placeholder text and prompt suggestions — the question that produced the run appeared nowhere on the page. Search was already fine because its collapsed Step 1 card carries the query.
**Alternatives considered:** A title above the composer (rejected — duplicates the header the re-run screens already use, and the two sections should match).

### 2026-08-27
**Decision:** **Search waiting states use the same Run Log as Agent**, with its own checkpoint vocabulary (READ / MATCH / CHECK, never Agent's RESEARCH / CONSOLIDATE / NEXT STEP). The log starts **after Confirm search**, not while filters are being derived.
**Why:** A search takes at least thirty seconds. A skeleton implies an imminent answer and leaves half a minute unaccounted for. The skeleton states built the day before assumed a two-second wait and were replaced.
**Alternatives considered:** Skeleton rows (rejected — wrong duration model); a spinner (rejected for the same reason the Agent view rejects one: the backend knows what it just did).

### 2026-08-26
**Decision:** **A run is a list that grows, not a query that repeats.** "Re-run" continues the same saved question and appends new rows behind a batch divider. "Edit" and run **forks a new saved query** with its own history entry, starting empty.
**Why:** A run returns roughly 20 firms and 50 contacts because the research is too intensive to do at once. It is not a ranked top-N with a page 2 — the next run reaches the same question a different way, and the backend already knows what it gave you. The screen is therefore about the *question*, not the run.
**Supporting decisions:** "New" is relative to the last run and decays to a run marker once another lands · sorting applies only to rows below the newest divider, since earlier batches are settled · export defaults to the newest batch · nothing in the UI explains how results are chosen.
**Alternatives considered:** Pagination (rejected — there is no ranked list to page through); "Run again" (rejected — implies repetition, when the system deliberately avoids repeating); explaining approach selection (rejected — "use our system, it's magic").
**Where this goes:** the 20-a-day ceiling is a cadence, not a limit. The end state is a standing order, so the header is laid out to accept a recurring toggle without rearranging.

### 2026-08-14
**Decision:** **One credit balance per scope, no abstraction.** Every action drains credits; subscription plans are discounted credits per month, not a second bucket. Personal and Organization remain two wallets a person swaps between. **No per-member allocations, caps, requests, or approvals** — members spend the org's credits and `used` is reporting only.
**Why:** Philosophy is empower, not protect. "One employee burned the pool" is deliberately unsolved in v1; cost control is an admin choosing not to enable auto top-up. Authority order was the founder's written spec over the product meeting over the earlier billing brief.
**Supersedes:** the July per-member cap model. Three components existed only because members had allocations and were deleted: Edit member, Edit allocation, Cap reached.
**Deferred to v2, parked not rejected:** per-user allocations, the request-and-approve flow, per-member auto top-off.

### 2026-08-14
**Decision:** **Credits and Billing live only under ORGANIZATION** in the settings nav, not under both headings.
**Why:** The org is the account that holds the money. Listing them under both made people pick a side.

### 2026-08-14
**Decision:** The Search flow is **four numbered step cards** — Describe, Review filters, Pick firms, Get contacts — and **each card carries its own step number** so the sequence cannot drift.
**Why:** The numbering had already drifted: one screen ran STEP 2 → STEP 4 → STEP 5 and step 1 was never labelled. Binding the number to the card makes that failure impossible rather than merely unlikely.
**Alternatives considered:** A shared stepper component (rejected — the number is a property of the step, and separating them is what allowed the drift).

### 2026-08-11
**Decision:** **Columns are boolean properties on the table row, never variants**, and rows are stacked instances. One `Table Cell` component with a `Type` axis replaced seven single-purpose cell components. Every column fills with a minimum width, and every text node truncates.
**Why:** The tables kept breaking. The header row hugged while body rows filled, so columns drifted apart; nothing truncated, so long content pushed columns; one fixed data column made the minimum width exceed the container. Variants for column combinations explode combinatorially and still cannot reorder.
**Alternatives considered:** Column-count variants (rejected — explodes); keeping per-column cell components (rejected — header and body could disagree, and did).

### 2026-08-14
**Decision:** **Every icon has the same five layer names at the same depth** — two stroke-painted, three fill-painted, with unused ones as blank transparent locked vectors.
**Why:** Figma has no color inheritance, so a component that recolors its icon per state overrides the icon's inner shapes, and those overrides survive an instance swap **only** when the incoming icon has matching layer names at matching depth. Before this, every icon was named differently and swapping one silently dropped the state color.
**Consequence:** a new icon must ship with all five names. One paint channel per node. A component that recolors icons binds both channels on every variant.

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

- [ ] **The sidebar balance is internally inconsistent.** One Search screen shows `2,000 credits / 40% of plan`, another shows `25,000 credits / 40% of plan`. Only the first is arithmetically possible against the entry plan; the second implies a tier that is not sold. Separately, the low-balance screen shows 40% while the spec puts the low state at 10% or below. — *Waiting on: a decision on which numbers are canonical*
- [ ] **"X% of plan" has no agreed definition** — share of the monthly allotment, or of the balance against it? They diverge the moment someone tops up mid-cycle. — *Waiting on: founder + billing*
- [ ] **Raw credit counts are always visible**, reversing the earlier "no raw numbers by default" decision. The written spec is explicit, but it re-imports the accounting the redesign removed. Worth arguing before the API settles. — *Waiting on: founder*
- [ ] **Agent mode may be renamed "commissioned research."** The prototype says Agent everywhere. — *Waiting on: founder*
- [ ] **Agent tables now inherit a select-all but render all-unchecked**, contradicting "export defaults to the newest batch checked." — *Waiting on: design decision before engineering builds it*
- [ ] **The contact-explicit bypass** (skipping the get-contacts step when the query already asks for contact info) is designed but unconfirmed. — *Waiting on: backend*
- [ ] How should the query management / saved queries view work? — *Waiting on: design direction*
- [ ] Light mode token values — existing dark mode tokens have semantic names, light mode values TBD — *Waiting on: design session*
- [ ] Mobile/responsive behavior — current designs are desktop-only (1440px) — *Waiting on: product roadmap*

---

## Design Debt

- [ ] **This log went three weeks without an entry** (2026-08-06 to 2026-08-28) while eleven substantive decisions were made. They were reconstructed on 2026-08-28 from session memory, which is point-in-time and lossy. *Ideal: an entry at the time of the decision. Reason deferred: the work was moving faster than the record.*
- [ ] **The prototype leads Figma on the Search and Agent work** and the two are not fully reconciled. `prototype.json` declares `mode: prototype-first` so this is deliberate, not drift, but the debt is real. *Ideal: Figma catches up on the surfaces that have settled.*
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
