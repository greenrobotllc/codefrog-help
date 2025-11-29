---
title: Accessibility Testing
layout: help
---

## Overview

CodeFrog includes comprehensive accessibility testing tools designed to help you meet WCAG AA (Web Content Accessibility Guidelines Level AA) standards. These tools help identify and fix accessibility issues before your app or website goes live.

## Purpose

Accessibility testing ensures your application is usable by people with disabilities, including:

- Visual impairments (blindness, low vision, color blindness)
- Motor impairments (limited dexterity, keyboard-only navigation)
- Cognitive impairments (attention disorders, learning disabilities)
- Hearing impairments (deafness, hard of hearing)

Meeting WCAG AA standards is not just good practice—it's often required by law in many jurisdictions.

## How to Run Accessibility Tests

1. Open your project in CodeFrog
2. Navigate to the **Analyze** tab
3. Select **Accessibility** from the analysis options
4. Choose the files or directories to scan
5. Click **Run Analysis**

The accessibility scanner will check:

- Color contrast ratios (text vs. background)
- Keyboard navigation support
- ARIA attributes and roles
- Focus management
- Screen reader compatibility
- Alt text for images
- Semantic HTML structure

## Interpreting Results

### Color Contrast

The scanner reports contrast ratios for all text elements:

- **AA Standard:** 4.5:1 for normal text, 3:1 for large text
- **AAA Standard:** 7:1 for normal text, 4.5:1 for large text

Results show:
- ✅ Pass: Meets or exceeds AA standards
- ⚠️ Warning: Close to threshold, consider improving
- ❌ Fail: Below AA standards, must be fixed

### Keyboard Navigation

The scanner verifies:

- All interactive elements are keyboard accessible
- Tab order is logical
- Focus indicators are visible
- No keyboard traps
- Skip links are present where needed

### ARIA Validations

Checks include:

- Proper use of ARIA roles
- ARIA labels and descriptions
- ARIA state attributes (aria-expanded, aria-hidden, etc.)
- Landmark regions (navigation, main, etc.)

## Keyboard and Focus Checks

### Manual Testing

While automated tools catch many issues, manual testing is essential:

1. **Tab Navigation Test:**
   - Use only the Tab key to navigate
   - Verify all interactive elements are reachable
   - Check that focus indicators are visible
   - Ensure tab order is logical

2. **Keyboard Shortcuts:**
   - Test all keyboard shortcuts
   - Verify they work without mouse
   - Check for conflicts with screen readers

3. **Focus Management:**
   - Modal dialogs should trap focus
   - Focus should return to trigger element when modal closes
   - Dynamic content changes should announce to screen readers

## Exporting Results

Accessibility scan results can be exported in multiple formats:

- **Markdown:** Human-readable report
- **JSON:** Machine-readable for CI/CD integration
- **HTML:** Formatted report for sharing

Export options are available from the results screen.

## Troubleshooting

### False Positives

Some automated checks may flag issues that aren't actual problems:

- **Dynamic Content:** Content loaded via JavaScript may not be detected initially
- **Third-Party Components:** External libraries may have their own accessibility features
- **Context-Dependent:** Some checks require understanding of user flow

### Common Issues and Fixes

**Low Contrast:**
- Increase contrast between text and background
- Use color contrast checker tools
- Consider dark mode alternatives

**Missing ARIA Labels:**
- Add `aria-label` or `aria-labelledby` attributes
- Ensure form inputs have associated labels
- Use semantic HTML where possible

**Keyboard Traps:**
- Review focus management in modals
- Ensure Escape key closes dialogs
- Test with keyboard-only navigation

**Missing Focus Indicators:**
- Add visible focus styles (outline, border, etc.)
- Ensure focus indicators meet contrast requirements
- Test in high contrast mode

## Best Practices

1. **Test Early and Often:** Run accessibility scans during development, not just before launch
2. **Combine Automated and Manual Testing:** Automated tools catch many issues, but manual testing is essential
3. **Test with Real Screen Readers:** Use VoiceOver (macOS), NVDA (Windows), or JAWS
4. **Involve Users with Disabilities:** Get feedback from actual users when possible
5. **Follow WCAG Guidelines:** Use the official WCAG 2.1 guidelines as your reference

## Related Topics

- [Getting Started with Accessibility](/help/mas/getting-started-accessibility) - Quick start guide for new users
- [Why Accessibility Matters](/help/mas/why-accessibility-matters) - Learn about the importance of accessibility for disabled users and screen readers
- [Accessibility Best Practices](/help/mas/accessibility-best-practices) - Best practices for accessibility and HTML validation
- [Benefits of Valid HTML and Accessibility](/help/mas/benefits-valid-html-accessibility) - Discover the indirect benefits including SEO, performance, and user experience
- [Building Inclusive Web Applications](https://codefrog.app/docs/accessibility_testing_with_codefrog) - Blog post on accessibility testing with CodeFrog

## Next Steps

- [Launch Checklist](/help/mas/launch-checklist) - Include accessibility in your pre-launch checks
- [Security Testing](/help/mas/security) - Comprehensive security validation
- [Troubleshooting](/help/mas/troubleshooting) - Common issues and solutions

