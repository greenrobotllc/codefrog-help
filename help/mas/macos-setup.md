---
title: macOS Setup Guide
layout: help
---

# macOS Setup Guide

This guide walks you through the macOS system settings required for CodeFrog to work properly with local projects and SSH connections.

## Overview

CodeFrog requires two macOS permissions for full functionality:

1. **Remote Login (SSH)** - Enables localhost SSH connections for terminal access and local project features
2. **Full Disk Access for Remote Users** - Allows SSH access to protected folders (Documents, Desktop, Downloads)

## Enabling Remote Login (SSH)

Remote Login enables SSH connections to your Mac, which CodeFrog uses for localhost connections and terminal access.

### Step-by-Step Instructions

1. **Open System Settings**
   - Click the Apple menu → **System Settings**
   - Or press `⌘,` (Command + Comma)

2. **Navigate to Sharing**
   - Click **General** in the sidebar
   - Click **Sharing**

3. **Enable Remote Login**
   - Find **Remote Login** in the list
   - Toggle the switch to **ON** (green)

4. **Configure User Access**
   - Click the **(i)** button next to Remote Login
   - Under **Allow access for**, choose one of:
     - **All users** (recommended for simplicity)
     - **Only these users** - then add your username to the list
   - **Important:** Your username must be in the allowed list for CodeFrog to connect

5. **Verify Remote Login is Active**
   - The Remote Login toggle should be green
   - You should see "Remote Login: On" in the status

### Why Remote Login is Needed

- **Terminal Access**: CodeFrog uses SSH to provide terminal functionality for local projects
- **Localhost Connections**: Enables SSH connections to `localhost` for local development workflows
- **File Operations**: Allows secure file access through SSH protocols

## Full Disk Access for Remote Users

When using Remote Login, you need to enable "Full Disk Access for remote users" to access protected folders like Documents, Desktop, and Downloads via SSH.

### Step-by-Step Instructions

1. **Open Remote Login Settings**
   - System Settings → General → Sharing
   - Click the **(i)** button next to **Remote Login**

2. **Enable Full Disk Access**
   - Find the **"Allow full disk access for remote users"** checkbox
   - Check the box to enable it

3. **Verify User Access**
   - Ensure **"Allow access for"** is set to **"All users"** OR includes your username
   - This is critical - if your username isn't allowed, you won't be able to access protected folders

### Why This is Needed

macOS protects certain folders (Documents, Desktop, Downloads, iCloud Drive) with special permissions. When accessing these folders via SSH (which CodeFrog uses for local projects), you need to explicitly grant "Full Disk Access for remote users" to bypass these protections.

## Verification

After enabling both settings, verify everything is working:

### Test Remote Login

1. **Check SSH Service**
   - Open Terminal
   - Run: `sudo lsof -i :22`
   - You should see `sshd` listening on port 22

2. **Test Local SSH Connection**
   - In Terminal, try: `ssh localhost`
   - You should be able to connect (may require password or key)

3. **Verify in CodeFrog**
   - Create a new local project in CodeFrog
   - The terminal should work without errors
   - File browser should access your folders

### Common Issues

- **"Connection refused"** - Remote Login may not be fully enabled, try toggling it off and on
- **"Permission denied"** - Your username may not be in the allowed users list
- **Cannot access Documents/Desktop** - Full Disk Access for remote users may not be enabled

## Troubleshooting

If you encounter issues after setup:

- **Remote Login won't enable**: Restart your Mac and try again
- **SSH connection fails**: Verify your username is in the allowed users list
- **File access denied**: Check that "Full Disk Access for remote users" is enabled
- **Terminal not working in CodeFrog**: Ensure Remote Login is enabled and restart CodeFrog

For more detailed troubleshooting, see the [Troubleshooting Guide](/help/mas/troubleshooting).

## Next Steps

- [Getting Started Guide](/help/mas/getting-started) - Learn how to create your first project
- [Project Workflows](/help/mas/workflows) - Understand local vs. remote development
- [Troubleshooting](/help/mas/troubleshooting) - Find solutions to common issues

