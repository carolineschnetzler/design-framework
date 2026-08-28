---
name: changelog
description: "Append a design change to the project's running log for the implementing engineer. STRICTLY opt-in — only run when the user explicitly says to log something for the engineer. Never offer it, never include it in broader doc updates."
---

# Engineering Changelog

Appends to `projects/<name>/design-changes.md`, the running log of design changes the implementing engineer needs to pick up.

---

## This skill is opt-in and the rule is absolute

**Only append when the user explicitly asks**, in words like "add this to the list for [engineer]" or "log this for the dev".

- **Never offer it.** Do not ask "want me to log this?" Do not suggest it as a next step.
- **Never include it in broad doc-update requests.** "Update the docs", "update the design system files", "log this somewhere" do **not** include this file.
- **If the phrasing is ambiguous, do nothing** and wait for an explicit instruction.

**Why:** the log is a communication channel the user owns. They decide what engineering sees and when. Volunteering entries takes that decision away from them and has been corrected more than once.

---

## What to write

Append a dated section. Lead with the model or the rule, then the components, then the behavior — an engineer needs to understand *why* the change is shaped this way before a list of node changes means anything.

```markdown
## YYYY-MM-DD — <short title>

**The model, first, because everything else follows from it.**
<One paragraph: the rule or concept the change encodes.>

**New components**
| Component | Notes |
|---|---|

**Changed components**
| Component | Change |
|---|---|

**Behaviour to build to**
- <Rules that are not visible in a static frame: what decays, what sorts, what defaults, what is disabled when.>

**Open, needs a decision**
- <Anything contradictory or unresolved. Say so rather than papering over it.>
```

---

## Rules for the entries

- **Name the behavior a frame cannot show.** Defaults, disabled conditions, what happens on the second run, what sorting applies to. This is the part engineers cannot infer.
- **Answer their open questions in the log** when the answer came out of a design change, and reference their question.
- **Flag contradictions rather than hiding them.** "These two screens disagree about X, worth settling before you build it" is more useful than a confident wrong spec.
- **Use the project's copy rules** for any user-facing string quoted in the entry.
- Reference components and frames **by name**, never by raw node ID.
