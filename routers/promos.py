import logging
from typing import Optional

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

import crud
import schemas
from database import get_db

logger = logging.getLogger(__name__)

router = APIRouter(prefix="/promos", tags=["Promos"])


# GET /promos — список с фильтром и пагинацией
@router.get("/", response_model=list[schemas.PromoOut])
def list_promos(
    is_active: Optional[bool] = None,
    skip: int = 0,
    limit: int = 20,
    db: Session = Depends(get_db)
):
    return crud.get_promos(db, is_active=is_active, skip=skip, limit=limit)


# GET /promos/{promo_id} — один промокод или 404
@router.get("/{promo_id}", response_model=schemas.PromoOut)
def get_promo(promo_id: int, db: Session = Depends(get_db)):
    promo = crud.get_promo(db, promo_id)
    if not promo:
        raise HTTPException(status_code=404, detail="Promo not found")
    return promo


# POST /promos — создание, статус 201
@router.post("/", response_model=schemas.PromoOut,
             status_code=status.HTTP_201_CREATED)
def create_promo(data: schemas.PromoCreate,
                 db: Session = Depends(get_db)):
    logger.info(f"Creating promo: {data.code}")
    return crud.create_promo(db, data)


# PUT /promos/{promo_id} — обновление
@router.put("/{promo_id}", response_model=schemas.PromoOut)
def update_promo(promo_id: int, data: schemas.PromoUpdate,
                 db: Session = Depends(get_db)):
    promo = crud.update_promo(db, promo_id, data)
    if not promo:
        raise HTTPException(status_code=404, detail="Promo not found")
    return promo


# DELETE /promos/{promo_id} — удаление, статус 204
@router.delete("/{promo_id}",
               status_code=status.HTTP_204_NO_CONTENT)
def delete_promo(promo_id: int, db: Session = Depends(get_db)):
    if not crud.delete_promo(db, promo_id):
        raise HTTPException(status_code=404, detail="Promo not found")


# POST /promos/apply — применить промокод к корзине
@router.post("/apply", response_model=schemas.ApplyResponse)
def apply_promo(data: schemas.ApplyRequest,
                db: Session = Depends(get_db)):
    promo = crud.get_promo_by_code(db, data.code.upper())
    if not promo or not promo.is_active:
        logger.warning(f"Invalid promo attempt: {data.code}")
        raise HTTPException(status_code=400,
                            detail="Promo not found or inactive")
    saved = round(data.initial_cart_sum * promo.discount_percent / 100, 2)
    final_sum = round(data.initial_cart_sum - saved, 2)
    logger.info(f"Applied {promo.code}: saved {saved}")
    return {"final_sum": final_sum, "saved": saved}