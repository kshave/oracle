from fastapi import APIRouter

from api.routes import predictor
from app.api.routes import oracle

router = APIRouter()
#router.include_router(predictor.router, tags=["predictor"], prefix="/v1")
router.include_router(oracle.router, tags=["oracle"], prefix="/v1")