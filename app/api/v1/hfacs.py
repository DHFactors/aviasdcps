"""
================================================================================
FILE: app/api/v1/hfacs.py
VERSION: 0.1.0
PURPOSE: HFACS Nanocode reference API
================================================================================
"""

from fastapi import APIRouter, Query
from typing import Optional
from app.data.hfacs_codes import HFACS_CODES, search_hfacs, get_hfacs_by_category, get_hfacs_counts

router = APIRouter(prefix="/hfacs", tags=["hfacs"])

@router.get("/codes")
async def get_hfacs_codes(
    category: Optional[str] = Query(None, description="Filter by category: ACT, PRECOND, SUPER, ORG"),
    search: Optional[str] = Query(None, description="Search by code or description"),
    limit: int = Query(50, description="Max results")
):
    """Get HFACS codes with optional filtering."""
    result = HFACS_CODES
    
    if category:
        result = get_hfacs_by_category(category)
    
    if search:
        # intersect if both filters
        search_result = search_hfacs(search)
        if category:
            result = [c for c in result if c in search_result]
        else:
            result = search_result
    
    # Limit results
    if len(result) > limit:
        result = result[:limit]
    
    return {
        "total": len(HFACS_CODES),
        "filtered": len(result),
        "counts": get_hfacs_counts(),
        "codes": result
    }

@router.get("/categories")
async def get_hfacs_categories():
    """Get HFACS categories with counts."""
    counts = get_hfacs_counts()
    return {
        "categories": [
            {"name": "ACT", "label": "Acts", "count": counts.get("ACT", 0)},
            {"name": "PRECOND", "label": "Preconditions", "count": counts.get("PRECOND", 0)},
            {"name": "SUPER", "label": "Supervision", "count": counts.get("SUPER", 0)},
            {"name": "ORG", "label": "Organizational", "count": counts.get("ORG", 0)}
        ],
        "total": len(HFACS_CODES)
    }

@router.get("/suggest")
async def suggest_hfacs(
    text: str = Query(..., description="Text to match against HFACS descriptions"),
    limit: int = Query(5, description="Number of suggestions")
):
    """Suggest HFACS codes based on text input (for NLP integration)."""
    suggestions = search_hfacs(text)
    
    # Sort by relevance (simple scoring)
    sorted_suggestions = sorted(
        suggestions,
        key=lambda x: (
            text.lower() in x["description"].lower(),
            text.lower() in x["code"].lower()
        ),
        reverse=True
    )
    
    return {
        "query": text,
        "suggestions": sorted_suggestions[:limit]
    }
