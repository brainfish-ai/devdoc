---
name: generate-api-docs
description: Generate API documentation pages from OpenAPI spec or code
---

## Instructions

1. Analyze the OpenAPI spec or API code
2. Create documentation pages for:
   - Introduction/Overview
   - Authentication guide
   - Error handling
   - Rate limiting (if applicable)
3. Update docs.json to include API reference tab

## OpenAPI Tab Configuration

```json
{
  "tab": "API Reference",
  "type": "openapi",
  "path": "/api-reference",
  "spec": "api-reference/openapi.json",
  "groups": [
    {
      "group": "Overview",
      "pages": ["api-reference/introduction", "api-reference/authentication"]
    }
  ]
}
```

## GraphQL Tab Configuration

```json
{
  "tab": "GraphQL API",
  "type": "graphql",
  "path": "/graphql-api",
  "schema": "api-reference/schema.graphql",
  "endpoint": "https://api.example.com/graphql"
}
```

## Generated Pages

### api-reference/introduction.mdx
```mdx
---
title: "API Introduction"
description: "Overview of the API"
---

Brief overview of the API capabilities.

## Base URL

\`\`\`
https://api.example.com/v1
\`\`\`

## Authentication

All requests require authentication. See [Authentication](/api-reference/authentication).
```

### api-reference/authentication.mdx
```mdx
---
title: "Authentication"
description: "How to authenticate API requests"
---

<Tabs>
  <Tab title="Bearer Token">
    Include the token in the Authorization header:
    \`\`\`bash
    curl -H "Authorization: Bearer YOUR_TOKEN" https://api.example.com/v1/users
    \`\`\`
  </Tab>
  <Tab title="API Key">
    Include the API key in the header:
    \`\`\`bash
    curl -H "X-API-Key: YOUR_KEY" https://api.example.com/v1/users
    \`\`\`
  </Tab>
</Tabs>
```

## After Generating

1. Review and customize the generated content
2. Add real examples from your API
3. Update authentication details
