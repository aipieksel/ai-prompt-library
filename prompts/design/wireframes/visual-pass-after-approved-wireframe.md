---
id: "visual-pass-after-approved-wireframe"
title: "Visual Pass After Approved Wireframe"
type: "prompt"
primary_category: "design"
categories: ["design"]
subcategory: "wireframes"
when_to_use: "Use after wireframes are approved to create the polished design direction"
search_terms: ["visual-pass-after-approved-wireframe", "design", "wireframes", "approved", "approved-wireframe", "design-system", "pass", "ui-design", "visual", "visual-pass"]
inputs: ["APPROVED_WIREFRAMES", "DESIGN_SYSTEM"]
output: "A polished visual design pass preserving the approved UX and states."
mode: "design"
capabilities: ["file-access"]
related: ["general-balsamiq-wireframe", "balsamiq-ui-state-map", "execution-plan-from-approved-wireframe", "build-from-approved-balsamiq-wireframe"]
aliases: ["design/wireframes/visual-pass-after-approved-wireframe.md", "visual-pass-after-approved-wireframe.md"]
---

# Visual Pass After Approved Wireframe

Use after wireframes are approved to create the polished design direction.

**Type:** prompt · **Mode:** design · **ID:** `visual-pass-after-approved-wireframe`

**Expected output:** A polished visual design pass preserving the approved UX and states.

## Inputs

Replace every listed placeholder. For an optional source, enter `None` when it is unavailable.

| Placeholder | What to provide | Example |
| --- | --- | --- |
| `{{APPROVED_WIREFRAMES}}` | Approved layouts, flows, content, and states. | Approved feature wireframes and state map. |
| `{{DESIGN_SYSTEM}}` | Target HTML, tokens, components, or design-system document. | DESIGN.md and the existing component showcase. |

## Prompt

Copy the block below, not the metadata or usage notes.

<!-- prompt:start -->
````text
Approved wireframes:
{{APPROVED_WIREFRAMES}}

Target design system:
{{DESIGN_SYSTEM}}

Create the visual design pass using the approved Balsamiq-style wireframes as the UX source of truth.

Preserve layout, screens, states, user flows, information architecture, controls, affordances, signifiers, required content, and edge cases. Apply the target design system: colors, typography, spacing, radius, cards, buttons, forms, tables, tabs, modals, navigation, icons, states, and responsive behavior.

Do not reinterpret the product from scratch. Do not skip any state from the approved wireframes.

### Scope and evidence

Use supplied requirements, not invented features. Label missing data or behavior as an assumption or dependency. Include only states relevant to the feature, and explain any omitted state that the brief requires. “Balsamiq-style” describes low fidelity; do not claim to have created a native Balsamiq project unless that file was actually generated.
````
<!-- prompt:end -->

## Usage notes

Supply the actual referenced material. A filename or URL does not grant the assistant file, browser, account, or edit access.

**Relevant capabilities:** `file-access`. These are requirements or conditional needs, not tools installed by this file.

## Related entries

- [General Balsamiq Wireframe](general-balsamiq-wireframe.md) — Use for any project, feature, dashboard, page, workflow, or interface before implementation.
- [Balsamiq UI State Map](balsamiq-ui-state-map.md) — Use when you want every meaningful UI state mapped before building.
- [Execution Plan From Approved Wireframe](execution-plan-from-approved-wireframe.md) — Use after wireframes are approved to create an implementation plan before coding.
- [Build From Approved Balsamiq Wireframe](build-from-approved-balsamiq-wireframe.md) — Use when the wireframe is approved and the agent should implement from it.

[Browse the catalog](../../../CATALOG.md) · [Usage guide](../../../docs/usage.md)
