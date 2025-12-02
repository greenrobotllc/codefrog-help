---
title: Launch Checklist
layout: help
---

# Launch Checklist

## Overview

This checklist helps ensure your application is ready for launch. Follow these steps to verify accessibility, security, and overall quality before releasing your app or website.

## Accessibility Steps

### Automated Testing

1. **Run Accessibility Scan:**
   - Navigate to Analyze → Accessibility
   - Scan all user-facing pages/screens
   - Review all findings

2. **Fix Critical Issues:**
   - Address all contrast ratio failures
   - Fix keyboard navigation problems
   - Resolve ARIA validation errors
   - Ensure focus indicators are visible

3. **Manual Testing:**
   - Test with keyboard-only navigation
   - Verify with screen reader (VoiceOver, NVDA, JAWS)
   - Check in high contrast mode
   - Test with browser zoom at 200%

4. **Documentation:**
   - Export accessibility report
   - Keep records for compliance

### WCAG AA Compliance

Verify compliance with WCAG 2.1 Level AA:

- ✅ Color contrast meets 4.5:1 (normal text) or 3:1 (large text)
- ✅ All functionality available via keyboard
- ✅ Focus indicators visible
- ✅ Form labels associated with inputs
- ✅ Error messages identified and described
- ✅ Content structure is logical and semantic

## LaunchDay Checklist

### Pre-Launch Verification

1. **Code Quality:**
   - [ ] All tests passing
   - [ ] Code review completed
   - [ ] No known critical bugs
   - [ ] Performance benchmarks met

2. **Security:**
   - [ ] Security scan completed (see Security Testing below)
   - [ ] Secrets scan completed (see Secrets Testing below)
   - [ ] OSV scan completed (see OSV Testing below)
   - [ ] All vulnerabilities addressed or documented

3. **Documentation:**
   - [ ] User documentation complete
   - [ ] API documentation (if applicable)
   - [ ] Changelog updated
   - [ ] Release notes prepared

4. **Infrastructure:**
   - [ ] Production environment configured
   - [ ] Monitoring and logging set up
   - [ ] Backup procedures in place
   - [ ] Rollback plan prepared

5. **Legal & Compliance:**
   - [ ] Privacy policy updated
   - [ ] Terms of service current
   - [ ] GDPR/CCPA compliance verified (if applicable)
   - [ ] Accessibility statement published

## Testing Features

### Security Testing

Run comprehensive security scans:

1. **Security Scan:**
   - Navigate to Analyze → Security
   - Scan entire codebase
   - Review all findings by severity
   - Fix or document all Critical and High issues

2. **Verify HTTPS:**
   - Ensure all endpoints use HTTPS
   - Test HTTP retry fallback (if applicable)
   - Verify SSL certificate validity

3. **Review Exclusions:**
   - Ensure third-party code is properly excluded
   - Verify custom exclusions are appropriate
   - Don't exclude security-critical code

### Secrets Testing

1. **Run Gitleaks Scan:**
   - Navigate to Analyze → Secrets / Gitleaks
   - Scan entire repository (including history if needed)
   - Review all findings

2. **Verify No Secrets in Code:**
   - Confirm no API keys in code
   - Verify no passwords hardcoded
   - Check no tokens committed
   - Ensure private keys are not in repository

3. **Check Exclusions:**
   - Review default exclusions
   - Verify custom exclusions are appropriate
   - Don't exclude files that might contain real secrets

### OSV Testing

1. **Run OSV Scan:**
   - Navigate to Analyze → OSV / Supply Chain
   - Scan all dependency files
   - Review vulnerability advisories

2. **Update Vulnerable Dependencies:**
   - Identify all Critical and High vulnerabilities
   - Update to safe versions
   - Test after updates
   - Re-scan to verify fixes

3. **Document Unresolved Issues:**
   - If vulnerabilities cannot be immediately fixed, document:
     - Why it cannot be fixed now
     - Mitigation strategies
     - Timeline for resolution

## Code Review Setup

### CodeRabbit Integration

If using CodeRabbit for automated code review:

1. **Configure CodeRabbit:**
   - Set up CodeRabbit in your repository
   - Configure review rules
   - Enable PR comment export

2. **Import PR Comments to Tasks:**
   - Go to the GitHub tab in CodeFrog
   - Click on the PR you want to view
   - Use the PR Import Banner to import comments as tasks
   - Export to Markdown from the Tasks screen (upper right export button)
   - See [CodeRabbit + Augment workflow](/help/mas/ai-coder-coderabbit-augment) for details

3. **Import to Tasks:**
   - Import comments as tasks in CodeFrog
   - Format: `PR#{pr} Comment #{id}: {description}`
   - Hide nitpicks, focus on important issues

### Alternative Code Review Tools

If using other tools (GitHub Code Review, GitLab, etc.):

1. **Export Review Comments:**
   - Collect all unresolved review comments
   - Format as list of issues

2. **Create Tasks:**
   - Manually create tasks for each issue
   - Or use bulk import if available
   - Prioritize by severity

## Final Verification

### Pre-Launch Testing

1. **Functional Testing:**
   - [ ] All features work as expected
   - [ ] No regressions from previous version
   - [ ] Edge cases handled
   - [ ] Error handling works

2. **Performance Testing:**
   - [ ] Load times acceptable
   - [ ] No memory leaks
   - [ ] Database queries optimized
   - [ ] API response times within limits

3. **Cross-Platform Testing:**
   - [ ] Works on target platforms
   - [ ] Browser compatibility (if web app)
   - [ ] Mobile responsiveness (if applicable)

4. **User Acceptance Testing:**
   - [ ] Beta testers have tested
   - [ ] Feedback incorporated
   - [ ] Known issues documented

### Launch Day

1. **Final Checks:**
   - [ ] All checklist items completed
   - [ ] Team notified of launch
   - [ ] Monitoring active
   - [ ] Support team ready

2. **Deployment:**
   - [ ] Deploy to production
   - [ ] Verify deployment successful
   - [ ] Smoke test critical paths
   - [ ] Monitor for issues

3. **Post-Launch:**
   - [ ] Monitor error logs
   - [ ] Watch user feedback
   - [ ] Be ready to rollback if needed
   - [ ] Celebrate! 🎉

## Checklist Export

You can export this checklist as a Markdown file for:

- **Team Sharing:** Share with your team
- **Project Documentation:** Include in project docs
- **Compliance:** Keep records for audits
- **Future Reference:** Use as template for future launches

## Related Topics

- [WCAG Levels Explained](/help/mas/wcag-levels) - Understanding WCAG A, AA, and AAA conformance levels
- [Accessibility Testing](/help/mas/accessibility) - Detailed accessibility guide
- [Security Testing](/help/mas/security) - Comprehensive security scanning
- [OSV / Supply Chain](/help/mas/osv) - Dependency vulnerability scanning
- [Secrets Detection](/help/mas/secrets) - Finding secrets in code
- [CodeRabbit + Augment Workflow](/help/mas/ai-coder-coderabbit-augment) - Automated code review

