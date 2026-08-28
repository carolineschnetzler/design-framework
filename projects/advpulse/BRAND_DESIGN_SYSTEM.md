# AdvPulse Brand Design System
## For Claude Code / devs: follow these rules exactly when generating marketing / brand surfaces.

**Companion file:** `brand-tokens.json` contains the tokens below (colors, typography, logo) in machine-readable format.

> ⚠️ **This is the BRAND / MARKETING system — not the Product UI.** It governs the logo, marketing website, pitch deck, social, print, and lifecycle email. The in-app product uses a **completely separate** system (`DESIGN_SYSTEM.md` / `design-tokens.json`: Sora / DM Sans / Fragment Mono on a dark token foundation). **Never mix them.** The only value the two systems share is the green — brand **Pulse `#18DD65`** = product `color/green/500`. When a product screenshot appears inside a marketing surface, the screenshot keeps Product UI styling and the frame around it uses Brand styling.

---

## Brand Identity

AdvPulse gives the teams who sell to financial advisors a faster, clearer way to find the right firms, built on public SEC filings. The brand voice is editorial and confident: a restrained serif signature over a clean grotesque sans, high contrast, generous space. Light-ground (Paper) by default; Deep Teal for dark grounds.

---

## Color

Five colors, fixed roles. **Pulse is the signal — used sparingly, one thing at a time.** Deep Teal is the branded dark ground. Ink carries neutral text and UI. Mist is the muted accent. Paper is the light ground.

| Name | Hex | RGB | Role |
|------|-----|-----|------|
| **Pulse** | `#18DD65` | 24, 221, 101 | Signal / accent — used sparingly, one thing at a time |
| **Deep Teal** | `#113535` | 17, 53, 53 | Branded dark ground |
| **Ink** | `#1C1C1C` | 28, 28, 28 | Neutral text and UI |
| **Mist** | `#7C8D8D` | 124, 141, 141 | Muted accent |
| **Paper** | `#FAFAFA` | 250, 250, 250 | Light ground (default) |

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
| **Plus Jakarta Sans** (sans) | Headlines (H2) · Section titles · Subhead · Body · UI | The workhorse — carries every heading below the hero, plus all body and UI. At display sizes, use SemiBold with tight negative tracking so it reads as intentional. |
| **IBM Plex Mono** (mono) | Labels · Buttons · Links · Data | **Always uppercase**, positive tracking (+0.04em), so it reads as intentional. |

### Type scale

A **1.25 scale off a 16px base**. Headings sit tight; body runs loose at 1.6 line height. Playfair appears only at the Hero row, and at most once per surface; every other level is Plus Jakarta Sans.

| Level | Face | Weight | Size / line height | Tracking | Case |
|-------|------|--------|--------------------|----------|------|
| Hero (H1) | Playfair Display *(or Plus Jakarta Sans)* | 400 / 600 | 60 / 1.1 | −0.01em | Original |
| Headline (H2) | Plus Jakarta Sans | SemiBold 600 | 39 / 1.1 | −0.02em | Original |
| Section title (H3) | Plus Jakarta Sans | Bold 700 | 31 / 1.2 | −0.01em | Original |
| Subsection (H4) | Plus Jakarta Sans | SemiBold 600 | 25 / 1.25 | 0 | Original |
| Body | Plus Jakarta Sans | Regular 400 | 16 / 1.6 | 0 | Original |
| Label / button / link | IBM Plex Mono | Medium 500 | 14 | +0.04em | UPPERCASE |

### Typography rules
- **Playfair is a signature, not a workhorse.** One Playfair line per surface, at the hero only. Everything else is Plus Jakarta Sans.
- **Mono is always uppercase** with +0.04em tracking. Use it for labels, buttons, links, and data — never for prose.
- **Don't substitute faces.** No system-font fallbacks in mockups (email is the one exception — serif falls back to Georgia in table-based, Outlook-safe templates).

---

## Logo Suite

Three lockups, drawn from the orbital-globe mark.

| Lockup | When to use | Min size / clear space |
|--------|-------------|------------------------|
| **Primary** (horizontal wordmark) | Default — website header, decks, signage, wide formats | Clear space on all sides = height of the globe |
| **Secondary** (stacked) | Square / vertical spaces where the horizontal wordmark is too wide — social tiles, app stores, narrow columns | — |
| **Brandmark** (globe alone) | Where the name is established or space is tight — favicon, app icon, social avatar | **24px min** digital; below that the orbital lines fill in |

### Avatar / social sizing
- Pulse-on-Deep-Teal or Paper-on-Ink circular brandmark.
- Instagram 180×180 · YouTube 250×250 · Facebook 180×180 · X 400×400.

### Logo colorways & misuse
Colorways: Pulse on Deep Teal · Paper on Ink · Ink on Paper. **Never** set the logo in these failing combinations:
- Pulse on Paper · Paper on Pulse (neon and white never sit on each other)
- Deep Teal on Ink · Ink on Deep Teal (the two darks never sit together)

---

## Anti-Patterns (Never Do These)

- **Don't use the Product UI type system here** (Sora / DM Sans / Fragment Mono). That's the app, not the brand.
- **Don't reach for product tokens** (gray/green/violet-blue scales, dark-mode surfaces). The brand palette is the five roles above.
- **Don't splash Pulse.** It's a signal, one thing at a time.
- **Don't pair the two darks** (Deep Teal + Ink) or put small Pulse text on Paper.
- **Don't set Playfair below the hero.** If it repeats, it's wrong — use Plus Jakarta Sans.

---

## Where This Lives

- **Marketing website** — separate Figma file `Wwv8gQNkgQ92jSh6zspH8q` ("AdvPulse Website / design"). Editorial high-contrast serif display + grotesque sans body, glowing 3D wireframe sculptures, green→white gradient hero. The brand system at full editorial expression.
- **Welcome / lifecycle email** — `~/advpulse/email/welcome-email/` (hand-coded, table-based, Outlook-safe; serif → Georgia fallback).
- **API documentation site** — `~/advpulse/api-docs/` (brand-system styling).
- **Partner "Platform Preview"** — composite in the product Figma file (`kFyd7XSbESiizgbP6u8jAF`, page "Marketing — Platform Preview") — a deliberate cross-system artifact (Product screenshots in a brand frame).
- **Pitch deck** — separate file, separate token systems.

---

> **Status:** Local staging copy (2026-07-08). Not yet pushed to a repo. The brand system's dev-token home should be the marketing/website codebase, **not** the `chatbot-design` product app repo — co-locating brand tokens with product code invites exactly the cross-system mixing this doc warns against.
