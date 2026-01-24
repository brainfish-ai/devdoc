---
name: update-doc
description: Update existing documentation by analyzing codebase changes or user references.
---

## Instructions

When user wants to update documentation:

### Step 0: Read Context Memory

**First, read `.devdoc/context.json` if it exists:**
- Use `product.name` for product references
- Apply `terminology.glossary` for correct terms
- Avoid `terminology.avoidTerms`
- Match `documentation.voice` for writing style

### Step 1: Understand What to Update

Ask the user:

"What would you like to update?

1. **A specific page** - Tell me which page to update
2. **Sync with codebase** - I'll find outdated docs by comparing to code
3. **Navigation structure** - Update docs.json organization
4. **Multiple pages** - Describe the changes needed
5. **Fix issues** - Point me to errors or problems"

### Step 2: Analyze Current State

Based on their choice:

#### For Specific Page:
- "Which page? (e.g., `guides/authentication.mdx`)"
- Read the current page content
- "What changes do you want?
  - Update code examples
  - Add new sections
  - Fix errors/outdated info
  - Rewrite for clarity
  - Other (describe)"

#### For Codebase Sync:
- Locate source code (from context or `../`)
- Compare documentation against code:
  - Function signatures changed?
  - New exports not documented?
  - Removed features still documented?
  - Version numbers outdated?
- Generate sync report (see below)

#### For Navigation:
- Read current `docs.json`
- "What navigation changes?
  - Add new pages
  - Reorganize groups
  - Rename tabs
  - Remove pages
  - Other"

#### For Multiple Pages:
- "Which pages need updating?"
- "What's the common change across them?"

#### For Issues:
- "What's the problem you're seeing?"
- Analyze and propose fixes

### Step 3: Generate Sync Report (if syncing)

```
## Documentation Sync Report

### Outdated (Action Required)
- `docs/api/users.mdx`: Function signature changed
  - Documented: `createUser(name, email)`
  - Current: `createUser(options: CreateUserInput)`
  
- `docs/quickstart.mdx`: Package version outdated
  - Documented: v1.2.0
  - Current: v2.0.0

### Terminology Issues
- `docs/guides/intro.mdx:15`: Uses "charge" instead of "payment"

### Missing Documentation
- `src/utils/newFeature.ts` - New export, not documented
- `POST /api/v2/webhooks` - New endpoint

### Up to Date ✓
- `docs/guides/authentication.mdx`
- `docs/api/errors.mdx`
```

Ask: "How would you like to proceed?
1. **Fix all** - Update everything automatically
2. **Interactive** - Review each change
3. **Specific items** - Tell me which to fix"

### Step 4: Propose Changes

Before making changes, show what will be modified:

"I'll make these changes:

**`docs/api/users.mdx`**
- Update `createUser` signature and examples
- Add new `options` parameter documentation

**`docs/quickstart.mdx`**  
- Update version from 1.2.0 to 2.0.0
- Update installation command

**`docs.json`**
- Add new page: `guides/webhooks.mdx`

Proceed with these changes?"

### Step 5: Apply Updates

When updating:

1. **Preserve prose** - Keep explanations, update technical details
2. **Update code examples** - Match current signatures
3. **Fix terminology** - Apply context.json rules
4. **Add deprecation notices** for removed features:
   ```mdx
   <Warning>
   **Deprecated in v2.0**: This feature was removed. 
   See [migration guide](/guides/v2-migration).
   </Warning>
   ```
5. **Create stubs** for new features:
   ```mdx
   {/* TODO: Document this new feature */}
   ## New Feature
   Coming soon...
   ```

### Step 6: Update Navigation (if needed)

If pages were added/removed/moved:

1. Read current `docs.json`
2. Propose navigation changes
3. Apply after user confirms

### Step 7: Summary

"Updated:
- `docs/api/users.mdx` - Updated function signatures
- `docs/quickstart.mdx` - Updated to v2.0.0
- `docs.json` - Added webhooks page

Changes ready for review. Run `npm run dev` to preview.

Want me to commit these changes? Use `/commit` when ready."

---

## Update Patterns

### Changed Function Signature
```mdx
// Before
`createUser(name: string, email: string)`

// After  
`createUser(options: CreateUserInput)`

Where `CreateUserInput`:
```typescript
interface CreateUserInput {
  name: string;
  email: string;
  role?: 'admin' | 'user';
}
```
```

### Removed Feature
```mdx
<Warning>
**Removed in v2.0**: The `legacyAuth` method was removed.
Use `authenticate()` instead. See [migration guide](/migrate-v2).
</Warning>
```

### New Feature Stub
```mdx
---
title: "Webhooks"
description: "Receive real-time notifications"
---

{/* TODO: Complete this documentation */}

## Overview

Documentation coming soon.

## Quick Start

```typescript
// Example placeholder
```
```

---

## Quality Guidelines

- Always show changes before applying
- Preserve existing prose and explanations
- Update only technical details (code, versions, signatures)
- Add TODO markers for human review
- Apply terminology from context.json
- Create stubs rather than skip new features
