from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from .. import models, schemas
from ..database import get_db

router = APIRouter(
    prefix="/callback-requests",
    tags=["Заявки на обратный звонок"]
)

@router.post("/", response_model=schemas.CallbackRequestResponse, status_code=status.HTTP_201_CREATED)
def create_callback_request(request: schemas.CallbackRequestCreate, db: Session = Depends(get_db)):
    """Создаёт новую заявку на обратный звонок."""
    db_request = models.CallbackRequest(
        client_name=request.client_name,
        phone=request.phone,
        status="Ожидает обработки"
    )
    db.add(db_request)
    db.commit()
    db.refresh(db_request)
    return db_request

@router.get("/", response_model=List[schemas.CallbackRequestResponse])
def get_callback_requests(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """Возвращает список всех заявок на обратный звонок."""
    return db.query(models.CallbackRequest).offset(skip).limit(limit).all()

@router.get("/{request_id}", response_model=schemas.CallbackRequestResponse)
def get_callback_request(request_id: int, db: Session = Depends(get_db)):
    """Возвращает информацию о заявке по ID."""
    db_request = db.query(models.CallbackRequest).filter(models.CallbackRequest.id == request_id).first()
    if not db_request:
        raise HTTPException(status_code=404, detail="Заявка не найдена")
    return db_request

@router.put("/{request_id}", response_model=schemas.CallbackRequestResponse)
def update_callback_request(request_id: int, request: schemas.CallbackRequestUpdate, db: Session = Depends(get_db)):
    """Обновляет статус заявки."""
    db_request = db.query(models.CallbackRequest).filter(models.CallbackRequest.id == request_id).first()
    if not db_request:
        raise HTTPException(status_code=404, detail="Заявка не найдена")
    
    update_data = request.dict(exclude_unset=True)
    for key, value in update_data.items():
        setattr(db_request, key, value)
    
    db.commit()
    db.refresh(db_request)
    return db_request

@router.delete("/{request_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_callback_request(request_id: int, db: Session = Depends(get_db)):
    """Удаляет заявку."""
    db_request = db.query(models.CallbackRequest).filter(models.CallbackRequest.id == request_id).first()
    if not db_request:
        raise HTTPException(status_code=404, detail="Заявка не найдена")
    
    db.delete(db_request)
    db.commit()
    return None