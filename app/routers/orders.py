from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from uuid import UUID
from .. import crud, schemas, models
from ..database import get_db
from ..deps import get_current_user
from typing import List

router = APIRouter(prefix="/orders", tags=["Orders"])

@router.post("/", response_model=schemas.OrderOut)
def create_order(
    order: schemas.OrderCreate,
    db: Session = Depends(get_db),
    user: models.User = Depends(get_current_user)
):
    return crud.create_order(db, user.id, order.items)

@router.get("/me", response_model=List[schemas.OrderOut])
def get_my_orders(
    db: Session = Depends(get_db),
    user: models.User = Depends(get_current_user)
):
    return crud.get_orders_by_user(db, user.id)
