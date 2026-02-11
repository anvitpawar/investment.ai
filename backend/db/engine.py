from sqlmodel import SQLModel
from sqlalchemy.ext.asyncio import create_async_engine, AsyncEngine, AsyncSession
from sqlalchemy.orm import sessionmaker
from ..config.settings import settings


DATABASE_URL = settings.DATABASE_URL


def get_engine() -> AsyncEngine:
    return create_async_engine(DATABASE_URL, echo=False, future=True)


engine = get_engine()

async_session = sessionmaker(
    engine, class_=AsyncSession, expire_on_commit=False
)


async def init_db() -> None:
    # Create tables (for MVP we allow create_all during startup)
    async with engine.begin() as conn:
        await conn.run_sync(SQLModel.metadata.create_all)
