import pytest
import requests
from helpers import BASE_URL, generate_email


@pytest.fixture
def token_admin():
    payload = {
        "nome": "Admin Teste",
        "email": generate_email(),
        "password": "123456",
        "administrador": "true"
    }

    r = requests.post(f"{BASE_URL}/usuarios", json=payload)
    assert r.status_code == 201, f"Falha ao criar usuário admin: {r.text}"
    user_id = r.json()["_id"]

    login = {
        "email": payload["email"],
        "password": payload["password"]
    }

    response = requests.post(f"{BASE_URL}/login", json=login)
    assert response.status_code == 200, "Falha ao fazer login do admin"

    yield response.json()["authorization"]

    # Teardown: remove o usuário admin criado
    requests.delete(f"{BASE_URL}/usuarios/{user_id}")