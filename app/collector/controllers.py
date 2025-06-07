from datetime import datetime
import requests

import yaml 
from flask import request, jsonify

from .. import  dbt 
from  ..collector.models.models import Listing, Advertiser, Location
from  .services import Collect

def collect():
    colection = Collect()
    #tree_html_announcement, tree_html_location = colection._request_http()
    tree_html_announcement, tree_html_location = colection._request_http_offline()
    

    data_gross = colection.extraction_content(tree_html_announcement, tree_html_location )
    print(len(data_gross))
    print(data_gross)
    """    
    number_annoumcement =  len(data_gross_announcement)
    number_locations_companies =  len(data_gross_location_companies)
    
    print (data_gross_announcement)
    """
    """
    try:
        
        #date_manufacture= request_data['manufacture_year']
        #date_available= request_data['available']
        
        response= Advertiser.query.get(id)

        for contador in range (number_annoumcement):
            model = data_gross_announcement[contador]
            
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
            print( model['listings']['model'])
        dbt.session.add(listing)
        dbt.session.commit()
     
      
    except Exception as e:
        return e
    """
    







