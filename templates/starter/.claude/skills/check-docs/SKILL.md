---
name: check-docs
description: Quick check for documentation issues without making changes
---

## Instructions

Run a quick audit of documentation health:

1. **Broken Links** - Check all internal href links resolve
2. **Missing Pages** - Pages in docs.json but file doesn't exist
3. **Orphan Pages** - MDX files not in docs.json navigation
4. **Code Validity** - Syntax check code blocks
5. **Outdated Examples** - Compare imports against package exports
6. **Stale Versions** - Check version numbers against package.json

## Output Format

```
Documentation Health Check
==========================

Summary: X issues found

Broken Links (count)
   file.mdx:line → /path (page not found)

Outdated Code (count)
   file.mdx:line → import { oldFunc } from 'pkg'
   'oldFunc' no longer exported, use 'newFunc'

Orphan Pages (count)
   path/to/file.mdx (not in navigation)

Missing Pages (count)
   docs.json references 'page' but file not found

All version numbers current
All pages in docs.json exist
No syntax errors in code blocks
```

## Checks Performed

### Link Validation
- Internal links (`href="/path"`)
- Anchor links (`href="#section"`)
- Cross-references between pages

### Code Block Validation
- Language tag present
- Valid syntax (basic check)
- Import statements resolve

### Navigation Validation
- All pages in docs.json exist
- No duplicate entries
- Valid group structure

### Content Validation
- Frontmatter present (title, description)
- No H1 headings (title from frontmatter)
- Images have alt text

## Quick Fixes

After running check, common fixes:

1. **Broken link** → Update href or create missing page
2. **Orphan page** → Add to docs.json or delete if unused
3. **Missing frontmatter** → Add title and description
4. **Outdated import** → Update to current export name
