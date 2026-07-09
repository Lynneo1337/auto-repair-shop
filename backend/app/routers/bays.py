from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from .. import models, schemas
from ..database import get_db

router = APIRouter(
    prefix="/bays",
    tags=["Боксы"]
)

@router.post("/", response_model=schemas.BayResponse, status_code=status.HTTP_201_CREATED)
def create_bay(bay: schemas.BayCreate, db: Session = Depends(get_db)):
    """Создаёт новый бокс."""
    db_bay = models.Bay(**bay.dict())
    db.add(db_bay)
    db.commit()
    db.refresh(db_bay)
    return db_bay

@router.get("/", response_model=List[schemas.BayResponse])
def get_bays(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """Возвращает список всех боксов."""
    return db.query(models.Bay).offset(skip).limit(limit).all()

@router.get("/{bay_id}", response_model=schemas.BayResponse)
def get_bay(bay_id: int, db: Session = Depends(get_db)):
    """Возвращает информацию о боксе по ID."""
    db_bay = db.query(models.Bay).filter(models.Bay.id == bay_id).first()
    if not db_bay:
        raise HTTPException(status_code=404, detail="Бокс не найден")
    return db_bay

@router.put("/{bay_id}", response_model=schemas.BayResponse)
def update_bay(bay_id: int, bay: schemas.BayUpdate, db: Session = Depends(get_db)):
    """Обновляет данные бокса."""
    db_bay = db.query(models.Bay).filter(models.Bay.id == bay_id).first()
    if not db_bay:
        raise HTTPException(status_code=404, detail="Бокс не найден")
    
    update_data = bay.dict(exclude_unset=True)
    for key, value in update_data.items():
        setattr(db_bay, key, value)
    
    db.commit()
    db.refresh(db_bay)
    return db_bay

@router.delete("/{bay_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_bay(bay_id: int, db: Session = Depends(get_db)):
    """Удаляет бокс."""
    db_bay = db.query(models.Bay).filter(models.Bay.id == bay_id).first()
    if not db_bay:
        raise HTTPException(status_code=404, detail="Бокс не найден")
    
    db.delete(db_bay)
    db.commit()
    return None