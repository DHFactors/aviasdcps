from fastapi import APIRouter
router = APIRouter(prefix="/demo", tags=["demo"])

@router.get("/status")
async def get_status():
    return {"demo_mode": True, "message": "Demo is running"}
