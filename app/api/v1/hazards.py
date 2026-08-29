"""
================================================================================
 FILE: app/api/v1/hazards.py
 VERSION: 1.1.0
 DATE: 2026-08-29
 PURPOSE: Supabase-backed REST API for Hazard Register Intake & Querying (VSR/MOR).
================================================================================
"""

from fastapi import APIRouter, Header, HTTPException
from typing import Optional, List, Dict, Any
from pydantic import BaseModel
from app.core.database import supabase
import logging

router = APIRouter(tags=["Hazards"])
logger = logging.getLogger(__name__)

class HazardCreatePayload(BaseModel):
    id: Optional[str] = None
    source_type: str = "VSR"  # VSR or MOR
    area: str
    location: str
    title: str
    description: str
    priority: str = "High"
    hfacs_code: Optional[str] = "PC208"
    tenant_id: Optional[str] = "tenant-001"

@router.get("/hazards")
async def get_hazards(
    x_tenant_id: Optional[str] = Header(None, alias="X-Tenant-Id"),
    source_type: Optional[str] = None
):
    if not supabase:
        raise HTTPException(status_code=503, detail="Database client not configured")
    
    query = supabase.table("hazard_register").select("*").order("created_at", desc=True)
    
    if x_tenant_id and x_tenant_id != "all":
        query = query.eq("tenant_id", x_tenant_id)
        
    if source_type and source_type != "ALL":
        query = query.eq("source_type", source_type)
        
    response = query.execute()
    return {"status": "success", "count": len(response.data), "data": response.data}

@router.post("/hazards")
async def create_hazard(
    payload: HazardCreatePayload,
    x_tenant_id: Optional[str] = Header("tenant-001", alias="X-Tenant-Id")
):
    if not supabase:
        raise HTTPException(status_code=503, detail="Database client not configured")
    
    tenant = payload.tenant_id or x_tenant_id or "tenant-001"
    
    # Generate ID if omitted
    hazard_id = payload.id
    if not hazard_id:
        prefix = "FLT" if "Flight" in payload.area else ("MNT" if "Maint" in payload.area else "ENV")
        import random
        hazard_id = f"{prefix}/{random.randint(100, 999)}/{payload.priority[0]}/2026"

    insert_data = {
        "id": hazard_id,
        "tenant_id": tenant,
        "source_type": payload.source_type,
        "area": payload.area,
        "location": payload.location,
        "title": payload.title,
        "description": payload.description,
        "priority": payload.priority,
        "hfacs_code": payload.hfacs_code
    }

    try:
        res = supabase.table("hazard_register").insert(insert_data).execute()
        return {"status": "success", "hazard": res.data[0]}
    except Exception as e:
        logger.error(f"Failed to insert hazard to Supabase: {e}")
        raise HTTPException(status_code=500, detail=str(e))
