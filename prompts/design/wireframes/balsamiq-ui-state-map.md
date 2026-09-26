---
id: "balsamiq-ui-state-map"
title: "Balsamiq UI State Map"
type: "prompt"
primary_category: "design"
categories: ["design"]
subcategory: "wireframes"
when_to_use: "Use when you want every meaningful UI state mapped before building"
search_terms: ["balsamiq-ui-state-map", "design", "wireframes", "balsamiq", "edge-cases", "map", "no-code", "planning", "state", "states"]
inputs: ["BUILD_REQUEST", "REFERENCE_MATERIAL"]
output: "An annotated state map with actions, dependencies, validation, and transitions."
mode: "plan"
capabilities: ["file-access"]
related: ["general-balsamiq-wireframe", "execution-plan-from-approved-wireframe", "build-from-approved-balsamiq-wireframe"]
aliases: ["design/wireframes/balsamiq-ui-state-map.md", "balsamiq-ui-state-map.md"]
---

# Balsamiq UI State Map

Use when you want every meaningful UI state mapped before building.

**Type:** prompt · **Mode:** plan · **ID:** `balsamiq-ui-state-map`

**Expected output:** An annotated state map with actions, dependencies, validation, and transitions.

## Inputs

Replace every listed placeholder. For an optional source, enter `None` when it is unavailable.

| Placeholder | What to provide | Example |
| --- | --- | --- |
| `{{BUILD_REQUEST}}` | Feature whose states must be mapped. | Create and schedule a social post. |
| `{{REFERENCE_MATERIAL}}` | Brief, interfaces, data rules, or None. | Feature requirements and existing form screenshots. |

## Prompt

Copy the block below, not the metadata or usage notes.

<!-- prompt:start -->
````text
Project / feature description:
{{BUILD_REQUEST}}

Reference material:
{{REFERENCE_MATERIAL}}

Create a Balsamiq-style low-fidelity state map for every meaningful UI state the user may encounter.

Include default, empty, loading, partial-data, no-results, error, success, draft, scheduled/published/active, disabled/locked, validation-error, permission-denied, create, edit, detail, delete/confirmation, modal/drawer/popover/tab open/closed, and mobile/narrow states where relevant.

For each state, include rough layout, what changed from default, available actions, disabled actions and why, feedback shown, required data, validation rules, edge cases, backend/API dependencies, and implementation notes.

### Scope and evidence

Use supplied requirements, not invented features. Label missing data or behavior as an assumption or dependency. Include only states relevant to the feature, and explain any omitted state that the brief requires. “Balsamiq-style” describes low fidelity; do not claim to have created a native Balsamiq project unless that file was actually generated. Keep the output reviewable as annotated Markdown or clearly labeled wireframes; do not imply that a plan is an implemented interface. For each state, identify its trigger, allowed transitions, and recovery path so the map does not become an unconnected list.
````
<!-- prompt:end -->

## Usage notes

Supply the actual referenced material. A filename or URL does not grant the assistant file, browser, account, or edit access.

**Relevant capabilities:** `file-access`. These are requirements or conditional needs, not tools installed by this file.

## Related entries

- [General Balsamiq Wireframe](general-balsamiq-wireframe.md) — Use for any project, feature, dashboard, page, workflow, or interface before implementation.
- [Execution Plan From Approved Wireframe](execution-plan-from-approved-wireframe.md) — Use after wireframes are approved to create an implementation plan before coding.
- [Build From Approved Balsamiq Wireframe](build-from-approved-balsamiq-wireframe.md) — Use when the wireframe is approved and the agent should implement from it.

[Browse the catalog](../../../CATALOG.md) · [Usage guide](../../../docs/usage.md)
