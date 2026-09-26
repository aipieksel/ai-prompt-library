---
id: "smart-agent-logic"
title: "Smart Agent Logic"
type: "prompt"
primary_category: "coding"
categories: ["coding"]
subcategory: "code-quality"
when_to_use: "Use when the agent must build rules, scoring, matching, defaults, or automated behavior"
search_terms: ["smart-agent-logic", "coding", "code-quality", "agent", "automation", "edge-cases", "fallbacks", "logic", "rules", "smart"]
inputs: ["REQUIREMENT", "PROJECT_CONTEXT"]
output: "A testable rule definition, implementation, and verification results."
mode: "edit"
capabilities: ["file-access", "code-execution"]
related: ["codebase-first-implementation", "no-invention"]
aliases: ["coding/code-quality/smart-agent-logic.md", "smart-agent-logic.md"]
---

# Smart Agent Logic

Use when the agent must build rules, scoring, matching, defaults, or automated behavior.

**Type:** prompt · **Mode:** edit · **ID:** `smart-agent-logic`

**Expected output:** A testable rule definition, implementation, and verification results.

## Inputs

Replace every listed placeholder. For an optional source, enter `None` when it is unavailable.

| Placeholder | What to provide | Example |
| --- | --- | --- |
| `{{REQUIREMENT}}` | The automation or decision behavior to implement. | Match imported records to existing customers without duplicates. |
| `{{PROJECT_CONTEXT}}` | Existing rules, relevant files, sample inputs, and expected outputs. | Matching module, fixture records, and approved exact-match precedence. |

## Prompt

Copy the block below, not the metadata or usage notes.

<!-- prompt:start -->
````text
Logic requirement:
{{REQUIREMENT}}

Project context, representative inputs, and expected outputs:
{{PROJECT_CONTEXT}}

Design and implement predictable rules, scoring, matching, defaults, or automation for this requirement.

Before coding, define valid inputs, decision rules, priority and tie-breaking behavior, scoring where applicable, compatibility checks, missing/invalid/ambiguous-input handling, safe defaults, fallback behavior, and failure states. Use concrete input/output cases to make the intended behavior testable.

Do not invent arbitrary weights, thresholds, or product behavior as though they were approved requirements. Reuse project-defined rules; label proposed defaults and explain the effect of unresolved decisions.

Implement within existing architecture. Include representative normal, boundary, invalid, and failure cases in the available tests. Keep defaults understandable for non-technical users, and make failures visible and recoverable rather than random or silent.

Return the rule summary, exact implementation, tests run, and remaining uncertainties.
````
<!-- prompt:end -->

## Usage notes

Supply the actual referenced material. A filename or URL does not grant the assistant file, browser, account, or edit access.

**Relevant capabilities:** `file-access`, `code-execution`. These are requirements or conditional needs, not tools installed by this file.

## Related entries

- [Codebase-First Implementation](../codebase-alignment/codebase-first-implementation.md) — Use as a single strong prompt before coding tasks.
- [No Invention](../../../modifiers/no-invention.md) — Use when the agent must not make up claims, prices, features, APIs, or behavior.

[Browse the catalog](../../../CATALOG.md) · [Usage guide](../../../docs/usage.md)
