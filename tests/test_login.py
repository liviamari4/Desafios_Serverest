import requests
import uuid
from helpers import BASE_URL, generate_email


def test_login_valido():
    payload = {
        "nome": "User Teste",
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

    assert response.status_code == 200
    assert "authorization" in response.json()


def test_login_senha_errada():
    payload = {
        "nome": "User Teste",
        "email": generate_email(),
        "password": "123456",
        "administrador": "true"
    }

    requests.post(f"{BASE_URL}/usuarios", json=payload)

    login = {
        "email": payload["email"],
        "password": "senhaerrada"
    }

    response = requests.post(f"{BASE_URL}/login", json=login)

    assert response.status_code == 401


def test_login_email_inexistente():
    login = {
        "email": generate_email(),
        "password": "123456"
    }

    response = requests.post(f"{BASE_URL}/login", json=login)

    assert response.status_code == 401


def test_login_campos_vazios():
    login = {
        "email": "",
        "password": ""
    }

    response = requests.post(f"{BASE_URL}/login", json=login)

    assert response.status_code == 400