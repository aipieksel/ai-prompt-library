---
id: "integration-design-outline"
title: "Plan a Business Integration"
type: "prompt"
primary_category: "business"
categories: ["business"]
subcategory: "integration-planning"
when_to_use: "Turn a business idea into a stakeholder-ready integration design and phased build plan, without writing code"
search_terms: ["integration-design-outline", "business", "integration-planning", "business-plan", "automation", "webhooks", "sync", "integration"]
inputs: ["BUSINESS_BRIEF"]
output: "One stakeholder-ready integration-design Markdown file with a tailored ASCII diagram."
mode: "plan"
capabilities: ["file-access"]
related: ["research-before-deciding", "smart-agent-logic"]
aliases: ["business/business-plan.prompt.md", "business-plan.prompt.md", "business-plan"]
---

# Plan a Business Integration

Turn a business idea into a stakeholder-ready integration design and phased build plan, without writing code.

**Type:** prompt · **Mode:** plan · **ID:** `integration-design-outline`

**Expected output:** One stakeholder-ready integration-design Markdown file with a tailored ASCII diagram.

## Inputs

Replace every listed placeholder. For an optional source, enter `None` when it is unavailable.

| Placeholder | What to provide | Example |
| --- | --- | --- |
| `{{BUSINESS_BRIEF}}` | Markdown business idea, goals, systems, and known constraints. | Sync approved store orders to the accounting system and return invoice status. |

## Prompt

Copy the block below, not the metadata or usage notes.

<!-- prompt:start -->
````text
Business idea and goals:
{{BUSINESS_BRIEF}}

Create a high-level integration design outline for stakeholder approval. Do not write implementation code. Identify the source and target systems from the brief rather than assuming a particular platform.

Produce these sections:

### 1. Business idea and goals
Identify the systems, users, domain objects, and purpose. Relevant objects may include orders, customers, products, invoices, tickets, or tasks. Separate stated requirements from assumptions or proposed additions.

### 2. Practical setup
Describe the appropriate environment: a CMS plugin, middleware service, standalone application, or another justified arrangement. Explain outbound hooks/webhooks, inbound endpoints or queues, authentication such as OAuth or API keys, object mapping, and a queue/retry mechanism that prevents failed synchronization from blocking normal operations.

### 3. Typical data flow
Walk through a primary create/update event in the source system. Map it to the target objects, such as a contact plus invoice or a ticket plus customer. Include optional modules only where the brief warrants them. Explain how target updates return through webhooks or scheduled pulls and how external IDs link records.

### 4. Objects to synchronize
List the relevant entities and metadata, including statuses, lead sources, tags, currencies, tax rates, custom fields, and other domain-specific mapping needs. Do not add irrelevant object families merely to fill the list.

### 5. Key implementation decisions
Specify the proposed object mappings, ownership/source of truth for shared fields, synchronization direction, real-time versus scheduled behavior, duplicate handling, and partial-failure recovery. Identify decisions that require stakeholder confirmation.

### 6. Edge cases
Address relevant cases such as guest versus registered users, product variants/SKUs, discounts, multiple currencies, tax rules, refunds, adjustments, subscription renewals, historical backfills, API limits, and token refresh. Explain conflicts and failed or repeated deliveries rather than assuming ideal event ordering.

### 7. Recommended architecture
Define each system's role, mapping registry, external-ID storage, authentication, webhook validation, and sync logging. Include configuration/admin features such as credentials setup, field mapping, logs, and manual re-sync when appropriate. Do not include real credentials in the document. Verify uncertain platform capabilities from current official documentation when available; otherwise identify the dependency.

### 8. Phased build plan
Propose a rollout suited to the idea's complexity: for example, one-way synchronization of basic objects, then required two-way flows or extended objects, then advanced administration. Basic validation, safe retries, and essential logging belong with the first operational phase rather than being deferred until after reliability is needed.

### 9. Architecture diagram
Draw one ASCII diagram tailored to the actual systems and components. Use boxes, arrows, and labels to show source modules, processing/mapping, queues, APIs, target modules, and relevant admin interfaces. Do not return a generic example diagram or code implementation.

### 10. Delivery
Save the complete outline and diagram as one descriptively named Markdown file, such as integration-design.md. Use clear headings and appropriate lists, with a professional client-facing tone. Ensure the diagram, flow, entity list, and phased plan agree.

Return the completed Markdown file. If file creation is unavailable, return its full contents with the intended filename, without claiming a downloadable file was created.
````
<!-- prompt:end -->

## Usage notes

Supply the actual referenced material. A filename or URL does not grant the assistant file, browser, account, or edit access.

**Relevant capabilities:** `file-access`. These are requirements or conditional needs, not tools installed by this file.

## Related entries

- [Research Before Deciding](../../coding/agent-quality/research-before-deciding.md) — Use when the agent needs to compare options and make a practical recommendation.
- [Smart Agent Logic](../../coding/code-quality/smart-agent-logic.md) — Use when the agent must build rules, scoring, matching, defaults, or automated behavior.

[Browse the catalog](../../../CATALOG.md) · [Usage guide](../../../docs/usage.md)
