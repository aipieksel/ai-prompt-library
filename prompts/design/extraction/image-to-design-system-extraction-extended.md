---
id: "image-to-design-system-extraction-extended"
title: "Extract Images Into a Reusable Design Contract"
type: "prompt"
primary_category: "design"
categories: ["design"]
subcategory: "extraction"
when_to_use: "Produce a detailed visual extraction plus a reusable token-and-component implementation contract"
search_terms: ["image-to-design-system-extraction-extended", "design", "extraction"]
inputs: ["IMAGE_REFERENCES", "SUPPORTING_CONTEXT"]
output: "One complete Markdown extraction including a reusable design-system contract and fenced token schema."
mode: "extract"
capabilities: ["vision", "file-access"]
related: ["image-to-design-system-extraction", "create-design-system-showcase", "implementation-handoff-docs-from-mockup-or-html"]
aliases: ["design/image-to-design-system-extraction-extended.md", "image-to-design-system-extraction-extended.md"]
---

# Extract Images Into a Reusable Design Contract

Produce a detailed visual extraction plus a reusable token-and-component implementation contract.

**Type:** prompt · **Mode:** extract · **ID:** `image-to-design-system-extraction-extended`

**Expected output:** One complete Markdown extraction including a reusable design-system contract and fenced token schema.

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

The token schema below is an output template, not observed evidence or repository metadata. Example names and values such as #000000 must be replaced with evidence-backed values, labeled estimates, or null/unknown as appropriate. Keep the detailed component contract authoritative and cross-reference it from the inventory instead of writing contradictory duplicate specifications.

You will receive one or more reference images, screenshots, mockups, page previews, app screens, interface captures, component screenshots, full-page screenshots, or visual design references.

Task:
Analyze the provided image reference systematically and precisely, distinguishing observation from inference, then produce a complete implementation-grade Markdown extraction that documents:

1. the visible page/screen/interface structure
2. all readable copy
3. the full visual design system
4. reusable components
5. layout rules
6. implementation constraints
7. rebuild guidance

The output must be strong enough that another agent can recreate, extend, or implement the design with explicit evidence, confidence, and unresolved details rather than hidden guesses.

Do not loosely describe the image.
Do not summarize only the obvious parts.
Do not force the image into a generic landing page, dashboard, app screen, SaaS page, ecommerce page, or website template structure.
Do not stop at a normal “design extraction” summary.
You must also produce a proper design-system section in the style of a real design.md implementation contract.

Use the image as the visual source of truth.

If additional context is provided, such as brand name, product type, target page, existing CSS, HTML, scope file, design-system file, or implementation constraints, use that context only to clarify the extraction. Do not override what is visible in the image unless the supporting file explicitly corrects it.

If multiple images are provided, analyze each image individually first, then extract the shared design system and reusable patterns across the set.

## Core objective

Create one precise Markdown document that captures:

- what the image looks like
- what copy is visible
- how the page or screen is structured
- how the design system works
- what components are reusable
- what layout rules are visible or inferable
- what another agent must preserve
- what another agent must avoid
- how to rebuild or extend the design accurately
- how to express the extracted visual system as a reusable design.md-style implementation contract

The result should be practical enough for an implementation agent to recreate the design in HTML/CSS, apply the same design language to another page or interface, or create a new page from a separate scope using this extracted design system.

## Critical requirement: include a real design-system contract

The final Markdown must include a full design-system contract similar in depth and structure to a professional design.md file.

It must not only say things like “blue and pink” or “rounded cards.”
It must define reusable tokens, components, patterns, spacing rules, typography rules, layout rules, do/don’t rules, and an agent reconstruction checklist.

The design-system section must include:

- YAML-style front matter or a structured token block at the top
- design system name
- version
- description
- source image references
- color tokens
- typography tokens
- spacing tokens
- radius tokens
- layout tokens
- motion/elevation notes
- component inventory
- design principles
- layout patterns
- component usage rules
- do’s and don’ts
- agent reconstruction checklist

If exact values are not available, infer approximate values and mark confidence.

Do not omit this design-system contract.

## Analysis workflow

Before writing the final document, inspect the image carefully and treat it as the visual source of truth.

Do not assume the image follows a standard website, dashboard, app, landing page, SaaS, ecommerce, or marketing structure. First identify what kind of interface, page, screen, component, or visual system the image appears to show, then document it according to what is actually visible.

Analyze the image from the largest structure down to the smallest visible details.

### 1. Overall composition

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
- how the page or screen creates trust
- where the design feels custom rather than generic

### 2. Visible regions and sections

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

### 3. Content and copy

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

### 4. Visual system

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

### 5. Component system

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

### 6. Interaction and behavior implications

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

### 7. Responsive and implementation implications

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

### 8. Accuracy pass

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

## Final output structure

Return one complete Markdown document with the following structure.

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

## 6. Design System Contract

This section is mandatory.

Create a design-system contract similar to a professional design.md file.

It must be detailed, structured, reusable, and implementation-ready.

### 6.1 Design System Front Matter

Start the design system contract with YAML-style front matter.

Use this structure:

```yaml
version: "1.0"
name: "[Inferred Design System Name]"
description: "[Precise description of the visual system extracted from the image]"
source:
  type: "image-reference"
  confidence: "inferred from screenshot"
  notes:
    - "[important note]"
framework: "image-extracted/design.md"
scope: "visual reconstruction and implementation guidance from image reference"
colors:
  primary: "[hex]"
  primary_foreground: "[hex]"
  accent: "[hex]"
  background: "[hex]"
  surface: "[hex]"
  surface_soft: "[hex]"
  border: "[hex or rgba]"
  border_strong: "[hex or rgba]"
  heading: "[hex]"
  copy: "[hex]"
  muted: "[hex]"
  success: "[hex]"
  warning: "[hex]"
  danger: "[hex]"
typography:
  font_family_primary: "[font or closest implementation font]"
  font_family_heading: "[font or closest implementation font]"
  font_family_mono: "[font or closest implementation font]"
  h1: "[approx size / line-height / weight]"
  h2: "[approx size / line-height / weight]"
  h3: "[approx size / line-height / weight]"
  body: "[approx size / line-height / weight]"
  small: "[approx size / line-height / weight]"
  button: "[approx size / line-height / weight / casing]"
spacing:
  container: "[approx max-width and padding]"
  section_y: "[approx vertical spacing]"
  card_gap: "[approx]"
  card_padding: "[approx]"
  button_padding: "[approx]"
shape:
  card_radius: "[approx]"
  button_radius: "[approx]"
  panel_radius: "[approx]"
  table_radius: "[approx]"
layout:
  container_width: "[approx]"
  grid_system: "[summary]"
  breakpoints:
    desktop: "[inferred]"
    tablet: "[inferred]"
    mobile: "[inferred]"
components:
  - name: "[component name]"
    use_for: "[component purpose]"
```

If exact values cannot be determined, use approximate values and mark them as inferred in the notes.

### 6.2 Overview

Write a design-system overview.

Include:
- the design identity
- the product/page feel
- the dominant visual language
- the surface strategy
- the typography strategy
- the spacing strategy
- the CTA strategy
- the component strategy
- how this design differs from a generic template

### 6.3 Colors

Document the color system in detail.

Include:
- core brand colors
- accent colors
- text colors
- backgrounds
- card surfaces
- border colors
- success/warning/danger colors
- table colors
- CTA colors
- terminal/dashboard/mockup colors if visible
- footer colors

For each color, include:
- token name
- approximate hex value
- usage
- confidence

Use a table:

| Token | Approx. Hex | Usage | Confidence |
| --- | --- | --- | --- |

Then explain the color rules in prose:
- when to use primary
- when to use accent
- when to use success
- when to use muted text
- how section backgrounds alternate
- what not to do with the palette

### 6.4 Typography

Document the typography system in detail.

Include:
- likely font family or closest implementation font
- heading hierarchy
- body copy style
- card title style
- navigation style
- button style
- badge/label style
- table style
- FAQ style
- footer style
- code/terminal style if visible

Use a table:

| Role | Approx. Size / Line Height | Weight | Color | Usage |
| --- | --- | --- | --- | --- |

Then explain typography rules in prose:
- how headings should be used
- how section titles differ from card titles
- how labels and badges behave
- how buttons should be cased
- how terminal/code typography should be handled
- what typography mistakes to avoid

### 6.5 Layout

Document the layout system.

Include:
- container width
- page padding
- section vertical rhythm
- hero layout
- grid columns
- card grid behavior
- table layout
- footer layout
- visual/content balance
- dense vs spacious areas
- responsive stacking rules

Use practical implementation guidance:
- desktop layout rules
- tablet layout rules
- mobile layout rules
- when to use one column, two columns, three columns, four columns, or five columns
- how to avoid horizontal overflow

### 6.6 Elevation and Depth

Document:
- shadows
- borders
- glows
- surface layering
- dark panels
- floating mockups
- table surfaces
- CTA banner surfaces

Explain how depth is created.

Do not merely say “soft shadow.” Describe strength, use case, and restraint.

### 6.7 Shapes and Radius

Document:
- card radius
- button radius
- input radius if visible
- badge radius
- table radius
- hero visual radius
- terminal/mockup radius
- banner radius

Explain where each radius style should be reused.

### 6.8 Components

Document all extracted components in a reusable design-system style.

For each component:

### Component: [component name]

Use for:
[where this component should be used]

Anatomy:
- [part 1]
- [part 2]
- [part 3]

Visual rules:
- [color/surface]
- [typography]
- [spacing]
- [border/radius]
- [icon/visual treatment]

Behavior:
[visible or inferred behavior]

Responsive behavior:
[how it should adapt]

Do:
- [rule]
- [rule]

Don’t:
- [anti-pattern]
- [anti-pattern]

Include every meaningful component visible in the image.

### 6.9 Design Patterns

Document repeated patterns.

Examples:
- section intro pattern
- hero pattern
- card grid pattern
- pricing pattern
- checklist pattern
- trust/proof row pattern
- comparison table pattern
- FAQ pattern
- footer pattern
- CTA banner pattern
- visual mockup pattern
- icon tile pattern
- metadata label pattern

For each pattern, include:
- when to use it
- anatomy
- styling
- spacing
- what to avoid

### 6.10 Do’s and Don’ts

Create a design-system-specific list.

Do:
- preserve the extracted color hierarchy
- preserve the section rhythm
- preserve the CTA hierarchy
- preserve card styling
- preserve typography scale
- preserve icon style
- preserve visible page structure
- use inferred values consistently

Don’t:
- invent new colors
- replace the visual system
- add unrelated sections
- overuse shadows
- change CTA hierarchy
- change copy meaning
- use generic cards where specialized components are visible
- ignore small labels, badges, and table styling
- invent unreadable copy

### 6.11 Agent Reconstruction Checklist

Create a checklist another agent must follow before implementing from this extracted design system.

Include:
- identify page type
- select correct hero pattern
- reuse color tokens
- reuse typography tokens
- reuse card and CTA patterns
- preserve section order
- preserve extracted copy where required
- map new content into equivalent components
- verify responsive behavior
- check visual match against image
- avoid unsupported claims or invented copy

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
- failing to produce a reusable design-system contract

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
- design-system contract included
- token front matter included
- components documented as reusable design-system components
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
Do not omit the design-system contract.
Do not give only a normal screenshot summary.

If something is visible but uncertain, document it as inferred with confidence level.

If something is not visible, do not invent it.

Final output:
Return only the completed Markdown design extraction document.

The final Markdown must include both:
1. a complete visual/copy/page extraction
2. a reusable design-system contract similar to a professional design.md file
````
<!-- prompt:end -->

## Usage notes

Use the standard extraction for a detailed visual inventory; choose the extended variant when a reusable implementation contract is also needed.

**Relevant capabilities:** `vision`, `file-access`. These are requirements or conditional needs, not tools installed by this file.

## Related entries

- [Extract a Design System From Images](image-to-design-system-extraction.md) — Document visible copy, page anatomy, reusable components, and inferred design rules from image references.
- [Consolidate Sources Into a Design-System Showcase](../showcases/create-design-system-showcase.md) — Consolidate extracted design evidence into one coherent, standalone HTML component showcase.
- [Create an Implementation Handoff](../handoff/implementation-handoff-docs-from-mockup-or-html.md) — Document an approved mockup or HTML interface as three build-ready Markdown specifications.

[Browse the catalog](../../../CATALOG.md) · [Usage guide](../../../docs/usage.md)
