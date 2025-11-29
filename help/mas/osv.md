---
title: OSV / Supply Chain Security
layout: help
---

# OSV / Supply Chain Security

## What is OSV?

OSV (Open Source Vulnerabilities) is a distributed vulnerability database that aggregates security advisories from various open source ecosystems. CodeFrog integrates with OSV to help you identify known vulnerabilities in your project dependencies.

## Why OSV Matters

Supply chain attacks are increasingly common. Vulnerable dependencies can:

- Expose your application to known exploits
- Compromise user data
- Lead to compliance violations
- Damage your reputation

OSV helps you stay informed about vulnerabilities affecting your dependencies and provides remediation guidance.

## Supported Ecosystems

CodeFrog's OSV integration supports multiple package ecosystems:

- **npm** - Node.js packages
- **PyPI** - Python packages
- **Maven** - Java packages
- **Go** - Go modules
- **Cargo** - Rust crates
- **NuGet** - .NET packages
- **Composer** - PHP packages
- **RubyGems** - Ruby gems
- **CocoaPods** - iOS/macOS dependencies

## Running OSV Scans

1. Open your project in CodeFrog
2. Navigate to the **Analyze** tab
3. Select **OSV / Supply Chain** from analysis options
4. The scanner will:
   - Detect your project's dependency files (package.json, requirements.txt, etc.)
   - Query the OSV database for known vulnerabilities
   - Match dependencies against vulnerability records
5. Review the results

## Reading Advisories

OSV advisories include:

### Vulnerability Details

- **ID:** Unique OSV identifier (e.g., `GHSA-xxxx-xxxx-xxxx`)
- **Summary:** Brief description of the vulnerability
- **Severity:** CVSS score and severity rating
- **Affected Versions:** Which versions are vulnerable
- **Fixed Versions:** Which versions contain the fix

### Affected Packages

- Package name and ecosystem
- Version ranges affected
- Specific commit or version that introduced/fixed the issue

### References

- CVE numbers (if applicable)
- Links to security advisories
- GitHub security advisories
- Vendor announcements

## Remediation Guidance

### Updating Dependencies

1. **Identify Fixed Versions:** Check the advisory for the minimum safe version
2. **Update Dependency Files:**
   - `package.json` for npm
   - `requirements.txt` or `Pipfile` for Python
   - `pom.xml` for Maven
   - `Cargo.toml` for Rust
   - etc.
3. **Test After Update:** Ensure the update doesn't break functionality
4. **Re-scan:** Verify the vulnerability is resolved

### Pinning Versions

For critical dependencies, consider pinning to specific safe versions:

```json
{
  "dependencies": {
    "vulnerable-package": "1.2.3"  // Pin to safe version
  }
}
```

### Alternative Packages

If a package has unresolved vulnerabilities or is no longer maintained:

1. Search for alternative packages
2. Evaluate security track record
3. Plan migration strategy
4. Update gradually to minimize risk

## Interpreting Scan Results

### Vulnerability Report Structure

- **Critical:** Immediate action required
- **High:** Address soon
- **Medium:** Plan for remediation
- **Low:** Consider fixing
- **Unknown:** Severity not yet determined

### False Positives

Some vulnerabilities may be false positives:

- **Development Dependencies:** Vulnerabilities in dev-only packages may not affect production
- **Unused Features:** Vulnerabilities in unused code paths
- **Mitigated Risks:** Issues already addressed through other means

Mark false positives to exclude them from future scans.

## Best Practices

1. **Regular Scans:** Run OSV scans regularly, especially after dependency updates
2. **Automate in CI/CD:** Integrate OSV scanning into your build pipeline
3. **Stay Updated:** Keep dependencies updated to latest safe versions
4. **Review Advisories:** Don't just update blindly—understand the vulnerability
5. **Test After Updates:** Always test after updating dependencies
6. **Monitor for New Vulnerabilities:** Set up alerts for new advisories affecting your dependencies

## Integration with Other Tools

OSV scans complement other security tools:

- **Security Scans:** OSV focuses on dependencies, while security scans check your code
- **Secrets Detection:** Gitleaks finds secrets, OSV finds vulnerable packages
- **Accessibility:** Different concern, but part of overall quality

## Export and Reporting

OSV scan results can be exported for:

- **Compliance Reports:** Document vulnerability management
- **Security Audits:** Show due diligence in dependency management
- **Team Communication:** Share findings with development team
- **CI/CD Integration:** Automated vulnerability checks

## Related Topics

- [Security Testing](/help/mas/security) - Comprehensive security scanning
- [Secrets Detection](/help/mas/secrets) - Finding secrets in code
- [Launch Checklist](/help/mas/launch-checklist) - Pre-launch security verification

