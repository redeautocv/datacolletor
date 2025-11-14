import time  
import json
import traceback
from datetime import datetime

import yaml 
import requests
from flask import request
from flask import jsonify  
from pprint import pprint

from ... import  dbt 
from  ...app import app
from   app.collector.services.service import Collect
from   app.collector.services.caregamento import Carregamento
from  app.collector.services.service_ai import CollectIA
from  app.collector.models.anunciante import  Anunciante
from app.collector.models.anunciante import Anunciante
from app.collector.models.anuncio import Anuncio  
from app.collector.models.autenticacao import Autenticacao
     

@app.route("/utilizador")
def data_collect_user():
     colection = Collect()
     carregamento = Carregamento()
     config_link = colection.config_file()
     sites = config_link['sites'] 
     lista_anuncios = []   
     dados_anunciante =  {}   

     try :  
          for site in sites: 
               url_anunciante = site['anunciante']['link_local'] 
               url_anuncio = site['anuncio']['link_local'] 
               """ requisicão http online"""
               #tree_html_announcement, tree_html_location = colection._request_http()
               #tree_html_announcement, tree_html_location = colection._request_http()

               arvore_html = colection._request_http_offline(url_anunciante)
               dados_anunciante = colection.extraction_content_user(arvore_html, site)  
               
                
               arvore_html_anuncios = colection._request_http_offline(url_anuncio)
               numero_anuncios = colection.extraction_number_annouct(arvore_html_anuncios, site)
               
               for indice in range(numero_anuncios): 
                   dados_anuncios = colection.extraction_content_annouct(arvore_html_anuncios, site, indice)
                   lista_anuncios.append(dados_anuncios.to_dict())

               #resposta_estado = carregamento.verificar_estado_base_dados()
               #resposta_unicidade = carregamento.verificar_unicidade_base_dados(dados_anunciante.to_dict())
               resposta_anunciante = carregamento.criar_anunciante(dados_anunciante)
               print(f'-----------------------------') 
               resposta_anuncios = carregamento.criar_anuncio(anunciante=resposta_anunciante['anunciante'], anuncios=lista_anuncios) 


               
                       
               lista_anuncios.pop()    
                               
     except Exception as e :
          print("Erro aqui é isto aqui", e.__traceback__)
          traceback.print_exc()   
     
     #create(data_json)

     return jsonify({"status": "coleta com sucesso"})  # resposta HTTP

@app.route("/utilizador-ia")
def data_collect__user_ia():
     colection = Collect()
     colecao = CollectIA()
     config_link = colection.config_file()
     sites = config_link['sites']
     data_json_user = []   

     try:              
         for site in sites:
             users  = colecao.extraction_AI_content_user(site)
             print ("---",users)
             for user in users:
               dado = colecao.format_data_user(users)
               data_json_user.append(dado)  
               time.sleep(120)

     except Exception as e :
          print("Erro aqui é isto aqui", e)   
     
     print (len(data_json_user))
     print (data_json_user)
        

     #create(data_json)
     #resposta = requests.post("http://localhost:5001/received-data", json=data_json)

     return jsonify({"status": "coleta iniciada com sucesso"})  # resposta HTTP
