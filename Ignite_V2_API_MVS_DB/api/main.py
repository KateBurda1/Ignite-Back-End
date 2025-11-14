from fastapi import FastAPI, Request, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware
import os
from dotenv import load_dotenv
from routers import data_db, valuescores_db, insights_db, recommendations_db, segments_db, ingest_db, utility

load_dotenv()
API_KEY = os.getenv("API_KEY", "dev-key")
BASE_URL = "https://app.ingnityourgrowth.com"

app = FastAPI(
    title="Ignite AI Agentic API (DB-backed)",
    description=(
        "Public API for Conductor AI and the Ignite prototype.\n\n"
        "Base URL: https://app.ingnityourgrowth.com\n"
        "Authentication: header `x-api-key`\n\n"
        "Public (GET): /api/data, /api/valuescores, /api/insights, /api/recommendations, /api/segments, /api/fields, /api/sample/flyinghorse\n"
        "Private (POST ingest): /internal/ingest/*"
    ),
    version="2.0.0",
    servers=[
        {"url": BASE_URL, "description": "Production"},
        {"url": "http://127.0.0.1:8000", "description": "Local Development"}
    ]
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.middleware("http")
async def verify_api_key(request: Request, call_next):
    if request.url.path.startswith("/api") or request.url.path.startswith("/internal"):
        key = request.headers.get("x-api-key")
        if key != API_KEY:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid or missing API key")
    return await call_next(request)

# Routers
app.include_router(data_db.router)
app.include_router(valuescores_db.router)
app.include_router(insights_db.router)
app.include_router(recommendations_db.router)
app.include_router(segments_db.router)
app.include_router(ingest_db.router)
app.include_router(utility.router)

@app.get("/")
async def root():
    return {
        "status":"Ignite API Online",
        "base_url": BASE_URL,
        "auth": {"header":"x-api-key","type":"API key"},
        "public_endpoints": {
            "data": f"{BASE_URL}/api/data",
            "valuescores": f"{BASE_URL}/api/valuescores",
            "insights": f"{BASE_URL}/api/insights",
            "recommendations": f"{BASE_URL}/api/recommendations",
            "segments": f"{BASE_URL}/api/segments",
            "fields": f"{BASE_URL}/api/fields",
            "sample": f"{BASE_URL}/api/sample/flyinghorse"
        },
        "private_ingest_endpoints": {
            "data": f"{BASE_URL}/internal/ingest/data",
            "valuescores": f"{BASE_URL}/internal/ingest/valuescores",
            "insights": f"{BASE_URL}/internal/ingest/insights",
            "recommendations": f"{BASE_URL}/internal/ingest/recommendations",
            "segments": f"{BASE_URL}/internal/ingest/segments"
        }
    }
