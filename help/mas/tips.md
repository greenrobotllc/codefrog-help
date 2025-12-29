---
title: Tips for New Users
redirect_from:
  - /help/tips.php
  - /help/tips.php?flavor=mas
  - /help/mas/tips.php
layout: help
---

# Tips for New Users

Get the most out of CodeFrog with these platform-specific tips and AI assistant guidance.

## macOS-Specific Tips

### File Access Permissions

- **Security-Scoped Bookmarks**: CodeFrog uses macOS security-scoped bookmarks for local folder access. When you select a folder, macOS will ask for permission—this is normal and required for the app to access your files.
- **Granting Access**: If you move or rename a project folder, you may need to re-grant access. Use the project diagnostics tool (medical icon) to fix connection issues.
- **Multiple Folders**: Each project folder requires separate permission. CodeFrog can only access folders you explicitly grant access to.

### Keyboard Shortcuts

- **⌘S**: Save current file (works in code editor)
- **⌘W**: Close current tab or window
- **⌘K**: Quick project switcher
- **⌘T**: Open terminal
- **⌘P**: Quick file search

See the [Keyboard Shortcuts](/help/common/shortcuts) guide for the complete list.

### Menu Bar Integration

- **File > Open Recent**: Quickly access recently opened projects and files
- **File > Open**: Open a project folder or file directly
- **Project > Close Project**: Close the current project and return to Welcome screen

## AI Assistant Guidance

### Recommended Development Setup

For the best development experience, we recommend using CodeFrog alongside dedicated IDEs and AI tools:

- **Primary IDE**: Use [Cursor](https://cursor.sh) or [VS Code](https://code.visualstudio.com) for your main coding work
  - These IDEs provide better AI assistance, debugging, and extension support
  - CodeFrog complements these tools with testing, security scanning, and project management

- **AI Code Review**: Use [CodeRabbit](https://coderabbit.ai) for automated PR reviews
  - CodeFrog can import CodeRabbit PR comments as tasks
  - See [CodeRabbit + Augment Workflow](/help/common/ai-coder-coderabbit-augment) for integration details

- **CLI Workflows**: Use your Mac's Terminal app for AI CLI tools
  - CodeFrog doesn't include embedded AI CLI tools by design
  - This gives you flexibility to use the AI tools that work best for your workflow

### Why Not AI CLI in CodeFrog?

CodeFrog intentionally doesn't include embedded AI CLI programs. Instead, we recommend:

- **Using external IDEs** like Cursor for AI-powered coding
- **Using Terminal** for AI CLI tools when needed
- **Using CodeRabbit** for AI-powered code reviews

This approach provides better security, more flexibility, and lets you choose the AI tools that work best for you.

### Recommended Tools & Integrations

For a complete list of recommended tools and services that work well with CodeFrog, see our [Recommended Tools & Integrations](/help/common/recommended-tools) guide. This includes:

- **IDEs**: Cursor, VS Code, and other development environments
- **Cloud Services**: Hetzner, Linode for infrastructure
- **Email Services**: SendGrid, Mailchimp (REST API mode)
- **Version Control**: GitHub integration workflows

### Best Practices

- **Start with Onboarding**: Run the onboarding flow to configure your preferences
- **Use Project Workflows**: Choose the right workflow (local vs. remote) for your needs
- **Connect GitHub**: Link your GitHub account for PR automation and issue tracking
- **Use External IDEs**: Use Cursor or VS Code for primary development, CodeFrog for testing and management
- **Regular Backups**: CodeFrog doesn't automatically backup your code—use Git for version control

## Productivity Tips

### Project Management

- **Use Tags**: Organize projects with tags for easy filtering
- **Favorites**: Mark frequently used projects as favorites
- **Recent Projects**: The Welcome screen shows your 5 most recent projects

### Code Editor

- **Syntax Highlighting**: Automatically detects language from file extension
- **Save As**: Use File > Save As to save files to new locations
- **Multiple Tabs**: Open multiple files in tabs for easy switching

### Testing & Analysis

- **Web Testing**: Test both local HTML files and live URLs
- **Bulk Scanning**: Use Bulk Security Scanner for multiple domains at once
- **Mega Report**: Generate comprehensive reports combining all test results

## Troubleshooting Tips

- **Connection Issues**: Use the diagnostics tool (medical icon) on project cards
- **File Not Found**: Check that you've granted folder access permissions
- **Slow Performance**: Close unused projects and clear terminal history
- **GitHub Issues**: Verify your GitHub OAuth token is valid

## Next Steps

- [Getting Started Guide](/help/mas/getting-started) - Learn the basics
- [Project Workflows](/help/common/workflows) - Choose your workflow
- [Keyboard Shortcuts](/help/common/shortcuts) - Boost productivity
- [Troubleshooting](/help/common/troubleshooting) - Solve common issues

