---
title: Project Workflows
redirect_from:
  - /help/workflows.php
  - /help/workflows.php?flavor=mas
layout: help
---

## Workflow Overview

CodeFrog on macOS supports two primary development workflows. Choose the one that best fits your project and development style.

## Local Development Workflow

Work with files and folders directly on your Mac. This is the fastest and most straightforward workflow for local projects.

### When to Use Local Workflow

- Flutter or React Native projects on your Mac
- Web development projects (HTML, CSS, JavaScript)
- Any project stored on your Mac's file system
- Offline development without network dependency
- Projects that don't require remote server resources

### Setting Up a Local Project

1. Click **New Project** from the Welcome screen
2. Choose **Local Folder** as the connection type
3. Enter a project name
4. Click **Select Folder**
5. Navigate to your project folder in the macOS folder picker
6. Click **Open** to grant access
7. Configure optional settings (color theme, Git repository)
8. Click **Create Project**

### What You Can Do

- **File Browser:** Browse, edit, create, and delete files
- **Git Integration:** View changes, commit, push, and pull
- **GitHub PR Comments:** Import and manage pull request feedback
- **Code Validation:** Run security scans and code analysis
- **Web Testing:** Test HTML files in your browser

### File Access

CodeFrog uses macOS security-scoped bookmarks to access your project folder. This means:

- You explicitly grant access when creating the project
- CodeFrog can only access the folder you selected
- Access persists across app launches
- You can revoke access by deleting the project

### Limitations

- Cannot access files outside the selected folder
- Some system folders may require Full Disk Access
- Build operations run locally (no remote server resources)

## Remote Development Workflow

Connect to remote servers via SSH to work with projects hosted on cloud instances, remote Linux servers, or other machines.

### When to Use Remote Workflow

- Projects hosted on cloud servers (AWS, DigitalOcean, Linode, etc.)
- Remote Linux development environments
- Shared development servers
- Android-to-macOS remote development
- Projects requiring server-side resources (databases, APIs)
- Collaborative development on shared machines

### Setting Up a Remote Project

1. Click **New Project** from the Welcome screen
2. Choose **SSH Connection** as the connection type
3. Enter a project name
4. Configure SSH connection:
   - Server hostname or IP address
   - Port (default: 22)
   - Username
   - Authentication method (SSH key or password)
5. Test the connection
6. Select the remote project directory
7. Configure optional settings (color theme, Git repository)
8. Click **Create Project**

### What You Can Do

- **SSH Terminal:** Full terminal access to the remote server
- **File Browser:** Browse and edit files via SFTP
- **Git Integration:** Manage Git repositories on the remote server
- **Remote Builds:** Build and run projects using server resources
- **Server Admin:** Manage server settings, disk monitoring, etc.

### SSH Key Management

For secure, password-less authentication:

1. Generate an SSH key pair in CodeFrog (or import existing keys)
2. Copy the public key to your server's `~/.ssh/authorized_keys`
3. Use the private key when creating SSH connections

*Tip: CodeFrog can automatically inject your public key to new servers during setup.*

## Switching Between Projects

CodeFrog makes it easy to work with multiple projects and switch between them quickly.

### Quick Project Switcher

Press `⌘⇧P` to open the Quick Project Switcher:

- See all your projects at a glance
- Search by project name
- See connection status (local/remote)
- Switch with a single click or Enter key

### Recent Projects

The Welcome screen shows your most recently used projects:

- Click any project to open it immediately
- See project type (local folder or SSH connection)
- View last accessed time

### Project Name Tab

Click the project name in the tab bar to:

- Return to the Workspace view
- Refresh the current project
- See project details

### What Happens When You Switch

When switching projects, CodeFrog:

- Saves your current work
- Disconnects from SSH (if applicable)
- Loads the new project
- Reconnects to SSH (if applicable)

## Project Settings

Each project has its own settings that you can customize.

### Accessing Project Settings

- Click the hamburger menu (☰) in the app bar
- Select **Project Settings**

### Available Settings

- **General:** Project name, color theme, description
- **Connection:** SSH settings, folder path, connection details
- **Git:** Repository URL, default branch, Git user config
- **Build & Sync:** Build commands, SFTP sync settings
- **AI Tools:** Which AI CLI tools to use for this project

### Color Themes

Assign custom colors to projects for easy visual identification:

- Choose from preset colors or use a custom color picker
- Colors appear in the project list and tab bar
- Helps distinguish between local and remote projects
- All colors meet WCAG AA contrast standards

## Workflow Best Practices

### For Local Projects

- Keep projects in a dedicated folder (e.g., `~/Projects`)
- Use Git for version control
- Regularly commit and push changes
- Use meaningful project names

### For Remote Projects

- Use SSH keys instead of passwords
- Keep SSH keys secure with strong passphrases
- Regularly update remote servers
- Use descriptive server names
- Test connections before starting work

## Next Steps

- [Learn about AI tools](/help/mas/ai-tools) - Get started with AI-assisted coding
- [GitHub integration](/help/mas/github) - Connect your GitHub account
- [Explore features](/help/mas/features) - Discover what CodeFrog can do
- [Troubleshooting](/help/mas/troubleshooting) - Find solutions to common issues

