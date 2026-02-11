import asyncio
from fastapi import FastAPI
from .api.routes import router
from .db.engine import init_db
from .scheduler.jobs import start as start_scheduler


app = FastAPI(title="investment-ai-backend")
app.include_router(router)


@app.on_event("startup")
async def on_startup():
    await init_db()
    # Start scheduler in background
    loop = asyncio.get_event_loop()
    loop.call_soon(start_scheduler)


@app.on_event("shutdown")
async def on_shutdown():
    pass
