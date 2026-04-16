# UX Laws and Principles

Core principles that all design agents must consider when making decisions. Each principle includes actionable rules — not just theory.

---

## Perception and Aesthetics

### Aesthetic-Usability Effect
Users tolerate minor usability problems when an interface looks good. Visual appeal creates a halo effect that makes products feel like they work better — but beauty can mask real problems.

- Use visual polish to build user patience for minor friction, but never as a substitute for solving structural usability problems.
- Ensure aesthetics enhance task completion (clear hierarchy, readable type, intentional spacing) rather than decorating over broken flows.

---

## Cognitive Load and Memory

### Miller's Law — Working Memory Limits
The average person holds 4-7 chunks in working memory, each fading within 20-30 seconds. Users struggle with recall but excel at recognition.

- Display no more than 4-7 discrete pieces of information per view.
- Externalize memory with persistent UI elements (comparison tables, saved state, breadcrumbs, form preservation) so users never need to memorize across screens.

### Chunking
Breaking information into small groups (3-5 items) dramatically improves processing speed and retention.

- Group data that must be recalled or entered (IDs, codes, numbers) into chunks of 3-5 separated by visual delimiters.
- Cluster related items into distinct visual groups (cards, sections, whitespace breaks) so users process one cluster at a time.

### Working Memory
Working memory holds 4-7 chunks, fading in 20-30 seconds. Interfaces should support recognition over recall.

- Present only necessary information per view.
- Shift memory burden from the user to the system — persistent state, visible history, comparison tools.

### Reducing Cognitive Load
Every unnecessary element, decision point, or novel pattern consumes capacity that should go toward the user's actual goal.

- Every element in a layout must earn its place. If removing it doesn't hurt comprehension or task completion, remove it.
- Use smart defaults and pre-filled values to eliminate decisions wherever possible.

---

## Decision Making

### Hick's Law — Choice Overload
As choices increase, decision time increases and satisfaction drops. More features attract users initially but hurt them during actual use.

- Default to the minimum viable set of options for the primary use case. Add complexity only when justified.
- When multiple options are unavoidable, use progressive disclosure — common path first, edge cases behind deliberate interaction.

### Simplicity vs. Choice
Users are drawn to feature-rich products but perform worse and feel worse using them. Excessive options create decision paralysis.

- Break complex workflows into sequential screens with minimal choices per stage.
- Categorize ruthlessly — group related functions hierarchically rather than displaying all options at once.

### Decision Framing
Identical data leads to different decisions depending on whether it's framed as gain or loss. The frame drives the conclusion more than the data.

- When presenting metrics or states, deliberately choose framing that aligns with the intended action ("3 steps remaining" vs. "60% complete").
- When evaluating your own design decisions, restate findings in both positive and negative frames before acting.

### Occam's Razor
Among competing solutions that work equally well, choose the one with fewest assumptions and elements.

- Audit every component — remove anything that doesn't directly serve the core purpose.
- Launch with the fewest features needed. Add only what users demonstrably require.

---

## Visual Grouping (Gestalt)

### Law of Proximity
Objects near each other are perceived as a group. Spatial proximity is one of the strongest cues for visual grouping.

- Cluster related elements with tight spacing to signal shared purpose.
- Increase spacing between unrelated blocks so users perceive them as separate functional units.

### Law of Similarity
Elements with similar visual properties (color, shape, size) are perceived as belonging to the same group.

- Use consistent visual properties across elements that share the same function.
- Visually differentiate interactive elements from static content to signal distinct behavior.

### Law of Common Region
Items within a shared visual boundary are perceived as a group and assumed to share functionality.

- Use containers (borders, background fills) to group related elements only when whitespace alone creates ambiguity.
- Reserve explicit boundaries for high-priority relationships — overuse creates visual clutter and false stopping points.

### Law of Uniform Connectedness
Elements visually connected by lines, colors, frames, or linking treatments are perceived as more related than unconnected elements.

- Apply consistent visual treatments (shared background, borders, connecting lines) to reinforce functional grouping.
- Use connecting elements strategically for hierarchy — don't connect everything, or nothing stands out.

---

## Mental Models and Familiarity

### Jakob's Law
Users prefer your product to work the same way as the other products they already know.

- Default to established UI conventions (common layouts, standard controls, familiar navigation) rather than inventing novel interactions without justification.
- When redesigning, provide transitional states that let users acclimate gradually.

### Mental Models
Users' beliefs about how a system works — shaped by prior experience — drive their expectations regardless of how it actually works.

- Align with established patterns. Leverage existing mental models from familiar products.
- When deviating from convention, clarify system behavior before users form incorrect assumptions.

---

## Flow and Motivation

### Designing for Flow
Flow state requires: the next action is always obvious, feedback is immediate, visual noise is eliminated.

- Design linear task flows with a single obvious next action at each step. Hide secondary actions that would force a choice.
- Provide visible feedback within 100ms of any user action. If the system is slow, show an immediate placeholder.

### Goal-Gradient Effect
People accelerate effort as they approach a goal. Even the illusion of progress increases motivation to complete a task.

- Make progress visible at every stage of multi-step flows. Use progress bars, step counts, or completion percentages.
- Where possible, give users a head start (pre-fill the first step, start a progress bar at 10%) to trigger acceleration earlier.

---

## Memory and Sequence

### Serial Position Effect
Users best remember the first and last items in a series. Middle items are recalled least.

- Place essential actions and key information at the beginning and end of navigation, lists, and menus.
- Reserve middle positions for supplementary or lower-priority content.

### Peak-End Rule
People judge an experience by its most intense moment and its ending, not the average of every moment.

- Design moments of delight or clarity at critical junctures and especially at task completion.
- Ensure final touchpoints (confirmations, results, completion screens) deliver satisfaction — these become the lasting memory.
