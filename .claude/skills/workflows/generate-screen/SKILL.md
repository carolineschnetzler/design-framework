---
name: generate-screen
description: "Generate a screen on the Figma canvas based on the brief, taste profile, and design system. Use when the user says 'design this screen', 'build the dashboard', 'create the settings page', 'make a component', or any request to produce visual design output in Figma."
---

# Generate Screen Workflow

Triggered when the user asks to design, create, or build a screen or view.

---

## Prerequisites

Before generating any screen, verify:
1. A `design-brief.md` exists → if not, route to `/discover`
2. A `taste-profile.md` exists → if not, suggest `/taste`
3. The project's design system is loaded (tokens, components)

If prerequisites are missing, tell the user what's needed and offer to run the prerequisite workflow.

---

## Process

### Step 1: Understand the Screen

Clarify with the user:
- What screen or view is being designed
- What user task does it support
- What data or content will it contain
- Any specific requirements or constraints
- Reference any related screens already designed (check the Figma file)

### Step 2: Design Lead Takes Over

Dispatch the **design-lead** agent with:
- The screen requirements from the user
- The design brief (principles, direction, constraints)
- The taste profile (emotional target, craft standards, references)
- The design system (available tokens and components)
- Cross-project design memory (strong opinions from `taste-profile.md`)

The design-lead:
1. Loads the figma-canvas skill for mandatory practices
2. Checks existing Figma screens for established patterns
3. Searches the component library for reusable components
4. Loads variable definitions for available tokens
5. Designs and builds the screen on the Figma canvas

### Step 3: Content (if needed)

If the screen needs UI copy beyond placeholder text, dispatch the **content-writer** to write:
- Labels, button text, descriptions
- Empty states, error messages
- Any microcopy

The content-writer checks existing product copy for voice consistency.

### Step 4: Verify

After building:
- The design-lead takes a screenshot to verify the result matches intent
- The PostToolUse hook checks for token, naming, and auto layout compliance
- Present the screenshot to the user for feedback

### Step 5: Iterate

The user reviews and may:
- Approve the screen
- Request changes (layout, density, color, copy)
- Flag taste mismatches ("this isn't what I meant by spacious")
- Ask for alternatives ("show me a version with a sidebar")

Iterate until the user approves. Record key design decisions in `design-state.md`.

---

## Output

- A screen built on the Figma canvas following all figma-canvas standards
- Design decisions recorded in `projects/<name>/design-state.md`
- Screenshot shared with the user for review

---

## What Comes Next

After a screen is approved, typical next steps:
- **More screens** → Repeat this workflow
- **Motion and interaction** → Dispatch motion-designer
- **Review** → Run `/review` for formal critique
- **Handoff** → Run `/handoff` when ready for engineering
