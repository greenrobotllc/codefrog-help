---
title: GitHub Integration
layout: help
---

# GitHub Integration

CodeFrog's GitHub integration allows you to view pull requests, import PR comments as markdown for AI agents, and view/import GitHub issues. This integration streamlines code review workflows by making PR feedback easily accessible for tools like Cursor, Augment, and other AI coding assistants.

## Overview

**What GitHub Integration Provides:**
- View GitHub pull requests and comments
- Import PR comments as markdown format (for Cursor, Augment, etc.)
- View and import GitHub issues
- AI-powered comment summaries for easier review

**What GitHub Integration Does NOT Provide:**
- ❌ Git operations (commit, push, pull)
- ❌ Git diff viewing
- ❌ Branch detection
- ❌ Version control operations

For Git operations, use [GitHub Desktop](https://desktop.github.com/) or your preferred Git client.

## Getting Started

### Accessing GitHub Features

1. **Open a Project**
   - GitHub integration requires an open project in CodeFrog
   - Create a new project or open an existing one

2. **Navigate to GitHub Tab**
   - Click **GitHub** in the navigation menu
   - Or use the keyboard shortcut (if configured)

3. **Connect Your GitHub Account**
   - Follow the authentication steps below

## Connecting Your GitHub Account

CodeFrog uses GitHub's Device Authorization Flow (Device Flow) for secure OAuth authentication. This method is more secure than Personal Access Tokens and doesn't require storing credentials.

### Using CodeFrog's Default GitHub App

1. **Start Authentication**
   - In the GitHub tab, click **"Sign in with GitHub"** or **"Connect GitHub Account"**
   - CodeFrog will display a device code and verification URL

2. **Authorize on GitHub**
   - Open the verification URL in your browser (or copy/paste the code)
   - Log in to GitHub if needed
   - Authorize CodeFrog to access your repositories

3. **Complete Authorization**
   - GitHub will display a confirmation
   - Return to CodeFrog - the connection should be established automatically

### Using Your Own GitHub OAuth App (Enhanced Privacy)

For enhanced privacy and control, you can create your own GitHub OAuth app:

1. **Create GitHub OAuth App**
   - Go to GitHub Settings → Developer settings → OAuth Apps
   - Click **"New OAuth App"**
   - Fill in:
     - **Application name**: Your choice (e.g., "CodeFrog - My App")
     - **Homepage URL**: Your website or `https://codefrog.app`
     - **Authorization callback URL**: Use the callback URL shown in CodeFrog's GitHub settings
   - **Important**: Enable **"Device Flow"** (Device Authorization Grant) in OAuth app settings

2. **Configure in CodeFrog**
   - In CodeFrog's GitHub settings, enter your OAuth app's Client ID
   - CodeFrog will use your app for authentication instead of the default

3. **Benefits**
   - Full control over OAuth app permissions
   - Can revoke access independently
   - Enhanced privacy for enterprise users

### Required Permissions

The GitHub OAuth app needs these scopes:
- `repo` - Access to repositories (for PRs and issues)
- `read:user` - Read user profile information

## Viewing Pull Requests

Once connected, you can view pull requests for your repositories:

1. **Select Repository**
   - Choose a repository from the list
   - CodeFrog will load pull requests for that repository

2. **View PR Details**
   - Click on a pull request to view:
     - PR title and description
     - All comments and reviews
     - File-specific comments
     - Comment threading

3. **Note on Branch Detection**
   - CodeFrog does not automatically detect your current Git branch
   - This is due to technical limitations with the SSH localhost workaround
   - You'll need to manually select the PR you want to view

## Importing PR Comments as Markdown

One of the most powerful features is importing PR comments as markdown for use with AI coding assistants:

### Basic Import

1. **Select a Pull Request**
   - Navigate to the PR you want to import comments from

2. **Review Import Banner**
   - At the top of the PR view, you'll see:
     - Total unresolved comments
     - Number of importable comments (with AI summaries)
     - Number of complex comments (must be handled on GitHub web)

3. **Import Comments**
   - Click **"Import Importable Comments"** for all comments
   - Or use **"Import First 20 Comments"** / **"Import First 50 Comments"** for batch processing
   - Comments are formatted as markdown with:
     - PR number and comment ID
     - File paths and line numbers
     - Comment text and AI summaries

4. **Use with AI Agents**
   - Copy the markdown output
   - Paste into Cursor, Augment, or other AI coding assistants
   - The AI can process all comments at once

### Comment Format

Imported comments follow this format:
```markdown
PR#{pr_number} Comment #{comment_id}: {description}

File: {file_path}
Line: {line_number}

{comment_text}

AI Summary: {ai_generated_summary}
```

### AI Summaries

CodeFrog automatically generates AI summaries for PR comments to make them easier to understand:
- Extracts key points from long comments
- Highlights actionable items
- Simplifies technical jargon

## Viewing and Importing Issues

You can also view and import GitHub issues:

1. **View Issues**
   - In the GitHub tab, switch to the **Issues** view
   - See all open issues for the repository

2. **Import Issues**
   - Select issues to import
   - Export as markdown for AI agents
   - Format includes issue number, title, description, and labels

## Workflows

### CodeRabbit + Augment Workflow

1. CodeRabbit reviews your PR and leaves comments
2. Import PR comments into CodeFrog as markdown
3. Export to Augment Code's task manager
4. Fix issues and commit (using GitHub Desktop or Git client)
5. CodeRabbit automatically verifies fixes when you push

See [CodeRabbit + Augment Workflow](/help/common/ai-coder-coderabbit-augment) for detailed instructions.

### Cursor / Other AI Agents Workflow

1. Import PR comments as markdown from CodeFrog
2. Paste the markdown into Cursor or your AI agent
3. AI processes all comments and suggests fixes
4. Review and apply fixes
5. Commit and push using your Git client

See [Cursor / Other AI Agents](/help/common/ai-coder-cursor) for detailed instructions.

### Handling Large PRs

For PRs with many comments:
1. Manually review critical issues first (security, architecture)
2. Import remaining comments as markdown
3. Process bulk comments with AI agents
4. Fix and commit systematically

See [Handling PRs with Many Comments](/help/common/handling-pr-comments) for a complete workflow.

## Limitations

### What CodeFrog Cannot Do

- **No Git Operations**: CodeFrog does not support:
  - Viewing git diffs
  - Committing changes
  - Pushing to remote
  - Pulling from remote
  - Branch detection

- **No Branch Detection**: Due to technical limitations with the SSH localhost workaround, CodeFrog cannot automatically detect your current Git branch. You must manually select PRs to view.

### Recommended Tools for Git Operations

For version control operations, use:
- [GitHub Desktop](https://desktop.github.com/) - User-friendly Git client
- Command line Git - For advanced users
- Your preferred IDE's Git integration

## Troubleshooting

### Cannot Connect GitHub Account

**Problem:** OAuth authorization fails or doesn't redirect back to CodeFrog.

**Solutions:**
- Make sure you're logged into GitHub in your browser
- Try disconnecting and reconnecting your GitHub account
- Clear your browser cookies and try again
- Check that CodeFrog is allowed in your GitHub OAuth settings
- Visit [github.com/settings/applications](https://github.com/settings/applications) to manage authorized apps
- If using your own OAuth app, verify Device Flow is enabled

### PR Comments Not Importing

**Problem:** GitHub PR comments don't appear or can't be imported.

**Solutions:**
- Make sure the PR has unresolved comments
- Check that you're viewing the correct repository
- Try refreshing the PR view
- Verify your GitHub connection is still active
- Check if the comments are marked as "nitpick" (some may be hidden by default)

### Import Fails

**Problem:** Comment import fails or produces errors.

**Solutions:**
- Verify your GitHub OAuth token is valid
- Check your internet connection
- Try importing smaller batches (20-50 comments at a time)
- Complex comments without AI summaries must be handled on GitHub web interface

For more troubleshooting help, see platform-specific troubleshooting guides.

## Next Steps

- [Handling PRs with Many Comments](/help/common/handling-pr-comments) - Efficiently process large code reviews
- [CodeRabbit + Augment Workflow](/help/common/ai-coder-coderabbit-augment) - Automated code review workflow
- [Cursor / Other AI Agents](/help/common/ai-coder-cursor) - Using Cursor and other AI tools
- [Project Workflows](/help/common/workflows) - Understanding local vs. remote development
- [Troubleshooting](/help/mas/troubleshooting) - Common issues and solutions

