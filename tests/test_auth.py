import uuid as uuid

from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)

user_id = str(uuid.uuid4())


def test_register_user():
    response = client.post("/auth/register", json={
        "username": user_id,
        "email": user_id + "@example.com",
        "password": "testpass"
    })
    assert response.status_code == 200
    assert response.json()["email"] == user_id + "@example.com"


def test_login_user():
    response = client.post("/auth/login", json={
        "email": user_id + "@example.com",
        "password": "testpass"
    })
    assert response.status_code == 200
    assert "access_token" in response.json()
