from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

from app import schemas, crud
from app.database import engine, SessionLocal, Base

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Bookstore API")


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/users/", response_model=schemas.UserOut)
def register_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    return crud.create_user(db, user)


@app.get("/books/", response_model=list[schemas.BookOut])
def list_books(db: Session = Depends(get_db)):
    return crud.get_books(db)


@app.post("/books/", response_model=schemas.BookOut)
def create_book(book: schemas.BookCreate, db: Session = Depends(get_db)):
    return crud.create_book(db, book)
