---
name: discovery
description: "Define the problem, users, constraints, and design direction for a new project or feature. Use when the user says /discover, 'start a new project', 'what should we build', 'let's figure out the approach', or when no design-brief.md exists for the active project."
---

# Discovery Workflow

Triggered by `/discover` or when no `design-brief.md` exists for the active project.

---

## Purpose

Turn a vague idea or request into a structured design brief that all downstream workflows can build on. Discovery ends when the user approves a brief — not before.

---

## Process

### Step 0: Scaffold the project folder

If `projects/<name>/` does not exist, create it before dispatching anyone:

1. Copy `templates/project.json` in and fill what you already know. This file is how the framework knows the project exists — everything else can come later.
2. **Ask where the project's canonical docs live.** Many products already keep their design documentation somewhere else, in the product repo or a team wiki. If so, point at it under `canonicalDocs` and **do not copy anything in** — a copy is a contradiction waiting to happen.
3. Copy `templates/design-state.md` in and date it. Decisions start accumulating from the first conversation, not from the first screen.

Do not create `figma.json` or `prototype.json` yet. Those describe artifacts that do not exist during discovery, and guessing at them produces config that is wrong in a way nobody notices.

### Step 1: Understand the Problem

Dispatch the **design-strategist** agent to:
- Ask the user what they's trying to solve and for whom
- Identify the real constraint or opportunity (push past surface-level requests)
- Determine what success looks like

If the problem space is unfamiliar, also dispatch the **design-scout** to research the domain and competitive landscape.

### Step 2: Define Users

The design-strategist defines:
- Who the users are (role, context, goals)
- What they're trying to accomplish
- What they care about and what frustrates them
- What prior experience or mental models they bring

Use specifics from the user and any available research. Don't invent personas — use real user context.

### Step 3: Establish Principles

The design-strategist proposes 3-5 design principles that:
- Are specific to this project (not generic)
- Create real trade-offs (if everyone would agree, it's not a principle)
- Resolve tensions that will come up during design

### Step 4: Set Direction

The design-strategist recommends a direction:
- What approach to take and why
- What alternatives were considered
- What trade-offs this direction accepts
- What constraints bound the solution (technical, business, design)

### Step 5: Name the design systems

Before writing the brief, establish how many design systems this product has. **More than one is the norm, not an edge case** — a product app and its marketing surfaces usually diverge in type and color, and a physical product has a print system alongside a web one.

For each: what it governs, where its source of truth lives. Then name **exhaustively** what they share — usually one accent color and nothing else. "They share the palette" is not an answer; it is the absence of one, and it is how two systems quietly become one muddy system.

If the product genuinely has one system, record that explicitly so nobody re-litigates it later.

### Step 6: The User Reviews

Present the draft brief to the user. They may:
- Approve it as-is
- Redirect the problem framing
- Add constraints or context
- Reject and restart

Iterate until they approve.

---

---

## Output

Write `projects/<name>/design-brief.md` with:
- **Problem statement** — One paragraph, specific and falsifiable
- **Users** — Who, what they need, what context
- **Principles** — 3-5 with rationale
- **Direction** — Recommended approach with trade-offs
- **Design systems** — What exists, what each governs, what they share
- **Constraints** — What bounds the solution
- **Success criteria** — How to know the design worked

Plus `projects/<name>/project.json` and `design-state.md` from Step 0.

---

## What Comes Next

After discovery, the typical next step is `/taste` (if no taste profile exists) or `/generate-screen` (if taste is already established). Suggest the appropriate next step to the user.
