---
id: "fundamental-visual-redesign"
title: "Fundamental Visual Redesign"
type: "prompt"
primary_category: "design"
categories: ["design"]
subcategory: "redesign"
when_to_use: "Use when the agent keeps changing colors or spacing but the design still looks the same"
search_terms: ["fundamental-visual-redesign", "design", "redesign", "design-architecture", "fundamental", "layout-architecture", "not-restyle", "visual", "visual-hierarchy"]
inputs: ["TARGET", "CONSTRAINTS"]
output: "A materially redesigned target that preserves the stated requirements."
mode: "edit"
capabilities: ["visual-inspection"]
related: ["style-guided-redesign", "visual-identity-redesign"]
aliases: ["design/visual-redesign/fundamental-visual-redesign.md", "fundamental-visual-redesign.md"]
---

# Fundamental Visual Redesign

Use when the agent keeps changing colors or spacing but the design still looks the same.

**Type:** prompt · **Mode:** edit · **ID:** `fundamental-visual-redesign`

**Expected output:** A materially redesigned target that preserves the stated requirements.

**Not for:** A locked layout, CSS-only change, or strict existing-system polish.

## Inputs

Replace every listed placeholder. For an optional source, enter `None` when it is unavailable.

| Placeholder | What to provide | Example |
| --- | --- | --- |
| `{{TARGET}}` | Page, section, screenshot, HTML, or component to redesign. | Existing product hero and its HTML/CSS. |
| `{{CONSTRAINTS}}` | Required copy, links, behavior, brand rules, and deliverable format. | Preserve all SEO text, pricing, CTA URLs, and form behavior; return HTML. |

## Prompt

Copy the block below, not the metadata or usage notes.

<!-- prompt:start -->
````text
Design target:
{{TARGET}}

Content, brand, and functional constraints:
{{CONSTRAINTS}}

Create a fundamental redesign, not a visual refresh. Treat the current design as a content and functionality reference, not a layout to preserve.

Inventory what must survive. Then replace the layout architecture, component structure, visual hierarchy, proportions, and main visual concept. Avoid reusing the original composition, card model, pricing placement, central visual arrangement, pill badges, gradient treatment, spacing rhythm, or CTA arrangement unless explicitly required.

Preserve all required content, factual claims, pricing, links, and working functionality. Restructure their presentation without silently dropping or inventing content. Apply supplied brand constraints.

Compare the result with the original: a palette swap or minor rearrangement is not sufficient. If it still repeats the dominant old structure, revise the design. Check the relevant responsive states and accessibility of the new composition.

Return the redesigned target in the medium supplied or explicitly requested, with concise preservation and verification notes. Do not claim implementation when only a visual concept was produced.
````
<!-- prompt:end -->

## Usage notes

Supply the actual referenced material. A filename or URL does not grant the assistant file, browser, account, or edit access.

**Relevant capabilities:** `visual-inspection`. These are requirements or conditional needs, not tools installed by this file.

## Related entries

- [Style-Guided Redesign](../style-transfer/style-guided-redesign.md) — Use when the target page should be structurally redesigned, but inside the reference style system.
- [Visual Identity Redesign](visual-identity-redesign.md) — Use when the layout changed but the colors, glow, gradients, or atmosphere are still too similar.

[Browse the catalog](../../../CATALOG.md) · [Usage guide](../../../docs/usage.md)
