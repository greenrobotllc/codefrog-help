---
title: Complete Feature List
layout: help
show_version: true
---

# Complete CodeFrog Feature List

This is the authoritative, comprehensive list of all CodeFrog features. Use this page for SEO and as a reference for all available functionality.

## Table of Contents

{% for category in site.data.features.categories %}
- [{{ category.name }}](#{{ category.name | downcase | replace: ' ', '-' | replace: '/', '-' }})
{% endfor %}

---

{% for category in site.data.features.categories %}
## {{ category.name }}

{{ category.description }}

### Features

{% for item in category.items %}
- {{ item }}
{% endfor %}

{% endfor %}

---

## Getting Started

- [Getting Started Guide](/help/mas/getting-started) - Quick start guide for new users
- [Project Workflows](/help/mas/workflows) - Learn about local and remote development
- [Keyboard Shortcuts](/help/mas/shortcuts) - Master CodeFrog's keyboard shortcuts

## Advanced Features

- [Accessibility Testing](/help/mas/accessibility) - WCAG AA compliance testing
- [Getting Started with Accessibility](/help/mas/getting-started-accessibility) - Quick start guide for accessibility testing
- [Why Accessibility Matters](/help/mas/why-accessibility-matters) - Understanding the importance of accessibility for disabled users and screen readers
- [Accessibility Best Practices](/help/mas/accessibility-best-practices) - Best practices for accessibility and HTML validation
- [Benefits of Valid HTML and Accessibility](/help/mas/benefits-valid-html-accessibility) - SEO, performance, and user experience benefits
- [Security Scanning](/help/mas/security) - Comprehensive security validation
- [Mega Report](/help/mas/mega-report) - Unified web testing and code analysis report
- [SEO Testing](/help/mas/seo-testing) - Complete SEO analysis and optimization
- [OSV / Supply Chain](/help/mas/osv) - Open Source Vulnerability detection
- [Secrets Detection](/help/mas/secrets) - Gitleaks integration for secrets scanning

## AI & Automation

- [CodeRabbit + Augment Workflow](/help/mas/ai-coder-coderabbit-augment) - Automated code review workflow
- [Cursor / Other AI Agents](/help/mas/ai-coder-cursor) - Using Cursor and other AI tools

## Launch & Quality

- [Launch Checklist](/help/mas/launch-checklist) - Pre-launch verification steps
- [Troubleshooting](/help/mas/troubleshooting) - Common issues and solutions

---

*Last updated: {{ site.time | date: "%B %Y" }}*

