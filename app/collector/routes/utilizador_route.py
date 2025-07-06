import time  
import json
from datetime import datetime

import yaml 
import requests
from flask import request
from flask import jsonify  

from   app.collector.services.service import Collect
from  app.collector.services.service_ai import CollectIA
from schema import Anuncio
from schema import Utilizador
from schema import Avaliacao
from ... import  dbt 
from  app.collector.models.collector import  DataCollector
from  ...app import app

@app.route("/utilizador")
def data_collect_user():
     colection = Collect()
     config_link = colection.config_file()
     sites = config_link['sites'] 
        
     data_json_user = []   
     try :  
          for site in sites: 
               url_user = site['utilizador']['link_offline'] 
        
               #tree_html_announcement, tree_html_location = colection._request_http()
               tree_html_user = colection._request_http_offline(url_user)

               dados_user = colection.extraction_content_user(tree_html_user, site)  
                            
               data_json_user.append(dados_user)
     
     except Exception as e :
          print("Erro aqui é isto aqui", e)   
     
     print(len(data_json_user))
     print(data_json_user)
     #create(data_json)
     #resposta = requests.post("http://localhost:5001/received-data", json=data_json_user)
     return jsonify({"status": "coleta iniciada com sucesso"})  # resposta HTTP
     
 
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
                 dado = colecao.format_data_user(user)
                 data_json_user.append(dado)  
             time.sleep(120)

     except Exception as e :
          print("Erro aqui é isto aqui", e)   
     
     print (len(data_json_user))
     print (data_json_user)
        

     #create(data_json)
     #resposta = requests.post("http://localhost:5001/received-data", json=data_json)

     return jsonify({"status": "coleta iniciada com sucesso"})  # resposta HTTP
