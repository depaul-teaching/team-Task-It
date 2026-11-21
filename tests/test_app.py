
import pytest
from app import app


@pytest.fixture
def client():
    app.config["TESTING"] = True

    with app.test_client() as client:
        yield client


def test_health(client):
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json == {"status": "ok"}


def test_homepage(client):
    response = client.get("/")

    assert response.status_code == 200


def test_add_task(client):
    response = client.post(
        "/add",
        data={"task": "Test Task"},
        follow_redirects=True
    )

    assert response.status_code == 200
    assert b"Test Task" in response.data

