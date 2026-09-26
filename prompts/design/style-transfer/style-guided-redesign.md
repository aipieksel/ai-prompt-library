---
id: "style-guided-redesign"
title: "Style-Guided Redesign"
type: "prompt"
primary_category: "design"
categories: ["design"]
subcategory: "style-transfer"
when_to_use: "Use when the target page should be structurally redesigned, but inside the reference style system"
search_terms: ["style-guided-redesign", "design", "style-transfer", "guided", "not-style-transfer", "redesign", "redesign-inside-reference-style", "style"]
inputs: ["STYLE_REFERENCE", "TARGET"]
output: "A structurally redesigned implementation within the reference visual system."
mode: "edit"
capabilities: ["file-access", "visual-inspection"]
related: ["fundamental-visual-redesign", "apply-reference-style"]
aliases: ["design/design-system-style-transfer/style-guided-redesign.md", "style-guided-redesign.md"]
---

# Style-Guided Redesign

Use when the target page should be structurally redesigned, but inside the reference style system.

**Type:** prompt · **Mode:** edit · **ID:** `style-guided-redesign`

**Expected output:** A structurally redesigned implementation within the reference visual system.

**Not for:** Locked markup or a layout-preserving style transfer.

## Inputs

Replace every listed placeholder. For an optional source, enter `None` when it is unavailable.

| Placeholder | What to provide | Example |
| --- | --- | --- |
| `{{STYLE_REFERENCE}}` | Approved design-system file, reference HTML, or accessible website. | DESIGN.md |
| `{{TARGET}}` | Target page plus any locked content or functional constraints. | target.html; keep all SEO copy, links, and existing form behavior. |

## Prompt

Copy the block below, not the metadata or usage notes.

<!-- prompt:start -->
````text
Reference design system:
{{STYLE_REFERENCE}}

Target page and required constraints:
{{TARGET}}

Fundamentally redesign the target's structure inside the reference's visual system. This is not a simple restyle.

Inspect the target to inventory required content, SEO wording, links, controls, factual claims, and functionality. Inspect the reference to extract colors, typography, spacing, radius, surfaces, buttons, cards, shadows, backgrounds, interactions, density, and visual atmosphere.

Replace the target's layout architecture, section composition, component arrangements, visual hierarchy, proportions, and repeated patterns where permitted. You may move and regroup required content; do not delete, shorten, rewrite, or invent it without explicit permission. Preserve interaction outcomes and all hooks required by the implementation, updating references safely if an approved structural change requires it.

The result must look structurally different while remaining native to the reference system. Check content coverage, functional continuity, responsive behavior, and visual fit.

Return the complete redesigned implementation with a concise account of structural changes and verification.
````
<!-- prompt:end -->

## Usage notes

Supply the actual referenced material. A filename or URL does not grant the assistant file, browser, account, or edit access.

**Relevant capabilities:** `file-access`, `visual-inspection`. These are requirements or conditional needs, not tools installed by this file.

## Related entries

- [Fundamental Visual Redesign](../redesign/fundamental-visual-redesign.md) — Use when the agent keeps changing colors or spacing but the design still looks the same.
- [Apply Reference Style](apply-reference-style.md) — Use when the current design should keep its content and functionality but visually match a reference style.

[Browse the catalog](../../../CATALOG.md) · [Usage guide](../../../docs/usage.md)
