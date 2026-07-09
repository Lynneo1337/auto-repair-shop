from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from .. import models, schemas
from ..database import get_db

router = APIRouter(
    prefix="/discount-rules",
    tags=["Правила скидок"]
)

@router.post("/", response_model=schemas.DiscountRuleResponse, status_code=status.HTTP_201_CREATED)
def create_discount_rule(rule: schemas.DiscountRuleCreate, db: Session = Depends(get_db)):
    """Создаёт новое правило начисления скидок."""
    db_rule = models.DiscountRule(**rule.dict())
    db.add(db_rule)
    db.commit()
    db.refresh(db_rule)
    return db_rule

@router.get("/", response_model=List[schemas.DiscountRuleResponse])
def get_discount_rules(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """Возвращает список всех правил скидок."""
    return db.query(models.DiscountRule).offset(skip).limit(limit).all()

@router.get("/{rule_id}", response_model=schemas.DiscountRuleResponse)
def get_discount_rule(rule_id: int, db: Session = Depends(get_db)):
    """Возвращает информацию о правиле по ID."""
    db_rule = db.query(models.DiscountRule).filter(models.DiscountRule.id == rule_id).first()
    if not db_rule:
        raise HTTPException(status_code=404, detail="Правило не найдено")
    return db_rule

@router.put("/{rule_id}", response_model=schemas.DiscountRuleResponse)
def update_discount_rule(rule_id: int, rule: schemas.DiscountRuleUpdate, db: Session = Depends(get_db)):
    """Обновляет данные правила."""
    db_rule = db.query(models.DiscountRule).filter(models.DiscountRule.id == rule_id).first()
    if not db_rule:
        raise HTTPException(status_code=404, detail="Правило не найдено")
    
    update_data = rule.dict(exclude_unset=True)
    for key, value in update_data.items():
        setattr(db_rule, key, value)
    
    db.commit()
    db.refresh(db_rule)
    return db_rule

@router.delete("/{rule_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_discount_rule(rule_id: int, db: Session = Depends(get_db)):
    """Удаляет правило."""
    db_rule = db.query(models.DiscountRule).filter(models.DiscountRule.id == rule_id).first()
    if not db_rule:
        raise HTTPException(status_code=404, detail="Правило не найдено")
    
    db.delete(db_rule)
    db.commit()
    return None