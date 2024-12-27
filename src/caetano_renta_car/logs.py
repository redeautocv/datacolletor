import requests
from .controllers import create_tables
from flask import  request ,jsonify 
from  .ad_controlers import ads ,listings , dati ,locations
from  ..main import app
import json



@app.route("/Annou",methods=['GET'])
def received_announcement():    
    create_tables ()
    return "returnoo"

@app.route("/data-send",methods=['GET'])
def send_announcement():    
        server_url='http://127.0.0.1:5000/received-data'
        response = requests.post(server_url,json=dati)
        return jsonify({'data':dati})
 