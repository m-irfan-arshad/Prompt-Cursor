# System Monitoring Prompt

## Purpose
Design comprehensive monitoring strategies and implement monitoring solutions to ensure system health, performance, and availability.

## When to Use
- Setting up new monitoring systems
- Improving existing monitoring
- Troubleshooting performance issues
- Planning for high availability
- Implementing SRE practices

## Input Requirements
- System architecture details
- Current monitoring setup
- Performance requirements
- Team size and expertise
- Budget constraints

## Example Usage

```prompt
I need to design a comprehensive monitoring strategy for a [system type] with the following characteristics:

System Details:
- Architecture: [microservices/monolith/distributed]
- Technology Stack: [list technologies]
- Scale: [number of users/servers]
- Criticality: [high/medium/low]
- Current Monitoring: [existing tools]

Requirements:
- [availability requirements]
- [performance requirements]
- [response time requirements]
- [budget constraints]
- [team expertise level]

Please provide:
1. Monitoring Architecture
   - Tool recommendations
   - Data collection strategy
   - Storage and retention policies
   - Visualization setup

2. Key Metrics to Monitor
   - Infrastructure metrics
   - Application metrics
   - Business metrics
   - Custom metrics

3. Alerting Strategy
   - Alert thresholds
   - Escalation procedures
   - On-call rotations
   - Alert fatigue prevention

4. Dashboard Design
   - Executive dashboards
   - Operational dashboards
   - Developer dashboards
   - Custom views

5. Incident Response
   - Runbook templates
   - Communication procedures
   - Post-incident analysis
   - Continuous improvement

6. Cost Optimization
   - Resource utilization
   - Data retention policies
   - Tool consolidation
   - ROI analysis
```

## Expected Output
- Complete monitoring architecture
- Tool recommendations and setup
- Alerting and escalation procedures
- Dashboard designs
- Incident response plans

## Tips & Tricks
- Start with critical metrics first
- Implement gradual rollouts
- Plan for data retention costs
- Consider team skill levels
- Document everything thoroughly

## Related Prompts
- [Log Analysis](./log-analysis.md)
- [Performance Tuning](./performance-tuning.md)
- [Incident Response](./incident-response.md)
