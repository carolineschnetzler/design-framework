# Design Brief — AdvPulse

> Created: 2026-03-20
> Last updated: 2026-04-06

---

## Problem Statement

Distribution teams at asset managers, fintech vendors, and custodians spend hours manually searching fragmented databases to find and qualify financial advisors. The existing tools (ISS MarketPro, Discovery Data) are expensive ($5K-20K/yr), have legacy UIs, and require users to know exactly what filters to apply. AdvPulse needs to make this workflow feel as intuitive as asking a question — and deliver results that are immediately actionable.

---

## Users

### Primary Users
- **Who:** Heads of Distribution, VPs of Sales, Directors of Strategic Partnerships at asset managers, fintech vendors, and custodians
- **Context:** Desktop, during business hours, often multitasking between prospecting and outreach. Experienced with financial data but not technical users. Used to clunky legacy tools — low UX expectations but high data expectations.
- **Goal:** Find qualified RIA firms matching specific criteria (geography, AUM, strategy, client type), research them, and generate personalized outreach.
- **Frustrations:** Manual filter-based search is slow. Can't search in natural language. Results require switching between multiple tools to act on.

---

## Design Principles

1. **Chat is a starting point, not the whole experience** — Provide buttons, filters, tables, and UI affordances alongside chat. Don't force everything through conversation. *Trade-off: more UI complexity to build and maintain.*
2. **Show the work** — Make AI processes transparent through activity logs, progress cards, and status indicators. Users in financial services need to trust the data. *Trade-off: more screen real estate for process visibility.*
3. **Progressive disclosure** — Start simple, reveal complexity as needed. Don't overwhelm with every filter and option upfront. *Trade-off: power users may need extra clicks to reach advanced features.*
4. **UX is the moat** — Every interaction should feel obviously better than ISS MarketPro. Speed, clarity, and polish are competitive advantages, not nice-to-haves. *Trade-off: higher design and engineering investment per feature.*

---

## Direction

### Recommended Approach
A hybrid AI-chat + structured-UI approach with two layout modes:
- **Full-screen chat** for initial queries and conversational interaction (Side Nav)
- **Split-panel** for results exploration, workspace management, and firm detail (Top Nav + Chat Panel + Content)

The AI can trigger UI state changes (showing tables, expanding filters, navigating views) as tool calls, creating a fluid transition between conversation and structured data interaction.

### Alternatives Considered
- Pure chat interface — rejected because financial data needs structured presentation (tables, charts, filters)
- Traditional dashboard-first — rejected because natural language query is the core differentiator

### Trade-offs Accepted
- Two distinct layout modes adds navigation complexity
- Chat panel in split view is constrained (423px) — limits conversational richness when viewing data

---

## Constraints

- **Technical:** GPT-4 orchestration with ~6 custom database tools. Dynamic UI via tool calls. SEC/FINRA data (~21,669 firms, ~330,000 advisors).
- **Business:** $200-500/mo price point (10x cheaper than incumbents). Must feel premium despite lower price.
- **Design:** Dark mode primary. Light mode planned. Sora + DM Sans type system. Ghost/outline button style.

---

## Design System Constraint

**All design output must strictly adhere to the AdvPulse design system and design tokens.** No values, colors, spacing, typography, or radius outside what is defined in `projects/advpulse/design-system.md`. If a token doesn't exist for what the design needs, flag it to the user — do not improvise. The general cross-project taste at `taste-profile.md` informs the user's preferences but does NOT override the AdvPulse design system.

### Project-Specific Design Decisions
- **No glass/frosted/neumorphic treatments** — AdvPulse is traditional and data-forward. Solid dark surfaces only.
- **Two-layout system** — Full-screen chat (Side Nav, spacious) and split-panel (Top Nav + ChatPanel + Content, dense). Mode switching is intentional.
- **Ghost/outline buttons as default** — Transparent bg, colored border.
- **Brand green (#18dd65) as single accent** — Active states, AI-executed actions. ~10% of surface area.
- **Success green (#2eff7d) for completion** — Distinct from brand green. Two greens, two semantic roles.
- **Blue (#1861ff) for in-progress only** — Reserved for badge states.
- **AgenticCard as primary AI progress visualization** — Cards contain multi-step AI complexity. Not inline status messages.
- **Monospace logs (Fragment Mono) for AI transparency** — "Watching the machine work" feel.

---

## Success Criteria

- [ ] New user can execute a natural language query and get structured results within 60 seconds
- [ ] AI progress is visible and understandable during query execution
- [ ] Users can seamlessly transition between chat and structured data views
- [ ] Interface feels faster and more modern than ISS MarketPro at first glance
- [ ] Outreach workflow (find → research → contact) can be completed without leaving AdvPulse
