---
id: "component-concept-redesign-with-direction"
title: "Component Concept Redesign With Direction"
type: "prompt"
primary_category: "design"
categories: ["design"]
subcategory: "components"
when_to_use: "Use when you want to replace a current component and specify the new component direction, such as server rack or timeline"
search_terms: ["component-concept-redesign-with-direction", "design", "components", "component", "component-direction", "component-redesign", "concept", "direction", "dynamic-html-css", "redesign"]
inputs: ["CURRENT_COMPONENT", "DIRECTION"]
output: "An editable HTML/CSS component, minimal JavaScript if justified, and integration notes."
mode: "build"
capabilities: ["file-access", "visual-inspection"]
related: ["component-direction-recommendations", "paste-ready-component-direction-recommendations"]
aliases: ["design/component-design/component-concept-redesign-with-direction.md", "component-concept-redesign-with-direction.md"]
---

# Component Concept Redesign With Direction

Use when you want to replace a current component and specify the new component direction, such as server rack or timeline.

**Type:** prompt · **Mode:** build · **ID:** `component-concept-redesign-with-direction`

**Expected output:** An editable HTML/CSS component, minimal JavaScript if justified, and integration notes.

## Inputs

Replace every listed placeholder. For an optional source, enter `None` when it is unavailable.

| Placeholder | What to provide | Example |
| --- | --- | --- |
| `{{CURRENT_COMPONENT}}` | Existing component, its code, and surrounding constraints. | Current hero visualization and required labels. |
| `{{DIRECTION}}` | Chosen new component type or visual metaphor. | Provisioning timeline, server rack, or resource-allocation view. |

## Prompt

Copy the block below, not the metadata or usage notes.

<!-- prompt:start -->
````text
Current component to replace:
{{CURRENT_COMPONENT}}

New component direction:
{{DIRECTION}}

Fundamentally redesign the existing focal component in this section. Treat the current component as a reference for intent, content, and function only, not as a structure to preserve.

First inspect the current component and identify its dominant visual pattern. Then replace it with the requested component direction while avoiding the old component’s shapes, layout structure, focal arrangement, decorative treatment, animation style, card model, label placement, and visual metaphor.

The new component must communicate the same core message through the requested direction. It should feel premium, technical, modern, editable, responsive, and visually interesting without becoming cluttered.

Build it as real HTML/CSS, not as a static image. Use lightweight JavaScript only if it improves interaction or motion.

### Scope and quality checks

Inspect the actual reference before describing the current component. Preserve the section's required message, factual content, links, pricing, and functionality; treat decorative changes separately from product behavior. Do not invent metrics or technical capabilities. Keep concepts practical, distinct, and useful rather than decorative. Build editable, responsive HTML/CSS rather than a static image. Use lightweight JavaScript only where it improves a real interaction or appropriate motion; respect reduced-motion preferences. Preserve the surrounding page and verify the changed component at relevant sizes. Return complete component code, integration placement, and actual verification status.
````
<!-- prompt:end -->

## Usage notes

Supply the actual referenced material. A filename or URL does not grant the assistant file, browser, account, or edit access.

**Relevant capabilities:** `file-access`, `visual-inspection`. These are requirements or conditional needs, not tools installed by this file.

## Related entries

- [Component Direction Recommendations](component-direction-recommendations.md) — Use before building when a section already has a focal component and you want replacement component ideas.
- [Paste-Ready Component Direction Recommendations](paste-ready-component-direction-recommendations.md) — Use when recommendation output should be formatted so the selected option can be pasted directly into the redesign prompt.

[Browse the catalog](../../../CATALOG.md) · [Usage guide](../../../docs/usage.md)
