# devdoc-api-typescript

Auto-generated TypeScript SDK with full type safety.

## Installation

```bash
npm install devdoc-api-typescript
# or
yarn add devdoc-api-typescript
```

## Usage

```typescript
import { client, setConfig } from 'devdoc-api-typescript';
import type { paths, components } from 'devdoc-api-typescript';

// Configure the client
setConfig({
  baseUrl: 'https://api.example.com',
  headers: {
    'Authorization': 'Bearer YOUR_API_KEY',
  },
});

// Make type-safe API calls
const response = await client.get('/endpoint');

// Use generated types
type MySchema = components['schemas']['MySchema'];
```

## Type Safety

This SDK includes full TypeScript types generated from the OpenAPI specification:

- `paths` - All API endpoints with request/response types
- `components` - All schema definitions

## Generated

This SDK was auto-generated from an OpenAPI specification using DevDoc SDK Generator.
