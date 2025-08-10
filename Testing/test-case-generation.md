# Test Case Generation Prompt

## Purpose
Generate comprehensive test cases covering functional, non-functional, edge cases, and error scenarios to ensure robust application testing.

## When to Use
- Setting up new test suites
- Adding features to existing applications
- Ensuring complete test coverage
- Creating regression test plans
- Preparing for release testing

## Input Requirements
- Application functionality description
- User stories or requirements
- Technology stack details
- Testing framework preferences
- Performance requirements

## Example Usage

```prompt
I need to generate comprehensive test cases for a [application type] with the following functionality:

Application Details:
- Type: [web app/mobile app/API/etc.]
- Technology: [programming language/framework]
- Testing Framework: [preferred framework]
- Key Features: [list main features]

User Stories:
1. [user story 1]
2. [user story 2]
3. [user story 3]

Requirements:
- [functional requirements]
- [non-functional requirements]
- [performance requirements]
- [security requirements]

Please generate test cases for:
1. Unit Tests
   - Individual component testing
   - Edge cases
   - Error handling

2. Integration Tests
   - Component interaction
   - API endpoints
   - Database operations

3. Functional Tests
   - User workflows
   - Business logic
   - Feature validation

4. Non-Functional Tests
   - Performance testing
   - Security testing
   - Usability testing

5. Regression Tests
   - Critical path testing
   - Previous bug fixes
   - Core functionality

For each test case, include:
- Test ID and name
- Preconditions
- Test steps
- Expected results
- Test data requirements
- Priority level
- Automation feasibility
```

## Expected Output
- Comprehensive test case suite
- Test data specifications
- Priority classifications
- Automation recommendations
- Coverage analysis

## Tips & Tricks
- Start with happy path scenarios
- Include negative test cases
- Consider boundary conditions
- Plan for data-driven testing
- Focus on high-risk areas first

## Related Prompts
- [Load Testing](./load-testing.md)
- [Security Testing](./security-testing.md)
- [API Testing](./api-testing.md)
