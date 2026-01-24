---
name: sync-docs
description: Analyze existing documentation against codebase. Reads context memory for consistency.
---

## Instructions

When syncing documentation with the codebase:

### Step 0: Read Context Memory

**First, read `.devdoc/context.json` if it exists:**

```json
{
  "product": { "name": "...", "type": "..." },
  "terminology": { "glossary": {}, "avoidTerms": [] },
  "documentation": { "voice": "...", "codeExamples": { "primaryLanguage": "..." } }
}
```

**Use context throughout:**
- Use correct `product.name` in any updates
- Apply `terminology.glossary` - use correct terms
- Avoid `terminology.avoidTerms` - don't use these words
- Match `documentation.voice` when writing updates
- Use `documentation.codeExamples.primaryLanguage` for code

**If no context exists:** Suggest running bootstrap first, or proceed with basic sync.

### Step 1: Locate Source Code

Determine where the source code is:
- If `docs.json` exists here → you're in docs folder, source code is in `../`
- If `package.json` and `src/` exist here → you're at repo root
- Check `codebase.sourceLocation` in context.json if set

### Step 2: Get Documentation Type

**Check `docs.json` for `docType` field:**

```json
{ "docType": "api" }  // "internal" | "api" | "product"
```

**If `docType` is set:** Use that value automatically.

**If `docType` is NOT set, detect from structure:**
- Has `architecture/`, `development/` → "internal"
- Has `api-reference/`, `sdks/` → "api"  
- Has `features/`, `tutorials/` → "product"

**If still unclear, ask and save to docs.json.**

### Step 3: Build Documentation Inventory

Scan all MDX files and extract:
- Documented functions, classes, components
- Code examples and their imports
- API endpoints referenced
- Package versions mentioned
- CLI commands documented

### Step 4: Analyze Current Codebase

Compare documentation against source code:
- Check if documented functions still exist
- Verify function signatures match (parameters, return types)
- Confirm API endpoints are still valid
- Check if package versions are current
- Identify new exports not yet documented

### Step 5: Generate Sync Report

Output a report categorizing issues:

```
## Documentation Sync Report

### Outdated (Breaking Changes)
- `docs/api/users.mdx`: `createUser()` signature changed
  - Documented: `createUser(name: string)`
  - Current: `createUser(data: UserInput)`

### Outdated (Minor Changes)  
- `docs/quickstart.mdx`: Package version outdated
  - Documented: `v1.2.0`
  - Current: `v1.5.0`

### Terminology Issues
- `docs/guides/intro.mdx`: Uses "charge" instead of "payment"
  (per terminology.avoidTerms in context)

### Missing Documentation
- `src/utils/validator.ts` - New export, not documented
- `POST /api/v2/webhooks` - New endpoint, not documented

### Up to Date
- `docs/guides/authentication.mdx`
- `docs/components/button.mdx`
```

### Step 6: Update Options

Ask user preference:
1. **Auto-fix all** - Update all outdated docs automatically
2. **Interactive** - Review each change before applying
3. **Report only** - Just show the report, don't change anything

### Step 7: Apply Updates

When updating:
- **Read appropriate template** from `.devdoc/templates/` for structure guidance
- Preserve existing prose and explanations
- Update code examples to match current signatures
- Use terminology from context.json
- Add TODO markers for sections needing human review
- Update version numbers
- Add stubs for missing documentation

**After updates, consider updating context.json:**
If you discover new patterns or terminology, add to `learned.insights`:

```json
{
  "learned": {
    "insights": [
      {
        "date": "2026-01-24",
        "category": "api",
        "insight": "Webhooks require HMAC signature verification",
        "source": "code analysis"
      }
    ]
  }
}
```

## Detection Patterns

| Documentation Pattern | Codebase Check |
|----------------------|----------------|
| `import { X } from 'pkg'` | Verify X is exported from pkg |
| `function X(a, b)` | Check X signature in source |
| `v1.2.3` version strings | Compare with package.json |
| `POST /api/users` | Verify route exists |
| `<Component prop={x}>` | Check component props interface |

## Update Strategies

### For Changed Function Signatures
```mdx
// Before (outdated)
createUser(name: string, email: string)

// After (updated)
createUser(data: UserInput)
// Where UserInput = { name: string, email: string, role?: string }
```

### For Removed Features
```mdx
<Warning>
**Deprecated**: This feature was removed in v2.0. 
See [migration guide](/guides/v2-migration) for alternatives.
</Warning>
```

### For New Features (stub)
```mdx
---
title: "New Feature"
description: "Description"
---

{/* TODO: Document this feature */}

## Overview

Coming soon...
```

## Type-Specific Checks

### For docType: "internal"
- Dev setup instructions still work
- Architecture diagrams match current code
- Internal tool versions are current

### For docType: "api"
- API endpoints match OpenAPI spec
- Auth examples are correct
- SDK versions are current
- Error codes are complete

### For docType: "product"
- Screenshots match current UI
- Feature descriptions are accurate
- Tutorials still work
