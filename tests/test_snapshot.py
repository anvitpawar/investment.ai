import asyncio
import pytest
from httpx import AsyncClient

from backend.main import app
from backend.integrations.zerodha.mock_client import MockZerodhaClient
from backend.services.normalizer import normalize_holdings


@pytest.mark.asyncio
async def test_normalize_and_snapshot(tmp_path):
    client = MockZerodhaClient()
    raw = await client.fetch_holdings()
    mf = await client.fetch_mf_holdings()
    raw.extend(mf)
    normalized = normalize_holdings(raw)
    assert any(p["symbol"] == "RELIANCE" for p in normalized)


@pytest.mark.asyncio
async def test_health_endpoint():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        r = await ac.get("/health")
        assert r.status_code == 200
        assert r.json()["status"] == "ok"
