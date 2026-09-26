---
id: "research-campaign-design-system"
title: "Research a Campaign Design System"
type: "prompt"
primary_category: "design"
categories: ["design"]
subcategory: "showcases"
when_to_use: "Define a campaign-specific visual and conversion system before building the campaign landing page"
search_terms: ["research-campaign-design-system", "design", "showcases"]
inputs: ["CAMPAIGN_BRIEF"]
output: "One complete standalone HTML showcase with research notes, design tokens, components, and QA guidance."
mode: "research-and-build"
capabilities: ["research", "browser", "code-execution"]
related: ["research-vps-palette-comparison", "create-design-system-showcase", "build-html-page-from-scope-and-design-system"]
aliases: ["design-system-showcase/research-campaign-pallete.md", "research-campaign-pallete.md", "research-campaign-pallete"]
---

# Research a Campaign Design System

Define a campaign-specific visual and conversion system before building the campaign landing page.

**Type:** prompt · **Mode:** research-and-build · **ID:** `research-campaign-design-system`

**Expected output:** One complete standalone HTML showcase with research notes, design tokens, components, and QA guidance.

**Not for:** The final campaign or product landing page; this defines its design system first.

## Inputs

Replace every listed placeholder. For an optional source, enter `None` when it is unavailable.

| Placeholder | What to provide | Example |
| --- | --- | --- |
| `{{CAMPAIGN_BRIEF}}` | Campaign, offer, audience, industry, conversion goal, approved facts, and brand constraints. | A self-managed VPS campaign for developers, with approved offer facts and no invented customer proof. |

## Prompt

Copy the block below, not the metadata or usage notes.

<!-- prompt:start -->
````text
You are a research-led campaign design system and page strategy generator.

I want to create a new marketing campaign page for:

{{CAMPAIGN_BRIEF}}

Before creating the actual page, your task is to research the best visual direction, color strategy, UI style, section patterns, and conversion-focused component system for this campaign.

Your final output must be a complete standalone HTML design system showcase that defines the visual system the campaign page should use.

Do not create the final campaign landing page yet.
Do not only give me research notes.
Do not only give me a palette.
Do not only give me generic SaaS components.
Create the design system showcase first so the campaign page can be built from it afterwards.

Research requirements:
Research the campaign context and determine the strongest visual approach based on:
- target audience
- product category
- buying intent
- competitor visual patterns
- conversion expectations
- trust requirements
- accessibility
- current design trends
- emotional tone
- content density
- CTA hierarchy
- pricing or offer presentation needs
- mobile-first usability

From the research, define:
- visual direction
- brand mood
- color palette
- typography system
- spacing system
- component style
- section patterns
- CTA hierarchy
- trust-building patterns
- form patterns
- comparison/pricing patterns
- responsive behavior
- anti-patterns to avoid

The output must be one complete standalone HTML file from <!doctype html> to </html>.

The HTML file must include:
- internal CSS
- CSS variables for all design tokens
- no external dependencies unless explicitly authorized in the brief
- no random external assets
- no broken images
- semantic HTML
- accessible labels and states
- responsive behavior
- realistic campaign-oriented sample content
- usage guidance inside the page
- implementation notes inside the page
- QA checks inside the page

Use this page structure:

1. Campaign Design System Header
2. Research Summary
3. Recommended Visual Direction
4. Token Reference
5. Color System
6. Typography System
7. Layout and Grid System
8. Core Components
9. Campaign Section Patterns
10. Conversion Patterns
11. Forms and Lead Capture
12. Trust and Proof Patterns
13. States and Interactions
14. Responsive Behavior
15. Usage Rules and Anti-Patterns
16. Component Index

The showcase must include these component groups:

Global tokens:
- colors
- typography
- spacing
- radius
- borders
- shadows
- transitions
- focus rings
- z-index/layering

Core components:
- primary CTA
- secondary CTA
- ghost button
- outline button
- destructive button if relevant
- disabled button
- icon button
- text link
- inline link
- badge
- pill
- chip
- card
- feature card
- pricing card
- testimonial card
- metric card
- comparison table
- form fields
- select
- textarea
- checkbox
- radio
- toggle
- search/filter input if relevant
- alert
- toast
- modal
- drawer if relevant
- empty state
- loading state

Campaign section patterns:
- hero section
- offer summary
- benefits grid
- feature section
- use-case section
- pricing/plan section
- comparison section
- proof/testimonial section
- FAQ section
- CTA banner
- lead form section
- footer pattern

For each component and section, include:
- name
- purpose
- visual example
- variants
- states
- when to use it
- how to use it
- what not to do
- implementation checks

The showcase must be specific enough that a developer can build the campaign page from it without guessing.

Important quality rules:
- Do not invent fake testimonials, fake customer logos, fake claims, or fake statistics.
- If proof is needed but not provided, use labelled placeholders such as “Customer proof placeholder” rather than fake proof.
- Use the researched design direction, but keep the system implementation-friendly.
- Avoid overly decorative visuals that cannot be translated into production HTML/CSS.
- Avoid excessive gradients, shadows, and animations unless the campaign direction specifically supports them.
- Keep CTA hierarchy clear.
- Keep mobile layout clean and conversion-focused.

Mobile requirements:
The design system showcase must work at:
- 1440px
- 1280px
- 1024px
- 768px
- 480px
- 390px
- 360px
- 320px

On mobile:
- no horizontal page overflow
- badges and chips must remain content-sized
- CTA groups must stack cleanly
- forms must be full-width but not cramped
- pricing cards must stack cleanly
- comparison tables must scroll inside wrappers
- hero content must not create awkward gaps
- section padding must be reduced but still balanced
- typography must remain readable
- no component may look stretched, misaligned, or asymmetrical

Final review before returning:
Before returning the file, inspect the source and rendered page with available tools; distinguish completed checks from checks not run:
- the page is complete
- tokens are used consistently
- all major components are shown
- campaign section patterns are shown
- mobile behavior is handled
- badges are not full width
- tables do not break the viewport
- CTA hierarchy is clear
- no fake claims were added
- no broken asset links exist
- the page is ready to save and use

### Research and QA evidence

Use primary sources for factual or version-sensitive claims. Put concise source links, access dates, the research rationale, and uncertainty in the Research Summary inside the HTML. Treat aesthetic recommendations as reasoned design judgments, not proven conversion improvements. Do not copy protected brand assets without supplied rights or permission.

If live research is unavailable, label the direction provisional and identify which decisions rely only on the brief; do not claim current competitor or trend research. Mark all sample metrics, prices, testimonials, and proof as demonstrations. Do not invent customer evidence. Measure contrast for the actual foreground/background pairs and record the checks performed instead of declaring accessibility from appearance alone.

Render and inspect the specified widths when browser tools are available. Record passed, failed, and not-run checks inside the showcase QA section; do not claim tool execution that did not happen. These notes belong inside the HTML, preserving the HTML-only output contract.

Final output:
Return only the complete standalone HTML file.
Do not return a Markdown summary.
Do not return only CSS.
Do not return a fragment.
Do not say “rest unchanged.”
Return the full file from <!doctype html> to </html>.
````
<!-- prompt:end -->

## Usage notes

Supply the actual referenced material. A filename or URL does not grant the assistant file, browser, account, or edit access.

**Relevant capabilities:** `research`, `browser`, `code-execution`. These are requirements or conditional needs, not tools installed by this file.

## Related entries

- [Compare Six VPS Brand Palettes](research-vps-palette-comparison.md) — Compare six palettes in a neutral editorial HTML document while preserving a fixed dark-indigo brand anchor.
- [Consolidate Sources Into a Design-System Showcase](create-design-system-showcase.md) — Consolidate extracted design evidence into one coherent, standalone HTML component showcase.
- [Build an HTML Page From Scope and Design Rules](../page-builds/build-html-page-from-scope-and-design-system.md) — Build one standalone HTML page using separate content requirements and visual design rules.

[Browse the catalog](../../../CATALOG.md) · [Usage guide](../../../docs/usage.md)
