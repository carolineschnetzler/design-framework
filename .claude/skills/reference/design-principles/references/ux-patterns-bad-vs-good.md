# UX Patterns — Bad vs. Good

Applied design rules from the user's reference collection. Each rule shows what NOT to do and what to do instead. Agents must follow the "good" patterns.

---

## Layout and Eye Flow

### Z-Shaped Scan Pattern (Gutenberg Principle)
Users scan content in a Z-shaped movement: top-left → top-right → bottom-left → bottom-right.

- **Do:** Place primary info/branding top-left, visual anchor top-right, supporting content bottom-left, CTA bottom-right.
- **Don't:** Place key content outside the Z-path (centered elements with empty corners, important actions in unexpected positions).

### Action Placement — Bottom, Not Top
Users scan content first, then decide to act.

- **Do:** Place primary action buttons at the END of the content flow. After the user has read/scanned, the button is right there.
- **Don't:** Put primary action buttons at the top of a content area. This forces the eye to scan down, then backtrack up to act.

---

## Typography

### Balanced Type Scaling
The ratio between hierarchy levels matters more than the absolute sizes.

- **Do:** Keep heading-to-body ratio moderate and consistent (24px heading / 16px subheading / 14px body). Balance button text with body text.
- **Don't:** Over-scale headings while shrinking supporting text (28px heading with 11px subheading). Extreme ratios make the smaller text feel like an afterthought.

---

## Information Architecture

### Eliminate Redundant Labels
If the layout makes meaning obvious, the label is noise.

- **Do:** "Margherita pizza" as bold heading, "$15" and "★ 4.3" inline below, description as body text. The position and style communicate what each piece of data is.
- **Don't:** "Name: Margherita pizza / Price: $15 / Ratings: 4.3 / Details: A classic..." — every field explicitly labeled in a key-value list when context makes labels unnecessary.

### Show, Don't Label
When data can be communicated visually, prefer visual encoding over text labels.

- **Do:** Progress ring around avatar to show completion %, icon + number pairs with a divider between groups, stacked avatar group for participants.
- **Don't:** "Profile completed: 67%" as a text line. "Name: Alexander / Level: Beginner / Rank: 32 / Points: 459" as a plain text list.

---

## Spacing and Containers

### Overlapping Elements Save Space
Elements that relate to each other can share visual boundaries.

- **Do:** Avatar overlapping the hero image edge, stacked avatar groups with negative margin, timestamps overlaid on images.
- **Don't:** Separate every element with full margins and gaps when overlap would communicate relationship AND save space.

### Remove Unnecessary Borders
Borders around non-interactive metadata add visual noise without adding clarity.

- **Do:** "🏠 House · 🛏 2 beds · 🛁 1 bath · 🚗 1 garage" as plain icons + text in a horizontal row.
- **Don't:** Each metadata item in its own bordered box when it's informational, not interactive.

### Size and Spacing Create Hierarchy
When elements feel cramped and same-sized, hierarchy disappears.

- **Do:** Larger avatar, larger name text, full-width buttons, generous spacing between list items. Let important elements be bigger.
- **Don't:** Uniform small sizing on everything, tight spacing that treats all elements as equal. If everything is the same size, nothing is important.

---

## Summary Rule for Agents

Before finalizing any layout, ask:
1. Does the eye follow a natural scan pattern (Z or F)?
2. Is the primary action at the end of the content flow?
3. Can any labels be removed because the layout makes meaning obvious?
4. Can any bordered containers be removed because spacing alone creates grouping?
5. Is the type hierarchy balanced (no extreme ratio jumps)?
6. Could any elements overlap to save space and show relationship?
