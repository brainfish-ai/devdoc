<p align="center">
  <pre align="center">
██████╗ ███████╗██╗   ██╗██████╗  ██████╗  ██████╗
██╔══██╗██╔════╝██║   ██║██╔══██╗██╔═══██╗██╔════╝
██║  ██║█████╗  ██║   ██║██║  ██║██║   ██║██║     
██║  ██║██╔══╝  ╚██╗ ██╔╝██║  ██║██║   ██║██║     
██████╔╝███████╗ ╚████╔╝ ██████╔╝╚██████╔╝╚██████╗
╚═════╝ ╚══════╝  ╚═══╝  ╚═════╝  ╚═════╝  ╚═════╝
  </pre>
</p>

<p align="center">
  <strong>Beautiful documentation powered by AI agents</strong>
</p>

<p align="center">
  <a href="https://devdoc.sh">Website</a> •
  <a href="https://devdoc.sh/docs">Documentation</a> •
  <a href="https://github.com/brainfish-ai/devdoc/issues">Issues</a>
</p>

---

## Features

| Feature | Description |
|---------|-------------|
| Write in MDX | Markdown with React components for rich documentation |
| Beautiful Design | Modern UI with dark mode out of the box |
| Agentic Search | AI-powered search with agentic UX and sandbox |
| API Playground | Postman/Hoppscotch-like client for testing API endpoints |
| AI Agent Support | Use Claude Code or Cursor to write docs faster |
| OpenAPI Support | Auto-generate API reference from OpenAPI specs |
| GraphQL Playground | Interactive query explorer for GraphQL APIs |
| Fast Setup | Deploy in under 5 minutes |

## Quick Start

Create a new documentation project in seconds:

```bash
npx @brainfish-ai/devdoc create my-docs
```

Choose your template type:
- **Basic** — Simple documentation site with guides
- **OpenAPI** — REST API docs with interactive playground
- **GraphQL** — GraphQL API with schema explorer

Then start developing:

```bash
cd my-docs
npm install
npm run dev
```

Open [http://localhost:3333](http://localhost:3333) to view your documentation.

## AI Agent Support

DevDoc includes built-in support for AI coding agents. Set up AI skills:

```bash
npx @brainfish-ai/devdoc ai
```

**Available commands in Claude Code:**

| Command | Description |
|---------|-------------|
| `/bootstrap-docs` | Generate docs from your codebase |
| `/migrate-docs` | Migrate from Mintlify, Docusaurus, etc. |
| `/import-api-spec` | Import OpenAPI, GraphQL, or AsyncAPI specs |
| `/check-docs` | Quick health check |
| `/blame-doc` | Find duplicates, outdated content, discrepancies |
| `/create-doc` | Create a new documentation page |
| `/update-doc` | Update existing documentation |
| `/delete-doc` | Delete documentation pages |
| `/commit-doc` | Commit documentation changes |

**In Cursor**, just ask in Agent mode:
- "Generate initial documentation from this repo"
- "Blame docs - find duplicates and outdated content"
- "Create a new guide about authentication"
- "Update the quickstart guide"

## Repository Structure

| Directory | Description |
|-----------|-------------|
| [`/docs`](./docs) | Official DevDoc documentation ([devdoc.sh](https://devdoc.sh)) |
| [`/templates`](./templates) | Starter template for new projects |
| [`/themes`](./themes) | Theme presets for customization |

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

Visit [devdoc.sh](https://devdoc.sh) for full documentation:

- [Getting Started](https://devdoc.sh/quickstart)
- [CLI Reference](https://devdoc.sh/cli/overview)
- [AI Agents](https://devdoc.sh/ai-agents/overview)
- [Configuration](https://devdoc.sh/essentials/configuration)
- [Components](https://devdoc.sh/essentials/components)

## Contributing

We welcome contributions! See [CONTRIBUTING.md](./CONTRIBUTING.md) for guidelines.

- [Report bugs](https://github.com/brainfish-ai/devdoc/issues/new?template=bug_report.md)
- [Request features](https://github.com/brainfish-ai/devdoc/issues/new?template=feature_request.md)
- Improve documentation
- Create new themes
- Submit pull requests

## License

MIT © [Brainfish AI](https://brainfi.sh)
