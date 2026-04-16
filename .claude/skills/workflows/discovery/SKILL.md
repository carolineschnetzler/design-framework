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

### Step 5: The User Reviews

Present the draft brief to the user. They may:
- Approve it as-is
- Redirect the problem framing
- Add constraints or context
- Reject and restart

Iterate until they approve.

---

## Output

Write `projects/<name>/design-brief.md` with:
- **Problem statement** — One paragraph, specific and falsifiable
- **Users** — Who, what they need, what context
- **Principles** — 3-5 with rationale
- **Direction** — Recommended approach with trade-offs
- **Constraints** — What bounds the solution
- **Success criteria** — How to know the design worked

---

## What Comes Next

After discovery, the typical next step is `/taste` (if no taste profile exists) or `/generate-screen` (if taste is already established). Suggest the appropriate next step to the user.
