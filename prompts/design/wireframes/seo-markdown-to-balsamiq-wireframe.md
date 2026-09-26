---
id: "seo-markdown-to-balsamiq-wireframe"
title: "SEO Markdown to Balsamiq Wireframe"
type: "prompt"
primary_category: "design"
categories: ["design"]
subcategory: "wireframes"
when_to_use: "You have SEO research or page content in Markdown and want a Balsamiq-style wireframe before design or implementation"
search_terms: ["seo-markdown-to-balsamiq-wireframe", "design", "wireframes", "balsamiq", "wireframe", "seo markdown", "content markdown", "page structure", "content hierarchy", "mockup"]
inputs: ["CONTENT_MARKDOWN"]
output: "A full-page low-fidelity wireframe plan mapped to the source Markdown; no implementation."
mode: "plan"
capabilities: ["file-access"]
related: ["implement-page-from-markdown-wireframe-and-reference-html", "content-audit"]
aliases: ["design/wireframes/seo-markdown-to-balsamiq-wireframe.md", "seo-markdown-to-balsamiq-wireframe.md"]
---

# SEO Markdown to Balsamiq Wireframe

You have SEO research or page content in Markdown and want a Balsamiq-style wireframe before design or implementation.

**Type:** prompt · **Mode:** plan · **ID:** `seo-markdown-to-balsamiq-wireframe`

**Expected output:** A full-page low-fidelity wireframe plan mapped to the source Markdown; no implementation.

## Inputs

Replace every listed placeholder. For an optional source, enter `None` when it is unavailable.

| Placeholder | What to provide | Example |
| --- | --- | --- |
| `{{CONTENT_MARKDOWN}}` | Complete approved SEO/content Markdown. | linux-vps-content.md |

## Prompt

Copy the block below, not the metadata or usage notes.

<!-- prompt:start -->
````text
Create a Balsamiq-style low-fidelity wireframe based on the attached SEO/content Markdown file.

## Content source

{{CONTENT_MARKDOWN}}

## Task

Use the Markdown file as the source of truth for the page content, page structure, section order, headings, messaging, offers, proof points, FAQs, CTAs, and SEO intent.

Do not write production code. Do not create a polished visual design. First translate the Markdown content into a rough black-and-white Balsamiq-style wireframe that shows what the page should look like structurally.

The goal is to turn the content into a clear page mock-up with the right sections, hierarchy, flow, and UI patterns so the page can be reviewed before design or implementation.

Before creating the wireframe, inspect the Markdown file and identify:

- the page’s main goal
- the target audience
- the primary CTA
- the key value proposition
- the section structure implied by the content
- supporting sections such as features, use cases, benefits, comparisons, FAQs, proof, pricing cues, or CTAs
- any repeated themes or keywords that affect hierarchy
- any content that should be visually emphasized
- any missing states or supporting UI patterns needed to present the content clearly

Then create a Balsamiq-style wireframe for the full page.

The wireframe should include the appropriate sections based on the Markdown content, such as:

- hero section
- supporting intro/value section
- feature or benefits sections
- use case or workflow sections
- comparison section if relevant
- proof/trust section if relevant
- FAQ section if relevant
- CTA sections
- footer or final conversion section

For each section, show:

- section title
- layout structure
- content blocks
- headings/subheadings
- CTA placement
- cards, lists, tables, badges, tabs, icons, or panels if relevant
- annotations explaining what the section is communicating
- notes on what content from the Markdown belongs in that section

Use a hand-drawn Balsamiq-style layout with rough boxes, simple labels, arrows, placeholder icons, handwritten-style notes, and callouts. Focus on content hierarchy, structure, flow, affordances, and clarity. Do not focus on polished UI styling, colors, gradients, or final typography.

Return the result as a wireframe plan that includes:

- the page section order
- the wireframe for each section
- notes on why each section exists
- how the page flows from top to bottom
- how the content is grouped and prioritized
- where the primary and secondary CTAs should appear

Do not implement the page. Do not write HTML, CSS, JavaScript, or polished UI. Only produce the Balsamiq-style wireframe plan based on the Markdown content.

### Scope and evidence

Use supplied requirements, not invented features. Label missing data or behavior as an assumption or dependency. Include only states relevant to the feature, and explain any omitted state that the brief requires. “Balsamiq-style” describes low fidelity; do not claim to have created a native Balsamiq project unless that file was actually generated. Keep the output reviewable as annotated Markdown or clearly labeled wireframes; do not imply that a plan is an implemented interface.

Preserve the source section order and required content. Represent unsupported proof or pricing as missing input rather than inventing it. Do not add a pricing, testimonial, or feature section merely because it appears in the examples.
````
<!-- prompt:end -->

## Usage notes

Supply the actual referenced material. A filename or URL does not grant the assistant file, browser, account, or edit access.

**Relevant capabilities:** `file-access`. These are requirements or conditional needs, not tools installed by this file.

## Related entries

- [Implement Page from Markdown, Wireframe, and Reference HTML](../page-builds/implement-page-from-markdown-wireframe-and-reference-html.md) — You have a content Markdown file, an approved Balsamiq wireframe, and a reference HTML page, and you want the agent to implement the final page in the same website style.
- [Audit Website Copy](../../content/editing/content-audit.md) — Find contextual, factual, repetitive, and misplaced website copy without rewriting the source.

[Browse the catalog](../../../CATALOG.md) · [Usage guide](../../../docs/usage.md)
