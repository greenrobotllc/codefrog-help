---
title: Accessibility Best Practices
layout: help
---

# Accessibility Best Practices

## Overview

This guide combines best practices for both accessibility and HTML validation to help you build websites that are usable, standards-compliant, and performant.

## HTML Validation Best Practices

### Use Semantic HTML

Semantic HTML helps both accessibility and SEO:

```html
<!-- Bad: Generic divs -->
<div class="header">...</div>
<div class="content">...</div>
<div class="footer">...</div>

<!-- Good: Semantic elements -->
<header>...</header>
<main>...</main>
<footer>...</footer>
```

**Benefits**:
- Screen readers understand page structure
- Search engines better index your content
- Easier to style and maintain

### Proper Heading Hierarchy

Always maintain logical heading order:

```html
<!-- Bad: Skipping levels -->
<h1>Main Title</h1>
<h3>Subsection</h3>

<!-- Good: Sequential hierarchy -->
<h1>Main Title</h1>
<h2>Section</h2>
<h3>Subsection</h3>
```

**Why it matters**:
- Screen reader users navigate by headings
- Search engines use headings to understand content structure
- Creates a clear document outline

### Valid HTML Structure

Ensure your HTML is valid:

- **Close all tags**: Every opening tag needs a closing tag (or be self-closing)
- **Nest properly**: Don't overlap elements incorrectly
- **Use proper DOCTYPE**: `<!DOCTYPE html>` for HTML5
- **Validate regularly**: Use CodeFrog's HTML validation

**Tools**:
- CodeFrog HTML validation
- W3C Markup Validator
- Browser developer tools

## Accessibility Best Practices

### Images and Media

#### Alt Text Guidelines

**Descriptive alt text** for informative images:
```html
<img src="chart.png" alt="Sales increased 25% from Q1 to Q2, shown in a bar chart">
```

**Empty alt text** for decorative images:
```html
<img src="decorative-border.png" alt="">
```

**Functional images** (buttons, links):
```html
<a href="/download">
  <img src="download-icon.png" alt="Download PDF">
</a>
```

#### Video and Audio

- Provide captions for all video content
- Include transcripts for audio content
- Ensure media players are keyboard accessible

### Forms and Inputs

#### Label All Form Fields

```html
<!-- Bad -->
<input type="email" name="email" placeholder="Email">

<!-- Good -->
<label for="email">Email Address</label>
<input type="email" id="email" name="email">
```

#### Group Related Fields

```html
<fieldset>
  <legend>Shipping Address</legend>
  <label for="street">Street</label>
  <input type="text" id="street" name="street">
  <!-- More fields -->
</fieldset>
```

#### Error Messages

- Associate error messages with form fields
- Use `aria-describedby` to link errors to inputs
- Provide clear, actionable error messages

```html
<label for="email">Email</label>
<input type="email" id="email" aria-describedby="email-error">
<span id="email-error" role="alert">Please enter a valid email address</span>
```

### Color and Contrast

#### Minimum Contrast Ratios

- **Normal text**: 4.5:1 (WCAG AA) or 7:1 (WCAG AAA)
- **Large text** (18pt+): 3:1 (WCAG AA) or 4.5:1 (WCAG AAA)
- **UI components**: 3:1 for visual indicators

#### Don't Rely on Color Alone

```html
<!-- Bad: Color only -->
<span style="color: red">Required field</span>

<!-- Good: Color + indicator -->
<span style="color: red">* Required field</span>
```

### Keyboard Navigation

#### All Interactive Elements Must Be Keyboard Accessible

- Links, buttons, form inputs
- Custom widgets and components
- Modal dialogs and dropdowns

#### Focus Management

- **Visible focus indicators**: Users must see where they are
- **Logical tab order**: Follow visual order
- **No keyboard traps**: Users must be able to escape
- **Skip links**: Allow users to skip repetitive content

```html
<!-- Skip to main content -->
<a href="#main-content" class="skip-link">Skip to main content</a>
```

#### Keyboard Shortcuts

- Don't override browser shortcuts
- Provide alternatives for custom shortcuts
- Document all keyboard shortcuts

### ARIA (Accessible Rich Internet Applications)

#### Use ARIA When HTML Isn't Enough

ARIA supplements HTML but doesn't replace it:

```html
<!-- Prefer semantic HTML -->
<button>Close</button>

<!-- Use ARIA when needed -->
<div role="button" tabindex="0" aria-label="Close dialog">×</div>
```

#### Common ARIA Patterns

**Landmarks**:
```html
<nav aria-label="Main navigation">
<main aria-label="Main content">
<aside aria-label="Related articles">
```

**Live Regions**:
```html
<div role="status" aria-live="polite">Item added to cart</div>
<div role="alert" aria-live="assertive">Error: Invalid input</div>
```

**States**:
```html
<button aria-expanded="false" aria-controls="menu">Menu</button>
<div id="menu" aria-hidden="true">...</div>
```

### Dynamic Content

#### Announce Changes to Screen Readers

When content changes dynamically:

```html
<div role="status" aria-live="polite" id="status">
  <!-- Status updates appear here -->
</div>
```

#### Loading States

```html
<button aria-busy="true" aria-label="Loading...">Submit</button>
```

## Combining HTML Validation and Accessibility

### Semantic HTML = Better Accessibility

Valid, semantic HTML is inherently more accessible:

- `<nav>` tells screen readers this is navigation
- `<main>` identifies the main content area
- `<article>` indicates standalone content
- `<section>` groups related content

### Performance Benefits

Valid HTML often means:
- Faster parsing by browsers
- Better caching
- Smaller file sizes
- Improved mobile performance

### SEO Benefits

Search engines favor:
- Valid HTML structure
- Semantic markup
- Proper heading hierarchy
- Descriptive alt text

## Testing Strategy

### Automated Testing

1. **CodeFrog Accessibility Testing**: Run on every build
2. **HTML Validation**: Check before deployment
3. **CI/CD Integration**: Automate in your pipeline

### Manual Testing

1. **Screen Reader Testing**: Use VoiceOver, NVDA, or JAWS
2. **Keyboard Navigation**: Test without a mouse
3. **Browser Testing**: Test across different browsers
4. **Mobile Testing**: Test on actual devices

### User Testing

- Involve users with disabilities
- Get feedback on real-world usage
- Iterate based on user needs

## Common Patterns

### Accessible Modal Dialog

```html
<div role="dialog" aria-modal="true" aria-labelledby="dialog-title">
  <h2 id="dialog-title">Confirm Action</h2>
  <p>Are you sure you want to proceed?</p>
  <button>Cancel</button>
  <button>Confirm</button>
</div>
```

### Accessible Navigation

```html
<nav aria-label="Main navigation">
  <ul>
    <li><a href="/">Home</a></li>
    <li><a href="/about">About</a></li>
    <li><a href="/contact">Contact</a></li>
  </ul>
</nav>
```

### Accessible Form

```html
<form>
  <fieldset>
    <legend>Contact Information</legend>
    <label for="name">Name</label>
    <input type="text" id="name" name="name" required>
    
    <label for="email">Email</label>
    <input type="email" id="email" name="email" required
           aria-describedby="email-help">
    <small id="email-help">We'll never share your email</small>
  </fieldset>
  
  <button type="submit">Submit</button>
</form>
```

## Maintenance

### Regular Audits

- Schedule monthly accessibility reviews
- Run automated tests after major changes
- Keep up with WCAG updates

### Documentation

- Document accessibility decisions
- Maintain a style guide with accessibility guidelines
- Share knowledge with your team

### Continuous Improvement

- Fix issues as you find them
- Don't wait for a major redesign
- Small improvements add up

## Related Resources

- [Getting Started with Accessibility](/help/mas/getting-started-accessibility) - Quick start guide
- [Accessibility Testing Guide](/help/mas/accessibility) - Detailed testing instructions
- [Why Accessibility Matters](/help/mas/why-accessibility-matters) - Understanding the importance
- [Benefits of Valid HTML and Accessibility](/help/mas/benefits-valid-html-accessibility) - Additional benefits

## External Resources

- [WCAG 2.1 Guidelines](https://www.w3.org/WAI/WCAG21/quickref/)
- [MDN Accessibility Guide](https://developer.mozilla.org/en-US/docs/Web/Accessibility)
- [WebAIM Resources](https://webaim.org/resources/)
- [A11y Project Checklist](https://www.a11yproject.com/checklist/)

---

*Following these best practices will help you build websites that are accessible, standards-compliant, and provide a great experience for all users.*

