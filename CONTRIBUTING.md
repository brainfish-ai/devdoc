# Contributing to DevDoc

Thank you for your interest in contributing to DevDoc! This document provides guidelines and instructions for contributing.

## Table of Contents

- [Code of Conduct](#code-of-conduct)
- [Getting Started](#getting-started)
- [How to Contribute](#how-to-contribute)
- [Development Setup](#development-setup)
- [Pull Request Process](#pull-request-process)
- [Style Guidelines](#style-guidelines)

## Code of Conduct

Please be respectful and constructive in all interactions. We're all here to build something great together.

## Getting Started

1. **Fork the repository** - Click the "Fork" button on GitHub
2. **Clone your fork** - `git clone https://github.com/YOUR_USERNAME/devdoc.git`
3. **Create a branch** - `git checkout -b feature/your-feature-name`

## How to Contribute

### Documentation Improvements

Documentation lives in the `/docs` directory. To contribute:

1. Edit or add `.mdx` files in `/docs`
2. Update `docs.json` if adding new pages
3. Test locally with `cd docs && npx devdoc dev`
4. Submit a pull request

### New Templates

Templates live in `/templates`. To create a new template:

1. Copy an existing template as a starting point
2. Modify the content and configuration
3. Ensure it includes:
   - `docs.json` - Configuration
   - `theme.json` - Theme settings
   - `index.mdx` - Home page
   - `quickstart.mdx` - Getting started guide
   - `assets/` - Static assets (favicon, logo, images)
   - `README.md` - Template documentation
4. Test thoroughly with `npx devdoc dev`
5. Submit a pull request

### New Themes

Themes live in `/themes`. To create a new theme:

1. Create a new directory under `/themes`
2. Add required files:
   - `theme.json` - Theme configuration
   - `custom.css` - Custom styles
   - `README.md` - Theme documentation
3. Test with an existing template
4. Submit a pull request

### Bug Fixes

1. Check existing issues to avoid duplicates
2. Create an issue describing the bug
3. Fork and create a fix
4. Submit a pull request referencing the issue

## Development Setup

### Prerequisites

- Node.js 18+
- npm or yarn

### Local Development

```bash
# Clone the repository
git clone https://github.com/brainfish-ai/devdoc.git
cd devdoc

# Test a template
cd templates/basic
npm install
npx devdoc dev

# Test documentation
cd docs
npm install
npx devdoc dev
```

## Pull Request Process

1. **Create a descriptive PR title** - e.g., "Add dark mode toggle to minimal theme"
2. **Fill out the PR template** - Describe what changes you made and why
3. **Link related issues** - Use "Fixes #123" or "Relates to #456"
4. **Wait for review** - A maintainer will review your PR
5. **Address feedback** - Make requested changes if any
6. **Merge!** - Once approved, your PR will be merged

### PR Checklist

- [ ] Code follows project style guidelines
- [ ] Documentation is updated if needed
- [ ] All tests pass (if applicable)
- [ ] Commit messages are clear and descriptive

## Style Guidelines

### Documentation (MDX)

- Use clear, concise language
- Include code examples where helpful
- Use proper heading hierarchy (h1 → h2 → h3)
- Add alt text to images

### Code

- Use 2-space indentation
- Use meaningful variable names
- Add comments for complex logic
- Follow existing patterns in the codebase

### Commit Messages

Follow conventional commits:

```
feat: add new feature
fix: resolve bug
docs: update documentation
style: format code
refactor: restructure code
test: add tests
chore: maintenance tasks
```

## Questions?

- Open an issue for bugs or feature requests
- Start a discussion for general questions
- Check existing issues and discussions first

Thank you for contributing! 🎉
