from fastapi import FastAPI
from app.database import Base, engine, SessionLocal

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Bookstore API")

from app.routers import books, auth, users

app.include_router(books.router)
app.include_router(auth.router)
app.include_router(users.router)



# @app.post("/users/", response_model=schemas.UserOut)
# def register_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
#     return crud.create_user(db, user)
#
#
# @app.get("/books/", response_model=list[schemas.BookOut])
# def list_books(db: Session = Depends(get_db)):
#     return crud.get_books(db)
#
#
# @app.post("/books/", response_model=schemas.BookOut)
# def create_book(book: schemas.BookCreate, db: Session = Depends(get_db)):
#     return crud.create_book(db, book)
