import pytest
from fastapi.testclient import TestClient
from api import app

client = TestClient(app)


def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert "message" in response.json()


def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "healthy"


def test_calculate_addition():
    response = client.post("/calculate", json={
        "first_number": 5,
        "second_number": 3,
        "operation": "+"
    })
    assert response.status_code == 200
    assert response.json()["result"] == 8


def test_calculate_subtraction():
    response = client.post("/calculate", json={
        "first_number": 10,
        "second_number": 4,
        "operation": "-"
    })
    assert response.status_code == 200
    assert response.json()["result"] == 6


def test_calculate_multiplication():
    response = client.post("/calculate", json={
        "first_number": 6,
        "second_number": 7,
        "operation": "*"
    })
    assert response.status_code == 200
    assert response.json()["result"] == 42


def test_calculate_division():
    response = client.post("/calculate", json={
        "first_number": 20,
        "second_number": 4,
        "operation": "/"
    })
    assert response.status_code == 200
    assert response.json()["result"] == 5


def test_calculate_division_by_zero():
    response = client.post("/calculate", json={
        "first_number": 10,
        "second_number": 0,
        "operation": "/"
    })
    assert response.status_code == 400
    assert "Division by zero" in response.json()["detail"]


def test_invalid_operation():
    response = client.post("/calculate", json={
        "first_number": 5,
        "second_number": 3,
        "operation": "^"
    })
    assert response.status_code == 400


def test_calculate_returns_int_for_whole_number():
    response = client.post("/calculate", json={
        "first_number": 10,
        "second_number": 5,
        "operation": "/"
    })
    assert response.status_code == 200
    assert response.json()["result"] == 2


if __name__ == "__main__":
    pytest.main([__file__, "-v"])