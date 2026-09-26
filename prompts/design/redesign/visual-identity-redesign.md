---
id: "visual-identity-redesign"
title: "Visual Identity Redesign"
type: "prompt"
primary_category: "design"
categories: ["design"]
subcategory: "redesign"
when_to_use: "Use when the layout changed but the colors, glow, gradients, or atmosphere are still too similar"
search_terms: ["visual-identity-redesign", "design", "redesign", "atmosphere", "color-direction", "identity", "palette", "surface-treatment", "visual", "visual-identity"]
inputs: ["TARGET", "CONSTRAINTS"]
output: "A redesigned visual identity with preserved required content and behavior."
mode: "edit"
capabilities: ["visual-inspection"]
related: ["fundamental-visual-redesign", "research-palette-showcase"]
aliases: ["design/visual-redesign/visual-identity-redesign.md", "visual-identity-redesign.md"]
---

# Visual Identity Redesign

Use when the layout changed but the colors, glow, gradients, or atmosphere are still too similar.

**Type:** prompt · **Mode:** edit · **ID:** `visual-identity-redesign`

**Expected output:** A redesigned visual identity with preserved required content and behavior.

## Inputs

Replace every listed placeholder. For an optional source, enter `None` when it is unavailable.

| Placeholder | What to provide | Example |
| --- | --- | --- |
| `{{TARGET}}` | Design whose visual identity needs replacement. | Existing page screenshot and implementation. |
| `{{CONSTRAINTS}}` | Required content, facts, functionality, and any fixed brand elements. | Preserve copy and working CTAs; the palette and surfaces may change. |

## Prompt

Copy the block below, not the metadata or usage notes.

<!-- prompt:start -->
````text
Target:
{{TARGET}}

Preservation and brand constraints:
{{CONSTRAINTS}}

Change the visual identity of this section or page, not merely its arrangement. Preserve required content, factual claims, links, pricing, and functionality.

Unless explicitly required by the constraints, replace the existing palette, gradient language, glow colors, background treatment, card colors, accent distribution, lighting, and surfaces. Build a clearly different color direction and visual atmosphere that still fits the product and remains usable.

Do not replace a familiar palette with arbitrary decoration. Define coherent background, text, accent, border, state, and focus roles; verify readable contrast and responsive behavior where possible.

Compare the new and old designs to ensure the result is not the same identity rearranged. Return the updated design or implementation in the requested medium and state what was actually verified.
````
<!-- prompt:end -->

## Usage notes

Supply the actual referenced material. A filename or URL does not grant the assistant file, browser, account, or edit access.

**Relevant capabilities:** `visual-inspection`. These are requirements or conditional needs, not tools installed by this file.

## Related entries

- [Fundamental Visual Redesign](fundamental-visual-redesign.md) — Use when the agent keeps changing colors or spacing but the design still looks the same.
- [Research a Palette and Build Its Showcase](../showcases/research-palette-showcase.md) — Research a product or brand direction and demonstrate the full proposed design system in HTML.

[Browse the catalog](../../../CATALOG.md) · [Usage guide](../../../docs/usage.md)
