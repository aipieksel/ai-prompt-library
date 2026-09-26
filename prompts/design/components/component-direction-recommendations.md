---
id: "component-direction-recommendations"
title: "Component Direction Recommendations"
type: "prompt"
primary_category: "design"
categories: ["design"]
subcategory: "components"
when_to_use: "Use before building when a section already has a focal component and you want replacement component ideas"
search_terms: ["component-direction-recommendations", "design", "components", "component", "component-ideas", "direction", "existing-focal-component", "paste-ready", "recommendations"]
inputs: ["CURRENT_SECTION"]
output: "Exactly eight distinct component directions, each with paste-ready follow-up instructions."
mode: "plan"
capabilities: ["file-access", "visual-inspection"]
related: ["component-concept-redesign-with-direction", "paste-ready-component-direction-recommendations"]
aliases: ["design/component-design/component-direction-recommendations.md", "component-direction-recommendations.md"]
---

# Component Direction Recommendations

Use before building when a section already has a focal component and you want replacement component ideas.

**Type:** prompt · **Mode:** plan · **ID:** `component-direction-recommendations`

**Expected output:** Exactly eight distinct component directions, each with paste-ready follow-up instructions.

## Inputs

Replace every listed placeholder. For an optional source, enter `None` when it is unavailable.

| Placeholder | What to provide | Example |
| --- | --- | --- |
| `{{CURRENT_SECTION}}` | Section containing the focal component to replace. | Current hero HTML and screenshot. |

## Prompt

Copy the block below, not the metadata or usage notes.

<!-- prompt:start -->
````text
Section / current component:
{{CURRENT_SECTION}}

Analyze the current section and its existing focal component. Do not redesign or implement anything yet. Recommend multiple fresh component directions that could replace the existing component in a later prompt.

First inspect the section and identify:

- the section’s main message
- the role the current component plays
- the current component’s dominant visual pattern
- what content, labels, data, or messages the replacement component must preserve
- what the new component should avoid repeating

Return 8 component directions. Each recommendation must include:

- Component name
- Current component to replace: a paste-ready description of the current component
- New component direction: a short component type / visual metaphor
- Use this direction: one concise paragraph explaining what the component should become
- Avoid: one concise sentence listing old patterns or unrelated component types to avoid
- Best for: one concise sentence explaining when this direction is strongest
- Paste-ready version: wording I can paste into component-concept-redesign-with-direction.md

Keep ideas practical for real HTML/CSS and meaningfully different from each other. Do not implement anything yet.

### Scope and quality checks

Inspect the actual reference before describing the current component. Preserve the section's required message, factual content, links, pricing, and functionality; treat decorative changes separately from product behavior. Do not invent metrics or technical capabilities. Keep concepts practical, distinct, and useful rather than decorative. Return exactly eight options. Do not implement them. When no component exists, say so in the replacement field rather than inventing one. Make every paste-ready direction self-contained enough to use with the referenced section.
````
<!-- prompt:end -->

## Usage notes

Supply the actual referenced material. A filename or URL does not grant the assistant file, browser, account, or edit access.

**Relevant capabilities:** `file-access`, `visual-inspection`. These are requirements or conditional needs, not tools installed by this file.

## Related entries

- [Component Concept Redesign With Direction](component-concept-redesign-with-direction.md) — Use when you want to replace a current component and specify the new component direction, such as server rack or timeline.
- [Paste-Ready Component Direction Recommendations](paste-ready-component-direction-recommendations.md) — Use when recommendation output should be formatted so the selected option can be pasted directly into the redesign prompt.

[Browse the catalog](../../../CATALOG.md) · [Usage guide](../../../docs/usage.md)
