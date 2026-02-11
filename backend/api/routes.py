from fastapi import APIRouter, Depends, BackgroundTasks
from ..db.engine import init_db
from ..scheduler.jobs import start as start_scheduler, run_snapshot_job
from sqlmodel import select
from ..db.engine import async_session
from ..models.schema import PortfolioSnapshot, SnapshotPosition

router = APIRouter()


@router.get("/health")
async def health():
    return {"status": "ok"}


@router.post("/sync/manual")
async def manual_sync(background_tasks: BackgroundTasks):
    # Run snapshot in background
    background_tasks.add_task(run_snapshot_job)
    return {"status": "sync_started"}


@router.get("/snapshots/latest")
async def get_latest_snapshot():
    async with async_session() as session:
        result = await session.exec(select(PortfolioSnapshot).order_by(PortfolioSnapshot.timestamp.desc()).limit(1))
        snap = result.first()
        if not snap:
            return {"snapshot": None}
        pos_res = await session.exec(select(SnapshotPosition).where(SnapshotPosition.snapshot_id == snap.id))
        positions = pos_res.all()
        return {"snapshot": snap, "positions": positions}
