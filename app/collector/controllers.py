from datetime import datetime
import requests
 
import yaml 
from flask import request, jsonify

from .. import  dbt 
from  ..collector.models.models import Listing, Advertiser, Location
from  ..collector.models.collector import  DataCollector
from  .services import Collect
from schema import Anuncio,Utilizador,Avaliacao


def collect():
    colection = Collect()
    config_link = colection.config_file()
    sites = config_link['sites'] 
    data_json = []  
    agora = datetime.now()

    try :  
        for site in sites: 
            url_location = site['localizacao']['link_offline']
            url_announcement = site['anuncio']['link_offline'] 
        
            #tree_html_announcement, tree_html_location = colection._request_http()
            tree_html_location = colection._request_http_offline(url_location)
            tree_html_announcement = colection._request_http_offline(url_announcement)

            data_gross_location = colection.extraction_content_location(tree_html_location, site)
            data_gross_annouct = colection.extraction_content_annouct(tree_html_announcement, site)
            
            print(data_gross_location)
            print("--------------------------------------------------------------")
            
            data_json.append(data_gross_location)
            data_json.append(data_gross_annouct)
    
    except Exception as e :
        print(e)   
    return data_json
    
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




