---
id: "calendar-page-from-existing-design-system"
title: "Calendar Page From Existing Design System"
type: "prompt"
primary_category: "design"
categories: ["design"]
subcategory: "page-builds"
when_to_use: "Use to build a scheduled-posts calendar overview using an existing HTML design system"
search_terms: ["calendar-page-from-existing-design-system", "design", "page-builds", "calendar", "existing-design-system", "page", "scheduled-posts", "separate-css", "system"]
inputs: ["REFERENCE_FILES"]
output: "A full new calendar HTML page and scheduled-posts-calendar.css scoped to .scheduled-calendar-page."
mode: "build"
capabilities: ["file-access", "visual-inspection"]
related: ["social-post-composer-from-existing-design-system", "dashboard-balsamiq-wireframe"]
aliases: ["design/page-feature-builds/calendar-page-from-existing-design-system.md", "calendar-page-from-existing-design-system.md"]
---

# Calendar Page From Existing Design System

Use to build a scheduled-posts calendar overview using an existing HTML design system.

**Type:** prompt · **Mode:** build · **ID:** `calendar-page-from-existing-design-system`

**Expected output:** A full new calendar HTML page and scheduled-posts-calendar.css scoped to .scheduled-calendar-page.

## Inputs

Replace every listed placeholder. For an optional source, enter `None` when it is unavailable.

| Placeholder | What to provide | Example |
| --- | --- | --- |
| `{{REFERENCE_FILES}}` | Existing app HTML/design system, plus available scheduled-post data. | App shell, posts data, and current tokens. |

## Prompt

Copy the block below, not the metadata or usage notes.

<!-- prompt:start -->
````text
Request:
Create a calendar overview page for scheduled posts.

Reference HTML/design system:
{{REFERENCE_FILES}}

Create a new Calendar / Scheduled Posts overview page using the attached HTML file as the design-system source of truth.

The page should show posts scheduled by day and platform, including X and LinkedIn. It must support multiple posts on the same day, platform indicators or badges, a legend, summary counts, month navigation, filters, and a responsive mobile layout.

Use existing CSS variables, typography, spacing, colors, borders, shadows, radius, layout primitives, buttons, cards, inputs, navigation, and component patterns already present in the reference file. Do not create a new visual identity or unrelated CSS system.

Put all new calendar-specific CSS in a separate file named scheduled-posts-calendar.css, scoped under .scheduled-calendar-page. Return the full new HTML page and the separate CSS file.

### Behavior and verification

Use supplied post data; explicitly label demonstration records as sample data when no real source is provided. Distinguish the displayed calendar month from filtering and selection state. Make month navigation and filters work in the implemented context, or clearly identify unavailable backend behavior. Keep X and LinkedIn indicators understandable without color alone.

Verify multiple posts per day, empty days, an empty filtered result, month changes, and narrow layouts. Scope any necessary JavaScript to the calendar page and preserve unrelated reference behavior.
````
<!-- prompt:end -->

## Usage notes

Supply the actual referenced material. A filename or URL does not grant the assistant file, browser, account, or edit access.

**Relevant capabilities:** `file-access`, `visual-inspection`. These are requirements or conditional needs, not tools installed by this file.

## Related entries

- [Social Post Composer From Existing Design System](social-post-composer-from-existing-design-system.md) — Use to build a social post composer with list view, editor, platform-specific fields, and image picker modal.
- [Dashboard Balsamiq Wireframe](../wireframes/dashboard-balsamiq-wireframe.md) — Use when planning a dashboard/admin interface before implementation.

[Browse the catalog](../../../CATALOG.md) · [Usage guide](../../../docs/usage.md)
