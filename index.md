---
layout: help
title: Complete Feature List
show_version: true
permalink: /
---

# Complete CodeFrog Feature List

This is the authoritative, comprehensive list of all CodeFrog features. Use this page for SEO and as a reference for all available functionality.

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

- [Getting Started Guide](/help/mas/getting-started) (macOS) or [Getting Started Guide](/help/windows/getting-started) (Windows) - Quick start guide for new users
- [Project Workflows](/help/common/workflows) - Learn about local and remote development
- [Keyboard Shortcuts](/help/common/shortcuts) - Master CodeFrog's keyboard shortcuts

## Advanced Features

- [Accessibility Testing](/help/common/accessibility) - WCAG AA compliance testing
- [Security Scanning](/help/common/security) - Comprehensive security validation
- [OSV / Supply Chain](/help/common/osv) - Open Source Vulnerability detection
- [Secrets Detection](/help/common/secrets) - Gitleaks integration for secrets scanning

## AI & Automation

- [CodeRabbit + Augment Workflow](/help/common/ai-coder-coderabbit-augment) - Automated code review workflow
- [Cursor / Other AI Agents](/help/common/ai-coder-cursor) - Using Cursor and other AI tools

## Launch & Quality

- [Launch Checklist](/help/common/launch-checklist) - Pre-launch verification steps
- [Troubleshooting](/help/common/troubleshooting) - Common issues and solutions

---

*Last updated: {{ site.time | date: "%B %Y" }}*
