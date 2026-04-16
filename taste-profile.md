# PureMath Design Memory

> This file persists across all PureMath projects and captures your evolving design identity.
> Updated by the /retro workflow at project end. Loaded at session start.
> Last updated: 2026-04-08 (first taste session, seeded from AdvPulse project)

---

## Aesthetic Identity

### Visual Language
Soft material quality with structural precision. Rounded containers, generous radius, glass/frosted treatments on utility elements. Dense information organized through panel separation and strong type hierarchy — not through whitespace reduction. Data-forward: numbers and metrics are the visual design, not decoration around them.

### Interaction Style
Fast and understated for direct manipulation (100-200ms). Deliberate transparency for AI operations — show the work through progress cards and step-by-step logs. Primary actions use filled treatments; everything else is ghost/outline. The interface should feel responsive without being flashy.

### Content Voice
Professional precision. Not warm, not cold. Clear and concise — if the layout communicates meaning, drop the label. Data speaks first, copy supports.

---

## Strong Opinions

- Mixed column layouts where content determines proportions — never rigid 50/50 grids
- Type hierarchy is the primary organizational tool: big numbers, small uppercase labels, dramatic but balanced size contrast
- Restrained accent color (~5-10% of surface) doing focused semantic work — one accent, not many
- Ghost/outline buttons as default; filled button reserved for single primary action
- Large border radius on containers — soft, rounded
- Every section gets a heading + subtitle pair as minimum organization
- Eliminate redundant labels — if position and style make meaning obvious, drop the label
- Dividers and spacing over heavy borders — don't create boxes inside boxes
- Action buttons at the END of content flow, not the top
- Data visualization: monochrome, minimal chrome, numbers as hero, pattern fills over color fills

---

## Soft Patterns

- Glass/frosted/neumorphic UI as general preference — confirmed for utility elements, but application varies by project (not used broadly on data-heavy products like AdvPulse)
- Inline data chips (horizontal metric rows) over vertical label-value stacking
- Mini gradient sliders for values on a known scale
- Floating panels for read-mostly supplementary content
- Overlapping elements to save space and show relationship (avatar over hero, stacked avatar groups)
- Mixed radius by element type (circles for CTAs, pills for tags, large radius for cards)
- Three-panel layouts (nav / content / configuration) for complex views

---

## Anti-Patterns

- Fighting natural Z-scan patterns with misplaced elements
- Extreme type ratio jumps (28px heading with 11px subtitle)
- Labeling what the layout already communicates ("Name: Margherita pizza" as a label when it's the heading)
- Bordering non-interactive metadata — icon + text inline reads better than icon + text in a box
- Uniform small sizing that treats all elements as equal — size IS hierarchy
- Multi-color chart palettes on dark backgrounds — stay monochrome, use line style and pattern to differentiate
- Cramming content through compression rather than organizing through structure

---

## Visual References

Screenshots saved in `taste-references/`. Each entry notes what specifically resonates.

### Fashion App Mobile (`taste-references/fashion-app-mobile.png`)
- Green accent on dark backgrounds — single accent color doing all the work
- Bold display type with mix of weights (light "Looks" next to bold "Handpicked")
- Overlapping image compositions — photos breaking out of containers
- Pill-shaped category filters as horizontal scroll
- **Takeaway:** Dark theme with restrained green accent, dramatic type hierarchy, image-forward layout

### Dark AI Chat (`taste-references/dark-ai-chat.png`)
- Centered chat input with suggested action cards above
- Dark theme with green accent on interactive elements
- Minimal chrome — the input and prompt suggestions are the entire UI
- Left sidebar for conversation history
- **Takeaway:** AI chat pattern — spacious, focused, dark with green accent. Directly relevant to AdvPulse chat layout

### Spark Pixel Dashboard (`taste-references/spark-pixel-dashboard.png`)
- Big numbers as hero elements in stat cards (TOTAL REVENUE: $20,320)
- Small uppercase labels above large values — dramatic size contrast
- Monochrome bar charts with minimal axis chrome
- Sidebar nav grouped by category (Main Menu, Customers, Management, Settings)
- **Takeaway:** Data-forward dashboard where numbers ARE the design. Type hierarchy does all the organizational work

### Sunset App (`taste-references/sunset-app.png`)
- Warm gradient background with data overlaid directly
- Giant time display (7:44) as the centerpiece — number as hero
- Small uppercase labels ("TIME TO DESTINATION", "SUNSET CONDITIONS") with larger values below
- Minimal UI — no borders, no cards, just type on gradient
- **Takeaway:** Numbers as visual design, label/value pairs with dramatic size contrast, atmospheric color

### Glass UI Concepts (`taste-references/glass-ui-concepts.png`)
- Frosted glass cards with soft blur and rounded corners
- Warm gradient accents (amber/orange organic shapes)
- Login form with glass treatment — inputs feel embedded, not bordered
- Mixed card sizes in a loose grid — not rigid columns
- **Takeaway:** Glass/frosted/neumorphic treatment on utility elements, large radius, warm accent tones

### Firecrawl Overview (`taste-references/firecrawl-overview.png`)
- Endpoint cards in a horizontal row — icon + title + description, outlined not filled
- Usage chart (scraped pages) with soft orange fill, no grid lines
- API Key and MCP Integration sections as simple text blocks — not over-designed
- **Takeaway:** Developer dashboard that mixes data viz, code blocks, and cards without overcomplicating any of them

### Firecrawl Dashboard (`taste-references/firecrawl-dashboard.png`)
- Subtle dividers for layout — hairline rules doing the organizational work, not heavy borders or card outlines
- Grayscale shading — multiple shades of gray creating depth and hierarchy without color
- CTA importance — clear visual weight on primary actions, everything else recedes
- Mixed horizontal and vertical layouts — integrations grid is horizontal icon rows, example projects stack vertically, both coexist naturally
- **Takeaway:** Dense content organized through spacing, type weight, and subtle dividers rather than boxing everything

### Firecrawl Playground (`taste-references/firecrawl-playground.png`)
- Clean form layout — URL input, format selector, action button in a single row
- Results displayed as structured metadata (Endpoint, Status) then rendered content below
- Tab switching between Markdown / JSON views
- **Takeaway:** Input-then-results pattern with minimal decoration — the content IS the interface

---

## Project History

### AdvPulse — In progress (2026)
- **Emotional target:** Data-forward, structurally precise, professional without being corporate
- **Key taste decisions:** Dark theme with layered surfaces, ghost buttons, brand green as single accent at ~10%, Sora + DM Sans type system, two-layout system (spacious chat vs. dense split-panel)
- **What worked:** Strong type hierarchy with Sora for numbers/headings, selective green accent, monospace logs for AI transparency
- **What didn't:** TBD — project in progress
- **Carried forward:** Accent restraint, type-as-hierarchy, panel separation for density management → all moved to strong opinions
