from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def get_token():
    login = client.post("/auth/login", json={
        "email": "testuser@example.com",
        "password": "testpass"
    })
    return login.json()["access_token"]

def test_create_order():
    token = get_token()
    # Создаём книгу для заказа
    book_resp = client.post("/books/", json={
        "title": "Order Book",
        "description": "Book for order test",
        "price": 15.99,
        "author": "Tester",
        "category": "Orders",
        "stock": 3
    })
    book_id = book_resp.json()["id"]

    response = client.post("/orders/", json={
        "items": [
            {"book_id": book_id, "quantity": 2}
        ]
    }, headers={"Authorization": f"Bearer {token}"})
    assert response.status_code == 200
    assert len(response.json()["items"]) == 1

def test_get_my_orders():
    token = get_token()
    response = client.get("/orders/me", headers={"Authorization": f"Bearer {token}"})
    assert response.status_code == 200
    assert isinstance(response.json(), list)
