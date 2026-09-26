---
id: "build-from-approved-balsamiq-wireframe"
title: "Build From Approved Balsamiq Wireframe"
type: "prompt"
primary_category: "design"
categories: ["design"]
subcategory: "wireframes"
when_to_use: "Use when the wireframe is approved and the agent should implement from it"
search_terms: ["build-from-approved-balsamiq-wireframe", "design", "wireframes", "approved", "approved-wireframe", "balsamiq", "build", "codebase-first", "implementation", "wireframe"]
inputs: ["APPROVED_WIREFRAMES", "PROJECT_CONTEXT"]
output: "Implementation files matching the approved wireframes, with verification."
mode: "edit"
capabilities: ["file-access", "code-execution", "visual-inspection"]
related: ["general-balsamiq-wireframe", "balsamiq-ui-state-map", "execution-plan-from-approved-wireframe"]
aliases: ["design/wireframes/build-from-approved-balsamiq-wireframe.md", "build-from-approved-balsamiq-wireframe.md"]
---

# Build From Approved Balsamiq Wireframe

Use when the wireframe is approved and the agent should implement from it.

**Type:** prompt · **Mode:** edit · **ID:** `build-from-approved-balsamiq-wireframe`

**Expected output:** Implementation files matching the approved wireframes, with verification.

## Inputs

Replace every listed placeholder. For an optional source, enter `None` when it is unavailable.

| Placeholder | What to provide | Example |
| --- | --- | --- |
| `{{APPROVED_WIREFRAMES}}` | Approved layouts, state maps, and flow annotations. | Approved wireframe specification. |
| `{{PROJECT_CONTEXT}}` | Editable files, architecture, stack, and design system. | Repository, component library, routes, and relevant handlers. |

## Prompt

Copy the block below, not the metadata or usage notes.

<!-- prompt:start -->
````text
Approved wireframes:
{{APPROVED_WIREFRAMES}}

Codebase / project context:
{{PROJECT_CONTEXT}}

Implement the feature using the approved Balsamiq-style wireframes as the source of truth. Before coding, inspect the relevant files and existing architecture.

Use the wireframes for screen structure, views, states, flows, controls, fields, actions, modals/drawers/popovers, empty/loading/error states, validation points, and responsive behavior. Use the codebase for file structure, naming conventions, CSS architecture, component patterns, JavaScript patterns, backend/API patterns, state management, security practices, and design system.

Return the final implementation with exact files changed or created. Review the result against the approved wireframes before returning.

Verify screen, state, flow, and control coverage against the approved wireframes. Run available tests and visual checks; report checks that could not run. Do not silently redesign the feature or omit a required state.
````
<!-- prompt:end -->

## Usage notes

Supply the actual referenced material. A filename or URL does not grant the assistant file, browser, account, or edit access.

**Relevant capabilities:** `file-access`, `code-execution`, `visual-inspection`. These are requirements or conditional needs, not tools installed by this file.

## Related entries

- [General Balsamiq Wireframe](general-balsamiq-wireframe.md) — Use for any project, feature, dashboard, page, workflow, or interface before implementation.
- [Balsamiq UI State Map](balsamiq-ui-state-map.md) — Use when you want every meaningful UI state mapped before building.
- [Execution Plan From Approved Wireframe](execution-plan-from-approved-wireframe.md) — Use after wireframes are approved to create an implementation plan before coding.

[Browse the catalog](../../../CATALOG.md) · [Usage guide](../../../docs/usage.md)
