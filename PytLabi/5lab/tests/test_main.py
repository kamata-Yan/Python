from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_create_task():
    response = client.post("/tasks/", json={"id": 1, "title": "Test Task"})
    assert response.status_code == 200
    assert response.json()["title"] == "Test Task"

def test_get_tasks():
    response = client.get("/tasks/")
    assert response.status_code == 200

def test_get_task():
    client.post("/tasks/", json={"id": 2, "title": "Test Task 2"})
    response = client.get("/tasks/2")
    assert response.status_code == 200
    assert response.json()["title"] == "Test Task 2"

def test_update_task():
    client.post("/tasks/", json={"id": 3, "title": "Test Task 3"})
    response = client.put("/tasks/3", json={"id": 3, "title": "Updated Task 3", "completed": True})
    assert response.status_code == 200
    assert response.json()["title"] == "Updated Task 3"

def test_delete_task():
    client.post("/tasks/", json={"id": 4, "title": "Test Task 4"})
    response = client.delete("/tasks/4")
    assert response.status_code == 200
