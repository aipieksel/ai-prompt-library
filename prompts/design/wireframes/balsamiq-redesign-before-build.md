---
id: "balsamiq-redesign-before-build"
title: "Balsamiq Redesign Before Build"
type: "prompt"
primary_category: "design"
categories: ["design"]
subcategory: "wireframes"
when_to_use: "Use when the current UI is weak and you want rough redesign concepts before code"
search_terms: ["balsamiq-redesign-before-build", "design", "wireframes", "balsamiq", "before-build", "build", "no-code", "planning", "redesign", "ux"]
inputs: ["CURRENT_INTERFACE", "REDESIGN_GOAL", "REFERENCE_MATERIAL"]
output: "An annotated redesign wireframe plan before visual design or implementation."
mode: "plan"
capabilities: ["file-access"]
related: ["general-balsamiq-wireframe", "balsamiq-ui-state-map", "execution-plan-from-approved-wireframe", "build-from-approved-balsamiq-wireframe"]
aliases: ["design/wireframes/balsamiq-redesign-before-build.md", "balsamiq-redesign-before-build.md"]
---

# Balsamiq Redesign Before Build

Use when the current UI is weak and you want rough redesign concepts before code.

**Type:** prompt · **Mode:** plan · **ID:** `balsamiq-redesign-before-build`

**Expected output:** An annotated redesign wireframe plan before visual design or implementation.

## Inputs

Replace every listed placeholder. For an optional source, enter `None` when it is unavailable.

| Placeholder | What to provide | Example |
| --- | --- | --- |
| `{{CURRENT_INTERFACE}}` | Current screenshot, HTML, URL, or interface description. | Existing admin screen and its primary user flow. |
| `{{REDESIGN_GOAL}}` | Problems and desired UX improvements. | Reduce confusing navigation and make failed jobs actionable. |
| `{{REFERENCE_MATERIAL}}` | Product, design-system, and implementation constraints, or None. | Approved design rules and required features. |

## Prompt

Copy the block below, not the metadata or usage notes.

<!-- prompt:start -->
````text
Current interface:
{{CURRENT_INTERFACE}}

Redesign goal:
{{REDESIGN_GOAL}}

Reference material:
{{REFERENCE_MATERIAL}}

Create Balsamiq-style low-fidelity redesign wireframes. Do not write production code or create final visual design.

Inspect the current interface and identify what it is trying to do, what is confusing or weak, the primary action, the most important information, missing states, unclear affordances/signifiers, flows that need simplification, and components that should be grouped, separated, or replaced.

Return a redesigned wireframe plan with revised default view, hierarchy, actions, navigation/section flow, states, confirmations, responsive layout, and notes explaining why the structure changed.

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
