"""CRUD operations for books, users, and orders in the Bookstore API."""

from typing import List
from uuid import UUID

from sqlalchemy.orm import Session

from . import models, schemas


def get_book(db: Session, book_id: UUID):
    """Retrieve a book by its ID."""
    return db.query(models.Book).filter(models.Book.id == book_id).first()


def get_books(db: Session, skip: int = 0, limit: int = 10):
    """Retrieve a list of books with pagination."""
    return db.query(models.Book).offset(skip).limit(limit).all()


def create_book(db: Session, book: schemas.BookCreate):
    """Create a new book in the database."""
    db_book = models.Book(**book.model_dump())
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book


def update_book(db: Session, book_id: UUID, book: schemas.BookUpdate):
    """Update an existing book by its ID."""
    db_book = get_book(db, book_id)
    if db_book:
        for key, value in book.model_dump().items():
            setattr(db_book, key, value)
        db.commit()
        db.refresh(db_book)
    return db_book


def delete_book(db: Session, book_id: UUID):
    """Delete a book from the database by its ID."""
    db_book = get_book(db, book_id)
    if db_book:
        db.delete(db_book)
        db.commit()
    return db_book


def create_order(db: Session, user_id: UUID, items: List[schemas.OrderItemCreate]):
    """Create a new order with associated items."""
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
    """Get all orders made by a specific user."""
    return db.query(models.Order).filter(models.Order.user_id == user_id).all()
