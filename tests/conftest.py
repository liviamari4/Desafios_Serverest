import pytest
import requests
import uuid

BASE_URL = "https://compassuol.serverest.dev"


def generate_email():
    return f"user_{uuid.uuid4().hex}@test.com"


@pytest.fixture
def token_admin():
    payload = {
        "nome": "Admin Teste",
        "email": generate_email(),
        "password": "123456",
        "administrador": "true"
    }

    requests.post(f"{BASE_URL}/usuarios", json=payload)

    login = {
        "email": payload["email"],
        "password": payload["password"]
    }

    response = requests.post(f"{BASE_URL}/login", json=login)

    assert response.status_code == 200, "Falha ao fazer login do admin"

    return response.json()["authorization"]