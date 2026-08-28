---
name: figma-canvas
description: The canvas quality standards every design file in this framework is held to — semantic tokens, auto layout, component reuse, slots, naming, state coverage, and variant architecture. Load before any canvas work. These are policy; the mechanics of executing them live in Figma's own skills.
---

# Figma Canvas Standards

**This file is policy, not API documentation.**

Figma ships and maintains its own skills for *how* to drive the canvas — `figma-use` for writes, `figma-generate-library` for building systems, `figma-generate-design` for composing views, `figma-design-to-code` for reading designs out. Load those for mechanics. They are versioned with the API and updated continuously; anything this framework restates about them will be wrong within weeks.

What follows is the standard the *work* is held to, regardless of how the API changes to meet it. Where a vendor skill and this file appear to conflict: **the vendor skill wins on mechanics, this file wins on policy.**

---

## 1. Semantic tokens — no raw values

Every fill, stroke, effect color, text style, spacing value, and radius binds to a **semantic** variable from the project's system. Semantic means the name describes purpose, not value: `background/card`, not `neutral/800`. `spacing/section-gap`, not `spacing/32`.

A raw hex tells engineering nothing about intent. A semantic token survives theme changes, mode switches, and rebrands.

- Every text node uses a **text style**. Not a manual font/size/weight combination that happens to match one.
- If a token doesn't exist for what the design needs, **stop and flag it**. Do not improvise a raw value, and do not alias a primitive to paper over the gap.
- Semantics alias primitives. Screens bind semantics only.
- New variables get values for **every mode**, in the correct collection, following the project's naming convention.
- **Never change scopes on an existing variable.** Set them at creation; changing them later can break picker visibility across the whole file.

---

## 2. Auto layout is the default

Every frame representing a component or layout region uses auto layout, with direction, padding, and gap set explicitly from the spacing scale. Hug what should size to content, fill what should stretch, fix only what has a known intentional size.

**Minimize nesting.** Do not wrap a frame in a frame unless auto layout genuinely requires a different direction, spacing, or alignment. One level is almost always enough. Never wrap a single text node in a frame just to position it — put it in the auto-layout parent directly.

### Children that legitimately sit outside the flow

The parent still uses auto layout; these children are absolutely positioned:

- Badges, counts, and status dots that overlap a parent's boundary
- Close and dismiss buttons pinned to a corner regardless of content length
- Floating controls anchored to a container edge
- Tooltips, popovers, and dropdowns, which must not participate in flow
- Decorative and background elements that sit behind content
- Labels and ribbons that hang off an edge
- Loading overlays centered over content without displacing it

### Frames that legitimately have no auto layout

Rare. Justify each one.

- Top-level page frames with pinned sections, where the sections themselves still use auto layout
- Deliberately overlapping compositions where no linear flow exists
- Scaffolding that never ships — annotation layers, redline frames, documentation

---

## 3. Reuse before you create

- **Search the library first.** The most common failure is building a duplicate of something that already exists under a name you didn't guess. Search several terms before concluding it's missing.
- **Pull the canonical component, not a screen instance.** An instance shows one variant; the canonical shows every variant and property.
- **Never detach.** If a component can't do what's needed: look for a property you missed, then flag the gap. Creating a local one-off is a last resort with the user's approval.
- **Overrides are for content**, not for colors and spacing. If you're overriding many properties, the component isn't the right fit.
- **Don't delete nodes you don't understand.** A clipped or hidden layer that looks like a duplicate is often a scroll, hover, or interaction state.

---

## 4. Slots vs. instance swap

|  | Instance swap | Slot |
|---|---|---|
| Accepts | One instance from a defined set | Any content — components, frames, text, images |
| Cardinality | Exactly 1:1 | 0 to many, reorderable |
| Best for | Icons, avatars, badges | Card bodies, toolbars, content areas |

A slot is just a named auto-layout frame inside the component: descriptive name, fill-container, a min size so it can't collapse, and default content so the component is usable and communicates what belongs there.

Don't reach for a slot when the answer is simpler: a fixed set of options is an instance swap, present-or-absent is a boolean, and a changing string is a text property.

---

## 5. Variant architecture

Getting this wrong is what makes a library explode and then break.

- **Options and columns are booleans or properties, never variants.** Variants for column counts or row counts multiply combinatorially and still can't reorder.
- **Repeats are stacked instances**, not variants.
- **Componentize what repeats *and* is invariant.** Anything whose geometry is data — a bar whose length encodes a value — cannot be an instance child; every instance will render the component's dimensions and quietly lie. The bar length is data, not design.
- **Expose meaningful nested instances** so a consumer can drive them from the properties panel without diving into the layer tree.
- Consistent property names across components: `State`, `Size`, `Type`, `Icon`. The default variant is the most common usage.

---

## 6. State coverage

Every interactive element carries these as **variants**, not as separate layers:

| State | Visual change |
|---|---|
| Default | Base |
| Hover | Subtle emphasis |
| Focus | Visible ring, never color alone |
| Active | Pressed treatment, visibly distinct from hover |
| Disabled | Reduced opacity, out of the interactive flow |

Plus, where the component needs them: error, loading, selected, empty.

**When adding a state to something that already has siblings, copy an existing example's stroke, color, and token exactly.** Do not substitute what seems reasonable — the point is matching the system, not matching your judgment of it.

---

## 7. Naming

Names describe what an element **is**, not what it looks like. No auto-generated names survive. No `BlueBox`, no `BigText`.

**Adopt the project's existing convention and record it in `design-system.md`.** Conventions are per-file, and consistency inside a file beats correctness across files. Where a project has none, this is a reasonable default:

| Layer type | Convention |
|---|---|
| Frames and groups | `Title-Kebab-Case` |
| Components | `PascalCase`, slashes for hierarchy |
| Primitives | `lowercase-kebab-case` |
| Text layers | The literal text content |
| Slots | `PascalCase` |

---

## 8. Verification

- **Screenshot after every structural change.** Never stack a change on an unverified previous step.
- **Check that content fits.** No overflow, no clipping, no text pushing a column. Long content truncates rather than breaking the layout.
- Resize the frame after building to confirm auto layout actually responds.
- **Place new frames in clear empty space**, never overlapping existing work.
- Verify on assembled screens with real instances. Component-definition previews render modes unreliably.

---

## 9. Motion

Timing defaults, where the project has no opinion: micro-interactions 100–150ms, state transitions 200–300ms, page transitions 300–400ms. Ease-out for entrances, ease-in for exits.

Prototype the flows that need stakeholder buy-in or engineering clarification. Not every interaction needs a connection.

---

## Pre-edit checklist

1. ☐ I know which of the project's design systems applies to this surface
2. ☐ I've loaded the project's variables and text styles
3. ☐ I've searched for existing components
4. ☐ I've loaded Figma's own current skills for the mechanics

## Post-edit checklist

1. ☐ No raw values — everything bound to semantic variables and text styles
2. ☐ Auto layout throughout, exceptions only from the documented lists
3. ☐ Existing components used; nothing recreated or detached
4. ☐ Interactive elements have full state coverage
5. ☐ Layers named per the project's convention
6. ☐ Screenshot taken; nothing clipped, overflowing, or overlapping
