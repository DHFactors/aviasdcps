"""
================================================================================
FILE: app/schemas/hazard.py
VERSION: 0.1.0
PURPOSE: Pydantic schemas for hazard data validation
================================================================================
"""

from pydantic import BaseModel
from typing import Optional

class HazardBase(BaseModel):
    title: str
    description: str
    category: str
    severity: str
    probability: str
    mitigation_plan: Optional[str] = None
    owner: Optional[str] = None
    location: Optional[str] = None

class HazardCreate(HazardBase):
    pass

class HazardUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    category: Optional[str] = None
    severity: Optional[str] = None
    probability: Optional[str] = None
    status: Optional[str] = None
    mitigation_plan: Optional[str] = None
    owner: Optional[str] = None
    location: Optional[str] = None

class HazardResponse(HazardBase):
    id: str
    tenant_id: str
    risk_level: str
    status: str
    created_at: str
    updated_at: str
