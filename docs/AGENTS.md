# AGENTS.md - Development Guidelines for bead Documentation

## Build/Test Commands
- `bundle install` - Install Ruby dependencies
- `bundle exec jekyll serve` - Run local development server (http://localhost:4000)
- `bundle exec jekyll build` - Build static site to _site/ directory
- No specific test commands - this is a static documentation site

## Code Style Guidelines

### HTML/Liquid Templates
- Use semantic HTML5 elements
- Indent with 2 spaces
- Use Liquid template syntax for Jekyll variables: `{{ variable }}` and `{% tag %}`
- Include proper meta tags and SEO elements
- Use relative URLs with `| relative_url` filter

### CSS
- Use CSS custom properties (--color-primary, --font-sans, etc.)
- Follow BEM-like naming conventions for classes
- Mobile-first responsive design
- Use semantic color names (--color-text, --color-bg-alt)

### Content (Markdown)
- Use kramdown syntax with GFM input
- Include proper frontmatter with title, description
- Use code blocks with language specification
- Keep line length reasonable for readability