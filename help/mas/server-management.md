---
title: Server Management & File Operations
layout: help
---

# Server Management & File Operations

CodeFrog provides comprehensive SSH server management and SFTP file operations, allowing you to connect to remote servers, monitor system resources, and manage files seamlessly. This feature is essential for remote development workflows, server administration, and managing projects hosted on cloud servers.

## Overview

Server Management & File Operations enables you to:

- **Connect to Remote Servers**: Secure SSH connections using RSA 4096-bit keys
- **Monitor Server Resources**: Real-time CPU, RAM, and disk usage tracking
- **Manage Files Remotely**: Full SFTP file operations (upload, download, delete, move, copy, rename)
- **Terminal Access**: Persistent terminal sessions for remote command execution
- **Connection Management**: Efficient connection pooling and health monitoring

## Accessing Server Management

**Access**: Welcome screen → **Manage Servers** or Navigation → **Servers**

You can access server management from:
- The Welcome screen's **"Manage Servers"** button
- The navigation menu's **"Servers"** option
- When creating a new project, choose **"SSH Connection"** as the connection type

## Setting Up SSH Connections

### Creating a New Server Connection

1. **Open Server Management**: Navigate to **Servers** in the navigation menu
2. **Add Server**: Click **"Add Server"** or **"New Connection"**
3. **Configure Connection**:
   - **Server Name**: A descriptive name for this server (e.g., "Production Web Server")
   - **Hostname or IP**: The server's hostname or IP address
   - **Port**: SSH port (default: 22)
   - **Username**: Your SSH username
   - **Authentication Method**: Choose SSH key or password
4. **SSH Key Setup** (Recommended):
   - Generate a new RSA 4096-bit key in CodeFrog, or
   - Import an existing private key
   - CodeFrog can automatically inject your public key to new servers during setup
5. **Test Connection**: Verify the connection works before saving
6. **Save Connection**: Store the connection for future use

### SSH Key Management

For secure and convenient connections, SSH key-based authentication is recommended:

#### Generating a New SSH Key

1. **In CodeFrog Settings**: Navigate to SSH key management
2. **Generate Key**: Click **"Generate New Key"**
3. **Key Type**: RSA 4096-bit (recommended for security)
4. **Save Private Key**: CodeFrog securely stores your private key
5. **Copy Public Key**: Copy the public key to add to your server

#### Adding Public Key to Server

1. **On Your Server**: Log in via SSH or console
2. **Create .ssh Directory** (if it doesn't exist):
   ```bash
   mkdir -p ~/.ssh
   chmod 700 ~/.ssh
   ```
3. **Add Public Key**: Append your public key to `~/.ssh/authorized_keys`:
   ```bash
   echo "your-public-key-here" >> ~/.ssh/authorized_keys
   chmod 600 ~/.ssh/authorized_keys
   ```
4. **Verify Permissions**: Ensure correct permissions on authorized_keys

#### Importing Existing SSH Keys

1. **In CodeFrog Settings**: Navigate to SSH key management
2. **Import Key**: Click **"Import Existing Key"**
3. **Select Private Key File**: Choose your private key file (usually `~/.ssh/id_rsa`)
4. **Enter Passphrase**: If your key is encrypted, enter the passphrase
5. **Save**: CodeFrog securely stores your imported key

### Password Authentication

Password authentication is also supported but is less secure:

- **Password Storage**: Passwords are stored securely but expire automatically
- **Security Note**: SSH keys are more secure and convenient
- **Use Cases**: Useful for temporary connections or when keys aren't available

## Server Monitoring

### Real-Time Resource Monitoring

CodeFrog provides real-time monitoring of server resources:

- **CPU Usage**: Current CPU utilization percentage
- **RAM Usage**: Memory usage and available memory
- **Disk Usage**: Hard drive space usage and available space
- **Connection Status**: Server connection health and status

### Monitoring Features

- **Live Updates**: Resource metrics update in real-time
- **Visual Indicators**: Color-coded status indicators (green/yellow/red)
- **Historical Tracking**: View resource usage over time
- **Alerts**: Notifications for high resource usage or connection issues

### Server Health

Monitor overall server health:

- **Connection Status**: Active, disconnected, or error states
- **Response Time**: Server response latency
- **Uptime**: Server uptime information
- **Health Score**: Overall server health assessment

## File Operations (SFTP)

CodeFrog provides comprehensive SFTP file management capabilities:

### File Upload

Upload files and folders to remote servers:

- **Single File Upload**: Upload individual files via file picker
- **Folder Upload**: Upload entire directories recursively
- **Drag and Drop**: Drag files from your Mac directly to the remote server
- **Progress Tracking**: See upload progress in real-time
- **Resume Support**: Resume interrupted uploads

### File Download

Download files and folders from remote servers:

- **Single File Download**: Download individual files
- **Recursive Download**: Download entire directories with all subdirectories
- **Selective Download**: Choose specific files or folders to download
- **Progress Tracking**: Monitor download progress
- **Resume Support**: Resume interrupted downloads

### File Operations

Manage files and folders on remote servers:

- **Delete**: Delete files and folders (with confirmation for safety)
- **Move**: Move files and folders to different locations
- **Copy**: Copy files and folders (duplicate)
- **Rename**: Rename files and folders
- **Create Directory**: Create new directories
- **View Properties**: See file size, permissions, modified time

### File Browser

Browse remote file systems with a familiar interface:

- **Directory Navigation**: Navigate through remote directories
- **File Listing**: View files with details (size, type, modified date)
- **Quick Look**: Preview files without downloading
- **Search**: Search for files and folders
- **Sorting**: Sort by name, size, date, or type

## Terminal Access

CodeFrog provides persistent terminal sessions for remote command execution:

### Terminal Features

- **Persistent Sessions**: Terminal sessions remain active across app restarts
- **Multiple Terminals**: Open multiple terminal sessions per server
- **Full Terminal Support**: All standard terminal features and commands
- **Command History**: Access previous commands
- **Copy/Paste**: Standard copy and paste functionality

### Use Cases

- **Remote Command Execution**: Run commands on remote servers
- **Server Administration**: Manage server configuration and services
- **Debugging**: Debug production issues remotely
- **File Operations**: Use command-line tools for advanced file operations
- **Log Viewing**: View and tail log files

## Connection Management

### Connection Pooling

CodeFrog efficiently manages SSH connections:

- **Reuse Connections**: Reuses existing connections when possible
- **Automatic Cleanup**: Closes idle connections to free resources
- **Connection Limits**: Manages connection limits per server
- **Performance**: Optimized for speed and resource usage

### Connection Health

Monitor and manage connection health:

- **Status Indicators**: Visual indicators for connection status
- **Auto-Reconnect**: Automatically reconnects on connection loss
- **Health Checks**: Periodic health checks to ensure connections are active
- **Error Handling**: Graceful handling of connection errors

### Managing Connections

- **View All Connections**: See all active and stored connections
- **Edit Connections**: Update connection settings
- **Test Connections**: Verify connections before use
- **Remove Connections**: Delete unused connections
- **Connection History**: View connection history and logs

## Remote Project Workflows

Server Management integrates with CodeFrog's project system:

### Creating Remote Projects

1. **New Project**: Click **"New Project"** from Welcome screen
2. **Choose Connection Type**: Select **"SSH Connection"**
3. **Select Server**: Choose an existing server connection or create a new one
4. **Select Project Directory**: Choose the remote project directory
5. **Create Project**: CodeFrog creates the project and connects to the server

### Working with Remote Projects

Once a remote project is created, you can:

- **File Browser**: Browse and edit files via SFTP
- **Code Editor**: Edit files directly in CodeFrog's code editor
- **Terminal Access**: Use terminal for build commands and Git operations
- **Code Analysis**: Run code analysis on remote files
- **GitHub Integration**: View PRs and import comments (Git operations require terminal)

See [Project Workflows](/help/mas/workflows) for detailed information on remote development.

## Security Best Practices

### SSH Key Security

- **Use Strong Keys**: Always use RSA 4096-bit or stronger keys
- **Protect Private Keys**: Never share private keys
- **Use Passphrases**: Encrypt private keys with strong passphrases
- **Rotate Keys**: Regularly rotate SSH keys for security

### Connection Security

- **Use SSH Keys**: Prefer SSH key authentication over passwords
- **Secure Servers**: Ensure remote servers are properly secured
- **Firewall Rules**: Configure firewall rules to restrict SSH access
- **Regular Updates**: Keep servers and SSH software updated

### File Transfer Security

- **SFTP Only**: CodeFrog uses secure SFTP (not unencrypted FTP)
- **Verify Files**: Verify file integrity after transfers
- **Backup Before Operations**: Always backup before major file operations
- **Confirm Destructive Actions**: CodeFrog confirms before deleting files

## Troubleshooting

### Connection Issues

**Problem**: Cannot connect to remote server

**Solutions**:
- Verify server hostname/IP address is correct
- Check that SSH service is running on the server
- Ensure firewall allows SSH connections (port 22)
- Test connection using Terminal: `ssh user@hostname`
- Verify SSH key is correctly added to server

### Authentication Failures

**Problem**: SSH authentication fails

**Solutions**:
- Verify SSH key is correctly added to `~/.ssh/authorized_keys` on server
- Check file permissions on server: `chmod 600 ~/.ssh/authorized_keys`
- Ensure correct username is being used
- Try password authentication to verify server access
- Check server logs for authentication errors

### File Operation Issues

**Problem**: File operations fail or are slow

**Solutions**:
- Check server disk space availability
- Verify file permissions on remote server
- Check network connectivity and latency
- Try smaller file transfers first
- Check server resource usage (CPU, RAM, disk I/O)

### Terminal Not Working

**Problem**: Terminal sessions don't work or disconnect

**Solutions**:
- Verify SSH connection is active
- Check server SSH configuration allows terminal access
- Try reconnecting to the server
- Check server logs for SSH errors
- Verify terminal is enabled in server SSH config

See [Troubleshooting](/help/mas/troubleshooting) for more detailed troubleshooting guidance.

## Use Cases

### Development Workflows

- **Remote Development**: Work on projects hosted on cloud servers
- **Server-Side Development**: Develop applications requiring server resources
- **Team Collaboration**: Share development environments via remote servers

### Server Administration

- **Server Monitoring**: Monitor server resources and health
- **Configuration Management**: Manage server configuration files
- **Log Management**: View and manage server logs
- **Service Management**: Start, stop, and restart services

### File Management

- **Deployment**: Upload application files to production servers
- **Backup Management**: Download backups and archives
- **Asset Management**: Manage static assets and media files
- **Configuration Sync**: Sync configuration files between environments

## Related Topics

- [Project Workflows](/help/mas/workflows) - Setting up local and remote projects
- [macOS Setup Guide](/help/mas/macos-setup) - macOS configuration for local SSH
- [Tools Available](/help/mas/tools) - Overview of all CodeFrog tools
- [Troubleshooting](/help/mas/troubleshooting) - Common issues and solutions

