from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from .. import models, schemas
from ..database import get_db

router = APIRouter(
    prefix="/cars",
    tags=["Автомобили"]
)

@router.post("/", response_model=schemas.CarResponse, status_code=status.HTTP_201_CREATED)
def create_car(car: schemas.CarCreate, db: Session = Depends(get_db)):
    """Создаёт новый автомобиль, привязанный к клиенту."""
    # Проверяем, существует ли клиент
    db_client = db.query(models.Client).filter(models.Client.id == car.client_id).first()
    if not db_client:
        raise HTTPException(status_code=404, detail="Клиент не найден")
    
    # Проверяем уникальность VIN
    db_car = db.query(models.Car).filter(models.Car.vin == car.vin).first()
    if db_car:
        raise HTTPException(status_code=400, detail="Автомобиль с таким VIN уже существует")
    
    db_car = models.Car(**car.dict())
    db.add(db_car)
    db.commit()
    db.refresh(db_car)
    return db_car

@router.get("/", response_model=List[schemas.CarResponse])
def get_cars(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """Возвращает список всех автомобилей."""
    return db.query(models.Car).offset(skip).limit(limit).all()

@router.get("/{car_id}", response_model=schemas.CarResponse)
def get_car(car_id: int, db: Session = Depends(get_db)):
    """Возвращает информацию об автомобиле по ID."""
    db_car = db.query(models.Car).filter(models.Car.id == car_id).first()
    if not db_car:
        raise HTTPException(status_code=404, detail="Автомобиль не найден")
    return db_car

@router.put("/{car_id}", response_model=schemas.CarResponse)
def update_car(car_id: int, car: schemas.CarUpdate, db: Session = Depends(get_db)):
    """Обновляет данные автомобиля."""
    db_car = db.query(models.Car).filter(models.Car.id == car_id).first()
    if not db_car:
        raise HTTPException(status_code=404, detail="Автомобиль не найден")
    
    update_data = car.dict(exclude_unset=True)
    for key, value in update_data.items():
        setattr(db_car, key, value)
    
    db.commit()
    db.refresh(db_car)
    return db_car

@router.delete("/{car_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_car(car_id: int, db: Session = Depends(get_db)):
    """Удаляет автомобиль."""
    db_car = db.query(models.Car).filter(models.Car.id == car_id).first()
    if not db_car:
        raise HTTPException(status_code=404, detail="Автомобиль не найден")
    
    db.delete(db_car)
    db.commit()
    return None