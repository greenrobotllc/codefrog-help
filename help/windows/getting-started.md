---
title: Getting Started with CodeFrog
redirect_from:
  - /help/getting-started.php
  - /help/getting-started.php?flavor=windows
  - /help/windows/getting-started.php
layout: help
---

# Getting Started with CodeFrog

Welcome to CodeFrog on Windows! This guide will help you get started quickly.

## Quick Start

1. **Complete Windows Setup**
   - Follow the [Windows Setup Guide](/help/windows/windows-setup) to configure your system
   - Enable long path support if working with deep directory structures
   - Ensure OpenSSH Client is installed

2. **Open CodeFrog**
   - Launch CodeFrog from the Start menu or Microsoft Store
   - Complete the onboarding flow to set your preferences

3. **Create Your First Project**
   - **Local Folder**: Use files on your Windows computer
   - **SSH Connection**: Work on a remote server via SSH
   - Click "New Project" and choose your project type

4. **Start Coding**
   - Use the File Browser to navigate your project
   - Open the Terminal for command-line access
   - Use Git tools for version control

## Windows Setup Steps

Before you start using CodeFrog, complete these Windows-specific setup steps:

### 1. Enable Long Path Support (Recommended)

Windows has a 260-character path limit by default. Enable long path support:

1. Run PowerShell as Administrator
2. Execute:
   ```powershell
   New-ItemProperty -Path "HKLM:\SYSTEM\CurrentControlSet\Control\FileSystem" -Name "LongPathsEnabled" -Value 1 -PropertyType DWORD -Force
   ```
3. Restart your computer

See [Windows Setup Guide](/help/windows/windows-setup) for detailed instructions.

### 2. Install OpenSSH Client

OpenSSH is required for terminal functionality:

1. Open Settings → Apps → Optional Features
2. Click "Add a feature"
3. Search for "OpenSSH Client" and install it

Or use PowerShell (as Administrator):
```powershell
Add-WindowsCapability -Online -Name OpenSSH.Client~~~~0.0.1.0
```

### 3. Configure Terminal (Optional but Recommended)

Install Windows Terminal for the best experience:

1. Open Microsoft Store
2. Search for "Windows Terminal"
3. Install and set as default terminal

## Recommended Setup

- **Windows users**: Follow the [Windows Setup Guide](/help/windows/windows-setup) for complete configuration
- **Decide your workflow**: Choose between [Local or Remote](/help/windows/workflows) development
- **Connect GitHub**: Link your [GitHub account](/help/windows/github-integration) for PR comments and issues
- **Review shortcuts**: Check [keyboard shortcuts](/help/common/shortcuts) for productivity

## Creating Your First Project

### Local Project

1. Click "New Project" on the Welcome screen
2. Select "Local Folder"
3. Choose a folder on your Windows computer
4. Grant permissions if Windows asks
5. Your project is ready!

### Remote Project (SSH)

1. Click "New Project" on the Welcome screen
2. Select "SSH Connection"
3. Enter your server details:
   - Hostname or IP address
   - Username
   - Port (default: 22)
   - Authentication method (password or SSH key)
4. Click "Connect"
5. Select the project folder on the server

## Windows-Specific Workflow Considerations

### File Paths

- **Keep paths short**: Avoid very deep directory structures
- **Enable long paths**: If needed, enable long path support (see setup guide)
- **Case sensitivity**: Windows is case-insensitive, but be aware when deploying to case-sensitive systems

### Terminal Usage

- **Windows Terminal**: Recommended for best experience
- **PowerShell**: Pre-installed, works well
- **Command Prompt**: Basic support available

### Permissions

- **UAC prompts**: Click "Yes" when Windows asks for permission
- **Folder access**: Keep projects in user folders (Documents, Desktop) for easier access
- **SSH keys**: Store in `C:\Users\YourUsername\.ssh\`

## Next Steps

- Try [Remote Development](/help/windows/workflows#remote-workflow) for server-based projects
- Learn about [Security Scanning](/help/common/security) and [Security Headers](/help/common/security-headers) to secure your applications
- See [Windows Troubleshooting](/help/windows/windows-troubleshooting) if you hit issues
- Check [Tips for New Users](/help/common/tips) for Windows-specific productivity tips

## Getting Help

- [Windows Setup Guide](/help/windows/windows-setup) - Detailed Windows configuration
- [Windows Troubleshooting](/help/windows/windows-troubleshooting) - Solve common Windows issues
- [Tips for New Users](/help/common/tips) - Platform-specific tips and best practices
- [Windows Store Subscriptions](/help/windows/windows-iap) - Manage your subscription

