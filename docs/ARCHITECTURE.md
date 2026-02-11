# ARCHITECTURE (summary)

High-level architecture
- Backend: Python + FastAPI (stateless services)
- Database: PostgreSQL (RDS)
- Dashboard: Streamlit (UI pages under `dashboard/`)
- Scheduler: APScheduler / cron jobs for 3 daily snapshots
- Alerts: Telegram bot for notifications
- AI: LLM API (OpenAI-class) for explanations and conversational assistant; deterministic metrics produced in code
- Infra: AWS (VPC, RDS, EC2 or ECS), secrets in AWS Secrets Manager

Data flow (simplified)
1. Scheduler triggers fetch from Zerodha Kite + Coin connectors
2. Ingested holdings/transactions are validated and stored in Postgres
3. Snapshot job computes metrics and stores them in `snapshots` table
4. Dashboard reads from API endpoints powered by FastAPI
5. Alert engine evaluates rules and posts to Telegram
6. AI engine builds a context bundle (latest metrics + history) and calls LLM for narrative outputs

Design constraints
- Read-only broker access
- Deterministic computations in backend (no numeric calc inside LLM)
- Encrypted secrets and audit logs

Key files to inspect when implementing features
- `PROJECT_CONTEXT/PROJECT_CONTEXT.md`
- `PROJECT_CONTEXT/PRD and MVP Doc.md`
- `backend/` (expected)
- `dashboard/` (expected)
