# Default Theme

The default DevDoc theme - clean, professional, and accessible.

## Features

- Clean, modern design
- System-aware dark/light mode
- Emerald green accent color
- Inter font family
- JetBrains Mono for code

## Usage

This theme is applied by default to all DevDoc projects. To explicitly use it:

```json
{
  "$schema": "https://devdoc.sh/theme.json",
  "extends": "github:brainfish-ai/devdoc/themes/default"
}
```

## Customization

Override any values in your `theme.json`:

```json
{
  "$schema": "https://devdoc.sh/theme.json",
  "extends": "github:brainfish-ai/devdoc/themes/default",
  "colors": {
    "primary": "#3B82F6"
  }
}
```

## Preview

![Default Theme Preview](https://devdoc.sh/themes/default/preview.png)
