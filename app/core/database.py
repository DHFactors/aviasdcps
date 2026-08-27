"""
================================================================================
FILE: app/core/database.py
VERSION: 0.2.0
PURPOSE: Firestore database connection and CRUD operations with ordering
================================================================================
"""

import os
import logging
from typing import Optional, Dict, Any, List
from google.cloud import firestore
from google.cloud.firestore_v1 import Client

logger = logging.getLogger(__name__)

class FirestoreDB:
    _instance: Optional[Client] = None
    
    @classmethod
    def get_client(cls) -> Client:
        if cls._instance is None:
            try:
                emulator_host = os.getenv("FIRESTORE_EMULATOR_HOST")
                if emulator_host:
                    logger.info(f"🔥 Using Firestore Emulator at {emulator_host}")
                    cls._instance = firestore.Client(
                        project=os.getenv("FIRESTORE_PROJECT_ID", "avia-sdcps-demo")
                    )
                else:
                    logger.info("🌐 Using production Firestore")
                    cls._instance = firestore.Client(
                        project=os.getenv("FIRESTORE_PROJECT_ID")
                    )
                logger.info("✅ Firestore client initialized successfully")
            except Exception as e:
                logger.error(f"❌ Failed to initialize Firestore: {e}")
                raise
        return cls._instance
    
    @classmethod
    def get_collection(cls, collection_name: str):
        return cls.get_client().collection(collection_name)
    
    @classmethod
    async def create_document(cls, collection: str, data: Dict[str, Any], doc_id: Optional[str] = None) -> str:
        try:
            doc_ref = cls.get_collection(collection).document(doc_id) if doc_id else cls.get_collection(collection).document()
            doc_ref.set(data)
            logger.info(f"✅ Document created in '{collection}' with ID: {doc_ref.id}")
            return doc_ref.id
        except Exception as e:
            logger.error(f"❌ Error creating document: {e}")
            raise
    
    @classmethod
    async def get_document(cls, collection: str, doc_id: str) -> Optional[Dict[str, Any]]:
        try:
            doc_ref = cls.get_collection(collection).document(doc_id)
            doc = doc_ref.get()
            if doc.exists:
                data = doc.to_dict()
                data['id'] = doc.id
                return data
            return None
        except Exception as e:
            logger.error(f"❌ Error getting document: {e}")
            return None
    
    @classmethod
    async def update_document(cls, collection: str, doc_id: str, data: Dict[str, Any]) -> bool:
        try:
            doc_ref = cls.get_collection(collection).document(doc_id)
            doc_ref.update(data)
            logger.info(f"✅ Document updated in '{collection}' with ID: {doc_id}")
            return True
        except Exception as e:
            logger.error(f"❌ Error updating document: {e}")
            return False
    
    @classmethod
    async def delete_document(cls, collection: str, doc_id: str) -> bool:
        try:
            doc_ref = cls.get_collection(collection).document(doc_id)
            doc_ref.delete()
            logger.info(f"✅ Document deleted from '{collection}' with ID: {doc_id}")
            return True
        except Exception as e:
            logger.error(f"❌ Error deleting document: {e}")
            return False
    
    @classmethod
    async def list_documents(
        cls, 
        collection: str, 
        filters: Optional[Dict[str, Any]] = None,
        limit: int = 100,
        order_by: Optional[str] = None,
        order_direction: str = "descending"
    ) -> List[Dict[str, Any]]:
        try:
            query = cls.get_collection(collection)
            if filters:
                for key, value in filters.items():
                    query = query.where(key, "==", value)
            if order_by:
                direction = firestore.Query.ASCENDING if order_direction == "ascending" else firestore.Query.DESCENDING
                query = query.order_by(order_by, direction=direction)
            if limit:
                query = query.limit(limit)
            docs = query.stream()
            results = [{**doc.to_dict(), 'id': doc.id} for doc in docs]
            logger.info(f"✅ Retrieved {len(results)} documents from '{collection}'")
            return results
        except Exception as e:
            logger.error(f"❌ Error listing documents: {e}")
            return []

db = FirestoreDB
