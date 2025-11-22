---
title: AI Code Review Workflow - CodeRabbit + Augment Code
layout: help
---

## Overview

This workflow helps you efficiently handle code review feedback from CodeRabbit by importing comments into Augment Code tasks, fixing issues with AI assistance, and tracking progress.

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
   - Commit separately with clear messages

### 2. Export PR Comments to Markdown

When CodeRabbit reviews your pull request, export the comments:

1. **In CodeRabbit Interface:**
   - Navigate to your PR
   - Find the export option (usually in PR settings or comments section)
   - Export unresolved comments to Markdown format

2. **Include in Export:**
   - PR number (e.g., `PR#123`)
   - Comment IDs (e.g., `Comment #456`)
   - Comment text and context
   - File paths and line numbers

3. **Save Export:**
   - Save as `pr-comments.md` or similar
   - Keep it accessible for import

### 3. Selective Bulk Import (Simple/Routine Issues Only)

**⚠️ Only import simple/routine issues in bulk. Major/complex issues should already be handled individually.**

Import the exported comments as tasks in CodeFrog:

1. **Open CodeFrog:**
   - Navigate to the Tasks tab
   - Select "Import Tasks" or "Bulk Create"

2. **Select Issues to Import:**
   - **Only select simple/routine issues** from your List B
   - Skip any major/complex issues (these should be handled individually)
   - Verify you're only importing low-risk, straightforward fixes

3. **Format Tasks:**
   - Task title format: `PR#{pr} Comment #{id}: {description}`
   - Example: `PR#123 Comment #456: Fix null pointer exception`
   - Include file path and line number in description

4. **Import Settings:**
   - **Import unresolved only:** Don't import comments that are already resolved
   - **Hide nitpicks:** Filter out minor style suggestions
   - **Group by file:** Optionally group related comments

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

3. **Using Augment:**
   - Open the file with the issues
   - Select the problematic code
   - Use Augment's AI suggestions to fix
   - **Review each fix carefully** before accepting
   - Test each fix before moving to the next

4. **Task Management:**
   - Mark tasks as "In Progress" while working
   - Mark as "Completed" when fixed and tested
   - CodeFrog supports auto-completion when code changes are detected
   - Complete one batch before starting the next

### 5. Verify Fixes

After fixing issues:

1. **Test Changes:**
   - Run tests to ensure fixes work
   - Verify no regressions introduced
   - Check edge cases

2. **Update Tasks:**
   - Mark tasks as completed
   - Add notes about the fix
   - Link to commit or PR

3. **Re-run CodeRabbit:**
   - Push changes to PR
   - Let CodeRabbit re-review
   - Verify issues are resolved

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

## Screenshots and Examples

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
5. Mark all tasks complete
6. Commit with message: "Fix CodeRabbit issues in UserService.java"

## Auto-Completion Support

CodeFrog supports automatic task completion:

- **Code Detection:** Detects when code matching task description is changed
- **Git Integration:** Links tasks to commits
- **Status Updates:** Automatically updates task status

To enable:

1. Open Task Settings
2. Enable "Auto-complete on code change"
3. Configure matching rules

## Troubleshooting

### Import Issues

- **Format Problems:** Ensure Markdown export includes PR# and Comment# IDs
- **Missing Comments:** Check CodeRabbit export settings
- **Duplicate Tasks:** CodeFrog should detect and skip duplicates

### Augment Issues

- **No Suggestions:** Ensure Augment CLI is installed and configured
- **Wrong Fixes:** Review Augment suggestions carefully, don't accept blindly
- **Context Missing:** Provide more context in task description

## Related Topics

- [Cursor / Other AI Agents](/help/mas/ai-coder-cursor) - Using other AI tools
- [Getting Started](/help/mas/getting-started) - CodeFrog basics
- [Project Workflows](/help/mas/workflows) - Development workflows

