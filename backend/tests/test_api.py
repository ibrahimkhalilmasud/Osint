from fastapi.testclient import TestClient

from app.main import app


client = TestClient(app)


def token(role: str = "analyst") -> str:
    response = client.post("/auth/token", json={"username": "tester", "role": role})
    return response.json()["access_token"]


def test_investigation_creation_normalizes_fields() -> None:
    response = client.post(
        "/investigation",
        headers={"Authorization": f"Bearer {token()}"},
        json={
            "full_name": "Jane Doe",
            "phone_number": "+1 (415) 555-2671",
            "email_address": "Jane.Doe@example.com",
            "username": " Jane.Doe ",
            "domain": "https://Example.com/path",
            "company_name": "Example Inc",
        },
    )

    assert response.status_code == 200
    data = response.json()
    assert data["input"]["phone_number"] == "+14155552671"
    assert data["input"]["username"] == "jane.doe"
    assert data["input"]["domain"] == "example.com"


def test_viewer_cannot_create_investigation() -> None:
    response = client.post(
        "/investigation",
        headers={"Authorization": f"Bearer {token('viewer')}"},
        json={"full_name": "Jane Doe"},
    )

    assert response.status_code == 403
