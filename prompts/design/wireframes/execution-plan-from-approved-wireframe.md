---
id: "execution-plan-from-approved-wireframe"
title: "Execution Plan From Approved Wireframe"
type: "prompt"
primary_category: "design"
categories: ["design"]
subcategory: "wireframes"
when_to_use: "Use after wireframes are approved to create an implementation plan before coding"
search_terms: ["execution-plan-from-approved-wireframe", "design", "wireframes", "approved", "approved-wireframe", "execution", "execution-plan", "implementation-plan", "phases", "plan"]
inputs: ["APPROVED_WIREFRAMES", "PROJECT_CONTEXT"]
output: "A phased implementation plan with testing, risks, and rollback notes; no code changes."
mode: "plan"
capabilities: ["file-access"]
related: ["general-balsamiq-wireframe", "balsamiq-ui-state-map", "build-from-approved-balsamiq-wireframe"]
aliases: ["design/wireframes/execution-plan-from-approved-wireframe.md", "execution-plan-from-approved-wireframe.md"]
---

# Execution Plan From Approved Wireframe

Use after wireframes are approved to create an implementation plan before coding.

**Type:** prompt · **Mode:** plan · **ID:** `execution-plan-from-approved-wireframe`

**Expected output:** A phased implementation plan with testing, risks, and rollback notes; no code changes.

## Inputs

Replace every listed placeholder. For an optional source, enter `None` when it is unavailable.

| Placeholder | What to provide | Example |
| --- | --- | --- |
| `{{APPROVED_WIREFRAMES}}` | Approved screen, state, and user-flow specification. | Approved wireframe document. |
| `{{PROJECT_CONTEXT}}` | Relevant repository structure and implementation constraints. | Current routes, components, data model, and tests. |

## Prompt

Copy the block below, not the metadata or usage notes.

<!-- prompt:start -->
````text
Approved wireframes:
{{APPROVED_WIREFRAMES}}

Codebase / project context:
{{PROJECT_CONTEXT}}

Create an execution plan using the approved wireframes as the implementation reference. Do not reinterpret the feature from scratch.

Include files to inspect, files to modify, files to create, components to build, CSS required, JavaScript required, backend/API changes, data model changes, state handling, validation rules, error handling, accessibility requirements, responsive requirements, testing checklist, risk areas, and rollback notes.

Return the plan in phases: inspection, structure, data/state, UI components, interactions, styling, responsive behavior, validation/error handling/accessibility, testing, and final review.

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
- [Build From Approved Balsamiq Wireframe](build-from-approved-balsamiq-wireframe.md) — Use when the wireframe is approved and the agent should implement from it.

[Browse the catalog](../../../CATALOG.md) · [Usage guide](../../../docs/usage.md)
