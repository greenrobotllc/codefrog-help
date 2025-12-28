---
title: Windows Troubleshooting
redirect_from:
  - /help/windows-troubleshooting.php
layout: help
---

# Windows Troubleshooting

This guide helps you resolve common issues when using CodeFrog on Windows.

## Missing DLL Errors

### libgmp-10.dll Missing

**Problem**: CodeFrog shows an error about missing `libgmp-10.dll` when running code analysis.

**Error Message**: 
```
OpenGrep binary failed to start: Missing required DLL (libgmp-10.dll)
```

**Solution**:

1. **Check DLL Location**
   - The DLL should be in the same directory as `opengrep.exe`
   - Expected location: `{CodeFrog Data Directory}\binaries\opengrep\libgmp-10.dll`
   - Check if the DLL file exists alongside the executable

2. **Re-extract Binaries**
   - CodeFrog should automatically extract required DLLs when extracting the OpenGrep binary
   - If DLLs are missing, try:
     - Close CodeFrog completely
     - Delete the binaries cache folder (usually in AppData)
     - Restart CodeFrog - it will re-extract binaries and DLLs

3. **Manual DLL Installation** (if automatic extraction fails)
   - Download `libgmp-10.dll` from MinGW-w64: https://www.mingw-w64.org/downloads/
   - Or download from a trusted source
   - Place the DLL in the same directory as `opengrep.exe`
   - Ensure the DLL version matches your system architecture (32-bit or 64-bit)

4. **Verify Other Required DLLs**
   - OpenGrep may also require:
     - `libstdc++-6.dll`
     - `libgcc_s_seh-1.dll`
   - These should be extracted automatically with the binary
   - If missing, download from MinGW-w64 and place in the same directory

### Other DLL Errors

**Problem**: Other DLL-related errors when running CodeFrog tools.

**Solutions**:
- **Visual C++ Redistributable**: Install Microsoft Visual C++ Redistributable
  - Download from: https://aka.ms/vs/17/release/vc_redist.x64.exe
  - Install and restart CodeFrog
- **Check Windows Version**: Ensure you're running Windows 10 version 1607 or later
- **System File Checker**: Run `sfc /scannow` in PowerShell as Administrator to repair system files

## Windows Store Issues

### Installation Problems

**Problem**: CodeFrog won't install from Microsoft Store.

**Solutions**:
- **Check Store Status**: Visit https://status.microsoft.com to check if Store services are down
- **Update Windows Store**: Open Microsoft Store → Click your profile → Settings → App updates → Get updates
- **Reset Store Cache**: 
  1. Press `Win + R`, type `wsreset.exe`, press Enter
  2. Wait for Store to reset and reopen
  3. Try installing again
- **Check Disk Space**: Ensure you have enough free disk space (at least 500MB)
- **Windows Updates**: Install pending Windows updates and restart

### Update Issues

**Problem**: CodeFrog won't update from Microsoft Store.

**Solutions**:
- **Check for Updates**: Open Microsoft Store → Library → Get updates
- **Restart Store**: Close Microsoft Store completely and reopen it
- **Clear Store Cache**: Run `wsreset.exe` (see above)
- **Check Internet**: Ensure you have a stable internet connection
- **Restart Computer**: Sometimes a restart resolves update issues

### Permission Issues

**Problem**: CodeFrog requests permissions but they're not granted.

**Solutions**:
- **UAC Prompts**: Click "Yes" when Windows asks for permission
- **App Permissions**: 
  1. Open Settings → Privacy
  2. Check each permission category (Camera, Microphone, etc.)
  3. Ensure CodeFrog has necessary permissions
- **Run as Administrator**: Only if absolutely necessary (not recommended for regular use)

## File Permissions

### Access Denied Errors

**Problem**: "Access Denied" when trying to access files or folders.

**Solutions**:

1. **Check Folder Permissions**
   - Right-click the folder → Properties → Security tab
   - Ensure your user account has "Full control" or "Modify" permissions
   - Click "Edit" to change permissions if needed

2. **UAC Settings**
   - Lower UAC settings may help (not recommended for security)
   - Settings → Accounts → Family & other users → Change account type

3. **Run as Administrator** (temporary workaround)
   - Right-click CodeFrog → Run as administrator
   - Not recommended for regular use due to security concerns

4. **Move Project Folder**
   - Move your project to a location with standard permissions (e.g., `C:\Users\YourName\Documents\Projects`)
   - Avoid system-protected folders

### Long Path Issues

**Problem**: "Path too long" errors when accessing files.

**Solutions**:

1. **Enable Long Path Support** (Recommended)
   - Run PowerShell as Administrator
   - Execute: `New-ItemProperty -Path "HKLM:\SYSTEM\CurrentControlSet\Control\FileSystem" -Name "LongPathsEnabled" -Value 1 -PropertyType DWORD -Force`
   - Restart your computer
   - See [Windows Setup Guide](/help/windows/windows-setup) for detailed instructions

2. **Move Project to Shorter Path**
   - Move project to a shorter path (e.g., `C:\Projects` instead of `C:\Users\YourName\Documents\GitHub\VeryLongProjectName`)
   - Update any references to the old path

3. **Use UNC Paths** (for network drives)
   - Use `\\Server\Share\Path` format for network locations
   - Note: UNC paths have their own length limits

## SSH Connectivity

### OpenSSH Not Installed

**Problem**: CodeFrog can't connect via SSH because OpenSSH is not available.

**Solutions**:

1. **Install OpenSSH Client**
   - Open Settings → Apps → Optional Features
   - Click "Add a feature"
   - Search for "OpenSSH Client"
   - Install it

2. **Install via PowerShell** (as Administrator)
   ```powershell
   Add-WindowsCapability -Online -Name OpenSSH.Client~~~~0.0.1.0
   ```

3. **Verify Installation**
   ```powershell
   ssh -V
   ```
   - Should display version information

### SSH Connection Failures

**Problem**: Cannot connect to localhost or remote servers via SSH.

**Solutions**:

1. **Check OpenSSH Server** (for localhost connections)
   ```powershell
   Get-Service sshd
   ```
   - Should show "Running" status
   - If not running: `Start-Service sshd`
   - Set to auto-start: `Set-Service -Name sshd -StartupType 'Automatic'`

2. **Install OpenSSH Server** (if not installed)
   ```powershell
   Add-WindowsCapability -Online -Name OpenSSH.Server~~~~0.0.1.0
   Start-Service sshd
   Set-Service -Name sshd -StartupType 'Automatic'
   ```

3. **Check Windows Firewall**
   - Open Windows Security → Firewall & network protection
   - Ensure "OpenSSH SSH Server" is allowed
   - If not, click "Allow an app through firewall" and enable OpenSSH Server

4. **Test SSH Connection**
   ```powershell
   ssh localhost
   ```
   - Should connect (may require password or key)

5. **Check SSH Service Status**
   ```powershell
   Get-Service sshd | Select-Object Status, StartType
   ```

### SSH Key Issues

**Problem**: SSH authentication fails even with correct credentials.

**Solutions**:

1. **Check SSH Key Location**
   - User keys: `C:\Users\YourUsername\.ssh\`
   - Ensure private key is named `id_rsa` or `id_ed25519`
   - Public key should be `id_rsa.pub` or `id_ed25519.pub`

2. **Verify Key Permissions**
   - Private key should have restricted permissions
   - Right-click private key → Properties → Security
   - Remove all users except your account
   - Ensure only you have "Full control"

3. **Generate New SSH Key** (if needed)
   ```powershell
   ssh-keygen -t ed25519 -C "your_email@example.com"
   ```
   - Follow prompts to create new key pair

4. **Add Public Key to Server**
   - Copy public key content
   - Add to server's `~/.ssh/authorized_keys` file

## Terminal Configuration

### Terminal Not Starting

**Problem**: Terminal doesn't open or shows errors in CodeFrog.

**Solutions**:

1. **Check OpenSSH Installation**
   - Ensure OpenSSH Client is installed (see SSH Connectivity section)

2. **Verify Terminal Application**
   - Windows Terminal (recommended): Available from Microsoft Store
   - PowerShell: Pre-installed on Windows 10/11
   - Command Prompt: Pre-installed

3. **Check PATH Environment Variable**
   - Press `Win + X` → System → Advanced system settings → Environment Variables
   - Verify PATH includes: `C:\Windows\System32\WindowsPowerShell\v1.0\`
   - Also check: `C:\Windows\System32\`

4. **Test Terminal Manually**
   - Open PowerShell or Command Prompt directly
   - If it works outside CodeFrog, the issue may be with CodeFrog's terminal integration
   - Try restarting CodeFrog

### PowerShell Issues

**Problem**: PowerShell commands don't work or show errors.

**Solutions**:

1. **Check Execution Policy**
   ```powershell
   Get-ExecutionPolicy
   ```
   - Should be "RemoteSigned" or "Unrestricted"
   - If "Restricted", change it:
     ```powershell
     Set-ExecutionPolicy RemoteSigned -Scope CurrentUser
     ```

2. **Update PowerShell**
   - Install PowerShell 7+ from Microsoft Store or GitHub
   - PowerShell 7 is more modern and compatible

3. **Check PATH Configuration**
   - Ensure PowerShell is in your PATH
   - Default location: `C:\Windows\System32\WindowsPowerShell\v1.0\`

### Windows Terminal Issues

**Problem**: Windows Terminal doesn't work or isn't detected.

**Solutions**:

1. **Install Windows Terminal**
   - Download from Microsoft Store
   - Or from: https://aka.ms/terminal

2. **Set as Default**
   - Open Windows Terminal
   - Settings → Startup → Default profile
   - Choose PowerShell or Command Prompt

3. **Check Installation**
   - Windows Terminal should be in: `C:\Users\YourUsername\AppData\Local\Microsoft\WindowsApps\`
   - Verify it's accessible from Start menu

## Multi-Window Management

### Windows Not Opening

**Problem**: New windows don't open when using "File → New Window".

**Solutions**:

1. **Check Window Limits**
   - CodeFrog may have limits on number of open windows
   - Close some windows and try again

2. **Restart CodeFrog**
   - Close all CodeFrog windows
   - Restart the application
   - Try opening a new window

3. **Check System Resources**
   - Open Task Manager (`Ctrl + Shift + Esc`)
   - Check memory and CPU usage
   - Close other applications if resources are low

### Window Management Issues

**Problem**: Windows behave unexpectedly or don't respond.

**Solutions**:

1. **Window Focus Issues**
   - Click on the window to bring it to focus
   - Use `Alt + Tab` to switch between windows
   - Check if window is minimized

2. **Window Positioning**
   - Drag windows to reposition
   - Use `Win + Arrow keys` to snap windows
   - Reset window layout in CodeFrog settings

3. **Multiple Monitors**
   - Ensure windows aren't on disconnected monitors
   - Use `Win + Shift + Arrow keys` to move windows between monitors

## Chrome Detection Issues

**Problem**: CodeFrog can't detect Chrome for web testing.

**Solutions**:

1. **Check Chrome Installation**
   - Verify Chrome is installed in default location:
     - `C:\Program Files\Google\Chrome\Application\chrome.exe`
     - `C:\Program Files (x86)\Google\Chrome\Application\chrome.exe`
   - Or user installation:
     - `C:\Users\YourUsername\AppData\Local\Google\Chrome\Application\chrome.exe`

2. **Reinstall Chrome**
   - Uninstall Chrome completely
   - Download and reinstall from: https://www.google.com/chrome/
   - Install to default location

3. **Check PATH**
   - Chrome should be accessible from PATH
   - Or CodeFrog should detect it automatically

4. **Manual Chrome Path**
   - Some CodeFrog features may allow manual Chrome path specification
   - Check settings for Chrome path configuration

## General Issues

### CodeFrog Won't Start

**Solutions**:
- **Check Windows Version**: Ensure Windows 10 version 1607+ or Windows 11
- **Restart Computer**: Sometimes a restart resolves startup issues
- **Check Event Viewer**: 
  1. Press `Win + X` → Event Viewer
  2. Check Windows Logs → Application
  3. Look for CodeFrog errors
- **Reinstall CodeFrog**: Uninstall and reinstall from Microsoft Store

### Performance Issues

**Solutions**:
- **Close Unused Windows**: Close windows you're not using
- **Check System Resources**: Use Task Manager to check CPU and memory
- **Disable Antivirus Temporarily**: Some antivirus software can slow down apps (re-enable after testing)
- **Update Windows**: Install latest Windows updates
- **Update CodeFrog**: Ensure you're running the latest version

### Crashes or Freezes

**Solutions**:
- **Check Logs**: CodeFrog logs may be in: `%APPDATA%\CodeFrog\logs\`
- **Update CodeFrog**: Install latest version from Microsoft Store
- **Update Windows**: Install latest Windows updates
- **Check for Conflicts**: Disable other security software temporarily
- **Report Issue**: Contact CodeFrog support with crash details

## Getting More Help

If you're still experiencing issues:

1. **Check Other Guides**
   - [Windows Setup Guide](/help/windows/windows-setup) - Detailed setup instructions
   - [Windows Store Subscriptions](/help/windows/windows-iap) - Subscription issues
   - [Getting Started](/help/windows/getting-started) - Basic usage

2. **Collect Information**
   - Note the exact error message
   - Check CodeFrog logs (if available)
   - Note what you were doing when the issue occurred
   - Check Windows Event Viewer for system errors

3. **Contact Support**
   - Visit CodeFrog support website
   - Include error messages and steps to reproduce
   - Mention you're using Windows and include your Windows version

## Next Steps

- [Windows Setup Guide](/help/windows/windows-setup) - Configure CodeFrog properly
- [Windows Store Subscriptions](/help/windows/windows-iap) - Manage your subscription
- [Getting Started](/help/windows/getting-started) - Learn CodeFrog basics

