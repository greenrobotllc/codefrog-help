---
title: SEO Testing Tools and Best Practices
layout: help
---

# SEO Testing

CodeFrog's SEO Testing provides comprehensive search engine optimization analysis to help improve your website's visibility and ranking in search results. SEO testing is available as part of the Mega Report and includes validation of sitemaps, robots.txt, meta tags, heading hierarchy, structured data, and more.

## Overview

SEO (Search Engine Optimization) testing helps ensure your website is properly configured for search engines. CodeFrog analyzes multiple SEO factors to provide actionable recommendations for improving your site's search visibility.

### Benefits of SEO Testing

- **Better Search Rankings**: Optimize your site to rank higher in search results
- **Increased Visibility**: More people can discover your website
- **Technical SEO**: Identify and fix technical issues that hurt rankings
- **Content Optimization**: Ensure your content is structured for search engines
- **Mobile-Friendliness**: Verify your site works well on mobile devices

## SEO Features

CodeFrog's SEO testing includes comprehensive analysis of:

### Sitemap.xml Validation

- **Structure Validation**: Verifies sitemap.xml format and structure
- **URL Discovery**: Automatically discovers URLs from sitemap files
- **Completeness Check**: Identifies missing or broken URLs
- **Priority and Frequency**: Validates sitemap metadata

**How it works:**
- Provide a sitemap URL (e.g., `https://example.com/sitemap.xml`)
- CodeFrog parses the sitemap and validates all URLs
- Reports any structural issues or broken links

### Robots.txt Validation

- **Syntax Validation**: Checks robots.txt format and syntax
- **Directive Analysis**: Validates allow/disallow directives
- **Sitemap References**: Verifies sitemap declarations
- **Crawl Rules**: Analyzes crawl delay and user-agent rules

### Meta Tags Optimization

- **Title Tags**: Validates presence and length of title tags
- **Meta Descriptions**: Checks description tags for optimal length
- **Keywords**: Analyzes keyword meta tags (if present)
- **Open Graph Tags**: Validates social media sharing tags
- **Twitter Card Tags**: Checks Twitter Card metadata
- **Canonical URLs**: Verifies canonical link tags

### Heading Hierarchy

- **Structure Validation**: Ensures proper H1-H6 hierarchy
- **Missing Headings**: Identifies pages without proper heading structure
- **Skipped Levels**: Detects improper heading sequences (e.g., H1 → H3)
- **Multiple H1 Tags**: Flags pages with multiple H1 tags (usually should be one)

**Why it matters:**
- Search engines use headings to understand content structure
- Proper hierarchy improves accessibility and SEO
- Screen readers rely on headings for navigation

### Structured Data (Schema.org)

- **Schema Validation**: Checks for valid Schema.org markup
- **Rich Snippets**: Identifies opportunities for rich search results
- **JSON-LD Validation**: Validates JSON-LD structured data
- **Microdata**: Checks microdata markup

### Mobile-Friendliness

- **Responsive Design**: Verifies mobile-responsive layouts
- **Viewport Configuration**: Checks viewport meta tags
- **Touch Targets**: Validates touch-friendly interface elements
- **Mobile Performance**: Analyzes mobile page load times

### Content Quality Analysis

- **Content Length**: Analyzes page content for optimal length
- **Keyword Usage**: Checks keyword density and placement
- **Readability**: Assesses content readability
- **Internal Linking**: Validates internal link structure
- **External Links**: Checks external link quality

### Technical SEO

- **Page Speed**: Analyzes page load times
- **HTTPS**: Verifies secure connections
- **URL Structure**: Validates clean, SEO-friendly URLs
- **Image Optimization**: Checks image alt tags and optimization
- **404 Errors**: Identifies broken links and missing pages

## How to Run SEO Tests

### Via Mega Report

1. **Access Mega Report**
   - From Welcome Screen: Click **"Mega Report (Mega)"**
   - From Navigation: Go to **"Generate Mega Report"**

2. **Configure Test Target**
   - **Single URL**: Enter a specific webpage URL
   - **Sitemap Mode**: Provide a sitemap URL to test multiple pages
     - Set maximum URLs to test (default: 100)
     - Set timeout per URL (default: 5 minutes)

3. **Select Tests**
   - Under **Web Testing**, ensure **SEO Testing** is checked ✅
   - You can also include other tests (Accessibility, Security, Meta Tags, HTML Validation)

4. **Generate Report**
   - Click **"Generate Report"**
   - CodeFrog will run all selected tests
   - Results appear as they complete

### Sitemap Mode

For comprehensive site-wide SEO analysis:

1. **Provide Sitemap URL**
   - Enter your sitemap URL: `https://example.com/sitemap.xml`
   - CodeFrog automatically discovers all URLs from the sitemap

2. **Configure Limits**
   - **Max URLs**: Set how many URLs to test (recommended: 50-100 for initial scan)
   - **Timeout**: Set timeout per URL (default: 5 minutes)

3. **Benefits of Sitemap Mode**
   - Tests entire site systematically
   - Identifies site-wide SEO issues
   - Provides comprehensive SEO audit
   - Discovers pages you might have forgotten

**Note:** Large sitemaps may take significant time. Start with a lower URL limit and increase as needed.

## Interpreting Results

### SEO Score

The Mega Report provides an overall SEO health grade (A-F) based on:
- Number and severity of SEO issues found
- Critical issues (missing title tags, broken sitemap)
- Warning issues (suboptimal meta descriptions, heading hierarchy)
- Info issues (optimization suggestions)

### Common Issues and Fixes

#### Missing Title Tags
- **Issue**: Page has no `<title>` tag
- **Fix**: Add a descriptive title tag (50-60 characters)
- **Impact**: Critical - search engines need title tags

#### Missing Meta Descriptions
- **Issue**: No meta description tag
- **Fix**: Add compelling meta description (150-160 characters)
- **Impact**: High - affects click-through rates from search results

#### Improper Heading Hierarchy
- **Issue**: Skipped heading levels (H1 → H3)
- **Fix**: Use sequential heading levels (H1 → H2 → H3)
- **Impact**: Medium - affects content structure understanding

#### Missing Sitemap
- **Issue**: No sitemap.xml found
- **Fix**: Create and submit sitemap to search engines
- **Impact**: Medium - helps search engines discover all pages

#### Broken Robots.txt
- **Issue**: Invalid robots.txt syntax
- **Fix**: Correct robots.txt format
- **Impact**: Medium - may prevent proper crawling

#### Missing Structured Data
- **Issue**: No Schema.org markup
- **Fix**: Add appropriate structured data for your content type
- **Impact**: Low - opportunity for rich snippets

## Integration with Mega Report

SEO Testing is part of CodeFrog's comprehensive Mega Report, which combines:

- **Web Testing**: Accessibility, Security, Meta Tags, HTML Validation, SEO
- **Code Analysis**: Secrets Detection, OSV Vulnerabilities, Static Analysis

### Export Options

- **Markdown**: Export full report with all SEO findings
- **HTML**: View report in browser
- **PDF**: Shareable PDF format with all details

### Report History

- Track SEO improvements over time
- Compare reports to see progress
- Identify recurring issues

## Best Practices

### Regular SEO Audits

- Run SEO tests monthly or quarterly
- Track improvements over time
- Address critical issues immediately

### Sitemap Maintenance

- Keep sitemap.xml up to date
- Include all important pages
- Remove deleted pages
- Submit sitemap to Google Search Console

### Meta Tags

- Write unique, compelling titles for each page
- Create descriptive meta descriptions
- Use Open Graph tags for social sharing
- Keep titles under 60 characters
- Keep descriptions under 160 characters

### Heading Structure

- Use one H1 per page
- Maintain logical heading hierarchy
- Use headings to organize content, not for styling
- Make headings descriptive and keyword-rich

### Mobile Optimization

- Ensure responsive design
- Test on actual mobile devices
- Optimize images for mobile
- Minimize page load times

## Related Guides

- [Mega Report](/help/mas/mega-report) - Comprehensive testing and analysis
- [WCAG Levels Explained](/help/mas/wcag-levels) - Understanding WCAG A, AA, and AAA conformance levels
- [Accessibility Testing](/help/mas/accessibility) - WCAG compliance (also affects SEO)
- [Benefits of Valid HTML and Accessibility](/help/mas/benefits-valid-html-accessibility) - SEO benefits of valid HTML
- [Meta Tags Analysis](/help/mas/tools) - Detailed meta tags validation
- [Launch Checklist](/help/mas/launch-checklist) - Pre-launch SEO checks

## Next Steps

- [Mega Report](/help/mas/mega-report) - Run comprehensive SEO analysis
- [Accessibility Testing](/help/mas/accessibility) - Improve accessibility (also helps SEO)
- [Launch Checklist](/help/mas/launch-checklist) - Pre-launch validation
- [Tools Available](/help/mas/tools) - Overview of all CodeFrog tools

