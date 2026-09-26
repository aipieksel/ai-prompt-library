---
id: "multi-concept-balsamiq-wireframe"
title: "Multi-Concept Balsamiq Wireframe"
type: "prompt"
primary_category: "design"
categories: ["design"]
subcategory: "wireframes"
when_to_use: "Use when you want several different rough layout directions before choosing one"
search_terms: ["multi-concept-balsamiq-wireframe", "design", "wireframes", "balsamiq", "compare-directions", "concept", "concepts", "multi", "no-code", "planning"]
inputs: ["BUILD_REQUEST", "REFERENCE_MATERIAL"]
output: "Exactly three meaningfully different low-fidelity concepts; no implementation."
mode: "plan"
capabilities: ["file-access"]
related: ["general-balsamiq-wireframe", "balsamiq-ui-state-map", "execution-plan-from-approved-wireframe", "build-from-approved-balsamiq-wireframe"]
aliases: ["design/wireframes/multi-concept-balsamiq-wireframe.md", "multi-concept-balsamiq-wireframe.md"]
---

# Multi-Concept Balsamiq Wireframe

Use when you want several different rough layout directions before choosing one.

**Type:** prompt · **Mode:** plan · **ID:** `multi-concept-balsamiq-wireframe`

**Expected output:** Exactly three meaningfully different low-fidelity concepts; no implementation.

## Inputs

Replace every listed placeholder. For an optional source, enter `None` when it is unavailable.

| Placeholder | What to provide | Example |
| --- | --- | --- |
| `{{BUILD_REQUEST}}` | One shared requirement set for all concepts. | A prompt library with search, detail preview, and edit flows. |
| `{{REFERENCE_MATERIAL}}` | Constraints and current references, or None. | Existing app shell and required metadata. |

## Prompt

Copy the block below, not the metadata or usage notes.

<!-- prompt:start -->
````text
Project / feature description:
{{BUILD_REQUEST}}

Reference material:
{{REFERENCE_MATERIAL}}

Create 3 meaningfully different Balsamiq-style low-fidelity concept directions. Each concept must solve the same requirements, but use a different layout strategy, information architecture, and user-flow structure.

For each concept, include concept name, core layout idea, rough screen layout, primary user flow, navigation/page structure, key components, required screens/states, affordances, signifiers, strengths, weaknesses, best use case, and implementation risks.

Do not create final visual design or production code. Return only the rough concept directions.

### Scope and evidence

Use supplied requirements, not invented features. Label missing data or behavior as an assumption or dependency. Include only states relevant to the feature, and explain any omitted state that the brief requires. “Balsamiq-style” describes low fidelity; do not claim to have created a native Balsamiq project unless that file was actually generated. Keep the output reviewable as annotated Markdown or clearly labeled wireframes; do not imply that a plan is an implemented interface.
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
