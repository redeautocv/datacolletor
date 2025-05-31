from datetime import datetime
import requests

import yaml 
from flask import request, jsonify

from .. import  dbt 
from  .models import Listing, Advertiser, Location
from  .services import Collect

def collect():
    colection = Collect()
    tree_html_anuncio, tree_html_morada = colection._request_http()
    data_gross_anuncios_numero, data_gross_loclizacao_empresa = colection.extraction_content(tree_html_anuncio, tree_html_morada)
    
    numero_anuncios = len(data_gross_anuncios_numero)
    data_gross_anuncios, data_gross_loclizacao_empresa = colection.extraction_content(tree_html_anuncio, tree_html_morada)
    numero_anuncios =  len(data_gross_anuncios)
    numero_localizacao_empresa =  len(data_gross_loclizacao_empresa)

    try:
        
        #date_manufacture= request_data['manufacture_year']
        #date_available= request_data['available']
        
        response= Advertiser.query.get(id)

        for contador in range (numero_anuncios):
            model = data_gross_anuncios[numero_anuncios]
            
            listing = Listing( 
                model = model['listings']['model'],
                #extra_fees=request_data['extra_fees'],
                available = 'sim',
                price = model['listings']['price'],
                fuel_type = model['listings']['fuel_type'],
                passenger_number = model['listings']['passenger_number'],
                door_number = model['listings']['door_number'],
                t_advertiser_id_advertiser = 1
            ) 
        dbt.session.add(listing)
        dbt.session.commit()

      
    except Exception as e:
        return e

    







