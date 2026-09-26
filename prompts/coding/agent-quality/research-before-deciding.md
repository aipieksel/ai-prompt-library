---
id: "research-before-deciding"
title: "Research Before Deciding"
type: "prompt"
primary_category: "coding"
categories: ["coding", "design"]
subcategory: "agent-quality"
when_to_use: "Use when the agent needs to compare options and make a practical recommendation"
search_terms: ["research-before-deciding", "coding", "agent-quality", "comparison", "current-evidence", "deciding", "decision-making", "recommendation", "research"]
inputs: ["DECISION", "CONSTRAINTS"]
output: "An evidence-backed comparison, recommendation, trade-offs, and implementation path."
mode: "research"
capabilities: ["research"]
related: ["no-invention", "integration-design-outline"]
aliases: ["coding/agent-quality/research-before-deciding.md", "research-before-deciding.md"]
---

# Research Before Deciding

Use when the agent needs to compare options and make a practical recommendation.

**Type:** prompt · **Mode:** research · **ID:** `research-before-deciding`

**Expected output:** An evidence-backed comparison, recommendation, trade-offs, and implementation path.

## Inputs

Replace every listed placeholder. For an optional source, enter `None` when it is unavailable.

| Placeholder | What to provide | Example |
| --- | --- | --- |
| `{{DECISION}}` | The choice or question that needs a recommendation. | Choose a queue strategy for the existing import pipeline. |
| `{{CONSTRAINTS}}` | Relevant requirements, existing stack, costs, and evidence. | Existing database, expected job volume, retry needs, and deployment constraints. |

## Prompt

Copy the block below, not the metadata or usage notes.

<!-- prompt:start -->
````text
Decision:
{{DECISION}}

Project requirements and constraints:
{{CONSTRAINTS}}

Research before recommending an option. Inspect relevant project evidence, available alternatives, and current primary documentation for material claims.

Compare options against the actual constraints: required capabilities, compatibility, implementation effort, maintenance, risks, and any specified budget or operating limits. State the evidence, its date where time-sensitive, and uncertainty. Do not invent benchmarks or rely on preference alone.

Recommend one practical option, explain why it fits better than the credible alternatives, and give a clear implementation path. Separate verified facts from inferences and identify the conditions that would change the recommendation.

If source access is unavailable, produce a clearly labeled provisional comparison from the supplied evidence. Do not claim current verification.
````
<!-- prompt:end -->

## Usage notes

Supply the actual referenced material. A filename or URL does not grant the assistant file, browser, account, or edit access.

**Relevant capabilities:** `research`. These are requirements or conditional needs, not tools installed by this file.

## Related entries

- [No Invention](../../../modifiers/no-invention.md) — Use when the agent must not make up claims, prices, features, APIs, or behavior.
- [Plan a Business Integration](../../business/integration-planning/integration-design-outline.md) — Turn a business idea into a stakeholder-ready integration design and phased build plan, without writing code.

[Browse the catalog](../../../CATALOG.md) · [Usage guide](../../../docs/usage.md)
