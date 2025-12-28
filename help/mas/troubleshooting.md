---
title: Troubleshooting & FAQ
redirect_from:
  - /help/troubleshooting.php
  - /help/troubleshooting.php?flavor=mas
layout: help
---

# Troubleshooting & FAQ

## macOS-Specific Issues

### Cannot Access Local Folder

**Problem:** CodeFrog shows an error when trying to access a local project folder.

**Solutions:**
- Make sure you granted folder access when creating the project
- Try deleting and recreating the project to re-grant access
- Check if the folder still exists at the original location
- For system folders, you may need to grant Full Disk Access (see [macOS Setup](/help/mas/macos-setup))

### Remote Login Not Working

**Problem:** CodeFrog cannot connect to localhost even though Remote Login is enabled.

**Solutions:**
- Open System Settings → General → Sharing → Remote Login
- Make sure Remote Login is toggled ON
- Ensure your user account is in the "Allow access for" list
- Try toggling Remote Login OFF and back ON
- Restart CodeFrog after enabling Remote Login
- Check if SSH is listening: run `sudo lsof -i :22` in Terminal

### Terminal Not Starting

**Problem:** The terminal shows an error or doesn't start.

**Solutions:**
- Ensure Remote Login is enabled (for local projects)
- Check App Settings to verify terminal configuration
- Try restarting the project
- Check the terminal output for specific error messages

### Full Disk Access Issues

**Problem:** CodeFrog cannot access certain files or folders.

**Solutions:**
- Open System Settings → Privacy & Security → Full Disk Access
- Add CodeFrog to the list if it's not there
- Toggle CodeFrog OFF and back ON
- Restart CodeFrog
- If issues persist, remove CodeFrog from the list and re-add it
- See [macOS Setup Guide](/help/mas/macos-setup) for detailed instructions

## Connection Issues

### Cannot Connect to Remote Server

**Problem:** SSH connection fails when trying to connect to a remote server.

**Solutions:**
- Verify the server hostname/IP address is correct
- Check that the port is correct (default: 22)
- Ensure the server is running and accessible
- Test the connection using Terminal: `ssh user@hostname`
- Check your network connection
- Verify firewall settings aren't blocking SSH
- Make sure SSH service is running on the remote server

### SSH Authentication Failed

**Problem:** SSH connection fails with authentication error.

**Solutions:**
- Verify your username is correct
- If using password: Check that the password is correct
- If using SSH key: Ensure the public key is in the server's `~/.ssh/authorized_keys`
- Check SSH key permissions: private key should be 600, public key should be 644
- Try password authentication as a fallback
- Generate a new SSH key pair if the current one isn't working

### Connection Drops Frequently

**Problem:** SSH connection disconnects unexpectedly.

**Solutions:**
- Check your network stability
- Increase SSH keep-alive settings on the server
- Try connecting from a different network
- Contact your server administrator about connection timeouts

## GitHub Integration Issues

### Cannot Connect GitHub Account

**Problem:** OAuth authorization fails or doesn't redirect back to CodeFrog.

**Solutions:**
- Make sure you're logged into GitHub in your browser
- Try disconnecting and reconnecting your GitHub account
- Clear your browser cookies and try again
- Check that CodeFrog is allowed in your GitHub OAuth settings
- Visit [github.com/settings/applications](https://github.com/settings/applications) to manage authorized apps

### PR Comments Not Importing

**Problem:** GitHub PR comments don't appear in the task manager.

**Solutions:**
- Make sure the PR has unresolved comments
- Check that you're viewing the correct repository
- Try refreshing the PR view
- Verify your GitHub connection is still active
- Check if the comments are marked as "nitpick" (hidden by default)

## File Browser Issues

### Files Not Showing

**Problem:** File browser is empty or doesn't show all files.

**Solutions:**
- Click the refresh button to reload the file list
- Check if you're in the correct directory
- For local projects: Verify folder access permissions
- For remote projects: Check SSH connection status
- Look for hidden files (files starting with .)

## Getting More Help

- [Getting Started Guide](/help/mas/getting-started) - Basic setup instructions
- [macOS Setup](/help/mas/macos-setup) - Detailed macOS configuration
- [Project Workflows](/help/common/workflows) - Understanding local vs. remote workflows
- [Send Feedback](https://greenrobot.freshdesk.com/support/solutions/9000119001) - Contact support

