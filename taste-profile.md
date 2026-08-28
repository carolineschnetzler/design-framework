# Design Memory

> Cross-project design memory. What belongs to the **designer**, not to any one product.
> Loaded at session start. Updated by `/retro` at project end.
> Last updated: 2026-08-28

**The test for what belongs here:** would this opinion still hold for a different client, a different medium, a different product? If it would change — if it is about dark mode, or a radius scale, or a type family — it belongs in that project's own `taste-profile.md`, not here.

Keep this file small. A bloated cross-project profile stops being read, and starts contradicting itself the moment two projects disagree.

---

## Aesthetic Identity

### Visual Language
Structural precision. Dense information organized through panel separation and strong type hierarchy, not through whitespace reduction. Data-forward: numbers and metrics are the visual design, not decoration around them. Material quality — softness, glass, texture, weight — is a **per-project** decision, not a constant.

### Interaction Style
Fast and understated for direct manipulation. Deliberate transparency for machine operations: show the work through progress logs and step accounting rather than spinners. Responsive without being flashy.

### Content Voice
Professional precision. Not warm, not cold. If the layout communicates meaning, drop the label. Data speaks first, copy supports.

---

## Strong Opinions

Constraints for every project unless the project explicitly overrides them.

- **Type hierarchy is the primary organizational tool** — big numbers, small uppercase labels, dramatic but balanced size contrast
- **One accent, doing focused semantic work** — restrained, roughly 5–10% of surface. Many accents means none.
- **Mixed column layouts where content determines proportions** — never rigid halves
- **Eliminate redundant labels** — if position and style make meaning obvious, the label is noise
- **Dividers and spacing over heavy borders** — do not create boxes inside boxes
- **Do not card-wrap a feed** — notifications, activity, logs. A card around every row is a tell that nobody made a decision.
- **Every section gets a heading and subtitle pair** as minimum organization
- **Action buttons at the end of the content flow**, not the top
- **Data visualization is monochrome** — numbers as hero, minimal chrome, pattern and line style to differentiate rather than a color per series
- **Everything binds to a variable or a text style.** No raw values, ever. If the token does not exist, flag it rather than improvising one.
- **Minimal nesting** — never wrap a frame in a frame, or a text node in a frame, without a layout reason
- **Nothing ships broken.** Content fits its container. Nothing clips, overflows, or overlaps. Verify before moving on.
- **No em dashes in user-facing copy.** Rewrite the sentence rather than substituting another dash.

---

## Soft Patterns

Suggestions. Apply where they fit; drop them without ceremony where they do not.

- Inline data chips (horizontal metric rows) over vertical label-value stacking
- Floating panels for read-mostly supplementary content
- Overlapping elements to save space and show relationship
- Mixed radius by element type, where the project's radius scale allows any radius at all
- Three-panel layouts (nav / content / configuration) for complex views
- Mini gradient sliders for values on a known scale

---

## Anti-Patterns

Exclusions. Respected unless explicitly overridden.

- Fighting natural scan patterns with misplaced elements
- Extreme type ratio jumps — a 28px heading over an 11px subtitle
- Labeling what the layout already communicates
- Bordering non-interactive metadata — icon and text inline reads better than icon and text in a box
- Uniform small sizing that treats every element as equal. Size **is** hierarchy.
- Multi-color chart palettes — especially on dark grounds
- Cramming through compression rather than organizing through structure
- Inventing UI that traces to nothing. Every element comes from the design, or is flagged as authored.

---

## Visual References

Screenshots in `taste-references/`. Each notes what specifically resonates — not "the spacing", but which spacing and why.

### Fashion App Mobile (`fashion-app-mobile.png`)
Single accent on dark. Bold display type mixing weights within one line. Images breaking out of their containers. Pill filters as horizontal scroll.
**Takeaway:** dramatic type hierarchy with one restrained accent; image-forward composition.

### Dark AI Chat (`dark-ai-chat.png`)
Centered input with suggestion cards above. Minimal chrome — the input and the suggestions are the entire UI. History in a left rail.
**Takeaway:** the spacious, focused shape of a conversational entry point.

### Spark Pixel Dashboard (`spark-pixel-dashboard.png`)
Big numbers as hero. Small uppercase labels over large values. Monochrome bars with almost no axis chrome. Sidebar grouped by category.
**Takeaway:** data-forward layout where type hierarchy does all the organizational work.

### Sunset App (`sunset-app.png`)
Giant numeral as the centerpiece. Label/value pairs at dramatic size contrast. No borders, no cards — type on a gradient.
**Takeaway:** number as visual design; atmosphere without chrome.

### Glass UI Concepts (`glass-ui-concepts.png`)
Frosted cards, soft blur, large radius. Inputs that feel embedded rather than bordered. Loose grid of mixed card sizes.
**Takeaway:** the material vocabulary for projects that call for it. Explicitly not a default.

### Firecrawl Overview / Dashboard / Playground (`firecrawl-*.png`)
Hairline rules doing the organizational work instead of card outlines. Grayscale shading creating depth without color. Clear weight on the primary action, everything else receding. Horizontal and vertical layouts coexisting naturally. Input-then-results with minimal decoration.
**Takeaway:** density organized through spacing, type weight, and subtle dividers rather than boxing everything.

---

## Project History

One line each. The detail lives in each project's own taste profile.

- **AdvPulse** (2026, in progress) — dense B2B product UI. Confirmed: accent restraint, type-as-hierarchy, panel separation for density, monospace logs for machine transparency. See `projects/advpulse/taste-profile.md`.
