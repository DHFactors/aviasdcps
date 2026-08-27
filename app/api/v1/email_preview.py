from fastapi import APIRouter
router = APIRouter(prefix="/email-preview", tags=["email-preview"])

@router.get("/recent")
async def get_recent_emails():
    return {"message": "Email preview endpoint"}
