from fastapi import APIRouter
router = APIRouter(prefix="/state-risk", tags=["state-risk"])

@router.get("/metrics")
async def get_metrics():
    return {"message": "State risk metrics endpoint"}
