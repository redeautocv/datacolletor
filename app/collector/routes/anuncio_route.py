import time  
import json
from datetime import datetime

import yaml 
import requests
from flask import request
from flask import jsonify  

from   app.collector.services.service import Collect
from  app.collector.services.service_ai import extraction_AI_content_annouct
from schema import Anuncio
from schema import Utilizador
from schema import Avaliacao
from ... import  dbt 
from  app.collector.models.collector import  DataCollector
from  ...app import app

@app.route("/anuncio")
def data_collect_anuncio():
     colection = Collect()
     config_link = colection.config_file()
     sites = config_link['sites'] 
     data_json_annouct = []   

     try :  
          for site in sites: 
               url_announcement = site['anuncio']['link_offline'] 
        
               #tree_html_announcement, tree_html_location = colection._request_http()
               tree_html_announcement = colection._request_http_offline(url_announcement)

               numero_anuncios = colection.extraction_number_annouct(tree_html_announcement, site)

               for indice in range(numero_anuncios): 
                   dados__annouct = colection.extraction_content_annouct(tree_html_announcement, site, indice)
                   data_json_annouct.append(dados__annouct)  
           
          
     except Exception as e :
          print("Erro aqui é isto aqui", e)   
     print(dados__annouct)
     #response =requests.get("http://localhost:5001/listings")
     
     #create(data_json)
     #resposta = requests.post("http://localhost:5001/listings", json=data_json_annouct)
     return jsonify({"status": "coleta com sucesso"})  # resposta HTTP
     
 
@app.route("/anuncio-ia")
def data_collect_anuncio_ia():
     colection = Collect()
     config_link = colection.config_file()
     sites = config_link['sites']  
     data_json_annouct = []   
     
     try :
         for site in sites:               
             dados_annouct = extraction_AI_content_annouct(site)
             time.sleep(120)

             dados_json = json.loads(dados_annouct)
             data_json_annouct.append(dados_json)   
             

     except Exception as e :
          print("Erro aqui é isto aqui", e)   
     print ("--------------------------")
     print (len(data_json_annouct))
     print ("--------------------------")
     print (data_json_annouct)
     
     #create(data_json)
     #resposta = requests.post("http://localhost:5001/received-data", json=data_json)

     return jsonify({"status": "coleta iniciada com sucesso"})  # resposta HTTP
    