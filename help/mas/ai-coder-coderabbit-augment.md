---
title: AI Code Review Workflow - CodeRabbit + Augment Code
layout: help
---

## Overview

This workflow helps you efficiently handle code review feedback from CodeRabbit by importing comments into CodeFrog tasks, exporting them to Markdown format, fixing issues with Augment Code AI assistance, and tracking progress.

## ⚠️ Critical: Manual Review First

**Before using any bulk import or automation, you MUST:**

1. **Review all issues manually** - Don't skip this step!
2. **Identify major/complex issues** - These include:
   - Security vulnerabilities
   - Architectural changes
   - Complex logic bugs
   - Performance issues
   - Breaking changes
3. **Handle major/complex issues individually** - Fix these one at a time with careful review
4. **Identify simple/routine issues** - These include:
   - Style fixes (formatting, naming)
   - Simple null checks
   - Minor refactoring
   - Simple validation additions
5. **Only bulk import simple/routine issues** - Never bulk import complex issues

**Why this matters:** Bulk processing complex issues can lead to incorrect fixes, introduce bugs, or miss important context. Always triage manually first.

## Workflow Steps

### 1. Manual Review and Triage

**CRITICAL STEP - Do not skip:**

1. **Review all CodeRabbit comments:**
   - Read through every comment carefully
   - Understand the context and severity
   - Note which issues are related

2. **Categorize issues:**
   - **Major/Complex:** Handle individually (see above)
   - **Simple/Routine:** Can be bulk processed (see above)

3. **Create separate lists:**
   - List A: Major/complex issues (handle individually)
   - List B: Simple/routine issues (can bulk import)

4. **Handle major issues first:**
   - Fix each major/complex issue individually
   - Test thoroughly
   - Use [GitHub Desktop](https://desktop.github.com/) or your Git client to commit separately with clear messages

### 2. Import PR Comments to Tasks and Export to Markdown

When CodeRabbit reviews your pull request, import the comments into CodeFrog tasks and then export them:

1. **Navigate to GitHub Tab:**
   - Open CodeFrog
   - Go to the **GitHub** tab
   - Click on the PR you want to view

2. **Import PR Comments to Tasks:**
   - In the **PR Import Banner** (shown at the top of the PR view), you'll see options to import comments
   - Click the import button to import PR comments to the Tasks screen in CodeFrog
   - The banner will guide you through the import process
   - After importing, you'll be prompted to export to Markdown format

3. **Export Tasks:**
   - Navigate to the **Tasks** screen (🤖 Task Manager)
   - Find the **Export Tasks to Markdown** button in the upper right corner of the screen (download icon)
   - Click it to export your imported tasks
   - Choose your export format:
     - **Augment Code format**: For automated import into Augment Code (import the MD task list directly)
     - **Simple text format**: For other AI agents like Cursor (automated export, then paste the list of issues into the agent)
   - The file will be saved automatically

**Note:** The PR Import Banner also provides guidance on exporting the file after importing comments.

### 3. Selective Bulk Import (Simple/Routine Issues Only)

**⚠️ Only import simple/routine issues in bulk. Major/complex issues should already be handled individually.**

The import process happens directly in the PR Import Banner:

1. **In the PR Import Banner:**
   - The banner shows available comments to import
   - **Only simple/routine issues** with AI summaries can be imported automatically
   - Complex comments and those without AI summaries are marked and must be handled on the web

2. **Import Options:**
   - **Import Importable Comments:** Imports all simple/routine comments that have AI summaries
   - **Import First 20 Comments:** Imports the first 20 importable comments (recommended batch size)
   - **Import First 50 Comments:** Imports the first 50 importable comments (for larger batches)

3. **Task Format (Automatic):**
   - Tasks are automatically formatted as: `PR#{pr} Comment #{id}: {description}`
   - Example: `PR#123 Comment #456: Fix null pointer exception`
   - File paths and line numbers are included automatically

4. **After Import:**
   - You'll be prompted to export immediately
   - Choose **Augment Code format** for automated import, or **Simple text format** for pasting into other agents
   - Or navigate to the Tasks screen to export later using the export button in the upper right

5. **Review Imported Tasks:**
   - Verify only simple/routine issues were imported
   - Check task descriptions are complete
   - Adjust priorities if needed

### 4. Fix with Augment (Batch Processing)

Use Augment Code to fix the simple/routine issues in batches:

1. **Recommended Batch Sizes:**
   - **Small batch (5-10 issues):** Recommended for first-time users or complex codebases
   - **Medium batch (10-15 issues):** Standard workflow, optimal for most cases
   - **Large batch (15-20 issues):** Only for very simple, routine fixes
   - **Never exceed 20 issues** in a single batch

2. **Batch Processing Steps:**
   - Select one batch of issues (same file or similar fixes)
   - Work on one batch at a time
   - Keep related issues together (same file, similar fixes)
   - Don't try to fix everything at once

3. **Using Augment Code:**
   - Import the exported Markdown file (Augment Code format) into Augment Code
   - The task list will be automatically imported
   - Open the file with the issues
   - Select the problematic code
   - Use Augment's AI suggestions to fix
   - **Review each fix carefully** before accepting
   - Test each fix before moving to the next

4. **Task Management:**
   - Mark tasks as "In Progress" while working
   - Mark as "Completed" manually in CodeFrog when fixed and tested, or delete completed tickets (one or all) as an alternative
   - **Note:** CodeFrog does not automatically close tickets or mark PR comments as done
   - Complete one batch before starting the next

### 5. Verify Fixes

After fixing issues:

1. **Test Changes:**
   - Run tests to ensure fixes work
   - Verify no regressions introduced
   - Check edge cases

2. **Update Tasks in CodeFrog:**
   - Manually mark tasks as completed in CodeFrog, or delete completed tickets (one or all) as an alternative
   - Add notes about the fix before marking complete or deleting
   - Link to commit or PR
   - **Note:** CodeFrog does not automatically close tickets or mark PR comments as done

3. **CodeRabbit Resolution Tracking:**
   - Use [GitHub Desktop](https://desktop.github.com/) or your Git client to push changes to PR
   - CodeRabbit AI automatically verifies your fixes when you commit
   - CodeRabbit marks PR comments as resolved once your changes are committed
   - Let CodeRabbit re-review to verify all issues are resolved

## Best Practices

### Batch Size

- **10-20 issues:** Optimal batch size for focused work
- **Too small:** Inefficient context switching
- **Too large:** Overwhelming, hard to track progress

### Keeping Issues Together

Group related issues:

- **Same file:** Fix all issues in a file together
- **Similar fixes:** Fix similar issues in one batch
- **Dependencies:** Fix issues that depend on each other together

### Task Organization

- **Use labels/tags:** Categorize by type (bug, style, security)
- **Set priorities:** Critical issues first
- **Track progress:** Use task status to see what's done

## Examples and Workflow

### Example Task Import

```
PR#123 Comment #456: Fix null pointer exception in UserService.getUser()
File: src/services/UserService.java
Line: 42
Issue: Potential null pointer when user not found
```

### Example Batch Work

1. Select 15 tasks from same file
2. Open file in editor
3. Use Augment to fix all issues
4. Test changes
5. Mark all tasks complete (or delete completed tickets as an alternative)
6. Use [GitHub Desktop](https://desktop.github.com/) or your Git client to commit with message: "Fix CodeRabbit issues in UserService.java"

## Task and Comment Resolution

**CodeFrog Task Management:**
- CodeFrog does **not** support automatic task completion
- You must manually mark tasks as completed in CodeFrog, or delete completed tickets (one or all) as an alternative
- CodeFrog does not automatically close tickets or mark PR comments as done

**CodeRabbit Resolution Tracking:**
- CodeRabbit AI automatically verifies your fixes when you commit changes to the PR
- CodeRabbit marks PR comments as resolved once your committed changes address the issues
- This happens automatically on the GitHub PR - no manual action needed in CodeRabbit
- CodeRabbit's AI verification ensures your fixes actually resolve the reported issues

## Troubleshooting

### Import Issues

- **Format Problems:** Tasks are automatically formatted with PR# and Comment# IDs when imported from the PR Import Banner
- **Missing Comments:** Check that comments have AI summaries (required for automatic import). Complex comments must be handled on the web
- **Duplicate Tasks:** CodeFrog automatically detects and skips duplicates when importing

### Augment Issues

- **No Suggestions:** Ensure Augment CLI is installed and configured
- **Wrong Fixes:** Review Augment suggestions carefully, don't accept blindly
- **Context Missing:** Provide more context in task description

## Related Topics

- [Handling PRs with Many Comments](/help/mas/handling-pr-comments) - Efficiently process large code reviews with many comments
- [Cursor / Other AI Agents](/help/mas/ai-coder-cursor) - Using other AI tools
- [Getting Started](/help/mas/getting-started) - CodeFrog basics
- [Project Workflows](/help/mas/workflows) - Development workflows

