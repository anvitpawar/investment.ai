# SECURITY (summary)

Security baseline for the project (MVP)

Secrets & credentials
- Never commit secrets. Use AWS Secrets Manager for broker API keys and other credentials.
- Provide `.env.example` for dev, keep real values in Secrets Manager or CI secrets.

Access control
- Read-only broker API keys only. No trading/execution permissions.
- Role-based access for admin CLI/console if implemented.

Data protection
- TLS for all endpoints
- AES-256 encryption at rest for RDS

Logging & audit
- Audit logs for all actions that change data and for LLM calls (store prompts/response IDs, not raw secrets).

Deployment
- Use private DB subnets, restrict inbound IPs, use IAM roles for EC2/ECS.

Incident response
- Documented runbook in `docs/runbook.md` (create when ready).
