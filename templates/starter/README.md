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
  <strong>Beautiful documentation for your project</strong>
</p>

<p align="center">
  <a href="https://your-subdomain.devdoc.sh">Live Docs</a> •
  <a href="#getting-started">Getting Started</a> •
  <a href="#project-structure">Structure</a> •
  <a href="#deployment">Deploy</a>
</p>

---

## ✨ Features

- 📝 **Write in MDX** — Markdown with React components for rich documentation
- 🎨 **Beautiful Design** — Modern UI with dark mode out of the box
- 🔍 **AI-Powered Search** — Help users find answers instantly
- ⚡ **Fast Setup** — Get started in under 5 minutes
- 📱 **Responsive** — Looks great on all devices

## 🚀 Getting Started

Install dependencies:

```bash
npm install
```

Start the development server:

```bash
npm run dev
```

Open [http://localhost:3000](http://localhost:3000) to view your documentation.

## 📁 Project Structure

```
├── docs.json              # Navigation & site configuration
├── theme.json             # Theme & color customization
├── index.mdx              # Homepage
├── quickstart.mdx         # Quickstart guide
│
├── guides/                # Documentation guides
│   ├── overview.mdx       # Core concepts
│   └── configuration.mdx  # Configuration reference
│
├── api-reference/         # API documentation (if enabled)
│   ├── introduction.mdx   # API introduction
│   ├── authentication.mdx # Auth guide
│   ├── errors.mdx         # Error handling
│   ├── openapi.json       # OpenAPI spec (REST)
│   └── schema.graphql     # GraphQL schema
│
└── public/                # Static assets
    ├── logo.svg           # Your logo
    └── favicon.svg        # Browser favicon
```

## ⚙️ Configuration

Edit `docs.json` to customize your documentation:

| Setting | Description |
|---------|-------------|
| `name` | Your documentation site name |
| `logo` | Logo image paths (light/dark mode) |
| `colors.primary` | Primary brand color |
| `navigation.tabs` | Configure tabs and page groups |

See the [Configuration Guide](/guides/configuration) for more details.

## 🚢 Deployment

Deploy to DevDoc hosting with a single command:

```bash
npx @brainfish-ai/devdoc deploy
```

Your docs will be live at `https://your-subdomain.devdoc.sh`

## 📚 Learn More

- [DevDoc Documentation](https://devdoc.sh/docs) — Full platform docs
- [Components](https://devdoc.sh/components) — Available MDX components
- [CLI Reference](https://devdoc.sh/cli) — Command line tools

---

<p align="center">
  Built with <a href="https://devdoc.sh">DevDoc</a> 🐟
</p>
