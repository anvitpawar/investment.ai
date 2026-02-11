## Quick start for AI coding agents (investment.ai)

Purpose
- Help AI agents (Copilot, Copilot Chat, ChatGPT tooling) be immediately productive in this repo by describing the high-level architecture, key files to read, project conventions, and actionable tasks.

Read these first (in order)
- `PROJECT_CONTEXT/PROJECT_CONTEXT.md` — canonical system context, architecture, and security requirements.
- `PROJECT_CONTEXT/PRD and MVP Doc.md` — prioritized MVP features, acceptance criteria, and release roadmap.
- `README.md` — repository-level summary.

Big picture (what this repo is about)
- FastAPI backend + PostgreSQL (RDS) + Streamlit dashboard.
- AWS-hosted infra, secrets in Secrets Manager, scheduler for 3 daily snapshots (open/midday/close).
- Zerodha Kite + Coin connectors for holdings, transactions, pricing.
- Telegram alerts + LLM-powered insights (LLM must only explain deterministic metrics; calculations live in code).

PRD highlights (use these as authoritative implementation cues)
- Core MVP modules: Data Ingestion Service, Portfolio Database, Analytics Engine, AI Insights Engine, Alert Service, API Layer, Streamlit Dashboard.
- Key tables to model: `holdings`, `transactions`, `prices`/`navs`, `snapshots`, `metrics`.
- Analytics must compute deterministic metrics in backend: valuation, allocation %, absolute returns, XIRR/CAGR (later), top gainers/losers — LLM only summarizes these outputs.
- Alert rules (MVP): large price movement, allocation drift, position-size thresholds; Telegram deliverables must be testable.
- Sprint acceptance criteria to reference: accurate portfolio value vs Kite, snapshots stored 3× daily, alerts delivered, AI explains portfolio performance (narratives from computed metrics).
- Security constraints: read-only broker access, TLS + encryption at rest, secrets in AWS Secrets Manager, audit logging for LLM calls and critical actions.

Key files & locations to reference
- `PROJECT_CONTEXT/*` — authoritative product/architecture definitions. Always map feature work back to a PRD section.
- `backend/` — (expected) FastAPI application, services, models, scheduler. Look here first when editing API or analytics logic.
- `dashboard/` — (expected) Streamlit app and pages.
- `infra/terraform/` — (expected) infrastructure-as-code artifacts (if present).

> If a file or folder above is missing, consult `PROJECT_CONTEXT/*` and create the scaffold using the stack (FastAPI + Streamlit + PostgreSQL) described in the PRD.

Sprint & scope guidance (1-month MVP)
- The project uses an aggressive 4×7-day sprint plan. Keep PRs small and tied to a single sprint deliverable.
- Tie each branch/PR to a PRD reference: e.g. `mvp/sprint1-zerodha-sync` with PR body containing `PRD: 3.1 Portfolio Data Integration`.

Project-specific conventions
- Docs-first: `PROJECT_CONTEXT/*` is authoritative. If code conflicts with docs, update docs and call out the discrepancy in PR.
- Security-first: never add secrets to code. Use `aws-secrets-manager`/env and include `.env.example` when adding envs.
- Deterministic metrics: do all numeric/financial computations in code (backend/analytics). The LLM only consumes those outputs to generate explanations.

Developer workflows (what to run)
- No language manifests detected yet in repo. When adding a stack, include clear commands in `README.md`. Use these project templates:
  - Python (FastAPI): `python -m venv .venv && .venv/bin/pip install -r requirements.txt && uvicorn backend.main:app --reload`
  - Streamlit: `streamlit run dashboard/streamlit_app.py`
  - Tests: `pytest`

VS Code extensions (install these in the workspace)
- Python (Microsoft), Pylance, Python Debugger
- GitHub Copilot, GitHub Copilot Chat
- AWS Toolkit, Docker
- PostgreSQL / SQLTools, REST Client or Thunder Client
- GitLens, Error Lens

How to feed context to Copilot and AI agents
- Add these files to the repo root (or `docs/`) so Copilot reads them automatically:
  - `docs/PRD.md` (copy of `PROJECT_CONTEXT/PRD and MVP Doc.md`)
  - `docs/ARCHITECTURE.md` (detailed architecture diagrams/notes)
  - `docs/SECURITY.md` (security controls, secrets handling, IAM guidance)
  - `PROJECT_CONTEXT.md` (short index/summary for quick reference)
- Keep these docs small, explicit, and up-to-date; Copilot builds prompts from the entire workspace.

Prompting examples for Copilot Chat (short)
- "Create FastAPI endpoint `GET /portfolio` that returns latest snapshot and computed allocation percentages. Use `backend/services/valuation.py` to compute metrics. Add unit test.`"
- "Scaffold Streamlit page `pages/portfolio_summary.py` showing allocation donut and P&L table sourced from `/api/snapshots/latest`"

PR guidance & acceptance
- Every PR must include: mapping to PRD, brief run instructions, tests or manual test steps, and any infra changes.
- Keep PRs under 500 lines when possible. Prefer multiple small PRs over one large change.

If you need to scaffold
- Ask for the preferred language/runtime. If approved, create the minimal structure shown in `PROJECT_CONTEXT` (backend/, dashboard/, infra/, docs/) and include `requirements.txt`, `README.md` updates, and a basic GitHub Actions CI workflow.

Where to escalate questions
- If product scope ambiguity: reference `PROJECT_CONTEXT/PRD and MVP Doc.md` and open an issue titled `clarify: <section>`.
- If infra or security uncertainty: open an issue tagged `security` and link to `PROJECT_CONTEXT/PROJECT_CONTEXT.md`.

Feedback cycle
- After edits, update `docs/ARCHITECTURE.md` with any structural changes. Keep the PRD mapping in the PR body. Ask reviewers to confirm invariants (read-only broker access, no plaintext secrets, deterministic metrics outside LLM).

--
This guidance was generated from the project's `PROJECT_CONTEXT/*` documents and the 1-month MVP plan supplied by the product owner. If you want a different tone or more detail (e.g., exact file templates, CI workflows, or prompt library), say which sprint or component to prioritize and I will expand.
