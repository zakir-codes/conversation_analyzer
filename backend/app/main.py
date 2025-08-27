from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from typing import Optional
import logging
import asyncio

# Database (Beanie + Motor)
from beanie import init_beanie
from motor.motor_asyncio import AsyncIOMotorClient


from .core.config import settings


def create_app() -> FastAPI:
    app = FastAPI(title=settings.app_name)

    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    @app.on_event("startup")
    async def startup_event() -> None:
        try:
            client = AsyncIOMotorClient(settings.mongodb_uri)
            await init_beanie(database=client.get_default_database(), document_models=[])
            logging.getLogger(__name__).info("Connected to MongoDB")
        except Exception as exc:  # noqa: BLE001
            logging.getLogger(__name__).error(f"MongoDB connection failed: {exc}")

    # Health directly on root app
    @app.get("/health", tags=["system"])
    async def health() -> dict:
        return {"status": "ok"}

    # API Router mount (future expansion)
    from .api.v1.routes import api_router as api_v1_router  # type: ignore

    app.include_router(api_v1_router, prefix="/api/v1")

    @app.get("/")
    async def root() -> dict:
        return {"message": "Sales Analyzer Backend running"}

    return app


app = create_app()


