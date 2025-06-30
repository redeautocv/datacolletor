"""
import time  
import json
from datetime import datetime

import yaml 
import requests
from flask import request
from flask import jsonify  

from   app.collector.services import Collect
from  app.collector.service_ai import extraction_AI_content_user
from  app.collector.service_ai import extraction_AI_content_annouct
from schema import Anuncio
from schema import Utilizador
from schema import Avaliacao
from .. import  dbt 
from  app.collector.models.collector import  DataCollector
from  .controllers import collect,create
from  ..app import app

@app.route("/start")
def data_collect():
     colection = Collect()
     config_link = colection.config_file()
     sites = config_link['sites'] 
     data_json_annouct = []   
     data_json_user = []  
     data_json = collect() 
     try :  
          for site in sites: 
               url_user = site['utilizador']['link_offline']
               url_announcement = site['anuncio']['link_offline'] 
        
               #tree_html_announcement, tree_html_location = colection._request_http()
               tree_html_user = colection._request_http_offline(url_user)
               tree_html_announcement = colection._request_http_offline(url_announcement)

               numero_anuncios = colection.extraction_number_annouct(tree_html_announcement, site)

               for indice in range(numero_anuncios): 
                   dados__annouct = colection.extraction_content_annouct(tree_html_announcement, site, indice)
                   data_json_annouct.append(dados__annouct)
            
               dados_user = colection.extraction_content_user(tree_html_user, site)  
            
               data_json_annouct.append(dados__annouct)
               data_json_user.append(dados_user) 
             
               dados_user = json.loads(dados_user)
               dados__annouct = json.loads(dados__annouct)
    
            
            #data_json.append(dados_dict_annouct)
            #data_json.append(dados_dict_user)
    
     except Exception as e :
          print("Erro aqui é isto aqui", e)   
          print(data_json_user )
          print(data_json_annouct )
     #create(data_json)
     #resposta = requests.post("http://localhost:5001/received-data", json=data_json)
     return jsonify({"status": "coleta iniciada com sucesso"})  # resposta HTTP
     
 
@app.route("/start_AI")
def data_collect():
     colection = Collect()
     config_link = colection.config_file()
     site = config_link['sites']  
     data_json = collect() 
     
     try :              
            dados__annouct = extraction_AI_content_annouct(site)
            time.sleep(120)

            dados_user = extraction_AI_content_user(site)
            time.sleep(120)
         
            dados_user = json.loads(dados_user)
            dados__annouct = json.loads(dados__annouct)
            
     except Exception as e :
          print("Erro aqui é isto aqui", e)   

     create(data_json)
     #resposta = requests.post("http://localhost:5001/received-data", json=data_json)

     return jsonify({"status": "coleta iniciada com sucesso"})  # resposta HTTP
"""