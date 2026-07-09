from sqlalchemy import Column, Integer, String, Numeric, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from .database import Base

class Client(Base):
    __tablename__ = "clients"
    
    id = Column(Integer, primary_key=True, index=True)
    full_name = Column(String, nullable=False)
    phone = Column(String, unique=True, nullable=False)
    email = Column(String, unique=True, nullable=False)
    password_hash = Column(String, nullable=False)
    visit_count = Column(Integer, default=0)
    current_discount = Column(Numeric(5, 2), default=0.0)
    
    cars = relationship("Car", back_populates="client")
    orders = relationship("Order", back_populates="client")

class Car(Base):
    __tablename__ = "cars"
    
    id = Column(Integer, primary_key=True, index=True)
    client_id = Column(Integer, ForeignKey("clients.id"))
    brand_model = Column(String, nullable=False)
    license_plate = Column(String, nullable=False)
    vin = Column(String, unique=True, nullable=False)
    
    client = relationship("Client", back_populates="cars")
    orders = relationship("Order", back_populates="car")

class Service(Base):
    __tablename__ = "services"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    price = Column(Numeric(10, 2), nullable=False)
    req_specialization = Column(String, nullable=False)

class Mechanic(Base):
    __tablename__ = "mechanics"
    
    id = Column(Integer, primary_key=True, index=True)
    full_name = Column(String, nullable=False)
    specialization = Column(String, nullable=False)
    login = Column(String, unique=True, nullable=False)
    password_hash = Column(String, nullable=False)

class Bay(Base):
    __tablename__ = "bays"
    
    id = Column(Integer, primary_key=True, index=True)
    number = Column(String, nullable=False)
    capacity = Column(Integer, default=2)

class Order(Base):
    __tablename__ = "orders"
    
    id = Column(Integer, primary_key=True, index=True)
    client_id = Column(Integer, ForeignKey("clients.id"))
    car_id = Column(Integer, ForeignKey("cars.id"))
    mechanic_id = Column(Integer, ForeignKey("mechanics.id"), nullable=True)
    bay_id = Column(Integer, ForeignKey("bays.id"), nullable=True)
    status = Column(String, default="Ожидает")
    planned_start = Column(DateTime, nullable=True)
    planned_end = Column(DateTime, nullable=True)
    total_cost = Column(Numeric(10, 2), default=0)
    final_cost = Column(Numeric(10, 2), default=0)
    created_at = Column(DateTime, default=datetime.utcnow)

    client = relationship("Client", back_populates="orders")
    car = relationship("Car", back_populates="orders")
    items = relationship("OrderItem", back_populates="order")

class OrderItem(Base):
    __tablename__ = "order_items"
    
    id = Column(Integer, primary_key=True, index=True)
    order_id = Column(Integer, ForeignKey("orders.id"))
    service_id = Column(Integer, ForeignKey("services.id"))
    quantity = Column(Integer, default=1)
    fact_price = Column(Numeric(10, 2))

    order = relationship("Order", back_populates="items")
    service = relationship("Service")