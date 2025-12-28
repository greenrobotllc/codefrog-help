---
title: Accessibility Testing
layout: help
---

# Accessibility Testing

CodeFrog includes comprehensive accessibility testing tools designed to help you meet WCAG (Web Content Accessibility Guidelines) standards at all three conformance levels: A, AA, and AAA. These tools help identify and fix accessibility issues before your app or website goes live.

## Overview

Accessibility testing ensures your application is usable by people with disabilities, including:

- Visual impairments (blindness, low vision, color blindness)
- Motor impairments (limited dexterity, keyboard-only navigation)
- Cognitive impairments (attention disorders, learning disabilities)
- Hearing impairments (deafness, hard of hearing)

Meeting WCAG standards is not just good practice—it's often required by law in many jurisdictions. Level AA is typically the target for legal compliance, while Level A is the minimum and Level AAA represents enhanced accessibility.

## Windows Screen Reader Context

When testing accessibility on Windows, it's important to understand how screen readers work:

### Windows Screen Readers

**Windows Narrator** (Built-in):
- Pre-installed on Windows 10/11
- Activate with `Win + Ctrl + Enter`
- Basic screen reading functionality
- Good for initial testing

**NVDA** (NonVisual Desktop Access):
- Free, open-source screen reader
- Download from: https://www.nvaccess.org/
- More advanced than Narrator
- Recommended for comprehensive testing

**JAWS** (Job Access With Speech):
- Commercial screen reader
- Industry standard for professional testing
- Most comprehensive feature set
- Available from: https://www.freedomscientific.com/

### Testing with Screen Readers

When testing your web applications:

1. **Install a Screen Reader**
   - Start with NVDA (free and comprehensive)
   - Or use Windows Narrator for basic testing

2. **Test Navigation**
   - Use keyboard-only navigation (Tab, Arrow keys, Enter)
   - Verify all interactive elements are reachable
   - Check that focus indicators are visible

3. **Test Content Reading**
   - Verify headings are announced correctly
   - Check that form labels are read with inputs
   - Ensure images have descriptive alt text
   - Verify link text is meaningful out of context

4. **Test Forms**
   - Ensure all form fields have labels
   - Verify error messages are announced
   - Check that required fields are indicated

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

- **WCAG AA Standard:** 4.5:1 for normal text, 3:1 for large text
- **WCAG AAA Standard:** 7:1 for normal text, 4.5:1 for large text

Results show:
- Elements that fail contrast requirements
- Current contrast ratio vs. required ratio
- Suggested color adjustments

### Keyboard Navigation

The scanner verifies:
- All interactive elements are keyboard accessible
- Tab order is logical
- Focus indicators are visible
- No keyboard traps (can't escape with keyboard)

### ARIA and Semantic HTML

Checks include:
- Proper use of ARIA labels and roles
- Semantic HTML elements (header, nav, main, etc.)
- Landmark regions for screen reader navigation
- Live regions for dynamic content

## Windows-Specific Testing Notes

### Browser Testing

When testing accessibility in browsers on Windows:

- **Chrome**: Good screen reader support with NVDA/JAWS
- **Edge**: Excellent Narrator integration
- **Firefox**: Good NVDA support
- Test in multiple browsers for comprehensive coverage

### Keyboard Testing

Windows keyboard navigation:
- `Tab`: Move forward through interactive elements
- `Shift + Tab`: Move backward
- `Enter` or `Space`: Activate buttons/links
- `Arrow keys`: Navigate within components (menus, lists)
- `Esc`: Close dialogs/modals

### High Contrast Mode

Test in Windows High Contrast Mode:
1. Settings → Ease of Access → High contrast
2. Enable high contrast theme
3. Verify your application remains usable
4. Check that all content is visible

### Zoom Testing

Test at different zoom levels:
- `Ctrl + Plus`: Zoom in
- `Ctrl + Minus`: Zoom out
- `Ctrl + 0`: Reset zoom
- Verify layout doesn't break and content remains readable

## Best Practices

### During Development

- **Use semantic HTML**: Prefer `<button>` over `<div>` for buttons
- **Provide alt text**: All images need descriptive alt attributes
- **Label forms**: Every input needs an associated label
- **Test early**: Test accessibility as you build, not just at the end
- **Use ARIA wisely**: Don't overuse ARIA - prefer semantic HTML

### Testing Workflow

1. **Automated Testing**: Run CodeFrog's accessibility scanner first
2. **Manual Testing**: Test with actual screen readers
3. **Keyboard Testing**: Navigate entire application with keyboard only
4. **Color Testing**: Check contrast and color-blind accessibility
5. **User Testing**: Get feedback from users with disabilities

## Common Issues and Solutions

### Low Contrast Text

**Problem**: Text doesn't meet contrast requirements

**Solution**: 
- Increase contrast between text and background
- Use darker text on light backgrounds (or vice versa)
- Test with online contrast checkers
- Consider using bold for small text

### Missing Alt Text

**Problem**: Images lack descriptive alt attributes

**Solution**:
- Add meaningful alt text to all images
- Use empty alt (`alt=""`) for decorative images
- Describe the image's purpose, not just what it looks like

### Keyboard Traps

**Problem**: Users can't escape a component with keyboard

**Solution**:
- Ensure `Esc` key closes modals/dialogs
- Provide clear "Close" buttons
- Test tab order within components
- Allow focus to move outside component

### Missing Focus Indicators

**Problem**: Users can't see which element has focus

**Solution**:
- Add visible focus styles (outline, border, etc.)
- Ensure focus indicators meet contrast requirements
- Don't remove default browser focus styles without replacement

## Resources

- [WCAG 2.1 Guidelines](https://www.w3.org/WAI/WCAG21/quickref/)
- [NVDA Screen Reader](https://www.nvaccess.org/)
- [WebAIM Contrast Checker](https://webaim.org/resources/contrastchecker/)
- [ARIA Authoring Practices](https://www.w3.org/WAI/ARIA/apg/)

## Next Steps

- [WCAG Levels Explained](/help/common/wcag-levels) - Understand A, AA, and AAA levels
- [Windows Setup Guide](/help/windows/windows-setup) - Configure CodeFrog on Windows
- [Windows Troubleshooting](/help/windows/windows-troubleshooting) - Solve Windows-specific issues

