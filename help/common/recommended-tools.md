---
title: Recommended Tools & Integrations
redirect_from:
  - /help/recommended-tools.php
  - /help/recommended-tools.php?flavor=mas
layout: help
---

# Recommended Tools & Integrations

CodeFrog works best when combined with other professional development tools. This guide recommends tools and services that complement CodeFrog's workflow.

## Integrated Development Environments (IDEs)

While CodeFrog provides code editing capabilities, we recommend using dedicated IDEs for your primary development work:

### Cursor

**Why we recommend it**: Cursor is an AI-powered code editor that integrates seamlessly with your development workflow.

- **AI-Powered**: Built-in AI assistant for code generation and refactoring
- **Git Integration**: Excellent Git workflow integration
- **Terminal Access**: Built-in terminal for CLI tools
- **Extension Support**: Compatible with VS Code extensions
- **Cross-Platform**: Available on macOS, Windows, and Linux

**Best for**: AI-assisted coding, rapid prototyping, code refactoring

### Visual Studio Code

**Why we recommend it**: VS Code is a lightweight, powerful editor with extensive extension ecosystem.

- **Extensive Extensions**: Huge marketplace of extensions
- **Git Integration**: Built-in Git support
- **Debugging**: Excellent debugging capabilities
- **Terminal**: Integrated terminal for CLI workflows
- **Free & Open Source**: Completely free to use

**Best for**: General development, debugging, extension-based workflows

### Other IDEs

- **JetBrains IDEs** (IntelliJ, WebStorm, PyCharm): Full-featured IDEs for specific languages
- **Sublime Text**: Lightweight, fast editor
- **Vim/Neovim**: Terminal-based editors for power users

## AI & Code Review Tools

### CodeRabbit

**Why we recommend it**: CodeRabbit provides automated code review and AI-powered PR feedback.

- **Automated Reviews**: AI-powered pull request reviews
- **GitHub Integration**: Seamless GitHub integration
- **Task Management**: Import PR comments as tasks
- **Code Quality**: Automated code quality checks

**Integration with CodeFrog**: CodeFrog can import CodeRabbit PR comments as tasks and export them to task management systems.

See [CodeRabbit + Augment Workflow](/help/common/ai-coder-coderabbit-augment) for integration details.

### Cursor

As mentioned above, Cursor provides AI-powered coding assistance that complements CodeFrog's workflow.

## Cloud Infrastructure

### Hetzner Cloud

**Why we recommend it**: Cost-effective cloud infrastructure with excellent performance.

- **Affordable**: Competitive pricing for cloud resources
- **Performance**: High-performance SSD storage
- **Global Locations**: Data centers in multiple regions
- **API Access**: Full API for automation
- **Simple Pricing**: Transparent, predictable pricing

**Use with CodeFrog**: CodeFrog can manage Hetzner servers via SSH connections. Perfect for remote development workflows.

### Linode

**Why we recommend it**: Reliable cloud infrastructure with excellent developer experience.

- **Developer-Friendly**: Great documentation and support
- **Performance**: High-performance infrastructure
- **Global Network**: Worldwide data center locations
- **Flexible Plans**: Scalable pricing options
- **API Access**: Comprehensive API for automation

**Use with CodeFrog**: Connect to Linode servers via SSH for remote development and server management.

## Communication & Email Services

### SendGrid

**Why we recommend it**: Reliable email delivery service for transactional emails.

- **Reliable Delivery**: High deliverability rates
- **API Integration**: RESTful API for programmatic email sending
- **Analytics**: Detailed email analytics and tracking
- **Templates**: Email template management
- **Webhooks**: Real-time event notifications

**Use with CodeFrog**: Integrate SendGrid API keys in CodeFrog for automated email notifications and alerts.

### Mailchimp (REST API Mode)

**Why we recommend it**: Powerful email marketing platform when used securely via REST API.

> **Important Security Note**: Mailchimp should only be used in REST API mode for maximum security. Avoid embedded JavaScript implementations that may have security concerns.

- **REST API**: Secure API-based integration
- **Audience Management**: Email list management
- **Campaigns**: Email campaign creation and management
- **Analytics**: Comprehensive email analytics
- **Automation**: Automated email workflows

**Security Best Practices**:
- Always use REST API mode
- Store API keys securely (CodeFrog uses macOS Keychain)
- Never embed Mailchimp JavaScript directly
- Use server-side API calls only

## Version Control & Collaboration

### GitHub

**Why we recommend it**: Industry-standard version control and collaboration platform.

- **Git Integration**: Full Git workflow support
- **Pull Requests**: Code review and collaboration
- **Issues**: Project management and bug tracking
- **Actions**: CI/CD automation
- **Packages**: Package registry

**Integration with CodeFrog**: 
- View and manage PR comments
- Import PR feedback as tasks
- Track GitHub issues
- Automate code review workflows

See [Project Workflows](/help/common/workflows) for GitHub integration details.

## Recommended Workflow Combinations

### AI-Assisted Development

1. **Cursor** for primary coding with AI assistance
2. **CodeRabbit** for automated PR reviews
3. **CodeFrog** for testing, security scanning, and project management
4. **GitHub** for version control and collaboration

### Remote Development

1. **Hetzner or Linode** for cloud infrastructure
2. **CodeFrog** for SSH server management and monitoring
3. **VS Code or Cursor** with Remote SSH extension
4. **GitHub** for version control

### Full-Stack Workflow

1. **Cursor or VS Code** for development
2. **CodeFrog** for testing and security validation
3. **SendGrid** for transactional emails
4. **Mailchimp** (REST API) for marketing emails
5. **GitHub** for version control and deployment

## Why Not AI CLI Programs in CodeFrog?

CodeFrog intentionally does not include embedded AI CLI tools (such as Auggie, Cursor CLI, or similar). Instead, we recommend:

- **Using your Mac's Terminal app** for AI CLI tools
- **Using dedicated IDEs** like Cursor for AI-powered coding
- **Using external services** like CodeRabbit for AI-powered reviews

This approach provides:
- **Better Security**: No embedded third-party AI tools in the app
- **More Flexibility**: Use the AI tools that work best for your workflow
- **Cleaner Architecture**: CodeFrog focuses on testing, security, and project management
- **User Choice**: You control which AI tools to use and how

## Next Steps

- [Project Workflows](/help/common/workflows) - Set up your development workflow
- [CodeRabbit + Augment Workflow](/help/common/ai-coder-coderabbit-augment) - AI integration guide

