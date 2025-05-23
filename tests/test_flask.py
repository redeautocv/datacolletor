import pytest
from src.app import create_app

@pytest.fixture
def cliente():
    app = create_app("development")  # Presuma que existe uma config 'testing'
    #app.config["TESTING"] = True 
    with app.test_client() as cliente:
        yield cliente

def test_home(cliente):
    resposta = cliente.get("/")
    assert resposta.status_code == 200
    assert resposta.data.decode("utf-8") == "Olá Mundo"

def test_received_data(cliente):
    payload = {
        "titulo": "Casa no centro",
        "descricao": "Bonita casa perto da praia"
    }
    resposta = cliente.post("/received-data", json=payload)
    assert resposta.status_code == 200
    dados = resposta.get_json()
    assert dados["message"] == "Dados recebidos com sucesso!"
    assert dados["data"] == payload
