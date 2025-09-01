# bead Documentation Website

This is the Jekyll-based documentation website for bead.

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

The site is deployed to https://bead.zip/

For deployment:
1. Build the site: `bundle exec jekyll build`
2. Deploy the `_site/` directory to the web server

The site can also be deployed to:
- Netlify
- Vercel
- Any static hosting service