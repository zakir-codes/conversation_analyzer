from fastapi import APIRouter

api_router = APIRouter()


@api_router.get("/health", tags=["system"])  # duplicate health under /api/v1
async def api_health() -> dict:
    return {"status": "ok"}


