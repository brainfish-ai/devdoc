---
name: docs-from-code
description: Generate documentation from specific code files, functions, or modules
---

## Instructions

When generating docs from specific code:

1. Analyze the code structure and purpose
2. Identify:
   - Public API/exports
   - Function signatures and parameters
   - Return types and values
   - Usage patterns from tests or examples
3. Generate documentation with:
   - Overview of the module/function
   - Parameter descriptions
   - Code examples
   - Common use cases

## Output Format

```mdx
---
title: "{Module/Function Name}"
description: "{Brief purpose}"
---

{Overview paragraph}

## Installation

{If applicable}

## Usage

<Steps>
  <Step title="Import">
    ```typescript
    import { function } from 'package';
    ```
  </Step>
  <Step title="Basic Usage">
    {Example code}
  </Step>
</Steps>

## API Reference

### `functionName(params)`

{Description}

**Parameters:**
| Name | Type | Description |
|------|------|-------------|
| param1 | `type` | Description |

**Returns:** `type` - Description

## Examples

{Practical examples with code blocks}
```

## Best Practices

1. Extract real code examples - don't fabricate
2. Include TypeScript types when available
3. Show common use cases
4. Document edge cases and error handling
5. Link to related functions/modules
