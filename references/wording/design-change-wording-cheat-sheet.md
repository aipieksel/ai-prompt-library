---
id: "design-change-wording-cheat-sheet"
title: "Design Change Wording Cheat Sheet"
type: "reference"
primary_category: "design"
categories: ["design"]
subcategory: "wording"
when_to_use: "Use as a reference when giving design feedback to an agent"
search_terms: ["design-change-wording-cheat-sheet", "design", "wording", "change", "design-feedback", "layout", "phrases", "ui-polish", "visual-quality"]
inputs: []
output: "Selected wording to add to a concrete task; no standalone deliverable."
mode: "reference"
capabilities: []
related: ["preserve-existing-system", "fundamental-visual-redesign", "minimal-scope-change"]
aliases: ["design/design-wording/design-change-wording-cheat-sheet.md", "design-change-wording-cheat-sheet.md"]
---

# Design Change Wording Cheat Sheet

Use as a reference when giving design feedback to an agent.

**Type:** reference · **Mode:** reference · **ID:** `design-change-wording-cheat-sheet`

**Expected output:** Selected wording to add to a concrete task; no standalone deliverable.

**Not for:** Running the entire collection as a single prompt.

## Inputs

No placeholders. Select the wording relevant to the authorized task.

## Reference

Copy the block below, not the metadata or usage notes.

<!-- prompt:start -->
````text
Choose the line that describes the authorized change; do not paste this entire menu as one instruction.

Preserving a layout and replacing its architecture are different tasks. Likewise, full-file output and a minimal patch are alternatives. Keep required content and behavior unless the main brief explicitly authorizes changing them.

Use these labels and sentences when giving design feedback.

## Bigger Change Needed

### Fundamental redesign
I want a fundamental redesign, not a restyle. Preserve the required content and functionality, but replace the layout architecture, component structure, visual hierarchy, proportions, and visual concept so it looks clearly different at first glance.

### Too similar to the original
This is still too close to the original. Do not reuse the same composition, component model, visual metaphor, spacing rhythm, color treatment, or CTA arrangement. Redesign it from first principles.

### Theme changed but design stayed the same
You changed the surface styling, but not the design architecture. Redesign the structure, layout, hierarchy, and main visual concept, not only the colors, shadows, and spacing.

## Visual Identity / Color

### Same colors again
The layout changed, but the visual identity is still too close. Replace the current color palette, gradient language, glow colors, background treatment, card colors, and accent distribution with a clearly different direction.

### Too glow-heavy
Reduce the glow-heavy treatment. Use glow only where it adds focus or depth. Replace excessive blur, neon, and bloom effects with cleaner contrast, sharper surfaces, and controlled lighting.

### Too generic gradient
Replace the generic gradient treatment with a more intentional background system. The background should support the content, add atmosphere, and not feel like a default SaaS template.

## Layout / Composition

### Weak layout
Rework the layout architecture. Improve structure, proportions, content flow, section balance, column relationships, and component placement. Do not only move items slightly.

### Poor alignment
Fix the alignment precisely. Elements should line up cleanly across columns, cards, text blocks, buttons, icons, and section edges. Remove visual drift and uneven offsets.

### Bad spacing
Refine the spacing system. Improve vertical rhythm, padding, gaps, section breathing room, and alignment consistency. Do not randomly add space; make it intentional and balanced.

### Too much empty space
Reduce wasted space while preserving readability. Tighten excessive padding, close unnecessary gaps, improve grouping, and make the layout feel more efficient without becoming cramped.

### Too cramped
Give the layout more breathing room. Increase spacing around important content, improve section rhythm, reduce cramped groupings, and make the design easier to scan.

## Visual Quality

### Cluttered design
Reduce visual clutter without making the design empty. Remove only unnecessary decoration, simplify repeated visual details, improve grouping, increase breathing room, and make the key content easier to scan.

### Boring design
Make the design more visually interesting without adding clutter. Introduce a stronger visual concept, better composition, more intentional contrast, subtle depth, and a distinctive focal component.

### Cheap-looking design
Make this feel more premium and considered. Improve spacing, proportions, typography, contrast, surface treatment, and visual restraint. Avoid cheap gradients, oversized effects, generic cards, and template-like patterns.

### Template-looking design
Make this feel custom-designed, not like a generic template. Avoid predictable card grids, stock-looking gradients, repeated pill badges, generic SaaS blocks, and common landing-page patterns unless necessary.

### Flat design
Add visual depth without clutter. Use layering, surface contrast, subtle elevation, background separation, and focal components to make the design feel more dimensional.

## Hierarchy / Readability

### Weak hierarchy
Improve the visual hierarchy. Make it immediately clear what the user should notice first, second, and third. Adjust size, weight, spacing, contrast, placement, and grouping so the layout reads naturally.

### Text hard to read
Improve readability. Refine paragraph width, line height, text contrast, spacing between text groups, and heading-to-body relationships so the content is easier to scan.

### CTA not obvious
Improve the conversion flow. Make the primary CTA clearer, reduce distractions around it, strengthen the value proposition, improve the presentation of verified proof points, and guide the eye naturally toward action.
````
<!-- prompt:end -->

## Usage notes

Select compatible excerpts. Verification language requires actual evidence, not a guarantee of correctness.

## Related entries

- [Preserve Existing System](../../modifiers/preserve-existing-system.md) — Use when the agent must fix or improve something without changing the surrounding system.
- [Fundamental Visual Redesign](../../prompts/design/redesign/fundamental-visual-redesign.md) — Use when the agent keeps changing colors or spacing but the design still looks the same.
- [Minimal Scope Change](../../modifiers/minimal-scope-change.md) — Use when the agent keeps changing unrelated code, styling, or behavior.

[Browse the catalog](../../CATALOG.md) · [Usage guide](../../docs/usage.md)
