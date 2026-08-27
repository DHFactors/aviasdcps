"""
================================================================================
FILE: app/repositories/firestore.py
VERSION: 0.1.0
PURPOSE: Firestore repository implementation for hazard management
================================================================================
"""

from typing import Dict, Any, Optional, List
from ..core.database import db
import logging

logger = logging.getLogger(__name__)

class FirestoreRepository:
    """Firestore CRUD operations for any collection"""
    
    def __init__(self, collection_name: str):
        self.collection = collection_name
    
    async def create(self, data: Dict[str, Any], doc_id: Optional[str] = None) -> str:
        return await db.create_document(self.collection, data, doc_id)
    
    async def get(self, doc_id: str) -> Optional[Dict[str, Any]]:
        return await db.get_document(self.collection, doc_id)
    
    async def update(self, doc_id: str, data: Dict[str, Any]) -> bool:
        return await db.update_document(self.collection, doc_id, data)
    
    async def delete(self, doc_id: str) -> bool:
        return await db.delete_document(self.collection, doc_id)
    
    async def list(
        self, 
        filters: Optional[Dict[str, Any]] = None, 
        limit: int = 100,
        order_by: Optional[str] = "created_at",
        order_direction: str = "descending"
    ) -> List[Dict[str, Any]]:
        return await db.list_documents(
            self.collection, 
            filters, 
            limit,
            order_by,
            order_direction
        )
