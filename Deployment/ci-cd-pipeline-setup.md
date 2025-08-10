# CI/CD Pipeline Setup Prompt

## Purpose
Design and implement a robust CI/CD pipeline that automates building, testing, and deploying applications with proper security, testing, and rollback capabilities.

## When to Use
- Setting up new CI/CD pipelines
- Migrating from manual deployments
- Improving existing pipelines
- Adding new environments
- Implementing security scanning
- Optimizing deployment speed

## Input Requirements
- Application type and technology stack
- Current deployment process
- Target environments
- Security requirements
- Team size and expertise
- Infrastructure details

## Example Usage

```prompt
I need to set up a CI/CD pipeline for a [application type] built with [technology stack] that needs to deploy to [environments].

Current Setup:
- Source Control: [GitHub/GitLab/etc.]
- Build Tool: [Maven/Gradle/npm/etc.]
- Runtime: [Java/Node.js/Python/etc.]
- Infrastructure: [Cloud provider]
- Current Process: [describe current deployment]

Requirements:
- [List specific requirements]
- [Security needs]
- [Performance expectations]
- [Compliance requirements]
- [Team workflow preferences]

Please provide:
1. Complete CI/CD pipeline configuration
2. Build and test stages
3. Security scanning integration
4. Deployment strategies
5. Rollback procedures
6. Monitoring and alerting
7. Environment-specific configurations
8. Team access controls
9. Documentation and runbooks
10. Cost optimization recommendations

Include best practices for [specific tools] and consider security, performance, and maintainability.
```

## Expected Output
- Complete pipeline configuration files
- Build and deployment scripts
- Security scanning setup
- Environment configurations
- Monitoring and alerting setup
- Documentation and procedures

## Tips & Tricks
- Start with a simple pipeline and iterate
- Include comprehensive testing stages
- Implement security scanning early
- Plan for parallel deployments
- Consider infrastructure costs
- Document everything thoroughly

## Related Prompts
- [Docker Configuration](./docker-configuration.md)
- [Kubernetes Deployment](./kubernetes-deployment.md)
- [Blue-Green Deployment](./blue-green-deployment.md)
