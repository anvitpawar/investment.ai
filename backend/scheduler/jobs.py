from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.triggers.cron import CronTrigger
from zoneinfo import ZoneInfo
from datetime import datetime
from ..integrations.zerodha.mock_client import MockZerodhaClient
from ..services.normalizer import normalize_holdings
from ..services.snapshot import create_snapshot


scheduler = AsyncIOScheduler(timezone=ZoneInfo("Asia/Kolkata"))


async def run_snapshot_job():
    client = MockZerodhaClient()
    raw = await client.fetch_holdings()
    mf = await client.fetch_mf_holdings()
    raw.extend(mf)
    prices = await client.fetch_ltp([r["symbol"] for r in raw])
    normalized = normalize_holdings(raw)
    for p in normalized:
        p["current_price"] = prices.get(p["symbol"], 0.0)

    snapshot_id = await create_snapshot(normalized)
    print(f"Snapshot created: {snapshot_id} at {datetime.utcnow().isoformat()}")


def register_jobs():
    # 09:15 IST
    scheduler.add_job(run_snapshot_job, CronTrigger(hour=9, minute=15))
    # 12:30 IST
    scheduler.add_job(run_snapshot_job, CronTrigger(hour=12, minute=30))
    # 15:30 IST
    scheduler.add_job(run_snapshot_job, CronTrigger(hour=15, minute=30))


def start():
    register_jobs()
    scheduler.start()
