---
id: "component-direction-recommendations-without-existing-focal-component"
title: "Component Direction Recommendations Without Existing Focal Component"
type: "prompt"
primary_category: "design"
categories: ["design"]
subcategory: "components"
when_to_use: "Use when a section has no clear component and needs dynamic component ideas"
search_terms: ["component-direction-recommendations-without-existing-focal-component", "design", "components", "add-component", "component", "component-ideas", "direction", "focal", "no-focal-component", "recommendations"]
inputs: ["CURRENT_SECTION"]
output: "Exactly eight distinct component directions, each with paste-ready follow-up instructions."
mode: "plan"
capabilities: ["file-access", "visual-inspection"]
related: ["component-direction-recommendations", "component-concept-redesign-with-direction", "paste-ready-component-direction-recommendations"]
aliases: ["design/component-design/component-direction-recommendations-without-existing-focal-component.md", "component-direction-recommendations-without-existing-focal-component.md"]
---

# Component Direction Recommendations Without Existing Focal Component

Use when a section has no clear component and needs dynamic component ideas.

**Type:** prompt · **Mode:** plan · **ID:** `component-direction-recommendations-without-existing-focal-component`

**Expected output:** Exactly eight distinct component directions, each with paste-ready follow-up instructions.

## Inputs

Replace every listed placeholder. For an optional source, enter `None` when it is unavailable.

| Placeholder | What to provide | Example |
| --- | --- | --- |
| `{{CURRENT_SECTION}}` | Section that needs a useful focal component. | Text-heavy benefits section and required copy. |

## Prompt

Copy the block below, not the metadata or usage notes.

<!-- prompt:start -->
````text
Section reference:
{{CURRENT_SECTION}}

Analyze the current section. Do not redesign or implement anything yet. Recommend multiple dynamic component directions that could be added to make the section stronger, more useful, and more visually interesting.

First identify:

- what the section is trying to communicate
- what the user should understand first
- what content, claims, features, proof points, or actions need visual support
- whether the section feels empty, generic, flat, repetitive, text-heavy, cluttered, or weak
- what kind of component would improve clarity, hierarchy, conversion, or visual interest

Return 8 component directions. Each recommendation must include a paste-ready version that can be used in a follow-up build prompt.

Keep the ideas practical for real HTML/CSS. Avoid static-image concepts, overcomplicated 3D scenes, vague decoration, or generic SaaS filler.

### Scope and quality checks

Inspect the actual reference before describing the current component. Preserve the section's required message, factual content, links, pricing, and functionality; treat decorative changes separately from product behavior. Do not invent metrics or technical capabilities. Keep concepts practical, distinct, and useful rather than decorative. Return exactly eight options. Do not implement them. When no component exists, say so in the replacement field rather than inventing one. Make every paste-ready direction self-contained enough to use with the referenced section.
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
