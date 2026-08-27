from fastapi import APIRouter
router = APIRouter(prefix="/lead-capture", tags=["lead-capture"])

@router.post("/")
async def capture_lead():
    return {"message": "Lead capture endpoint"}
