from passlib.context import CryptContext
from datetime import datetime, timedelta
from jose import JWTError, jwt
from fastapi import HTTPException, status
import os


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# Секретный ключ для подписи JWT-токенов
# В реальном проекте его нужно хранить в .env!
SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30


def hash_password(password: str) -> str:
    """
    Хеширует пароль с помощью bcrypt.
    
    Args:
        password: Пароль в открытом виде
        
    Returns:
        Хеш пароля
    """
    return pwd_context.hash(password)


def verify_password(plain_password: str, hashed_password: str) -> bool:
    """
    Проверяет, соответствует ли пароль хешу.
    
    Args:
        plain_password: Пароль в открытом виде (введённый пользователем)
        hashed_password: Хеш пароля из базы данных
        
    Returns:
        True, если пароль верный, иначе False
    """
    return pwd_context.verify(plain_password, hashed_password)


def create_access_token(data: dict, expires_delta: timedelta = None) -> str:
    """
    Создаёт JWT-токен для аутентификации.
    
    Args:
        data: Данные, которые нужно закодировать в токен (например, id пользователя)
        expires_delta: Время жизни токена
        
    Returns:
        JWT-токен в виде строки
    """
    to_encode = data.copy()
    
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    
    return encoded_jwt


def verify_token(token: str) -> dict:
    """
    Проверяет и декодирует JWT-токен.
    
    Args:
        token: JWT-токен
        
    Returns:
        Данные из токена
        
    Raises:
        HTTPException: Если токен невалидный
    """
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except JWTError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Невалидный токен",
            headers={"WWW-Authenticate": "Bearer"},
        )