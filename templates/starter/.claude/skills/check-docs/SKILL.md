---
name: check-docs
description: Quick health check for documentation issues. Reads context memory for validation.
---

## Instructions

Run a quick audit of documentation health.

### Step 0: Read Context Memory

**First, read `.devdoc/context.json` if it exists:**

```json
{
  "product": { "name": "..." },
  "terminology": { 
    "glossary": { "term": "definition" },
    "avoidTerms": [{ "wrong": "...", "correct": "..." }],
    "brandNames": { "ProductName": "ProductName" }
  },
  "api": { "style": "REST", "authentication": { "type": "api_key" } }
}
```

**Use context for additional checks:**
- Verify terminology usage matches glossary
- Flag usage of terms in `avoidTerms`
- Check brand name capitalization
- Validate API patterns match `api.conventions`

### Step 1: Get Documentation Type

**Read `docs.json` for `docType` field:**
```json
{ "docType": "api" }  // "internal" | "api" | "product"
```

**If not set, detect from structure:**
- Has `architecture/`, `development/` → "internal"
- Has `api-reference/`, `sdks/` → "api"
- Has `features/`, `tutorials/` → "product"

This helps tailor the checks:
- **internal**: Should have setup guides, architecture docs
- **api**: Should have authentication, error handling, API reference
- **product**: Should have screenshots, tutorials, FAQs

### Step 2: Run Checks

#### Standard Checks:
1. **Broken Links** - Check all internal href links resolve
2. **Missing Pages** - Pages in docs.json but file doesn't exist
3. **Orphan Pages** - MDX files not in docs.json navigation
4. **Code Validity** - Syntax check code blocks
5. **Outdated Examples** - Compare imports against package exports
6. **Stale Versions** - Check version numbers against package.json

#### Context-Based Checks (if context.json exists):
7. **Terminology** - Flag incorrect terms from `avoidTerms`
8. **Brand Names** - Check capitalization matches `brandNames`
9. **Product Name** - Ensure consistent use of `product.name`
10. **API Patterns** - Verify examples follow `api.conventions`

### Output Format

```
Documentation Health Check
==========================

Context: Using .devdoc/context.json ✓
DocType: api

Summary: X issues found

## Critical Issues

### Broken Links (count)
   file.mdx:line → /path (page not found)

### Missing Pages (count)
   docs.json references 'page' but file not found

## Warnings

### Terminology Issues (count)
   file.mdx:line → Uses "charge" instead of "payment"
   file.mdx:line → Uses "transaction" instead of "payment"
   (per terminology.avoidTerms in context)

### Brand Name Issues (count)
   file.mdx:line → "productname" should be "ProductName"

### Outdated Code (count)
   file.mdx:line → import { oldFunc } from 'pkg'
   'oldFunc' no longer exported, use 'newFunc'

### Orphan Pages (count)
   path/to/file.mdx (not in navigation)

## Passed

✓ All version numbers current
✓ All internal links resolve
✓ No syntax errors in code blocks
✓ Product name used consistently
```

## Checks By DocType

### For docType: "internal"
- [ ] Setup guide exists and references correct tools
- [ ] Architecture docs present
- [ ] Development workflow documented
- [ ] Prerequisites clearly listed

### For docType: "api"
- [ ] Authentication page exists
- [ ] Error codes documented
- [ ] API reference present (OpenAPI or manual)
- [ ] Quickstart under 5 minutes
- [ ] Code examples in primary language

### For docType: "product"
- [ ] Screenshots present and described
- [ ] Tutorials have clear steps
- [ ] FAQ section exists
- [ ] Non-technical language used

## Detailed Checks

### Link Validation
- Internal links (`href="/path"`)
- Anchor links (`href="#section"`)
- Cross-references between pages

### Code Block Validation
- Language tag present
- Valid syntax (basic check)
- Import statements resolve
- Uses correct primary language from context

### Navigation Validation
- All pages in docs.json exist
- No duplicate entries
- Valid group structure

### Content Validation
- Frontmatter present (title, description)
- No H1 headings (title from frontmatter)
- Images have alt text

### Terminology Validation (from context)
- No terms from `avoidTerms` used
- Brand names capitalized correctly
- Glossary terms used consistently

## Quick Fixes

After running check, common fixes:

1. **Broken link** → Update href or create missing page
2. **Orphan page** → Add to docs.json or delete if unused
3. **Missing frontmatter** → Add title and description
4. **Outdated import** → Update to current export name
5. **Wrong terminology** → Replace with correct term from context
6. **Brand name** → Fix capitalization per context.json
