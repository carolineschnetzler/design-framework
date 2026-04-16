---
name: retrospective
description: "Post-project reflection that captures learnings and feeds them into cross-project design memory. Use when the user says /retro, 'we're done with this project', 'let's reflect', 'what did we learn', or at the end of a major project phase."
---

# Retrospective Workflow

Triggered by `/retro` or when the user says a project (or a significant phase) is complete.

---

## Purpose

Capture what was learned so future projects start smarter. The retrospective feeds into two places: the project's own `design-state.md` and the cross-project design memory at `taste-profile.md`.

---

## Process

### Step 1: Review the Project Arc

Read through the project's files to reconstruct the journey:
- `design-brief.md` — What was the original problem and direction?
- `design-state.md` — What decisions were made along the way? What changed?
- `taste-profile.md` — How did taste evolve during the project?
- The Figma file — What was actually built?

Summarize the arc: where we started, what shifted, where we ended up.

### Step 2: Reflect with the user

Ask the user structured questions:

**On the design itself:**
- What worked best in the final design?
- What would you do differently if starting over?
- Were the principles useful? Did any need revision mid-project?
- Did the taste profile accurately capture what you wanted?

**On the process:**
- Which workflows were most useful?
- Where did the framework slow you down or get in the way?
- Were there decisions that took too long or needed too many iterations?
- What felt missing?

**On taste evolution:**
- Did your aesthetic preferences shift during this project?
- Are there new strong opinions to carry into future projects?
- Are there things you tried that you'd never do again?

### Step 3: Extract Learnings

From the user's answers, identify:

**Taste learnings:**
- New strong opinions (confirmed across decisions, should carry to all future projects)
- New soft patterns (appeared but not yet confirmed — carry as suggestions)
- New anti-patterns (explicitly rejected — carry as exclusions)
- Refined existing opinions (sharper or softened based on this project)

**Process learnings:**
- What worked about the workflow and should be preserved
- What was friction and might need framework adjustment

**Design patterns:**
- Solutions that worked well and could be reused
- Approaches that failed and should be avoided

### Step 4: Update Cross-Project Memory

Update `taste-profile.md`:
- Add new strong opinions to the strong opinions section
- Add new soft patterns to the soft patterns section
- Add new anti-patterns to the anti-patterns section
- Move soft patterns to strong opinions if this project confirmed them
- Update the project history section with a summary of this project's key taste decisions

### Step 5: Close the Project Record

Append a retrospective summary to `projects/<name>/design-state.md`:
- What was delivered
- Key taste learnings
- Process notes for future reference

### Step 6: Run Audit (Optional)

At the end of retrospective, offer to run `/audit` to check if the framework should be updated based on new Claude Code or Figma MCP capabilities released since the project started.

---

## Output

- Updated `taste-profile.md` with new learnings
- Retrospective summary appended to `projects/<name>/design-state.md`
- Process feedback noted (for the user to act on if they want to update the framework)

---

## Why This Matters

Without retrospective, every project starts from zero. The taste profile drifts because nobody recorded what was learned. The same mistakes get made twice. This workflow is what makes the framework compound over time.
