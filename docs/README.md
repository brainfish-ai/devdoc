# DevDoc Documentation

This is the official documentation for [DevDoc](https://devdoc.sh), a documentation platform for APIs and products.

## Development

```bash
# Start development server
npm run dev
```

Open [http://localhost:3000](http://localhost:3000) to view the docs.

## Structure

```
├── docs.json          # Navigation and configuration
├── theme.json         # Theme customization
├── index.mdx          # Homepage
├── quickstart.mdx     # Getting started guide
├── deployment.mdx     # Deployment guide
├── ci-cd.mdx          # CI/CD integration
├── cli/               # CLI documentation
│   ├── overview.mdx
│   ├── deploy.mdx
│   ├── dev.mdx
│   └── keys.mdx
├── config/            # Configuration guides
│   ├── docs-json.mdx
│   └── theme.mdx
├── essentials/        # Content writing guides
├── components/        # MDX component examples
└── api-reference/     # OpenAPI specs
```

## Deployment

```bash
devdoc deploy
```

## License

MIT
