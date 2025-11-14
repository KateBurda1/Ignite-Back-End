from fastapi import APIRouter, Depends
from sqlalchemy import text
from sqlalchemy.orm import Session
from .deps import get_db

router = APIRouter(prefix="/api/valuescores", tags=["Value Scoring"])

@router.get("")
def get_value_scores(parentCompanyId: str = None, businessUnitId: str = None, db: Session = Depends(get_db)):
    q = "SELECT * FROM value_scores WHERE 1=1"
    params = {}
    if parentCompanyId:
        q += " AND parent_company_id=:parentCompanyId"
        params["parentCompanyId"] = parentCompanyId
    if businessUnitId:
        q += " AND business_unit_id=:businessUnitId"
        params["businessUnitId"] = businessUnitId
    rows = db.execute(text(q), params).mappings().all()
    return [dict(r) for r in rows]
