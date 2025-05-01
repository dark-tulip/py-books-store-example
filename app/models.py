import uuid
from datetime import datetime

from sqlalchemy import Column, String, Integer, Float, ForeignKey, DateTime
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from .database import Base


class User(Base):
    __tablename__ = "users"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)

    orders = relationship("Order", back_populates="user")


class Book(Base):
    __tablename__ = "books"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    title = Column(String)
    description = Column(String)
    price = Column(Float)
    author = Column(String)
    category = Column(String)
    stock = Column(Integer)


class Order(Base):
    __tablename__ = "orders"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id"))
    created_at = Column(DateTime, default=datetime.utcnow)
    status = Column(String, default="pending")

    user = relationship("User", back_populates="orders")
    items = relationship("OrderItem", back_populates="order")


class OrderItem(Base):
    __tablename__ = "order_items"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    order_id = Column(UUID(as_uuid=True), ForeignKey("orders.id"))
    book_id = Column(UUID(as_uuid=True), ForeignKey("books.id"))
    quantity = Column(Integer)

    order = relationship("Order", back_populates="items")
    book = relationship("Book")
