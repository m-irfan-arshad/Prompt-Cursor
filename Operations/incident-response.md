# Incident Response Prompt

## Purpose
Handle operational incidents systematically and efficiently by following established incident response procedures, coordinating with teams, and ensuring proper communication and resolution.

## When to Use
- Responding to system outages or failures
- Handling security incidents
- Managing performance degradation
- Coordinating emergency responses
- Documenting incident procedures
- Conducting post-incident reviews

## Input Requirements
- Incident details and symptoms
- System affected and impact scope
- Current status and timeline
- Team availability and roles
- Communication channels
- Escalation procedures

## Example Usage

```prompt
I need to handle an incident response for [incident type] with the following details:

Incident Information:
- Type: [outage/security/performance/degradation]
- Severity: [critical/high/medium/low]
- Systems Affected: [list affected systems]
- User Impact: [number of users, business impact]
- Detection Time: [when incident was detected]
- Current Status: [ongoing/resolved/escalated]

Initial Assessment:
- Symptoms: [what's happening]
- Error Messages: [any error logs or messages]
- Recent Changes: [recent deployments or changes]
- Monitoring Alerts: [alerts that triggered]

Team Context:
- On-Call Engineer: [who is responding]
- Available Resources: [team members, tools]
- Escalation Contacts: [who to contact if needed]
- Communication Channels: [Slack, email, phone]

Please provide:
1. Immediate Response Actions
   - First steps to assess and contain the incident
   - Communication plan for stakeholders
   - Escalation criteria and procedures
   - Resource allocation and team coordination

2. Investigation and Diagnosis
   - Systematic approach to identify root cause
   - Tools and commands to gather information
   - Log analysis and monitoring data review
   - Hypothesis testing and validation

3. Resolution Strategy
   - Immediate fixes and workarounds
   - Long-term solution planning
   - Rollback procedures if needed
   - Verification steps to confirm resolution

4. Communication Plan
   - Stakeholder notification templates
   - Status update frequency and format
   - Customer communication strategy
   - Internal team coordination

5. Post-Incident Actions
   - Documentation requirements
   - Lessons learned process
   - Improvement recommendations
   - Follow-up tasks and timeline

6. Prevention Measures
   - Monitoring improvements
   - Process enhancements
   - Training and knowledge sharing
   - Infrastructure improvements

Follow incident response best practices and maintain clear communication throughout the process.
```

## Expected Output
- Structured incident response plan
- Communication templates and procedures
- Investigation and resolution steps
- Post-incident review framework
- Prevention and improvement recommendations

## Tips & Tricks
- Stay calm and systematic during incidents
- Communicate early and often
- Document everything for post-incident review
- Follow established runbooks when available
- Prioritize user impact and business continuity

## Related Prompts
- [Troubleshooting](./troubleshooting.md)
- [Team Coordination](./team-coordination.md)
- [Operational Documentation](./operational-documentation.md)
