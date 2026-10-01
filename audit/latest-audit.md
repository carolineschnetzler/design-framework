# Framework Audit — 2026-10-01

Second recorded audit, and the first run by the monthly cloud routine rather than by hand. Five changes, all small. Nothing structural is wrong with the framework.

---

## Method

- Ran `./doctor.py --repo-only` and separated real findings from artifacts of running in a cloud checkout
- Re-read the current Claude Code subagent and hooks field references and diffed them against `doctor.py`'s `AGENT_KEYS` / `MODEL_VALUES` and against every file in `.claude/agents/`
- Read Figma's **live** served skill index (`skill://index.json`) and the `figma-use` skill with its `gotchas.md`, `component-patterns.md`, and `api-reference.md` references, then went through `figma-plugin-api` and `figma-canvas` section by section asking whether the vendor now covers it
- Grepped `mcp__` across the framework layer and checked each hit against the tool names actually present in a live session
- Checked README counts and hunted for assertions about tooling that are no longer true

## Environment at time of audit

| | |
|---|---|
| Date / trigger | 2026-10-01, monthly routine (`0 15 1 * *`) |
| Figma MCP server | Remote, `https://mcp.figma.com/mcp` — still the recommended path |
| Skills it ships | **15**, up from 12 in August |
| Framework layer | 11 agents · 18 skills · 13 workflows |
| Doctor | 2 errors, 10 warnings — **all of them cloud artifacts, see below** |

**`doctor.py` output is not usable as-is in this environment.** Every error and warning it reported is a `hostProjectPath` or `canonicalDocs` path under `~/` or `/Users/cschnetzler/` — the designer's laptop, which a cloud checkout cannot see. There is no evidence any of these are broken on the real machine, and this audit treated none of them as findings. The useful signal was the top line: counts, and the hardcoded-vendor-name tally.

---

## Findings acted on

**The canvas-quality hook could not fire. This was the real finding.** The `PostToolUse` matcher was `mcp__figma.*__(use_figma|generate_figma_design|create_new_file)` — case-sensitive, and the Figma MCP server is registered as `Figma` in this session, so the live tools are `mcp__Figma__use_figma` and friends. The matcher misses them entirely. `CLAUDE.md` says plainly that "the enforcement layer is the hook, not this prose", so a hook that silently never runs means canvas standards went unchecked after every write in any session where the server is capitalised. Now `(?i)mcp__[a-z0-9_]*figma[a-z0-9_]*__(…)` — case-insensitive and tolerant of the server-name segment. This is the same silent-failure class as the two dead frontmatter keys in August: nothing announces it.

**Four reviewer agents' write-blocks have the same mismatch — not fixed, see Deferred.** It is the one thing below that needs a human.

**`doctor.py` was missing a subagent field.** `omitClaudeMd` (launches a subagent without the user/project CLAUDE.md files; Claude Code v2.1.271+) is now in the reference and was absent from `AGENT_KEYS`, so `doctor.py` would have reported a legitimate use of it as an unrecognised key — the validator failing the thing it exists to protect. Added. `MODEL_VALUES` needed nothing: `sonnet`, `opus`, `haiku`, `fable`, `inherit` matches the current reference exactly, and every agent's `model` is a valid value. No agent uses an unrecognised key. **The August fix is still holding.**

**Two deletions in `figma-plugin-api`, taken under its own rule.** The file says that if an entry ever contradicts or duplicates the official skills it should be deleted. Holding it to that:

- **§3, the regeneration heuristic, lost its general rule.** `figma-use` now documents stale node references directly — `detachInstance()` invalidating ancestor IDs, with WRONG/CORRECT examples in both `gotchas.md` and `component-patterns.md`, slot appends invalidating a child handle, and the same fix the framework was giving ("re-discover by traversal from a stable non-instance parent"). That is upstream now and no longer belongs here. What survives is the **variant** case, which the vendor still does not document: switching an instance's variant or setting a property on a nested instance regenerates the subtree, and the second `setProperties` on a held reference silently no-ops. Section is now four lines and ends with the condition for deleting it entirely.
- **§5 asserted something false about the API.** It claimed node IDs "shift when nodes are renamed, moved, regenerated, or recreated." Rename and move do not change a Figma node ID — nothing in the vendor's reference says so, `node.name` is an ordinary property write, and the only ID-invalidation causes documented are detach, regeneration, and recreation. Corrected, and reframed as what it actually is: a **documentation** policy, not an API claim. The policy is still right and still underpins `CLAUDE.md`'s rule that screen inventories never live in markdown — a node ID in a doc rots because the *file* gets reorganised by people who never read the doc, not because IDs are unstable.

**The framework's list of vendor skills was quietly incomplete.** Figma ships 15 skills now; `CLAUDE.md` and `figma-canvas` each named 4–5 as though that were the set. The gap that mattered: `figma-use-motion` exists and nothing here pointed at it, so `motion-designer` — whose whole job is animating Figma nodes — had no route to the vendor's motion guidance. Also new since August: `figma-create-new-file` (a mandatory prerequisite before `create_new_file`), `figma-generate-diagram`, `figma-implement-motion`, `figma-shaders`, `figma-swiftui`, `figma-generative-plugins`, `figma-use-figjam`, `figma-use-slides`.

Both files now name the motion skill, say explicitly that the list is examples rather than the set, and point at `skill://index.json` for what exists right now. **No agent file needed editing** — `motion-designer` loads `figma-canvas`, so fixing the policy file reached it. This is the framework's own principle applied to itself: it was enumerating a vendor's surface and the enumeration had gone stale, exactly as predicted.

**This workflow file described a cadence and a mechanism that no longer exist.** `audit/SKILL.md` said "biweekly scheduled agent" in three places — the trigger is monthly — and ended with "the user reviews on their next session", which stopped being true once the routine started opening pull requests. Its Step 2 also told the run to read `~/.claude/plugins/installed_plugins.json` for plugin versions, which a cloud run cannot do and which the trigger prompt already overrides. Replaced with the live `skill://index.json` read, which is the better source anywhere: it is versioned with the API, not with whatever plugin version a laptop happens to have installed. The deferred item from August — "scheduling this audit" — is **done**, and the file now reflects how it actually runs.

---

## Deferred — one item, and it needs a decision

**The four read-only reviewer agents name Figma's write tools in `disallowedTools`, and those names do not match the live tools.** `accessibility-reviewer`, `design-critic`, `design-scout`, and `heuristic-evaluator` all carry:

```
disallowedTools: Write, Edit, NotebookEdit, mcp__figma__use_figma, mcp__figma__generate_figma_design, mcp__figma__create_new_file
```

In this session the tools are `mcp__Figma__*`, so those three entries resolve to nothing and the write tools stay available. A non-resolving `disallowedTools` entry fails **silently** — no error, no warning, and the session's own agent listing repeats the dead names back as though they were in force, which is what makes it hard to notice.

**This is not an open barn door.** All four agents carry the prose belt — *"You are read-only. You do not write to the canvas and you do not edit files… This holds even if a tool that could write is available to you."* — which is the layer `CLAUDE.md` says to rely on. The denylist is the suspenders, and the suspenders are not attached.

Not fixed here, because the right fix depends on two things this run could not establish from a cloud container:

1. **What the server is called on the designer's machine.** If it is `figma` there, the denylist works locally and only cloud sessions are affected. If it is `Figma`, it has never worked anywhere.
2. **Whether subagent `disallowedTools` honours glob patterns.** Deny rules in `settings.json` definitely do — the permissions reference is explicit that deny rules accept globs in the tool-name position, and that `mcp__puppeteer` matches every tool from that server. The subagent reference only says `disallowedTools` takes the "same format as `tools`", which is not the same claim. One live local session settles it.

Two options, and they pull against each other:

- **Add the capitalised names alongside the existing ones.** Safe, zero risk, works immediately — and takes the hardcoded vendor names from 3 to 7, which is the maintenance liability `doctor.py` tracks and which `CLAUDE.md` forbids in as many words ("Never enumerate tool names as a permanent list").
- **Replace all three with one pattern**, once glob support is confirmed. Fewer names, survives renames, matches the stated principle. Needs the verification first.
- A whole-server deny (`mcp__figma`) is **wrong** and should not be used: reviewers need the Figma *read* tools (`get_design_context`, `get_screenshot`) to do their jobs at all.

Recommendation: verify both in one local session, then take the pattern. Until then the prose is carrying it, which it was designed to do.

Also still deferred, unchanged from August and still correctly deferred:

- **Code Connect.** Wants a stable component API; mappings before that are maintenance for nothing. The vendor's `figma-code-connect` skill is current and will be there when the moment comes.
- **Subagent `memory`, `permissionMode`, `effort`.** Still available, still not obviously worth the complexity. `memory` remains the interesting one for a framework with cross-project taste — but `/retro` writing to `taste-profile.md` is working and is inspectable, which an opaque memory store is not.

---

## No change needed

- **Vendor integration path is unchanged.** The remote server at `mcp.figma.com/mcp` is still what Figma recommends; the desktop server remains the narrow enterprise/Dev-seat case. No deprecations, no renamed tools, nothing the framework points at has moved.
- **README counts are correct.** 11 specialist agents, 13 workflow skills — both match the filesystem. `doctor.py` checks these on every session start, which is why they are right.
- **`figma-canvas` is holding up as policy.** Every section is a standard the work is held to, not API mechanics. Its slots-vs-instance-swap table is a *decision* table where the vendor's is a how-to — correct division, no overlap to delete. Its motion section is timing taste, which no vendor skill covers.
- **`figma-plugin-api` §1, §2, §4 are all still uncovered upstream.** Checked directly against the vendor's `gotchas.md`: zero hits for comments, zero for seats or licensing, zero for plugin/server desync. Comments genuinely are REST-only and absent from the Plugin API. These three are why the file still exists, and they are 40 of its 68 lines.
- **Agent frontmatter is clean.** Every key recognised, every model value valid, no empty tool lists. The August repair held for four months.
- **Hook events are current.** `SessionStart` and `PostToolUse` both still exist and behave as the framework assumes. The reference has grown a lot of new events — `SubagentStop`, `PreCompact`, `PermissionDenied`, `FileChanged` and others — and none of them is something this framework needs today.

### One thing I could not check

**Figma's published docs were unreachable.** `developers.figma.com` is blocked by this environment's network egress proxy, so step 3 was answered from the MCP server's **live** skill index and server instructions plus a web search, not from the vendor's documentation pages. For "what skills exist and what does the API say", the served index is the better source — it is the thing actually loaded at runtime. For prose-only material like deprecation notices and migration guidance, it is not, and this run has a blind spot there. If that matters, either allow `developers.figma.com` in the environment's network settings or run `/audit` locally once.

---

## Standing instruction for the next run

**The highest-value finding is still a deletion, but the highest-*risk* finding is a silent failure.** This run found two of the latter and they were both the same shape as August's: a string naming a vendor's surface, drifting out of alignment with reality, failing with no error. First the hook matcher, then the reviewer denylists, and both were invisible from the file alone — you only see it by comparing what the framework writes down against the tool names a live session actually has. **Do that comparison every time.** Grep `mcp__`, then check each hit against the live tool list, not against what the file says.

Specifically for next month:

1. **Close out the deferred denylist item.** It is the only open decision. If the capitalised-vs-lowercase question and the glob question got answered, apply the fix; if not, ask again, because it does not get better on its own.
2. **Re-read `skill://index.json` and diff it against what the framework names.** It went 12 → 15 in five weeks. The question is never "did they rename something", it is "did they ship a skill that makes one of our files redundant, or that an agent here needs and cannot reach".
3. **Hold `figma-plugin-api` §3 to its new exit condition.** It now says: if the vendor documents the variant-switch invalidation case, delete the section. Check that specifically. §1, §2 and §4 are the durable core — do not re-litigate them, just confirm the vendor still has nothing on comments, seats, or desync.
4. **Keep reading `doctor.py` output with the cloud caveat in hand.** Every `~/` path it flags will look like an error and almost certainly isn't. Do not spend the run on them, and do not "fix" them by editing `project.json` to point somewhere that exists in a container.
5. **Recommending nothing remains a valid outcome.** Five small changes this month, none of them structural. If next month is genuinely quiet, say so in one paragraph and stop.
