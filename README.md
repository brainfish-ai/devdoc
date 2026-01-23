# DevDoc

Beautiful API documentation, instantly.

<p align="center">
  <a href="https://devdoc.sh">Website</a> •
  <a href="https://devdoc.sh/docs">Documentation</a> •
  <a href="https://github.com/brainfish-ai/devdoc/issues">Issues</a>
</p>

## What's Inside

| Directory | Description |
|-----------|-------------|
| 📚 [`/docs`](./docs) | Official DevDoc documentation (deployed to [devdoc.sh](https://devdoc.sh)) |
| 🎨 [`/templates`](./templates) | Starter templates for new documentation projects |
| 🖌️ [`/themes`](./themes) | Theme presets for customization |
| 💡 [`/examples`](./examples) | Advanced usage examples |

## Quick Start

Create a new documentation project in seconds:

```bash
# Create with default template
npx create-devdoc-doc my-docs

# Or choose a specific template
npx create-devdoc-doc my-docs --template openapi
npx create-devdoc-doc my-docs --template graphql
```

Then start the development server:

```bash
cd my-docs
npm install
npx devdoc dev
```

## Templates

| Template | Description | Best For |
|----------|-------------|----------|
| [`basic`](./templates/basic) | Simple documentation site | General docs, guides, knowledge bases |
| [`graphql`](./templates/graphql) | GraphQL API documentation | GraphQL APIs with interactive playground |
| [`openapi`](./templates/openapi) | REST API documentation | REST APIs with OpenAPI/Swagger specs |

## Themes

| Theme | Description |
|-------|-------------|
| [`default`](./themes/default) | Clean, professional look with emerald accents |
| [`minimal`](./themes/minimal) | Stripped-down, content-focused design |
| [`enterprise`](./themes/enterprise) | Professional theme for enterprise docs |

### Using a Theme

Add to your `theme.json`:

```json
{
  "$schema": "https://devdoc.sh/theme.json",
  "extends": "github:brainfish-ai/devdoc/themes/minimal"
}
```

## Documentation

Visit [devdoc.sh](https://devdoc.sh) for full documentation, including:

- [Getting Started](https://devdoc.sh/quickstart)
- [CLI Reference](https://devdoc.sh/cli/overview)
- [Configuration](https://devdoc.sh/essentials/configuration)
- [Components](https://devdoc.sh/essentials/components)

## Contributing

We welcome contributions! See [CONTRIBUTING.md](./CONTRIBUTING.md) for guidelines.

### Ways to Contribute

- 🐛 [Report bugs](https://github.com/brainfish-ai/devdoc/issues/new?template=bug_report.md)
- 💡 [Request features](https://github.com/brainfish-ai/devdoc/issues/new?template=feature_request.md)
- 📝 Improve documentation
- 🎨 Create new templates or themes
- 💻 Submit pull requests

## License

MIT © [Brainfish AI](https://brainfi.sh)
