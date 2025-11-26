---
title: Privacy & External Connections
redirect_from:
  - /help/privacy.php
layout: help
---

## Privacy Overview

CodeFrog is designed with privacy in mind. This page explains what external services CodeFrog connects to and why.

**Key Privacy Principles:**
- CodeFrog only connects to external services when you use specific features
- Your code and files are never sent to external services without your explicit action
- All connections use HTTPS encryption
- You can use CodeFrog entirely offline for local projects
- CodeFrog does not include embedded AI CLI tools (use your Mac's Terminal app for AI CLI tools like Auggie, Cursor, etc.)

## External Services

### W3C Validator (validator.w3.org)

**Used for:** Web Testing feature - HTML validation  
**What's sent:** HTML file content you choose to validate  
**Privacy:** W3C stores submitted files/content on servers in the USA for caching and service improvement; W3C staff may review content — see [W3C Validator Terms & Confidentiality](https://validator.w3.org/docs/help.html#privacy) for details.  
**When:** Only when you explicitly use the Web Testing feature

### Semgrep (semgrep.dev)

**Used for:** Static code analysis and security scanning  
**What's sent:** Code snippets from files you choose to scan  
**Privacy:** Semgrep's privacy policy applies. Code is analyzed and results returned.  
**When:** Only when you explicitly run a Semgrep scan  
**Alternative:** Use OpenGrep (local) for complete privacy

### OSV (Open Source Vulnerabilities - osv.dev)

**Used for:** Vulnerability database lookups  
**What's sent:** Package names and versions from your project  
**Privacy:** Google's privacy policy applies. Only package identifiers are sent, not your code.  
**When:** Only when you explicitly run vulnerability scans

### GitHub (github.com)

**Used for:** Pull requests, issues, and repository integration  
**What's sent:** OAuth tokens, repository queries, PR comment updates  
**Privacy:** GitHub's privacy policy applies. CodeFrog uses OAuth for secure authentication.  
**Permissions:** Read repositories, read/write PR comments, read issues  
**When:** Only when you connect your GitHub account and use GitHub features  
**Enhanced Privacy:** You can register your own GitHub OAuth app for direct control over authentication.

### Linode (linode.com)

**Used for:** Optional cloud server management  
**What's sent:** API tokens, server management commands  
**Privacy:** Linode's privacy policy applies.  
**When:** Only if you configure Linode API integration

### SendGrid (sendgrid.com)

**Used for:** Optional disk usage monitoring email notifications  
**What's sent:** Email notifications with disk usage data  
**Privacy:** SendGrid's privacy policy applies. Only disk usage metrics are sent.  
**Setup:** Completely optional. You configure your own SendGrid API key.  
**When:** Only if you set up disk monitoring with SendGrid notifications

## AI Features & Internet Requirements

**Current Status:**
CodeFrog does **not** currently use external AI services that require internet connectivity. The app includes local text processing for GitHub PR comment summaries, which operates entirely offline and does not send data to external AI providers.

**Embedded AI CLI Tools:**
- CodeFrog does **not** include embedded AI CLI tools (such as Auggie, Cursor CLI, or similar)
- Users can use AI CLI tools in their Mac's Terminal app instead
- This may change in future releases, but currently no AI terminal features are included

**AI Features That May Require Internet (If Added in Future):**
If AI features requiring internet connectivity are added in the future, they will be documented here with:
- **Feature Name:** Specific AI feature description
- **Data Sent:** Exact data transmitted (e.g., code snippets, prompts, file contents)
- **External Provider:** AI service provider name and privacy policy link
- **Data Retention:** How long data is retained by the provider
- **Training Policy:** Whether submitted data is used for model training
- **Opt-Out Controls:** Settings or UI controls to disable the feature
- **When Data Is Sent:** On explicit user action or automatic background processing

**Current Local AI Processing:**
- **GitHub PR Comment Summaries:** Local text extraction and formatting (no network calls)
- **Comment Title Extraction:** Local parsing of comment text (no network calls)
- **No External AI APIs:** No calls to OpenAI, Anthropic, or other AI providers

For more details on future AI features, see our [Privacy Policy](https://greenrobot.com/privacy).

## Analytics, Telemetry & Crash Reporting

**Current Status:**
CodeFrog does **not** currently collect telemetry, analytics, or crash reporting data. No analytics services (such as Google Analytics, Firebase Analytics, Sentry, or Crashlytics) are implemented or active in the application.

**Future Implementation:**
If telemetry or crash reporting is added in the future, it will be:
- **Opt-in only:** Users must explicitly enable it
- **Disabled by default:** No data collection without user consent
- **Transparent:** Fully documented in this privacy policy
- **Controllable:** Users can disable it at any time

**How to Ensure Telemetry Remains Disabled:**
- Set the `DISABLE_TELEMETRY` environment variable to `true` (if using environment-based configuration)
- Telemetry is disabled by default in all builds
- No action is required to prevent data collection

**What Would Be Collected (If Enabled in Future):**
If telemetry is implemented in the future, it may include:
- **Usage Events:** Feature usage, button clicks, navigation patterns
- **Performance Metrics:** App startup time, feature load times, response times
- **Crash Reports:** Error messages, stack traces, device information (no source code)
- **Device Information:** OS version, app version, device type (anonymized)

**Data Collection Principles (If Enabled):**
- **No Source Code:** Your code and files are never sent
- **No Personal Data:** No names, emails, or identifying information
- **Anonymized:** Data is aggregated and anonymized
- **Secure Transmission:** All data sent over HTTPS encryption
- **User Control:** Can be disabled at any time via settings or environment variable

**Third-Party Services (If Implemented):**
Any future analytics or crash reporting services would be listed here with:
- Service name and purpose
- Link to their privacy policy
- What data they receive
- How to opt out

For more details, see our [Privacy Policy](https://greenrobot.com/privacy).

## Local Data Storage

### What CodeFrog Stores Locally

- **Project Settings:** Project names, connection details, preferences (SQLite database)
- **SSH Keys:** Encrypted private keys (Flutter Secure Storage)
- **API Keys:** Encrypted API tokens (Flutter Secure Storage)
- **Security-Scoped Bookmarks:** Encrypted folder access permissions (macOS only)
- **Task Manager Data:** Your tasks and GitHub PR comments (SQLite database)
- **App Preferences:** Theme, settings, and user preferences (SQLite database)

### Data Encryption

Sensitive data is encrypted using:
- **Flutter Secure Storage:** Uses platform-native secure storage (Keychain on macOS)
- **AES-GCM Encryption:** For security-scoped bookmarks and sensitive settings
- **No Plain Text Storage:** Passwords and keys are never stored in plain text

## Your Privacy Rights

- **Access:** You can view all stored data through CodeFrog's settings
- **Deletion:** Delete projects and data at any time
- **Control:** Choose which external services to use
- **Transparency:** This page documents all external connections

## Questions?

If you have questions about privacy or data handling:
- [Contact Support](https://greenrobot.freshdesk.com/support/solutions/9000119001)
- Review our [Terms of Service](https://greenrobot.com/terms)
- Check our [Privacy Policy](https://greenrobot.com/privacy)

