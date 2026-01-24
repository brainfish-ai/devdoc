---
name: create-doc
description: Create new documentation pages interactively. Analyzes codebase and guides you through the process.
---

## Instructions

When user wants to create documentation:

### Step 0: Read Context Memory

**First, read `.devdoc/context.json` if it exists:**
- Use `product.name` for product references
- Apply `terminology.glossary` for correct terms
- Use `documentation.codeExamples.primaryLanguage` for code
- Read templates from `documentation.templates`

### Step 1: Understand What to Create

Ask the user:

"What would you like to document?

1. **A specific feature or concept** - I'll create a guide/tutorial
2. **Code files or functions** - Point me to the code, I'll generate docs
3. **API endpoints** - I'll analyze your API and create reference docs
4. **Something else** - Describe what you need"

### Step 2: Gather Information

Based on their choice:

#### For Feature/Concept:
- "What's the topic/title?"
- "What type of page?
  - Guide - Explains how to do something
  - Tutorial - Step-by-step walkthrough
  - Reference - Technical specifications
  - Troubleshooting - Problem/solution format"
- "Any specific sections you want included?"

#### For Code Documentation:
- "Which files or directories should I analyze?"
- "What should I focus on?
  - Public API/exports
  - Internal architecture
  - Usage examples
  - All of the above"
- Read the specified files
- Extract functions, classes, types, examples

#### For API Documentation:
- Check for existing OpenAPI/GraphQL specs
- If found: "I found `{spec}`. Should I generate docs from it?"
- If not: "Point me to your API routes/controllers"
- Extract endpoints, parameters, responses

#### For Other:
- Ask clarifying questions
- Understand the scope and purpose

### Step 3: Analyze Codebase (if applicable)

When documenting code:

```
Scan for:
- Function signatures and JSDoc/docstrings
- Type definitions and interfaces
- Usage examples in tests
- README sections about this feature
- Existing related documentation
```

Show user what you found:
"I found:
- 5 exported functions in `src/utils/`
- Type definitions in `types/index.ts`
- 3 test files with usage examples

Should I proceed with generating documentation for these?"

### Step 4: Choose Template

Read the appropriate template from `.devdoc/templates/`:

| Content Type | Template |
|--------------|----------|
| How-to guide | `guide.md` |
| Tutorial | `tutorial.md` |
| API endpoint | `api-reference.md` |
| Quick start | `quickstart.md` |
| FAQ/Issues | `troubleshooting.md` |

### Step 5: Generate Content

Create the documentation:

1. **Read the template** for structure guidance
2. **Apply context** (terminology, voice, language)
3. **Include mermaid diagrams** for flows/architecture
4. **Add real code examples** from codebase
5. **Use proper MDX components** (Steps, Cards, Tabs, etc.)

### Step 6: Propose File Location

Suggest where to save:

"I'll create this page at: `docs/guides/{topic}.mdx`

Does this location work, or would you prefer somewhere else?"

### Step 7: Create and Update Navigation

1. Write the MDX file
2. Ask: "Should I add this to the navigation in docs.json?"
3. If yes, update docs.json with the new page

### Step 8: Summary

"Created:
- `docs/guides/{topic}.mdx` - {description}
- Updated `docs.json` navigation

Preview with `npm run dev`

Want me to create another page or make changes to this one?"

---

## Code Documentation Examples

### From TypeScript/JavaScript:

```typescript
// Source: src/utils/auth.ts
export function validateToken(token: string): boolean {
  // ... implementation
}
```

Generates:

```mdx
## validateToken

Validates an authentication token.

### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `token` | `string` | The JWT token to validate |

### Returns

`boolean` - `true` if valid, `false` otherwise

### Example

```typescript
import { validateToken } from '@package/auth';

const isValid = validateToken(userToken);
if (!isValid) {
  throw new Error('Invalid token');
}
```
```

### From Python:

```python
# Source: src/auth.py
def validate_token(token: str) -> bool:
    """
    Validate an authentication token.
    
    Args:
        token: The JWT token to validate
        
    Returns:
        True if valid, False otherwise
    """
```

Generates similar documentation following the template structure.

---

## Quality Guidelines

- Extract real code examples, don't fabricate
- Include error handling in examples
- Add TODO markers for sections needing human review
- Use mermaid diagrams for complex flows
- Link to related documentation
- Apply terminology from context.json
