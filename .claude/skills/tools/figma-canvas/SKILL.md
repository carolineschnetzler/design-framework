---
name: figma-canvas
description: Mandatory Figma canvas standards for semantic tokens, auto layout, component usage, slots, layer naming, state management, and responsive design. Load before every use_figma call that creates or edits design elements. Also load when auditing Figma file quality or preparing for handoff.
---

# Figma Canvas Standards

This skill defines mandatory practices for all canvas edits. Every agent with Figma write access (design-lead, motion-designer, design-builder) must follow these rules. The PostToolUse hook enforces them automatically.

---

## 1. Semantic Tokens — No Raw Values

Every visual property must be bound to a **semantic** token from the project's design system. Semantic means the token name describes its purpose, not its value. Use `color/background/card`, not `color/neutral/800`. Use `spacing/section-gap`, not `spacing/32`. If only primitive tokens exist, bind to semantics where available and flag gaps to the user.

### Why Semantic
A raw hex or a primitive token (`gray-800`) tells engineering nothing about intent. A semantic token (`background/card`) survives theme changes, dark/light mode, and rebrands. Agents must think in terms of role, not value.

### Creating and Editing Variables

Agents can create and edit Figma variables programmatically via `use_figma` (Figma Plugin API). This includes:
- Creating variable collections and adding modes (e.g., Light, Dark)
- Creating new semantic variables (`figma.variables.createVariable()`)
- Setting per-mode values (`variable.setValueForMode()`)
- Binding variables to node properties
- Aliasing semantic variables to primitive variables

**When building components**: if a semantic token is missing, the agent should create it (with the user's approval) rather than using a raw value. New variables must:
- Live in the correct semantic collection (not the primitives collection)
- Have values set for **all modes** (both Light and Dark)
- Follow the project's naming convention (e.g., `background/card`, `text/primary`, `border/subtle`)
- Alias to primitive variables where the project uses that pattern

**For existing projects** (like AdvPulse): semantic variables already exist. Check with `get_variable_defs` before creating new ones. Only add or edit variables when the existing set doesn't cover what the design needs.

### Color
- Bind every fill, stroke, and effect color to a **semantic** Figma variable (`text/primary`, `border/subtle`, `background/surface` — not `neutral/100` or `#1c1c1c`)
- Never type a hex value directly. Use the variable picker or `set_variable_binding`
- If no semantic token exists for the color you need, stop and flag it to the user — don't invent a token, alias a primitive, or use raw hex
- Background, text, border, and state colors all come from semantic tokens

### Typography
- Use the project's type scale. Every text layer must reference a text style or token
- Font family, size, weight, line-height, and letter-spacing all come from the type scale
- Use semantic style names where available (`heading/page`, `body/default`, `label/sm`) rather than raw size tokens
- Don't create one-off text sizes. If the scale doesn't have what you need, flag it

### Spacing
- Padding and gap values come from the spacing scale (typically 4px base: 4, 8, 12, 16, 20, 24, 32, 40, 48, 64, 80)
- Never use arbitrary spacing values. Round to the nearest scale value.
- Bind spacing to semantic variables where the design system supports them (`spacing/card-padding`, `spacing/section-gap`)

### Border Radius
- Use the project's semantic radius tokens (`radius/card`, `radius/button`, `radius/input`)
- Don't use arbitrary radius values or bind to primitive scale values when a semantic token exists

---

## 2. Auto Layout — Default, With Known Exceptions

Every frame that represents a UI component or layout region must use auto layout. This is the default — deviate only for the specific exceptions listed below.

### Structure
- Set direction (horizontal/vertical), padding (top, right, bottom, left), and gap explicitly
- Use "hug contents" for elements that should size to their content
- Use "fill container" for elements that should stretch to their parent
- Use "fixed" only for elements with a known, intentional size (icons, avatars)

### Nesting
- Auto layout frames can nest inside auto layout frames — this is how responsive layouts work
- Every child of an auto layout frame must have its sizing mode set correctly

### Alignment
- Use auto layout alignment (top-left, center, space-between) instead of manual positioning
- For complex layouts, use nested auto layout frames rather than fighting a single frame's alignment

### What Auto Layout Replaces
- Centering → auto layout with center alignment
- Equal spacing → auto layout with gap
- Sidebar + main → horizontal auto layout with fixed + fill
- Stacked cards → vertical auto layout with gap
- Grid → nested horizontal auto layouts inside a vertical auto layout

### Valid Exceptions — "Ignore Auto Layout" Children

The parent frame still uses auto layout. These children are set to absolute position ("Ignore auto layout") because they must sit outside the normal flow:

- **Badges and indicators** — Notification counts, status dots positioned at the corner of an avatar or icon. They overlap the parent boundary.
- **Close/dismiss buttons** — Pinned to a corner of a card, modal, or dialog regardless of content length.
- **Floating controls** — Scroll-to-top buttons, FABs, or anchored actions pinned to a container edge.
- **Tooltips, popovers, and dropdowns** — Overlay adjacent content and must not participate in flow. Auto layout z-ordering can also cause rendering issues (tooltips behind siblings).
- **Decorative/background elements** — Illustrations, gradient shapes, or watermarks that sit behind content without affecting spacing.
- **Overlapping labels** — "NEW" ribbons, sale tags, or status badges that hang off a card edge.
- **Loading overlays** — Spinners or skeleton states centered over content without displacing it.

### Valid Exceptions — Frames Without Auto Layout

These are rare. Justify each one.

- **Top-level page frames** — The outermost artboard representing a device viewport may use constraints-based positioning rather than auto layout, especially when sections are pinned (fixed sidebar, sticky header). Sections within it should still use auto layout.
- **Complex overlapping compositions** — Hero sections or marketing layouts where multiple elements intentionally overlap in z-space and none follow a linear flow. Don't force auto layout frame nesting just to avoid this exception.
- **Non-shipped frames** — Prototype scaffolding, annotation layers, or redline frames that exist for documentation only.

---

## 3. Component Usage

### Instances
- Always use component instances from the design system library
- Never recreate a component that already exists — search the library first with `search_design_system`
- If you need a variation, check if it exists as a variant before creating something new

### Detachment
- Never detach a component instance. If the component doesn't support what you need:
  1. Check if there's a variant or property you missed
  2. If not, flag the gap to the user — the design system may need updating
  3. Only as a last resort, with the user's approval, create a local component

### Overrides
- Component overrides (text, icon swaps, boolean toggles) are fine — that's what they're for
- Don't override colors or spacing on instances — use the component's variant properties instead
- If you're overriding many properties, the component probably isn't the right fit

### Slots (Content Drop Zones)

Use slots when a component needs to accept **variable, open-ended content** — not a fixed 1:1 swap, but a region where consumers drop whatever they need.

**What a slot is:** A named frame inside a component with auto layout applied. Consumers can drag any content into it — components, frames, text, images. There is no special "slot" toggle in Figma; slots are a structural pattern.

**When to use slots vs. instance swap:**

| | Instance Swap | Slot |
|---|---|---|
| Accepts | One component instance from a defined set | Any content — components, frames, text, images |
| Cardinality | Exactly 1:1 | 0 to many children, reorderable |
| Best for | Icons, avatars, badges — constrained choices | Card bodies, toolbar actions, content areas — open-ended |
| Discovery | Dropdown in properties panel | Drag into the frame in layers panel |

**How to create a slot:**
1. Add a frame inside the component. Name it descriptively: `Content`, `Actions`, `Leading`, `Trailing` — not `Frame 47`
2. Apply auto layout to the slot frame (set direction, gap, padding)
3. Set the slot frame to fill-container so it adapts to the component's size
4. Set min-width/min-height to prevent collapse when empty
5. Place default content inside so the component is usable out of the box and communicates what belongs there
6. Enable "Clip content" when overflow should be hidden (cards, modals)

**Slot naming convention:** Use the same Title-Kebab-Case as other layers. Describe the content role: `Card-Body`, `Action-Bar`, `Leading-Content`.

**When NOT to use slots:**
- If there are exactly N valid options (e.g., 5 icon choices) → use instance swap with `preferredValues`
- If the element is just present or absent → use a boolean property
- If only a string changes → use a text property

---

## 4. Layer Naming

### Convention

Naming follows the patterns established in AdvPulse. Different layer types use different conventions:

| Layer Type | Convention | Examples |
|---|---|---|
| Custom frames and groups | **Title-Kebab-Case** | `Main-Content`, `Chat-Input-Area`, `Filter-Bar` |
| Components and instances | **PascalCase with slashes** for hierarchy, **spaces** for simple names | `AgenticCard/Progress`, `Top Nav`, `Message Bubble` |
| Primitives (shapes, vectors) | **lowercase-kebab-case** | `table-background`, `tab-divider-1` |
| Text layers | **Literal text content** | `Good Afternoon, Dylan.`, `NOTIFICATIONS` |
| Slots/viewports | **PascalCase** | `MessageViewport`, `ContentArea` |
| Screen/page frames | **PascalCase** or **Title-Kebab** | `InitialChat`, `Reco-Firms-Progress`, `Workspace` |

### Rules
- Names must be semantic — describe what the element IS, not what it looks like
- Every layer must be named intentionally. No auto-generated names left in place.

### Forbidden
- Auto-generated names: "Frame 47", "Group 3", "Rectangle 12"
- Visual descriptions: "BlueBox", "BigText", "LargeSection"
- Abbreviations that aren't universally understood

---

## 5. State Management

### Required States for Interactive Elements
Every interactive element must have these states as component variants:

| State | When | Visual Change |
|-------|------|--------------|
| Default | No interaction | Base appearance |
| Hover | Cursor over element | Subtle emphasis (lighter bg, underline, shadow) |
| Focus | Keyboard focused | Visible focus ring (2px+ outline, offset, high contrast) |
| Active/Pressed | Being clicked | Compressed or depressed appearance |
| Disabled | Not available | Reduced opacity (0.4-0.5), no cursor change |

### Additional States (as needed)
| State | When | Visual Change |
|-------|------|--------------|
| Error | Validation failed | Error color on border/text, error message visible |
| Loading | Async operation | Spinner or skeleton, content hidden or dimmed |
| Selected | Active selection | Persistent emphasis (fill, checkmark, border) |
| Empty | No data | Placeholder content with guidance |

### Implementation
- States are component **variants**, not separate layers or hidden elements
- Use a "State" variant property with values matching the state names above
- Focus states must be visible without color alone (use outline/ring, not just color change)
- Disabled states remove the element from the interactive flow — it shouldn't respond to hover

---

## 6. Variant Structure

### Component Sets
- Group related variants into a component set
- Use consistent property names across components: `State`, `Size`, `Type`, `Icon`
- Property values are lowercase-kebab: `state=default`, `size=md`, `type=primary`

### Property Types
- **Variant properties**: For visual differences that change the component structure (state, size, type)
- **Boolean properties**: For toggling optional elements (hasIcon, showBadge, isCompact)
- **Instance swap properties**: For swappable child components from a constrained set (icon, avatar, badge)
- **Text properties**: For editable text content (label, description, placeholder)
- **Slots**: For open-ended content areas where consumers provide their own content (see section 3: Slots)

### Naming
- Component set name: PascalCase (`Button`, `InputField`, `Card`)
- Variant combination names auto-generate from properties — keep property names clean
- Default variant should be the most common usage

---

## 7. Responsive Design

### Breakpoint Thinking
- Design for the primary breakpoint first (usually desktop for B2B tools)
- Use auto layout constraints that adapt: fill-container elements grow, hug-contents elements don't
- Sidebar + content layouts: sidebar is fixed width, content fills remaining space

### Min/Max Widths
- Set min-width on text containers to prevent content from collapsing
- Set max-width on text blocks for readability (60-80 characters)
- Cards in grids should have min-width to prevent unreadable compression

### Testing
- After building a screen, resize the top-level frame to verify auto layout responds correctly
- Check that text wraps, cards reflow, and no content clips or overflows

---

## 8. Prototype and Animation Setup

### Connections
- Name prototype flows descriptively: `LoginFlow`, `QuerySubmitFlow`
- Use smart animate between variant states for smooth transitions
- Set trigger types correctly: click for actions, hover for tooltips, after delay for auto-advance

### Timing Defaults
- Micro-interactions (button press, toggle): 100-150ms
- State transitions (panel open, tab switch): 200-300ms
- Page transitions: 300-400ms
- Easing: ease-out for entrances, ease-in for exits, ease-in-out for state changes

### What NOT to Prototype
- Don't prototype every possible interaction — focus on flows that need stakeholder buy-in or engineering clarification
- Static screens with clear state variants don't need prototype connections

---

## Pre-Edit Checklist

Before making any canvas edit, verify:

1. ☐ I know which project's design system applies
2. ☐ I've loaded the variable definitions with `get_variable_defs`
3. ☐ I've searched for existing components with `search_design_system`
4. ☐ I know the token names for colors, spacing, and type I'll use

## Post-Edit Checklist

After every canvas edit, verify:

1. ☐ No raw hex values — all colors bound to **semantic** variables
2. ☐ All layout frames use auto layout — exceptions only for the documented cases in section 2
3. ☐ All layers named with semantic names following the convention table in section 4
4. ☐ Component instances used where available — slots used for open-ended content areas
5. ☐ Interactive elements have state variants
6. ☐ Spacing values from the spacing scale, bound to semantic tokens where available
7. ☐ Take a screenshot to verify visual result matches intent
