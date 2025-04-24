from fastapi import APIRouter, HTTPException
from app.models.oracle import HealthResponse, EnlightenResponse
from app.services.enlighten import LLM as model

router = APIRouter()

@router.get(
    "/enlighten",
    response_model=EnlightenResponse,
    name="oracle:enlighten"
)
async def enlighten() -> EnlightenResponse:
    resp = model.query()
    return EnlightenResponse(response=resp)

@router.get(
    "/health",
    response_model=HealthResponse,
    name="oracle:get-status",
)
async def health():
    return HealthResponse(status="healthy")