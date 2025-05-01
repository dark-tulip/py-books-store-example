# routers/users.py

from fastapi import APIRouter, Depends
from ..deps import get_current_user
from .. import schemas, models

router = APIRouter(prefix="/users", tags=["Users"])

@router.get("/me", response_model=schemas.UserOut)
def read_current_user(current_user: models.User = Depends(get_current_user)):
    return current_user
