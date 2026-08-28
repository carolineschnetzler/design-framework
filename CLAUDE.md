# Design Framework

A framework for designing and building products with Claude Code. This file governs every session run from this directory or against a project registered here.

The user is the designer and creative director. They set direction and make the design decisions. You do the scaffolding, the execution, and the parts that are mechanical.

---

## The one principle that keeps this framework useful

**This framework owns judgment and process. It does not own vendor APIs.**

Design tooling moves faster than any document in this repo can. Figma ships and maintains its own skills for its MCP server; Claude Code ships its own capabilities. Both change continuously. Anything this framework restates about them starts rotting immediately.

So:

- **Never restate a vendor's API surface here.** Load the vendor's own current skill instead. For Figma that means `figma-use` before any write, plus `figma-generate-design`, `figma-generate-library`, `figma-design-to-code`, and `figma-code-connect` for their respective jobs.
- **Never enumerate tool names as a permanent list.** Agents inherit the tools available to them, so new capability arrives automatically. Where an agent must be constrained, express the *intent* — "you are read-only" — in prose and in `disallowedTools`, not as an allowlist that goes stale the moment a tool is added.
- **When a vendor skill and this framework appear to conflict: the vendor wins on mechanics, this framework wins on policy.** How to bind a variable is theirs. Whether a raw hex is ever acceptable is ours.
- **When you notice this framework is behind**, say so in the session and offer `/audit`. Do not quietly work around it.

What belongs here is what does not expire: taste, principles, process sequencing, quality standards, project structure, and the specific traps this framework has actually hit.

---

## Models

Agents declare a real model in their frontmatter — `opus` for subjective and creative judgment, `sonnet` for research, review, and structured evaluation. Update the individual agent files when the model lineup changes; there is no indirection layer, because an indirection layer that silently doesn't work is worse than none.

---

## Commands

| Command | What it does |
|---|---|
| `/discover` | Define the problem, users, principles, and direction. Writes the brief. |
| `/taste` | Build or update the project's aesthetic profile from references and conversation |
| `/generate-screen` | Design a screen against the brief, taste, and system |
| `/prototype` | Build or extend a running artifact in the project's declared stack |
| `/review` | Parallel critique: design, usability, accessibility |
| `/design-debate` | Force competing directions to argue before choosing |
| `/design-feedback` | Work a batch of comments or annotations the user left by pointing |
| `/sync-tokens` | Pull live variables from the design file into the code token layer |
| `/audit-system` | Audit a design system for drift, duplication, and missing states |
| `/handoff` | Clean the file and write the engineering spec |
| `/changelog` | Append a change to the engineering log — **explicit request only** |
| `/retro` | Reflect, and feed learnings into cross-project memory |
| `/audit` | Check this framework against current Claude Code and vendor capabilities |

When the user doesn't use a command, interpret their intent and route to the matching skill or agent.

---

## Routing

Before responding to design work, check:

1. **Is there an active project?** Look in `projects/`. If none matches, ask which project, or suggest `/discover`.
2. **Does it have a brief?** If no `design-brief.md`, route to `/discover` first.
3. **Does it have taste established?** A project taste profile or a brief containing project-specific design decisions both count. Only suggest `/taste` if neither exists.
4. **Which of the project's design systems applies?** Many products have more than one. See below.

### Skill priority when several could apply

discovery → design-taste → generate-screen → prototype → design-review → design-debate → handoff → retrospective → audit

---

## Agents

| Task | Agent |
|---|---|
| Problem definition, strategy, principles | design-strategist |
| Competitive research, pattern analysis, visual references | design-scout |
| Layout, typography, color, canvas composition | design-lead |
| Tokens, variables, component libraries, variant architecture | design-systems-engineer |
| Running prototypes in any stack | prototype-engineer |
| UI copy, labels, error messages | content-writer |
| Animation specs, transitions, canvas prototypes | motion-designer |
| WCAG compliance, inclusive design | accessibility-reviewer |
| Critique against brief and taste | design-critic |
| Usability and intuitiveness | heuristic-evaluator |
| Production-ready output, engineering handoff | design-builder |

Reviewers are read-only by design. They report; the user decides; a builder executes.

---

## Project structure

Each project lives in `projects/<name>/`:

| File | Purpose |
|---|---|
| `project.json` | What this project is, who implements it, where its canonical docs live |
| `design-brief.md` | Problem, users, principles, direction, constraints |
| `design-system.md` | Tokens, type, spacing, component inventory — documentation; the design file is the source of truth |
| `taste-profile.md` | Aesthetic preferences specific to this project |
| `design-state.md` | Running decisions log, open questions, design debt |
| `design-changes.md` | Engineering changelog — only written via `/changelog` |
| `figma.json` | File key and page node IDs |
| `prototype.json` | Host project path, stack, and paths the drift check guards |

**A project's canonical docs may live outside this repo.** When they do, `project.json` points at them and the framework reads from there. Do not duplicate a canonical doc into `projects/` — a copy is a future contradiction. Pointers, not copies.

**Screen inventory is never tracked in markdown.** The design file is the only source of truth for what screens exist and their current IDs. Pull the inventory live. Any node ID written into a doc is a snapshot, not an address.

---

## Products often have more than one design system

This is the norm, not an edge case. A product app and its marketing surfaces usually diverge in type and color, and they should — they have different jobs. A physical product may have a print system and a web system.

When a project has more than one:

- Name them, define what each governs, and record the boundary in `design-brief.md`
- Name what they share, explicitly and exhaustively. Usually it is one accent color and nothing else.
- **Pick the system by surface, then adhere strictly.** Never mix faces or palettes across the boundary.
- The usual sanctioned exception is a real product screenshot inside a marketing layout: the screenshot keeps product styling, the frame around it uses brand styling.

---

## Prototyping

The framework produces design artifacts, engineering specs, **and** running prototypes. Prototypes are built by the prototype-engineer in the stack declared in `prototype.json` — React, a Shopify theme, a static site, a publishable artifact, or print production files. Never assume a stack; read it.

**Two rules that survive every stack:**

1. **Prototypes consume the design system as code.** They do not reinvent it. If the host project has no component and token layer, building that layer is the first task, not an optional step.
2. **Say which direction the work is flowing.** Translating an existing design is the default and it is faithful — narrow substitutions only. Designing in code is legitimate when a static frame cannot answer the question, and then the design file follows and gets reconciled. Authoring is legitimate when the user asks for it. What is forbidden is inventing silently while claiming to translate.

**On standalone HTML:** do not hand-roll a standalone HTML file as a substitute for a real prototype — that reinvents the design system every time and loses fidelity. A published **artifact** is different and is sanctioned: it is a distribution format for people who will not run a dev server, and it is declared as `"stack": "artifact"` in `prototype.json`.

Operational detail lives in the `prototype` skill, not here. A `PostToolUse` hook catches drift on the paths a project declares — the enforcement layer is the hook, not this prose.

---

## Cross-project memory

`taste-profile.md` at the repo root holds what belongs to the **designer**, across every project:

- **Strong opinions** — constraints for all projects
- **Soft patterns** — suggestions, not enforced
- **Anti-patterns** — exclusions

What belongs to a *product* goes in that project's own taste profile. The test: if the opinion would change for a different client or a different medium, it is not cross-project. Keep the root file small; a bloated one stops being read.

`/retro` updates it at project end.

---

## Canvas quality

All canvas work follows `.claude/skills/tools/figma-canvas/SKILL.md` — semantic tokens with no raw values, auto layout by default, component reuse before creation, complete state coverage, and verification by screenshot after every structural change. That file is policy. Load the vendor's own skills for how to execute it.

Two rules worth repeating here because they are violated most often:

- **Search for an existing component before building anything.** Building a duplicate you did not find is the most common failure.
- **Never leave broken output.** Content fits its container. Nothing clips, overflows, or overlaps. Verify before moving on.

---

## Narration

1. **Arrival** — what you are picking up and why
2. **Working** — surface decisions as you make them, so the user can redirect before you build further
3. **Departure** — what was done, what is open, what is next

The user can redirect at any point. Defer to their judgment on aesthetic and strategic calls.
