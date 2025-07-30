# Bead Documentation Website

This is the Jekyll-based documentation website for Bead.

## Local Development

### Prerequisites

- Ruby 2.7+
- Bundler (`gem install bundler`)

### Setup

```bash
# Install dependencies
bundle install

# Run local server
bundle exec jekyll serve

# Visit http://localhost:4000
```

### Building for Production

```bash
bundle exec jekyll build
# Output in _site/ directory
```

## Structure

- `index.html` - Homepage with hero, features, and examples
- `getting-started.md` - Quick start guide
- `_guides/` - In-depth guide collection
- `reference.md` - CLI reference
- `_layouts/` - Page templates
- `assets/css/` - Styles

## Deployment

The site can be deployed to:
- GitHub Pages
- Netlify
- Any static hosting service

Just point to the `_site/` directory after building.