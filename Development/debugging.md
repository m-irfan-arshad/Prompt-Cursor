# Debugging Prompt

## Purpose
Systematically debug complex issues by analyzing error messages, logs, and system behavior to identify root causes and provide solutions.

## When to Use
- Application crashes or errors
- Performance issues
- Integration problems
- Infrastructure failures
- Security incidents
- Data inconsistencies

## Input Requirements
- Error messages and stack traces
- Relevant logs
- System configuration
- Steps to reproduce
- Environment details
- Recent changes

## Example Usage

```prompt
I'm experiencing [specific issue] in my [application/service] running on [platform/environment].

Error Details:
- Error Message: [paste error message]
- Stack Trace: [paste stack trace if available]
- Timestamp: [when it occurred]
- Frequency: [how often it happens]

Environment:
- Platform: [OS/Cloud]
- Runtime: [language/version]
- Dependencies: [relevant versions]
- Configuration: [relevant config]

Steps to Reproduce:
1. [step 1]
2. [step 2]
3. [step 3]

Recent Changes:
- [list recent deployments/changes]
- [any configuration updates]
- [new dependencies added]

What I've Tried:
- [list debugging attempts]
- [tools used]
- [results]

Please help me:
1. Identify the root cause
2. Provide a step-by-step debugging approach
3. Suggest immediate fixes
4. Recommend long-term solutions
5. List tools for better debugging
6. Create a monitoring strategy to prevent recurrence
```

## Expected Output
- Root cause analysis
- Step-by-step debugging approach
- Immediate and long-term solutions
- Recommended tools and techniques
- Prevention strategies
- Monitoring recommendations

## Tips & Tricks
- Start with the most recent error
- Check logs from multiple sources
- Verify environment consistency
- Test in isolation when possible
- Document your debugging process
- Use systematic elimination approach

## Related Prompts
- [Error Handling](./error-handling.md)
- [Logging Best Practices](./logging-best-practices.md)
- [Performance Optimization](./performance-optimization.md)
