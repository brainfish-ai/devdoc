---
name: update-docs-json
description: Add new pages to docs.json navigation configuration
---

## Instructions

When updating docs.json:

1. Read the current docs.json structure
2. Identify the appropriate group for the new page
3. Add the page path (without .mdx extension)
4. Maintain consistent ordering (introductory pages first)

## Navigation Structure

```json
{
  "navigation": {
    "tabs": [
      {
        "tab": "Tab Name",
        "type": "docs",
        "groups": [
          {
            "group": "Group Name",
            "icon": "phosphor-icon-name",
            "pages": ["page-path", "folder/page-path"]
          }
        ]
      }
    ]
  }
}
```

## Page Path Format

- Use relative paths from docs root
- Omit the `.mdx` extension
- Use forward slashes for nested paths
- Examples: `"quickstart"`, `"guides/authentication"`

## Common Icons (Phosphor)

- `rocket-launch` - Getting started
- `book-open` - Documentation
- `terminal` - CLI/Commands
- `gear` - Configuration
- `code` - Development
- `puzzle-piece` - Components
- `key` - Authentication
- `cloud-arrow-up` - Deployment

## Best Practices

1. Group related pages together
2. Order pages from basic to advanced
3. Use descriptive group names
4. Keep navigation depth shallow (max 2 levels)
