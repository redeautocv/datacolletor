import time  
import json
from datetime import datetime

import yaml 
import requests
from flask import request, jsonify

from  .services import Collect
from  .service_ai import extraction_AI_content_user
from  .service_ai import extraction_AI_content_annouct
from schema import Anuncio
from schema import Utilizador
from schema import Avaliacao
from .. import  dbt 
from  ..collector.models.collector import  DataCollector

def collect():
    colection = Collect()
    config_link = colection.config_file()
    sites = config_link['sites'] 
    data_json_annouct = []   
    data_json_user = []  
    try :  
        for site in sites: 
            
            url_user = site['utilizador']['link_offline']
            url_announcement = site['anuncio']['link_offline'] 
        
            #tree_html_announcement, tree_html_location = colection._request_http()
            tree_html_user = colection._request_http_offline(url_user)
            tree_html_announcement = colection._request_http_offline(url_announcement)

            numero_sites = colection.extraction_number_annouct(tree_html_announcement, site)

            for indice in range(numero_sites): 
                dados__annouct = colection.extraction_content_annouct(tree_html_announcement, site, indice)
                data_json_annouct.append(dados__annouct)
            dados_user = colection.extraction_content_user(tree_html_user, site)  
            #dados__user = extraction_AI_content_user(site)
            #time.sleep(120)

            #dados__annouct = extraction_AI_content_annouct(site)
            #time.sleep(120)

            #dados_user = json.loads(dados_user)
            #dados__annouct = json.loads(dados__annouct)
    
            #data_json_annouct.append(dados__annouct)
            data_json_user.append(dados_user) 
            
            #data_json.append(dados_dict_annouct)
            #data_json.append(dados_dict_user)
    
    except Exception as e :
     print("Erro aqui é isto aqui", e)   
   
    print(data_json_user )

    #return data_json_annouct
 
def create(data_groos):
    agora = datetime.now()
    time_Now = agora.strftime("%d/%m/%Y %H:%M:%S")

    novo_registro = DataCollector (
        data_coleta = time_Now,
        nome_empresa = "",
        dados_anuncios = data_groos, 
        dados_localizacao = data_groos,
    )            
     
    dbt.session.add(novo_registro)
    dbt.session.commit()




