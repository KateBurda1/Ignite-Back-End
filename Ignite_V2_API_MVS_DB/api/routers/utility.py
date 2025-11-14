from fastapi import APIRouter

router = APIRouter(tags=["Utility"])

@router.get("/api/fields")
async def field_definitions():
    return {
        "parentCompanyId": "string – top-level company (e.g., Flying Horse Resort)",
        "childCompanyId": "string – optional sub-organization",
        "businessUnitId": "string – operational unit (hotel, golf, spa)",
        "revenueSegmentId": "string – revenue channel (restaurant, bar, etc.)",
        "microSegmentId": "string – fine-grain subset (e.g., Pool Bar)",
        "revenue": "number – total revenue",
        "cost": "number – total cost",
        "profitMargin": "number – profit margin (0-1)",
        "growthRate": "number – growth rate (0-1)",
        "transactions": "integer – count of transactions",
        "title": "string – insight title",
        "summary": "string – human-readable insight",
        "confidence": "number – confidence in insight",
        "recommendation": "string – tactical action",
        "priority": "string – low/medium/high"
    }

@router.get("/api/sample/flyinghorse")
async def sample_flyinghorse():
    return {
        "parentCompany": "Flying Horse Resort",
        "childCompanies": [],
        "businessUnits": [
            {
                "id": "BU_HOTEL",
                "name": "Hotel",
                "revenueSegments": [
                    {"id":"RS_BAR", "name":"Bar", "microSegments": ["Pool Bar", "Lobby Bar"]},
                    {"id":"RS_RESTAURANT", "name":"Restaurant", "microSegments": ["Main Dining", "Patio"]}
                ]
            },
            {
                "id": "BU_GOLF",
                "name": "Golf Course",
                "revenueSegments": [
                    {"id":"RS_PROSHOP", "name":"Pro Shop", "microSegments": ["Equipment", "Apparel"]}
                ]
            }
        ]
    }
