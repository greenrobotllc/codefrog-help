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
   - Copy the device code shown in CodeFrog
   - Open the verification URL in your browser (or CodeFrog will open it automatically)
   - Paste the device code on GitHub's authorization page
   - Click "Authorize" to grant CodeFrog access

3. **Complete Authorization**
   - GitHub will confirm authorization
   - CodeFrog will automatically detect the authorization
   - Your GitHub account is now connected

### Windows-Specific SSH Setup

For SSH-based GitHub operations (if needed for advanced workflows):

1. **Generate SSH Key** (if you don't have one)
   ```powershell
   ssh-keygen -t ed25519 -C "your_email@example.com"
   ```
   - Press Enter to accept default location: `C:\Users\YourUsername\.ssh\id_ed25519`
   - Enter a passphrase (optional but recommended)

2. **Add SSH Key to GitHub**
   - Copy your public key:
     ```powershell
     Get-Content C:\Users\YourUsername\.ssh\id_ed25519.pub
     ```
   - Go to GitHub → Settings → SSH and GPG keys
   - Click "New SSH key"
   - Paste your public key and save

3. **Test SSH Connection**
   ```powershell
   ssh -T git@github.com
   ```
   - Should respond: "Hi username! You've successfully authenticated..."

### Windows Credential Management

Windows stores Git credentials in Windows Credential Manager:

**Viewing Stored Credentials**:
1. Open Control Panel → Credential Manager
2. Click "Windows Credentials"
3. Look for `git:https://github.com` entries

**Managing Credentials**:
- **Update**: Click credential → Edit → Update password
- **Remove**: Click credential → Remove (Git will prompt for credentials next time)

**Using Credential Manager**:
- Git for Windows automatically uses Credential Manager
- Credentials are stored securely by Windows
- No need to manually manage for HTTPS connections

## Windows-Specific GitHub CLI Setup

If you want to use GitHub CLI (`gh`) alongside CodeFrog:

1. **Install GitHub CLI**
   - Download from: https://cli.github.com/
   - Or use winget: `winget install GitHub.cli`
   - Or use Chocolatey: `choco install gh`

2. **Authenticate**
   ```powershell
   gh auth login
   ```
   - Choose GitHub.com
   - Choose authentication method (browser recommended)
   - Follow prompts to authorize

3. **Verify Installation**
   ```powershell
   gh --version
   gh auth status
   ```

## Using GitHub Features

### Viewing Pull Requests

1. **Navigate to GitHub Tab**
   - Open your project in CodeFrog
   - Click "GitHub" in the navigation

2. **Select Repository**
   - Choose the repository from the list
   - Or enter repository name/URL

3. **View PRs**
   - Browse open pull requests
   - Click a PR to view details and comments

### Importing PR Comments

1. **Open a Pull Request**
   - Navigate to the PR in CodeFrog's GitHub tab

2. **Import Comments**
   - Click "Import Comments" or similar button
   - Comments will be converted to markdown format
   - Suitable for pasting into AI tools like Cursor or Augment

3. **Use with AI Tools**
   - Copy the markdown comments
   - Paste into your AI coding assistant
   - Use for context-aware code improvements

### Viewing and Importing Issues

1. **Navigate to Issues**
   - Go to GitHub tab → Issues section

2. **Browse Issues**
   - View open and closed issues
   - Filter by labels, assignees, etc.

3. **Import Issues**
   - Select issues to import
   - Convert to tasks or markdown format
   - Use for project management

## Troubleshooting

### Authentication Issues

**Problem**: Can't connect GitHub account

**Solutions**:
- **Clear Browser Cache**: Clear cookies for github.com
- **Try Different Browser**: Use a different browser for authorization
- **Check Firewall**: Ensure Windows Firewall isn't blocking GitHub
- **Re-authenticate**: Disconnect and reconnect your GitHub account

### SSH Connection Issues

**Problem**: SSH authentication fails

**Solutions**:
- **Check SSH Key**: Verify key exists in `C:\Users\YourUsername\.ssh\`
- **Test Connection**: Run `ssh -T git@github.com` in PowerShell
- **Check Key Permissions**: Ensure private key has restricted permissions
- **Regenerate Key**: Create new SSH key if current one doesn't work

### Credential Manager Issues

**Problem**: Git keeps asking for credentials

**Solutions**:
- **Update Credentials**: Update stored credentials in Credential Manager
- **Remove Old Credentials**: Delete old/invalid credentials
- **Use Personal Access Token**: Generate PAT and use as password
- **Switch to SSH**: Use SSH instead of HTTPS for authentication

### Network Issues

**Problem**: Can't connect to GitHub

**Solutions**:
- **Check Internet**: Verify internet connection is working
- **Check Firewall**: Ensure Windows Firewall allows GitHub connections
- **VPN Issues**: If using VPN, try disabling temporarily
- **Proxy Settings**: Check if proxy settings are interfering

## Best Practices

### Security

- **Use Device Flow**: Prefer Device Flow over Personal Access Tokens
- **SSH Keys**: Use SSH keys for Git operations when possible
- **Regular Updates**: Keep CodeFrog updated for security patches
- **Credential Management**: Use Windows Credential Manager for secure storage

### Workflow

- **Regular Sync**: Regularly sync PR comments and issues
- **Organize Comments**: Use labels and filters to organize PR comments
- **AI Integration**: Use imported comments with AI tools for better code reviews
- **Version Control**: Use Git/GitHub Desktop for actual version control operations

## Next Steps

- [Windows Setup Guide](/help/windows/windows-setup) - Configure CodeFrog on Windows
- [Windows Troubleshooting](/help/windows/windows-troubleshooting) - Solve Windows-specific issues
- [Getting Started](/help/windows/getting-started) - Learn CodeFrog basics

