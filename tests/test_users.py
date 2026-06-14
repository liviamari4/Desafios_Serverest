import requests
import uuid

BASE_URL = "https://compassuol.serverest.dev"


def generate_email():
    return f"user_{uuid.uuid4().hex}@test.com"

def test_listar_usuarios():
    response = requests.get(f"{BASE_URL}/usuarios")

    assert response.status_code == 200
    assert "usuarios" in response.json()

def test_cadastrar_usuario_valido():
    payload = {
        "nome": "Livia Teste",
        "email": generate_email(),
        "password": "123456",
        "administrador": "true"
    }
    response = requests.post(f"{BASE_URL}/usuarios", json=payload)

    assert response.status_code == 201
    assert "_id" in response.json()
    assert response.json()["message"] == "Cadastro realizado com sucesso"

def test_cadastrar_email_duplicado():
    payload = {
        "nome": "User Teste",
        "email": generate_email(),
        "password": "123456",
        "administrador": "true"
    }

    requests.post(f"{BASE_URL}/usuarios", json=payload)

    response = requests.post(f"{BASE_URL}/usuarios", json=payload)

    assert response.status_code == 400

def test_cadastrar_campos_faltando():
    payload = {
        "nome": "User Teste",
        "email": generate_email()
    }

    response = requests.post(f"{BASE_URL}/usuarios", json=payload)

    assert response.status_code == 400

def test_buscar_usuario():
    payload = {
        "nome": "user test",
        "email": generate_email(),
        "password": "123456",
        "administrador": "true"
    }

    criado = requests.post(f"{BASE_URL}/usuarios", json=payload)
    user_id = criado.json()["_id"]

    response = requests.get(f"{BASE_URL}/usuarios/{user_id}")

    assert response.status_code == 200
    assert "_id" in response.json()

def test_buscar_usuario_id_invalido():
    response = requests.get(f"{BASE_URL}/usuarios/id_que_nao_existe")

    assert response.status_code == 400

def test_atualizar_usuario():
   
    payload = {
        "nome": "User Teste",
        "email": generate_email(),
        "password": "123456",
        "administrador": "true"
    }
    criado = requests.post(f"{BASE_URL}/usuarios", json=payload)
    user_id = criado.json()["_id"]

    payload_atualizado = {
        "nome": "User Atualizado",
        "email": generate_email(),
        "password": "123456",
        "administrador": "true"
    }
    response = requests.put(f"{BASE_URL}/usuarios/{user_id}", json=payload_atualizado)

    assert response.status_code == 200
    assert "message" in response.json()
    assert response.json()["message"] == "Registro alterado com sucesso"
    
def test_excluir_usuario():

    payload = {
        "nome": "User Teste",
        "email": generate_email(),
        "password": "123456",
        "administrador": "true"
    }
    criado = requests.post(f"{BASE_URL}/usuarios", json=payload)
    user_id = criado.json()["_id"]

    response = requests.delete(f"{BASE_URL}/usuarios/{user_id}")

    assert response.status_code == 200
    assert "message" in response.json()
    assert response.json()["message"] == "Registro excluído com sucesso"

def test_cadastrar_email_invalido():
    payload = {
        "nome": "User Teste",
        "email": "emailsemarroba.com",
        "password": "123456",
        "administrador": "true"
    }
    response = requests.post(f"{BASE_URL}/usuarios", json=payload)

    assert response.status_code == 400

def test_cadastrar_nome_vazio():
    payload = {
        "nome": "",
        "email": generate_email(),
        "password": "123456",
        "administrador": "true"
    }
    response = requests.post(f"{BASE_URL}/usuarios", json=payload)

    assert response.status_code == 400
    
    