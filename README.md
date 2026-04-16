# Design Framework

An AI-native design framework built on [Claude Code](https://claude.com/claude-code). It structures how a designer collaborates with AI agents to run discovery, critique, visual execution, and engineering handoff — with opinionated defaults about taste, Figma canvas quality, and cross-project design memory.

The framework isn't a prompt or a plugin. It's a working directory — agents, skills, hooks, and templates — that turns Claude Code into a functioning design team.

> **Author:** Caroline Schnetzler · Design consultant, PureMath
> **License:** MIT
> **Status:** Working framework, used in production consulting work

---

## Start here

If you have five minutes, read the two standalone docs — they're the most portable parts of the framework:

- **[15 Figma Canvas Standards](docs/figma-canvas-standards.md)** — Opinionated, enforceable rules for production-ready Figma files. Semantic tokens, auto layout exceptions, slot vs. instance swap, required state variants. Usable on any project, with or without AI.
- **[Design Memory](docs/design-memory.md)** — A schema for capturing a designer's aesthetic identity in a way that persists across projects and is readable by AI agents. Three-layer structure (Strong Opinions / Soft Patterns / Anti-Patterns). Solves the "taste resets every project" problem.

If you want to understand how the framework works end-to-end, keep reading.

---

## What's inside

```
design-framework/
├── CLAUDE.md                        # Framework-wide instructions for all agents
├── taste-profile.md                 # Cross-project design memory (the designer's identity)
├── .claude/
│   ├── settings.json                # Hooks: session-init, PostToolUse Figma check, Stop log
│   ├── agents/                      # 9 specialist agents
│   │   ├── design-strategist.md     # Defines problem, users, principles, direction
│   │   ├── design-scout.md          # Competitive research + visual references
│   │   ├── design-lead.md           # Layout, typography, color — primary Figma author
│   │   ├── design-builder.md        # Production-ready cleanup + handoff spec
│   │   ├── design-critic.md         # Critique against brief, taste, principles
│   │   ├── motion-designer.md       # Transitions, prototypes, motion specs
│   │   ├── content-writer.md        # UI copy — labels, errors, microcopy
│   │   ├── heuristic-evaluator.md   # Usability, Nielsen heuristics
│   │   └── accessibility-reviewer.md # WCAG compliance, inclusive design
│   └── skills/
│       ├── reference/               # Design principles, taste, component specs
│       ├── tools/figma-canvas/      # Canvas standards (see docs/figma-canvas-standards.md)
│       └── workflows/               # /discover /taste /generate-screen /review
│                                    # /design-debate /handoff /retro /audit
├── hooks/session-init.sh            # Prints framework status + loaded memory
├── templates/                       # Brief, state, memory, handoff-spec templates
├── projects/advpulse/               # Example project using the framework
└── docs/                            # Shareable standalone docs (canvas standards, design memory)
```

---

## The core ideas

### 1. Taste is cross-project, not project-bound

Most design systems tether taste to a project brief. The framework separates them:

- **Cross-project memory** (`taste-profile.md`) — strong opinions, soft patterns, anti-patterns that belong to the designer, not any single project
- **Project taste profile** (`projects/<name>/taste-profile.md`) — what's specific to this brief

Agents load both. Cross-project memory acts as constraint (for strong opinions), suggestion (for soft patterns), or exclusion (for anti-patterns). The `/retro` workflow updates cross-project memory at project end — so taste is versioned, not static.

Full schema at [docs/design-memory.md](docs/design-memory.md).

### 2. Figma canvas quality is enforceable, not optional

A `PostToolUse` hook runs after every Figma canvas edit, checking against the canvas standards (semantic tokens, auto layout, naming, state completeness). Violations are flagged and, where automatic, fixed immediately.

Most design frameworks document standards. This one enforces them.

Full standards at [docs/figma-canvas-standards.md](docs/figma-canvas-standards.md).

### 3. Design principles must create trade-offs

The `design-principles` skill teaches agents that a principle that doesn't create a trade-off is a platitude. "Be intuitive" isn't a principle. "Prioritize speed over completeness" is.

The `design-strategist` agent is trained to name the trade-off every principle creates — and to flag principles that don't. The `design-critic` agent uses those principles as the standard for critique.

### 4. Workflows over freeform prompts

The framework ships with eight workflow skills that match the phases of a real design engagement:

| Workflow | What it does |
|---|---|
| `/discover` | Dispatches design-strategist and design-scout to write the brief |
| `/taste` | Builds or updates the project's taste profile from references and conversation |
| `/generate-screen` | Design-lead creates screens against brief, taste, and system |
| `/review` | Parallel critique from design-critic, heuristic-evaluator, accessibility-reviewer |
| `/design-debate` | Forces competing directions to argue their case before choosing |
| `/handoff` | Design-builder cleans the file and writes the engineering spec |
| `/retro` | Post-project reflection, updates cross-project memory |
| `/audit` | Checks the framework against current Claude Code and Figma MCP capabilities |

Each workflow is a `SKILL.md` file — not just a prompt, but a structured process with steps, outputs, and quality gates.

### 5. Role-based model assignments

Agents declare a role in their frontmatter (`creative` or `analytical`). The model for each role is mapped once in `CLAUDE.md`:

```
creative   → claude-opus-4-6   (subjective judgment, visual decisions)
analytical → claude-sonnet-4-6 (research, review, structured evaluation)
```

When new models release, update the mapping once — every agent inherits automatically.

---

## Who this is for

- **Designers using Claude Code** who want a real working structure instead of ad-hoc prompts
- **Design engineers** evaluating how to structure AI-assisted design work in their own codebase
- **Consultants** who want cross-project design memory that survives client churn
- **Teams building AI design tools** who want a reference for how agents, skills, hooks, and memory interact in production

This isn't a general-purpose framework. It reflects the author's opinions on design process, Figma practice, and what AI agents should and shouldn't own. The parts most likely to generalize — the canvas standards and the design-memory schema — are in `docs/` as standalone documents.

---

## Installation

```
git clone https://github.com/cschnetzler/design-framework.git
cd design-framework
```

Claude Code will load `CLAUDE.md`, `.claude/settings.json`, and the agent/skill definitions automatically when you run `claude` from the directory. The session-init hook prints framework status on startup.

To use it with your own project:
1. Copy the framework into your working directory
2. Remove the `projects/advpulse/` example and create a new project folder
3. Run `/discover` to start the first project

To adopt just one piece (e.g., the canvas standards): copy `docs/figma-canvas-standards.md` and the matching `.claude/skills/tools/figma-canvas/SKILL.md` into your own setup.

---

## Philosophy

The framework is built on three assumptions:

1. **AI agents should do the scaffolding, not the judgment.** Agents write briefs, run critiques, and clean up Figma files. The designer makes the design decisions.
2. **Taste is the hardest thing to transfer.** Capturing it in a durable, agent-readable format is the highest-leverage move for AI-assisted design work.
3. **Production quality requires enforcement.** Documenting standards isn't enough. The framework enforces them via hooks, so violations don't survive a session.

---

## Feedback

If you're using this or an adaptation of it, feedback is welcome. Open an issue on [GitHub](https://github.com/cschnetzler/design-framework).
