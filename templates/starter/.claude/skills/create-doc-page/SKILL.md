---
name: create-doc-page
description: Create a new documentation page. Reads context memory for consistency.
---

## Instructions

When creating a new documentation page:

### Step 0: Read Context Memory

**First, read `.devdoc/context.json` if it exists:**

```json
{
  "product": { "name": "...", "targetAudience": "..." },
  "terminology": { "glossary": {}, "avoidTerms": [] },
  "documentation": { 
    "voice": "...", 
    "codeExamples": { "primaryLanguage": "..." },
    "templates": { "guide": ".devdoc/templates/guide.md", ... }
  }
}
```

**Apply context throughout page creation:**
- Use `product.name` for product references
- Use terminology from `terminology.glossary`
- Avoid terms from `terminology.avoidTerms`
- Match `documentation.voice` for writing style
- Use `documentation.codeExamples.primaryLanguage` for code blocks

### Step 1: Get Documentation Type

**Read `docs.json` for `docType` field:**
```json
{ "docType": "api" }  // "internal" | "api" | "product"
```

If set, use it automatically. If not set, ask user and save their choice to docs.json.

### Step 2: Gather Requirements

Ask the user:

1. **What is this page about?** (topic/title)

2. **What kind of page?**
   - Guide/Overview - Explains concepts
   - Tutorial - Step-by-step walkthrough
   - Reference - Technical specifications
   - Troubleshooting - Problem/solution format

### Step 3: Read Appropriate Template

**Based on page type, read the template from `.devdoc/templates/`:**

| Page Type | Template File |
|-----------|---------------|
| Guide/Overview | `.devdoc/templates/guide.md` |
| Tutorial | `.devdoc/templates/tutorial.md` |
| API Reference | `.devdoc/templates/api-reference.md` |
| Quickstart | `.devdoc/templates/quickstart.md` |
| Troubleshooting | `.devdoc/templates/troubleshooting.md` |

Read the template file and follow its structure and guidelines.

### Step 4: Generate Page

---

## Internal/Developer Docs (docType: "internal")

**Voice:** Technical, direct (from context or default)

### Setup/Configuration Page
```mdx
---
title: "{Feature} Setup"
description: "How to configure {feature} for local development"
---

This guide covers setting up {feature} in your local development environment.

## Prerequisites

- Node.js 18+
- Docker (optional)
- Access to {internal resource}

## Installation

<Steps>
  <Step title="Install dependencies">
    ```{primaryLanguage}
    npm install
    ```
  </Step>
  <Step title="Configure environment">
    Copy `.env.example` to `.env` and set:
    ```bash
    FEATURE_API_KEY=your-key
    ```
  </Step>
</Steps>

## Configuration Options

| Variable | Description | Default |
|----------|-------------|---------|
| `OPTION_1` | Description | `value` |

## Troubleshooting

<Accordion title="Common issue">
Solution here
</Accordion>
```

### Architecture Page
```mdx
---
title: "{System} Architecture"
description: "Technical overview of {system} design and components"
---

Overview of how {system} is architected.

## High-Level Design

{Diagram or description}

## Components

### Component A
{Description, responsibilities}

### Component B
{Description, responsibilities}

## Data Flow

<Steps>
  <Step title="Step 1">Request comes in...</Step>
  <Step title="Step 2">Processing...</Step>
</Steps>

## Design Decisions

<Note>
We chose X over Y because...
</Note>
```

---

## Customer API Docs (docType: "api")

**Voice:** Professional, helpful (from context or default)

### API Guide Page
```mdx
---
title: "{Feature} Guide"
description: "Learn how to {action} using the {product.name} API"
---

This guide shows you how to {action} using the {product.name} API.

## Prerequisites

- A {product.name} account ([sign up](https://...))
- An API key ([get one here](/authentication))

## Quick Example

```{primaryLanguage}
import { Client } from '{package}';

const client = new Client({ apiKey: 'your-key' });
const result = await client.feature.action();
```

## Step-by-Step

<Steps>
  <Step title="Initialize the client">
    ```{primaryLanguage}
    const client = new Client({ apiKey: process.env.API_KEY });
    ```
  </Step>
  <Step title="Make your first request">
    ```{primaryLanguage}
    const response = await client.feature.action({ param: 'value' });
    ```
  </Step>
</Steps>

## Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `param` | string | Yes | Description |

## Response

```json
{
  "id": "123",
  "status": "success"
}
```

## Error Handling

<Warning>
Always wrap API calls in try/catch blocks.
</Warning>

```{primaryLanguage}
try {
  const result = await client.feature.action();
} catch (error) {
  if (error.code === 'RATE_LIMITED') {
    // Handle rate limiting
  }
}
```

## Next Steps

<CardGroup cols={2}>
  <Card title="API Reference" icon="code" href="/api-reference">
    Full API documentation
  </Card>
  <Card title="Examples" icon="github-logo" href="/examples">
    See more examples
  </Card>
</CardGroup>
```

---

## Product/User Docs (docType: "product")

**Voice:** Friendly, supportive (from context or default)

### Feature Guide Page
```mdx
---
title: "{Feature Name}"
description: "Learn how to use {feature} in {product.name}"
---

{Feature} helps you {benefit}. This guide walks you through everything you need to know.

## Overview

{Screenshot or visual}

{Brief explanation of what the feature does}

## Getting Started

<Steps>
  <Step title="Navigate to {Feature}">
    Click on **Settings** → **{Feature}** in the sidebar.
  </Step>
  <Step title="Configure your preferences">
    Select your preferred options...
  </Step>
</Steps>

## Key Features

<CardGroup cols={2}>
  <Card title="Feature A" icon="star">
    Description of capability
  </Card>
  <Card title="Feature B" icon="lightning">
    Description of capability
  </Card>
</CardGroup>

## Tips & Best Practices

<Tip>
Pro tip for getting the most out of this feature.
</Tip>

## Frequently Asked Questions

<AccordionGroup>
  <Accordion title="How do I...?">
    Answer here
  </Accordion>
  <Accordion title="Can I...?">
    Answer here
  </Accordion>
</AccordionGroup>

## Need Help?

<Card title="Contact Support" icon="chat-circle" href="/support">
  Reach out to our support team
</Card>
```

---

## After Creating

1. Add the new page to `docs.json` navigation
2. Link to the page from related documentation
3. Verify all code examples work
4. Ensure terminology matches context.json glossary
