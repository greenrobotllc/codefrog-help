# CodeFrog Help Documentation

This directory contains the Jekyll-based help documentation for CodeFrog, hosted on GitHub Pages at [help.codefrog.app](https://help.codefrog.app).

## Structure

```
public_html/
├── _config.yml          # Jekyll configuration
├── Gemfile              # Ruby dependencies
├── CNAME                # Custom domain configuration
├── _layouts/            # Jekyll layouts
│   └── help.html        # Main help page layout
├── _data/               # Data files
│   └── features.yml     # Feature list data
├── assets/              # Static assets
│   ├── css/            # Stylesheets
│   ├── js/             # JavaScript (Simple-Jekyll-Search)
│   └── images/         # Images
├── help/                # Help documentation
│   ├── index.md        # Complete Feature List
│   └── mas/            # Mac App Store help pages
│       ├── shortcuts.md
│       ├── workflows.md
│       ├── accessibility.md
│       ├── security.md
│       ├── osv.md
│       ├── secrets.md
│       ├── launch-checklist.md
│       └── ...
└── search.json          # Search index (generated)
```

## Local Development

### Prerequisites

- Ruby 2.7 or later
- Bundler gem: `gem install bundler`

### Setup

1. Install dependencies:
   ```bash
   cd landing-page/public_html
   bundle install
   ```

2. Run local server:
   ```bash
   bundle exec jekyll serve --livereload
   ```

3. Open browser:
   ```
   http://localhost:4000/help/
   ```

### Local Apache Development

For local Apache development with PHP redirects, the `.htaccess` file provides redirects from legacy PHP URLs to new Jekyll structure.

## Deployment

### Automated Deployment

Use the deployment script:

```bash
./landing-page/scripts/deploy_docs.sh
```

The script will:
1. Check for uncommitted changes
2. Install dependencies
3. Build the Jekyll site
4. Deploy to `gh-pages` branch
5. Push to GitHub

### Manual Deployment

1. Build the site:
   ```bash
   cd landing-page/public_html
   JEKYLL_ENV=production bundle exec jekyll build -d _site
   ```

2. Deploy `_site` directory to GitHub Pages (gh-pages branch)

## Adding New Pages

1. Create a new Markdown file in `help/mas/` (or `help/direct/` for Direct Download)
2. Add front matter:
   ```yaml
   ---
   title: Page Title
   layout: help
   redirect_from:
     - /help/old-page.php
   ---
   ```
3. Write content in Markdown
4. Add to navigation in `_layouts/help.html` if needed

## Search

Search uses **Lunr.js** (a lightweight, client-side search engine) with a generated `search.json` file. The search index is built client-side from all pages in the `help/` directory.

### Why Lunr.js?

- ✅ Actively maintained (unlike deprecated Simple-Jekyll-Search)
- ✅ Client-side only (no server or API keys needed)
- ✅ Works perfectly with GitHub Pages
- ✅ Fast and lightweight
- ✅ Full-text search with relevance scoring

The search implementation is in `assets/js/lunr-search.js` and uses the Lunr.js CDN.

## Redirects

Legacy PHP URLs are redirected using:
- **GitHub Pages:** `jekyll-redirect-from` plugin (in page front matter)
- **Local Apache:** `.htaccess` rules

## Custom Domain

The site is configured for `help.codefrog.app`:
1. CNAME file contains the domain
2. DNS: CNAME record pointing to GitHub Pages
3. HTTPS: Enabled in GitHub Pages settings

## Maintenance

- **Update Features:** Edit `_data/features.yml`
- **Update Styles:** Edit `assets/css/help.css`
- **Update Layout:** Edit `_layouts/help.html`
- **Add Pages:** Create new Markdown files in `help/`

## Resources

- [Jekyll Documentation](https://jekyllrb.com/docs/)
- [GitHub Pages](https://pages.github.com/)
- [Simple-Jekyll-Search](https://github.com/christian-fei/Simple-Jekyll-Search)

