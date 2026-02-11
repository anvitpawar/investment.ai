# PRD (short) — Investment Monitor AI Agent

This document is a concise, workspace-visible copy of the product requirements and MVP scope.

Vision
- Professional, secure AI-powered investment monitoring platform: automatic portfolio tracking, risk detection, actionable insights, dashboard and conversational assistant.

Primary users
- Individual power investors, long-term wealth builders, active SIP investors.

In-scope (MVP)
- Zerodha Kite broker integration
- Zerodha Coin mutual funds (if available)
- Daily portfolio snapshots (3× daily)
- Deterministic analytics: valuation, allocation, top gainers/losers
- Streamlit dashboard (portfolio summary, holdings, allocation, performance)
- Telegram alerts for threshold breaches
- LLM-powered AI explanations (consumes deterministic outputs; no calculation inside LLM)

Release roadmap (1-month MVP)
- Sprint 1: infra + data pipeline (AWS, FastAPI skeleton, DB, Zerodha sync, scheduler)
- Sprint 2: analytics + dashboard (valuation, allocation, Streamlit pages)
- Sprint 3: alerts + AI insights (alert rules, Telegram, LLM integration)
- Sprint 4: chat interface + security hardening + release (chat assistant, rate-limiting, logging)

Files of interest
- `PROJECT_CONTEXT/PRD and MVP Doc.md` (full PRD)
