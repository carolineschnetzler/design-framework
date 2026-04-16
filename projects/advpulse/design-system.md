# Design System — AdvPulse

> Theme: Dark mode primary, light mode planned
> Last updated: 2026-04-06
> Source: Live Figma variable pull across all 8 screens

---

## Color Tokens

### Brand
- `brand/green`: #18dd65

### Primitive: Gray Scale
| Token | Value | Confirmed |
|-------|-------|-----------|
| `color/gray/0` | #ffffff | yes |
| `color/gray/50` | #fafafa | yes |
| `color/gray/100` | #f5f5f5 | yes |
| `color/gray/200` | #e0e0e0 | yes |
| `color/gray/250` | #d4d4d4 | yes |
| `color/gray/300` | #c2c2c2 | prev docs only |
| `color/gray/350` | #b0b0b0 | yes |
| `color/gray/400` | #9e9e9e | yes |
| `color/gray/450` | #8c8c8c | yes |
| `color/gray/500` | #7a7a7a | yes |
| `color/gray/550` | #6e6e6e | yes |
| `color/gray/600` | #606060 | prev docs only |
| `color/gray/650` | #545454 | prev docs only |
| `color/gray/700` | #484848 | yes |
| `color/gray/750` | #3c3c3c | yes |
| `color/gray/850` | #262626 | yes |
| `color/gray/900` | #1c1c1c | yes |
| `color/gray/950` | #121212 | yes |
| `color/gray/1000` | #000000 | yes |

Note: gray/300, gray/600, gray/650 were in previous documentation but didn't appear in live `get_variable_defs` pulls. Their values (#c2c2c2, #606060, #545454) are used by semantic tokens like `border/default` and `dropdown/border`, so the primitives likely exist but aren't bound on the checked screens.

### Primitive: Green Scale
| Token | Value | Confirmed |
|-------|-------|-----------|
| `color/green/50` | #dfffed | yes |
| `color/green/100` | #b3ffd4 | yes |
| `color/green/200` | #86ffb7 | yes |
| `color/green/300` | #5aff9a | yes |
| `color/green/400` | #2eff7d | yes |
| `color/green/500` | #18dd65 | yes |

### Primitive: Blue Scale
| Token | Value | Confirmed |
|-------|-------|-----------|
| `color/blue/50` | #e8f0ff | yes |
| `color/blue/500` | #1861ff | yes |

---

### Semantic: Text
| Token | Value | Confirmed |
|-------|-------|-----------|
| `text/primary` | #fafafa | yes |
| `text/secondary` | #9e9e9e | yes |
| `text/tertiary` | #8c8c8c | yes |
| `text/label` | #d4d4d4 | yes |
| `text/on-surface` | #ffffff | yes |
| `text/on-accent` | #000000 | yes |
| `text/placeholder` | #6e6e6e | yes |
| `text/success` | #2eff7d | yes |
| `text/disabled` | #545454 | prev docs only |

### Semantic: Surfaces
| Token | Value | Confirmed |
|-------|-------|-----------|
| `surface/page` | #000000 | yes |
| `surface/card` | #1c1c1c | yes |
| `surface/sidebar` | #121212 | yes |
| `surface/header` | #1c1c1c | yes |
| `surface/input` | #1c1c1c | yes |
| `surface/elevated` | #303030 | yes |
| `surface/selected` | #18dd65 | yes |
| `surface/control` | #3c3c3c | yes |
| `surface/muted` | #484848 | prev docs only |
| `surface/selected-hover` | #5aff9a | prev docs only |
| `surface/important` | #606060 | prev docs only |

### Semantic: Borders
| Token | Value | Confirmed |
|-------|-------|-----------|
| `border/default` | #545454 | yes |
| `border/secondary` | #18dd65 | yes |
| `border/tertiary` | #fafafa | yes |
| `border/card` | #8c8c8c | yes |
| `border/nav` | #b0b0b0 | yes |
| `border/active` | #18dd65 | prev docs only |
| `border/disabled` | #545454 | prev docs only |
| `border/control` | #606060 | prev docs only |

### Semantic: Icons
| Token | Value | Confirmed |
|-------|-------|-----------|
| `icon/primary` | #fafafa | yes |
| `icon/secondary` | #9e9e9e | yes |
| `icon/accent` | #18dd65 | yes |
| `icon/inverted` | #121212 | yes |
| `icon/disabled` | #545454 | prev docs only |

### Semantic: Dividers
| Token | Value | Confirmed |
|-------|-------|-----------|
| `divider/surface` | #7a7a7a | yes |
| `divider/default` | #484848 | prev docs only |

### Semantic: Avatar
| Token | Value (Dark) | Value (Light) | Confirmed |
|-------|-------------|---------------|-----------|
| `avatar/primary/default/bg` | #053d24 | #DFFFED | yes |
| `avatar/primary/default/border` | #5aff9a | #0CB84E | yes |
| `avatar/primary/default/text` | #fafafa | #053D24 | yes |
| `avatar/secondary/bg` | #303030 | #F5F5F5 | prev docs only |
| `avatar/secondary/border` | #B0B0B0 | #9E9E9E | prev docs only |
| `avatar/secondary/text` | #FAFAFA | #262626 | prev docs only |

### Semantic: Badge
| Token | Value | Confirmed |
|-------|-------|-----------|
| `badge/complete/text` | #2eff7d | yes |
| `badge/complete/bg` | #032818 | yes |
| `badge/complete/border` | #075230 | yes |
| `badge/in-progress/bg` | #130c3d | yes |

### Semantic: Pill
| Token | Value | Confirmed |
|-------|-------|-----------|
| `pill/bg-selected` | #18dd65 | yes |
| `pill/text-selected` | #000000 | yes |

### Misc
| Token | Value | Confirmed |
|-------|-------|-----------|
| `Background Gradient 1` | (gradient) | yes |
| `Zero` | 0 | yes |

---

## Component Tokens

### Button (Primary)
| Token | Value | Confirmed |
|-------|-------|-----------|
| `button/primary/text` | #18dd65 | yes |
| `button/primary/bg` | transparent | yes |
| `button/primary/border` | #18dd65 | yes |
| `button/primary/text-hover` | #000000 | prev docs only |
| `button/primary/bg-hover` | #18dd65 | prev docs only |
| `button/primary/text-disabled` | #545454 | prev docs only |
| `button/primary/bg-disabled` | transparent | prev docs only |
| `button/primary/border-disabled` | #545454 | prev docs only |
| `button/primary/text-focus` | #18dd65 | prev docs only |
| `button/primary/bg-focus` | transparent | prev docs only |
| `button/primary/border-focus` | #fafafa | prev docs only |

### Button (Secondary)
| Token | Value | Confirmed |
|-------|-------|-----------|
| `button/secondary/text` | #fafafa | yes |
| `button/secondary/bg` | transparent | yes |
| `button/secondary/border` | #fafafa | yes |
| `button/secondary/text-hover` | #000000 | prev docs only |
| `button/secondary/bg-hover` | #fafafa | prev docs only |
| `button/secondary/text-disabled` | #545454 | prev docs only |
| `button/secondary/border-disabled` | #545454 | prev docs only |
| `button/secondary/text-focus` | #ffffff | prev docs only |
| `button/secondary/border-focus` | #18dd65 | prev docs only |

### Status Chip
| Token | Value | Confirmed |
|-------|-------|-----------|
| `status-chip/icon` | #2eff7d | yes |
| `status-chip/text` | #d4d4d4 | yes |
| `status-chip/label` | #8c8c8c | yes |
| `status-chip/dropdown` | #d4d4d4 | yes |
| `status-chip/bg` | #484848 | yes |

### Checkbox
| Token | Value | Confirmed |
|-------|-------|-----------|
| `checkbox/border-default` | #606060 | yes |
| `checkbox/selected-bg` | #18dd65 | yes |
| `checkbox/border-hover` | #8c8c8c | prev docs only |
| `checkbox/border-disabled` | #545454 | prev docs only |
| `checkbox/border-focus` | #b0b0b0 | prev docs only |
| `checkbox/selected-bg-hover` | #5aff9a | prev docs only |
| `checkbox/selected-border-focus` | #f5f5f5 | prev docs only |

### RadioButton
| Token | Value | Confirmed |
|-------|-------|-----------|
| `radio/border-default` | #606060 | yes |
| `radio/selected-border` | #18dd65 | yes |
| `radio/border-hover` | #8c8c8c | prev docs only |
| `radio/border-disabled` | #545454 | prev docs only |
| `radio/border-focus` | #b0b0b0 | prev docs only |
| `radio/selected-bg-hover` | #5aff9a | prev docs only |
| `radio/selected-border-focus` | #f5f5f5 | prev docs only |

### Dropdown
| Token | Value | Confirmed |
|-------|-------|-----------|
| `dropdown/icon` | #9e9e9e | yes |
| `dropdown/bg` | transparent | yes |
| `dropdown/border` | #606060 | yes |
| `dropdown/bg-hover` | #1c1c1c | yes |
| `dropdown/border-focus` | #9e9e9e | yes |
| `dropdown/text` | #6e6e6e | prev docs only |
| `dropdown/text-hover` | #8c8c8c | prev docs only |
| `dropdown/icon-hover` | #d4d4d4 | prev docs only |
| `dropdown/text-disabled` | #545454 | prev docs only |
| `dropdown/icon-disabled` | #545454 | prev docs only |
| `dropdown/border-disabled` | #545454 | prev docs only |

### Dropdown Pill (Incomplete)
| Token | Value | Confirmed |
|-------|-------|-----------|
| `dropdown-pill/incomplete/text` | #d4d4d4 | yes |
| `dropdown-pill/incomplete/icon` | #d4d4d4 | yes |
| `dropdown-pill/incomplete/text-hover` | #e0e0e0 | prev docs only |
| `dropdown-pill/incomplete/icon-hover` | #e0e0e0 | prev docs only |
| `dropdown-pill/incomplete/text-focus` | #d4d4d4 | prev docs only |
| `dropdown-pill/incomplete/icon-focus` | #d4d4d4 | prev docs only |
| `dropdown-pill/incomplete/border-focus` | #fafafa | prev docs only |
| `dropdown-pill/incomplete/text-disabled` | #7a7a7a | prev docs only |
| `dropdown-pill/incomplete/icon-disabled` | #7a7a7a | prev docs only |

### Dropdown Pill (Working)
| Token | Value | Confirmed |
|-------|-------|-----------|
| `dropdown-pill/working/text` | #fafafa | yes |
| `dropdown-pill/working/icon` | #fafafa | yes |
| `dropdown-pill/working/text-hover` | #ffffff | prev docs only |
| `dropdown-pill/working/icon-hover` | #ffffff | prev docs only |
| `dropdown-pill/working/border` | #18dd65 | prev docs only |
| `dropdown-pill/working/border-focus` | #fafafa | prev docs only |

### Dropdown Pill (Completed)
| Token | Value | Confirmed |
|-------|-------|-----------|
| `dropdown-pill/completed/icon-left` | #18dd65 | yes |
| `dropdown-pill/completed/text` | #d4d4d4 | yes |
| `dropdown-pill/completed/icon-right` | #d4d4d4 | yes |
| `dropdown-pill/completed/bg-focus` | #303030 | yes |
| `dropdown-pill/completed/text-hover` | #e0e0e0 | prev docs only |
| `dropdown-pill/completed/text-focus` | #d4d4d4 | prev docs only |
| `dropdown-pill/completed/icon-focus` | #d4d4d4 | prev docs only |
| `dropdown-pill/completed/border-focus` | #fafafa | prev docs only |

### Filter Chip
| Token | Value | Confirmed |
|-------|-------|-----------|
| `filter-chip/text` | #d4d4d4 | yes |
| `filter-chip/icon` | #d4d4d4 | yes |
| `filter-chip/bg` | #121212 | yes |
| `filter-chip/text-hover` | #e0e0e0 | prev docs only |
| `filter-chip/icon-hover` | #e0e0e0 | prev docs only |
| `filter-chip/bg-hover` | #3c3c3c | prev docs only |
| `filter-chip/text-disabled` | #545454 | prev docs only |
| `filter-chip/icon-disabled` | #545454 | prev docs only |
| `filter-chip/bg-disabled` | #121212 | prev docs only |
| `filter-chip/text-focus` | #f5f5f5 | prev docs only |
| `filter-chip/icon-focus` | #d4d4d4 | prev docs only |
| `filter-chip/bg-focus` | #121212 | prev docs only |
| `filter-chip/border-focus` | #b0b0b0 | prev docs only |

### Search
| Token | Value | Confirmed |
|-------|-------|-----------|
| Default: bg `surface/input`, border `border/default`, text `text/placeholder` | — | inferred |
| Active: border `border/secondary` (#18dd65) | — | inferred |

---

## Strokes

| Token | Value | Confirmed |
|-------|-------|-----------|
| `stroke/xs` | 1px | yes |
| `stroke/s` | 2px | yes |

---

## Typography

### Font Families
- **Sora** — Display, headings, labels, numbers
- **DM Sans** — Body text
- **Fragment Mono** — Task update logs (monospace)

### Text Styles (as Figma variables)

Confirmed in live pulls:

| Style | Font | Size | Weight | Line Height | Letter Spacing |
|-------|------|------|--------|-------------|----------------|
| Display M | Sora | 28px | 400 (Regular) | 100% | 0 |
| Display S | Sora | 20px | 300 (Light) | 100% | 0 |
| Heading XS | Sora | 18px | 400 (Regular) | 100% | 0 |
| Body L | DM Sans | 18px | 400 (Regular) | 100% | 0 |
| Body MB | DM Sans | 16px | 700 (Bold) | 100% | 0 |
| Body M | DM Sans | 16px | 400 (Regular) | 100% | 0 |
| Body S | DM Sans | 14px | 400 (Regular) | 100% | 0 |
| Body XS | DM Sans | 12px | 400 (Regular) | 100% | 0 |
| Label L | Sora | 16px | 300 (Light) | 100% | 0 |
| Label S | Sora | 10px | 300 (Light) | 100% | 5% |
| Number S | Sora | 15px | 300 (Light) | 100% | 0 |

From previous documentation (not returned by `get_variable_defs` — may exist as text styles rather than variables):

| Style | Font | Size | Weight | Line Height | Letter Spacing |
|-------|------|------|--------|-------------|----------------|
| Display XL | Sora | 60px | 400 (Regular) | 100% | 0 |
| Display L | Sora | 38px | 400 (Regular) | 100% | 0 |
| Heading L | Sora | 26px | 400 (Regular) | 100% | 0 |
| Heading M | Sora | 22px | 400 (Regular) | 100% | 0 |
| Heading S | Sora | 20px | 400 (Regular) | 100% | 0 |
| Body LB | DM Sans | 18px | 600 (SemiBold) | 100% | 0 |

---

## Spacing

### Primitive Scale
| Token | Value | Confirmed |
|-------|-------|-----------|
| `space/4` | 4px | yes |
| `space/8` | 8px | yes |
| `space/12` | 12px | yes |
| `space/16` | 16px | yes |
| `space/24` | 24px | yes |
| `space/32` | 32px | yes |
| `space/48` | 48px | prev docs only |
| `space/88` | 88px | yes |
| `space/96` | 96px | yes |

### Semantic Spacing
| Token | Value | Usage | Confirmed |
|-------|-------|-------|-----------|
| `spacing/inline-gap` | 4px | Gap between inline elements (icon + text) | yes |
| `spacing/icon-gap` | 4px | Gap around icons | yes |
| `spacing/item-gap` | 8px | Gap between items in a list or group | yes |
| `spacing/control-padding-y` | 8px | Vertical padding inside controls | yes |
| `spacing/control-padding-x` | 12px | Horizontal padding inside controls | yes |
| `spacing/card-padding-compact` | 12px | Padding inside compact cards | yes |
| `spacing/card-padding` | 16px | Padding inside standard cards | yes |
| `spacing/field-gap` | 16px | Gap between form fields | yes |
| `spacing/section-gap` | 24px | Gap between sections within a panel | yes |
| `spacing/panel-padding` | 24px | Padding inside panels | yes |
| `spacing/page-padding` | 32px | Padding at page level | yes |
| `spacing/nav-padding` | 48px | Padding inside navigation | yes |
| `spacing/section-break` | 48px | Large break between major sections | yes |
| `Zero` | 0 | Explicit zero value | yes |

---

## Radius

| Token | Value | Confirmed |
|-------|-------|-----------|
| `radius/s` | 8px | yes |
| `radius/m` | 16px | yes |
| `radius/l` | 32px | yes |
| `radius/full` | 999px (pill) | yes |

---

## Component Inventory

### Core Controls
| Component | Node ID | Variants |
|-----------|---------|----------|
| Button | 153:1302 | Primary/Secondary x Default/Hover/Disabled/Focus |
| Button/Icon/Big | 152:890 | Primary/Secondary icon buttons |
| Toggle | 564:7993 | On/Off |
| Checkbox | 343:1446 | Default/Hover/Disabled/Focus x Selected/Unselected |
| RadioButton | 361:2132 | Default/Hover/Disabled/Focus x Selected/Unselected |
| Search | 312:1610 | Default/Active |

### Form Controls
| Component | Node ID | Variants |
|-----------|---------|----------|
| Dropdown | 343:5788 | Empty/Filled x Default/Hover/Disabled/Focus |
| Dropdown Item | 343:1757 | Checkbox/RadioButton type x states |
| Dropdown-pill | 341:6204 | Incomplete/Working/Complete x states |
| Filter chip | 343:5807 | Default/Hover/Disabled/Focus |
| RangeSlider | 363:4875 | Full/Small x Default/Disabled |
| Pill | 210:1055 | Default/Hover/Selected/Hover-selected |

### Chat Components
| Component | Node ID | Variants |
|-----------|---------|----------|
| Chat Input | 152:915 | First Chat/Reply x Default/Disabled |
| Chat + Buttons | 310:1564 | Send/Stop x Default/Disabled |
| message bubble | 226:2307 | User/Chatbot x Body/HeaderBody/Title |
| Suggestion Group | 226:2575 | 2/3/4 suggestions |
| Prompt Suggestion | 226:2558 | — |

### Agentic Components
| Component | Node ID | Variants |
|-----------|---------|----------|
| AgenticCard/Progress | 224:1817 | Expanded/Collapsed x Full/Small |
| AgenticCard/Intake | 363:7126 | Expanded/Collapsed x Full/Small |
| agentic chat message | 211:13287 | Working/Done |
| Progress indicator | 218:4088 | Done/Working x Collapsed/Expanded x Default/Small |
| Task group | 223:1374 | 0-5 updates |
| Task update | 211:13276 | Default/Found results |
| Status indicator | 207:835 | Loading 1-4, Complete |

### Navigation & Layout
| Component | Node ID | Notes |
|-----------|---------|-------|
| Top Nav | 153:1110 | Logo, icons, avatar |
| Side Nav | 151:751 | Logo, nav icons, avatar |
| ChatPanel/Side/Shell | 235:2619 | Sidebar with chat input |

### Data Display
| Component | Node ID | Notes |
|-----------|---------|-------|
| Simple Table Cell | 522:3744 | Default/Header |
| badge | 538:2584 | Complete/In Progress |
| Bullet result | 522:3588 | Firm name with CRD |
| File Upload | 153:1162 | File name + size |

### Icons (23 icons, 16px and 24px sizes)
See icon library for full list with node IDs.

---

## Layout Patterns

### Two-layout system
1. **Full-screen chat** (InitialChat, AgenticChat): Side Nav (72-77px) + centered content (1000px max-width)
2. **Split panel** (RecoFirms, Workspace, Firm Detail): Top Nav (72px height) + ChatPanel (423px) + Content area (remaining)

### Navigation rules
- Side Nav: Full-screen chat views only (72-77px wide, vertical)
- Top Nav: Split-panel views only (1440px wide, 72px tall)
- Never appear together on the same screen

### Design decisions
- All buttons are ghost/outline style by default (transparent bg, colored border)
- Brand green (#18dd65) used for accent, active states, and AI-executed actions
- Success green (#2eff7d) used for completion states and positive feedback
- Blue (#1861ff) reserved for in-progress badges

---

## Token Status Key

- **yes** — Returned by `get_variable_defs` on live Figma screens (2026-04-06)
- **prev docs only** — Documented in previous design system review but not returned by live variable pulls. May exist as variables not bound to checked screens, or as Figma text/color styles rather than variables. Verify before assuming these are current.
