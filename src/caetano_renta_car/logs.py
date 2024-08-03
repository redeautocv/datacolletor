import requests
from flask import  request ,jsonify 
from  .ad_controlers import ads ,listings , dati ,locations
from  ..main import app
import json

@app.route("/data-send",methods=['GET'])
def send_announcement():    
        listings_json = json.dumps(dati)
        headers = {
            'Content-Type': 'application/json'
        }
        response = requests.post('http://127.0.0.1:4001/received-data', headers=headers, data=listings_json)
        return jsonify({'data':listings_json})
 