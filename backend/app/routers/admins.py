from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from ..auth import hash_password, verify_password, create_access_token
from ..schemas import Token, LoginRequest
from .. import models, schemas
from ..database import get_db

router = APIRouter(
    prefix="/admins",
    tags=["Администраторы"]
)



@router.post("/", response_model=schemas.AdminResponse, status_code=status.HTTP_201_CREATED)
def create_admin(admin: schemas.AdminCreate, db: Session = Depends(get_db)):
    """Создаёт нового администратора с хешированием пароля."""
    # Проверяем уникальность логина
    db_admin = db.query(models.Admin).filter(models.Admin.login == admin.login).first()
    if db_admin:
        raise HTTPException(status_code=400, detail="Администратор с таким логином уже существует")
    
    # ХЕШИРУЕМ ПАРОЛЬ!
    hashed_password = hash_password(admin.password)
    
    db_admin = models.Admin(
        full_name=admin.full_name,
        login=admin.login,
        password_hash=hashed_password  # Сохраняем хеш!
    )
    db.add(db_admin)
    db.commit()
    db.refresh(db_admin)
    return db_admin


# --- НОВЫЙ ЭНДПОИНТ: Вход для администратора ---
@router.post("/login", response_model=Token)
def login_admin(login_data: LoginRequest, db: Session = Depends(get_db)):
    """Аутентификация администратора по логину и паролю."""
    db_admin = db.query(models.Admin).filter(
        models.Admin.login == login_data.login
    ).first()
    
    if not db_admin:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Неверный логин или пароль"
        )
    
    if not verify_password(login_data.password, db_admin.password_hash):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Неверный логин или пароль"
        )
    
    access_token = create_access_token(
        data={"user_id": db_admin.id, "user_type": "admin"}
    )
    
    return {"access_token": access_token, "token_type": "bearer"}