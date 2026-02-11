from datetime import datetime
from typing import List
from sqlmodel import select
from sqlalchemy import func
from ..db.engine import async_session
from ..models.schema import PortfolioSnapshot, SnapshotPosition
from ..services.normalizer import normalize_holdings


async def create_snapshot(normalized_positions: List[dict]):
    """Create a portfolio snapshot transactionally."""
    async with async_session() as session:
        async with session.begin():
            total_value = 0.0
            total_invested = 0.0
            for p in normalized_positions:
                qty = p.get("quantity", 0.0)
                price = p.get("current_price", p.get("average_price", 0.0))
                value = qty * price
                total_value += value
                total_invested += qty * p.get("average_price", 0.0)

            total_pnl = total_value - total_invested

            snapshot = PortfolioSnapshot(
                timestamp=datetime.utcnow(),
                total_value=total_value,
                total_invested=total_invested,
                total_pnl=total_pnl,
            )
            session.add(snapshot)
            await session.flush()

            for p in normalized_positions:
                qty = p.get("quantity", 0.0)
                price = p.get("current_price", p.get("average_price", 0.0))
                value = qty * price
                pos = SnapshotPosition(
                    snapshot_id=snapshot.id,
                    symbol=p.get("symbol"),
                    quantity=qty,
                    price=price,
                    value=value,
                )
                session.add(pos)

            await session.commit()
            return snapshot.id
