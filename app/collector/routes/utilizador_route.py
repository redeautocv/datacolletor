import time  
import json
from datetime import datetime

import yaml 
import requests
from flask import request
from flask import jsonify  

from   app.collector.services.service import Collect
from  app.collector.services.service_ai import extraction_AI_content_user
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
               
               print (dados_user)
     
     except Exception as e :
          print("Erro aqui é isto aqui", e)   
     

     #create(data_json)
     #resposta = requests.post("http://localhost:5001/received-data", json=data_json)
     return jsonify({"status": "coleta iniciada com sucesso"})  # resposta HTTP
     
 
@app.route("/utilizador-ia")
def data_collect__user_ia():
     colection = Collect()
     config_link = colection.config_file()
     sites = config_link['sites']  
     try :              
            for site in sites:
               dados__annouct = extraction_AI_content_user(site)
               time.sleep(120)

               dados__annouct = json.loads(dados__annouct)
               print (dados__annouct)
            
     except Exception as e :
          print("Erro aqui é isto aqui", e)   
    

     #create(data_json)
     #resposta = requests.post("http://localhost:5001/received-data", json=data_json)

     return jsonify({"status": "coleta iniciada com sucesso"})  # resposta HTTP
    