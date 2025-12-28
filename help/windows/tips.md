---
title: Tips for New Users
redirect_from:
  - /help/tips.php
  - /help/tips.php?flavor=windows
  - /help/windows/tips.php
layout: help
---

# Tips for New Users

Get the most out of CodeFrog on Windows with these platform-specific tips and best practices.

## Windows-Specific Tips

### Terminal Configuration

CodeFrog works best with Windows Terminal, but also supports PowerShell and Command Prompt.

**Windows Terminal (Recommended)**:
- Install from Microsoft Store for the best experience
- Supports tabs, multiple panes, and customization
- Better color support and font rendering
- Set as default terminal in Windows Terminal settings

**PowerShell**:
- Pre-installed on Windows 10/11
- More powerful than Command Prompt
- Better script support and modern features
- Use PowerShell 7+ for best compatibility

**Command Prompt (CMD)**:
- Basic terminal support
- Use for simple commands
- Less feature-rich than PowerShell

**Terminal Tips**:
- Use `Ctrl + Shift + T` to open new terminal tabs (Windows Terminal)
- Right-click terminal for context menu options
- Customize terminal appearance in Windows Terminal settings
- Use `Ctrl + C` to cancel running commands

### File Path Handling

Windows file paths have unique characteristics:

**Long Paths**:
- Windows has a 260-character path limit by default
- Enable long path support for deep directory structures:
  ```powershell
  New-ItemProperty -Path "HKLM:\SYSTEM\CurrentControlSet\Control\FileSystem" -Name "LongPathsEnabled" -Value 1 -PropertyType DWORD -Force
  ```
  **Important**: This command must be run from an elevated PowerShell prompt (Run as Administrator). After running the command, restart your computer.
  
  **Note**: Enabling the registry key alone is not sufficient—applications must be marked `longPathAware` in their application manifest to actually use extended paths. Some applications (especially older ones) may not honor this setting even after the registry change. Modern applications like CodeFrog typically include this manifest setting, but you may need to check with individual application developers or modify application manifests for custom applications.
- See [Windows Setup Guide](/help/windows/windows-setup) for detailed instructions

**Case Sensitivity**:
- Windows file system is case-insensitive by default
- `File.txt` and `file.txt` are treated as the same file
- This differs from macOS/Linux which are case-sensitive
- Be aware when working with projects that will run on case-sensitive systems

**Path Formats**:
- Standard: `C:\Users\Username\Documents\Project`
- UNC (network): `\\Server\Share\Path`
- Avoid special characters: `< > : " / \ | ? *`

**Path Tips**:
- Keep project paths short to avoid long path issues
- Use forward slashes in code (they work on Windows too): `path/to/file`
- Be careful with spaces in paths - use quotes when needed

### SSH Key Management

Windows OpenSSH stores keys in a specific location:

**Key Locations**:
- User keys: `C:\Users\YourUsername\.ssh\`
- Private key: `id_rsa` or `id_ed25519`
- Public key: `id_rsa.pub` or `id_ed25519.pub`

**Key Management**:
- Generate new key: `ssh-keygen -t ed25519 -C "your_email@example.com"`
- Set proper permissions: Right-click private key → Properties → Security → Remove all users except your account
- Add public key to servers: Copy content of `.pub` file to server's `~/.ssh/authorized_keys`

**SSH Tips**:
- Use `ed25519` keys for better security and performance
- Keep private keys secure - never share them
- Use different keys for different servers if needed
- Test SSH connection: `ssh user@hostname` in PowerShell

### Chrome Detection

CodeFrog needs to detect Chrome for web testing features:

**Default Chrome Locations**:
- System: `C:\Program Files\Google\Chrome\Application\chrome.exe`
- 32-bit: `C:\Program Files (x86)\Google\Chrome\Application\chrome.exe`
- User: `C:\Users\YourUsername\AppData\Local\Google\Chrome\Application\chrome.exe`

**Chrome Tips**:
- Install Chrome to default location for automatic detection
- If Chrome isn't detected, reinstall to default location
- CodeFrog should automatically find Chrome in standard locations
- Some features may allow manual Chrome path specification

### OpenGrep DLL Dependencies

CodeFrog's code analysis uses OpenGrep, which requires specific DLL files:

**Required DLLs**:
- `libgmp-10.dll` - GNU Multiple Precision Arithmetic Library
- `libstdc++-6.dll` - C++ standard library
- `libgcc_s_seh-1.dll` - GCC runtime library

**DLL Management**:
- DLLs should be extracted automatically with OpenGrep binary
- If you see "missing DLL" errors:
  1. Close CodeFrog completely
  2. Delete the binaries cache folder (typically located at `C:\Users\YourUsername\AppData\Local\CodeFrog\Cache\Binaries`)
  3. Restart CodeFrog - it will re-extract DLLs
- Manual installation: Download DLLs from MinGW-w64 and place in same directory as `opengrep.exe`

**DLL Tips**:
- Ensure DLL architecture matches your system (32-bit vs 64-bit)
- Keep DLLs in the same directory as the executable
- Don't delete DLL files manually - let CodeFrog manage them

### File System Permissions

Windows uses User Account Control (UAC) and file permissions:

**UAC Prompts**:
- Windows may ask for permission for certain operations
- Click "Yes" when prompted (verify it's from CodeFrog)
- UAC is a security feature - don't disable it

**Folder Permissions**:
- Right-click folder → Properties → Security tab
- Ensure your user has "Full control" or "Modify" permissions
- Some system folders require elevated permissions

**Permission Tips**:
- Keep projects in user folders (Documents, Desktop) for easier access
- Avoid system-protected folders when possible
- If access is denied, check folder permissions
- Don't run CodeFrog as Administrator unless necessary

## General Tips

### Keyboard Shortcuts

While CodeFrog doesn't have platform-specific shortcuts, Windows system shortcuts work:

- `Win + D`: Show desktop
- `Win + Tab`: Task view
- `Alt + Tab`: Switch between windows
- `Win + Arrow keys`: Snap windows
- `Ctrl + Shift + Esc`: Task Manager

### Project Management

- **Use Short Paths**: Keep project paths short to avoid long path issues
- **Organize Projects**: Use a dedicated folder like `C:\Projects` or `C:\Dev`
- **Backup Regularly**: Use Git or other version control
- **Close Unused Windows**: Close windows you're not using to improve performance

### Performance Tips

- **Close Unused Windows**: Each window uses system resources
- **Check System Resources**: Use Task Manager to monitor CPU and memory
- **Update Windows**: Keep Windows updated for best performance
- **Update CodeFrog**: Install latest version from Microsoft Store

### Best Practices

- **Start with Setup**: Follow the [Windows Setup Guide](/help/windows/windows-setup) first
- **Enable Long Paths**: Enable long path support if working with deep directories
- **Use Windows Terminal**: Install Windows Terminal for better terminal experience
- **Keep OpenSSH Updated**: Ensure OpenSSH Client is installed and up to date
- **Regular Backups**: CodeFrog doesn't automatically backup - use Git for version control

## AI Assistant Guidance

### Recommended Development Setup

For the best development experience, we recommend using CodeFrog alongside dedicated IDEs and AI tools:

- **Primary IDE**: Use [Cursor](https://cursor.sh) or [VS Code](https://code.visualstudio.com) for your main coding work
  - These IDEs provide better AI assistance, debugging, and extension support
  - CodeFrog complements these tools with testing, security scanning, and project management

- **AI Code Review**: Use [CodeRabbit](https://coderabbit.ai) for automated PR reviews
  - CodeFrog can import CodeRabbit PR comments as tasks
  - See [CodeRabbit + Augment Workflow](/help/common/ai-coder-coderabbit-augment) for integration details

- **CLI Workflows**: Use PowerShell or Windows Terminal for AI CLI tools
  - CodeFrog doesn't include embedded AI CLI tools by design
  - This gives you flexibility to use the AI tools that work best for your workflow

### Why Not AI CLI in CodeFrog?

CodeFrog intentionally doesn't include embedded AI CLI programs. Instead, we recommend:

- **Using external IDEs** like Cursor for AI-powered coding
- **Using PowerShell/Terminal** for AI CLI tools when needed
- **Using CodeRabbit** for AI-powered code reviews

This approach provides better security, more flexibility, and lets you choose the AI tools that work best for you.

## Troubleshooting Tips

- **DLL Errors**: See [Windows Troubleshooting](/help/windows/windows-troubleshooting) for DLL issues
- **SSH Issues**: Check OpenSSH installation and firewall settings
- **Path Issues**: Enable long path support or move projects to shorter paths
- **Permission Issues**: Check folder permissions and UAC settings
- **Performance**: Close unused windows and check system resources

## Next Steps

- [Getting Started Guide](/help/windows/getting-started) - Learn the basics
- [Windows Setup Guide](/help/windows/windows-setup) - Configure CodeFrog properly
- [Windows Troubleshooting](/help/windows/windows-troubleshooting) - Solve common issues
- [Keyboard Shortcuts](/help/windows/shortcuts) - Boost productivity

