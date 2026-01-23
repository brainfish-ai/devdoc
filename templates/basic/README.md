# My Documentation

Documentation site built with [DevDoc](https://github.com/brainfish-ai/devdoc).

[![Deploy with Vercel](https://vercel.com/button)](https://vercel.com/new/clone?repository-url=https://github.com/brainfish-ai/devdoc-starter)

## Quick Start

### Prerequisites

- [Node.js](https://nodejs.org/) 18.0 or later
- npm, yarn, or pnpm

### Installation

1. **Clone this repository**

   ```bash
   git clone https://github.com/your-username/your-docs.git
   cd your-docs
   ```

   Or use the GitHub template button above.

2. **Install dependencies**

   ```bash
   npm install
   ```

3. **Start the development server**

   ```bash
   npm run dev
   ```

4. **Open your browser**

   Visit [http://localhost:3000](http://localhost:3000) to see your docs.

## Project Structure

```
.
├── docs.json              # Site configuration
├── index.mdx              # Homepage
├── quickstart.mdx         # Quickstart guide
├── guides/
│   ├── overview.mdx       # Overview page
│   └── configuration.mdx  # Configuration guide
├── public/
│   ├── logo.svg           # Site logo
│   └── favicon.svg        # Favicon
├── package.json
├── vercel.json            # Vercel deployment config
└── README.md
```

## Configuration

Edit `docs.json` to customize your site:

```json
{
  "name": "My Documentation",
  "logo": "/logo.svg",
  "navigation": {
    "tabs": [
      {
        "tab": "Documentation",
        "type": "docs",
        "groups": [
          {
            "group": "Getting Started",
            "pages": ["index", "quickstart"]
          }
        ]
      }
    ]
  }
}
```

## Writing Content

Create `.mdx` files with frontmatter:

```mdx
---
title: Page Title
description: Page description for SEO
---

# Your Content Here

Write Markdown with React components.

<Note>
  Use components like Note, Card, Steps, and more.
</Note>
```

## Available Commands

| Command | Description |
|---------|-------------|
| `npm run dev` | Start development server |
| `npm run build` | Build for production |
| `npm run start` | Start production server |
| `npm run check` | Validate configuration |

## Deployment

### Vercel (Recommended)

Click the "Deploy with Vercel" button above, or:

1. Push your code to GitHub
2. Import the repository in [Vercel](https://vercel.com)
3. Deploy!

### Other Platforms

```bash
# Build the site
npm run build

# Output is in the dist/ directory
```

## Learn More

- [DevDoc Documentation](https://devdoc.sh/docs)
- [MDX Documentation](https://mdxjs.com/)
- [Vercel Documentation](https://vercel.com/docs)

## License

MIT
