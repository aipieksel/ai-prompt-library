---
id: "content-audit"
title: "Audit Website Copy"
type: "prompt"
primary_category: "content"
categories: ["content"]
subcategory: "editing"
when_to_use: "Find contextual, factual, repetitive, and misplaced website copy without rewriting the source"
search_terms: ["content-audit", "content", "editing"]
inputs: ["CONTENT_FILES"]
output: "One feedback-<base>.md audit per source file; no changes to original copy."
mode: "audit"
capabilities: ["file-access"]
related: ["content-update", "no-invention"]
aliases: ["content/content-audit.prompt.md", "content-audit.prompt.md"]
---

# Audit Website Copy

Find contextual, factual, repetitive, and misplaced website copy without rewriting the source.

**Type:** prompt · **Mode:** audit · **ID:** `content-audit`

**Expected output:** One feedback-<base>.md audit per source file; no changes to original copy.

## Inputs

Replace every listed placeholder. For an optional source, enter `None` when it is unavailable.

| Placeholder | What to provide | Example |
| --- | --- | --- |
| `{{CONTENT_FILES}}` | Complete website-copy Markdown files or their contents. | original-linux-vps.md and original-windows-vps.md |

## Prompt

Copy the block below, not the metadata or usage notes.

<!-- prompt:start -->
````text
Website copy Markdown:
{{CONTENT_FILES}}

Audit the copy logically and contextually. Do not apply edits or rewrite the source. Find only issues worth fixing: text that does not make sense, mismatches a heading, repeats the wrong idea, is misplaced, contradicts another section, uses the wrong product/service/audience context, is generic, or reveals page-insensitive AI writing.

### Boundaries

- Do not invent features, services, claims, prices, locations, guarantees, specifications, or business details.
- Do not propose expansion unless a small correction is genuinely needed for sense.
- Preserve structure, headings, section and page order, tone, positioning, and approximate length unless an actual contextual defect justifies a targeted change.
- Do not rewrite for polish alone or make the copy more salesy, long, or creative without a clear reason.
- Check the page topic, heading, section purpose, paragraph meaning, CTA relevance, and internal consistency together.
- Explain uncertainty instead of guessing. A missing claim is not automatically a defect.

### Issue format

For each issue, assign a stable identifier such as COPY-001 and include:
- Page or section name and a precise location.
- Exact text or heading involved.
- What is wrong and why it does not fit.
- Severity: Critical, Medium, or Minor.
- Recommended fix direction.
- Change type: contextual rewrite, small wording correction, removal, or relocation.

Use Critical for materially misleading or contradictory copy, Medium for meaningful contextual or clarity problems, and Minor for worthwhile local polish. Keep subjective preference separate from an actual defect.

### Audit summary

Group the outcome under:
1. Critical issues that should be fixed.
2. Medium issues that would improve clarity or consistency.
3. Minor polish items.
4. Sections that are sound and should not change.

### Delivery

Create one feedback-<base>.md file per source Markdown file. For source original-<base>.md, remove the existing original- prefix before adding feedback-. For another source such as linux-vps.md, use feedback-linux-vps.md. Preserve internal dots in a filename and remove only the final .md extension.

Keep each page's evidence and conclusions separate. Return the audit file or files, not rewritten copy. Await approval before the content-update stage. If file creation is unavailable, provide the complete Markdown under its intended filename.
````
<!-- prompt:end -->

## Usage notes

Supply the actual referenced material. A filename or URL does not grant the assistant file, browser, account, or edit access.

**Relevant capabilities:** `file-access`. These are requirements or conditional needs, not tools installed by this file.

## Related entries

- [Apply Approved Content Feedback](content-update.md) — Apply approved feedback to matching Markdown files and return corrected copy with a change summary.
- [No Invention](../../../modifiers/no-invention.md) — Use when the agent must not make up claims, prices, features, APIs, or behavior.

[Browse the catalog](../../../CATALOG.md) · [Usage guide](../../../docs/usage.md)
