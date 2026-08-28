"""
FILE: app/api/v1/nlp.py
PURPOSE: NLP Hazard Extraction via Groq API (with heuristic fallback)
"""
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
import os
import re
import json
import logging

logger = logging.getLogger(__name__)
router = APIRouter(prefix="/nlp", tags=["nlp"])

class ReportRequest(BaseModel):
    text: str
    tenant_id: str = "tenant-001"

class HazardExtraction(BaseModel):
    title: str
    description: str
    category: str
    nano_code: str
    nano_description: str
    severity: str
    probability: str
    risk_level: str

HFACS_MAP = {
    "PC307": "Fatigue",
    "PC501": "Motion Illusion",
    "PC504": "Misperception of Changing Environment",
    "PC305": "Physical Illness/Injury",
    "PC202": "Psychological Problem",
    "PC206": "Overconfidence",
    "PC207": "Pressing",
    "PC208": "Complacency",
    "PP106": "Critical Information Not Communicated",
    "PP108": "Failed to Effectively Communicate",
    "AE101": "Unintended Operation of Equipment",
    "AE201": "Inadequate Real-Time Risk Assessment",
    "AE205": "Ignored a Caution/Warning",
    "AV002": "Commits Widespread/Routine Violation",
    "PE101": "Environmental Conditions Affecting Vision",
    "PE201": "Seat and Restraint System Problems",
    "PE202": "Instrumentation and Warning System Issues",
}

# Enable fallback mode for demo — set to False when Groq API is available
USE_MOCK = os.getenv("NLP_USE_MOCK", "true").lower() in ("1", "true", "yes")

def get_mock_analysis(text: str):
    """Return mock analysis for demo purposes — keyword-based per Task 5."""
    keywords = {
        'bird': {'category': 'Environmental', 'severity': 'High', 'probability': 'Likely'},
        'fatigue': {'category': 'Human Factors', 'severity': 'Medium', 'probability': 'Possible'},
        'weather': {'category': 'Environmental', 'severity': 'Medium', 'probability': 'Possible'},
        'fuel': {'category': 'Technical', 'severity': 'Critical', 'probability': 'Rare'},
        'communication': {'category': 'Human Factors', 'severity': 'High', 'probability': 'Unlikely'},
        'runway': {'category': 'Operational', 'severity': 'Medium', 'probability': 'Possible'},
        'navigation': {'category': 'Technical', 'severity': 'Critical', 'probability': 'Rare'},
    }
    for word, data in keywords.items():
        if word.lower() in text.lower():
            return {
                "title": f"Extracted hazard from report ({word})",
                "description": text[:200] + ("..." if len(text) > 200 else ""),
                "category": data.get("category", "Operational"),
                "nano_code": "PC307" if word=="fatigue" else "PE101" if word in ("bird","weather") else "PE202" if word in ("fuel","navigation") else "PP108" if word=="communication" else "AE201",
                "nano_description": HFACS_MAP.get("PC307" if word=="fatigue" else "PE101" if word in ("bird","weather") else "PE202" if word in ("fuel","navigation") else "PP108" if word=="communication" else "AE201", ""),
                "severity": data.get("severity", "Medium"),
                "probability": data.get("probability", "Possible"),
                "risk_level": "High" if data.get("severity")=="Critical" else "Medium"
            }
    return {
        "title": "Safety concern reported",
        "description": text[:200] + ("..." if len(text) > 200 else ""),
        "category": "Operational",
        "nano_code": "PC208",
        "nano_description": "Complacency",
        "severity": "Medium",
        "probability": "Possible",
        "risk_level": "Medium"
    }

def heuristic_extract(text: str) -> dict:
    t = text.lower()
    if any(k in t for k in ["bird", "runway", "fod", "debris", "takeoff", "landing", "excursion"]):
        category = "Operational"
        nano_code = "AE201"
    elif any(k in t for k in ["fuel", "hydraulic", "engine", "system", "gps", "navigation", "instrument"]):
        category = "Technical"
        nano_code = "PE202"
    elif any(k in t for k in ["fatigue", "crew", "human", "communication", "atc"]):
        category = "Human Factors"
        nano_code = "PC307" if "fatigue" in t else "PP108"
    elif any(k in t for k in ["weather", "thunderstorm", "monsoon", "wind", "icing", "storm"]):
        category = "Environmental"
        nano_code = "PE101"
    else:
        category = "Organizational"
        nano_code = "AE201"
    if any(k in t for k in ["critical", "emergency", "failure", "collision", "crash"]):
        severity = "Critical"
        probability = "Possible"
    elif any(k in t for k in ["high", "severe", "go-around", "quarantine"]):
        severity = "High"
        probability = "Likely" if "likely" in t or "multiple" in t else "Possible"
    elif any(k in t for k in ["medium", "shortage", "leak"]):
        severity = "Medium"
        probability = "Possible"
    else:
        severity = "Medium"
        probability = "Possible"
    sev_w = {"Low":1,"Medium":2,"High":3,"Critical":4}
    prob_w = {"Rare":1,"Unlikely":2,"Possible":3,"Likely":4,"Almost Certain":5}
    score = sev_w.get(severity,2)*prob_w.get(probability,3)
    if score <=4: risk_level="Low"
    elif score<=8: risk_level="Medium"
    elif score<=12: risk_level="High"
    else: risk_level="Critical"
    words = text.strip().split()
    title = " ".join(words[:8]).capitalize()
    if len(title) > 60: title = title[:57]+"..."
    description = text.strip()
    if len(description) > 240: description = description[:237]+"..."
    if len(description.split(".")) <2:
        description = description + " Hazard requires assessment per ICAO Annex 19."
    return {
        "title": title,
        "description": description,
        "category": category,
        "nano_code": nano_code,
        "nano_description": HFACS_MAP.get(nano_code, ""),
        "severity": severity,
        "probability": probability,
        "risk_level": risk_level
    }

@router.post("/analyze", response_model=HazardExtraction)
async def analyze_report(request: ReportRequest):
    """
    Analyze a safety report using Groq API with fallback for demo (USE_MOCK).
    """
    text = (request.text or "").strip()
    if not text or len(text) < 10:
        raise HTTPException(status_code=400, detail="Report text too short")
    # Demo fallback mode: return mock immediately if enabled or no key
    api_key = os.getenv("GROQ_API_KEY")
    if USE_MOCK or not api_key:
        logger.info(f"Using mock analysis (USE_MOCK={USE_MOCK}, has_key={bool(api_key)})")
        return get_mock_analysis(text)
    # Try Groq via OpenAI SDK
    try:
        import openai  # type: ignore
        client = openai.OpenAI(
            base_url="https://api.groq.com/openai/v1",
            api_key=api_key
        )
        prompt = f"""
You are an aviation safety expert. Analyze the following safety report and extract hazard information.

Safety Report:
"{text}"

Extract the following fields in JSON format:
1. title: A concise hazard title (max 8 words)
2. description: A detailed description of the hazard (2-3 sentences)
3. category: One of [Operational, Technical, Human Factors, Environmental, Organizational]
4. nano_code: HFACS code from the list below
5. nano_description: HFACS code description
6. severity: One of [Low, Medium, High, Critical]
7. probability: One of [Rare, Unlikely, Possible, Likely, Almost Certain]
8. risk_level: One of [Low, Medium, High, Critical] based on severity × probability

HFACS Codes:
- PC307: Fatigue
- PC501: Motion Illusion
- PC504: Misperception of Changing Environment
- PC305: Physical Illness/Injury
- PC202: Psychological Problem
- PC206: Overconfidence
- PC207: Pressing
- PC208: Complacency
- PP106: Critical Information Not Communicated
- PP108: Failed to Effectively Communicate
- AE101: Unintended Operation of Equipment
- AE201: Inadequate Real-Time Risk Assessment
- AE205: Ignored a Caution/Warning
- AV002: Commits Widespread/Routine Violation
- PE101: Environmental Conditions Affecting Vision
- PE201: Seat and Restraint System Problems
- PE202: Instrumentation and Warning System Issues

Return ONLY valid JSON with these keys:
{{
    "title": "",
    "description": "",
    "category": "",
    "nano_code": "",
    "nano_description": "",
    "severity": "",
    "probability": "",
    "risk_level": ""
}}
"""
        response = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[
                {"role": "system", "content": "You are an aviation safety expert. Extract hazard information from safety reports."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.3,
            max_tokens=500
        )
        result_text = response.choices[0].message.content or ""
        json_match = re.search(r'\{.*\}', result_text, re.DOTALL)
        if json_match:
            result = json.loads(json_match.group())
            if result.get("nano_code") in HFACS_MAP:
                result["nano_description"] = HFACS_MAP[result["nano_code"]]
            else:
                result["nano_code"] = result.get("nano_code","AE201")
                result["nano_description"] = HFACS_MAP.get(result["nano_code"],"")
            return result
    except Exception as e:
        logger.warning(f"Groq call failed, fallback to mock: {e}")
    # Fallback to mock on any Groq error
    return get_mock_analysis(text)
