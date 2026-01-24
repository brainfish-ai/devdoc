---
name: sync-docs
description: Analyze existing documentation against codebase and identify/fix outdated content
---

## Instructions

When syncing documentation with the codebase:

### Step 1: Build Documentation Inventory

Scan all MDX files and extract:
- Documented functions, classes, components
- Code examples and their imports
- API endpoints referenced
- Package versions mentioned
- CLI commands documented

### Step 2: Analyze Current Codebase

Compare documentation against source code:
- Check if documented functions still exist
- Verify function signatures match (parameters, return types)
- Confirm API endpoints are still valid
- Check if package versions are current
- Identify new exports not yet documented

### Step 3: Generate Sync Report

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

### Missing Documentation
- `src/utils/validator.ts` - New export, not documented
- `POST /api/v2/webhooks` - New endpoint, not documented

### Up to Date
- `docs/guides/authentication.mdx`
- `docs/components/button.mdx`
```

### Step 4: Update Options

Ask user preference:
1. **Auto-fix all** - Update all outdated docs automatically
2. **Interactive** - Review each change before applying
3. **Report only** - Just show the report, don't change anything

### Step 5: Apply Updates

When updating:
- Preserve existing prose and explanations
- Update code examples to match current signatures
- Add TODO markers for sections needing human review
- Update version numbers
- Add stubs for missing documentation

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
