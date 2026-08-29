# Design Framework

An AI-native design framework built on [Claude Code](https://claude.com/claude-code). It structures how a designer works with AI agents across discovery, critique, canvas execution, running prototypes, and engineering handoff — with opinionated defaults about taste, design-file quality, and cross-project design memory.

It isn't a prompt or a plugin. It's a working directory — agents, skills, hooks, and templates — that turns Claude Code into a functioning design team.

> **Author:** Caroline Schnetzler
> **License:** MIT
> **Status:** Working framework, used in production consulting work

---

## Start here

If you have five minutes, read the two standalone docs. They're the most portable parts:

- **[Figma Canvas Standards](docs/figma-canvas-standards.md)** — Enforceable rules for production-ready design files. Semantic tokens, auto layout exceptions, slot vs. instance swap, variant architecture, required states. Usable on any project, with or without AI.
- **[Design Memory](docs/design-memory.md)** — A schema for capturing a designer's aesthetic identity so it persists across projects and is readable by agents. Three layers: strong opinions, soft patterns, anti-patterns. Solves the "taste resets every project" problem.

---

## The principle that keeps it useful

**This framework owns judgment and process. It does not own vendor APIs.**

Design tooling moves faster than any document in a repo can. Figma ships and maintains its own skills for its MCP server. Claude Code ships its own capabilities. Both change continuously, and anything a framework restates about them starts rotting immediately.

So the framework deliberately does **not**:

- restate a vendor's API surface — it loads the vendor's current skill instead
- enumerate tool names as permanent allowlists — agents inherit their tools, so new capability arrives automatically
- cache what someone else maintains better

Where a vendor skill and this framework conflict: **the vendor wins on mechanics, the framework wins on policy.** How to bind a variable is theirs. Whether a raw hex is ever acceptable is ours.

The highest-value output of the `/audit` workflow is therefore a **deletion** — finding something this framework explains that the vendor now explains better.

---

## What's inside

```
design-framework/
├── CLAUDE.md              Framework-wide instructions
├── install.sh             Symlinks agents + skills into ~/.claude/ so they load everywhere
├── taste-profile.md       Cross-project design memory
├── .claude/
│   ├── settings.json      Hooks: session init, canvas standards check, prototype drift check
│   ├── agents/            11 specialist agents
│   └── skills/
│       ├── reference/     design-principles · taste-profile · component-specs · figma-plugin-api
│       ├── tools/         figma-canvas (policy, not API docs)
│       └── workflows/     13 workflow skills
├── hooks/                 session-init · prototype-drift-check
├── templates/             brief · state · memory · handoff-spec · project.json · prototype.json · figma.json
├── projects/              One folder per product
└── docs/                  Shareable standalone docs
```

---

## Agents

Eleven specialists. Reviewers are read-only by design — they report, the designer decides, a builder executes.

| Agent | Owns |
|---|---|
| design-strategist | Problem, users, principles, direction |
| design-scout | Competitive research, patterns, visual references |
| design-lead | Layout, typography, color, canvas composition |
| design-systems-engineer | Tokens, variables, component libraries, variant architecture |
| prototype-engineer | Running prototypes in any declared stack |
| content-writer | UI copy, labels, error messages |
| motion-designer | Transitions, canvas prototypes, motion specs |
| design-builder | Production cleanup, engineering handoff |
| design-critic | Critique against brief and taste |
| heuristic-evaluator | Usability and intuitiveness |
| accessibility-reviewer | WCAG compliance, inclusive design |

---

## Workflows

| Workflow | What it does |
|---|---|
| `/discover` | Dispatches strategist and scout to write the brief |
| `/taste` | Builds the project's taste profile from references and conversation |
| `/generate-screen` | Design-lead creates screens against brief, taste, and system |
| `/prototype` | Builds a running artifact in the project's declared stack |
| `/review` | Parallel critique: design, usability, accessibility |
| `/design-debate` | Forces competing directions to argue before choosing |
| `/design-feedback` | Works a batch of comments or annotations left by pointing |
| `/sync-tokens` | Pulls live variables into the code token layer |
| `/audit-system` | Audits a design system for drift, duplication, missing states |
| `/handoff` | Cleans the file and writes the engineering spec |
| `/changelog` | Appends to the engineering log — opt-in only |
| `/retro` | Reflects, and updates cross-project memory |
| `/audit` | Checks the framework against current tooling |

---

## The core ideas

### 1. Taste is cross-project, not project-bound

Most systems tether taste to a brief. This one separates them. The root `taste-profile.md` holds what belongs to the **designer** — opinions that would still hold for a different client and a different medium. Anything that would change for another product lives in that project's own profile.

The test is real, not decorative: one project in this repo uses large radii and rejects glass; another uses zero radius and embraces it. An opinion that flips between two products was never cross-project memory.

### 2. File quality is enforced, not documented

A `PostToolUse` hook runs after every design-file write and checks against the canvas standards. A second hook guards prototype paths each project declares, so translated screens can't quietly become authored ones.

Most frameworks document standards. This one enforces them — and where a rule can't be enforced, it says so rather than pretending.

### 3. Principles must create trade-offs

A principle that doesn't create a trade-off is a platitude. "Be intuitive" isn't a principle. "Prioritize speed over completeness" is. The strategist names the trade-off every principle creates and flags the ones that don't.

### 4. Products usually have more than one design system

A product app and its marketing surfaces diverge in type and color, and they should. A physical product has a print system and a web system. The framework treats this as the norm: name the systems, define what each governs, name exhaustively what they share, then adhere strictly by surface.

### 5. Prototypes are first-class, in whatever stack the project uses

Stack is declared in `prototype.json`, never assumed — React, a Shopify theme, a static site, a published artifact, print production files.

Direction of flow is declared too. Translating an existing design is faithful and narrow. **Designing in code is legitimate** when a static frame can't answer the question, and then the design file follows. Authoring is legitimate when asked for. What's forbidden is inventing silently while claiming to translate.

---

## Installation

```
git clone https://github.com/carolineschnetzler/design-framework.git
cd design-framework
./install.sh
```

`install.sh` symlinks the agents and skills into `~/.claude/`, so they load in **every** session rather than only when Claude Code starts in this directory. Symlinks, not copies — the repo stays the source of truth and edits take effect immediately. `--status` shows what's linked; `--uninstall` removes only what it created.

Hooks stay project-scoped on purpose — the canvas standards check and the prototype drift check run when you work from this directory, not against unrelated repos.

**One exception worth making global.** `doctor.py` checks the framework for the kind of rot that fails silently: unrecognised frontmatter keys, dead symlinks, guards pointing at paths nobody writes to, project configs aimed at directories that no longer exist. Project-scoped, it only runs when you are already in this directory — which is not where a broken agent actually bites you. Add it to `~/.claude/settings.json` so it runs everywhere:

```json
{ "hooks": { "SessionStart": [ { "matcher": "", "hooks": [
  { "type": "command",
    "command": "$HOME/design-framework/doctor.py --quiet --errors-only 2>/dev/null || true" } ] } ] } }
```

It costs about 0.08s, prints nothing when clean, and `--errors-only` keeps hygiene warnings in the framework directory where they belong. The `|| true` matters: a missing or renamed framework must never block an unrelated session.

To start a project: copy `templates/project.json` into `projects/<name>/` and run `/discover`.

To adopt one piece: `docs/figma-canvas-standards.md` and `docs/design-memory.md` stand alone.

---

## Who this is for

- **Designers using Claude Code** who want a real structure instead of ad-hoc prompts
- **Design engineers** structuring AI-assisted design work in their own codebase
- **Consultants** who need design memory that survives client churn
- **Teams building AI design tools** who want a reference for how agents, skills, hooks, and memory interact in production

It reflects one designer's opinions about process and craft. The parts most likely to generalize are in `docs/`.

---

## Philosophy

1. **Agents do the scaffolding, not the judgment.** They write briefs, run critiques, clean files, build prototypes. The designer makes the design decisions.
2. **Taste is the hardest thing to transfer.** Capturing it durably is the highest-leverage move in AI-assisted design work.
3. **Production quality requires enforcement.** Documenting a standard isn't enough. Hooks enforce, so violations don't survive a session.
4. **Know what you don't own.** A framework that tries to own its vendors' APIs is a framework that is always wrong.

---

## Feedback

Open an issue on [GitHub](https://github.com/carolineschnetzler/design-framework).
