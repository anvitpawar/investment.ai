Investment Monitor AI Agent — System Context

This project builds a secure AI-powered investment monitoring platform integrating Zerodha Kite and Coin APIs.

Architecture:
	•	Python FastAPI backend
	•	PostgreSQL database
	•	Streamlit analytics dashboard
	•	AWS hosted infrastructure
	•	Telegram alert system
	•	LLM powered insights engine

Core capabilities:
	•	Portfolio data ingestion (3 daily refresh cycles)
	•	Deterministic analytics computation
	•	AI interpretation layer (LLM reasoning only)
	•	Conversational portfolio assistant
	•	Risk monitoring and alerting

Key design principles:
	•	Read-only broker integration
	•	Human-in-the-loop decision making
	•	Deterministic financial calculations
	•	Secure credential storage
	•	Audit logging
	•	SOC2 aligned architecture

AI system role:
The AI model does not compute financial metrics.
It receives structured analytics outputs and provides explanation, risk commentary, and recommendation narratives.

Deployment:
AWS infrastructure with encrypted data at rest and in transit.

Alert schedule:
Opening snapshot
Midday snapshot
End-of-day snapshot

Primary objective:
Provide professional grade portfolio intelligence and monitoring with strong security and compliance posture.