from fastapi import APIRouter, Depends
from sqlalchemy import text
from sqlalchemy.orm import Session
from .deps import get_db

router = APIRouter(prefix="/api/segments", tags=["Segmentation"])

@router.get("")
def get_segments(db: Session = Depends(get_db)):
    # Return the latest segments json
    row = db.execute(text("SELECT json_data FROM segments ORDER BY created_at DESC LIMIT 1")).mappings().first()
    return row["json_data"] if row else {"businessUnits": []}
