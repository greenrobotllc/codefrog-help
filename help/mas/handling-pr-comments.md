---
title: Handling Pull Requests with Many Comments
redirect_from:
  - /help/handling-pr-comments.php
  - /help/handling-pr-comments.php?flavor=mas
layout: help
---

# Handling Pull Requests with Many Comments

When a pull request receives dozens or hundreds of code review comments (especially from automated tools like CodeRabbit), it can feel overwhelming. CodeFrog provides a streamlined workflow to help you efficiently process and address all feedback.

## Overview

The key to handling large PRs is a **two-phase approach**:

1. **Manual Review First**: Review and handle critical/tough issues independently
2. **Bulk Import & AI Assistance**: Import remaining issues to markdown for AI agent assistance

This workflow ensures you address important issues with proper care while efficiently handling routine feedback.

## Step-by-Step Workflow

### Phase 1: Manual Review of Critical Issues

**⚠️ Critical Step - Do Not Skip**

Before importing anything, manually review all PR comments to identify issues that need individual attention:

1. **Open the PR in CodeFrog:**
   - Navigate to the **GitHub** tab
   - Select the repository and pull request
   - Review all comments in the PR view

2. **Identify Critical/Tough Issues:**
   - **Security vulnerabilities** - These need careful review
   - **Architectural changes** - Major design decisions
   - **Complex logic bugs** - Issues requiring deep understanding
   - **Performance issues** - Optimization opportunities
   - **Breaking changes** - Changes that affect other code
   - **Context-dependent issues** - Comments requiring domain knowledge

3. **Handle Critical Issues First:**
   - Fix each critical issue individually
   - Test thoroughly after each fix
   - Use [GitHub Desktop](https://desktop.github.com/) or your Git client to commit separately with clear commit messages
   - Mark as resolved in GitHub if applicable

4. **Note Simple/Routine Issues:**
   - Style fixes (formatting, naming conventions)
   - Simple null checks
   - Minor refactoring
   - Simple validation additions
   - Documentation updates

**Why this matters:** Critical issues require human judgment and context. Bulk processing them can lead to incorrect fixes or missed important details.

### Phase 2: Import All Issues to Markdown

Once you've handled the critical issues, use CodeFrog's GitHub tab to import all remaining comments into a markdown file:

1. **Navigate to GitHub Tab:**
   - Open CodeFrog
   - Go to the **GitHub** tab (in the navigation menu)
   - Select your repository
   - Click on the pull request with many comments

2. **Review the PR Import Banner:**
   - At the top of the PR view, you'll see the **PR Import Banner**
   - It shows:
     - Total number of unresolved comments
     - Number of importable comments (those with AI summaries)
     - Number of complex comments (must be handled on web)

3. **Import All Comments:**
   - Click **"Import Importable Comments"** to import all comments with AI summaries
   - Or use **"Import First 20 Comments"** or **"Import First 50 Comments"** for batch processing
   - Comments are automatically imported as tasks with format: `PR#{pr} Comment #{id}: {description}`
   - File paths and line numbers are included automatically

4. **Export to Markdown:**
   - After importing, you'll be prompted to export immediately
   - Or navigate to the **Tasks** screen (🤖 Task Manager icon)
   - Click the **Export Tasks to Markdown** button (download icon) in the upper right
   - Choose your export format:
     - **Augment Code format**: For automated import into Augment Code
     - **Simple text format**: For pasting into other AI agents like Cursor

5. **Use with AI Agents:**
   - Open the exported markdown file
   - Copy the contents
   - Paste into your AI agent of choice (Cursor, ChatGPT, Claude, etc.)
   - The AI agent can help you:
     - Prioritize remaining issues
     - Generate fixes for routine issues
     - Suggest code improvements
     - Create a plan for addressing all comments

## Best Practices

### Triage Strategy

**Handle Individually:**
- Security vulnerabilities
- Architectural decisions
- Complex bugs
- Performance optimizations
- Breaking changes

**Bulk Process:**
- Style fixes
- Simple null checks
- Formatting issues
- Minor refactoring
- Documentation updates

### Import Strategy

1. **Start Small**: Use "Import First 20 Comments" to test the workflow
2. **Review Imported Tasks**: Check that tasks are formatted correctly
3. **Export Early**: Export to markdown after each batch to avoid losing work
4. **Clear Between PRs**: Clear your task list before importing a new PR

### AI Agent Workflow

When pasting into AI agents:

1. **Provide Context**: Include relevant code snippets or file paths
2. **Ask for Prioritization**: Have the AI suggest which issues to tackle first
3. **Request Fixes**: Ask for code fixes for routine issues
4. **Review AI Suggestions**: Always review AI-generated fixes before applying
5. **Test Thoroughly**: Test all fixes, even AI-generated ones

## Example Workflow

### Scenario: PR with 150 CodeRabbit Comments

1. **Manual Review (30 minutes):**
   - Review all 150 comments
   - Identify 15 critical issues (security, architecture)
   - Fix 15 critical issues individually
   - Use your Git client to commit each fix separately

2. **Bulk Import (5 minutes):**
   - Import remaining 135 comments via GitHub tab
   - Export to markdown format
   - Clear task list

3. **AI Assistance (20 minutes):**
   - Paste markdown into Cursor or other AI agent
   - Have AI prioritize remaining issues
   - Generate fixes for routine issues
   - Review and apply fixes

4. **Final Review (10 minutes):**
   - Test all changes
   - Verify all comments are addressed
   - Update PR with status

**Total Time**: ~65 minutes vs. hours of manual work

## Tips for Large PRs

### Organization

- **Use Tags**: Tag imported tasks by category (security, style, refactor)
- **Filter by Priority**: Use task priority to focus on high-priority items first
- **Batch Processing**: Process comments in batches of 20-50 at a time

### Efficiency

- **Export Frequently**: Export after each import batch
- **Clear Between PRs**: Don't mix tasks from different PRs
- **Use AI Summaries**: Focus on comments with AI summaries for bulk processing
- **Handle Complex Comments Separately**: Complex comments without AI summaries need web review

### Quality

- **Always Review**: Even AI-generated fixes need human review
- **Test Everything**: Test all changes, especially bulk-processed ones
- **Commit Strategically**: Use your Git client to group related fixes in single commits
- **Document Decisions**: Add comments explaining non-obvious fixes

## Troubleshooting

### Import Issues

- **No Comments Showing**: Ensure you're viewing the correct PR and repository
- **Import Fails**: Check your GitHub OAuth token is valid
- **Missing Comments**: Complex comments without AI summaries must be handled on GitHub web interface

### Export Issues

- **Export Button Missing**: Ensure you have imported tasks first
- **Wrong Format**: Choose the correct format for your AI agent
- **File Not Found**: Check your Downloads folder or the path shown in the success message

### AI Agent Issues

- **Too Many Issues**: Break the markdown into smaller chunks (50-100 issues at a time)
- **Context Missing**: Include file paths and line numbers when pasting to AI
- **Format Issues**: Use "Simple text format" for most AI agents

## Related Guides

- [CodeRabbit + Augment Workflow](/help/mas/ai-coder-coderabbit-augment) - Detailed AI integration workflow
- [Recommended Tools & Integrations](/help/mas/recommended-tools) - IDEs and tools that work with CodeFrog
- [Project Workflows](/help/mas/workflows) - Setting up your development workflow
- [Tips for New Users](/help/mas/tips) - General productivity tips

## Summary

Handling PRs with many comments doesn't have to be overwhelming:

1. ✅ **Review manually first** - Identify and fix critical issues
2. ✅ **Import to CodeFrog** - Use the GitHub tab to import all comments
3. ✅ **Export to markdown** - Create a markdown file from the Tasks screen
4. ✅ **Use AI agents** - Paste markdown into Cursor or other AI tools
5. ✅ **Review and test** - Always review AI suggestions before applying

This workflow combines human judgment for critical issues with AI efficiency for routine feedback, making large PRs manageable.

