from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from ..auth import hash_password, verify_password, create_access_token
from ..schemas import Token, LoginRequest
from .. import models, schemas
from ..database import get_db

router = APIRouter(
    prefix="/clients",
    tags=["Клиенты"]
)

@router.post("/", response_model=schemas.ClientResponse, status_code=status.HTTP_201_CREATED)
def create_client(client: schemas.ClientCreate, db: Session = Depends(get_db)):
    """
    Создаёт нового клиента с хешированием пароля.
    """
    # Проверяем уникальность email и телефона
    db_client = db.query(models.Client).filter(
        (models.Client.email == client.email) | 
        (models.Client.phone == client.phone)
    ).first()
    
    if db_client:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Клиент с таким email или телефоном уже существует"
        )
    
    # ХЕШИРУЕМ ПАРОЛЬ перед сохранением!
    hashed_password = hash_password(client.password)
    
    db_client = models.Client(
        full_name=client.full_name,
        phone=client.phone,
        email=client.email,
        password_hash=hashed_password,  # Сохраняем хеш, а не открытый пароль!
        visit_count=0,
        current_discount=0.0
    )
    
    db.add(db_client)
    db.commit()
    db.refresh(db_client)
    
    return db_client


# --- НОВЫЙ ЭНДПОИНТ: Вход для клиента ---
@router.post("/login", response_model=Token)
def login_client(login_data: LoginRequest, db: Session = Depends(get_db)):
    """
    Аутентификация клиента по email/телефону и паролю.
    Возвращает JWT-токен.
    """
    # Ищем клиента по email или телефону
    db_client = db.query(models.Client).filter(
        (models.Client.email == login_data.login) | 
        (models.Client.phone == login_data.login)
    ).first()
    
    if not db_client:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Неверный логин или пароль"
        )
    
    # Проверяем пароль
    if not verify_password(login_data.password, db_client.password_hash):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Неверный логин или пароль"
        )
    
    # Создаём JWT-токен
    access_token = create_access_token(
        data={"user_id": db_client.id, "user_type": "client"}
    )
    
    return {"access_token": access_token, "token_type": "bearer"}