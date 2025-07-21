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

@app.route("/anuncio")
def data_collect_anuncio():
     colection = Collect()
     config_link = colection.config_file()
     sites = config_link['sites'] 
     data_json_annouct = []   
     data_json_user = []
     
     try :  
          for site in sites: 
               # 
               url_announcement = site['anuncio']['link_offline'] 
               url_user = site['utilizador']['link_offline'] 
           
               #tree_html_announcement, tree_html_location = colection._request_http()
               tree_html_announcement = colection._request_http_offline(url_announcement)

               numero_anuncios = colection.extraction_number_annouct(tree_html_announcement, site)
     
               for indice in range(numero_anuncios): 
                   dados__annouct = colection.extraction_content_annouct(tree_html_announcement, site, indice)
                   data_json_annouct.append(dados__annouct)  
          
     
               #tree_html_announcement, tree_html_location = colection._request_http()
               tree_html_user = colection._request_http_offline(url_user)

               dados_user = colection.extraction_content_user(tree_html_user, site)  
                            
               data_json_user.append(dados_user)  
     
     except Exception as e :
          print("Erro aqui é isto aqui", e)   
     print(len(data_json_annouct))
     #response =requests.get("http://localhost:5001/listings")
     
     #create(data_json)
     #requests.post("http://localhost:5001/listings", json=data_json_annouct)
     return jsonify({"status": "coleta com sucesso"})  # resposta HTTP
     
 
@app.route("/anuncio-ia")
def data_collect_anuncio_ia():
     colection = CollectIA()
     colecao = Collect()
     config_link = colecao.config_file()
     sites = config_link['sites']  
     data_json_annouct = []   
     
     try :
         
         for site in sites:                      
         
             anuncios = colection.extraction_AI_content_annouct(site)  
         
             for anuncio in anuncios:
                 dados_formatados = colection.format_data(anuncio)
                 data_json_annouct.append(dados_formatados)   
         
             time.sleep(120)
                 
     except Exception as e :
          print("Erro aqui é isto aqui", e)   

     print (data_json_annouct)
     
     #create(data_json)
     requests.post("http://localhost:5001/received-data", json=data_json_annouct)

     return jsonify({"status": "coleta iniciada com sucesso"})  # resposta HTTP
    