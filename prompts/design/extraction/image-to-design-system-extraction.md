---
id: "image-to-design-system-extraction"
title: "Extract a Design System From Images"
type: "prompt"
primary_category: "design"
categories: ["design"]
subcategory: "extraction"
when_to_use: "Document visible copy, page anatomy, reusable components, and inferred design rules from image references"
search_terms: ["image-to-design-system-extraction", "design", "extraction"]
inputs: ["IMAGE_REFERENCES", "SUPPORTING_CONTEXT"]
output: "One complete Markdown extraction covering visible copy, structure, components, and design rules."
mode: "extract"
capabilities: ["vision", "file-access"]
related: ["image-to-design-system-extraction-extended", "create-design-system-showcase", "implementation-handoff-docs-from-mockup-or-html"]
aliases: ["design/image-to-design-system-extraction.md", "image-to-design-system-extraction.md"]
---

# Extract a Design System From Images

Document visible copy, page anatomy, reusable components, and inferred design rules from image references.

**Type:** prompt · **Mode:** extract · **ID:** `image-to-design-system-extraction`

**Expected output:** One complete Markdown extraction covering visible copy, structure, components, and design rules.

## Inputs

Replace every listed placeholder. For an optional source, enter `None` when it is unavailable.

| Placeholder | What to provide | Example |
| --- | --- | --- |
| `{{IMAGE_REFERENCES}}` | One or more accessible reference images, with filenames or screen labels. | home-desktop.png and home-mobile.png |
| `{{SUPPORTING_CONTEXT}}` | Optional approved HTML/CSS, brand rules, brief, and explicit corrections; use None if absent. | None |

## Prompt

Copy the block below, not the metadata or usage notes.

<!-- prompt:start -->
````text
Image references:
{{IMAGE_REFERENCES}}

Supporting source files or context (None when absent):
{{SUPPORTING_CONTEXT}}

### Evidence rules

Use only images actually supplied and accessible. Record which image supports each region, component, or token. Read visible text directly where possible; transcribe it faithfully, mark uncertain text [approximate] and illegible text [unreadable], and do not reconstruct missing wording as fact.

A screenshot does not establish hidden behavior, exact font identity, breakpoint values, hover states, animation, or off-screen content. Mark estimates and responsive proposals as inferred with confidence. Use unknown for unsupported token values. Clearly separate a documented observation from an implementation recommendation. Exact values from approved HTML/CSS can refine estimates; record their source.

You will receive one or more reference images, screenshots, mockups, page previews, app screens, interface captures, component screenshots, full-page screenshots, or visual design references.

Task:
Analyze the provided image reference systematically and precisely, distinguishing observation from inference, then document the complete design, style, layout, copy, sections, components, visual system, and implementation guidance so another agent can recreate, extend, or implement it with explicit evidence, confidence, and unresolved details rather than hidden guesses.

Do not loosely describe the image.
Do not summarize only the obvious parts.
Do not force the image into a generic landing page, dashboard, app screen, SaaS page, ecommerce page, or website template structure.

Use the image as the visual source of truth.

If additional context is provided, such as brand name, product type, target page, existing CSS, HTML, scope file, design-system file, or implementation constraints, use that context only to clarify the extraction. Do not override what is visible in the image unless the supporting file explicitly corrects it.

If multiple images are provided, analyze each one individually first, then extract the shared design system and reusable patterns across the set.

## Core objective

Create a precise Markdown design extraction document that captures:

- what the image looks like
- what copy is visible
- how the page or screen is structured
- how the design system works
- what components are reusable
- what layout rules are visible or inferable
- what another agent must preserve
- what another agent must avoid
- how to rebuild or extend the design accurately

The result should be practical enough for an implementation agent to recreate the design in HTML/CSS or apply the same design language to another page or interface.

## Analysis workflow

Before writing the final document, inspect the image carefully and treat it as the visual source of truth.

Do not assume the image follows a standard website, dashboard, app, landing page, SaaS, ecommerce, or marketing structure. First identify what kind of interface, page, screen, component, or visual system the image appears to show, then document it according to what is actually visible.

Analyze the image from the largest structure down to the smallest visible details:

1. Overall composition

Identify the full layout, visual hierarchy, page/screen type, content flow, density, alignment, whitespace, focal points, section rhythm, viewport assumptions, and how the viewer’s eye is guided through the design.

Describe:
- the dominant layout structure
- the main focal area
- the primary conversion or interaction path
- the balance between content and visuals
- the use of empty space
- the overall density
- the visual mood
- the level of polish
- the intended product/category feel

2. Visible regions and sections

Identify every meaningful region in the image based on what is visible, not based on a fixed checklist.

This may include:
- navigation
- hero areas
- sidebars
- topbars
- cards
- dashboards
- forms
- panels
- tables
- comparison blocks
- pricing blocks
- visual components
- charts
- content sections
- product cards
- step cards
- CTA banners
- trust sections
- review areas
- FAQ accordions
- footers
- modals
- drawers
- tabs
- filters
- command bars
- media areas
- decorative backgrounds
- any other interface structure present in the image

Do not ignore a visible region because it does not match a known website section name.

3. Content and copy

Extract all readable text from the image.

Include:
- headings
- subheadings
- navigation labels
- CTA labels
- button text
- card titles
- card body copy
- badges
- labels
- table text
- comparison row labels
- form labels
- helper text
- metadata
- pricing text
- trust indicators
- review snippets
- FAQ questions
- footer headings
- footer links
- small UI labels
- visual labels inside mockups or illustrations

Rules:
- Preserve exact wording where readable.
- Preserve capitalization where readable.
- Preserve punctuation where readable.
- Mark uncertain text as [approximate].
- Mark unreadable text as [unreadable].
- Do not invent exact copy when it cannot be read.
- If copy is too small but the purpose is clear, summarize the purpose and mark it as inferred.

4. Visual system

Extract the design language from the image.

Document:
- color palette
- typography
- spacing rhythm
- grid logic
- alignment rules
- border treatment
- radius system
- shadow/elevation style
- surface hierarchy
- divider style
- icon style
- illustration style
- image treatment
- background treatment
- decorative patterns
- gradients
- visual effects
- CTA hierarchy
- card hierarchy
- section rhythm
- responsive implications

Do not say “modern”, “clean”, “premium”, or “professional” without explaining the actual visual properties that create that effect.

5. Component system

Identify reusable components from the image based on repeated structure or visual logic.

Do not limit this to standard web components.

Name each component according to its purpose and anatomy.

Examples:
- global header
- primary hero
- recommendation card
- proof strip
- feature card
- use-case card
- comparison table
- setup step card
- checklist row
- pricing card
- CTA banner
- FAQ row
- footer link group
- visual mockup
- status badge
- icon tile
- testimonial card
- side info card
- metric card
- form control
- dashboard panel
- tab group
- filter control
- modal panel
- image frame
- decorative background system

For each reusable component, document:
- purpose
- anatomy
- layout behavior
- visual styling
- text/copy pattern
- spacing
- interaction implication
- implementation notes

6. Interaction and behavior implications

Infer likely interactions only where the visual design clearly implies them.

Examples:
- buttons
- links
- dropdowns
- tabs
- accordions
- filters
- forms
- search fields
- cards that look clickable
- comparison rows
- modals
- drawers
- pagination
- sliders
- carousel controls
- copy buttons
- pricing toggles
- mobile menus

Do not invent behavior that is not visually implied.

Mark inferred behavior clearly.

7. Responsive and implementation implications

Infer how the layout should likely adapt on tablet and mobile.

Identify what should:
- stack
- collapse
- scroll
- resize
- become a dropdown
- become a carousel
- become an accordion
- remain fixed
- become full-width
- reduce typography scale
- simplify spacing
- preserve CTA visibility

Mark these as inferred when the image only shows desktop.

8. Accuracy pass

Re-check the image for small details that are easy to miss.

Look for:
- microcopy
- tiny labels
- icon styling
- badge shapes
- border weights
- card shadows
- background textures
- soft glows
- section dividers
- row dividers
- CTA hierarchy
- pricing details
- trust markers
- footer links
- small illustration labels
- repeated layout rules
- subtle color changes
- hover/active state implications
- text alignment
- optical spacing

Do not flatten the image into a generic template.

If the image contains an unusual layout or custom visual pattern, document that pattern directly instead of translating it into a generic component name.

## Output

Return one complete Markdown document with the following structure:

# Design Extraction From Image Reference

## 1. Executive Summary

Summarize the design direction in a few precise paragraphs.

Include:
- what type of page, screen, component, or interface this appears to be
- overall visual style
- product or use-case category
- primary user impression
- design maturity level
- main layout strategy
- strongest reusable patterns
- main visual hierarchy
- most important implementation constraints

Avoid vague statements. Explain what creates the style.

## 2. Image Type and Structural Classification

Identify what the image appears to be.

Include:
- image type: full-page screenshot, app screen, component mockup, landing page, dashboard, product card, mobile screen, etc.
- visible viewport or crop assumption
- whether the image shows a complete page or partial section
- whether the design is marketing-focused, product-focused, dashboard-focused, editorial, app-like, technical, ecommerce, or another category
- whether the layout is standard or custom
- any visible brand/product context

## 3. Full Structure Breakdown

Document the visible structure in order from top to bottom or from outer shell inward, depending on the image type.

Do not use a fixed section checklist. Create section names based on what is actually visible.

For each visible region or section, include:

### Section / Region: [name]

Purpose:
[what this region does]

Visible content:
- Heading:
- Supporting copy:
- CTA/buttons:
- Cards/items:
- Labels/badges:
- Links:
- Other visible text:

Layout:
[describe columns, grid, alignment, spacing, visual hierarchy, and how it relates to surrounding sections]

Visual treatment:
[background, cards, typography, colors, borders, icons, illustration, shadows, spacing]

Implementation notes:
[what an implementation agent must preserve]

Confidence:
High / Medium / Low

If a region is visible but unclear, still document it and mark uncertainty.

## 4. Copy Inventory

Extract all readable copy from the image.

Group the copy by visible region.

Use this structure:

### [Region name]

- [Exact visible text]
- [Exact visible text]
- [approximate] [text]
- [unreadable] [location or role of unreadable text]

Rules:
- Preserve spelling and capitalization where readable.
- Preserve CTA labels exactly.
- Preserve visible headings exactly.
- Preserve card titles exactly.
- Preserve navigation labels exactly.
- Mark uncertain text as [approximate].
- Mark unreadable text as [unreadable].
- Do not invent missing copy.

## 5. Visual Hierarchy

Document how the design guides attention.

Include:
- primary focal point
- secondary focal points
- how CTAs are prioritized
- how headings differ from body copy
- how cards or sections are grouped
- how color creates hierarchy
- how spacing creates hierarchy
- how icons or visuals support hierarchy
- where the user is expected to look first, second, and third

## 6. Inferred Design System

Document the inferred design system from the image.

### 6.1 Color Tokens

Create a color token table.

For each color, include:
- token name
- approximate hex value
- usage
- confidence level: high / medium / low

Include any visible:
- primary brand color
- accent color
- background color
- section background color
- card background color
- border color
- heading color
- body text color
- muted text color
- link color
- success color
- warning color
- danger/error color
- CTA color
- icon color
- table/header color
- footer color

Example table:

| Token | Approx. Hex | Usage | Confidence |
| --- | --- | --- | --- |
| primary | #000000 | Main brand color | Medium |

If exact colors cannot be determined, infer them visually and mark confidence.

### 6.2 Typography

Document:
- likely font family or closest implementation font
- heading style
- body style
- button text style
- card title style
- label/kicker style
- navigation style
- table text style
- FAQ text style
- footer text style
- approximate sizes
- weights
- line heights
- letter spacing
- casing rules

If the exact font cannot be determined, describe the visual qualities and recommend the closest implementation font.

### 6.3 Spacing and Layout Rhythm

Document:
- page/container width
- section vertical spacing
- horizontal page padding
- grid gaps
- card padding
- button spacing
- header spacing
- hero spacing
- footer spacing
- row spacing
- dense vs spacious areas
- mobile spacing assumptions

Use approximate pixel values where possible.

### 6.4 Borders, Radius, and Elevation

Document:
- card radius
- button radius
- input radius if visible
- table radius if visible
- border thickness
- border color behavior
- shadows
- glows
- dividers
- surface layering
- hover/active implications if visible

### 6.5 Backgrounds and Surfaces

Document:
- page background
- section backgrounds
- card surfaces
- visual mockup surfaces
- gradient usage
- texture usage
- decorative background elements
- contrast between sections
- alternating section rhythm

### 6.6 Icon and Illustration Style

Document:
- icon stroke/fill style
- icon weight
- icon containers
- icon color usage
- illustration style
- visual metaphor
- diagram style
- mockup style
- decorative patterns
- background treatments
- image/component treatment

## 7. Component Inventory

List every reusable component visible in the image.

For each component, use this format:

### Component: [component name]

Purpose:
[what it does]

Anatomy:
- [part 1]
- [part 2]
- [part 3]

Visual style:
[colors, border, radius, typography, spacing]

Behavior or interaction implication:
[if visible or inferred]

Implementation rules:
- [rule]
- [rule]

Do not:
- [anti-pattern]
- [anti-pattern]

Include every meaningful component visible, not only major page sections.

## 8. Layout and Grid Rules

Document:
- container strategy
- desktop layout
- section grid systems
- card column counts
- hero column layout
- content/visual balance
- table layout
- footer layout
- how sections align with each other
- how repeated components are spaced
- inferred tablet layout
- inferred mobile layout

Include practical guidance like:
- stack sections on mobile
- keep CTA row near headline
- preserve card density
- keep comparison tables scrollable or simplified
- avoid horizontal overflow
- keep visual components readable
- keep footer columns stacked on mobile

## 9. Section-by-Section Implementation Map

Create an implementation map that tells another agent how to rebuild or extend the page.

Use this format:

| Order | Section / Region | Component Pattern | Visible Content | Implementation Notes |
| --- | --- | --- | --- | --- |

Every visible section or region should appear in this table.

## 10. Reusable Design Patterns

Document repeated patterns that should be reused when extending the design.

Examples:
- section intro pattern
- card grid pattern
- CTA pattern
- trust row pattern
- table pattern
- pricing card pattern
- checklist pattern
- FAQ pattern
- visual mockup pattern
- footer pattern
- icon tile pattern
- metadata label pattern

For each pattern, include:
- when to use it
- anatomy
- styling
- spacing
- what to avoid

## 11. Responsive Behavior Guidance

Even if the image shows only desktop, infer a responsible responsive approach.

Document:
- desktop behavior
- tablet behavior
- mobile behavior
- navigation behavior
- hero behavior
- card grid behavior
- table behavior
- CTA behavior
- footer behavior
- image/visual component behavior
- typography scaling
- spacing changes

Mark all responsive assumptions as inferred unless visible.

## 12. Implementation Constraints

Document what an implementation agent must preserve.

Include:
- section order
- copy accuracy
- color palette
- typography
- CTA hierarchy
- spacing rhythm
- card treatment
- grid rules
- visual component style
- icon style
- footer structure
- responsive behavior
- accessibility considerations
- semantic heading hierarchy

Also document:
- what can be adapted
- what must not be changed
- what should not be invented
- what requires confirmation

## 13. Anti-Patterns to Avoid

List what would make the recreation inaccurate.

Include:
- using a different color palette
- changing CTA styling
- changing heading hierarchy
- making the layout too generic
- replacing structured cards with random blocks
- adding unsupported sections
- changing copy meaning
- overusing shadows or gradients
- ignoring spacing rhythm
- using a different illustration style
- inventing missing text
- making mobile unreadable
- treating inferred content as confirmed
- ignoring small labels, badges, or trust markers

## 14. Rebuild Checklist

Create a final checklist for the implementation agent.

Include:
- image type identified correctly
- section order documented
- copy extracted accurately
- colors approximated with confidence
- typography documented
- spacing documented
- component inventory complete
- visual hierarchy documented
- hero or primary focal area documented
- cards documented
- CTAs documented
- tables/comparisons documented if visible
- forms documented if visible
- FAQ/footer documented if visible
- responsive behavior planned
- implementation constraints documented
- anti-patterns documented
- no unsupported content invented

## Accuracy requirements

Be thorough about visible detail and explicit about uncertainty.

Do not say “modern design” without specifying what makes it modern.
Do not say “clean cards” without documenting card radius, border, padding, background, and spacing.
Do not say “blue and pink” without extracting approximate hex values and usage.
Do not skip small elements such as breadcrumbs, badges, trust rows, footer links, metadata labels, card subtitles, or secondary CTAs.
Do not flatten the image into a generic template.
Do not force the extraction into predefined page sections.
Do not ignore visible elements because they are not listed in the prompt.
Do not invent missing sections, copy, or functionality.
Do not classify the reference as a landing page, dashboard, app, or website without sufficient visual evidence; label uncertain classifications.

If something is visible but uncertain, document it as inferred with confidence level.

If something is not visible, do not invent it.

Final output:
Return only the completed Markdown design extraction document.
````
<!-- prompt:end -->

## Usage notes

Use the standard extraction for a detailed visual inventory; choose the extended variant when a reusable implementation contract is also needed.

**Relevant capabilities:** `vision`, `file-access`. These are requirements or conditional needs, not tools installed by this file.

## Related entries

- [Extract Images Into a Reusable Design Contract](image-to-design-system-extraction-extended.md) — Produce a detailed visual extraction plus a reusable token-and-component implementation contract.
- [Consolidate Sources Into a Design-System Showcase](../showcases/create-design-system-showcase.md) — Consolidate extracted design evidence into one coherent, standalone HTML component showcase.
- [Create an Implementation Handoff](../handoff/implementation-handoff-docs-from-mockup-or-html.md) — Document an approved mockup or HTML interface as three build-ready Markdown specifications.

[Browse the catalog](../../../CATALOG.md) · [Usage guide](../../../docs/usage.md)
