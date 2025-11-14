from fastapi import APIRouter, Depends
from sqlalchemy import text
from sqlalchemy.orm import Session
from .deps import get_db

router = APIRouter(prefix="/api/data", tags=["Data Ingestion"])

@router.get("")
def get_data(parentCompanyId: str = None, businessUnitId: str = None, db: Session = Depends(get_db)):
    q = "SELECT * FROM data WHERE 1=1"
    params = {}
    if parentCompanyId:
        q += " AND parent_company_id=:parentCompanyId"
        params["parentCompanyId"] = parentCompanyId
    if businessUnitId:
        q += " AND business_unit_id=:businessUnitId"
        params["businessUnitId"] = businessUnitId
    rows = db.execute(text(q), params).mappings().all()
    return [dict(r) for r in rows]
