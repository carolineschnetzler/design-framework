---
name: figma-plugin-api
description: The small set of Figma behaviors this framework has hit that the official Figma skills do not cover — comments, editor seats, subtree regeneration, and the sync failure that causes data loss. Load alongside the official figma-use skill, never instead of it.
---

# Figma — What the Official Skills Don't Cover

**Load `figma-use` first. It is the source of truth for the Plugin API.**

Figma ships and maintains its own skills (`figma-use`, `figma-generate-design`, `figma-generate-library`, `figma-code-connect`, `figma-design-to-code`, and others), including a large, frequently-updated gotchas reference. Figma's own documentation instructs clients to install them. They are versioned with the API; this file is not.

**So this file is deliberately short.** It holds only what this framework has hit that the official references do not address. If something here ever starts contradicting the official skills, **the official skills win** and the entry here should be deleted.

Everything about node creation, component properties, variants, auto layout order, text and fonts, variables and modes, paint binding, cleanup, and async batching is covered upstream. Do not duplicate it here.

---

## 1. Comments are not in the Plugin API at all

The word does not appear in it, and no Figma MCP tool exposes comments. They come from the REST API with a personal access token (`file_comments:read`, `file_comments:write`, `file_content:read`):

```
curl -s -H "X-Figma-Token: $FIGMA_TOKEN" \
  "https://api.figma.com/v1/files/<FILE_KEY>/comments"
```

Each comment carries `message`, `user.handle`, `resolved_at`, `parent_id`, `order_id`, and `client_meta.node_id`, so a pin resolves to a real layer.

**Deleting a comment through REST is not reversible.** Never delete or resolve one unless the user explicitly asks. See the `design-feedback` workflow for how comment batches are worked.

---

## 2. Editor seats fail in a way that looks like a code bug

A file in a team where the user holds a **View seat** refuses every write and caps reads at a low monthly quota. Duplicating the file does not help — the seat follows the team, not the file.

**Detect it early.** An unexplained permission error on a *first* write is usually the seat, not the script. The path forward is a local plugin running in the desktop app under the user's own session, or a copy in a team where they hold an Editor seat. Do not spend a session debugging code that was never going to be allowed to run.

---

## 3. The regeneration heuristic

Most "the write didn't work" bugs are not write failures, they are **stale node references**. Several operations regenerate a node's subtree, and a reference captured beforehand still resolves while pointing at nothing on screen. The symptom is distinctive: the first `setProperties` works, a second call on the same reference silently does nothing.

Operations that do this include switching an instance's variant, setting a property on a nested instance, and changing the visibility or structure of a main component's children.

**The rule:** never hold node references across a mutation. Capture names and IDs before mutating, re-query by ID after, and when updating many instances re-query inside the loop rather than iterating a list captured up front.

---

## 4. When the plugin and the server disagree, stop writing

If `get_screenshot` renders a node that `use_figma`'s `getNodeByIdAsync` says does not exist, the desktop plugin's document is **out of sync with the saved file**. Continuing to write risks clobbering saved work.

This has caused real data loss in this framework: a frame was rebuilt from scratch after a multiplayer save conflict silently discarded it.

**Stop. Ask the user to reload the desktop app and close extra editors. Re-verify before writing anything else.**

---

## 5. Node IDs are snapshots, not addresses

IDs shift when nodes are renamed, moved, regenerated, or recreated. **Find frames, sections, and components by name.** Any ID written into a document is a record of where something was, not a way to reach it — treat every stored ID as needing verification before use.

This is also why design docs in this framework never carry screen inventories: see the note in `templates/design-state.md`.
