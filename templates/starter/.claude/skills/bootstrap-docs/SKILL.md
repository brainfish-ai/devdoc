---
name: bootstrap-docs
description: Analyze repository and generate documentation. Creates context memory for consistent AI assistance.
---

## Instructions

When bootstrapping documentation from a repository:

### Step 1: Check Context Memory

**First, check if `.devdoc/context.json` exists:**

**If context.json exists and is populated:**
- Read the context file
- Tell user: "Found existing product context. Using saved configuration."
- Skip to Step 4 (Generate Documentation)

**If context.json is empty or doesn't exist:**
- Proceed to Step 2 (Discovery Flow)

### Step 2: Discovery Flow (Context Creation)

#### 2a. Detect Project Structure

**If `docs.json` exists in current directory:**
- You're in a DevDoc docs folder
- Source code is likely in `../` (parent directory)

**If `package.json` and `src/` exist:**
- You're at repo root
- Create docs in `./docs/` subfolder

**If neither matches:**
- Ask user for the source code path

#### 2b. Auto-Discover Information

Scan the repository and extract:

```
From README.md:
- Product name
- Description
- Key features

From package.json / pyproject.toml / Cargo.toml:
- Primary language
- Framework (from dependencies)
- Project type (library, cli, api, etc.)

From OpenAPI spec (if exists):
- API style: REST
- Base URL
- Authentication type
- Common patterns

From GraphQL schema (if exists):
- API style: GraphQL
- Schema patterns

From source code structure:
- Key directories
- Naming conventions
```

#### 2c. Ask Key Questions

After auto-discovery, ask the user to confirm/provide:

**Question 1: Documentation Type**
"What type of documentation are you creating?
1. **internal** - For your team: setup guides, architecture, contribution guidelines
2. **api** - For developers using your product: API reference, SDKs, integration guides  
3. **product** - For end users: feature guides, tutorials, FAQs"

**Question 2: Target Audience**
"Who is your primary audience?
(e.g., 'Backend developers integrating our payment API', 'Internal engineering team', 'Non-technical business users')"

**Question 3: Terminology (optional)**
"Any specific terminology I should know? For example:
- Brand names with specific capitalization
- Terms to avoid or prefer
- Domain-specific vocabulary

(Press Enter to skip)"

**Question 4: Code Examples**
"What language should I use for code examples?
(e.g., TypeScript, Python, curl)"

#### 2d. Create Context Memory

Create `.devdoc/` folder and `context.json` with discovered + user info:

```json
{
  "$schema": "https://devdoc.sh/schemas/context.json",
  "version": "1.0",
  "lastUpdated": "2026-01-24T10:30:00Z",
  "product": {
    "name": "[from README/package.json]",
    "description": "[from README]",
    "type": "[api/sdk/platform/cli/library]",
    "domain": "[inferred or asked]",
    "targetAudience": "[from Question 2]",
    "keyFeatures": ["[from README]"]
  },
  "terminology": {
    "glossary": {},
    "avoidTerms": [],
    "brandNames": {}
  },
  "api": {
    "style": "[REST/GraphQL/etc if detected]",
    "baseUrl": "[from OpenAPI if found]",
    "authentication": {
      "type": "[from OpenAPI if found]",
      "headerName": "",
      "description": ""
    }
  },
  "codebase": {
    "language": "[from package.json]",
    "framework": "[from dependencies]",
    "sourceLocation": "../"
  },
  "documentation": {
    "voice": "[based on docType]",
    "perspective": "second_person",
    "codeExamples": {
      "primaryLanguage": "[from Question 4]",
      "additionalLanguages": []
    },
    "templates": {
      "guide": ".devdoc/templates/guide.md",
      "apiReference": ".devdoc/templates/api-reference.md",
      "tutorial": ".devdoc/templates/tutorial.md",
      "quickstart": ".devdoc/templates/quickstart.md",
      "troubleshooting": ".devdoc/templates/troubleshooting.md"
    }
  },
  "learned": {
    "insights": [],
    "corrections": []
  }
}
```

Also copy template files to `.devdoc/templates/` if they don't exist.

Tell user: 
"Created product context in `.devdoc/context.json`
- Product: {name}
- Type: {docType}
- Audience: {targetAudience}
- Code examples: {primaryLanguage}

This context will be used for consistent documentation generation."

### Step 3: Update docs.json with docType

**Read existing `docs.json` or create new one.**

Add the `docType` field:

```json
{
  "name": "Project Name",
  "docType": "api",  // from Question 1
  "navigation": { ... }
}
```

Tell user: "Saved docType: {type} to docs.json"

### Step 4: Generate Documentation

**Read context from `.devdoc/context.json` before generating.**

**Read the appropriate template** from `.devdoc/templates/` for each page type:
- For guides: read `.devdoc/templates/guide.md`
- For API reference: read `.devdoc/templates/api-reference.md`
- For quickstart: read `.devdoc/templates/quickstart.md`
- For tutorials: read `.devdoc/templates/tutorial.md`

**Apply context throughout:**
- Use correct product name from `product.name`
- Use terminology from `terminology.glossary`
- Avoid terms from `terminology.avoidTerms`
- Use code language from `documentation.codeExamples.primaryLanguage`
- Match voice from `documentation.voice`

---

## docType: "internal"

For internal team documentation, create:

```
docs/
├── .devdoc/
│   ├── context.json
│   └── templates/
├── docs.json
├── index.mdx              # Project overview
├── getting-started/
│   ├── setup.mdx          # Dev environment setup
│   ├── prerequisites.mdx  # Required tools/versions
│   └── first-contribution.mdx
├── architecture/
│   ├── overview.mdx       # System architecture
│   ├── folder-structure.mdx
│   └── decisions.mdx      # ADRs, design decisions
├── development/
│   ├── workflow.mdx       # Git workflow, PR process
│   ├── testing.mdx        # How to run/write tests
│   ├── debugging.mdx      # Common issues, debugging tips
│   └── deployment.mdx     # How to deploy
├── api/                   # Internal API docs (if applicable)
│   └── ...
└── contributing.mdx       # Contribution guidelines
```

**Content focus:**
- How to set up local development
- Codebase architecture and patterns
- Internal APIs and services
- Debugging and troubleshooting
- Team conventions and standards

**Voice:** Technical, direct, assumes familiarity with codebase

---

## docType: "api"

For external developers using your API/SDK, create:

```
docs/
├── .devdoc/
│   ├── context.json
│   └── templates/
├── docs.json
├── index.mdx              # Product intro, value prop
├── quickstart.mdx         # 5-minute getting started
├── authentication.mdx     # Auth setup (API keys, OAuth)
├── guides/
│   ├── overview.mdx       # Concepts overview
│   └── {use-case}.mdx     # Common use case tutorials
├── api-reference/
│   ├── introduction.mdx   # API overview, base URL, versioning
│   ├── authentication.mdx # Auth details
│   ├── errors.mdx         # Error codes and handling
│   └── openapi.json       # Full API spec
├── sdks/                  # If SDKs exist
│   ├── javascript.mdx
│   ├── python.mdx
│   └── ...
├── webhooks.mdx           # If webhooks exist
└── changelog.mdx          # API changelog
```

**Content focus:**
- Quick time-to-first-API-call
- Authentication and authorization
- API reference with examples
- SDKs and client libraries
- Error handling and troubleshooting
- Rate limits and best practices

**Voice:** Professional, helpful, code-focused

---

## docType: "product"

For end users of your product, create:

```
docs/
├── .devdoc/
│   ├── context.json
│   └── templates/
├── docs.json
├── index.mdx              # Product overview
├── getting-started/
│   ├── quickstart.mdx     # First steps
│   ├── account-setup.mdx  # Account creation, onboarding
│   └── key-concepts.mdx   # Core concepts explained
├── features/
│   ├── {feature-1}.mdx    # Feature guides
│   ├── {feature-2}.mdx
│   └── ...
├── tutorials/
│   ├── {workflow-1}.mdx   # Step-by-step tutorials
│   └── ...
├── integrations/          # If integrations exist
│   └── ...
├── troubleshooting/
│   ├── common-issues.mdx
│   └── faq.mdx
└── release-notes.mdx      # What's new
```

**Content focus:**
- Non-technical language (minimal code)
- Screenshots and visual guides
- Step-by-step tutorials
- Use case focused
- FAQs and troubleshooting
- Feature explanations

**Voice:** Friendly, supportive, non-technical

---

## docs.json Templates (with docType)

### Internal Docs
```json
{
  "name": "{Project Name}",
  "docType": "internal",
  "navigation": {
    "tabs": [
      {
        "tab": "Documentation",
        "groups": [
          { "group": "Getting Started", "pages": ["index", "getting-started/setup", "getting-started/prerequisites"] },
          { "group": "Architecture", "pages": ["architecture/overview", "architecture/folder-structure"] },
          { "group": "Development", "pages": ["development/workflow", "development/testing", "development/deployment"] },
          { "group": "Contributing", "pages": ["contributing"] }
        ]
      }
    ]
  }
}
```

### Customer API Docs
```json
{
  "name": "{Product Name}",
  "docType": "api",
  "navigation": {
    "tabs": [
      {
        "tab": "Guides",
        "groups": [
          { "group": "Getting Started", "pages": ["index", "quickstart", "authentication"] },
          { "group": "Guides", "pages": ["guides/overview"] }
        ]
      },
      {
        "tab": "API Reference",
        "type": "openapi",
        "spec": "api-reference/openapi.json"
      }
    ]
  }
}
```

### Product Docs
```json
{
  "name": "{Product Name}",
  "docType": "product",
  "navigation": {
    "tabs": [
      {
        "tab": "Documentation",
        "groups": [
          { "group": "Getting Started", "pages": ["index", "getting-started/quickstart", "getting-started/key-concepts"] },
          { "group": "Features", "pages": ["features/..."] },
          { "group": "Tutorials", "pages": ["tutorials/..."] },
          { "group": "Help", "pages": ["troubleshooting/common-issues", "troubleshooting/faq"] }
        ]
      }
    ]
  }
}
```

## Quality Guidelines

- Extract real code examples from source, don't fabricate
- Match tone to audience based on docType
- Add TODO markers for sections needing human review
- Include relevant screenshots for product docs
- Test all code examples work
- Always use terminology from context.json
- Update context.json if you learn new information
