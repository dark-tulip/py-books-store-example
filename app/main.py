from fastapi import FastAPI
from app.database import Base, engine, SessionLocal

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Bookstore API")

from app.routers import books, auth, users,orders

app.include_router(books.router)
app.include_router(auth.router)
app.include_router(users.router)
app.include_router(orders.router)
