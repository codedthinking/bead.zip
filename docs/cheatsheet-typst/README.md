# bead Cheatsheet Typst Renderer

This folder contains a Typst application to render the bead cheatsheet as a single-page landscape A4 PDF document.

## Requirements

- [Typst](https://typst.app/) - Install via:
  - macOS: `brew install typst`
  - Other platforms: See [installation instructions](https://github.com/typst/typst#installation)

## Build

To generate the PDF:

```bash
make
```

Or directly:

```bash
typst compile cheatsheet.typ
```

## Development

To watch for changes and auto-rebuild:

```bash
make watch
```

Or:

```bash
typst watch cheatsheet.typ
```

## Output

The generated `cheatsheet.pdf` is a single-page landscape A4 document with:
- Three-column layout for optimal information density
- Rounded boxes with color-coded sections
- Syntax-highlighted code blocks
- Brand colors matching the bead documentation style guide