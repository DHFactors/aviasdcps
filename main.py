"""
================================================================================
 FILE: main.py
 VERSION: 1.2.0
 DATE: 2026-08-29
 PURPOSE: FastAPI Application Gateway & Multi-Page Application (MPA) Static Router.
================================================================================
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
import os
import logging
from pathlib import Path

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI(
    title="AVIA SDCPS API",
    description="Aviation Safety Data Collection and Processing System",
    version="1.2.0",
    docs_url="/docs"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ==================== SERVE STATIC FILES ====================
PUBLIC_DIR = Path(__file__).resolve().parent / "public"
logger.info(f"📁 Public directory: {PUBLIC_DIR}")

# Mount static folders
js_dir = PUBLIC_DIR / "js"
css_dir = PUBLIC_DIR / "css"
views_dir = PUBLIC_DIR / "views"
components_dir = PUBLIC_DIR / "components"

if js_dir.exists():
    app.mount("/js", StaticFiles(directory=str(js_dir)), name="js")
if css_dir.exists():
    app.mount("/css", StaticFiles(directory=str(css_dir)), name="css")
if views_dir.exists():
    app.mount("/views", StaticFiles(directory=str(views_dir)), name="views")
if components_dir.exists():
    app.mount("/components", StaticFiles(directory=str(components_dir)), name="components")

def _serve_page(filename: str):
    file_path = PUBLIC_DIR / filename
    if file_path.exists():
        return FileResponse(str(file_path))
    return {"error": f"{filename} not found"}

# ==================== MPA HTML ROUTES ====================
@app.get("/")
async def serve_index():
    return _serve_page("index.html")

@app.get("/ae-view")
@app.get("/ae-view.html")
async def serve_ae_view():
    return _serve_page("ae-view.html")

@app.get("/sms-maturity")
@app.get("/sms-maturity.html")
async def serve_sms_maturity():
    return _serve_page("sms-maturity.html")

# 4 Dedicated Registers
@app.get("/hazard-register")
@app.get("/hazard-register.html")
async def serve_hazard_register():
    return _serve_page("hazard-register.html")

@app.get("/risk-register")
@app.get("/risk-register.html")
async def serve_risk_register():
    return _serve_page("risk-register.html")

@app.get("/can-register")
@app.get("/can-register.html")
async def serve_can_register():
    return _serve_page("can-register.html")

@app.get("/cap-register")
@app.get("/cap-register.html")
async def serve_cap_register():
    return _serve_page("cap-register.html")

@app.get("/state-oversight")
@app.get("/state-oversight.html")
async def serve_state_oversight():
    return _serve_page("state-oversight.html")

# Backward Compatibility Aliases
@app.get("/dashboard")
@app.get("/dashboard.html")
async def serve_dashboard():
    return _serve_page("dashboard.html")

@app.get("/hazard-log")
@app.get("/hazard-log.html")
async def serve_hazard_log_alias():
    return _serve_page("hazard-register.html")

@app.get("/can-cap")
@app.get("/can-cap.html")
async def serve_can_cap_alias():
    return _serve_page("can-register.html")
    
@app.get("/onboarding-guide")
@app.get("/onboarding-guide.html")
async def serve_onboarding_guide():
    return _serve_page("onboarding-guide.html")

# ==================== API ENDPOINTS ====================
@app.get("/api")
async def api_root():
    return {
        "message": "AVIA SDCPS API is running!",
        "demo_mode": os.getenv("DEMO_MODE", "true"),
        "version": "1.2.0"
    }

@app.get("/health")
async def health_check():
    return {
        "status": "healthy",
        "demo_mode": os.getenv("DEMO_MODE", "true"),
        "version": "1.2.0"
    }

# Router imports
from app.api.v1.hazards import router as hazards_router
from app.api.v1.state_risk import router as state_risk_router
from app.api.v1.demo import router as demo_router
from app.api.v1.lead_capture import router as lead_capture_router
from app.api.v1.leads import router as leads_router
from app.api.v1.email_preview import router as email_preview_router
from app.api.v1.nlp import router as nlp_router
from app.api.v1.hfacs import router as hfacs_router

app.include_router(hazards_router, prefix="/api/v1")
app.include_router(state_risk_router, prefix="/api/v1")
app.include_router(demo_router, prefix="/api/v1")
app.include_router(lead_capture_router, prefix="/api/v1")
app.include_router(leads_router, prefix="/api/v1")
app.include_router(email_preview_router, prefix="/api/v1")
app.include_router(nlp_router, prefix="/api/v1")
app.include_router(hfacs_router, prefix="/api/v1")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
