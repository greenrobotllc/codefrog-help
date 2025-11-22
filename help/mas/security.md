---
title: Security Testing
layout: help
---

## Overview

CodeFrog provides comprehensive security scanning capabilities to help identify vulnerabilities, security misconfigurations, and potential security risks in your codebase.

## HTTPS-First with HTTP Retry

CodeFrog uses an HTTPS-first approach for all network communications:

1. **Primary Attempt:** All requests default to HTTPS
2. **Automatic Retry:** If HTTPS fails, the system automatically retries with HTTP
3. **Security Warning:** HTTP connections are logged with security warnings
4. **Best Practice:** Always prefer HTTPS endpoints when available

This approach ensures maximum security while maintaining compatibility with legacy systems.

## Secrets Detection Basics

CodeFrog integrates with Gitleaks for comprehensive secrets detection. See the [Secrets / Gitleaks page](/help/mas/secrets) for detailed information about:

- What secrets are and why they matter
- How Gitleaks works
- Default exclusion patterns
- Adding custom exclusions
- Exporting and acting on results

## Vulnerability Coverage

The security scanner checks for:

### Common Vulnerabilities

- **SQL Injection:** Unsanitized database queries
- **Cross-Site Scripting (XSS):** Unescaped user input
- **Command Injection:** Unsafe command execution
- **Path Traversal:** Directory traversal vulnerabilities
- **Insecure Dependencies:** Known vulnerable packages
- **Hardcoded Credentials:** Secrets in code
- **Weak Cryptography:** Outdated or weak encryption

### Severity Levels

Vulnerabilities are categorized by severity:

- **Critical:** Immediate action required, potential for data breach
- **High:** Should be addressed soon, significant security risk
- **Medium:** Moderate risk, should be planned for remediation
- **Low:** Minor risk, consider fixing in next update
- **Info:** Informational findings, not necessarily vulnerabilities

**Note:** The scanner includes zero-count severities in reports, meaning if no issues are found in a category, it will still be listed as "0 Critical, 0 High, etc." This helps verify that all categories were scanned.

## Excluding Third-Party Code

By default, CodeFrog excludes common third-party directories from security scans:

- **Pods/** - CocoaPods dependencies
- **node_modules/** - npm dependencies
- **vendor/** - Vendor libraries
- **builds/** - Build artifacts
- **dist/** - Distribution files
- ***.log** - Log files

This prevents false positives from dependencies you don't control and speeds up scans.

### Custom Exclusions

You can add custom exclusion patterns:

1. Open Project Settings
2. Navigate to Security Settings
3. Add exclusion patterns:
   - File extensions: `*.min.js`, `*.bundle.js`
   - Directory paths: `legacy/`, `third-party/`
   - Specific files: `config/old-secrets.json`

## Bulk Scanning

### Scan First N Unscanned Files

For large codebases, you can perform incremental scans:

1. Select "Scan First N Unscanned" option
2. Specify the number of files (e.g., 100, 500, 1000)
3. The scanner will:
   - Skip files already scanned in previous runs
   - Focus on new or modified files
   - Maintain a scan history database

This is useful for:
- Initial scans of large repositories
- Regular incremental security checks
- CI/CD integration with limited time budgets

## Running Security Scans

1. Open your project in CodeFrog
2. Navigate to the **Analyze** tab
3. Select **Security** from analysis options
4. Configure scan settings:
   - Choose directories to scan
   - Set exclusion patterns
   - Select severity levels to report
5. Click **Run Scan**

## Interpreting Results

### Scan Report Structure

- **Summary:** Total issues by severity
- **File-by-File:** Detailed findings per file
- **Issue Details:** Description, severity, and remediation guidance
- **False Positive Marking:** Mark issues as false positives to exclude from future scans

### Acting on Results

1. **Prioritize by Severity:** Start with Critical and High issues
2. **Review Context:** Understand why the issue was flagged
3. **Verify False Positives:** Mark legitimate false positives
4. **Plan Remediation:** Create tasks or tickets for fixes
5. **Re-scan After Fixes:** Verify issues are resolved

## Export and Integration

Security scan results can be exported for:

- **CI/CD Pipelines:** JSON format for automated checks
- **Issue Tracking:** Import findings as tasks or tickets
- **Compliance Reports:** Formatted reports for audits
- **Team Sharing:** Markdown or HTML reports

## Best Practices

1. **Regular Scans:** Run security scans regularly, not just before launch
2. **Fix Critical Issues Immediately:** Don't delay on critical vulnerabilities
3. **Review Dependencies:** Keep third-party packages updated
4. **Use HTTPS:** Always prefer HTTPS endpoints
5. **Don't Commit Secrets:** Use environment variables or secure storage
6. **Review Exclusion Patterns:** Ensure you're not excluding important code

## Related Topics

- [Secrets / Gitleaks](/help/mas/secrets) - Detailed secrets detection guide
- [OSV / Supply Chain](/help/mas/osv) - Open Source Vulnerability database
- [Launch Checklist](/help/mas/launch-checklist) - Pre-launch security checks

