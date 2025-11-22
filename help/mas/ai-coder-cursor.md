---
title: AI Code Review Workflow - Cursor / Other Agents
layout: help
---

## Overview

This workflow helps you use Cursor or other AI coding agents to fix code review issues efficiently by providing structured prompts and managing the fix process.

## Workflow Steps

### 1. Prepare Issue List

Collect all code review issues:

1. **From Code Review:**
   - Export comments from GitHub, GitLab, or other platforms
   - Format as a simple list
   - Include file paths and line numbers

2. **From CodeFrog Scans:**
   - Export findings from security scans
   - Export accessibility issues
   - Include severity and descriptions

3. **Format for AI:**
   - One issue per line or bullet point
   - Include context (file, line, description)
   - Group by file or type

### 2. Create AI Prompt

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

### 3. Batch Processing

Work in manageable batches:

1. **Recommended Batch Size:**
   - **10-15 issues:** Optimal for focused work
   - Small enough to review carefully
   - Large enough to be efficient

2. **Grouping Strategy:**
   - **By file:** Fix all issues in one file together
   - **By type:** Fix similar issues together (e.g., all null checks)
   - **By dependency:** Fix issues that depend on each other

3. **Process:**
   - Paste issue list into AI agent
   - Review AI suggestions
   - Accept or modify fixes
   - Test changes

### 4. Testing and Verification

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

### 5. Commit Strategy

Commit changes in logical chunks:

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
- **Optimal (10-15):** Good balance of focus and efficiency
- **Too Large (20+):** Overwhelming, hard to review properly

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

- [CodeRabbit + Augment Workflow](/help/mas/ai-coder-coderabbit-augment) - Automated code review workflow
- [Getting Started](/help/mas/getting-started) - CodeFrog basics
- [Project Workflows](/help/mas/workflows) - Development workflows

