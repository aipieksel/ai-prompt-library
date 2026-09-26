---
id: "reference-design-system-style-transfer-to-target-html"
title: "Reference Design System Style Transfer to Target HTML"
type: "prompt"
primary_category: "design"
categories: ["design"]
subcategory: "style-transfer"
when_to_use: "Use when the style reference is a design-system Markdown file, website, or HTML reference"
search_terms: ["reference-design-system-style-transfer-to-target-html", "design", "style-transfer", "design-system-md", "highest-priority-source", "html", "markdown-reference", "reference", "style", "system"]
inputs: ["TARGET_HTML", "DESIGN_REFERENCE"]
output: "A complete restyled HTML file following the documented design system."
mode: "build"
capabilities: ["file-access", "visual-inspection"]
related: ["reference-style-transfer-to-target-html", "strict-design-system-compliance"]
aliases: ["design/design-system-style-transfer/reference-design-system-style-transfer-to-target-html.md", "reference-design-system-style-transfer-to-target-html.md"]
---

# Reference Design System Style Transfer to Target HTML

Use when the style reference is a design-system Markdown file, website, or HTML reference.

**Type:** prompt · **Mode:** build · **ID:** `reference-design-system-style-transfer-to-target-html`

**Expected output:** A complete restyled HTML file following the documented design system.

## Inputs

Replace every listed placeholder. For an optional source, enter `None` when it is unavailable.

| Placeholder | What to provide | Example |
| --- | --- | --- |
| `{{TARGET_HTML}}` | Target HTML file. | target.html |
| `{{DESIGN_REFERENCE}}` | Design-system document plus optional supporting HTML or URL. | DESIGN.md and reference.html |

## Prompt

Copy the block below, not the metadata or usage notes.

<!-- prompt:start -->
````text
Target HTML:
{{TARGET_HTML}}

Design-system Markdown and optional visual reference:
{{DESIGN_REFERENCE}}

Create a new HTML file that preserves the target while transferring the supplied design system.

Preserve the target's content, section inventory, ordering, links, controls, IDs, classes, data attributes, scripts, accessibility attributes, and functional behavior. Do not import reference copy or unrelated sections. Do not silently remove a component to make the transfer easier.

Extract the actual style system before applying it: colors, typography, spacing rhythm, density, radius, borders, surfaces, shadows, backgrounds, component anatomy, state treatments, and responsive rules. Apply these through the real component selectors, not just root-variable replacements. Keep source content and target behavior distinct from visual evidence.

Check all affected regions and states, including navigation, headings, cards, badges, buttons, forms, tables, FAQs, overlays, footers, hover/focus, and responsive layouts where present. Do not claim rendered verification without inspecting the rendered result.

When supplied, the approved design-system Markdown is the style authority. Parse its visual theme, color palette, typography rules, component styles, layout principles, page anatomy, depth/gradients/motion, do/don't rules, responsive behavior, and prompt recipes. Use exact button, card, heading, spacing, and layout recipes where provided. A website or HTML reference supports these rules; it does not silently override them.

Map each relevant style rule onto the existing target components. Do not rely on memory, generic brand impressions, or token-only recoloring. Apply layout principles within the target's preserved structure. If a rule cannot be satisfied without a forbidden structural change, report the conflict rather than redesigning the page.

Return the complete new HTML file and its required CSS.
````
<!-- prompt:end -->

## Usage notes

Supply the actual referenced material. A filename or URL does not grant the assistant file, browser, account, or edit access.

**Relevant capabilities:** `file-access`, `visual-inspection`. These are requirements or conditional needs, not tools installed by this file.

## Related entries

- [Reference Style Transfer to Target HTML](reference-style-transfer-to-target-html.md) — Use when a target HTML file should keep its content and components but inherit the style of a URL or second HTML file.
- [Strict Design System Compliance](strict-design-system-compliance.md) — Use when the agent should polish within an existing design system, not invent a new style.

[Browse the catalog](../../../CATALOG.md) · [Usage guide](../../../docs/usage.md)
