---
title: Complete Feature List
layout: help
show_version: true
---

# Complete CodeFrog Feature List

Browse all CodeFrog features organized by category.

## Table of Contents

{% for category in site.data.features.categories %}
- [{{ category.name }}](#{{ category.name | downcase | replace: ' ', '-' | replace: '/', '' | replace: '&', '' | replace: '---', '-' | replace: '--', '-' }})
{% endfor %}

---

{% for category in site.data.features.categories %}
## {{ category.name }} {#{{ category.name | downcase | replace: ' ', '-' | replace: '/', '' | replace: '&', '' | replace: '---', '-' | replace: '--', '-' }}}

{{ category.description }}

### Features

{% for item in category.items %}
- {{ item }}
{% endfor %}

{% endfor %}

---

## Getting Started

- [Getting Started Guide](/help/mas/getting-started) - Quick start guide for new users (macOS)
- [Windows Setup Guide](/help/windows/windows-setup) - Windows setup and configuration
- [macOS Setup Guide](/help/mas/macos-setup) - Enable Remote Login and Full Disk Access on macOS
- [Project Workflows](/help/common/workflows) - Learn about local and remote development
- [Keyboard Shortcuts](/help/common/shortcuts) - Master CodeFrog's keyboard shortcuts

## Advanced Features

- [Accessibility Testing](/help/common/accessibility) - WCAG AA compliance testing
- [Getting Started with Accessibility](/help/common/getting-started-accessibility) - Quick start guide for accessibility testing
- [Why Accessibility Matters](/help/common/why-accessibility-matters) - Understanding the importance of accessibility for disabled users and screen readers
- [Accessibility Best Practices](/help/common/accessibility-best-practices) - Best practices for accessibility and HTML validation
- [Benefits of Valid HTML and Accessibility](/help/common/benefits-valid-html-accessibility) - SEO, performance, and user experience benefits
- [Security Scanning](/help/common/security) - Comprehensive security validation
- [Mega Report](/help/common/mega-report) - Unified web testing and code analysis report
- [SEO Testing](/help/common/seo-testing) - Complete SEO analysis and optimization
- [OSV / Supply Chain](/help/common/osv) - Open Source Vulnerability detection
- [Secrets Detection](/help/common/secrets) - Gitleaks integration for secrets scanning
- [Code Analysis](/help/common/code-analysis) - Static analysis and code quality metrics
- [Server Management](/help/common/server-management) - SSH server management and SFTP file operations

## AI & Automation

- [GitHub Integration](/help/common/github) - View PRs, import comments as markdown for AI agents
- [CodeRabbit + Augment Workflow](/help/common/ai-coder-coderabbit-augment) - Automated code review workflow
- [Cursor / Other AI Agents](/help/common/ai-coder-cursor) - Using Cursor and other AI tools
- [Handling PRs with Many Comments](/help/common/handling-pr-comments) - Efficiently process large code reviews
- [Recommended Tools & Integrations](/help/common/recommended-tools) - IDEs, cloud services, and tools that work with CodeFrog

## Launch & Quality

- [Launch Checklist](/help/common/launch-checklist) - Pre-launch verification steps
- [Troubleshooting](/help/common/troubleshooting) - Common issues and solutions
- [Windows Troubleshooting](/help/windows/windows-troubleshooting) - Common Windows issues and solutions

---

*Last updated: {{ site.time | date: "%B %Y" }}*

