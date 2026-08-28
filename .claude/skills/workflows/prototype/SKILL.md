---
name: prototype
description: "Build or extend a running prototype from a design — React, Shopify theme, static site, artifact, or print. Use when the user says /prototype, 'build a prototype', 'make this clickable', 'add a screen', 'ship this as an artifact', or any request to turn a design into something that runs. Reads the target stack from the project's prototype.json; never assumes React."
---

# Prototype Workflow

Triggered when the user asks to build or extend a running artifact from a design.

**Read this first, every time:** if you are translating an existing design and the code you are about to write is not a translation of `get_design_context` output with token-name and asset substitutions only, stop. You are about to drift.

That rule has one legitimate exception, and it is not a loophole: some work is genuinely designed in code (see **Direction of flow**). Say which mode you are in before you start.

---

## Prerequisites

1. **`projects/<name>/prototype.json`** exists and declares `stack` and `hostProjectPath`. If missing, ask where the host project lives or whether one needs scaffolding. Do not improvise a stack.
2. **The host project runs.** Start it once before building anything. Never build on a broken host.
3. **`design-system.md` and `figma.json`** exist, when the source is Figma.

---

## Direction of flow — decide it out loud, first

| Mode | When | What it means |
|---|---|---|
| **Figma leads** | The design exists and is settled | Faithful translation. The pipeline below, in order. |
| **Prototype leads** | The question cannot be answered by a static frame — streaming, progressive results, dense interaction, real data volume, timing | You design in code. Figma follows afterward and the two get reconciled. |
| **Authoring** | The user explicitly asks you to invent a component, copy, or data | Say in one sentence that you are authoring. Return to translation afterward. |

**Prototype-first is legitimate.** What is forbidden is *silent* invention while claiming to translate. When the prototype leads, record it in `design-state.md` and say what Figma still owes.

---

## Stacks

Read `stack` from `prototype.json`. The pipeline below is written for design-to-code translation; the shape holds across stacks, the mechanics differ.

- **`react-vite`** — Components in the project's component directory, screens/routes in its screen directory, tokens in its CSS layer.
- **`shopify-liquid`** — Sections and snippets against a real theme. Check the CLI's supported Node version first; a mismatch surfaces as unrelated-looking network errors.
- **`static-site`** — Marketing or docs. Usually its own type system even when it shares a token layer.
- **`artifact`** — A single self-contained page, for people who will not run a dev server. External requests are blocked, so inline everything. This is a **sanctioned** output, not a violation of the no-standalone-HTML rule, because it is a distribution format rather than a substitute for a host project.
- **`print`** — Bleed, trim, dieline, and color space are correctness, not polish.

---

## Process — one screen at a time, no batching

**Halt after each screen for visual review.** The common failure is racing through screens 2 to N after screen 1 worked.

### Step 0 — Pre-flight (once per session)

1. Read `design-system.md`, `figma.json`, `prototype.json`.
2. Read the existing prototype. **List the components that already exist. You will not recreate them.**
3. Re-read the project's feedback and correction notes. Re-read them again after every correction in this session.

**Frame inventory — pull live, never from markdown.** Design files are the only source of truth for what exists and its current IDs. Call `get_metadata` on the screens page, then **ask which frames are in scope** — the MCP server cannot see the user's selection in the app. Accept frame names, URLs, or node IDs. Confirm the resolved list before proceeding.

**Readiness audit — the most important pre-flight step.** The MCP returns clean output only when the source file is structurally sound. When it is not, it falls back to absolute positioning and raw hex, which is exactly what breaks prototypes downstream.

For every target node, check: auto layout end to end · real components rather than detached groups · fills, strokes, text, spacing and radii bound to variables · semantic layer names. Produce a report listing each issue and its specific fix, then **halt**. The user says "fix all", "fix these", "I'll do it myself", or "skip it". Once they say fix-all, execute without pausing per item.

### Step 1 — Canonical components before screens

For each component the screen uses, pull the **canonical component** from the design system — not the instance on the screen. A screen instance shows one variant; the canonical shows all of them.

Build missing components first, one at a time, and diff each against its canonical screenshot before moving on.

### Step 2 — The screen

Translate the frame. Preserve a header comment naming the source node and the date it was pulled. Preserve whatever traceability attributes the MCP returns — they are the audit trail the drift check reads.

### Step 3 — Diff

Render it, screenshot the source, compare side by side. Widths match. Text matches exactly. Components trace to canonical. Colors and spacing bound to tokens.

**Do not trust your own visual self-evaluation.** Show both to the user and let them call drift.

### Step 4 — Halt

Wait for approval. Do not start the next screen. If drift is reported, fix it in place before moving on.

### Step 5 — Wire interactions

Only after every screen in the flow is approved. Routing, then handlers, then states — and states only where the design specifies them.

### Step 6 — Instrument for review

Add the annotation mode described in the `design-feedback` workflow, so the user can point rather than describe. Do this before sharing, not after the first round of notes.

---

## What this workflow must not do

- **Invent silently.** Name the mode.
- Rewrite exports for cleaner architecture. Cleanup is a separate task, after parity.
- Add responsiveness the design does not specify. A fixed-width canvas becomes a fixed-width prototype.
- Invent visual treatments — divider colors, badge palettes, hover behaviors — that are not in the design.
- Pause for permission on directives already given. Yes/no questions are for genuine forks.

---

## The drift check

`hooks/prototype-drift-check.sh` runs after writes to the paths listed in `prototype.json`'s `verbatimPaths`. It checks for source-node traceability, a header comment, and raw values outside the token pattern.

It is a guardrail on the **translation** path. If the project is legitimately prototype-first, declare that in `prototype.json` (`"mode": "prototype-first"`) rather than working around the hook — an unenforced rule and a silently bypassed rule are the same thing.

---

## Output

- A running artifact, verified in a browser before being reported as working
- Components tracing to the design system, with anything authored clearly flagged
- Routing matching the described flow
- A `design-state.md` entry for any decision the prototype made that the design file does not yet reflect
