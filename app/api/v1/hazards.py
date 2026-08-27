"""
================================================================================
FILE: app/api/v1/hazards.py
VERSION: 0.2.0
PURPOSE: Hazard management endpoints with Firestore integration
================================================================================
"""

from fastapi import APIRouter, Depends, HTTPException, Query
from typing import List, Optional
from datetime import datetime
import uuid
import logging

from ...repositories.firestore import FirestoreRepository
from ..deps import get_tenant_id, get_user_role
from ...schemas.hazard import HazardCreate, HazardUpdate, HazardResponse

logger = logging.getLogger(__name__)
router = APIRouter(prefix="/hazards", tags=["hazards"])

def calculate_risk_level(severity: str, probability: str) -> str:
    severity_weights = {"Low": 1, "Medium": 2, "High": 3, "Critical": 4}
    prob_weights = {"Rare": 1, "Unlikely": 2, "Possible": 3, "Likely": 4, "Almost Certain": 5}
    risk_score = severity_weights.get(severity, 0) * prob_weights.get(probability, 0)
    if risk_score <= 4:
        return "Low"
    elif risk_score <= 8:
        return "Medium"
    elif risk_score <= 12:
        return "High"
    else:
        return "Critical"

@router.get("/", response_model=List[HazardResponse])
async def list_hazards(
    tenant_id: str = Depends(get_tenant_id),
    category: Optional[str] = None,
    severity: Optional[str] = None,
    status: Optional[str] = None,
    limit: int = Query(100, le=500)
):
    repo = FirestoreRepository("hazards")
    filters = {"tenant_id": tenant_id}
    if category:
        filters["category"] = category
    if severity:
        filters["severity"] = severity
    if status:
        filters["status"] = status
    hazards = await repo.list(filters, limit, order_by="created_at", order_direction="descending")
    logger.info(f"Retrieved {len(hazards)} hazards for tenant {tenant_id}")
    return hazards

@router.get("/{hazard_id}", response_model=HazardResponse)
async def get_hazard(
    hazard_id: str,
    tenant_id: str = Depends(get_tenant_id)
):
    repo = FirestoreRepository("hazards")
    hazard = await repo.get(hazard_id)
    if not hazard:
        raise HTTPException(status_code=404, detail="Hazard not found")
    if hazard.get("tenant_id") != tenant_id:
        raise HTTPException(status_code=403, detail="Access denied")
    return hazard

@router.post("/", response_model=HazardResponse)
async def create_hazard(
    hazard_data: HazardCreate,
    tenant_id: str = Depends(get_tenant_id),
    role: str = Depends(get_user_role)
):
    if role not in ["admin", "analyst"]:
        raise HTTPException(status_code=403, detail="Insufficient permissions")
    repo = FirestoreRepository("hazards")
    risk_level = calculate_risk_level(hazard_data.severity, hazard_data.probability)
    hazard_dict = hazard_data.dict()
    hazard_dict.update({
        "id": str(uuid.uuid4()),
        "tenant_id": tenant_id,
        "risk_level": risk_level,
        "status": "Open",
        "created_at": datetime.utcnow().isoformat(),
        "updated_at": datetime.utcnow().isoformat()
    })
    doc_id = await repo.create(hazard_dict, hazard_dict["id"])
    logger.info(f"Created hazard {doc_id} for tenant {tenant_id}")
    return hazard_dict

@router.put("/{hazard_id}", response_model=HazardResponse)
async def update_hazard(
    hazard_id: str,
    hazard_data: HazardUpdate,
    tenant_id: str = Depends(get_tenant_id),
    role: str = Depends(get_user_role)
):
    if role not in ["admin", "analyst"]:
        raise HTTPException(status_code=403, detail="Insufficient permissions")
    repo = FirestoreRepository("hazards")
    existing = await repo.get(hazard_id)
    if not existing:
        raise HTTPException(status_code=404, detail="Hazard not found")
    if existing.get("tenant_id") != tenant_id:
        raise HTTPException(status_code=403, detail="Access denied")
    update_data = hazard_data.dict(exclude_unset=True)
    if "severity" in update_data or "probability" in update_data:
        severity = update_data.get("severity", existing["severity"])
        probability = update_data.get("probability", existing["probability"])
        update_data["risk_level"] = calculate_risk_level(severity, probability)
    update_data["updated_at"] = datetime.utcnow().isoformat()
    success = await repo.update(hazard_id, update_data)
    if not success:
        raise HTTPException(status_code=500, detail="Failed to update hazard")
    logger.info(f"Updated hazard {hazard_id} for tenant {tenant_id}")
    updated = await repo.get(hazard_id)
    return updated

@router.delete("/{hazard_id}")
async def delete_hazard(
    hazard_id: str,
    tenant_id: str = Depends(get_tenant_id),
    role: str = Depends(get_user_role)
):
    if role != "admin":
        raise HTTPException(status_code=403, detail="Insufficient permissions")
    repo = FirestoreRepository("hazards")
    existing = await repo.get(hazard_id)
    if not existing:
        raise HTTPException(status_code=404, detail="Hazard not found")
    if existing.get("tenant_id") != tenant_id:
        raise HTTPException(status_code=403, detail="Access denied")
    success = await repo.delete(hazard_id)
    if not success:
        raise HTTPException(status_code=500, detail="Failed to delete hazard")
    logger.info(f"Deleted hazard {hazard_id} for tenant {tenant_id}")
    return {"success": True, "message": "Hazard deleted"}
