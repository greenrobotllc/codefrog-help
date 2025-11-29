---
title: Getting Started with Accessibility
layout: help
---

# Getting Started with Accessibility

## Quick Start Guide

This guide will help you get started with accessibility testing in CodeFrog. Follow these steps to begin making your website more accessible.

## Step 1: Run Your First Accessibility Test

1. **Open CodeFrog** and navigate to the **Web Testing** section
2. **Choose your test source**:
   - **Local HTML file**: Select a file from your project
   - **URL**: Enter a localhost, staging, or production URL
   - **Sitemap**: Provide a sitemap URL to test your entire site
3. **Click "Run Accessibility Test"**
4. **Review the results**: CodeFrog will show you all accessibility issues found

## Step 2: Understand the Results

### Severity Levels

Accessibility findings are categorized by severity:

- **Critical**: Must be fixed immediately (e.g., missing form labels, keyboard traps)
- **Serious**: Should be fixed soon (e.g., low contrast, missing alt text)
- **Moderate**: Should be addressed (e.g., improper heading hierarchy)
- **Minor**: Nice to have improvements (e.g., redundant alt text)

### Common First Issues

When you run your first test, you'll likely see:

1. **Missing Alt Text**: Images without descriptive alt attributes
2. **Low Contrast**: Text that doesn't meet WCAG contrast requirements
3. **Missing Form Labels**: Input fields without associated labels
4. **Heading Hierarchy**: Skipped heading levels (H1 → H3)
5. **Missing ARIA Labels**: Interactive elements without proper labels

## Step 3: Fix the Most Critical Issues First

### Priority Fixes

Start with these high-impact fixes:

1. **Add Alt Text to Images**
   ```html
   <!-- Bad -->
   <img src="logo.png">
   
   <!-- Good -->
   <img src="logo.png" alt="CodeFrog logo">
   ```

2. **Label Form Inputs**
   ```html
   <!-- Bad -->
   <input type="email" name="email">
   
   <!-- Good -->
   <label for="email">Email Address</label>
   <input type="email" id="email" name="email">
   ```

3. **Fix Heading Hierarchy**
   ```html
   <!-- Bad: Skipping from H1 to H3 -->
   <h1>Main Title</h1>
   <h3>Subsection</h3>
   
   <!-- Good: Proper hierarchy -->
   <h1>Main Title</h1>
   <h2>Subsection</h2>
   ```

4. **Improve Color Contrast**
   - Use a contrast checker tool
   - Aim for at least 4.5:1 for normal text (WCAG AA)
   - Use 7:1 for AAA compliance

5. **Add ARIA Labels Where Needed**
   ```html
   <!-- Bad -->
   <button>×</button>
   
   <!-- Good -->
   <button aria-label="Close dialog">×</button>
   ```

## Step 4: Test Again

After making fixes:

1. **Re-run the accessibility test** in CodeFrog
2. **Compare results**: See how many issues you've resolved
3. **Focus on remaining issues**: Continue fixing in priority order

## Step 5: Test with Real Tools

Automated testing catches many issues, but manual testing is essential:

### Screen Reader Testing

1. **macOS**: Use VoiceOver (Cmd + F5 to enable)
2. **Windows**: Use NVDA (free) or JAWS (commercial)
3. **iOS**: VoiceOver is built-in
4. **Android**: TalkBack is built-in

### Keyboard Navigation Testing

1. **Disconnect your mouse** (or put it away)
2. **Navigate using only Tab** and arrow keys
3. **Verify**:
   - All interactive elements are reachable
   - Focus indicators are visible
   - Tab order is logical
   - No keyboard traps

## Step 6: Integrate into Your Workflow

### During Development

- Run accessibility tests before committing code
- Fix issues as you build, not after
- Use CodeFrog's real-time feedback

### Before Launch

- Run a comprehensive accessibility scan
- Test with actual screen readers
- Review the [Launch Checklist](/help/mas/launch-checklist)

### Continuous Improvement

- Schedule regular accessibility audits
- Monitor for regressions
- Keep up with WCAG updates

## Common Beginner Mistakes

### 1. Decorative Images

**Mistake**: Adding alt text to decorative images
```html
<!-- Unnecessary -->
<img src="decorative-line.png" alt="Decorative line">
```

**Solution**: Use empty alt text for decorative images
```html
<img src="decorative-line.png" alt="">
```

### 2. Redundant Alt Text

**Mistake**: Repeating information already in text
```html
<p>Click <img src="download.png" alt="Download button"> to download</p>
```

**Solution**: Use empty alt text when context is clear
```html
<p>Click <img src="download.png" alt=""> to download</p>
```

### 3. Generic Link Text

**Mistake**: Using "click here" or "read more"
```html
<a href="/article">Click here</a>
```

**Solution**: Use descriptive link text
```html
<a href="/article">Read our accessibility guide</a>
```

### 4. Color-Only Information

**Mistake**: Conveying information only through color
```html
<span style="color: red">Error</span>
```

**Solution**: Add text or icons
```html
<span style="color: red">⚠️ Error: Please check your input</span>
```

## Quick Reference Checklist

Use this checklist for each page:

- [ ] All images have appropriate alt text
- [ ] All form inputs have labels
- [ ] Heading hierarchy is logical (H1 → H2 → H3)
- [ ] Color contrast meets WCAG AA (4.5:1)
- [ ] All interactive elements are keyboard accessible
- [ ] Focus indicators are visible
- [ ] ARIA labels are used where needed
- [ ] Page can be navigated with keyboard only
- [ ] Tested with a screen reader

## Next Steps

Now that you've started with accessibility:

- [Accessibility Testing Guide](/help/mas/accessibility) - Detailed guide on all accessibility features
- [Why Accessibility Matters](/help/mas/why-accessibility-matters) - Understand the importance
- [Accessibility Best Practices](/help/mas/accessibility-best-practices) - Learn advanced techniques
- [Benefits of Valid HTML and Accessibility](/help/mas/benefits-valid-html-accessibility) - Discover additional benefits

## Resources

- [WCAG 2.1 Quick Reference](https://www.w3.org/WAI/WCAG21/quickref/)
- [WebAIM Contrast Checker](https://webaim.org/resources/contrastchecker/)
- [WAVE Browser Extension](https://wave.webaim.org/extension/)

---

*Accessibility is a journey, not a destination. Start with these basics and gradually improve your site's accessibility over time.*

