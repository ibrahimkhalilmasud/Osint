import logging

from fastapi import FastAPI

from .config import settings
from .routers.auth import router as auth_router
from .routers.investigations import router as investigations_router


logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(name)s %(message)s")

app = FastAPI(title=settings.app_name)
app.include_router(auth_router)
app.include_router(investigations_router)


@app.get("/health")
def health() -> dict:
    return {"status": "ok", "service": settings.app_name, "environment": settings.environment}
