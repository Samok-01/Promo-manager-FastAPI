from sqlalchemy.orm import Session
from typing import Optional
from models import Promo
from schemas import PromoCreate, PromoUpdate

def get_promo(db: Session, promo_id: int) -> Optional[Promo]:
    return db.get(Promo, promo_id)

def get_promo_by_code(db: Session, code: str) -> Optional[Promo]:
    return db.query(Promo).filter(Promo.code == code).first()

def get_promos(
    db: Session,
    is_active: Optional[bool] = None,
    skip: int = 0,
    limit: int = 20
) -> list[Promo]:
    query = db.query(Promo)
    if is_active is not None:
        query = query.filter(Promo.is_active == is_active)
    return query.offset(skip).limit(limit).all()

def create_promo(db: Session, data: PromoCreate) -> Promo:
    promo = Promo(**data.model_dump())
    db.add(promo)
    db.commit()
    db.refresh(promo)
    return promo

def update_promo(
    db: Session,
    promo_id: int,
    data: PromoUpdate
) -> Optional[Promo]:
    promo = get_promo(db, promo_id)
    if not promo:
        return None
    for field, value in data.model_dump(exclude_unset=True).items():
        setattr(promo, field, value)
    db.commit()
    db.refresh(promo)
    return promo

def delete_promo(db: Session, promo_id: int) -> bool:
    promo = get_promo(db, promo_id)
    if not promo:
        return False
    db.delete(promo)
    db.commit()
    return True