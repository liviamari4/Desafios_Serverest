import requests
from helpers import BASE_URL


def test_listar_produtos():
    response = requests.get(f"{BASE_URL}/produtos")
    assert response.status_code == 200
    assert "produtos" in response.json()


def test_cadastrar_produto_admin(token_admin):
    headers = {"Authorization": token_admin}

    payload = {
        "nome": f"Produto {uuid.uuid4().hex[:6]}",
        "preco": 100,
        "descricao": "Produto teste",
        "quantidade": 10
    }

    response = requests.post(
        f"{BASE_URL}/produtos",
        json=payload,
        headers=headers
    )

    assert response.status_code == 201
    assert "_id" in response.json()
    assert response.json()["message"] == "Cadastro realizado com sucesso"


def test_cadastrar_produto_sem_token():
    payload = {
        "nome": f"Produto {uuid.uuid4().hex[:6]}",
        "preco": 100,
        "descricao": "Produto teste",
        "quantidade": 10
    }

    response = requests.post(f"{BASE_URL}/produtos", json=payload)

    assert response.status_code == 401


def test_buscar_produto_por_id(token_admin):
    headers = {"Authorization": token_admin}

    payload = {
        "nome": f"Produto {uuid.uuid4().hex[:6]}",
        "preco": 100,
        "descricao": "Produto teste",
        "quantidade": 10
    }

    criado = requests.post(
        f"{BASE_URL}/produtos",
        json=payload,
        headers=headers
    )
    assert criado.status_code == 201, f"Falha ao criar produto: {criado.text}"

    produto_id = criado.json()["_id"]

    response = requests.get(f"{BASE_URL}/produtos/{produto_id}")

    assert response.status_code == 200
    assert "_id" in response.json()

def test_buscar_produto_id_invalido():
    response = requests.get(f"{BASE_URL}/produtos/id_invalido")

    assert response.status_code == 400


def test_atualizar_produto(token_admin):
    headers = {"Authorization": token_admin}

    payload = {
        "nome": f"Produto {uuid.uuid4().hex[:6]}",
        "preco": 100,
        "descricao": "Produto teste",
        "quantidade": 10
    }

    criado = requests.post(
        f"{BASE_URL}/produtos",
        json=payload,
        headers=headers
    )
    assert criado.status_code == 201, f"Falha ao criar produto: {criado.text}"

    produto_id = criado.json()["_id"]

    payload_atualizado = {
        "nome": f"Produto Atualizado {uuid.uuid4().hex[:4]}",
        "preco": 200,
        "descricao": "Descricao atualizada",
        "quantidade": 20
    }

    response = requests.put(
        f"{BASE_URL}/produtos/{produto_id}",
        json=payload_atualizado,
        headers=headers
    )

    assert response.status_code == 200
    assert "message" in response.json()
    assert response.json()["message"] == "Registro alterado com sucesso"


def test_excluir_produto(token_admin):
    headers = {"Authorization": token_admin}

    payload = {
        "nome": f"Produto {uuid.uuid4().hex[:6]}",
        "preco": 100,
        "descricao": "Produto teste",
        "quantidade": 10
    }

    criado = requests.post(
        f"{BASE_URL}/produtos",
        json=payload,
        headers=headers
    )
    assert criado.status_code == 201, f"Falha ao criar produto: {criado.text}"

    produto_id = criado.json()["_id"]

    response = requests.delete(
        f"{BASE_URL}/produtos/{produto_id}",
        headers=headers
    )

    assert response.status_code == 200
    assert "message" in response.json()
    assert response.json()["message"] == "Registro excluído com sucesso"