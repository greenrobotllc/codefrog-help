---
title: Mega Report - Unified Web Testing & Analysis
redirect_from:
  - /help/mega-report.php
  - /help/mega-report.php?flavor=mas
layout: help
---

# Unified Web Testing and Code Analysis - Mega Report

Mega Report is CodeFrog's all-encompassing web testing and code analysis tool. It combines multiple testing and analysis tools into a single, unified report that runs all tests in parallel for comprehensive coverage.

## Overview

Mega Report is designed to be your one-stop solution for comprehensive website and codebase validation. Instead of running individual tests separately, Mega Report runs everything in parallel and combines all results into a single, easy-to-review report.

### What Makes It "Mega"

- **Unified Testing**: Combines web testing and code analysis in one report
- **Parallel Execution**: All tests run simultaneously for faster results
- **Comprehensive Coverage**: Tests accessibility, security, SEO, code quality, and more
- **Single View**: All results in one place for easy review
- **Export Options**: Export to Markdown for sharing and documentation
- **Report History**: Track and compare results over time

## Web Testing Components

Mega Report includes comprehensive web testing capabilities:

### Accessibility Testing

- **WCAG AA Compliance**: Tests against Web Content Accessibility Guidelines Level AA
- **Automated Scanning**: Uses axe-core for comprehensive accessibility checks
- **Issue Detection**: Identifies accessibility barriers and violations
- **Recommendations**: Provides actionable fixes for accessibility issues

See [Accessibility Testing](/help/mas/accessibility) for detailed guidance.

### Security Testing

- **OWASP-based Checks**: Industry-standard security validation
- **Security Headers**: Validates security headers (CSP, HSTS, X-Frame-Options, X-Content-Type-Options, Referrer-Policy, Permissions-Policy, COOP, COEP, and cookie security flags) to prevent XSS, clickjacking, MITM attacks, and information leakage
- **SSL/TLS Configuration**: Checks certificate validity and configuration
- **Vulnerability Detection**: Identifies common security issues
- **Severity Classification**: Findings categorized by severity (Critical, High, Medium, Low, Info)

Security headers provide defense-in-depth protection by instructing browsers how to handle your site's content. Missing or misconfigured headers leave your site vulnerable to common attacks. See [Security Headers: Why They Matter](/help/mas/security-headers) for detailed information about each header and what it prevents.

See [Security Scanning](/help/mas/security) for detailed security guidance.

### Meta Tags Analysis

- **SEO Meta Tags**: Validates title, description, keywords, and Open Graph tags
- **Social Media Tags**: Checks Twitter Cards and Facebook Open Graph
- **Missing Tags**: Identifies important meta tags that are missing
- **Tag Quality**: Validates tag content and format

### HTML Validation

- **W3C Standards**: Validates HTML against W3C standards using Nu Html Checker
- **Semantic Correctness**: Ensures proper HTML structure
- **Cross-Browser Compatibility**: Identifies markup issues that could cause browser problems
- **Error Reporting**: Detailed error messages with line numbers

### SEO Testing

- **SEO Analysis**: Comprehensive SEO validation and optimization
- **Page Structure**: Validates heading hierarchy and content structure
- **Content Quality**: Analyzes content for SEO best practices
- **Technical SEO**: Checks technical SEO factors

## Code Analysis Components

When you have a project open, Mega Report can also analyze your codebase:

### Secrets Detection (Gitleaks)

- **Secret Scanning**: Detects hardcoded secrets, API keys, and credentials
- **Multiple Formats**: Supports various secret patterns and formats
- **Exclusions**: Automatically excludes build directories, dependencies, and common false positives
- **Severity Levels**: Classifies findings by risk level

See [Secrets Detection](/help/mas/secrets) for detailed information.

### Supply Chain Vulnerabilities (OSV)

- **Dependency Scanning**: Detects vulnerabilities in project dependencies
- **OSV Database**: Uses Open Source Vulnerabilities database
- **Vulnerability Details**: Provides CVE information and remediation guidance
- **Severity Assessment**: Categorizes vulnerabilities by severity

See [OSV / Supply Chain](/help/mas/osv) for detailed information.

### Static Analysis

- **Semgrep**: Advanced static analysis for code quality and security
- **OpenGrep**: Pattern-based code search and analysis
- **Code Quality**: Identifies code smells and potential bugs
- **Best Practices**: Enforces coding standards and best practices

## Running a Mega Report

### Accessing Mega Report

1. **From Welcome Screen**: Click **"Mega Report (Mega)"** button
2. **From Navigation**: Go to **"Generate Mega Report"** in the navigation menu
3. **No Project Required**: Mega Report can run on URLs without an open project (web testing only)
4. **With Project**: Open a project to include code analysis in the report

### Configuration Options

When generating a report, you can configure:

#### Test Target

- **Single URL**: Test a specific webpage
- **Sitemap**: Test multiple URLs from a sitemap
  - Set maximum URLs to test (default: 100)
  - Set timeout per URL (default: 5 minutes)
  - Automatically discovers URLs from sitemap

#### Test Selection

Choose which tests to include:

**Web Testing:**
- ✅ Accessibility Testing
- ✅ Security Testing
- ✅ Meta Tags Analysis
- ✅ HTML Validation
- ✅ SEO Testing

**Code Analysis** (requires open project):
- ✅ Gitleaks (Secrets Detection)
- ✅ OSV (Supply Chain Vulnerabilities)
- ✅ Semgrep (Static Analysis)
- ✅ OpenGrep (Code Search)

#### Authorization

- **Authorization Confirmation**: Confirm you have permission to test the target
- **Ethical Use**: Only test systems you own or have explicit authorization to test

### Report Generation

1. **Enter URL or Sitemap**: Provide the target URL or sitemap URL
2. **Select Tests**: Choose which tests to run (all enabled by default)
3. **Configure Options**: Set max URLs and timeout for sitemap mode
4. **Confirm Authorization**: Check the authorization checkbox
5. **Generate Report**: Click to start the report generation

### During Report Generation

- **Real-time Progress**: See progress for each test section
- **Parallel Execution**: All selected tests run simultaneously
- **Status Updates**: Watch as each test completes
- **Cancel Option**: You can cancel the report if needed

## Understanding Report Results

### Report Structure

The Mega Report presents results in organized sections:

1. **Summary View**: Overview of all findings by severity
2. **Section Details**: Detailed results for each test type
3. **Finding Details**: Individual findings with descriptions and recommendations

### Severity Levels

Findings are categorized by severity:

- **Critical**: Immediate action required (security vulnerabilities, breaking issues)
- **High**: Important issues that should be addressed soon
- **Medium**: Issues that should be addressed in normal development cycle
- **Low**: Minor issues or suggestions for improvement
- **Info**: Informational findings without immediate action required

### Health Score

The report includes an overall health score (A through F) that aggregates findings from all test sections. The grade provides a quick visual assessment of your project's overall health.

#### How Grades Are Calculated

The grade is calculated based on the total count of findings across all sections (accessibility, security, SEO, HTML validation, secrets detection, OSV vulnerabilities, and static analysis). The calculation uses the following thresholds:

- **F**: Any critical findings (1 or more critical issues)
- **D**: More than 5 high severity findings (6+ high issues)
- **C**: Any high findings OR more than 10 medium findings (1+ high OR 11+ medium)
- **B**: Any medium findings OR more than 20 low findings (1+ medium OR 21+ low)
- **A**: No critical, no high, no medium, and low ≤ 20

**Examples:**
- 1 critical finding = **F** (regardless of other findings)
- 6 high findings = **D**
- 1 high finding = **C**
- 11 medium findings (no high) = **C**
- 1 medium finding (no high) = **B**
- 21 low findings (no medium, no high) = **B**
- 0 critical, 0 high, 0 medium, 5 low = **A**

**Important Note on Info Findings:**
- Info findings are counted and displayed in reports
- Most info findings do **NOT** directly affect the A-F grade calculation (the calculation only checks critical, high, medium, and low)
- **OSV (supply chain) findings are treated as real security issues** and are included in grading. OSV findings are mapped to severity based on CVSS scores:
  - CVSS ≥ 9.0 → Critical
  - CVSS ≥ 7.0 → High
  - CVSS ≥ 4.0 → Medium
  - CVSS > 0 (but < 4.0) → Low
  - **OSV entries without CVSS scores (or invalid/≤0 scores) are promoted to High severity** to ensure they are properly prioritized
- Any OSV findings cause that section to fail
- Always review OSV findings carefully, as they represent real security vulnerabilities in your dependencies

#### Understanding Your Grade

- **A (Excellent)**: No critical, high, or medium issues; low issues ≤ 20. Your project is in excellent shape.
- **B (Good)**: Some medium issues or low issues > 20. Good overall, but improvements can be made.
- **C (Needs Improvement)**: High issues present OR medium issues > 10. Significant issues need attention.
- **D (Poor)**: High issues > 5. Multiple high-priority issues require immediate attention.
- **F (Critical)**: Any critical findings present. Critical security or functionality issues must be addressed immediately.

#### Improving Your Grade

1. **Prioritize by Severity**: Start with critical and high issues first
2. **Fix Critical Issues**: Any critical finding results in an F grade
3. **Address High Issues**: More than 5 high issues drops you to D; any high issues drop you to C
4. **Reduce Medium Issues**: More than 10 medium issues drops you to C
5. **Manage Low Issues**: More than 20 low issues drops you to B
6. **Address OSV Findings**: OSV findings are treated as real security issues and are included in grading. Findings without CVSS scores (or invalid scores) are promoted to high severity. Any OSV findings cause that section to fail.
7. **Re-run Report**: After fixing issues, generate a new report to see your improved grade

#### Trend Tracking

Compare grades across multiple reports to track improvement over time. A grade that improves from F → D → C → B → A shows clear progress in addressing issues.

## Exporting Reports

### Export to Markdown

1. **Open Completed Report**: Navigate to the Mega Report screen
2. **Click Export**: Use the "Export Markdown" button
3. **File Location**: Report is saved automatically
4. **Shareable Format**: Markdown format is easy to share and review

### Use Cases for Exported Reports

- **Client Reporting**: Share comprehensive test results with clients
- **Documentation**: Include in project documentation
- **Team Review**: Share with team members for review
- **Compliance**: Use for compliance and audit documentation
- **Historical Record**: Keep records of project health over time

## Report History

### Viewing History

- **Report List**: View all previously generated reports
- **Compare Reports**: Compare results across different time periods
- **Trend Analysis**: See how project health changes over time

### Report Details

Each saved report includes:

- **Timestamp**: When the report was generated
- **Target URL**: What was tested
- **Test Configuration**: Which tests were run
- **Results Summary**: Overall findings and health score
- **Full Results**: Complete detailed findings

## Best Practices

### When to Use Mega Report

- **Pre-Launch Validation**: Comprehensive testing before going live
- **Regular Audits**: Periodic health checks (weekly, monthly)
- **After Major Changes**: Validate after significant updates
- **Client Deliverables**: Generate reports for client review
- **Compliance Checks**: Verify compliance with standards

### Recommended Workflow

1. **Before Launch**: Run full Mega Report with all tests
2. **Address Critical Issues**: Fix all critical and high-severity findings
3. **Re-run Report**: Generate new report to verify fixes
4. **Document Results**: Export and save report for records
5. **Schedule Regular Reports**: Set up periodic reports

### Optimization Tips

- **Selective Testing**: Disable tests you don't need for faster reports
- **Sitemap Mode**: Use sitemap mode for comprehensive site coverage
- **Batch Processing**: Use max URLs limit for large sites
- **Project Context**: Open project for code analysis when needed

## Use Cases

### Pre-Launch Checklist

Run Mega Report before launching to ensure:

- ✅ Accessibility compliance (WCAG AA)
- ✅ Security best practices
- ✅ SEO optimization
- ✅ HTML validity
- ✅ No hardcoded secrets
- ✅ No known vulnerabilities

### Regular Quality Audits

Schedule regular Mega Reports to:

- Track project health over time
- Identify regressions early
- Maintain code quality standards
- Ensure ongoing compliance

### Client Reporting

Generate Mega Reports for:

- Client deliverables
- Project status updates
- Compliance documentation
- Quality assurance reports

### Development Workflow

Integrate Mega Report into your workflow:

- Run after major feature additions
- Validate before merging PRs
- Check staging environments
- Monitor production health

## Limitations

### Code Analysis Requirements

- **Requires Open Project**: Code analysis (Gitleaks, OSV, Semgrep) requires a project to be open
- **Local Projects**: Code analysis works best with local projects
- **Remote Projects**: Code analysis may have limitations with SSH projects

### Sitemap Mode

- **URL Limits**: Set maximum URLs to prevent extremely long reports
- **Timeout Settings**: Configure timeouts to prevent hanging on slow URLs
- **Resource Usage**: Large sitemaps may take significant time and resources

### Network Dependencies

- **Internet Required**: Web testing requires internet connectivity
- **Target Availability**: Target URLs must be accessible
- **Rate Limiting**: Some sites may rate-limit requests

## Troubleshooting

### Report Fails to Start

- **Check Authorization**: Ensure authorization checkbox is checked
- **Verify URL**: Confirm the URL is valid and accessible
- **Check Internet**: Ensure you have internet connectivity
- **Project Status**: For code analysis, ensure project is open and accessible

### Tests Not Completing

- **Timeout Issues**: Increase timeout settings for slow URLs
- **Network Problems**: Check network connectivity
- **Target Availability**: Verify target URLs are accessible
- **Cancel and Retry**: Cancel and restart with adjusted settings

### Missing Code Analysis

- **Open Project**: Code analysis requires an open project
- **Check Project Type**: Ensure project is accessible (local or SSH)
- **Verify Test Selection**: Ensure code analysis tests are enabled

### Export Issues

- **Report Must Complete**: Wait for report to finish before exporting
- **Check Permissions**: Ensure you have write permissions for export location
- **File Path**: Check the file path shown in success message

## Related Guides

- [Accessibility Testing](/help/mas/accessibility) - Detailed accessibility guidance
- [Security Scanning](/help/mas/security) - Security testing details
- [OSV / Supply Chain](/help/mas/osv) - Dependency vulnerability scanning
- [Secrets Detection](/help/mas/secrets) - Secrets scanning with Gitleaks
- [Tools Available](/help/mas/tools) - Overview of all CodeFrog tools
- [Launch Checklist](/help/mas/launch-checklist) - Pre-launch validation steps

## Summary

Mega Report is CodeFrog's comprehensive solution for web testing and code analysis:

- ✅ **Unified Testing**: All tests in one place
- ✅ **Parallel Execution**: Fast, efficient testing
- ✅ **Comprehensive Coverage**: Web testing + code analysis
- ✅ **Easy Review**: Single-page view of all results
- ✅ **Exportable**: Markdown export for sharing
- ✅ **Historical Tracking**: Compare results over time

Whether you're preparing for launch, conducting regular audits, or generating client reports, Mega Report provides the comprehensive testing and analysis you need in a single, unified tool.

