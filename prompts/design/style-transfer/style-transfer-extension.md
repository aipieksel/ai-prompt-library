---
id: "style-transfer-extension"
title: "Style Transfer Extension"
type: "prompt"
primary_category: "design"
categories: ["design"]
subcategory: "style-transfer"
when_to_use: "Use when you have a reference design file and a target page that needs to match that design language"
search_terms: ["style-transfer-extension", "design", "style-transfer", "extension", "infer-design-system", "reference-file", "style", "target-page", "transfer"]
inputs: ["STYLE_REFERENCE", "TARGET"]
output: "An updated target in the reference style, including compatible missing-component extensions."
mode: "edit"
capabilities: ["file-access", "visual-inspection"]
related: ["style-extension-from-reference", "apply-reference-style"]
aliases: ["design/design-system-style-transfer/style-transfer-extension.md", "style-transfer-extension.md"]
---

# Style Transfer Extension

Use when you have a reference design file and a target page that needs to match that design language.

**Type:** prompt · **Mode:** edit · **ID:** `style-transfer-extension`

**Expected output:** An updated target in the reference style, including compatible missing-component extensions.

## Inputs

Replace every listed placeholder. For an optional source, enter `None` when it is unavailable.

| Placeholder | What to provide | Example |
| --- | --- | --- |
| `{{STYLE_REFERENCE}}` | File containing the approved visual language. | approved-interface.html |
| `{{TARGET}}` | File that controls content and functionality. | new-feature.html |

## Prompt

Copy the block below, not the metadata or usage notes.

<!-- prompt:start -->
````text
Reference design file:
{{STYLE_REFERENCE}}

Target file:
{{TARGET}}

Apply the reference's reusable design language to the target. Treat the reference as the visual source of truth and the target as the content and behavior source of truth.

Preserve the target's content, section inventory, ordering, links, controls, IDs, classes, data attributes, scripts, accessibility attributes, and functional behavior. Do not import reference copy or unrelated sections. Do not silently remove a component to make the transfer easier.

Extract the actual style system before applying it: colors, typography, spacing rhythm, density, radius, borders, surfaces, shadows, backgrounds, component anatomy, state treatments, and responsive rules. Apply these through the real component selectors, not just root-variable replacements. Keep source content and target behavior distinct from visual evidence.

Check all affected regions and states, including navigation, headings, cards, badges, buttons, forms, tables, FAQs, overlays, footers, hover/focus, and responsive layouts where present. Do not claim rendered verification without inspecting the rendered result.

Preserve the target's SEO wording, factual claims, and structure unless the task explicitly approves those changes. Do not introduce a new visual identity, unrelated components, different typography, random colors, inconsistent spacing, or unrelated button styles.

Where the reference lacks a required component, derive the closest compatible pattern from its existing system and identify it as an extension, not an observed reference component. Do not copy the exact reference layout unless explicitly required.

Return the complete updated target and required styles.
````
<!-- prompt:end -->

## Usage notes

Supply the actual referenced material. A filename or URL does not grant the assistant file, browser, account, or edit access.

**Relevant capabilities:** `file-access`, `visual-inspection`. These are requirements or conditional needs, not tools installed by this file.

## Related entries

- [Style Extension From Reference](style-extension-from-reference.md) — Use when one approved HTML section should become the visual source of truth for building more sections.
- [Apply Reference Style](apply-reference-style.md) — Use when the current design should keep its content and functionality but visually match a reference style.

[Browse the catalog](../../../CATALOG.md) · [Usage guide](../../../docs/usage.md)
