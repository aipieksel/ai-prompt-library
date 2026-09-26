---
id: "wordpress-plugin-admin-balsamiq-wireframe"
title: "WordPress Plugin Admin Balsamiq Wireframe"
type: "prompt"
primary_category: "design"
categories: ["design"]
subcategory: "wireframes"
when_to_use: "Use when planning a WordPress plugin admin page before PHP/CSS/JS implementation"
search_terms: ["wordpress-plugin-admin-balsamiq-wireframe", "design", "wireframes", "admin", "balsamiq", "no-code", "planning", "plugin", "plugin-admin", "ux"]
inputs: ["PAGE_REQUEST", "TARGET_PLUGIN", "SOURCE_REQUIREMENTS"]
output: "A WordPress admin wireframe and behavior notes; no PHP, CSS, or JavaScript."
mode: "plan"
capabilities: ["file-access"]
related: ["general-balsamiq-wireframe", "balsamiq-ui-state-map", "execution-plan-from-approved-wireframe", "build-from-approved-balsamiq-wireframe"]
aliases: ["design/wireframes/wordpress-plugin-admin-balsamiq-wireframe.md", "wordpress-plugin-admin-balsamiq-wireframe.md"]
---

# WordPress Plugin Admin Balsamiq Wireframe

Use when planning a WordPress plugin admin page before PHP/CSS/JS implementation.

**Type:** prompt · **Mode:** plan · **ID:** `wordpress-plugin-admin-balsamiq-wireframe`

**Expected output:** A WordPress admin wireframe and behavior notes; no PHP, CSS, or JavaScript.

## Inputs

Replace every listed placeholder. For an optional source, enter `None` when it is unavailable.

| Placeholder | What to provide | Example |
| --- | --- | --- |
| `{{PAGE_REQUEST}}` | What the WordPress admin page needs to do. | Manage import jobs and review failures. |
| `{{TARGET_PLUGIN}}` | Existing plugin files, admin layout, and design system. | Plugin admin wrapper, navigation, and table examples. |
| `{{SOURCE_REQUIREMENTS}}` | Features to add, migrate, or redesign. | Filtering, record detail, retries, and permission rules. |

## Prompt

Copy the block below, not the metadata or usage notes.

<!-- prompt:start -->
````text
Plugin/admin page description:
{{PAGE_REQUEST}}

Existing target plugin/design system:
{{TARGET_PLUGIN}}

Source requirements:
{{SOURCE_REQUIREMENTS}}

Create Balsamiq-style wireframes for the WordPress plugin admin page before implementation. Include WordPress admin wrapper/page structure, header, tabs/navigation, settings/content panels, tables/lists/cards, forms and fields, save/apply/reset actions, notices, validation states, loading/empty/error states, confirmations, modals/drawers/popovers, permission notes, nonce/AJAX/REST behavior notes, and responsive behavior inside WordPress admin.

Do not write PHP, CSS, or JavaScript yet.

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
