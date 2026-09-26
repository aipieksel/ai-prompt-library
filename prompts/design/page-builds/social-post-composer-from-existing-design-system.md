---
id: "social-post-composer-from-existing-design-system"
title: "Social Post Composer From Existing Design System"
type: "prompt"
primary_category: "design"
categories: ["design"]
subcategory: "page-builds"
when_to_use: "Use to build a social post composer with list view, editor, platform-specific fields, and image picker modal"
search_terms: ["social-post-composer-from-existing-design-system", "design", "page-builds", "composer", "image-picker", "infinite-scroll", "linkedin", "post", "separate-css-js", "social"]
inputs: ["REFERENCE_FILES"]
output: "Full HTML, social-post-composer.css, and social-post-composer.js when required, scoped to .social-post-composer-page."
mode: "build"
capabilities: ["file-access", "visual-inspection"]
related: ["calendar-page-from-existing-design-system", "balsamiq-ui-state-map"]
aliases: ["design/page-feature-builds/social-post-composer-from-existing-design-system.md", "social-post-composer-from-existing-design-system.md"]
---

# Social Post Composer From Existing Design System

Use to build a social post composer with list view, editor, platform-specific fields, and image picker modal.

**Type:** prompt · **Mode:** build · **ID:** `social-post-composer-from-existing-design-system`

**Expected output:** Full HTML, social-post-composer.css, and social-post-composer.js when required, scoped to .social-post-composer-page.

## Inputs

Replace every listed placeholder. For an optional source, enter `None` when it is unavailable.

| Placeholder | What to provide | Example |
| --- | --- | --- |
| `{{REFERENCE_FILES}}` | App HTML, campaigns list, tokens, image library, and available post/platform configuration. | Existing ?tab=campaigns view and generated-assets section. |

## Prompt

Copy the block below, not the metadata or usage notes.

<!-- prompt:start -->
````text
Reference HTML/design system:
{{REFERENCE_FILES}}

Create a new Social Post Composer page using the attached HTML file as the design-system source of truth.

The page should include two main states:

1. Posts list view
2. Create/edit post view

When the Social Composer opens, show the all-posts list first. Show 10 posts at a time, then load the next 10 automatically as the user scrolls. Use the existing HTML ?tab=campaigns section as the structural and visual reference for the posts list. Reuse the same list/card structure, spacing, row layout, action placement, empty/loading states, buttons, typography, borders, and selected/hover states wherever possible.

The editor should only open after Create New Post or Edit is clicked. The create/edit view must include separate X and LinkedIn sections. Each platform must support its own content, link, date, status, character counter, allowed text length, and image assignment. Status options are Scheduled, Draft, and In Review.

Image selection should happen through a modal that shows images from the generated assets / image library section. After choosing an image, the user can assign it to X, LinkedIn, or both. Assigned images must have Change Image and Remove Image buttons. If one platform is missing an image, clearly prompt for another image.

Put all new page-specific CSS in social-post-composer.css and all new JavaScript in social-post-composer.js if JavaScript is required. Link both files from the HTML. Scope CSS and JS to .social-post-composer-page.

### Behavior and verification

Inspect whether the referenced ?tab=campaigns view and generated-assets library actually exist. If either is missing, identify that input rather than inventing an exact source layout or asset integration. Reuse supplied post data; label sample records as demonstrations.

Obtain platform text limits from supplied configuration or current official documentation. Do not hard-code a remembered limit as universal across account types. Keep content counters and validation separate for X and LinkedIn.

Prevent duplicate records during incremental loading. Include end-of-list, loading, empty, and error behavior. Check create/edit navigation, status selection, per-platform content/link/date validation, image assignment to either or both platforms, change/remove actions, modal keyboard handling, and mobile layout. Do not imply that the prototype publishes posts or saves remotely without an implemented backend.
````
<!-- prompt:end -->

## Usage notes

Supply the actual referenced material. A filename or URL does not grant the assistant file, browser, account, or edit access.

**Relevant capabilities:** `file-access`, `visual-inspection`. These are requirements or conditional needs, not tools installed by this file.

## Related entries

- [Calendar Page From Existing Design System](calendar-page-from-existing-design-system.md) — Use to build a scheduled-posts calendar overview using an existing HTML design system.
- [Balsamiq UI State Map](../wireframes/balsamiq-ui-state-map.md) — Use when you want every meaningful UI state mapped before building.

[Browse the catalog](../../../CATALOG.md) · [Usage guide](../../../docs/usage.md)
