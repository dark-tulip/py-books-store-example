from fastapi import FastAPI
from starlette.testclient import TestClient

app = FastAPI()

@app.get("/")
def read_root():
    return {"msg": "Hello"}

def test_root():
    client = TestClient(app)
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"msg": "Hello"}
