from datetime import datetime
from uuid import UUID

from pydantic import BaseModel, EmailStr


class UserCreate(BaseModel):
    username: str
    email: EmailStr
    password: str


class UserOut(BaseModel):
    id: UUID
    username: str
    email: EmailStr
    created_at: datetime

    class Config:
        orm_mode = True


class BookCreate(BaseModel):
    title: str
    description: str
    price: float
    author: str
    category: str
    stock: int


class BookOut(BookCreate):
    id: UUID

    class Config:
        orm_mode = True
