---
id: "reference-style-transfer-to-target-html"
title: "Reference Style Transfer to Target HTML"
type: "prompt"
primary_category: "design"
categories: ["design"]
subcategory: "style-transfer"
when_to_use: "Use when a target HTML file should keep its content and components but inherit the style of a URL or second HTML file"
search_terms: ["reference-style-transfer-to-target-html", "design", "style-transfer", "html", "preserve-target", "reference", "reference-url", "selector-level-css", "style", "target"]
inputs: ["TARGET_HTML", "STYLE_REFERENCE"]
output: "A new complete HTML file with the transferred styling."
mode: "build"
capabilities: ["file-access", "visual-inspection"]
related: ["reference-design-system-style-transfer-to-target-html", "apply-reference-style"]
aliases: ["design/design-system-style-transfer/reference-style-transfer-to-target-html.md", "reference-style-transfer-to-target-html.md"]
---

# Reference Style Transfer to Target HTML

Use when a target HTML file should keep its content and components but inherit the style of a URL or second HTML file.

**Type:** prompt · **Mode:** build · **ID:** `reference-style-transfer-to-target-html`

**Expected output:** A new complete HTML file with the transferred styling.

## Inputs

Replace every listed placeholder. For an optional source, enter `None` when it is unavailable.

| Placeholder | What to provide | Example |
| --- | --- | --- |
| `{{TARGET_HTML}}` | Target HTML file to preserve. | existing-page.html |
| `{{STYLE_REFERENCE}}` | Accessible website URL or reference HTML file. | reference.html |

## Prompt

Copy the block below, not the metadata or usage notes.

<!-- prompt:start -->
````text
Target HTML:
{{TARGET_HTML}}

Reference website or HTML:
{{STYLE_REFERENCE}}

Create a new HTML file that transfers the reference style onto the target without replacing the target's content or behavior.

Preserve the target's content, section inventory, ordering, links, controls, IDs, classes, data attributes, scripts, accessibility attributes, and functional behavior. Do not import reference copy or unrelated sections. Do not silently remove a component to make the transfer easier.

Extract the actual style system before applying it: colors, typography, spacing rhythm, density, radius, borders, surfaces, shadows, backgrounds, component anatomy, state treatments, and responsive rules. Apply these through the real component selectors, not just root-variable replacements. Keep source content and target behavior distinct from visual evidence.

Check all affected regions and states, including navigation, headings, cards, badges, buttons, forms, tables, FAQs, overlays, footers, hover/focus, and responsive layouts where present. Do not claim rendered verification without inspecting the rendered result.

Inspect the full target and accessible reference first. If a reference URL is inaccessible, identify it and request an exported file or screenshot instead of pretending to have inspected it. Preserve the target's markup and layout intent; make no structural redesign.

Return the full new HTML document, including all CSS required for the visual transfer. Leave the source target unchanged unless explicitly authorized to overwrite it.
````
<!-- prompt:end -->

## Usage notes

Supply the actual referenced material. A filename or URL does not grant the assistant file, browser, account, or edit access.

**Relevant capabilities:** `file-access`, `visual-inspection`. These are requirements or conditional needs, not tools installed by this file.

## Related entries

- [Reference Design System Style Transfer to Target HTML](reference-design-system-style-transfer-to-target-html.md) — Use when the style reference is a design-system Markdown file, website, or HTML reference.
- [Apply Reference Style](apply-reference-style.md) — Use when the current design should keep its content and functionality but visually match a reference style.

[Browse the catalog](../../../CATALOG.md) · [Usage guide](../../../docs/usage.md)
