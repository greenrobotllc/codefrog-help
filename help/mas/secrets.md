---
title: Secrets Detection / Gitleaks
layout: help
---

## Why Secrets Detection Matters

Secrets (API keys, passwords, tokens, certificates) accidentally committed to version control are a major security risk:

- **Public Repositories:** Secrets in public repos are immediately exposed
- **Private Repositories:** Even private repos can be compromised
- **Git History:** Once committed, secrets persist in Git history even if removed
- **Compliance:** Many regulations require protecting sensitive data

CodeFrog integrates Gitleaks to help you find and fix secrets before they cause problems.

## What is Gitleaks?

Gitleaks is an open-source tool that scans Git repositories for secrets and sensitive information. CodeFrog bundles Gitleaks and provides a user-friendly interface for running scans and reviewing results.

## Default Exclusions

Gitleaks is configured to exclude common false positive sources:

### File Extensions

- `*.log` - Log files often contain formatted data that looks like secrets
- `*.min.js` - Minified JavaScript files
- `*.bundle.js` - Bundled JavaScript files

### Directories

- `builds/` - Build artifacts
- `dist/` - Distribution files
- `Pods/` - CocoaPods dependencies
- `node_modules/` - npm dependencies
- `vendor/` - Vendor libraries

### Why Exclude These?

These patterns are excluded because they:
- Often contain false positives
- Are typically not committed to repositories
- Are generated files, not source code
- Would slow down scans unnecessarily

## Adding Custom Exclusions

You can add custom exclusion patterns for your project:

### By File Extension

Add patterns like:
- `*.test.js` - Test files that may contain mock secrets
- `*.example.json` - Example configuration files
- `*.template.*` - Template files

### By Path

Exclude specific directories:
- `legacy/` - Old code that's being phased out
- `third-party/` - Third-party code you don't control
- `docs/examples/` - Documentation examples

### Configuration

1. Open Project Settings
2. Navigate to Security → Secrets Detection
3. Add exclusion patterns:
   - File extensions: One per line, e.g., `*.test.js`
   - Paths: Directory paths relative to project root
4. Save settings

## Running Secrets Scans

1. Open your project in CodeFrog
2. Navigate to the **Analyze** tab
3. Select **Secrets / Gitleaks** from analysis options
4. Configure scan options:
   - Choose directories to scan
   - Review exclusion patterns
   - Select scan depth (current commit vs. full history)
5. Click **Run Scan**

## Interpreting Results

### Secret Types Detected

Gitleaks detects many types of secrets:

- **API Keys:** AWS, Google Cloud, GitHub, etc.
- **Passwords:** Database passwords, service passwords
- **Tokens:** OAuth tokens, JWT tokens, access tokens
- **Private Keys:** SSH keys, SSL certificates
- **Credentials:** Usernames and passwords
- **Connection Strings:** Database connection strings with credentials

### Result Details

Each finding includes:

- **Type:** What kind of secret was detected
- **File:** Location of the secret
- **Line Number:** Exact line where found
- **Snippet:** Code context around the secret
- **Confidence:** How certain Gitleaks is (high/medium/low)

## What to Do When Secrets Are Found

### Immediate Actions

1. **Rotate the Secret:** Immediately revoke and regenerate the exposed secret
2. **Remove from Code:** Delete the secret from the current codebase
3. **Clean Git History:** Use `git filter-branch` or BFG Repo-Cleaner to remove from history
4. **Notify Team:** Inform team members who may have cloned the repository

### Long-Term Prevention

1. **Use Environment Variables:** Store secrets in environment variables, not code
2. **Use Secret Management:** Services like AWS Secrets Manager, HashiCorp Vault
3. **Add to .gitignore:** Ensure secret files are in `.gitignore`
4. **Pre-commit Hooks:** Run Gitleaks before commits
5. **CI/CD Integration:** Scan in your build pipeline

## Export and Next Steps

### Export Options

- **Markdown Report:** Human-readable report for documentation
- **JSON:** Machine-readable for CI/CD integration
- **CSV:** For spreadsheet analysis

### Integration with Task Management

Export findings can be imported as tasks:

1. Export scan results
2. Use the import feature in CodeFrog's task management
3. Create tasks for each secret that needs rotation
4. Track remediation progress

## Best Practices

1. **Scan Regularly:** Don't wait for problems—scan proactively
2. **Scan Before Commits:** Use pre-commit hooks to catch secrets early
3. **Review Exclusions:** Periodically review exclusion patterns to ensure they're appropriate
4. **Rotate Immediately:** If a secret is found, rotate it immediately
5. **Document Secrets:** Keep a secure record of where secrets are stored (outside the repo)
6. **Train Team:** Educate team members about secrets management

## Common False Positives

Some patterns may look like secrets but aren't:

- **Example Values:** `password123`, `test-key`
- **Hashed Values:** SHA-256 hashes (not the original secret)
- **UUIDs:** Random-looking strings that are actually UUIDs
- **Mock Data:** Test data that looks like real secrets

Mark these as false positives to exclude from future scans.

## Related Topics

- [Security Testing](/help/mas/security) - Comprehensive security scanning
- [OSV / Supply Chain](/help/mas/osv) - Dependency vulnerability scanning
- [Launch Checklist](/help/mas/launch-checklist) - Pre-launch security verification

