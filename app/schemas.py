"""Pydantic schemas for API input/output models in the Bookstore application."""

from datetime import datetime
from uuid import UUID
from typing import List

from pydantic import BaseModel, EmailStr


class UserCreate(BaseModel):
    """Schema for registering a new user."""
    username: str
    email: EmailStr
    password: str


class UserOut(BaseModel):
    """Schema for returning user info."""
    id: UUID
    username: str
    email: EmailStr
    created_at: datetime

    class Config:
        from_attributes = True


class Token(BaseModel):
    """Schema for JWT access token."""
    access_token: str
    token_type: str


class UserLogin(BaseModel):
    """Schema for user login credentials."""
    email: EmailStr
    password: str


class BookBase(BaseModel):
    """Base schema for book data."""
    title: str
    description: str
    price: float
    author: str
    category: str
    stock: int


class BookCreate(BookBase):
    """Schema for creating a book."""
    pass


class BookUpdate(BookBase):
    """Schema for updating a book."""
    pass


class BookOut(BookBase):
    """Schema for returning book data."""
    id: UUID

    class Config:
        from_attributes = True


class OrderItemCreate(BaseModel):
    """Schema for a book item inside an order (input)."""
    book_id: UUID
    quantity: int


class OrderCreate(BaseModel):
    """Schema for creating a new order."""
    items: List[OrderItemCreate]


class OrderItemOut(OrderItemCreate):
    """Schema for an order item (output with nested book info)."""
    id: UUID
    book: BookOut

    class Config:
        from_attributes = True


class OrderOut(BaseModel):
    """Schema for returning an order with items."""
    id: UUID
    created_at: datetime
    status: str
    items: List[OrderItemOut]

    class Config:
        from_attributes = True
