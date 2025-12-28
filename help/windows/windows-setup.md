---
title: Windows Setup Guide
redirect_from:
  - /help/windows-setup.php
layout: help
---

# Windows Setup Guide

This guide walks you through the Windows system settings and configuration required for CodeFrog to work properly with local projects and SSH connections.

## Overview

CodeFrog on Windows requires several system configurations for full functionality:

1. **Windows Store Installation** - Installing CodeFrog from the Microsoft Store
2. **System Requirements** - Ensuring your Windows version meets requirements
3. **File Access Permissions** - Understanding Windows file system permissions
4. **SSH Setup** - Configuring OpenSSH for localhost connections
5. **Long Path Support** - Enabling support for paths longer than 260 characters
6. **Terminal Integration** - Configuring Windows Terminal, PowerShell, or CMD
7. **Security Considerations** - Windows Defender and firewall settings

## Windows Store Installation

If you're installing CodeFrog from the Microsoft Store:

1. **Open Microsoft Store**
   - Click the Start menu
   - Search for "Microsoft Store" and open it

2. **Search for CodeFrog**
   - Type "CodeFrog" in the search bar
   - Select CodeFrog from the results

3. **Install the App**
   - Click the "Get" or "Install" button
   - Wait for the installation to complete

4. **Launch CodeFrog**
   - Click "Launch" from the Store, or
   - Find CodeFrog in your Start menu and launch it

### Post-Installation

After installation, CodeFrog will:
- Automatically check for updates through the Microsoft Store
- Handle permissions through Windows Store security model
- Provide automatic updates when new versions are available

## System Requirements

CodeFrog requires:

- **Windows 10 version 1607 or later** (for long path support)
- **Windows 11** (fully supported)
- **Administrator privileges** (for some setup steps like enabling long paths)
- **OpenSSH Client** (usually pre-installed on Windows 10/11)

### Checking Your Windows Version

1. Press `Win + R` to open Run dialog
2. Type `winver` and press Enter
3. Check the version number displayed

## File Access Permissions

Windows uses User Account Control (UAC) and file system permissions to protect your files.

### Understanding Windows Permissions

- **User Account Control (UAC)**: Windows may prompt for administrator privileges for certain operations
- **File System Permissions**: Each folder has specific access permissions
- **Long Paths**: Windows has a default 260-character path limit that may need to be enabled

### Granting Folder Access

When CodeFrog needs to access a folder:

1. **Select Folder Dialog**
   - CodeFrog will show a folder picker dialog
   - Navigate to and select your project folder
   - Click "Select Folder"

2. **UAC Prompts**
   - If Windows shows a UAC prompt, click "Yes" to allow access
   - This is normal and required for file operations

3. **Permission Issues**
   - If you see "Access Denied" errors, check folder permissions
   - Right-click the folder → Properties → Security tab
   - Ensure your user account has "Full control" or "Modify" permissions

## Long Path Support

Windows has a default 260-character path limit. CodeFrog may need to access files in deep directory structures, so enabling long path support is recommended.

### Enabling Long Path Support

**Option 1: Using PowerShell Script (Recommended)**

1. **Run PowerShell as Administrator**
   - Right-click PowerShell in Start menu
   - Select "Run as Administrator"

2. **Navigate to CodeFrog Directory**
   ```powershell
   cd C:\path\to\codefrog\project
   ```

3. **Run the Enable Script**
   ```powershell
   .\enable_long_paths.ps1
   ```

4. **Restart Your Computer**
   - The change requires a restart to take effect
   - The script will offer to restart automatically

**Option 2: Manual Registry Edit**

1. **Open Registry Editor**
   - Press `Win + R`
   - Type `regedit` and press Enter
   - Click "Yes" on UAC prompt

2. **Navigate to File System Key**
   - Go to: `HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\FileSystem`

3. **Create or Modify LongPathsEnabled**
   - Find or create DWORD: `LongPathsEnabled`
   - Set value to: `1`
   - Click OK

4. **Restart Your Computer**

**Option 3: PowerShell Command**

Run this in PowerShell as Administrator:
```powershell
New-ItemProperty -Path "HKLM:\SYSTEM\CurrentControlSet\Control\FileSystem" -Name "LongPathsEnabled" -Value 1 -PropertyType DWORD -Force
```

Then restart your computer.

### Verifying Long Path Support

After restarting, verify it's enabled:
```powershell
Get-ItemProperty -Path "HKLM:\SYSTEM\CurrentControlSet\Control\FileSystem" -Name "LongPathsEnabled"
```

Should return: `LongPathsEnabled : 1`

## SSH Setup

CodeFrog uses SSH for terminal access and local project features. Windows 10 and 11 include OpenSSH Client by default.

### Checking OpenSSH Installation

1. **Open PowerShell**
   - Press `Win + X`
   - Select "Windows PowerShell" or "Terminal"

2. **Check SSH Version**
   ```powershell
   ssh -V
   ```
   - Should display version information if OpenSSH is installed

### Installing OpenSSH (If Not Installed)

1. **Open Settings**
   - Press `Win + I`
   - Go to **Apps** → **Optional Features**

2. **Add OpenSSH Client**
   - Click "Add a feature"
   - Search for "OpenSSH Client"
   - Select it and click "Install"

3. **Alternative: Using PowerShell (as Administrator)**
   ```powershell
   Add-WindowsCapability -Online -Name OpenSSH.Client~~~~0.0.1.0
   ```

### Configuring SSH for Localhost

For local projects, CodeFrog connects to `localhost` via SSH:

1. **SSH Service Status**
   - OpenSSH Server may need to be installed for localhost connections
   - Check if SSH server is running:
     ```powershell
     Get-Service sshd
     ```

2. **Installing OpenSSH Server (If Needed)**
   ```powershell
   Add-WindowsCapability -Online -Name OpenSSH.Server~~~~0.0.1.0
   Start-Service sshd
   Set-Service -Name sshd -StartupType 'Automatic'
   ```

3. **Firewall Configuration**
   - Windows Firewall should automatically allow SSH
   - If connection fails, check Windows Firewall settings
   - Ensure "OpenSSH SSH Server" is allowed

### SSH Key Management

SSH keys are stored in:
- **User keys**: `C:\Users\YourUsername\.ssh\`
- **System keys**: `C:\ProgramData\ssh\`

CodeFrog will use your default SSH keys for authentication.

## Terminal Integration

CodeFrog integrates with Windows terminal environments:

### Windows Terminal (Recommended)

Windows Terminal provides the best experience:

1. **Install Windows Terminal** (if not already installed)
   - Available from Microsoft Store
   - Or download from: https://aka.ms/terminal

2. **Configure as Default**
   - Windows Terminal is usually set as default on Windows 11
   - On Windows 10, set it in Windows Terminal settings

### PowerShell

PowerShell is the default terminal on modern Windows:

- **PowerShell 5.1**: Pre-installed on Windows 10/11
- **PowerShell 7+**: Available from Microsoft Store or GitHub

### Command Prompt (CMD)

CMD is available but less feature-rich:

- Use for basic commands
- PowerShell is recommended for better compatibility

### PATH Configuration

Ensure your PATH environment variable includes necessary tools:

1. **Open Environment Variables**
   - Press `Win + X` → System → Advanced system settings
   - Click "Environment Variables"

2. **Edit PATH**
   - Under "User variables", select "Path"
   - Click "Edit"
   - Add any custom tool paths if needed

## Security Considerations

### Windows Defender

Windows Defender may need to allow CodeFrog:

1. **Add Exclusion (If Needed)**
   - Open Windows Security
   - Go to Virus & threat protection
   - Click "Manage settings"
   - Add CodeFrog folder to exclusions if false positives occur

### Firewall Settings

Windows Firewall should automatically allow CodeFrog:

1. **Check Firewall Status**
   - Open Windows Security
   - Go to Firewall & network protection
   - Ensure firewall is enabled

2. **Allow Through Firewall (If Prompted)**
   - If Windows asks to allow CodeFrog through firewall, click "Allow"
   - This is required for network features

### UAC Prompts

User Account Control may prompt for certain operations:

- **File Access**: May prompt when accessing protected folders
- **Registry Changes**: Required for long path support
- **Network Access**: May prompt for firewall rules

Always verify the prompt is from CodeFrog before allowing.

## File Path Handling

Windows file paths have some unique characteristics:

### Path Formats

- **Standard paths**: `C:\Users\Username\Documents\Project`
- **UNC paths**: `\\Server\Share\Path` (for network drives)
- **Long paths**: Require long path support (see above)

### Case Sensitivity

- **Windows file system is case-insensitive by default**
- File names like `File.txt` and `file.txt` are treated as the same
- This differs from macOS/Linux which are case-sensitive

### Special Characters

Avoid these characters in file/folder names:
- `< > : " / \ | ? *`
- These are reserved by Windows

## Verification

After completing setup, verify everything is working:

### Test File Access

1. **Create a Test Project**
   - Open CodeFrog
   - Create a new local project
   - Select a folder on your system

2. **Verify File Browser**
   - Navigate to the project in CodeFrog
   - File browser should show your files
   - Try opening a file in the editor

### Test Terminal

1. **Open Terminal in CodeFrog**
   - Open your project
   - Click the Terminal tab
   - Terminal should open and be functional

2. **Test Commands**
   - Try basic commands: `dir`, `cd`, `pwd`
   - Verify you can navigate the file system

### Test SSH Connection

1. **Check SSH Service**
   ```powershell
   Get-Service sshd
   ```
   - Should show "Running" status

2. **Test Local Connection**
   ```powershell
   ssh localhost
   ```
   - Should connect (may require password or key)

## Common Issues

### "Path too long" Errors

**Solution**: Enable long path support (see Long Path Support section above)

### "Access Denied" Errors

**Solutions**:
- Check folder permissions (right-click → Properties → Security)
- Run CodeFrog as Administrator (not recommended for regular use)
- Check UAC settings

### SSH Connection Failures

**Solutions**:
- Verify OpenSSH Client is installed
- Check if OpenSSH Server is running (for localhost)
- Verify Windows Firewall allows SSH
- Check SSH service status: `Get-Service sshd`

### Terminal Not Starting

**Solutions**:
- Verify OpenSSH is installed
- Check Windows Terminal or PowerShell is available
- Try restarting CodeFrog
- Check terminal output for specific error messages

## Troubleshooting

If you encounter issues after setup:

- **Long paths not working**: Restart your computer after enabling
- **SSH connection fails**: Verify OpenSSH Server is installed and running
- **File access denied**: Check folder permissions and UAC settings
- **Terminal not working**: Ensure OpenSSH Client is installed

For more detailed troubleshooting, see the [Windows Troubleshooting Guide](/help/windows/windows-troubleshooting).

## Next Steps

- [Getting Started Guide](/help/windows/getting-started) - Learn how to create your first project
- [Project Workflows](/help/windows/workflows) - Understand local vs. remote development
- [Windows Troubleshooting](/help/windows/windows-troubleshooting) - Find solutions to common Windows issues

