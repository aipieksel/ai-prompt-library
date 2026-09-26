---
id: "alternative-infrastructure-visual-metaphor"
title: "Alternative Infrastructure Visual Metaphor"
type: "prompt"
primary_category: "design"
categories: ["design"]
subcategory: "components"
when_to_use: "Use when you want the same message communicated through a different technical visual component"
search_terms: ["alternative-infrastructure-visual-metaphor", "design", "components", "alternative", "dynamic-component", "hero-visual", "infrastructure", "metaphor", "not-static-image", "visual"]
inputs: ["CURRENT_SECTION", "DIRECTION"]
output: "An editable HTML/CSS component, minimal JavaScript if justified, and integration notes."
mode: "build"
capabilities: ["file-access", "visual-inspection"]
related: ["component-direction-recommendations", "component-concept-redesign-with-direction", "paste-ready-component-direction-recommendations"]
aliases: ["design/component-design/alternative-infrastructure-visual-metaphor.md", "alternative-infrastructure-visual-metaphor.md"]
---

# Alternative Infrastructure Visual Metaphor

Use when you want the same message communicated through a different technical visual component.

**Type:** prompt · **Mode:** build · **ID:** `alternative-infrastructure-visual-metaphor`

**Expected output:** An editable HTML/CSS component, minimal JavaScript if justified, and integration notes.

## Inputs

Replace every listed placeholder. For an optional source, enter `None` when it is unavailable.

| Placeholder | What to provide | Example |
| --- | --- | --- |
| `{{CURRENT_SECTION}}` | Current hero, section, or HTML visual. | Existing infrastructure illustration and surrounding copy. |
| `{{DIRECTION}}` | Preferred metaphor, or None to let the agent propose a different one. | A deployment timeline rather than a central-node diagram. |

## Prompt

Copy the block below, not the metadata or usage notes.

<!-- prompt:start -->
````text
Current visual / section:
{{CURRENT_SECTION}}

Desired direction:
{{DIRECTION}}

Create a new infrastructure visual metaphor for this section. Do not reuse the existing visual concept, component structure, shapes, layout, glow treatment, floating labels, central node, ring, dashboard, rack, grid, or other dominant pattern from the current design.

Keep the same core message and required content, but communicate it through a different visual concept. The result should be a real HTML/CSS component, not a static image. Use lightweight JavaScript only if it improves the interaction or motion.

The new component should feel premium, technical, modern, responsive, editable, and visually interesting without becoming cluttered.

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
