# Design System — AdvPulse (Product UI)

> System: **Product UI** — governs the AdvPulse application (every in-app screen)
> Theme: Dark mode (primary) + Light mode (defined, not yet shipped in screens)
> Last updated: 2026-07-08 (live Figma re-audit: brand/black→gray/900, brand/dark teal flagged, Mono S text style added; Two-Systems framing added 2026-06-30)
> Source: Live Plugin API enumeration of all variable collections, text styles, effect styles, and paint styles

---

## Two Systems — Read First

AdvPulse runs on **two distinct design systems** with different jobs. This document is the **Product UI** system. The **Brand / Marketing** system (logo, website, pitch, social, print, email) lives in [`brand-guidelines.md`](brand-guidelines.md). Do not mix them.

| | **Product UI** (this doc) | **Brand / Marketing** (`brand-guidelines.md`) |
|---|---|---|
| **Governs** | The AdvPulse application | Logo, marketing website, pitch deck, social, print, email |
| **Type** | Sora · DM Sans · Fragment Mono | Playfair Display · Plus Jakarta Sans · IBM Plex Mono |
| **Color** | Token system (gray/green/orange-error/violet-blue), Dark + Light | Pulse / Deep Teal / Ink / Mist / Paper (5 fixed roles) |
| **Source of truth** | Figma `kFyd7XSbESiizgbP6u8jAF` (live tokens) | `brand-guidelines.md` + Brand & Style Guide |

**The only shared value** is the green: product **`color/green/500` (`brand/green`)** = brand **Pulse `#18DD65`**. Everything else is intentionally different. The two worlds meet only at that green and where a product screenshot sits inside a marketing surface.

---

## Collections Overview

| Collection | Modes | Variables | Purpose |
|------------|-------|-----------|---------|
| **Base** | Base (1 mode) | 60 | Primitive scales (color/gray, color/green, color/orange-error, color/violet-blue, space, radius, stroke) |
| **Semantic** | Dark, Light (2 modes) | 232 | All semantic and component tokens — every value aliases to a Base primitive |

Semantic-mode usage: Every consuming surface (frames, components, screens) should bind to Semantic tokens, never directly to Base primitives. Semantic tokens resolve per mode automatically.

---

## Base Collection (Primitives)

### Color: Gray Scale (19 values)
| Token | Value |
|-------|-------|
| `color/gray/0` | #ffffff |
| `color/gray/50` | #fafafa |
| `color/gray/100` | #f5f5f5 |
| `color/gray/200` | #e0e0e0 |
| `color/gray/250` | #d4d4d4 |
| `color/gray/300` | #c2c2c2 |
| `color/gray/350` | #b0b0b0 |
| `color/gray/400` | #9e9e9e |
| `color/gray/450` | #8c8c8c |
| `color/gray/500` | #7a7a7a |
| `color/gray/550` | #6e6e6e |
| `color/gray/600` | #606060 |
| `color/gray/650` | #545454 |
| `color/gray/700` | #484848 |
| `color/gray/750` | #3c3c3c |
| `color/gray/800` | #303030 |
| `color/gray/850` | #262626 |
| `color/gray/900` | #1c1c1c |
| `color/gray/950` | #121212 |
| `color/gray/1000` | #000000 |

### Color: Green Scale (10 values)
| Token | Value |
|-------|-------|
| `color/green/50` | #dfffed |
| `color/green/100` | #b3ffd4 |
| `color/green/200` | #86ffb7 |
| `color/green/300` | #5aff9a |
| `color/green/400` | #2eff7d |
| `color/green/500` | #18dd65 (brand) |
| `color/green/600` | #0cb84e |
| `color/green/700` | #075230 |
| `color/green/800` | #053d24 |
| `color/green/900` | #032818 |

### Color: Orange-Error Scale (4 values, NEW since 2026-04-06)
| Token | Value |
|-------|-------|
| `color/orange-error/100` | #ffd0c0 |
| `color/orange-error/400` | #ff6e40 |
| `color/orange-error/500` | #ff4520 |
| `color/orange-error/600` | #d9301a |

### Color: Violet-Blue Scale (3 values, NEW since 2026-04-06)
| Token | Value |
|-------|-------|
| `color/violet-blue/100` | #8ea6ff |
| `color/violet-blue/500` | #4b4efb |
| `color/violet-blue/900` | #130c3d |

Used for `badge/in-progress/*`. Note: `color/blue/{50,500}` from previous docs no longer exist as Base variables — replaced by violet-blue.

### Color: Alpha
| Token | Value |
|-------|-------|
| `color/0-alpha/transparent` | #000000 alpha=0 |

### Spacing (12 values, NEW: 64/72/80)
| Token | Value | Scope |
|-------|-------|-------|
| `space/4` | 4 | GAP |
| `space/8` | 8 | GAP |
| `space/12` | 12 | GAP |
| `space/16` | 16 | GAP |
| `space/24` | 24 | GAP |
| `space/32` | 32 | GAP |
| `space/48` | 48 | GAP |
| `space/64` | 64 | GAP |
| `space/72` | 72 | GAP |
| `space/80` | 80 | GAP |
| `space/88` | 88 | GAP |
| `space/96` | 96 | GAP |

### Radius (5 values, NEW: none)
| Token | Value | Scope |
|-------|-------|-------|
| `radius/none` | 0 | CORNER_RADIUS |
| `radius/s` | 8 | CORNER_RADIUS |
| `radius/m` | 16 | CORNER_RADIUS |
| `radius/l` | 32 | CORNER_RADIUS |
| `radius/full` | 999 (pill) | CORNER_RADIUS |

### Stroke (5 values, NEW: m/l/xl)
| Token | Value | Scope |
|-------|-------|-------|
| `stroke/xs` | 1 | STROKE_FLOAT |
| `stroke/s` | 2 | STROKE_FLOAT |
| `stroke/m` | 4 | STROKE_FLOAT |
| `stroke/l` | 6 | STROKE_FLOAT |
| `stroke/xl` | 8 | STROKE_FLOAT |

---

## Semantic Collection (Dark + Light)

All Semantic tokens alias Base primitives. The table below shows the alias target per mode. Resolved hex values are listed in parentheses for Dark-mode visibility checks.

### Brand
| Token | Dark | Light |
|-------|------|-------|
| `brand/green` | → color/green/500 (#18dd65) | → color/green/500 (#18dd65) |
| `brand/white` | → color/gray/50 (#fafafa) | → color/gray/50 (#fafafa) |
| `brand/black` | → color/gray/900 (#1c1c1c) | → color/gray/900 (#1c1c1c) |

> `brand/black` was retargeted from gray/1000 (#000000) to gray/900 (#1c1c1c) — a softer brand black, confirmed intentional.
> A stray `brand/dark teal` (raw #113535 = Brand Deep Teal) briefly appeared in this collection; it was unused and deleted on 2026-07-08 — Deep Teal is marketing-only and lives in [`brand-guidelines.md`](brand-guidelines.md).

### Surfaces
| Token | Dark | Light |
|-------|------|-------|
| `surface/page` | gray/1000 | gray/0 |
| `surface/header` | gray/900 | gray/0 |
| `surface/sidebar` | gray/950 | gray/50 |
| `surface/card` | gray/900 | gray/0 |
| `surface/input` | gray/900 | gray/100 |
| `surface/elevated` | gray/800 | gray/100 |
| `surface/elevated-on-card` | gray/800 | #ffffff (raw) |
| `surface/hover` | gray/800 | gray/200 |
| `surface/hover-on-elevated` | gray/700 | #ffffff (raw) |
| `surface/overlay` | gray/900 | gray/0 |
| `surface/control` | gray/750 | gray/100 |
| `surface/important-on-control` | gray/300 | gray/800 |
| `surface/important` | gray/600 | gray/950 |
| `surface/muted` | gray/700 | gray/200 |
| `surface/disabled` | gray/800 | gray/300 |
| `surface/table-header` | gray/800 | gray/100 |
| `surface/table-row` | gray/900 | gray/100 |
| `surface/table-row-alt` | gray/850 | gray/50 |
| `surface/selected` | green/500 | green/500 |
| `surface/selected-hover` | green/300 | green/300 |
| `surface/interactive-hover` | gray/50 | gray/950 |

### Text
| Token | Dark | Light |
|-------|------|-------|
| `text/primary` | gray/50 | gray/950 |
| `text/secondary` | gray/400 | gray/600 |
| `text/tertiary` | gray/450 | gray/450 |
| `text/label` | gray/250 | gray/700 |
| `text/secondary-label` | gray/550 | gray/250 |
| `text/on-surface` | gray/0 | gray/0 |
| `text/on-accent` | gray/1000 | gray/1000 |
| `text/placeholder` | gray/550 | gray/400 |
| `text/placeholder-on-surface` | gray/450 | gray/500 |
| `text/disabled` | gray/650 | gray/200 |
| `text/accent` | green/500 | green/700 |
| `text/accent-subtle` | green/100 | green/700 |
| `text/accent-muted` | green/200 | green/700 |
| `text/accent-medium` | green/300 | green/700 |
| `text/success` | green/400 | green/700 |
| `text/link` | green/500 | green/700 |
| `text/error` | orange-error/500 | orange-error/600 |
| `text/agent` | green/200 | green/600 |

### Borders
| Token | Dark | Light |
|-------|------|-------|
| `border/default` | gray/650 | gray/200 |
| `border/secondary` | green/500 | green/400 |
| `border/tertiary` | gray/50 | gray/1000 |
| `border/card` | gray/550 | gray/350 |
| `border/control` | gray/600 | gray/300 |
| `border/subtle` | gray/750 | gray/100 |
| `border/nav` | gray/350 | gray/350 |
| `border/hover` | gray/450 | gray/450 |
| `border/active` | green/500 | green/600 |
| `border/disabled` | gray/650 | gray/200 |
| `border/error` | orange-error/500 | orange-error/600 |

### Icons
| Token | Dark | Light |
|-------|------|-------|
| `icon/primary` | gray/50 | gray/950 |
| `icon/secondary` | gray/400 | gray/600 |
| `icon/accent` | green/500 | green/700 |
| `icon/inverted` | gray/950 | gray/50 |
| `icon/disabled` | gray/650 | gray/200 |

### Dividers
| Token | Dark | Light |
|-------|------|-------|
| `divider/default` | gray/700 | gray/450 |
| `divider/surface` | gray/500 | gray/550 |
| `divider/active` | gray/350 | gray/650 |

### Interactive
| Token | Dark | Light |
|-------|------|-------|
| `interactive/primary` | green/500 | green/600 |
| `interactive/primary-hover` | green/400 | green/700 |
| `interactive/primary-selected-hover` | green/300 | green/300 |
| `interactive/secondary` | gray/800 | gray/100 |
| `interactive/secondary-hover` | gray/750 | gray/200 |
| `interactive/disabled` | gray/650 | gray/200 |

### Spacing (semantic, aliased to Base `space/*`)
| Token | Dark | Light | Usage |
|-------|------|-------|-------|
| `spacing/inline-gap` | space/4 | space/4 | Gap between inline elements (icon + text) |
| `spacing/icon-gap` | space/4 | space/4 | Gap around icons |
| `spacing/item-gap` | space/8 | space/8 | Gap between items in a list/group |
| `spacing/control-padding-y` | space/8 | space/8 | Vertical padding inside controls |
| `spacing/control-padding-x` | space/12 | space/12 | Horizontal padding inside controls |
| `spacing/card-padding-compact` | space/12 | space/12 | Padding inside compact cards |
| `spacing/card-padding` | space/16 | space/16 | Padding inside standard cards |
| `spacing/field-gap` | space/16 | space/16 | Gap between form fields |
| `spacing/section-gap` | space/24 | space/24 | Gap between sections within a panel |
| `spacing/panel-padding` | space/24 | space/24 | Padding inside panels |
| `spacing/nav-padding` | space/24 | space/24 | Padding inside navigation |
| `spacing/page-padding` | space/32 | space/32 | Padding at page level |
| `spacing/section-break` | space/48 | space/48 | Large break between major sections |
| `spacing/hero-spacing` | space/64 | space/64 | Hero/marquee-level spacing |

Note: `spacing/nav-padding` is now 24 (was previously documented as 48); the 48 value moved to `spacing/section-break`.

---

## Component Tokens (Semantic)

### Button — Primary (ghost/outline)
| Token | Dark | Light |
|-------|------|-------|
| `button/primary/bg` | transparent | transparent |
| `button/primary/text` | green/500 | green/600 |
| `button/primary/border` | green/500 | green/600 |
| `button/primary/bg-hover` | green/500 | green/600 |
| `button/primary/text-hover` | gray/1000 | gray/1000 |
| `button/primary/border-hover` | green/500 | green/600 |
| `button/primary/bg-disabled` | transparent | transparent |
| `button/primary/text-disabled` | gray/650 | gray/200 |
| `button/primary/border-disabled` | gray/650 | gray/200 |
| `button/primary/bg-focus` | transparent | transparent |
| `button/primary/text-focus` | green/500 | green/600 |
| `button/primary/border-focus` | gray/50 | gray/950 |

### Button — Secondary (ghost/outline)
| Token | Dark | Light |
|-------|------|-------|
| `button/secondary/bg` | transparent | transparent |
| `button/secondary/text` | gray/50 | gray/950 |
| `button/secondary/border` | gray/50 | gray/950 |
| `button/secondary/bg-hover` | gray/50 | gray/950 |
| `button/secondary/text-hover` | gray/1000 | gray/0 |
| `button/secondary/border-hover` | gray/1000 | gray/950 |
| `button/secondary/bg-disabled` | transparent | transparent |
| `button/secondary/text-disabled` | gray/650 | gray/300 |
| `button/secondary/border-disabled` | gray/650 | gray/200 |
| `button/secondary/bg-focus` | transparent | transparent |
| `button/secondary/text-focus` | gray/0 | gray/950 |
| `button/secondary/border-focus` | green/500 | green/600 |

### Button — Danger (NEW since 2026-04-06)
| Token | Dark | Light |
|-------|------|-------|
| `button/danger/bg` | transparent | transparent |
| `button/danger/text` | orange-error/500 | orange-error/600 |
| `button/danger/border` | orange-error/500 | orange-error/600 |
| `button/danger/bg-hover` | orange-error/500 | orange-error/600 |
| `button/danger/text-hover` | gray/1000 | gray/0 |
| `button/danger/border-hover` | orange-error/500 | orange-error/600 |
| `button/danger/bg-disabled` | transparent | transparent |
| `button/danger/text-disabled` | gray/650 | gray/300 |
| `button/danger/border-disabled` | gray/650 | gray/200 |
| `button/danger/bg-focus` | transparent | transparent |
| `button/danger/text-focus` | orange-error/500 | orange-error/600 |
| `button/danger/border-focus` | gray/50 | gray/950 |

Plus legacy `button/Color` raw (#ffffff, both modes) — used for icon button glyphs.

### Checkbox
| Token | Dark | Light |
|-------|------|-------|
| `checkbox/border-default` | gray/600 | gray/300 |
| `checkbox/border-hover` | gray/450 | gray/450 |
| `checkbox/border-focus` | gray/350 | gray/600 |
| `checkbox/border-disabled` | gray/650 | gray/200 |
| `checkbox/selected-bg` | green/500 | green/600 |
| `checkbox/selected-bg-hover` | green/300 | green/300 |
| `checkbox/selected-border-focus` | gray/100 | gray/950 |

### Radio
| Token | Dark | Light |
|-------|------|-------|
| `radio/border-default` | gray/600 | gray/300 |
| `radio/border-hover` | gray/450 | gray/450 |
| `radio/border-focus` | gray/350 | gray/600 |
| `radio/border-disabled` | gray/650 | gray/200 |
| `radio/selected-border` | green/500 | green/600 |
| `radio/selected-bg-hover` | green/300 | green/300 |
| `radio/selected-border-focus` | gray/100 | gray/950 |

### Input (NEW token group since 2026-04-06)
| Token | Dark | Light |
|-------|------|-------|
| `input/border-default` | gray/600 | gray/300 |
| `input/border-active` | green/500 | green/600 |
| `input/border-disabled` | gray/800 | gray/200 |
| `input/placeholder` | gray/550 | gray/400 |
| `input/placeholder-disabled` | gray/650 | gray/300 |

### Dropdown
| Token | Dark | Light |
|-------|------|-------|
| `dropdown/bg` | transparent | transparent |
| `dropdown/text` | gray/550 | gray/400 |
| `dropdown/icon` | gray/400 | gray/600 |
| `dropdown/border` | gray/600 | gray/250 |
| `dropdown/bg-hover` | gray/900 | gray/100 |
| `dropdown/text-hover` | gray/450 | gray/600 |
| `dropdown/icon-hover` | gray/250 | gray/700 |
| `dropdown/text-disabled` | gray/650 | gray/200 |
| `dropdown/icon-disabled` | gray/650 | gray/200 |
| `dropdown/border-disabled` | gray/650 | gray/200 |
| `dropdown/border-focus` | gray/400 | gray/600 |

### Dropdown Pill — Incomplete
| Token | Dark | Light |
|-------|------|-------|
| `dropdown-pill/incomplete/bg` | gray/800 | gray/100 |
| `dropdown-pill/incomplete/text` | gray/250 | gray/600 |
| `dropdown-pill/incomplete/icon` | gray/250 | gray/600 |
| `dropdown-pill/incomplete/bg-hover` | gray/700 | gray/200 |
| `dropdown-pill/incomplete/text-hover` | gray/200 | gray/700 |
| `dropdown-pill/incomplete/icon-hover` | gray/200 | gray/800 |
| `dropdown-pill/incomplete/bg-disabled` | gray/800 | gray/200 |
| `dropdown-pill/incomplete/text-disabled` | gray/500 | gray/500 |
| `dropdown-pill/incomplete/icon-disabled` | gray/500 | gray/500 |
| `dropdown-pill/incomplete/bg-focus` | gray/800 | gray/100 |
| `dropdown-pill/incomplete/text-focus` | gray/250 | gray/600 |
| `dropdown-pill/incomplete/icon-focus` | gray/250 | gray/600 |
| `dropdown-pill/incomplete/border-focus` | gray/50 | gray/950 |

### Dropdown Pill — Working
| Token | Dark | Light |
|-------|------|-------|
| `dropdown-pill/working/bg` | gray/800 | gray/100 |
| `dropdown-pill/working/text` | gray/50 | gray/950 |
| `dropdown-pill/working/icon` | gray/50 | gray/950 |
| `dropdown-pill/working/border` | green/500 | green/500 |
| `dropdown-pill/working/bg-hover` | gray/700 | gray/200 |
| `dropdown-pill/working/text-hover` | gray/0 | gray/1000 |
| `dropdown-pill/working/icon-hover` | gray/0 | gray/1000 |
| `dropdown-pill/working/border-hover` | green/500 | green/500 |
| `dropdown-pill/working/bg-disabled` | gray/800 | gray/200 |
| `dropdown-pill/working/text-disabled` | gray/500 | gray/500 |
| `dropdown-pill/working/icon-disabled` | gray/500 | gray/500 |
| `dropdown-pill/working/bg-focus` | gray/800 | gray/100 |
| `dropdown-pill/working/text-focus` | gray/50 | gray/950 |
| `dropdown-pill/working/icon-focus` | gray/50 | gray/950 |
| `dropdown-pill/working/border-focus` | gray/50 | gray/950 |

### Dropdown Pill — Completed
| Token | Dark | Light |
|-------|------|-------|
| `dropdown-pill/completed/bg` | gray/800 | gray/100 |
| `dropdown-pill/completed/text` | gray/250 | gray/600 |
| `dropdown-pill/completed/icon-left` | green/500 | green/500 |
| `dropdown-pill/completed/icon-right` | gray/250 | gray/600 |
| `dropdown-pill/completed/Color` | green/500 | green/500 |
| `dropdown-pill/completed/bg-hover` | gray/700 | gray/200 |
| `dropdown-pill/completed/text-hover` | gray/200 | gray/700 |
| `dropdown-pill/completed/icon-hover` | gray/200 | gray/700 |
| `dropdown-pill/completed/bg-disabled` | gray/800 | gray/200 |
| `dropdown-pill/completed/text-disabled` | gray/500 | gray/500 |
| `dropdown-pill/completed/icon-disabled` | gray/500 | gray/500 |
| `dropdown-pill/completed/bg-focus` | gray/800 | gray/100 |
| `dropdown-pill/completed/text-focus` | gray/250 | gray/600 |
| `dropdown-pill/completed/icon-focus` | gray/250 | gray/600 |
| `dropdown-pill/completed/border-focus` | gray/50 | gray/950 |

### Filter Chip
| Token | Dark | Light |
|-------|------|-------|
| `filter-chip/bg` | gray/950 | gray/100 |
| `filter-chip/text` | gray/250 | gray/700 |
| `filter-chip/icon` | gray/250 | gray/600 |
| `filter-chip/bg-hover` | gray/750 | gray/200 |
| `filter-chip/text-hover` | gray/200 | gray/600 |
| `filter-chip/icon-hover` | gray/200 | gray/700 |
| `filter-chip/bg-disabled` | gray/950 | gray/300 |
| `filter-chip/text-disabled` | gray/650 | gray/250 |
| `filter-chip/icon-disabled` | gray/650 | gray/250 |
| `filter-chip/bg-focus` | gray/950 | gray/100 |
| `filter-chip/text-focus` | gray/100 | gray/900 |
| `filter-chip/icon-focus` | gray/250 | gray/600 |
| `filter-chip/border-focus` | gray/350 | gray/600 |

### Pill
| Token | Dark | Light |
|-------|------|-------|
| `pill/text` | gray/50 | gray/950 |
| `pill/border-default` | gray/50 | gray/950 |
| `pill/border-hover` | green/500 | green/600 |
| `pill/text-selected` | gray/1000 | gray/1000 |
| `pill/bg-selected` | green/500 | green/600 |

### Status Chip
| Token | Dark | Light |
|-------|------|-------|
| `status-chip/bg` | gray/700 | gray/100 |
| `status-chip/text` | gray/250 | gray/600 |
| `status-chip/icon` | green/400 | green/500 |
| `status-chip/label` | gray/450 | gray/500 |
| `status-chip/dropdown` | gray/250 | gray/400 |

### Avatar — Primary
| Token | Dark | Light |
|-------|------|-------|
| `avatar/primary/default/bg` | green/800 | gray/0 |
| `avatar/primary/default/text` | gray/50 | green/800 |
| `avatar/primary/default/border` | green/300 | gray/0 |
| `avatar/primary/hover/bg` | green/700 | green/100 |
| `avatar/primary/hover/text` | gray/0 | green/900 |
| `avatar/primary/hover/border` | green/200 | green/500 |

### Avatar — Secondary
| Token | Dark | Light |
|-------|------|-------|
| `avatar/secondary/default/bg` | gray/800 | gray/100 |
| `avatar/secondary/default/text` | gray/50 | gray/850 |
| `avatar/secondary/default/border` | gray/350 | gray/400 |
| `avatar/secondary/hover/bg` | gray/750 | gray/200 |
| `avatar/secondary/hover/text` | gray/0 | gray/950 |
| `avatar/secondary/hover/border` | gray/250 | gray/500 |

### Badge
| Token | Dark | Light |
|-------|------|-------|
| `badge/complete/bg` | green/900 | green/50 |
| `badge/complete/text` | green/400 | green/500 |
| `badge/complete/border` | green/700 | green/200 |
| `badge/in-progress/bg` | violet-blue/900 | violet-blue/100 |
| `badge/in-progress/text` | violet-blue/100 | violet-blue/900 |
| `badge/in-progress/border` | violet-blue/500 | violet-blue/500 |

---

## Typography

### Font Families
- **Sora** — Display, headings, labels, numbers
- **DM Sans** — Body text
- **Fragment Mono** — Task update logs / agent activity (now a registered text style: `Mono S`, 13px)
- **Inter** — `Label Italics` only

> These are the **Product UI** faces. The Brand / Marketing system uses a different trio (Playfair Display / Plus Jakarta Sans / IBM Plex Mono) — see [`brand-guidelines.md`](brand-guidelines.md). Never use brand faces in-app or product faces in marketing.

### Text Styles (25 styles, all confirmed via `getLocalTextStylesAsync`)

| Style | Font | Weight | Size | Case | Letter spacing |
|-------|------|--------|------|------|----------------|
| Display XL | Sora | Light (300) | 60 | Original | 0 |
| Display L | Sora | Light (300) | 38 | Original | 0 |
| Display M | Sora | Regular (400) | 28 | Original | 0 |
| Display S | Sora | Light (300) | 20 | Original | 0 |
| Heading L | Sora | Regular (400) | 26 | Original | 0 |
| Heading M | Sora | Regular (400) | 22 | Original | 0 |
| Heading S | Sora | Regular (400) | 20 | Original | 0 |
| Heading XS | Sora | Regular (400) | 18 | Original | 0 |
| Body L | DM Sans | Regular (400) | 18 | Original | 0 |
| Body LB | DM Sans | SemiBold (600) | 18 | Original | 0 |
| Body M | DM Sans | Regular (400) | 16 | Original | 0 |
| Body MB | DM Sans | Bold (700) | 16 | Original | 0 |
| Body S | DM Sans | Regular (400) | 14 | Original | 0 |
| Body XS | DM Sans | Regular (400) | 12 | Original | 0 |
| Mono S | Fragment Mono | Regular (400) | 13 | Original | 0 |
| Label L | Sora | Light (300) | 16 | UPPER | 0 |
| Label M | Sora | Light (300) | 14 | UPPER | 0 |
| Label S | Sora | Light (300) | 10 | UPPER | 0 |
| Label Italics | Inter | Italic | 14 | Original | 0 |
| Number L | Sora | Light (300) | 26 | Original | 0 |
| Number M | Sora | Light (300) | 20 | Original | 0 |
| Number S | Sora | Light (300) | 15 | Original | 0 |
| Number SB | Sora | Medium (500) | 15 | Original | 0 |
| Number XS | Sora | Light (300) | 12 | Original | 0 |
| Number XXS | Sora | Light (300) | 10 | Original | 0 |

All line heights are AUTO. All letter-spacing values measured at 0% (the previously documented Label S 5% tracking is no longer present).

Corrections from previous docs:
- Display XL is **Light**, not Regular
- Display L is **Light**, not Regular
- Label L is **Light**, not the previously listed Light alias — confirmed UPPER text case
- Body LB is **SemiBold (600) at 18**, was previously listed as "prev docs only"
- Heading L/M/S and Display L were "prev docs only" — all confirmed live

---

## Effect & Paint Styles

### Effect Styles
| Name | Type | Spec |
|------|------|------|
| `Light Shadow` | Drop shadow | radius 25, offset (1, 1), color rgba(201, 219, 255, 0.25), spread 0 |

### Paint Styles
| Name | Type |
|------|------|
| `Background Gradient 1` | Gradient |
| `Radial` | Radial gradient |

---

## Component Inventory

> Node IDs verified via the Components page (`12:611`). Always pull metadata for the canvas before re-using IDs — they shift when components are renamed or moved.

### Core Controls
| Component | Node ID | Variants |
|-----------|---------|----------|
| Button | 153:1302 | Primary/Secondary/Danger x Default/Hover/Disabled/Focus x Default/Small/Big |
| Button (Big) — Primary | 3792:7528 | — |
| Button (Big) — Secondary | 3793:7558 | — |
| Button/Icon/Big | 152:890 | Primary/Secondary icon buttons |
| Text Button | 559:7213 | Default/Hover/Focus |
| Link | 2852:5361 | Default/Hover/Focus |
| Toggle | 564:7993 | On/Off + Focus-on/Focus-off |
| Checkbox | 343:1446 | Default/Hover/Disabled/Focus x Selected/Unselected |
| RadioButton | 361:2132 | Default/Hover/Disabled/Focus x Selected/Unselected |
| Search | 312:1610 | Default/Active |
| Segmented Control | 3020:12221 | Classic 3020:12220, Agent 3020:12222 |
| Segment Item | 3020:12203 | Selected/Inactive/Hover/Focus |

### Form Controls
| Component | Node ID | Variants |
|-----------|---------|----------|
| Dropdown | 343:5788 | Empty/Filled x Default/Hover/Disabled/Focus |
| Dropdown Item | 343:1757 | Checkbox/RadioButton type x Default/Hover/Disabled/Focus |
| Dropdown-pill | 341:6204 | Incomplete/Working/Complete x states |
| Filter chip | 343:5807 | Default/Hover/Disabled/Focus |
| RangeSlider | 363:4875 | Full/Small x Default/Disabled |
| Pill | 210:1055 | Default/Hover/Selected/Hover-selected/Focus/Focus-selected (Default 210:1053, Selected 343:5512) |
| Settings Input Field | 3742:6018 | Default/Hover/Focus/Disabled |

### Chat & Messaging
| Component | Node ID | Variants |
|-----------|---------|----------|
| Chat Input | 152:915 | First Chat/Reply x Default/Disabled |
| Chat + Buttons | 310:1564 | Send/Stop x Default/Disabled |
| ChatPanel | 3686:8456 | — |
| ChatPanel/Side/Shell | 235:2619 | Sidebar with chat input |
| Message Bubble | 226:2307 | User/Chatbot x Body/HeaderBody/Title |
| Suggestion Group | 226:2575 | 2/3/4 suggestions |
| Prompt Suggestion | 226:2558 | — |

### Agentic
| Component | Node ID | Variants |
|-----------|---------|----------|
| AgenticCard/Progress | 224:1817 | Expanded/Collapsed x Full/Small |
| AgenticCard/Intake | 363:7126 | Expanded/Collapsed x Full/Small |
| Agentic chat message | 211:13287 | Working/Done |
| Progress indicator | 218:4088 | Done/Working x Collapsed/Expanded x Default/Small |
| Task group | 223:1374 | 0–5 updates |
| Task update | 211:13276 | Default/Found results |
| Status indicator | 207:835 | Loading 1–4, Complete |

### Navigation & Layout
| Component | Node ID | Notes |
|-----------|---------|-------|
| Top Nav | 153:1110 | Logo, icons, avatar |
| Side Nav | 151:751 | Logo, nav icons, avatar |

### Data Display
| Component | Node ID | Notes |
|-----------|---------|-------|
| Table Row | 2968:8836 | State=Default/Alt x Style=Default/Hover/Focus |
| Table Cells — Firm/Website/Contact-Block | 2968:8807 / 2968:8814 / 3516:8590 | Default/Hover/Focus |
| Top-Result-Card | 2852:5389 (set 4039:8695) | Default/Hover/Focus |
| Simple Table Cell | 522:3744 | Default/Header |
| Bullet result | 522:3588 | Firm name with CRD |
| Badge | 538:2584 | Complete/In Progress |
| NotificationRow | 3894:6707 | Default/Hover/Focus |
| Session Card | 3934:11089 | Default/Hover/Focus |
| File Upload | 153:1162 | File name + size (single state — needs Hover/Focus/Disabled, see design debt) |

### Account & Menus
| Component | Node ID | Notes |
|-----------|---------|-------|
| Avatar | 2844:2623 | Primary/Secondary x Default/Hover/Disabled/Focus x Default/Small (Default Primary 151:761) |
| Menu Item | 2576:8512 | Default/Disabled/Focus x All Items/Sign Out x Hover=true/false |
| Account Menu | 2596:8994 | Also 3690:9348 |
| Settings Modal | 3772:11546 | Profile / Security / Notifications tabs |
| Settings Nav Item | 3740:6010 | Active/Inactive/Hover/Focus |
| NotificationPopover | 3941:7769 | — |
| Tooltip | 3905:7568 | — |
| Folder Item | 3632:20574 | Default/Hover/Focus (in Nav Drawer) |
| Chat Item | 3632:20605 | Default/Hover/Focus (in Nav Drawer) |
| Timeline Row | 109:985 | — |
| Export Modal | 3548:8791 | — |

### Icons
23+ icons at 16px and 24px sizes — see canonical Components page (`12:611`) under the icons section, plus the dedicated Icons page (`12:610`).

---

## Focus State Pattern (added 2026-05-13)

**Universal focus ring:** every interactive component's Focus variant uses a 1px stroke bound to `border/tertiary` (gray/50 in dark, gray/1000 in light — i.e. white-on-dark, black-on-light), `strokeAlign: INSIDE`.

This pattern applies to all keyboard-focusable elements. Component-scoped focus tokens (e.g. `button/primary/border-focus`, `dropdown/border-focus`) exist for components that need to deviate from the default — but the default ring should be used everywhere else, including on components that don't have their own focus tokens.

**Per-component focus sources** (where they exist):
- `button/{primary,secondary,danger}/border-focus`
- `checkbox/border-focus`, `checkbox/selected-border-focus`
- `radio/border-focus`, `radio/selected-border-focus`
- `dropdown/border-focus`
- `dropdown-pill/{incomplete,working,completed}/border-focus`
- `filter-chip/border-focus`

**No new focus tokens were created during the 2026-05-13 audit.** The 17 components without their own focus tokens (Pill, Toggle, Segment Item, Folder Item, Chat Item, Firm Cell, Website Cell, Contact Block, NotificationRow, Session Card, Top-Result-Card, Table Row, Menu Item, Avatar, Text Button, Link, Settings Nav Item) all bind directly to `border/tertiary`.

**Exempt from focus rings:** display-only components (Tooltip, Badge, Timestamp, Status indicator, Progress indicator, Agentic Cards, Message Bubble), and non-keyboard-focusable elements (RangeSlider — thumb-level focus is an outstanding design debt item, not a component-level ring).

---

## Layout Patterns

### Two-layout system
1. **Full-screen chat** (InitialChat, AgenticChat): Side Nav (72–77px) + centered content (1000px max-width)
2. **Split panel** (RecoFirms, Workspace, Firm Detail): Top Nav (72px height) + ChatPanel (423px) + Content area (remaining)

### Navigation rules
- Side Nav: Full-screen chat views only (72–77px wide, vertical)
- Top Nav: Split-panel views only (1440px wide, 72px tall)
- Never appear together on the same screen

### Design decisions
- All buttons are ghost/outline by default (transparent bg, colored border) — Primary, Secondary, and now Danger
- Brand green (#18dd65) used for accent, active states, and AI-executed actions
- Success green (#2eff7d) used for completion states and positive feedback
- Violet-blue (#4b4efb / #130c3d) reserved for in-progress badges
- Orange-error (#ff4520) reserved for danger and error states (text/error, border/error, button/danger)

---

## Audit Notes (2026-07-08)

- **Live Figma re-pull (Base + Semantic + text styles) to answer "is the dev repo current?"** Base is unchanged at 60 primitives (no `blue` scale — that was never a Figma variable). Semantic is **232** and text styles **25** after this pass.
- **`brand/black` retargeted** gray/1000 (#000000) → gray/900 (#1c1c1c). Confirmed intentional (softer brand black).
- **`brand/dark teal` deleted** — a raw `#113535` (Brand Deep Teal) token had been added to the Product Semantic collection but was bound to **zero nodes** across all 9 pages (~23k nodes scanned). Confirmed marketing-only and removed from Figma (Semantic 233 → 232). Deep Teal lives in the brand system.
- **`Mono S` text style added** — Fragment Mono 13px; Fragment Mono is now a registered style rather than an unregistered in-screen face.
- **Downstream sync:** the `puremath-ai/chatbot-design` dev repo (`design-updates` branch) was brought current in the same pass — fixed two stale values it carried (`border/card` Dark `#8c8c8c`→`#6e6e6e`, `surface/table-row` Light `#ffffff`→`#f5f5f5`), removed its stale `blue/*` scale, and added `Mono S` + `Number XXS`. This canonical doc and the prototype CSS already had the correct `border/card`/`table-row` values; only the repo had drifted on those.
- **Not yet reflected in prototype CSS:** `~/advpulse/prototype/src/index.css` (last synced 2026-05-13) still has `brand/black` #000000 and lacks `brand/dark teal`. Re-run `/sync-tokens` when convenient — deferred pending the `brand/dark teal` decision.

## Audit Notes (2026-05-13)

- **Three-way drift audit (Figma ↔ design-system.md ↔ prototype CSS):** confirmed Figma and this doc agree on **every** Base primitive, Semantic token, and text style (0 drift across 292 variables + 24 text styles).
- **Prototype CSS regenerated via /sync-tokens:** `~/advpulse/prototype/src/index.css` now mirrors Figma 1:1 — all 60 Base primitives + all 232 Semantic tokens in both Dark (`:root` default) and Light (`.theme-light` class) modes. Semantic tokens are `var(--base-primitive)` aliases rather than resolved hex, so a single Base edit cascades. Prior CSS was generated 2026-04-30, contained one wrong value (`--border-card: #8c8c8c`, should be `#6e6e6e`), and was missing ~80 tokens (all input/*, button focus/disabled/hover states, danger, light mode, etc.). All fixed.
- **Component code note:** `TopResultCard.tsx` has stale fallback values `var(--border-card, #8c8c8c)` in two places (lines 71, 146 at time of audit). Resolved CSS value is now correct (#6e6e6e), so visual output is fine, but the in-code fallbacks drifted from Figma. Other prototype files use the correct fallback `#6e6e6e`. Cleanup item.
- **Focus state coverage expanded:** added 24 Focus variants across 14 components that previously had no Focus state (Pill, Toggle, Segment Item, Folder Item, Chat Item, Firm Cell, Website Cell, Contact Block, NotificationRow, Session Card, Top-Result-Card, Table Row, Menu Item, Avatar, Text Button, Link, Settings Nav Item). All bound to existing `border/tertiary` at 1px INSIDE. See Focus State Pattern section above.
- **Responsive sizing fixes:** 14 components updated so instances stretch to fill their auto-layout parents — Top Nav, Settings Sections (Profile/Notifications/Security), Settings Avatar Row, Settings Nav Item, Settings Input Field, Session Card, Dropdown Item, DropdownList (SearchSelect + Select), Pill Side Scroll, Range Display, RangeSlider Full. Variants inside component sets received `layoutSizingHorizontal = FILL`; standalone components received `layoutAlign = STRETCH` (top-level components can't take FILL directly).
- **No new tokens added** — all new variants reuse existing `border/tertiary` for the focus ring.
- **RangeSlider** Focus variant intentionally NOT added at the component level — keyboard focus belongs on the thumb element, not a frame ring. Tracked as design debt.
- **Singleton components without state variants** (File Upload, Prompt Suggestion, List Item) skipped — adding Focus requires converting to a component set with full state matrix; tracked as design debt.

## Audit Notes (2026-05-01)

- **Two collections only**: `Base` and `Semantic`. No separate Typography collection — type is registered as Figma text styles, not variables.
- **Light mode is fully defined** in Semantic (every variable has a value for both Dark and Light modes). Screens are still built only in Dark mode; verify Light-mode visuals before shipping a light theme.
- **Spacing semantic tokens live in the Semantic collection** (aliased to `space/*` primitives in Base), not in Base directly.
- **Net new since 2026-04-06**: orange-error and violet-blue Base scales; `0-alpha/transparent`; `space/64,72,80`; `radius/none`; `stroke/m,l,xl`; full `button/danger/*`, `interactive/*`, `input/*` token sets; expanded surface, text, border, icon, divider, avatar groups; `spacing/hero-spacing`; 7 new text styles (Label M, Label Italics, Number L/M/SB/XS/XXS).
- **Removed/renamed**: `color/blue/{50,500}` no longer exist as Base primitives (replaced by violet-blue scale). The previous `divider/default` value (#484848 → gray/700) is unchanged but the resolved hex stays consistent.
- **Text-style corrections**: Display XL and Display L are Sora **Light**, not Regular. Label S has 0% letter-spacing, not 5%.
- All Semantic tokens are scoped `ALL_SCOPES`. All Base spacing is scoped `GAP`, radius `CORNER_RADIUS`, stroke `STROKE_FLOAT`.
