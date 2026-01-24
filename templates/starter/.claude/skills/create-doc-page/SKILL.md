---
name: create-doc-page
description: Create a new DevDoc MDX documentation page with proper structure and components
---

## Instructions

When creating a new documentation page:

1. Ask for the page topic and type (guide, reference, tutorial)
2. Generate MDX with:
   - Proper frontmatter (title, description)
   - Clear introduction paragraph
   - Structured sections with H2/H3
   - Appropriate components (Steps, Cards, Callouts)
   - Navigation cards at the bottom

## Template Structure

```mdx
---
title: "{Title}"
description: "{Description}"
---

{Introduction paragraph explaining the topic}

## {Section 1}

{Content with appropriate components}

## {Section 2}

{More content}

## Next Steps

<CardGroup cols={2}>
  <Card title="Related Topic" icon="icon-name" href="/path">
    Brief description
  </Card>
</CardGroup>
```

## Component Usage Guidelines

- Use `<Steps>` for procedural content
- Use `<CardGroup>` for navigation/feature highlights
- Use `<Tip>` for helpful hints
- Use `<Warning>` for important cautions
- Use `<Note>` for additional context
- Use `<Accordion>` for optional/advanced details

## After Creating

1. Add the new page to `docs.json` navigation
2. Link to the page from related documentation
