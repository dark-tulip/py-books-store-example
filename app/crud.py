# crud.py

from uuid import UUID

from sqlalchemy.orm import Session

from . import models, schemas
from typing import List


def get_book(db: Session, book_id: UUID):
    return db.query(models.Book).filter(models.Book.id == book_id).first()


def get_books(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Book).offset(skip).limit(limit).all()


def create_book(db: Session, book: schemas.BookCreate):
    db_book = models.Book(**book.dict())
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book


def update_book(db: Session, book_id: UUID, book: schemas.BookUpdate):
    db_book = get_book(db, book_id)
    if db_book:
        for key, value in book.dict().items():
            setattr(db_book, key, value)
        db.commit()
        db.refresh(db_book)
    return db_book


def delete_book(db: Session, book_id: UUID):
    db_book = get_book(db, book_id)
    if db_book:
        db.delete(db_book)
        db.commit()
    return db_book


def create_order(db: Session, user_id: UUID, items: List[schemas.OrderItemCreate]):
    order = models.Order(user_id=user_id)
    db.add(order)
    db.flush()  # получить order.id до коммита

    for item in items:
        db_item = models.OrderItem(
            order_id=order.id,
            book_id=item.book_id,
            quantity=item.quantity
        )
        db.add(db_item)

    db.commit()
    db.refresh(order)
    return order

def get_orders_by_user(db: Session, user_id: UUID):
    return db.query(models.Order).filter(models.Order.user_id == user_id).all()
