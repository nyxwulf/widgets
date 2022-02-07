# Simple stub for adding more tests

from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


def test_list_widgets():
    response = client.get("/widgets")
    assert response.status_code == 200


def test_read_bad_url():
    response = client.get("/widgets/asdf")
    assert response.status_code == 422

