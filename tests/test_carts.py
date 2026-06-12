import requests

BASE_URL = "https://compassuol.serverest.dev"

def test_listar_carrinhos():
    response = requests.get(f"{BASE_URL}/carrinhos")

    assert response.status_code == 200
    assert "carrinhos" in response.json()


def test_buscar_carrinho_id_invalido():
    response = requests.get(f"{BASE_URL}/carrinhos/id_invalido")

    assert response.status_code == 400