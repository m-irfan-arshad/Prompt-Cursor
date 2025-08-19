# Testing Phase Prompts

This folder contains prompts for comprehensive testing strategies - from unit tests to end-to-end testing and performance validation. These prompts help you create robust testing suites that ensure your application works correctly under all conditions.

---

## Prompts Overview

### [Test Generation](./test-generation.md)
- **Purpose:** Generate unit, integration, and end-to-end (E2E) tests for your codebase.
- **How to Use:** Supply your code or function signatures and specify the types of tests you need. The prompt will help you scaffold tests for new or existing features, including edge cases and business logic.

### [Integration Testing](./integration-testing.md)
- **Purpose:** Validate how different modules, services, or components interact.
- **How to Use:** Describe the system components and their interactions. The prompt will help you create integration test scenarios, including both success and failure cases.

### [E2E Testing Strategy](./e2e-testing.md)
- **Purpose:** Simulate real user workflows to ensure business-critical flows work as expected.
- **How to Use:** Outline the user journeys or workflows to be tested. The prompt will help you generate E2E test scripts and strategies for cross-platform and cross-browser coverage.

### [Performance Testing](./performance-testing.md)
- **Purpose:** Assess application behavior under load, stress, and benchmark conditions.
- **How to Use:** Define expected traffic, data volumes, and performance goals. The prompt will help you create test plans and scripts to identify bottlenecks and validate scalability.

---

## How to Use This Folder

1. **Start with Test Generation** to ensure code coverage for new and existing code.
2. **Add Integration Tests** to verify component and service interactions.
3. **Develop E2E Tests** to validate complete user workflows.
4. **Run Performance Tests** to ensure your system meets performance and scalability requirements.

For each prompt:
- Open the corresponding `.md` file for detailed instructions and examples.
- Customize the input to match your project’s needs.
- Use the generated outputs as a foundation and adapt as needed.

---

## Best Practices

- Focus on critical business logic and user-facing features first.
- Cover both typical and edge cases in all tests.
- Use real integrations where possible; mock only when necessary.
- Prioritize high-value user journeys for E2E tests.
- Establish baseline metrics and test with realistic data for performance validation.

---

## Integration with Other Phases

- Use these prompts to validate code during development.
- Derive test scenarios from planning requirements.
- Integrate tests into your CI/CD pipeline.
- Update and refactor tests as your application evolves.

---

**Explore each prompt in this folder for step-by-step guidance and examples to strengthen your testing process.**