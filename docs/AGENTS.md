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

## Copy Style Guide

### Product Name Spelling
The product name "bead" should always be lowercase, even at the beginning of sentences.

**Correct examples:**
- ✅ "bead is a tool for reproducible research"
- ✅ "Getting Started with bead"
- ✅ "bead packages your computational workflows"
- ✅ "When using bead, you can..."

**Incorrect examples:**
- ❌ "Bead is a tool for reproducible research"
- ❌ "Getting Started with Bead"
- ❌ "BEAD packages your computational workflows"

### File Extensions and Formats
Always use lowercase for file extensions with a period prefix.

**Correct examples:**
- ✅ "Each bead is a simple .zip file"
- ✅ "Save your work as a .bead archive"
- ✅ "Export to .csv format"
- ✅ "The .zip file contains all dependencies"

**Incorrect examples:**
- ❌ "Each bead is a simple ZIP file"
- ❌ "Save your work as a BEAD archive"
- ❌ "Export to CSV format"
- ❌ "The ZIP file contains all dependencies"

### Command-Line Examples
- Always show the prompt as `$` for bash commands
- Use comments with `#` to explain commands
- Show actual output when relevant
- Use consistent spacing and formatting

**Example:**
```bash
$ bead new my-analysis
Created "my-analysis"

$ cd my-analysis
$ bead save results  # Creates .zip archive
Successfully stored bead at ~/beads/my-analysis_20250730T120000.zip
```

### Technical Terms
- Use "bead" (lowercase) when referring to the tool or a computational unit
- Use "workspace" for active development directories
- Use "archive" for saved .zip files
- Use "box" for storage locations
- Use "dependency" or "input" for upstream beads

### Writing Tone
- Be direct and concise
- Use active voice
- Avoid jargon when possible
- Focus on practical examples
- Address common pain points directly