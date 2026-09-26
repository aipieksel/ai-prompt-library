---
id: "exact-output-format"
title: "Exact Output Format"
type: "modifier"
primary_category: "coding"
categories: ["coding", "design"]
subcategory: "agent-quality"
when_to_use: "Use when you need the agent to return exactly the requested format with no extra commentary"
search_terms: ["exact-output-format", "coding", "agent-quality", "format", "no-extras", "output", "output-format", "ready-to-paste", "single-version"]
inputs: ["OUTPUT_FORMAT"]
output: "Only the output required by the supplied contract."
mode: "modify"
capabilities: []
related: ["implementation-ready-output", "no-invention"]
aliases: ["coding/agent-quality/exact-output-format.md", "exact-output-format.md"]
---

# Exact Output Format

Use when you need the agent to return exactly the requested format with no extra commentary.

**Type:** modifier · **Mode:** modify · **ID:** `exact-output-format`

**Expected output:** Only the output required by the supplied contract.

## Inputs

Replace every listed placeholder. For an optional source, enter `None` when it is unavailable.

| Placeholder | What to provide | Example |
| --- | --- | --- |
| `{{OUTPUT_FORMAT}}` | Exact schema, template, filenames, and allowed failure representation. | Valid JSON with keys "status", "changed_files", and "verification". |

## Modifier

Copy the block below, not the metadata or usage notes.

<!-- prompt:start -->
````text
Required output contract:
{{OUTPUT_FORMAT}}

Return the main task's result in exactly this format. Do not add preambles, alternative versions, commentary, wrappers, or fields that the contract does not request. Do not leave unfinished placeholders in a completed deliverable.

Check syntax, required fields, ordering, filenames, and completeness before returning. For machine-readable formats, validate with an available parser rather than relying on appearance alone.

Do not fabricate data to satisfy the format. Use the contract's documented error or unavailable-value representation. If none exists and a blocking input is missing, request that input before producing the final artifact; do not emit a success-shaped result that conceals failure.
````
<!-- prompt:end -->

## Usage notes

This is a modifier: append it to a concrete prompt only when their scopes and output contracts agree.

## Related entries

- [Implementation-Ready Output](implementation-ready-output.md) — Use when you need exact code, files, patches, steps, or validation checks instead of vague advice.
- [No Invention](no-invention.md) — Use when the agent must not make up claims, prices, features, APIs, or behavior.

[Browse the catalog](../CATALOG.md) · [Usage guide](../docs/usage.md)
