# Framework Audit — 2026-11-01

Second recorded audit, and the first run on a schedule rather than by hand. Run from a cloud checkout, which turned out to matter: a third of what `doctor.py` reported was an artifact of the environment rather than a problem with the framework.

The deletion hunt came back mostly empty. That is reported as a result, not padded out.

---

## Method

- Ran `./doctor.py --repo-only` and treated its output as a hypothesis, not a verdict
- Re-read the current Claude Code reference for subagent frontmatter and for hooks, and diffed the documented field sets against `doctor.py`'s `AGENT_KEYS` / `MODEL_VALUES` and against every file in `.claude/agents/`
- Read the Figma MCP server's **live skill index** (`skill://index.json`) and its `figma-use` skill, and checked the framework's own `figma-plugin-api` entries section by section against the vendor's ~1,000-line gotchas reference
- Grepped `mcp__` across the framework layer and checked every hardcoded name against the tools the server actually exposes
- Checked README counts, and every claim either file makes about how the tooling behaves

## Environment at time of audit

| | |
|---|---|
| Figma MCP skills | **16** (12 at the last audit) |
| Figma docs site | **Unreachable** — `developers.figma.com` is denied by this environment's network policy |
| Claude Code subagent fields | 19 documented; two are new since the last audit |
| Claude Code hook events | 33 documented |
| Agents · skills | 11 · 18 (README matches both) |

The published Figma docs could not be read at all, so step 3 was answered from the live MCP server instead — its skill index, tool schemas and skill text. That is a better source for "what does the vendor ship right now" than a docs page anyway, but it cannot speak to deprecation *notices*, so anything below about a withdrawn tool is marked as inference.

---

## Findings acted on

**The canvas-standards hook has not been firing.** Its matcher was `mcp__figma.*__(…)`. Hook matchers are case-sensitive regexes, and this session's Figma server is registered as `Figma`, so the matcher could not match `mcp__Figma__use_figma` — the framework's single enforcement mechanism, silently enforcing nothing. The same defect sat in the `disallowedTools` of all four read-only reviewers, where the stakes are higher: `Write`/`Edit` bound correctly, so the agents were read-only against the filesystem while remaining free to write to the canvas. README and `CLAUDE.md` both assert reviewers are "read-only by design."

Both are fixed, and the matcher now also covers write paths that did not exist when it was written (`html_to_figma`, `send_code_to_figma`, `upload_assets`, `generate_image`). The reviewer denylists name both casings, because `disallowedTools` takes exact names and not patterns.

I could not verify which casing the designer's own machine uses — only that this one uses `Figma` and the framework assumed `figma`. Both spellings occur depending on how the server was added, so both are now listed.

**`doctor.py` was missing two subagent fields.** `autoCompactWindow` and `omitClaudeMd` are both current and documented; neither was in `AGENT_KEYS`, so adding either to an agent would have been reported as an error. This is the inverse of the 2026-08 bug — a false alarm rather than a silent failure — but it has the same cause and the same cure. `MODEL_VALUES` needed no change: `sonnet`/`opus`/`haiku`/`fable`/`inherit` plus a `claude-` prefix still matches the reference exactly.

**`doctor.py` did not validate hooks at all,** which is why the matcher bug survived. It now checks event names and handler types against the current reference, and flags a tool matcher that pins an MCP server in a single casing. Both classes are silent in the harness: an unknown event never fires, an unknown handler type never runs. Verified against deliberately broken input, not just assumed.

**`--repo-only` was reporting eleven problems that no checkout could ever satisfy.** Every `canonicalDocs` and `hostProjectPath` entry points at a directory on the designer's Mac — one is literally `/Users/cschnetzler/…` — so from the cloud they all read as missing: two errors and nine warnings of pure noise, in exactly the environment this monthly audit runs in. `doctor.py`'s own comment beside the install check warns that this is "the fastest way to teach someone to ignore the output," and the same argument applies verbatim to host paths. Under `--repo-only` the path-existence checks are now skipped; the structural ones still run, and a full local run is unchanged. `--repo-only` is now clean on a healthy checkout, which is what makes it worth reading.

**The framework had hardcoded the vendor's skill list, and it had rotted.** `CLAUDE.md`, `figma-canvas` and `figma-plugin-api` each enumerated five Figma skills. The vendor now ships sixteen, including ones that bear directly on agents this framework defines: `figma-use-motion` and `figma-implement-motion` for the motion-designer, `figma-spec` for `/handoff`, `figma-create-new-file` which is now a mandatory prerequisite for a tool the framework's own hook matches. All three now point at the live index at `skill://index.json` instead. This is the same mistake as a hardcoded tool list, one level up, and the framework's stated principle already forbade it.

**One genuine deletion.** `figma-plugin-api` §2 told the reader to infer a View-seat problem from the shape of a permission error. The vendor now ships `whoami`, whose own description says to call it when hitting file access or rate-limit problems, and it returns the user's seat per plan. The heuristic is gone; the judgment the vendor does *not* supply — what to do about a View seat — stays.

---

## Deferred

- **The reviewer denylist is now twelve hardcoded tool names, up from four.** That is the wrong direction and I am flagging it rather than hiding it. Claude Code offers no way to deny an MCP server's *write* tools by intent — `tools` is an allowlist the framework rejected on principle, `disallowedTools` takes exact names, and denying the whole server would also remove the reads reviewers need. So correctness required more names, not fewer. `doctor.py`'s threshold sits at 12 and is now a live tripwire rather than slack. If Claude Code grows a pattern or server-scoped denial, this should collapse back to one line.

- **`figma-plugin-api` §5 may now contradict the vendor.** The framework says node IDs are snapshots and to find nodes by name. The vendor's gotchas reference says the opposite as a performance matter: prefer capturing an ID and re-fetching with `getNodeByIdAsync` over searching by name again. These are reconcilable — the vendor is optimising a lookup, the framework is warning about staleness across a mutation — but "the vendor wins on mechanics" is this framework's own rule, and which this is turns on lived experience I do not have. **This one wants a decision, not an edit.**

- **Figma's published docs could not be read.** `developers.figma.com` is denied by this environment's network policy, so the recommended-integration-path question and any deprecation notices went unanswered. The live server covered most of it. To close the gap, add `developers.figma.com` under Allowed domains in the environment's Network access settings (cloud environment menu → Edit), leaving the package-manager box ticked.

- **`generate_figma_design` is referenced but not exposed.** It appears in the server's own instructions and in `use_figma`'s tool description, but is not among the tools this session can call. Most likely plan- or flag-gated rather than withdrawn. It is still named in the hook matcher and the reviewer denylists, which is harmless either way — a matcher entry for a tool that does not exist costs nothing. Worth confirming locally before anyone prunes it.

- **Code Connect.** Unchanged from the last audit: still wants a stable component API. The server has since grown `get_code_connect_suggestions` and `get_context_for_code_connect`, which lower the cost of adopting it later, but the reason to wait has not changed.

## No change needed

- **`figma-plugin-api` survived the deletion hunt almost intact, and that is the headline.** Checked all five entries against the vendor's ~1,000-line gotchas reference: comments, View seats, the regeneration heuristic, plugin/server desync and ID instability are *all* still uncovered there. The vendor covers exactly one adjacent case the framework does not mention (`detachInstance()` invalidating a cached ancestor ID) and does not cover the three regeneration triggers the framework names. The 2026-08 cut from 116 lines to 65 has held: what is left is genuinely the residue.
- **README counts are accurate** — 11 specialist agents, 13 workflow skills, both matching the repo. `docs/figma-canvas-standards.md` is a genuine standalone rewrite, not a copy of the skill file, so it does not violate the pointers-not-copies rule.
- **Every other `doctor.py` check and the rest of the hook configuration** validate clean against the current reference. The `Write|Edit` matcher, the `SessionStart` empty matcher, and both command hooks are all correct as written.
- **Agent frontmatter** is otherwise current: all 11 declare a real model, no unrecognised keys, names match filenames.

---

## Standing instruction for the next run

**The deletion hunt is still the first job, but do not manufacture one.** This run found a single deletion in `figma-plugin-api`, and the honest answer for the rest of that file was "keep." Say so plainly rather than cutting something to show work.

**Trust nothing about the environment.** This run's two most useful findings came from distrusting it: a hook matcher that looked right and matched nothing, and eleven `doctor.py` complaints that were the checkout's fault rather than the framework's. Before reporting a `doctor.py` finding, ask whether a cloud checkout could possibly satisfy it.

**Verify tool names against the live server, not against this repo.** Read `skill://index.json` for the skill set and check each hardcoded `mcp__` name against the tools actually exposed — including its casing, which is what broke this time. The published Figma docs may still be unreachable; the MCP server is the better source regardless.

**Re-validate frontmatter and hook fields against the reference every time.** Two new subagent fields appeared in two months. `doctor.py` now encodes the hook event list too, so it rots on the same schedule and needs the same check.

**Open question carried forward:** whether `figma-plugin-api` §5 (find by name) should yield to the vendor's prefer-IDs guidance. Awaiting the designer's call.
