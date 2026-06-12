import requests

BASE_URL = "https://compassuol.serverest.dev"

def test_listar_produtos():
    response = requests.get(f"{BASE_URL}/produtos")

    assert response.status_code == 200
    assert "produtos" in response.json()

def test_buscar_produto_id_invalido():
    response = requests.get(f"{BASE_URL}/produtos/id_invalido")

    assert response.status_code == 400