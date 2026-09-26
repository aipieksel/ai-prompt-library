---
id: "create-design-system-showcase"
title: "Consolidate Sources Into a Design-System Showcase"
type: "prompt"
primary_category: "design"
categories: ["design"]
subcategory: "showcases"
when_to_use: "Consolidate extracted design evidence into one coherent, standalone HTML component showcase"
search_terms: ["create-design-system-showcase", "design", "showcases"]
inputs: ["SOURCE_FILES"]
output: "One complete standalone HTML design-system and component showcase."
mode: "build"
capabilities: ["file-access", "vision-when-needed", "browser"]
related: ["image-to-design-system-extraction-extended", "extend-vps-design-system-showcase", "research-vps-palette-comparison"]
aliases: ["design-system/create-design-system-showcase.md", "create-design-system-showcase.md"]
---

# Consolidate Sources Into a Design-System Showcase

Consolidate extracted design evidence into one coherent, standalone HTML component showcase.

**Type:** prompt · **Mode:** build · **ID:** `create-design-system-showcase`

**Expected output:** One complete standalone HTML design-system and component showcase.

**Not for:** Inventing a new visual identity or presenting six palette alternatives neutrally.

## Inputs

Replace every listed placeholder. For an optional source, enter `None` when it is unavailable.

| Placeholder | What to provide | Example |
| --- | --- | --- |
| `{{SOURCE_FILES}}` | All relevant extracted sources, with any canonical file identified. | design.md (canonical), source.css, recreated pages, screenshots, and extraction notes. |

## Prompt

Copy the block below, not the metadata or usage notes.

<!-- prompt:start -->
````text
Extracted source files, screenshots, and any explicitly canonical design reference:
{{SOURCE_FILES}}

You will receive a collection of extracted design-system documents, style notes, screenshots, recreated HTML files, CSS files, component notes, browser-inspection notes, and/or page recreation attempts from one website, dashboard, web app, or product interface.

These inputs may be messy, incomplete, duplicated, inconsistent, or partially inaccurate.

Your task is to consolidate all of the provided material into one complete HTML design-system showcase page.

The final output should act like a visual brand guide, component library, and implementation reference in one file.

It should show all major discovered styles, sections, components, layouts, patterns, states, and reusable UI elements from the analyzed pages in a clean, organized, implementation-ready showcase.

Do not create a normal marketing page.
Do not create a new website.
Do not redesign the brand from scratch.
Do not only summarize the design system in Markdown.
Do not blindly paste all extracted HTML together.
Do not include duplicate components unless they show meaningful variants.

Use the provided extracted material as source evidence, then normalize it into one coherent design guide page.

## Input types you may receive

You may receive any combination of:

- extracted design-system Markdown files
- visual audit notes
- browser inspection notes
- recreated HTML pages
- CSS files
- JavaScript files
- screenshots
- page/component mockups
- token lists
- component inventories
- layout notes
- typography notes
- color notes
- spacing notes
- accessibility notes
- interaction notes

Inspect all provided files before building.

## Goal

Create one complete HTML file that showcases the full extracted design system.

The page must include:

- global design tokens
- colors
- typography
- spacing
- radius
- shadows/elevation
- buttons
- links
- forms/inputs
- navigation patterns
- cards
- badges
- tables
- tabs
- accordions
- modals or overlays if discovered
- dropdowns or selects if discovered
- alerts/toasts if discovered
- charts/metrics if discovered
- dashboard panels if discovered
- hero/landing sections if discovered
- pricing/product sections if discovered
- feature sections if discovered
- footer patterns if discovered
- all meaningful component variants
- interaction states where possible
- responsive notes or examples
- component usage notes

The showcase should make it easy for a developer or designer to see the entire visual system at once and reuse the patterns later.

## Source handling rules

First analyze all inputs and identify:

- confirmed styles
- repeated tokens
- recurring component patterns
- page-specific one-off components
- duplicated components
- inconsistent recreation attempts
- missing but inferable styles
- design rules that appear stable across pages
- components that should be grouped into the same family
- components that should be shown as separate variants

If different files conflict, prefer the most repeated and visually consistent pattern.

If a recreated HTML file looks weaker than the notes or screenshots, do not preserve its bad execution. Use the extracted information to reconstruct the component more cleanly.

If exact values are known, use them.
If values are inferred, use sensible approximations and label them as inferred inside the showcase notes.

Do not invent a new design system. Consolidate the one provided.

## Output requirement

Return one complete standalone HTML file.

The HTML must include:

- internal CSS
- organized sections
- all showcased components
- realistic sample content
- component labels
- implementation notes inside the page
- responsive behavior
- accessible semantic structure

Use no external dependencies unless the provided design system already requires them.

If the extracted design system depends on a font, use the closest safe fallback unless the font is already available through the provided files.

Do not hotlink random external assets.
Do not include broken image links.
Use CSS/SVG placeholders only when the visual pattern matters and no real asset is available.

## Page structure

Build the showcase using this structure:

1. Showcase Header
2. Design System Overview
3. Token Reference
4. Typography System
5. Color System
6. Layout and Grid System
7. Core Components
8. Page Section Patterns
9. Dashboard/App Patterns
10. States and Interactions
11. Responsive Behavior
12. Usage Rules and Anti-Patterns
13. Component Index

Only include sections that make sense for the provided source material, but keep the page organized in this general order.

## 1. Showcase Header

Create a clear top section for the design-system showcase.

Include:

- design system name, inferred from the source if possible
- short description
- source summary
- last generated label
- quick links / sticky nav to major showcase sections

The header should use the extracted design language itself, not a generic documentation style.

## 2. Design System Overview

Summarize the visual language in the page itself.

Include:

- design direction
- product/interface type
- brand mood
- density level
- primary UI patterns
- strongest reusable components
- key implementation constraints

Keep this concise and practical.

## 3. Token Reference

Create a token overview section.

Include tables or cards for:

- colors
- typography
- spacing
- radii
- borders
- shadows/elevation
- transitions/motion if found
- z-index/layering if found

Each token should show:

- token name
- value
- usage
- confidence: confirmed / inferred

Use visual swatches for colors.

## 4. Typography System

Show the extracted typography as rendered examples.

Include:

- display heading
- H1
- H2
- H3
- H4
- body text
- small text
- labels
- metadata
- button text
- code/mono text if relevant

For each typography sample, show:

- visual example
- usage note
- approximate size/weight/line-height if known

## 5. Color System

Show the color palette as swatches.

Include:

- primary colors
- accent colors
- semantic colors
- backgrounds
- surfaces
- borders
- text colors
- muted colors
- hover/focus colors where known

Each swatch must have visible contrast and labels.

## 6. Layout and Grid System

Show layout patterns discovered across the extracted sources.

Include examples such as:

- content container
- two-column layout
- three-column grid
- four-column grid
- sidebar/content layout
- dashboard shell
- hero split layout
- card grid
- table layout
- responsive stacking behavior

Use real component-style examples, not just abstract boxes.

## 7. Core Components

Create a component library section.

For each component family, include:

- component name
- visual example
- variants
- states
- usage notes
- do/don’t notes if relevant

Component families may include:

### Buttons

Show:
- primary
- secondary
- ghost
- outline
- destructive
- disabled
- icon button
- button with icon
- small/large variants if found

### Cards

Show:
- default card
- feature card
- product card
- metric card
- dashboard panel
- selected/active card
- warning/info card
- compact card

### Badges and Labels

Show:
- status badges
- category pills
- metadata labels
- success/warning/error/info states

### Forms

Show:
- text input
- textarea
- select/dropdown
- checkbox
- radio
- toggle
- search input
- validation states
- helper text
- disabled state

### Navigation

Show:
- header nav
- sidebar nav
- tabs
- breadcrumbs
- pagination
- mobile nav behavior if discovered

### Tables and Lists

Show:
- standard table
- comparison table
- data table
- compact list
- row actions
- empty table state

### Feedback

Show:
- alert
- toast
- modal
- confirmation panel
- empty state
- loading/skeleton state if discovered

Only include components that are supported by the provided material or reasonably inferable from repeated patterns.

## 8. Page Section Patterns

Show larger page sections discovered from the source pages.

Examples may include:

- hero section
- feature grid
- pricing section
- product comparison
- testimonials / trust proof
- FAQ section
- CTA banner
- footer
- setup/workflow section
- architecture diagram section
- use-case section
- related links section

Each section example should look like a real reusable section, not a wireframe.

For each section, include a small label explaining:

- source pattern
- intended use
- key components inside it

## 9. Dashboard/App Patterns

If the extracted material includes dashboards, apps, admin panels, or client areas, include a dashboard pattern section.

Show:

- app shell
- sidebar
- topbar
- table/card layout
- settings panel
- inspector panel
- detail view
- split view
- metric cards
- filters
- editor/list/detail layout
- empty state
- action toolbar

If the extracted material is only a marketing website, omit this section.

## 10. States and Interactions

Show component states where possible.

Include:

- default
- hover
- focus
- active
- selected
- disabled
- loading
- empty
- error
- success
- warning
- destructive confirmation

For hover/focus states, use static examples or CSS hover styles.

## 11. Responsive Behavior

Add a section that documents how the system should respond.

Include:

- desktop behavior
- tablet behavior
- mobile behavior
- grid collapse rules
- nav collapse rules
- table overflow rules
- card stacking rules
- hero stacking rules
- form behavior
- CTA behavior

Include at least one responsive sample section if practical.

## 12. Usage Rules and Anti-Patterns

Create practical rules for future use.

Include:

### Do

- reuse the extracted tokens
- use the correct component family
- preserve spacing rhythm
- preserve typography hierarchy
- use the right CTA hierarchy
- preserve card/border/radius rules
- keep sections aligned to the same container
- keep states consistent

### Do not

- invent new colors
- mix unrelated radii
- overuse shadows
- create generic SaaS cards if the source has specific card anatomy
- use page-specific components as global patterns without reason
- duplicate components unnecessarily
- hardcode values when tokens exist
- add fake content or proof

## 13. Component Index

At the end, create a compact index of all showcased components.

Use a table:

| Component | Variants shown | Source confidence | Notes |
| --- | --- | --- | --- |

## Component consolidation rules

When similar components appear across multiple pages:

- merge them into one component family
- show meaningful variants
- remove duplicates
- preserve important differences
- document where each variant should be used

Example:
If three pages have slightly different feature cards, create one “Feature Card” component with variants such as:
- icon-top
- icon-left
- compact
- highlighted

Do not create three unrelated feature-card systems unless they are truly different.

## HTML quality rules

The final HTML must be:

- complete
- standalone
- valid
- responsive
- accessible
- readable
- well-organized
- easy to edit
- implementation-friendly

Use semantic HTML:

- header
- main
- section
- nav
- table
- button
- form controls
- footer

Add accessible labels where needed.

Use CSS variables for tokens.

Organize CSS into sections:

1. Root tokens
2. Base styles
3. Layout
4. Components
5. Section patterns
6. States
7. Responsive rules

## Visual fidelity rules

The showcase should feel like it belongs to the extracted brand/design system.

Do not make it look like generic documentation unless the source design itself is documentation-style.

The showcase page should itself be a polished example of the design system.

If the source is dark, make the showcase dark.
If the source is light, make the showcase light.
If the source has both modes, include light/dark examples or a mode section.

## Final review before returning

Before returning the HTML, verify:

- all source files were inspected
- duplicate components were consolidated
- major tokens are represented
- all major component families are shown
- page section patterns are included
- states are represented
- the showcase itself follows the extracted design system
- no fake claims or unsupported copy were added
- no broken asset links are included
- responsive behavior works
- the HTML is complete and ready to save

## Final output

Return the complete HTML file only.

Do not return a Markdown summary instead.
Do not return fragments.
Do not return only CSS.
Do not return only a component inventory.
Do not say “rest of file unchanged.”
Return the full standalone HTML document from `<!doctype html>` to `</html>`.

### Conflict resolution and evidence

Use an explicitly approved canonical design contract first. Inspect original HTML/CSS and visible screenshots before trusting a recreation attempt. Repeated generated copies are not independent evidence, so majority agreement does not override authoritative source material. Keep a short provenance and conflict note inside the showcase for material decisions.

Consolidate duplicate examples by component family while retaining every meaningful variant, state, section pattern, and unique source requirement. Do not remove content or components merely to make the showcase shorter. Mark absent behavior or token values as inferred/proposed rather than verified. Demonstration data must be labeled; no sample metric, review, logo, or claim may appear to be real evidence.

This showcase should use the extracted design language. It is not the neutral six-palette comparison document. Test only with available tools and distinguish static review from rendered checks inside the QA section. Do not claim all viewport checks passed when they were not run.
````
<!-- prompt:end -->

## Usage notes

Supply the actual referenced material. A filename or URL does not grant the assistant file, browser, account, or edit access.

**Relevant capabilities:** `file-access`, `vision-when-needed`, `browser`. These are requirements or conditional needs, not tools installed by this file.

## Related entries

- [Extract Images Into a Reusable Design Contract](../extraction/image-to-design-system-extraction-extended.md) — Produce a detailed visual extraction plus a reusable token-and-component implementation contract.
- [Extend a Showcase With VPS Website Components](extend-vps-design-system-showcase.md) — Extend an existing dashboard showcase with a complete VPS website component layer and updated documentation.
- [Compare Six VPS Brand Palettes](research-vps-palette-comparison.md) — Compare six palettes in a neutral editorial HTML document while preserving a fixed dark-indigo brand anchor.

[Browse the catalog](../../../CATALOG.md) · [Usage guide](../../../docs/usage.md)
