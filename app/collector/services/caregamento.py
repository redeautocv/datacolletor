import requests

class Carregamento:
    def __init__(self):
        
        pass
    
    def criar_anunciante(self, anunciante):
        reposta =requests.post("http://localhost:5002/utilizador", json=anunciante.to_dict())
        if reposta.status_code < 200 and reposta.status_code > 299 :
            print ( f'Erro na criação de Anunciante:{anunciante= } {reposta.text=} {reposta.status_code=}')
        else:
            print(f'{reposta.json()= }')
            return {"status_code":reposta.status_code, 'anunciante': reposta.json(),}
    
    def criar_anuncio(self, anunciante, anuncios):
        id_anunciante = anunciante["id_anunciante"]
        
        for anuncio in anuncios:
            anuncio["id_anunciante"]= id_anunciante     
        
        reposta = requests.post("http://localhost:5003/anuncio", json=anuncios)
        
        if reposta.status_code < 200 and reposta.status_code > 299 :
            print ( f'Erro na criação de Anuncios:{anuncios= } {reposta.text=} {reposta.status_code=}')
        else:
            print(f'{reposta.json()= }')
            return {"status_code":reposta.status_code, 'anuncios': reposta.json()}
