---
title: Frequently Asked Questions
layout: help
---

## Web Testing

### Why is my web testing request being blocked?

Some websites block automated testing tools. CodeFrog identifies itself transparently as `CodeFrog/1.0.0 (Web Testing Tool; +https://codefrog.app)` rather than impersonating a browser. This is the ethical approach, but some sites may still block automated access.

**Solutions:**
- Try the full URL path (e.g., `https://www.microsoft.com/en-us/` instead of `microsoft.com`)
- Check if the site requires authentication or has specific bot policies
- Use the accessibility test instead (it uses a real browser via Puppeteer/Playwright)
- Configure a custom User-Agent in Web Testing options (see [Privacy page](/help/mas/privacy) for details)

### Why does accessibility testing work but meta tags testing doesn't?

Accessibility testing uses a real browser (Puppeteer/Playwright) which behaves like a normal user visit, while meta tags testing uses a simple HTTP client. Some sites block simple HTTP clients but allow real browsers.

**Solutions:**
- Use accessibility testing for sites that block automated tools
- Try the full URL with path (e.g., `https://www.example.com/page` instead of `https://example.com`)
- Check the site's robots.txt or terms of service

### How do I test local development URLs (like `http://codefrog.local`)?

In the Mega Report dialog, check the "Local development URL (vhost)" checkbox. This relaxes URL validation to allow local development vhosts that don't have a TLD (top-level domain).

**Note:** Local URLs are validated but not checked for reachability, since they may require specific network configuration or VPN access.

### What's the difference between HTML Validation and Meta Tags testing?

- **HTML Validation:** Checks HTML markup for syntax errors, missing tags, and structural issues
- **Meta Tags Testing:** Analyzes Open Graph and Twitter Card metadata for social sharing optimization

Both are useful for SEO and social media sharing, but they test different aspects of your website.

### How do I export web testing results?

- **Individual Tests:** Use the "Export" button in each test tab (Markdown format)
- **Mega Report:** Export comprehensive reports in Markdown, HTML, or PDF format
- **PDF Exports:** Open automatically in your system's default PDF viewer (Preview on macOS)
- **Markdown Exports:** Open in a new CodeFrog window for editing

## Security Scanning

### What permissions do I need for Linode security scanning?

For Linode API integration, you need a Personal Access Token (PAT) with:
- **Domains: Read-Only** (to discover domains)
- **Linodes: Read-Only** (to discover Linode instances)
- **Account: Read-Only** (recommended for token validation)

**Important:** The token is validated before saving. If validation fails, check:
- Token permissions are correct
- Token hasn't expired
- Token hasn't been revoked

### Why do I need to authorize security testing?

Security scanning can be used maliciously. CodeFrog requires explicit authorization to ensure you're only testing sites you own or have permission to test. This protects both you and website owners.

### Can I scan sites that require authentication?

Currently, CodeFrog's web testing features don't support authentication headers or cookies. For authenticated sites:
- Use the accessibility test (it may work if you're logged in via browser)
- Consider testing the public-facing pages only
- Future versions may support authentication headers

## Accessibility Testing

### Why does accessibility testing require SSH on macOS?

On Mac App Store builds, accessibility testing uses a localhost SSH workaround to run Puppeteer/Playwright. This is required due to macOS App Sandbox restrictions.

**Setup:**
1. Enable Remote Login in System Settings > General > Sharing
2. CodeFrog will automatically connect to `localhost` when needed
3. No manual SSH configuration required

### Can I test local HTML files?

Yes! Use the file picker in the Accessibility tab to select local HTML files. The test will run on the file content without requiring network access.

## Mega Report

### What's included in a Mega Report?

A Mega Report combines results from:
- **Code Analysis:** Secrets detection, supply chain vulnerabilities, static analysis
- **Web Testing:** Accessibility, security scanning, meta tags, HTML validation, SEO testing
- **Sitemap Mode:** Tests multiple URLs from a sitemap.xml file

### How do I test multiple URLs at once?

Use **Sitemap Mode** in the Mega Report:
1. Enter your sitemap URL (e.g., `https://example.com/sitemap.xml`)
2. Set the maximum number of URLs to test
3. CodeFrog will discover URLs from the sitemap and test them

### Why are some results missing from PDF export?

PDF exports use automatic pagination. If you see only one page:
- Check if the report is very large (hundreds of errors)
- Try exporting to Markdown or HTML for full results
- The on-screen view always shows complete results

## General

### How do I configure a custom User-Agent?

In Web Testing options, you can provide a custom User-Agent string. However, CodeFrog's default transparent identification (`CodeFrog/1.0.0 (Web Testing Tool)`) is recommended for ethical testing.

**Note:** Using a browser-like User-Agent to bypass bot detection may violate website terms of service.

### Why does CodeFrog need internet access?

CodeFrog only connects to external services when you use specific features:
- **Web Testing:** Fetches web pages for analysis
- **W3C Validator:** Validates HTML (optional)
- **OSV Database:** Checks for vulnerabilities
- **GitHub:** Pull requests and repository integration
- **Linode/Hetzner:** Server management (optional)

You can use CodeFrog entirely offline for local projects and code analysis.

### How do I troubleshoot connection issues?

1. **Check your internet connection**
2. **Verify the URL is correct** (include `https://` or `http://`)
3. **Check if the site is blocking automated tools** (try accessibility test instead)
4. **Review error messages** - they often indicate the specific issue
5. **Check firewall/VPN settings** - some corporate networks block certain requests

### Can I use CodeFrog without a project open?

Yes! Many features work without a project:
- **Web Testing:** All features work standalone
- **Accessibility Testing:** Works with URLs or local files
- **Bulk Security Scanner:** Independent of projects
- **Mega Report:** Can test URLs directly

Some features require a project:
- **Code Analysis:** Needs project files to scan
- **GitHub Integration:** Needs project context for PRs

### How do I report a bug or request a feature?

- **Support:** [Contact Support](https://greenrobot.freshdesk.com/support/solutions/9000119001)
- **GitHub:** Open an issue on the repository (if public)
- **Email:** Check the support portal for contact information

## Privacy & Security

### What data does CodeFrog send to external services?

See the [Privacy & External Connections](/help/mas/privacy) page for complete details. CodeFrog only sends data when you explicitly use features, and your code is never sent without your action.

### Are my API keys secure?

Yes! API keys are stored using Flutter Secure Storage, which uses:
- **macOS:** Keychain (Apple's secure storage)
- **Encryption:** AES-GCM for sensitive data
- **No Plain Text:** Keys are never stored unencrypted

### Can I use CodeFrog offline?

Yes! Many features work offline:
- **Code Analysis:** Local static analysis, secrets detection
- **File Editing:** All editor features
- **Project Management:** Local project operations
- **Accessibility Testing:** With local HTML files

Features that require internet:
- **Web Testing:** Needs to fetch web pages
- **Vulnerability Scanning:** Needs OSV database access
- **GitHub Integration:** Needs GitHub API access

---

**Still have questions?** [Contact Support](https://greenrobot.freshdesk.com/support/solutions/9000119001) or check the [Troubleshooting](/help/mas/troubleshooting) page.

