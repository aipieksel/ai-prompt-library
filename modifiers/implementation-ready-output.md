---
id: "implementation-ready-output"
title: "Implementation-Ready Output"
type: "modifier"
primary_category: "coding"
categories: ["coding"]
subcategory: "implementation-control"
when_to_use: "Use when you need exact code, files, patches, steps, or validation checks instead of vague advice"
search_terms: ["implementation-ready-output", "coding", "implementation-control", "exact-code", "files", "implementation", "implementation-ready", "output", "patch", "validation"]
inputs: []
output: "Exact apply-ready files, patches, or steps in the main task's requested format."
mode: "modify"
capabilities: []
related: ["exact-output-format", "verify-before-returning"]
aliases: ["coding/implementation-control/implementation-ready-output.md", "implementation-ready-output.md"]
---

# Implementation-Ready Output

Use when you need exact code, files, patches, steps, or validation checks instead of vague advice.

**Type:** modifier · **Mode:** modify · **ID:** `implementation-ready-output`

**Expected output:** Exact apply-ready files, patches, or steps in the main task's requested format.

## Inputs

No placeholders. Use this with a concrete main task.

## Modifier

Copy the block below, not the metadata or usage notes.

<!-- prompt:start -->
````text
Return an implementation-ready deliverable for the main task, not vague advice or several speculative approaches.

Provide the exact files, code, patch, or execution steps the requested output requires. Identify file paths, required placement, necessary configuration, and focused validation checks wherever they are needed to apply the change correctly.

Keep the result complete and consistent with the inspected project. Do not use “rest unchanged” inside a requested full-file replacement, conceal missing sections, or describe unexecuted edits as applied.

If tool access prevents implementation or verification, say exactly what was produced and what remains to be applied or checked. Respect a stricter output contract from the main task.
````
<!-- prompt:end -->

## Usage notes

This is a modifier: append it to a concrete prompt only when their scopes and output contracts agree.

## Related entries

- [Exact Output Format](exact-output-format.md) — Use when you need the agent to return exactly the requested format with no extra commentary.
- [Verify Before Returning](verify-before-returning.md) — Use when the agent should check its own work before returning it.

[Browse the catalog](../CATALOG.md) · [Usage guide](../docs/usage.md)
