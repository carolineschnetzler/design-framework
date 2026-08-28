# Framework Audit — 2026-08-28

First recorded audit. Run as part of the general-purpose refresh, so most findings were acted on in the same pass rather than deferred.

---

## Method

- Read every file in the repo and classified each as durable (judgment, process, standards) or volatile (vendor API surface)
- Compared framework documentation against the installed vendor skills, file by file
- Validated agent and hook configuration against the current Claude Code reference documentation
- Checked the vendor's own current guidance for its recommended integration path

## Environment at time of audit

| | |
|---|---|
| Figma plugin | 2.2.96, updated 2026-08-21 |
| Skills it ships | 12, including a 1,013-line maintained gotchas reference |
| Vendor guidance | Remote MCP server recommended; clients instructed to install the vendor's skills |

---

## Findings acted on

**The framework was caching vendor API surface.** Its Plugin API reference was roughly 85% redundant with the vendor's own gotchas file, which is updated far more often than this repo. Cut 116 lines to 65, keeping only what the vendor does not cover: comments (REST only — the word does not appear in the Plugin API), view-seat write refusals, the stale-node-reference heuristic, and the plugin/server desync that has caused real data loss here. The canvas standards file was rewritten from API mechanics to policy.

**Two agent frontmatter keys were silently ignored.** `allowed-tools` is not a recognised key — the field is `tools` — so every agent inherited all tools regardless of its list. And `model: creative` / `model: analytical` are not valid values, so the role-to-model mapping documented in `CLAUDE.md` and the README never functioned; every agent ran on `inherit`. Both fixed. **A field the harness does not recognise fails silently**, which is why this class of bug survives for months and why frontmatter validation is now a standing step of this workflow.

**Tool allowlists were removed entirely rather than corrected.** Enumerating tool names is a maintenance liability: the allowlist silently excludes every capability added after it was written. Agents now inherit, and constrained agents express intent via `disallowedTools` plus prose. A denylist that fails open on one new tool is strictly better than an allowlist that fails closed on all of them.

**The enforcement hook guarded a path nobody used.** It matched one hardcoded directory that had not been written to in three months. Now driven by each project's declared `verbatimPaths`, with an explicit opt-out for prototype-first projects.

**Framework skills and agents did not load in ordinary sessions.** They were project-scoped to this directory while the actual work happens elsewhere. `install.sh` now symlinks them into the user scope.

---

## Deferred

- **Scheduling this audit.** A recurring run would catch vendor drift without anyone remembering to look. Not set up; worth doing once the cadence is known.
- **Code Connect.** Still premature — it wants a stable component API, and adding mappings before that is maintenance for nothing.
- **Newer subagent capabilities** — `memory` for cross-session learning, `permissionMode`, `effort`. `skills` preloading was adopted; the rest are noted but not obviously worth their complexity yet.

## No change needed

- The workflow set matches the phases of a real engagement, and the additions this pass (`/prototype`, `/design-feedback`, `/changelog`, `/audit-system`) closed the gaps between documented process and actual practice.
- The design memory schema held up. What failed was its *contents*, which had one product's opinions promoted to universal — a content problem, not a schema problem.

---

## Standing instruction for the next run

**The highest-value finding is a deletion.** Look first for anything this framework explains that a vendor now explains better, and delete it rather than syncing it. Grep for `mcp__` across the repo — every hit is a maintenance liability and most should not exist. Re-validate agent and hook configuration against the current reference docs, because silent failures do not announce themselves.
