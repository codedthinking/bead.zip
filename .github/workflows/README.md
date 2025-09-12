# GitHub Actions for Bead Documentation

## Deploy Documentation to GitHub Pages

The `deploy-docs.yml` workflow automatically builds and deploys the Jekyll documentation site to GitHub Pages.

### Setup Instructions

1. **Enable GitHub Pages in your repository:**
   - Go to Settings → Pages
   - Under "Build and deployment", select "GitHub Actions" as the source

2. **Ensure branch protection (optional but recommended):**
   - The workflow triggers on pushes to `main` or `master`
   - Consider protecting your default branch to prevent accidental deployments

3. **The workflow will:**
   - Trigger automatically when changes are pushed to the `docs/` directory
   - Build the Jekyll site with the correct base URL for GitHub Pages
   - Deploy to `https://bead.zip/`

### Manual Deployment

You can also trigger the deployment manually:
1. Go to Actions tab
2. Select "Deploy Documentation to GitHub Pages"
3. Click "Run workflow"

### Customization

To deploy to a custom domain:
1. Add a `CNAME` file to `docs/` with your domain
2. Configure DNS settings as per GitHub's documentation
3. Update the `url` in `docs/_config.yml`

### Troubleshooting

If deployment fails:
- Check that GitHub Pages is enabled in repository settings
- Ensure the repository is public (or you have GitHub Pro for private repos)
- Review the Actions logs for specific error messages