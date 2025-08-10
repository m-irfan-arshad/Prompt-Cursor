# Code Review Prompt

## Purpose
Perform thorough code reviews by analyzing code quality, security, performance, and best practices to ensure production-ready code.

## When to Use
- Reviewing pull requests
- Auditing existing code
- Preparing code for production
- Onboarding new team members
- Improving code quality standards

## Input Requirements
- Code to review
- Programming language and framework
- Project context and requirements
- Team coding standards
- Performance requirements

## Example Usage

```prompt
Please perform a comprehensive code review for this [language/framework] code:

```[language]
[paste code here]
```

Context:
- Project: [project name]
- Purpose: [what the code does]
- Team Standards: [coding standards to follow]
- Performance Requirements: [any specific requirements]
- Security Considerations: [security requirements]

Please review for:
1. Code quality and readability
2. Security vulnerabilities
3. Performance issues
4. Best practices compliance
5. Error handling
6. Documentation
7. Testing coverage
8. Maintainability
9. Scalability concerns
10. Potential bugs

Provide:
- Specific issues found with line numbers
- Suggested improvements
- Security recommendations
- Performance optimizations
- Code examples for fixes
- Priority levels for each issue
```

## Expected Output
- Detailed review with specific issues
- Code examples for improvements
- Security and performance recommendations
- Priority-based action items
- Best practices suggestions

## Tips & Tricks
- Focus on high-impact issues first
- Provide specific, actionable feedback
- Include code examples for fixes
- Consider the broader system impact
- Balance perfection with practicality

## Related Prompts
- [Debugging](./debugging.md)
- [Performance Optimization](./performance-optimization.md)
- [Security Implementation](./security-implementation.md)
