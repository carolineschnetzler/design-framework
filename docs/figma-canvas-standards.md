# 15 Figma Canvas Standards

A distilled set of standards for building production-ready Figma files. Opinionated, enforceable, and battle-tested — these are the rules you'd want a junior designer to internalize on day one so your handoffs don't bleed Slack threads.

Written for working designers and design engineers. If you're building an agent that edits Figma, the machine-readable version lives at `.claude/skills/tools/figma-canvas/SKILL.md`.

---

## Tokens & variables

### 1. Bind every visual property to a semantic token

Every color, spacing, type, and radius value must be bound to a **semantic** variable — never a raw hex, never a primitive-only binding.

- Semantic: `background/card`, `text/primary`, `spacing/section-gap`, `radius/card`
- Primitive (avoid as a final binding): `neutral/800`, `spacing/32`, `radius/16`
- Raw value (never): `#1c1c1c`, `32px`, `16px`

**Why:** A raw hex tells engineering nothing about intent. A primitive token doesn't survive a theme swap. A semantic token names the role — so dark/light mode, rebrands, and new modes just work. Engineering reads the variable bindings, not the pixel values.

**How to apply:** If a semantic token is missing for what you need, stop and flag it. Don't alias a primitive on the fly, and never type a hex value directly into the paint panel. Create the semantic variable properly (with values for every mode) or escalate.

### 2. "Coincidentally the right color" is not a binding

A layer fill can *look* correct because you picked the matching hex visually — but if the Figma variable panel doesn't show a binding, engineering has no link back to the design system.

**How to verify:** Select any filled node, open the fill panel, and confirm the variable name is shown. If you see only a color swatch and a hex, it's unbound.

### 3. Never modify variable scopes on existing variables

When creating a new variable, set its scope explicitly (e.g., "available for fills only"). But never change scopes on variables that already exist — the change cascades through the entire design system picker and can hide variables from places they used to work.

**How to apply:** Set scope at creation time and leave it alone. If a variable should be visible in a new context, create a new variable or alias rather than widening an existing scope.

---

## Auto layout

### 4. Auto layout is the default — deviate only for documented exceptions

Every frame that represents a UI component or layout region uses auto layout. Centering, equal spacing, sidebar + content, stacked cards, grids — all of it is nested auto layout.

**Known valid exceptions (absolute-positioned children inside an auto-layout parent):**

| Exception | Why |
|---|---|
| Badges, status dots, notification counts | Overlap the parent boundary |
| Close/dismiss buttons | Pinned to corner regardless of content length |
| Floating controls (FABs, scroll-to-top) | Anchored to a container edge |
| Tooltips, popovers, dropdowns | Must overlay adjacent siblings |
| Decorative backgrounds, watermarks | Behind content without affecting spacing |
| Overlapping labels ("NEW" ribbons) | Hang off a card edge |
| Loading overlays, spinners | Centered over content without displacing it |

**Known valid exceptions (frames without any auto layout):**

- Top-level viewport frames with pinned sticky sections
- Complex overlapping hero/marketing compositions with intentional z-space layering
- Annotation/redline scaffolding that never ships

If you find yourself reaching for absolute positioning outside this list, you're probably missing a nested auto-layout opportunity.

### 5. Every auto-layout child has an explicit sizing mode

Every child of an auto-layout frame must be set to **hug contents**, **fill container**, or **fixed**. Never leave sizing ambiguous.

- **Hug:** element sizes to its content (buttons, labels, icon wrappers)
- **Fill:** element stretches to parent (main content areas, flexible inputs)
- **Fixed:** element has a known, intentional size (icons, avatars, divider thickness)

**Why:** An unset sizing mode is the #1 source of "this screen looks fine at 1440 but breaks at 1200" bugs. Auto layout can't respond correctly without knowing the intent of each child.

### 6. Nest auto layout — don't fight a single frame's alignment

If a single auto-layout frame can't express what you need, add a nested auto-layout frame. Use:
- Sidebar + main → horizontal auto layout with `fixed + fill`
- Grid → nested horizontal auto layouts inside a vertical auto layout
- "Space between with a trailing icon" → two nested frames, each with its own alignment

A design that needs three levels of carefully-nested auto layout is almost always cleaner than a design that uses absolute positioning to hack around a single frame.

### 7. Minimize frame nesting — flat beats deep

The opposite pitfall: don't wrap frames in frames unless auto layout requires a different direction, spacing, or alignment. One level of nesting is almost always enough.

Signs you've over-nested:
- A frame that contains exactly one child
- Three wrapper frames all with the same direction and no different padding
- You can't remember which wrapper owns which property

**How to apply:** Before committing a layout, try flattening. If the design still works with one less wrapper, delete the wrapper.

---

## Components & slots

### 8. Always use instances — never recreate a component

Search the library first (`search_design_system` in the MCP, the Assets panel in the UI). If something exists, use the instance. Recreating a component creates drift: the next library update won't reach your copy, and reviewers can't tell which one is canonical.

### 9. Never detach as a shortcut — fix at the source

If an instance doesn't support what you need:
1. Check every variant and property you might've missed
2. If genuinely unsupported, update the source component — don't detach the instance
3. Detach only as a last resort, with explicit approval, and only to create a new local component

**Why:** Detached instances are invisible design debt. They look fine until the design system changes and they silently diverge. Three months later, nobody knows why this one card behaves differently.

### 10. Slots for open-ended content, instance swap for constrained choices

When a component needs to accept variable content, choose the right mechanism:

| | Instance Swap | Slot (auto-layout frame inside the component) |
|---|---|---|
| Accepts | One instance from a defined set | Any content — components, frames, text, images |
| Cardinality | Exactly 1:1 | 0 to many children, reorderable |
| Best for | Icons, avatars, badges | Card bodies, toolbar actions, content areas |
| Discovery | Dropdown in properties panel | Drag into the layers panel |

**Slot checklist:**
- Named descriptively (`Card-Body`, `Action-Bar`, not `Frame 47`)
- Has auto layout applied
- Set to `fill-container`
- Has min-width / min-height to prevent collapse
- Contains default content so the component is usable out of the box
- "Clip content" enabled where overflow should hide (cards, modals)

**When to use neither:**
- Fixed set of N visual options → variant property
- Something is present or absent → boolean property
- Only a string changes → text property

---

## Naming

### 11. Every layer has a semantic name — no auto-generated names

"Frame 47" and "Group 3" are banned. Every layer must be named by what it **is**, not what it looks like.

**Conventions by layer type:**

| Layer Type | Convention | Examples |
|---|---|---|
| Custom frames and groups | Title-Kebab-Case | `Main-Content`, `Chat-Input-Area`, `Filter-Bar` |
| Components and instances | PascalCase + slashes for hierarchy | `AgenticCard/Progress`, `Top Nav`, `Message Bubble` |
| Primitives (shapes, vectors) | lowercase-kebab-case | `table-background`, `tab-divider` |
| Text layers | Literal text content | `Good Afternoon, Dylan.`, `NOTIFICATIONS` |
| Slots / viewports | PascalCase | `MessageViewport`, `ContentArea` |
| Screen / page frames | PascalCase or Title-Kebab | `InitialChat`, `Reco-Firms-Progress` |

**Forbidden:** "BlueBox", "BigText", "LargeSection" — names that describe appearance, not role. They break the moment you change the color or size.

---

## State

### 12. Every interactive element has five states as variants

Default, Hover, Focus, Active, Disabled — minimum. Each one is a **variant**, not a duplicated layer or a hidden frame.

| State | When | Visual Change |
|---|---|---|
| Default | No interaction | Base appearance |
| Hover | Cursor over element | Subtle emphasis (lighter bg, shadow, underline) |
| Focus | Keyboard focused | Visible focus ring (2px+ outline, offset, high contrast) |
| Active / Pressed | Being clicked | Compressed or depressed |
| Disabled | Not available | Reduced opacity (0.4–0.5), no cursor change |

Add Error, Loading, Selected, Empty as needed. Use a `State` variant property — don't scatter states across separate component sets.

### 13. Focus states must be visible without color alone

A focus ring that differs from default by color only will fail WCAG and real keyboard users. Use an outline, ring, offset, or glow that's perceivable without color distinction.

**How to verify:** View the focus state in grayscale (Figma → Plugins → Color Contrast or a grayscale preview). If you can't tell it from Default, it's not accessible.

### 14. Variant property for visual differences; boolean for presence; text for strings

Choose the right property type for each thing that changes:

- **Variant property** → visual differences that change structure (state, size, type)
- **Boolean property** → toggling optional elements (hasIcon, showBadge, isCompact)
- **Instance swap property** → swapping child instances from a constrained set
- **Text property** → editable string content (label, description, placeholder)

Mixing these up (e.g., using a variant for what should be a boolean) produces combinatorial explosions of variants that nobody can maintain.

---

## Verification

### 15. Screenshot after every structural change

After any structural edit — new section, resized frame, added component — take a screenshot and check for:

- Text overflow or clipping
- Misalignment across siblings
- Content that breaks container boundaries
- Unexpected auto-layout reflow
- Spacing that visibly differs from the design system scale

**Why:** Figma's API and plugin-based edits can produce results that look fine in one node view but are broken at the frame level. The only way to catch this is to look at the actual rendered output between steps.

Pair this with resizing the top-level frame before committing — if the design doesn't hold at ±200px of width variation, the auto-layout setup is wrong.

---

## Pre-edit checklist

Before making any canvas edit:

- [ ] I know which project's design system applies
- [ ] I've loaded the variable definitions (`get_variable_defs` or check the Variables panel)
- [ ] I've searched existing components (`search_design_system` or the Assets panel)
- [ ] I know the token names for the colors, spacing, and type I'll use

## Post-edit checklist

After every canvas edit:

- [ ] No raw hex — all colors bound to **semantic** variables
- [ ] All layout frames use auto layout, exceptions only for the documented cases
- [ ] All layers named semantically — no auto-generated names
- [ ] Component instances used where available; slots used for open-ended content
- [ ] Interactive elements have state variants (default/hover/focus/active/disabled)
- [ ] Spacing values bound to semantic tokens where available
- [ ] Screenshot taken to verify visual result matches intent

---

## How to use this document

- **In a team:** Link to it from your design system README. Use the pre- and post-edit checklists in PR reviews of `.fig` file changes or as acceptance criteria for Figma work.
- **With an AI design agent:** The machine-readable version at `.claude/skills/tools/figma-canvas/SKILL.md` contains the same standards formatted for an agent's system prompt, plus a `PostToolUse` hook in `.claude/settings.json` that re-checks every canvas edit automatically.
- **Solo:** Treat it as the pre-flight checklist before shipping a file to engineering. Most handoff bugs come from violating standards 1, 5, 9, and 12.
