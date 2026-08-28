---
name: sync-tokens
description: "Pull design tokens live from a Figma file via the Figma MCP and write them as CSS custom properties to a project's stylesheet. Use when the user says /sync-tokens, 'sync tokens from Figma', 'update the design tokens', 'tokens are stale', or before any code work that depends on token-accurate styling. Always overwrites only the marked block in the target CSS — non-token rules are preserved."
---

# Sync Tokens Workflow

Triggered by `/sync-tokens` or when the user wants to refresh design tokens from Figma into a code project.

---

## Purpose

Treat the Figma file as the single source of truth for design tokens. This skill pulls live variables from Figma via the MCP, transforms them into CSS custom properties, and writes them into the target project's stylesheet under a clearly-marked block. Non-token CSS (Tailwind directives, body styles, custom utilities) is preserved on every sync.

The local `design-system.md` becomes documentation — Figma is the source of truth.

---

## Inputs

The skill needs a project config at `projects/<project-name>/figma.json` containing at minimum:

```json
{
  "fileKey": "<the design file key>",
  "tokenOutputPath": "/absolute/path/to/project/src/index.css"
}
```

If the project name isn't supplied, infer from `cwd` (look for an `figma.json` up the tree from the user's current project) or ask which project to sync.

---

## Process

### Step 1: Resolve the project config

1. If the user supplied a project name (e.g. `/sync-tokens <project>`), read `projects/<name>/figma.json`.
2. Otherwise, look for `figma.json` adjacent to the current working directory or ask the user which project to sync.
3. Validate the config has both `fileKey` and `tokenOutputPath`. If missing, ask the user to add them and stop.

### Step 2: Pull variables from Figma

Pull the file's variable definitions through the design tool's current MCP (for Figma, the variable-defs tool; load the vendor's own skill rather than assuming a tool name). The response is a structured list of variable collections, each containing variables with their values, types, and modes.

If the call returns nothing or errors:
- Verify the fileKey is correct (open the URL in browser).
- Check the Figma file has variables defined (some files use legacy color/text styles instead).
- Surface the error to the user with the fileKey for manual debugging.

### Step 3: Transform variables to CSS custom properties

For each variable, generate a CSS custom property line:

- **Naming**: replace slashes with dashes. `text/primary` → `--text-primary`. Replace any other CSS-invalid characters (spaces, dots) with dashes too.
- **Color values**: Figma RGBA `{r: 0.98, g: 0.98, b: 0.98, a: 1}` → hex `#fafafa`. If alpha < 1, output `rgba(...)` instead.
- **Number values**: append `px` suffix when the variable name contains `space`, `radius`, `size`, `width`, `height`, `padding`, `gap`, `stroke`. Otherwise output the raw number.
- **String values**: output as-is, quoted if needed.
- **Boolean values**: skip (CSS custom properties don't represent booleans cleanly).
- **Aliased variables** (one variable references another): output as `var(--<aliased-name>)`.

### Step 4: Handle multi-mode variables

If a variable has multiple modes (e.g. light/dark), emit each mode as a separate themed selector:

```css
:root {
  /* default mode */
  --surface-page: #000000;
}

.theme-light {
  --surface-page: #ffffff;
}
```

The default mode goes in `:root`. Other modes get class selectors.

### Step 5: Read the existing CSS file and find the markers

Read the file at `tokenOutputPath`. Locate the marker lines:

```css
/* === SYNCED TOKENS START === */
...
/* === SYNCED TOKENS END === */
```

If the markers don't exist, prepend them at the top of the file (after `@tailwind` directives if present) and treat the existing content as preserved.

### Step 6: Replace the content between markers

Replace everything between the start and end markers with the freshly-generated tokens. Preserve everything outside the markers byte-for-byte.

### Step 7: Surface what wasn't synced

`get_variable_defs` only returns Figma **variables**, not styles. If the Figma file uses legacy color styles or text styles, those won't be captured. After writing the CSS, surface a short report:

- Total variables synced.
- Total modes found.
- Any styles in the Figma file that aren't bound to variables — recommend converting them in Figma so they participate in future syncs.

Detect unbound styles by pulling metadata for the components page (if `figma.json` lists one) and looking for color or text values that are not variable references.

### Step 8: Verify

After writing the file:

1. If the project has a dev server running on a known port, hit it with curl to confirm CSS still parses.
2. Report back to the user:
   - How many tokens were synced.
   - Which modes are now available.
   - The full path of the file that was updated.
   - Anything that needs follow-up (un-bound styles, missing aliases).

---

## Output format example

After running, the target CSS file should look like:

```css
@tailwind base;
@tailwind components;
@tailwind utilities;

/* === SYNCED TOKENS START === */
:root {
  /* Brand */
  --brand-accent: <value>;

  /* Text semantic */
  --text-primary: <value>;
  --text-secondary: <value>;
  ...

  /* Spacing */
  --space-4: 4px;
  --space-8: 8px;
  ...
}
/* === SYNCED TOKENS END === */

/* Existing non-token CSS preserved below */
body { ... }
.design-frame { ... }
```

---

## Failure modes to watch

- **Markers missing from target file** → prepend them, preserve existing content as non-token region.
- **Figma file has variables but they're empty/all 0** → likely fileKey mismatch or the variables collection is in a library file. Surface this.
- **Variables reference other Figma files** (cross-file aliases) → emit as `var(--<aliased-name>)` and warn that the aliased file needs to be synced separately.
- **Target CSS file has tokens already in it but no markers** → don't blow away anything. Ask the user to add markers manually first, or offer to wrap their existing token block in markers.

---

## Re-running

This skill is idempotent. Re-running it is safe — every run reads fresh from Figma and overwrites only the marked block. Run it any time:

- Before starting a new screen/component build.
- After changes to Figma variables.
- When CSS values look inconsistent with Figma.
- As a sanity check before deploys.

---

## Direction

This skill is one-way: the design file is the source of truth and the code token layer is generated from it. **Never hand-edit the generated block** — the next sync silently discards the edit.

Where a project genuinely needs code to lead (a token layer that already exists in production, for instance), that is a different job: build the variables in the design file from the code definitions once, then resume one-way syncing. Say which direction is authoritative in `design-system.md` so the next session does not have to guess.
