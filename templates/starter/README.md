# My Documentation

This documentation site was created with [DevDoc](https://devdoc.sh).

## Getting Started

Install dependencies:

```bash
npm install
```

Start the development server:

```bash
npm run dev
```

Open [http://localhost:3000](http://localhost:3000) to view your documentation.

## Project Structure

```
├── docs.json           # Configuration file
├── theme.json          # Theme customization
├── index.mdx           # Homepage
├── quickstart.mdx      # Quickstart guide
├── guides/             # Documentation guides
│   ├── overview.mdx
│   └── configuration.mdx
├── api-reference/      # API documentation (if enabled)
│   ├── introduction.mdx
│   ├── authentication.mdx
│   ├── errors.mdx
│   ├── openapi.json    # OpenAPI spec (for REST APIs)
│   └── schema.graphql  # GraphQL schema (for GraphQL APIs)
└── public/             # Static assets
    ├── logo.svg
    └── favicon.svg
```

## Configuration

Edit `docs.json` to customize your documentation:

- **Navigation**: Configure tabs, groups, and pages
- **Branding**: Set logo, colors, and favicon
- **API Reference**: Enable OpenAPI or GraphQL documentation

See the [Configuration Guide](/guides/configuration) for more details.

## Deployment

Deploy to DevDoc hosting:

```bash
npx @brainfish-ai/devdoc deploy
```

Your docs will be available at `https://your-subdomain.devdoc.sh`

## Learn More

- [DevDoc Documentation](https://devdoc.sh/docs)
- [GitHub Repository](https://github.com/brainfish-ai/devdoc)
