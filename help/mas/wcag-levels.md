---
title: WCAG Levels Explained
layout: help
---

# WCAG Levels Explained

## Overview

The Web Content Accessibility Guidelines (WCAG) define three levels of conformance: **A**, **AA**, and **AAA**. Understanding these levels helps you set appropriate accessibility goals for your projects and interpret CodeFrog's accessibility test results.

## What is WCAG?

WCAG (Web Content Accessibility Guidelines) is an international standard published by the World Wide Web Consortium (W3C) that provides guidelines for making web content accessible to people with disabilities. The current version is WCAG 2.1, with WCAG 2.2 in development.

## The Three Conformance Levels

### Level A: Minimum

Level A represents the **minimum level of accessibility**. Meeting Level A means your website is accessible to some users with disabilities, but may still have significant barriers for others.

**Key Level A Requirements:**
- All images must have alternative text (alt attributes)
- All form inputs must have labels
- Content must be structured with proper headings
- Color cannot be the only means of conveying information
- All functionality must be keyboard accessible
- No content that flashes more than 3 times per second
- Page titles must be descriptive

**When to Target Level A:**
- As a starting point for accessibility improvements
- For internal tools or applications with limited user base
- When beginning your accessibility journey

**Note:** Level A alone is typically not sufficient for legal compliance in most jurisdictions.

### Level AA: Standard (Recommended)

Level AA is the **most commonly targeted conformance level** and is often required by law in many countries, including:
- United States (Americans with Disabilities Act - ADA)
- European Union (EN 301 549)
- Canada (Accessible Canada Act)
- Australia (Disability Discrimination Act)

**Key Level AA Requirements:**
- Text contrast ratio of at least **4.5:1** for normal text
- Text contrast ratio of at least **3:1** for large text (18pt+ or 14pt+ bold)
- All functionality must be accessible via keyboard
- Focus indicators must be visible
- Headings and labels must be descriptive
- Error messages must be clear and helpful
- Content must be readable and understandable
- Navigation must be consistent
- Multiple ways to find content (navigation, search, sitemap)

**When to Target Level AA:**
- For public-facing websites and applications
- When legal compliance is required
- For most commercial and government websites
- As the standard for most projects

**Legal Compliance:** Level AA is typically the target for legal compliance. Many organizations are required to meet WCAG 2.1 Level AA standards.

### Level AAA: Enhanced

Level AAA represents the **highest level of accessibility conformance**. While it's the gold standard, achieving full AAA compliance can be challenging and may not be practical for all content types.

**Key Level AAA Requirements:**
- Text contrast ratio of at least **7:1** for normal text
- Text contrast ratio of at least **4.5:1** for large text
- Sign language interpretation for audio content
- Extended audio descriptions for video content
- No timing constraints (except for real-time events)
- Context-sensitive help available
- Abbreviations explained on first use
- Reading level appropriate for content

**When to Target Level AAA:**
- For high-priority public services
- When maximum accessibility is a core value
- For specific content types (educational materials, government services)
- As an aspirational goal for critical user flows

**Important Limitations:**
- Full AAA conformance requires **manual testing** with assistive technologies
- Some AAA requirements may not be practical for all content types
- Automated tools like CodeFrog can test for many AAA rules, but cannot catch everything

## How CodeFrog Tests WCAG Levels

CodeFrog uses **axe-core**, the industry-leading automated accessibility testing engine, to test your websites for WCAG compliance. Our testing covers all three WCAG levels.

### What Gets Tested

When you run an accessibility scan, CodeFrog tests for violations across:

- **WCAG 2.0 Level A** (`wcag2a` tag)
- **WCAG 2.0 Level AA** (`wcag2aa` tag)
- **WCAG 2.1 Level AA** (`wcag21aa` tag)
- **WCAG 2.1 Level AAA** (`wcag21aaa` tag)

### Understanding WCAG Ratings in Results

After running an accessibility scan, CodeFrog displays a **WCAG Rating** that shows which level your page passes:

- **WCAG A**: No Level A violations found
- **WCAG AA**: No Level A or AA violations found
- **WCAG AAA**: No violations found at any level (A, AA, or AAA)

**Example:**
- If your page has no Level A or AA violations but has some AAA violations, your rating would be **"WCAG AA"**
- If your page has no violations at all, your rating would be **"WCAG AAA"**
- If your page has Level A violations, it does not pass any level

### What CodeFrog Checks

CodeFrog's accessibility testing checks for:

**Color and Contrast:**
- Text contrast ratios (AA: 4.5:1, AAA: 7:1)
- Color-only information without alternative indicators

**Keyboard Navigation:**
- All interactive elements are keyboard accessible
- Logical tab order
- Visible focus indicators
- No keyboard traps

**ARIA and Semantics:**
- Proper use of ARIA roles and attributes
- ARIA labels and descriptions
- Semantic HTML structure
- Proper heading hierarchy

**Images and Media:**
- Alt text for all images
- Captions for video content
- Audio descriptions where required

**Forms:**
- All inputs have associated labels
- Error messages are clear and helpful
- Form validation is accessible

**Document Structure:**
- Proper heading hierarchy (no skipping levels)
- Page landmarks (main, navigation, contentinfo)
- No duplicate IDs

## Interpreting Your Results

### WCAG Rating

The WCAG rating indicates the **highest level your page passes**. This is calculated by:

1. Checking if there are any Level A violations
2. If no Level A violations, checking for Level AA violations
3. If no Level AA violations, checking for Level AAA violations
4. The rating is the highest level with no violations

### Health Score

In addition to the WCAG rating, CodeFrog provides an **A-F health score** based on the severity of findings:

- **A**: No critical, high, or medium issues; low issues ≤ 20
- **B**: Some medium issues or low issues > 20
- **C**: High issues present OR medium issues > 10
- **D**: High issues > 5
- **F**: Any critical findings

The health score and WCAG rating work together to give you a complete picture:
- **WCAG Rating**: Which accessibility standard level you meet
- **Health Score**: Overall quality based on issue severity

### Finding Details

Each finding in your results includes:
- **WCAG Level Tags**: Shows which WCAG level(s) the violation affects
- **Severity**: Critical, High, Medium, Low, or Info
- **Description**: What the issue is and why it matters
- **Remediation**: How to fix the issue
- **Affected Elements**: Selectors or HTML snippets showing where the issue occurs

## Best Practices

### 1. Target Level AA for Most Projects

For most websites and applications, **Level AA is the recommended target** because:
- It meets legal requirements in most jurisdictions
- It provides good accessibility for most users
- It's achievable without being overly restrictive
- It's the industry standard

### 2. Test Early and Often

Run accessibility scans during development, not just before launch:
- Catch issues when they're easier to fix
- Build accessibility into your workflow
- Avoid costly last-minute fixes

### 3. Combine Automated and Manual Testing

While CodeFrog catches many issues automatically, **manual testing is essential**:
- Test with real screen readers (VoiceOver, NVDA, JAWS)
- Test keyboard-only navigation
- Test with users who have disabilities
- Verify that automated fixes actually work

### 4. Prioritize by Severity

When fixing issues:
1. **Critical and High** severity issues first
2. **Level A** violations before Level AA
3. **Level AA** violations before Level AAA
4. Focus on issues that affect the most users

### 5. Understand AAA Limitations

Remember that:
- Full AAA conformance requires manual testing
- Some AAA requirements may not be practical for all content
- Automated tools can only test a portion of AAA criteria
- Focus on AAA for critical user flows, not necessarily entire sites

## Common Questions

### Can I achieve AAA with CodeFrog alone?

No. While CodeFrog can test for many AAA rules, full AAA conformance requires:
- Manual testing with assistive technologies
- Human judgment for some criteria
- Testing with actual users who have disabilities

CodeFrog helps you get close, but manual testing is required for full AAA compliance.

### What if I have AAA violations but pass AA?

That's normal! Your WCAG rating will show **"WCAG AA"** if you have no A or AA violations but some AAA violations. This means you meet the standard level (AA) but not the enhanced level (AAA).

### Should I fix all AAA violations?

Not necessarily. Consider:
- **Priority**: Fix AAA violations in critical user flows
- **Impact**: Focus on violations that affect many users
- **Feasibility**: Some AAA requirements may not be practical for all content
- **Resources**: Balance accessibility goals with other priorities

### How do I know which level to target?

- **Level A**: Starting point, internal tools
- **Level AA**: Most projects, legal compliance, public websites
- **Level AAA**: High-priority services, maximum accessibility goals

## Related Topics

- [Accessibility Testing](/help/mas/accessibility) - How to run accessibility tests in CodeFrog
- [Why Accessibility Matters](/help/mas/why-accessibility-matters) - The importance of accessibility
- [Accessibility Best Practices](/help/mas/accessibility-best-practices) - Tips for improving accessibility
- [Mega Report](/help/mas/mega-report) - Comprehensive testing including accessibility

## External Resources

- [WCAG 2.1 Quick Reference](https://www.w3.org/WAI/WCAG21/quickref/) - Official W3C reference
- [Understanding WCAG 2.1](https://www.w3.org/WAI/WCAG21/Understanding/) - Detailed explanations
- [WebAIM Contrast Checker](https://webaim.org/resources/contrastchecker/) - Test color contrast ratios

