# Projects

One folder per product. The folder is the framework's handle on that product — it is what `/discover`, `/generate-screen`, `/prototype`, `/sync-tokens`, and `/handoff` read before doing anything.

## Starting one

Copy what applies from `../templates/` and fill it in. Nothing is mandatory except `project.json`, which is how the framework knows the project exists and what shape it is.

```
projects/<name>/
  project.json        required — what this is, who implements it, where its docs live
  design-brief.md     problem, users, principles, direction   (/discover writes it)
  design-system.md    tokens, type, spacing, components       (documentation, not truth)
  taste-profile.md    aesthetics specific to this product     (/taste writes it)
  design-state.md     decisions, open questions, design debt
  design-changes.md   engineering changelog                   (/changelog only, opt-in)
  figma.json          file key + page-level node IDs
  prototype.json      host project path, stack, guarded paths
```

## Three rules that keep this useful

**Pointers, not copies.** A project's canonical docs may live outside this repo — in the product's own repo, or wherever the team already keeps them. When they do, `project.json` names them under `canonicalDocs` and the framework reads from there. Never copy a canonical doc into this folder: a copy is a contradiction waiting to happen, and the copy always loses.

**No screen inventory, ever.** The design file is the only source of truth for what screens exist and what their node IDs are. Page-level IDs in `figma.json` are fine because pages are stable. Individual frame and component IDs are not — they shift on rename, move, and regeneration. Any ID written into a document is a snapshot, not an address.

**The design system doc is documentation.** The design file holds the real tokens; `/sync-tokens` generates the code layer from it. When the three disagree, the design file wins and the other two are stale.

## What lives here now

| Project | Shape | Why it's here |
|---|---|---|
| `advpulse` | Dense B2B product UI, two design systems, React prototype | The project the framework grew up around |
| `deepwell` | Product UI, canonical docs external | Contradicts AdvPulse on radius, glass, and accent — which is what keeps cross-project taste memory honest |
| `refuge-linen` | Shopify theme plus a print system, canonical docs external | Broke the React assumption and the write-access assumption |

Three products that disagree with each other is the point. A framework validated against one product is that product's framework.
