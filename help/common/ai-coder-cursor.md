---
title: AI Code Review: Cursor & Other Agents
layout: help
---

# AI Code Review: Cursor & Other Agents

## Overview

This workflow helps you use Cursor or other AI coding agents to fix code review issues efficiently by providing structured prompts and managing the fix process.

## ⚠️ Critical: Manual Review First

**Before using any bulk copy/paste or automation, you MUST:**

1. **Review all issues by hand** - Don't skip this step!
2. **Identify major/complex problems** - These include:
   - Security vulnerabilities
   - Architectural changes
   - Complex logic bugs
   - Performance issues
   - Breaking changes
3. **Address major/complex problems one at a time** - Fix these individually with careful review
4. **Identify straightforward, low-risk issues** - These include:
   - Simple null checks
   - Style fixes
   - Minor refactoring
   - Simple validation
5. **Only bulk copy/paste straightforward, low-risk issues** - Never bulk process complex problems

**Why this matters:** Bulk processing complex issues can lead to incorrect fixes, introduce bugs, or miss important context. Always triage manually first.

## Workflow Steps

### 1. Manual Review and Triage

**CRITICAL STEP - Do not skip:**

1. **Review all code review issues:**
   - Read through every issue carefully
   - Understand the context and severity
   - Note which issues are related

2. **Categorize issues:**
   - **Major/Complex:** Handle individually (see above)
   - **Straightforward/Low-risk:** Can be bulk processed (see above)

3. **Create separate lists:**
   - List A: Major/complex problems (handle individually)
   - List B: Straightforward, low-risk issues (can bulk process)

4. **Handle major problems first:**
   - Fix each major/complex problem individually
   - Test thoroughly
   - Use [GitHub Desktop](https://desktop.github.com/) or your Git client to commit separately with clear messages

### 2. Prepare Issue List (Straightforward Issues Only)

**⚠️ Only prepare straightforward, low-risk issues for bulk processing. Major/complex problems should already be handled individually.**

Collect only the straightforward, low-risk issues from your List B:

1. **From Code Review:**
   - For GitHub PRs: Use CodeFrog's GitHub tab → PR Import Banner → Import to Tasks → Export in **Simple text format** (automated export, then paste the list of issues into the agent)
   - For other platforms: Export comments manually
   - **Only include straightforward, low-risk issues**
   - Format as a simple list
   - Include file paths and line numbers

2. **From CodeFrog Scans:**
   - Export findings from security scans (only simple fixes)
   - Export accessibility issues (only straightforward fixes)
   - Include severity and descriptions

3. **Format for AI:**
   - One issue per line or bullet point
   - Include context (file, line, description)
   - Group by file or type
   - **Maximum 15-20 issues** for optimal AI performance

### 3. Create AI Prompt

Use this prompt template with Cursor or other AI agents:

```
Fix these code review issues. Keep existing behavior intact, write tests for changes, and summarize the diffs.

Issues to fix:
{issue_list}

Requirements:
- Maintain existing functionality
- Write unit tests for all changes
- Follow existing code style
- Add comments for complex logic
- Summarize what was changed and why
```

### 4. Batch Processing

Work in manageable batches with careful review:

1. **Recommended Batch Sizes:**
   - **Small batch (5-10 issues):** Recommended for first-time users or complex codebases
   - **Medium batch (10-15 issues):** Optimal for most cases, standard workflow
   - **Large batch (15-20 issues):** Only for very simple, routine fixes
   - **Maximum: 20 issues** - Never exceed this limit

2. **Grouping Strategy:**
   - **By file:** Fix all issues in one file together
   - **By type:** Fix similar issues together (e.g., all null checks, naming issues, or formatting problems)
   - **By dependency:** Fix issues that depend on each other

3. **Process:**
   - Paste issue list into AI agent (one batch at a time)
   - **Review AI suggestions carefully** - don't accept blindly
   - Accept or modify fixes based on your review
   - Test changes before moving to next batch
   - Complete one batch before starting the next

### 5. Testing and Verification

After AI makes fixes:

1. **Run Tests:**
   - Execute existing test suite
   - Run new tests written by AI
   - Verify all tests pass

2. **Manual Review:**
   - Review code changes carefully
   - Ensure behavior is preserved
   - Check code style consistency

3. **Integration Testing:**
   - Test affected features
   - Verify no regressions
   - Check edge cases

### 6. Commit Strategy

Use [GitHub Desktop](https://desktop.github.com/) or your Git client to commit changes in logical chunks:

1. **One File Per Commit:**
   - Commit all fixes in one file together
   - Clear commit message: "Fix code review issues in {filename}"

2. **Related Changes:**
   - Group related fixes together
   - Separate unrelated changes

3. **Commit Messages:**
   - Clear and descriptive
   - Reference issue numbers if applicable
   - Include summary of changes

## Best Practices

### Prompt Engineering

**Good Prompt:**
```
Fix these 12 issues in UserService.java. Maintain existing API contracts, add null checks where needed, and write tests for new validation logic.

Issues:
1. Line 42: Potential null pointer
2. Line 67: Missing input validation
...
```

**Poor Prompt:**
```
Fix bugs
```

### Batch Size Guidelines

- **Too Small (1-5):** Inefficient, too much context switching
- **Small (5-10):** Good for first-time users or complex codebases
- **Optimal (10-15):** Good balance of focus and efficiency, standard workflow
- **Large (15-20):** Only for very simple, routine fixes
- **Too Large (20+):** Overwhelming, hard to review properly - **NEVER exceed 20 issues**

### Code Review

Always review AI-generated code:

- **Don't Accept Blindly:** AI can make mistakes
- **Verify Logic:** Ensure fixes are correct
- **Check Style:** Maintain code style consistency
- **Test Thoroughly:** Run comprehensive tests

## Example Workflow

### Step 1: Collect Issues

```
Issues to fix:
1. src/services/UserService.java:42 - Null pointer exception risk
2. src/services/UserService.java:67 - Missing input validation
3. src/utils/Validator.java:15 - Inefficient regex pattern
4. src/utils/Validator.java:23 - Missing error handling
...
```

### Step 2: Create Prompt

```
Fix these 10 code review issues in UserService and Validator classes. 
Keep existing behavior, add proper error handling, and write tests.

[Paste issue list]
```

### Step 3: Review AI Fixes

- Review each change
- Test functionality
- Verify tests pass
- Check code style

### Step 4: Commit

```bash
git add src/services/UserService.java src/utils/Validator.java
git commit -m "Fix code review issues: null checks, validation, error handling"
```

## Using with Different AI Agents

### Cursor

- Use Cursor's chat interface
- Paste issue list
- Review inline suggestions
- Accept or modify changes

### GitHub Copilot

- Use Copilot Chat
- Provide structured prompt
- Review suggestions
- Apply fixes

### ChatGPT / Claude

- Use code editor integration
- Paste code and issues
- Review suggestions
- Apply manually

### Other Tools

- Adapt workflow to tool capabilities
- Use structured prompts
- Always review and test

## Troubleshooting

### AI Makes Wrong Fixes

- **Provide More Context:** Include surrounding code
- **Be More Specific:** Clarify requirements
- **Break Into Smaller Batches:** Simplify the task
- **Manual Review:** Always review AI suggestions

### Tests Fail After Fixes

- **Review Test Changes:** AI may have modified tests incorrectly
- **Check Test Logic:** Ensure tests are testing the right thing
- **Run Tests Individually:** Isolate failing tests
- **Fix Tests Manually:** Don't rely solely on AI for tests

### Code Style Issues

- **Provide Style Guide:** Include style guidelines in prompt
- **Review Formatting:** Check indentation, spacing, etc.
- **Use Formatters:** Run code formatter after AI changes

## Related Topics

- [CodeRabbit + Augment Workflow](/help/common/ai-coder-coderabbit-augment) - Automated code review workflow
- [Project Workflows](/help/common/workflows) - Development workflows

