---
id: "best-default-prompt-lines"
title: "Best Default Prompt Lines"
type: "reference"
primary_category: "coding"
categories: ["coding", "design"]
subcategory: "agent-quality"
when_to_use: "Use when you want quick reusable lines instead of full prompts"
search_terms: ["best-default-prompt-lines", "coding", "agent-quality", "best-defaults", "default", "lines", "phrases", "prompt", "quick-lines"]
inputs: []
output: "Selected wording to add to a concrete task; no standalone deliverable."
mode: "reference"
capabilities: []
related: ["preserve-existing-system", "fundamental-visual-redesign", "minimal-scope-change"]
aliases: ["coding/agent-quality/best-default-prompt-lines.md", "best-default-prompt-lines.md"]
---

# Best Default Prompt Lines

Use when you want quick reusable lines instead of full prompts.

**Type:** reference · **Mode:** reference · **ID:** `best-default-prompt-lines`

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

## General agent work
Be rigorous and deliberate. Inspect the actual files, identify the system from the supplied evidence, preserve required content and functionality, label assumptions and resolve material uncertainty, make the implementation complete, verify the result, and return only the final output in the requested format.

## General design work
Be rigorous with the design. Preserve the required content and functionality, but improve the layout, hierarchy, spacing, alignment, typography, components, and responsive behavior with intention.

## Fundamental redesign
Create a fundamental redesign, not a restyle. Preserve only the content, required functionality, and brand constraints. Replace the layout architecture, component structure, visual hierarchy, proportions, and visual metaphor so the result is clearly different from the original at first glance.

## Hero/component visual
Replace the current hero visual with a completely different dynamic HTML/CSS component. Do not reuse the existing component structure, shape language, layout, glow, floating labels, or visual metaphor.

## Reference style work
Use the reference file for style and the target file for content. Infer the design system from the reference, then apply it to the target without copying the reference layout blindly or introducing a new visual identity.

## Code work
Be rigorous and codebase-first. Inspect the relevant files, understand the existing architecture and patterns, then implement the smallest robust solution that fits the current system.
````
<!-- prompt:end -->

## Usage notes

Select compatible excerpts. Verification language requires actual evidence, not a guarantee of correctness.

## Related entries

- [Preserve Existing System](../../modifiers/preserve-existing-system.md) — Use when the agent must fix or improve something without changing the surrounding system.
- [Fundamental Visual Redesign](../../prompts/design/redesign/fundamental-visual-redesign.md) — Use when the agent keeps changing colors or spacing but the design still looks the same.
- [Minimal Scope Change](../../modifiers/minimal-scope-change.md) — Use when the agent keeps changing unrelated code, styling, or behavior.

[Browse the catalog](../../CATALOG.md) · [Usage guide](../../docs/usage.md)
