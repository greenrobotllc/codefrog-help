---
title: Code Analysis Tools and Features
redirect_from:
  - /help/code-analysis.php
  - /help/code-analysis.php?flavor=mas
  - /help/common/code-analysis.php
layout: help
---

# Code Analysis

CodeFrog's Code Analysis feature provides comprehensive code quality and security analysis for your codebase. It combines static analysis, line counting, secrets detection, and dependency vulnerability scanning to give you a complete picture of your code's health.

## Overview

Code Analysis helps you:

- **Measure Code Quality**: Get metrics on code size, complexity, and structure
- **Find Security Issues**: Detect secrets, vulnerabilities, and security anti-patterns
- **Track Dependencies**: Identify vulnerable packages and outdated dependencies
- **Improve Codebase**: Get actionable insights for code improvements

## Accessing Code Analysis

**Access**: Navigation → **Analyze** (requires open project)

Code Analysis requires an open project in CodeFrog. You can analyze both local projects and remote projects (via SSH), though local projects provide the best performance and most complete results.

## Features

### Line Counting

CodeFrog provides intelligent line counting with automatic exclusions for build artifacts and generated files:

- **Smart Exclusions**: Automatically excludes common build directories:
  - `Pods/` (iOS/macOS dependencies)
  - `.dart_tool/` (Flutter build artifacts)
  - `build/`, `dist/`, `out/` (compiled outputs)
  - `node_modules/` (Node.js dependencies)
  - `.git/` (version control)
  - Log files and temporary files
- **Language Detection**: Identifies code files by extension
- **Accurate Metrics**: Provides real code size metrics, not inflated by dependencies

### Static Analysis

CodeFrog integrates with industry-standard static analysis tools to find code quality issues and security vulnerabilities:

- **Semgrep Integration**: Advanced static analysis for multiple languages
- **Security Patterns**: Detects common security anti-patterns
- **Code Quality**: Identifies code smells and best practice violations
- **Multi-Language Support**: Works with JavaScript, TypeScript, Python, Java, Go, and more

#### What Static Analysis Finds

- **Security Vulnerabilities**: SQL injection, XSS, insecure deserialization, and more
- **Code Quality Issues**: Unused variables, dead code, complexity issues
- **Best Practice Violations**: Missing error handling, improper use of APIs
- **Performance Issues**: Inefficient algorithms, memory leaks

### Secrets Detection

CodeFrog uses Gitleaks to scan your codebase for accidentally committed secrets:

- **API Keys**: Detects exposed API keys and tokens
- **Passwords**: Finds hardcoded passwords
- **Credentials**: Identifies database credentials and connection strings
- **Private Keys**: Detects SSH keys and certificates

See [Secrets Detection](/help/common/secrets) for detailed information on secrets scanning.

### OSV Integration

CodeFrog integrates with the Open Source Vulnerabilities (OSV) database to scan your dependencies:

- **Dependency Scanning**: Automatically detects dependency files: `pubspec.lock`, `package-lock.json` (v1–v3), `requirements.txt`, and `composer.lock`. The scanner relies on lock files with pinned versions rather than source manifests.
- **Vulnerability Matching**: Matches dependencies against known vulnerabilities
- **Remediation Guidance**: Provides information on fixed versions and patches

See [OSV / Supply Chain Security](/help/common/osv) for detailed information on vulnerability scanning.

## Running Code Analysis

### Basic Analysis

1. **Open Your Project**: Ensure a project is open in CodeFrog
2. **Navigate to Analyze**: Click **Analyze** in the navigation menu
3. **Select Analysis Type**: Choose which analyses to run:
   - Line Counting
   - Static Analysis (Semgrep)
   - Secrets Detection (Gitleaks)
   - OSV Vulnerability Scanning
4. **Run Analysis**: Click the run button to start analysis
5. **Review Results**: View findings organized by severity and type

### Analysis Options

You can run individual analyses or combine them:

- **Quick Scan**: Line counting only (fastest)
- **Security Scan**: Secrets + OSV + Static Analysis (security-focused)
- **Full Analysis**: All analyses combined (comprehensive)

## Interpreting Results

### Severity Levels

Findings are categorized by severity:

- **Critical**: Immediate security risks requiring urgent attention
- **High**: Significant issues that should be addressed soon
- **Medium**: Issues that should be planned for remediation
- **Low**: Minor issues or suggestions for improvement
- **Info**: Informational findings or best practice recommendations

### Result Categories

#### Line Counting Results

- Total lines of code
- Files analyzed
- Languages detected
- Excluded files/directories

#### Static Analysis Results

Each finding includes:

- **Location**: File path and line number
- **Rule**: The static analysis rule that triggered the finding
- **Message**: Description of the issue
- **Severity**: Critical, High, Medium, Low, or Info
- **Recommendation**: Suggested fix or improvement

#### Secrets Detection Results

Each secret finding includes:

- **Secret Type**: What kind of secret was found (API key, password, etc.)
- **Location**: File path and line number
- **Snippet**: Code snippet showing where the secret appears
- **Recommendation**: How to fix the issue (rotate keys, use environment variables, etc.)

#### OSV Vulnerability Results

Each vulnerability includes:

- **Vulnerability ID**: OSV identifier (e.g., GHSA-xxxx-xxxx-xxxx)
- **Package**: Affected package name
- **Severity**: CVSS score and severity rating
- **Affected Versions**: Which versions are vulnerable
- **Fixed Versions**: Which versions contain the fix
- **References**: Links to advisories and CVE numbers

## Best Practices

### Regular Analysis

- **Run Before Commits**: Check for secrets and critical issues before committing
- **CI/CD Integration**: Integrate code analysis into your build pipeline
- **Scheduled Scans**: Run full analysis regularly (weekly or monthly)

### Addressing Findings

1. **Prioritize by Severity**: Fix critical and high-severity issues first
2. **Review Context**: Understand why a finding was flagged before fixing
3. **Test After Fixes**: Verify that fixes don't introduce new issues
4. **Update Dependencies**: Keep dependencies updated to avoid vulnerabilities

### False Positives

Some findings may be false positives:

- **Development Dependencies**: Vulnerabilities in dev-only packages may not affect production
- **Unused Code**: Issues in unused code paths may not be exploitable
- **Mitigated Risks**: Issues already addressed through other means

Mark false positives to exclude them from future scans.

## Integration with Mega Report

Code Analysis is integrated into CodeFrog's Mega Report, which combines:

- **Web Testing**: Accessibility, security headers, SEO, HTML validation
- **Code Analysis**: Secrets detection, OSV vulnerabilities, static analysis

Running a Mega Report gives you a comprehensive view of both your web application and codebase health in a single report with an overall A-F health grade.

See [Mega Report](/help/common/mega-report) for more information.

## Export and Reporting

Code Analysis results can be exported for:

- **Team Communication**: Share findings with your development team
- **Compliance Reports**: Document code quality and security posture
- **CI/CD Integration**: Automated quality gates
- **Historical Tracking**: Compare results over time

## Limitations

### Project Requirements

- **Requires Open Project**: Code Analysis requires a project to be open
- **Local vs. Remote**: Local projects provide better performance and more complete results
- **File Access**: Analysis requires read access to project files

### Analysis Scope

- **Language Support**: Static analysis supports multiple languages, but coverage varies
- **Large Codebases**: Very large codebases may take longer to analyze
- **Network Dependencies**: OSV scanning requires internet connectivity

## Troubleshooting

### Analysis Not Running

- **Check Project Status**: Ensure a project is open and accessible
- **Verify File Access**: Check that CodeFrog has access to project files
- **Network Connection**: OSV scanning requires internet connectivity

### Missing Results

- **Check Analysis Selection**: Ensure the desired analyses are enabled
- **Review Exclusions**: Check if files are being excluded unintentionally
- **File Permissions**: Verify CodeFrog has read access to project files

### Slow Performance

- **Large Codebases**: Consider running analyses separately instead of all at once
- **Network Issues**: OSV scanning may be slow with poor connectivity
- **Resource Usage**: Close other applications to free up system resources

## Related Topics

- [OSV / Supply Chain Security](/help/common/osv) - Dependency vulnerability scanning
- [Secrets Detection](/help/common/secrets) - Finding secrets in code
- [Mega Report](/help/common/mega-report) - Comprehensive testing and analysis
- [Project Workflows](/help/common/workflows) - Setting up projects for analysis

