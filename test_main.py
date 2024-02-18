from fastapi import FastAPI
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {
        "message": "Wikipedia API. Call /search or /wiki or /phrase"
    }


def test_read_phrase():
    response = client.get("/phrase/Ho Chi Minh")
    assert response.status_code == 200
    assert response.json() == {
        "result": [
            "hồ chí minh",
            "nguyễn sinh cung",
            "may",
            "september",
            "uncle ho",
            "bác hồ",
            "uncle",
            "bác",
        ]
    }
