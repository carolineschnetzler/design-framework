# Refuge Mountain Linen

**Canonical state lives outside this repo**, at `~/refugelinen/PROJECT.md`. See `project.json` for the map.

## Why this project matters to the framework

Refuge is the project that proved the framework was not general. It has:

- **A non-React stack.** A Shopify theme, where the prototype pipeline's React assumptions do not apply.
- **A print system alongside a web system.** Bleed, trim, dieline, and color space are correctness, not polish — a category the framework had no vocabulary for.
- **A design file the designer cannot write to.** The packaging files sit in a team where the seat is view-only, so MCP writes are refused and reads are capped. The workaround is a local plugin running in the desktop app.

Each of those is now handled by declaration rather than assumption: `stack` in `prototype.json`, the print entry in the stack table, and the seat failure mode in the `figma-plugin-api` reference.

## Framework files not yet created here

`design-brief.md` · `design-system.md` · `design-state.md` · `taste-profile.md` · `figma.json`
