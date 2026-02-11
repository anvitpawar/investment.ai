from typing import Optional
from datetime import datetime
from sqlmodel import SQLModel, Field, Column, Integer, String, Float, DateTime, ForeignKey


class Holding(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    symbol: str = Field(index=True)
    instrument_type: Optional[str]
    quantity: float
    average_price: float
    last_price: Optional[float] = None
    market_value: Optional[float] = None
    broker_source: Optional[str]
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)


class PortfolioSnapshot(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    timestamp: datetime = Field(index=True)
    total_value: float
    total_invested: float
    total_pnl: float


class SnapshotPosition(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    snapshot_id: int = Field(foreign_key="portfoliosnapshot.id")
    symbol: str
    quantity: float
    price: float
    value: float
