# Design Memory: A Schema for Cross-Project Taste

> A pattern for capturing a designer's aesthetic identity in a way that persists across projects and is readable by AI agents.

---

## The problem

When you work across multiple projects — whether as a consultant, an in-house designer on many products, or an AI agent supporting a designer — you hit a version of the same problem every time:

**Taste resets to zero at the start of each project.**

Every new brief starts with "what's our aesthetic going to be?" — as if the designer's preferences were a blank slate. In reality, every designer has strong opinions that should carry forward (I always prefer restrained accent colors), soft preferences that might apply (I often like glass UI, but not on data-heavy products), and hard anti-patterns they've already rejected (I never use uniform small sizing — size IS hierarchy).

Without a shared representation of that identity, designers re-explain themselves every project. Worse, AI agents generate output that drifts toward generic "good design" instead of the specific judgment the designer has built up over years.

Design memory is the fix: a single file, in the designer's home base, that captures their aesthetic identity in a way that agents can load, apply, and update.

---

## The schema

Design memory has three layers, each with a different commitment level:

```
Strong Opinions          → Constraints. Apply everywhere unless explicitly overridden.
Soft Patterns            → Suggestions. Apply when relevant, skip when the project doesn't fit.
Anti-Patterns            → Exclusions. Never do these unless the designer explicitly overrides.
```

Plus:

- **Aesthetic Identity** — the designer's overall visual language, interaction style, and content voice in 2–3 paragraphs
- **Visual References** — a curated library of reference screens with specific takeaways (what to borrow, what to leave)
- **Project History** — one entry per completed project, capturing what was learned and what moved up into Strong Opinions

The full template is at `templates/design-memory.md` in this repo; an instantiated example is at `taste-profile.md` at the root.

---

## Why three layers

The three-layer structure resolves a tension that a flat list can't: **not every preference should have equal authority**.

- If you put "glass UI" in a flat list and an agent sees it, the agent applies it to your next project — including a data-heavy dashboard where it doesn't fit.
- If you leave it out entirely, the agent doesn't know you have this preference at all.

The three-layer schema forces you to decide, for every preference: is this something that should always apply, or something that should apply when it fits? This decision itself is useful — it clarifies your own taste.

| Layer | Commitment | Example |
|---|---|---|
| **Strong Opinions** | Always apply | "Ghost/outline buttons as default; filled reserved for single primary action" |
| **Soft Patterns** | Apply when it fits | "Glass/frosted UI — good for utility elements, not data-heavy products" |
| **Anti-Patterns** | Never apply | "No multi-color chart palettes on dark backgrounds — stay monochrome, differentiate by pattern" |

---

## What each layer should contain

### Strong Opinions

**Definition:** Preferences confirmed across multiple projects, or preferences the designer considers non-negotiable regardless of brief.

**Test:** If someone handed you a brief that asked for the opposite, would you push back on the brief or follow it? If you'd push back, it's a Strong Opinion.

**Format:** Single sentence, specific enough that an agent could act on it without further clarification.

**Good:**
- "Mixed column layouts where content determines proportions — never rigid 50/50 grids"
- "Restrained accent color (~5–10% of surface) doing focused semantic work — one accent, not many"

**Bad:**
- "Good typography" (not specific)
- "Spacing should feel balanced" (subjective without a rule)

### Soft Patterns

**Definition:** Preferences that appeared in one project, or that the designer applies when the context fits but doesn't consider universal.

**Test:** Would you apply this to every project without thinking? If no, it's a Soft Pattern.

**Format:** Rule plus context — under what conditions it applies, and under what conditions it doesn't.

**Good:**
- "Three-panel layouts (nav / content / configuration) — good for complex configuration-heavy tools, not for casual consumer apps"
- "Inline data chips over vertical label-value stacking — when information density is a goal, not when the screen has room to breathe"

### Anti-Patterns

**Definition:** Things the designer has explicitly rejected — either because they've been burned by them before, or because they contradict the designer's visual identity.

**Test:** If you saw an agent output this, would you ask them to redo the work?

**Format:** What to avoid, and specifically why.

**Good:**
- "Extreme type ratio jumps (28px heading with 11px subtitle) — hierarchy should feel musical, not jarring"
- "Labeling what the layout already communicates ('Name: Margherita pizza' when it's the heading) — redundancy is noise"

---

## How to populate it

You don't start design memory from scratch. You seed it from existing work.

**Step 1: Review 3–5 recent projects.** For each one, extract:
- Design decisions that felt obvious to you but might surprise someone else
- Rules you applied without being asked
- Critiques you gave that kept coming up
- Things you explicitly rejected in review

**Step 2: Categorize.** For each extracted preference, decide: Strong / Soft / Anti.

**Step 3: Write it in the schema.** Use the template at `templates/design-memory.md`. Keep each entry to one sentence where possible.

**Step 4: Add reference screens.** Screenshot 5–10 designs you admire (from other products, not your own). For each, annotate what specifically resonates — not "it's clean," but "the 8px gutters between cards" or "the monospace on tabular data."

**Step 5: Audit against upcoming projects.** Apply the memory to your next project. Anything that breaks or needs to be overridden gets re-classified or demoted.

---

## How agents consume design memory

The framework loads design memory at session start (see `hooks/session-init.sh`). Agents then apply it with this priority order:

1. **Explicit direction from the designer in this session** — always overrides everything below
2. **Project taste profile** (`projects/<name>/taste-profile.md`) — the primary source for project-specific aesthetics
3. **Cross-project Strong Opinions** — carry forward unless the project explicitly overrides
4. **Cross-project Soft Patterns** — apply when the project fits, skip when it doesn't
5. **Cross-project Anti-Patterns** — always respect as exclusions unless the designer overrides in session

This priority order is the critical part. Without it, agents either ignore cross-project memory or apply it too aggressively to a new project where it doesn't fit.

---

## How design memory evolves

Design memory isn't a one-time document. The `/retro` workflow updates it at project end. After each project, consider:

- **What worked?** Taste signals that produced good output — candidates to promote from Soft Pattern to Strong Opinion.
- **What didn't?** Taste signals that needed correction — candidates to demote from Strong Opinion to Soft Pattern, or to add as Anti-Patterns.
- **What's new?** Preferences you discovered mid-project that weren't in memory before.

Keep a `Project History` section with one entry per completed project. Each entry lists:
- Emotional target (what the project aimed for)
- Key taste decisions made
- What worked / what didn't
- What was carried forward into Strong Opinions or Anti-Patterns

Over time, this history becomes a record of how your taste has evolved — useful in its own right, and honest about the fact that taste isn't static.

---

## When design memory and the design system conflict

Sometimes the taste profile implies something the project's design system tokens don't support. When this happens:

1. **Don't silently compromise.** Flag the conflict.
2. **Don't break the design system.** Tokens exist for consistency across the product.
3. **Present the tension.** "The taste profile suggests tighter spacing than the token scale allows. Should we use the nearest existing token, or add a new one?"
4. **Record the resolution** in `design-state.md` for the project.

This is a feature, not a bug. The conflict itself surfaces a design question worth discussing — and forces a deliberate choice instead of drift.

---

## Why this pattern matters for AI-assisted design

Without design memory, AI design agents default to "AI-aesthetic" — rounded corners, purple gradients, generic good-taste output. This is the distinctive failure mode of LLM-generated UI: it looks plausible, but it doesn't look like any particular designer.

Design memory fixes this by making the designer's specific judgment legible to the agent. "Prefer ghost buttons over filled" doesn't sound like a strong rule — but when an agent applies it consistently across ten screens, the output stops looking generic and starts looking like the designer's work.

The pattern also makes collaboration more honest. When an AI agent does something you don't like, you can ask: "Is this an Anti-Pattern I haven't written down yet?" Most of the time, it is. The correction goes into memory, and the next project is better.

---

## Adopting the pattern

If you're not using this framework but want to adopt design memory for your own work:

1. **Create a single file** at your home base — `~/design-memory.md`, or similar. Don't scatter it across projects.
2. **Use the schema** — Aesthetic Identity / Strong Opinions / Soft Patterns / Anti-Patterns / Visual References / Project History.
3. **Seed from 3–5 recent projects** — don't try to write it from scratch.
4. **Keep entries specific and actionable** — single sentences, testable rules.
5. **Re-read it at the start of each project** — the act of reading reinforces your own identity.
6. **Update it after each project** — promote, demote, or add entries based on what you learned.

If you're using AI agents to assist your design work, point them at the file. If they're any good, they'll apply it. If they're not, you'll learn quickly that your design memory is more valuable than their generic taste.

---

## Example

A lightly abbreviated example of the pattern in use — the canonical version of this file sits at `taste-profile.md` in this repo.

```markdown
# Design Memory — [Designer]

## Aesthetic Identity

### Visual Language
Soft material quality with structural precision. Rounded containers, generous radius,
glass/frosted treatments on utility elements. Dense information organized through panel
separation and strong type hierarchy — not through whitespace reduction. Data-forward:
numbers and metrics are the visual design, not decoration around them.

## Strong Opinions
- Mixed column layouts where content determines proportions — never rigid 50/50 grids
- Type hierarchy is the primary organizational tool: big numbers, small uppercase labels
- Restrained accent color (~5-10% of surface) doing focused semantic work — one accent, not many
- Ghost/outline buttons as default; filled button reserved for single primary action
- Action buttons at the END of content flow, not the top

## Soft Patterns
- Glass/frosted/neumorphic UI — good for utility elements, not broadly on data-heavy products
- Inline data chips over vertical label-value stacking — when density is a goal
- Three-panel layouts — for complex configuration-heavy tools

## Anti-Patterns
- Uniform small sizing that treats all elements as equal — size IS hierarchy
- Labeling what the layout already communicates
- Multi-color chart palettes on dark backgrounds — stay monochrome, differentiate by pattern
- Bordering non-interactive metadata — icon + text inline reads better than boxed

## Project History

### [Project Name] — [Date]
- **Emotional target:** [What the project aimed for]
- **Key taste decisions:** [Major aesthetic choices]
- **What worked:** [Taste signals that produced good output]
- **What didn't:** [Taste signals that needed correction]
- **Carried forward:** [What moved into Strong Opinions or Anti-Patterns]
```

The whole file should fit in ~150 lines. If it's longer than that, it's probably turning into a design system spec instead of a memory.
