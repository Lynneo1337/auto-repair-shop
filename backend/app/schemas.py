from pydantic import BaseModel, EmailStr, Field
from typing import Optional, List
from datetime import datetime

class ClientCreate(BaseModel):
    full_name: str = Field(..., min_length=3, max_length=100, description="ФИО клиента")
    phone: str = Field(..., pattern=r"^\+?[0-9]{10,15}$", description="Телефон в формате +79991234567")
    email: EmailStr = Field(..., description="Email клиента")
    password: str = Field(..., min_length=6, description="Пароль (минимум 6 символов)")

class ClientUpdate(BaseModel):
    full_name: Optional[str] = Field(None, min_length=3, max_length=100)
    phone: Optional[str] = Field(None, pattern=r"^\+?[0-9]{10,15}$")
    email: Optional[EmailStr] = None

class ClientResponse(BaseModel):
    id: int
    full_name: str
    phone: str
    email: str
    visit_count: int
    current_discount: float
    
    class Config:
        from_attributes = True


class CarBase(BaseModel):
    brand_model: str = Field(..., min_length=2, max_length=100, description="Марка и модель")
    license_plate: str = Field(..., min_length=6, max_length=10, description="Гос. номер")
    vin: str = Field(..., min_length=17, max_length=17, description="VIN-код (17 символов)")

class CarCreate(CarBase):
    client_id: int = Field(..., description="ID клиента-владельца")

class CarUpdate(BaseModel):
    brand_model: Optional[str] = None
    license_plate: Optional[str] = None
    vin: Optional[str] = None

class CarResponse(CarBase):
    id: int
    client_id: int
    
    class Config:
        from_attributes = True


class ServiceBase(BaseModel):
    name: str = Field(..., min_length=3, max_length=200, description="Название услуги")
    price: float = Field(..., gt=0, description="Цена услуги (больше 0)")
    req_specialization: str = Field(..., description="Требуемая специализация мастера")

class ServiceCreate(ServiceBase):
    pass

class ServiceUpdate(BaseModel):
    name: Optional[str] = None
    price: Optional[float] = None
    req_specialization: Optional[str] = None

class ServiceResponse(ServiceBase):
    id: int
    
    class Config:
        from_attributes = True


class MechanicBase(BaseModel):
    full_name: str = Field(..., min_length=3, max_length=100)
    specialization: str = Field(..., description="Специализация мастера")
    login: str = Field(..., min_length=3, max_length=50)

class MechanicCreate(MechanicBase):
    password: str = Field(..., min_length=6)

class MechanicUpdate(BaseModel):
    full_name: Optional[str] = None
    specialization: Optional[str] = None
    login: Optional[str] = None

class MechanicResponse(MechanicBase):
    id: int
    
    class Config:
        from_attributes = True


class BayBase(BaseModel):
    number: str = Field(..., description="Номер бокса")
    capacity: int = Field(default=2, ge=1, le=10, description="Вместимость бокса")

class BayCreate(BayBase):
    pass

class BayUpdate(BaseModel):
    number: Optional[str] = None
    capacity: Optional[int] = None

class BayResponse(BayBase):
    id: int
    
    class Config:
        from_attributes = True


class DiscountRuleBase(BaseModel):
    min_visits: int = Field(..., ge=0, description="Минимальное количество посещений")
    max_visits: Optional[int] = Field(None, ge=0, description="Максимальное количество посещений (None = без лимита)")
    discount_percent: float = Field(..., ge=0, le=100, description="Процент скидки (0-100)")

class DiscountRuleCreate(DiscountRuleBase):
    pass

class DiscountRuleUpdate(BaseModel):
    min_visits: Optional[int] = None
    max_visits: Optional[int] = None
    discount_percent: Optional[float] = None

class DiscountRuleResponse(DiscountRuleBase):
    id: int
    
    class Config:
        from_attributes = True


class OrderBase(BaseModel):
    status: str = Field(default="Ожидает", description="Статус заявки")
    planned_start: Optional[datetime] = None
    planned_end: Optional[datetime] = None
    total_cost: float = Field(default=0, ge=0)
    final_cost: float = Field(default=0, ge=0)

class OrderCreate(OrderBase):
    client_id: int
    car_id: int
    mechanic_id: Optional[int] = None
    bay_id: Optional[int] = None

class OrderUpdate(BaseModel):
    status: Optional[str] = None
    mechanic_id: Optional[int] = None
    bay_id: Optional[int] = None
    planned_start: Optional[datetime] = None
    planned_end: Optional[datetime] = None
    total_cost: Optional[float] = None
    final_cost: Optional[float] = None

class OrderResponse(OrderBase):
    id: int
    client_id: int
    car_id: int
    mechanic_id: Optional[int]
    bay_id: Optional[int]
    created_at: datetime
    
    class Config:
        from_attributes = True


class OrderItemBase(BaseModel):
    quantity: int = Field(default=1, ge=1)
    fact_price: float = Field(..., ge=0)

class OrderItemCreate(OrderItemBase):
    service_id: int

class OrderItemResponse(OrderItemBase):
    id: int
    order_id: int
    service_id: int
    
    class Config:
        from_attributes = True


class AdminBase(BaseModel):
    full_name: str = Field(..., min_length=3, max_length=100)
    login: str = Field(..., min_length=3, max_length=50)

class AdminCreate(AdminBase):
    password: str = Field(..., min_length=6)

class AdminUpdate(BaseModel):
    full_name: Optional[str] = None
    login: Optional[str] = None

class AdminResponse(AdminBase):
    id: int
    
    class Config:
        from_attributes = True

class CallbackRequestBase(BaseModel):
    client_name: str = Field(..., min_length=2, max_length=100)
    phone: str = Field(..., pattern=r"^\+?[0-9]{10,15}$")

class CallbackRequestCreate(CallbackRequestBase):
    pass

class CallbackRequestUpdate(BaseModel):
    status: Optional[str] = None

class CallbackRequestResponse(CallbackRequestBase):
    id: int
    status: str
    created_at: datetime
    
    class Config:
        from_attributes = True


class Token(BaseModel):
    """Схема для возврата JWT-токена после успешного входа."""
    access_token: str
    token_type: str = "bearer"

class TokenData(BaseModel):
    """Схема для данных внутри токена."""
    user_id: Optional[int] = None
    user_type: Optional[str] = None  # "client", "mechanic", "admin"

class LoginRequest(BaseModel):
    """Схема для запроса на вход."""
    login: str = Field(..., description="Email/телефон для клиента, логин для мастера/админа")
    password: str = Field(..., min_length=6, description="Пароль")