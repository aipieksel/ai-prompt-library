---
id: "example-task"
title: "Example Task"
type: "prompt"
primary_category: "coding"
categories: ["coding"]
subcategory: "agent-quality"
when_to_use: "Describe the distinct situation and desired outcome"
search_terms: ["example", "task"]
inputs: ["TASK", "SOURCE_CONTEXT"]
output: "Describe the concrete deliverable and any blocking-input behavior"
mode: "edit"
capabilities: ["file-access"]
related: []
aliases: []
---

# Example Task

Replace this example with the actual purpose and boundaries. Copy the finished file into the canonical folder matching its metadata; this template is not itself a catalog entry.

**Expected output:** A concrete, reviewable deliverable.

## Inputs

| Placeholder | What to provide | Example |
| --- | --- | --- |
| `{{TASK}}` | The exact authorized operation. | Fix the specified validation error. |
| `{{SOURCE_CONTEXT}}` | Actual source, constraints, and expected behavior. | Component file and relevant tests. |

## Prompt

<!-- prompt:start -->
````text
Task:
{{TASK}}

Source and constraints:
{{SOURCE_CONTEXT}}

Inspect the supplied source before changing it. Implement only the authorized task, preserving unrelated content, structure, and working behavior.

Return the complete deliverable required by the task. Verify the affected path with available tools, and distinguish performed checks from unverified assumptions. Report a blocking missing input rather than inventing it.
````
<!-- prompt:end -->

## Usage notes

Replace generic instructions with the task's concrete source hierarchy, requirements, examples, and output contract. Keep essential instructions inside the copyable block.

[Format specification](../docs/prompt-format.md) · [Contribution guide](../CONTRIBUTING.md)
