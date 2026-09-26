---
id: "apply-reference-style"
title: "Apply Reference Style"
type: "prompt"
primary_category: "design"
categories: ["design"]
subcategory: "style-transfer"
when_to_use: "Use when the current design should keep its content and functionality but visually match a reference style"
search_terms: ["apply-reference-style", "design", "style-transfer", "apply", "design-system", "keep-content", "reference", "restyle-current-design", "style", "style-source"]
inputs: ["STYLE_REFERENCE", "TARGET"]
output: "A complete restyled target with the required CSS."
mode: "edit"
capabilities: ["file-access", "visual-inspection"]
related: ["reference-style-transfer-to-target-html", "style-guided-redesign"]
aliases: ["design/design-system-style-transfer/apply-reference-style.md", "apply-reference-style.md"]
---

# Apply Reference Style

Use when the current design should keep its content and functionality but visually match a reference style.

**Type:** prompt · **Mode:** edit · **ID:** `apply-reference-style`

**Expected output:** A complete restyled target with the required CSS.

**Not for:** Replacing the target layout; use Style-Guided Redesign for that.

## Inputs

Replace every listed placeholder. For an optional source, enter `None` when it is unavailable.

| Placeholder | What to provide | Example |
| --- | --- | --- |
| `{{STYLE_REFERENCE}}` | Approved visual reference file. | approved-style.html |
| `{{TARGET}}` | The file that must keep its content and structure. | product-page.html |

## Prompt

Copy the block below, not the metadata or usage notes.

<!-- prompt:start -->
````text
Style reference:
{{STYLE_REFERENCE}}

Target to restyle:
{{TARGET}}

Restyle the target so it follows the reference's visual language. The reference controls appearance; the target controls content, structure, purpose, and behavior.

Preserve the target's content, section inventory, ordering, links, controls, IDs, classes, data attributes, scripts, accessibility attributes, and functional behavior. Do not import reference copy or unrelated sections. Do not silently remove a component to make the transfer easier.

Extract the actual style system before applying it: colors, typography, spacing rhythm, density, radius, borders, surfaces, shadows, backgrounds, component anatomy, state treatments, and responsive rules. Apply these through the real component selectors, not just root-variable replacements. Keep source content and target behavior distinct from visual evidence.

Check all affected regions and states, including navigation, headings, cards, badges, buttons, forms, tables, FAQs, overlays, footers, hover/focus, and responsive layouts where present. Do not claim rendered verification without inspecting the rendered result.

Keep the existing layout architecture. Adapt the reference's reusable styling to the target rather than copying its composition or merging the two pages.

Return the complete restyled target and any stylesheet required to use it.
````
<!-- prompt:end -->

## Usage notes

Supply the actual referenced material. A filename or URL does not grant the assistant file, browser, account, or edit access.

**Relevant capabilities:** `file-access`, `visual-inspection`. These are requirements or conditional needs, not tools installed by this file.

## Related entries

- [Reference Style Transfer to Target HTML](reference-style-transfer-to-target-html.md) — Use when a target HTML file should keep its content and components but inherit the style of a URL or second HTML file.
- [Style-Guided Redesign](style-guided-redesign.md) — Use when the target page should be structurally redesigned, but inside the reference style system.

[Browse the catalog](../../../CATALOG.md) · [Usage guide](../../../docs/usage.md)
