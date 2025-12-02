---
title: Tools Available
redirect_from:
  - /help/tools.php
  - /help/tools.php?flavor=mas
layout: help
---

# Tools Available

CodeFrog provides a comprehensive suite of development and testing tools. This guide gives you an overview of all available tools and how to access them.

## Server Management & File Operations

**Access**: Welcome screen → **Manage Servers** or Navigation → **Servers**

Connect to and monitor remote servers via SSH with comprehensive SFTP file management:

- **SSH Connections**: Secure connections using RSA 4096-bit keys
- **Real-time Monitoring**: CPU, RAM, and disk usage tracking
- **Terminal Access**: Persistent terminal sessions
- **Connection Pooling**: Efficient connection management
- **Server Health**: Monitor connection status and health
- **File Upload**: Upload files and folders to remote servers (drag and drop or file picker)
- **File Download**: Download files and folders from remote servers (recursive directory downloads)
- **File Operations**: Delete, move, copy, and rename files and folders on remote servers
- **Directory Management**: Create directories, browse remote file systems, view file properties

### Use Cases

- Monitor server resources
- Execute commands remotely
- Manage remote servers
- Debug production issues
- Upload application files and assets to production servers
- Download logs and configuration files
- Organize and manage remote file structures
- Sync files between local and remote environments

## Web Testing

**Access**: Welcome screen → **Web Testing** or Navigation → **Web Testing**

Comprehensive web testing suite for validating websites and web applications:

- **HTML Validation**: W3C standards validation using Nu Html Checker
- **Meta Tags Analysis**: SEO and social media meta tag validation
- **Page Timing Metrics**: Load time and performance analysis
- **Size Analysis**: Page and resource size metrics
- **Accessibility Testing**: WCAG AA compliance scanning with axe-core
- **HTTPS/HTTP Fallback**: Automatic fallback with clear indicators
- **Local & Remote**: Test both local HTML files and live URLs

### Use Cases

- Validate HTML markup
- Check SEO optimization
- Test accessibility compliance
- Analyze page performance
- Verify meta tags

See [Accessibility Testing](/help/mas/accessibility) for detailed accessibility guidance.

## Bulk Security Scanner

**Access**: Welcome screen → **Bulk Security Scanner** or Navigation → **Bulk Security Scanner**

Scan multiple domains concurrently for security vulnerabilities:

- **Concurrent Scanning**: Process multiple targets simultaneously
- **Real-time Results**: Results stream in as each target completes
- **OWASP-based Checks**: Industry-standard security validation
- **Severity Filtering**: Filter by Critical, High, Medium, Low, Info
- **Critical Alerts**: Popup notifications for critical findings
- **Export Options**: JSON, Markdown, and CSV export
- **HTTPS/HTTP Fallback**: Automatic fallback with indicators
- **Incremental Scanning**: "Scan first N unscanned" for large target sets

### Use Cases

- Portfolio security audits
- Multi-site vulnerability scanning
- Security compliance checking
- Regular security monitoring

> **Important**: Only scan systems you own or have explicit authorization to test. See our [Security Scanning Policy](/help/mas/security-scanning-policy) for details.

See [Security Scanning](/help/mas/security) for detailed security guidance.

## Mega Report

**Access**: Welcome screen → **Mega Report (Mega)** or Navigation → **Generate Mega Report**

Unified report combining web testing and code analysis:

- **Comprehensive Testing**: Run all tests in parallel
- **Single Report**: View all results in one place
- **Export to Markdown**: Shareable report format
- **Report History**: Track and compare results over time
- **Detailed Findings**: In-depth analysis of all test results

### Use Cases

- Pre-launch validation
- Regular quality audits
- Comprehensive site analysis
- Client reporting

See [Mega Report - Unified Web Testing and Code Analysis](/help/mas/mega-report) for comprehensive documentation.

## Code Analysis

**Access**: Navigation → **Analyze Code** (requires open project)

Analyze your codebase for quality and security:

- **Line Counting**: Smart exclusions for build artifacts and logs
- **Static Analysis**: Integration with code quality tools
- **Secrets Detection**: Gitleaks integration for secrets scanning
- **OSV Integration**: Open Source Vulnerability detection
- **Exclusions**: Automatically exclude Pods, .dart_tool, build directories

### Use Cases

- Code quality metrics
- Security vulnerability detection
- Dependency analysis
- Codebase statistics

See [OSV / Supply Chain](/help/mas/osv) and [Secrets Detection](/help/mas/secrets) for detailed information.

## GitHub Integration

**Access**: Navigation → **GitHub** (requires open project)

GitHub integration for viewing and importing PR comments and issues:

- **PR Viewing**: View pull requests and comments
- **PR Comment Import**: Import PR comments as markdown for AI agents (Cursor, Augment, etc.)
- **Issue Viewing**: View GitHub issues
- **Issue Import**: Import issues as markdown
- **AI Summaries**: Automatic summaries for PR comments

**Note:** CodeFrog does NOT support git operations (commit, push, pull, diff viewing, branch detection). Use [GitHub Desktop](https://desktop.github.com/) or your preferred Git client for version control.

### Use Cases

- Import PR comments for AI coding assistants
- Bulk process code review feedback
- View and import GitHub issues
- Streamline code review workflows

## Quick Access

All tools are accessible from:

1. **Welcome Screen**: Quick access buttons for main tools
2. **Navigation Menu**: Full list of all available tools
3. **Keyboard Shortcuts**: Fast navigation (see [Shortcuts](/help/mas/shortcuts))

## Tool Combinations

### Recommended Workflows

- **Pre-Launch**: Mega Report + Security Scan + Accessibility Test
- **Regular Audits**: Bulk Security Scanner + Web Testing
- **Code Review**: Code Analysis + GitHub Integration
- **Server Monitoring**: Server Management + Terminal Access

## Next Steps

- [Getting Started](/help/mas/getting-started) - Learn the basics
- [Project Workflows](/help/mas/workflows) - Set up your workflow
- [Security Scanning](/help/mas/security) - Deep dive into security tools
- [WCAG Levels Explained](/help/mas/wcag-levels) - Understanding WCAG A, AA, and AAA conformance levels
- [Accessibility Testing](/help/mas/accessibility) - WCAG compliance guide

