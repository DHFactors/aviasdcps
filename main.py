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
    version="1.0.0",
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

# Helper to serve MPA pages
def _serve_page(filename: str):
    file_path = PUBLIC_DIR / filename
    if file_path.exists():
        return FileResponse(str(file_path))
    return {"error": f"{filename} not found"}

# ==================== HTML PAGES ====================
@app.get("/")
async def serve_index():
    """Serve the landing page"""
    return _serve_page("index.html")

@app.get("/aviasdcps.html")
async def serve_aviasdcps():
    """Legacy SPA — keep for backward compat, redirect to MPA dashboard preferred"""
    return _serve_page("aviasdcps.html")

# MPA pages - both clean URLs and .html
@app.get("/dashboard")
@app.get("/dashboard.html")
async def serve_dashboard():
    return _serve_page("dashboard.html")

@app.get("/hazard-log")
@app.get("/hazard-log.html")
async def serve_hazard_log_mpa():
    return _serve_page("hazard-log.html")

@app.get("/hazard-analysis")
@app.get("/hazard-analysis.html")
async def serve_hazard_analysis():
    return _serve_page("hazard-analysis.html")

@app.get("/can-cap")
@app.get("/can-cap.html")
async def serve_can_cap():
    return _serve_page("can-cap.html")

@app.get("/state-oversight")
@app.get("/state-oversight.html")
async def serve_state_oversight():
    return _serve_page("state-oversight.html")

@app.get("/reports")
@app.get("/reports.html")
async def serve_reports():
    return _serve_page("reports.html")

@app.get("/about")
@app.get("/about.html")
async def serve_about():
    return _serve_page("about.html")

@app.get("/login")
@app.get("/login.html")
async def serve_login():
    return _serve_page("login.html")

# Legacy view path
@app.get("/views/hazard-log.html")
async def serve_hazard_log():
    """Legacy Hazard Log view path"""
    file_path = PUBLIC_DIR / "views" / "hazard-log.html"
    if file_path.exists():
        return FileResponse(str(file_path))
    return _serve_page("hazard-log.html")

# Clean URLs for hazards/state aliases (Task 7)
@app.get("/hazards")
async def serve_hazards_alias():
    return _serve_page("hazard-log.html")

@app.get("/state")
async def serve_state_alias():
    return _serve_page("state-oversight.html")

# ==================== API ENDPOINTS ====================
@app.get("/api")
async def api_root():
    return {
        "message": "AVIA SDCPS API is running!",
        "demo_mode": os.getenv("DEMO_MODE", "true"),
        "version": "1.0.0",
        "endpoints": {
            "docs": "/docs",
            "health": "/health",
            "hazards": "/api/v1/hazards",
            "state_risk": "/api/v1/state-risk"
        }
    }

@app.get("/health")
async def health_check():
    return {
        "status": "healthy",
        "demo_mode": os.getenv("DEMO_MODE", "true"),
        "version": "1.0.0"
    }

# ==================== IMPORT AND REGISTER ROUTERS ====================
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
