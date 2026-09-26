---
id: "assess-html-publish-readiness"
title: "Assess HTML Publish Readiness"
type: "prompt"
primary_category: "design"
categories: ["design"]
subcategory: "quality"
when_to_use: "Assess an HTML page for SEO, conversion, credibility, factual safety, and publish readiness without editing it"
search_terms: ["assess-html-publish-readiness", "design", "quality", "publish readiness", "SEO", "404", "pre-launch", "asses-this-page"]
inputs: ["HTML_FILE", "PAGE_CONTEXT", "DEPLOYMENT_STATE"]
output: "assessed-<source-stem>.md plus a short score and recommendation message."
mode: "audit"
capabilities: ["file-access", "research", "browser-when-available"]
related: ["fix-html-from-assessment", "content-audit", "visual-verification"]
aliases: ["asses-this-page.md", "asses-this-page"]
---

# Assess HTML Publish Readiness

Assess an HTML page for SEO, conversion, credibility, factual safety, and publish readiness without editing it.

**Type:** prompt · **Mode:** audit · **ID:** `assess-html-publish-readiness`

**Expected output:** assessed-<source-stem>.md plus a short score and recommendation message.

## Inputs

Replace every listed placeholder. For an optional source, enter `None` when it is unavailable.

| Placeholder | What to provide | Example |
| --- | --- | --- |
| `{{HTML_FILE}}` | The complete HTML file, not only a screenshot or excerpt. | linux-vps.html |
| `{{PAGE_CONTEXT}}` | Page goal, intended audience, approved product facts, and source references; use None for unavailable context. | Linux VPS product page for self-managed deployments; approved product brief attached. |
| `{{DEPLOYMENT_STATE}}` | One of live, unpublished, or unknown. | unpublished |

## Prompt

Copy the block below, not the metadata or usage notes.

<!-- prompt:start -->
````text
HTML source to assess:
{{HTML_FILE}}

Page purpose, audience, product facts, and supporting references:
{{PAGE_CONTEXT}}

Deployment state (live, unpublished, or unknown):
{{DEPLOYMENT_STATE}}

Audit the actual HTML for SEO, search intent, conversion, credibility, factual safety, design consistency, and publish readiness. Read the whole file, including metadata, structured data, links, scripts relevant to the assessment, and visible copy. Do not edit or rewrite the HTML in this task.

### Establish the page context

Identify the page's purpose, target audience, search intent, primary offer, main CTA, intended canonical URL, and deployment state from the supplied evidence. Distinguish a local or staged preview from a published page. A URL returning 404 does not by itself establish that the page is intended to be live.

Use the supplied provider and product facts, not assumptions about a particular company. Do not invent features, prices, locations, partnerships, customer reviews, guarantees, managed services, or technical capabilities. Distinguish a provider's commercial plan recommendation from an application's official minimum requirements.

### Research before making factual corrections

Verify material, time-sensitive or uncertain technical and product claims against current primary sources where access is available. Examples include software requirements, supported deployment methods, version compatibility, product capabilities, promotional eligibility, and official setup guidance. Cite the source URL and access date.

For each research item record:
- What was checked.
- The source and date checked.
- What the source actually establishes.
- How it affects this page.
- The recommended correction, if any.
- Confidence and any remaining uncertainty.

Do not turn an unverified assumption into a confirmed defect. Use research status **Confirmed**, **Not confirmed**, or **Not required**. If live research or browser access is unavailable, identify that limitation and separate static inspection from unperformed checks. Verification is dated evidence, not a permanent guarantee.

### Assess seven categories

Score each category from 0 to 10 and explain the score using concrete evidence:

1. **SEO structure:** title and description, H1 and heading hierarchy, canonical and social metadata, meaningful links, image alternatives, indexability directives, structured-data syntax and consistency with visible content.
2. **Search intent match:** relevance to the query and audience, answer completeness, helpful section order, topic focus, appropriate comparisons, and practical next steps.
3. **Conversion strength:** clarity of the offer, plan or product guidance, CTA labels and destinations, decision support, friction, useful proof, and whether disclaimers or repetition overwhelm the action.
4. **Trust and credibility:** clarity, consistency, substantiated claims, transparent limitations, credible supporting sources, and absence of misleading reassurance or fabricated proof.
5. **Technical and factual safety:** accurate terminology, requirements, commands, deployment assumptions, compatibility, security-sensitive guidance, support boundaries, and qualified claims.
6. **Design and UX consistency:** layout, density, spacing, typography, component consistency, readability, accessible controls, responsive behavior, and visible interaction affordances. Do not claim a rendered defect from unrendered source alone.
7. **Publish readiness:** whether the page's HTML and copy are ready for their intended deployment, subject to separately listed launch checks.

Scoring is an editorial review, not a search-engine ranking prediction or external benchmark. Use a consistent rubric: 0–2 = fundamentally unusable or misleading; 3–4 = major rework; 5–6 = usable only after significant fixes; 7–8 = strong with specific remaining issues; 9–10 = strong, supported, and ready within the checks performed. The overall score is the arithmetic mean of the seven category scores, rounded to one decimal. State the evidence limits beside it.

### Unpublished-page URL rule

For an unpublished or staged page, a correctly formed intended page URL, self-link, canonical URL, Open Graph URL, Twitter URL, breadcrumb URL, or explicitly planned internal destination may legitimately return 404 before deployment.

Do not lower a score, classify a critical/high issue, block publication, or add an HTML-fix instruction solely because such an intended future URL is not live yet. Put those checks in a separate **Pre-launch/deployment QA** section.

An incorrect host, malformed value, wrong slug, inconsistent URL, missing required attribute, or genuinely broken destination expected to be live is still an HTML issue. Explain the evidence for that distinction. For unknown deployment state, flag uncertainty; do not infer a confirmed broken-link defect from 404 alone.

### Report issues precisely

For every issue include:
- A stable issue ID, such as HTML-001.
- Category and exact location: element, selector, section, metadata property, or line when available.
- The exact current wording or relevant HTML excerpt.
- The specific problem and its effect on readers or the page goal.
- A concrete correction, including proposed wording or HTML where evidence permits.
- Priority: **Critical**, **High**, **Medium**, or **Low**.
- Research status: **Confirmed**, **Not confirmed**, or **Not required**, with supporting evidence.

Use Critical for severe misleading, unsafe, or fundamentally blocking defects; High for substantial correctness or conversion problems; Medium for meaningful improvements; Low for polish. Do not inflate minor wording preferences into launch blockers. Do not repeatedly list the same issue under different categories.

Preserve useful detail. Identify repetition by quoting the specific passages; do not instruct a blanket content reduction. Recommend only changes justified by the source and the page goal. Do not add unrelated sections or generic SEO tasks.

### Examples of appropriately scoped recommendations

These examples illustrate the level of specificity, not mandatory edits to every page:
- Refine an overlong or unclear meta description; approximately 150–160 characters can be a working copy target where suitable, not a universal search-display rule.
- Clarify eligibility for a supplied promotion such as WELCOME20 only after checking the applicable offer.
- Qualify Docker deployment wording when support depends on the application's official instructions.
- Identify a Example Hosting starter plan as a provider recommendation, not an application's official minimum specification, when that distinction applies to the supplied page.
- Reduce an identified repetitive passage by roughly 15–20% only where its meaning and important information remain intact.
- Match FAQ structured data to the visible FAQ content and verify relevant documentation links.
- Treat a planned /status/ URL as deployment QA rather than an HTML defect unless the supplied URL is actually incorrect.

### Required Markdown report

Create one report named **assessed-<original HTML filename without extension>.md**. For example, `linux-vps.html` produces `assessed-linux-vps.md`. Do not replace this with a generic fixed filename.

Use these sections in order:

1. **Overall assessment:** overall score, a two-to-four-sentence explanation, and the deployment/evidence limits.
2. **Confirmed research:** checked claims, dated sources, findings, impact, confidence, and unresolved factual questions.
3. **Category scores:** all seven scores and short evidence-based rationales.
4. **Critical and high-priority issues:** the actionable blockers and substantial problems, or an explicit statement that none were found within the performed checks.
5. **Detailed assessment:** findings under each of the seven categories using the issue schema above.
6. **Pre-launch/deployment QA:** future-URL activation and other deployment-only checks, clearly excluded from HTML defect scoring.
7. **Exact HTML fix list:** one deduplicated checklist keyed to issue IDs, ordered by priority. Include exact wording or locations and acceptance checks. Exclude deployment-only tasks and unconfirmed corrections that require a factual decision first.
8. **Final recommendation:** choose one of “Ready to publish,” “Ready after minor fixes,” “Needs significant fixes before publishing,” or “Not ready to publish,” and justify it from the findings.

Return the Markdown file and a brief message with the overall score, recommendation, Critical/High counts, principal reason, and a link to the file that was actually created. If file tools are unavailable, return the complete report under its exact intended filename and state that it was not saved. Never claim a browser test, research check, or created file that did not occur.
````
<!-- prompt:end -->

## Usage notes

Supply the actual referenced material. A filename or URL does not grant the assistant file, browser, account, or edit access.

**Relevant capabilities:** `file-access`, `research`, `browser-when-available`. These are requirements or conditional needs, not tools installed by this file.

## Related entries

- [Fix HTML From an Approved Assessment](fix-html-from-assessment.md) — Apply only the approved issues from an HTML assessment; preserve all unrelated content, design, and behavior.
- [Audit Website Copy](../../content/editing/content-audit.md) — Find contextual, factual, repetitive, and misplaced website copy without rewriting the source.
- [Visual Verification](../redesign/visual-verification.md) — Use after UI changes when the agent should compare the result visually and fix issues.

[Browse the catalog](../../../CATALOG.md) · [Usage guide](../../../docs/usage.md)
