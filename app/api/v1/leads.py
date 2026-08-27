from fastapi import APIRouter
router = APIRouter(prefix="/leads", tags=["leads"])

@router.post("/register")
async def register_lead():
    return {"message": "Lead registration endpoint"}
