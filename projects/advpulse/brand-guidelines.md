# Brand Guidelines — AdvPulse (Marketing)

> System: **Brand / Marketing** — external-facing identity (logo, website, pitch, social, print, email)
> Last updated: 2026-07-07 (typography: Playfair reserved to a single hero moment; Plus Jakarta Sans now carries H2 and below)
> Source: AdvPulse Brand & Style Guide (`~/Downloads/AdvPulse_Brand_Style_Guide.html`, 16pp, "Caroline Avery Design", 2026)

---

## Two Systems — Read First

AdvPulse runs on **two distinct design systems** with different jobs. Do not mix them.

| | **Brand / Marketing** (this doc) | **Product UI** (`design-system.md`) |
|---|---|---|
| **Governs** | Logo, marketing website, pitch deck, social, print, partner marketing, lifecycle email | The AdvPulse application (every in-app screen) |
| **Type** | Playfair Display · Plus Jakarta Sans · IBM Plex Mono | Sora · DM Sans · Fragment Mono |
| **Color** | Pulse / Deep Teal / Ink / Mist / Paper (5 fixed roles) | Token system: gray/green/orange-error/violet-blue, Dark + Light modes |
| **Theme** | Light-ground default (Paper), Deep Teal for dark grounds | Dark mode primary, Light mode defined |
| **Source of truth** | This doc + Brand & Style Guide | Figma file `kFyd7XSbESiizgbP6u8jAF` (live tokens) |
| **Tooling** | Hand-built marketing artifacts | Figma variables → `/sync-tokens` → prototype CSS |

**The only shared value** is the green: brand **Pulse `#18DD65`** = product **`color/green/500` (`brand/green`)**. Everything else is intentionally different. When an asset spans both worlds (e.g. a product screenshot inside a marketing page), the screenshot keeps Product UI styling and the surrounding marketing frame uses Brand styling.

---

## Mission & Vision

- **Mission** — AdvPulse exists to give the teams who sell to financial advisors a faster, clearer way to find the right firms, built on public SEC filings and shaped around how salespeople actually work.
- **Vision** — A market where finding the right advisor no longer means hours lost in dated databases. Where prospect research is quick and accurate, drawn straight from regulatory filings, so teams spend their time in conversations instead of spreadsheets.

---

## Color

Five colors, fixed roles. Pulse is the signal — used sparingly, one thing at a time. Deep Teal is the branded dark ground. Ink carries neutral text and UI. Mist is the muted accent. Paper is the light ground.

| Name | Hex | RGB | Role |
|------|-----|-----|------|
| **Pulse** | `#18DD65` | 24, 221, 101 | Signal / accent — used sparingly, one thing at a time |
| **Deep Teal** | `#113535` | 17, 53, 53 | Branded dark ground |
| **Ink** | `#1C1C1C` | 28, 28, 28 | Neutral text and UI |
| **Mist** | `#7C8D8D` | 124, 141, 141 | Muted accent |
| **Paper** | `#FAFAFA` | 250, 250, 250 | Light ground |

Hex and RGB are exact. Derive CMYK per the print profile in use rather than from a fixed conversion, so proofs match the press.

### Color usage rules
- Use high-contrast pairings. As size drops, contrast matters more.
- **Pulse never carries small text on Paper** (fails contrast). Pulse-on-Paper is invalid.
- **The two darks never pair together** — Deep Teal and Ink must not sit on each other.
- Mist on Deep Teal is acceptable only at large sizes; Mist on Paper at small sizes is invalid.
- **Valid pairings:** Pulse on Deep Teal · Paper on Ink · Ink on Pulse · Mist on Deep Teal (large).
- **Invalid pairings:** Pulse on Paper · Paper on Pulse · Deep Teal on Ink · Mist on Paper (small).

---

## Typography

Three faces, three jobs. Do not substitute. **Playfair is used sparingly — the sans carries the system.**

| Face | Role | Notes |
|------|------|-------|
| **Playfair Display** (serif) | Reserved — one signature hero line per surface (H1) | The brand voice, used with restraint. Regular (400). **Not** for section titles, sub-heads, running headings, or repeated labels. When in doubt, set it in Plus Jakarta Sans. |
| **Plus Jakarta Sans** (sans) | Headlines (H2) · Section titles · Subhead · Body · UI | The workhorse — now carries every heading below the hero, plus all body and UI. At display sizes, use SemiBold with tight negative tracking so it reads as intentional. |
| **IBM Plex Mono** (mono) | Labels · Buttons · Links · Data | **Always uppercase**, positive tracking (+0.04em), so it reads as intentional. |

### Type scale
A **1.25 scale off a 16px base**. Headings sit tight; body runs loose at 1.6 line height. Playfair appears only at the Hero row, and at most once per surface; every other level is Plus Jakarta Sans.

| Level | Face | Weight | Size / line height | Tracking |
|-------|------|--------|--------------------|----------|
| Hero (H1) | Playfair Display *(or Plus Jakarta Sans)* | 400 / 600 | 60 / 1.1 | −0.01em |
| Headline (H2) | Plus Jakarta Sans | SemiBold 600 | 39 / 1.1 | −0.02em |
| Section title (H3) | Plus Jakarta Sans | Bold 700 | 31 / 1.2 | −0.01em |
| Subsection (H4) | Plus Jakarta Sans | SemiBold 600 | 25 / 1.25 | 0 |
| Body | Plus Jakarta Sans | Regular 400 | 16 / 1.6 | 0 |
| Label / button / link | IBM Plex Mono | Medium 500 | 14 / +0.04em | UPPERCASE |

---

## Logo Suite

Three lockups, drawn from the orbital-globe mark.

| Lockup | When to use | Min size / clear space |
|--------|-------------|------------------------|
| **Primary** (horizontal wordmark) | Default for most applications — website header, decks, signage, wide formats | Clear space on all sides = height of the globe |
| **Secondary** (stacked) | Square / vertical spaces where the horizontal wordmark is too wide — social tiles, app stores, narrow columns | — |
| **Brandmark** (globe alone) | Where the name is already established or space is tight — favicon, app icon, social avatar | **24px min** digital; below that the orbital lines fill in |

### Avatar / social sizing
- Pulse-on-Deep-Teal or Paper-on-Ink circular brandmark.
- Instagram 180×180 · YouTube 250×250 · Facebook 180×180 · X 400×400.

### Logo color & misuse
Logo colorways: Pulse on Deep Teal, Paper on Ink, Ink on Paper. **Never** set the logo in these failing combinations:
- Pulse on Paper · Paper on Pulse (neon and white never sit on each other)
- Deep Teal on Ink · Ink on Deep Teal (the two darks never sit together)

---

## Where This Lives

- **Marketing website** — separate Figma file `Wwv8gQNkgQ92jSh6zspH8q` ("AdvPulse Website / design"). Editorial high-contrast serif (Playfair-family) display + grotesque sans body, glowing 3D wireframe sculptures, green→white gradient hero. This is the brand system applied at full editorial expression.
- **Welcome / lifecycle email** — `~/advpulse/email/welcome-email/` (hand-coded, table-based, Outlook-safe; serif translated to Georgia fallback).
- **Partner "Platform Preview"** — composite in the product Figma file (`kFyd7XSbESiizgbP6u8jAF`, page "Marketing — Platform Preview"). Note: this one frames real **Product UI** screenshots in a marketing layout — a deliberate cross-system artifact.
- **Pitch deck** — see `puremath-pitch-deck` (separate file, separate token systems).

---

## Relationship to Product UI

The product app deliberately does **not** use the brand type system. In-app screens use Sora / DM Sans / Fragment Mono on a dark token-driven foundation — see `design-system.md`. The brand and product worlds meet only at the green (`#18DD65`) and at the moments where a product screenshot appears inside a marketing surface. Keep the two systems separate by default; converge only with explicit intent.
