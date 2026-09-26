---
id: "dashboard-balsamiq-wireframe"
title: "Dashboard Balsamiq Wireframe"
type: "prompt"
primary_category: "design"
categories: ["design"]
subcategory: "wireframes"
when_to_use: "Use when planning a dashboard/admin interface before implementation"
search_terms: ["dashboard-balsamiq-wireframe", "design", "wireframes", "admin", "balsamiq", "dashboard", "no-code", "planning", "ux", "wireframe"]
inputs: ["DASHBOARD_PURPOSE", "USERS", "CORE_ACTIONS", "DISPLAY_DATA", "REFERENCE_MATERIAL"]
output: "A dashboard wireframe covering the required flows and states."
mode: "plan"
capabilities: ["file-access"]
related: ["general-balsamiq-wireframe", "balsamiq-ui-state-map", "execution-plan-from-approved-wireframe", "build-from-approved-balsamiq-wireframe"]
aliases: ["design/wireframes/dashboard-balsamiq-wireframe.md", "dashboard-balsamiq-wireframe.md"]
---

# Dashboard Balsamiq Wireframe

Use when planning a dashboard/admin interface before implementation.

**Type:** prompt · **Mode:** plan · **ID:** `dashboard-balsamiq-wireframe`

**Expected output:** A dashboard wireframe covering the required flows and states.

## Inputs

Replace every listed placeholder. For an optional source, enter `None` when it is unavailable.

| Placeholder | What to provide | Example |
| --- | --- | --- |
| `{{DASHBOARD_PURPOSE}}` | What the dashboard is for. | Monitor scheduled publishing jobs. |
| `{{USERS}}` | Who uses it and their access roles. | Editors and administrators. |
| `{{CORE_ACTIONS}}` | Tasks users must complete. | Search jobs, inspect failures, and retry authorized jobs. |
| `{{DISPLAY_DATA}}` | Required records, metrics, statuses, and controls. | Job table, status counts, filters, and timestamps. |
| `{{REFERENCE_MATERIAL}}` | Current interface or design references, or None. | Existing app shell and table patterns. |

## Prompt

Copy the block below, not the metadata or usage notes.

<!-- prompt:start -->
````text
Dashboard description:
{{DASHBOARD_PURPOSE}}

Users:
{{USERS}}

Core actions:
{{CORE_ACTIONS}}

Data shown:
{{DISPLAY_DATA}}

Reference material:
{{REFERENCE_MATERIAL}}

Create a Balsamiq-style low-fidelity dashboard wireframe. Include dashboard header, navigation/sidebar, summary cards, main list/table/grid/card area, filters/search/sort controls, primary actions, secondary actions, status labels, detail view, create/edit flow, empty/loading/error/no-results states, confirmation states, and mobile/narrow layout where relevant.

Focus on structure, hierarchy, data visibility, and user flow. Do not implement the dashboard.

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
