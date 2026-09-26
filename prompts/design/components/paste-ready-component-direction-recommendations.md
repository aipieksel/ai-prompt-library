---
id: "paste-ready-component-direction-recommendations"
title: "Paste-Ready Component Direction Recommendations"
type: "prompt"
primary_category: "design"
categories: ["design"]
subcategory: "components"
when_to_use: "Use when recommendation output should be formatted so the selected option can be pasted directly into the redesign prompt"
search_terms: ["paste-ready-component-direction-recommendations", "design", "components", "component", "component-ideas", "direction", "direction-block", "paste", "paste-ready", "recommendations"]
inputs: ["CURRENT_SECTION"]
output: "Exactly eight distinct component directions, each with paste-ready follow-up instructions."
mode: "plan"
capabilities: ["file-access", "visual-inspection"]
related: ["component-direction-recommendations", "component-concept-redesign-with-direction"]
aliases: ["design/component-design/paste-ready-component-direction-recommendations.md", "paste-ready-component-direction-recommendations.md"]
---

# Paste-Ready Component Direction Recommendations

Use when recommendation output should be formatted so the selected option can be pasted directly into the redesign prompt.

**Type:** prompt · **Mode:** plan · **ID:** `paste-ready-component-direction-recommendations`

**Expected output:** Exactly eight distinct component directions, each with paste-ready follow-up instructions.

## Inputs

Replace every listed placeholder. For an optional source, enter `None` when it is unavailable.

| Placeholder | What to provide | Example |
| --- | --- | --- |
| `{{CURRENT_SECTION}}` | Section and current component when one exists. | Feature section HTML; no focal component yet. |

## Prompt

Copy the block below, not the metadata or usage notes.

<!-- prompt:start -->
````text
Section / component reference:
{{CURRENT_SECTION}}

Analyze the current section and its existing component, if one exists. Do not redesign or implement anything yet.

Recommend 8 fresh dynamic HTML/CSS component directions. Each recommendation must be written as a ready-to-paste component direction block for a follow-up prompt like component-concept-redesign-with-direction.md.

Use this format for every option:

## [Option number]. [Component name]

Current component to replace:
[Current component description, or “No existing focal component”]

New component direction:
[Short component type or metaphor]

Use this direction:
[One concise paragraph explaining the new component]

Avoid:
[One sentence naming patterns to avoid]

Best for:
[One sentence describing when this direction works best]

Paste-ready version:
[Complete wording to paste into the build prompt]

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

[Browse the catalog](../../../CATALOG.md) · [Usage guide](../../../docs/usage.md)
