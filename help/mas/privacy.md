---
title: Privacy & External Connections
redirect_from:
  - /help/privacy.php
  - /help/privacy.php?flavor=mas
layout: help
---

## Privacy Overview

CodeFrog is designed with privacy in mind. This page explains what external services CodeFrog connects to and why.

**Key Privacy Principles:**
- CodeFrog only connects to external services when you use specific features
- Your code and files are never sent to external services without your explicit action
- All connections use HTTPS encryption
- You can use CodeFrog entirely offline for local projects (except AI features)

## External Services

### W3C Validator (validator.w3.org)

**Used for:** Web Testing feature - HTML validation  
**What's sent:** HTML file content you choose to validate  
**Privacy:** W3C's privacy policy applies. Files are validated and results returned; W3C does not store your files.  
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

## Local Data Storage

### What CodeFrog Stores Locally

- **Project Settings:** Project names, connection details, preferences (SQLite database)
- **SSH Keys:** Encrypted private keys (Flutter Secure Storage)
- **API Keys:** Encrypted API tokens (Flutter Secure Storage)
- **Security-Scoped Bookmarks:** Encrypted folder access permissions (macOS only)
- **AI Terminal History:** Command history for AI sessions (SQLite database)
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

