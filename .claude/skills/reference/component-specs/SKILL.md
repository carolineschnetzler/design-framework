---
name: component-specs
description: How to find, evaluate, and use existing Figma components from the project's design system. Load before any Figma canvas work, when creating or editing components, when checking if a component already exists, or during handoff preparation.
---

# Component Specs Reference

This skill teaches agents how to find, evaluate, and use existing components from the project's Figma design system. The goal is to reuse what exists before creating anything new.

---

## Before Building Anything

Every agent with Figma write access must check for existing components before creating new elements:

1. **Search the design system** — Use `search_design_system` with the fileKey to find components matching what you need
2. **Check variable definitions** — Use `get_variable_defs` to understand available tokens and their current values across modes
3. **Check the project's design-system.md** — This file documents the component inventory, naming conventions, and usage guidelines

Only after confirming no existing component covers the need should you create something new — and even then, get the user's approval first.

---

## How to Use Existing Components

### Finding Components
- `search_design_system` returns components by name and description
- Search broadly first ("Button," "Card," "Input") then narrow down
- Components use slash-separated naming for hierarchy: `AgenticCard/Progress`, `Button/Icon/Big`
- Check for component sets — a component may have variants you haven't seen yet

### Importing Components
- Use `importComponentByKeyAsync(key)` or `importComponentSetByKeyAsync(key)` to import from the library
- Create instances with `.createInstance()` on the imported component
- Never recreate a component by manually building its structure — always instance it

### Configuring Instances
- Use **variant properties** to switch between states, sizes, and types
- Use **boolean properties** to toggle optional elements
- Use **instance swap properties** to swap constrained child components (icons, avatars)
- Use **slots** (named content frames) for open-ended content areas
- Use **text properties** to set labels and descriptions
- Override text content directly on text layers as needed

### What NOT to Do
- Don't detach instances to customize them
- Don't override colors or spacing on instances — use variant properties
- Don't create a one-off frame that looks like an existing component — use the real component
- Don't assume a component doesn't exist because you didn't find it on the first search — try alternate names

---

## When a Component Doesn't Exist

If the design needs a component that doesn't exist in the system:

1. **Confirm it's truly missing** — Search with multiple terms, check component sets for hidden variants
2. **Flag it to the user** — Describe what's needed and why existing components don't cover it
3. **If the user approves creation**, follow these rules:
   - Match the naming convention of existing components (slash hierarchy, PascalCase)
   - Include all required states (default, hover, focus, active, disabled)
   - Use semantic tokens for all values
   - Add slots for any open-ended content areas
   - Set up proper variant properties
   - Create it as a local component in the project file (not in the shared library — that's a separate decision)

---

## Component Quality Check

When reviewing or auditing components, verify:

- [ ] All state variants present and correctly configured
- [ ] Semantic variables bound (not raw values)
- [ ] Auto layout applied with correct sizing modes
- [ ] Slot frames named descriptively with auto layout and default content
- [ ] Instance swap properties use `preferredValues` to filter valid options
- [ ] Boolean properties named clearly (`hasIcon`, `showLabel`, not `toggle1`)
- [ ] Text properties exposed for all editable strings
- [ ] Layer naming follows convention (Title-Kebab for frames, PascalCase for components)
- [ ] Component description filled in (explains when and how to use it)

---

## Where Component Info Lives

- **Figma file** — The source of truth for component structure, variants, and properties
- **Project design-system.md** — Documents the component inventory and usage guidelines
- **Project design-tokens.json** — Machine-readable token values
- **`get_variable_defs`** — Live variable values and mode mappings from the Figma file
- **`search_design_system`** — Search for components by name in the Figma library
- **`get_code_connect_suggestions`** — How components map to code (relevant during handoff)
