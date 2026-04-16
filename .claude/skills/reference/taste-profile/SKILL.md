---
name: taste-profile
description: How to read and apply the active taste profile when making visual decisions. Load when generating screens, reviewing designs, calibrating aesthetics, or when the user says output "feels off", "isn't right", or "doesn't match what I want."
---

# Taste Profile Reference

This skill teaches agents how to interpret and apply taste profiles. The actual taste data lives in each project's `taste-profile.md` and the cross-project memory at `taste-profile.md`.

---

## What a Taste Profile Contains

A taste profile captures the user's aesthetic intent for a project. It includes:

- **Emotional target** — How the product should feel (e.g., "sophisticated but not cold," "data-dense but approachable")
- **Visual references** — Products and interfaces that capture aspects of the target feel, with specific annotations on what to borrow
- **Anti-references** — What the project should NOT look or feel like
- **Craft standards** — Specific expectations for spacing, typography, color usage, information density
- **Personality** — The voice and character of the visual language

---

## How to Apply Taste

### For layout decisions:
- Check the taste profile's information density preference. Dense = more content per viewport, tighter spacing. Spacious = fewer elements, more breathing room.
- Check spacing rhythm — does the profile specify a rhythm (e.g., consistent 16px gutters) or variable rhythm?
- Check the references for layout patterns that match what you're building

### For color decisions:
- Check color usage proportions — how much of the palette is background vs. accent? Is color used sparingly or generously?
- Check the emotional target — "warm" means different color choices than "clinical"
- Verify against anti-references — make sure your color application doesn't drift toward something the user explicitly rejected

### For typography decisions:
- Check the type hierarchy expectations — how many levels? How dramatic is the scale between them?
- Check weight distribution — does the profile lean toward light/airy type or bold/heavy?
- Match the personality — "technical precision" calls for different type treatment than "friendly conversation"

### For interaction and motion:
- Check the tempo — "snappy and responsive" vs. "smooth and deliberate" changes timing curves and durations
- Check the density implication — dense interfaces usually need faster, subtler motion so animations don't slow users down

---

## Hierarchy of Taste Sources

When multiple taste signals exist, apply in this priority order:

1. **Explicit direction from the user in this session** — Always overrides everything
2. **Project taste profile** (`projects/<name>/taste-profile.md`) — The primary source
3. **Cross-project strong opinions** (`taste-profile.md`, strong opinions section) — Carry forward unless the project explicitly overrides them
4. **Cross-project soft patterns** (`taste-profile.md`, soft patterns section) — Use as suggestions, not constraints
5. **Cross-project anti-patterns** (`taste-profile.md`, anti-patterns section) — Always respect as exclusions unless the user overrides

---

## When Taste and Design System Conflict

Sometimes the taste profile implies something the design system tokens don't support (e.g., the taste calls for tighter spacing than the token scale allows). When this happens:

1. Don't silently compromise — name the conflict
2. Don't break the design system — tokens exist for consistency
3. Present the tension to the user: "The taste profile suggests X, but the closest token is Y. Should I use Y, or should we add a new token?"
4. Record the resolution in `design-state.md`

---

## Evolving Taste

Taste profiles are not static. They evolve as:
- the user sees output and calibrates ("this is too dense," "the spacing feels better now")
- New references are added or removed
- The `/retro` workflow captures taste learnings at project end

When the user gives taste feedback during a session, apply it immediately to the current work AND note it for the taste profile update. The `/taste` workflow handles formal updates.
