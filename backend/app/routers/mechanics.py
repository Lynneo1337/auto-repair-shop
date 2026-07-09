from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from ..auth import hash_password, verify_password, create_access_token
from ..schemas import Token, LoginRequest
from .. import models, schemas
from ..database import get_db

router = APIRouter(
    prefix="/mechanics",
    tags=["Мастера"]
)


@router.post("/", response_model=schemas.MechanicResponse, status_code=status.HTTP_201_CREATED)
def create_mechanic(mechanic: schemas.MechanicCreate, db: Session = Depends(get_db)):
    """Создаёт нового мастера с хешированием пароля."""
    # Проверяем уникальность логина
    db_mechanic = db.query(models.Mechanic).filter(models.Mechanic.login == mechanic.login).first()
    if db_mechanic:
        raise HTTPException(status_code=400, detail="Мастер с таким логином уже существует")
    
    # ХЕШИРУЕМ ПАРОЛЬ!
    hashed_password = hash_password(mechanic.password)
    
    db_mechanic = models.Mechanic(
        full_name=mechanic.full_name,
        specialization=mechanic.specialization,
        login=mechanic.login,
        password_hash=hashed_password  # Сохраняем хеш!
    )
    db.add(db_mechanic)
    db.commit()
    db.refresh(db_mechanic)
    return db_mechanic


# --- НОВЫЙ ЭНДПОИНТ: Вход для мастера ---
@router.post("/login", response_model=Token)
def login_mechanic(login_data: LoginRequest, db: Session = Depends(get_db)):
    """Аутентификация мастера по логину и паролю."""
    db_mechanic = db.query(models.Mechanic).filter(
        models.Mechanic.login == login_data.login
    ).first()
    
    if not db_mechanic:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Неверный логин или пароль"
        )
    
    if not verify_password(login_data.password, db_mechanic.password_hash):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Неверный логин или пароль"
        )
    
    access_token = create_access_token(
        data={"user_id": db_mechanic.id, "user_type": "mechanic"}
    )
    
    return {"access_token": access_token, "token_type": "bearer"}