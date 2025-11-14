from fastapi import APIRouter, Depends, Body
from typing import List, Dict, Any, Union
from sqlalchemy import text
from sqlalchemy.orm import Session
from .deps import get_db

router = APIRouter(prefix="/internal/ingest", tags=["_Internal Ingest"])

@router.post("/data")
def ingest_data(payload: Union[List[Dict[str, Any]], Dict[str, Any]] = Body(...), db: Session = Depends(get_db)):
    items = payload if isinstance(payload, list) else [payload]
    for r in items:
        db.execute(text("""
          INSERT INTO data (parent_company_id, child_company_id, business_unit_id, revenue_segment_id, micro_segment_id,
                            revenue, cost, profit_margin, growth_rate, transactions)
          VALUES (:parentCompanyId, :childCompanyId, :businessUnitId, :revenueSegmentId, :microSegmentId,
                  :revenue, :cost, :profitMargin, :growthRate, :transactions)
        """), r)
    db.commit()
    return {"status":"ok","inserted":len(items)}

@router.post("/valuescores")
def ingest_valuescores(payload: Union[List[Dict[str, Any]], Dict[str, Any]] = Body(...), db: Session = Depends(get_db)):
    items = payload if isinstance(payload, list) else [payload]
    for r in items:
        db.execute(text("""
          INSERT INTO value_scores (parent_company_id, business_unit_id, revenue_segment_id, micro_segment_id,
                                    revenue, profit_margin, growth_rate, value_score)
          VALUES (:parentCompanyId, :businessUnitId, :revenueSegmentId, :microSegmentId,
                  :revenue, :profitMargin, :growthRate, :valueScore)
        """), r)
    db.commit()
    return {"status":"ok","inserted":len(items)}

@router.post("/insights")
def ingest_insights(payload: Union[List[Dict[str, Any]], Dict[str, Any]] = Body(...), db: Session = Depends(get_db)):
    items = payload if isinstance(payload, list) else [payload]
    for r in items:
        db.execute(text("""
          INSERT INTO insights (parent_company_id, business_unit_id, revenue_segment_id, micro_segment_id,
                                title, summary, confidence, source)
          VALUES (:parentCompanyId, :businessUnitId, :revenueSegmentId, :microSegmentId,
                  :title, :summary, :confidence, :source)
        """), r)
    db.commit()
    return {"status":"ok","inserted":len(items)}

@router.post("/recommendations")
def ingest_recommendations(payload: Union[List[Dict[str, Any]], Dict[str, Any]] = Body(...), db: Session = Depends(get_db)):
    items = payload if isinstance(payload, list) else [payload]
    for r in items:
        db.execute(text("""
          INSERT INTO recommendations (parent_company_id, business_unit_id, revenue_segment_id, micro_segment_id,
                                       recommendation, priority)
          VALUES (:parentCompanyId, :businessUnitId, :revenueSegmentId, :microSegmentId,
                  :recommendation, :priority)
        """), r)
    db.commit()
    return {"status":"ok","inserted":len(items)}

@router.post("/segments")
def replace_segments(payload: Dict[str, Any] = Body(...), db: Session = Depends(get_db)):
    db.execute(text("INSERT INTO segments (json_data) VALUES (:j)"), {"j": payload})
    db.commit()
    return {"status":"ok","message":"segments updated"}
