Act as a Senior Infrastructure Architect with 10+ years of AWS experience. Design a complete Terraform module for a multi-tenant SaaS application with the following requirements:

ARCHITECTURE REQUIREMENTS:
- 3-tier web application (web, api, database)
- Auto-scaling between 2-20 instances based on CPU/memory
- RDS PostgreSQL with read replicas
- Redis for session management
- Load balancer with SSL termination

SECURITY REQUIREMENTS:
- VPC with private subnets for database tier
- Security groups following least privilege
- WAF protection for web tier
- Secrets managed via AWS Secrets Manager

CLIENT SPECIFICATIONS:
- Environment: [staging/production]
- Expected traffic: [concurrent users]
- Compliance: [SOC2/HIPAA/PCI]
- Budget constraint: [monthly AWS spend]

OUTPUT FORMAT:
1. Complete Terraform modules with variables
2. Security checklist with compliance mappings
3. Deployment runbook with rollback procedures
4. Cost estimation with optimization recommendations

CONTEXT: This is for a regulated fintech client requiring enterprise-grade security and 99.9% uptime SLA.