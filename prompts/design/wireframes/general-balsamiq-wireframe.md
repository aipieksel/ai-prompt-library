---
id: "general-balsamiq-wireframe"
title: "General Balsamiq Wireframe"
type: "prompt"
primary_category: "design"
categories: ["design"]
subcategory: "wireframes"
when_to_use: "Use for any project, feature, dashboard, page, workflow, or interface before implementation"
search_terms: ["general-balsamiq-wireframe", "design", "wireframes", "balsamiq", "dynamic", "no-code", "planning", "ux", "wireframe"]
inputs: ["BUILD_REQUEST", "REFERENCE_MATERIAL"]
output: "A low-fidelity wireframe specification for review; no production code."
mode: "plan"
capabilities: ["file-access"]
related: ["balsamiq-ui-state-map", "execution-plan-from-approved-wireframe", "build-from-approved-balsamiq-wireframe"]
aliases: ["design/wireframes/general-balsamiq-wireframe.md", "general-balsamiq-wireframe.md"]
---

# General Balsamiq Wireframe

Use for any project, feature, dashboard, page, workflow, or interface before implementation.

**Type:** prompt · **Mode:** plan · **ID:** `general-balsamiq-wireframe`

**Expected output:** A low-fidelity wireframe specification for review; no production code.

## Inputs

Replace every listed placeholder. For an optional source, enter `None` when it is unavailable.

| Placeholder | What to provide | Example |
| --- | --- | --- |
| `{{BUILD_REQUEST}}` | Project, feature, workflow, or interface to plan. | A searchable document library with preview and editing. |
| `{{REFERENCE_MATERIAL}}` | Relevant files, screenshots, design systems, or None. | Current interface screenshots and the feature brief. |

## Prompt

Copy the block below, not the metadata or usage notes.

<!-- prompt:start -->
````text
Project / feature description:
{{BUILD_REQUEST}}

Reference material:
{{REFERENCE_MATERIAL}}

Create Balsamiq-style low-fidelity wireframes for the project, feature, dashboard, page, workflow, or interface described above.

Do not write production code. Do not create final visual design. First translate the description into a rough wireframe plan that maps structure, screens, states, user flows, affordances, signifiers, data needs, edge cases, validation points, and backend/API dependencies.

Create rough black-and-white wireframes using simple boxes, placeholder icons, labels, arrows, handwritten-style notes, callouts, state notes, and annotations.

Include every screen or state needed: default/main view, create/add flow, edit flow, detail view, empty state, loading state, error state, no-results state, delete/confirmation flow, and mobile/narrow layout if relevant.

Return a wireframe specification that can be reviewed before implementation.

### Scope and evidence

Use supplied requirements, not invented features. Label missing data or behavior as an assumption or dependency. Include only states relevant to the feature, and explain any omitted state that the brief requires. “Balsamiq-style” describes low fidelity; do not claim to have created a native Balsamiq project unless that file was actually generated. Keep the output reviewable as annotated Markdown or clearly labeled wireframes; do not imply that a plan is an implemented interface.
````
<!-- prompt:end -->

## Usage notes

Supply the actual referenced material. A filename or URL does not grant the assistant file, browser, account, or edit access.

**Relevant capabilities:** `file-access`. These are requirements or conditional needs, not tools installed by this file.

## Related entries

- [Balsamiq UI State Map](balsamiq-ui-state-map.md) — Use when you want every meaningful UI state mapped before building.
- [Execution Plan From Approved Wireframe](execution-plan-from-approved-wireframe.md) — Use after wireframes are approved to create an implementation plan before coding.
- [Build From Approved Balsamiq Wireframe](build-from-approved-balsamiq-wireframe.md) — Use when the wireframe is approved and the agent should implement from it.

[Browse the catalog](../../../CATALOG.md) · [Usage guide](../../../docs/usage.md)
