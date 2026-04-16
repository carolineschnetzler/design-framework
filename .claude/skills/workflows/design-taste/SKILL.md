---
name: design-taste
description: "Build or update the project's aesthetic preferences through conversation with the user. Use when they say /taste, 'the output feels off', 'this isn't the right vibe', 'let me show you what I like', shares reference screenshots, or when no taste-profile.md exists before visual work begins."
---

# Design Taste Workflow

Triggered by `/taste` or when the user says the output "feels off" or wants to calibrate aesthetics.

---

## Purpose

Build or update the project's taste profile through a structured conversation with the user. Taste is subjective — this workflow's job is to make it specific and actionable.

---

## Process

### Step 1: Load Existing Taste Context

Before starting the conversation:
- Load `projects/<name>/taste-profile.md` if it exists (we're updating, not starting from scratch)
- Load `taste-profile.md` for cross-project strong opinions and anti-patterns
- Load the project's `design-brief.md` for the emotional and strategic context

### Step 2: Gather Taste Signals

Dispatch the **design-scout** to support the conversation. Two sources of taste signals:

**From existing work:**
- If the project has Figma screens, analyze them for taste signals: spacing rhythms, color usage proportions, typography patterns, card treatments, information density, visual weight distribution
- Identify what's working well (preserve) and what's drifting (calibrate)

**From the user directly:**
- Ask the user for their emotional target: how should the product feel?
- Ask for external references — screenshots of UI they admires. For each one:
  - What specifically they likes (be precise: "the spacing" is not enough — "the 8px gutters between cards" is)
  - What to borrow vs. what to leave
  - How it relates to their emotional target
  - **Save the screenshot:** Copy it from `~/Desktop/inspo/` (or wherever the user shares it from) to `taste-references/` with a descriptive filename (e.g., `firecrawl-dashboard.png`). Add an annotated entry to the Visual References section of `taste-profile.md` using the user's specific callouts — not your own interpretation.
- Ask for anti-references — what should this NOT look or feel like?
- Ask about craft standards — what level of density, whitespace, type contrast, color restraint?

### Step 3: Identify Tensions

The design-scout flags tensions between references:
- "You like the density of X but the whitespace of Y — here's how to reconcile those"
- "Your anti-reference Z shares a trait with reference A — which trait is the problem?"

Present tensions to the user for resolution. Don't paper over contradictions.

### Step 4: Synthesize

Compile everything into a structured taste profile:
- **Emotional target** — 1-2 sentences capturing the feel
- **References** — Each with specific borrowable qualities
- **Anti-references** — Each with specific qualities to avoid
- **Craft standards** — Spacing, density, type, color, interaction tempo
- **Personality** — The character of the visual language

### Step 5: The User Reviews

Present the taste profile. They may:
- Approve it
- Refine specific signals ("denser than this," "not that warm")
- Add more references or anti-references

Iterate until they approve.

---

## Output

Write or update `projects/<name>/taste-profile.md`.

If this is the first taste session for PureMath, also seed `taste-profile.md` with the user's strongest opinions as cross-project memory.

If updating an existing taste profile, note what changed and why in `design-state.md`.

---

## When to Re-run

- At project start (before any visual design work)
- When the user says output feels wrong ("too dense," "too corporate," "not what I meant")
- When adding new reference material
- During `/retro` to capture taste learnings
