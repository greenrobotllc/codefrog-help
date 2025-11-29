---
title: Security Headers - Why They Matter
layout: help
---

# Security Headers: Why They Matter

Security headers are HTTP response headers that tell browsers how to handle your website's content. They provide defense-in-depth protection against common web vulnerabilities like XSS, clickjacking, man-in-the-middle attacks, and information leakage.

## Overview

Without security headers, your website relies on default browser behavior, which is often permissive and can leave you vulnerable to attacks. Security headers act as an additional layer of protection, instructing browsers to enforce security policies that prevent or mitigate common exploits.

CodeFrog checks for the presence and proper configuration of security headers as part of its comprehensive security scanning. This helps identify missing or misconfigured headers that could leave your site vulnerable.

## Why Security Headers Matter

Security headers address **OWASP A05: Security Misconfiguration**, one of the most common security issues. They prevent:

- **Cross-Site Scripting (XSS)** attacks
- **Clickjacking** attacks
- **Man-in-the-Middle (MITM)** attacks
- **Information leakage** through referrers
- **Content type confusion** attacks
- **Cross-origin** information leakage
- **Cookie theft** via XSS

## Headers Checked by CodeFrog

### HSTS (Strict-Transport-Security)

**What it does:** Forces browsers to use HTTPS for all future connections to your site.

**What it prevents:**
- Man-in-the-middle attacks
- Protocol downgrade attacks
- Cookie hijacking over HTTP

**Without it:** Users can be tricked into connecting via HTTP, where their traffic can be intercepted and modified by attackers.

**With it:** Browsers remember to always use HTTPS, even if a user types `http://` or clicks an HTTP link.

**Example configuration:**
```
Strict-Transport-Security: max-age=31536000; includeSubDomains; preload
```

**CodeFrog checks:** Presence of HSTS header on HTTPS responses. Missing HSTS is flagged as **Medium** severity.

---

### X-Content-Type-Options: nosniff

**What it does:** Prevents browsers from MIME-sniffing (guessing) content types.

**What it prevents:**
- Content type confusion attacks
- XSS via incorrectly interpreted content
- Execution of files that should be treated as data

**Without it:** A file like `image.jpg` could be executed as JavaScript if the browser guesses the wrong content type, leading to XSS vulnerabilities.

**With it:** Browsers strictly respect the declared `Content-Type` header and won't try to guess.

**Example configuration:**
```
X-Content-Type-Options: nosniff
```

**CodeFrog checks:** Presence and correct value (`nosniff`). Missing or incorrect value is flagged as **Medium** severity.

---

### Referrer-Policy

**What it does:** Controls how much referrer information is sent to other sites when users click links.

**What it prevents:**
- Information leakage through referrer URLs
- Exposure of sensitive paths, tokens, or user data
- Privacy violations

**Without it:** Full URLs (including query parameters, paths, and tokens) can leak to third-party sites when users click links.

**With it:** You control what referrer information is shared, protecting sensitive data in URLs.

**Example configurations:**
```
Referrer-Policy: strict-origin-when-cross-origin
Referrer-Policy: no-referrer
Referrer-Policy: same-origin
```

**CodeFrog checks:** Presence of Referrer-Policy header. Missing header is flagged as **Low** severity.

---

### X-Frame-Options / CSP frame-ancestors

**What it does:** Prevents your site from being embedded in iframes on other domains.

**What it prevents:**
- Clickjacking attacks
- UI redressing attacks
- Social engineering via embedded content

**Without it:** Attackers can embed your site in an iframe and overlay malicious content, tricking users into clicking buttons they think are safe.

**With it:** Browsers block your site from being framed, preventing clickjacking attacks.

**Example configurations:**
```
X-Frame-Options: DENY
X-Frame-Options: SAMEORIGIN
Content-Security-Policy: frame-ancestors 'none';
Content-Security-Policy: frame-ancestors 'self';
```

**CodeFrog checks:** Presence of either `X-Frame-Options` or CSP `frame-ancestors` directive. Missing protection is flagged as **Medium** severity.

---

### Content-Security-Policy (CSP)

**What it does:** Restricts which sources can load scripts, styles, images, fonts, and other resources.

**What it prevents:**
- XSS attacks via injected scripts
- Data exfiltration
- Unauthorized resource loading
- Code injection attacks

**Without it:** Any malicious script injected into your page can execute, leading to XSS attacks, data theft, and session hijacking.

**With it:** Only resources from allowed sources can load, dramatically reducing the impact of XSS vulnerabilities.

**Example configuration:**
```
Content-Security-Policy: default-src 'self'; script-src 'self' cdn.example.com; style-src 'self' 'unsafe-inline';
```

**Risky configurations CodeFrog flags:**
- `'unsafe-inline'` in `script-src` - **High** severity (allows inline scripts, reducing XSS protection)
- `'unsafe-eval'` in `script-src` - **High** severity (allows `eval()`, dangerous for XSS)
- Wildcard (`*`) sources - **Medium** severity (too permissive)

**CodeFrog checks:** 
- Presence of CSP header - **Medium** severity if missing
- Risky directives (`unsafe-inline`, `unsafe-eval`, wildcards) - **High** or **Medium** severity depending on directive

---

### Permissions-Policy (formerly Feature-Policy)

**What it does:** Controls which browser features (camera, microphone, geolocation, etc.) your site can access.

**What it prevents:**
- Unauthorized access to sensitive browser features
- Privacy violations
- Unintended feature activation

**Without it:** Your site can access sensitive features without explicit user consent, potentially violating user privacy.

**With it:** You explicitly control which features are available, reducing privacy risks and preventing accidental feature activation.

**Example configuration:**
```
Permissions-Policy: geolocation=(), camera=(), microphone=(), payment=()
```

**CodeFrog checks:** 
- Presence of Permissions-Policy header - **Medium** severity if missing
- Overly permissive policies (wildcards for sensitive features) - **High** severity

---

### Cross-Origin-Opener-Policy (COOP)

**What it does:** Isolates your browsing context from cross-origin windows.

**What it prevents:**
- Cross-origin information leakage
- Spectre-style attacks
- Cross-origin window access

**Without it:** Cross-origin windows can access your window object, potentially leaking sensitive information.

**With it:** Your window is isolated from cross-origin windows, preventing information leakage.

**Example configurations:**
```
Cross-Origin-Opener-Policy: same-origin
Cross-Origin-Opener-Policy: same-origin-allow-popups
```

**CodeFrog checks:** 
- Presence of COOP header - **Medium** severity if missing
- `unsafe-none` value - **Medium** severity (provides no protection)

---

### Cross-Origin-Embedder-Policy (COEP)

**What it does:** Requires cross-origin resources to opt in to being embedded.

**What it prevents:**
- Unauthorized resource embedding
- Cross-origin data access

**Without it:** You can't safely use powerful features like `SharedArrayBuffer` that require isolation.

**With it:** When combined with COOP, enables powerful browser features while maintaining security.

**Example configuration:**
```
Cross-Origin-Embedder-Policy: require-corp
Cross-Origin-Embedder-Policy: credentialless
```

**CodeFrog checks:** Presence of COEP header. Missing header is flagged as **Medium** severity (or **Low** if COOP is also missing).

---

### Cookie Security Flags

**What they do:** Control how cookies are transmitted and accessed.

**Flags checked:**
- **Secure:** Cookie only sent over HTTPS
- **HttpOnly:** Cookie not accessible via JavaScript
- **SameSite:** Controls cross-site cookie sending

**What they prevent:**
- Cookie theft via XSS (HttpOnly)
- Cookie transmission over HTTP (Secure)
- CSRF attacks (SameSite)

**Without them:** Cookies can be stolen via XSS attacks, transmitted over insecure connections, or used in CSRF attacks.

**With them:** Cookies are protected from common attack vectors.

**Example configurations:**
```
Set-Cookie: sessionid=abc123; Secure; HttpOnly; SameSite=Strict
Set-Cookie: csrftoken=xyz789; Secure; HttpOnly; SameSite=Lax
```

**CodeFrog checks:**
- Missing `Secure` flag on HTTPS - **Medium** severity
- Missing `HttpOnly` flag - **Low** severity
- `SameSite=None` without `Secure` - **Medium** severity (browser requirement)

---

### Subresource Integrity (SRI)

**What it does:** Verifies that external scripts and stylesheets haven't been tampered with.

**What it prevents:**
- Supply chain attacks
- CDN compromise attacks
- Malicious code injection via third-party resources

**Without it:** If a CDN is compromised, malicious code can be injected into your site via external resources.

**With it:** Browsers verify the cryptographic hash of external resources, preventing tampered code from executing.

**Example configuration:**
```html
<script src="https://cdn.example.com/library.js" 
        integrity="sha384-oqVuAfXRKap7fdgcCY5uykM6+R9GqQ8K/uxy9rx7HNQlGYl1kPzQho1wx4JwY8wC"
        crossorigin="anonymous"></script>
```

**CodeFrog checks:** Presence of `integrity` attribute on external scripts and stylesheets. Missing SRI is flagged as **Medium** severity for scripts, **Low** for stylesheets.

---

## How CodeFrog Checks Security Headers

CodeFrog performs non-invasive, read-only checks of your website's security headers:

1. **Sends HTTP requests** to your site (HEAD/GET)
2. **Analyzes response headers** for security header presence and values
3. **Flags missing or misconfigured headers** with appropriate severity levels
4. **Provides recommendations** for fixing issues

All checks are safe and don't modify your site in any way.

## Severity Levels

CodeFrog categorizes security header findings by severity:

- **Critical:** Immediate security risk (rare for headers)
- **High:** Significant security risk (e.g., unsafe CSP directives)
- **Medium:** Moderate risk (e.g., missing HSTS, CSP, X-Frame-Options)
- **Low:** Minor risk (e.g., missing Referrer-Policy, HttpOnly cookies)
- **Info:** Informational findings

## Implementation Guides

### Quick Setup Options

- **Cloudflare:** Add security headers via Transform Rules (see [Cloudflare Security Headers Guide](/help-setup/CLOUDFLARE_SECURITY_HEADERS))
- **Apache:** Use `.htaccess` or server configuration
- **Nginx:** Add headers in server block configuration
- **Application-level:** Set headers in your application code

### Testing Your Headers

After implementing security headers:

1. Run CodeFrog's security scan on your site
2. Check results for any remaining issues
3. Verify headers are present using browser DevTools (Network tab)
4. Test with [SecurityHeaders.com](https://securityheaders.com) for additional validation

## Best Practices

1. **Start with high-priority headers:** HSTS, CSP, X-Frame-Options, X-Content-Type-Options
2. **Test thoroughly:** Some headers can break functionality if misconfigured
3. **Use CSP Report-Only first:** Test CSP in report-only mode before enforcing
4. **Keep headers updated:** Review and update headers as your site evolves
5. **Monitor regularly:** Run security scans regularly to catch regressions

## Common Issues

### CSP Breaking Functionality

If CSP breaks your site:
- Start with `Content-Security-Policy-Report-Only` to test
- Gradually tighten policies
- Use nonces or hashes for inline scripts/styles
- Review CSP violation reports

### HSTS Preload Requirements

To add your site to HSTS preload:
- Include `preload` directive
- Set `max-age` to at least 31536000 (1 year)
- Include all subdomains with `includeSubDomains`
- Submit to [hstspreload.org](https://hstspreload.org)

### Cookie SameSite Issues

If cookies stop working:
- `SameSite=Strict` blocks all cross-site requests
- `SameSite=Lax` allows top-level navigation
- `SameSite=None` requires `Secure` flag

## Related Topics

- [Security Scanning](/help/mas/security) - Comprehensive security testing guide
- [What We Check](https://codefrog.app/what-we-check) - Complete list of security checks
- [OWASP Coverage](https://codefrog.app/owasp-coverage) - How CodeFrog maps to OWASP Top 10
- [Mega Report](/help/mas/mega-report) - Unified security and quality testing

## Summary

Security headers are a critical defense-in-depth mechanism that prevent real-world attacks:

- ✅ **HSTS** prevents MITM attacks
- ✅ **CSP** reduces XSS impact
- ✅ **X-Frame-Options** prevents clickjacking
- ✅ **X-Content-Type-Options** prevents content type confusion
- ✅ **Cookie flags** prevent cookie theft and CSRF
- ✅ **Other headers** provide additional layers of protection

CodeFrog helps you identify missing or misconfigured headers so you can secure your site effectively. Regular security scans ensure your headers remain properly configured as your site evolves.

