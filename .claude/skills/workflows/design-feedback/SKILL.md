---
name: design-feedback
description: "Work a batch of design feedback the user left by pointing at things — native Figma comments, or pins dropped in a running prototype. Use when they say 'read my Figma comments', 'work my comments', 'here are my notes', or paste a numbered block of annotations. Treats each item as a change request and reports back per item."
---

# Design Feedback Workflow

Triggered by "read my comments", "work my notes", or a pasted block of numbered annotations.

---

## Why this exists

Reviewing by pointing beats reviewing by describing, and reviewing in one pass beats interrupting to message each note separately. The user drops feedback across a file or a running prototype, then hands the whole batch over at once. Your job is to work the list, not to negotiate it item by item.

Treat every item as a change request against the exact element it is attached to.

---

## Source 1 — Native Figma comments

The Plugin API cannot see comments. They come from the REST API.

```
curl -s -H "X-Figma-Token: $FIGMA_TOKEN" \
  "https://api.figma.com/v1/files/<FILE_KEY>/comments"
```

The token is a personal access token with `file_comments:read` and `file_content:read`. Each comment carries `message`, `user.handle`, `resolved_at`, `parent_id`, `order_id`, and `client_meta.node_id` — so a pin resolves to an actual layer, which is more precise than any description.

### Which comments to act on

1. **Only unresolved threads.** Resolution is **thread-level**: walk `parent_id` to the root and skip the whole thread if the root has `resolved_at`. Resolved means done — never re-raise.
2. **Skip threads addressed to a named person other than the user.** Match on the message text at **thread** level, so a reply inside someone else's thread is skipped too. Mentions are stored as the full display name even when typed short.
3. **Do not act on comments authored by other people.** Those are usually someone asking the user a question. **Surface them separately as "waiting on you"** rather than silently ignoring them.
4. **Everything else authored by the user is the work queue.**

### The rule that matters most

**Never delete or resolve a comment.** The user resolves them as they verify the work — an open comment is how they go back and check. Clearing them destroys the review queue, and REST deletion is **not reversible**. Report what was done against each comment and leave every one untouched.

---

## Source 2 — Prototype annotations

A running prototype should ship with an annotation mode: a keypress arms it, hovering names the element from the component tree, clicking drops a numbered pin and opens a note field, and a copy action puts a text block on the clipboard:

```
1. Badge in ModeToggle — "Fast"
   the cost meter should not read as a rating
```

The user pastes that block into chat. Each numbered entry is a separate change request against that exact component.

Two conventions worth keeping when you build one:
- **Its chrome is deliberately not the design system** — monospace on a raw alarming color, so a redline can never be mistaken for product UI. This is the one place raw hex is correct; do not "fix" it to tokens.
- Builds that minify must preserve component names, or the readout degrades to meaningless identifiers.

---

## Process

1. **Pull the batch and list it back** — numbered, each with the element it targets, before changing anything. This catches misreads while they are still cheap.
2. **Group by component.** Several comments often resolve to one component change. Fix at the source, not per instance.
3. **Work the list.** Do not stop for approval between items; the batch *was* the approval. Stop only for an item that turns out to need a design decision the user has not made.
4. **Report per item** — what changed, or why it did not. Match the user's numbering so they can check the list against the file.
5. **Leave the comments alone.** Say which ones are done; let the user resolve them.

---

## Output

- The changes, made at component level where possible
- A per-item report matching the user's numbering
- A separate short list: items that need a decision, and comments from other people waiting on the user
- No comments deleted, no comments resolved
