---
name: bootstrap-docs
description: Analyze repository and generate complete initial documentation structure
---

## Instructions

When bootstrapping documentation from a repository:

### Step 1: Analyze Repository Structure

Scan and identify:
- `README.md` - Project overview, installation, usage
- `package.json` / `Cargo.toml` / `pyproject.toml` - Dependencies, scripts, metadata
- `src/` or `lib/` - Main source code structure
- `api/` or `routes/` - API endpoints (REST, GraphQL)
- `components/` - UI components (React, Vue, etc.)
- `docs/` - Existing documentation
- `.env.example` - Environment variables
- `docker-compose.yml` / `Dockerfile` - Deployment info
- `openapi.json` / `swagger.yaml` - API specifications
- `schema.graphql` - GraphQL schemas

### Step 2: Generate Documentation Structure

Create the following based on what's found:

```
docs/
├── docs.json              # Navigation config
├── index.mdx              # Homepage (from README)
├── quickstart.mdx         # Getting started guide
├── installation.mdx       # Installation instructions
├── configuration.mdx      # Environment/config setup
├── guides/
│   ├── overview.mdx       # Architecture overview
│   └── {feature}.mdx      # Feature-specific guides
├── api-reference/
│   ├── introduction.mdx   # API overview
│   ├── authentication.mdx # Auth guide
│   └── openapi.json       # (if found/generated)
├── components/            # (if UI library)
│   └── {component}.mdx
└── deployment.mdx         # Deployment guide
```

### Step 3: Content Generation

For each page, generate:
1. Frontmatter with title and description
2. Clear introduction explaining the topic
3. Code examples extracted from source
4. Links to related documentation

### Step 4: Generate docs.json

Create navigation structure:
```json
{
  "name": "{Project Name from package.json}",
  "navigation": {
    "tabs": [
      {
        "tab": "Guides",
        "type": "docs",
        "groups": [
          {
            "group": "Getting Started",
            "pages": ["index", "quickstart", "installation"]
          },
          {
            "group": "Guides",
            "pages": ["guides/overview"]
          }
        ]
      }
    ]
  }
}
```

## What to Extract from Source Code

| Source | Documentation Generated |
|--------|------------------------|
| README.md | Homepage content, project overview |
| package.json scripts | CLI commands, development workflow |
| Exported functions | API reference pages |
| React components | Component documentation with props |
| API routes | Endpoint reference |
| OpenAPI spec | Full API documentation |
| GraphQL schema | GraphQL type documentation |
| Config files | Configuration reference |
| Tests | Usage examples |

## Output Quality Guidelines

- Extract real code examples, don't fabricate
- Preserve existing documentation where found
- Note areas that need human review with TODOs
- Generate SEO-friendly descriptions
- Include installation commands from package manager
