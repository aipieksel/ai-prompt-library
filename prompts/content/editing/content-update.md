---
id: "content-update"
title: "Apply Approved Content Feedback"
type: "prompt"
primary_category: "content"
categories: ["content"]
subcategory: "editing"
when_to_use: "Apply approved feedback to matching Markdown files and return corrected copy with a change summary"
search_terms: ["content-update", "content", "editing"]
inputs: ["FILE_PAIRS"]
output: "updated-<base>.md and summary-<base>.md for every matched pair."
mode: "edit"
capabilities: ["file-access", "research-when-needed"]
related: ["content-audit", "no-invention"]
aliases: ["content/content-update.prompt.md", "content-update.prompt.md"]
---

# Apply Approved Content Feedback

Apply approved feedback to matching Markdown files and return corrected copy with a change summary.

**Type:** prompt · **Mode:** edit · **ID:** `content-update`

**Expected output:** updated-<base>.md and summary-<base>.md for every matched pair.

## Inputs

Replace every listed placeholder. For an optional source, enter `None` when it is unavailable.

| Placeholder | What to provide | Example |
| --- | --- | --- |
| `{{FILE_PAIRS}}` | Matching original- and approved feedback- Markdown files. | original-linux-vps.md plus feedback-linux-vps.md |

## Prompt

Copy the block below, not the metadata or usage notes.

<!-- prompt:start -->
````text
Original copy and approved feedback files:
{{FILE_PAIRS}}

Apply the approved feedback to the matching Markdown source. For each pair, return updated-<base>.md and summary-<base>.md. Keep the source files unchanged.

### Match and isolate inputs

Match original-<base>.md only with feedback-<base>.md. Process one pair at a time as an independent task. Do not transfer conclusions, assumptions, copy changes, or context between pairs. Do not merge outputs or combine feedback across pages.

Before editing, identify missing partners or ambiguous duplicate basenames. Report unmatched files instead of applying feedback to a guessed source. An approved feedback file defines the authorized changes; do not treat unapproved suggestions as permission.

### Editing rules

1. Do not invent features, services, guarantees, pricing, locations, technical specifications, claims, certifications, performance details, or business information.
2. Do not rewrite merely to sound better, or lengthen copy unless a genuine issue requires it.
3. Preserve Markdown headings, page/section order, formatting, links, lists, metadata, tone, style, and positioning except where approved feedback requires a change.
4. Apply feedback that is supported by the original page. Flag an unrelated newly discovered issue in the summary rather than expanding scope silently.
5. Where the heading and body disagree, correct the body to fit the heading and page topic unless the evidence specifically identifies the heading as wrong.
6. Correct a wrong product, service, audience, location, CTA, or context using only page-specific evidence or verified research.
7. Make the smallest safe correction when evidence is incomplete. Otherwise leave the relevant wording unchanged and record the issue as unresolved.
8. Remove or correct identified repetition, vague claims, misplaced paragraphs, contradictions, and copy that does not belong in its section. Avoid generic filler.
9. Add or remove sections only when the approved feedback explicitly supports that action.
10. Preserve valid URLs, slugs, anchors, product names, and brand names unless they are identified as incorrect.
11. Do not change a factual assertion without evidence that the correction is justified.

### Research

Verify time-sensitive or uncertain facts before editing them: pricing, locations, product names, technical claims, company information, platform capabilities, and legal/compliance wording. Prefer the company's official website, documentation, product/pricing pages, and other relevant primary sources.

Do not claim current verification without source access. If research confirms a correction, record the source and access date in the summary. If research is inconclusive, keep the wording conservative and record the uncertainty. Research for one file pair does not authorize edits to another pair unless it independently applies to that page.

### Apply feedback item by item

Locate the issue in the matching source, understand its surrounding context, and select the needed action: small correction, contextual rewrite, relocation, deletion, CTA adjustment, factual correction, or no change when the feedback is unsupported. Preserve issue IDs when available. Apply the smallest edit that fully resolves the supported issue.

### Updated-copy output

The updated Markdown must be clean and ready to use. Do not insert audit commentary, implementation notes, unresolved feedback, or hidden placeholders into public copy unless that was already an intentional part of the original format.

### Summary output

Use this structure:

# Summary of Changes

## Files Processed
List the original, feedback, updated, and summary filenames.

## Overall Result
Explain what was fixed overall.

## Issues Fixed
For each meaningful change include page/section, original issue, change made, reason, feedback ID/item addressed, whether research was used, and source/confirmation note when applicable.

## Issues Not Changed
Identify unapplied or unresolved feedback with a reason: insufficient information, vague feedback, source already correct, unsupported claim, or business confirmation needed.

## Research Notes
Include only when research was used. State what was verified, the source, and when it was checked.

## Final Notes
Identify remaining human review, especially uncertain pricing, product facts, compliance wording, or business-specific claims.

### Output contract

Return exactly two separate files for each successfully matched pair: updated-<base>.md and summary-<base>.md. Do not merge them or add a long chat explanation. Report missing-pair blockers separately without manufacturing outputs.

Example inputs:
- original-linux-vps.md
- feedback-linux-vps.md
- original-windows-vps.md
- feedback-windows-vps.md

Example outputs:
- updated-linux-vps.md
- summary-linux-vps.md
- updated-windows-vps.md
- summary-windows-vps.md

If file tools are unavailable, return complete Markdown contents under each exact output filename and state that files were not created.
````
<!-- prompt:end -->

## Usage notes

Supply the actual referenced material. A filename or URL does not grant the assistant file, browser, account, or edit access.

**Relevant capabilities:** `file-access`, `research-when-needed`. These are requirements or conditional needs, not tools installed by this file.

## Related entries

- [Audit Website Copy](content-audit.md) — Find contextual, factual, repetitive, and misplaced website copy without rewriting the source.
- [No Invention](../../../modifiers/no-invention.md) — Use when the agent must not make up claims, prices, features, APIs, or behavior.

[Browse the catalog](../../../CATALOG.md) · [Usage guide](../../../docs/usage.md)
