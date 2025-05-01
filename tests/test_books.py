import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

book_data = {
    "title": "Test Book",
    "description": "A test book description",
    "price": 9.99,
    "author": "Author Test",
    "category": "Testing",
    "stock": 5
}

def test_create_book():
    response = client.post("/books/", json=book_data)
    assert response.status_code == 200
    global book_id
    book_id = response.json()["id"]

def test_get_books():
    response = client.get("/books/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_get_single_book():
    response = client.get(f"/books/{book_id}")
    assert response.status_code == 200
    assert response.json()["title"] == book_data["title"]

def test_update_book():
    response = client.put(f"/books/{book_id}", json={
        **book_data, "price": 19.99
    })
    assert response.status_code == 200
    assert response.json()["price"] == 19.99

def test_delete_book():
    response = client.delete(f"/books/{book_id}")
    assert response.status_code == 200
