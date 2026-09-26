---
id: "component-concept-redesign"
title: "Component Concept Redesign"
type: "prompt"
primary_category: "design"
categories: ["design"]
subcategory: "components"
when_to_use: "Use when you want to replace an existing focal component with a fresh dynamic component without naming the old component"
search_terms: ["component-concept-redesign", "design", "components", "component", "component-redesign", "concept", "dynamic-html-css", "focal-component", "redesign", "visual-metaphor"]
inputs: ["CURRENT_SECTION"]
output: "An editable HTML/CSS component, minimal JavaScript if justified, and integration notes."
mode: "build"
capabilities: ["file-access", "visual-inspection"]
related: ["component-direction-recommendations", "component-concept-redesign-with-direction", "paste-ready-component-direction-recommendations"]
aliases: ["design/component-design/component-concept-redesign.md", "component-concept-redesign.md"]
---

# Component Concept Redesign

Use when you want to replace an existing focal component with a fresh dynamic component without naming the old component.

**Type:** prompt · **Mode:** build · **ID:** `component-concept-redesign`

**Expected output:** An editable HTML/CSS component, minimal JavaScript if justified, and integration notes.

## Inputs

Replace every listed placeholder. For an optional source, enter `None` when it is unavailable.

| Placeholder | What to provide | Example |
| --- | --- | --- |
| `{{CURRENT_SECTION}}` | Section containing the existing focal component. | Hero section HTML and screenshot. |

## Prompt

Copy the block below, not the metadata or usage notes.

<!-- prompt:start -->
````text
Section / component reference:
{{CURRENT_SECTION}}

Fundamentally redesign the existing focal component in this section. Treat the current component as a reference for intent, content, and function only, not as a structure to preserve.

Do not restyle the existing component. Replace its visual concept, component model, internal layout, interaction pattern, visual hierarchy, and overall presentation with a fresh dynamic component.

First inspect the current component and identify its dominant visual pattern. Then avoid repeating that pattern. Do not reuse the same shapes, layout structure, focal arrangement, decorative treatment, animation style, card model, label placement, or visual metaphor.

Create a new dynamic HTML/CSS component that communicates the same core message in a different way. Use lightweight JavaScript only if it improves interaction or motion. Preserve surrounding SEO text, links, pricing, claims, factual content, and functionality.

### Scope and quality checks

Inspect the actual reference before describing the current component. Preserve the section's required message, factual content, links, pricing, and functionality; treat decorative changes separately from product behavior. Do not invent metrics or technical capabilities. Keep concepts practical, distinct, and useful rather than decorative. Build editable, responsive HTML/CSS rather than a static image. Use lightweight JavaScript only where it improves a real interaction or appropriate motion; respect reduced-motion preferences. Preserve the surrounding page and verify the changed component at relevant sizes. Return complete component code, integration placement, and actual verification status.
````
<!-- prompt:end -->

## Usage notes

Supply the actual referenced material. A filename or URL does not grant the assistant file, browser, account, or edit access.

**Relevant capabilities:** `file-access`, `visual-inspection`. These are requirements or conditional needs, not tools installed by this file.

## Related entries

- [Component Direction Recommendations](component-direction-recommendations.md) — Use before building when a section already has a focal component and you want replacement component ideas.
- [Component Concept Redesign With Direction](component-concept-redesign-with-direction.md) — Use when you want to replace a current component and specify the new component direction, such as server rack or timeline.
- [Paste-Ready Component Direction Recommendations](paste-ready-component-direction-recommendations.md) — Use when recommendation output should be formatted so the selected option can be pasted directly into the redesign prompt.

[Browse the catalog](../../../CATALOG.md) · [Usage guide](../../../docs/usage.md)
