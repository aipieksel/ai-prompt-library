---
id: "extend-vps-design-system-showcase"
title: "Extend a Showcase With VPS Website Components"
type: "prompt"
primary_category: "design"
categories: ["design"]
subcategory: "showcases"
when_to_use: "Extend an existing dashboard showcase with a complete VPS website component layer and updated documentation"
search_terms: ["extend-vps-design-system-showcase", "design", "showcases", "VPS", "Example Hosting", "52 sections", "charts", "usage", "0%", "100%", "320px"]
inputs: ["EXISTING_SHOWCASE", "PACKAGE_DOCUMENTS", "PREVIOUS_ATTEMPTS"]
output: "A ZIP containing the full updated HTML and seven required Markdown documents."
mode: "edit"
capabilities: ["file-access", "code-execution", "browser", "archive-creation"]
related: ["create-design-system-showcase", "design-system-compliance-audit-and-fix", "research-vps-palette-comparison"]
aliases: ["design-system-showcase/extend-existing-showcase.md", "extend-existing-showcase.md", "extend-existing-showcase"]
---

# Extend a Showcase With VPS Website Components

Extend an existing dashboard showcase with a complete VPS website component layer and updated documentation.

**Type:** prompt · **Mode:** edit · **ID:** `extend-vps-design-system-showcase`

**Expected output:** A ZIP containing the full updated HTML and seven required Markdown documents.

## Inputs

Replace every listed placeholder. For an optional source, enter `None` when it is unavailable.

| Placeholder | What to provide | Example |
| --- | --- | --- |
| `{{EXISTING_SHOWCASE}}` | The full working standalone dashboard/product-console HTML. | showcase.html |
| `{{PACKAGE_DOCUMENTS}}` | DESIGN.md, INDEX.md, README.md, and COMPONENT_IMPLEMENTATION_AND_QA_SPEC.md, plus existing VPS docs if present. | The four canonical Markdown files from the current design-system package. |
| `{{PREVIOUS_ATTEMPTS}}` | Optional earlier HTML attempts and observed problems; use None if absent. | None |

## Prompt

Copy the block below, not the metadata or usage notes.

<!-- prompt:start -->
````text
Existing standalone HTML showcase:
{{EXISTING_SHOWCASE}}

Supporting package files:
{{PACKAGE_DOCUMENTS}}

Optional earlier attempts and specific issues to avoid (None when absent):
{{PREVIOUS_ATTEMPTS}}

Extend the existing dashboard/product-console design-system showcase with a complete VPS website component layer. Preserve the original console system, its sections, visual identity, behavior, and documentation. Add the marketing layer inside the same showcase rather than replacing the original or attaching an unrelated landing page.

### Source authority

Read every supplied file. The existing HTML is the implementation base. DESIGN.md defines the canonical design system; INDEX.md maps component families; README.md explains the package; COMPONENT_IMPLEMENTATION_AND_QA_SPEC.md is the implementation and QA contract. Use earlier attempts only as supporting evidence, not as an alternative authority. Identify a material conflict before editing rather than silently discarding requirements.

Do not assume earlier attempts exist. Avoid a flat, colorless VPS component inventory: compact console elements stay restrained, while VPS hero/banner examples, pricing, product cards, CTA strips, promotional banners, and proof structures demonstrate the permitted marketing emphasis. Charts must show varied values, not only zero.

### Deliverables

Return one ZIP containing all eight files:
1. The complete updated standalone HTML file.
2. Updated DESIGN.md.
3. Updated INDEX.md.
4. Updated README.md.
5. Updated COMPONENT_IMPLEMENTATION_AND_QA_SPEC.md.
6. VPS_COMPONENT_IMPLEMENTATION_AND_QA_SPEC.md.
7. VPS_COMPONENT_INDEX.md.
8. CHANGELOG.md.

Both VPS-specific documents are required. Update an existing version rather than creating a second conflicting copy. The detailed document requirements below control their contents.

The HTML must use internal CSS, no external dependencies, no hotlinked assets, no external fonts or icon libraries, and no framework dependency. Preserve accessibility and responsive behavior. Do not include broken images, invented logos, fake testimonials or awards, or private data. Clearly label all sample prices, usage, product capabilities, regions, and proof structures; the examples below are demonstration requirements, not verified business claims.

If an essential source is missing, identify it before pretending the extension is complete. If file creation is unavailable, return the complete file contents under their intended names and state that a ZIP was not created. Never invent a download link.

# DESIGN SYSTEM FOUNDATION

Keep the existing dashboard/product-console design language:
- light neutral background
- white cards and panels
- subtle gray borders
- compact controls
- restrained typography
- low/no shadow
- small-radius UI elements
- black or existing primary actions where the base system requires them
- muted secondary actions
- controlled semantic colour use
- dense but readable tables
- clear active states
- minimal ornamentation
- implementation-ready layout

However, the VPS website extension is allowed to be more visually expressive than the dashboard side.

The VPS website layer should feel like:
“A VPS website component system built from the existing console design language, with stronger marketing and conversion components.”

It should not feel like:
“A random SaaS landing page pasted under the dashboard design system.”

# CRITICAL VISUAL DIRECTION FOR VPS WEBSITE LAYER

The VPS website sections need more colour, hierarchy, and impact.

The dashboard side must remain compact, neutral, and console-like.

The VPS website side may use controlled website accents:
- dark indigo brand anchor
- blue technical trust accents
- green success/trust accents
- pink or warm CTA/promo accent where appropriate
- pale tinted section surfaces
- dark technical/code sections
- stronger pricing-card highlights
- more visually distinct CTA strips
- more obvious hero/banner/page-header examples
- more meaningful usage/progress/chart states

The VPS website layer must still be disciplined:
- no childish gradients
- no decorative cloud/server theatre
- no fake app screenshots
- no giant SaaS hero dominating the showcase
- no random colourful cards
- no rainbow token system
- no fake testimonials or fake awards
- no uncontrolled shadows
- no unrelated dark app shell
- no full marketing page mockup

But it must not be dead or bland.

The inner VPS examples should visually prove:
- CTA colour strength
- pricing-card hierarchy
- product-card differentiation
- promo-banner visibility
- trust/proof hierarchy
- hero/page-header colour treatment
- technical/code readability
- table readability
- chart colour behaviour at different percentages
- dense VPS sales-page usability

# VISUAL INTENSITY RULE

Use a three-tier visual system:

Tier 1 — Existing dashboard/admin components:
- neutral
- compact
- low colour
- border-led
- restrained

Tier 2 — VPS website standard components:
- still compact and system-aligned
- slightly more visual
- small accent rails
- subtle tints
- stronger hierarchy
- clearer CTA emphasis

Tier 3 — VPS marketing/conversion components:
- more visually distinct
- controlled use of colour
- contained hero/banner/CTA examples
- stronger pricing-card emphasis
- richer but still clean layout
- never theatrical or full landing-page style

The previous output mostly stayed in Tier 1.
The revised VPS layer must include Tier 2 and Tier 3 components.

# REQUIRED BRAND / VPS TOKEN EXTENSION

Add or improve a restrained additive VPS token layer.

Do not replace existing tokens.

Add these tokens if they do not exist:

--vps-brand-indigo: #020281
--vps-brand-indigo-soft
--vps-accent-blue
--vps-accent-blue-soft
--vps-cta-pink
--vps-cta-pink-hover
--vps-trust-green
--vps-trust-green-soft
--vps-promo-warm
--vps-promo-warm-soft
--vps-code-bg
--vps-code-text
--vps-pricing-highlight
--vps-pricing-highlight-soft
--vps-table-header
--vps-region
--vps-storage
--vps-windows
--vps-linux
--vps-dark-section
--vps-dark-section-border

If the base system is Google Cloud-style, use the same density and Google-like component language, but introduce the VPS tokens as contained accents.

If the base system is OpenAI-style, use the same neutral border-led system, but introduce the VPS tokens as contained accents.

The required fixed brand colour is:
Dark Indigo: #020281

Dark Indigo must appear meaningfully in the VPS website extension.

Use it for:
- VPS website hero/page-header examples
- premium trust banners
- dark technical sections
- CTA strip variants
- pricing highlight accents
- section treatment examples
- token documentation

Do not flood the entire showcase page with dark indigo.

# REQUIRED CHART / USAGE VISUAL CORRECTION

The previous Google Cloud-style result had many 0% charts/circles/bars.

Fix this.

All chart, graph, donut, meter, progress, bar, and resource usage examples must include varied values.

Required values to demonstrate:
- 0%
- 12%
- 20%
- 38%
- 40%
- 64%
- 72%
- 88%
- 90%
- 100%

Use different states:
- normal low usage
- normal mid usage
- high usage
- warning threshold
- error/critical threshold
- full/complete state
- empty/no-data state

Create chart and usage examples for:
- CPU usage
- RAM usage
- disk usage
- bandwidth usage
- storage allocation
- backup completion
- snapshot usage
- uptime indicator
- monthly traffic
- quota usage
- plan resource allocation
- pricing comparison usage bars

Each chart must include:
- visible label
- numeric value
- colour state
- text explanation
- accessible text
- no colour-only meaning

Do not leave all charts at 0%.
Do not use 100% for every success state.
Do not make charts decorative.
Use charts to test real colour and state behaviour.

# REQUIRED MARKETING COMPONENT CORRECTION

The previous VPS layer lacked marketing components that visually stand out.

Add compact, contained marketing components that are stronger than plain admin cards.

Include these new or improved components:

1. VPS hero banner colour treatment
2. VPS product hero block
3. VPS pricing hero block
4. VPS storage VPS hero block
5. VPS Linux VPS hero block
6. VPS Windows VPS hero block
7. VPS comparison page hero block
8. VPS campaign/promo hero block
9. VPS CTA strip variants
10. VPS promo/offer banner variants
11. VPS migration banner
12. VPS custom quote banner
13. VPS trust/proof banner
14. VPS deployment process banner
15. VPS specs highlight band
16. VPS dark technical section
17. VPS page-header variants
18. VPS product-family showcase row
19. VPS “plan recommended” visual treatment
20. VPS “high storage” visual treatment
21. VPS “developer-ready” visual treatment
22. VPS “business hosting” visual treatment

These must be compact and contained.
They must not become full landing pages.
They must be visually strong enough to judge colour and hierarchy.

# HERO / BANNER REQUIREMENTS

Add a section called:

VPS Marketing Components

This section must show compact, labelled hero and banner examples.

Required examples:

1. Product hero block
- eyebrow
- heading
- short copy
- primary action
- secondary action
- compact specs summary
- contained visual treatment
- dark indigo or controlled gradient background

2. Pricing hero block
- pricing-focused heading
- short value proposition
- “from placeholder price” line
- billing-cycle note
- action area
- small trust note

3. Storage VPS hero block
- storage capacity emphasis
- NVMe/storage accent
- backup/snapshot note
- compact action area

4. Linux VPS hero block
- root access
- distro support
- SSH/code-friendly block
- green/Linux accent

5. Windows VPS hero block
- RDP/Windows Server note
- blue Windows accent
- plan compatibility note

6. Comparison hero block
- “Compare VPS plans”
- short intro
- feature/spec scan row
- restrained CTA area

7. Promo campaign banner
- offer label
- concise discount/promo copy
- action
- legal/terms placeholder

8. Trust/proof banner
- dark indigo or trust-green treatment
- uptime/support/security/backups proof labels
- no fake metrics unless labelled placeholder

Each example must include a note:
- use when
- do not use when
- QA check

# SECTION — VPS WEBSITE OVERVIEW

Create a section explaining how the existing dashboard design system is extended for VPS website pages.

Include:
- purpose of the VPS website extension
- how it relates to the existing dashboard system
- what stays neutral
- what becomes more marketing-oriented
- what gets stronger colour
- what must never become decorative or unrelated
- list of major VPS component families
- difference between dashboard components and VPS website components

Make clear:
The website layer is more sales/content-oriented than the dashboard layer, but it must still feel compact, precise, technical, and trustworthy.

# SECTION — VPS WEBSITE TOKEN EXTENSION

Create or update the VPS token extension.

Show a token table with:
- token name
- value
- usage
- do
- do not
- example component
- confidence/reason

Include swatches for every token.

Show practical mini examples for:
- dark indigo hero
- pink CTA
- green trust state
- blue technical accent
- warm promo accent
- dark code section
- pricing highlight

# SECTION — PRICING CARD SYSTEM

Create a more visually useful pricing-card system.

Include:
- single plan card
- recommended plan card
- discounted/promo plan card
- enterprise/custom quote card
- storage-heavy plan card
- Windows VPS plan card
- Linux VPS plan card
- compact mobile-stacked version preview

Each card must include:
- plan name
- short use case
- price placeholder
- billing cycle
- CPU
- RAM
- storage
- bandwidth
- IPv4 / IPv6
- included snapshot / backup indicators
- recommended badge where relevant
- primary plan action
- secondary plan link
- small billing/legal note

Make the recommended card visually stronger than the other cards, but not loud.

Use:
- clear border emphasis
- small accent rail or top rule
- compact recommended badge
- strong price hierarchy
- clearly visible primary action

Do not:
- make every card colourful
- turn cards into random marketing tiles
- use fake discounts unless labelled placeholder
- use giant shadows
- hide legal/renewal notes

QA rules:
- price readable
- recommended plan obvious
- badges compact
- mobile stacking preserves hierarchy
- no horizontal overflow
- CTA visible

# SECTION — PLAN COMPARISON TABLES

Create stronger compact comparison tables.

Include:
- feature comparison table
- specs comparison table
- pricing comparison table
- included/not included states
- highlighted row
- recommended column
- action cell
- status cell
- usage/progress cell
- horizontal scroll wrapper on mobile

Rows should include:
- vCPU
- RAM
- NVMe storage
- bandwidth
- IPv4
- IPv6
- root access
- snapshots
- backups
- DDoS protection
- Linux images
- Windows Server
- support level
- deployment time
- upgrade path
- control panel
- managed support

Add at least one row with usage/progress indicators at:
- 20%
- 40%
- 72%
- 100%

QA rules:
- table headers readable
- row height compact
- no colouring every cell
- highlighted row subtle
- table scrolls inside wrapper on mobile
- status meaning includes text
- usage bars show varied values

# SECTION — PRODUCT FAMILY CARDS

Create product cards for:
- Cloud VPS
- Storage VPS
- Linux VPS
- Windows VPS
- Managed VPS
- Developer VPS
- Business VPS
- AI / Automation VPS

Each card should include:
- product name
- short use case
- starting price placeholder
- 3 key features
- compact action/link area
- small accent treatment
- product-specific token accent

Make product differences visible through:
- accent rail
- icon placeholder
- top mini label
- controlled highlight tint
- not full-card random colours

QA rules:
- same anatomy
- product distinction clear
- no random styles
- cards align
- mobile stacks

# SECTION — USE-CASE CARDS

Create use-case cards for:
- WordPress hosting
- business applications
- development environments
- backups and archives
- media storage
- game servers
- automation workloads
- remote desktop
- ecommerce hosting
- databases
- staging environments

Each card should include:
- use case title
- who it is for
- recommended VPS product
- short note
- optional related link

Add subtle visual grouping:
- business use cases
- developer use cases
- storage use cases
- Windows/remote desktop use cases

QA rules:
- SEO/content-friendly
- compact
- no forced CTA on every card
- not decorative

# SECTION — SPECS / RESOURCE CARDS

Create resource cards for:
- CPU
- RAM
- NVMe storage
- bandwidth
- region
- operating system
- snapshots
- backups
- root access
- IPv4 / IPv6

Each card should include:
- resource label
- value placeholder
- helper explanation
- status/availability indicator where useful
- optional usage meter with a varied percentage

Use varied states:
- CPU 38%
- RAM 64%
- Disk 72%
- Bandwidth 20%
- Backup 100%
- Snapshot 40%

QA rules:
- values visually dominant
- short descriptions
- meters not colour-only
- mobile readable

# SECTION — SERVER LOCATION / REGION CARDS

Create location/region components.

Include:
- single region card
- region availability grid
- recommended region state
- unavailable/coming soon region state
- latency-style region card
- data centre information card
- country/region selector preview

Example regions:
- Johannesburg
- Frankfurt
- Dallas
- London
- Singapore
- New York

Each region card should include:
- location
- status
- recommended for
- latency placeholder or availability label
- product availability note

QA rules:
- status not colour-only
- no fake map
- text-based geography
- selected/recommended state obvious

# SECTION — OPERATING SYSTEM SELECTOR CARDS

Create OS selector cards for:
- Ubuntu
- Debian
- AlmaLinux / Rocky
- Windows Server
- custom ISO placeholder
- selected OS state
- unavailable OS state

Each card should include:
- OS name
- version placeholder
- compatibility note
- selected/unavailable state
- text-based icon placeholder

QA rules:
- no external logos
- selected state obvious
- unavailable state clear
- cards compact

# SECTION — CONFIGURATION / PLAN BUILDER PANELS

Create a VPS configuration panel.

Include:
- CPU selector row
- RAM selector row
- storage selector row
- bandwidth row
- region selector
- OS selector
- backup toggle row
- snapshot add-on row
- managed support toggle
- billing cycle selector
- live summary area

Make the plan-builder feel more useful than a plain form:
- selected options should be obvious
- add-on states should be visible
- summary should update visually as a static mock
- price summary must be readable
- use subtle accent/tint only where it clarifies selection

QA rules:
- labels visible
- options compact
- selected state obvious
- no fake interactivity unless already supported
- mobile stacks cleanly

# SECTION — ORDER SUMMARY / CHECKOUT SIDEBAR

Create an order summary panel.

Include:
- selected plan
- selected region
- selected OS
- selected billing cycle
- add-ons
- promo code row
- subtotal
- discount placeholder
- VAT/tax placeholder
- total
- renewal note
- terms note

Make total visually clear.

QA rules:
- total readable
- tax/renewal notes visible
- promo applied/invalid states shown
- sidebar stacks below configuration panel on mobile

# SECTION — ADD-ON CARDS

Create add-on cards for:
- extra backup
- extra snapshot
- additional IPv4
- managed support
- control panel
- extra storage
- monitoring
- migration assistance
- firewall/security add-on

Each should include:
- add-on name
- short description
- price placeholder
- selected/unselected state
- compatibility note if useful

QA rules:
- selected state clear
- add-ons do not look like primary products
- pricing secondary to main plan

# SECTION — BILLING CYCLE SELECTOR

Create a billing cycle block.

Include:
- monthly
- quarterly
- yearly
- savings note
- selected state
- renewal note
- billing disclaimer

QA rules:
- selected state clear
- savings note controlled
- renewal note visible
- not confused with navigation tabs

# SECTION — PROMO CODE BLOCK

Create promo code component.

Include:
- empty state
- applied promo state
- invalid promo state
- discount summary
- removal action

QA rules:
- invalid state includes text
- applied discount visible but not over-promotional
- removal action lower emphasis

# SECTION — CURRENCY / REGION PRICING NOTE

Create currency and regional pricing components.

Include:
- currency selector
- local currency note
- VAT/tax note
- region-specific price note
- exchange-rate disclaimer placeholder

QA rules:
- pricing notes readable
- disclaimers visible
- selector does not dominate pricing

# SECTION — CTA STRIPS / CONVERSION BANNERS

Improve this heavily.

Create compact CTA strips with stronger visual treatment.

Include:
- simple CTA strip
- migration CTA strip
- quote/contact CTA strip
- bottom-of-page CTA strip
- in-content CTA strip
- upgrade CTA strip
- storage upgrade strip
- business VPS quote strip

Examples:
- “Deploy your VPS in minutes”
- “Need more storage?”
- “Migrate your server”
- “Compare plans”
- “Talk to hosting support”
- “Get a custom VPS quote”
- “Add backups before launch”
- “Upgrade RAM without rebuilding”

CTA strips must be compact, but visibly stronger than normal cards.

Use:
- dark indigo variant
- light tinted variant
- promo variant
- trust variant
- technical/code variant

QA rules:
- compact, not hero-sized
- one primary action
- secondary action lower emphasis
- copy short
- no giant gradients
- no fake landing-page treatment
- CTA visible

# SECTION — PROMO / OFFER BANNERS

Improve offer banners.

Include:
- welcome discount banner
- limited-time offer banner
- plan upgrade banner
- free snapshot banner
- backup included banner
- migration assistance banner
- seasonal campaign banner
- pricing-page offer row
- storage bonus banner

Offer banners must be more visible than plain info cards, but must not feel cheap.

QA rules:
- offer colour controlled
- no warning/error colours as promo colours
- offer label compact
- legal/terms note visible
- not fake scarcity unless labelled placeholder

# SECTION — TRUST / PROOF BLOCKS

Create trust/proof components.

Do not use fake testimonials, fake awards, or fake customer names.

Use generic trust/proof structures:
- uptime target block
- data centre/location block
- backup policy block
- security controls block
- support availability block
- root access/full control block
- transparent pricing block
- deployment process block
- SLA-style information block
- service status summary block

Make this section more visually useful:
- one trust banner
- one trust checklist
- one proof card grid
- one status summary panel
- one policy strip

No fake claims unless labelled placeholder.

QA rules:
- factual/generic
- calm but visually clear
- no fake metrics
- proof hierarchy visible

# SECTION — FEATURE GRID SYSTEM

Create feature grids.

Include:
- 3-card feature grid
- 4-card feature grid
- icon/label + title + copy card
- technical feature card
- business benefit card
- security feature card
- performance feature card
- storage feature card

Feature examples:
- NVMe performance
- full root access
- snapshots
- backups
- IPv4 + IPv6
- Linux images
- Windows Server
- instant deployment
- scalable resources
- firewall/security

Make feature grids less bland:
- use subtle accent rails
- use controlled icon placeholders
- use section label
- use compact link area
- avoid random colours

QA rules:
- cards align
- copy short
- icon placeholders restrained
- not every card needs action

# SECTION — SERVER STATUS CARDS

Create server status cards.

Include:
- online status
- offline status
- degraded status
- maintenance status
- provisioning status
- backup completed
- backup failed
- snapshot status
- network status
- storage usage status

Each status must include:
- status dot/icon
- status text
- short explanation
- optional value/percentage
- no colour-only meaning

Use varied values:
- online 100%
- degraded 72%
- maintenance 40%
- provisioning 20%
- backup completed 100%
- backup failed 0%
- storage usage 88%

QA rules:
- semantic colours reserved
- text explains state
- usable in public trust section and dashboard preview

# SECTION — ALERT AND STATE BLOCKS FOR VPS

Create VPS-specific alert/state blocks.

Include:
- server online
- server offline
- deployment pending
- backup completed
- backup failed
- payment required
- quota warning
- location unavailable
- OS image deprecated
- high usage warning
- security notice
- maintenance notice

QA rules:
- alerts inline and contextual
- not decorative
- each alert has text/action/explanation
- warning/error not used for ordinary promos

# SECTION — METRIC / RESOURCE CARDS

Create metric cards for:
- CPU usage
- RAM usage
- disk usage
- bandwidth usage
- uptime
- response time
- snapshot count
- backup count
- active services
- monthly traffic

Use varied values:
- CPU 38%
- RAM 64%
- disk 72%
- bandwidth 20%
- uptime placeholder 100%
- response time placeholder
- snapshots 12
- backups 4
- services 8
- monthly traffic 40%

QA rules:
- metric number clear
- label visible
- trend/status secondary
- no fake claim unless placeholder

# SECTION — MINI CHART / USAGE BLOCKS

Create simple CSS/SVG-style chart previews.

Include:
- line chart placeholder
- bar chart placeholder
- usage meter
- circular storage meter
- progress bar
- bandwidth meter
- uptime indicator
- resource allocation bar
- warning threshold bar
- complete state bar
- no-data chart

Mandatory values:
- 0%
- 12%
- 20%
- 38%
- 40%
- 64%
- 72%
- 88%
- 90%
- 100%

QA rules:
- no external chart libraries
- no canvas required
- visualizations compact
- labels included
- no colour-only meaning
- not all values zero

# SECTION — TECHNICAL / CODE BLOCKS

Create technical content blocks.

Include:
- install command block
- SSH command block
- API request block
- config snippet block
- copyable command row
- code block with label
- code block with status/result line
- cloud-init placeholder
- nginx config placeholder

Use clean documentation-style code blocks.

Do not create fake terminal theatre.

QA rules:
- code scrolls inside wrapper
- text readable
- label explains context
- copy action secondary

# SECTION — DOCUMENTATION CALLOUTS

Create docs callouts for:
- info callout
- warning callout
- success callout
- error callout
- technical note callout
- migration note callout
- billing note callout
- security note callout

QA rules:
- semantic colours consistent
- text explains state
- not decorative
- not too large

# SECTION — FAQ BLOCKS

Create FAQ components.

Include:
- simple FAQ list
- accordion-style FAQ
- pricing FAQ
- technical FAQ
- migration FAQ
- support FAQ

Example questions:
- Can I upgrade later?
- Do I get root access?
- Is IPv6 included?
- Are backups included?
- Can I install my own software?
- Do you support Windows Server?
- What happens if I exceed bandwidth?
- Can I change regions?

QA rules:
- compact content
- accessible accordion
- questions relevant to VPS buying decisions

# SECTION — PROCESS / STEP BLOCKS

Create process blocks for:
- deployment steps
- migration steps
- backup setup steps
- upgrade steps
- ordering steps
- support escalation steps

Example flow:
1. Choose a VPS plan
2. Select region and OS
3. Configure add-ons
4. Deploy server
5. Connect via SSH/RDP

Add one more visual process banner:
- compact horizontal deployment process
- numbered steps
- status labels
- progress values, not all zero

QA rules:
- steps compact
- numbers visible
- mobile stacks
- not decorative timeline unless useful

# SECTION — TIMELINE / ACTIVITY BLOCKS

Create timeline blocks for:
- provisioning timeline
- backup history
- maintenance timeline
- billing event timeline
- support ticket timeline
- deployment log timeline

QA rules:
- chronological structure clear
- status labels visible
- no fake live data
- works as public proof and dashboard preview

# SECTION — SECURITY AND COMPLIANCE BLOCKS

Create security-related components.

Include:
- firewall card
- SSH key card
- password reset card
- 2FA reminder card
- DDoS protection block
- backup retention block
- access control block
- audit log preview
- SSL/TLS note block

QA rules:
- calm factual security language
- do not overuse danger colour
- not alarmist

# SECTION — SUPPORT / CONTACT BLOCKS

Create support components.

Include:
- support card
- ticket CTA block
- live chat available/unavailable state
- knowledge base card
- emergency support card
- migration assistance card
- sales quote card

QA rules:
- support states clear
- sales/contact CTAs not too loud
- no fake response times unless placeholder

# SECTION — TESTIMONIAL / REVIEW STRUCTURE ONLY

Create testimonial/review structure only.

Do not include fake testimonials.

Use placeholders:
- quote placeholder
- reviewer placeholder
- company placeholder
- rating placeholder
- source placeholder

Label clearly:
“Structure only — replace with real customer proof.”

QA rules:
- do not invent social proof
- design supports real proof later

# SECTION — LOGO / COMPATIBILITY STRIPS

Create text-only compatibility strips.

Do not use fake logos.

Include:
- operating system compatibility strip
- payment method strip placeholder
- technology compatibility strip
- control panel compatibility strip
- data centre/region strip

Use text labels only unless real logos are supplied.

QA rules:
- no fake brand logos
- compact
- wraps cleanly

# SECTION — SEO CONTENT SECTION BLOCKS

Create SEO/content page blocks.

Include:
- intro content block
- two-column content block
- comparison content block
- specs explanation block
- “who this is for” block
- “when not to choose this” block
- internal link block
- related pages block

Make these more useful:
- use one soft tinted content band
- use one dark technical content band
- use one trust/limitations block
- use one internal-link card group

QA rules:
- readable
- not too card-heavy
- internal links clear
- useful for long product pages

# SECTION — RELATED PRODUCT / INTERNAL LINK CARDS

Create related page cards.

Include:
- related VPS plans
- related guides
- related locations
- related operating systems
- related use cases
- upgrade path cards

QA rules:
- links secondary
- cards compact
- no duplicate CTA dominance

# SECTION — TABLE OF CONTENTS / SIDE NAV FOR WEBSITE PAGES

Create TOC components for long VPS pages.

Include:
- sticky contents nav preview
- section anchor list
- active state
- mobile collapsed variant

QA rules:
- low emphasis
- active state clear
- mobile contained

# SECTION — BREADCRUMBS

Create breadcrumb examples for:
- product page
- docs page
- comparison page
- location page
- use-case page

QA rules:
- low emphasis
- compact
- not substitute for primary nav

# SECTION — PAGE HEADER PATTERNS

Create page header patterns.

Include:
- standard VPS page header
- compact page header
- technical page header
- pricing page header
- documentation page header
- comparison page header
- location page header
- product hero header
- campaign header

These must be more visually useful than the previous output.

They must show:
- heading hierarchy
- eyebrow/metadata
- action area
- specs row or trust row where relevant
- light and dark treatment examples
- controlled accent usage

QA rules:
- not giant landing sections
- compact and documentation-like
- hierarchy clear
- actions optional

# SECTION — EMPTY STATES

Create empty states for:
- no servers yet
- no backups yet
- no snapshots yet
- no invoices yet
- no support tickets yet
- no monitoring data yet

QA rules:
- useful explanation
- one recovery action
- compact
- not decorative

# SECTION — LOADING / SKELETON STATES

Create skeleton states for:
- pricing card skeleton
- table skeleton
- server card skeleton
- chart skeleton
- form skeleton

QA rules:
- subtle
- no layout shift
- same shape as final component

# SECTION — ERROR STATES

Create error states for:
- failed to load plans
- payment failed
- region unavailable
- OS image unavailable
- server deployment failed
- backup failed

QA rules:
- error clearly explained
- recovery action present
- not colour-only
- destructive colour reserved

# SECTION — UPGRADE / UPSELL BLOCKS

Create upgrade blocks for:
- upgrade RAM
- add storage
- add backups
- add monitoring
- upgrade to managed support
- upgrade to yearly billing
- add additional IP

Make them visually stronger than plain cards, but not aggressive.

QA rules:
- useful, not pushy
- one action
- pricing clear
- no fake scarcity

# SECTION — GUARANTEE / POLICY BLOCKS

Create policy blocks for:
- refund policy
- uptime policy
- backup policy
- fair-use bandwidth note
- SLA note
- acceptable use note
- data retention note

QA rules:
- readable
- caveats visible
- no fake guarantees
- no exaggerated claims

# SECTION — VPS-SPECIFIC TRUST CHECKLIST

Create a checklist block with:
- full root access
- NVMe storage
- IPv4 + IPv6
- snapshots
- backups
- scalable resources
- operating system choice
- support access
- transparent pricing
- no long-term lock-in placeholder if applicable

QA rules:
- compact
- icons/marks not colour-only
- no unsupported claims

# SECTION — COMPETITOR / ALTERNATIVE COMPARISON BLOCKS

Create comparison blocks for:
- VPS vs shared hosting
- VPS vs dedicated server
- VPS vs hyperscaler cloud
- VPS vs managed hosting
- Cloud VPS vs Storage VPS
- Linux VPS vs Windows VPS

Use generic labels only.

Do not name real competitors unless supplied.

QA rules:
- neutral comparison
- no false claims
- tables readable
- highlighted recommendation subtle

# SECTION — BEST FOR / NOT BEST FOR BLOCK

Create decision helper block.

Include:
- best for developers
- best for small businesses
- best for agencies
- best for storage workloads
- best for remote desktop
- not best for fully managed hosting unless managed support exists
- not best for non-technical users unless support/management exists

QA rules:
- useful conversion guidance
- honest limitations
- not sales hype

# SECTION — SECTION DIVIDER / BACKGROUND TREATMENTS

Create section background examples.

Include:
- white section
- subtle tinted section
- bordered section
- dark indigo section
- restrained gradient section
- technical/code section
- compact CTA section
- trust/proof band
- promo band

This section should explicitly show that VPS pages can have stronger visual rhythm than dashboard pages.

QA rules:
- background treatment helps hierarchy
- no random decorative gradients
- long text remains readable

# SECTION — WEBSITE RESPONSIVE BEHAVIOUR RULES

Add VPS website responsive QA section.

Include:
- pricing cards stack cleanly
- product cards stack cleanly
- tables scroll inside wrappers
- specs cards readable
- order summary stacks below config panel
- CTA strips not cramped
- hero banners become compact
- promo banners remain readable
- badges and chips remain inline-sized
- forms single column on mobile
- TOC collapses or stacks
- no horizontal page overflow at 390px, 360px, 320px
- chart labels remain visible
- usage meters keep values visible

# SECTION — VPS WEBSITE COMPONENT INDEX

Add final VPS website component index table.

Columns:
- Component
- Existing dashboard component reused
- Use when
- Do not use when
- Required anatomy
- Visual intensity tier
- Mobile QA check
- Failure condition
- Documentation file updated

Include every new VPS component family.

Make it practical for future agents.

# INTEGRATION WITH EXISTING DASHBOARD SYSTEM

For every new VPS component, identify which existing dashboard component or pattern it extends.

Examples:
- pricing card extends product card / selected card / metric card
- comparison table extends data table
- order summary extends right inspector / summary panel
- configuration panel extends forms + settings rows
- region selector extends product card / selected card
- OS selector extends selectable card
- CTA strip extends alert/card/action group
- promo banner extends info/warning card, but must not misuse warning colour
- trust/proof block extends card / metric card
- process steps extend setup checklist
- timeline extends event feed / activity timeline
- code block extends code panel / query editor styling
- related links extend related-link cards
- empty states extend existing empty state
- status cards extend service health/status components
- hero/banner examples extend page header / section treatment patterns
- marketing proof sections extend content section + card group patterns
- usage charts extend chart panels / quota meters / donut charts

Add this mapping visibly in the component index.

# DOCUMENTATION DELIVERABLES

You must update the documentation, not only the HTML.

Update README.md to include:
- package purpose
- updated file list
- how to open the HTML showcase
- how to use the VPS Website section
- how to use the docs
- QA expectations
- zip contents

Update DESIGN.md to include:
- VPS website extension overview
- additive VPS token system
- visual intensity tiers
- VPS marketing component rules
- VPS chart/usage state rules
- pricing card rules
- comparison table rules
- CTA/promo/banner rules
- hero/page-header treatment rules
- trust/proof rules
- responsive rules
- anti-patterns

Update INDEX.md to include:
- all VPS components
- keywords
- use when
- do not use when
- related existing component pattern
- QA notes

Update COMPONENT_IMPLEMENTATION_AND_QA_SPEC.md to include:
- VPS extension implementation rules
- VPS compact component rules
- VPS marketing component rules
- chart value requirements
- 0/20/40/72/90/100 percentage testing
- mobile QA rules
- failure conditions

Create VPS_COMPONENT_IMPLEMENTATION_AND_QA_SPEC.md with:
- all VPS components
- implementation anatomy
- do / do not
- responsive behaviour
- accessibility
- visual intensity tier
- QA checks
- failure conditions

Create VPS_COMPONENT_INDEX.md with:
- component name
- category
- keywords
- existing dashboard component reused
- use when
- do not use when
- required anatomy
- visual intensity tier
- QA check

Create CHANGELOG.md with:
- summary of changes
- added VPS components
- visual impact corrections
- chart/value corrections
- documentation updates
- known placeholders

Return all files in a zip.

# COMPONENT_IMPLEMENTATION_AND_QA_SPEC.md AUTHORITY

The QA spec is not optional.
It is the pass/fail authority.

Apply these rules to every new VPS component:
- No compact component may become full width unless explicitly defined as a row component.
- Badges, chips, labels, metadata pills, icon buttons, tabs, command shortcuts, and small utility controls must remain intrinsic-width on mobile.
- Tables, comparison tables, pricing tables, code blocks, configuration tables, and dense technical content may scroll inside their own wrapper, but the page itself must not horizontally overflow.
- Mobile drawers, menus, toolbars, order summaries, configuration panels, and inspector-like panels must align to the same gutters as surrounding content.
- Primary actions must remain visually primary, but there must not be multiple competing primary buttons in one local action group.
- Shadows are allowed mainly for overlays, menus, drawers, modals, and toasts. Normal cards use borders, not shadows.
- Semantic colours must indicate semantic state. They are not decorative accents.
- All focusable controls must have visible focus states and accessible names.
- Forms must have visible labels.
- Errors must include text, not colour alone.
- Status must not rely on colour alone.
- Dense tables and code snippets must not cause page-level horizontal scroll.
- If a badge stretches full width, the implementation is wrong.
- If a chip looks like a CTA, the implementation is wrong.
- If a pricing or comparison table overflows the page, the implementation is wrong.
- If mobile at 390px, 360px, or 320px breaks, the implementation is wrong.

# REQUIRED REVIEW WIDTHS

After implementation, visually inspect the updated HTML at:
- 1440px
- 1280px
- 1024px
- 920px
- 768px
- 640px
- 480px
- 390px
- 360px
- 320px

These mobile widths are mandatory.

# AUTOMATIC REJECTION CONDITIONS

Reject your own implementation and fix it before returning if any of these are true:
- the VPS section remains visually bland
- there are no compact hero/banner/marketing components that stand out
- CTA strips look like plain cards
- pricing cards do not show clear hierarchy
- charts/meters are all 0%
- chart states do not include varied percentages
- a compact badge becomes full width
- a chip looks like a primary action
- a table causes page-level horizontal overflow
- a code block, query, command, or long technical value causes page-level overflow
- a toolbar wraps randomly instead of by logical group
- a card has asymmetric padding
- a normal card uses modal/dropdown-level shadow
- there are multiple competing primary actions in one local group
- semantic colours are used decoratively
- a form field lacks a visible label
- an icon-only control lacks an accessible name
- focus states are missing or clipped
- drawer/menu/modal layout breaks at 390px, 360px, or 320px
- the VPS extension looks unrelated to the existing dashboard system
- the VPS extension becomes a decorative marketing landing page instead of a design-system showcase
- documentation files are not updated
- zip file is not returned

# COMPLETE SHOWCASE SECTION INVENTORY

The updated HTML must contain:

Existing sections preserved:
- header
- overview
- tokens
- typography
- colors
- layout
- components
- sections
- app patterns
- states
- responsive
- rules
- index

New or improved VPS sections:
1. VPS website overview
2. VPS website token extension
3. VPS visual intensity tiers
4. VPS marketing components
5. VPS hero/banner treatments
6. VPS pricing card system
7. VPS plan comparison tables
8. VPS product family cards
9. VPS use-case cards
10. VPS specs/resource cards
11. VPS region/location cards
12. VPS operating system selector cards
13. VPS configuration/plan builder panels
14. VPS order summary/checkout sidebar
15. VPS add-on cards
16. VPS billing cycle selector
17. VPS promo code block
18. VPS currency/region pricing notes
19. VPS CTA strips
20. VPS promo/offer banners
21. VPS trust/proof blocks
22. VPS feature grids
23. VPS server status cards
24. VPS alerts/states
25. VPS metrics/resource cards
26. VPS mini chart/usage blocks with varied percentages
27. VPS technical/code blocks
28. VPS documentation callouts
29. VPS FAQ blocks
30. VPS process/step blocks
31. VPS timeline/activity blocks
32. VPS security/compliance blocks
33. VPS support/contact blocks
34. VPS testimonial/review structure only
35. VPS compatibility strips
36. VPS SEO content section blocks
37. VPS related product/internal link cards
38. VPS table of contents/side nav
39. VPS breadcrumbs
40. VPS page header patterns
41. VPS empty states
42. VPS loading/skeleton states
43. VPS error states
44. VPS upgrade/upsell blocks
45. VPS guarantee/policy blocks
46. VPS trust checklist
47. VPS competitor/alternative comparison blocks
48. VPS best-for/not-best-for block
49. VPS section divider/background treatments
50. VPS responsive behaviour rules
51. VPS website component index
52. VPS QA checklist

# IMPORTANT CONTENT RULES

Use placeholder content where exact business data is not supplied.

Do not invent:
- real customer names
- real testimonials
- real awards
- real uptime metrics
- real SLA values
- real data centre claims
- exact pricing unless already supplied
- exact support response times
- competitor claims
- fake scarcity
- fake benchmark claims

Use generic placeholders:
- “Placeholder price”
- “Region availability placeholder”
- “SLA placeholder”
- “Support response placeholder”
- “Replace with real customer proof”
- “Terms placeholder”
- “VAT/tax placeholder”
- “Placeholder uptime target”
- “Placeholder discount”
- “Placeholder latency”
- “Placeholder monthly traffic”

# FINAL REVIEW CHECKLIST

Before returning, confirm:
- existing design system remains intact
- VPS section is clearly added
- VPS components use existing tokens and style language
- VPS tokens are additive, not replacements
- VPS layer is more visually impactful than previous output
- compact hero/banner/marketing components exist
- charts/meters show varied percentage values
- not all charts are 0%
- pricing cards have clear hierarchy
- CTA strips are visible and useful
- promo banners are controlled but noticeable
- trust/proof blocks are visually scannable
- COMPONENT_IMPLEMENTATION_AND_QA_SPEC.md has been applied
- no decorative SaaS/landing-page redesign
- no dark command-deck redesign
- no fake dashboard theatre
- no external assets
- no broken links
- no fake social proof
- no private data
- tables scroll inside wrappers
- badges/chips stay inline-sized
- order summary stacks
- configuration panel stacks
- toolbars wrap by group
- code blocks scroll internally
- focus states visible
- form labels visible
- mobile at 390px, 360px, and 320px is usable
- README.md updated
- DESIGN.md updated
- INDEX.md updated
- COMPONENT_IMPLEMENTATION_AND_QA_SPEC.md updated
- VPS docs created
- CHANGELOG.md created
- zip file returned

# COMPLETION AND VERIFICATION

Return the completed ZIP containing the eight deliverables specified above. Preserve the console, extend the VPS layer, keep all 52 VPS sections in the inventory, and record any unsupported claims as labeled sample placeholders rather than facts.

Perform the specified source, interaction, accessibility, and viewport checks with available tools. In the QA documents, record each check as passed, failed, or not run, with evidence. A generated checklist is not proof of execution. Do not score an unperformed visual check as passed or describe a package as fully verified when required checks remain unavailable.
````
<!-- prompt:end -->

## Usage notes

A specialized VPS extension, not a generic showcase template. Preserves all 52 required sections, additive #020281 brand token, chart values, and ten review widths.

**Relevant capabilities:** `file-access`, `code-execution`, `browser`, `archive-creation`. These are requirements or conditional needs, not tools installed by this file.

## Related entries

- [Consolidate Sources Into a Design-System Showcase](create-design-system-showcase.md) — Consolidate extracted design evidence into one coherent, standalone HTML component showcase.
- [Audit and Implement Design-System Compliance](../quality/design-system-compliance-audit-and-fix.md) — Extract atomic design requirements, implement them in controlled passes, and score only verified compliance.
- [Compare Six VPS Brand Palettes](research-vps-palette-comparison.md) — Compare six palettes in a neutral editorial HTML document while preserving a fixed dark-indigo brand anchor.

[Browse the catalog](../../../CATALOG.md) · [Usage guide](../../../docs/usage.md)
