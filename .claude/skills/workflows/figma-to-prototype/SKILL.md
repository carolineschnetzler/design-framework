---
name: figma-to-prototype
description: "Build or extend a working code prototype from Figma frames using a strict verbatim-paste pipeline. Use when the user says /figma-to-prototype, 'build a prototype', 'make this Figma flow clickable', 'add a screen to the prototype', or any request to translate Figma frames into a runnable React prototype. Does NOT generate standalone HTML — requires a host React project."
---

# Figma → Prototype Workflow

Triggered when the user asks to build or extend an interactive code prototype from Figma frames.

**Read this first, every time, before doing anything:** If the JSX you're about to write is not a paste of `mcp__figma__get_design_context` output with token-name and asset-tag substitutions only, **stop**. You are about to drift. The framework will catch you via the prototype-drift-check hook, but the right thing is to not need catching.

---

## The non-negotiable rule

**Default mode is verbatim translation. Two narrow substitutions only:**
1. Slash-named CSS vars (`var(--foo/bar)`) → dash-named (`var(--foo-bar)`).
2. `<img src={imgX}/>` from MCP → the project's `<Icon>` / `<Logo>` / asset components.

That is the entire transformation in default mode. No "cleaner architecture." No extracted props. No abstracted layouts. No fluid responsive classes. No invented copy. No hover/focus/disabled states beyond what's in the Figma frame. If a value is missing in MCP output, it is missing in the prototype — flag to the user, do not invent.

---

## Authoring Mode (explicit invocation only)

The default is verbatim translation. **Authoring mode activates only when the user explicitly asks** for invention — examples:

- "Create a new `<NotificationItem>` component, I haven't designed it yet."
- "Fill in realistic mock data for these firm cards."
- "Write smart copy for this empty state."

When in authoring mode:
1. **State explicitly that you are authoring, not translating**, so the user can verify intent. One sentence at the start of the response: *"Authoring [component/copy/data] — this is invented per your request, not pulled from Figma."*
2. Stay close to the project's existing patterns and design system. New components must use the same tokens, layout primitives, and naming conventions as existing ones.
3. After authoring, return to default verbatim mode for any subsequent work in the same session unless the user re-invokes.

When the user is silent on intent, the default is always verbatim. Never switch into authoring mode on your own initiative.

---

## Prerequisites

Before any prototype work, verify:

1. **Active project has a `prototype.json`** at `projects/<name>/prototype.json` pointing at the host React repo path. If missing, stop and ask the user where the host project lives (or whether one needs scaffolding).
2. **Host project exists and runs.** `cd` to the path in `prototype.json`, run `npm run dev` once to confirm. If it doesn't run, fix that first; do not attempt to build screens on a broken host.
3. **Active project has `design-system.md` and `figma.json`.** Without these, the per-screen pipeline can't run.

If any prerequisite is missing, stop and report what's needed. Do not improvise.

---

## Process — One screen at a time, no batching

This is a pipeline, not advice. Run it linearly. **Halt after each screen for user visual review before moving to the next.** The most common failure mode is racing through screens 2–N after screen 1 worked; the cadence rule prevents this.

### Step 0 — Pre-flight (once per session)

**Context loading:**
1. Read `projects/<name>/design-system.md`, `projects/<name>/figma.json`, and `projects/<name>/prototype.json`.
2. Read every existing file under the host project's `src/screens/` and `src/components/`. List the components that already exist. **You will not create components that already exist** unless the user explicitly invokes authoring mode to replace one.
3. Read every `feedback_*.md` memory file relevant to prototype/Figma work. Re-read after every user correction in this session — corrections invalidate prior assumptions.
4. Confirm with the user the target frame node ID (or get it from the conversation).

**Figma readiness audit (the most important pre-flight step):**

The MCP server only returns clean output when the source Figma file is structurally sound — auto layout end-to-end, real components (not detached), semantic layer names, all values bound to variables. When the file isn't ready, MCP falls back to absolute positioning + raw hex, which is the exact failure mode that breaks prototypes downstream. **Audit before pulling.**

For every target component and screen:
1. Call `mcp__figma__get_metadata` for the node.
2. Check for:
   - **Auto layout** — every layout frame uses auto layout. Absolute positioning only for documented exceptions (badges, tooltips, decorative overlays).
   - **Real components** — instances are connected to a source component, not detached groups.
   - **Variable bindings** — fills, strokes, text colors, spacing, radii bound to Figma variables, not raw hex/RGB.
   - **Semantic layer names** — `CardContainer`, not `Group 5` or `Frame 47`.
3. Produce an **audit report** listing every node with issues and the specific fix for each. Format:
   ```
   FIGMA READINESS AUDIT
   Target: <screen/component name> (node <id>)

   Issues found: <count>

   1. [node <id>, "<layer name>"] Missing auto layout — child elements use absolute positioning.
      Fix: Apply Auto Layout (vertical, gap 12, padding 16) — matches sibling frames.
   2. [node <id>, "<layer name>"] Raw hex #1c1c1c on fill.
      Fix: Bind to surface-card variable.
   ...
   ```
4. **Halt and present the report to the user.** Do not proceed to component or screen building until the user directs:
   - **"Fix all"** — claude executes every fix in the report, then re-runs the audit to confirm clean state. Per `feedback_dont_ask_permission`: do not pause for per-item approval once the user says fix-all.
   - **"Fix items N, M, ..."** — claude executes the named fixes only.
   - **"I'll fix manually"** — claude waits. After the user says they're done, re-run the audit.
   - **"Skip the audit, build anyway"** — claude proceeds with a one-line warning that drift is likely.
5. Every fix claude executes is itself a Figma write, which the existing Figma `PostToolUse` hook will validate against the canvas standards. Trust the hook.

### Step 1 — Pull canonical components first, not the screen

For every component the target screen uses, pull the **canonical component** from the Components page (per `componentsPageNodeId` in `figma.json`) — not the instance on the screen. Screen instances show only one variant; the canonical shows all variants. Reference: cross-project memory `feedback_pull_canonical_component`.

Build any missing components in `src/components/` first, one at a time, by:
1. Calling `mcp__figma__get_design_context` for the canonical component node.
2. Pasting the output verbatim into a new file.
3. Substituting per the two-rule transformation above.
4. Taking a screenshot of the rendered component (Storybook-style preview file is encouraged: `src/dev/components-preview.tsx`).
5. Calling `mcp__figma__get_screenshot` for the canonical component.
6. Visually diffing the two. Halting if drift is visible.

Do **not** start the screen until every component it needs exists and matches Figma at the canonical level. Exception: if the user explicitly invokes authoring mode to design a brand-new component, follow the Authoring Mode rules above.

### Step 2 — Pull the screen frame

1. Call `mcp__figma__get_design_context` for the target screen's nodeId. If you get "invalid node ID," the file may have been edited — ask the user to confirm the current node ID for that frame; do not guess.
2. Paste the output into `src/screens/<ScreenName>.tsx` as a new file. Preserve the verbatim header comment naming the source Figma node ID:
   ```tsx
   // Verbatim translation of Figma node <nodeId> (<frameName>).
   // Pulled via mcp__figma__get_design_context on <YYYY-MM-DD>.
   ```
3. Apply the two-rule transformation (slash → dash on CSS vars; `<img>` → component imports). Nothing else.
4. **Preserve every `data-node-id` attribute MCP returned.** These are the audit trail; the drift hook checks for them.

### Step 3 — Screenshot diff

1. Run the dev server and capture the rendered screen (or describe to the user how to capture it).
2. Call `mcp__figma__get_screenshot` for the same Figma node.
3. Compare side by side. Specific things to check:
   - Pixel widths match (Figma frame = code frame). Body horizontal scroll on narrow viewports is expected and correct — do not "fix" by adding fluid classes.
   - Every text string matches Figma exactly.
   - Every component used matches its canonical component.
   - Color/spacing/radius all bound to CSS vars, not raw hex.
4. **Do not trust your own visual self-evaluation.** Show both screenshots to the user and let them call drift. AI cannot reliably self-evaluate visual parity.

### Step 4 — Halt for user review

Stop. Wait for the user to approve before moving on. Do not start the next screen.

If the user reports drift, fix in place. Do not move to the next screen with a known-broken previous screen.

### Step 5 — Wire interactions (only after all screens are approved)

After every screen in the target flow is approved at pixel parity:
1. Add routes (one per screen) using `react-router-dom`. The host project already has it as a dependency.
2. Wire onclick handlers per the user's specified flow. Five lines of routing per screen is fine; do not over-engineer.
3. Hover/focus/disabled states only if specified in Figma or explicitly requested.

---

## What this skill must NOT do

- **Invent silently.** Authoring is allowed only when the user explicitly invokes it (see Authoring Mode). Default is verbatim.
- Rewrite Figma exports for "cleaner architecture." Architecture cleanup is a separate task that happens after pixel parity is achieved, never during.
- Make the design responsive. A 1440px fixed Figma canvas → a 1440px fixed prototype.
- Invent visual treatments — divider colors, badge palettes, icon variations, hover behaviors that aren't documented in Figma.
- Pause for permission on directives already given. If the user said "build the prototype, follow the flow," commit and ship. Yes/no questions are for genuine forks. Cross-project memory: `feedback_dont_ask_permission`.
- Generate standalone HTML files. Ever. The framework's Prototyping section in `CLAUDE.md` has the full reasoning.

---

## The hook will catch you

A `PostToolUse` hook at `hooks/prototype-drift-check.sh` runs after every Write/Edit to a file under `*/advpulse-prototype/src/screens/*.tsx` (or any future `*/prototype/src/screens/*.tsx`). It greps for:

- Missing `data-node-id` attributes (proves MCP-derived).
- Raw hex values outside `var(--token, #fallback)` patterns.
- Missing verbatim header comment.

If any check fails, the hook exits non-zero and shows the violations. Treat this as a hard stop — do not work around it. Re-run the pipeline correctly.

The hook does not run on files under `src/components/` because authored components are legitimate there — but components built from canonical Figma nodes should still follow verbatim conventions whenever possible.

---

## Output

- One or more screens under `src/screens/` matching the target Figma frames at pixel parity.
- Any new or pulled components under `src/components/`, each matching its canonical Figma component (or, for authored components, clearly flagged as authored).
- Routing in `src/App.tsx` (or equivalent) connecting the approved screens.
- All design decisions and node ID references documented in the verbatim headers.

---

## What comes next

After the target flow is approved end-to-end:
- **More flows** → Repeat this workflow.
- **Deploy** → Push the host repo, deploy to preview URL (Vercel preview or equivalent).
- **Code Connect** → Only after the component library has stabilized. Adding mappings prematurely is wasted maintenance work.
