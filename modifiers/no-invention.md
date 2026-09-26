---
id: "no-invention"
title: "No Invention"
type: "modifier"
primary_category: "coding"
categories: ["coding", "design"]
subcategory: "agent-quality"
when_to_use: "Use when the agent must not make up claims, prices, features, APIs, or behavior"
search_terms: ["no-invention", "coding", "agent-quality", "claims", "content-accuracy", "evidence", "invention", "no", "verified-facts"]
inputs: []
output: "The main task deliverable without unsupported factual or functional claims."
mode: "modify"
capabilities: []
related: ["research-before-deciding", "content-audit"]
aliases: ["coding/agent-quality/no-invention.md", "no-invention.md"]
---

# No Invention

Use when the agent must not make up claims, prices, features, APIs, or behavior.

**Type:** modifier · **Mode:** modify · **ID:** `no-invention`

**Expected output:** The main task deliverable without unsupported factual or functional claims.

## Inputs

No placeholders. Use this with a concrete main task.

## Modifier

Copy the block below, not the metadata or usage notes.

<!-- prompt:start -->
````text
Use only facts, features, prices, locations, services, APIs, settings, behaviors, and business details supplied by the user, supported by the inspected project, or verified through available evidence.

Inspect first when uncertain. Verify time-sensitive claims against relevant current primary sources when access is available. Distinguish a project-defined requirement from a confirmed real-world capability; stale project text is not independent proof.

Do not add unsupported marketing claims, guarantees, integrations, product specifications, pricing, credentials, testimonials, metrics, or functionality. Do not present inference as observation.

When evidence is missing, identify the uncertainty, keep the original fact unchanged where safe, or use the task's approved unavailable state. Explicitly labeled sample data is permitted only when the main task requests a demonstration; it must never look like real evidence.
````
<!-- prompt:end -->

## Usage notes

This is a modifier: append it to a concrete prompt only when their scopes and output contracts agree.

## Related entries

- [Research Before Deciding](../prompts/coding/agent-quality/research-before-deciding.md) — Use when the agent needs to compare options and make a practical recommendation.
- [Audit Website Copy](../prompts/content/editing/content-audit.md) — Find contextual, factual, repetitive, and misplaced website copy without rewriting the source.

[Browse the catalog](../CATALOG.md) · [Usage guide](../docs/usage.md)
