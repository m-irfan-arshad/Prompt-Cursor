Act as a Senior Site Reliability Engineer specializing in observability. Design a complete monitoring solution for a microservices architecture with the following specifications:

INFRASTRUCTURE:
- 12 microservices (Node.js, Python, Go)
- Kubernetes cluster (EKS)
- PostgreSQL, Redis, RabbitMQ
- Expected: 10M requests/day, 50ms p95 latency

MONITORING REQUIREMENTS:
- Application metrics (latency, throughput, errors)
- Infrastructure metrics (CPU, memory, disk, network)
- Business metrics (user actions, revenue impact)
- Custom alerts for SLA violations

DELIVERABLES:
1. Prometheus configuration with service discovery
2. Grafana dashboards (infrastructure, application, business)
3. AlertManager rules with escalation policies
4. Runbooks for common incidents
5. Integration with PagerDuty/Slack

CONSTRAINTS:
- Budget: <$500/month for monitoring tools
- Team size: 3 engineers (junior level)
- Must integrate with existing CI/CD pipeline

Generate production-ready configurations with explanatory comments