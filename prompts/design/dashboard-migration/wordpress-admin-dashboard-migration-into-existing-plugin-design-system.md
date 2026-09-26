---
id: "wordpress-admin-dashboard-migration-into-existing-plugin-design-system"
title: "WordPress Admin Dashboard Migration Into Existing Plugin Design System"
type: "prompt"
primary_category: "design"
categories: ["design"]
subcategory: "dashboard-migration"
when_to_use: "Use when migrating one plugin/admin dashboard into another while keeping the target plugin design system"
search_terms: ["wordpress-admin-dashboard-migration-into-existing-plugin-design-system", "design", "dashboard-migration", "admin", "dashboard", "migration", "plugin", "plugin-admin", "security", "system"]
inputs: ["TARGET_PLUGIN", "SOURCE_DASHBOARD"]
output: "Updated target plugin files, migrated-item coverage, and verification status."
mode: "edit"
capabilities: ["file-access", "code-execution", "visual-inspection"]
related: ["dashboard-url-to-url-migration-into-target-design-system", "wordpress-plugin-admin-balsamiq-wireframe"]
aliases: ["design/dashboard-migration/wordpress-admin-dashboard-migration-into-existing-plugin-design-system.md", "wordpress-admin-dashboard-migration-into-existing-plugin-design-system.md"]
---

# WordPress Admin Dashboard Migration Into Existing Plugin Design System

Use when migrating one plugin/admin dashboard into another while keeping the target plugin design system.

**Type:** prompt · **Mode:** edit · **ID:** `wordpress-admin-dashboard-migration-into-existing-plugin-design-system`

**Expected output:** Updated target plugin files, migrated-item coverage, and verification status.

## Inputs

Replace every listed placeholder. For an optional source, enter `None` when it is unavailable.

| Placeholder | What to provide | Example |
| --- | --- | --- |
| `{{TARGET_PLUGIN}}` | Editable target plugin and design-system files. | target-plugin/ and DESIGN.md |
| `{{SOURCE_DASHBOARD}}` | Source dashboard files, exported HTML, or authorized reference. | source-plugin/admin/dashboard.php and related handlers. |

## Prompt

Copy the block below, not the metadata or usage notes.

<!-- prompt:start -->
````text
Target plugin files and design system:
{{TARGET_PLUGIN}}

Source plugin dashboard:
{{SOURCE_DASHBOARD}}

Migrate the relevant source layout, sections, controls, fields, labels, options, text, flows, and functional intent into the target WordPress plugin dashboard.

Inspect both implementations first. Keep the target's design system, CSS architecture, WordPress admin structure, components, tokens, scripts, and naming conventions. Translate source requirements into target components rather than copying source CSS, classes, global styles, scripts, assets, or layout code blindly.

Preserve unrelated target functionality. Map source actions and data requirements to actual target handlers. Do not expose a control as functional when its integration is missing; show the appropriate disabled or unavailable state and identify the gap.

Preserve and verify capability checks, nonces, sanitization, escaping, translation functions, scoped enqueueing, AJAX/REST conventions, and safe admin hooks. Inspect the existing project patterns and current official documentation where a security or API detail needs confirmation.

Check migrated interactions, permission boundaries, forms, notices, empty/error states, navigation, and responsive layout. Return updated target plugin files with exact paths, a migration coverage summary, and checks performed or blocked.
````
<!-- prompt:end -->

## Usage notes

Supply the actual referenced material. A filename or URL does not grant the assistant file, browser, account, or edit access.

**Relevant capabilities:** `file-access`, `code-execution`, `visual-inspection`. These are requirements or conditional needs, not tools installed by this file.

## Related entries

- [Dashboard URL-to-URL Migration Into Target Design System](dashboard-url-to-url-migration-into-target-design-system.md) — Use when the source and target are live WordPress/admin dashboard URLs instead of files.
- [WordPress Plugin Admin Balsamiq Wireframe](../wireframes/wordpress-plugin-admin-balsamiq-wireframe.md) — Use when planning a WordPress plugin admin page before PHP/CSS/JS implementation.

[Browse the catalog](../../../CATALOG.md) · [Usage guide](../../../docs/usage.md)
