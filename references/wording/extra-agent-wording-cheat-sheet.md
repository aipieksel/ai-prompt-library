---
id: "extra-agent-wording-cheat-sheet"
title: "Extra Agent Wording Cheat Sheet"
type: "reference"
primary_category: "coding"
categories: ["coding", "design"]
subcategory: "agent-quality"
when_to_use: "Use for quick wording around reference files, content preservation, and implementation behavior"
search_terms: ["extra-agent-wording-cheat-sheet", "coding", "agent-quality", "agent", "output", "phrases", "reference-work", "scope", "style-transfer", "wording"]
inputs: []
output: "Selected wording to add to a concrete task; no standalone deliverable."
mode: "reference"
capabilities: []
related: ["preserve-existing-system", "fundamental-visual-redesign", "minimal-scope-change"]
aliases: ["coding/agent-quality/extra-agent-wording-cheat-sheet.md", "extra-agent-wording-cheat-sheet.md"]
---

# Extra Agent Wording Cheat Sheet

Use for quick wording around reference files, content preservation, and implementation behavior.

**Type:** reference · **Mode:** reference · **ID:** `extra-agent-wording-cheat-sheet`

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

## Infer pattern
Infer the reusable system from the reference instead of hard-coding page-specific details.

## Adapt, don’t copy
Use the reference to understand the style system, but adapt it to the target content and purpose.

## Preserve SEO
Preserve all SEO-critical text, headings, links, pricing, factual claims, and keyword-targeted copy exactly unless I ask for copy changes.

## Move, don’t rewrite
You may rearrange where content appears, but do not rewrite, shorten, remove, or invent content.

## Implicit design system
Treat the file as an implicit design system and continue building from its tokens, spacing, components, and visual language.

## Extend style
Extend the style, not the exact section. Create variation while keeping the same design language.

## Preserve identity
Improve execution while preserving the current visual identity, design language, and component style.

## Change identity
Change the visual direction as well as the structure. Do not preserve the current palette, lighting, gradients, or component atmosphere unless required.

## Avoid generic SaaS
Avoid predictable SaaS patterns like generic card grids, floating pills, vague gradients, and stock dashboard blocks.

## Preserve logic
Do not change working logic while redesigning the UI. Preserve links, forms, scripts, IDs, data attributes, tracking hooks, and event behavior.

## Keep editable
Keep the result editable with real HTML text, CSS-driven visuals, reusable classes, and maintainable markup.

## Full file
Return the full updated target file, ready to paste over the existing file.

## Minimal patch
Return a minimal patch only for the affected sections. Do not rewrite unrelated code.

## Best reference-to-target line
Use the reference file for style and the target file for content. Infer the design system from the reference, then apply it to the target without copying the reference layout blindly, changing the target’s SEO text, or introducing a new visual identity.
````
<!-- prompt:end -->

## Usage notes

Select compatible excerpts. Verification language requires actual evidence, not a guarantee of correctness.

## Related entries

- [Preserve Existing System](../../modifiers/preserve-existing-system.md) — Use when the agent must fix or improve something without changing the surrounding system.
- [Fundamental Visual Redesign](../../prompts/design/redesign/fundamental-visual-redesign.md) — Use when the agent keeps changing colors or spacing but the design still looks the same.
- [Minimal Scope Change](../../modifiers/minimal-scope-change.md) — Use when the agent keeps changing unrelated code, styling, or behavior.

[Browse the catalog](../../CATALOG.md) · [Usage guide](../../docs/usage.md)
