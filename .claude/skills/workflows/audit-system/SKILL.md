---
name: audit-system
description: "Audit a project's design system for drift, duplication, missing states, and unbound values. Use when the user says /audit-system, 'audit the design system', 'why does this component keep breaking', 'is anything duplicated', or before a handoff."
---

# Design System Audit

Triggered by `/audit-system`, before `/handoff`, or when something in the system keeps breaking.

Dispatch the **design-systems-engineer**.

---

## What to walk

Walk every frame in scope, **skipping the inside of instances** — an instance's contents are the component's problem, not the screen's. Count raw nodes, then classify them.

---

## What to look for

**Duplication.** The same shape built more than once under different names. This is the most valuable finding and the hardest to see, because the duplicate is usually named something you would not have searched for. Check for hand-built copies of real components — a rail, a nav, a toggle rebuilt inline because someone did not find the original. These have missed every change made to the real component since.

**Unbound values.** Raw hex, manual type, arbitrary spacing. Report the count and the fix. Where many nodes share one unbound value, the fix is usually a new token rather than a new component — a rectangle with one property has no internal structure worth standardizing.

**Missing states.** Interactive elements without the full set. Note deliberate exceptions: static cards, tiles, and headers have no interactive states by design, and saying so is a finding too.

**Variant architecture problems.** Variants used where booleans belong. Header and body components that can disagree with each other. Sets that have grown past what anyone can reason about.

**Things that should stay raw.** Page scaffolding, prototype hotspots, one-or-two-use bits. Name them explicitly as deliberate, so the next audit does not re-raise them. **Not everything should be a component.** Content-specific elements with per-instance geometry work better as structured frames.

**Parity.** Does the design file, `design-system.md`, and the code token layer tell the same story? Name every place they diverge and which one is right.

---

## Rules while auditing

- **Fix at the source.** An instance-level fix does not scale and creates drift.
- **Mutating a component regenerates its instances.** Capture names and IDs before mutating; re-query after.
- **Check the instance count before consolidating.** A component with thirty live instances is a different risk than one with three.
- **Do not delete a node you do not understand.** Clipped or hidden layers that look like duplicates are often scroll, hover, or interaction states.

---

## Output

A report, and the fixes the user approves:

```
DESIGN SYSTEM AUDIT — <project>, <date>

Walked: <N> frames, <M> raw nodes, <K> distinct shapes.

Duplication
- <what> — <where> — <recommended action>

Unbound values
- <count> <what> — <fix>

Missing states
- <component> — missing <states>

Architecture
- <finding> — <why it breaks> — <fix>

Left raw on purpose
- <list, so the next audit doesn't re-raise them>

Parity
- <divergence> — <which source is right>
```

Present it, let the user pick what to fix, then execute without pausing per item.
