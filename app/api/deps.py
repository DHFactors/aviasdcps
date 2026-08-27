from fastapi import Header, HTTPException
from typing import Optional
import os
import logging

logger = logging.getLogger(__name__)

DEMO_API_KEYS = {
    "demo-key-001": {"tenant": "tenant-001", "role": "admin"},
    "demo-key-002": {"tenant": "tenant-002", "role": "viewer"},
    "demo-key-003": {"tenant": "tenant-003", "role": "analyst"},
}

async def get_tenant_id(
    x_tenant_id: Optional[str] = Header(None),
    x_api_key: Optional[str] = Header(None)
) -> str:
    if os.getenv("DEMO_MODE", "true").lower() == "true":
        if x_tenant_id in ["tenant-001", "tenant-002", "tenant-003"]:
            return x_tenant_id
        if not x_tenant_id:
            return "tenant-001"
    
    if x_api_key and x_api_key in DEMO_API_KEYS:
        return DEMO_API_KEYS[x_api_key]["tenant"]
    
    raise HTTPException(
        status_code=401,
        detail="Invalid tenant ID or API key"
    )

async def get_user_role(
    x_api_key: Optional[str] = Header(None)
) -> str:
    if x_api_key and x_api_key in DEMO_API_KEYS:
        return DEMO_API_KEYS[x_api_key]["role"]
    return "viewer"
