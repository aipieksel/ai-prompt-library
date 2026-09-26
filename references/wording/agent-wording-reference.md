---
id: "agent-wording-reference"
title: "Agent Wording Reference"
type: "reference"
primary_category: "coding"
categories: ["coding", "design"]
subcategory: "agent-quality"
when_to_use: "Use as a compact reference for common instruction wording"
search_terms: ["agent-wording-reference", "coding", "agent-quality", "agent", "agent-instructions", "phrases", "quality", "reference", "wording"]
inputs: []
output: "Selected wording to add to a concrete task; no standalone deliverable."
mode: "reference"
capabilities: []
related: ["preserve-existing-system", "fundamental-visual-redesign", "minimal-scope-change"]
aliases: ["coding/agent-quality/agent-wording-reference.md", "agent-wording-reference.md"]
---

# Agent Wording Reference

Use as a compact reference for common instruction wording.

**Type:** reference · **Mode:** reference · **ID:** `agent-wording-reference`

**Expected output:** Selected wording to add to a concrete task; no standalone deliverable.

**Not for:** Running the entire collection as a single prompt.

## Inputs

No placeholders. Select the wording relevant to the authorized task.

## Reference

Copy the block below, not the metadata or usage notes.

<!-- prompt:start -->
````text
Choose the line that describes the authorized change; do not paste this entire menu as one instruction.

Preserving a layout and replacing its architecture are different tasks. Likewise, full-file output and a minimal patch are alternatives. Keep required content and behavior unless the main brief explicitly authorizes changing them.

## Rigorous work
Be rigorous and deliberate. Inspect the task closely, reason through the edge cases, verify assumptions against the actual files or evidence, and review the result against the requirements, and report remaining uncertainty or unverified behavior instead of claiming perfection.

## Fundamental redesign
Create a fundamental redesign, not a visual refresh. Treat the current design as a content reference only, not as a layout to preserve. Replace the page from first principles while keeping only required content, brand constraints, and functionality.

## Alternative visual metaphor
Create a different visual metaphor that communicates the same idea without reusing the same layout, shapes, glow, labels, or component arrangement.

## Preserve existing system
Make the smallest correct change. Preserve the existing structure, logic, styling, and behavior.

## Implementation-ready output
Return the exact implementation, ready to paste or apply.

## Verify before returning
Inspect, change, test, and report what was verified.

## No invention
Use only verified project facts. Do not invent features, claims, prices, or behavior.

## Tight scope
Fix only the requested issue. Do not change unrelated code, styling, or behavior.

## Exact output format
Return only the requested output, exactly in the requested format, with no extras.

## Best default instruction
Be rigorous and deliberate. Inspect the actual files, preserve the existing system, label assumptions and resolve material uncertainty, make the smallest correct change, verify the result, and return only the final implementation-ready output in the exact format requested.
````
<!-- prompt:end -->

## Usage notes

Select compatible excerpts. Verification language requires actual evidence, not a guarantee of correctness.

## Related entries

- [Preserve Existing System](../../modifiers/preserve-existing-system.md) — Use when the agent must fix or improve something without changing the surrounding system.
- [Fundamental Visual Redesign](../../prompts/design/redesign/fundamental-visual-redesign.md) — Use when the agent keeps changing colors or spacing but the design still looks the same.
- [Minimal Scope Change](../../modifiers/minimal-scope-change.md) — Use when the agent keeps changing unrelated code, styling, or behavior.

[Browse the catalog](../../CATALOG.md) · [Usage guide](../../docs/usage.md)
