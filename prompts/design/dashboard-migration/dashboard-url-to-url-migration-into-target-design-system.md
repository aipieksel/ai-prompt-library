---
id: "dashboard-url-to-url-migration-into-target-design-system"
title: "Dashboard URL-to-URL Migration Into Target Design System"
type: "prompt"
primary_category: "design"
categories: ["design"]
subcategory: "dashboard-migration"
when_to_use: "Use when the source and target are live WordPress/admin dashboard URLs instead of files"
search_terms: ["dashboard-url-to-url-migration-into-target-design-system", "design", "dashboard-migration", "dashboard", "dashboard-url", "migration", "source-url", "system", "target", "target-url"]
inputs: ["SOURCE_URL", "TARGET_URL", "TARGET_PROJECT"]
output: "Migrated target files and verification, or an explicitly labeled plan when edit access is missing."
mode: "edit"
capabilities: ["file-access", "authenticated-browser", "code-execution"]
related: ["wordpress-admin-dashboard-migration-into-existing-plugin-design-system", "html-content-and-layout-import-into-existing-design-system"]
aliases: ["design/dashboard-migration/dashboard-url-to-url-migration-into-target-design-system.md", "dashboard-url-to-url-migration-into-target-design-system.md"]
---

# Dashboard URL-to-URL Migration Into Target Design System

Use when the source and target are live WordPress/admin dashboard URLs instead of files.

**Type:** prompt · **Mode:** edit · **ID:** `dashboard-url-to-url-migration-into-target-design-system`

**Expected output:** Migrated target files and verification, or an explicitly labeled plan when edit access is missing.

## Inputs

Replace every listed placeholder. For an optional source, enter `None` when it is unavailable.

| Placeholder | What to provide | Example |
| --- | --- | --- |
| `{{SOURCE_URL}}` | Source dashboard URL accessible with authorized tools. | An authenticated source dashboard URL. |
| `{{TARGET_URL}}` | Dashboard whose design and architecture must be retained. | An authenticated target dashboard URL. |
| `{{TARGET_PROJECT}}` | Editable target repository/files, or None for planning only. | Target plugin files and development environment. |

## Prompt

Copy the block below, not the metadata or usage notes.

<!-- prompt:start -->
````text
Source dashboard URL:
{{SOURCE_URL}}

Target dashboard URL:
{{TARGET_URL}}

Target codebase or editable files:
{{TARGET_PROJECT}}

Inspect the source and target dashboards using authorized access. Migrate the relevant source sections, controls, fields, labels, filters, tables, widgets, user flows, interactions, and functional intent into the target.

Use the target as the authority for visual style, design system, admin layout, CSS variables, components, JavaScript patterns, WordPress conventions where applicable, and implementation architecture. Use the source as the authority for the experience being migrated. Do not copy its CSS or make the target look like the source.

Map the source inventory to target components before editing. Preserve unrelated target functionality. Implement required behavior in the target architecture and check every migrated flow, permission boundary, and responsive state.

A URL is not write access to a codebase. If either URL is inaccessible, identify which failed and request screenshots, exported HTML, plugin files, or page source. If editable target files are unavailable, return a clearly labeled migration plan instead of claiming implementation. Never request credentials in a public prompt or bypass authentication.

When implementation access is available, return the changed target files with exact paths, migrated-item coverage, and actual verification results.
````
<!-- prompt:end -->

## Usage notes

Supply the actual referenced material. A filename or URL does not grant the assistant file, browser, account, or edit access.

**Relevant capabilities:** `file-access`, `authenticated-browser`, `code-execution`. These are requirements or conditional needs, not tools installed by this file.

## Related entries

- [WordPress Admin Dashboard Migration Into Existing Plugin Design System](wordpress-admin-dashboard-migration-into-existing-plugin-design-system.md) — Use when migrating one plugin/admin dashboard into another while keeping the target plugin design system.
- [HTML Content and Layout Import Into Existing Design System](../style-transfer/html-content-and-layout-import-into-existing-design-system.md) — Use when you want to import another HTML file’s layout/content into your current HTML but keep your current design system.

[Browse the catalog](../../../CATALOG.md) · [Usage guide](../../../docs/usage.md)
